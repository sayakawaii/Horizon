---
layout: default
title: "Horizon Summary: 2026-06-14 (EN)"
date: 2026-06-14
lang: en
---

> From 99 items, 9 important content pieces were selected

---

<section class="cat cat-geopolitics" markdown="1">

## 🌐 Geopolitics (1)

<a id="item-1"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">US orders suspension of Anthropic's Fable 5 and Mythos 5</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

The US government issued an export control directive to suspend all access to Anthropic's Fable 5 and Mythos 5 models, citing national security concerns over a potential jailbreak method. Anthropic was forced to abruptly disable the models for all customers globally, including foreign national employees. This unprecedented government intervention in AI model access sets a major precedent for national security controls on advanced AI capabilities. It could reshape how AI companies deploy powerful models and how governments regulate AI globally. The directive was received at 5:21pm ET on June 12, 2026, and access was cut off by 6:59pm PT. Anthropic stated the alleged jailbreak technique was non-universal and that similar capabilities are available from other models like OpenAI's GPT-5.5.

🔗 [Source](https://simonwillison.net/2026/Jun/13/us-government-directive-to-suspend-access/#atom-everything)

rss · Simon Willison · Jun 13, 01:01

**Background**: Anthropic launched Claude Fable 5 and Claude Mythos 5 earlier in June 2026, with Mythos 5 being a highly advanced model capable of finding security vulnerabilities. The government's concern centered on a potential jailbreak that could bypass safety guardrails, though Anthropic argued the vulnerabilities were minor and not unique to its models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/06/09/anthropic-mythos-claude-fable-5.html">Anthropic releases Mythos-like AI model to the public, Claude Fable 5</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-06-13/anthropic-says-us-limits-foreign-access-to-fable-5-mythos-5">Anthropic Says US Limits Foreign Access to Fable 5 , Mythos 5</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#national security`, `#Anthropic`, `#export control`, `#jailbreaking`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (8)

<a id="item-2"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">Pyodide 314.0 enables WASM wheels on PyPI</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

Pyodide 314.0 allows package maintainers to publish WebAssembly (WASM) wheels directly to PyPI, using the PyEmscripten platform defined in PEP 783. Previously, the Pyodide team manually maintained over 300 packages; now anyone can build and upload WASM wheels just like native ones. This removes a major bottleneck for the Python-in-browser ecosystem, enabling faster growth and community contributions. It also simplifies distribution of Python packages compiled to WASM, making it easier to run Python code in browsers and other WASM environments. The PR to PyPI's warehouse repository supporting WASM wheels landed on April 21st. The PyEmscripten platform is versioned (e.g., pyemscripten_2026_0_wasm32) and encapsulates the Emscripten compiler version and linked libraries. Simon Willison demonstrated the feature by publishing a luau-wasm package that compiles the Luau language to WASM.

🔗 [Source](https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/#atom-everything)

rss · Simon Willison · Jun 13, 23:55

**Background**: Pyodide is a Python distribution for the browser based on WebAssembly. Previously, package maintainers could not publish WASM wheels to PyPI, so the Pyodide team had to build and host over 300 packages manually. PEP 783 defined the PyEmscripten platform, enabling standard tooling like cibuildwheel to build WASM wheels that PyPI can accept.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/">Publishing WASM wheels to PyPI for use with Pyodide</a></li>
<li><a href="https://peps.python.org/pep-0783/">PEP 783 – Emscripten Packaging | peps .python.org</a></li>
<li><a href="https://news.lavx.hu/article/pypi-now-accepts-wasm-wheels-for-pyodide-via-pep-783-support">PyPI Now Accepts WASM Wheels for Pyodide via PEP 783 Support</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was highly positive, with many expressing excitement about the reduced burden on Pyodide maintainers and the potential for more packages to become available in the browser. Some commenters noted the importance of PEP 783 and the collaborative effort behind the change.

**Tags**: `#Pyodide`, `#WASM`, `#PyPI`, `#Python`, `#WebAssembly`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">vLLM v0.23.0: DeepSeek-V4 optimizations and Model Runner V2 expansion</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

vLLM v0.23.0 introduces major improvements for DeepSeek-V4, including sparse MLA metadata decoupling, TRTLLM-gen attention kernel, and EPLB support for Mega-MoE. It also expands Model Runner V2 to Llama and Mistral dense models by default, and adds a Rust frontend with streaming generate and dynamic LoRA endpoints. These optimizations significantly improve inference efficiency for state-of-the-art models like DeepSeek-V4, reducing latency and enabling larger-scale deployments. The expansion of Model Runner V2 to popular dense models lowers the barrier for users to adopt vLLM's advanced inference pipeline. The release includes 408 commits from 200 contributors, with new model support for Step-3.7-Flash, Cosmos3 Reasoner, and Gemma 4 Unified. Multi-tier KV cache offloading now includes an object-store secondary tier, and the Rust frontend adds streaming generate and dynamic LoRA endpoints.

🔗 [Source](https://github.com/vllm-project/vllm/releases/tag/v0.23.0)

github · khluu · Jun 12, 23:29

**Background**: vLLM is an open-source high-throughput LLM inference engine widely used in production. DeepSeek-V4 is a large Mixture-of-Experts (MoE) model with sparse attention, requiring specialized kernels for efficient inference. Model Runner V2 is vLLM's next-generation execution pipeline that improves performance through better scheduling and kernel fusion.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lmsys.org/blog/2026-04-25-deepseek-v4/">DeepSeek-V4 on Day 0: From Fast Inference to Verified RL with SGLang and Miles - LMSYS Blog | LMSYS Org</a></li>
<li><a href="https://github.com/vllm-project/vllm/issues/20468">[Feature]: Support EPLB for More MoE Models, e.g. Qwen 3, Llama 4 · Issue #20468 · vllm-project/vllm</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#open source`, `#AI infrastructure`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Rio's Homegrown LLM Revealed as Weighted Merge of Existing Models</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Rio de Janeiro's claimed homegrown LLM, Rio-3.5-Open-397B, is actually a weighted merge of approximately 60% Nex-N2 Pro and 40% Qwen3.5-397B-A17B, as revealed by a GitHub issue with detailed technical analysis. This raises serious questions about transparency and attribution in open-source AI, as the model was presented as a homegrown fine-tune but appears to be a simple merge without proper disclosure. The analysis shows that every weight tensor in the Rio model is a 0.6/0.4 blend of Nex and Qwen across all 60 layers, which is inconsistent with a typical fine-tune but characteristic of a weighted merge.

🔗 [Source](https://github.com/nex-agi/Nex-N2/issues/4)

hackernews · unrvl22 · Jun 14, 15:37 · [Discussion](https://news.ycombinator.com/item?id=48528371)

**Background**: Model merging is a technique that combines the weights of two or more pre-trained models into a single model without additional training, often used to improve performance or combine capabilities. Weighted merging assigns different importance to each model's weights. This is different from fine-tuning, which involves additional training on a specific dataset.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-model-merging-for-llms/">An Introduction to Model Merging for LLMs | NVIDIA Technical Blog</a></li>
<li><a href="https://arxiv.org/abs/2408.07666">[2408.07666] Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, Applications and Opportunities</a></li>
<li><a href="https://huggingface.co/blog/mlabonne/merge-models">Merge Large Language Models with mergekit</a></li>

</ul>
</details>

**Discussion**: Community comments express skepticism and concern about the lack of attribution, with some noting that the model's performance improvement may come from the merge itself rather than any novel training. Others point out that the municipality may have intended to disclose the base model but failed to do so properly.

**Tags**: `#LLM`, `#open-source`, `#AI ethics`, `#model merging`, `#controversy`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Jane Street on Formal Methods in Production</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Jane Street published a blog post detailing their practical experience using formal methods in production, highlighting both benefits and challenges. The post has sparked community discussion on the role of verification, especially in the context of AI-generated code. This discussion is significant because it comes from a reputable financial firm that uses formal methods at scale, providing real-world insights. It also addresses the growing need for verification as AI-generated code becomes more prevalent, potentially shaping future software engineering practices. The blog post is part of a series on formal methods at Jane Street, covering topics like proof assistants, theorem provers, and static analysis. The community comments include historical perspectives from early verification work and modern applications with expressive type systems in Scala 3.

🔗 [Source](https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1)

hackernews · eatonphil · Jun 14, 12:35 · [Discussion](https://news.ycombinator.com/item?id=48526633)

**Background**: Formal methods are mathematically-based techniques for specifying, developing, and verifying software and hardware systems. Unlike traditional testing, which is reactive, formal methods aim to prove correctness properties statically, reducing bugs. Jane Street, a quantitative trading firm, is known for using OCaml and has invested in formal verification for critical systems.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.janestreet.com/formal-methods-at-jane-street-index/">Jane Street Blog - Formal methods and the future of programming</a></li>
<li><a href="https://www.builtinnyc.com/company/jane-street/jobs">Jane Street NYC Jobs + Careers | Built In NYC</a></li>

</ul>
</details>

**Discussion**: Commenters shared diverse views: some recalled early proof automation systems like the Boyer-Moore prover, while others discussed using expressive types in Scala 3 to enforce compile-time proofs. A key concern was whether formal specs are just 'tests in a different way' and can suffer from the same bugs as implementations.

**Tags**: `#formal methods`, `#programming`, `#verification`, `#Jane Street`, `#software engineering`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">2014 Talk Predicted JavaScript's Rise and Fall</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Gary Bernhardt's 2014 talk 'The Birth and Death of JavaScript' humorously predicted that JavaScript would become a universal compilation target and eventually be replaced, a forecast largely validated by the rise of WebAssembly and TypeScript. The talk's prescience highlights how community insights can anticipate major shifts in web development, influencing how developers think about language evolution and compilation targets. The talk specifically mentioned asm.js, which was later deprecated in favor of WebAssembly, and foresaw the trend of transpiling other languages to JavaScript, now common with TypeScript and tools like Emscripten.

🔗 [Source](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript)

hackernews · subset · Jun 14, 12:38 · [Discussion](https://news.ycombinator.com/item?id=48526661)

**Background**: JavaScript was originally designed as a simple scripting language for web browsers. Over time, it became the dominant language for web development, but its limitations led to the creation of compile-to-JS languages like TypeScript and alternative runtime targets like WebAssembly, a binary instruction format that runs alongside JavaScript.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly - Wikipedia</a></li>
<li><a href="https://webassembly.org/">WebAssembly</a></li>
<li><a href="https://github.com/appcypher/awesome-wasm-langs">GitHub - appcypher/awesome-wasm-langs: 😎 A curated list of languages that compile directly to or have their VMs in WebAssembly</a></li>

</ul>
</details>

**Discussion**: Commenters noted the talk's accurate prediction of a global disaster around 2020-2025 (though the wrong type), and debated WebAssembly's slow progress and lack of DOM access, which still requires JavaScript as glue code. Some praised the talk's humor and foresight, while others pointed out that Electron has brought web technologies to desktop apps, albeit with performance concerns.

**Tags**: `#JavaScript`, `#WebAssembly`, `#Programming Languages`, `#Web Development`, `#Tech Predictions`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Developer indexes 669 GB of GoPro videos locally with M1 Max</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A developer built a project to index 628 GoPro videos (669 GB, 15+ hours of footage) on an M1 Max Mac using open-source ML models, enabling search and export of interesting clips directly to a DaVinci Resolve timeline. This demonstrates that powerful local AI video indexing is feasible on consumer hardware, reducing reliance on cloud services and preserving privacy. It opens up practical applications for personal media management and content creation. The pipeline processes 1 frame per second, analyzing 57,537 frames total, with a compute time of 67 hours 40 minutes. It uses open-source models for scene detection and object recognition, and integrates with DaVinci Resolve via its API.

🔗 [Source](https://news.ycombinator.com/item?id=48528029)

hackernews · iliashad · Jun 14, 15:13

**Background**: Video indexing typically requires significant computational resources, often relying on cloud-based AI services. Local processing on Apple Silicon chips like the M1 Max offers a privacy-preserving alternative, though it can be time-intensive. DaVinci Resolve is a professional video editing application that includes its own AI search features in the Studio version.

<details><summary>References</summary>
<ul>
<li><a href="https://notifire.in/tech/local-ai-turns-m1-mac-into-a-video-search-engine">Local ML Models Index 669 GB of Video on an M1 Max Mac | Notifire</a></li>
<li><a href="https://news.ycombinator.com/item?id=48528029">I indexed 669 GB of my GoPro videos using my... | Hacker News</a></li>

</ul>
</details>

**Discussion**: Commenters noted similar projects, with one user having built a comparable system days earlier. Others pointed out that DaVinci Resolve 21 already includes built-in AI indexing, and there was curiosity about compute time optimization and potential cloud acceleration options.

**Tags**: `#machine learning`, `#video indexing`, `#local AI`, `#GoPro`, `#M1 Max`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">AI adoption not universal despite hype</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A new analysis argues that despite widespread AI hype, actual usage is far from universal, with many individuals and businesses not adopting AI tools. The article cites data showing over 50% of people use AI less than once per week. This challenges the dominant narrative that AI is being universally embraced, highlighting a gap between hype and reality. It matters for investors, developers, and policymakers who may be overestimating the pace of AI integration. The analysis points out that AI usage is often conflated with occasional interactions, and that many people do not integrate AI into their daily workflows. The author suggests that AI adoption may follow a slower, more uneven path than expected.

🔗 [Source](https://gabrielweinberg.com/p/people-are-consuming-ai-like-they)

hackernews · yegg · Jun 14, 14:44 · [Discussion](https://news.ycombinator.com/item?id=48527700)

**Background**: The article is part of a broader debate about the real-world adoption of AI technologies, especially large language models like ChatGPT. While tech companies and media often emphasize rapid adoption, surveys and anecdotal evidence suggest many users remain skeptical or uninterested.

**Discussion**: Commenters shared mixed experiences: some noted that employers ask about LLM use in interviews, reflecting uncertainty about AI's role. Others argued that AI is being integrated into existing software rather than used directly, which may undercount adoption.

**Tags**: `#AI adoption`, `#technology trends`, `#software engineering`, `#hype cycle`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Mapping SQLite result columns back to source table.column</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Simon Willison used Claude Code (Opus 4.8) to programmatically map SQL query result columns back to their source table.column, exploring solutions via apsw, ctypes, and EXPLAIN output. This enables Datasette to enrich arbitrary SQL query results with column provenance metadata, improving data understanding and trust. It demonstrates how AI-assisted development can solve practical database tooling problems. SQLite internally computes column provenance and exposes it via the sqlite3_column_table_name() C function, but Python's standard sqlite3 module does not expose it. Claude Code identified three approaches: using the apsw library, calling the C function via ctypes, or parsing EXPLAIN output.

🔗 [Source](https://simonwillison.net/2026/Jun/13/sqlite-column-provenance/#atom-everything)

rss · Simon Willison · Jun 13, 23:05

**Background**: Datasette is an open-source tool for exploring and publishing relational databases. Column provenance — knowing which table and column each result field originates from — is valuable for data lineage and debugging, especially in queries with joins or CTEs. SQLite's C API includes functions like sqlite3_column_table_name() that return this metadata, but they are not exposed in Python's built-in sqlite3 module.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/jun/13/sqlite-column-provenance/">Research: Mapping SQLite result columns back to their source...</a></li>
<li><a href="https://docs.datasette.io/en/stable/metadata.html">Metadata - Datasette documentation</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Tags**: `#SQL`, `#Datasette`, `#AI-assisted development`, `#database`, `#column provenance`

</details>


</section>