---
layout: default
title: "Horizon Summary: 2026-07-11 (EN)"
date: 2026-07-11
lang: en
---

> From 102 items, 11 important content pieces were selected

---

<section class="cat cat-finance" markdown="1">

## 💹 Finance & Markets (1)

<a id="item-1"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Circular Financing in the GPU Boom: Nvidia, CoreWeave, Nebius</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

An analysis reveals that Nvidia, CoreWeave, and Nebius are engaged in circular financing, where Nvidia invests in cloud companies that then use the funds to buy Nvidia's GPUs, fueling the AI infrastructure boom. This financing model raises concerns about sustainability and economic risk, as it may inflate demand and lead to overbuilding of data centers, potentially echoing the dot-com bubble. Nvidia invested $2 billion in CoreWeave for a 9% equity stake, while CoreWeave plans $35 billion in CapEx for 2026, meaning Nvidia's investment covers only 5.7% of that spending. The rest comes from other sources, challenging the notion of purely circular financing.

🔗 [Source](https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom)

hackernews · adletbalzhanov · Jul 11, 17:21 · [Discussion](https://news.ycombinator.com/item?id=48873836)

**Background**: Circular financing is a looped funding arrangement where an investor provides capital to a company, and that company then spends the money on the investor's products or services. In the AI industry, examples include Microsoft's $10 billion investment in OpenAI, which committed to using Azure. This model has drawn comparisons to the dot-com era.

<details><summary>References</summary>
<ul>
<li><a href="https://builtin.com/articles/ai-circular-financing">How Circular Financing Is Fueling the AI Boom | Built In</a></li>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nebius_Group">Nebius Group - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters debate whether the financing is truly circular, noting Nvidia's investment is a small fraction of CoreWeave's CapEx. Some question the economic profitability of AI infrastructure builds, while others warn of overbuild risks and potential economic fallout similar to the 2008 financial crisis.

**Tags**: `#AI infrastructure`, `#GPU boom`, `#circular financing`, `#Nvidia`, `#datacenter economics`

</details>


</section>

<section class="cat cat-science" markdown="1">

## 🧪 Science (1)

<a id="item-2"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Relativity governs chemical bonds in heavy elements</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

New research published in Science shows that Einstein's theory of relativity, specifically spin-orbit coupling, dominates the chemical bonding in heavy elements, overturning traditional quantum chemistry models that treat spin and orbit independently. This finding reshapes our fundamental understanding of chemical bonding for heavy elements, which is crucial for fields like materials science, catalysis, and nuclear chemistry. It also validates that relativistic effects are not just corrections but the primary force in these systems. The research demonstrates that for heavy elements, electron spin and orbital motion are strongly coupled (spin-orbit coupling), leading to bond types (sigma and pi bonds) that differ from lighter elements. The study provides direct experimental evidence for this relativistic bonding regime.

🔗 [Source](https://www.brown.edu/news/2026-07-09/chemical-bonds-relativity)

hackernews · hhs · Jul 10, 22:30 · [Discussion](https://news.ycombinator.com/item?id=48866134)

**Background**: In quantum chemistry, chemical bonds are typically described by non-relativistic Schrödinger equations, which work well for light elements. However, for heavy elements like gold or mercury, electrons near the nucleus travel at a significant fraction of the speed of light, making relativistic effects important. Spin-orbit coupling, a relativistic effect, links an electron's spin to its orbital motion, altering energy levels and bonding behavior. Previous work had shown relativistic effects on properties like gold's color, but this study directly links them to chemical bond formation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.brown.edu/news/2026-07-09/chemical-bonds-relativity">Einstein’s relativity rules chemical bonds in heavy elements , new...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Relativistic_quantum_chemistry">Relativistic quantum chemistry - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the idea of relativistic effects in heavy elements is not entirely new, citing examples like gold's color and mercury's liquid state. However, they appreciated the direct experimental evidence linking relativity to chemical bond formation. Some users provided additional context, such as the periodic table's shape arising from spherical symmetry, and expressed admiration for Einstein's continued relevance.

**Tags**: `#physics`, `#chemistry`, `#relativity`, `#quantum mechanics`, `#heavy elements`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (9)

<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">vLLM v0.25.0: MRv2 Default, PagedAttention Removed</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

vLLM v0.25.0 makes Model Runner V2 (MRv2) the default execution path for all dense models and removes the legacy PagedAttention implementation. It also adds new models like LLaVA-OneVision-2 and GLM-5, introduces a Streaming Parser Engine, and delivers performance improvements including a Transformers backend now as fast as native vLLM. This release marks a major architectural shift for vLLM, simplifying the codebase by removing PagedAttention and standardizing on MRv2, which improves maintainability and performance. The new models and optimizations expand vLLM's applicability to a wider range of LLM workloads, benefiting the AI/ML community that relies on vLLM for efficient inference. MRv2 now supports EVS (efficient variable-size sequences), realtime embeddings, prefix caching for Mamba hybrid models, and dynamic speculative decoding with full CUDA graphs. The Transformers backend gained FP8 MoE support and CUDA graph fixes, and the new Streaming Parser Engine unifies tool-call and reasoning parsing.

🔗 [Source](https://github.com/vllm-project/vllm/releases/tag/v0.25.0)

github · khluu · Jul 11, 20:06

**Background**: vLLM is an open-source high-throughput LLM inference engine that uses PagedAttention for efficient memory management of KV caches. Model Runner V2 is a newer execution backend that improves performance and flexibility. This release consolidates vLLM's architecture by making MRv2 the default and removing the older PagedAttention code.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm -project/ vllm</a></li>
<li><a href="https://docs.vllm.ai/en/latest/models/supported_models/">Supported Models - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#open source`, `#AI/ML`, `#release notes`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">ClickHouse scales PgBouncer to 4x throughput</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

ClickHouse detailed how they scaled PgBouncer to 4x throughput using SO_REUSEPORT and query cancel peering. This optimization significantly improves PostgreSQL connection pooling performance, benefiting large-scale deployments that rely on PgBouncer. SO_REUSEPORT allows multiple PgBouncer processes to share the same port, while peering forwards cancel requests to the correct process, solving a key bottleneck.

🔗 [Source](https://clickhouse.com/blog/pgbouncer-clickhouse-managed-postgres)

hackernews · saisrirampur · Jul 11, 15:28 · [Discussion](https://news.ycombinator.com/item?id=48872874)

**Background**: PgBouncer is a lightweight connection pooler for PostgreSQL. Without peering, a cancel request may land on a process that doesn't own the query, causing it to be ignored. SO_REUSEPORT is a socket option that enables multiple sockets to bind to the same port, distributing incoming connections across processes.

<details><summary>References</summary>
<ul>
<li><a href="https://stackoverflow.com/questions/14388706/how-do-so-reuseaddr-and-so-reuseport-differ">How do SO_REUSEADDR and SO_REUSEPORT differ? - Stack Overflow</a></li>
<li><a href="https://lwn.net/Articles/542629/">The SO_REUSEPORT socket option [LWN.net]</a></li>
<li><a href="https://dataegret.com/2024/08/handling_cancellation_request/">Handling Cancellation Request - Data Egret</a></li>

</ul>
</details>

**Discussion**: Commenters suggested alternative solutions like Odyssey and pgdog, and asked whether peering is built into PgBouncer. The discussion reflects interest in scalable PgBouncer alternatives and practical deployment details.

**Tags**: `#PostgreSQL`, `#PgBouncer`, `#scaling`, `#connection pooling`, `#ClickHouse`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Apple sues OpenAI over trade secret theft</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Apple filed a lawsuit against OpenAI, alleging that the company systematically stole trade secrets by recruiting former Apple employees who emailed confidential information to themselves and instructed new hires to conceal their employment. This lawsuit could set a precedent for how AI companies handle trade secrets and employee mobility, potentially reshaping hiring practices in the tech industry. It also highlights the growing tension between established tech giants and AI startups over intellectual property. Apple claims OpenAI used confidential Apple hardware information when approaching Apple suppliers and tricked suppliers into believing OpenAI had Apple's support. The lawsuit also alleges that OpenAI instructed new hires not to disclose their new job to Apple to prolong their access.

🔗 [Source](https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/)

hackernews · stock_toaster · Jul 10, 20:47 · [Discussion](https://news.ycombinator.com/item?id=48865019)

**Background**: Trade secret theft lawsuits are common in the tech industry, but this case involves two of the most prominent AI players. Apple has long prioritized secrecy in its hardware development, while OpenAI has faced criticism for its data practices. The outcome could influence how companies protect proprietary information in the age of AI.

**Discussion**: Commenters largely side with Apple, calling OpenAI's actions 'damning' and predicting severe consequences, such as the end of OpenAI's hardware ambitions. Some express concern that this reflects a broader pattern of OpenAI disregarding intellectual property laws, and advise businesses to avoid using OpenAI models due to potential IP risks.

**Tags**: `#Apple`, `#OpenAI`, `#lawsuit`, `#trade secrets`, `#AI ethics`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Hotz warns of AI censorship in 2040 essay</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

George Hotz published a blog post titled 'AI 2040 and the cult of intelligence,' arguing against AI censorship and warning that large language models could enforce ideological conformity. The post has sparked intense debate on the balance between free speech and AI safety, highlighting concerns about LLMs being used to suppress dissent and log 'thoughtcrime.' Hotz argues that unrestricted access to information is a First Amendment issue, but commenters note that this logic fails when AI agents take real-world actions, such as hacking a car.

🔗 [Source](https://geohot.github.io//blog/jekyll/update/2026/07/11/ai-2040.html)

hackernews · rvz · Jul 11, 18:04 · [Discussion](https://news.ycombinator.com/item?id=48874200)

**Background**: Large language models (LLMs) like GPT-4 are increasingly used in chatbots and agents. Companies often implement safety filters to prevent harmful outputs, but critics argue this amounts to censorship. The debate mirrors longstanding tensions between security and liberty.

**Discussion**: Commenters are divided: some agree with Hotz on free speech grounds, while others argue that AI agents capable of real-world harm require limits. A key concern is the potential for invisible bias injection and logging of 'thoughtcrime.'

**Tags**: `#AI safety`, `#censorship`, `#free speech`, `#LLM`, `#ethics`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Ant: A New JavaScript Runtime and Ecosystem</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Ant is a new JavaScript runtime built from scratch with its own engine, package manager, registry, deployment platform, and desktop app framework, aiming to be a coherent alternative to existing JavaScript stacks. This project represents a significant technical undertaking that could provide a more integrated and efficient development experience, potentially challenging established ecosystems like Node.js and Deno. Ant uses a custom bytecode virtual machine (Silver VM) and is written in C, with a focus on lightweight and high performance. It also includes Ant Desktop for building native desktop apps, similar to Electron.

🔗 [Source](https://antjs.org/)

hackernews · theMackabu · Jul 11, 20:07 · [Discussion](https://news.ycombinator.com/item?id=48875377)

**Background**: JavaScript runtimes like Node.js and Deno execute JavaScript outside the browser. Most runtimes use the V8 engine (from Chrome) or SpiderMonkey (from Firefox). Ant introduces its own engine, which is rare and ambitious. The project also includes a package registry (ants.land) and a deployment platform, aiming for an end-to-end solution.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/themackabu/ant">GitHub - theMackabu/ ant : javascript for 's, a tiny runtime with big...</a></li>
<li><a href="https://deepwiki.com/theMackabu/ant">theMackabu/ ant | DeepWiki</a></li>

</ul>
</details>

**Discussion**: Community comments raised concerns about the project's origins, noting that early versions relied on an existing AGPL codebase (Elk), though the author claims to have rewritten it since. There were also naming conflicts with Apache Ant and Anthropic's ant CLI. Some commenters saw potential for FaaS due to sandboxing and fast startup.

**Tags**: `#JavaScript`, `#runtime`, `#ecosystem`, `#web development`, `#open source`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Prefer strict tables in SQLite for type safety</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

An article advocates using STRICT tables in SQLite, introduced in version 3.37.0 (2021-11-27), to enforce rigid type checking and prevent accidental data type mismatches. This matters because SQLite's default dynamic typing can lead to subtle bugs, especially in multi-application or long-lived databases; adopting STRICT tables improves data integrity and reduces debugging effort. STRICT tables reject values that do not match the declared column type (e.g., inserting a string into an INTEGER column fails), and they support only a subset of types: INT, INTEGER, REAL, TEXT, BLOB, and ANY.

🔗 [Source](https://evanhahn.com/prefer-strict-tables-in-sqlite/)

hackernews · ingve · Jul 11, 17:33 · [Discussion](https://news.ycombinator.com/item?id=48873940)

**Background**: SQLite traditionally uses dynamic typing (type affinity), where column types are hints rather than strict rules. This flexibility allows inserting any value into any column, which can cause unexpected behavior. STRICT tables, introduced in SQLite 3.37.0, enforce static typing similar to traditional SQL databases, providing stronger guarantees.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sqlite.org/stricttables.html">STRICT Tables</a></li>
<li><a href="https://antonz.org/sqlite-strict-tables/">STRICT tables in SQLite</a></li>
<li><a href="https://sqlite.org/datatype3.html">Datatypes In SQLite</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree that STRICT tables should be the default, citing benefits like preventing UUID-to-number conversion bugs. Some note that SQLite's flexibility is useful for embedded single-application use cases, but for shared databases, strict typing is preferred.

**Tags**: `#SQLite`, `#database`, `#type safety`, `#best practices`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Nilay Patel: AR Glasses Require Always-On Cameras, Cloud Processing</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Nilay Patel argues that practical augmented reality glasses inevitably require always-on cameras and cloud processing, creating unavoidable privacy invasions that may be too costly for society. This commentary highlights a fundamental trade-off in AR development that could shape industry direction and public policy. If Patel is correct, the pursuit of sleek AR glasses may be ethically untenable without major privacy safeguards. Patel states that no chip small enough to fit in a glasses stem can provide both sufficient power and energy efficiency for real-time processing, necessitating cloud offloading. He contrasts this with Apple's Vision Pro, which uses a tethered external battery pack but still relies on local processing.

🔗 [Source](https://simonwillison.net/2026/Jul/10/nilay-patel/#atom-everything)

rss · Simon Willison · Jul 10, 17:05

**Background**: Augmented reality glasses overlay digital information onto the real world, requiring real-time analysis of the user's environment. Current designs face a trade-off between processing power, battery life, and form factor. Always-on cameras raise privacy concerns because they continuously record everything the wearer sees, potentially capturing bystanders without consent.

<details><summary>References</summary>
<ul>
<li><a href="https://dissenter.com/tech/metas-always-on-spy-glasses-record-everything-hide-the-warning-light">Meta's Always - On Spy Glasses Record Everything, Hide... | Dissenter</a></li>
<li><a href="https://eyeware.store/ar-and-smart-lenses-why-your-home-router-and-phone-matter-mo">AR Glasses : Why Your Router & Phone Matter</a></li>
<li><a href="https://www.wired.com/story/one-part-of-apple-vision-pro-apple-doesnt-want-you-to-see/">The One Part of the Vision Pro That Apple Doesn’t Want You... | WIRED</a></li>

</ul>
</details>

**Tags**: `#augmented reality`, `#privacy`, `#cloud computing`, `#ethics`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Profiling Attention Layers in PyTorch for Transformer Optimization</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A new Hugging Face blog post provides a detailed guide on profiling attention layers in PyTorch, using the PyTorch Profiler to identify bottlenecks and optimize transformer model performance. Attention mechanisms are central to modern transformers, and profiling them is crucial for improving training and inference efficiency. This guide helps practitioners reduce computational costs and memory usage in large-scale AI models. The blog covers using the PyTorch Profiler to trace operator-level execution, measure GPU utilization, and identify inefficiencies in attention implementations. It includes practical tips for interpreting profiler outputs and applying optimizations like kernel fusion.

🔗 [Source](https://huggingface.co/blog/torch-attention-profile)

rss · Hugging Face Blog · Jul 10, 00:00

**Background**: PyTorch Profiler is a built-in tool that records operator calls and GPU events during model execution, helping developers pinpoint performance bottlenecks. Attention layers, especially in transformers, often dominate computation and memory, making them prime targets for optimization. Techniques like flash attention and sparse attention have emerged to address these challenges.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html">PyTorch Profiler — PyTorch Tutorials 2.13.0+cu130 documentation</a></li>
<li><a href="https://github.com/Quentin-Anthony/torch-profiling-tutorial">GitHub - Quentin-Anthony/torch-profiling-tutorial · GitHub</a></li>

</ul>
</details>

**Tags**: `#PyTorch`, `#profiling`, `#attention`, `#transformers`, `#optimization`

</details>


<a id="item-11"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Meta pulls AI image feature after backlash</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Meta removed an AI-powered image editing feature on Instagram just days after its release, following widespread user backlash. This incident underscores the growing public scrutiny of AI deployment in social media, especially regarding ethical concerns and user consent. The feature allowed users to alter Instagram content using AI, but it drew swift blowback from users who raised concerns about misuse and lack of transparency.

🔗 [Source](https://www.bbc.co.uk/news/articles/c2dy6e8klw0o?at_medium=RSS&at_campaign=rss)

rss · BBC World · Jul 11, 01:45

**Background**: Meta has been integrating AI features across its platforms, including Instagram and Facebook, to enhance user engagement. However, such features often raise privacy and ethical questions, especially when they involve altering user-generated content.

**Tags**: `#AI`, `#Meta`, `#social media`, `#ethics`, `#backlash`

</details>


</section>