---
layout: default
title: "Horizon Summary: 2026-07-11 (ZH)"
date: 2026-07-11
lang: zh
---

> 从 102 条内容中筛选出 11 条重要资讯。

---

<section class="cat cat-finance" markdown="1">

## 💹 财经 / 市场 (1)

<a id="item-1"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">GPU 热潮中的循环融资：英伟达、CoreWeave 与 Nebius</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

一项分析揭示，英伟达、CoreWeave 和 Nebius 正参与循环融资：英伟达投资云公司，这些公司再用资金购买英伟达的 GPU，从而推动 AI 基础设施热潮。 这种融资模式引发了对可持续性和经济风险的担忧，因为它可能夸大需求并导致数据中心过度建设，有可能重蹈互联网泡沫的覆辙。 英伟达向 CoreWeave 投资 20 亿美元获得 9%股权，而 CoreWeave 计划 2026 年资本支出 350 亿美元，英伟达的投资仅占其中的 5.7%。其余资金来自其他来源，这挑战了纯粹循环融资的说法。

🔗 [来源](https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom)

hackernews · adletbalzhanov · 7月11日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=48873836)

**背景**: 循环融资是一种闭环资金安排：投资者向公司提供资金，该公司再将资金用于购买投资者的产品或服务。在 AI 行业，例如微软向 OpenAI 投资 100 亿美元，后者承诺使用 Azure。这种模式被拿来与互联网时代相提并论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://builtin.com/articles/ai-circular-financing">How Circular Financing Is Fueling the AI Boom | Built In</a></li>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nebius_Group">Nebius Group - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者就融资是否真正循环展开辩论，指出英伟达的投资仅占 CoreWeave 资本支出的一小部分。有人质疑 AI 基础设施建设的经济盈利能力，而另一些人则警告过度建设风险以及类似 2008 年金融危机的潜在经济后果。

**标签**: `#AI infrastructure`, `#GPU boom`, `#circular financing`, `#Nvidia`, `#datacenter economics`

</details>


</section>

<section class="cat cat-science" markdown="1">

## 🧪 科学 (1)

<a id="item-2"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">相对论主宰重元素化学键</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

发表在《科学》杂志上的新研究表明，爱因斯坦的相对论，特别是自旋-轨道耦合，主导了重元素的化学键，推翻了传统量子化学模型中自旋和轨道独立的假设。 这一发现重塑了我们对重元素化学键的基本理解，对材料科学、催化和核化学等领域至关重要。它也验证了相对论效应在这些系统中不仅是修正项，而是主导力量。 该研究表明，对于重元素，电子自旋和轨道运动强烈耦合（自旋-轨道耦合），导致与轻元素不同的键型（σ键和π键）。该研究为这种相对论键合机制提供了直接的实验证据。

🔗 [来源](https://www.brown.edu/news/2026-07-09/chemical-bonds-relativity)

hackernews · hhs · 7月10日 22:30 · [社区讨论](https://news.ycombinator.com/item?id=48866134)

**背景**: 在量子化学中，化学键通常由非相对论薛定谔方程描述，这对轻元素效果良好。但对于金或汞等重元素，靠近原子核的电子速度可达光速的显著比例，使得相对论效应变得重要。自旋-轨道耦合是一种相对论效应，它将电子的自旋与其轨道运动联系起来，改变能级和成键行为。先前的研究已显示相对论效应对金颜色等性质的影响，但这项研究直接将其与化学键形成联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.brown.edu/news/2026-07-09/chemical-bonds-relativity">Einstein’s relativity rules chemical bonds in heavy elements , new...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Relativistic_quantum_chemistry">Relativistic quantum chemistry - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，重元素中的相对论效应并非全新概念，他们引用了金颜色和汞液态等例子。但他们赞赏这项研究提供了相对论与化学键形成直接联系的实验证据。一些用户提供了额外背景，例如周期表形状源于球对称性，并对爱因斯坦理论的持续相关性表示钦佩。

**标签**: `#physics`, `#chemistry`, `#relativity`, `#quantum mechanics`, `#heavy elements`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 科技 / AI (9)

<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">vLLM v0.25.0：MRv2 成为默认，PagedAttention 被移除</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

vLLM v0.25.0 将 Model Runner V2 (MRv2) 设为所有稠密模型的默认执行路径，并移除了旧的 PagedAttention 实现。它还新增了 LLaVA-OneVision-2 和 GLM-5 等模型，引入了流式解析引擎，并实现了性能提升，包括 Transformers 后端现在与原生 vLLM 速度相当。 此版本标志着 vLLM 的重大架构转变，通过移除 PagedAttention 并标准化 MRv2 来简化代码库，从而提高了可维护性和性能。新模型和优化扩展了 vLLM 对更广泛 LLM 工作负载的适用性，使依赖 vLLM 进行高效推理的 AI/ML 社区受益。 MRv2 现在支持 EVS（高效可变大小序列）、实时嵌入、Mamba 混合模型的前缀缓存以及带有完整 CUDA 图的动态推测解码。Transformers 后端获得了 FP8 MoE 支持和 CUDA 图修复，新的流式解析引擎统一了工具调用和推理解析。

🔗 [来源](https://github.com/vllm-project/vllm/releases/tag/v0.25.0)

github · khluu · 7月11日 20:06

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理引擎，使用 PagedAttention 实现 KV 缓存的高效内存管理。Model Runner V2 是一个较新的执行后端，可提高性能和灵活性。此版本通过将 MRv2 设为默认并移除较旧的 PagedAttention 代码来巩固 vLLM 的架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm -project/ vllm</a></li>
<li><a href="https://docs.vllm.ai/en/latest/models/supported_models/">Supported Models - vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#open source`, `#AI/ML`, `#release notes`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">ClickHouse 将 PgBouncer 吞吐量提升 4 倍</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

ClickHouse 详细介绍了他们如何利用 SO_REUSEPORT 和查询取消对等（peering）技术将 PgBouncer 的吞吐量提升 4 倍。 这一优化显著提升了 PostgreSQL 连接池的性能，使依赖 PgBouncer 的大规模部署受益。 SO_REUSEPORT 允许多个 PgBouncer 进程共享同一端口，而对等机制则将取消请求转发到正确的进程，解决了关键瓶颈。

🔗 [来源](https://clickhouse.com/blog/pgbouncer-clickhouse-managed-postgres)

hackernews · saisrirampur · 7月11日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=48872874)

**背景**: PgBouncer 是 PostgreSQL 的轻量级连接池。没有对等机制时，取消请求可能落在不拥有该查询的进程上，导致请求被忽略。SO_REUSEPORT 是一种套接字选项，允许多个套接字绑定到同一端口，将传入连接分发到不同进程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stackoverflow.com/questions/14388706/how-do-so-reuseaddr-and-so-reuseport-differ">How do SO_REUSEADDR and SO_REUSEPORT differ? - Stack Overflow</a></li>
<li><a href="https://lwn.net/Articles/542629/">The SO_REUSEPORT socket option [LWN.net]</a></li>
<li><a href="https://dataegret.com/2024/08/handling_cancellation_request/">Handling Cancellation Request - Data Egret</a></li>

</ul>
</details>

**社区讨论**: 评论者提出了 Odyssey 和 pgdog 等替代方案，并询问对等机制是否内置于 PgBouncer。讨论反映了对可扩展 PgBouncer 替代方案及实际部署细节的兴趣。

**标签**: `#PostgreSQL`, `#PgBouncer`, `#scaling`, `#connection pooling`, `#ClickHouse`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">苹果起诉 OpenAI 窃取商业机密</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

苹果对 OpenAI 提起诉讼，指控其通过招募前苹果员工系统性地窃取商业机密，这些员工将机密信息通过电子邮件发送给自己，并指示新员工隐瞒其就业情况。 这起诉讼可能为 AI 公司如何处理商业机密和员工流动树立先例，并可能重塑科技行业的招聘实践。它还凸显了老牌科技巨头与 AI 初创公司之间在知识产权方面日益加剧的紧张关系。 苹果声称 OpenAI 在接触苹果供应商时使用了苹果的机密硬件信息，并欺骗供应商使其相信 OpenAI 得到了苹果的支持。诉讼还指控 OpenAI 指示新员工不要向苹果透露新工作，以延长其访问权限。

🔗 [来源](https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/)

hackernews · stock_toaster · 7月10日 20:47 · [社区讨论](https://news.ycombinator.com/item?id=48865019)

**背景**: 商业机密盗窃诉讼在科技行业很常见，但本案涉及两家最著名的 AI 公司。苹果长期以来在硬件开发中高度重视保密，而 OpenAI 则因其数据实践受到批评。结果可能影响公司在 AI 时代如何保护专有信息。

**社区讨论**: 评论者大多支持苹果，称 OpenAI 的行为“确凿无疑”，并预测严重后果，例如 OpenAI 硬件雄心的终结。一些人担心这反映了 OpenAI 无视知识产权法的更广泛模式，并建议企业避免使用 OpenAI 模型，因为存在潜在的知识产权风险。

**标签**: `#Apple`, `#OpenAI`, `#lawsuit`, `#trade secrets`, `#AI ethics`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Hotz 发文警告 AI 审查制度</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

George Hotz 发表了一篇题为《AI 2040 与智能崇拜》的博客文章，反对 AI 审查制度，并警告大型语言模型可能强制推行意识形态一致性。 这篇文章引发了关于言论自由与 AI 安全之间平衡的激烈辩论，凸显了人们对 LLM 被用于压制异议和记录“思想犯罪”的担忧。 Hotz 认为不受限制的信息获取是第一修正案问题，但评论者指出，当 AI 代理采取现实行动（例如入侵汽车）时，这种逻辑就不成立了。

🔗 [来源](https://geohot.github.io//blog/jekyll/update/2026/07/11/ai-2040.html)

hackernews · rvz · 7月11日 18:04 · [社区讨论](https://news.ycombinator.com/item?id=48874200)

**背景**: 像 GPT-4 这样的大型语言模型越来越多地被用于聊天机器人和代理。公司通常会实施安全过滤器以防止有害输出，但批评者认为这相当于审查。这场辩论反映了安全与自由之间长期存在的紧张关系。

**社区讨论**: 评论者意见不一：一些人基于言论自由同意 Hotz 的观点，而另一些人则认为能够造成现实伤害的 AI 代理需要限制。一个关键担忧是潜在的无形偏见注入和“思想犯罪”记录。

**标签**: `#AI safety`, `#censorship`, `#free speech`, `#LLM`, `#ethics`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Ant：一个新的 JavaScript 运行时与生态系统</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Ant 是一个从头构建的 JavaScript 运行时，拥有自己的引擎、包管理器、注册中心、部署平台和桌面应用框架，旨在成为现有 JavaScript 栈的连贯替代方案。 该项目代表了一项重大的技术工程，可能提供更集成、更高效的开发体验，有潜力挑战 Node.js 和 Deno 等现有生态系统。 Ant 使用自定义字节码虚拟机（Silver VM），用 C 语言编写，注重轻量和高性能。它还包含 Ant Desktop 用于构建原生桌面应用，类似于 Electron。

🔗 [来源](https://antjs.org/)

hackernews · theMackabu · 7月11日 20:07 · [社区讨论](https://news.ycombinator.com/item?id=48875377)

**背景**: 像 Node.js 和 Deno 这样的 JavaScript 运行时在浏览器之外执行 JavaScript。大多数运行时使用 V8 引擎（来自 Chrome）或 SpiderMonkey（来自 Firefox）。Ant 引入了自己的引擎，这很少见且雄心勃勃。该项目还包括一个包注册中心（ants.land）和一个部署平台，旨在提供端到端的解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/themackabu/ant">GitHub - theMackabu/ ant : javascript for 's, a tiny runtime with big...</a></li>
<li><a href="https://deepwiki.com/theMackabu/ant">theMackabu/ ant | DeepWiki</a></li>

</ul>
</details>

**社区讨论**: 社区评论对该项目的起源提出了担忧，指出早期版本依赖于现有的 AGPL 代码库（Elk），尽管作者声称此后已重写。还存在与 Apache Ant 和 Anthropic 的 ant CLI 的命名冲突。一些评论者认为由于沙箱和快速启动，该项目在 FaaS 方面有潜力。

**标签**: `#JavaScript`, `#runtime`, `#ecosystem`, `#web development`, `#open source`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">在 SQLite 中优先使用严格表以确保类型安全</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

一篇文章提倡在 SQLite 中使用严格表（STRICT tables），该功能自 3.37.0 版本（2021-11-27）引入，可强制进行严格的类型检查，防止意外的数据类型不匹配。 这很重要，因为 SQLite 默认的动态类型可能导致细微的错误，尤其是在多应用或长期使用的数据库中；采用严格表可提高数据完整性并减少调试工作量。 严格表会拒绝与声明的列类型不匹配的值（例如，向 INTEGER 列插入字符串会失败），并且仅支持部分类型：INT、INTEGER、REAL、TEXT、BLOB 和 ANY。

🔗 [来源](https://evanhahn.com/prefer-strict-tables-in-sqlite/)

hackernews · ingve · 7月11日 17:33 · [社区讨论](https://news.ycombinator.com/item?id=48873940)

**背景**: SQLite 传统上使用动态类型（类型亲和性），列类型只是提示而非严格规则。这种灵活性允许向任何列插入任何值，可能导致意外行为。严格表在 SQLite 3.37.0 中引入，强制实施类似于传统 SQL 数据库的静态类型，提供更强的保证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sqlite.org/stricttables.html">STRICT Tables</a></li>
<li><a href="https://antonz.org/sqlite-strict-tables/">STRICT tables in SQLite</a></li>
<li><a href="https://sqlite.org/datatype3.html">Datatypes In SQLite</a></li>

</ul>
</details>

**社区讨论**: 评论者大多同意严格表应成为默认设置，并提到其能防止 UUID 转数字等错误。一些人指出，SQLite 的灵活性对嵌入式单应用场景有用，但对于共享数据库，严格类型更受青睐。

**标签**: `#SQLite`, `#database`, `#type safety`, `#best practices`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Nilay Patel：AR 眼镜需要始终开启的摄像头和云处理</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Nilay Patel 认为，实用的增强现实眼镜不可避免地需要始终开启的摄像头和云处理，从而造成不可避免的隐私侵犯，这对社会来说可能代价过高。 这一评论凸显了 AR 开发中的根本性权衡，可能影响行业方向与公共政策。如果 Patel 所言正确，那么追求轻便 AR 眼镜在缺乏重大隐私保护措施的情况下可能在伦理上站不住脚。 Patel 指出，没有足够小的芯片能同时提供足够的性能和能效来放入眼镜腿中进行实时处理，因此必须将数据发送到云端。他将此与苹果 Vision Pro 进行对比，后者使用外接电池包但仍依赖本地处理。

🔗 [来源](https://simonwillison.net/2026/Jul/10/nilay-patel/#atom-everything)

rss · Simon Willison · 7月10日 17:05

**背景**: 增强现实眼镜将数字信息叠加到现实世界上，需要实时分析用户环境。当前设计面临处理能力、电池续航和外形尺寸之间的权衡。始终开启的摄像头引发隐私担忧，因为它们持续记录佩戴者所见的一切，可能未经同意就捕捉到旁观者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dissenter.com/tech/metas-always-on-spy-glasses-record-everything-hide-the-warning-light">Meta's Always - On Spy Glasses Record Everything, Hide... | Dissenter</a></li>
<li><a href="https://eyeware.store/ar-and-smart-lenses-why-your-home-router-and-phone-matter-mo">AR Glasses : Why Your Router & Phone Matter</a></li>
<li><a href="https://www.wired.com/story/one-part-of-apple-vision-pro-apple-doesnt-want-you-to-see/">The One Part of the Vision Pro That Apple Doesn’t Want You... | WIRED</a></li>

</ul>
</details>

**标签**: `#augmented reality`, `#privacy`, `#cloud computing`, `#ethics`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">在 PyTorch 中对注意力层进行性能分析以优化 Transformer</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

一篇新的 Hugging Face 博客文章详细介绍了如何在 PyTorch 中对注意力层进行性能分析，利用 PyTorch Profiler 识别瓶颈并优化 Transformer 模型性能。 注意力机制是现代 Transformer 的核心，对其进行分析对于提高训练和推理效率至关重要。本指南帮助从业者降低大规模 AI 模型的计算成本和内存使用。 该博客介绍了如何使用 PyTorch Profiler 跟踪算子级别的执行、测量 GPU 利用率以及识别注意力实现中的低效问题。它包含解读分析器输出和应用内核融合等优化的实用技巧。

🔗 [来源](https://huggingface.co/blog/torch-attention-profile)

rss · Hugging Face Blog · 7月10日 00:00

**背景**: PyTorch Profiler 是一个内置工具，可记录模型执行期间的算子调用和 GPU 事件，帮助开发者定位性能瓶颈。注意力层，尤其是在 Transformer 中，通常占据主要计算和内存，因此成为优化的重点目标。诸如 flash attention 和稀疏注意力等技术已出现以应对这些挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html">PyTorch Profiler — PyTorch Tutorials 2.13.0+cu130 documentation</a></li>
<li><a href="https://github.com/Quentin-Anthony/torch-profiling-tutorial">GitHub - Quentin-Anthony/torch-profiling-tutorial · GitHub</a></li>

</ul>
</details>

**标签**: `#PyTorch`, `#profiling`, `#attention`, `#transformers`, `#optimization`

</details>


<a id="item-11"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Meta 因用户反对撤回 AI 图像功能</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Meta 在 Instagram 上推出 AI 图像编辑功能仅数天后，因用户强烈反对而将其移除。 这一事件凸显了公众对社交媒体中 AI 应用的日益审视，尤其是在伦理问题和用户同意方面。 该功能允许用户使用 AI 修改 Instagram 内容，但迅速引发用户反弹，用户担忧其被滥用且缺乏透明度。

🔗 [来源](https://www.bbc.co.uk/news/articles/c2dy6e8klw0o?at_medium=RSS&at_campaign=rss)

rss · BBC World · 7月11日 01:45

**背景**: Meta 一直在其平台（包括 Instagram 和 Facebook）中集成 AI 功能，以提升用户参与度。然而，此类功能常引发隐私和伦理问题，尤其是在涉及修改用户生成内容时。

**标签**: `#AI`, `#Meta`, `#social media`, `#ethics`, `#backlash`

</details>


</section>