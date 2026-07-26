---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> 从 102 条内容中筛选出 9 条重要资讯。

---

<section class="cat cat-tech" markdown="1">

## 🔬 科技 / AI (9)

<a id="item-1"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">vLLM v0.26.0：支持 Inkling 模型，优化 DeepSeek-V4</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

vLLM v0.26.0 引入了对 Inkling 模型系列的支持、DeepSeek-V4 的性能优化、fp32 lm_head 支持以及灵活的注意力后端。该版本包含来自 212 位贡献者的 411 次提交。 此版本显著提升了 LLM 推理效率并扩展了模型支持，有利于大规模 AI 部署。对 DeepSeek-V4 的优化和新 Inkling 系列的引入，使 vLLM 能够支持前沿模型。 关键特性包括 DeepSeek-V4 专用路由内核（端到端 TPOT 提升 2.94%）、通过 head_dtype 实现的 fp32 lm_head、按 KV 缓存组选择注意力后端，以及带分层存储的 KV 卸载。Rust 前端现在支持多模态视频和音频。

🔗 [来源](https://github.com/vllm-project/vllm/releases/tag/v0.26.0)

github · khluu · 7月25日 10:38

**背景**: vLLM 是一个高吞吐、内存高效的 LLM 推理引擎，广泛用于生产环境。Inkling 模型是 Thinking Machines Lab 推出的 Mamba 混合、256 专家混合专家多模态推理模型。DeepSeek-V4 是一个大型语言模型，需要优化的内核以实现高效服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-07-22-kimi-k3-preview">A Preview of Production-Scale Kimi K3 Support on vLLM | vLLM Blog</a></li>
<li><a href="https://build.nvidia.com/thinkingmachines/inkling/modelcard">inkling Model by Thinkingmachines | NVIDIA NIM</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling : Our Open-Weights Model - Thinking Machines Lab</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek`, `#CUDA`, `#AI/ML`

</details>


<a id="item-2"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">中继市场助长 AI 代币转售与欺诈</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

一个繁荣的中继市场被揭露，转售商通过汇集被盗的 API 密钥并利用计费系统漏洞，提供折扣 AI 推理服务，助长欺诈并可能操纵模型。 这破坏了 AI 提供商的收入和安全，使恶意行为者能够廉价访问前沿模型进行滥用、模型蒸馏或影响力活动，威胁 AI 服务的完整性。 该市场分层运作：上游池聚合 API 密钥，下游中继将 API 包装成用户友好产品，最终用户包括寻求廉价推理的中国开发者和初创公司。

🔗 [来源](https://vectoral.com/blog/token-relay-market)

hackernews · mlenhard · 7月26日 15:17 · [社区讨论](https://news.ycombinator.com/item?id=49058993)

**背景**: AI 推理计算成本高昂，通常按 token 计费。转售商利用免费额度、被盗凭证和计费漏洞，以官方价格的一小部分提供 token，形成了一个利润丰厚的套利市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vectoral.com/blog/token-relay-market">An Inside Look at the Relay Market Powering Token Resellers and Fraud | Vectoral</a></li>
<li><a href="https://simonwillison.net/2026/Jul/26/relay-market/">An Inside Look at the Relay Market Powering Token Resellers and...</a></li>
<li><a href="https://www.sourcery.ai/security/categories/inference_abuse">Inference Abuse & Resource Exhaustion | Security Categories</a></li>

</ul>
</details>

**社区讨论**: 评论者指出这并非新鲜事，将其比作广告欺诈和票贩。担忧包括无法检测合并账户从而影响模型，以及滥用免费云额度带来不公平竞争优势。

**标签**: `#AI security`, `#fraud`, `#token reselling`, `#inference abuse`, `#cybersecurity`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">欧盟提议浏览器级隐私设置以消灭 Cookie 横幅</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

欧盟委员会提出一项法规，要求网页浏览器提供内置隐私偏好设置，让用户一次性设定同意选项，从此不再看到 Cookie 横幅。 这可能消除无处不在且常常误导用户的 Cookie 横幅，将同意管理从网站转移到浏览器层面，从而改善用户体验，但也引发了对知情同意的担忧。 该提案是 ePrivacy 法规改革的一部分，包括机器可读同意信号的标准。加利福尼亚州的类似立法将于 2027 年 1 月生效，要求浏览器提供隐私控制。

🔗 [来源](https://killthecookiebanner.eu/)

hackernews · rapnie · 7月26日 11:53 · [社区讨论](https://news.ycombinator.com/item?id=49057175)

**背景**: Cookie 横幅是根据欧盟 ePrivacy 指令引入的，用于获取用户对跟踪 Cookie 的同意。然而，它们因侵入性、令人困惑且常被设计成诱导用户接受跟踪而受到批评。提议的浏览器级设置旨在简化同意流程，同时保持用户控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/EPrivacy_Regulation">ePrivacy Regulation - Wikipedia</a></li>
<li><a href="https://www.truevault.com/learn/gdpr-2-0-eu-proposes-overhaul-of-data-privacy-laws">TrueVault | GDPR 2.0? EU Proposes Overhaul of Data Privacy Laws</a></li>
<li><a href="https://datainnovation.org/2025/12/europes-eprivacy-reforms-come-too-late-and-go-too-small/">Europe’s ePrivacy Reforms Are Too Late—and Too Small</a></li>

</ul>
</details>

**社区讨论**: 评论者大多欢迎这一举措，但就自动化同意是否会削弱知情同意展开辩论。一些人认为点击按钮不能构成知情同意，而另一些人则指出并非所有网站都值得相同的偏好设置，并希望有逐站自定义功能。

**标签**: `#privacy`, `#cookie banners`, `#EU regulation`, `#web standards`, `#browser`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Ruff v0.16.0 将默认 lint 规则从 59 条扩展到 413 条</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Ruff v0.16.0 于 2026 年 7 月 23 日发布，将默认 lint 规则从 59 条增加到 413 条，无需任何配置即可捕获更多语法错误和运行时问题。 这一大幅扩展意味着 Python 开发者将自动发现项目中更多的错误和代码质量问题，虽然可能导致 CI 流水线中断，但最终会带来更健壮的代码。 自 v0.1.0 以来，Ruff 的规则总数已从 708 条增加到 968 条；新的默认规则包括针对语法错误、即时运行时错误以及其他以前需要手动启用的严重问题的规则。

🔗 [来源](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything)

rss · Simon Willison · 7月25日 22:44

**背景**: Ruff 是一个用 Rust 编写的快速 Python linter 和代码格式化工具，旨在替代 Flake8、isort 和 Black 等工具。它将来自数十个现有工具的 900 多条 lint 规则整合到一个二进制文件中，运行速度比替代工具快 10-100 倍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and code formatter, written in Rust. · GitHub</a></li>
<li><a href="https://realpython.com/ruff-python/">Ruff: A Modern Python Linter for Error-Free and Maintainable Code – Real Python</a></li>
<li><a href="https://pydevtools.com/blog/ruff-0-16-0-default-rules/">Ruff 0 . 16 . 0 Enables 7x More Rules by Default | pydevtools</a></li>

</ul>
</details>

**标签**: `#Python`, `#linting`, `#Ruff`, `#tooling`, `#release`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Anthropic 的 Opus 5 展现出强大的提示注入抵抗力</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Anthropic 的 Claude Opus 5 模型在抵抗提示注入攻击方面表现出显著改进，这一点由 Boris Cherny 强调并在系统卡中详细说明。这使其成为 Anthropic 迄今为止最不易受提示注入影响的模型。 提示注入是大语言模型的一个关键安全漏洞，改进的抵抗力直接增强了 AI 部署的安全性和可靠性。这一进展可能为模型安全性设定新标准，并鼓励在敏感应用中更广泛地采用 LLM。 这一说法得到了评估和红队测试结果的支持，尽管具体指标在系统卡中有些隐蔽。Opus 5 还展现出改进的通用能力，包括更好的漏洞发现能力，但 Anthropic 有意避免对其在网络利用任务上进行训练。

🔗 [来源](https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything)

rss · Simon Willison · 7月25日 00:42

**背景**: 提示注入是一种网络安全利用手段，恶意输入会覆盖模型的指令，导致意外行为。这对于 LLM 来说是一个主要问题，尤其是那些具有网页浏览或文件上传能力的模型。系统卡是 AI 公司发布的详细文档，描述模型的能力、限制和安全测试结果。红队测试涉及模拟对抗性攻击，以在部署前发现漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://en.wikipedia.org/wiki/Red_teaming">Red teaming</a></li>
<li><a href="https://www.linkedin.com/pulse/ai-system-cards-luis-adolfo-villalobos-hllme">AI System Cards</a></li>

</ul>
</details>

**标签**: `#prompt-injection`, `#anthropic`, `#claude`, `#generative-ai`, `#ai-safety`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Decker 以 1 位图形复兴 HyperCard 到现代平台</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Decker 是一个现代平台，它重现了 HyperCard 的体验，采用 1 位图形，并受经典 macOS 启发，提供了自包含的应用开发环境。 Decker 复兴了 HyperCard 那种易用、友好的范式，它曾让非程序员也能创建交互式应用，有望在复古计算的背景下激发创造力和教育价值。 Decker 使用 1 位图形（黑白），可在现代系统上运行，提供类似 HyperCard 的基于堆栈的隐喻。它专为自包含应用设计，这些应用可以作为单个文件共享。

🔗 [来源](https://beyondloom.com/decker/)

hackernews · tosh · 7月26日 18:23 · [社区讨论](https://news.ycombinator.com/item?id=49060856)

**背景**: HyperCard 由苹果公司于 1987 年发布，是一款开创性的超媒体工具，它将数据库与名为 HyperTalk 的可视化编程语言相结合。用户可以创建包含交互内容的卡片“堆栈”，广泛应用于教育、原型设计和小型企业应用。Decker 旨在为现代用户重新捕捉那种简洁与强大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/HyperCard">HyperCard</a></li>
<li><a href="https://en.wikipedia.org/wiki/Binary_image">Binary image - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对 HyperCard 的怀旧之情，一位用户回忆起在 6-7 岁时用它创建个人词典的经历。其他人则讨论这类界面在今天是否还有用武之地，指出 FileMaker 和 LiveCode 等类似工具已经演变或停止开发。有人提到了 2022 年和 2024 年 Hacker News 上的先前讨论。

**标签**: `#HyperCard`, `#retrocomputing`, `#visual programming`, `#creative tools`, `#platform`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">AI 编码抽象可能削弱开发者专业能力</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

David Nicholas Williams 认为，依赖 AI 抽象化编码细节会阻碍开发者建立真正的理解和能力，引发了关于生产力与技能发展之间权衡的讨论。 随着 AI 辅助编码工具的普及，这一讨论凸显了一个关键矛盾：AI 在提高生产力的同时，也可能导致技能退化，尤其是对跳过基础学习的新手开发者。 文章提到了“vibecoding”——开发者在不完全理解的情况下接受 AI 生成代码的做法——并指出即使是经验丰富的开发者也难以引导日益独立的模型，导致输出草率且知识共享不佳。

🔗 [来源](https://davidnicholaswilliams.com/its-not-empowering-to-hand-off-the-details/)

hackernews · davnicwil · 7月26日 17:58 · [社区讨论](https://news.ycombinator.com/item?id=49060592)

**背景**: Vibecoding 是一种软件开发方式，开发者用自然语言描述项目，AI 生成代码，而开发者往往不深入理解输出。这种方法以理解深度换取速度，引发了对长期技能发展的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding - Wikipedia</a></li>
<li><a href="https://larsfaye.com/articles/ai-coding-will-prevent-expertise">AI Coding will Prevent Expertise | Lars Faye</a></li>
<li><a href="https://dev.to/ilyatech/ai-assisted-learning-gaps-addressing-foundational-programming-skills-for-independent-3of5">AI - Assisted Learning Gaps: Addressing... - DEV Community</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：有人将 AI 捷径比作健身者跳过艰苦训练，警告会浪费潜力；另一些人认为，凭借良好的判断力，可以略过细节而专注于高层设计；一位制作世嘉 Genesis 游戏爱好者则认为 AI 解放了自己，能专注于创意方面。

**标签**: `#AI-assisted coding`, `#software engineering`, `#developer experience`, `#vibecoding`, `#skill development`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">AI 将开发者焦点从构建转向完成</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

一篇文章探讨了 AI 工具如何将开发者的焦点从构建软件转向完成软件，引发了社区关于减少依赖与增加碎片化之间权衡的讨论。 这一转变可能从根本上改变软件开发工作流程，可能提高生产力，但也可能导致大量不兼容的初级项目泛滥。 社区评论强调，AI 使开发者能够探索副业项目并修复配置问题，但也导致了大量 99%完成的项目积压，以及一个重复且不兼容软件的“又一个”时代。

🔗 [来源](https://www.rickmanelius.com/p/the-new-ai-superpowers-focus-and)

hackernews · mooreds · 7月26日 13:13 · [社区讨论](https://news.ycombinator.com/item?id=49057877)

**背景**: 像 GitHub Copilot 和 ChatGPT 这样的 AI 编码助手已变得流行，用于快速生成代码。然而，完成一个项目不仅仅是编写代码，还需要测试、调试和集成，AI 可能无法完全解决这些问题。

**社区讨论**: 评论者报告了不同的体验：一些人使用 AI 来减少认知负荷并避免倦怠，而另一些人则担心近完成项目堆积如山。大家一致认为 AI 有助于前 99%，但对最后 1%帮助不大。

**标签**: `#AI`, `#software engineering`, `#productivity`, `#developer tools`, `#workflow`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">GrapheneOS 自动重启阻止锁定设备数据提取</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

GrapheneOS 具有自动重启功能，可在可配置的非活动期（默认 18 小时）后将设备恢复到首次解锁前（BFU）模式，从而阻止从锁定设备中提取数据。 这种保护对于记者、活动人士以及任何面临边境搜查或设备扣押的人来说至关重要，因为它确保即使设备被物理获取，加密数据仍然无法访问。 自动重启计时器可由用户在 10 分钟到 72 小时之间调整，该功能与 GrapheneOS 的其他安全措施（如胁迫 PIN/密码和双因素指纹解锁）配合使用。

🔗 [来源](https://discuss.grapheneos.org/d/40700-grapheneos-protections-against-data-extraction-from-locked-devices)

hackernews · Cider9986 · 7月26日 05:57 · [社区讨论](https://news.ycombinator.com/item?id=49055169)

**背景**: 首次解锁前（BFU）模式是 Android 上的一种加密状态，此时设备基于文件的加密密钥尚未加载到内存中，使得数据提取极其困难。首次解锁后（AFU），密钥可用，数据更容易被访问。GrapheneOS 的自动重启功能在非活动期后将设备强制恢复到 BFU 模式，从而缩短了取证攻击的时间窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grapheneos.org/features">Features overview | GrapheneOS</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/grapheneos-frequent-android-auto-reboots-block-firmware-exploits/">GrapheneOS : Frequent Android auto - reboots block firmware exploits</a></li>
<li><a href="https://cyberpress.org/android-security-feature/">New Android Security Feature Automatically Restarts Device After...</a></li>

</ul>
</details>

**社区讨论**: 社区成员称赞自动重启功能，但指出缺乏完整的备份/恢复解决方案来在过境前擦除设备。一些人讨论了密码熵，图案锁仅提供约 18.57 位熵，而长密码则更安全。

**标签**: `#GrapheneOS`, `#mobile security`, `#data extraction`, `#privacy`, `#Android`

</details>


</section>