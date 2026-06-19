---
layout: default
title: "Horizon Summary: 2026-06-19 (EN)"
date: 2026-06-19
lang: en
---

> From 145 items, 14 important content pieces were selected

---

<section class="cat cat-geopolitics" markdown="1">

## 🌐 Geopolitics (1)

<a id="item-1"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Bipartisan Bill Targets Government Coercion of Online Speech</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Senators Ron Wyden and Ted Cruz introduced a bipartisan bill, the JAWBONE Act, to curb government pressure on online platforms to silence lawful speech. The Electronic Frontier Foundation (EFF) praised the bill for addressing this critical issue. This bill could protect lawful online speech from behind-the-scenes government coercion, which has been used to suppress dissent without due process. It addresses a growing concern about government influence on platform content moderation. The bill is named the Justice Against Weaponized Bureaucratic Overreach to Networked Expression (JAWBONE) Act. It aims to prevent federal agencies from pressuring platforms to remove content that is protected under the First Amendment.

🔗 [Source](https://www.eff.org/deeplinks/2026/06/new-bill-takes-aim-government-pressure-silence-lawful-online-speech)

hackernews · hn_acker · Jun 19, 17:34 · [Discussion](https://news.ycombinator.com/item?id=48600950)

**Background**: Governments have increasingly used informal pressure, such as letters and meetings, to push online platforms to remove content, bypassing legal processes. The EFF has fought against such coercion, including representing the creator of ICEBlock, an app for reporting immigration enforcement. This bill seeks to formalize protections against such practices.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/02/platforms-bend-over-backward-to-help-dhs-censor-ice-critics-advocates-say/">Platforms bend over backward to help DHS censor ICE... - Ars Technica</a></li>

</ul>
</details>

**Discussion**: Commenters noted the clever acronym JAWBONE and expressed cautious optimism, with some questioning whether the bill would protect speech they disagree with. Others highlighted the bipartisan nature of the bill, noting that both Cruz and Wyden co-sponsored it, and shared links to related privacy legislation.

**Tags**: `#online speech`, `#government pressure`, `#bipartisan bill`, `#EFF`, `#privacy`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (12)

<a id="item-2"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">Project Valhalla Value Types Arrive in JDK 28</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

Project Valhalla introduces value types to Java, enabling dense memory layouts and performance improvements, with the final design arriving in JDK 28. This represents a decade of work and a paradigm shift in JVM memory management, allowing Java developers to write more efficient and less error-prone code. Value types are reference types that give up identity, allowing the JVM to store values densely in arrays without per-element headers or pointers.

🔗 [Source](https://www.jvm-weekly.com/p/project-valhalla-explained-how-a)

hackernews · philonoist · Jun 19, 06:35 · [Discussion](https://news.ycombinator.com/item?id=48595511)

**Background**: In Java, objects are typically reference types with identity, which leads to memory overhead from headers and pointers. Value types, similar to primitives but user-defined, eliminate this overhead by storing data inline. Project Valhalla has been in development for over a decade to bring this capability to the JVM.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Valhalla_(Java_language)">Project Valhalla ( Java language) - Wikipedia</a></li>
<li><a href="https://practicaldev-herokuapp-com.freetls.fastly.net/adaumircosta/understanding-value-types-project-valhalla-faf">Understanding Value Types ( Project Valhalla ) - DEV Community</a></li>
<li><a href="https://www.baeldung.com/java-valhalla-project">Java Valhalla Project | Baeldung</a></li>

</ul>
</details>

**Discussion**: Comments show mixed sentiment: some appreciate the performance gains but criticize the complexity and null-safety trade-offs, while others defend the design choices and note that Java has evolved significantly.

**Tags**: `#Java`, `#JVM`, `#Project Valhalla`, `#value types`, `#performance`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">GLM-5.2: Top Open-Weights LLM with 753B Parameters</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

Z.ai released GLM-5.2, a 753B-parameter open-weights LLM under MIT license, with a 1M token context window and top benchmark performance. GLM-5.2 is the leading open-weights model on the Artificial Analysis Intelligence Index, surpassing other major open models, and is ranked 2nd on Code Arena WebDev leaderboard, demonstrating that open-source AI can compete with proprietary models. The model uses Mixture of Experts with 40 active parameters out of 753B total, and has a 1.51TB size. It is text-only, with a separate vision model GLM-5V-Turbo not open-weights. Pricing via OpenRouter is $1.40/M input and $4.40/M output.

🔗 [Source](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything)

rss · Simon Willison · Jun 17, 23:58

**Background**: Mixture of Experts (MoE) is an architecture where only a subset of parameters (experts) are activated per token, enabling larger models with lower computational cost. Open-weights models allow anyone to download, modify, and use the model weights, fostering transparency and customization. A 1M token context window enables processing very long documents, such as entire books or codebases, in a single pass.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tensorops.ai/post/what-is-mixture-of-experts-llm">LLM Mixture of Experts Explained</a></li>
<li><a href="https://medium.com/@UjjwalJain_/what-does-a-1-million-token-context-window-actually-change-for-everyday-users-62d94664f2df">What Does a 1 Million Token Context Window Actually... | Medium</a></li>
<li><a href="https://medium.com/@aruna.kolluru/exploring-the-world-of-open-source-and-open-weights-ai-aa09707b69fc">Exploring the World of Open Source and Open Weights AI | Medium</a></li>

</ul>
</details>

**Discussion**: The community is impressed by GLM-5.2's benchmark performance and open license, but notes its high token usage (43k output tokens per task) compared to peers. Some users are excited about the 1M context window, while others express disappointment in the model's SVG generation quality for certain prompts.

**Tags**: `#LLM`, `#open-weights`, `#AI`, `#GLM-5.2`, `#benchmark`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Norway bans AI in elementary schools</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Norway announced a near-ban on AI use in elementary schools, with pupils aged 6-13 generally prohibited from using AI, while those aged 14-16 may use it cautiously under teacher supervision. This policy sets a precedent for AI regulation in education, sparking debate on how to balance AI's potential benefits with the need to preserve foundational learning skills. The ban applies to generative AI tools, with exceptions for supervised use in lower secondary school. The government emphasized that children under 13 need to learn reading, writing, and comprehension without AI assistance.

🔗 [Source](https://www.reuters.com/technology/norway-imposes-near-ban-ai-elementary-school-2026-06-19/)

hackernews · ilreb · Jun 19, 16:03 · [Discussion](https://news.ycombinator.com/item?id=48600093)

**Background**: Generative AI, such as ChatGPT, can produce human-like text and is increasingly used in education. However, concerns have risen that over-reliance on AI may hinder the development of critical thinking and basic skills. Norway's decision reflects a cautious approach similar to earlier debates about calculators in classrooms.

**Discussion**: Commenters largely supported the ban, drawing analogies to not allowing calculators before understanding arithmetic. Some raised concerns about teachers using AI to generate incorrect exercises, while others highlighted the potential of AI as a 1:1 tutor with proper safeguards.

**Tags**: `#AI regulation`, `#education`, `#Norway`, `#policy`, `#generative AI`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">ATProto Has No Instances, Says Dan Abramov</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Dan Abramov published a blog post explaining that ATProto, the protocol behind Bluesky, does not have 'instances' like Mastodon, and instead uses a modular architecture of Personal Data Servers (PDS), Relays, and AppViews. This clarification addresses a common misconception about ATProto's decentralized architecture, helping developers and users understand how it differs from ActivityPub-based systems like Mastodon, which could influence adoption and tooling decisions. Abramov uses an RSS analogy to illustrate the separation of concerns: PDS hosts user data, Relays aggregate firehoses, and AppViews process data for specific applications. He argues that asking 'where are the instances?' is a category error stemming from Mastodon-centric thinking.

🔗 [Source](https://overreacted.io/there-are-no-instances-in-atproto/)

hackernews · danabramov · Jun 19, 15:10 · [Discussion](https://news.ycombinator.com/item?id=48599515)

**Background**: ATProto is the decentralized protocol powering Bluesky, designed to enable portable accounts and interoperable social apps. Unlike Mastodon's instance-based federation, ATProto separates data storage (PDS), data relay, and application logic (AppViews) to avoid fragmentation and enable global aggregation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>
<li><a href="https://atproto.wiki/en/wiki/reference/core-architecture/appview">AppViews | AT Protocol Community Wiki</a></li>
<li><a href="https://atproto.brussels/atproto-architecture">ATProto Architecture • atproto.brussels</a></li>

</ul>
</details>

**Discussion**: Comments on the post debate the accuracy of the RSS analogy, with some arguing that Relays are a critical dependency unlike RSS readers. Others praise the architectural clarity but note that PDS still resembles a client-server model, not fully peer-to-peer.

**Tags**: `#ATProto`, `#decentralization`, `#social media`, `#protocols`, `#architecture`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Hyundai fully acquires Boston Dynamics from SoftBank</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Hyundai Motor Group exercised a put option to buy the remaining stake in Boston Dynamics from SoftBank, completing full ownership of the robotics company for a total valuation of about $1.1 billion. This acquisition positions Hyundai to lead in advanced robotics, potentially integrating Boston Dynamics' humanoid and quadruped robots into manufacturing and logistics, addressing labor shortages and automation needs. Hyundai initially bought an 80% stake in December 2020 for $880 million, valuing Boston Dynamics at $1.1 billion. The remaining 9% stake (after SoftBank retained a small share) was acquired through a put option exercised by SoftBank.

🔗 [Source](https://startupfortune.com/hyundai-takes-full-control-of-boston-dynamics-as-softbank-exits-for-325-million/)

hackernews · ck2 · Jun 19, 16:28 · [Discussion](https://news.ycombinator.com/item?id=48600312)

**Background**: Boston Dynamics is known for advanced robots like Atlas (humanoid) and Spot (quadruped). Hyundai, a major automaker, aims to leverage robotics for manufacturing and mobility. South Korea has the world's highest robot density, with 1,220 robots per 10,000 employees in 2024.

<details><summary>References</summary>
<ul>
<li><a href="https://spectrum.ieee.org/hyundai-buys-boston-dynamics">Hyundai Buys Boston Dynamics for Nearly $1 Billion. - IEEE Spectrum</a></li>
<li><a href="https://en.wikipedia.org/wiki/Atlas_(robot)">Atlas ( robot ) - Wikipedia</a></li>
<li><a href="https://www.hyundaimotorgroup.com/en/story/CONT0000000000001671">[Op-ed] Robots Jump into the Mobility Industry | Hyundai Motor Group</a></li>

</ul>
</details>

**Discussion**: Commenters debated the value of humanoid robots versus purpose-built designs, with some arguing humanoid forms are inefficient for manufacturing. Others linked the acquisition to South Korea's declining working-age population and high robot density, suggesting a strategic move to address labor shortages.

**Tags**: `#robotics`, `#acquisition`, `#Hyundai`, `#Boston Dynamics`, `#manufacturing`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Amateur cracks ancient Linear A script using AI</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

An amateur researcher, Tom Di Mino, used Anthropic's Claude Code to build Python scripts that systematically analyzed the Linear A corpus, resulting in over 300 translated words. The work is currently under academic review by linguistics experts at Rutgers and Cambridge. Linear A has remained undeciphered for over a century, and this is the first credible attempt to translate a substantial portion of the script. If validated, it could unlock Minoan language and culture, and demonstrates how AI tools can assist in complex linguistic research. The total Linear A corpus is only about 7,500 characters spread across 1,500 inscriptions, making it extremely fragmentary. Di Mino's approach used the 'Libation Formula' as a starting point and his translations also solve some problems in Linear B, adding credibility.

🔗 [Source](https://aiclambake.com/clamtakes/linear-a/)

hackernews · Kosturdistan · Jun 19, 16:04 · [Discussion](https://news.ycombinator.com/item?id=48600107)

**Background**: Linear A is a writing system used by the Minoan civilization on Crete from 1800 to 1450 BC. It was rediscovered in 1900 but remains undeciphered, unlike its descendant Linear B which was cracked in the 1950s and found to represent an early form of Greek. The script's small corpus and unknown underlying language have hindered progress.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Linear_A_script">Linear A script</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Discussion**: The community is cautiously optimistic, noting that Di Mino's work is being reviewed by experts and that his approach is methodologically rigorous, using AI to build tools rather than as a black-box solver. Some commenters highlight the extreme difficulty due to the small corpus, but acknowledge that this is the most credible attempt so far.

**Tags**: `#Linear A`, `#AI`, `#linguistics`, `#Claude Code`, `#ancient scripts`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">AI reasoning model helps diagnose rare childhood genetic diseases</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Researchers used an OpenAI reasoning model to identify 18 new diagnoses for rare genetic diseases in children from previously unsolved cases. This demonstrates the practical value of AI reasoning models in healthcare, potentially accelerating diagnosis for rare diseases that often go undiagnosed for years. The model used was OpenAI o1, a reasoning model that spends time 'thinking' before answering, making it better at complex tasks like analyzing clinical and genetic data.

🔗 [Source](https://openai.com/index/diagnose-rare-childhood-diseases)

rss · OpenAI Blog · Jun 18, 08:00

**Background**: Rare genetic diseases affect millions of children worldwide but are difficult to diagnose due to their rarity and diverse symptoms. AI models, especially reasoning models, can analyze large amounts of clinical and genetic data to suggest diagnoses that human physicians might miss. OpenAI's o1 is the first in a series of reasoning models designed to improve performance on complex reasoning tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_o1">OpenAI o1 - Wikipedia</a></li>
<li><a href="https://www.nature.com/articles/d41586-026-00290-9">AI succeeds in diagnosing rare diseases</a></li>

</ul>
</details>

**Tags**: `#AI`, `#healthcare`, `#rare diseases`, `#diagnosis`, `#OpenAI`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">MosaicLeaks: Research Agents Vulnerable to Data Leakage</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

ServiceNow researchers discovered a vulnerability called MosaicLeaks in research agents that can reconstruct sensitive information from mosaic-like data fragments, and proposed mitigation strategies. This vulnerability poses a serious threat to AI agent security, as research agents often handle confidential data; if exploited, it could lead to widespread data breaches. The attack exploits the way research agents aggregate information from multiple sources, allowing an attacker to piece together fragments into complete secrets. The researchers demonstrated the attack on a simulated research agent and provided code for detection.

🔗 [Source](https://huggingface.co/blog/ServiceNow/mosaicleaks)

rss · Hugging Face Blog · Jun 18, 18:13

**Background**: Research agents are AI systems that autonomously gather and synthesize information from various sources, often used for tasks like literature review or data analysis. Data reconstruction attacks are a known class of privacy attacks where an adversary recovers training data from a model's outputs.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/information-technology/2025/09/new-attack-on-chatgpt-research-agent-pilfers-secrets-from-gmail-inboxes/">New attack on ChatGPT research agent pilfers secrets... - Ars Technica</a></li>
<li><a href="https://aisecurityandsafety.org/en/glossary/data-reconstruction-attack/">Data Reconstruction Attack — Definition, Examples & Prevention in AI</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#security`, `#research agents`, `#data leakage`, `#vulnerability`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Beyond LoRA: Exploring Better Fine-Tuning Methods</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Hugging Face published a blog post investigating fine-tuning methods beyond LoRA, comparing their performance and efficiency. The post explores alternatives like (IA)³, Prefix Tuning, and AdaLoRA, providing benchmarks and practical insights. LoRA is the most popular parameter-efficient fine-tuning technique, but alternatives may offer better performance or efficiency for specific tasks. This analysis helps practitioners choose the right method for their use case, potentially improving model adaptation while reducing costs. The blog compares methods like (IA)³, which scales activations, and AdaLoRA, which dynamically allocates rank. It reports that (IA)³ can match LoRA's performance with fewer parameters, while AdaLoRA adapts the rank per layer for better efficiency.

🔗 [Source](https://huggingface.co/blog/peft-beyond-lora)

rss · Hugging Face Blog · Jun 18, 00:00

**Background**: Parameter-efficient fine-tuning (PEFT) methods adapt large pre-trained models by updating only a small fraction of parameters, reducing computational cost. LoRA (Low-Rank Adaptation) is a widely used PEFT technique that injects trainable low-rank matrices into model layers. However, researchers continue to develop new methods that may offer better trade-offs between performance and efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/peft">Parameter-Efficient Fine-Tuning using 🤗 PEFT</a></li>
<li><a href="https://huggingface.co/learn/llm-course/chapter11/4">LoRA (Low-Rank Adaptation) · Hugging Face</a></li>
<li><a href="https://www.ibm.com/think/topics/parameter-efficient-fine-tuning">What is parameter-efficient fine-tuning (PEFT)? | IBM</a></li>

</ul>
</details>

**Tags**: `#fine-tuning`, `#LoRA`, `#PEFT`, `#machine learning`, `#Hugging Face`

</details>


<a id="item-11"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Benchmarking Open Models for Agentic Tasks</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Hugging Face published a guide on benchmarking open-source models for agentic tasks using custom tooling, emphasizing evaluation methodology and reproducibility. This addresses a critical need for standardized evaluation of agentic capabilities in open models, which is essential as agent-based AI systems proliferate. The guide covers how to design benchmarks that measure tool use, multi-step reasoning, and goal-directed behavior, using frameworks like Inspect and agent-eval.

🔗 [Source](https://huggingface.co/blog/is-it-agentic-enough)

rss · Hugging Face Blog · Jun 18, 00:00

**Background**: AI agents are semi- or fully autonomous systems that perceive, reason, and act using tools. Unlike traditional ML models, evaluating agents requires assessing decision-making and environmental interaction, not just accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://galileo.ai/learn/benchmark-ai-agents">How to Benchmark AI Agents Effectively - Galileo AI: The AI Observability and Evaluation Platform</a></li>
<li><a href="https://allenai.org/blog/astabench">AstaBench: Rigorous benchmarking of AI agents with a holistic scientific research suite | Ai2</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#benchmarking`, `#open-source models`, `#tooling`

</details>


<a id="item-12"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Google Workspace Can Block Firefox via Admin Policy</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Google Workspace's context-aware access feature can block Firefox users, but this is an admin-configurable policy, not a Google-wide decision. This highlights the growing use of browser detection in enterprise security, which can inadvertently restrict user choice and raise concerns about browser diversity. The feature is available only in Google Workspace Enterprise editions, not in Business Plus, and is controlled by organization admins via the Admin console.

🔗 [Source](https://tales.fromprod.com/2026/169/google-workspace-threatening-to-block-firefox.html)

hackernews · birdculture · Jun 19, 16:30 · [Discussion](https://news.ycombinator.com/item?id=48600345)

**Background**: Context-aware access is a Google Workspace security feature that allows admins to create granular access policies based on user identity, device security status, location, and other attributes. It is part of a zero-trust security model. Browser detection can be used to enforce policies like requiring Chrome for access.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@heenashree2010/google-workspace-access-management-implementing-context-aware-access-the-right-way-73edfc3bb5b9">Google Workspace Access Management: Implementing... | Medium</a></li>
<li><a href="https://www.portnox.com/cybersecurity-101/context-aware-access/">Context - aware access - Portnox</a></li>

</ul>
</details>

**Discussion**: Commenters clarified that the blocking is due to admin-configured context-aware access policies, not a Google decision. The blog author confirmed they are not using IAP and are on Business Plus, so the block likely comes from a different security mechanism. Some criticized browser detection over feature detection.

**Tags**: `#Google Workspace`, `#Firefox`, `#browser detection`, `#enterprise security`, `#context-aware access`

</details>


<a id="item-13"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Datasette Apps: Host Custom HTML Apps Inside Datasette</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

The datasette-apps plugin allows users to host sandboxed HTML+JavaScript applications inside Datasette that can execute read-only and configured write SQL queries against the underlying data. This plugin significantly expands Datasette's capabilities by enabling custom interactive applications directly within the platform, making it a more versatile tool for data exploration and presentation. Apps run in a constrained <iframe sandbox="allow-scripts allow-forms"> with an injected CSP header that prevents HTTP requests to external hosts, blocking data exfiltration. The plugin registers permissions for create, view, edit, delete, and manage app access.

🔗 [Source](https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything)

rss · Simon Willison · Jun 18, 23:58

**Background**: Datasette is an open-source tool for exploring and publishing data, providing a JSON API for custom frontends. The datasette-apps plugin builds on this by allowing users to embed custom HTML/JS apps that interact with the API directly, without needing a separate server.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/18/datasette-apps/">Datasette Apps : Host custom HTML applications inside Datasette</a></li>
<li><a href="https://pypi.org/project/datasette-apps/">Create apps that live inside Datasette</a></li>
<li><a href="https://docs.datasette.io/en/0.43/plugins.html">Plugins — Datasette documentation</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#plugin`, `#web-applications`, `#sql`, `#sandbox`

</details>


</section>

<section class="cat cat-other" markdown="1">

## 📌 Other (1)

<a id="item-14"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">EFF Argues Court Records Should Be Free</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

The Electronic Frontier Foundation (EFF) published an article arguing that court records should be free and accessible, criticizing the current PACER fee system. The article highlights the Open Courts Act, a legislative proposal to replace aging PACER and CM/ECF systems with a modern, unified platform. Public access to court records is fundamental to transparency and justice, but current fees create a barrier. If the Open Courts Act passes, it could significantly reduce costs and improve access for researchers, journalists, and the public. The Open Courts Act would replace the aging PACER and CM/ECF systems with a modern, unified platform designed to improve public access, strengthen cybersecurity, and reduce long-term costs. Currently, PACER charges fees per page, though exemptions exist for indigents, pro bono attorneys, academic researchers, and non-profit organizations.

🔗 [Source](https://www.eff.org/deeplinks/2026/06/court-records-should-be-free)

hackernews · hn_acker · Jun 19, 17:34 · [Discussion](https://news.ycombinator.com/item?id=48600946)

**Background**: PACER (Public Access to Court Electronic Records) is an electronic public access service for United States federal court documents, charging users per page. The EFF has long advocated for free access to court records, arguing that the public already pays for the judicial system through taxes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PACER_(law)">PACER (law) - Wikipedia</a></li>
<li><a href="https://pacer.uscourts.gov/pacer-pricing-how-fees-work">PACER Pricing: How fees work | PACER : Federal Court Records</a></li>
<li><a href="https://free.law/pacer-facts">Facts About PACER and CM/ECF | Free Law Project | Making the legal...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed support for free court records, with one highlighting CourtListener and the Recap program as practical solutions that automatically share purchased PACER documents. Another commenter noted that courts serve the public and it makes no sense to pay twice.

**Tags**: `#legal`, `#public access`, `#EFF`, `#PACER`, `#open data`

</details>


</section>