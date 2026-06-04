---
layout: default
title: "Horizon Summary: 2026-06-04 (EN)"
date: 2026-06-04
lang: en
---

> From 123 items, 13 important content pieces were selected

---

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (13)

<a id="item-1"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">Meta ships facial recognition on smart glasses</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

Meta has quietly embedded a complete face-recognition pipeline in the companion app for its Ray-Ban Meta smart glasses, including three ExecuTorch models for face detection and recognition. The feature is currently dormant but could be activated at any time, raising significant privacy and legal concerns. This marks a major step toward ubiquitous facial recognition on wearable devices, reigniting debates about privacy, consent, and surveillance. If activated, it could enable real-time identification of strangers without their knowledge, potentially violating biometric privacy laws like Illinois' BIPA. The three models are based on open-source architectures: SCRFD for face detection and SFace for face recognition, both from the InsightFace project. The models are delivered via Meta's NMLML asset-delivery system and are currently dormant on the device.

🔗 [Source](https://www.buchodi.com/meta-glasses-facial-recognition/)

hackernews · buchodi · Jun 4, 19:36 · [Discussion](https://news.ycombinator.com/item?id=48403588)

**Background**: Facial recognition technology identifies or verifies a person from an image or video. Wearable devices like smart glasses raise unique privacy risks because they can record surreptitiously. Laws such as Illinois' Biometric Information Privacy Act (BIPA) require explicit consent before collecting biometric data, and similar regulations exist under GDPR and CCPA.

<details><summary>References</summary>
<ul>
<li><a href="https://www.buchodi.com/meta-glasses-facial-recognition/">Meta's smart glasses companion app ships a complete, dormant face-recognition pipeline on a stock account.</a></li>
<li><a href="https://www.nytimes.com/2026/02/13/technology/meta-facial-recognition-smart-glasses.html">Meta Plans to Add Facial Recognition Technology to Its Smart Glasses - The New York Times</a></li>
<li><a href="https://www.biometricupdate.com/202606/iflytek-launches-ai-glasses-as-privacy-concerns-grow-over-wearable-cameras">iFlytek launches AI glasses as privacy concerns grow over wearable cameras | Biometric Update</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong concerns: one noted that Google Glass terms explicitly forbade such use, while another wished for an offline version to aid face blindness without sacrificing privacy. Others suggested countermeasures like IR LEDs to disrupt facial recognition or a notification system to alert when someone is using such glasses.

**Tags**: `#facial recognition`, `#privacy`, `#wearables`, `#ethics`, `#AI`

</details>


<a id="item-2"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Anthropic open-sources AI framework for vulnerability discovery</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Anthropic released an open-source framework that uses AI agents to automatically discover software vulnerabilities, hosted on GitHub under the name 'defending-code-reference-harness'. This framework lowers the barrier for security researchers to apply AI in vulnerability discovery, potentially accelerating the identification of critical flaws in open-source software. The framework supports parallel agents with estimated costs ranging from hundreds to thousands of dollars depending on the model used (e.g., Opus or Mythos). It is part of Anthropic's Project Glasswing, which commits up to $100M in usage credits for Mythos Preview.

🔗 [Source](https://github.com/anthropics/defending-code-reference-harness)

hackernews · binyu · Jun 4, 20:11 · [Discussion](https://news.ycombinator.com/item?id=48403980)

**Background**: AI-powered vulnerability discovery uses large language models to analyze code and find security weaknesses. Anthropic's Model Context Protocol (MCP) is an open standard for integrating AI with external tools, which may underpin this framework. The approach is part of a broader trend where AI systems can discover vulnerabilities in minutes to hours, changing the economics of security research.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments highlight practical concerns: tptacek compares the framework to a 'shop jig' that researchers can customize, simonw questions the cost (hundreds to thousands of dollars), and pizlonator doubts that AI has produced breakthroughs beyond itself. Some users share alternative tools like 'vulture' and note better results with NVIDIA-hosted models.

**Tags**: `#AI`, `#security`, `#vulnerability discovery`, `#open-source`, `#Anthropic`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Cloudflare Acquires VoidZero, Creator of Vite</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Cloudflare has acquired VoidZero, the company behind the popular JavaScript build tool Vite, and committed $1 million to an open source fund. This acquisition could influence the future direction of Vite, a critical tool in the JavaScript ecosystem, and signals Cloudflare's intent to deepen its developer platform and AI-native web strategy. VoidZero is an open-source-first company that develops the Vite toolchain. Cloudflare plans to keep Vite open source and has set up a $1 million fund to support the broader open source community.

🔗 [Source](https://blog.cloudflare.com/voidzero-joins-cloudflare/)

hackernews · coloneltcb · Jun 4, 13:00 · [Discussion](https://news.ycombinator.com/item?id=48398055)

**Background**: Vite is a modern frontend build tool that provides fast development server startup and hot module replacement using native ES modules. It has become widely adopted in the JavaScript ecosystem, especially with frameworks like Vue.js and React. Cloudflare is a major cloud connectivity company that offers CDN, security, and edge computing services.

<details><summary>References</summary>
<ul>
<li><a href="https://www.businesswire.com/news/home/20260604108073/en/Cloudflare-Acquires-VoidZero-to-Build-the-Future-of-the-AI-Native-Web">Cloudflare Acquires VoidZero to Build the Future of the AI-Native Web</a></li>
<li><a href="https://www.investing.com/news/company-news/cloudflare-acquires-voidzero-commits-1m-to-open-source-fund-93CH-4726787">Cloudflare acquires VoidZero, commits $1M to open source fund By Investing.com</a></li>
<li><a href="https://vite.dev/">Vite | Next Generation Frontend Tooling</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed feelings: some worry about the long-term independence of Vite under Cloudflare, while others see it as a positive step for funding. Skepticism about Cloudflare's developer experience and the 'acqui-hire' business model is also noted.

**Tags**: `#acquisition`, `#Vite`, `#Cloudflare`, `#open-source`, `#JavaScript`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Huawei's KVarN: Native vLLM Backend for KV-Cache Quantization</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Huawei has released KVarN, a native vLLM backend for KV-cache quantization that claims better performance than TQ and better quality than FP16. KVarN could significantly improve LLM inference efficiency by reducing memory usage while maintaining high quality, potentially enabling longer context windows and higher throughput. KVarN is a variance-normalized KV-cache quantization method designed for autoregressive decoding, addressing cumulative quantization errors that occur in long-horizon decoding.

🔗 [Source](https://github.com/huawei-csl/KVarN)

hackernews · theanonymousone · Jun 4, 15:18 · [Discussion](https://news.ycombinator.com/item?id=48399974)

**Background**: KV-cache stores key and value tensors during LLM inference to avoid recomputation, but it grows with sequence length and becomes a memory bottleneck. Quantizing the cache to lower precision (e.g., FP8) reduces memory usage but can degrade quality. vLLM is a popular inference engine that supports various backends for efficient attention computation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.03458">[2606.03458] KVarN: Variance-Normalized KV-Cache Quantization ...</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/">Quantized KV Cache - vLLM</a></li>

</ul>
</details>

**Discussion**: Community comments express surprise at the claimed performance-quality tradeoff, with one user asking if they read correctly that KVarN outperforms TQ in performance and FP16 in quality. Another user questions why KVarN is not submitted as a PR to vLLM.

**Tags**: `#LLM`, `#quantization`, `#vLLM`, `#inference`, `#KV-cache`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">OpenAI Proposes AI Biodefense Action Plan</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

OpenAI published a policy blueprint titled 'Biodefense in the Intelligence Age,' outlining a federal framework for using frontier AI to enhance biological resilience and national security. This proposal addresses the critical intersection of AI and biodefense, aiming to mitigate risks of AI-enabled biological threats while leveraging AI for early detection and response, which could shape future U.S. governance of frontier AI. The blueprint includes measures such as preparedness evaluations, bio-specific capability assessments, safer model behavior for dual-use biological requests, expert red teaming, and security controls for higher-risk capabilities.

🔗 [Source](https://openai.com/index/biodefense-in-the-intelligence-age)

rss · OpenAI Blog · Jun 4, 00:00

**Background**: Frontier AI models are the most advanced general-purpose AI systems, capable of reasoning, multimodal generation, and agentic workflows. As these models become more capable in biology, there is growing concern about their potential misuse for developing biological weapons. OpenAI's approach focuses on layered resilience, combining safeguards with proactive biodefense investments.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/strengthening-societal-resilience-with-rosalind-biodefense/">Strengthening societal resilience with Rosalind Biodefense | OpenAI</a></li>
<li><a href="https://www.iguazio.com/glossary/frontier-model/">What is a Frontier Model?</a></li>

</ul>
</details>

**Tags**: `#AI`, `#biodefense`, `#policy`, `#security`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">OpenAI unveils new GPT-Rosalind capabilities for life sciences</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

OpenAI announced new capabilities for GPT-Rosalind, its frontier reasoning model for life sciences, enhancing biological reasoning, medicinal chemistry, genomics analysis, and experimental workflow support. This advancement could accelerate drug discovery, protein engineering, and genomics research by providing researchers with a specialized AI tool that understands complex biological data and workflows. GPT-Rosalind is optimized for scientific workflows with improved tool use and deeper understanding across chemistry, protein engineering, and genomics. The model builds on OpenAI's reasoning technology to support biology, drug discovery, and translational medicine.

🔗 [Source](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind)

rss · OpenAI Blog · Jun 3, 13:15

**Background**: GPT-Rosalind is a specialized AI model from OpenAI designed for life sciences research, named after Rosalind Franklin. It combines large language model capabilities with domain-specific knowledge in biology and chemistry to assist researchers in tasks such as protein structure prediction, drug molecule design, and genomic data analysis.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-rosalind/">Introducing GPT-Rosalind for life sciences research | OpenAI</a></li>
<li><a href="https://www.publicnow.com/view/188B53216336E8A3B4383708BFDB112B1FE51C34">OpenAI Inc. (via Public) / Introducing GPT-Rosalind for life ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#life sciences`, `#genomics`, `#OpenAI`, `#research`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">DPO Beyond Chatbots: New Frontiers in AI Alignment</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A Hugging Face blog post explores applying Direct Preference Optimization (DPO) beyond chatbots to broader AI alignment tasks, demonstrating its versatility in non-conversational domains. This extension shows DPO can replace RLHF in diverse alignment scenarios, potentially simplifying and scaling AI safety research beyond language models. DPO directly optimizes a language model using preference pairs without a separate reward model or reinforcement learning loop, making it simpler and more efficient than RLHF.

🔗 [Source](https://huggingface.co/blog/Dharma-AI/direct-preference-optimization-beyond-chatbots)

rss · Hugging Face Blog · Jun 3, 12:55

**Background**: Direct Preference Optimization (DPO) is an alignment technique that aligns AI behavior with human preferences by directly optimizing on chosen vs. rejected response pairs. It emerged as a simpler alternative to Reinforcement Learning from Human Feedback (RLHF), which requires training a separate reward model and running a policy optimization loop. DPO has been widely adopted in open-source LLM pipelines.

<details><summary>References</summary>
<ul>
<li><a href="https://www.taskade.com/wiki/ai/dpo">DPO : The Simpler RLHF That Took Over Alignment (2026) | Taskade AI</a></li>
<li><a href="https://sebastianraschka.com/faq/docs/rlhf-vs-dpo.html">How is RLHF different from DPO at a high... | Sebastian Raschka, PhD</a></li>
<li><a href="https://arbisoft.com/blogs/rlhf-vs-dpo-a-closer-look-into-the-process-and-methodology">RLHF vs DPO : A Closer Look into the Process and Methodology</a></li>

</ul>
</details>

**Tags**: `#DPO`, `#RLHF`, `#AI alignment`, `#preference optimization`, `#Hugging Face`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Gaussian Point Splatting: A New Rendering Method</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Gaussian Point Splatting is a novel rendering technique that samples pixel-sized opaque points from 3D Gaussians and splats them using 64-bit atomics, enabling efficient rendering of scenes with many Gaussians. This method could influence future game graphics by offering a scalable alternative to traditional polygon rendering, potentially enabling more detailed and dynamic scenes. The technique is stochastic and scales extremely well to large numbers of Gaussians, using 64-bit atomics for splatting. It draws comparisons to Ecstatica's ellipsoid rendering from 1994.

🔗 [Source](https://momentsingraphics.de/Siggraph2026.html)

hackernews · ibobev · Jun 4, 10:48 · [Discussion](https://news.ycombinator.com/item?id=48396792)

**Background**: Gaussian splatting is a recent rendering method that represents scenes with 3D Gaussians, enabling real-time radiance field rendering. Traditional point splatting from the 1990s used opaque points, but Gaussian splatting uses anisotropic Gaussians for better quality. Gaussian Point Splatting combines ideas from both, using opaque points sampled from Gaussians.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_splatting">Gaussian splatting - Wikipedia</a></li>
<li><a href="https://github.com/graphdeco-inria/gaussian-splatting">GitHub - graphdeco-inria/gaussian-splatting: Original reference implementation of "3D Gaussian Splatting for Real-Time Radiance Field Rendering" · GitHub</a></li>
<li><a href="https://momentsingraphics.de/Siggraph2026.html">Gaussian Point Splatting</a></li>

</ul>
</details>

**Discussion**: Commenters expressed interest in seeing AAA games adopt such methods, with one drawing a historical parallel to Ecstatica's ellipsoid rendering. Another user noted the difficulty in finding tutorials for classic point splatting due to Gaussian Splatting dominating search results.

**Tags**: `#computer graphics`, `#rendering`, `#gaussian splatting`, `#game development`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Google Asks 404 Media to Remove 'Humans in the Loop' Pledge</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Google asked 404 Media to revise a statement that originally said it's critical to maintain humans in the loop for AI, removing that commitment after employees internally shared memes about the company's AI quality issues. This reveals Google's internal acknowledgment of AI quality problems and a concerning retreat from human oversight, raising questions about AI ethics and transparency in the industry. The original statement emphasized the importance of keeping humans in the loop, but after the story was published, Google's spokesperson requested a version that omitted that phrase. The change was reported by 404 Media based on internal employee memes mocking Google's AI.

🔗 [Source](https://simonwillison.net/2026/Jun/4/a-slightly-different-version/#atom-everything)

rss · Simon Willison · Jun 4, 16:38

**Background**: Human-in-the-loop (HITL) is a practice where human feedback is used to improve AI models and serve as a safeguard when AI systems perform poorly. It is widely considered a key principle for responsible AI development. Google's removal of this commitment signals a potential shift away from that principle.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Human-in-the-loop">Human-in-the-loop - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/human-in-the-loop">What Is Human In The Loop (HITL)? | IBM</a></li>

</ul>
</details>

**Tags**: `#ai-ethics`, `#google`, `#ai`, `#journalism`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Uber Caps AI Coding Tool Usage at $1,500 per Month</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Uber has capped employee monthly token spending on agentic AI coding tools like Claude Code and Cursor at $1,500 per tool, after blowing its entire 2026 AI budget in just four months due to unexpectedly high usage. This is one of the first major real-world examples of a large enterprise grappling with the cost of agentic AI coding tools, setting a precedent for how other companies may manage AI spending. It also highlights the tension between AI productivity gains and the unpredictable token costs that come with them. The $1,500 cap applies per tool, meaning an engineer using both Claude Code and Cursor could spend up to $3,000 per month. The cap is roughly 11% of the median software engineer compensation at Uber ($330,000 per year).

🔗 [Source](https://simonwillison.net/2026/Jun/3/uber-caps-usage/#atom-everything)

rss · Simon Willison · Jun 3, 12:01

**Background**: Agentic coding tools like Claude Code and Cursor are AI systems that can read codebases, edit files, run commands, and even commit code autonomously. They consume tokens (units of AI computation) that are priced by providers like Anthropic and OpenAI. Uber's budget was set in 2025, before the explosive popularity of these tools was fully anticipated.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zerohedge.com/ai/uber-introduces-1500-monthly-cap-ai-coding-tools-after-budget-blowout">Uber Introduces $1,500 Monthly Cap On AI Coding Tools ... | ZeroHedge</a></li>
<li><a href="https://www.businessinsider.com/tokenmaxxing-ai-token-leaderboards-debate-2026-4">'Tokenmaxxing' Is the New Silicon Valley AI Debate - Business Insider</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cost management`, `#enterprise`, `#coding agents`, `#Uber`

</details>


<a id="item-11"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">NVIDIA Nemotron 3.5: Customizable Multimodal Safety for Enterprise AI</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

NVIDIA released Nemotron 3.5 Content Safety, a compact 4B-parameter multimodal guardrail model fine-tuned from Google Gemma-3-4B, which can evaluate the safety of text and image inputs and outputs for LLMs and VLMs. This model addresses a critical need for customizable, multimodal safety in enterprise AI deployments, enabling organizations to enforce content policies across text and images with low latency. The model is built on the Gemma-3-4B backbone with an adapter-based classification head, and it accepts a prompt, an optional image, and an optional response as input, returning a safety classification.

🔗 [Source](https://huggingface.co/blog/nvidia/nemotron-3-5-content-safety)

rss · Hugging Face Blog · Jun 4, 18:57

**Background**: AI safety models are used to detect and filter unsafe content such as hate speech, violence, or sensitive information. Previous models like Nemotron 8B focused only on text for LLMs, while Nemotron 3.5 extends to multimodal inputs (text and images) for both LLMs and VLMs, making it suitable for modern AI applications that process multiple modalities.

<details><summary>References</summary>
<ul>
<li><a href="https://build.nvidia.com/nvidia/nemotron-3.5-content-safety/modelcard">nemotron - 3 . 5 - content - safety Model by NVIDIA | NVIDIA NIM</a></li>
<li><a href="https://openrouter.ai/nvidia/nemotron-3.5-content-safety:free/api">NVIDIA: Nemotron 3 . 5 Content Safety (free) – API Quickstart</a></li>
<li><a href="https://developer.nvidia.com/blog/building-nvidia-nemotron-3-agents-for-reasoning-multimodal-rag-voice-and-safety/">Building NVIDIA Nemotron 3 Agents for Reasoning, Multimodal RAG, Voice, and Safety | NVIDIA Technical Blog</a></li>

</ul>
</details>

**Tags**: `#AI Safety`, `#Multimodal`, `#Enterprise AI`, `#NVIDIA`, `#Content Moderation`

</details>


<a id="item-12"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">EVA-Bench Data 2.0: 121 Tools, 213 Scenarios</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

ServiceNow AI released EVA-Bench Data 2.0, an expanded benchmark for evaluating LLMs' tool-use capabilities across three domains (e.g., enterprise, productivity, and coding) with 121 tools and 213 scenarios. This benchmark provides a more comprehensive and realistic evaluation of LLMs' ability to use external tools, which is critical for building reliable AI agents in real-world applications. The benchmark covers three domains: enterprise, productivity, and coding, with 121 tools and 213 scenarios. It is designed to test LLMs on multi-step tool use, state dependency, and error handling.

🔗 [Source](https://huggingface.co/blog/ServiceNow-AI/eva-bench-data)

rss · Hugging Face Blog · Jun 4, 12:24

**Background**: LLMs are increasingly used as agents that can call external tools (e.g., APIs, databases) to perform tasks. Benchmarks like EVA-Bench are essential to measure and compare how well different models handle tool use, which is a key capability for autonomous AI systems.

**Tags**: `#LLM`, `#benchmark`, `#tool-use`, `#AI evaluation`

</details>


<a id="item-13"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Hugging Face launches agent-optimized CLI for Hub</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Hugging Face announced a new CLI tool, hf, designed specifically for AI agents to interact with the Hugging Face Hub efficiently. The tool provides structured outputs and agent-friendly commands to streamline workflows. This addresses a growing need for AI agents to programmatically access the Hub, enabling automated model management, dataset operations, and deployment tasks. It positions Hugging Face as a key infrastructure provider for the agentic AI ecosystem. The hf CLI is built on the existing huggingface_hub Python package and uses Typer for command structure. It includes commands for authentication, repository management, file upload/download, and is optimized for agent consumption with structured output flags.

🔗 [Source](https://huggingface.co/blog/hf-cli-for-agents)

rss · Hugging Face Blog · Jun 4, 00:00

**Background**: The Hugging Face Hub is a central platform for hosting models, datasets, and spaces. The existing CLI (huggingface_hub) was primarily designed for human use. With the rise of AI coding agents and automated workflows, there is a need for CLIs that return machine-parseable output and support headless operation.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/docs/huggingface_hub/guides/cli">Command Line Interface (CLI) · Hugging Face</a></li>
<li><a href="https://github.com/huggingface/huggingface_hub/blob/main/docs/source/en/guides/cli.md">huggingface_hub/docs/source/en/guides/cli.md at main ... - GitHub</a></li>
<li><a href="https://deepwiki.com/huggingface/huggingface_hub/7-command-line-interface">Command Line Interface | huggingface/huggingface_hub | DeepWiki</a></li>

</ul>
</details>

**Tags**: `#CLI`, `#AI agents`, `#Hugging Face`, `#MLOps`, `#tooling`

</details>


</section>