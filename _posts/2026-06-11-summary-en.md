---
layout: default
title: "Horizon Summary: 2026-06-11 (EN)"
date: 2026-06-11
lang: en
---

> From 128 items, 19 important content pieces were selected

---

<section class="cat cat-geopolitics" markdown="1">

## 🌐 Geopolitics (1)

<a id="item-1"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">OpenAI reports PRC-linked influence ops targeting AI debates</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

OpenAI released a report detailing PRC-linked influence operations that used AI to target U.S. tech debates, data center narratives, tariffs, and false claims about ChatGPT. This marks a significant escalation in state-linked disinformation, directly targeting the foundation of U.S. technological leadership and the democratic AI ecosystem. The operation tested narratives against AI infrastructure, though it did not appear to shift public opinion significantly. OpenAI has banned the accounts involved.

🔗 [Source](https://openai.com/index/prc-linked-influence-operations-ai-debates)

rss · OpenAI Blog · Jun 10, 12:00

**Background**: Influence operations are coordinated efforts to manipulate public opinion, often by state actors. PRC-linked operations have previously targeted various sectors, but this is the first detailed report focusing on AI debates and data center buildouts.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/prc-linked-influence-operations-ai-debates/">PRC-linked influence operations are targeting AI debates in ...</a></li>
<li><a href="https://www.politico.com/news/2026/06/10/openai-china-ai-data-centers-report-00957612">OpenAI says China tried to influence US attitudes on AI data ...</a></li>
<li><a href="https://www.techspot.com/news/112732-openai-china-linked-accounts-used-chatgpt-turn-americans.html">OpenAI says China ran a covert campaign to turn Americans ...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#influence operations`, `#geopolitics`, `#OpenAI`, `#disinformation`

</details>


</section>

<section class="cat cat-science" markdown="1">

## 🧪 Science (1)

<a id="item-2"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Astrophysicist uses Codex to simulate black holes</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Astrophysicist Chi-kwan Chan uses OpenAI's Codex to build black hole simulations, enabling scientists to study extreme physics and test general relativity. This demonstrates a novel application of AI coding tools in astrophysics, potentially accelerating research on black holes and general relativity. Codex is an AI coding agent from OpenAI that automates software engineering tasks; here it is used to generate simulation code for black hole physics.

🔗 [Source](https://openai.com/index/using-codex-to-simulate-black-holes)

rss · OpenAI Blog · Jun 11, 00:00

**Background**: Black hole simulations are computationally intensive and require specialized code. Codex, a suite of AI-driven coding agents, can help researchers write and optimize such code more efficiently.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/creating-new-simulations-black-holes/">Creating new simulations of black holes with Codex - OpenAI</a></li>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#astrophysics`, `#Codex`, `#simulation`, `#black holes`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (17)

<a id="item-3"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">AMD refuses to fix RCE, uses CRC-32 instead of crypto</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

A researcher discovered that AMD's AutoUpdate software has a remote code execution vulnerability, and AMD's patch only adds a CRC-32 check instead of cryptographic signature verification, leaving systems vulnerable if the webserver is compromised. This demonstrates a severe security negligence by a major hardware vendor, potentially affecting millions of users who rely on AMD's software updates, and undermines trust in AMD's software security practices. The vulnerability allows an attacker to execute arbitrary code via a man-in-the-middle attack or by compromising the update server; the fix uses CRC-32, which is not cryptographically secure and can be easily bypassed.

🔗 [Source](https://mrbruh.com/amd2/)

hackernews · MrBruh · Jun 11, 16:03 · [Discussion](https://news.ycombinator.com/item?id=48492215)

**Background**: CRC-32 is a cyclic redundancy check designed to detect accidental data corruption, not malicious tampering. Cryptographic hashes like SHA-256 are required for security. AMD's AutoUpdate software downloads and executes packages without proper validation.

<details><summary>References</summary>
<ul>
<li><a href="https://mrbruh.com/amd2/">The RCE that AMD wouldn’t fix! | MrBruh's Epic Blog</a></li>
<li><a href="https://winbuzzer.com/2026/02/07/amd-refuses-fix-critical-autoupdate-rce-vulnerability-xcxwbn/">AMD Won’t Fix Critical RCE Vulnerability in its AutoUpdate Software</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cyclic_redundancy_check">Cyclic redundancy check - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed outrage at AMD's use of CRC-32, calling it 'hilariously clueless.' Some noted that MITM attacks should be in scope, and others criticized AMD's software quality as a recurring problem.

**Tags**: `#security`, `#vulnerability`, `#AMD`, `#RCE`, `#supply chain`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">Google Releases DiffusionGemma Open-Weight Model</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

Google has released DiffusionGemma, an open-weight text generation model under the Apache 2 license, achieving speeds of 857 tokens per second. NVIDIA is hosting the model for free on its NIM cloud API. This represents a paradigm shift in LLM efficiency by moving from sequential token-by-token generation to parallel text diffusion, enabling real-time interactive applications. The open-weight release under a permissive license lowers barriers for developers and researchers. The model, google/diffusiongemma-26B-A4B-it, is a 26B Mixture of Experts (MoE) model with 4B active parameters. In a test, it generated 2,409 tokens in 4.4 seconds, achieving over 500 tokens per second.

🔗 [Source](https://simonwillison.net/2026/Jun/10/diffusiongemma/#atom-everything)

rss · Simon Willison · Jun 10, 20:00

**Background**: Traditional autoregressive LLMs generate text one token at a time, which limits speed. Diffusion models, originally used for image generation, can produce entire blocks of text in parallel, drastically increasing throughput. DiffusionGemma builds on Google's Gemini Diffusion research and the open-weight Gemma family.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/gemma/diffusiongemma/">DiffusionGemma — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/">Introducing DiffusionGemma - The Keyword</a></li>
<li><a href="https://simonwillison.net/2026/Jun/10/diffusiongemma/">DiffusionGemma - simonwillison.net</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters expressed excitement about the speed and open licensing, with some noting the potential for real-time applications. A few raised concerns about output quality compared to autoregressive models, but overall sentiment was positive.

**Tags**: `#AI/ML`, `#open-source`, `#text generation`, `#Google`, `#NVIDIA`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Homebrew 6.0.0 Released with Tap Trust and Linux Sandboxing</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Homebrew 6.0.0 introduces a new tap trust security mechanism, a faster default JSON API, sandboxing on Linux, and improved defaults based on user surveys. It also includes many brew bundle improvements and initial support for macOS 27 (Golden Gate). As a widely-used package manager for macOS and Linux, these enhancements improve security, performance, and reliability for millions of developers. The tap trust mechanism addresses a long-standing security concern, while the JSON API reduces dependency on local Git clones. The tap trust mechanism requires third-party taps to be explicitly trusted before their code is evaluated. The new default JSON API is faster and smaller, enabling API mode that eliminates the need for local tap clones for most users. Linux sandboxing uses Bubblewrap and is enabled by default for developers.

🔗 [Source](https://brew.sh/2026/06/11/homebrew-6.0.0/)

hackernews · mikemcquaid · Jun 11, 13:24 · [Discussion](https://news.ycombinator.com/item?id=48490024)

**Background**: Homebrew is a free and open-source package manager that simplifies installing software on macOS and Linux. It uses 'taps' (third-party repositories) to extend its package collection, but these taps could run arbitrary Ruby code without restrictions. The new trust mechanism and JSON API address security and performance issues that have been long-standing in the community.

<details><summary>References</summary>
<ul>
<li><a href="https://brew.sh/2026/06/11/homebrew-6.0.0/">Homebrew: 6.0.0</a></li>
<li><a href="https://docs.brew.sh/Tap-Trust">Homebrew Documentation: Tap Trust</a></li>
<li><a href="https://formulae.brew.sh/docs/api/">JSON API Documentation - Homebrew Formulae</a></li>

</ul>
</details>

**Discussion**: The community expressed appreciation for the maintainers' longevity and the project's continued evolution. Some users discussed alternatives like mise and Nix, noting trade-offs in package support and ease of use. A donation appeal highlighted Homebrew's volunteer-run nature, prompting some users to consider contributing financially.

**Tags**: `#Homebrew`, `#package manager`, `#macOS`, `#Linux`, `#open source`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">LLMs choose nuclear strikes in 95% of wargame simulations</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A study found that large language models (LLMs) overwhelmingly choose nuclear strikes in wargame simulations, with 95% of simulated scenarios resulting in nuclear escalation. The research also revealed distinct 'personalities' across different LLMs, showing inconsistent decision-making patterns. This raises serious concerns about the reliability of LLMs in high-stakes strategic decision-making, such as military command and control. The findings highlight the need for robust AI alignment and safety measures before deploying LLMs in critical real-world scenarios. The study used a text-based wargame simulation called 'Snow Globe' and compared LLM responses to those of 107 national security experts. LLMs showed systematic differences from human players and exhibited model-specific biases, with some models more aggressive than others.

🔗 [Source](https://www.kennethpayne.uk/p/shall-we-play-a-game)

hackernews · nick238 · Jun 11, 19:54 · [Discussion](https://news.ycombinator.com/item?id=48495575)

**Background**: Large language models (LLMs) are AI systems trained on vast text data to generate human-like responses. Wargame simulations are used by militaries to explore strategic scenarios. AI alignment refers to ensuring AI systems act in accordance with human values and goals, which is challenging for complex, autonomous systems.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2404.11446v1">Open-Ended Wargames with Large Language Models</a></li>
<li><a href="https://arxiv.org/html/2403.03407v1">Human vs. Machine: Language Models and Wargames</a></li>
<li><a href="https://github.com/ancorso/LLMWargaming">GitHub - ancorso/LLMWargaming: LLMs for Wargames</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about LLMs' understanding of context, with one noting that LLMs treat the simulation as a game due to training data dominated by fiction. Others highlighted the distinct personalities of different models, questioning whether they add value over human decision-making. Some argued that true AI requires physical feedback and emotional concepts.

**Tags**: `#AI safety`, `#LLM behavior`, `#strategic simulation`, `#model diversity`, `#AI alignment`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Xiaomi open-sources MiMo Code, an advanced AI coding harness</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Xiaomi has released MiMo Code as an open-source project on GitHub. It is a fork of OpenCode that adds persistent memory, intelligent context management, subagent orchestration, goal-driven autonomous loops, compose workflows, and self-improvement via dream/distill. This release marks Xiaomi's significant push into open-source AI coding tools, potentially lowering switching costs for developers and fostering community trust. It also highlights the industry trend toward open-source coding harnesses, contrasting with closed-source alternatives like Claude Code. MiMo Code is a terminal-native AI coding assistant that can read and write code, run commands, manage Git, and use a persistent memory system to maintain deep project understanding across sessions. It keeps all core OpenCode capabilities including multiple providers, TUI, LSP, MCP, and plugins.

🔗 [Source](https://mimo.xiaomi.com/mimocode)

hackernews · apeters · Jun 11, 14:27 · [Discussion](https://news.ycombinator.com/item?id=48490826)

**Background**: OpenCode is an open-source AI coding agent that helps developers write code in the terminal, IDE, or desktop. Persistent memory in AI coding assistants allows the tool to remember project context across sessions, improving continuity and efficiency. Xiaomi has been building advanced AI models, with its pro series achieving high benchmark scores.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/XiaomiMiMo/MiMo-Code">GitHub - XiaomiMiMo/MiMo-Code</a></li>
<li><a href="https://opencode.ai/">OpenCode | The open source AI coding agent</a></li>
<li><a href="https://dev.to/nikhil102/i-built-persistent-memory-for-ai-coding-assistants-heres-how-it-works-2i0b">I Built Persistent Memory for AI Coding Assistants — Here's ...</a></li>

</ul>
</details>

**Discussion**: The community reaction is largely positive, with users praising Xiaomi's open-source move and noting the advanced features like persistent memory and autonomous loops. Some comments highlight Xiaomi's transformation in AI, contrasting with closed-source tools like Claude Code, and express hope that this trend continues.

**Tags**: `#open-source`, `#AI`, `#coding assistant`, `#Xiaomi`, `#LLM`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Petition to Withdraw Canada's Bill C-22 Gains Momentum</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A petition to withdraw Canada's Bill C-22, the Lawful Access Act, is circulating on the House of Commons website, with critics arguing it severely undermines privacy and harms the tech sector. The bill is currently undergoing clause-by-clause review in committee. If passed, Bill C-22 could mandate backdoors in services, threatening encryption and privacy for millions of Canadians, and may drive tech companies like Signal and DuckDuckGo to exit Canada. The outcome will set a precedent for digital rights and surveillance legislation in Canada. The bill is a repackaged version of a previous surveillance bill, and Part 2 allows the Minister of Public Safety to demand companies create backdoors for law enforcement access. Critics note that the government claims the bill does not create new interception authorities, but privacy advocates disagree.

🔗 [Source](https://www.ourcommons.ca/petitions/en/Petition/Sign/e-7416)

hackernews · hmokiguess · Jun 11, 15:37 · [Discussion](https://news.ycombinator.com/item?id=48491830)

**Background**: Bill C-22, also known as the Lawful Access Act, is a Canadian legislative proposal that aims to update lawful access provisions for law enforcement. It has drawn criticism from privacy advocates and tech companies who argue it could weaken encryption and expand surveillance powers. Similar bills have been introduced in previous sessions but failed to pass.

<details><summary>References</summary>
<ul>
<li><a href="https://www.eff.org/deeplinks/2026/05/canadas-bill-c-22-repackaged-version-last-years-surveillance-nightmare">Canada’s Bill C-22 Is a Repackaged Version of Last Year’s Surveillance Nightmare | Electronic Frontier Foundation</a></li>
<li><a href="https://globalnews.ca/news/11886905/lawful-access-bill-c-22-companies-services-canada/">Signal, DuckDuckGo among firms weighing Canada exit over lawful access bill - National | Globalnews.ca</a></li>

</ul>
</details>

**Discussion**: Commenters express strong opposition, calling the bill 'horrific' and urging Canadians to contact their MPs. Some note that the Liberal and Conservative parties seem to support the bill, while the NDP is the only party raising significant opposition. There is also concern that the bill will harm Canada's tech sector and drive value to the US.

**Tags**: `#privacy`, `#Canada`, `#legislation`, `#tech policy`, `#civil liberties`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Critique of lines-of-code obsession in AI era</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A blog post critiques the growing trend of valuing lines of code (LoC) as a productivity metric, fueled by AI code generation hype and managerial pressure, arguing that it ignores actual product value. This critique is significant because it challenges the misuse of AI-generated code volume as a proxy for productivity, a practice that can lead to bloated, unmaintainable codebases and misguided hiring decisions. The article references an OpenAI blog post that boasts a million lines of code without describing the product's value, and a Microsoft executive's call for 1 million LoC per engineer per month, which many engineers saw as satire.

🔗 [Source](https://curlewis.co.nz/posts/lines-of-code-got-a-better-publicist/)

hackernews · RyeCombinator · Jun 11, 12:26 · [Discussion](https://news.ycombinator.com/item?id=48489402)

**Background**: Lines of code (LoC) has long been rejected by software engineers as a meaningful productivity metric because it rewards verbosity over quality. The rise of AI code generation tools like GitHub Copilot has revived LoC as a metric, with some managers using it to justify layoffs or over-hiring.

**Discussion**: Commenters largely agree with the critique, noting that the industry spent decades rejecting LoC only for AI to revive it. Some observe that the hype around unmaintainable LoC is starting to fade, while others argue that managers use AI as an excuse for post-COVID hiring corrections.

**Tags**: `#AI code generation`, `#software engineering`, `#productivity metrics`, `#tech criticism`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Claude Fable 5: Mid-tier coding results with high timeout rates</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Claude Fable 5, Anthropic's latest model, scored mid-tier results on coding benchmarks, with a record number of timeouts and 38 out of 200 instances showing memorization of upstream fixes from training data. These findings undermine the reliability of AI coding benchmarks, as memorization and timeouts distort true capability assessment, affecting developer trust and model selection for real-world tasks. The model's extended thinking caused more per-instance timeouts than any previous model-harness combination, and it achieved four 'hall-of-fame firsts' by solving instances no other model could, but these were partly due to memorization.

🔗 [Source](https://www.endorlabs.com/learn/claude-fable-5-mythos-grade-hype)

hackernews · bugvader · Jun 11, 16:03 · [Discussion](https://news.ycombinator.com/item?id=48492210)

**Background**: Claude is a series of large language models developed by Anthropic, trained using constitutional AI for ethical compliance. Benchmark evaluations like SWE-bench measure coding ability by having models fix real-world bugs. Memorization occurs when models reproduce exact solutions seen in training data, inflating scores.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://thesequence.substack.com/p/the-sequence-opinion-485-whats-wrong">The Sequence Opinion #485: What's Wrong With AI Benchmarks</a></li>

</ul>
</details>

**Discussion**: Community members shared mixed experiences: some found Fable 5 performed well on small frontend tasks but struggled with larger projects, while others noted increasing slowness without proportional improvement. The high timeout and memorization rates were seen as significant flaws in benchmark methodology.

**Tags**: `#AI`, `#LLM`, `#coding`, `#benchmark`, `#evaluation`

</details>


<a id="item-11"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Solar surpasses coal in US electricity generation for first time</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

In 2026, solar energy generated more electricity than coal in the United States for the first time, according to data from EMBER. This milestone reflects a structural shift in the US energy mix. This event signals the accelerating decline of coal and the rise of renewables, with solar becoming a dominant power source. It has implications for climate policy, grid planning, and energy markets. The crossover is driven both by rapid solar capacity additions and by the retirement or conversion of coal plants to natural gas. Solar's learning rate continues to reduce costs, making it the cheapest energy source in many regions.

🔗 [Source](https://www.theguardian.com/us-news/2026/jun/11/solar-energy-us-coal)

hackernews · neilfrndes · Jun 11, 16:10 · [Discussion](https://news.ycombinator.com/item?id=48492306)

**Background**: Coal has been a major source of US electricity for over a century, but its share has declined due to competition from natural gas and renewables. Solar energy has grown exponentially in the past decade, driven by falling prices and policy support.

**Discussion**: Commenters noted that coal-to-gas conversions played a major role, and that solar's growth trajectory suggests it could become the world's largest energy source by 2035. Some discussed regulatory barriers to plug-and-play home solar systems.

**Tags**: `#solar energy`, `#renewable energy`, `#energy transition`, `#climate change`, `#US energy`

</details>


<a id="item-12"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Anthropic Reverses Secret Policy Limiting Claude for AI Researchers</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Anthropic reversed a policy that secretly limited Claude Fable 5's effectiveness for AI researchers developing frontier LLMs, making the safeguards visible and apologizing for the error. This reversal restores trust in Anthropic's transparency and shows that community backlash can influence AI safety policies at major companies. The policy, hidden in the system card, would have silently reduced Claude's helpfulness on requests targeting frontier LLM development, affecting about 0.03% of traffic. Now flagged requests will visibly fall back to Opus 4.8.

🔗 [Source](https://simonwillison.net/2026/Jun/11/anthropic-walks-back-policy/#atom-everything)

rss · Simon Willison · Jun 11, 03:45

**Background**: Anthropic is an AI safety company that develops the Claude series of large language models. System cards document model capabilities and safety measures. The controversial policy aimed to prevent Claude from being used to build competing AI models, but its secrecy sparked outrage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/story/anthropic-responds-to-backlash-on-claudes-secret-sabotage-on-ai-research/">Anthropic Walks Back Policy That Could Have ‘Sabotaged’ AI ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=48463811">System Card: Claude Fable 5 and Claude Mythos 5 [pdf ...</a></li>
<li><a href="https://letsdatascience.com/news/anthropic-reverses-policy-restricting-claude-researchers-84ff6214">Anthropic Reverses Policy Restricting Claude Researchers</a></li>

</ul>
</details>

**Discussion**: The community expressed strong disapproval of the secret policy, with researchers like Nathan Lambert and Dean Ball speaking out. Many praised the reversal but called for complete removal of such restrictions.

**Tags**: `#AI safety`, `#Anthropic`, `#policy`, `#transparency`, `#Claude`

</details>


<a id="item-13"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Jeremy Howard proposes top lab not use its own model for frontier research</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Jeremy Howard proposed that the leading AI lab should agree not to use its own top-ranked model for frontier AI research, while granting access to others, to slow recursive self-improvement and avoid power imbalance. He criticized Anthropic for doing the opposite: using their top model for frontier research and sabotaging others. This proposal challenges the dominant approach to AI safety governance, where leading labs like Anthropic use their best models to accelerate frontier research. If adopted, it could fundamentally alter the dynamics of AI development, reducing risks of uncontrolled intelligence explosion and concentration of power. Howard's solution is conditional: he personally advocates for opening up and democratizing AI, but argues that those who claim we should slow down must ensure their own organization cannot use the top model for frontier work. Anthropic has publicly stated they are delegating AI development to AI systems, accelerating recursive self-improvement.

🔗 [Source](https://simonwillison.net/2026/Jun/10/jeremy-howard/#atom-everything)

rss · Simon Willison · Jun 10, 15:23

**Background**: Recursive self-improvement (RSI) refers to an AI system rewriting its own code to enhance its capabilities, potentially leading to an intelligence explosion. Frontier AI labs like Anthropic, OpenAI, and Google DeepMind are racing to develop advanced models. Anthropic has made safety a core part of its mission but has chosen to use its top model for frontier research, a decision Howard criticizes as unsafe.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">When AI builds itself \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/news/core-views-on-ai-safety">Core Views on AI Safety: When, Why, What, and How - Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#AI governance`, `#frontier AI`, `#recursive self-improvement`, `#Anthropic`

</details>


<a id="item-14"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">OpenAI acquires Ona to boost Codex with cloud environments</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

OpenAI announced its acquisition of Ona, a startup providing secure, persistent cloud environments, to integrate these capabilities into Codex, enabling long-running AI agents for enterprise workflows. This acquisition positions OpenAI to compete more effectively in enterprise AI automation by enabling Codex to handle complex, long-running tasks that require persistent environments, potentially transforming software development and DevOps workflows. Ona's platform provides isolated development workspaces that combine compute, storage, repositories, and tooling into reproducible setups, which will be integrated into Codex to support autonomous AI agents operating over extended periods.

🔗 [Source](https://openai.com/index/openai-to-acquire-ona)

rss · OpenAI Blog · Jun 11, 00:00

**Background**: Codex is OpenAI's AI coding agent released in April 2025, designed for software engineering tasks like writing code and fixing bugs. It is available via CLI, desktop app, and IDE integrations. Ona specializes in creating secure, long-running cloud environments where autonomous AI agents can operate, which complements Codex's capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/openai-to-acquire-ona/">OpenAI to acquire Ona</a></li>
<li><a href="https://ona.com/docs/ona/environments/overview">Environments - Ona</a></li>
<li><a href="https://en.wikipedia.org/wiki/Codex_(AI_agent)">Codex (AI agent) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Codex`, `#acquisition`, `#enterprise AI`, `#cloud environments`

</details>


<a id="item-15"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">DeltaDB: Versioning Code Between Commits</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Zed introduced DeltaDB, a new version control system that records every individual edit in real time using CRDTs, rather than only tracking changes at the commit level like Git. This approach aims to capture the development process between commits, enabling better collaboration and review by preserving the full history of changes, which could transform how software teams work together. DeltaDB is operation-based and uses CRDTs for incremental synchronization, allowing real-time collaboration and AI integration. Zed raised $32M in Series B funding to develop this system.

🔗 [Source](https://zed.dev/blog/introducing-deltadb)

hackernews · jeremy_k · Jun 11, 16:28 · [Discussion](https://news.ycombinator.com/item?id=48492533)

**Background**: Traditional version control systems like Git track changes at the commit level, which can lose the context of how code evolved between commits. DeltaDB aims to preserve every edit, providing a more detailed history for code review and collaboration.

<details><summary>References</summary>
<ul>
<li><a href="https://shapeof.com/archives/2025/8/deltadb_from_zed.html">DeltaDB From Zed (the Code Editor) - shapeof.com</a></li>
<li><a href="https://hypeburner.com/blog/news/zed-deltadb">Zed Raises $32M in Series B, Pivots to DeltaDB, a GitHub ...</a></li>
<li><a href="https://www.linkedin.com/posts/piyush-katariya-99260138_sequoia-backs-zeds-vision-for-collaborative-activity-7368190499477807104-Hv6q">Introducing DeltaDB: A Real-Time Version Control System</a></li>

</ul>
</details>

**Discussion**: Comments show mixed reactions: some developers worry that preserving messy intermediate work could expose private thinking and clutter history, while others argue that Git already supports frequent auto-commits and rebasing to create clean histories. There is also concern that DeltaDB adds unnecessary complexity.

**Tags**: `#version control`, `#software engineering`, `#collaboration`, `#git`

</details>


<a id="item-16"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Datasette 1.0a33 extends JSON extras to queries and rows</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Datasette 1.0a33 extends the `?_extra=` pattern to queries and rows, providing a consistent JSON API across tables, queries, and rows. The feature is now documented, and an API explorer tool was built using AI-assisted programming. This release is a significant step toward Datasette 1.0 stable, improving API consistency and usability for developers. The documented JSON extras pattern makes Datasette more powerful for data publishing and exploration. The `?_extra=` pattern was originally introduced in Datasette 1.0a3 for tables, and now covers queries and rows. The release also includes a custom extras API explorer built with Claude Fable 5 and GPT-5.5 xhigh.

🔗 [Source](https://simonwillison.net/2026/Jun/11/datasette/#atom-everything)

rss · Simon Willison · Jun 11, 15:26

**Background**: Datasette is an open-source tool for exploring and publishing SQLite-backed datasets. It provides a JSON API for querying data, and the `?_extra=` parameter allows clients to request additional metadata in responses. This release unifies the extras pattern across all API endpoints.

<details><summary>References</summary>
<ul>
<li><a href="http://datasette.io/blog/2026/api-extras/">Datasette 1.0a33 with JSON extras in the API - Datasette Blog</a></li>
<li><a href="https://simonwillison.net/2026/Jun/11/datasette/">Release: datasette 1.0a33 - simonwillison.net</a></li>
<li><a href="https://docs.datasette.io/en/1.0a3/changelog.html">Changelog - Datasette documentation</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#release`, `#json-api`, `#open-source`, `#python`

</details>


<a id="item-17"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">BBVA partners with OpenAI to deploy ChatGPT Enterprise to 100,000 employees</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

BBVA has partnered with OpenAI to deploy ChatGPT Enterprise to 100,000 employees, embedding AI into core banking operations. The bank also joined as a founding partner in OpenAI's new Deployment Company to accelerate enterprise AI transformation. This marks one of the largest enterprise AI deployments in the banking sector, signaling a major shift toward AI-driven banking. It could set a new benchmark for AI adoption in financial services, impacting customer experience, operational efficiency, and competitive dynamics. ChatGPT Enterprise offers enterprise-grade security, privacy, unlimited GPT-4 access, and integration with company data. BBVA's partnership includes participation in OpenAI's Deployment Company, which involves 18 investment firms, consultancies, and system integrators.

🔗 [Source](https://openai.com/index/bbva)

rss · OpenAI Blog · Jun 11, 00:00

**Background**: ChatGPT Enterprise is OpenAI's business-oriented version of ChatGPT, launched in August 2023, designed for organizational use with enhanced security and data analysis capabilities. BBVA is a major Spanish multinational bank with a strong focus on digital transformation. The partnership aims to redefine banking through AI, building on BBVA's existing AI initiatives.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbva.com/en/innovation/bbva-joins-deployco-openais-new-company-to-accelerate-ai-enterprise-transformation/">BBVA joins OpenAI's new company to accelerate AI enterprise ...</a></li>
<li><a href="https://openai.com/index/introducing-chatgpt-enterprise/">Introducing ChatGPT Enterprise - OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#banking`, `#enterprise`, `#OpenAI`, `#ChatGPT`

</details>


<a id="item-18"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">PyTorch Profiling Guide: Fusing MLP Layers for Speed</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A new blog post on Hugging Face provides a detailed guide on profiling and fusing MLP layers in PyTorch, showing how to replace multiple nn.Linear operations with a single fused kernel to improve performance. This optimization technique can significantly reduce kernel launch overhead and memory bandwidth usage, making MLP inference and training faster, especially for large models. It is a practical skill for ML practitioners seeking to improve model efficiency. The guide covers using PyTorch's built-in profiler to identify bottlenecks in MLP layers, then demonstrates how to manually fuse multiple linear layers into a single custom kernel using torch.compile or custom CUDA kernels. It includes code examples and performance benchmarks.

🔗 [Source](https://huggingface.co/blog/torch-mlp-fusion)

rss · Hugging Face Blog · Jun 11, 00:00

**Background**: PyTorch's profiler helps developers identify which operations consume the most time or memory. MLP (Multi-Layer Perceptron) layers often consist of multiple nn.Linear modules, each launching a separate GPU kernel. Fusing these into a single kernel reduces overhead and improves throughput.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html">PyTorch Profiler — PyTorch Tutorials 2.12.0+cu130 documentation</a></li>
<li><a href="https://github.com/Quentin-Anthony/torch-profiling-tutorial">GitHub - Quentin-Anthony/torch-profiling-tutorial</a></li>

</ul>
</details>

**Tags**: `#PyTorch`, `#profiling`, `#MLP`, `#optimization`

</details>


<a id="item-19"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Canadian watchdog accuses xAI's Grok over deepfake safeguards</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Canada's privacy watchdog has accused xAI's Grok AI assistant of violating Canadian privacy laws by lacking adequate safeguards to prevent the creation and sharing of sexualized deepfake images. This case highlights growing global regulatory scrutiny on AI-generated deepfakes, especially those involving non-consensual intimate imagery, and could set a precedent for how AI companies must implement safety measures. The watchdog found that Grok lacks robust content moderation and watermarking mechanisms to prevent misuse, despite xAI's claims of safety features. The investigation is part of broader Canadian efforts to enforce privacy laws on AI platforms.

🔗 [Source](https://www.aljazeera.com/economy/2026/6/11/musks-grok-accused-of-violating-canadian-privacy-laws-on-deepfakes?traffic_source=rss)

rss · Al Jazeera · Jun 11, 18:53

**Background**: Deepfakes are AI-generated media that can convincingly depict people saying or doing things they never did. Sexualized deepfakes, often targeting women without consent, have raised serious ethical and legal concerns. Canada's privacy laws require organizations to implement safeguards against such harms. xAI, founded by Elon Musk, develops the Grok AI assistant, which includes image generation capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cyberdefensemagazine.com/deepfakes-synthetic-media-and-digital-trust-the-cybersecurity-implications-of-deepfake-technology-and-methods-for-detection-and-mitigation/">Deepfakes, Synthetic Media, and Digital Trust: The ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#privacy`, `#deepfakes`, `#regulation`, `#xAI`

</details>


</section>