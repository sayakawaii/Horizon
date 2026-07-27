---
layout: default
title: "Horizon Summary: 2026-07-27 (ZH)"
date: 2026-07-27
lang: zh
---

> 从 136 条内容中筛选出 13 条重要资讯。

---

<section class="cat cat-geopolitics" markdown="1">

## 🌐 国际局势 (1)

<a id="item-1"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">英国最高法院驳回巴林间谍软件豁免权主张</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

英国最高法院驳回了巴林王国关于国家豁免权的上诉，该上诉针对两名巴林异见人士的诉讼，他们声称自己在英国时电脑被感染了间谍软件。 这一里程碑式的裁决确立了法律先例，即外国政府因在英国境内对个人使用间谍软件可在英国法院被起诉，从而加强了对跨国镇压和网络间谍活动的问责。 该案涉及巴林据称对异见人士使用的德国制造的间谍软件。裁决否定了此类行为的国家豁免权，为针对其他国家的类似诉讼打开了大门。

🔗 [来源](https://www.aljazeera.com/news/2026/7/27/british-court-dismisses-bahrains-bid-to-block-activists-spyware-lawsuit?traffic_source=rss)

rss · Al Jazeera · 7月27日 20:32

**背景**: 国家豁免权通常保护外国政府免于在另一国法院被起诉。但对于在管辖范围内的商业活动或侵权行为存在例外。该裁决澄清，对位于英国的设备发动间谍软件攻击构成英国管辖范围内的侵权行为，从而突破了国家豁免权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amnesty.org/en/latest/news/2026/07/uk-supreme-court/">UK: Supreme Court ruling on Bahrain spyware case sends a ...</a></li>
<li><a href="https://www.computerweekly.com/news/366646130/Bahrain-cannot-claim-sovereign-immunity-for-spyware-attack-against-UK-dissidents-top-UK-court-rules">Bahrain denied sovereign immunity over spyware attack in UK</a></li>

</ul>
</details>

**标签**: `#spyware`, `#legal precedent`, `#cybersecurity`, `#human rights`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 科技 / AI (12)

<a id="item-2"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">vLLM v0.26.0 新增 Inkling 模型系列与重大优化</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

vLLM v0.26.0 提供了对 1 万亿参数 Inkling 多模态模型系列的 Day-0 支持，同时包含 DeepSeek-V4 性能优化、fp32 lm_head 支持以及灵活的注意力后端。该版本由 212 位贡献者提交了 411 次提交。 此版本显著提升了 LLM 推理效率与模型支持能力，使得 Inkling 和 DeepSeek-V4 等前沿模型能够以优化吞吐量投入生产部署。灵活的注意力后端和 KV 卸载改进惠及广泛的混合模型和大上下文模型。 关键技术亮点包括 Inkling 的分段 CUDA 图、为 DeepSeek-V4 带来 2.94% 端到端 TPOT 提升的专用路由内核，以及按 KV 缓存组选择注意力后端。该版本还通过分层二级存储和对象存储支持使 KV 卸载更加成熟。

🔗 [来源](https://github.com/vllm-project/vllm/releases/tag/v0.26.0)

github · khluu · 7月27日 01:06

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理引擎，广泛用于生产环境。Thinking Machines Lab 的 Inkling 模型是一个 1 万亿参数的多模态模型，支持文本、图像和音频输入，上下文长度可达 100 万 token。FlashAttention-4 (FA4) 是最新的注意力算法，针对 Hopper GPU 进行了优化，性能优于 FA3。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-07-15-inkling">TML Inkling on vLLM: Day-0 Support with Optimized Performance</a></li>
<li><a href="https://recipes.vllm.ai/thinkingmachines/inkling">thinkingmachines/inkling | vLLM Recipes</a></li>
<li><a href="https://alphasignal.ai/news/vllm-v0-26-0-ships-day-0-support-for-inkling-s-1t-parameter-multimodal-model">vLLM v0.26.0 Ships Day-0 Support for Inkling's 1T-Parameter ...</a></li>

</ul>
</details>

**社区讨论**: 社区表达了强烈的积极情绪，称赞对 Inkling 的快速 Day-0 支持以及 DeepSeek-V4 的大量性能工作。一些用户注意到版本的复杂性，并对详细的更新日志表示赞赏。

**标签**: `#vLLM`, `#LLM inference`, `#performance optimization`, `#model support`, `#open source`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">法官驳回谷歌用 DMCA 抗辩数据抓取</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

一名法官裁定谷歌的搜索结果页面不受版权保护，驳回了谷歌试图利用 DMCA 阻止 SerpAPI 抓取的行为。 该裁决确立了法律先例，即搜索引擎结果是事实汇编而非创造性作品，可能限制平台通过版权主张阻止数据抓取的能力。 案件核心在于谷歌搜索结果页面是否达到版权保护所需的原创性门槛；法官认定其缺乏足够的创造性。

🔗 [来源](https://www.techdirt.com/2026/07/27/judge-rejects-googles-attempt-to-dmca-its-way-out-of-being-scraped/)

hackernews · cdrnsf · 7月27日 18:15 · [社区讨论](https://news.ycombinator.com/item?id=49073513)

**背景**: DMCA 的反规避条款（第 1201 条）被平台用来主张抓取绕过了保护版权内容的技术措施。然而，版权法要求作品具有原创性和创造性。网络抓取是从网站自动提取数据的行为，常用于竞争分析或研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/07/google-wont-give-up-odd-war-against-ai-web-scraping-despite-court-loss/">Google won’t give up odd war against AI web scraping despite ...</a></li>
<li><a href="https://blog.ericgoldman.org/archives/2026/01/relitigating-hiq-labs-and-scraping-through-the-lens-of-the-dmca-1201-anti-circumvention-guest-blog-post.htm">Relitigating hiQ Labs and Scraping Through the Lens of DMCA ...</a></li>
<li><a href="https://capstonedc.com/insights/why-dmca-claims-against-web-scrapers-face-long-odds/">Why DMCA Claims Against Web Scrapers Face Long Odds</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持该裁决，批评谷歌利用法律手段对付小型抓取者。有人指出谷歌缺乏可行的搜索 API 是抓取的驱动因素，也有人对地图等整理数据的版权性提出担忧。

**标签**: `#DMCA`, `#web scraping`, `#copyright`, `#Google`, `#legal`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">研究人员攻破沃尔沃/埃彻车队平台，获得完全控制权</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

一名安全研究人员发现 VE 商用车公司的 My Eicher 车队管理平台存在严重漏洞，可未经授权访问所有用户和车辆。研究人员于 2025 年 11 月报告该问题，主要漏洞在数周内被修复，但完整披露于 2026 年 7 月发布。 此事件凸显了联网车辆平台中的严重安全风险，一个漏洞就可能危及整个车队。同时强调了负责任披露的重要性，以及围绕汽车维修权和云依赖性的持续争论。 研究人员发现未经验证的内部 API 暴露了 74.8 万客户、17.4 万用户和 67.6 万车辆，另一个 API 返回了 250 万个一次性密码。研究人员多次跟进后漏洞被修复，但未发布官方 CVE 或致谢。

🔗 [来源](https://eaton-works.com/2026/07/27/my-eicher-hack/)

hackernews · EatonZ · 7月27日 15:08 · [社区讨论](https://news.ycombinator.com/item?id=49070756)

**背景**: My Eicher 是沃尔沃集团与埃彻汽车合资企业 VE 商用车旗下的卡车和客车车队监控平台。车队管理系统通常依赖云 API 进行远程控制和监控，使其成为攻击者的目标。负责任披露是指在公开披露前私下向供应商报告漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eaton-works.com/2026/07/27/my-eicher-hack/">Exploiting Volvo/Eicher’s fleet management platform to gain ...</a></li>
<li><a href="https://daily.dev/posts/exploiting-volvo-eicher-s-fleet-platform-to-gain-control-over-all-users-vehicles-gkfj0eqmw">Exploiting Volvo/Eicher's fleet platform to gain control...</a></li>
<li><a href="https://www.eichertrucksandbuses.com/support-solutions/my-eicher">My Eicher | Fleet Monitoring Platform for Trucks & Buses</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬了研究人员在披露时间线上的耐心，指出公司响应缓慢。一些人表达了对现代汽车依赖云服务的广泛担忧，举例说明车辆因连接问题无法启动。其他人将讨论与维修权倡导以及 AI 对安全研究的潜在影响联系起来。

**标签**: `#security`, `#automotive`, `#vulnerability disclosure`, `#fleet management`, `#right-to-repair`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Moonshot AI 发布 3T 参数 MoE 模型 Kimi-K3</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Moonshot AI 在 HuggingFace 上发布了 Kimi-K3，这是一个拥有 3 万亿参数的混合专家（MoE）模型，并原生支持 mxfp4 量化。该模型以开放权重形式提供，采用自定义许可证。 此次发布标志着首个 3 万亿参数级别的开放模型诞生，使初创公司和研究人员能够定制和微调前沿模型。通过提供具有竞争力的开放权重，它挑战了专有模型的经济模式。 由于采用 mxfp4 量化，该模型托管需要约 1.5TB 显存，接近当前硬件（如 8 块 B200）的极限。许可证包含基于收入的条款：年收入超过 2000 万美元的实体需另行协商商业用途。

🔗 [来源](https://huggingface.co/moonshotai/Kimi-K3)

hackernews · nateb2022 · 7月27日 06:18 · [社区讨论](https://news.ycombinator.com/item?id=49065752)

**背景**: 混合专家（MoE）是一种神经网络架构，每次输入仅激活部分参数，从而在高效推理的同时支持更大模型。MXFP4 是一种 4 位浮点量化格式，可在保持大型模型精度的同时减少内存占用。开放权重模型允许用户下载、修改和自行托管，提供数据主权和定制化优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.08713">Unveiling the Potential of Quantization with MXFP4 ...</a></li>
<li><a href="https://rocm.blogs.amd.com/software-tools-optimization/mxfp4-mxfp6-quantization/README.html">High-Accuracy MXFP4, MXFP6, and Mixed-Precision Models on AMD ...</a></li>

</ul>
</details>

**社区讨论**: 社区对定制化和数据主权感到兴奋，用户注意到可以在专有数据上进行微调。然而，也有人担心托管成本（1.5TB 显存）以及模型自称“Claude”的 bug。许可证中的收入上限也引发了关于开源定义的讨论。

**标签**: `#AI`, `#LLM`, `#open-source`, `#MoE`, `#quantization`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Bun 的 Rust 重写进展与 v1.4 发布延迟</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Bun 的 Rust 重写已在一个多月前随 Claude Code 发布，但 v1.4 版本因尚未达到承诺的 Node.js 兼容性改进而延迟。 此次更新罕见地揭示了重大运行时重写的进展，凸显了在过渡到新语言的同时保持兼容性的挑战。 项目负责人 Jarred 表示 Rust 重写整体进展顺利，但 v1.4 版本因尚未达到特定数量的新增通过 Node.js 测试而被阻塞。实现该目标的 PR 已提交但尚未合并。

🔗 [来源](https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html)

hackernews · tomlockwood · 7月27日 11:12 · [社区讨论](https://news.ycombinator.com/item?id=49067854)

**背景**: Bun 是一个快速的全能 JavaScript 运行时、打包器和包管理器，最初用 Zig 编写。2025 年，团队宣布用 Rust 重写以提升性能和可维护性。Claude Code 是 Anthropic 开发的 AI 辅助编码工具，使用大语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/bun: Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一：有人指出重写进展顺利，也有人质疑使用 LLM 进行翻译，并提到像 'buz' 这样的替代方案声称修复了原始 Zig 代码库。讨论还强调了适应新代码库所需的时间。

**标签**: `#Bun`, `#Rust`, `#JavaScript runtime`, `#rewrite`, `#Node.js compatibility`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">LLM 令牌中继市场助长欺诈与滥用</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Matt Lenhard 的一项调查揭示了一个蓬勃发展的中继市场，通过汇集来自免费试用、被盗凭证和未受保护端点的 API 密钥，利用 one-api 和 new-api 等开源代理软件，以折扣价转售 LLM 令牌。 该市场提供了廉价访问 LLM 的途径，绕过了地理限制，并促进了模型蒸馏，给 LLM 提供商带来了重大的安全和收入风险，也引发了公开暴露应用的开发者的担忧。 中继市场主要位于中国，使用 one-api 及其分支 new-api 等开源代理面板来聚合和负载均衡多个账户的请求。买家寻求廉价令牌、规避地理封锁或收集数据用于模型蒸馏。

🔗 [来源](https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything)

rss · Simon Willison · 7月26日 19:30

**背景**: LLM API 提供商按令牌收费，许多还提供免费试用额度。转售者利用这些试用额度，以及被盗信用卡和未受保护的支持机器人，以低成本或零成本获取令牌，然后通过模仿官方 API 的代理服务转售。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/26/relay-market/">An Inside Look at the Relay Market Powering Token Resellers and Fraud</a></li>
<li><a href="https://vectoral.com/blog/token-relay-market">An Inside Look at the Relay Market Powering Token Resellers and Fraud | Vectoral</a></li>
<li><a href="https://github.com/songquanpeng/one-api">GitHub - songquanpeng/one-api: LLM API 管理 & 分发系统，支持 Open...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论强调了 API 安全问题以及需要更好的速率限制和支出上限。一些评论者指出，开源工具本身是合法的，但其滥用助长了欺诈。

**标签**: `#LLM`, `#API security`, `#fraud`, `#open-source`, `#token reselling`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Ruff v0.16.0 默认规则从 59 条扩展到 413 条</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Ruff v0.16.0 于 2026 年 7 月 23 日发布，默认启用的 lint 规则从 59 条增加到 413 条，扩大了七倍。这一变化导致未固定 Ruff 依赖的项目出现 CI 失败。 Ruff 现在默认启用 413 条规则，而 v0.1.0 中为 59 条，同时规则总数从 708 条增加到 968 条。新的默认规则优先处理语法错误和即时运行时错误，该工具为许多问题提供自动修复。

🔗 [来源](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything)

rss · Simon Willison · 7月25日 22:44

**背景**: Ruff 是一个用 Rust 编写的快速 Python linter 和格式化工具，重新实现了来自 Flake8、isort 和 pyupgrade 等工具的 900 多条规则。它由 Astral 开发，Astral 于 2026 年 3 月被 OpenAI 收购。默认规则集自 2023 年 10 月的 v0.1.0 以来未更新过。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://astral.sh/blog/ruff-v0.16.0">Ruff v0.16.0 - Astral</a></li>
<li><a href="https://docs.astral.sh/ruff/linter/">The Ruff Linter | Ruff - Astral</a></li>
<li><a href="https://pypi.org/project/ruff/">ruff · PyPI</a></li>

</ul>
</details>

**社区讨论**: 社区讨论指出，虽然扩展的默认规则提高了代码质量，但会导致未固定依赖的项目出现严重的 CI 中断。一些开发者赞赏对细微错误的捕获，而另一些则对突然需要修复数百个问题表示不满。

**标签**: `#Python`, `#linting`, `#Ruff`, `#tooling`, `#release`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">NVIDIA Cosmos-H-Dreams：手术机器人的实时生成式仿真</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

NVIDIA 发布了 Cosmos-H-Dreams，这是一个用于手术机器人的实时、动作条件生成式世界模型，允许人类操作员或学习策略实时与合成的手术场景交互。它是 Cosmos-H-Surgical-Simulator 的微调变体，带有支持键盘或 Meta Quest 控制器输入的流式服务器。 该框架通过生成逼真的交互式仿真，将手术机器人训练时间从数小时大幅缩短至几分钟，解决了医疗机器人领域关键的数据稀缺问题。它有助于更安全、更高效地开发自主手术系统，可能改善患者预后。 Cosmos-H-Dreams 基于 NVIDIA 的 Cosmos 世界模型平台构建，并在 Hugging Face 上以开源检查点形式提供。它使用流式服务器提供实时仿真，且模型是动作条件化的，能够响应来自键盘或 VR 控制器的实时输入。

🔗 [来源](https://huggingface.co/blog/nvidia/cosmos-h-dreams)

rss · Hugging Face Blog · 7月27日 09:32

**背景**: 传统的手术机器人训练依赖于昂贵的物理设备或预录数据集，这些数据集在多样性和规模上有限。像 Cosmos-H-Dreams 这样的生成式世界模型可以创建合成但物理可信的环境，并支持实时交互，从而在没有真实世界风险的情况下实现快速策略学习和测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/isaac-for-healthcare/Cosmos-H-Dreams">GitHub - isaac-for-healthcare/Cosmos-H-Dreams</a></li>
<li><a href="https://huggingface.co/nvidia/Cosmos-H-Dreams">nvidia/Cosmos-H-Dreams · Hugging Face</a></li>
<li><a href="https://isaac-for-healthcare.github.io/medical-physics-simulation/cosmos_h_dreams/">Cosmos-H-Dreams - NVIDIA Isaac for Healthcare</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#generative simulation`, `#surgical robotics`, `#AI`, `#real-time`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Paged Out #9：一本设计精美的黑客杂志</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Paged Out #9 已发布，这是一本让人联想到 Phrack 和 2600 的免费 PDF 杂志，包含关于 C 语言编程、亚像素渲染和可计算铺砌等主题的深度技术文章。 该杂志满足了黑客爱好者对主流出版物之外的高质量、深度技术内容的需求，社区参与度表明它备受重视。 这期 68 页的杂志包含《C 语言入门》、《亚像素动物园》以及一篇关于可计算铺砌的文章，后者独立重新发现了 1960 年代王浩的工作。杂志设计精美，配有光栅图像艺术。

🔗 [来源](https://pagedout.institute/download/PagedOut_009.pdf)

hackernews · laurensr · 7月27日 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49070138)

**背景**: Paged Out 是一本免费的、由社区驱动的技术杂志，涵盖从编程到复古计算的广泛主题。它在精神上类似于经典的黑客杂志 Phrack 和 2600，这些杂志在黑客文化历史上具有影响力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Subpixel_rendering">Subpixel rendering</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-0-387-09680-3_13">Computability of Tilings | Springer Nature Link</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了杂志的幽默和深度，有人指出《C 语言入门》文章非常搞笑。另一人强调了亚像素渲染文章，还有一人指出可计算铺砌文章是未注明出处的对 1960 年代王浩工作的重新发现。

**标签**: `#hacker culture`, `#technical magazine`, `#programming`, `#computer science`, `#retro computing`

</details>


<a id="item-11"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">从 React 迁移到 HTMX 构建论坛界面</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Misago 论坛项目从其代码库中移除了 React.js，转而采用 HTMX 实现 UI 交互，从而实现了更简单的服务端渲染架构。这一迁移在 2023 年的案例研究中被记录，并引发了广泛的社区讨论。 该案例研究展示了重型客户端框架的替代方案，表明 HTMX 可以有效替代许多交互式 UI 中的 React。它验证了超媒体驱动的方法，并可能鼓励其他项目考虑更简单的、以服务器为中心的架构。 HTMX 通过自定义属性扩展 HTML，无需编写 JavaScript 即可直接使用 AJAX、WebSocket 和服务器发送事件。此次迁移使 Misago 在降低复杂性的同时，保持了动态功能，如部分页面更新和通过服务器发送事件实现的实时更新。

🔗 [来源](https://misago-project.org/t/removing-reactjs-from-the-codebase-and-adapting-htmx-for-ui-interactivity/1267/)

hackernews · Ralfp · 7月27日 09:58 · [社区讨论](https://news.ycombinator.com/item?id=49067301)

**背景**: React 是一个流行的用于构建客户端用户界面的 JavaScript 库，但它需要大量的 JavaScript 代码和客户端处理。HTMX 由 Carson Gross 创建，提供了一种超媒体驱动的替代方案，将逻辑保留在服务器端，并通过网络发送 HTML 片段。这种方法可以简化开发，并提高像论坛这样内容密集型网站的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Htmx">Htmx</a></li>
<li><a href="https://htmx.org/">htmx - high power tools for html</a></li>
<li><a href="https://en.wikipedia.org/wiki/Server-side_rendering">Server-side rendering</a></li>

</ul>
</details>

**社区讨论**: 社区成员普遍称赞这次迁移，认为 HTMX 非常适合服务端渲染的应用程序和论坛。一些人分享了替代工具如 PyView（受 Phoenix LiveView 启发），并推荐将 HTMX 与 DaisyUI+TailwindCSS 搭配使用。少数人提醒注意大型 HTML 响应可能带来的性能问题，但总体情绪是积极的。

**标签**: `#HTMX`, `#React`, `#web development`, `#server-side rendering`, `#JavaScript frameworks`

</details>


<a id="item-12"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Libsm64：将《超级马里奥 64》作为可复用库供游戏引擎使用</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Libsm64 将《超级马里奥 64》的角色和物理引擎提取为独立的共享库，开发者可通过简单的 C API 将马里奥集成到任何外部游戏引擎中。 该项目展示了一种将经典游戏资产重新用作可复用组件的新颖方法，无需依赖专有元宇宙平台即可实现创意混搭，例如在《半条命 2》中加入马里奥。 该库的整个外部 API 定义在单个头文件（libsm64.h）中，客户端项目只需包含该头文件并加载库即可。它基于原版《超级马里奥 64》的反编译构建。

🔗 [来源](https://github.com/libsm64/libsm64)

hackernews · klaussilveira · 7月27日 10:04 · [社区讨论](https://news.ycombinator.com/item?id=49067352)

**背景**: 《超级马里奥 64》是 1996 年任天堂 64 上的一款里程碑式平台游戏。近年来，该游戏的源代码被完全逆向工程，催生了原生 PC 移植版以及像 libsm64 这样提取特定组件以供复用的项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/libsm64/libsm64">GitHub - libsm64/libsm64: Mario 64 as a library for use in external game engines · GitHub</a></li>
<li><a href="https://grokipedia.com/page/libsm64">libsm64</a></li>

</ul>
</details>

**社区讨论**: 社区反响非常积极，评论称其“不可思议”，并将其比作元宇宙概念的实际实现。用户分享了演示视频和一份使用 libsm64 的项目精选列表，显示出浓厚的兴趣和实用价值。

**标签**: `#game development`, `#reverse engineering`, `#open source`, `#library`, `#retro gaming`

</details>


<a id="item-13"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">英伟达计划投资 2500 亿美元支持 OpenAI 基础设施</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

英伟达宣布了一项 2500 亿美元的投资计划，以支持 OpenAI 的基础设施建设，包括数据中心和 AI 计算资源。此举正值美国多个州出现政治反对声音并提议禁止新建数据中心之际。 这笔巨额投资凸显了前沿 AI 开发对资本的巨大需求，并突显了 AI 快速扩张与监管阻力之间的紧张关系。它可能重塑 AI 基础设施的竞争格局，并影响关于数据中心监管的政策辩论。 2500 亿美元的规模是史上最大的企业基础设施投资之一，目标涵盖数据中心、能源和网络。由于多个州以环境和能源问题为由提议禁止新建数据中心，该计划面临不确定性。

🔗 [来源](https://www.aljazeera.com/economy/2026/7/27/nvidia-plans-250bn-push-to-bolster-openais-infrastructure-ambitions?traffic_source=rss)

rss · Al Jazeera · 7月27日 21:08

**背景**: 英伟达是 AI 芯片的主导供应商，尤其是用于训练大型模型（如 OpenAI 的 GPT 系列）的 GPU。OpenAI 需要庞大的计算基础设施来训练和部署其 AI 系统，英伟达的投资旨在确保这一能力。数据中心消耗大量电力和水资源，引发环境担忧和当地反对。

**标签**: `#Nvidia`, `#OpenAI`, `#AI infrastructure`, `#data centers`, `#regulation`

</details>


</section>