---
layout: default
title: "Horizon Summary: 2026-08-02 (EN)"
date: 2026-08-02
lang: en
---

> From 114 items, 8 important content pieces were selected

---

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (7)

<a id="item-1"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">OpenAI's Astra Solves Ten Open Math Problems</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

OpenAI announced that an internal version of its next major model, Astra, solved ten long-standing open problems in mathematics and theoretical computer science, covering geometry, cryptography, and complexity. The company claims each solution cost less than $2,000 at GPT-5.6 Sol token prices, and they have released Lean 4 formalizations and a paper describing the results. This marks a significant milestone in AI-driven mathematical research, potentially accelerating discovery in fields that rely on complex proofs. It could shift how mathematicians work, moving toward human-AI collaboration as envisioned by Terence Tao's 'big mathematics' concept. The results are formalized in Lean 4, ensuring verifiability, and OpenAI released a paper and an LLM-generated PDF reconstructing the proof process. However, the company did not disclose how many problems were attempted unsuccessfully, and the prompts used were not shared, limiting full transparency.

🔗 [Source](https://openai.com/index/ten-advances-in-mathematics)

rss · OpenAI Blog · Aug 1, 00:00

**Background**: Lean 4 is an interactive theorem prover that allows formal verification of mathematical proofs, making AI-generated results more trustworthy. OpenAI's announcement follows Anthropic's recent discovery of cryptographic weaknesses using Claude Mythos Preview, highlighting a trend of AI tackling complex mathematical challenges. The field of AI for mathematics has been growing, with models like GPT-4 and AlphaTensor making strides, but solving decade-old open problems is a new frontier.

<details><summary>References</summary>
<ul>
<li><a href="https://www.datacamp.com/blog/open-ai-model-astra-solved-ten-open-math-problems">OpenAI's New Model, Astra, Has Solved Ten Open Math Problems</a></li>
<li><a href="https://aitoolsreview.co.uk/insights/openai-astra-mathematics">OpenAI Astra Mathematics Results: Ten Claimed Advances Explained</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-sol">GPT-5.6 Sol - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion reflects a mix of awe and skepticism. Some mathematicians express a 'Deep Blue moment' feeling, while others question the lack of detail on failed attempts and the absence of prompts. There is also debate about the significance of the results, with some noting that formalization in Lean adds credibility, but independent verification is still needed.

**Tags**: `#mathematics`, `#theoretical computer science`, `#cryptography`, `#complexity`, `#OpenAI`

</details>


<a id="item-2"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Kakehashi: Run macOS Binaries on Linux ARM</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Kakehashi is an experimental userspace translation layer that loads Darwin Mach-O binaries on Linux aarch64, mapping a freestanding libSystem and translating BSD syscalls. It currently has working prototypes for 7-Zip, curl, and Xcode tools Git, with 7-Zip passing multi-threaded compression tests on an 8k-file tree. This project could enable running macOS CLI tools natively on Linux ARM, similar to how WINE/Proton allows Windows apps on Linux, potentially expanding cross-platform compatibility. It addresses a gap for developers and users who need macOS-specific tools on ARM Linux devices. Kakehashi is CLI-first and does not use JIT, instead translating syscalls in userspace. The 7-Zip prototype is currently about 5.2x slower than native Linux execution, but the author has a clear optimization plan. The project is early-stage and experimental, with a focus on CLI tools rather than GUI applications.

🔗 [Source](https://github.com/wie-project/kakehashi)

hackernews · vlad_kalinkin · Aug 2, 16:26 · [Discussion](https://news.ycombinator.com/item?id=49145937)

**Background**: macOS binaries use the Mach-O format and rely on macOS-specific system libraries and syscalls, making them incompatible with Linux. Compatibility layers like WINE translate Windows API calls to run Windows apps on Linux, and Darling is a similar project for macOS, but it has limited ARM64 support. Kakehashi takes a different approach by focusing on userspace translation without kernel modules, aiming for speed and simplicity.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/wie-project/kakehashi">GitHub - wie-project/kakehashi: Userspace macOS translation ...</a></li>
<li><a href="https://news.mcan.sh/item/49145937">Show HN: Kakehashi – Experimental userspace to run macOS ...</a></li>
<li><a href="https://habr.com/ru/articles/1065502/">Kakehashi : запуск macOS бинарников на Linux ARM. Часть... / Хабр</a></li>

</ul>
</details>

**Discussion**: The community is enthusiastic, with users expressing long-term interest and comparing it to the Darling project, suggesting potential collaboration. Some commenters note the project is still early and the problem is complex, while others hope for future extensions like running AU binaries on Linux. The author is actively engaging and sharing technical details.

**Tags**: `#macOS`, `#Linux`, `#ARM`, `#compatibility layer`, `#reverse engineering`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">F*: A Proof-Oriented Programming Language for Verified Software</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

F* is a general-purpose proof-oriented programming language that combines functional programming with refinement types and dependent types, enabling formal verification of critical software. It is actively developed by Microsoft Research and Inria, and can extract code to OCaml, F#, C, WebAssembly, and assembly. F* provides a practical way to write software with machine-checked proofs of correctness and security properties, which is crucial for high-assurance systems in areas like cryptography, networking, and critical infrastructure. Its ability to extract to multiple languages makes it versatile for integrating verified components into existing codebases. F* uses SMT solving and tactic-based interactive theorem proving to automate proofs. It supports both purely functional and effectful programming, and its type system includes dependent types, monadic effects, and refinement types. The KaRaMeL tool extracts low-level F* to C or WebAssembly, while Vale extracts to assembly.

🔗 [Source](https://fstar-lang.org/)

hackernews · ducktective · Aug 2, 12:31 · [Discussion](https://news.ycombinator.com/item?id=49143925)

**Background**: Formal verification uses mathematical methods to prove that software behaves correctly according to its specification. Refinement types enrich a language's type system with logical predicates, allowing more precise specifications. F* is part of a lineage of proof-oriented languages like Coq and Agda, but focuses on practical verification with automation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F*_(programming_language)">F* (programming language) - Wikipedia</a></li>
<li><a href="https://fstar-lang.org/">F*: A Proof-Oriented Programming Language</a></li>
<li><a href="https://github.com/FStarLang/FStar">GitHub - FStarLang/FStar: A Proof-oriented Programming Language F* (programming language) - Wikipedia Proof-oriented Programming in F* — Proof-Oriented Programming ... Proof-Oriented Programming Languages - emergentmind.com FStarLang · GitHub F* – general-purpose, proof-oriented programming language</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion shows interest in F*'s practical use, such as migrating C codebases, and curiosity about industry adoption. Some users criticized the website for lacking code examples on the front page, while others pointed to the tutorial. Overall sentiment is positive, with users finding the language solid and interesting.

**Tags**: `#formal verification`, `#programming languages`, `#proof-oriented`, `#functional programming`, `#F*`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">AI Industry Open Letters Debate Open-Weight Models and Regulation</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

In late July 2026, Microsoft shepherded an open letter signed by 235 AI companies, including NVIDIA and OpenAI, advocating for open-weight AI models against potential government restrictions. Anthropic and a group of 1,324 frontier AI employees published separate responses, with the latter calling for international efforts to pace AI development. This debate highlights a critical policy fork: whether to prioritize open innovation or mitigate risks from powerful AI. The outcome could shape global AI regulation, influence competitive dynamics between the US and China, and determine how AI safety is balanced with economic growth. The Microsoft-led letter explicitly supports distillation, a practice where models train on outputs from other models, arguing it is a legitimate technique. Anthropic's response, while not advocating a ban, warns of risks from authoritarian misuse and calls for cracking down on industrial-scale distillation operations. Notably, Anthropic did not sign the Microsoft letter.

🔗 [Source](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything)

rss · Simon Willison · Aug 2, 04:16

**Background**: Open-weight models are AI models whose core components, including the trained weights, are publicly released, allowing anyone to download and use them. This contrasts with closed models, which are accessible only via APIs. The debate centers on whether open weights enable broader research and safety improvements or pose risks due to difficulty in applying guardrails and monitoring usage.

<details><summary>References</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://www.anthropic.com/news/position-open-weights-models">Our position on open-weights models \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open-source`, `#open-weight models`, `#regulation`, `#industry`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">DeepSeek V4-Flash-0731: 304B Model with Top Value-Per-Intelligence</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

DeepSeek released V4-Flash-0731, a 304B parameter model with substantially enhanced agentic capabilities, replacing the earlier preview. It is priced at $0.14 per million input tokens and $0.27 per million output tokens, and ranks ahead of MiniMax M3 (428B) on the Artificial Analysis Intelligence Index. This release offers one of the best value-per-intelligence ratios in the market, making advanced AI capabilities more accessible and cost-effective for developers and enterprises. Its strong agentic performance could accelerate adoption of AI agents in production workflows, intensifying competition among model providers. The model is 167GB on Hugging Face and available via OpenRouter and LM Studio. Simon Willison's tests showed that default reasoning level produced poor results, but setting reasoning_effort to 'high' significantly improved output quality, highlighting the importance of tuning reasoning effort.

🔗 [Source](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything)

rss · Simon Willison · Jul 31, 23:59

**Background**: DeepSeek is a Chinese AI research company known for releasing open-weight models that compete with leading proprietary models at lower cost. The Artificial Analysis Intelligence Index is a composite benchmark that evaluates reasoning, coding, knowledge, and multi-step task completion. Agentic capabilities refer to a model's ability to autonomously perform tasks, such as using tools and planning, which are crucial for AI agents.

<details><summary>References</summary>
<ul>
<li><a href="https://lmstudio.ai/models/deepseek-v4-flash">DeepSeek V 4 Flash</a></li>
<li><a href="https://api-docs.deepseek.com/news/news260424/">DeepSeek V 4 Preview Release | DeepSeek API Docs</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#DeepSeek`, `#model release`, `#pricing`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Stateless MCP Revives Interest, Inspires New Tools</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Simon Willison discusses the Stateless MCP update (MCP 2.0), which simplifies the protocol by removing the session handshake and enabling single-request tool calls. He built three new tools this week, including mcp-explorer and datasette-mcp, inspired by the new specification. This update makes MCP more accessible and scalable, potentially reigniting adoption among developers who had shifted to alternatives like Skills. It also enables smaller models to drive tools effectively, broadening the ecosystem of AI agents. The new stateless MCP uses a single HTTP request with headers like MCP-Protocol-Version and Mcp-Method, eliminating the need for session IDs and server-side state. This simplifies client and server implementation and improves scalability for web applications.

🔗 [Source](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything)

rss · Simon Willison · Jul 31, 23:13

**Background**: MCP (Model Context Protocol) is a standard for exposing tools to LLM-powered agents, introduced by Anthropic in November 2024. It gained huge popularity in 2025 but was later overshadowed by Skills, which offered more flexibility via terminal access. The stateless update addresses complexity and security concerns, making MCP more attractive again.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/">Announcing v2.0 of the official MCP C# SDK - .NET Blog</a></li>
<li><a href="https://modelcontextprotocol.io/specification/2026-07-28/changelog">Key Changes - Model Context Protocol</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#AI agents`, `#protocol`, `#Simon Willison`, `#LLM`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Karpathy Highlights Pelican-on-a-Bicycle Benchmark for LLM Physical World Understanding</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Andrej Karpathy highlighted a new benchmark that uses prompts like 'pelican on a bicycle' to test LLMs' understanding of the physical world, moving beyond simple image generation. This benchmark, originally created by Simon Willison, asks models to generate an SVG of a pelican riding a bicycle. This benchmark provides a qualitative measure of how well LLMs grasp physical concepts and spatial reasoning, which is crucial for advancing AI beyond text and image generation. It sparks discussion on benchmarking methodology and raises expectations for AI's ability to understand and simulate the real world. The benchmark was created by Simon Willison in late 2024 and has been used to track progress in LLMs over time. Karpathy's tweet suggests that while models have improved, the benchmark still exposes limitations in physical world understanding, and it may need to evolve to remain useful.

🔗 [Source](https://twitter.com/karpathy/status/2083749667410727319)

hackernews · delichon · Aug 2, 04:05 · [Discussion](https://news.ycombinator.com/item?id=49140998)

**Background**: Large language models (LLMs) are trained on vast amounts of text data and can generate coherent text, code, and images. However, their understanding of the physical world is often superficial, leading to errors in tasks that require spatial reasoning or common sense. Benchmarks like 'pelican on a bicycle' aim to test these abilities by requiring models to generate a specific visual representation from a simple prompt, revealing their grasp of physical constraints and relationships.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Pelican_on_a_bicycle_AI_benchmark">Pelican on a bicycle (AI benchmark) — Grokipedia</a></li>
<li><a href="https://github.com/simonw/pelican-bicycle">GitHub - simonw/pelican-bicycle: LLM benchmark: Generate an SVG of a pelican riding a bicycle · GitHub</a></li>
<li><a href="https://simonwillison.net/2025/Jun/6/six-months-in-llms/">The last six months in LLMs, illustrated by pelicans on bicycles</a></li>

</ul>
</details>

**Discussion**: The community discussion shows a mix of skepticism and support. Some commenters question the value of such benchmarks, arguing that they may be exhausted or that the quality of outputs is still poor. Others see it as a useful qualitative measure of progress, noting that models have moved beyond image generation to better expose physical world understanding. There is also a suggestion that perception methods need to scale more efficiently for significant improvements.

**Tags**: `#LLM`, `#benchmarking`, `#AI`, `#physical world understanding`, `#Karpathy`

</details>


</section>

<section class="cat cat-other" markdown="1">

## 📌 Other (1)

<a id="item-8"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">eBay Executives Sentenced in Harassment Campaign, $56M Payout</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

eBay executives were sentenced for orchestrating a harassment campaign against a couple, resulting in a $56 million payout. The sentences include prison time for key figures like Jim Baugh, former Senior Director of Safety and Security. This case highlights corporate accountability and the severe consequences of security team misconduct, serving as a warning to tech companies about the legal and ethical boundaries of protecting their interests. It underscores the importance of oversight and ethical conduct in corporate security operations. Jim Baugh received 57 months in prison, while Brian Gilbert was sentenced to time served, one year of supervised release, and a $20,000 fine. The campaign involved seven members of eBay's security team, including former police captains, who harassed and intimidated the victims.

🔗 [Source](https://www.ft.com/content/06ec1b03-d4af-40cf-b12a-4ba5a410f6d2)

hackernews · JumpCrisscross · Aug 2, 19:19 · [Discussion](https://news.ycombinator.com/item?id=49147435)

**Background**: The case stems from a 2019 incident where eBay executives targeted David and Ina Steiner, publishers of a newsletter critical of eBay, with a campaign of threats, surveillance, and harassment. The $56 million payout was part of a settlement with the Department of Justice, reflecting the severity of the misconduct.

**Discussion**: Community comments express skepticism about whether the harassment was limited to one couple, with some suggesting broader investigations. Others discuss human behavior under lack of supervision, referencing Scott Adams, and some criticize eBay's high seller fees compared to competitors like Leboncoin.

**Tags**: `#eBay`, `#harassment`, `#legal`, `#corporate ethics`, `#security`

</details>


</section>