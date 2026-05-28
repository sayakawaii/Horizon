"""Daily summary generation — pure programmatic rendering."""

import re
from typing import List, Dict

from ..models import ContentItem


_CJK = r"[\u4e00-\u9fff\u3400-\u4dbf]"
_ASCII = r"[A-Za-z0-9]"


def _pangu(text: str) -> str:
    """Insert a space between CJK and ASCII letters/digits (Pangu spacing)."""
    text = re.sub(rf"({_CJK})({_ASCII})", r"\1 \2", text)
    text = re.sub(rf"({_ASCII})({_CJK})", r"\1 \2", text)
    return text


LABELS = {
    "en": {
        "header": "Horizon Daily",
        "source": "Source",
        "background": "Background",
        "discussion": "Discussion",
        "references": "References",
        "tags": "Tags",
        "selected_items": "From {total} items, {selected} important content pieces were selected",
        "empty_analyzed": "Analyzed {total} items, but none met the importance threshold.",
        "categories": {
            "tech": "🔬 Tech & AI",
            "geopolitics": "🌐 Geopolitics",
            "disaster": "🌍 Breaking & Disasters",
            "finance": "💹 Finance & Markets",
            "science": "🧪 Science",
            "other": "📌 Other",
        },
        "empty_body": (
            "No significant developments today. This might indicate:\n"
            "- A quiet day in your tracked sources\n"
            "- The AI score threshold is too high\n"
            "- Your information sources need expansion\n\n"
            "Consider:\n"
            "1. Lowering the `ai_score_threshold` in config.json\n"
            "2. Adding more diverse information sources\n"
            "3. Checking if the AI model is working correctly\n"
        ),
    },
    "zh": {
        "header": "Horizon 每日速递",
        "source": "来源",
        "background": "背景",
        "discussion": "社区讨论",
        "references": "参考链接",
        "tags": "标签",
        "selected_items": "从 {total} 条内容中筛选出 {selected} 条重要资讯。",
        "empty_analyzed": "已分析 {total} 条内容，但没有达到重要性阈值的条目。",
        "categories": {
            "tech": "🔬 科技 / AI",
            "geopolitics": "🌐 国际局势",
            "disaster": "🌍 突发事件",
            "finance": "💹 财经 / 市场",
            "science": "🧪 科学",
            "other": "📌 其他",
        },
        "empty_body": (
            "今日暂无重要动态，可能原因：\n"
            "- 今天关注的信息源较平静\n"
            "- AI 评分阈值设置过高\n"
            "- 信息源种类有待扩充\n\n"
            "建议：\n"
            "1. 在 config.json 中降低 `ai_score_threshold`\n"
            "2. 添加更多多样化的信息源\n"
            "3. 检查 AI 模型是否正常工作\n"
        ),
    },
}


# Category buckets. Order matters: first match wins (disaster > geopolitics > tech).
CATEGORY_ORDER = ["disaster", "geopolitics", "finance", "science", "tech", "other"]

_CATEGORY_KEYWORDS = {
    "disaster": [
        "earthquake", "quake", "tsunami", "flood", "hurricane", "typhoon", "cyclone",
        "wildfire", "volcano", "eruption", "landslide", "outbreak", "pandemic",
        "epidemic", "disaster", "famine", "drought", "storm",
        "地震", "海啸", "洪水", "台风", "飓风", "山火", "野火", "火山", "喷发",
        "山体", "塌方", "疫情", "瘟疫", "灾害", "暴雨", "旱灾", "饥荒",
    ],
    "geopolitics": [
        "war", "conflict", "election", "sanction", "treaty", "diplomacy", "summit",
        "military", "nato", "united nations", "putin", "trump", "biden", "gaza",
        "ukraine", "russia", "iran", "israel", "palestine", "taiwan", "korea",
        "geopolitic", "tariff", "trade war",
        "战争", "冲突", "选举", "制裁", "外交", "地缘", "联合国", "北约",
        "中美", "俄乌", "以色列", "巴勒斯坦", "伊朗", "朝鲜", "台海", "关税",
        "军事", "政治",
    ],
    "tech": [
        "ai", "ml", "llm", "gpt", "model", "release", "open source", "framework",
        "library", "compiler", "kernel", "rust", "python", "javascript", "typescript",
        "kubernetes", "docker", "cloud", "gpu", "cuda", "transformer", "research",
        "paper", "benchmark", "vector", "database", "api", "sdk", "developer",
        "programming", "software", "github", "huggingface", "anthropic", "openai",
        "google", "meta", "deepseek", "nvidia", "apple", "microsoft",
        "科技", "技术", "模型", "开源", "框架", "算法", "芯片", "云计算",
        "人工智能", "机器学习", "大模型", "深度学习", "编程", "开发者",
    ],
}


def _categorize(item: "ContentItem") -> str:
    """Bucket an item into one of CATEGORY_ORDER.

    Preference: AI-supplied `metadata['category']` > keyword heuristic.
    """
    meta = item.metadata or {}
    ai_cat = meta.get("category")
    if isinstance(ai_cat, str) and ai_cat.strip().lower() in CATEGORY_ORDER:
        return ai_cat.strip().lower()

    haystack_parts: List[str] = []
    if item.ai_tags:
        haystack_parts.extend(item.ai_tags)
    if item.title:
        haystack_parts.append(item.title)
    for key in ("title_en", "title_zh", "feed_category", "category"):
        v = meta.get(key)
        if v:
            haystack_parts.append(str(v))
    haystack = " ".join(haystack_parts).lower()

    # Source-type heuristic: github/hackernews almost always tech
    src = getattr(item.source_type, "value", "") if item.source_type else ""
    if src in {"github", "hackernews"}:
        # still let an explicit disaster/geopolitics keyword override
        for cat in ("disaster", "geopolitics"):
            if any(kw in haystack for kw in _CATEGORY_KEYWORDS[cat]):
                return cat
        return "tech"

    for cat in CATEGORY_ORDER:
        if cat == "other":
            continue
        if any(kw in haystack for kw in _CATEGORY_KEYWORDS[cat]):
            return cat
    return "other"


class DailySummarizer:
    """Generates daily Markdown summaries from pre-analyzed content items."""

    def __init__(self):
        pass

    async def generate_summary(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate daily summary in Markdown format.

        Items are rendered in score-descending order (already sorted by orchestrator).

        Args:
            items: High-scoring content items (already enriched)
            date: Date string (YYYY-MM-DD)
            total_fetched: Total number of items fetched before filtering
            language: Output language, either "en" or "zh"

        Returns:
            str: Markdown formatted summary
        """
        labels = LABELS.get(language, LABELS["en"])

        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        header = (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['selected_items'].format(total=total_fetched, selected=len(items))}\n\n"
            "---\n\n"
        )

        # Group items into category buckets, preserving score order inside each bucket
        buckets: Dict[str, List[ContentItem]] = {cat: [] for cat in CATEGORY_ORDER}
        for item in items:
            buckets[_categorize(item)].append(item)

        # Render each non-empty category as a <section> with category-specific class.
        sections_md: List[str] = []
        running_index = 0
        for cat in CATEGORY_ORDER:
            bucket = buckets[cat]
            if not bucket:
                continue
            cat_label = labels["categories"][cat]
            section_lines: List[str] = [
                f'<section class="cat cat-{cat}" markdown="1">',
                "",
                f"## {cat_label} ({len(bucket)})",
                "",
            ]
            for item in bucket:
                running_index += 1
                section_lines.append(self._format_item(item, labels, language, running_index))
            section_lines.append("</section>")
            section_lines.append("")
            sections_md.append("\n".join(section_lines))

        return header + "\n".join(sections_md)

    def generate_webhook_overview(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate a compact overview for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        if language == "zh":
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> 从 {total_fetched} 条内容中筛选出 {len(items)} 条重要资讯。\n\n"
                "下面会按新闻逐条发送详情，你可以只看感兴趣的标题。\n\n"
            )
        else:
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> Selected {len(items)} important items from {total_fetched} fetched items.\n\n"
                "Details will be sent item by item so you can read only the topics you care about.\n\n"
            )

        entries = []
        for i, item in enumerate(items, start=1):
            title = str(item.metadata.get(f"title_{language}") or item.title).replace("[", "(").replace("]", ")")
            if language == "zh":
                title = _pangu(title)
            score = item.ai_score or "?"
            entries.append(f"{i}. [{title}]({item.url}) \u2b50\ufe0f {score}/10")

        return header + "\n".join(entries)

    def generate_webhook_item(
        self,
        item: ContentItem,
        language: str,
        index: int,
        total: int,
    ) -> str:
        """Generate one item message for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        prefix = f"第 {index}/{total} 条\n\n" if language == "zh" else f"Item {index}/{total}\n\n"
        return prefix + self._format_item(item, labels, language, index).rstrip("-\n ")

    def _format_item(self, item: ContentItem, labels: dict, language: str, index: int) -> str:
        """Format a single ContentItem into Markdown."""
        _title = item.metadata.get(f"title_{language}") or item.title
        title = str(_title).replace("[", "(").replace("]", ")")
        url = str(item.url)
        score = item.ai_score or "?"
        meta = item.metadata

        summary = (
            meta.get(f"detailed_summary_{language}")
            or meta.get("detailed_summary")
            or item.ai_summary
            or ""
        )
        background = meta.get(f"background_{language}") or meta.get("background") or ""
        discussion = (
            meta.get(f"community_discussion_{language}")
            or meta.get("community_discussion")
            or ""
        )

        if language == "zh":
            title = _pangu(title)
            summary = _pangu(summary)
            background = _pangu(background)
            discussion = _pangu(discussion)

        # Source line with parts joined by " · ", link appended at end
        source_type = item.source_type.value
        source_parts = [source_type]
        if meta.get("subreddit"):
            source_parts.append(f"r/{meta['subreddit']}")
        if meta.get("feed_name"):
            source_parts.append(meta["feed_name"])
        else:
            source_parts.append(item.author or "unknown")
        if item.published_at:
            if language == "zh":
                source_parts.append(
                    f"{item.published_at.month}月{item.published_at.day}日 "
                    f"{item.published_at:%H:%M}"
                )
            else:
                day = item.published_at.strftime("%d").lstrip("0")
                source_parts.append(item.published_at.strftime(f"%b {day}, %H:%M"))
        source_line = " \u00b7 ".join(source_parts)  # ·

        discussion_url = meta.get("discussion_url")
        if discussion_url:
            discussion_url = str(discussion_url)
            if discussion_url != url:
                source_line += f' · [{labels["discussion"]}]({discussion_url})'

        # Each item is a collapsible card. Use kramdown's markdown="1" so the
        # inner Markdown is still processed.
        score_str = str(score)
        lines = [
            f'<a id="item-{index}"></a>',
            f'<details class="hz-item" data-score="{score_str}" markdown="1">',
            f'<summary><span class="hz-item-title">{title}</span>'
            f' <span class="hz-item-score">⭐️ {score_str}/10</span></summary>',
            "",
            summary,
            "",
            f'🔗 [{labels["source"]}]({url})',
            "",
            source_line,
        ]

        if background:
            lines.append("")
            lines.append(f"**{labels['background']}**: {background}")

        sources = meta.get("sources") or []
        if sources:
            items_html = "".join(f'<li><a href="{s["url"]}">{s["title"]}</a></li>\n' for s in sources)
            lines += [
                "",
                f'<details><summary>{labels["references"]}</summary>\n<ul>\n{items_html}\n</ul>\n</details>',
            ]

        if discussion:
            lines.append("")
            lines.append(f"**{labels['discussion']}**: {discussion}")

        if item.ai_tags:
            tags_str = ", ".join([f"`#{t}`" for t in item.ai_tags])
            lines.append("")
            lines.append(f"**{labels['tags']}**: {tags_str}")

        lines.append("")
        lines.append("</details>")
        lines.append("")

        return "\n".join(lines) + "\n"

    def _generate_empty_summary(self, date: str, total_fetched: int, labels: dict) -> str:
        """Generate summary when no high-scoring items were found."""
        return (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['empty_analyzed'].format(total=total_fetched)}\n\n"
            + labels["empty_body"]
        )
