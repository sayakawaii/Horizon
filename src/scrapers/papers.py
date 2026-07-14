"""Academic paper scraper (arXiv API + optional Hugging Face trending).

Fetches the latest AI-related papers from the arXiv API, filtered by
category and time window, then optionally annotates them with Hugging Face
"Daily Papers" community trending signals (upvotes). Every emitted item is
tagged with ``metadata['category'] = 'papers'`` so the summarizer renders it
in a dedicated "Papers" section.
"""

import logging
import re
from datetime import datetime, timezone
from typing import Dict, List, Optional

import httpx
import feedparser

from .base import BaseScraper
from ..models import ContentItem, SourceType, PapersConfig

logger = logging.getLogger(__name__)

ARXIV_API_URL = "https://export.arxiv.org/api/query"
HF_DAILY_PAPERS_URL = "https://huggingface.co/api/daily_papers"


class PapersScraper(BaseScraper):
    """Scraper for the latest AI papers from arXiv (+ HF trending signal)."""

    def __init__(self, config: PapersConfig, http_client: httpx.AsyncClient):
        super().__init__(config.model_dump(), http_client)
        self._cfg = config

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self._cfg.enabled:
            return []

        items: List[ContentItem] = []
        try:
            items = await self._fetch_arxiv(since)
        except httpx.HTTPError as e:
            logger.warning("Error fetching arXiv papers: %s", e)
        except Exception as e:  # feedparser / parsing safety net
            logger.warning("Error parsing arXiv papers: %s", e)

        # Best-effort Hugging Face trending enrichment / augmentation.
        if self._cfg.huggingface_trending:
            try:
                trending = await self._fetch_hf_trending(since)
                items = self._merge_trending(items, trending, since)
            except Exception as e:
                logger.warning("Skipping Hugging Face trending papers: %s", e)

        return items

    # ------------------------------------------------------------------ arXiv

    async def _fetch_arxiv(self, since: datetime) -> List[ContentItem]:
        categories = self._cfg.categories or ["cs.AI"]
        search_query = " OR ".join(f"cat:{c}" for c in categories)
        params = {
            "search_query": search_query,
            "start": 0,
            "max_results": self._cfg.max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }

        response = await self.client.get(
            ARXIV_API_URL, params=params, follow_redirects=True
        )
        response.raise_for_status()

        feed = feedparser.parse(response.text)
        keywords = [k.lower() for k in (self._cfg.keywords or [])]

        items: List[ContentItem] = []
        for entry in feed.entries:
            published_at = self._parse_date(entry)
            if not published_at or published_at < since:
                continue

            title = " ".join((entry.get("title") or "").split())
            abstract = " ".join((entry.get("summary") or "").split())

            if keywords:
                haystack = f"{title} {abstract}".lower()
                if not any(kw in haystack for kw in keywords):
                    continue

            arxiv_id = self._extract_arxiv_id(entry.get("id", ""))
            if not arxiv_id:
                continue

            items.append(
                self._build_item(
                    arxiv_id=arxiv_id,
                    title=title or "Untitled",
                    abstract=abstract,
                    authors=[a.get("name", "") for a in entry.get("authors", [])],
                    published_at=published_at,
                    categories=[t.get("term") for t in entry.get("tags", []) if t.get("term")],
                    primary_category=self._primary_category(entry),
                    abs_url=self._abs_url(entry, arxiv_id),
                    pdf_url=self._pdf_url(entry, arxiv_id),
                    comment=entry.get("arxiv_comment"),
                )
            )

        return items

    # ---------------------------------------------------------------- HuggingFace

    async def _fetch_hf_trending(self, since: datetime) -> Dict[str, dict]:
        """Return a map of base arXiv id -> HF daily-paper record.

        Best-effort: any network/parse failure yields an empty map.
        """
        response = await self.client.get(
            HF_DAILY_PAPERS_URL,
            params={"limit": 100},
            follow_redirects=True,
        )
        response.raise_for_status()
        data = response.json()

        trending: Dict[str, dict] = {}
        for record in data or []:
            paper = record.get("paper") or {}
            raw_id = paper.get("id") or record.get("id") or ""
            base_id = self._base_id(raw_id)
            if not base_id:
                continue
            upvotes = int(paper.get("upvotes") or record.get("upvotes") or 0)
            if upvotes < self._cfg.hf_min_upvotes:
                continue
            trending[base_id] = {
                "upvotes": upvotes,
                "title": paper.get("title") or record.get("title") or "",
                "summary": paper.get("summary") or "",
                "authors": [a.get("name", "") for a in (paper.get("authors") or [])],
                "published_at": self._parse_iso(record.get("publishedAt")),
                "num_comments": record.get("numComments"),
            }
        return trending

    def _merge_trending(
        self,
        items: List[ContentItem],
        trending: Dict[str, dict],
        since: datetime,
    ) -> List[ContentItem]:
        if not trending:
            return items

        by_id = {}
        for item in items:
            base = self._base_id(item.metadata.get("arxiv_id", ""))
            if base:
                by_id[base] = item

        # Annotate existing arXiv items with upvote signal.
        for base, record in trending.items():
            item = by_id.get(base)
            if item is not None:
                item.metadata["hf_upvotes"] = record["upvotes"]
                if record.get("num_comments") is not None:
                    item.metadata["hf_comments"] = record["num_comments"]

        # Optionally ingest HF-only trending papers (outside category query).
        if self._cfg.include_hf_only:
            for base, record in trending.items():
                if base in by_id:
                    continue
                published_at = record.get("published_at")
                if not published_at or published_at < since:
                    continue
                title = " ".join((record.get("title") or "").split())
                if not title:
                    continue
                item = self._build_item(
                    arxiv_id=base,
                    title=title,
                    abstract=" ".join((record.get("summary") or "").split()),
                    authors=record.get("authors") or [],
                    published_at=published_at,
                    categories=[],
                    primary_category=None,
                    abs_url=f"https://arxiv.org/abs/{base}",
                    pdf_url=f"https://arxiv.org/pdf/{base}",
                    comment=None,
                )
                item.metadata["hf_upvotes"] = record["upvotes"]
                if record.get("num_comments") is not None:
                    item.metadata["hf_comments"] = record["num_comments"]
                items.append(item)

        return items

    # ------------------------------------------------------------------ helpers

    def _build_item(
        self,
        *,
        arxiv_id: str,
        title: str,
        abstract: str,
        authors: List[str],
        published_at: datetime,
        categories: List[str],
        primary_category: Optional[str],
        abs_url: str,
        pdf_url: str,
        comment: Optional[str],
    ) -> ContentItem:
        authors = [a for a in authors if a]
        if len(authors) > 3:
            author_display = ", ".join(authors[:3]) + " et al."
        else:
            author_display = ", ".join(authors) if authors else "unknown"

        return ContentItem(
            id=self._generate_id("papers", "arxiv", self._base_id(arxiv_id)),
            source_type=SourceType.PAPERS,
            title=title,
            url=abs_url,
            content=abstract,
            author=author_display,
            published_at=published_at,
            metadata={
                # Force this item into the summarizer's "papers" bucket.
                "category": "papers",
                "is_paper": True,
                "arxiv_id": arxiv_id,
                "authors": authors,
                "arxiv_categories": categories,
                "primary_category": primary_category,
                "pdf_url": pdf_url,
                "comment": comment,
            },
        )

    @staticmethod
    def _extract_arxiv_id(entry_id: str) -> str:
        """Extract the arXiv id (with version) from an entry id/URL."""
        if not entry_id:
            return ""
        return entry_id.rstrip("/").split("/abs/")[-1].split("/")[-1]

    @staticmethod
    def _base_id(arxiv_id: str) -> str:
        """Strip the trailing version (e.g. ``2401.01234v2`` -> ``2401.01234``)."""
        if not arxiv_id:
            return ""
        base = arxiv_id.rstrip("/").split("/")[-1]
        return re.sub(r"v\d+$", "", base)

    @staticmethod
    def _primary_category(entry: dict) -> Optional[str]:
        primary = entry.get("arxiv_primary_category")
        if isinstance(primary, dict):
            return primary.get("term")
        return None

    def _abs_url(self, entry: dict, arxiv_id: str) -> str:
        for link in entry.get("links", []):
            if link.get("rel") == "alternate" and link.get("href"):
                return link["href"]
        return f"https://arxiv.org/abs/{self._base_id(arxiv_id)}"

    def _pdf_url(self, entry: dict, arxiv_id: str) -> str:
        for link in entry.get("links", []):
            if link.get("title") == "pdf" and link.get("href"):
                return link["href"]
        return f"https://arxiv.org/pdf/{self._base_id(arxiv_id)}"

    @staticmethod
    def _parse_date(entry: dict) -> Optional[datetime]:
        import calendar

        for field in ("published", "updated"):
            parsed = entry.get(f"{field}_parsed")
            if parsed:
                return datetime.fromtimestamp(calendar.timegm(parsed), tz=timezone.utc)
        return None

    @staticmethod
    def _parse_iso(value: Optional[str]) -> Optional[datetime]:
        if not value:
            return None
        try:
            dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except (ValueError, AttributeError):
            return None
