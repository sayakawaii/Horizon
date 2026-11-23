---
layout: default
title: "Horizon Summary: 2026-11-23 (EN)"
date: 2026-11-23
lang: en
---

> From 99 items, 5 important content pieces were selected

---

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (4)

<a id="item-1"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">OpenAI Explores How Perplexity Correlates with Model Intelligence</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

OpenAI Chief Scientist Jakub Pachocki published an article arguing that perplexity, a measure of prediction uncertainty, correlates with model intelligence and that as models approach human-level intelligence, progress on perplexity will slow but smaller gains will correspond to larger leaps in intelligence. The article sparked a Hacker News discussion with 458 points and 311 comments debating the implications and historical context of this relationship. This matters because perplexity is a simple, well-understood metric from information theory that could serve as a benchmark for model intelligence, potentially replacing increasingly convoluted benchmarks. It also suggests that despite the rise of reinforcement learning, cross-entropy loss remains a fundamental driver of model capabilities, affecting how researchers evaluate and train large language models. Perplexity is defined as the degree of surprise in predicting the next token over a sequence; at worst it equals the vocabulary size, and at best it is 1. The article notes that smaller gains in perplexity will correspond to larger leaps in intelligence as models approach human-level performance, implying a diminishing returns relationship.

🔗 [Source](https://openai.com/index/perplexity-and-intelligence/)

hackernews · OpenAI Blog · Nov 22, 17:06 · [Discussion](https://news.ycombinator.com/item?id=50601525)

**Background**: Perplexity is a metric from information theory that measures how well a probability model predicts a sample; in language modeling, it quantifies the uncertainty of predicting the next token in a sequence. Lower perplexity indicates better prediction, and it has been a standard intrinsic metric for evaluating language models, closely tied to cross-entropy loss and scaling laws. Historically, perplexity has been used to compare models and guide training, but recent focus has shifted to reinforcement learning and emergent abilities.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/perplexity-and-intelligence/">Perplexity and Intelligence | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Perplexity">Perplexity - Wikipedia</a></li>
<li><a href="https://zeroentropy.dev/concepts/perplexity/">Perplexity : the standard intrinsic metric for LLM quality</a></li>

</ul>
</details>

**Discussion**: Commenters clarified the definition of perplexity and expressed surprise that cross-entropy loss remains so relevant despite the trend toward reinforcement learning. Some linked the idea to historical arguments about prediction as compression, while others were skeptical about claims that specific abilities emerge at given perplexities, noting that specialized models may have higher general perplexity.

**Tags**: `#AI`, `#machine learning`, `#perplexity`, `#language models`, `#OpenAI`

</details>


<a id="item-2"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Tim O'Reilly critiques Silicon Valley's shareholder-value focus, urges mechanism design for human flourishing</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

In a new essay, Tim O'Reilly argues that Silicon Valley has optimized for shareholder value rather than human flourishing, and calls for rethinking the 'game' using mechanism design—asking 'What game ought we be playing?' instead of just playing the current rules. The essay challenges the tech industry's underlying incentives and has sparked a broader debate on how to align capitalism with societal good, especially as AI-driven cannibalization and post-ZIRP economics reshape the landscape. O'Reilly draws on mechanism design as 'reverse game theory'—starting from a desired outcome (human flourishing) and working backwards to design rules that produce it—and notes that the most important idea is buried near the end of the long essay.

🔗 [Source](https://www.oreilly.com/radar/what-happened-to-silicon-valley/)

hackernews · greenyouse · Nov 22, 19:20 · [Discussion](https://news.ycombinator.com/item?id=50602947)

**Background**: Mechanism design is a branch of economics and game theory that studies how to construct rules (mechanisms) that yield good outcomes even when players' preferences are unknown; it is sometimes called reverse game theory and has applications in auction design, voting, and internet routing. ZIRP (Zero Interest Rate Policy) refers to central banks setting near-zero interest rates to stimulate borrowing and investment, a condition that persisted for years after the 2008 financial crisis and fueled high-risk, high-growth tech ventures.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanism_design">Mechanism design</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero_interest-rate_policy">Zero interest - rate policy - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters largely agreed with O'Reilly's critique but added that the ZIRP era allowed companies to grow to grotesque proportions and incentivized upstarts to chase green fields rather than compete in known markets; some also noted that with rates back up, tech companies are cannibalizing core competencies via AI, and questioned whether markets will discipline reckless spending. Others criticized the rise of 'VC influencers' and a perceived decline in Silicon Valley's integrity.

**Tags**: `#silicon-valley`, `#tech-industry`, `#mechanism-design`, `#capitalism`, `#ai`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">mod_wsgi Creator Graham Dumpleton Launches Muru, an AI-Assisted Rust ASGI/WSGI Server</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Graham Dumpleton, who started mod_wsgi 20 years ago, has begun publishing detailed development write-ups for Muru, a new AI-assisted Rust server designed to run both ASGI and WSGI Python applications in development and production. Since November 4, 2026, he has published roughly 19 posts covering worker internals, import-once-fork-many, HTTPS in development, WSGI/ASGI coexistence, releases without restarts, canary deployments without a service mesh, Kubernetes integration, scaling to zero, and a per-page toolbar with tracing. Muru brings two decades of hard-won Python web serving experience into a modern Rust implementation, potentially offering an alternative to established servers like Gunicorn, uWSGI, Uvicorn, Hypercorn, and Granian. Its explicit focus on both WSGI and ASGI, plus built-in development and deployment features, could simplify how Python teams serve applications across environments. The project is still early-stage, and the linked item is a brief pointer rather than a deep technical dive; the substantive material lives in Dumpleton's own posts. Notably, the code is being written with substantial AI assistance, though Dumpleton stresses that judging what is not yet good enough remains his responsibility, informed by his mod_wsgi experience.

🔗 [Source](https://simonwillison.net/2026/Nov/21/muru/)

rss · Simon Willison · Nov 21, 23:56

**Background**: WSGI is the long-standing Python standard interface for synchronous web applications, while ASGI is its asynchronous successor that supports async code, WebSockets, and long-lived connections. mod_wsgi is an Apache HTTP Server module by Graham Dumpleton that hosts WSGI Python applications under Apache, and it has been widely used for roughly two decades. Rust has become a popular language for writing high-performance web servers and proxies, which is why a Rust-based Python application server is notable.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mod_wsgi">mod_wsgi - Wikipedia</a></li>
<li><a href="https://grahamdumpleton.me/posts/2026/11/twenty-years-of-mod-wsgi/">Twenty years of mod_wsgi, and what comes next - Graham Dumpleton</a></li>
<li><a href="https://www.deployhq.com/blog/python-application-servers-wsgi-vs-asgi-guide">Python Application Servers in 2026: WSGI vs ASGI , Gunicorn to...</a></li>

</ul>
</details>

**Tags**: `#python`, `#asgi`, `#wsgi`, `#rust`, `#web-servers`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">FBI investigates apparent hack of National Crime Information Center database</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

The FBI is investigating an apparent hack of its National Crime Information Center (NCIC) database, according to BBC and other reports. President Donald Trump confirmed on Saturday that the database was targeted, though details of the breach remain limited. The NCIC is a critical tool for law enforcement nationwide, containing sensitive data on fugitives, missing persons, criminal histories, and stolen property. A breach could expose sensitive information and undermine trust in the systems that police rely on for daily operations and national security. The NCIC, established in 1967, is a centralized database used by federal, state, and local law enforcement to share crime-related information. The investigation is ongoing, and it is not yet clear what data, if any, was accessed or how the breach occurred.

🔗 [Source](https://www.bbc.co.uk/news/articles/cvze7de86pk3o?at_medium=RSS&at_campaign=rss)

rss · BBC World · Nov 22, 00:10

**Background**: The National Crime Information Center (NCIC) is the United States' central database for tracking crime-related information, created in 1967 to help law enforcement agencies share data across jurisdictions. It contains records on fugitives, missing persons, criminal histories, stolen property, and more, and is accessible to federal, state, and local agencies. The FBI operates and maintains the system, which is considered a lifeline for police work.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/National_Crime_Information_Center">National Crime Information Center - Wikipedia</a></li>
<li><a href="https://apnews.com/article/fbi-database-ncic-hack-d066cff87a64a564db0a00172c124972">FBI probing hack of its national criminal justice database ...</a></li>
<li><a href="https://abcnews.com/US/fbis-national-crime-database-targeted-hack-trump/story?id=138347810">FBI's national crime database targeted in hack, Trump says</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#data breach`, `#FBI`, `#law enforcement`, `#national security`

</details>


</section>

<section class="cat cat-other" markdown="1">

## 📌 Other (1)

<a id="item-5"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Toyota, Nissan, Honda to standardize parts to cut costs</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Japan's seven major automakers, including Toyota, Nissan, and Honda, have begun discussions to standardize automotive parts in an effort to reduce costs and better compete with Chinese manufacturers like BYD. The initial talks will involve domestic Japanese parts suppliers, with international suppliers expected to join later. This move could significantly lower production costs for Japanese automakers, helping them counter the price advantage of Chinese rivals like BYD, which produces 75-85% of its parts in-house. If successful, it may reshape supply chain dynamics and set a precedent for cross-company collaboration in the industry. The standardization effort involves all seven of Japan's major automakers: Toyota, Nissan, Honda, Mazda, Subaru, Mitsubishi, and Suzuki. The plan is still in early stages, with discussions set to include domestic suppliers first, and no specific parts or timelines have been announced yet.

🔗 [Source](https://www.caranddriver.com/news/a74490092/toyota-nissan-honda-standardize-parts-lower-costs/)

hackernews · zdw · Nov 22, 04:04 · [Discussion](https://news.ycombinator.com/item?id=50596133)

**Background**: BYD, founded in 1995 as a battery maker, has become the world's largest manufacturer of plug-in electric vehicles through aggressive vertical integration, producing most components in-house. Japanese automakers, traditionally reliant on a network of external suppliers, face mounting pressure to reduce costs as Chinese EVs gain global market share. Standardizing parts across companies is a strategy to achieve economies of scale similar to those of vertically integrated rivals.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/BYD_Auto">BYD Auto - Wikipedia</a></li>
<li><a href="https://www.caranddriver.com/news/a74490092/toyota-nissan-honda-standardize-parts-lower-costs/">Toyota, Nissan, and Honda to Standardize Parts to Lower Costs</a></li>

</ul>
</details>

**Discussion**: Commenters noted historical precedents like the GM-Ford 6-speed transmission collaboration, but emphasized that Japanese automakers are being forced to act because BYD's vertical integration gives it a major cost advantage. Some also speculated that the move could serve as a shadow bailout for financially troubled Nissan, while others questioned the broader economic impact on jobs.

**Tags**: `#automotive`, `#manufacturing`, `#standardization`, `#competition`, `#industry`

</details>


</section>