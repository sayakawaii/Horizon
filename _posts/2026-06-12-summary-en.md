---
layout: default
title: "Horizon Summary: 2026-06-12 (EN)"
date: 2026-06-12
lang: en
---

> From 124 items, 17 important content pieces were selected

---

<section class="cat cat-science" markdown="1">

## 🧪 Science (1)

<a id="item-1"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">CRISPR Cas12a2 shreds cancer cells, targets undruggable mutations</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Researchers have developed a CRISPR-based technique using Cas12a2 that selectively shreds cancer cells by detecting tumor-specific mutations, including those previously considered undruggable. This approach offers a potential treatment for cancers with mutations that cannot be targeted by conventional drugs, expanding the scope of precision oncology. Unlike Cas9, which only damages DNA at the target site, Cas12a2 shreds chromatin upon activation, causing more extensive cell destruction. The technique is described in a Nature paper and a preprint on bioRxiv.

🔗 [Source](https://innovativegenomics.org/news/crispr-technique-selectively-shreds-cancer-cells/)

hackernews · gmays · Jun 12, 15:15 · [Discussion](https://news.ycombinator.com/item?id=48505231)

**Background**: CRISPR-Cas systems are bacterial defense mechanisms that cut nucleic acids. Cas12a2 is a recently discovered enzyme that cuts both RNA and DNA when triggered by a specific RNA target. 'Undruggable' refers to proteins that cannot be targeted by conventional small-molecule drugs due to their structure or function.

<details><summary>References</summary>
<ul>
<li><a href="https://medicalxpress.com/news/2026-06-crispr-enzyme-precisely-shreds-dna.html">CRISPR enzyme precisely detects and shreds DNA in cancer...</a></li>

</ul>
</details>

**Discussion**: Commenters noted that while the idea of using CRISPR to detect mutations is not new, Cas12a2's destructive mechanism is a significant advance. Concerns were raised about potential resistance evolution, and some argued that viral vector therapies may be more promising than CRISPR in the long run.

**Tags**: `#CRISPR`, `#cancer research`, `#gene editing`, `#biotechnology`, `#Cas12a2`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (15)

<a id="item-2"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Malware embeds nuclear, bioweapon text to evade AI analysis</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Malware developers have embedded references to nuclear and biological weapons into spyware targeting bioinformatics and MCP developers, aiming to confuse AI-assisted analysis tools and evade detection. This novel technique exploits the safety filters of large language models used in malware analysis, potentially allowing malicious code to bypass automated sandboxing and threat detection systems. The malware, discovered by Socket.dev, includes packages named 'mini-shai-hulud', 'miasma', and 'hades-worms' that contain nuclear and bioweapon text strings. This tactic is designed to trigger content moderation in AI analysis tools, causing them to refuse to analyze the code.

🔗 [Source](https://twitter.com/jsrailton/status/2064661778978533571)

hackernews · marc__1 · Jun 11, 20:24 · [Discussion](https://news.ycombinator.com/item?id=48495928)

**Background**: Bioinformatics developers work with genomic data and often use open-source packages, making them targets for supply chain attacks. MCP (Model Context Protocol) is an open protocol by Anthropic that connects AI models to external tools and data, and its developers are also targeted. Sandboxing is a cybersecurity technique that isolates suspicious files in a controlled environment for analysis, but AI-assisted analysis can be tricked by carefully crafted content.

<details><summary>References</summary>
<ul>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://www.sentinelone.com/cybersecurity-101/endpoint-security/what-is-sandboxing/">What Is Sandboxing in Cybersecurity ? Detecting Threats</a></li>

</ul>
</details>

**Discussion**: Commenters debate the effectiveness of LLM safety filters, with some arguing that nuclear weapons knowledge is already publicly available and not a secret, while others note that such content can still trigger censorship in models like GPT-4.8. One commenter warns that threat actors are now aware of AI-based analysis and emphasizes the need for proper sandboxing.

**Tags**: `#malware`, `#cybersecurity`, `#AI safety`, `#bioinformatics`, `#supply chain attack`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Critique of AI Over-Reliance in Specialized Fields</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

An essay titled 'Don't You Just Upload It to ChatGPT?' critiques the naive assumption that AI can replace human expertise in specialized fields like translation, using a personal anecdote to illustrate the value of nuanced human skill. This essay highlights the ongoing debate about AI's limitations in tasks requiring deep cultural and contextual understanding, challenging the trend of over-reliance on AI in specialized domains. The author uses their own experience as a translator to argue that AI lacks the cultural nuance and creativity that human experts bring, and that trusting AI blindly can lead to poor outcomes.

🔗 [Source](https://correresmidestino.com/dont-you-just-upload-it-to-chatgpt/)

hackernews · speckx · Jun 12, 17:52 · [Discussion](https://news.ycombinator.com/item?id=48507278)

**Background**: AI language models like ChatGPT have become widely used for tasks such as translation, writing, and summarization. However, critics argue that these models often miss subtle cultural references, idioms, and context that human experts naturally handle. The essay contributes to a broader discussion about the appropriate role of AI in knowledge work.

**Discussion**: Commenters largely agree with the essay's premise, sharing personal anecdotes about AI's shortcomings in translation and other specialized tasks. Some note that while AI translation has improved, it still requires human auditing for quality. Others express concern that AI may reduce demand for human translators, shifting the role to oversight rather than creation.

**Tags**: `#AI`, `#human expertise`, `#translation`, `#technology critique`, `#Hacker News`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">LLM-Generated PRs Violate Open Source Social Contract</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A prominent open-source maintainer argues that LLM-generated pull requests degrade collaboration by violating the implicit social contract of effort, where contributors are expected to invest more work than reviewers. This highlights a growing tension in open-source maintenance as AI-generated code floods projects, shifting maintainer sentiment from excitement to frustration and potentially harming community health. The essay contrasts pre-LLM PRs, which were rare and exciting, with current low-effort AI submissions that require significant reviewer effort. Studies show AI-generated PRs have 1.7x more issues than human ones.

🔗 [Source](https://blog.miguelgrinberg.com/post/i-am-not-a-reverse-centaur)

hackernews · ibobev · Jun 12, 17:53 · [Discussion](https://news.ycombinator.com/item?id=48507282)

**Background**: Open-source projects rely on an implicit social contract where contributors voluntarily invest effort, and maintainers review changes. LLMs enable non-coders to generate code, but often produce shallow or incorrect patches that burden maintainers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Social_contract">Social contract - Wikipedia</a></li>
<li><a href="https://prodmoh.com/blog/checklist-for-reviewing-llm-generated-prs">Checklist for Reviewing LLM - Generated PRs (Deep Technical Guide...)</a></li>
<li><a href="https://www.linkedin.com/posts/joshuacornejo_on-average-ai-generated-pull-requests-activity-7408063144243273728-M-zW">AI- Generated Pull Requests Have 1.7x More Issues | LinkedIn</a></li>

</ul>
</details>

**Discussion**: Commenters agree with the author, noting a shift from excitement to dread when receiving PRs. Some suggest creating non-canonical software ecosystems for AI-generated contributions, while others emphasize the need for better tooling to filter low-quality PRs.

**Tags**: `#open-source`, `#LLM`, `#software maintenance`, `#AI ethics`, `#pull requests`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Anthropic Reverses Secret Policy Limiting Claude for AI Research</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Anthropic reversed a policy that secretly limited Claude Fable 5's effectiveness when used for frontier LLM development, and apologized for the lack of transparency. The company will now make such safeguards visible to users, showing a fallback to Opus 4.8 and providing refusal reasons on the API. This policy reversal restores trust with the AI research community, which relies on Claude for cutting-edge work. It also sets a precedent for transparency in AI model safeguards, potentially influencing how other companies handle similar restrictions. The invisible safeguards affected approximately 0.03% of traffic and used methods like prompt modification and steering vectors to limit effectiveness. Anthropic initially chose invisible safeguards to ship quickly with few false positives, but acknowledged that was the wrong tradeoff.

🔗 [Source](https://simonwillison.net/2026/Jun/11/anthropic-walks-back-policy/#atom-everything)

rss · Simon Willison · Jun 11, 03:45

**Background**: Claude Fable 5 is Anthropic's most capable model, part of the Mythos tier above Opus 4.8. The company had hidden a policy in its system card that would silently limit the model's assistance on frontier LLM development, sparking backlash when discovered.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/story/anthropic-responds-to-backlash-on-claudes-secret-sabotage-on-ai-research/">Anthropic Walks Back Policy That Could Have ‘Sabotaged... | WIRED</a></li>
<li><a href="https://www.theneuron.ai/explainer-articles/everything-to-know-about-claude-fable-5-anthropics-new-and-first-public-release-of-its-mythos-model/">Claude Fable 5: Anthropic’s Mythos Launch Explained | The Neuron</a></li>
<li><a href="https://digg.com/tech/fpdiy0g6">Anthropic silently restricts Fable 5 from assisting with frontier LLM ...</a></li>

</ul>
</details>

**Discussion**: The community outcry was significant, with many researchers accusing Anthropic of sabotaging their work. The reversal was welcomed, but some still argue that the category of refusals should be dropped entirely, not just made visible.

**Tags**: `#AI policy`, `#Anthropic`, `#Claude`, `#transparency`, `#AI safety`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">OpenAI to acquire Ona for Codex cloud environments</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

OpenAI announced plans to acquire Ona, a provider of on-demand secure cloud environments, to integrate persistent cloud environments into Codex for long-running AI agents in enterprise workflows. This acquisition enables Codex to support long-running, persistent AI agents that can operate securely in enterprise environments, expanding its use from coding assistance to broader enterprise automation. Ona provides ephemeral, pre-configured cloud environments that are ready in seconds, allowing AI agents to execute end-to-end in the background with network access and permissions.

🔗 [Source](https://openai.com/index/openai-to-acquire-ona)

rss · OpenAI Blog · Jun 11, 00:00

**Background**: Codex is an AI coding agent by OpenAI released in April 2025, available via CLI, desktop app, and IDE integrations. By March 2026, it had over 2 million weekly active users, and OpenAI is positioning it as an enterprise agent platform beyond software development.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/openai-to-acquire-ona/">OpenAI to acquire Ona | OpenAI</a></li>
<li><a href="https://ona.com/cases/ona-environments">Cloud environments for developers and coding agents · Ona</a></li>
<li><a href="https://en.wikipedia.org/wiki/Codex_(AI_agent)">Codex (AI agent)</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#acquisition`, `#Codex`, `#AI agents`, `#enterprise`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Olmo-eval: A Workbench for LLM Development Loop Evaluation</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Allen AI has introduced olmo-eval, an open-source evaluation workbench designed to streamline model evaluation during the iterative development loop of large language models. This tool addresses a critical need in LLM development by providing a unified, extensible framework for running evaluation pipelines, enabling faster and more reliable model improvements. The codebase includes task sets and example configurations, allowing users to easily register custom evaluation suites and integrate them into the model development loop.

🔗 [Source](https://huggingface.co/blog/allenai/olmo-eval)

rss · Hugging Face Blog · Jun 12, 15:56

**Background**: Evaluating large language models during development is crucial for iterative improvement, but existing tools often lack flexibility or integration. Olmo-eval provides a unified workbench that supports various NLP tasks and can be extended with custom evaluations.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/allenai/olmo-eval">GitHub - allenai/ olmo - eval · GitHub</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#evaluation`, `#tooling`, `#AI engineering`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Mother sues OpenAI after daughter's death linked to ChatGPT</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A mother has filed a lawsuit against OpenAI in the United States, alleging that the company failed to intervene despite warning signs in her daughter's ChatGPT conversations, which she claims contributed to her daughter's death. This case could set a legal precedent for AI safety and accountability, highlighting the real-world harm that can arise from unmoderated AI interactions and pressuring companies to implement stronger safeguards. The lawsuit accuses OpenAI of negligence and failing to act on known risks, though specific details about the conversations and the daughter's death have not been publicly disclosed.

🔗 [Source](https://www.aljazeera.com/economy/2026/6/12/mother-sues-openai-in-us-after-daughters-death-linked-to-chatgpt-use?traffic_source=rss)

rss · Al Jazeera · Jun 12, 21:38

**Background**: ChatGPT is a large language model that generates human-like text based on user input. Concerns have been raised about its potential to cause emotional distress or encourage harmful behavior, especially among vulnerable users. This lawsuit is one of the first to directly link AI chatbot use to a death.

**Tags**: `#AI safety`, `#legal`, `#ethics`, `#OpenAI`, `#ChatGPT`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Guide to Setting Up a Local Coding Agent on macOS</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A detailed tutorial explains how to configure a local coding agent on macOS using llama.cpp and open-source models, enabling AI-assisted coding without cloud dependencies. This guide empowers developers to run coding agents locally, enhancing privacy and reducing costs, while contributing to the growing trend of local AI tooling. The setup leverages llama.cpp for model inference and supports various open-source models; the tutorial includes benchmarking but community comments note that short token generation may yield misleading speed results.

🔗 [Source](https://ikyle.me/blog/2026/how-to-setup-a-local-coding-agent-on-macos)

hackernews · kkm · Jun 12, 17:34 · [Discussion](https://news.ycombinator.com/item?id=48507020)

**Background**: Local coding agents use large language models (LLMs) running on the user's machine to assist with code generation, review, and debugging. Tools like llama.cpp enable efficient inference on consumer hardware, making local AI assistants feasible without internet connectivity or cloud costs.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/rosgluk/llamacpp-quickstart-with-cli-and-server-bfl">llama . cpp Quickstart with CLI and Server - DEV Community</a></li>
<li><a href="https://joeywang.github.io/posts/lm-studio-gemma4/">Using LM Studio and Gemma as a Local Engine for Coding Agents</a></li>

</ul>
</details>

**Discussion**: Commenters suggested alternative tools like Ollama with opencode, LM Studio, and omlx.ai, and noted that the benchmark's short token generation might give false positives for speed improvements. One user also pointed out that llama.cpp can download models directly without huggingface-cli.

**Tags**: `#local-llm`, `#coding-agent`, `#macOS`, `#llama.cpp`, `#tutorial`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Adaptive PDFs: Content Changes Based on How It's Read</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A new technique embeds Markdown source within a PDF so that text extraction returns structured Markdown while visual display shows the original PDF layout. This innovation could improve accessibility and machine readability of PDFs, but also raises concerns about security and potential misuse for hiding malicious instructions from human readers. The PDF embeds Markdown in a way that PDF viewers ignore but text extractors read, effectively creating dual content. This is distinct from simply zipping PDF with Markdown sources.

🔗 [Source](https://sgaud.com/texts/pdf)

hackernews · SarthakGaud · Jun 12, 16:32 · [Discussion](https://news.ycombinator.com/item?id=48506209)

**Background**: PDF is a fixed-layout format widely used for documents, but extracting text from PDFs often loses structure like headings and lists. Markdown is a lightweight markup language that preserves structure. This technique bridges the two by hiding structured source inside the PDF.

<details><summary>References</summary>
<ul>
<li><a href="https://adaptivereader.com/">Adaptive Reader | The Accessibility Layer for Education</a></li>

</ul>
</details>

**Discussion**: Commenters discussed potential misuse, such as embedding AI-specific instructions invisible to humans, similar to 'white text' hacks. Some also noted this could be used in resumes to influence LLM screening, sparking an arms race in hiring.

**Tags**: `#PDF`, `#security`, `#innovation`, `#document-engineering`

</details>


<a id="item-11"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">MaxProof: Scaling Mathematical Proof with AI</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A new arXiv paper introduces MaxProof, a population-level test-time scaling framework for competition-level mathematical proof, developed as part of the MiniMax-M3 series. This work pushes the boundaries of AI's ability to solve complex mathematical problems, potentially impacting fields like formal verification and automated theorem proving. The MaxProof framework reportedly enabled the M3 model to exceed the human gold-medal threshold on competition-level problems, using generative-verifier reinforcement learning and population-level test-time scaling.

🔗 [Source](https://arxiv.org/abs/2606.13473)

hackernews · ilreb · Jun 12, 12:00 · [Discussion](https://news.ycombinator.com/item?id=48503014)

**Background**: Test-time scaling is a technique where a model uses additional computation during inference to improve performance. Population-level scaling extends this by coordinating multiple model instances. The IMO (International Mathematical Olympiad) gold medal threshold is a common benchmark for AI math reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.13473">[2606.13473] MaxProof : Scaling Mathematical Proof with...</a></li>
<li><a href="https://www.minimax.io/blog/minimax-maxproof-math-proof-evolution">MaxProof : Scaling Mathematical Proof with... | MiniMax</a></li>
<li><a href="https://news.ycombinator.com/item?id=48503014">Maxproof | Hacker News</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion humorously ties the paper to IMO scoring anomalies, with comments like 'The real AGI test is apparently not solving the IMO, but getting caught in the same scoring traffic jam as 46 teenagers.' Some commenters highlight the need for formal verification.

**Tags**: `#AI`, `#formal verification`, `#IMO`, `#arXiv`

</details>


<a id="item-12"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Claude Fable 5 Shows Relentless Proactivity in Debugging</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Simon Willison observed Claude Fable 5 autonomously debugging a UI scrollbar bug by writing test HTML, opening Safari, and using pyobjc to capture screenshots without being instructed to do so. This demonstrates a new level of model autonomy and tool chaining, where the LLM proactively invokes system tools and writes code to achieve its goal, hinting at a future where AI agents can independently handle complex software engineering tasks. Fable 5 used Python with pyobjc-framework-Quartz to enumerate macOS windows, filtered for Safari windows containing 'textarea', then used screencapture to grab screenshots of its own test pages to diagnose the bug.

🔗 [Source](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/#atom-everything)

rss · Simon Willison · Jun 11, 23:35

**Background**: Claude Fable 5 is Anthropic's most capable generally available model, released in June 2026. It is known for strong vision and code generation abilities. Datasette Agent is an AI assistant for exploring and querying data in Datasette, built by Simon Willison.

<details><summary>References</summary>
<ul>
<li><a href="https://www.datacamp.com/blog/claude-fable-5">Claude Fable 5 : A Mythos-Class Model You Can Use | DataCamp</a></li>
<li><a href="https://agent.datasette.io/">Datasette Agent : an AI assistant for Datasette to help explore and...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Claude`, `#LLM`, `#software engineering`, `#debugging`

</details>


<a id="item-13"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Datasette 1.0a33 extends JSON API with extras pattern</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Datasette 1.0a33 extends the `?_extra=` pattern to queries and rows, allowing developers to request additional properties in JSON API responses. This release also includes documentation for the pattern and an interactive extras explorer tool built with AI assistance. This release is a significant step toward a stable Datasette 1.0, improving the flexibility and usability of its JSON API. Developers building data-driven applications will benefit from more granular control over API responses, reducing payload size and improving performance. The `?_extra=` pattern was originally introduced in Datasette 1.0a3 for tables and is now extended to cover queries and rows. The release also includes a custom extras API explorer built using Claude Fable 5 and GPT-5.5 xhigh, demonstrating the feature interactively.

🔗 [Source](https://simonwillison.net/2026/Jun/11/datasette/#atom-everything)

rss · Simon Willison · Jun 11, 15:26

**Background**: Datasette is an open-source tool for exploring and publishing data, providing a JSON API for SQLite databases. The `?_extra=` mechanism allows users to request additional data fields in API responses, such as column types or row counts, without over-fetching. This alpha release brings that capability to more API endpoints.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/11/datasette/">Release: datasette 1.0a33 | Simon Willison’s Weblog</a></li>
<li><a href="https://docs.datasette.io/en/stable/json_api.html">JSON API - Datasette documentation</a></li>
<li><a href="https://github.com/simonw/datasette/issues/262">Add ?_ extra = mechanism for requesting extra properties in JSON ...</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#release`, `#API`, `#open-source`, `#data`

</details>


<a id="item-14"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Astrophysicist uses Codex to simulate black holes</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Astrophysicist Chi-kwan Chan uses OpenAI's Codex to build black hole simulations, enabling researchers to study extreme physics and test general relativity. This demonstrates a novel application of AI coding assistants in scientific computing, potentially accelerating research in astrophysics and general relativity. Codex is an AI assistant that understands and generates code in multiple languages, and here it is used to write simulation code for black hole physics.

🔗 [Source](https://openai.com/index/using-codex-to-simulate-black-holes)

rss · OpenAI Blog · Jun 11, 00:00

**Background**: Black hole simulations are computationally intensive and require solving Einstein's equations of general relativity. Codex can automate parts of the coding process, making it easier for scientists to develop and modify simulations.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/OpenAI_Codex">OpenAI Codex</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Codex`, `#astrophysics`, `#black holes`, `#scientific computing`

</details>


<a id="item-15"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">BBVA partners with OpenAI to deploy ChatGPT Enterprise to 100,000 employees</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

BBVA has partnered with OpenAI to deploy ChatGPT Enterprise to 100,000 employees, aiming to accelerate AI-powered banking transformation worldwide. This partnership signals a major trend of large financial institutions adopting enterprise AI at scale, potentially reshaping banking operations and customer experiences. ChatGPT Enterprise offers enhanced security, privacy, and integration capabilities, with no usage caps and up to 2x faster performance compared to the consumer version.

🔗 [Source](https://openai.com/index/bbva)

rss · OpenAI Blog · Jun 11, 00:00

**Background**: ChatGPT Enterprise is OpenAI's business-oriented version of ChatGPT, designed for organizational use with features like data encryption, single sign-on, and integration with company data sources. BBVA is a major Spanish multinational bank, and this deployment is one of the largest known enterprise AI rollouts in the banking sector.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-enterprise/">Introducing ChatGPT Enterprise | OpenAI</a></li>
<li><a href="https://help.openai.com/en/articles/8265053-what-is-chatgpt-enterprise">What is ChatGPT Enterprise ? | OpenAI Help Center</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Enterprise`, `#Banking`, `#OpenAI`, `#ChatGPT`

</details>


<a id="item-16"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">PyTorch MLP Fusion Guide for Performance</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

This blog post provides a detailed guide on profiling and fusing MLP layers in PyTorch, showing how to combine multiple linear layers into a single kernel for faster execution. MLP融合可以显著减少内核启动开销和内存带宽使用，从而在深度学习推理和训练中实现大幅加速。 The guide uses PyTorch's profiler to identify bottlenecks and then applies operator fusion techniques, such as using torch.jit.script or custom CUDA kernels, to fuse the MLP layers.

🔗 [Source](https://huggingface.co/blog/torch-mlp-fusion)

rss · Hugging Face Blog · Jun 11, 00:00

**Background**: MLP (Multilayer Perceptron) is a fundamental neural network architecture consisting of multiple fully connected layers. In PyTorch, each linear layer is typically launched as a separate GPU kernel, which can incur overhead. Operator fusion combines multiple kernels into one to improve performance.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/torch-profiler">Profiling in PyTorch (Part 1): A Beginner's Guide to torch. profiler</a></li>
<li><a href="https://docs.pytorch.org/tutorials/beginner/profiler.html">Profiling your PyTorch Module — PyTorch Tutorials 2.12.0+cu130...</a></li>

</ul>
</details>

**Tags**: `#PyTorch`, `#profiling`, `#MLP`, `#performance optimization`, `#deep learning`

</details>


</section>

<section class="cat cat-other" markdown="1">

## 📌 Other (1)

<a id="item-17"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Dumpster behind library sparks debate on book pulping</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A dumpster appeared behind a university library, symbolizing the practice of pulping books after digitization, as discussed in a Yale Review article. This highlights the tension between physical and digital archives, raising questions about accessibility, preservation, and the future of libraries. The article and community comments note that many libraries digitize books and then pulp them to free up space, though some argue that digitization can actually increase demand for physical copies.

🔗 [Source](https://yalereview.org/article/sheila-liming-the-end-of-books)

hackernews · mooreds · Jun 12, 14:21 · [Discussion](https://news.ycombinator.com/item?id=48504543)

**Background**: Libraries have been digitizing collections for years to improve access and save space. However, after scanning, some libraries discard the physical books, a practice critics call 'the great pulping.' This raises concerns about preserving rare editions and ensuring long-term access.

<details><summary>References</summary>
<ul>
<li><a href="https://news.cornell.edu/stories/2023/10/digitizing-books-can-spur-demand-physical-copies">Digitizing books can spur demand for physical copies</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_library">Digital library - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters debated the necessity of keeping physical copies when digital versions and interlibrary loans exist, with some viewing book pulping as practical and others as a loss of cultural heritage. One commenter compared the emotional attachment to books to commodity fetishism.

**Tags**: `#libraries`, `#digitization`, `#books`, `#information storage`, `#community debate`

</details>


</section>