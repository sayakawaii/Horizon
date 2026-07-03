---
layout: default
title: "Horizon Summary: 2026-07-03 (ZH)"
date: 2026-07-03
lang: zh
---

> 从 117 条内容中筛选出 15 条重要资讯。

---

<section class="cat cat-geopolitics" markdown="1">

## 🌐 国际局势 (1)

<a id="item-1"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">欧盟间谍软件调查员手机遭飞马入侵</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

公民实验室确认，曾参与调查间谍软件的欧洲议会前议员斯特利奥斯·库洛格卢的 iPhone 在 2022 年和 2023 年多次被飞马间谍软件感染。 此事件凸显了调查监控滥用的官员成为攻击目标，引发对民主机构安全和法治的严重担忧。 感染发生在库洛格卢担任 PEGA 委员会成员期间；同一设备上的个人医疗记录和机密政府文件可能均遭泄露。

🔗 [来源](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/)

hackernews · ledoge · 7月3日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: 飞马是由以色列 NSO 集团开发的强大间谍软件，仅出售给政府用于反恐和打击犯罪，但经常被用来针对记者、活动家和政治家。公民实验室是多伦多大学的一个研究小组，调查对公民社会的数字威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://therecord.media/pegasus-spyware-european-parliament-pega-committee-member">Spyware found on phone of European Parliament member probing it | The Record from Recorded Future News</a></li>
<li><a href="https://www.wired.com/story/eu-politicians-investigated-pegasus-spyware-then-it-ended-up-on-one-of-their-phones/">EU Politicians Investigated Pegasus Spyware. Then It Ended Up on One of Their Phones | WIRED</a></li>

</ul>
</details>

**社区讨论**: 评论者指出间谍软件调查员被黑具有讽刺意味，并质疑欧盟议会为何缺乏区分工作与个人设备的政策。一些人将此攻击置于更广泛的希腊间谍软件丑闻中，该丑闻据称与总理办公室有关。

**标签**: `#cybersecurity`, `#surveillance`, `#Pegasus`, `#European Parliament`, `#spyware`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 科技 / AI (13)

<a id="item-2"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">BBC 发现 Instagram 在印度投放推广儿童性虐待材料的广告</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

BBC 的一项调查发现，Instagram 在印度投放付费广告，推广儿童性虐待材料，使用“强奸”和“儿童视频”等词汇，并链接到 Telegram 上的内容。 这暴露了 Instagram 内容审核系统的重大失败，对全球最大社交媒体市场之一的儿童安全和平台责任产生了严重影响。 这些广告在发布前已通过 Instagram 的审核技术批准，并链接到即时通讯应用 Telegram 上的儿童性虐待材料。

🔗 [来源](https://www.bbc.co.uk/news/articles/cvgm4e0316zo?at_medium=RSS&at_campaign=rss)

rss · BBC World · 7月3日 15:01

**背景**: Instagram 使用自动审核系统在广告上线前进行审查。Telegram 是一款以加密和隐私功能著称的流行即时通讯应用，但也面临内容审核方面的担忧。印度信息技术部长已指示官员就此事传唤 Meta 代表。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/cvgm4e0316zo">Instagram running ads promoting child sexual abuse material in India ...</a></li>
<li><a href="https://alphai.io/news/article/07-03/8081b33fc4e54e21/ashwini-vaishnaw-directs-meity-to-summon-meta-regarding-instagram-ads-promoting-child-sexual-abuse-material">Ashwini Vaishnaw directs MeitY to summon Meta regarding Instagram ...</a></li>

</ul>
</details>

**标签**: `#platform safety`, `#child protection`, `#content moderation`, `#social media`, `#ethics`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">PostgreSQL 与 OOM 杀手：为何采用严格内存过量使用</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Ubicloud 发布了一篇博客文章，解释了他们为何对 PostgreSQL 采用严格内存过量使用（vm.overcommit_memory=2）以避免 OOM 杀手，并详细说明了相关的权衡和配置。 这种配置可以显著减少内存压力下 PostgreSQL 的崩溃，提高托管提供商和自托管部署的数据库稳定性。讨论中包含了实际经验和注意事项，使其成为数据库管理员的有价值参考。 模式 2（严格）通过 CommitLimit 对总承诺虚拟内存设置硬限制，拒绝超出该限制的分配。文章还提到，如果调整了过量使用比例，模式 2 可能会阻止 fork，因此在生产部署前需要仔细测试。

🔗 [来源](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit)

hackernews · furkansahin · 7月3日 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48774509)

**背景**: Linux 内核的 OOM 杀手在系统内存不足时会终止进程。默认情况下，Linux 使用启发式过量使用（模式 0），这可能导致内存压力下的 OOM 杀死。严格过量使用（模式 2）防止过量承诺，减少 OOM 杀手调用，但可能导致分配失败。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit">PostgreSQL and the OOM Killer: Why We Use Strict Memory Overcommit</a></li>
<li><a href="https://www.postgresql.org/docs/current/kernel-resources.html">PostgreSQL: Documentation: 18: 18.4. Managing Kernel Resources</a></li>
<li><a href="https://www.cybertec-postgresql.com/en/what-you-should-know-about-linux-memory-overcommit-in-postgresql/">Memory overcommit and PostgreSQL | CYBERTEC PostgreSQL | Services & Support</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 Linux 默认设置在内存压力下存在问题，一些人分享了模式 2 导致 fork 失败的体验。作者承认标题过于强烈，同意严格过量使用有副作用，可能不适合所有场景。

**标签**: `#PostgreSQL`, `#Linux`, `#memory management`, `#OOM killer`, `#database administration`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Wordgard：ProseMirror 作者推出的新富文本编辑器</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Wordgard 是 ProseMirror 作者发布的一款新的浏览器内富文本编辑器，提供了更精致的所见即所得编辑体验，并改进了开发者体验和设计。 作为备受尊敬的 ProseMirror 作者的后续作品，Wordgard 可能影响富文本编辑器生态系统，为寻求现代、设计精良且注重程序化使用的开发者提供替代方案。 Wordgard 与 ProseMirror 共享许多概念，但不提供升级路径，迁移需要大量工作。它还旨在解决与文档模型的程序化交互问题，这是部分 ProseMirror 用户的痛点。

🔗 [来源](https://wordgard.net/)

hackernews · indy · 7月3日 08:50 · [社区讨论](https://news.ycombinator.com/item?id=48772573)

**背景**: ProseMirror 是一个经过实战检验的开源富文本编辑器框架，以其轻量级核心和顶级性能著称，但学习曲线陡峭。它是许多编辑器（如 Tiptap）的基础。所见即所得编辑器允许用户在编辑时看到最终格式化输出，但构建一个健壮的编辑器一直是 Web 开发中的长期挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prosemirror.net/">ProseMirror</a></li>
<li><a href="https://grokipedia.com/page/ProseMirror">ProseMirror</a></li>

</ul>
</details>

**社区讨论**: 社区讨论突出了对 Wordgard 背后“原因”的好奇，与 ProseMirror 的比较以及对迁移难度的担忧。一些用户称赞其设计，并在自己的方法中找到了验证，而另一些用户则感叹缺乏标准化的所见即所得编辑 Web 实现。

**标签**: `#rich-text editor`, `#ProseMirror`, `#web development`, `#open source`, `#WYSIWYG`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">半生不熟的产品：一次创业失败的复盘</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

一篇关于失败硬件创业公司的反思性复盘文章揭示了激励错位和缺乏领域专业知识如何导致产品失败。该文章获得了 1172 个点赞和 358 条评论的强烈社区参与。 这个警示故事突出了硬件创业公司常见的陷阱，如创始人动机与领域专业知识错位以及团队脱节。它为创业者和投资者提供了关于理解市场和技术重要性的永恒教训。 文章详细描述了创始人的主要动机是致富，导致他的愿景与领域专家认为可行的方案之间存在错配。团队存在脱节，每个角色（创始人、工程师、销售人员）对其他关键领域一无所知。

🔗 [来源](https://weli.dev/blog/half-baked-product/)

hackernews · weli · 7月3日 08:23 · [社区讨论](https://news.ycombinator.com/item?id=48772388)

**背景**: 与软件创业公司相比，硬件创业公司通常面临独特的挑战，包括更长的开发周期、更高的资金需求和复杂的供应链。领域专业知识对于理解技术可行性和市场需求至关重要。这篇文章作为一次复盘，是创业社区中分析失败并汲取教训的常见做法。

**社区讨论**: 社区评论强调创始人的财富驱动动机是一个关键问题，一位用户指出许多创始人缺乏领域专业知识，仅依赖市场分析。另一条评论幽默地将这种情况比作一个有打碎玻璃缺陷的洗碗机创业公司，而其他人则强调不同团队角色之间的脱节。

**标签**: `#startups`, `#product development`, `#hardware`, `#entrepreneurship`, `#failure`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">开源 AI 差距图发布</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Current AI（一个在巴黎 AI 行动峰会上成立的非营利组织）发布了开源 AI 差距图 v0.1，索引了 421 个开源 AI 产品，涵盖软件、模型、数据集和硬件。底层数据以 MIT 许可证发布在 GitHub 上。 该图提供了开源 AI 生态系统的全面结构化概览，帮助开发者和研究人员识别差距和机会。它得到了 4 亿美元承诺资金的支持，标志着对开源 AI 基础设施的重大投资。 该图详细列出了来自 228 个组织的 266 个软件工具、85 个模型、50 个数据集和 20 个硬件项目，按三个堆栈层的 14 个类别组织。另有 24,400 个工件被追踪但未分类。

🔗 [来源](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything)

rss · Simon Willison · 7月3日 22:04

**背景**: Current AI 是一个全球非营利合作伙伴关系，于 2025 年 2 月在巴黎 AI 行动峰会上启动，旨在为 AI 构建一个公共选项。差距图试图系统性地编目开源 AI 领域，该领域发展迅速但缺乏集中索引。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.multiminds.eu/news/ai-action-summit-paris-global-talk-with-local-impact/">AI Action Summit Paris : global talk with local impact | MultiMinds</a></li>

</ul>
</details>

**标签**: `#open source`, `#AI`, `#ecosystem`, `#mapping`, `#non-profit`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">理解才能参与：AI 编程协作的关键</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Geoffrey Litt 提出了“理解才能参与”的概念，作为与 AI 编程代理协作的原则，强调需要保持理解以避免认知债务。 这一见解解决了 AI 辅助开发中的一个关键挑战：随着代理生成更多代码，开发者可能失去理解，导致认知债务并降低创造性参与能力。 Litt 认为开发者必须了解代理在做什么，以保持积极参与，这需要丰富的概念来流畅思考项目。该演讲在 AIE 2026 上进行，Twitter 上有相关推文串。

🔗 [来源](https://simonwillison.net/2026/Jul/2/understand-to-participate/#atom-everything)

rss · Simon Willison · 7月2日 17:07

**背景**: 认知债务指的是软件系统中共享理解随时间侵蚀，导致用于推理变更的心智模型不足。随着 AI 编程代理能力增强，开发者可能接受不完全理解的代码，积累认知债务，阻碍未来参与。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/2/understand-to-participate/">Understand to participate - simonwillison.net</a></li>
<li><a href="https://x.com/geoffreylitt/status/2072522267414901109">That's where another answer comes in: we can understand to ...</a></li>
<li><a href="https://arxiv.org/abs/2603.22106">From Technical Debt to Cognitive and Intent Debt: Rethinking ...</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#cognitive debt`, `#software engineering`, `#human-AI collaboration`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">本地运行 SOTA 大模型指南</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Jamesob 在 GitHub 上发布了一份全面指南，详细介绍了如何本地运行最先进的大语言模型，硬件推荐从预算配置到超过 5 万美元的搭建方案。 该指南帮助开发者和爱好者了解本地运行大语言模型的真实成本和权衡，这对于隐私保护、离线使用以及避免云订阅费用至关重要。 该指南涵盖从单张 RTX 3090（低于 2000 美元）到超过 5 万美元（含四张单价 1.2 万美元的 GPU）的硬件配置，并讨论了降低内存需求的量化技术。

🔗 [来源](https://github.com/jamesob/local-llm)

hackernews · livestyle · 7月3日 15:03 · [社区讨论](https://news.ycombinator.com/item?id=48775921)

**背景**: 最先进的大语言模型（SOTA LLMs）需要大量计算资源，尤其是显存，才能以全精度运行。量化技术通过降低模型精度（例如从 FP32 降至 INT8）来减少内存占用，从而能够在消费级硬件上部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/daya-shankar/sota-ai-models">SOTA AI Models: Benchmarks, Metrics & Deployment Guide</a></li>
<li><a href="https://www.ibm.com/think/topics/quantization">What is Quantization? | IBM</a></li>
<li><a href="https://developer.nvidia.com/blog/optimizing-llms-for-performance-and-accuracy-with-post-training-quantization/">Optimizing LLMs for Performance and Accuracy with Post-Training Quantization | NVIDIA Technical Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者警告本地搭建仍然昂贵且质量通常低于云服务，有人指出 4 万美元的配置实际花费 5 万至 5.5 万美元。其他人建议折中方案，例如使用 128GB 统一内存运行 DeepSeek V4 flash，或采用低于 2000 美元的单张 RTX 3090 配置。

**标签**: `#local-llm`, `#hardware`, `#quantization`, `#deep-learning`, `#open-source`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Valve 开源 Steam Machine 电子墨水屏设计</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Valve 已开源 Steam Machine 电子墨水前面板（称为“Inkterface”）的设计文件和固件，任何人都可以自行制作。该公司不会自己生产该显示屏，但已发布 STL 文件和固件供 DIY 组装。 此举让社区能够围绕 Valve 生态系统创新独特的硬件配件，培养开放和定制的文化。同时也为其他硬件公司树立了将可选配件作为开源项目的先例。 该显示屏是标准的 Adafruit 5.83 英寸电子墨水面板（产品编号 6397），开源发布内容包括 CAD 文件和固件。Valve 最初向早期评测者展示了这款电子墨水前面板，但不会进行商业销售。

🔗 [来源](https://www.gamingonlinux.com/2026/07/valve-open-source-the-steam-machine-e-ink-screen-so-you-can-make-your-own/)

hackernews · ahlCVA · 7月3日 13:01 · [社区讨论](https://news.ycombinator.com/item?id=48774518)

**背景**: Steam Machine 是 Valve 于 2025 年底推出的客厅游戏 PC，采用模块化前面板系统。名为“Inkterface”的电子墨水前面板是发布时展示的多种可定制选项之一，能够显示游戏艺术图或系统信息。Valve 有开源硬件和软件的历史，例如 Steam Deck 的设计文件和 SteamOS 操作系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gamingonlinux.com/2026/07/valve-open-source-the-steam-machine-e-ink-screen-so-you-can-make-your-own/">Valve open source the Steam Machine e-ink screen... | GamingOnLinux</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pnbUpuQkVSRWxnTUZnbDgzZEJDZ0FQAQ?hl=en-US&gl=US&ceid=US:en">Valve open-sources "Inkterface" e - ink screen for Steam Machine ...</a></li>
<li><a href="https://www.digitalfoundry.net/news/2026/07/valve-releases-steam-machine-e-ink-faceplate-cad-files-and-firmware">Valve releases Steam Machine e - ink faceplate CAD... | Digital Foundry</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬 Valve 的开放态度，RataNova 希望更多公司能让社区自由发挥可选配件。dgellow 指出该显示屏是标准的 Adafruit 面板，anticorporate 表示有兴趣将其适配到 Framework Desktop。tra3 思考 Valve 的善意对业务的影响，指出这种开放很可能有前期成本。

**标签**: `#open-source`, `#hardware`, `#valve`, `#e-ink`, `#steam-machine`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">LLM 成本漏洞：将文本转为图像利用 OCR</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

一位开发者发布了名为 pxpipe 的工具，通过将文本转换为图像并利用 OCR，将 LLM API 成本降低高达 60%，利用了图像输入比文本输入更低的 token 定价。 这个定价漏洞可能大幅降低长上下文 LLM 应用的成本，但随着提供商调整计费方式，它可能是暂时的。这也凸显了跨模态更公平 token 定价的必要性。 该技术通过将文本渲染成紧凑的图像，减少所需的 512×512 图块数量，然后利用模型的 OCR 能力提取文本。但正如之前对 OpenAI 模型的尝试所指出的，它可能需要更多的补全 token 且速度更慢。

🔗 [来源](https://github.com/teamchong/pxpipe)

hackernews · dimitropoulos · 7月3日 15:50 · [社区讨论](https://news.ycombinator.com/item?id=48776464)

**背景**: LLM API 按 token 计费，而相同信息量的图像 token 通常比文本 token 更便宜。这种差异创造了套利机会：通过将文本转换为图像，用户可以为相同内容支付更少的费用。这种方法类似于将长文本压缩成图像以减少 token 数量，这是近期研究中探索的技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@pcb.it18/cutting-llm-costs-by-converting-long-text-into-images-28eebc61656d">Cutting LLM Costs by Converting Long Text Into Images | by Progressing Llama | Medium</a></li>
<li><a href="https://mail.bycloud.ai/p/how-to-compress-long-text-into-images-to-reduce-llm-tokens">How to Compress Long Text into Images To Reduce LLM Tokens</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，像 Gemini 这样的提供商已经在内部对 PDF 进行 OCR 而不额外收费，这表明这个漏洞利用了 token 记账的漏洞，可能会被修复。其他人指出，去年对 OpenAI 模型的类似尝试最终因补全 token 增加和速度变慢而更昂贵。还有人争论称此为“OCR”是否准确，因为模型处理的是视觉 token 而非提取文本。

**标签**: `#LLM`, `#pricing`, `#OCR`, `#hack`, `#cost optimization`

</details>


<a id="item-11"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">课程创作者报告销售额因 AI 下降超 50%</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Josh W. Comeau 报告称，他的新课程《Whimsical Animations》销量预计仅为通常水平的三分之一，现有课程销售额也较去年大幅下滑，整体收入下降 50%以上。他主要将此归因于 AI 引发的开发者就业不确定性，以及 LLM 作为免费辅导替代品的普及。 来自知名课程创作者的第一手数据表明，AI 对开发者教育市场产生了真实且重大的影响，可能重塑开发者的学习方式以及内容创作者的盈利模式。这凸显了 LLM 正在颠覆付费教育资源的更广泛趋势，引发了对原创内容未经同意使用和补偿问题的担忧。 Comeau 的第三门课程《Whimsical Animations》涵盖现代 CSS、JavaScript、SVG 和 2D Canvas 动画构建。他指出，多位课程创作者都观察到相同趋势：参与内容的人数减少，许多人转向使用未经同意或补偿就利用其作品的 LLM。

🔗 [来源](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything)

rss · Simon Willison · 7月3日 21:25

**背景**: Josh W. Comeau 是一位知名的开发者兼教育者，制作关于 CSS 和 React 等前端开发主题的互动课程。他的课程通常收费，并在开发者社区中颇受欢迎。GPT-4 等大型语言模型（LLM）的兴起实现了个性化辅导和代码生成，可能降低了人们对结构化付费课程的需求。这一转变是 AI 对就业和教育影响的更大讨论的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://whimsy.joshwcomeau.com/">Whimsical Animations , a new course from Josh W . Comeau</a></li>
<li><a href="https://www.joshwcomeau.com/courses/">Online Courses • Josh W . Comeau</a></li>
<li><a href="https://medium.com/@keshavarangarajan/the-impact-of-llms-on-learning-and-education-3cd2a8367c23">The Impact of LLMs on Learning and Education | by keshava rangarajan | Medium</a></li>

</ul>
</details>

**标签**: `#AI impact`, `#developer education`, `#online courses`, `#LLMs`, `#industry trends`

</details>


<a id="item-12"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Simon Willison 发布 llm-coding-agent 0.1a0</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Simon Willison 发布了 llm-coding-agent 0.1a0，这是一个基于他的 LLM 库构建的早期 alpha 编码代理，灵感来自 Claude Code。该代理可以读取和编辑文件、执行命令以及搜索代码，全部通过自然语言提示完成。 此版本展示了 LLM 库如何演变为代理框架，使开发者能够以最小的努力构建自定义编码代理。它降低了尝试 AI 辅助软件开发的门槛。 该代理提供了 edit_file、execute_command、list_files、read_file 和 search_files 等工具，并可通过 `uvx --prerelease=allow --with llm-coding-agent llm code` 运行。它还提供了一个带有 CodingAgent 类的 Python API。

🔗 [来源](https://simonwillison.net/2026/Jul/2/llm-coding-agent/#atom-everything)

rss · Simon Willison · 7月2日 19:33

**背景**: Simon Willison 的 LLM 库是一个 CLI 工具和 Python 库，用于与各种大型语言模型交互。它最近演变为一个代理框架，允许在循环中调用工具。Anthropic 的 Claude Code 是一个代理编码系统，启发了这个项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/2/llm-coding-agent/">Release: llm-coding-agent 0.1a0</a></li>
<li><a href="https://github.com/simonw/llm">GitHub - simonw/llm: Access large language models from the command-line · GitHub</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#coding agent`, `#LLM`, `#AI`, `#Python`, `#agent framework`

</details>


<a id="item-13"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">使用 DSPy 优化 Datasette Agent 的 SQL 提示</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Simon Willison 使用 DSPy 框架自动评估并改进了 Datasette Agent 的 SQL 系统提示，发现了列名猜测等问题并提出了提示优化建议。 该实验通过 Claude Code 使用了 GPT-4.1 mini 和 nano 模型，发现将列名包含在模式列表中或软化关于不要调用 describe_table 的建议可以减少错误重试循环。

🔗 [来源](https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/#atom-everything)

rss · Simon Willison · 7月2日 18:25

**背景**: DSPy 是斯坦福 NLP 实验室开发的框架，将 LLM 提示视为可优化的参数，利用训练数据和指标自动生成并选择更好的提示。Datasette Agent 是一个由 LLM 驱动的工具，可以执行只读 SQL 查询来回答用户关于数据的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dspy.ai/getting-started/gepa-optimization/">GEPA optimization - DSPy</a></li>
<li><a href="https://github.com/stanfordnlp/dspy">GitHub - stanfordnlp/dspy: DSPy: The framework for ... DSPy Framework — Programmatic Prompt Optimization (2026) Prompt Like a Data Scientist: Auto Prompt Optimization and ... [2604.04869] Optimizing LLM Prompt Engineering with DSPy ... Prompt Optimizer: DSpy. Introduction | by Nishtha kukreti ...</a></li>
<li><a href="https://github.com/datasette/datasette-agent">GitHub - datasette / datasette - agent : An LLM-powered agent for...</a></li>

</ul>
</details>

**标签**: `#DSPy`, `#prompt engineering`, `#Datasette Agent`, `#AI`, `#SQL`

</details>


<a id="item-14"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">美国热浪凸显 AI 数据中心能源压力</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

美国一场严重的热浪暴露了 AI 数据中心不断增长的能源需求对电网造成的日益严重的压力，引发了对基础设施韧性的担忧。 这一事件凸显了随着 AI 应用的加速，迫切需要可持续能源解决方案和电网升级，这将影响科技公司、政策制定者以及数据中心附近的社区。 AI 数据中心消耗大量电力用于训练大型语言模型和运行推理，其中 AI 计算占其能源使用的最大份额。在热浪期间，冷却需求进一步增加能耗，加剧了电网压力。

🔗 [来源](https://www.aljazeera.com/economy/2026/7/3/us-heatwave-raises-alarms-over-ai-data-centre-energy-demands?traffic_source=rss)

rss · Al Jazeera · 7月3日 19:48

**背景**: 数据中心是容纳 AI 工作负载计算基础设施的专用设施。随着 AI 热潮，其能源使用迅速增长，研究表明超大规模数据中心在电网压力下往往无法灵活削减负荷，这对电网运营商构成了挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pewresearch.org/short-reads/2025/10/24/what-we-know-about-energy-use-at-us-data-centers-amid-the-ai-boom/">US data centers’ energy use amid the artificial intelligence ...</a></li>
<li><a href="https://arxiv.org/html/2509.07218v1">Electricity Demand and Grid Impacts of AI Data Centers ...</a></li>
<li><a href="https://www.linkedin.com/posts/duthie-power-services_data-centers-the-grid-and-the-assumptions-activity-7412915839743492096-8We3">U.S. Energy Grid Strains from Data Centers | Duthie Power Services...</a></li>

</ul>
</details>

**标签**: `#AI`, `#data centers`, `#energy`, `#sustainability`, `#infrastructure`

</details>


</section>

<section class="cat cat-other" markdown="1">

## 📌 其他 (1)

<a id="item-15"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Costco 的仓储模式规避昂贵的最后一英里配送</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

一篇文章指出，Costco 的仓储会员店模式战略性地规避了昂贵的最后一英里配送问题，使其成为亚马逊电商模式的对立面。 这一分析凸显了影响物流成本、可持续性和消费者行为的基本商业战略差异，对零售业的未来具有启示意义。 Costco 的模式依赖顾客自行前往仓库并运输商品，从而消除了单件商品送货上门的需求，而这正是亚马逊的主要成本之一。

🔗 [来源](https://phenomenalworld.org/analysis/the-anti-amazon/)

hackernews · bookofjoe · 7月3日 15:14 · [社区讨论](https://news.ycombinator.com/item?id=48776044)

**背景**: 最后一英里配送问题是指将货物从运输枢纽运送到最终目的地的高成本和低效率，尤其是对于单个包裹。亚马逊投入巨资建立自己的最后一英里物流网络来管理这一成本。相比之下，Costco 采用仓储模式，顾客批量购买并自行将商品带回家，将最后一英里的负担转移给了消费者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Last_mile_(transportation)">Last mile (transportation) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Costco">Costco - Wikipedia</a></li>
<li><a href="https://www.damotech.com/blog/costco-warehouse-strategy">Inside Costco’s Warehouse Strategy: Efficient Layout & Supply Chain</a></li>

</ul>
</details>

**社区讨论**: 评论者就 Costco 的模式是否真正优越展开辩论，指出其不断增长的在线业务也涉及配送。一些人称赞规避最后一英里问题的智慧，而另一些人则指出了会员政策和非食品商品的地区差异。

**标签**: `#business strategy`, `#logistics`, `#e-commerce`, `#retail`, `#Costco`

</details>


</section>