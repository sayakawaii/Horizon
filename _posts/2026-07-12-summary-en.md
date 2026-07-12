---
layout: default
title: "Horizon Summary: 2026-07-12 (EN)"
date: 2026-07-12
lang: en
---

> From 105 items, 8 important content pieces were selected

---

<section class="cat cat-science" markdown="1">

## 🧪 Science (1)

<a id="item-1"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Shingles vaccine may reduce dementia risk</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A UK study using a natural age-based cutoff found that people eligible for the shingles vaccine had a significantly lower risk of developing dementia over seven years. This finding suggests a simple, widely available vaccine could help prevent dementia, a condition affecting millions worldwide with no cure. The study exploited a hard age cutoff in UK vaccine eligibility, creating a natural experiment that strengthens causal evidence. The effect was observed with the newer Shingrix vaccine, which contains adjuvants that may boost immune response.

🔗 [Source](https://www.economist.com/leaders/2026/07/09/a-no-brainer-for-protecting-your-brain)

hackernews · saikatsg · Jul 12, 15:23 · [Discussion](https://news.ycombinator.com/item?id=48881874)

**Background**: Dementia, including Alzheimer's disease, is a progressive brain disorder that impairs memory and cognition. Previous observational studies have hinted at a link between shingles vaccination and lower dementia risk, but confounding factors made causation uncertain. The age-cutoff design helps isolate the vaccine's effect.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nytimes.com/2025/04/02/health/shingles-vaccine-dementia.html">Shingles Vaccine Can Decrease Risk of Dementia , Study Finds...</a></li>
<li><a href="https://www.theguardian.com/society/2025/apr/02/study-finds-strongest-evidence-yet-that-shingles-vaccine-helps-cut-dementia-risk">Study finds strongest evidence yet that shingles vaccine helps cut...</a></li>
<li><a href="https://medicalxpress.com/news/2026-06-shingles-vaccine-dementia.html">Shingles vaccine may lower dementia risk , study suggests</a></li>

</ul>
</details>

**Discussion**: Commenters shared personal anecdotes and scientific context. Some expressed skepticism, citing a potential detection bias: vaccinated people may have fewer hospital visits and thus fewer incidental dementia diagnoses. Others noted multiple risk factors for dementia and argued the vaccine is a worthwhile intervention.

**Tags**: `#dementia`, `#vaccine`, `#public health`, `#neuroscience`, `#epidemiology`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (7)

<a id="item-2"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">vLLM v0.25.0: MRv2 Default, PagedAttention Removed</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

vLLM v0.25.0 makes Model Runner V2 the default for all dense models, removes the legacy PagedAttention implementation, and introduces a new Streaming Parser Engine. The release includes 558 commits from 232 contributors, adds support for new models like LLaVA-OneVision-2 and GLM-5, and improves the Transformers backend to match native vLLM performance. This release marks a major architectural shift in vLLM, consolidating execution paths and removing legacy code, which simplifies maintenance and improves performance. The new default MRv2 and removal of PagedAttention signal a mature, streamlined inference engine that benefits the entire LLM serving ecosystem. Model Runner V2 now supports EVS, realtime embeddings, prefix caching for Mamba hybrid models, and dynamic speculative decoding with full CUDA graphs. The Transformers backend achieved parity with native vLLM speed and gained FP8 MoE support, while the new Streaming Parser Engine provides a unified framework for tool-call and reasoning parsing.

🔗 [Source](https://github.com/vllm-project/vllm/releases/tag/v0.25.0)

github · khluu · Jul 11, 20:06

**Background**: vLLM is a high-throughput, memory-efficient LLM inference and serving engine originally developed at UC Berkeley. PagedAttention was its core innovation, enabling efficient memory management for attention computation. Model Runner V2 (MRv2) is a newer execution backend that consolidates model execution and improves performance. This release makes MRv2 the default for dense models and removes the older PagedAttention code, as the V1/MRv2 backends now cover all use cases.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm-project/vllm</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>
<li><a href="https://vllm.ai/blog/2023-06-20-vllm">vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#open source`, `#release`, `#AI infrastructure`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Claude Code uses 33k tokens before reading prompt vs OpenCode's 7k</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A study by Systima found that Claude Code sends approximately 33,000 tokens before reading the user's prompt, while OpenCode sends only about 7,000 tokens, a 4.7x difference in token overhead. This inefficiency can significantly increase costs for users, especially those on token-based billing, and raises questions about design trade-offs in AI coding tools. The overhead comes from system prompts, cache writes, MCP schema definitions, and subagent orchestration. However, on multi-step tasks, Claude Code's total token usage can be lower due to batching.

🔗 [Source](https://systima.ai/blog/claude-code-vs-opencode-token-overhead)

hackernews · systima · Jul 12, 18:25 · [Discussion](https://news.ycombinator.com/item?id=48883275)

**Background**: Claude Code and OpenCode are AI-powered coding assistants that use large language models to help developers write code. They send system prompts and context to the model before processing user input, which consumes tokens that users pay for.

<details><summary>References</summary>
<ul>
<li><a href="https://systima.ai/blog/claude-code-vs-opencode-token-overhead">Claude Code Sends 4.7x More Tokens Than OpenCode Before Reading Your Prompt | Systima Blog</a></li>
<li><a href="https://github.com/anthropics/claude-code/issues/26404">[Bug Report] Weekly token usage limit draining abnormally fast...</a></li>
<li><a href="https://www.truefoundry.com/blog/opencode-token-usage-how-it-works-and-how-to-optimize-it">OpenCode Token Usage: How It Works and How to Optimize It</a></li>

</ul>
</details>

**Discussion**: Commenters noted that subagents burn tokens quickly, and some suspected Anthropic designs Claude Code to use more tokens for profit. The author acknowledged a valid critique and plans to add qualitative comparisons and reproduce inputs/outputs.

**Tags**: `#AI coding tools`, `#token efficiency`, `#Claude Code`, `#OpenCode`, `#cost analysis`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Terry Tao on using LLM coding agents for apps</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Terry Tao, a renowned mathematician, shared his experience using modern LLM-based coding agents to build interactive visualizations and apps for his research papers, highlighting their utility for non-mission-critical tasks. This demonstrates that even top researchers are adopting LLM coding agents for practical software development, signaling a shift in how software is created across domains, especially for non-critical, exploratory tasks. Tao noted that while these agents are useful for generating supplements like visualizations, they are not trustworthy for mission-critical code, and he considers the risk acceptable for such non-essential components.

🔗 [Source](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/)

hackernews · subset · Jul 12, 11:09 · [Discussion](https://news.ycombinator.com/item?id=48880170)

**Background**: LLM coding agents are AI tools that use large language models to generate or assist in writing code. They have become increasingly popular for rapid prototyping and building simple applications, but their reliability for complex or safety-critical software remains debated.

<details><summary>References</summary>
<ul>
<li><a href="https://opencode.ai/">OpenCode | The open source AI coding agent</a></li>
<li><a href="https://cursor.com/">Cursor: AI coding agent</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about using LLMs for educational visualizations and noted the vast latent demand for software outside traditional tech fields. Some humorously compared Tao's experience to a chef discovering microwave dinners, while others emphasized the importance of treating LLMs as tools with appropriate trust boundaries.

**Tags**: `#LLM`, `#coding agents`, `#software development`, `#AI tools`, `#education`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">LLMs Are Transformative but Hype Is Overblown</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

George Hotz argues that while LLMs are transformative, frontier labs will not capture the value they create, and productivity gains are manifesting in private, one-off software rather than visible public projects. This analysis challenges the high valuations of frontier AI labs and highlights a shift in software development toward private, customized solutions, which could reshape open source dynamics and investment strategies. Hotz points out that frontier models are a no-brainer at $100–$200/month subscription, but the real productivity gains are happening in private homelabs and one-off scripts, not in public open source projects.

🔗 [Source](https://geohot.github.io//blog/jekyll/update/2026/07/12/i-love-llms.html)

hackernews · therepanic · Jul 12, 18:31 · [Discussion](https://news.ycombinator.com/item?id=48883343)

**Background**: Large Language Models (LLMs) like GPT-4 and Claude have shown remarkable capabilities in code generation, writing, and reasoning. Frontier labs such as OpenAI and Anthropic invest billions in training these models, betting on capturing value through subscriptions and APIs. However, open-source alternatives and private deployments are proliferating, raising questions about where the economic value ultimately accrues.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/ai-value-capture-the-shift-to-model">AI Value Capture - The Shift To Model Labs</a></li>
<li><a href="https://grokipedia.com/page/AI_Value_Capture">AI Value Capture</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree with Hotz's thesis, noting that LLMs enable a 'have it your way' era where forking and customizing software is easier than ever. Some express concern about the future of open source, as upstreaming becomes less attractive when maintaining a fork is trivial with LLM assistance.

**Tags**: `#LLMs`, `#AI hype`, `#open source`, `#productivity`, `#value capture`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Chromium 148 Math.tanh enables OS fingerprinting</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Chromium 148 introduced OS-dependent implementations of Math.tanh, allowing a single call to distinguish between Windows, macOS, and Linux. This creates a new browser fingerprinting vector that can reveal the underlying operating system. This technique undermines user privacy by making OS detection trivial, even when users spoof their User-Agent headers. It adds to the growing arsenal of fingerprinting methods that anti-fingerprinting tools must combat. The fingerprint works because Math.tanh implementations differ in rounding and precision across platforms. The technique can also fingerprint the browser version range, as the behavior may change between Chromium releases.

🔗 [Source](https://scrapfly.dev/posts/browser-math-os-fingerprint/)

hackernews · joahnn_s · Jul 12, 21:12 · [Discussion](https://news.ycombinator.com/item?id=48884853)

**Background**: Browser fingerprinting collects device and browser characteristics to identify users without cookies. Common techniques include canvas rendering, WebGL, and font detection. Math.tanh is a hyperbolic tangent function available in JavaScript; its implementation is not standardized to be identical across platforms, leading to OS-dependent behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Device_fingerprint">Device fingerprint - Wikipedia</a></li>
<li><a href="https://fingerprint.com/blog/browser-fingerprinting-techniques/">Browser Fingerprinting Techniques: 6 Top Methods Explained</a></li>
<li><a href="https://learn.microsoft.com/en-us/dotnet/api/system.math.tanh?view=net-10.0">Math.Tanh (Double) Method (System) | Microsoft Learn</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the technique can also fingerprint browser version ranges, which is more interesting than OS detection. Some criticized the article as likely AI-generated and motivated by the author's scraping business. Others advocated for correctly rounded transcendental functions to eliminate such fingerprinting vectors.

**Tags**: `#browser fingerprinting`, `#privacy`, `#Chromium`, `#JavaScript`, `#OS detection`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Irish datacenters now consume 23% of country's electricity</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Irish datacenters consumed 23% of the country's total metered electricity in 2025, up from 5% in 2015, according to recent data. This sharp rise highlights the growing energy demand from digital infrastructure, raising concerns about grid strain and sustainability, and fueling debates on energy solutions like nuclear power. By 2026, datacenters could account for 32% of Ireland's electricity consumption due to new builds. Ireland's total electricity use is about 40 TWh per year, less than the output of four EPR reactors.

🔗 [Source](https://www.theregister.com/on-prem/2026/07/11/irish-datacenters-now-guzzle-23-of-the-countrys-electricity/5270013)

hackernews · Bender · Jul 12, 20:16 · [Discussion](https://news.ycombinator.com/item?id=48884322)

**Background**: Ireland has become a major hub for datacenters due to favorable corporate taxes and a cool climate, attracting tech giants like Amazon and Google. The rapid expansion has strained the national grid, leading to a moratorium on new datacenter connections in Dublin until 2028. Nuclear power is not currently used in Ireland, but some propose it as a solution for baseload power.

<details><summary>References</summary>
<ul>
<li><a href="https://www.datacenterdynamics.com/en/news/global-data-center-electricity-use-to-double-by-2026-report/">Global data center electricity use to double by 2026 - IEA report - DCD</a></li>
<li><a href="https://extra.ie/2026/07/07/news/data-centres-consume-ireland-electricity">Data centres consume whopping amount of Irish electricity</a></li>
<li><a href="https://www.theregister.com/on-prem/2024/01/24/datacenters-could-draw-1/3-of-irelands-electricity-by-2026/1556307">Datacenters could draw 1/3 of Ireland 's electricity by 2026</a></li>

</ul>
</details>

**Discussion**: Commenters debated nuclear power as a solution, noting that a single reactor could power all Irish datacenters. Others criticized the article's wording as biased, and some compared Ireland's per-capita datacenter energy use to California's.

**Tags**: `#datacenter`, `#energy`, `#Ireland`, `#nuclear power`, `#sustainability`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">LLMs in coding: A CGI-like shift devaluing craftsmanship?</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Fabien Sanglard published an article comparing the rise of LLMs in coding to the CGI shift in film, arguing that while AI boosts volume, it may devalue craftsmanship and lead to a future backlash toward human-written code. This commentary resonates with many developers who worry that AI-generated code prioritizes quantity over quality, potentially eroding the value of hand-crafted software and sparking a long-term industry shift. The article notes that those who refuse to use LLMs may fall behind in volume, but emphasizes the importance of reading and understanding code architecture. It also highlights that writing tests is now easier, yet LLM-generated tests may not test the right behaviors.

🔗 [Source](https://fabiensanglard.net/extinct/index.html)

hackernews · zdw · Jul 12, 15:17 · [Discussion](https://news.ycombinator.com/item?id=48881830)

**Background**: Large Language Models (LLMs) like GPT-4 and Claude are increasingly used to generate code, promising speed and productivity gains. The film industry experienced a similar shift with CGI, which initially boosted visual effects but later faced criticism for replacing practical effects and devaluing skilled labor. Some now advocate for a return to practical effects, as seen in films like Project Hail Mary.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2506.16653">LLMs in Coding and their Impact on the Commercial Software ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computer-generated_imagery">Computer-generated imagery - Wikipedia</a></li>
<li><a href="https://www.nature.com/articles/s41599-025-04471-1">LLM-based collaborative programming: impact on students ...</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree with the analogy, noting that CGI devalued skilled labor due to non-unionized VFX houses, and predict a similar backlash toward AI-generated code. Some argue that volume-based evaluation is not common in software engineering, and that LLM-generated tests may miss behavioral correctness.

**Tags**: `#LLM`, `#software engineering`, `#AI impact`, `#craftsmanship`, `#analogy`

</details>


</section>