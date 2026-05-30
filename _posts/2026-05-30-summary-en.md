---
layout: default
title: "Horizon Summary: 2026-05-30 (EN)"
date: 2026-05-30
lang: en
---

> From 109 items, 15 important content pieces were selected

---

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (15)

<a id="item-1"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">vLLM v0.22.0: DeepSeek V4 hardening, Rust frontend</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

vLLM v0.22.0 introduces major hardening for DeepSeek V4, including NVFP4 fused MoE support, full CUDA graph, and MTP speculative decoding, along with an experimental Rust frontend and Model Runner V2 improvements. This release significantly improves inference performance and model support for state-of-the-art LLMs like DeepSeek V4, benefiting the open-source AI community with faster and more efficient serving. The release includes 459 commits from 230 contributors, batch-invariant inference with Cutlass FP8 achieving 28.9% latency improvement, and a new multi-tier KV cache offloading framework extending beyond CPU memory.

🔗 [Source](https://github.com/vllm-project/vllm/releases/tag/v0.22.0)

github · khluu · May 29, 10:28

**Background**: vLLM is a high-throughput, memory-efficient LLM inference engine widely used in production. DeepSeek V4 is a large Mixture-of-Experts (MoE) model requiring specialized kernels for efficient inference. MTP (Multi-Token Prediction) is a speculative decoding technique that predicts multiple future tokens simultaneously to accelerate generation.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/v0.10.2/api/vllm/model_executor/layers/quantization/utils/nvfp4_moe_support.html">nvfp4_moe_support - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/speculative_decoding/mtp/">MTP (Multi-Token Prediction) - vLLM</a></li>
<li><a href="https://langcopilot.com/posts/2026-05-15-deepseek-v4-megamoe-overlapping-communication-comp">DeepSeek-V4 MegaMoE: Overlapping Communication and Compute</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#vLLM`, `#DeepSeek`, `#open source`, `#machine learning`

</details>


<a id="item-2"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">OpenRouter raises $113M Series B for LLM proxy service</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

OpenRouter, a proxy service for accessing large language models (LLMs), announced a $113 million Series B funding round. The company provides a unified API with billing caps and low-friction model support. This funding highlights the growing demand for infrastructure that simplifies multi-model LLM access, especially as the number of providers and models increases. OpenRouter's billing caps address a key pain point for developers deploying AI in production. OpenRouter remains founder-led and founder-controlled after the raise. The service offers a unified API to over 300 models, with features like automatic fallback and zero-completion insurance.

🔗 [Source](https://openrouter.ai/announcements/series-b)

hackernews · freeCandy · May 30, 17:27 · [Discussion](https://news.ycombinator.com/item?id=48338660)

**Background**: OpenRouter acts as a proxy between developers and LLM providers, allowing users to try and use multiple models through a single API without managing separate accounts. It also provides billing caps, which are hard spending limits that prevent unexpected costs, a feature many providers lack.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/pricing">Pricing | OpenRouter</a></li>
<li><a href="https://openrouter.ai/docs/faq">OpenRouter FAQ | Developer Documentation | OpenRouter | Documentation</a></li>
<li><a href="https://apify.com/apify/openrouter">OpenRouter · Apify</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed sentiment. Some users praise OpenRouter for low-friction model access and billing caps, while others remain skeptical, arguing that the main value is just consolidating payment and that building a custom client is easy. The co-founder responded, emphasizing long-term commitment and product focus.

**Tags**: `#AI`, `#funding`, `#LLM`, `#infrastructure`, `#OpenRouter`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Zig ELF Linker Improvements Boost Iteration Speed</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Zig's devlog details major ELF linker improvements, including a new incremental linking mode that significantly reduces rebuild times. The new linker, called Elf2, delivers up to 11x faster incremental builds with near-zero overhead. These improvements make Zig a more compelling C replacement by enabling faster development iteration, similar to interpreted languages. Faster linking reduces the compile-edit-debug cycle, benefiting systems programmers and potentially expanding Zig's adoption. The incremental linking mode is designed for development builds and is mutually exclusive with link-time optimization (LTO), which is used for release builds. The linker is currently Linux-focused, with Windows improvements expected in future releases.

🔗 [Source](https://ziglang.org/devlog/2026/#2026-05-30)

hackernews · kristoff_it · May 30, 17:29 · [Discussion](https://news.ycombinator.com/item?id=48338673)

**Background**: A linker is a tool that combines compiled object files into a single executable or library. Traditional linkers like GNU ld or LLVM's lld can become a bottleneck in large projects, especially during development when only small changes are made. Zig's custom linker aims to provide near-instant relinking for changed code, dramatically improving developer productivity.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48338673">Zig ELF Linker Improvements Devlog | Hacker News</a></li>
<li><a href="https://biggo.com/news/202509220722_Zig_Elf2_Linker_11x_Faster_Builds">Zig's New Elf2 Linker Delivers 11x Faster Incremental Builds with Near-Zero Overhead - BigGo News</a></li>

</ul>
</details>

**Discussion**: Commenters are enthusiastic, with one noting that Zig could become 'THE C replacement' and enable iteration speeds comparable to JavaScript or Python. Another commenter expressed relief at choosing Zig over Rust as a transpilation target due to its build system and linker. Some raised concerns about the removal of @cImport and the Linux-only focus for now.

**Tags**: `#Zig`, `#linker`, `#systems programming`, `#compiler`, `#performance`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">EY Canada cybersecurity report had hallucinated citations</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

EY Canada published a 44-page cybersecurity report on loyalty-program fraud, but AI-detection firm GPTZero found that 16 of 27 citations (about 60%) were hallucinated, including broken URLs and invented sources attributed to McKinsey, Gartner, and Forbes. EY subsequently retracted the report. This incident exposes a widespread lack of human oversight in AI-generated content, especially in high-stakes consulting reports where accuracy is critical. It undermines trust in major consulting firms and highlights the need for rigorous vetting processes. GPTZero's investigation revealed that the report did not use footnotes or normal academic citations; many citations were broken URLs or never existed. The findings were covered by the Financial Times, leading to EY's retraction.

🔗 [Source](https://gptzero.me/investigations/ey)

hackernews · smartmic · May 30, 19:02 · [Discussion](https://news.ycombinator.com/item?id=48339580)

**Background**: AI hallucination refers to when an AI model generates false or misleading information presented as fact. In content generation, this is a known risk, especially for B2B marketing and consulting, where accuracy is paramount. Without proper human review, AI-generated content can contain fabricated citations and data.

<details><summary>References</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/ey-canada-retracts-report-with-60-hallucinated-citations">EY Canada retracts report with 60% hallucinated citations | AI Weekly</a></li>
<li><a href="https://gptzero.me/news/arxiv-ban/">GPTZero Research Motivates Major arXiv Ban on AI and Hallucinated ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration with the lack of vetting by knowledgeable professionals, noting that AI output is often skimmed or not reviewed before publication. Some criticized the report's poor formatting and JavaScript-heavy website, while others sarcastically dubbed the trend 'garbagemaxxing'.

**Tags**: `#AI`, `#cybersecurity`, `#hallucination`, `#consulting`, `#accountability`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Anthropic details sandboxing techniques across Claude products</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Anthropic published a detailed technical overview of sandboxing techniques used across Claude.ai, Claude Code, and Cowork, including gVisor, Seatbelt, and Bubblewrap. The article also discusses past security misses like the api.anthropic.com/v1/files exfiltration vector. This documentation addresses a common gap in trustworthiness for sandboxed AI products, providing transparency that helps users and developers assess security. It sets a precedent for other AI companies to openly document their isolation mechanisms. Claude.ai uses gVisor, a Google-developed container sandbox that implements Linux system calls in userspace. Claude Code uses Seatbelt on macOS and Bubblewrap on Linux, while Cowork runs a full VM via Apple's Virtualization framework or Windows HCS.

🔗 [Source](https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything)

rss · Simon Willison · May 30, 21:36

**Background**: Sandboxing isolates AI agents from the host system to prevent unauthorized access or data exfiltration. gVisor is an open-source application kernel that provides a lightweight isolation layer for containers. Seatbelt is macOS's built-in sandbox framework, and Bubblewrap is a Linux tool for unprivileged namespace-based sandboxing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GVisor">gVisor - Wikipedia</a></li>
<li><a href="https://github.com/containers/bubblewrap">GitHub - containers/bubblewrap: Low-level unprivileged ...</a></li>
<li><a href="https://github.com/bkircher/seatbelt">GitHub - bkircher/ seatbelt : Simple macOS Seatbelt wrapper that runs...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#sandboxing`, `#Anthropic`, `#security`, `#Claude`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Running Python ASGI apps in browser via Pyodide and service workers</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Simon Willison demonstrated a method to run Python ASGI applications in the browser using Pyodide and service workers, overcoming the previous limitation that script tags were not executed. He provided demos of a basic ASGI app and Datasette 1.0a31 running entirely client-side. This approach enables full-featured Python web applications to run entirely in the browser without a server, including support for JavaScript-heavy plugins. It significantly expands the capabilities of client-side Python frameworks like Datasette Lite. The solution uses service workers to intercept network requests and execute Python ASGI code via Pyodide, allowing script tags to execute normally. The implementation was developed with assistance from Claude Opus 4.8 in Claude Code for web.

🔗 [Source](https://simonwillison.net/2026/May/30/pyodide-asgi-browser/#atom-everything)

rss · Simon Willison · May 30, 21:02

**Background**: Pyodide is a port of CPython to WebAssembly that enables running Python in the browser. ASGI (Asynchronous Server Gateway Interface) is a standard for building async Python web applications. Service workers are scripts that run in the background of a web browser, intercepting network requests and enabling offline functionality. Datasette Lite is a version of the Datasette data exploration tool that runs entirely in the browser via Pyodide.

<details><summary>References</summary>
<ul>
<li><a href="https://pyodide.org/">Pyodide — Version 0.29.4</a></li>
<li><a href="https://github.com/pyodide/pyodide">GitHub - pyodide/pyodide: Pyodide is a Python distribution ... Home - Pyodide pyodide | Pyodide is a Python distribution for the browser ... Online Python (Pyodide) - Run Python in Browser via WebAssembly pyodide - npm Pyodide — Version 0.17.0</a></li>

</ul>
</details>

**Tags**: `#Pyodide`, `#ASGI`, `#WebAssembly`, `#Service Workers`, `#Datasette`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Anthropic's run-rate revenue hits $47 billion</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Anthropic announced that its run-rate revenue crossed $47 billion in May 2026, up from $9 billion at the end of 2025 and $30 billion in April 2026. This was disclosed as part of its $65 billion Series H funding round at a $965 billion post-money valuation. This explosive revenue growth signals massive enterprise adoption of AI, with Anthropic scaling organic revenue faster than any company in history. It also validates the business model of AI model providers and may influence investor expectations for the upcoming IPO. Run-rate revenue is an annualized projection based on the most recent month's revenue multiplied by 12. The $47 billion figure was disclosed in the Series H announcement, and the company previously reported $14 billion in February 2026 and $30 billion in April 2026.

🔗 [Source](https://simonwillison.net/2026/May/29/anthropic/#atom-everything)

rss · Simon Willison · May 29, 01:23

**Background**: Run-rate revenue is a metric that extrapolates current monthly revenue to estimate annual revenue, often used by fast-growing startups to indicate momentum. Anthropic is an AI company that develops the Claude model family, competing with OpenAI and others. The company has raised massive funding rounds and is reportedly preparing for an IPO.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/series-h">Anthropic raises $65B in Series H funding at $965B post-money ...</a></li>
<li><a href="https://www.investopedia.com/terms/r/runrate.asp">investopedia.com/terms/r/runrate.asp</a></li>
<li><a href="https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/">Anthropic raises $65 billion, nears $1T valuation ahead of IPO</a></li>

</ul>
</details>

**Discussion**: The post author notes that some skeptics, like Ed Zitron, questioned the earlier $30 billion figure, but argues that lying to investors in fundraising announcements would constitute securities fraud. The author also highlights that an AI consultant reported a client spending $500 million in a single month on Claude licenses without usage limits, which would add $6 billion to run-rate.

**Tags**: `#AI`, `#Anthropic`, `#revenue`, `#enterprise`, `#funding`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Boston Children's uses AI to diagnose rare diseases</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Boston Children's Hospital has used OpenAI technology to help diagnose more than 40 rare disease cases, improving patient care and reducing operational burden. This demonstrates a real-world, high-impact application of AI in healthcare, potentially shortening the diagnostic odyssey for rare disease patients and setting a precedent for AI-assisted clinical diagnosis. The hospital used OpenAI's technology, likely including GPT-4 or similar models, to analyze complex medical data and identify rare conditions that are often misdiagnosed or undiagnosed.

🔗 [Source](https://openai.com/index/boston-childrens-hospital)

rss · OpenAI Blog · May 29, 12:00

**Background**: Rare diseases affect millions worldwide but often take years to diagnose due to limited knowledge and specialist availability. AI models trained on vast medical literature can assist clinicians by suggesting possible diagnoses based on patient symptoms and test results. OpenAI has recently launched a dedicated healthcare suite to support such applications.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/openai-for-healthcare/">Introducing OpenAI for Healthcare</a></li>
<li><a href="https://www.beckershospitalreview.com/healthcare-information-technology/innovation/openais-growing-healthcare-footprint/">OpenAI’s growing healthcare footprint</a></li>
<li><a href="https://www.fiercehealthcare.com/health-tech/openai-rolls-out-chatgpt-healthcare-genai-workspace-enterprises">OpenAI launches ChatGPT for Healthcare to support enterprises</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Healthcare`, `#Rare Diseases`, `#OpenAI`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">OpenAI launches Rosalind Biodefense for biodefense</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

OpenAI announced Rosalind Biodefense, an initiative providing trusted access to its GPT-Rosalind AI model for vetted developers and U.S. government partners working on biodefense, public health, and pandemic preparedness. This initiative applies frontier AI to critical societal challenges, potentially accelerating biodefense research and pandemic response while ensuring responsible use through controlled access. Rosalind Biodefense builds on GPT-Rosalind, a reasoning model optimized for life sciences, and restricts access to vetted entities to prevent misuse.

🔗 [Source](https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense)

rss · OpenAI Blog · May 29, 03:00

**Background**: GPT-Rosalind is a frontier reasoning model introduced by OpenAI in April 2026, designed to support research in biology, drug discovery, and translational medicine. Rosalind Biodefense extends this model's availability to biodefense and public health applications, with a focus on trusted partnerships.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-rosalind/">Introducing GPT-Rosalind for life sciences research | OpenAI</a></li>
<li><a href="https://openai-dotcom-git-main-openai.vercel.app/index/strengthening-societal-resilience-with-rosalind-biodefense/">Strengthening societal resilience with Rosalind Biodefense | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#biodefense`, `#public health`, `#OpenAI`, `#pandemic preparedness`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Accenture acquires Ookla for $1.2B to boost network intelligence</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Accenture has agreed to acquire Ookla, the company behind Speedtest, Downdetector, Ekahau, and RootMetrics, for $1.2 billion. The deal aims to strengthen Accenture's network intelligence and data-driven services for enterprises. This acquisition gives Accenture access to Ookla's massive dataset of over 250 million consumer-initiated tests per month, which is critical for optimizing 5G and Wi-Fi networks. It positions Accenture to offer enhanced network intelligence and AI-powered solutions to telecom operators, hyperscalers, and enterprises. Ookla's data platform includes controlled drive, walk, and embedded testing options in addition to consumer-initiated tests. The deal is valued at $1.2 billion and is expected to close in the second half of 2026.

🔗 [Source](https://newsroom.accenture.com/news/2026/accenture-to-acquire-ookla-to-strengthen-network-intelligence-and-experience-with-data-and-ai-for-enterprises)

hackernews · Garbage · May 30, 16:28 · [Discussion](https://news.ycombinator.com/item?id=48337987)

**Background**: Ookla is best known for Speedtest.net, a widely used internet speed testing service, and Downdetector, which tracks real-time outages of websites and services. The company monetizes its data by selling insights to telecom operators who use it to improve network performance. Accenture is a global IT services and consulting firm that has been expanding its data and AI capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://newsroom.accenture.com/news/2026/accenture-to-acquire-ookla-to-strengthen-network-intelligence-and-experience-with-data-and-ai-for-enterprises">Accenture to Acquire Ookla to Strengthen Network Intelligence ...</a></li>
<li><a href="https://www.ookla.com/">Ookla® | Unmatched network and connectivity insights</a></li>
<li><a href="https://en.wikipedia.org/wiki/Downdetector">Downdetector - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Ookla's primary business is selling network performance data to telcos, who pay six-figure annual fees. Some expressed surprise at the high valuation, given the perceived simplicity of the products, while others pointed to the value of the data and the competitive moat built over years.

**Tags**: `#acquisition`, `#network intelligence`, `#telecom`, `#data monetization`, `#AI`

</details>


<a id="item-11"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Voxel Space: The 1992 Heightmap Rendering Algorithm Explained</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A detailed technical explanation of the Voxel Space algorithm used in the 1992 game Comanche has been published, along with community ports and applications. This algorithm was groundbreaking for its time, enabling real-time 3D terrain rendering on limited hardware, and its simplicity continues to inspire hobbyist game developers and demoscene projects. The Voxel Space engine rasters height and color maps by drawing vertical lines, making it a 2.5D engine rather than true voxel rendering. It does not compute illumination during rendering, relying on pre-colored maps.

🔗 [Source](https://s-macke.github.io/VoxelSpace/)

hackernews · davikr · May 30, 14:25 · [Discussion](https://news.ycombinator.com/item?id=48336564)

**Background**: In computer graphics, a heightmap is a grayscale image where pixel values represent elevation. Voxel Space uses a heightmap and a color map to render terrain from a first-person perspective. The algorithm is similar to ray casting but optimized for height fields, allowing the 1992 game Comanche to run smoothly on CPUs of that era.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Voxel">Voxel - Wikipedia</a></li>
<li><a href="https://web.archive.org/web/20250127131701/https://github.com/s-macke/VoxelSpace">GitHub - s-macke/VoxelSpace: Terrain rendering algorithm in less...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Heightmap">Heightmap - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the algorithm is technically a heightmap renderer, not true voxel graphics. They shared ports to C++ and the AGS Engine, and one user creatively applied the game's first mission as a metaphor for minimal testing in software development.

**Tags**: `#rendering`, `#voxel`, `#retro-gaming`, `#algorithm`, `#heightmap`

</details>


<a id="item-12"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Openrsync: OpenBSD's clean-room rsync implementation</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

OpenBSD's openrsync, a clean-room implementation of the rsync file synchronization tool, is now included in macOS 15.0. However, it lacks support for recent protocol features such as 64-bit timestamps. This provides a BSD-licensed alternative to the widely-used but GPL-licensed rsync, enabling broader adoption in systems that prefer permissive licenses. Its inclusion in macOS highlights its reliability, though missing features may limit its use for modern filesystems. Openrsync is developed as part of a RPKI validator project and does not support the latest rsync protocol versions, notably lacking 64-bit timestamp support. Users report issues with certain command-line behaviors, such as creating remote paths incorrectly.

🔗 [Source](https://github.com/kristapsdz/openrsync)

hackernews · sph · May 30, 10:51 · [Discussion](https://news.ycombinator.com/item?id=48334854)

**Background**: rsync is a widely used utility for synchronizing files locally or over a network, known for its delta-transfer algorithm that only sends differences. OpenBSD is a security-focused Unix-like operating system that produces many portable components under a BSD license.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Openrsync">Openrsync</a></li>
<li><a href="https://github.com/kristapsdz/openrsync">GitHub - kristapsdz/ openrsync : BSD-licensed implementation of rsync</a></li>
<li><a href="https://rsync.samba.org/features.html">rsync features</a></li>

</ul>
</details>

**Discussion**: Community members note that openrsync has improved over time but still has compatibility gaps, such as with --rsync-path. Some point out that a Go implementation also exists, and that openrsync is developed as part of an RPKI validator.

**Tags**: `#rsync`, `#OpenBSD`, `#open-source`, `#file-sync`, `#security`

</details>


<a id="item-13"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Datasette 1.0a31 adds write queries and stored queries</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Datasette 1.0a31 introduces the ability for authorized users to execute write queries (INSERT, UPDATE, DELETE) against databases and to save stored queries (renamed from 'canned queries') for sharing within a Datasette instance. This release transforms Datasette from a read-only exploration tool into a platform that supports data modification and collaborative query management, significantly expanding its use cases for data editing and team workflows. Write queries require appropriate permissions (e.g., insert-row, update-row) and are executed via a new interface. Stored queries persist in Datasette's internal database when run with the --internal flag.

🔗 [Source](https://simonwillison.net/2026/May/29/datasette/#atom-everything)

rss · Simon Willison · May 29, 03:32

**Background**: Datasette is an open-source tool for exploring and publishing SQLite databases. Previously, it only allowed read-only SQL queries via its web interface. This alpha release adds write capabilities and a way to save queries for reuse, building on the existing 'canned queries' feature.

<details><summary>References</summary>
<ul>
<li><a href="https://datasette.io/blog/2026/sql-write-queries/">SQL write queries and stored queries in Datasette 1.0a31</a></li>
<li><a href="https://github.com/simonw/datasette/issues/2735">Rebrand "canned queries " to " queries ", put them in internal ...</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#open source`, `#database`, `#SQL`, `#release`

</details>


<a id="item-14"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">OpenAI publishes framework for third-party AI evaluations</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

OpenAI has published a shared playbook for trustworthy third-party evaluations of frontier AI models, detailing how to assess capabilities, safeguards, and validity. This guidance helps standardize the evaluation of frontier AI systems, which is critical for AI safety and governance as models become more powerful and widely deployed. The framework covers three core areas: model capabilities (what the model can do), safeguards (built-in safety measures), and validity (whether evaluations are reliable and reproducible).

🔗 [Source](https://openai.com/index/trustworthy-third-party-evaluations-foundations)

rss · OpenAI Blog · May 29, 00:00

**Background**: Frontier AI models are the most advanced AI systems available at a given time, trained on massive datasets to achieve state-of-the-art performance across many tasks. Third-party evaluations are independent assessments conducted by external organizations to verify claims about a model's capabilities and safety, which is increasingly important as these models are integrated into critical applications.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/trustworthy-third-party-evaluations-foundations/">A shared playbook for trustworthy third party evaluations</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work - NVIDIA</a></li>
<li><a href="https://hai.stanford.edu/news/strengthening-ai-accountability-through-better-third-party-evaluations">Strengthening AI Accountability Through Better Third Party ...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#evaluation`, `#frontier models`, `#governance`, `#OpenAI`

</details>


<a id="item-15"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Hugging Face Publishes Beginner's Guide to PyTorch Profiler</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Hugging Face released a beginner-friendly blog tutorial on using torch.profiler to profile PyTorch models and identify performance bottlenecks. This tutorial helps developers optimize their deep learning models by providing practical profiling techniques, which is crucial for reducing training time and improving inference efficiency. The guide covers the torch.profiler context manager API, enabling users to examine operator costs, input shapes, stack traces, and GPU kernel activity.

🔗 [Source](https://huggingface.co/blog/torch-profiler)

rss · Hugging Face Blog · May 29, 00:00

**Background**: PyTorch Profiler (torch.profiler) is a built-in tool for collecting performance metrics during model training and inference. It helps developers understand which operations are most expensive and where bottlenecks occur, enabling targeted optimization.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.pytorch.org/docs/stable/profiler.html">torch.profiler — PyTorch 2.11 documentation</a></li>
<li><a href="https://docs.pytorch.org/tutorials/beginner/profiler.html">Profiling your PyTorch Module — PyTorch Tutorials 2.12.0+cu130...</a></li>

</ul>
</details>

**Tags**: `#PyTorch`, `#profiling`, `#performance optimization`, `#deep learning`, `#tutorial`

</details>


</section>