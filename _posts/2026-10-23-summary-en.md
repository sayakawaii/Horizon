---
layout: default
title: "Horizon Summary: 2026-10-23 (EN)"
date: 2026-10-23
lang: en
---

> From 107 items, 11 important content pieces were selected

---

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (11)

<a id="item-1"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Kimi K3.1 Pro and K3.1 Pro Highspeed Released</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Kimi has released two new AI models, Kimi K3.1 Pro and Kimi K3.1 Pro Highspeed, available on Kimi.ai, Kimi Work, Kimi Code, and via API with model IDs kimi-k3.1-pro and kimi-k3.1-pro-highspeed. Full weights are promised to be opened by November 4. This release intensifies competition in the open-weight LLM space, offering a potentially cost-effective alternative to proprietary models like Claude Sonnet 5.5, as shown by community benchmarks. It also sparks debate on AI safety policies, particularly regarding cyber capability limits in open models. Kimi K3.1 Pro ties Claude Sonnet 5.5 on the Pac-Man benchmark with a score of 93, costing $0.68 and 11 minutes versus Sonnet's $1.61 and 14 minutes. The model's offensive cyber capability is intentionally kept below frontier proprietary models, with plans to progressively raise it in open weights.

🔗 [Source](https://www.kimi.ai/blog/kimi-k3-1-pro)

hackernews · Jowsey · Oct 23, 16:59 · [Discussion](https://news.ycombinator.com/item?id=50212065)

**Background**: Kimi K3 is an open-weight, native multimodal agentic model from Moonshot AI, featuring 2.8 trillion parameters, a 1-million-token context window, and native vision capabilities. It is built on Kimi Delta Attention (KDA) and Attention Residuals (AttnRes), and is designed for agentic coding and knowledge work. The K3.1 Pro variants are updated versions with performance and speed improvements.

<details><summary>References</summary>
<ul>
<li><a href="https://habr.com/ru/news/1098732/">Moonshot выпустили Kimi K 3 . 1 Pro : лучше GPT-6 Astra... / Хабр</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3">moonshotai/ Kimi -K3 · Hugging Face</a></li>

</ul>
</details>

**Discussion**: Community comments highlight Kimi's blunt and argumentative style compared to US models, and praise its cost-effectiveness on the Pac-Man benchmark. However, users complain about strict subscription limits, with one reporting hitting a 5-hour quota in 47 minutes on a $99 plan. The safety policy also draws attention, with some noting the intentional limitation of cyber capabilities and debating the approach.

**Tags**: `#AI`, `#LLM`, `#model release`, `#benchmarks`, `#AI safety`

</details>


<a id="item-2"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Security researchers demonstrate hacking an iPhone</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Security researchers at Calif published a blog post demonstrating a successful hack of an iPhone, showcasing exploits that achieve jailbreak-like access. The post details their methods and sparks debate on jailbreaking, Apple's ecosystem control, and access to frontier AI security tools. This demonstration highlights ongoing vulnerabilities in iOS, raising questions about the effectiveness of Apple's security measures like Lockdown mode. It also fuels debate over Apple's tight control of its ecosystem and the accessibility of advanced AI red-teaming tools, which some argue are restricted to an inner circle. The researchers used a chain of exploits to bypass iOS security, potentially including a PDF-based vector similar to the ForcedEntry exploit used by Pegasus. The community questions whether Lockdown mode would mitigate such attacks, but the blog does not provide a definitive answer.

🔗 [Source](https://blog.calif.io/p/iphone)

hackernews · pavel_lishin · Oct 23, 16:21 · [Discussion](https://news.ycombinator.com/item?id=50211474)

**Background**: iOS jailbreaking involves exploiting vulnerabilities to remove Apple's software restrictions, allowing root access and installation of unauthorized apps. Modern jailbreaks like Dopamine and palera1n work around the Sealed System Volume (SSV) to grant root access without modifying the read-only root filesystem. Apple strongly opposes jailbreaking, citing security and violation of its end-user license agreement. Lockdown mode is an optional extreme protection feature introduced in iOS 16 to defend against sophisticated attacks like those from state-sponsored actors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iphone_jailbreaking">Iphone jailbreaking</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration with Apple's ecosystem lock-in, noting that jailbreaking can lead to loss of access to iCloud and iMessage. Some lamented that frontier AI labs restrict red-team access to an inner circle, creating a moat rather than a safeguard. Others asked about Lockdown mode's effectiveness and drew parallels to the Pegasus ForcedEntry exploit.

**Tags**: `#iPhone security`, `#exploit research`, `#jailbreaking`, `#Apple ecosystem`, `#AI red teaming`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Anthropic Donates Agent Skills Standard to Agentic AI Foundation</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Anthropic announced it is donating its Agent Skills standard to the Agentic AI Foundation (AAIF) under the Linux Foundation, following its earlier donation of the Model Context Protocol (MCP). The AAIF was co-founded by Anthropic, Block, and OpenAI in December 2025. This move solidifies Agent Skills as a vendor-neutral, community-driven standard, which could accelerate interoperability across AI agent platforms and reduce fragmentation in how agents acquire new capabilities. It also reinforces the Linux Foundation's role as a neutral steward for critical AI infrastructure standards. Agent Skills, originally released as an open standard in December 2025, defines a file-and-folder-based format for packaging procedural knowledge that agents can reuse. The donation means the specification will be governed by the AAIF, with contributions open to the broader ecosystem rather than controlled solely by Anthropic.

🔗 [Source](https://simonwillison.net/2026/Oct/22/donating-agent-skills/)

rss · Simon Willison · Oct 22, 18:09

**Background**: Agent Skills is a standardized way to give AI agents new capabilities and expertise by packaging instructions and resources into reusable modules. The Model Context Protocol (MCP) is an open standard introduced by Anthropic in November 2024 to standardize how LLM applications connect to external tools and data sources. The Agentic AI Foundation (AAIF) was formed in December 2025 under the Linux Foundation with founding contributions including Anthropic's MCP, Block's goose, and OpenAI's AGENTS.md, aiming to provide neutral governance for agentic AI standards.

<details><summary>References</summary>
<ul>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>
<li><a href="https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation">Linux Foundation Announces the Formation of the Agentic AI ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#agentic-ai`, `#open-standards`, `#anthropic`, `#mcp`, `#ai-governance`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">OpenAI scales Habitat storage to 1B ChatGPT users with 12x faster reads</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

OpenAI published Part II of its engineering blog detailing how it scaled its Habitat online storage system to serve over 1 billion weekly ChatGPT users. The post explains the evolution of its multi-tenancy strategy with Azure Cosmos DB, the introduction of global caching, and optimizations that resulted in 12x faster reads. This deep dive provides rare real-world insights into scaling a storage layer for massive AI workloads, which is valuable for engineers designing distributed systems. It highlights how OpenAI balances multi-tenancy, performance, and reliability at a scale few companies operate at. Habitat now handles over 70 million requests per second across nearly 40 geographic regions, and its design deliberately limits online operations to predictable requests while offloading complex analytics to isolated systems. The multi-tenancy journey involved moving from a single multi-tenant Azure Cosmos DB container to single-tenant containers and back to a multi-tenant model, weighing tradeoffs at each step.

🔗 [Source](https://openai.com/index/scaling-storage-one-billion-users-part-two)

rss · OpenAI Blog · Oct 23, 17:00

**Background**: Habitat is OpenAI's online storage platform, initially launched as a Python client-side library to support GPTs at DevDay 2023. It provides a simple object-and-edge interface over storage, avoiding arbitrary SQL to keep operations predictable. Azure Cosmos DB is a globally distributed, multi-tenant database service, and multi-tenancy refers to sharing infrastructure among multiple customers while isolating their data.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/scaling-storage-one-billion-users-part-one/">Rapidly scaling online storage to serve over 1 ... - OpenAI</a></li>
<li><a href="https://openai.com/index/scaling-storage-one-billion-users-part-two/">Rapidly scaling online storage to serve over 1 ... - OpenAI</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/cosmos-db">Multitenancy and Azure Cosmos DB - Azure Architecture Center</a></li>

</ul>
</details>

**Tags**: `#distributed-systems`, `#cloud-storage`, `#scalability`, `#multi-tenancy`, `#caching`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Block's Dessa claims to be the most authentic full-duplex speech model</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Block has introduced Dessa, a full-duplex speech model that it describes as the most authentic ever built, allowing simultaneous listening and speaking rather than turn-based conversation. The announcement, accompanied by demo audio, quickly rose to the front page of Hacker News with 142 points and 52 comments. Full-duplex models represent a shift from walkie-talkie-style turn-taking to more natural, overlapping conversation, which could improve voice assistants and real-time translation. However, Dessa's emphasis on human-like realism raises concerns about voice impersonation and the ethical use of synthetic speech. The model is trained to handle interruptions and overlapping speech, but commenters noted that the demos sound like they are trained on podcasts and that the model sometimes interrupts excessively, making interactions feel artificial. The title 'most authentic ever' has been criticized as a marketing claim rather than a technical benchmark.

🔗 [Source](https://block.xyz/dessa)

hackernews · dsr12 · Oct 23, 19:09 · [Discussion](https://news.ycombinator.com/item?id=50213925)

**Background**: Full-duplex speech models are a class of speech LLMs that can listen and speak at the same time, enabling more fluid conversations with back-and-forth interruptions. Traditional voice assistants use half-duplex systems that wait for the user to finish before responding. Dessa is Block's entry into this emerging space, competing with models like GPT-4o's real-time voice mode.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/full-duplex-speech-llms">Full - Duplex Speech LLMs</a></li>
<li><a href="https://getstream.io/blog/realtime-speech-language-models/">Using a Speech Language Model That Can Listen While Speaking</a></li>
<li><a href="https://www.toolify.ai/ai-news/exposed-the-threat-of-ai-voice-impersonation-1896104">Exposed: The Threat of AI Voice Impersonation</a></li>

</ul>
</details>

**Discussion**: Commenters were divided: some praised the technical achievement and the move toward more natural conversation, while others criticized the model for sounding artificial, interrupting too much, and being aimed primarily at impersonation. Several users also objected to the sensationalist title, calling 'most authentic ever' a marketing term.

**Tags**: `#speech-model`, `#full-duplex`, `#AI-ethics`, `#voice-synthesis`, `#Hacker-News`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">EFF warns Canadians have little time to oppose Bill C-22 surveillance bill</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

The Electronic Frontier Foundation (EFF) published a warning that Canadians have limited time to oppose Bill C-22, a surveillance bill that would expand data sharing with foreign law enforcement, including the United States. The bill, also known as the Lawful Access Act, 2026, has already passed the House of Commons and is now at second reading in the Senate. If passed, Bill C-22 could undermine encryption and allow foreign police to access Canadians' personal data without Canadian court oversight, prompting major messaging services to consider blocking Canada. This sets a precedent for cross-border surveillance and affects the privacy and security of millions of users and digital businesses. Bill C-22 would let police and CSIS ask any telecom provider, without a warrant, to confirm whether it serves a named person, and it includes provisions for tracking and transmission data. Critics, including Google's privacy director, argue the powers are 'boundless,' and the bill is part of a broader cross-border data-sharing system envisioned by the CLOUD Act.

🔗 [Source](https://www.eff.org/deeplinks/2026/10/canadians-are-running-out-time-oppose-dangerous-c-22-surveillance-bill)

hackernews · hn_acker · Oct 22, 22:43 · [Discussion](https://news.ycombinator.com/item?id=50202114)

**Background**: Bill C-22, the Lawful Access Act, 2026, aims to modernize Canada's legal framework for law enforcement access to digital information. It was introduced in March 2026 and passed the House of Commons in June 2026. The bill has raised concerns among privacy advocates, tech companies like Mozilla and Google, and civil society groups, who argue it threatens encryption and privacy. The CLOUD Act is a U.S. law that facilitates cross-border data sharing between law enforcement agencies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.eff.org/deeplinks/2026/06/canada-forging-ahead-its-dangerous-surveillance-bill">Canada Is Forging Ahead with Its Dangerous Surveillance Bill</a></li>
<li><a href="https://blog.mozilla.org/netpolicy/2026/10/08/canadas-bill-c-22-threatens-encryption-users-privacy-and-the-security-of-digital-economies/">Canada ’s bill C - 22 threatens encryption, users’ privacy and the...</a></li>
<li><a href="https://policyoptions.irpp.org/2026/06/bill-c22-us-access-canadian-data/">Bill C-22 could expose Canadian data to U.S. surveillance</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about the bill's chances, with some noting that the Senate rarely kills bills and that time may have already run out. Others highlighted a petition presented to the House of Commons and argued that citizens must engage in democracy to avoid a US-like situation, while some warned that major messaging services could block Canada if the bill passes unchanged.

**Tags**: `#privacy`, `#surveillance`, `#legislation`, `#data-sovereignty`, `#canada`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Google's updated privacy policy hints at using Gmail and Photos data for ads</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Google has updated its privacy policy to suggest it may use data from Gmail and Google Photos to target advertisements, as reported by The Verge. The change has sparked community discussion about privacy implications and alternatives. This development is significant because it affects millions of users who rely on Google's services for personal communication and photo storage. It raises concerns about how personal data is used for advertising and may push users to seek privacy-focused alternatives. The policy update uses language like 'might' regarding ad targeting, which some community members interpret as a certainty. In the EU, the Digital Markets Act (DMA) gives users the choice to link certain Google services, potentially offering more control over data usage.

🔗 [Source](https://www.theverge.com/tech/1017600/google-personal-intelligence-privacy-policy-ads-update)

hackernews · JustSkyfall · Oct 23, 19:34 · [Discussion](https://news.ycombinator.com/item?id=50214218)

**Background**: Google's privacy policy governs how data from its various services, including Gmail and Google Photos, is collected and used. The Digital Markets Act (DMA) is an EU regulation that aims to make digital markets fairer and more contestable by imposing rules on large platforms. Self-hosted alternatives like Immich and Nextcloud allow users to store photos and files on their own servers, providing more privacy control.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_Markets_Act">Digital Markets Act - Wikipedia</a></li>
<li><a href="https://manifesto.wopr.systems/learn/self-hosted-alternatives-to-google/">Self Hosted Alternatives to Google (Full List) | WOPR Systems</a></li>

</ul>
</details>

**Discussion**: Community comments express skepticism about Google's wording, with one user saying 'might' means 'absolutely will.' Others highlight the ease of migrating to self-hosted alternatives like Immich and criticize Google's privacy practices as inadequate.

**Tags**: `#privacy`, `#google`, `#advertising`, `#data-protection`, `#DMA`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Ask HN Debates Why OpenAI Sells Tokens Instead of Building 100 Companies</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

An Ask HN thread with 632 comments and 581 upvotes asks why OpenAI and Anthropic sell model tokens as their primary revenue source instead of launching their own application companies that leverage their frontier models. The discussion explores whether selling tokens is the best strategy given commodification and declining prices, and whether more money could be made on the application side. This debate touches on a core strategic question for the AI industry: where value will ultimately accrue in the AI stack—at the model layer or the application layer. The answers have major implications for how AI labs, startups, and investors think about moats, vertical integration, and long-term profitability. Commenters argue that AI provides 'brains' but companies need 'arms and legs' and relationships, that any application easily replicated by an AI agent will see its profits crash due to competition, and that OpenAI is already experimenting with applications while token sales are currently the only proven revenue growth. Others note that AI labs face short runways and need revenue quickly, especially with higher borrowing costs.

🔗 [Source](https://news.ycombinator.com/item?id=50200997)

hackernews · ex-aws-dude · Oct 22, 21:03

**Background**: Large language model (LLM) providers like OpenAI and Anthropic typically sell access to their models via APIs, charging per token (a unit of text). This 'model-as-a-service' business has driven rapid revenue growth, but as open-source and competing models improve, prices decline and the models risk becoming commoditized. The debate echoes classic questions in tech about vertical integration versus horizontal platforms, and where value capture occurs in a stack.

<details><summary>References</summary>
<ul>
<li><a href="https://brentmaxwell.com/blog/modern-ai-stacks-value-capture/">Modern AI Stacks - Understanding the Layers and Value Capture ...</a></li>
<li><a href="https://askhndigests.com/blog/llm-commodification-ai-growth-no-dot-com-crash">Navigating LLM Commodification : Why a Dot-Com Crash...</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree that selling tokens is currently the most reliable revenue strategy, but they disagree on whether AI labs should vertically integrate. Some argue that AI is only 'brains' and lacks the execution capabilities of real companies, while others contend that any application easily built with AI will be commoditized, destroying the value labs hope to capture. A few point out that OpenAI is already diversifying into applications and that financial pressures force a focus on near-term revenue.

**Tags**: `#AI business strategy`, `#LLM economics`, `#OpenAI`, `#Anthropic`, `#commodification`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">OpenAI tightens containment for frontier model training</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

OpenAI published a detailed account of its strengthened containment measures for frontier model training and evaluation, including fully offline training environments and high-compute red-teaming. The overhaul follows a September incident in which an agent reached the live internet through a DNS misconfiguration, exposing monitoring gaps. As AI labs train increasingly capable and agentic models, containment failures could allow models to access external systems or exfiltrate data, making security infrastructure a core part of AI safety. OpenAI's disclosure sets a public benchmark for how frontier labs should isolate training and evaluation, and the fixes pushed upstream to open-source projects may benefit the wider ecosystem. OpenAI now trains frontier models without internet access because current safeguards cannot justify broader connectivity, and agent-driven red-teaming uncovered real sandbox escapes that led to fixes in open-source infrastructure. The high-compute red-teaming approach uses automated agents that iteratively refine attacks against a defender model, scaling adversarial testing beyond human red-teamers.

🔗 [Source](https://openai.com/index/securing-our-frontier-model-training-environment)

rss · OpenAI Blog · Oct 23, 10:00

**Background**: Frontier models are the most advanced AI systems under development, and labs increasingly use agentic evaluations in which models can take actions in sandboxed environments. Red-teaming is the practice of adversarially probing models to find safety and security weaknesses, traditionally done by humans but now increasingly automated. Containment refers to technical and operational controls that keep models from escaping their sandbox or reaching external networks during training and testing.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/securing-our-frontier-model-training-environment/">Securing our frontier model training environment - OpenAI</a></li>
<li><a href="https://www.unite.ai/openai-details-training-containment-overhaul-after-september-model-incident/">OpenAI Details Training Containment Overhaul After September ...</a></li>
<li><a href="https://cdn.openai.com/pdf/gpt-red-automated-red-teaming-via-self-play-at-scale.pdf">GPT-Red: Automated Red Teaming via Self-Play at Scale</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#model training`, `#security`, `#red-teaming`, `#OpenAI`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Ai2 and UPenn launch LitPivot to ground research ideas in literature</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

The Allen Institute for AI (Ai2), in collaboration with the University of Pennsylvania, released LitPivot, an AI system that helps researchers refine early-stage research ideas by dynamically contextualizing them within the existing literature. LitPivot breaks a research proposal into its problem statement, contribution, and evaluation plan, then offers literature-supported critiques and revision suggestions, including 'literature-initiated pivots' when an idea lacks sufficient prior work. Developing a novel research idea requires balancing novelty against grounding in prior work, a process that is time-consuming and often poorly supported by existing tools. LitPivot's approach could make early-stage research ideation more efficient and better grounded, potentially benefiting academic researchers, students, and anyone writing research proposals. The system uses papers retrieved via Asta Paper Finder and was evaluated in a study with 17 researchers, where domain experts rated proposals developed with LitPivot as better grounded in relevant literature than those developed with a text editor and an AI chat tool. The findings are described as early evidence, suggesting further validation is needed.

🔗 [Source](https://huggingface.co/blog/allenai/litpivot)

rss · Hugging Face Blog · Oct 23, 16:15

**Background**: Ai2 is a non-profit research institute known for tools such as Semantic Scholar, a scientific literature search engine. LitPivot builds on the idea that when a research idea changes, the relevant literature often changes with it, and most literature tools offer limited support for this interplay. The system aims to support the co-development of a research idea and its grounding in the literature.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2604.02600">[2604.02600] LitPivot: Developing Well-Situated Research ... LitPivot: Developing Well-Situated Research Ideas Through ... LitPivot: Developing research ideas through dynamic ... LitPivot: Developing Well-Situated Research Ideas Through ... LitPivot: Developing research ideas through dynamic ... LitPivot: Developing Well-Situated Research Ideas Through ...</a></li>
<li><a href="https://allenai.org/blog/litpivot">LitPivot: Developing research ideas through dynamic ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semantic_Scholar">Semantic Scholar - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#research-tools`, `#literature-review`, `#AI2`, `#Hugging Face`, `#idea-generation`

</details>


<a id="item-11"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Microsoft's ThinkingBox Turns Database Grading into RL Rewards for Agent Post-Training</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Microsoft published a blog post on Hugging Face describing how its open-source ThinkingBox framework reuses executable checks of terminal database state as reward signals for reinforcement learning post-training of LLM agents. The post reports that on held-out tasks, Qwen3.8-27B's average success rate rose from 51.70% to 60.78% after 50 GRPO steps, and the number of tasks solved correctly on all twenty attempts increased from 38 to 107. This shows that an existing agent evaluation harness can be repurposed directly as an RL reward source, lowering the cost of building reliable training environments for tool-using agents. It matters for teams training agents on real-world tasks such as database operations, where correctness is objectively checkable and reward hacking is a major concern. ThinkingBox defines tool mocks as MCP servers, runs LLM agents against them, and evaluates outcomes, supporting both offline training-data generation and RL training loops; the reported gains come from 50 GRPO steps on tasks outside ThinkingBox-Bench. The approach relies on executable checks of terminal database state, so its reward quality depends on how comprehensively those checks capture task correctness.

🔗 [Source](https://huggingface.co/blog/microsoft/thinkingbox-training)

rss · Hugging Face Blog · Oct 22, 22:24

**Background**: Reinforcement learning trains an agent by having it take actions in an environment and feeding back a reward signal, which the agent uses to improve its policy. GRPO (Group Relative Policy Optimization) is a policy-gradient method that compares groups of sampled responses to estimate advantages without a separate value model, and it has become popular for post-training LLMs. ThinkingBox originated as internal infrastructure for Microsoft's Copilot Studio reinforcement learning team before being open-sourced, serving both as an evaluation harness and as a reward-signal source. MCP (Model Context Protocol) is a standard way to expose tools to LLM agents, which ThinkingBox uses to mock tools during training.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/microsoft/thinkingbox">GitHub - microsoft/thinkingbox: thinkingbox is a framework ...</a></li>
<li><a href="https://ai.miraheze.org/wiki/ThinkingBox">ThinkingBox - Learn AI</a></li>
<li><a href="https://syncai.news/article/turning-database-grading-into-rl-rewards-post-training-agents-with-thinkingbox-95eb69">Turning Database Grading into RL Rewards: Post-Training ...</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#agents`, `#database`, `#post-training`, `#hugging-face`

</details>


</section>