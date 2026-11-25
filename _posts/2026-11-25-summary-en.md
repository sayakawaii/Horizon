---
layout: default
title: "Horizon Summary: 2026-11-25 (EN)"
date: 2026-11-25
lang: en
---

> From 135 items, 17 important content pieces were selected

---

<section class="cat cat-science" markdown="1">

## 🧪 Science (2)

<a id="item-1"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">OpenAI preprint claims matrix multiplication exponent is exactly 9/4</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

A preprint released by OpenAI claims to prove that the matrix multiplication exponent ω is exactly 9/4, meaning any two n×n matrices can be multiplied in n^(9/4+o(1)) field operations and that this bound is optimal. The result is part of a batch of four papers that reportedly resolve eight problems from a Top 500 Open Problems in Math list, including Smale's ninth problem on strongly polynomial linear programming. Determining the optimal complexity of matrix multiplication is one of the most famous open problems in theoretical computer science, and settling it would close a decades-long quest that began with Strassen's algorithm in 1969. The claim also highlights the growing role of AI systems in producing frontier mathematical research, since the proof reportedly came from an unreleased OpenAI model and was formalized in Lean. The result establishes a lower bound of Ω(n^2.25); the matching upper bound of O(n^2.25) was already known from a recently published algorithm, though like other fast matrix multiplication algorithms it is a galactic algorithm with enormous constant factors and no practical use. The proof has not yet been peer-reviewed by leading mathematicians, and the model and training recipe behind it have not been disclosed.

🔗 [Source](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf)

hackernews · E-Reverance · Nov 25, 01:19 · [Discussion](https://news.ycombinator.com/item?id=50637220)

**Background**: The matrix multiplication exponent ω is the smallest number such that n×n matrices can be multiplied using n^(ω+o(1)) field operations. Schoolbook multiplication takes Θ(n^3) operations, and Strassen's 1969 algorithm was the first to beat that bound; since then researchers have gradually lowered the best known upper bounds on ω without knowing whether an optimal exponent exists or what it is. Matrix multiplication is a core subroutine in numerical linear algebra and optimization, so its asymptotic complexity is of major theoretical interest.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication">Computational complexity of matrix multiplication</a></li>
<li><a href="https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm">Matrix multiplication algorithm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_mathematical_discoveries_made_with_artificial_intelligence">List of mathematical discoveries made with artificial ...</a></li>

</ul>
</details>

**Discussion**: Commenters clarified that the result proves a lower bound of Ω(n^2.25) while the upper bound was already known, and noted that the title should use Θ(n^2.25) rather than O(n^2.25). Some expressed astonishment that OpenAI's model developed a new tensor geometry framework underlying the proofs, and others speculated that OpenAI may be holding back stronger models for internal research to create a compounding loop of breakthroughs.

**Tags**: `#matrix-multiplication`, `#computational-complexity`, `#algorithms`, `#open-problems`, `#AI-for-math`

</details>


<a id="item-2"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Heart attack and stroke risk detectable decades in advance</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A study from the University of Edinburgh suggests that heart attack and stroke risk can be detected decades in advance using routine biomarkers such as blood pressure, cholesterol, inflammation (CRP), BMI, troponin, and diabetes/smoking status. This finding could enable early prevention strategies, as many of these risk factors are modifiable through lifestyle changes and medications, potentially reducing the burden of cardiovascular disease, the leading cause of death globally. The study did not examine risk factors by ethnicity, and the team cautions that further research is needed to explore potential differences in risk factor and biomarker trajectories across ethnic groups.

🔗 [Source](https://www.ed.ac.uk/news/heart-attack-and-stroke-risk-detectable-decades-in-advance)

hackernews · gmays · Nov 24, 21:51 · [Discussion](https://news.ycombinator.com/item?id=50635271)

**Background**: Cardiovascular disease is the leading cause of death worldwide. Risk prediction tools like the Framingham Risk Score and the PREVENT equations use routine biomarkers to estimate an individual's likelihood of experiencing a heart attack or stroke over a certain period. Early identification of high-risk individuals allows for timely interventions, such as statins or lifestyle modifications, to prevent cardiovascular events.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ed.ac.uk/news/heart-attack-and-stroke-risk-detectable-decades-in-advance">Heart attack and stroke risk detectable decades in advance | News</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11688159/">A Narrative Review of the Role of Blood Biomarkers in the ...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s12471-022-01737-0">Biomarkers for cardiovascular risk prediction: from ...</a></li>

</ul>
</details>

**Discussion**: Commenters discussed practical risk calculators like the PREVENT equations and emphasized that many risk factors are modifiable. Some shared personal anecdotes about statins and dietary changes, while others debated the role of GLP-1 agonists and supplements like psyllium husk in managing risk.

**Tags**: `#health`, `#medical-research`, `#cardiovascular`, `#prevention`, `#biomarkers`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (15)

<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Ternary Bonsai 2.5 27B: Quantized Model Delivers Strong Local Agentic Coding</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

PrismML released Ternary Bonsai 2.5 27B, a ternary-quantized version of the Qwen3.8-27B hybrid-attention model, designed for agentic coding and multi-step tool use. It runs in about 5.9 GB and achieves SWE-bench Verified scores comparable to much larger frontier models, according to community reports. This demonstrates that aggressive quantization can shrink a 27B model to run on consumer hardware like a Mac Mini while retaining frontier-like coding abilities, potentially democratizing access to capable AI agents. It also fuels debate about whether small models are genuinely catching up or whether benchmarks are being gamed. Users report 22-25 tokens/s generation on a Mac Mini M5 Pro with 24GB RAM, with prompt evaluation around 2 seconds and support for up to 128k context in memory. The model is distributed as a Q2 GGUF file, making it compatible with llama.cpp and MLX-based inference.

🔗 [Source](https://prismml.com/news/bonsai-2-5-27b)

hackernews · b0m · Nov 24, 20:08 · [Discussion](https://news.ycombinator.com/item?id=50633922)

**Background**: Ternary quantization reduces model weights to three values (-1, 0, 1), drastically cutting memory and compute requirements compared to full-precision models. This technique enables large models to run on edge devices, but often at the cost of some accuracy. SWE-bench Verified is a benchmark that evaluates a model's ability to resolve real-world software engineering issues from GitHub, and is commonly used to gauge coding proficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://prismml.com/news/bonsai-2-family">PrismML — Introducing Ternary Bonsai 2 2B, 4B, and 9B: Bringing...</a></li>
<li><a href="https://research.buaa.edu.cn/en/publications/trq-ternary-neural-networks-with-residual-quantization/">TRQ: Ternary Neural Networks With Residual Quantization</a></li>

</ul>
</details>

**Discussion**: Commenters are impressed by the local performance, with one reporting 22-25 tokens/s on a Mac Mini and another noting a 29% reduction in task completion time compared to the previous version. However, skepticism exists about benchmark validity, with some wondering if the SWE-bench score reflects genuine progress or 'benchmaxxing,' and others requesting direct comparisons to similarly sized models like Qwen3.8 quantizations.

**Tags**: `#AI/ML`, `#model quantization`, `#local inference`, `#benchmarks`, `#efficient ML`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">GPT-6.2 designs protein minibinders via code, without specialized AI</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

OpenAI announced that GPT-6.2 was given the 3D structures of five target proteins and the desired binding sites, and it wrote code to generate 3D designs for potential minibinders without using specialized protein AI models. To convert these designs into testable proteins, OpenAI used the specialized model SolubleMPNN to suggest amino acid sequences, and lab tests found evidence of binding across the five targets. This suggests that general-purpose language models with strong coding abilities can meaningfully contribute to protein design, potentially lowering the barrier for researchers without access to specialized structural biology models. It also fuels the debate about whether such models are developing intrinsic scientific reasoning or merely automating the use of existing computational tools. GPT-6.2 only produced 3D backbone designs; the actual amino acid sequences were generated by SolubleMPNN, and other specialized protein models helped filter candidates for folding and binding. The lab validation showed binding evidence for all five targets, but the work still relies on specialized tools for sequence design and candidate selection.

🔗 [Source](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/)

hackernews · OpenAI Blog · Nov 24, 21:02 · [Discussion](https://news.ycombinator.com/item?id=50634658)

**Background**: Protein minibinders are small proteins engineered to bind tightly to specific target proteins, and they are typically designed using specialized deep learning models like RFdiffusion and ProteinMPNN. In a protein, the 3D structure determines function, and the amino acid sequence determines the structure, so designing a protein requires solving both the structure and sequence design problems. OpenAI's claim is that a general LLM can handle the structural design step by writing code, without being specifically trained on protein data.

<details><summary>References</summary>
<ul>
<li><a href="https://communities.springernature.com/posts/minibinders-tiny-proteins-with-huge-potential-in-bioengineering">Minibinders : Tiny Proteins with Huge Potential in Bioengineering</a></li>

</ul>
</details>

**Discussion**: Commenters were divided: some, like a Baker lab PhD, found the direction plausible and noted that fusing protein and language models was discussed years ago, while others questioned what GPT-6.2 actually designed since the sequences came from SolubleMPNN. A recurring theme was that code-writing is the models' superpower, enabling them to leverage existing scientific software rather than possessing intrinsic protein expertise.

**Tags**: `#AI`, `#protein-design`, `#GPT-6`, `#biotechnology`, `#machine-learning`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Check Point management servers hit by session cookie forgery attack</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

GreyNoise reported an active intrusion campaign against Check Point security management servers where attackers exploited a predictable JavaScript Math.random()-based session ID to reconstruct the V8 PRNG state and forge admin session cookies. The attack involved scanning and exploiting the HFS loginSrp1 endpoint to collect enough session IDs to recover the signing key. This incident highlights the dangers of using non-cryptographic random number generators for security-sensitive values, potentially allowing attackers to bypass authentication on critical security management servers. It affects organizations using Check Point Security Management Servers, which are central to managing firewall policies and could lead to full network compromise. The attack exploits the fact that V8's Math.random() uses a PRNG (xorshift128+) whose internal state can be reconstructed from consecutive outputs, enabling recovery of the session-cookie signing key. The initial access vector is suspected to be CVE-2026-16232, and the campaign targeted multiple Check Point customers, suggesting internet-exposed management servers.

🔗 [Source](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign)

hackernews · louiereederson · Nov 24, 16:32 · [Discussion](https://news.ycombinator.com/item?id=50630594)

**Background**: Check Point Security Management Servers are dedicated appliances that centrally manage security policies and objects for Check Point firewalls and gateways. JavaScript's Math.random() is not cryptographically secure; it uses a pseudo-random number generator (PRNG) whose internal state can be predicted from its outputs, making it unsuitable for security tokens. GreyNoise is a threat intelligence service that detects and classifies internet-wide scanning and attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://v8.dev/blog/math-random">There’s Math . random (), and then there’s Math . random () · V 8</a></li>
<li><a href="https://security.stackexchange.com/questions/84906/predicting-math-random-numbers">javascript - Predicting Math . random () numbers ? - Information...</a></li>
<li><a href="https://www.greynoise.io/">GreyNoise | Real-Time Network Threat Intelligence</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern about the broader implications, with some noting that LLM-driven cybercrime will make such attacks more common and others questioning why Math.random() isn't made secure by default. There was also speculation about the initial access vector and whether all affected organizations had their management servers exposed online.

**Tags**: `#security`, `#vulnerability`, `#prng`, `#check-point`, `#incident-response`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">GTA 6 Runs on Windows via Community Recompilation of Leaked Xbox Build</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A community project has demonstrated Grand Theft Auto 6 running on Windows by using a Wine-like recompilation approach on the leaked Xbox build of the game. The project, shared on Twitter, shows the game executable running on PC without official support from Rockstar. This feat highlights the growing capabilities of community-driven reverse engineering and recompilation, potentially pressuring developers to release official PC ports sooner. It also raises significant legal and ethical questions about game preservation and copyright in the absence of official releases. The approach leverages the fact that modern Xbox consoles are architecturally similar to Windows PCs, and the leaked binary lacks special DRM or obfuscation, simplifying compatibility work. Projects like xcl and VIctory are tackling graphics and system compatibility challenges.

🔗 [Source](https://twitter.com/raul_bs3/status/2125213756238291075)

hackernews · andrem · Nov 24, 13:19 · [Discussion](https://news.ycombinator.com/item?id=50627783)

**Background**: Wine is a compatibility layer that allows Windows applications to run on Unix-like systems by translating system calls, often used for running games on Linux. Game recompilation involves converting console binaries to run natively on PC, either through static recompilation or dynamic translation, and has been used for titles like Bayonetta 3 and Rocket: Robot on Wheels. The Xbox version of GTA 6 was leaked by a group called Cyberleek, first resources then the game binary, enabling these community efforts.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wine_compatibility_layer">Wine compatibility layer</a></li>
<li><a href="https://heldgames.com/guides/retro-decompilation-recompilation-explained">What Decompiled and Recompiled Games Actually Are... | Held Games</a></li>
<li><a href="https://www.retroreversing.com/xbox">Microsoft Xbox - Retro Reversing (Reverse Engineering)</a></li>

</ul>
</details>

**Discussion**: Commenters debated the legality and impact on game production, with some arguing that GTA 6's massive profitability means this won't harm Rockstar, while others raised concerns about future DRM and cloud-based components to prevent decompilation. Technical details about the leak and recompilation challenges were also shared, and related past Hacker News discussions were referenced.

**Tags**: `#game-recompilation`, `#reverse-engineering`, `#wine`, `#xbox-compatibility`, `#game-preservation`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Quad9 Pulls DNS Service from France Over Legal Constraints</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Quad9, a Swiss non-profit public DNS resolver, deactivated its service in France effective November 24, 2026, after French legal constraints made it impossible to continue operating. Users in France now receive a REFUSED response with an Extended DNS Error (EDE) code 18 indicating 'Prohibited: Service unavailable due to French legal constraints'. This withdrawal highlights the growing tension between government censorship mandates and global internet infrastructure, as France effectively makes it illegal for public DNS caches to operate without filtering. It sets a precedent that could pressure other public resolvers and affect internet privacy and openness far beyond France. Quad9's departure stems from a court order obtained by beIN Sports to block pirate sports streaming domains, which was expanded to require DNS blocking by public resolvers. Quad9 chose to exit rather than comply, and community members have set up alternative proxies (e.g., quad9.domainintelligence.uk) supporting DoH, DoT, and Do53 for affected users.

🔗 [Source](https://quad9.net/news/blog/quad9-service-deactivation-in-france/)

hackernews · farrokhi · Nov 24, 08:33 · [Discussion](https://news.ycombinator.com/item?id=50625384)

**Background**: Quad9 is a free public DNS service run by a Swiss non-profit foundation, offering privacy-focused resolution at 9.9.9.9 and encrypted DNS via DoH and DoT. DNS (Domain Name System) translates human-readable domain names into IP addresses, and public resolvers like Quad9, Google DNS, and Cloudflare are widely used as alternatives to ISP-provided DNS. France has increasingly required DNS blocking to combat piracy and other illegal content, and a court order can compel resolvers to filter domains, which conflicts with Quad9's no-filtering privacy model.

<details><summary>References</summary>
<ul>
<li><a href="https://quad9.net/">Quad 9 | A public and free DNS service for a better security and privacy</a></li>
<li><a href="https://techstackups.com/articles/quad9-leaves-france-dns-blocking/">Quad9 Is Leaving France : Why DNS Resolvers Are... | Tech Stackups</a></li>
<li><a href="https://en.wikipedia.org/wiki/DNS_over_HTTPS">DNS over HTTPS - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion shows strong concern that the French government effectively made DNS caches illegal, with commenters emphasizing this was not Quad9's choice. Users shared technical workarounds such as open proxies and noted verification of the shutdown via DNS queries returning REFUSED with EDE 18, while linking to earlier discussions and a TorrentFreak update on the expired piracy order.

**Tags**: `#DNS`, `#privacy`, `#censorship`, `#internet-infrastructure`, `#France`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Simon Willison identifies three LLM inflection points in twelve months</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

In a keynote at the AI Engineer Code Summit and a follow-up blog post, Simon Willison argues that LLMs and coding agents crossed three major capability inflection points in the past twelve months, anchored by the November 24, 2025 release of Claude Opus 4.5, which he says was the first model that made Claude Code reliably useful by default. The framing gives practitioners a concrete historical timeline for when AI coding tools shifted from error-prone assistants to dependable accelerants, which affects how teams plan adoption, tooling investment, and expectations for agent reliability. Willison notes that Claude Code was only nine months old when Opus 4.5 arrived, and that OpenAI's simultaneous GPT-5.1 Instant, Thinking, Codex, and Codex-Max releases had a similar effect on Codex; he also defines a new 'Fable class' of models that can solve problems with brute force when given a goal and tools, exemplified by Claude Fable 5's proactive behavior.

🔗 [Source](https://simonwillison.net/2026/Nov/24/llm-inflection-points/)

rss · Simon Willison · Nov 24, 23:02

**Background**: Claude is Anthropic's family of large language models, released in three tiers since Claude 3: Haiku, Sonnet, and Opus, with Opus being the most capable. Claude Code is Anthropic's terminal-based coding agent, introduced alongside Claude 3.7 Sonnet in February 2025. Coding agents are LLM-driven tools that can read code, run tests, diagnose failures, and propose or apply fixes with limited human intervention.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Opus_4.5">Claude Opus 4.5</a></li>
<li><a href="https://ai.engineer/code/2026">AI Engineer Code Summit 2026: AI Engineering Conference, Nov...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#coding-agents`, `#AI-engineering`, `#model-releases`, `#industry-analysis`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">GPT-6.2 Astra Solves 1808 Sketchbook Mystery in 22 Minutes</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

OpenAI's GPT-6.2 Astra autonomously identified the creator of an anonymous 1808 sketchbook held at Yale's Beinecke Library in just 22 minutes, using publicly available primary and secondary sources. The model discovered a little-known diary reference to a visit by the vicomte de Chabot and predicted that Chabot's travel journal, available only by order from Cleveland State University, would confirm the attribution—which it did. This case study demonstrates that agentic AI can autonomously conduct genuine historical research, potentially transforming how humanities scholars and archivists approach attribution and source discovery. It also raises questions about the evolving role of human historians as AI systems begin to perform tasks previously thought to require human expertise. The model used minimal prompting and relied on publicly available sources, including a digitized version of the sketchbook and a paper archive reference. The newly discovered source—Chabot's journal—is itself a significant find for Canadian and fur trade historians, and the entire process took only 22 minutes.

🔗 [Source](https://simonwillison.net/2026/Nov/24/astra-historical-mystery/)

rss · Simon Willison · Nov 24, 16:53

**Background**: GPT-6.2 Astra is OpenAI's frontier model released in November 2026 for complex, multistep projects, and it is available via API and Amazon Bedrock. The Beinecke Rare Book and Manuscript Library at Yale is a major repository of historical documents, and historical research typically involves analyzing primary sources (original documents) and secondary sources (interpretations). This case echoes the impact of Deep Blue on chess, prompting historian Mark Humphries to predict a mild 'crisis of confidence' among historians as agentic AI demonstrates capabilities beyond human researchers.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-2-astra-sol/">Introducing GPT-6.2 Astra and Sol | OpenAI</a></li>
<li><a href="https://beinecke.library.yale.edu/">Beinecke Library | Yale Library</a></li>
<li><a href="https://history.ucla.edu/primary-secondary-sources/">Primary & Secondary Sources - UCLA Department of History</a></li>

</ul>
</details>

**Tags**: `#AI`, `#historical research`, `#case study`, `#GPT-6.2`, `#archives`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Z.ai Releases GLM-5.4, Its First Loop Transformer Model</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Z.ai has released GLM-5.4, its first flagship model built on a looped transformer architecture, where a group of weight-shared layers runs for multiple iterations to deepen reasoning without increasing parameter count. The release follows Thinking Machines Lab's Inkling 2 Mini on November 20th, making it the second looped transformer announcement in a week. This signals an emerging architectural trend toward weight-shared iterative models that can achieve deeper reasoning at lower parameter cost, potentially reshaping how AI labs design efficient coding and agentic models. Practitioners focused on coding agents and efficient inference should pay close attention as more labs adopt this approach. GLM-5.4 is not yet available as open weights, with Z.ai stating it plans to open-source the model after safety hardening; it is currently accessible only through the Coding Plan subscription, which shares an OpenAI-compatible Responses API endpoint with the regular API. Simon Willison's pelican SVG test showed the model's output quality is comparable to OpenAI and Anthropic models, a stark style shift from earlier GLM generations.

🔗 [Source](https://simonwillison.net/2026/Nov/23/glm-54/)

rss · Simon Willison · Nov 23, 23:40

**Background**: A standard Transformer runs each layer once per forward pass, while a looped transformer reuses a group of weight-shared layers for multiple iterations, refining hidden states each time to simulate a deeper network without adding parameters. Weight sharing across layers has precedent in models like ALBERT, and recent research has explored looped architectures for improved reasoning and learning algorithms. Z.ai is a Chinese AI lab that has released successive GLM models, with GLM-5.4 positioned as the start of 'Generalized Coding' where code becomes a foundation for broader tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://z.ai/blog/glm-5.4">GLM-5.4: Toward Generalized Coding with Our First Loop ... - z.ai</a></li>
<li><a href="https://www.marktechpost.com/2026/11/23/zai-glm-5-4-loop-transformer/">Z AI Releases GLM-5.4: A 750B Loop Transformer ... - MarkTechPost</a></li>
<li><a href="https://www.emergentmind.com/topics/looped-transformer-architecture.md">emergentmind.com/topics/ looped - transformer - architecture .md</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#transformer-architecture`, `#model-release`, `#Z.ai`

</details>


<a id="item-11"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Ladybird browser ships first alpha for macOS and Linux</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

The Ladybird project released its first alpha on November 23, 2026, making the browser installable on macOS and Linux without requiring users to compile it from source. The release marks a major milestone for the independent browser, which implements its own HTML parser, CSS engine, layout, JavaScript, and WebAssembly components. Ladybird represents one of the few serious efforts to build a browser engine from scratch, offering a potential alternative to the Chromium, WebKit, and Gecko duopoly and helping preserve diversity in open web infrastructure. Its alpha release lowers the barrier for developers and users to test and contribute to a truly independent browser. Ladybird still relies on a few external libraries such as HarfBuzz for text shaping, Skia for 2D graphics, ffmpeg for video, and SQLite, while running each tab in a separate process for isolation. Early testing shows it handles WebAssembly-heavy tools like ffmpeg and Pyodide well, but some complex service-worker and web-worker arrangements, such as Datasette Lite, currently fail due to an unimplemented API.

🔗 [Source](https://simonwillison.net/2026/Nov/23/ladybird/)

rss · Simon Willison · Nov 23, 21:46

**Background**: Ladybird began as a browser for SerenityOS, a free and open-source desktop operating system started in 2018 by Andreas Kling, and later became an independent project. Building a browser engine from scratch is extremely rare because modern browsers rely on massive, mature codebases like Chromium's Blink or WebKit; Ladybird aims to implement most components itself, including HTML parsing, CSS, layout, JavaScript, and WebAssembly. HarfBuzz is an open-source text shaping library that converts Unicode text into properly positioned glyphs, while Skia is a widely used open-source 2D graphics library that powers Chrome, Android, and Flutter.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/HarfBuzz">HarfBuzz - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Skia_Graphics_Library">Skia Graphics Library</a></li>
<li><a href="https://en.wikipedia.org/wiki/SerenityOS">SerenityOS - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#browser`, `#ladybird`, `#open-source`, `#web-standards`, `#release`

</details>


<a id="item-12"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Songe: Fine-tune local LLMs on idle compute</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Sous Labs released Songe, an Apache-2.0 training engine that fine-tunes a user's local language model while the machine is idle, learning from corrections, stated preferences, and tool errors made during normal use. It offers a 'Quick Dream' that adds stated preferences to the model's instructions in minutes, and a 'Deep Dream' that trains a small adapter via on-policy distillation over an hour or more. This lowers the barrier to local model customization by turning everyday agent interactions into training data without sending anything off-device, which matters for privacy-conscious users and those with limited cloud budgets. It also opens a path toward continuous, personalized improvement of local AI assistants. The engine records tool results, errors, and user corrections during agent sessions and trains only while the machine is idle, so nothing leaves the local machine. The 'Deep Dream' mode uses on-policy distillation to train a small adapter, while 'Quick Dream' is a faster, instruction-level preference injection.

🔗 [Source](https://github.com/sous-labs/songe)

hackernews · bluepeter · Nov 24, 15:03 · [Discussion](https://news.ycombinator.com/item?id=50629231)

**Background**: Fine-tuning adapts a pre-trained large language model to specific tasks or preferences by further training it on domain-specific data. Traditional fine-tuning often requires uploading data to cloud services, raising privacy and cost concerns. Songe instead performs fine-tuning locally, using idle compute cycles, and leverages the model's own interactions as training signal. This aligns with the growing trend of local LLM deployment tools like Ollama and llama.cpp.

<details><summary>References</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/sous-labs-songe-fine-tunes-local-models-on-idle-compute">Sous Labs' Songe Fine-Tunes Local Models on Idle Compute</a></li>
<li><a href="https://ai-tldr.dev/tools/songe/">Songe: Local Model Training Engine, Install & How It Works</a></li>
<li><a href="https://daily.dev/posts/a-training-engine-for-your-local-model-using-your-idle-compute-psuafvv2g">A training engine for your local model, using your idle compute</a></li>

</ul>
</details>

**Discussion**: Commenters expressed enthusiasm for a 'SETI@home for LLMs' and asked about distributed training possibilities, rough improvement metrics per training epoch, and how improvement is judged. Others inquired about hardware requirements, specifically whether a GPU is necessary or if modest machines can benefit.

**Tags**: `#local-llm`, `#training-engine`, `#distributed-training`, `#open-source`, `#idle-compute`

</details>


<a id="item-13"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Splitting a USB-C port into separate USB 3 and USB 2 connections</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A blog post by Frank Chiarulli explains how to split a single USB-C port into separate USB 3 SuperSpeed and USB 2 connections, allowing both to operate simultaneously without a combined USB 3 hub chip. The technique leverages the fact that USB-C carries USB 2 (D+/D-) and USB 3 (TX/RX) as independent buses wired to distinct root ports on the host's xHCI controller. This approach can reduce bill-of-materials cost for embedded and DIY hardware projects by avoiding a more expensive USB 3 hub while still exposing both a high-speed USB 3 device and additional USB 2 devices through one connector. It is particularly relevant for designers of cameras, development boards, and compact peripherals who need multiple devices on a single USB-C port. The split works because USB 2 and USB 3 are physically separate differential pairs within the USB-C connector, but practical complications arise around power management: a host cutting power to a USB 3.x device typically needs to know which USB 2.x port that device is associated with, and the device tree or ACPI tables define these pairings. Community members also note that some cheap hubs exploit this by offering multiple USB 2.0 ports plus one USB 3.x port, where a device's position in the topology depends on whether it supports USB 2.0 or 3.x.

🔗 [Source](https://www.frankchiarulli.com/blog/splitting-usb-c/)

hackernews · fcjr · Nov 24, 14:54 · [Discussion](https://news.ycombinator.com/item?id=50629106)

**Background**: USB-C is a reversible 24-pin connector that can carry multiple protocols simultaneously, including USB 2.0, USB 3.x SuperSpeed, and alternate modes such as DisplayPort. USB 3.0 introduced a dual-bus architecture that retains the older USB 2.0 differential pair for backward compatibility while adding separate SuperSpeed transmit and receive lanes. Because these buses are independent, a USB-C port can expose them as two distinct logical connections to the host controller, which is the basis for the splitting technique described.

<details><summary>References</summary>
<ul>
<li><a href="https://daily.dev/posts/splitting-usb-c-usb-3-and-usb-2-on-one-port-2ayuldx32">Splitting USB-C: USB 3 and USB 2 on One Port - daily.dev</a></li>
<li><a href="https://www.frankchiarulli.com/blog/splitting-usb-c/">Splitting USB-C: USB 3 and USB 2 on One Port - frankchiarulli.com</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree the technique works but highlight power-management complications, such as the host needing to map USB 3.x devices to their paired USB 2.x ports for per-port power control. Others share BOM-cost tricks, like a USB-C port that changes functionality based on plug orientation, and reflect on the complexity of USB-C compared to the simplicity of USB-A's four pins. A recurring sentiment is that USB's backward compatibility approach—requiring a separate implementation of the old protocol alongside the new one—adds significant complexity.

**Tags**: `#USB-C`, `#hardware`, `#USB`, `#embedded systems`, `#power management`

</details>


<a id="item-14"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">iFood scales AI coding agents across 15,000 repositories</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

iFood, a Latin American delivery giant, has deployed a Remote Agents Platform that uses OpenAI's technology to automate coding tasks across its 15,000 code repositories. The platform centralizes routine engineering work such as dependency updates and code validation through an internal REST API, achieving an average inference cost of just $0.04 per run. This case demonstrates how AI coding agents can be scaled from single-repository assistants to company-wide infrastructure, potentially transforming software engineering workflows at large enterprises. It highlights a shift toward API-driven, cost-effective automation of routine coding tasks, which could free developers for higher-value work and set a precedent for other organizations. The Remote Agents Platform handles tasks like validating code against internal standards, fixing vulnerable dependencies, and running analyses, with an average inference cost of $0.04 per run. The solution addresses the challenge of scale, as solving for one repository is easy but managing 15,000 requires a centralized, API-driven approach.

🔗 [Source](https://openai.com/business/customer-stories/ifood)

rss · OpenAI Blog · Nov 24, 00:00

**Background**: AI coding agents are tools that use large language models to perform software engineering tasks autonomously, such as writing code, fixing bugs, or updating dependencies. Traditionally, these agents are used within a single repository or project, but scaling them across thousands of repositories requires orchestration, cost management, and integration with existing workflows. iFood's platform exemplifies an emerging trend of treating AI agents as enterprise infrastructure rather than isolated assistants.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/business/customer-stories/ifood/?from=bd_signal">How iFood scales coding agents across 15,000 repositories</a></li>
<li><a href="https://kongchang.com/en/articles/ifood-manages-15000-repositories-with-coding-agents-an-architectural-lesson-at-4-cents-per-run">iFood Manages 15,000 Repositories with Coding Agents: An ...</a></li>
<li><a href="https://grafy.ai/news/ifood-scales-coding-agents-across-15-000-repositories">iFood scales coding agents across 15,000 repositories - grafy.ai</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#coding assistants`, `#large-scale deployment`, `#software engineering`, `#OpenAI`

</details>


<a id="item-15"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">OpenAI and Cisco launch Shirudo, an open-source Linux security runtime</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

OpenAI and Cisco have released Shirudo, an open-source runtime for Linux that protects running systems while patches are being deployed. In a controlled test, a Codex-generated shield blocked a Java4Shell exploit attempt against a running Elasticsearch service without requiring a restart. This addresses a critical gap in patch management: the window between vulnerability disclosure and patch deployment, during which systems remain exposed. By providing temporary runtime protections, Shirudo could significantly reduce the risk of exploitation for organizations that cannot immediately patch, and it represents a notable collaboration between an AI company and a networking giant on open-source security infrastructure. Shirudo is built on eBPF, a technology that runs small custom programs inside the operating system kernel without changing its source code. The project is open source, and operators retain control over deployment; the controlled test involved a Java4Shell (CVSS 9.2) exploit against Elasticsearch.

🔗 [Source](https://openai.com/index/introducing-shirudo)

rss · OpenAI Blog · Nov 23, 21:20

**Background**: Patching Linux systems often requires restarts or downtime, and in large fleets, rolling out patches can take days or weeks. During that time, attackers can exploit known vulnerabilities. eBPF (extended Berkeley Packet Filter) allows sandboxed programs to run in the Linux kernel, enabling observability, networking, and security features without kernel modules. Shirudo uses eBPF to deploy temporary shields that block exploit attempts until permanent patches are applied.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-shirudo/">OpenAI and Cisco introduce Shirudo</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/new-shirudo-tool-uses-ai-to-shield-unpatched-linux-systems-from-exploits/">New Shirudo tool uses AI to shield unpatched Linux systems ...</a></li>
<li><a href="https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m11/cisco-and-openai-launch-shirudo-a-new-project-to-safeguard-agentic-ai.html">Cisco and OpenAI Launch Shirudo, A New Project to Safeguard</a></li>

</ul>
</details>

**Tags**: `#security`, `#open-source`, `#linux`, `#patching`, `#runtime`

</details>


<a id="item-16"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Microduck Obstacle Avoidance: A Sim2Real Workflow with Isaac Lab and Newton</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

The article presents a complete simulation-to-reality (Sim2Real) pipeline for microdrone obstacle avoidance using NVIDIA Isaac Lab and the Newton physics engine, covering training, deployment, and real-world validation. This work demonstrates a practical integration of simulation and real-world robotics, providing a valuable reference for robotics practitioners working on Sim2Real transfer and reinforcement learning for agile drones. The pipeline leverages Isaac Lab's GPU-accelerated simulation and Newton's differentiable physics for efficient training, and includes real-world validation on a microdrone, though the article does not claim a groundbreaking algorithmic breakthrough.

🔗 [Source](https://huggingface.co/blog/nvidia/microduck-obstacle-avoidance)

rss · Hugging Face Blog · Nov 24, 16:34

**Background**: Isaac Lab is an open-source modular framework for robot learning that simplifies reinforcement learning, learning from demonstrations, and motion planning in simulation. Newton is an open-source, GPU-accelerated, differentiable physics engine built on NVIDIA Warp and OpenUSD, developed by NVIDIA, Google DeepMind, and Disney Research, and managed by the Linux Foundation. Sim2Real refers to the challenge of transferring policies trained in simulation to real-world robots, where differences between simulated and real dynamics can cause failures.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/isaac/lab">Isaac Lab | NVIDIA Developer</a></li>
<li><a href="https://developer.nvidia.com/newton-physics">Newton Physics Engine | NVIDIA Developer</a></li>
<li><a href="https://newton-physics.github.io/newton/stable/guide/overview.html">Newton Physics Documentation — Newton Physics</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#sim2real`, `#reinforcement-learning`, `#isaac-lab`, `#obstacle-avoidance`

</details>


<a id="item-17"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">RoboTrack: Point tracking for real-world robotic manipulation</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

RoboTrack introduces a benchmark and training data suite for point tracking in robotic manipulation, including RoboTrack-Bench with 307 real-world clips and RoboTrack-15M with simulated training data. The method uses simulated manipulation data to improve point trackers on real robot video, enabling a robot to repeat a precise task from a single demonstration. This work addresses the gap between simulated and real-world robotic manipulation by providing a dedicated benchmark and training data, which could accelerate research in imitation learning and precise manipulation. It enables robots to learn from fewer demonstrations, potentially reducing the cost and time of programming robotic tasks. RoboTrack-Bench contains 307 clips of robots and people handling objects, with 2,522 point tracks, while RoboTrack-15M provides simulated training data from a Franka arm picking everyday objects in 300 procedurally generated environments. The approach leverages simulated data to improve tracking on real video, and the better tracks allow a robot to repeat a precise task from one demonstration.

🔗 [Source](https://huggingface.co/blog/allenai/robotrack)

rss · Hugging Face Blog · Nov 23, 17:20

**Background**: Point tracking is a computer vision task that estimates the movement of specific points in a video over time, and it is fundamental for applications in augmented reality and robotics. Recent methods like TAPIR and CoTracker have advanced tracking any point (TAP) in videos, but they are often trained on generic videos and may not perform well on robotic manipulation scenarios with fast motion and occlusions. RoboTrack addresses this by providing domain-specific data and a benchmark to evaluate and improve point trackers for real-world robotic manipulation.

**Tags**: `#robotics`, `#point tracking`, `#manipulation`, `#computer vision`, `#AI`

</details>


</section>