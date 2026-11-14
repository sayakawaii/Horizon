---
layout: default
title: "Horizon Summary: 2026-11-14 (EN)"
date: 2026-11-14
lang: en
---

> From 112 items, 10 important content pieces were selected

---

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (10)

<a id="item-1"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">SpaceX catches Starship booster with chopstick arms on Flight 15</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

SpaceX successfully caught the Super Heavy booster of its Starship rocket using the launch tower's mechanical 'chopstick' arms at the end of Flight 15, marking the first time the booster was recovered intact on land. This milestone demonstrates full reusability of the Super Heavy booster, a key step toward dramatically lowering the cost of access to space and enabling frequent, rapid re-flights. The catch occurred after the booster separated from the Starship upper stage and performed a controlled descent back to the launch site; the ship itself continued to orbit and deployed 26 Starlink satellites before returning.

🔗 [Source](https://x.com/i/broadcasts/2brajgZlOKRMka)

hackernews · ls612 · Nov 14, 21:22 · [Discussion](https://news.ycombinator.com/item?id=50500963)

**Background**: Starship is SpaceX's next-generation fully reusable launch system, consisting of the Super Heavy booster and the Starship spacecraft. The 'chopstick' arms on the launch tower are designed to catch the booster mid-air, eliminating the need for landing legs and enabling faster reuse. Previous test flights have progressively pushed the envelope, from initial hops to orbital attempts and now booster recovery.

<details><summary>References</summary>
<ul>
<li><a href="https://apnews.com/article/spacex-elon-musk-starship-rocket-df394c1b5a0f85e11194f9ff7db9ee6b">SpaceX’s Starship returns from orbit and is captured by ...</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/spacex-starship-flight-15-chopsticks-double-catch-super-heavy-ship">SpaceX launches Starship on ambitious 22-hour Flight 15 test... | Space</a></li>
<li><a href="https://thespaceroad.com/articles/how-does-starship-catch-work/">How does the Starship catch work? | The Space Road</a></li>

</ul>
</details>

**Discussion**: The Hacker News community reacted with overwhelming enthusiasm, calling it a historic achievement that could usher in a new era of cheap spaceflight. Commenters highlighted the potential for double catches and re-flights, while some noted the engineering challenges and the long road to full reusability.

**Tags**: `#spacex`, `#starship`, `#reusable-rockets`, `#aerospace`, `#engineering`

</details>


<a id="item-2"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">llama.cpp Reaches v1.0.0, Strengthening Local AI Inference</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

The llama.cpp project, a widely used open-source library for running large language models locally, has released version 1.0.0, marking its first major stable milestone since its creation in March 2023. Reaching v1.0.0 signals maturity and stability for a project that has become the de facto standard underlying many local AI tools, including Ollama and LM Studio, and could encourage broader adoption in production and enterprise environments. llama.cpp is co-developed with the GGML tensor library and uses the GGUF file format, which stores tensors and metadata in a single file for fast loading and backward compatibility across model architectures.

🔗 [Source](https://huggingface.co/blog/ggml-org/llama-cpp-v1)

rss · Hugging Face Blog · Nov 13, 14:05

**Background**: llama.cpp is an open-source C/C++ library that performs inference on large language models such as Meta's Llama entirely on-device, without relying on cloud services. It was started by Georgi Gerganov in March 2023 and is co-developed alongside the GGML project, a general-purpose tensor library. The library includes command-line tools and a server with a simple web interface, and it has become the core of almost all local inference tools. The GGUF format, introduced in August 2023, superseded earlier formats to better maintain compatibility as support for new model architectures was added.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://en.wikipedia.org/wiki/GGUF">GGUF - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/llamacpp">llama.cpp</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#local AI`, `#inference`, `#open source`, `#AI/ML`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Lovable apps leak passports and 200K messages via weak RLS</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A security researcher at Crissy Field published findings that apps built with the AI app builder Lovable exposed sensitive data, including passport details and more than 200,000 private messages, because the underlying Supabase database tables lacked sufficient Row-Level Security (RLS) policies. The post gained major traction on Hacker News, drawing a public response from Lovable's Head of Security. This incident shows how insecure defaults in AI-generated apps can cause real data breaches at scale, putting pressure on both AI app builders like Lovable and database platforms like Supabase to ship secure-by-default configurations. It also highlights that non-expert users of no-code AI tools may unknowingly deploy publicly readable databases. The root cause was insufficient RLS on Supabase tables, which by default are readable and writable by any role with a grant unless RLS is explicitly enabled. Lovable says it automatically scans every app before publishing and offers a free deeper SAST scan, with options to fix findings or enable auto-fix, while commenters note Supabase's historical permissive defaults may still affect existing projects.

🔗 [Source](https://www.crissyfield.de/research/lovable-en/)

hackernews · armcat · Nov 14, 17:43 · [Discussion](https://news.ycombinator.com/item?id=50499017)

**Background**: Lovable is an AI app builder that generates full applications, including database backends, from natural-language prompts, and it commonly uses Supabase, a Postgres-based backend-as-a-service, for data storage. Row-Level Security is a PostgreSQL feature that restricts which rows a user can access based on policies; without it, an exposed table can be read or written by anyone with API access. Because AI-generated apps often skip or misconfigure these policies, security researchers have warned that such apps are frequently insecure by default.

<details><summary>References</summary>
<ul>
<li><a href="https://supabase.com/docs/guides/database/postgres/row-level-security">Row Level Security - Supabase Docs</a></li>
<li><a href="https://lovable.dev/">App & Website Builder | Build Software in Minutes | Lovable</a></li>
<li><a href="https://bubble.io/blog/ai-generated-code-security/">AI-Generated Code Security: Risks and How to Fix Them - Bubble</a></li>

</ul>
</details>

**Discussion**: Commenters debated shared responsibility: some argued Supabase deserves blame for historically permissive defaults that may still apply to existing projects, while others said platforms need deny-by-default databases, least-privilege APIs, and automated auth tests to make insecure AI-generated deployments difficult. Lovable's Head of Security participated, explaining that insufficient RLS was the root cause and describing the company's scanning and auto-fix features, and the blog author also joined the thread.

**Tags**: `#security`, `#supabase`, `#row-level-security`, `#ai-generated-apps`, `#data-breach`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Project Zero to cut vulnerability disclosure deadline from 90 to 30 days by 2028</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Google Project Zero announced a phased reduction of its vulnerability disclosure deadline: starting today it adopts a "Full 90" policy, moving to "Full 60" on February 2, 2027, and "Full 30" on January 3, 2028, meaning vulnerabilities will be publicly disclosed 30 days after being reported to vendors. This is a significant policy shift that pressures vendors to patch faster and could reshape industry norms around coordinated vulnerability disclosure, affecting how software companies and open-source projects prioritize security fixes. The current policy is a 90+30 model giving vendors 90 days plus a 30-day grace period; the new timeline removes that buffer and compresses the window to 30 days by 2028, though Project Zero's FAQ notes some issues (e.g., hardware vulnerabilities) may be treated differently.

🔗 [Source](https://projectzero.google/2026/11/disclosure-policy.html)

hackernews · hacb · Nov 14, 11:13 · [Discussion](https://news.ycombinator.com/item?id=50496051)

**Background**: Project Zero is Google's security research team that finds zero-day vulnerabilities and reports them to vendors. Coordinated vulnerability disclosure gives vendors time to patch before details go public, balancing user protection with transparency. The 90-day deadline has been an industry benchmark, but critics argue it can be too short for complex fixes or too long for urgent threats.

<details><summary>References</summary>
<ul>
<li><a href="https://projectzero.google/vulnerability-disclosure-faq.html">Vulnerability Disclosure FAQ - Project Zero</a></li>
<li><a href="https://googleprojectzero.blogspot.com/p/vulnerability-disclosure-policy.html">Project Zero : Vulnerability Disclosure Policy</a></li>
<li><a href="https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure">Coordinated vulnerability disclosure - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters debated the policy's implications, with one raising concerns that vendors might leverage faster disclosure to push adoption of their own LLM-based security tools, and another noting the novelty of the .google TLD.

**Tags**: `#vulnerability-disclosure`, `#security`, `#project-zero`, `#policy`, `#software-engineering`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">OpenAI launches ChatGPT Wallet for agent purchases</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

OpenAI introduced ChatGPT Wallet, a secure payment mechanism that allows agents in ChatGPT Work, Codex, and dots to complete purchases with user approval and existing card protections. This marks a significant step toward agentic commerce, where AI agents can autonomously handle financial transactions on behalf of users, potentially transforming how people shop and manage payments online. The wallet requires explicit user approval for each purchase and leverages existing card protections, ensuring security and user control; it is integrated across ChatGPT Work, Codex, and dots, though specific technical details and availability are not yet disclosed.

🔗 [Source](https://openai.com/index/introducing-chatgpt-wallet)

rss · OpenAI Blog · Nov 13, 15:00

**Background**: ChatGPT Work is OpenAI's collaborative AI workspace for teams, Codex is an AI coding agent that runs locally or in the cloud, and dots are always-on personal agents introduced in September 2026. Agentic commerce refers to AI agents that can autonomously perform shopping and payment tasks, a growing trend among major tech companies.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/chatgpt-work/">ChatGPT Work for every team | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex">OpenAI Codex - Wikipedia</a></li>
<li><a href="https://openai.com/index/introducing-dots/">Introducing dots - OpenAI</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI agents`, `#payments`, `#agentic commerce`, `#product announcement`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">PyPI launches redesigned project pages with clearer security signals</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

PyPI has completed a redesign of its project pages, now live, that surfaces clearer security and provenance signals for each package release. The update highlights attestations and other trust indicators directly on the files section of project pages. Because PyPI is the default package registry for the Python ecosystem, making provenance and security signals more visible could encourage maintainers to adopt trusted publishing and sigstore-based signing, improving supply-chain security for millions of downstream users. It also shifts more responsibility onto package consumers to interpret these signals correctly. Provenance on PyPI is shared via attestations that record build and publishing details, and the new UI makes it easy to compare packages with and without them—for example, dlt currently shows no provenance while datasette does. However, provenance only verifies where a release came from; it does not detect malicious projects that were never benign.

🔗 [Source](https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/)

hackernews · rbanffy · Nov 14, 15:40 · [Discussion](https://news.ycombinator.com/item?id=50497892)

**Background**: Provenance describes where a release file came from, typically via attestations that provide a verifiable record of the build or publishing process. Sigstore is an open-source project that enables keyless signing using short-lived certificates tied to OIDC identities, making it easier for CI/CD pipelines to sign artifacts without managing long-lived private keys. Trusted publishing lets maintainers publish packages directly from CI providers like GitHub Actions without storing API tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.pypi.org/using-pypi/package-security/provenance/">Checking Provenance (package origin) - PyPI Docs</a></li>
<li><a href="https://www.sigstore.dev/">Home · Sigstore</a></li>
<li><a href="https://docs.pypi.org/using-pypi/pypi-basics/">PyPI Basics - PyPI User Documentation</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed the visibility of provenance but raised concerns that the trust model centralizes on big cloud CI providers and promotes lock-in, which some see as anti-Pythonic. Others highlighted gaps such as trusted publishing not yet supporting reusable workflows, and one commenter stressed that provenance detects compromised entries rather than malicious projects.

**Tags**: `#pypi`, `#supply-chain-security`, `#sigstore`, `#provenance`, `#package-management`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Minimal DeepSeek V3 inference in ~200 lines of pure JAX</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A developer released a ~190-line pure JAX implementation of DeepSeek V3 inference on GitHub, reimplementing its three key ideas: Multi-head Latent Attention, mixture-of-experts with bias-based load balancing, and multi-token prediction. The model is a 36.2M-parameter version trained on a MacBook Air M5 using jax-metal on 207 detective novels, taking about 2.6 hours for 12,000 steps. This project offers an educational, from-scratch implementation that helps developers understand modern LLM inference without the complexity of full-scale frameworks. A community member confirmed it ran end-to-end on an AMD RX 7600 XT 16GB GPU using ROCm, demonstrating practical value for consumer AMD hardware users. The implementation is about 190 lines and focuses on inference, not full-scale training; the trained model is a small 36.2M-parameter version, not the full 671B-parameter DeepSeek V3. For AMD RX 7600 XT, users need to set environment variables like HSA_OVERRIDE_GFX_VERSION=11.0.0 to work around JAX plugin issues.

🔗 [Source](https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax)

hackernews · VaibhaavTiwari · Nov 14, 15:04 · [Discussion](https://news.ycombinator.com/item?id=50497589)

**Background**: DeepSeek V3 is a large language model known for its efficient architecture, including Multi-head Latent Attention (MLA) and a mixture-of-experts (MoE) design with auxiliary-loss-free load balancing. JAX is a Python library for high-performance numerical computing and automatic differentiation, often used for machine learning research. ROCm is AMD's open-source software stack for GPU programming, serving as an alternative to NVIDIA's CUDA.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/DeepSeek-V3">GitHub - deepseek -ai/ DeepSeek - V 3 · GitHub</a></li>
<li><a href="https://docs.jax.dev/en/latest/automatic-differentiation.html">Automatic differentiation — JAX documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/ROCm">ROCm - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The discussion is positive and enthusiastic, with users praising the educational value of rebuilding a model from first principles. One user reported successfully running the project end-to-end on an AMD RX 7600 XT 16GB with ROCm, sharing gotchas about environment variables, while others asked for roadmaps to build intuition about inference.

**Tags**: `#jax`, `#deepseek`, `#llm-inference`, `#show-hn`, `#rocm`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">LinkedIn and Monster Remove Over 1,000 Fake Job Postings After CBC Investigation</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Following a CBC investigation, LinkedIn and Monster have taken down more than 1,000 fake job postings that were part of recruitment scams targeting job seekers. This highlights the growing problem of online job scams and raises questions about platform accountability for fraudulent listings, affecting millions of job seekers who rely on these platforms. The investigation likely uncovered a network of fake postings designed to collect personal information or money from applicants; platforms removed the listings but the scale suggests systemic issues in moderation.

🔗 [Source](https://www.cbc.ca/news/canada/linkedin-monster-take-down-over-1-000-fake-job-postings-after-cbc-investigation-9.7415379)

hackernews · gnabgib · Nov 14, 18:56 · [Discussion](https://news.ycombinator.com/item?id=50499723)

**Background**: Fake job postings are a common form of online fraud where scammers impersonate employers to steal personal data or money from job seekers. Platforms like LinkedIn and Monster have struggled to police such listings, which can be generated at scale using AI and other automated tools.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gem.com/blog/recruitment-fraud">Recruitment fraud: What you need to know - Gem</a></li>
<li><a href="https://www.bbb.org/scams/employment">Employment scams - Better Business Bureau</a></li>

</ul>
</details>

**Discussion**: Commenters shared personal experiences with job scams, expressed frustration with platforms like LinkedIn, and debated the broader prevalence of scams in the online economy, with some noting that even legitimate industries can feel scam-like.

**Tags**: `#job-scams`, `#platform-accountability`, `#online-fraud`, `#linkedin`, `#security`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">EFF Warns Tech Companies Are Redefining Privacy Again</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

The Electronic Frontier Foundation (EFF) published an analysis arguing that tech companies are once again attempting to shift the entire concept of privacy, likely to normalize extensive data collection and AI-driven surveillance. The piece sparked a substantive Hacker News discussion (423 points, 162 comments) focused on workplace AI surveillance and individual countermeasures. This matters because the framing of privacy shapes laws, product designs, and social norms; if companies succeed in redefining privacy as mere consent to data collection, workers and consumers may lose meaningful control over their personal information. The strong community response highlights growing unease with AI meeting recorders and always-on monitoring in professional settings. The EFF analysis does not propose a specific technical fix but critiques the rhetorical shift; commenters note that AI notetakers now record even 1:1 manager meetings, making opt-out practically impossible without risking employment. Legal frameworks like the UN Declaration of Human Rights Article 12 are cited by community members as a counterweight to corporate data practices.

🔗 [Source](https://www.eff.org/deeplinks/2026/11/tech-companies-are-trying-shift-entire-concept-privacy-again)

hackernews · gslin · Nov 14, 12:45 · [Discussion](https://news.ycombinator.com/item?id=50496602)

**Background**: The EFF is a nonprofit digital rights group that has long advocated for privacy and free expression online. In recent years, AI-powered meeting transcription and workplace monitoring tools have become widespread, raising concerns about consent and data retention. The Hacker News discussion reflects a broader debate over how much surveillance employees should tolerate as a condition of modern employment.

<details><summary>References</summary>
<ul>
<li><a href="https://thenarrativepost.com/ai-surveillance-2026-workplace-privacy-crisis/">AI Workplace Surveillance: 2026 Privacy Crisis?</a></li>
<li><a href="https://www.apa.org/monitor/2026/11-12/hidden-costs-workplace-surveillance">The hidden costs of workplace surveillance</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration that AI recording in meetings is becoming unavoidable, with one asking how to minimize exposure and whether it is acceptable to request that AI notetakers be turned off. Others cited the UN Universal Declaration of Human Rights and criticized tech companies for ignoring user consent, while some suggested practical steps like using throwaway identities and supporting advocacy organizations such as EFF.

**Tags**: `#privacy`, `#surveillance`, `#AI`, `#EFF`, `#policy`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">XYBench Tests Whether LLMs Can Infer the Real Problem Behind a Question</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

AI2 and Hugging Face have released XYBench, an 8,115-question benchmark that evaluates whether large language models can identify misconceptions in user requests and redirect users toward their underlying goal rather than answering the literal question. The benchmark draws from real Stack Overflow and Stack Exchange conversations, synthetically constructed WikiHow scenarios, and a manually curated set of everyday-domain queries. Most LLM benchmarks reward answering the stated question, so they miss a common real-world failure mode where a user asks for the wrong thing and a helpful assistant should push back. XYBench adds a pragmatic-helpfulness dimension to model evaluation, which matters for developers building assistants that need to correct users rather than simply comply. The benchmark is built around the 'XY problem,' where a user asks how to do X but actually needs to solve Y; models must detect the misconception and redirect toward a pragmatic solution. It combines real forum data, synthetic WikiHow-derived queries, and a manually curated everyday subset, and is documented in arXiv paper 2609.06842.

🔗 [Source](https://huggingface.co/blog/allenai/xybench)

rss · Hugging Face Blog · Nov 13, 17:02

**Background**: The XY problem is a well-known pattern in technical support: a user asks about their attempted solution (X) instead of their actual goal (Y), leading helpers down the wrong path. LLM benchmarks have traditionally measured accuracy on well-posed questions, so they do not capture whether a model can recognize that a question itself is misguided. XYBench is designed to fill that gap by scoring models on pragmatic redirection rather than literal answer quality.

<details><summary>References</summary>
<ul>
<li><a href="https://allenai.org/blog/xybench">XYBench: Helping with the problem behind the question | Ai2</a></li>
<li><a href="https://arxiv.org/abs/2609.06842">[2609.06842] XYBench: Can LLMs Respond Pragmatically to ...</a></li>
<li><a href="https://arxiv.org/pdf/2609.06842">XYBench: Can LLMs Respond Pragmatically to Queries with ...</a></li>

</ul>
</details>

**Tags**: `#benchmark`, `#LLM evaluation`, `#AI/ML`, `#question answering`, `#Hugging Face`

</details>


</section>