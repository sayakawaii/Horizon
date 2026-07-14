---
layout: default
title: "Horizon Summary: 2026-07-14 (EN)"
date: 2026-07-14
lang: en
---

> From 179 items, 34 important content pieces were selected

---

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (10)

<a id="item-1"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Bonsai 27B: 27B-Parameter Model Runs on Phones via Compression</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

PrismML released Bonsai 27B, a 27-billion-parameter model compressed to run on mobile devices, achieving 95% retention of full-precision performance in its ternary version and 90% in its 1-bit version. This breakthrough enables large language models to run locally on phones, reducing reliance on cloud inference and improving privacy and latency, potentially transforming mobile AI applications. The model uses aggressive quantization with effective bits per weight as low as 1.125, achieving a ~14.2x reduction vs FP16, and supports a 262K-token context with speculative decoding for speed.

🔗 [Source](https://prismml.com/news/bonsai-27b)

hackernews · xenova · Jul 14, 17:50 · [Discussion](https://news.ycombinator.com/item?id=48910545)

**Background**: Quantization reduces the precision of model weights to decrease memory footprint and computational cost, enabling large models to run on resource-constrained devices like phones. Traditional quantization below 4 bits often causes significant performance loss, but Bonsai 27B's method retains high accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://prismml.com/news/bonsai-27b">PrismML — Announcing Bonsai 27B: The First 27B-Class Model to Run on a Phone</a></li>
<li><a href="https://huggingface.co/prism-ml/Bonsai-27B-gguf">prism-ml/Bonsai-27B-gguf · Hugging Face</a></li>
<li><a href="https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf">prism-ml/Ternary-Bonsai-27B-gguf · Hugging Face</a></li>

</ul>
</details>

**Discussion**: Community members compared Bonsai 27B to Gemma 4 12B and Qwen models, noting concerns about tool-calling performance and factual accuracy in demos. Some praised the compression achievement but questioned practical utility.

**Tags**: `#quantization`, `#edge AI`, `#LLM`, `#mobile deployment`, `#model compression`

</details>


<a id="item-2"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Cursor IDE 0-Day: Full Disclosure After 6 Months Unpatched</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A critical 0-day vulnerability in Cursor IDE allows arbitrary code execution via malicious executables named git.exe in the project folder, and remains unpatched over six months after responsible disclosure by Mindgard. This incident highlights a failure in responsible disclosure, as the vendor ignored repeated reports, forcing public full disclosure as the only remaining protection for users. The vulnerability exploits Windows' behavior of searching the current working directory for executables before PATH; Cursor runs git.exe without prompting, enabling silent code execution. Mindgard reported the issue on December 15, 2025, but it was initially dismissed as out of scope.

🔗 [Source](https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left)

hackernews · Synthetic7346 · Jul 14, 17:58 · [Discussion](https://news.ycombinator.com/item?id=48910676)

**Background**: Cursor is a popular AI-powered code editor based on VS Code. Responsible disclosure is a process where security researchers privately report vulnerabilities to vendors, giving them time to fix before public disclosure. When vendors fail to respond, researchers may resort to full disclosure to warn users.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.checkpoint.com/research/cursor-ide-persistent-code-execution-via-mcp-trust-bypass/">Critical RCE Vulnerability in Cursor IDE Exposed</a></li>
<li><a href="https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure">Coordinated vulnerability disclosure - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Some commenters argue the vulnerability is minor because it requires a malicious executable already on the system, comparing it to replacing .bashrc. Others criticize Cursor for running executables without prompting and for ignoring the report, while noting that ACL prompts might mitigate the attack.

**Tags**: `#security`, `#vulnerability`, `#cursor`, `#responsible disclosure`, `#IDE`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Are we offloading too much thinking to AI?</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

An article on Artfish.ai explores the risks of over-relying on AI for cognitive tasks, warning that it may erode deep understanding and critical thinking skills. The piece sparked a discussion with diverse perspectives from readers. As AI tools become ubiquitous in software engineering, education, and daily life, this debate highlights a fundamental tension between productivity gains and the preservation of human expertise. The outcome could shape how professionals and educators approach AI integration. The article's framing is questioned by some commenters who argue that 'too much' is subjective and that AI can unlock potential, similar to calculators. However, a junior developer example shows blind reliance leading to inability to explain AI-generated code.

🔗 [Source](https://www.artfish.ai/p/offloading-thinking-to-ai)

hackernews · yenniejun111 · Jul 14, 15:18 · [Discussion](https://news.ycombinator.com/item?id=48908178)

**Background**: Large language models (LLMs) like GPT-4 are increasingly used for tasks ranging from coding to relationship advice. Critics worry that offloading thinking to AI may atrophy cognitive skills, while proponents see it as a tool for efficiency. The calculator analogy is often invoked, but the debate centers on whether AI replaces thinking or augments it.

**Discussion**: Commenters express mixed views: some argue that heavy AI users are still in control, while others share anecdotes of juniors unable to explain AI-generated code. A few note that most people don't truly 'think' anyway, and AI may just be a new pattern source.

**Tags**: `#AI`, `#cognition`, `#software engineering`, `#education`, `#critical thinking`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Linux Input Latency Measured: X11 vs Wayland, VRR, DXVK</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A detailed benchmark measured input latency on Linux comparing X11, Wayland, VRR, and DXVK, finding native Wayland and X11 are tied at ~7 ms, while XWayland roughly doubles latency. This provides empirical data to settle the long-standing debate over input latency differences between Linux display servers, helping gamers and developers optimize their setups. The test used a 500 Hz display, which may mask issues visible at lower refresh rates; the XWayland result showed 3 ms higher latency, potentially a full frame behind at high refresh rates.

🔗 [Source](https://marco-nett.de/blog/measuring-input-latency-on-linux-x11-vs-wayland-vrr-dxvk/)

hackernews · hoechst · Jul 14, 16:36 · [Discussion](https://news.ycombinator.com/item?id=48909424)

**Background**: X11 and Wayland are display server protocols on Linux; Wayland is newer and aims to be simpler and more secure. DXVK translates Direct3D calls to Vulkan, enabling Windows games on Linux. VRR (Variable Refresh Rate) synchronizes display refresh with frame output to reduce tearing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DXVK">DXVK</a></li>
<li><a href="https://en.wikipedia.org/wiki/Variable_refresh_rate">Variable refresh rate - Wikipedia</a></li>
<li><a href="https://www.reddit.com/r/linux/comments/1iajb1o/hard_numbers_in_the_wayland_vs_x11_input_latency/">r/linux on Reddit: Hard numbers in the Wayland vs X11 input latency discussion</a></li>

</ul>
</details>

**Discussion**: Commenters praised the empirical approach, noting that XWayland latency explains why some users perceive Wayland as slow. Others pointed out the 500 Hz display may hide issues, and suggested testing at 60/120 Hz. Some expressed hope that results will drive ecosystem improvements.

**Tags**: `#Linux`, `#input latency`, `#Wayland`, `#X11`, `#gaming`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Demis Hassabis outlines plan for safe AGI development</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Demis Hassabis, CEO of DeepMind, published an article in The Economist outlining a plan for safe AI development as AGI approaches, emphasizing regulation, safety measures, and international coordination. As a leading AI figure, Hassabis's views shape industry and policy debates on AI safety. His plan could influence how governments and companies approach AGI regulation, balancing innovation with risk mitigation. The plan includes publishing model cards, maintaining strong cybersecurity, vetting key personnel, and ensuring sufficient resources for safety research. Hassabis asserts that AGI is only a few years away.

🔗 [Source](https://twitter.com/demishassabis/status/2076957440109625718)

hackernews · asiergoni · Jul 14, 09:20 · [Discussion](https://news.ycombinator.com/item?id=48904095)

**Background**: Artificial General Intelligence (AGI) is a hypothetical AI system that can perform any intellectual task a human can. Current AI systems like large language models are narrow, excelling at specific tasks but lacking general cognitive abilities. AI safety research focuses on ensuring these systems are aligned with human values and do not cause unintended harm.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artificial_general_intelligence">Artificial general intelligence - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_safety">AI safety - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/artificial-general-intelligence">What is Artificial General Intelligence (AGI)? | IBM</a></li>

</ul>
</details>

**Discussion**: Community comments are skeptical: some question the imminence of AGI, noting that LLMs still make basic errors. Others criticize the plan as overly focused on US regulation while ignoring global competition, or view it as a bid for funding rather than a genuine safety effort.

**Tags**: `#AI safety`, `#AGI`, `#regulation`, `#Demis Hassabis`, `#technology policy`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Lobste.rs migrates from MariaDB to SQLite, cuts costs</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Lobste.rs, a popular community link-aggregation site, has completed its migration from MariaDB to SQLite, now running the entire Rails application on a single VPS. The move has reduced CPU usage, memory usage, and hosting costs by half, while improving site responsiveness. This migration demonstrates that SQLite can handle production web workloads for a moderately trafficked community site, challenging the assumption that a client-server database is always necessary. It provides a real-world case study for developers considering simpler, cheaper database architectures. The primary SQLite database is about 3.8GB, with additional 1.1GB cache, 218MB queue, and 555MB Rack::Attack databases. The migration PR added 735 lines and removed 593 lines across 30 commits and 188 files, building on four previous PRs.

🔗 [Source](https://simonwillison.net/2026/Jul/14/lobsters-sqlite/#atom-everything)

rss · Simon Willison · Jul 14, 19:44

**Background**: SQLite is a self-contained, serverless database engine that stores data in a single file, making it simpler to manage than client-server databases like MariaDB or PostgreSQL. It is often used for embedded systems and small-scale applications, but recent improvements (e.g., WAL mode, NVMe SSDs) have made it viable for many production web workloads. Lobste.rs had been planning a database migration since 2018, originally considering PostgreSQL before switching to SQLite.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/lobsters/lobsters">GitHub - lobsters/lobsters: Computing-focused community centered around link aggregation and discussion · GitHub</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-sqlite">What Is SQLite? The Database That Runs Inside Your App | MindStudio</a></li>
<li><a href="https://daily.dev/blog/sqlite-production-guide-when-how-to-use-beyond-prototyping/">SQLite for Production: When and How to Use It Beyond Prototyping | daily.dev</a></li>

</ul>
</details>

**Discussion**: The Lobste.rs community discussion (linked in the article) includes insightful comments about the architecture trade-offs, with many praising the reduced complexity and cost. Some commenters raised concerns about write concurrency and backup strategies, but the maintainers reported that SQLite's WAL mode handles the site's workload well.

**Tags**: `#SQLite`, `#database migration`, `#web architecture`, `#Rails`, `#Lobsters`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Armin Ronacher: Friction Builds Shared Understanding in Software</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Armin Ronacher argues that the shared language of a software project is maintained by friction, which AI agents risk bypassing, potentially undermining team understanding. This insight highlights a critical but often overlooked cost of AI-assisted programming: the erosion of shared understanding that is essential for large-scale software collaboration. Ronacher notes that before AI agents, changing another team's code required reading, asking questions, and coordinating—friction that synchronized understanding. AI agents can make changes without this friction, allowing the tower to keep rising even after shared understanding collapses.

🔗 [Source](https://simonwillison.net/2026/Jul/14/armin-ronacher/#atom-everything)

rss · Simon Willison · Jul 14, 18:04

**Background**: In software engineering, shared understanding refers to the common knowledge among team members about the system's concepts, boundaries, invariants, ownership, and design rationale. This understanding is built through code reviews, conversations, and arguments—processes that involve friction. AI coding agents can generate and modify code quickly without requiring human-to-human communication, potentially bypassing the friction that builds shared understanding.

<details><summary>References</summary>
<ul>
<li><a href="https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/">The Tower Keeps Rising | Armin Ronacher's Thoughts and Writings</a></li>
<li><a href="https://simonwillison.net/2026/Jul/14/armin-ronacher/">A quote from Armin Ronacher - Simon Willison's Weblog</a></li>

</ul>
</details>

**Discussion**: Commenters resonated with the essay, drawing parallels to the Lisp Curse and noting that agents can make it too easy to build without collaborating. Some expressed concern that lower-skill developers might violate architectural integrity by using agents naively.

**Tags**: `#software engineering`, `#AI agents`, `#team dynamics`, `#shared understanding`, `#code review`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">New York imposes one-year ban on large data centres</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

New York has enacted a one-year moratorium on the construction of large data centres, becoming the latest state to regulate the industry's rapid expansion. This landmark regulation could slow the growth of cloud computing and AI infrastructure in New York, potentially influencing other states to adopt similar policies amid concerns over energy consumption and environmental impact. The ban applies to large data centres, though specific size thresholds are not detailed in the summary. The moratorium lasts one year, giving regulators time to study the industry's impact.

🔗 [Source](https://www.aljazeera.com/economy/2026/7/14/new-york-imposes-landmark-one-year-ban-on-large-data-centres?traffic_source=rss)

rss · Al Jazeera · Jul 14, 20:13

**Background**: Data centres are facilities that house computer systems and associated components, such as telecommunications and storage. They consume vast amounts of electricity, raising concerns about grid strain and carbon emissions. In the US, at least a dozen states have proposed similar bans or moratoriums.

**Tags**: `#data centres`, `#regulation`, `#energy policy`, `#cloud computing`, `#tech industry`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Cache-friendly uvx usage in GitHub Actions</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Simon Willison published a recipe for using uvx in GitHub Actions that sets UV_EXCLUDE_NEWER to a fixed date and includes that date in the cache key, enabling caching of tool downloads. This avoids re-downloading tools from PyPI on every workflow run. This approach significantly reduces CI execution time and network usage for Python tool invocations in GitHub Actions. It addresses a common pain point where workflows repeatedly download the same tools, and provides a simple pattern that can be widely adopted. The environment variable UV_EXCLUDE_NEWER is set to a date like "2026-07-12", and that date is used in the GitHub Actions cache key. Bumping the date busts the cache and upgrades tools to newer versions. An existing issue on astral-sh/setup-uv requests that the default behavior be changed to cache rather than purge wheels.

🔗 [Source](https://simonwillison.net/2026/Jul/14/uvx-github-actions-cache/#atom-everything)

rss · Simon Willison · Jul 14, 00:56

**Background**: uv is a fast Python package and project manager, and uvx is its tool for running Python-based CLI tools without installing them permanently. GitHub Actions workflows often invoke tools like linters or formatters, and without caching, each run downloads the tool and its dependencies from PyPI, slowing down CI.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.astral.sh/uv/guides/tools/">Using tools | uv - Astral Docs</a></li>

</ul>
</details>

**Discussion**: The linked issue on astral-sh/setup-uv shows community interest in making caching the default behavior. The discussion likely supports the idea of reducing redundant downloads, though no direct comments from the news item are provided.

**Tags**: `#GitHub Actions`, `#uv`, `#CI/CD`, `#caching`, `#Python`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">LLM Agents Should Never Be DRIs</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Simon Willison argues that LLM-powered agents should never be considered Directly Responsible Individuals (DRIs) because they cannot take accountability, a concept from Apple and GitLab. This raises critical accountability questions as AI agents are increasingly integrated into human organizations, challenging the assumption that they can replace human decision-makers. Willison references GitLab's handbook definition of DRI and an IBM 1979 training slide stating that a computer must never make a management decision because it cannot be held accountable.

🔗 [Source](https://simonwillison.net/2026/Jul/12/directly-responsible-individuals/#atom-everything)

rss · Simon Willison · Jul 12, 23:57

**Background**: The Directly Responsible Individual (DRI) concept originated at Apple and is used in organizations like GitLab to assign clear ownership and accountability for projects. LLM agents are AI systems that can autonomously perform tasks, but they lack the capacity for moral or legal responsibility.

<details><summary>References</summary>
<ul>
<li><a href="https://handbook.gitlab.com/handbook/people-group/directly-responsible-individuals/">Directly Responsible Individuals (DRI) | The GitLab Handbook</a></li>
<li><a href="https://dbmteam.com/insights/directly-responsible-individual-dri/">Directly Responsible Individual (DRI) | D. Brown Management</a></li>
<li><a href="https://tettra.com/article/directly-responsible-individuals-guide/">Directly Responsible Individuals: The What, How and Why of DRIs - Tettra</a></li>

</ul>
</details>

**Tags**: `#accountability`, `#LLM agents`, `#organizational design`, `#AI ethics`

</details>


</section>

<section class="cat cat-papers" markdown="1">

## 📄 Papers (24)

<a id="item-11"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">SpectraReward: Using Pretrained MLLMs as Zero-Shot Reward Models for Text-to-Image Generation</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Existing reinforcement learning methods for text-to-image generation require either human preference labels or fine-tuned reward models, which are costly and limited in scalability. This paper addresses the need for a training-free reward function that can leverage pretrained multimodal large language models (MLLMs) without additional data or fine-tuning.

**Method:** SpectraReward measures the average image-conditioned prompt log-likelihood via a single teacher-forced forward pass of a pretrained MLLM, using it as the reward. Self-SpectraReward extends this to unified multimodal models where the policy's own understanding branch serves as the reward model, forming a closed-loop self-improving framework without external models.

**Results:** Extensive experiments on two diffusion models, three RL algorithms, nine MLLM backbones (4B to 235B parameters), and five benchmarks show that SpectraReward and Self-SpectraReward significantly and consistently improve generation performance, outperforming prior MLLM-derived reward training methods. Larger reward MLLMs are not always better, and Self-SpectraReward can match or surpass much larger external reward models.

**Significance:** SpectraReward provides a simple, training-free, and scalable reward function for text-to-image RL, eliminating the need for preference labels or reward model fine-tuning. The self-improving variant demonstrates that reward-policy alignment is a key factor, potentially enabling more efficient and autonomous image generation systems.

🔗 [Source](https://arxiv.org/abs/2607.11886v1)

papers · Runhui Huang, Qihui Zhang, Zhe Liu et al. · Jul 13, 17:59 · cs.CV · [PDF](https://arxiv.org/pdf/2607.11886v1)

**Tags**: `#multimodal learning`, `#reward modeling`, `#text-to-image generation`, `#reinforcement learning`, `#MLLM`

</details>


<a id="item-12"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Metacognition in LLMs: A Comprehensive Survey</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Despite the recognized importance of metacognition for intelligent AI, it remains unclear whether and how large language models (LLMs) can exhibit or be endowed with metacognitive abilities, and how such abilities can enhance AI capabilities and reliability.

**Method:** This paper presents the first comprehensive survey on metacognition for LLMs, taxonomizing the field and summarizing recent technical advancements, including methods and benchmarks for measuring and evaluating metacognitive abilities, techniques to elicit, improve, and apply metacognition, and findings from ongoing research.

**Results:** The survey organizes the landscape of metacognition in LLMs, covering evaluation benchmarks, improvement techniques, and applications, while identifying open questions and future directions.

**Significance:** This work provides a structured overview of an emerging field, serving as a foundation for future research on metacognitive AI systems and their potential to enhance transparency, reliability, and intelligence.

🔗 [Source](https://arxiv.org/abs/2607.11881v1)

papers · Gabrielle Kaili-May Liu, Areeb Gani, Jacqueline Lu et al. · Jul 13, 17:58 · cs.CL · 🔥 12 · [PDF](https://arxiv.org/pdf/2607.11881v1)

**Tags**: `#LLMs`, `#metacognition`, `#AI safety`, `#survey`, `#machine learning`

</details>


<a id="item-13"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Transformers' learning dynamics in inductive reasoning reduce to low-dimensional manifold</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Previous theoretical analyses of Transformer learning dynamics are mostly tied to specific tasks, lacking a unified framework. This paper addresses the need for a general theory explaining how inductive reasoning abilities emerge in Transformers.

**Method:** The authors study a generalized class of inductive tasks that unifies several synthetic tasks (e.g., in-context n-grams, multi-hop reasoning). They theoretically prove that the training dynamics of attention models can be confined to a low-dimensional invariant manifold, where learning is captured by a handful of interpretable coordinates.

**Results:** The framework characterizes how data statistics govern the competition between in-context and in-weights learning, and how random initializations determine which circuit wins when multiple solutions exist. It also demonstrates that the coordinate frame can automatically detect learned circuits in trained models.

**Significance:** By casting circuit formation as a low-dimensional dynamical phenomenon, this work takes a step toward a predictive theory of how Transformers learn, enabling more interpretable analysis of in-context vs. in-weights learning.

🔗 [Source](https://arxiv.org/abs/2607.11875v1)

papers · Tiberiu Musat, Tiago Pimentel, Nicholas Zucchet et al. · Jul 13, 17:56 · cs.LG · [PDF](https://arxiv.org/pdf/2607.11875v1)

**Tags**: `#transformers`, `#inductive reasoning`, `#learning dynamics`, `#mechanistic interpretability`, `#theoretical analysis`

</details>


<a id="item-14"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">REGRIND: Minimalist Retargeting-Guided RL for Dexterous Manipulation</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** The paper addresses the challenge of learning dexterous manipulation policies that can transfer zero-shot to real hardware from a single human demonstration, given the complex contact-rich dynamics of manipulation tasks.

**Method:** REGRIND retargets human hand-object motion to a robot reference preserving spatial and contact relationships, then trains a residual RL policy in simulation to track object-centric keypoints along that reference, and transfers the policy zero-shot to hardware with careful system identification.

**Results:** The resulting policies produce fluid, human-like behavior on two different multi-fingered hands across contact-rich tool-use tasks, including operating scissors and turning a screwdriver. Systematic hardware experiments identify key factors for sim-to-real transfer.

**Significance:** This work demonstrates that a simple retargeting-guided RL recipe can achieve zero-shot sim-to-real transfer for dexterous manipulation, providing practical guidance for contact-rich settings and enabling human-like behavior from a single demonstration.

🔗 [Source](https://arxiv.org/abs/2607.11874v1)

papers · Yunhai Feng, Natalie Leung, Jiaxuan Wang et al. · Jul 13, 17:56 · cs.RO · [PDF](https://arxiv.org/pdf/2607.11874v1)

**Tags**: `#reinforcement learning`, `#dexterous manipulation`, `#retargeting`, `#sim-to-real`, `#robotics`

</details>


<a id="item-15"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Mechanistic interpretability reveals and controls LLM-as-judge bias in hidden states</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Existing studies of LLM-as-judge scoring bias operate at the input-output level, lacking a representation-level understanding that could enable more effective mitigation.

**Method:** The authors analyze the hidden state geometry of LLM judges, identifying a low-dimensional subspace associated with biased inputs. They then perform causal control by steering hidden states along this subspace, and develop a linear projection method to predict judge failures on unseen benchmarks.

**Results:** Steering along the bias subspace reproduces biased scoring on clean inputs and restores baseline scoring on biased ones, with random directions producing an order-of-magnitude smaller effect. The linear projection method outperforms text-based alternatives in predicting judge failures on three unseen benchmarks.

**Significance:** This work provides a unified framework linking geometric structure, causal control, and operational prediction of LLM-as-judge bias, offering a new mechanistic understanding that goes beyond input-output analysis.

🔗 [Source](https://arxiv.org/abs/2607.11871v1)

papers · Zixiang Xu, Sixian Li, Huaxing Liu et al. · Jul 13, 17:55 · cs.LG · [PDF](https://arxiv.org/pdf/2607.11871v1)

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>

</ul>
</details>

**Tags**: `#mechanistic interpretability`, `#LLM bias`, `#LLM-as-judge`, `#representation analysis`, `#causal control`

</details>


<a id="item-16"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Evidence-Backed Video Question Answering with Spatio-Temporal Grounding</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Current Video LLMs answer questions without verifiable visual grounding, and existing explainability methods using text or sparse boxes fail to capture complex video dynamics like occlusions and deformations.

**Method:** The paper proposes Evidence-Backed Video Question Answering (E-VQA), requiring models to output both a semantic answer and spatio-temporal evidence: temporal segments and dense tracked segmentation masklets. They introduce ST-Evidence benchmark and ST-Evidence-Instruct dataset (160k samples) via automated pipelines, and fine-tune grounded Video LLMs on this data.

**Results:** Fine-tuning a 7B model on ST-Evidence-Instruct achieves +27.2 t-mean and +13.8 J&F over the UniPixel baseline, establishing a strong baseline for explainable video understanding.

**Significance:** This work reveals a decoupling between QA accuracy and visual perception that scaling alone cannot fix, and provides a benchmark and dataset to drive research toward truly grounded video understanding.

🔗 [Source](https://arxiv.org/abs/2607.11862v1)

papers · Shijie Wang, Honglu Zhou, Ziyang Wang et al. · Jul 13, 17:49 · cs.CV · 🔥 1 · [PDF](https://arxiv.org/pdf/2607.11862v1)

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.11862">Evidence-Backed Video Question Answering</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0957417425002726">Spatial–temporal video grounding with cross-modal understanding and enhancement - ScienceDirect</a></li>
<li><a href="https://openaccess.thecvf.com/content/CVPR2024/papers/Gu_Context-Guided_Spatio-Temporal_Video_Grounding_CVPR_2024_paper.pdf">Context-Guided Spatio-Temporal Video Grounding Xin Gu1,3∗ Heng Fan2∗ Yan Huang2</a></li>

</ul>
</details>

**Tags**: `#Video LLM`, `#Explainability`, `#Question Answering`, `#Spatio-Temporal Grounding`, `#Benchmark`

</details>


<a id="item-17"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">AdvancedMathBench: Benchmarking LLMs on Advanced Math Proofs</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Existing math benchmarks for LLMs focus on high-school or olympiad problems and rely on final-answer correctness, failing to assess advanced mathematical reasoning and proof validity. There is a need for a benchmark with broader disciplinary coverage and fine-grained evaluation of proof correctness.

**Method:** The paper introduces AdvancedMathBench, which includes ProverBench (296 problems from undergraduate and doctoral qualifying exams) and VerifierBench (888 model-generated proofs with expert annotations). They develop an automatic verification pipeline trained on large-scale expert annotations to provide both correctness verdicts and fine-grained error assessments.

**Results:** On ProverBench, GPT-5.5-xhigh achieves scores of 75.8 and 66.1 on the UGD and QE splits, respectively. On VerifierBench, the best model attains a Balanced F1 of only 65.1, with low true negative rates indicating difficulty in detecting critical errors.

**Significance:** AdvancedMathBench reveals that frontier LLMs still struggle with advanced mathematical proof generation and verification, highlighting a significant gap in reasoning capabilities. The benchmark and automated verification pipeline provide a foundation for future research on improving LLMs' mathematical reasoning.

🔗 [Source](https://arxiv.org/abs/2607.11849v1)

papers · Lingkai Kong, Zijian Wu, Yuzhe Gu et al. · Jul 13, 17:38 · cs.CL · 🔥 19 · [PDF](https://arxiv.org/pdf/2607.11849v1)

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Proof_assistant">Proof assistant - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/formal-verification-pipeline">Formal Verification Pipeline</a></li>
<li><a href="https://arxiv.org/html/2605.20531">Pseudo-Formalization for Automatic Proof Verification</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#mathematical reasoning`, `#benchmark`, `#proof verification`, `#AI safety`

</details>


<a id="item-18"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Input-Aware Dynamic Backdoor Attack Against Quantum Neural Networks</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Existing quantum backdoor attacks rely on fixed triggers, which are easily detected by defenses that exploit repeated patterns. Transferring input-aware dynamic backdoors from classical to quantum neural networks is challenging due to measurement compression and density matrix fluctuations.

**Method:** Q-DIBA jointly trains a classical trigger generator and a victim QNN using a three-mode mini-batch strategy and an ensemble density contrastive loss that operates on post-ansatz quantum states before measurement, contrasting mode-averaged density matrices.

**Results:** On MNIST and Fashion-MNIST across multiple QNN architectures, Q-DIBA achieves high clean accuracy, strong attack success, and high cross-trigger accuracy. It remains resilient against defenses including visual inspection, spectral-signature detection, and fine-tuning.

**Significance:** This is the first input-aware dynamic backdoor attack for QNNs, demonstrating that such attacks pose a serious threat to secure QNN deployment and highlighting the need for advanced defenses.

🔗 [Source](https://arxiv.org/abs/2607.11843v1)

papers · Junrui Zhang, Zemin Chen, Lusi Li et al. · Jul 13, 17:34 · quant-ph · [PDF](https://arxiv.org/pdf/2607.11843v1)

**Tags**: `#quantum machine learning`, `#backdoor attack`, `#quantum neural networks`, `#security`, `#adversarial machine learning`

</details>


<a id="item-19"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">HASTE: A No-Code Platform for Rapid Building Damage Assessment</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** After a large disaster, responders need building damage maps within hours, but existing models require matched before-and-after imagery and training data from similar past events, which are rarely available in the first day.

**Method:** HASTE is a no-code web platform offering two methods: (1) single-scene segmentation, where users label polygons over the post-disaster scene to train a small semantic segmentation model, and (2) few-shot classification, where users label a handful of buildings and a pretrained vision model embeds each footprint, then a logistic regression scores the rest in seconds.

**Results:** Preliminary experiments on xBD show that foundation-model embeddings pooled over footprints can separate damaged from intact buildings using only post-disaster imagery, matching a fully supervised ResNet-50 baseline with a twentieth of its labels. HASTE has supported over thirty real-world disaster responses since 2023, delivering results within hours to days.

**Significance:** HASTE enables non-ML experts to rapidly produce building damage maps from post-disaster satellite imagery, filling a critical gap in early disaster response. Its open-source release and proven real-world use make it a practical tool for humanitarian organizations.

🔗 [Source](https://arxiv.org/abs/2607.11838v1)

papers · Caleb Robinson, Anthony Ortiz, Simone Fobi Nsutezo et al. · Jul 13, 17:27 · cs.CV · [PDF](https://arxiv.org/pdf/2607.11838v1)

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/few-shot-learning">What Is Few-Shot Learning? | IBM</a></li>

</ul>
</details>

**Tags**: `#disaster response`, `#satellite imagery`, `#building damage assessment`, `#machine learning`, `#semantic segmentation`

</details>


<a id="item-20"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Cycle-World: Mitigating Error Accumulation in Long Video World Models</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Autoregressive diffusion models for video generation suffer from error accumulation over long horizons, leading to generative drift, structural collapse, and visual degradation.

**Method:** Cycle-World enforces temporal reversibility via a cycle-consistency objective. During training, a reverse-prediction model is integrated to embed causal constraints; at inference, it acts as a runtime corrector using gradient-based cycle guidance to refine latent representations.

**Results:** On the VBench benchmark, Cycle-World achieves state-of-the-art overall generation quality and long-horizon temporal consistency for 60-second video synthesis.

**Significance:** This work provides a principled approach to mitigating error drift in long-video generation, enabling stable and temporally consistent synthesis over extended durations.

🔗 [Source](https://arxiv.org/abs/2607.11836v1)

papers · Zihan Su, Teng Hu, Jiangning Zhang et al. · Jul 13, 17:27 · cs.CV · [PDF](https://arxiv.org/pdf/2607.11836v1)

**Tags**: `#video generation`, `#diffusion models`, `#error accumulation`, `#cycle consistency`, `#world models`

</details>


<a id="item-21"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Transformer-Guided Swarm Intelligence for Efficient Neural Architecture Search</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Neural Architecture Search (NAS) traditionally requires massive computational resources, often thousands of GPU-days, limiting its accessibility. This paper aims to democratize NAS on consumer-grade hardware while addressing the cold-start problem in metaheuristics and model bloat.

**Method:** The proposed frugal memetic NAS framework combines an autoregressive Transformer controller trained via Reinforcement Learning for global macro-search with an Artificial Bee Colony (ABC) algorithm for local micro-exploitation. A dynamic entropy mechanism prevents premature convergence during RL, and network depth is penalized to mitigate model bloat.

**Results:** On CIFAR-10, the method discovers an architecture with 84.85% accuracy and only ~174,000 parameters in 3 hours on an NVIDIA RTX 3060, significantly smaller than ResNet-20. For credit card fraud detection, it achieves an F1-Score of 0.71 with ~4,600 parameters.

**Significance:** This work makes NAS accessible on consumer-grade hardware, producing compact models suitable for edge deployment. The hybrid approach effectively combines global and local search, addressing key limitations of prior NAS methods.

🔗 [Source](https://arxiv.org/abs/2607.11826v1)

papers · Romain Amigon · Jul 13, 17:18 · cs.LG · [PDF](https://arxiv.org/pdf/2607.11826v1)

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artificial_bee_colony_optimization">Artificial bee colony optimization</a></li>
<li><a href="https://en.wikipedia.org/wiki/Memetic_algorithm">Memetic algorithm</a></li>

</ul>
</details>

**Tags**: `#Neural Architecture Search`, `#Transformer`, `#Swarm Intelligence`, `#Reinforcement Learning`, `#Efficient Deep Learning`

</details>


<a id="item-22"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">MM-ToolSandBox: A Benchmark for Visually Grounded Tool-Calling Agents</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Current tool-calling agents lack robust visual grounding capabilities, and existing benchmarks do not adequately evaluate multi-image, multi-turn scenarios with realistic conversational phenomena such as goal revisions and error corrections.

**Method:** MM-ToolSandBox provides a stateful execution environment with over 500 tools across 16 application domains. It uses an automated scenario generation pipeline with information-flow-guided planning and multi-stage quality filtering to create 258 human-verified nominal scenarios and 50 UI variants. The framework evaluates agents on multi-image, multi-turn tasks requiring grounded tool calls.

**Results:** Evaluating 12 state-of-the-art models (from 4B open-weight to proprietary systems) shows that even the best model achieves below 50% success rate. Failure analysis reveals that 53% of failures stem from incorrect information extraction from images despite correct task workflows, and a planning-to-precision crossover emerges with scale.

**Significance:** This work provides a comprehensive benchmark for visually grounded tool-calling, highlighting that visual precision is a primary bottleneck for capable models. It suggests different research directions for improving models at different capability levels, with the framework and benchmark publicly available.

🔗 [Source](https://arxiv.org/abs/2607.11818v1)

papers · Kaixin Ma, Di Feng, Alexander Metz et al. · Jul 13, 17:13 · cs.CV · [PDF](https://arxiv.org/pdf/2607.11818v1)

**Tags**: `#AI`, `#benchmark`, `#tool-calling`, `#visual grounding`, `#evaluation`

</details>


<a id="item-23"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Relaxing Faithfulness for Causal Discovery Using Interventions</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Causal discovery algorithms rely on the faithfulness assumption, which requires causally linked variables to be statistically dependent. However, many natural systems have stabilizing pathways that cancel out, violating faithfulness and causing algorithms to miss true causal dependencies.

**Method:** The paper proposes using hard interventions as the primary source of causal information, introducing a milder assumption called intervention-immediacy faithfulness that allows cancellations. This assumption is sufficient to nonparametrically identify causal structures with hard interventions, flipping the traditional paradigm that prioritizes conditional independence testing.

**Results:** The paper shows that intervention-immediacy faithfulness is sufficient for nonparametric identification of causal structures with hard interventions. It also characterizes equivalence classes when identification criteria are not met due to limited intervention scope.

**Significance:** This work relaxes a key assumption in causal discovery, making algorithms applicable to systems with stabilizing pathways. It repositions interventions as the primary carriers of causal information, potentially improving the robustness of causal discovery in complex systems.

🔗 [Source](https://arxiv.org/abs/2607.11816v1)

papers · Bijan Mazaheri, Jiaqi Zhang, Caroline Uhler · Jul 13, 17:12 · cs.LG · [PDF](https://arxiv.org/pdf/2607.11816v1)

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/1207.0547">Geometry of the faithfulness assumption in causal inference</a></li>
<li><a href="https://www.cmu.edu/dietrich/philosophy/docs/spirtes/uai05a.pdf">Strong Faithfulness and Uniform Consistency in Causal Inference</a></li>

</ul>
</details>

**Tags**: `#causal discovery`, `#faithfulness`, `#interventions`, `#causal inference`, `#machine learning`

</details>


<a id="item-24"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Boosting acoustic perception in audio-language models by amplifying encoder neurons</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Large audio-language models (LALMs) perform poorly on fine-grained non-semantic speech attributes like emotion, and existing inference-time interventions are coarse-grained and applied after the audio encoder, leaving the encoder's internal neurons unexplored.

**Method:** IAAN (Identifying and Amplifying Acoustic Neurons) scores each feed-forward neuron in the audio encoder by contrasting its activation on real waveforms versus noise references, then amplifies the top-scoring neurons at inference without retraining or labels.

**Results:** Across ten non-semantic speech attributes, IAAN improves average accuracy by 25.7 points on Audio-Flamingo-3, 21.4 on Qwen2.5-Omni, and 9.7 on Kimi-Audio, and also improves a model already fine-tuned for acoustic evidence.

**Significance:** This work demonstrates that a small, targeted intervention inside the audio encoder at the neuron level is an effective and largely untapped way to enhance LALMs' acoustic understanding, opening a new direction for inference-time methods.

🔗 [Source](https://arxiv.org/abs/2607.11801v1)

papers · Yu-Han Huang, Chih-Kai Yang, Ke-Han Lu et al. · Jul 13, 16:53 · cs.SD · [PDF](https://arxiv.org/pdf/2607.11801v1)

**Tags**: `#audio-language models`, `#neuron identification`, `#acoustic perception`, `#inference-time intervention`, `#speech attributes`

</details>


<a id="item-25"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Training-Free Narrative Grounding for Long-Form Audio Description</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Long-form audio description for blind and low-vision audiences requires preserving narrative context across scenes, but current video-language models treat each moment independently, leading to incoherent descriptions that miss character identities and story connections.

**Method:** StoryTeller maintains a verified narrative memory that carries story-relevant information across scenes, using semantic filtering and VLM verification to accept only facts supported by the video. It optionally retrieves public movie metadata for names and context, requiring no subtitles, scripts, or fine-tuning.

**Results:** On standard AD benchmarks and diverse long-form videos, StoryTeller consistently improves narrative coherence, factual grounding, and story comprehension over strong baselines in automatic, QA-based, and human evaluations.

**Significance:** StoryTeller is the first training-free framework for story-aware long-form AD, enabling accessible film experiences for BLV audiences without requiring expensive annotated data or task-specific training.

🔗 [Source](https://arxiv.org/abs/2607.11798v1)

papers · Seung Hyun Hahm, Minh T. Dinh, SouYoung Jin · Jul 13, 16:50 · cs.CV · [PDF](https://arxiv.org/pdf/2607.11798v1)

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2109.04988">[2109.04988] Panoptic Narrative Grounding</a></li>
<li><a href="https://arxiv.org/abs/2404.00209">[2404.00209] EventGround: Narrative Reasoning by Grounding to Eventuality-centric Knowledge Graphs</a></li>

</ul>
</details>

**Tags**: `#audio description`, `#video-language models`, `#narrative grounding`, `#accessibility`, `#long-form video`

</details>


<a id="item-26"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Exact instrument reveals input-driven mode migration in Mamba state-space models</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Selective state-space models like Mamba use a learned selection mechanism to route information through state modes, but it is unclear how the model allocates its state capacity across different inputs. Existing interpretability methods cannot precisely measure per-mode contributions or predict pruning errors offline.

**Method:** The paper introduces an exact instrument that exploits the diagonal state matrix to decompose each channel's output into per-mode contributions. A per-(layer, channel, window) Gram tensor computes the exact output error of dropping any subset of modes offline. The instrument is validated against the reference implementation with relative error 2.3e-7 on Mamba-1 and predicts deployed pruning error with median relative deviation 5e-7 over 4,464 configurations.

**Results:** Across Mamba-1 (130M–2.8B), Falcon-Mamba 7B, and Mamba-2, the instrument reveals that trained models re-allocate state space with input: which modes carry the signal migrates across contexts. Input-scheduled mode pruning outperforms static, Hankel-based, and layer-adaptive rankings at every scale, and at half the state budget it matches the unpruned model.

**Significance:** This work provides the first exact measure of state usage in selective SSMs, enabling precise pruning and revealing a previously unknown input-driven migration phenomenon. The findings suggest headroom for dynamic state allocation, though no deployed compute or memory savings are claimed.

🔗 [Source](https://arxiv.org/abs/2607.11796v1)

papers · Raktim Bhattacharya · Jul 13, 16:48 · cs.LG · [PDF](https://arxiv.org/pdf/2607.11796v1)

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mamba_(deep_learning_architecture)">Mamba (deep learning architecture) - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2312.00752">[2312.00752] Mamba: Linear-Time Sequence Modeling with Selective State Spaces</a></li>
<li><a href="https://www.ibm.com/think/topics/mamba-model">What Is A Mamba Model? | IBM</a></li>

</ul>
</details>

**Tags**: `#state-space models`, `#Mamba`, `#model interpretability`, `#pruning`, `#deep learning`

</details>


<a id="item-27"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">JobHop v2: Large-scale career trajectory dataset from 440k resumes</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Existing career trajectory datasets are either small, closed, or built from pre-standardized codes with synthetic text, lacking authentic free-text annotations. This limits large-scale workforce analysis and job recommendation research.

**Method:** The authors use an end-to-end LLM extraction pipeline with reasoning-controlled inference and a retry mechanism to parse ~440,000 pseudonymized multilingual resumes from VDAB. The pipeline extracts ESCO occupational codes, quarterly timestamps, and five-level education attainment, achieving 100% JSON parse rate.

**Results:** The released dataset contains 355,315 career trajectories. The best extractor trails the inter-annotator agreement ceiling by only 1.1–2.7 percentage points across three annotation baselines.

**Significance:** JobHop v2 provides a large-scale, richly annotated, and publicly available dataset for reproducible career-trajectory research, enabling improved workforce planning and job recommendation systems.

🔗 [Source](https://arxiv.org/abs/2607.11715v1)

papers · Iman Johary, Guillaume Bied, Alexandru C. Mara et al. · Jul 13, 15:42 · cs.CL · [PDF](https://arxiv.org/pdf/2607.11715v1)

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/European_Skills,_Competences,_Qualifications_and_Occupations">European Skills, Competences, Qualifications and Occupations - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#dataset`, `#career trajectory`, `#LLM`, `#labor market`, `#NLP`

</details>


<a id="item-28"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">VoxENES 2026: Benchmarking Speech Spoofing Detectors Against Modern TTS and VC</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Current speech spoofing detectors are evaluated on legacy benchmarks that do not reflect modern LLM-driven TTS and voice conversion systems, creating a temporal generalization gap that overestimates detector robustness.

**Method:** The authors introduce VoxENES 2026, a bilingual (English and Spanish) benchmark containing 53,628 audio samples generated using 10 contemporary speech synthesis methods and evaluated under 10 standardized post-processing conditions. They benchmark eight pretrained detectors without fine-tuning.

**Results:** The best model achieves only 28.98% equal error rate (EER) overall, while most detectors perform near or below random chance across modern generators and perturbations.

**Significance:** This work highlights the reliance on brittle artifacts in current detectors and establishes VoxENES 2026 as a practical testbed for developing robust audio spoofing countermeasures.

🔗 [Source](https://arxiv.org/abs/2607.11706v1)

papers · Aastha Sharma, Guangjing Wang · Jul 13, 15:35 · cs.SD · [PDF](https://arxiv.org/pdf/2607.11706v1)

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2404.13914v1">Audio Anti-Spoofing Detection: A Survey</a></li>

</ul>
</details>

**Tags**: `#speech spoofing`, `#benchmark`, `#LLM TTS`, `#voice conversion`, `#audio security`

</details>


<a id="item-29"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">A roadmap for physical intelligence via embodied brains and world action models</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** The field of World Action Models (WAMs) for physical intelligence is fragmented, with incompatible action spaces, inconsistent datasets, and limited system interfaces, hindering progress toward embodied agents that can reason and act in the physical world.

**Method:** The paper reviews the evolution toward WAMs and identifies three coupled gaps: model roles and representations, objectives and standardization, and system composition. It proposes a co-evolution roadmap centered on an 'embodied brain' that integrates multimodal context, compares candidate interventions, and issues high-level requests rather than direct commands. The roadmap includes a physical harness for grounding, shared contracts for alignment, and closed-loop post-training for self-improvement.

**Results:** The paper does not present new empirical results; instead, it provides a conceptual analysis and a proposed roadmap. It references Xiaomi-Robotics-U0 as an example of a foundation model achieving state-of-the-art results in embodied generation tasks, but those results are not the focus of this paper.

**Significance:** This paper offers a structured analysis of fragmentation in physical intelligence research and presents a comprehensive roadmap that could guide future integration and standardization efforts, potentially accelerating progress toward adaptive and self-improving embodied agents.

🔗 [Source](https://arxiv.org/abs/2607.11689v1)

papers · Yuanzhi Liang, Xufeng Zhan, Haibin Huang et al. · Jul 13, 15:22 · cs.RO · [PDF](https://arxiv.org/pdf/2607.11689v1)

**Tags**: `#World Action Models`, `#Physical Intelligence`, `#Embodied AI`, `#Robotics`, `#AI Roadmap`

</details>


<a id="item-30"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Decoupling exploration from alignment in LLM post-training via proxy models</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

**Problem:** Existing LLM post-training methods tightly couple policy exploration with distribution alignment, forcing expensive exploration directly on the primary model and hindering reuse of optimization signals across models.

**Method:** PUST uses a lightweight proxy model to efficiently explore high-reward behaviors, extracts the relative improvement signal between the proxy's initial and optimized states, and transfers this directional update to the primary model for policy alignment.

**Results:** Systematic evaluations on Qwen3-family models across math and code domains show that update signals extracted from substantially weaker proxies can robustly and adjustably enhance stronger primary models.

**Significance:** PUST transforms LLM post-training from a monolithic online optimization process into a modular, reusable, and cost-efficient paradigm, enabling asynchronous generation and cross-model transfer of optimization signals.

🔗 [Source](https://arxiv.org/abs/2607.11505)

papers · Daocheng Fu, Rong Wu, Yu Yang et al. · Jul 13, 08:56 · 🔥 7 · [PDF](https://arxiv.org/pdf/2607.11505)

<details><summary>References</summary>
<ul>
<li><a href="https://www.alphaxiv.org/abs/2607.11505">Proxy Exploration and Reusable Guidance: A Modular LLM Post-Training Paradigm via Proxy-Guided Update Signals | alphaXiv</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#post-training`, `#reinforcement learning`, `#proxy model`, `#alignment`

</details>


<a id="item-31"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Forgetting Helps Agents Align on Shared Meanings</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

**Problem:** Existing models of conceptual alignment assume partnership settings where agents share payoffs, but real-world communication often involves non-partnership scenarios. This paper asks how memory characteristics like adaptiveness and degradation affect the emergence of shared meaning in such settings.

**Method:** The authors model conceptual alignment as a non-partnership coordination game and simulate counterfactual scenarios with agents having varying levels of adaptiveness and memory degradation. They compare actual and perceived conceptual convergence.

**Results:** Adaptive agents achieved actual convergence faster and had closer final conceptual regions, while non-adaptive agents perceived convergence earlier. Weighing novel information less over time led to more stable agreements than fixing the weight.

**Significance:** This work highlights that memory features are critical for the emergence and evolution of both actual and perceived conceptual convergence, offering insights for designing multi-agent systems that develop shared meaning.

🔗 [Source](https://arxiv.org/abs/2607.11787v1)

papers · Landon Liu, Mary Kelly, Alan Tsang · Jul 13, 16:37 · cs.MA · [PDF](https://arxiv.org/pdf/2607.11787v1)

**Tags**: `#conceptual alignment`, `#multi-agent systems`, `#semantics`, `#memory`, `#coordination games`

</details>


<a id="item-32"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">How Temperature Shapes Ideological Discourse in RAG</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

**Problem:** Retrieval-Augmented Generation (RAG) can transmit ideological bias from retrieved documents into LLM outputs, but the impact of sampling temperature on this discourse transfer is not well understood.

**Method:** The authors used Lexical Multidimensional Analysis (LMDA) on 1,117 COVID-19 treatment articles to identify three ideological discourses. They then used this corpus as external knowledge for RAG and had several LLMs answer ideological questions at different sampling temperatures, assessing semantic and lexical similarity to ideological reference texts.

**Results:** The RAG framework transfers ideological discourses into LLM responses, with the highest alignment at moderate temperatures and lower alignment at low temperatures, indicating that overly deterministic sampling suppresses discourse transfer.

**Significance:** This study reveals that sampling temperature is a critical parameter influencing ideological bias in RAG systems, highlighting the need for careful temperature tuning to mitigate unwanted discourse amplification or suppression.

🔗 [Source](https://arxiv.org/abs/2607.11783v1)

papers · Elmira Salari, Hazem Amamou, José Victor de Souza et al. · Jul 13, 16:36 · cs.CL · [PDF](https://arxiv.org/pdf/2607.11783v1)

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation</a></li>

</ul>
</details>

**Tags**: `#Retrieval-Augmented Generation`, `#ideological bias`, `#LLM safety`, `#natural language processing`, `#COVID-19`

</details>


<a id="item-33"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Evaluating RE Practices for Explainability: Insights from Daimler Truck</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

**Problem:** Explainability is critical for AI systems, especially in safety-critical domains, but there is limited empirical understanding of how existing Requirements Engineering (RE) practices support explainability requirements across the RE lifecycle in an industrial context.

**Method:** The authors conducted a multi-phase qualitative study with eight practitioners at Daimler Truck, using think-aloud protocols and moderated group discussions across requirements elicitation, specification, and validation steps.

**Results:** Preliminary analysis reveals recurring challenges across all steps: conceptual ambiguity during elicitation, limited testability and expressiveness during specification, and fragmented validation due to vague criteria and regulatory uncertainty.

**Significance:** This paper provides empirical insights into step-specific and cross-cutting challenges of addressing explainability in RE, and outlines a research vision for developing an empirically grounded RE framework for explainable AI-based systems.

🔗 [Source](https://arxiv.org/abs/2607.11771v1)

papers · Umm-e- Habiba, Lucas Mauser, Jonas Fritzsch et al. · Jul 13, 16:28 · cs.SE · [PDF](https://arxiv.org/pdf/2607.11771v1)

**Tags**: `#requirements engineering`, `#explainability`, `#AI systems`, `#empirical study`, `#safety-critical`

</details>


<a id="item-34"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">CatRetriever: Retrieving Bulk Structures from Generated Catalyst Surfaces</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

**Problem:** Surface generative models for catalyst discovery produce slab-adsorbate structures but fail to provide the corresponding parent bulk structure, hindering assessment of bulk-dependent properties like formation energy and synthesizability.

**Method:** CatRetriever uses contrastive representation learning to align slab and bulk crystal representations in a shared latent space, enabling retrieval of plausible parent bulk candidates from a slab query. It is extended into an adsorption energy targeted bulk discovery pipeline combining bulk retrieval, generative search space expansion, and adsorption energy distribution analysis.

**Results:** CatRetriever achieves R@1 > 91% and R@3 > 98% on both in-distribution and holdout evaluation sets for retrieving parent bulk structures from slab queries.

**Significance:** CatRetriever provides a scalable route to connect catalyst generative models with physically plausible and adsorption energy compatible bulk catalyst discovery, enabling assessment of bulk-dependent properties and synthesizability.

🔗 [Source](https://arxiv.org/abs/2607.11712v1)

papers · Jungho Oh, Woosung Kim, Dong Hyeon Mok et al. · Jul 13, 15:38 · cs.LG · [PDF](https://arxiv.org/pdf/2607.11712v1)

**Tags**: `#contrastive learning`, `#materials discovery`, `#catalyst design`, `#representation learning`, `#generative models`

</details>


</section>