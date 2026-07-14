from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock

from src.models import PapersConfig
from src.scrapers.papers import PapersScraper


ARXIV_ATOM = """<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns:arxiv="http://arxiv.org/schemas/atom" xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2607.01234v1</id>
    <title>A New Transformer for Efficient LLM Reasoning</title>
    <updated>2026-07-13T05:08:41Z</updated>
    <published>2026-07-13T05:08:41Z</published>
    <summary>We propose a novel attention mechanism that improves reasoning.</summary>
    <link href="https://arxiv.org/abs/2607.01234v1" rel="alternate" type="text/html"/>
    <link href="https://arxiv.org/pdf/2607.01234v1" rel="related" type="application/pdf" title="pdf"/>
    <category term="cs.CL" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.AI" scheme="http://arxiv.org/schemas/atom"/>
    <arxiv:primary_category term="cs.CL"/>
    <author><name>Alice Zhang</name></author>
    <author><name>Bob Li</name></author>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2601.99999v2</id>
    <title>An Old Survey on Databases</title>
    <updated>2026-01-01T05:08:41Z</updated>
    <published>2026-01-01T05:08:41Z</published>
    <summary>A survey unrelated to the keyword.</summary>
    <link href="https://arxiv.org/abs/2601.99999v2" rel="alternate" type="text/html"/>
    <link href="https://arxiv.org/pdf/2601.99999v2" rel="related" type="application/pdf" title="pdf"/>
    <category term="cs.DB" scheme="http://arxiv.org/schemas/atom"/>
    <arxiv:primary_category term="cs.DB"/>
    <author><name>Carol Wu</name></author>
  </entry>
</feed>
"""


def _arxiv_response() -> MagicMock:
    response = MagicMock()
    response.text = ARXIV_ATOM
    response.raise_for_status.return_value = None
    return response


def test_arxiv_parsing_and_time_window() -> None:
    client = AsyncMock()
    client.get.return_value = _arxiv_response()
    cfg = PapersConfig(enabled=True, huggingface_trending=False)
    scraper = PapersScraper(cfg, client)
    since = datetime(2026, 7, 1, tzinfo=timezone.utc)

    items = asyncio.run(scraper.fetch(since))

    # The January paper is filtered out by the time window.
    assert len(items) == 1
    item = items[0]
    assert item.title == "A New Transformer for Efficient LLM Reasoning"
    assert item.metadata["category"] == "papers"
    assert item.metadata["is_paper"] is True
    assert item.metadata["arxiv_id"] == "2607.01234v1"
    assert item.id == "papers:arxiv:2607.01234"
    assert item.metadata["primary_category"] == "cs.CL"
    assert "cs.AI" in item.metadata["arxiv_categories"]
    assert item.metadata["pdf_url"] == "https://arxiv.org/pdf/2607.01234v1"
    assert item.author == "Alice Zhang, Bob Li"


def test_keyword_filter() -> None:
    client = AsyncMock()
    client.get.return_value = _arxiv_response()
    cfg = PapersConfig(
        enabled=True, huggingface_trending=False, keywords=["nonexistent-topic"]
    )
    scraper = PapersScraper(cfg, client)
    since = datetime(2026, 7, 1, tzinfo=timezone.utc)

    items = asyncio.run(scraper.fetch(since))
    assert items == []


def test_hf_trending_annotates_upvotes() -> None:
    hf_response = MagicMock()
    hf_response.raise_for_status.return_value = None
    hf_response.json.return_value = [
        {
            "paper": {"id": "2607.01234", "title": "x", "upvotes": 128},
            "publishedAt": "2026-07-13T05:08:41Z",
            "numComments": 4,
        }
    ]

    client = AsyncMock()
    client.get.side_effect = [_arxiv_response(), hf_response]
    cfg = PapersConfig(enabled=True, huggingface_trending=True, include_hf_only=False)
    scraper = PapersScraper(cfg, client)
    since = datetime(2026, 7, 1, tzinfo=timezone.utc)

    items = asyncio.run(scraper.fetch(since))
    assert len(items) == 1
    assert items[0].metadata["hf_upvotes"] == 128
    assert items[0].metadata["hf_comments"] == 4


def test_disabled_returns_empty() -> None:
    client = AsyncMock()
    scraper = PapersScraper(PapersConfig(enabled=False), client)
    since = datetime(2026, 7, 1, tzinfo=timezone.utc)
    assert asyncio.run(scraper.fetch(since)) == []
    client.get.assert_not_called()
