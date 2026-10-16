---
layout: default
title: "Horizon Summary: 2026-10-16 (ZH)"
date: 2026-10-16
lang: zh
---

> 从 135 条内容中筛选出 19 条重要资讯。

---

<section class="cat cat-tech" markdown="1">

## 🔬 科技 / AI (19)

<a id="item-1"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">Claude AI 揭示 NIST ECDSA 曲线种子来源</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

Anthropic 的 Claude AI 发现，NIST P-192、P-224、P-256、P-384 和 P-521 椭圆曲线的种子是使用 C 库的 lrand48 伪随机数生成器并以 Unix 时间戳作为种子生成的，从而解开了一个长达数十年的密码学谜团。第五个二进制种子 B-163 仍无法解释，可能是发布时的笔误所致。 这一发现驳斥了长期以来关于 NSA 故意削弱曲线的阴谋论，恢复了人们对广泛使用的密码学标准的信心。它还展示了 AI 在解决计算机科学中复杂长期问题方面的潜力。 种子是使用 lrand48（一种采用 48 位算术的线性同余生成器）生成的，并以 Unix 时间戳作为种子。虽然生成方法已确认，但这并不能排除曲线是从众多候选者中挑选出来以具有特定属性的可能性，因为生成过程持续了数月，且被丢弃的候选者未知。

🔗 [来源](https://www.anthropic.com/research/ecdsa-curve-origins)

hackernews · ahlCVA · 10月16日 18:55 · [社区讨论](https://news.ycombinator.com/item?id=50122800)

**背景**: ECDSA 是最广泛使用的椭圆曲线密码学标准，由 NIST 于 2000 年作为 FIPS 186-2 的一部分采纳。该标准规定了不同大小和安全级别的曲线，但其种子的来源未知，引发了关于潜在后门的猜测。lrand48 是 C 库中常见的伪随机数生成器，生成 48 位整数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://saweis.net/posts/nist-curve-seed-origins.html">How were the NIST ECDSA curve parameters generated ?</a></li>
<li><a href="https://www.anthropic.com/research/ecdsa-curve-origins">Claude reveals ECDSA curve origins \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区普遍庆祝这一发现，一些人指出它驳斥了多年的阴谋论。然而，像 fidotron 这样的评论者警告说，生成方法并不能证明曲线没有被挑选以具有特定属性，其他人则指出无法解释的 B-163 种子可能是笔误。

**标签**: `#cryptography`, `#ECDSA`, `#NIST`, `#AI`, `#random-number-generator`

</details>


<a id="item-2"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">Reflection AI 在 Hugging Face 发布 501B 开源权重模型 Beam</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

Reflection AI 在 Hugging Face 上发布了其首个开源权重模型 Beam，模型标识为 reflection/Beam-1.0-501B-A23B。Beam 是一个稀疏混合专家（MoE）模型，总参数量达 5010 亿，激活参数为 230 亿，专为编程、推理和智能体（agentic）任务设计。 这是开源 AI 领域的一个重要里程碑，因为用户可以拥有、定制和扩展的 5010 亿参数模型，让社区前所未有地获得了此前仅限于闭源实验室的大规模能力。这可能加速编程助手、自主智能体以及各行业领域微调等方面的创新。 Beam 采用稀疏混合专家架构，每个 token 仅激活 5010 亿参数中的 230 亿，从而在保持大模型容量的同时提升推理效率。它以开源权重形式在 Hugging Face 上发布，允许下载、本地部署和微调，但完整模型仍需要大量计算资源。

🔗 [来源](https://huggingface.co/blog/reflection-beam)

rss · Hugging Face Blog · 10月16日 00:00

**背景**: 混合专家（MoE）是一种神经网络设计，将多个专门的子网络（专家）组合起来，每次输入只激活其中一部分，从而降低计算成本。开源权重模型是指训练后的参数公开释放，任何人都可以运行、修改或微调，与只能通过 API 访问的闭源模型形成对比。Hugging Face 是分享和托管此类模型的领先平台，而 Reflection AI 是一家新进入开源模型领域的美国实验室。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/reflection-beam">Welcome Beam: a 501B open model you can own, customize, and scale</a></li>
<li><a href="https://reflection.ai/blog/introducing-beam">Introducing Beam: Reflection’s 501B open-weight model</a></li>
<li><a href="https://www.unite.ai/reflection-ai-unveils-beam-a-501b-parameter-open-weight-model/">Reflection AI Unveils Beam, a 501B-Parameter Open-Weight Model</a></li>

</ul>
</details>

**标签**: `#open-source`, `#large language models`, `#AI`, `#Hugging Face`, `#model release`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">Meta 发布 Muse Spark Open：开放权重前沿多模态 MoE 模型</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

Meta 发布了 Muse Spark Open，这是一个开放权重的前沿多模态混合专家（MoE）模型，并已在 Hugging Face 上公开。这是对开源 AI 的重要贡献，让研究人员和开发者能够直接获取前沿级多模态模型的权重。 以开放权重形式发布前沿多模态 MoE 模型，显著提升了开源 AI 的能力，使社区能够研究、微调并基于这一最先进模型构建应用。这也会加剧与闭源前沿实验室的竞争，并可能加速整个生态系统的研究与产品开发。 该模型采用混合专家（MoE）架构，通过将多个专门化的子网络（专家）与门控机制结合来提升容量，门控机制对每个输入仅激活一部分专家，从而提高效率。作为开放权重发布，其训练好的参数可公开下载；其多模态设计意味着它能处理和整合文本、图像、音频或视频等多种数据类型。

🔗 [来源](https://huggingface.co/blog/meta-muse-spark-open)

rss · Hugging Face Blog · 10月15日 00:00

**背景**: 混合专家（MoE）是一种神经网络架构，通过将多个专门化的子网络（专家）与门控机制结合来提升模型容量，门控机制对每个输入选择性地激活一部分专家。开放权重模型是指其训练好的参数（权重和偏置）被公开发布的 AI 模型，任何人都可以下载、运行、研究并修改它们。多模态学习是一种深度学习方式，能够整合和处理文本、音频、图像或视频等多种数据类型，从而支持视觉问答、图像描述等任务。自 2023 年以来，像 Google Gemini 和 GPT-4o 这样的大型多模态模型日益流行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_artificial_intelligence">Open weights - Wikipedia</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_model">Multimodal model</a></li>

</ul>
</details>

**标签**: `#multimodal`, `#mixture-of-experts`, `#open-weight`, `#Meta`, `#AI`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">特斯拉发布搭载冷气与火箭推进器的飞行版 Roadster 原型车</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

特斯拉发布了一款全新 Roadster 原型车，配备冷气推进器和可选装的燃烧火箭发动机，并在视频中演示了垂直起飞、吸附天花板等特技。该车提供两种模式：用于额外向前加速的冷气版本，以及演示中展示的仅限受邀用户购买的燃烧火箭版本。 这一发布通过将 SpaceX 衍生的推进技术集成到高性能电动汽车中，突破了汽车工程的边界，引发了关于可行性、经济性和安全性的激烈辩论。它可能影响未来的车辆设计，并重新点燃人们对飞行汽车的兴趣，尽管实际应用和监管障碍依然巨大。 冷气推进器系统使用 10,000 psi 的 COPV（复合材料缠绕压力容器）和 SpaceX 衍生的推进器，以帮助实现声称的 0.8 秒 0-60 英里/小时加速；燃烧火箭版本仅限受邀用户，燃料可能非常有限，只能进行短暂跳跃。据报道，预订冷气选项需要 25 万美元定金，并声称 2028 年投产。

🔗 [来源](https://www.tesla.com/roadster)

hackernews · shekhar101 · 10月16日 01:32 · [社区讨论](https://news.ycombinator.com/item?id=50112657)

**背景**: 冷气推进器是一种火箭发动机，利用加压惰性气体的膨胀产生推力，无需燃烧，因其简单可靠而常用于航天器姿态控制。火箭发动机根据牛顿第三定律，通过高速喷射反作用质量产生推力。eVTOL（电动垂直起降）飞行器是一类专为垂直飞行设计的电动飞机，但将此类系统集成到合法上路的汽车中面临着独特的工程和监管挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.motortrend.com/news/tesla-roadster-thrust-system-spacex-technology-explained">How Did the Tesla Roadster Fly? Here's How It Works - MotorTrend Tesla's Flying Roadster: What Was Shown, How Cold-Gas ... Cold Gas Thrusters - moog.com Tesla's redesigned Roadster has a cold-gas thruster option ... Cold Gas Thruster – Definition & Detailed Explanation ... How Tesla’s Roadster fan system and thrusters are built to ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cold_gas_thruster">Cold gas thruster</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论两极分化严重：许多人称赞这一工程壮举令人难以置信，是有史以来最酷的演示之一；而另一些人则批评其在经济上不可行、危险，更像是马戏团特技而非可量产汽车。一些评论者指出，底层技术已为人所熟知，并非革命性突破，并质疑有限压缩气体储存的实际可行性。

**标签**: `#Tesla`, `#electric vehicles`, `#rocket propulsion`, `#engineering`, `#Hacker News`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">PS5LM 让越狱 PS5 原生运行 GGUF 语言模型</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

一个名为 PS5LM 的新开源项目（托管于 github.com/cobanov/PS5LM）让越狱后的 PlayStation 5 能够原生运行 GGUF 格式的语言模型，据称可以以 2 比特量化运行 Qwen 3.8 27B 等模型。这表明该主机的定制 AMD APU 无需 PC 即可充当低成本的 AI 推理设备。 这表明被锁定的消费级硬件可以被改造成通用 AI 推理设备，可能为爱好者和中小型运营者提供一种比专用 GPU 更便宜的方案，用于长时间、低强度的 LLM 任务。这也进一步激发了人们对越狱主机以及在游戏中使用 LLM 驱动 NPC 的兴趣。 该项目依赖 llama.cpp 和 GGUF 模型格式，社区成员指出它只能以 2 比特量化运行 Qwen 3.8 27B，这会限制输出质量。评论者估算每天电费约 70 美分即可产出约 200 万个输出 token，并认为同样的方法或许也能用在基于 AMD 精简版“Cyan Skillfish” APU 的 BC250 矿卡上。

🔗 [来源](https://github.com/cobanov/PS5LM)

hackernews · Anon84 · 10月16日 18:32 · [社区讨论](https://news.ycombinator.com/item?id=50122431)

**背景**: llama.cpp 是一个用于在本地运行大型语言模型的开源库，被广泛视为 Ollama 和 LM Studio 等工具背后的实际标准。GGUF 是 llama.cpp 用来存储量化模型的文件格式，它通过牺牲一定精度来缩小模型体积和内存占用。越狱 PS5 意味着绕过索尼的软件限制，让用户可以运行未签名的自制软件，此前这一做法已让该主机能够运行模拟器和媒体应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://github.com/phantomptr/ps5upload">GitHub - phantomptr/ps5upload: Send games, apps and homebrew ...</a></li>
<li><a href="https://github.com/mihawk-99/PS5_RetroArch">GitHub - mihawk-99/PS5_RetroArch: RetroArch Homebrew for ...</a></li>

</ul>
</details>

**社区讨论**: 评论者总体热情高涨：有人表示这套方案非常适合监控服务器错误率或安防录像等长时间运行的任务，还有人说自己第一次因此考虑购买 PS5。也有人提出实际担忧，包括警告 GitHub 可能迫于索尼压力下架该页面、建议项目使用自有域名，以及猜测 LLM 驱动的 NPC 可能成为游戏标配。

**标签**: `#llama.cpp`, `#PS5`, `#jailbreak`, `#GGUF`, `#AI inference`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Mercor 报告：美国 90%工作时间缺乏 AI 基准测试覆盖</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Mercor 的一份研究报告发现，美国 90%的工作时间花在现有 AI 基准测试几乎没有覆盖的任务上，这使得人们很难评估 AI 模型在美国人实际从事的工作中表现如何。分析还显示，即使控制了 AI 暴露度，工资总额更高的职业所对应的 O*NET 任务在基准测试提示中仍被显著过度代表。 这一缺口意味着基准测试分数可能无法预测大多数工作的实际效用，从而可能误导企业、政策制定者和劳动者对 AI 真实能力及自动化风险的判断。它还表明 AI 开发在经济上偏向高薪职业，这可能会影响哪些岗位成为自动化的目标。 该报告将基准测试提示映射到 O*NET 职业任务，发现绝大多数工作时间对应的覆盖要么很薄弱要么完全缺失，而工资总额高的职业则被过度代表。社区评论者指出，“覆盖良好”有时仅意味着少量提示，例如针对“为有育儿问题的父母提供咨询”只有 13 条提示，无法代表这类工作的全部范围。

🔗 [来源](https://www.mercor.com/research/labor-index/benchmark-map/)

hackernews · speckx · 10月16日 17:08 · [社区讨论](https://news.ycombinator.com/item?id=50121179)

**背景**: AI 基准测试是用于比较模型能力的标准化测试，但它们通常聚焦于学术或编程任务，而非真实工作的全部范围。O*NET 是美国劳工部的一个数据库，描述职业任务和要求，常被用于研究自动化以及劳动力市场对 AI 的暴露程度。Mercor 是一家研究与数据公司，与主要 AI 实验室合作构建基准测试和评估工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mercor.com/research/">Mercor Research | Frontier AI Training Data & Human Evaluation</a></li>
<li><a href="https://laweconcenter.org/resources/ai-productivity-and-labor-markets-a-review-of-the-empirical-evidence/">AI, Productivity, and Labor Markets: A Review of the ...</a></li>
<li><a href="https://www.anthropic.com/research/labor-market-impacts">Labor market impacts of AI: A new measure \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认同该发现揭示了严重的衡量缺口，并引用“门卫谬误”来论证自动化忽视了工作中隐藏的功能。一些人批评企业用 AI 取代客服人员，另一些人质疑“覆盖良好”是否真的只意味着少量提示，还有人表示 AI 已经让自己一半的工作变得更容易。

**标签**: `#AI benchmarks`, `#labor economics`, `#AI impact on jobs`, `#benchmark coverage`, `#future of work`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">StarSkirmish Bench v0.2 用《星际争霸》机器人编程评测旗舰大模型</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

StarSkirmish Bench v0.2 发布，评测 OpenAI、Anthropic、Google 和 Meta 的旗舰大模型通过编写机器人代码来玩《星际争霸：母巢之战》的能力。每个模型都在其所属实验室的第一方 CLI 工具（Claude Code、Codex、Antigravity CLI、Muse Code）中以最高推理档位运行，网络搜索与抓取功能被关闭，限时一小时。 这提供了一个新颖的智能体编程基准，在即时战略环境中测试长周期代码生成能力，而非孤立的编程题目。它与一个独立的 9x9 围棋基准排名高度一致，说明它可能捕捉到一种可泛化的模型能力信号，对智能体开发者和模型评测者都有参考价值。 评测工具的网络搜索和抓取功能被关闭，智能体没有其他互联网访问权限；CLI 在计时开始前预装，一小时从智能体启动时算起，且没有提交工具。社区成员指出，排名前列的模型顺序（GPT-6 Astra > GPT-6.1 Sol > Gemini 4 Argon > Claude Opus 5.5 > Claude Fable 5.1 > Claude Sonnet 5.5）与一个独立的 GoBench 排名完全一致，并质疑智能体编写的机器人是否学到了超越劣质人类机器人策略之外的东西。

🔗 [来源](https://starskirmish.com/bench/v0-2/)

hackernews · __cayenne__ · 10月16日 14:18 · [社区讨论](https://news.ycombinator.com/item?id=50118688)

**背景**: 《星际争霸：母巢之战》是暴雪于 1998 年推出的即时战略资料片，至今仍是竞技游戏的重要项目，尤其在韩国，并自 2017 年起可免费下载。StarSkirmish Bench 是一个让大模型创建《母巢之战》机器人的竞技场，本次 v0.2 更新加入了 OpenAI、Anthropic、Google 和 Meta 旗舰模型的结果。常见的大模型编程基准通常衡量代码补全或调试等任务，而该基准评测的是智能体在时间和工具限制下编写完整机器人程序的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://starskirmish.com/bench/">StarSkirmish Bench</a></li>
<li><a href="https://en.wikipedia.org/wiki/StarCraft:_Brood_War">StarCraft: Brood War</a></li>
<li><a href="https://modernorange.io/item/49858284">Show HN: StarSkirmish , an arena where LLMs... | Modern Orange</a></li>

</ul>
</details>

**社区讨论**: 评论者认为该基准很有意思，有人指出其排名与一个独立的 9x9 围棋基准（GoBench）完全一致，说明跨基准具有一致性。也有人质疑，在如此短的时间限制下，智能体编写的机器人是否只是最佳人类机器人的劣化版本，以及它们是否是在人类机器人代码上训练的，还是只是重复应用相同的技术。还有评论者强调了评测工具的技术细节，并提到了另一个让大模型直接玩《星际争霸》的相关基准。

**标签**: `#llm-benchmark`, `#starcraft`, `#ai-agents`, `#code-generation`, `#game-ai`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">OpenBSD 37 年内核漏洞被利用获取 root 权限</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

安全公司 Calif 于 2026 年 10 月 16 日发布了一个概念验证漏洞利用程序，通过串联两个长期存在的 OpenBSD 内核缺陷——其中一个可追溯到约 37 年前的原始 BSD 源代码——实现了本地权限提升并获取 root 权限。该主要漏洞位于 SysV 共享内存子系统中，OpenBSD 项目已将其修复。 这表明即使是世界上审计最严格的代码库之一，也可能隐藏关键漏洞长达数十年，动摇了仅靠代码审查就能保证内核安全的假设。它凸显了将人工分析与模糊测试和静态分析相结合的必要性，以捕捉自动化工具常常遗漏的细微逻辑缺陷。 该漏洞利用串联了两个内核缺陷，主要漏洞源自原始 BSD 源代码并在 OpenBSD 中存活了约 37 年；它在 1999 年 8 月 NetBSD 重写该代码时被意外修复。该漏洞影响 SysV 共享内存实现，需要人工推理漏洞利用原语，而仅靠模糊测试或静态分析难以发现。

🔗 [来源](https://calif.io/research/big-fish)

hackernews · rs_rs_rs_rs_rs · 10月16日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=50118977)

**背景**: OpenBSD 是一个类 Unix 操作系统，以其注重安全的开发流程和广泛的代码审计而闻名。此类系统中的内核漏洞尤其危险，因为它们可以让无特权的本地用户提升为 root，从而完全控制机器。SysV 共享内存子系统是从 System V Unix 继承的遗留进程间通信机制，其年代久远使其成为容易被忽视的缺陷的温床。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/37-year-old-kernel-openbsd-flaw/">37-Year-Old Kernel Flaw Exploited to Gain Root Access on ...</a></li>
<li><a href="https://thedailytechfeed.com/37-year-old-kernel-bug-in-openbsd-finally-patched-after-root-exploit-poc/">37-Year-Old Kernel Bug in OpenBSD Finally Patched After Root ...</a></li>
<li><a href="https://www.openbsd.org/security.html">OpenBSD: Security</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了 OpenBSD Release 风格的图形，并指出该漏洞在 1999 年 NetBSD 重写时被意外修复。一个关键争论集中在模糊测试或静态分析是否真能发现这类漏洞，许多人认为这需要人类对漏洞利用原语的洞察。

**标签**: `#OpenBSD`, `#kernel`, `#security`, `#vulnerability`, `#exploit`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Anthropic 在 IPO 前告知投资者第三季度营收达 168 亿美元</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

据报道，Anthropic 周三告知投资者，其 2026 年第三季度营收环比增长近 50%，达到 168 亿美元，高于第二季度的 115 亿美元和第一季度的约 48 亿美元，公司正筹备 IPO。公司还披露，竞争对手实验室的模型蒸馏贡献了 5% 至 7% 的营收，并表示已在第三季度大幅削减了这类活动。 这些数字显示 Anthropic 的营收增速在企业软件领域极为罕见，而竞争对手斥资数亿美元蒸馏其模型的披露，则凸显出前沿 AI 实验室之间既竞争又相互变现的复杂关系。公司从年化流水收入转向季度营收口径，也表明其正在构建更常规、更符合 IPO 要求的财务叙事。 第三季度，Anthropic 每支出 1 美元算力成本可带来 1.70 美元收入，剔除股权激励后的调整后营业利润率为 11%。按 5% 的比例推算，未具名的竞争对手实验室仅第二季度就可能花费超过 5 亿美元用于蒸馏 Anthropic 的模型。

🔗 [来源](https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/)

rss · Simon Willison · 10月15日 13:04

**背景**: 模型蒸馏是一种机器学习技术，即用更大、更强模型生成的输出训练更小、更便宜的模型，使其能以低得多的成本在特定任务上接近大模型的性能。当竞争对手实验室通过 Anthropic 这类商业 API 进行蒸馏时，必须为生成训练数据所需的大量调用付费，这使竞争威胁同时变成了收入来源。Anthropic 是一家以 AI 安全为宗旨、开发 Claude 系列模型的公司，若成功上市，它将成为规模最大的纯 AI 上市公司之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://openai.com/index/api-model-distillation/">Model Distillation in the API - OpenAI</a></li>

</ul>
</details>

**标签**: `#anthropic`, `#ai-industry`, `#ipo`, `#revenue`, `#model-distillation`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">NVIDIA 与 Hugging Face 将印度语言预训练扩展至 2.8 万亿 Token</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

NVIDIA 与 IIT Madras 及其 AI4Bharat 实验室合作，发布了 Nemotron-pretraining-Indic-v1，这是一个约 2.8 万亿 Token、覆盖 22 种印度语言的合成预训练语料库，并在 Hugging Face 博客上介绍了配套的开放、GPU 加速的数据生成流水线。该语料库包含约 2601.0 亿原生文字 Token 和 224.6 亿罗马化 Token，均使用 Gemma-4 分词器统计。 印度语言长期以来在大语言模型预训练数据中代表性不足，因此这一发布为研究人员和开发者构建多语言模型提供了规模大得多的公开资源。开放的生成流水线还使团队能够将语料库扩展到新的语言和领域，而不必依赖单一固定数据集。 该语料库是合成数据，覆盖 22 种印度表列语言，混合了原生文字和罗马化文本，流水线经过 GPU 加速，使大规模数据整理变得可行。博客还指出，该数据混合将数学、代码和问答内容等精选英文材料引入印度语言。

🔗 [来源](https://huggingface.co/blog/nvidia/scaling-indic-pretraining)

rss · Hugging Face Blog · 10月16日 01:44

**背景**: 预训练是语言模型在针对特定任务微调之前，从海量文本中学习通用模式的阶段，文本的数量和质量在很大程度上决定了模型的能力。包括大多数印度语言在内的许多低资源语言，其数字化文本远少于英语，因此像 AI4Bharat 的 Sangraha 以及如今的 Nemotron-pretraining-Indic-v1 这样的项目都专注于构建大规模、经过清洗的语料库。合成数据生成——即由模型或流水线生成额外训练文本——已成为缩小这一差距的常见方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.explainx.ai/blog/nvidia-indic-pretraining-2-8-trillion-tokens-open-pipeline-2026">Nemotron Indic Pretraining: 2.8T Tokens, 22 Languages ...</a></li>
<li><a href="https://www.unite.ai/nvidia-unveils-2-8t-token-indic-pretraining-corpus-and-open-pipeline/">NVIDIA Unveils 2.8T-Token Indic Pretraining Corpus and Open ...</a></li>

</ul>
</details>

**标签**: `#NLP`, `#multilingual`, `#pretraining`, `#Indic languages`, `#open data`

</details>


<a id="item-11"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">FLUX.3 Image Klein 正式接入 Hugging Face Diffusers</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Black Forest Labs 发布了 FLUX.3 Image Klein，这是一个拥有 56 亿参数的开源权重模型，支持文生图、图像编辑以及最多使用 10 张参考图的多参考合成；Hugging Face 同时宣布该模型已集成到 Diffusers 库中，官方 diffusers 权重也已上传至模型仓库。 这让机器学习社区能够通过 Hugging Face 广泛使用的模块化工具箱 Diffusers 立即、标准化地使用这一先进的图像生成与编辑模型，降低了开发者构建生成式 AI 应用的门槛，也强化了重大模型发布时同步提供一流开源库支持的趋势。 该模型与完整版 FLUX 3 Image 共享核心能力，包括原生 4K 生成、像素级精确编辑，以及可控制元素位置或将编辑限制在指定区域的边界框功能；它使用 Qwen3-VL-4B-Instruct 作为文本编码器，并通过同一个模型完成文生图、单参考编辑和多参考合成任务。

🔗 [来源](https://huggingface.co/blog/flux-3)

rss · Hugging Face Blog · 10月15日 00:00

**背景**: 扩散模型是一类通过迭代去噪随机噪声来生成图像的生成式 AI，Stable Diffusion 和 Google 的 Imagen 等知名系统都基于这一技术。Hugging Face 的 Diffusers 库是一个用于运行和微调预训练扩散模型的模块化工具箱，提供简洁的 from_pretrained API，并可访问 Hugging Face Hub 上数万个模型检查点。FLUX 是 Black Forest Labs 推出的图像生成模型系列，而 'Klein' 变体是体积更小、权重开放的版本，旨在让该技术得到更广泛的普及。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bfl.ai/blog/flux-3-image-klein">FLUX 3 Image Klein: open weights, 5.6B parameters | Black ...</a></li>
<li><a href="https://huggingface.co/black-forest-labs/flux-3-image-klein">black-forest-labs/flux-3-image-klein · Hugging Face</a></li>
<li><a href="https://huggingface.co/docs/diffusers/index">Diffusers - Hugging Face</a></li>

</ul>
</details>

**标签**: `#diffusion-models`, `#image-generation`, `#hugging-face`, `#diffusers`, `#generative-ai`

</details>


<a id="item-12"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Waymo 宣布进军多伦多</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Waymo 宣布将其自动驾驶网约车服务扩展至加拿大多伦多，这是其进入的一个新国际市场。该消息在 Hacker News 上引发了 323 条评论的热烈讨论，用户们分享了褒贬不一的亲身乘坐体验，并就自动驾驶汽车的安全与监管问题展开辩论。 此次扩张是自动驾驶汽车领域的一个重要里程碑，表明 Waymo 有信心将其技术部署到现有美国市场之外的新监管环境中。这可能加速 Robotaxi 的全球推广，并促使其他城市制定明确的无人驾驶运营规则。 Waymo 是 Alphabet Inc.的子公司，使用其 Waymo Driver 系统，第六代 Ojai robotaxi 配备了 1700 万像素成像器和更新的传感器。多伦多上线将在新的气候和监管环境下测试该技术，不过公告中并未详细说明具体时间表和服务区域。

🔗 [来源](https://waymo.com/blog/2026/10/waymo-in-toronto/)

hackernews · ChrisArchitect · 10月16日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=50118981)

**背景**: Waymo 是一家总部位于加州山景城的美国自动驾驶技术公司，是 Google 母公司 Alphabet Inc.的子公司。它已在多个美国城市运营商业 Robotaxi 服务，并持续向包括国际市场在内的新市场扩张。自动驾驶汽车依赖详细的预制地图和传感器进行导航，但面临恶劣天气、狭窄街道和不同法规等挑战。此次进军多伦多延续了 Waymo 将其无人驾驶网约车服务扩展到最初美国测试地之外的更广泛战略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Waymo">Waymo - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Waymo_Ojai">Waymo Ojai - Wikipedia</a></li>
<li><a href="https://www.nhtsa.gov/vehicle-safety/automated-vehicle-safety">Automated Vehicle Safety - NHTSA</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论褒贬不一：一些用户分享了在旧金山和奥斯汀乘坐 Waymo 的正面体验，而另一些人则报告了问题，例如行程意外从 9 分钟延长到 45 分钟，以及丹佛一辆 Waymo 驶入农贸市场。一个主要担忧是缺乏对无人驾驶汽车提起刑事指控的法律，一位评论者认为城市在批准自动驾驶系统之前应制定严格且具有惩罚性的法规。

**标签**: `#autonomous-vehicles`, `#waymo`, `#self-driving`, `#transportation`, `#technology-expansion`

</details>


<a id="item-13"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Anthropic 的 Claude Code 团队详解每日 3 万次提交下的评估驱动代码审查</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Anthropic 的 Claude Code 团队发布博客文章，介绍了他们以评估（eval）驱动的自动化代码审查方法：大部分审查流程由自动化完成，人类注意力只集中在风险最高的地方。文章称该团队每天处理约 3 万次提交，并且对审查器本身的每一次改动都会用一套随事故不断扩充的评估集进行打分。 这是一次难得的机会，让外界看到一家领先 AI 实验室如何把 AI 应用于自身的软件工程流程，同时也提出了一个行业核心问题：在每天数万次提交的规模下，“审查”是否还有实际意义。如果这套方法行之有效，它可能成为 AI 密集型工程团队在大规模下管理代码质量与风险的范本。 该团队把“是否有人读过代码？”视为一个不精确的替代指标，真正要回答的问题是：这次改动可能出什么问题，以及哪种检查（自动或人工）最适合发现它。他们的评估集随每次事故而扩充，审查器的任何改动都要用全部累积的评估集打分，使审查器本身也持续接受回归测试。

🔗 [来源](https://claude.dev/blog/solving-code-review-at-anthropic/)

hackernews · pretext · 10月16日 19:04 · [社区讨论](https://news.ycombinator.com/item?id=50122951)

**背景**: 评估驱动开发（eval-driven development）是一种面向概率性系统（例如基于大模型的智能体）的工程方法：先明确正确性的规范，没有自动化证明满足该规范就不发布；一个评估通常由数据集、评分器和运行框架组成。Claude Code 是 Anthropic 的智能体编程工具，其 Code Review 功能会用多个智能体结合上下文代码阅读每个拉取请求，查找逻辑错误、安全漏洞和边界情况缺陷。随着 AI 生成代码日益普遍，其可靠性——语法正确性、功能准确性和健壮性——已成为研究和工程领域的重要议题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/resources/articles/code-review">Code Review for Claude Code | Claude by Anthropic</a></li>
<li><a href="https://evaldriven.org/">Eval-Driven Development</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者普遍持怀疑态度：有人质疑在每天 3 万次提交的规模下，还能否称得上真正意义上的审查；也有人分享亲身经历，称 Claude Code 会转述并偏离 API 文档，能通过自己写的冒烟测试却在真实 API 上失败。还有人质疑文章写作的真实性，认为读起来像 AI 生成的外部沟通稿；另有人批评文章忽视了开发者使用模型所需承担的成本视角。

**标签**: `#code-review`, `#AI-assisted-development`, `#Claude Code`, `#software-engineering-practices`, `#developer-tooling`

</details>


<a id="item-14"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">JPEG XL 与 AVIF：面向网页场景的实用图像格式对比</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Jake Archibald 发布了一篇针对网页使用场景的 JPEG XL 与 AVIF 详细对比文章，包含性能基准测试以及面向开发者的实用选型建议。 图像格式直接影响网页加载速度、带宽成本和视觉质量，因此这一对比能帮助开发者和网站运营者在浏览器支持不断演进的背景下，就采用哪种现代格式做出明智决策。 该对比涵盖了编码器性能的取舍：libjxl 的最高压缩档位对照片仅能缩小 2–7% 的文件体积，却需要 9–46 秒（比默认设置慢 50–180 倍）；而 AVIF 在线条图和截图上表现出色，但其无损压缩能力明显较弱。

🔗 [来源](https://jakearchibald.com/2026/jpeg-xl-vs-avif/)

hackernews · farlight · 10月16日 16:12 · [社区讨论](https://news.ycombinator.com/item?id=50120224)

**背景**: JPEG XL 是新一代图像格式，旨在以更好的压缩率和渐进式解码能力超越 PNG、JPEG 2000、GIF 和 WebP；而 AVIF 是基于 AV1 视频编解码器、封装在 HEIF 容器中的开放免版税格式。两者都试图取代传统的 JPEG 用于网页传输，但在编码速度、无损支持和硬件解码器兼容性上差异显著。开发者通常借助 HTML 的 picture 元素在两者间做选择，让浏览器自动挑选其支持的格式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jpegxl.info/">JPEG XL : Superior Image Compression</a></li>
<li><a href="https://en.wikipedia.org/wiki/AVIF">AVIF - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者就色度子采样的取舍展开讨论，指出 4:2:0 可能有助于兼容性，而 4:4:4 对某些编解码器反而会损害兼容性，且部分 AV1 硬件解码器可能仅支持 main profile。其他人则称赞 AVIF 在截图和线条图上的表现，讨论了 libjxl 因 Butteraugli 感知指标而导致高压缩档位编码缓慢的问题，并分享了用 ffmpeg 生成支持透明度的超小 AVIF 文件的实用参数。

**标签**: `#image-compression`, `#web-performance`, `#jpeg-xl`, `#avif`, `#codecs`

</details>


<a id="item-15"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">苹果 MLX 实现 Mac Studio 集群分布式大模型推理</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

苹果机器学习研究团队发布了一项关于 MLX 分布式推理的新研究，允许将大型开放权重语言模型拆分到多台 Apple Silicon Mac（如 Mac Studio）上联合推理。该发布附带了 Mac Studio 硬件上的 token 吞吐量基准测试，社区讨论则对基准测试的公平性和实际实用性提出了质疑。 这很重要，因为它提供了一种在苹果硬件上本地运行超大型开放权重模型的方式，而无需依赖云端 GPU，可能吸引注重隐私的用户、研究人员和小型团队。这也加强了苹果在本地 AI 推理生态中的地位，该领域已有 MLX、LM Studio 和 llama.cpp 等工具竞争。 MLX 支持分布式通信操作，可将训练或推理的计算成本分摊到多台物理机器上，苹果的研究页面专门在 Mac Studio 集群上演示了这一点。社区成员指出，标题中的吞吐量数据（约 15–36 token/秒）是在 8,192 token 上下文下测得的，有人认为这对现代用例来说太短，并且基准测试将 Meta 的模型以 4-bit 量化与仅以原生 BF16 运行的 Qwen 进行了对比。

🔗 [来源](https://machinelearning.apple.com/research/mlx-distributed-inference)

hackernews · antipaul · 10月16日 13:43 · [社区讨论](https://news.ycombinator.com/item?id=50118320)

**背景**: MLX 是苹果为 Apple Silicon 打造的开源机器学习数组框架，其分布式通信功能允许多台 Mac 汇集内存和算力，以运行单机无法容纳的大模型。开放权重模型是指训练参数公开的 AI 模型，任何人都可以下载并在本地运行，但许可条款各不相同。Mac Studio 是苹果的高内存桌面工作站，通常配置 256GB 或更多统一内存，因此成为本地大模型推理的热门选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍持怀疑态度：有人指出讽刺之处——Meta 花费数十亿美元构建开放权重模型，而用户却要付给苹果 2 万美元来运行它们；另一位则指责苹果通过将 Meta 模型以 4-bit 与 BF16 的 Qwen 对比来“放水”Qwen。其他人分享了实际测试结果，例如单台 256GiB 的 M5 Ultra 运行 DeepSeek 4.1 Flash 可达约 3200 token/秒预填充和约 45 token/秒，并批评标题图表使用的 8,192 token 上下文太短、不够实用。

**标签**: `#Apple`, `#MLX`, `#distributed inference`, `#local LLM`, `#benchmarking`

</details>


<a id="item-16"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Home Assistant 密码泄露检查未经同意发送哈希前缀</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

home-assistant.io 仓库的一个 GitHub issue 显示，Home Assistant 的 Supervisor 安全检查会在未经用户明确同意的情况下，将 SHA-1 哈希密码的前五个字符发送到 Have I Been Pwned (HIBP) API。开发者 Frenck 承认最初的回复过于轻率，并澄清可以通过命令 `ha security options --pwned=false` 禁用该功能。 这一事件凸显了开源项目中日益增长的隐私担忧，安全功能可能在未经同意的情况下无意中将用户数据分享给第三方。它影响了 Home Assistant 的大量用户，并可能削弱用户对平台处理敏感信息的信任。 该检查使用 k-匿名技术，仅发送 SHA-1 哈希的前五个字符，这是 HIBP 用于在不泄露完整哈希的情况下检查密码的标准方法。该功能已在 Supervisor 中存在多年，但最近的一个版本修复了显示该功能的警告，使得用户现在才注意到它。

🔗 [来源](https://github.com/home-assistant/home-assistant.io/issues/49314)

hackernews · trvrprkr · 10月16日 20:33 · [社区讨论](https://news.ycombinator.com/item?id=50124251)

**背景**: Have I Been Pwned (HIBP) 是一项允许用户检查其密码是否在数据泄露中被泄露的服务。它使用 k-匿名技术保护隐私：客户端用 SHA-1 对密码进行哈希，仅将哈希的前五个字符发送到 API，API 返回匹配的哈希后缀列表以供比较。Home Assistant 是一个流行的开源家庭自动化平台，运行在名为 Supervisor 的设备上，负责管理附加组件和系统设置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://haveibeenpwned.com/Passwords">Have I Been Pwned : Pwned Passwords</a></li>

</ul>
</details>

**社区讨论**: 社区成员表达了强烈的隐私担忧，认为任何数据共享，即使是哈希后的数据，都应需要用户选择加入。一些人质疑发送五个哈希字符是否构成真正的安全风险，而另一些人则批评开发者的轻率语气，并提及过去的有毒行为。开发者已道歉并澄清该功能可以禁用。

**标签**: `#privacy`, `#security`, `#home-assistant`, `#open-source`, `#data-sharing`

</details>


<a id="item-17"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">OpenAI 推出面向生命科学实验室的 Rosalind 学术计划</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

OpenAI 推出了 Rosalind 学术计划，为符合条件的学术实验室提供对 GPT-Rosalind 的赞助访问权限，这是其专为生命科学研究打造的前沿推理模型。据报道，符合条件的美国学术实验室可获得最多 30 个免费 Business Standard 席位，为期 12 个月，并附带 GPT-Rosalind 的使用权限。 此举降低了学术实验室使用先进 AI 进行生命科学研究的成本门槛，有望加速药物发现、基因组分析和蛋白质研究。这也表明 OpenAI 正推动将其专用模型嵌入科研工作流，并让更多资源有限的学术机构也能获得先进工具。 GPT-Rosalind 被描述为 OpenAI 在生命科学领域能力最强的模型，专为深度科学推理、更强的工具与数据库调用，以及跨蛋白质理解、基因组分析和生物化学推理的安全多步骤工作流而设计。该学术计划专门面向符合条件的学术机构，据报道美国实验室可获得最多 30 个免费 Business Standard 席位，为期 12 个月。

🔗 [来源](https://openai.com/index/introducing-the-rosalind-academic-plan)

rss · OpenAI Blog · 10月15日 19:00

**背景**: GPT-Rosalind 是 OpenAI 于 2026 年 4 月推出的前沿推理模型，专为生命科学研究打造，旨在加速药物发现、基因组分析和蛋白质推理。与通用模型不同，它针对科学数据分析、证据综合和复杂生物学问题探究进行了优化。Rosalind 学术计划将这一专用能力扩展到可能缺乏企业级 AI 工具预算的学术研究人员。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-rosalind/">Introducing GPT-Rosalind for life sciences research | OpenAI</a></li>
<li><a href="https://help.openai.com/en/articles/20001193-gpt-rosalind-for-life-sciences-research">GPT-Rosalind for life sciences research - OpenAI Help Center</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-Rosalind`, `#academic research`, `#life sciences`, `#AI for science`

</details>


<a id="item-18"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">澳大利亚拟立法允许用户关闭社交媒体推荐算法</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

澳大利亚提出了一项新法律草案，要求社交媒体平台必须为用户提供关闭推荐内容算法的开关。该草案建立在澳大利亚此前于 2025 年 12 月推出的 16 岁以下社交媒体禁令基础上，是该国激进平台监管议程的又一举措。 如果通过，该法律可能为算法透明度和用户控制设定全球先例，迫使 Facebook、TikTok 和 YouTube 等主要平台重新设计其核心信息流系统。这标志着一种转变，即把推荐算法视为用户有权选择退出的对象，可能对欧盟、英国和美国的科技政策产生连锁影响。 该提案专门针对“推荐内容”信息流，意味着用户可以切换到按时间顺序或非算法视图。目前仍为法律草案，因此关于执法、处罚以及覆盖哪些平台的细节仍在制定中。

🔗 [来源](https://www.bbc.co.uk/news/articles/cwr7y8er1n8vo?at_medium=RSS&at_campaign=rss)

rss · BBC World · 10月16日 18:11

**背景**: 社交媒体平台使用复杂的推荐算法来决定每个用户看到什么内容，并针对点击、点赞和观看时长等参与度信号进行优化。这些系统因放大有毒或极化内容、制造过滤气泡而受到批评。澳大利亚一直处于监管大型科技公司的前沿，此前曾通过法律要求平台为新闻内容付费，并禁止 16 岁以下儿童使用社交媒体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.exchange4media.com/digital-news/australia-unveils-draft-law-to-let-users-switch-off-social-media-algorithms-158044.html">Australia unveils draft law to let users switch off social media ...</a></li>
<li><a href="https://knightcolumbia.org/content/understanding-social-media-recommendation-algorithms">Understanding Social Media Recommendation Algorithms Social Media Recommendation Algorithms Technology Primer: Social Media Recommendation Algorithms Understanding Social Media Recommendation Algorithms Social Media Algorithms: Content Recommendation, Moderation ... How Recommendation Algorithms Shape What You Watch and Share ...</a></li>

</ul>
</details>

**标签**: `#social media`, `#regulation`, `#algorithms`, `#user control`, `#Australia`

</details>


<a id="item-19"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">以色列间谍软件以“AdFection”零点击攻击半岛电视台员工</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

由半岛电视台内部调查引发的 Citizen Lab 调查证实，以色列公司 Candiru 的间谍软件在 2024 至 2025 年间被植入至少 45 台半岛电视台设备，使用了一种研究人员命名为“AdFection”的新型零点击方法——恶意代码通过定向在线广告投放，而非用户任何操作。 这被认为是首例经证实的通过定向广告传播零点击间谍软件的案例，表明商业广告技术基础设施可被改用于与国家相关的监控活动，记者仅仅浏览一条广告就可能使手机被入侵。 Citizen Lab 与安全公司 Confiant 将此次攻击追溯到以色列广告技术公司 Discover-Tech 以及特拉维夫间谍软件厂商 Candiru（又名 Integrity Labs），后者已于 2021 年被美国政府列入黑名单；报告称 Discover-Tech 的用户画像能力使至少 45 台半岛电视台设备成为攻击目标。

🔗 [来源](https://www.aljazeera.com/video/newsfeed/2026/10/16/how-israeli-spyware-used-zero-click-hack-on-al-jazeera-staff?traffic_source=rss)

rss · Al Jazeera · 10月16日 21:08

**背景**: 零点击攻击无需受害者任何操作即可感染设备——无需点击钓鱼链接，也无需登录虚假页面——通常利用移动操作系统的漏洞实现。NSO 集团的 Pegasus 和 Candiru 等雇佣间谍软件多次被指用于监控记者、人权活动人士和政治异见者。AdFection 之所以引人注目，是因为它把遍布无数应用和网站的在线广告生态系统当作投递渠道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aljazeera.com/news/2026/10/15/israeli-ad-tech-firm-helped-spy-on-al-jazeera-devices">Israeli ad-tech firm helped place spyware on Al Jazeera ... | Al Jazeera</a></li>
<li><a href="https://cpj.org/2026/10/report-israeli-ad-tech-firm-enables-spyware-targeting-of-at-least-45-al-jazeera-devices/">Report: Israeli ad-tech firm enables spyware targeting of at least 45...</a></li>

</ul>
</details>

**标签**: `#spyware`, `#zero-click exploit`, `#mobile security`, `#surveillance`, `#privacy`

</details>


</section>