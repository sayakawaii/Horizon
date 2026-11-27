---
layout: default
title: "Horizon Summary: 2026-11-27 (ZH)"
date: 2026-11-27
lang: zh
---

> 从 115 条内容中筛选出 12 条重要资讯。

---

<section class="cat cat-science" markdown="1">

## 🧪 科学 (1)

<a id="item-1"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">预印本提出基于零锥的引力代数量子化方案</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

一篇新的 arXiv 预印本（2611.34924）提出在四维洛伦兹时空上对真空广义相对论进行背景无关的量子化：通过在相交零锥上求解引力约束，并在有限牛顿常数下将约化相空间的泊松括号提升为对易关系。 如果正确，这一方法可能为背景无关的量子引力理论提供一条具体途径，给出有限的跃迁振幅和离散的面积谱，并可能与黑洞熵计算相联系；然而该工作仍是未经同行评审的预印本，其重要性尚未确立。 该论文通过约化作用的形变构造可观测量代数，使用高斯波函数，并声称面积具有离散谱且跃迁振幅有限；社区评论者就代数类型（I 型与 II 型）以及洛伦兹路径积分的严格性提出了技术性质疑。

🔗 [来源](https://arxiv.org/abs/2611.34924)

hackernews · hecmmm · 11月26日 05:37 · [社区讨论](https://news.ycombinator.com/item?id=50651863)

**背景**: 量子引力旨在统一广义相对论与量子力学。一个关键难题是背景无关性：标准量子场论假设固定的时空背景，而引力应在没有背景的情况下量子化。零（光）锥是光在时空中传播的路径，基于零曲面的广义相对论表述将光锥结构而非度规视为基本变量。代数量子化则构造一个量子代数，使其经典极限还原给定的泊松代数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2611.34924v1">An algebraic quantization of gravity from the null cone</a></li>
<li><a href="https://en.wikipedia.org/wiki/Light_cone">Light cone - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quantum_gravity">Quantum gravity - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 讨论（215 分，76 条评论）在技术上有一定深度，但 largely 偏离主题：r/physics 版主指出大部分争论集中在 AI 而非量子引力上，并呼吁等待同行评审。kdavis 等评论者质疑 I 型代数结果和洛伦兹路径积分的严格性，还有人询问该论文是否提出任何新的可检验预言。

**标签**: `#quantum-gravity`, `#theoretical-physics`, `#arxiv`, `#algebraic-quantization`, `#research`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 科技 / AI (11)

<a id="item-2"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Aaronson 博客文章引发 AI 因式分解与矩阵乘法突破的传闻</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Scott Aaronson 于 2026 年 11 月 24 日发表了一篇博客文章，以极度兴奋的语气回应了有关 OpenAI、Anthropic 或两者可能发现了多项式时间大整数因式分解算法的传闻，该算法将破解 RSA 加密。文章还引用了一篇题为《矩阵乘法指数是九分之四》的预印本，该预印本建立了匹配的上界和下界，证明矩阵乘法指数 ω 等于 2.25。 如果存在多项式时间因式分解算法，它将破坏 RSA 和大部分现代公钥密码学，迫使全球向后量子方案迁移。另外，将 ω 确定为 2.25 将是计算复杂性领域的里程碑式成果，弥合了平凡下界 2 与已知最佳算法之间长达数十年的差距。 因式分解的说法仍未得到验证，基于 Aaronson 表示他多次听到的传闻；OpenAI 或 Anthropic 均未公开任何论文或算法。矩阵乘法成果于 11 月 24 日作为预印本发布，声称对任意域上的方阵乘法给出了匹配的上界和下界，但社区尚未确认该证明。

🔗 [来源](https://scottaaronson.blog/?p=10379)

hackernews · Kotlopou · 11月25日 19:11 · [社区讨论](https://news.ycombinator.com/item?id=50646108)

**背景**: RSA 加密依赖于分解两个大素数乘积在计算上不可行这一假设；快速的经典因式分解算法将破解它，而运行 Shor 算法的量子计算机已知会对其构成威胁。矩阵乘法指数 ω 是使得 n×n 矩阵可在 O(n^ω) 次操作内相乘的最小数字；几十年来它已从 3 被推向 2，而新声称的恰好 2.25 将是一个重大进展。Scott Aaronson 是德克萨斯大学奥斯汀分校著名的量子计算与复杂性理论家，其博客经常放大新兴成果和传闻。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://forklog.com/en/former-openai-employee-hints-at-ai-labs-breakthrough-in-rsa-encryption-vulnerability/">Former OpenAI Employee Hints at AI Labs’ Breakthrough in RSA ...</a></li>
<li><a href="https://interestingengineering.com/culture/openai-exact-2-25-matrix-multiplication-exponent">OpenAI establishes exact 2.25 exponent for matrix multiplication</a></li>
<li><a href="https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm">Matrix multiplication algorithm - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：一些人认为 AI 实验室规模太大，无法保守密码学突破的秘密，且没有确凿证据；另一些人则警告人类在心理上无法理解此类变化的严重程度。另一个讨论串探讨了 Lean 和 MathLib 等工具而非 LLM 是否应因加速数学进步而获得赞誉。

**标签**: `#AI`, `#cryptography`, `#matrix multiplication`, `#scientific progress`, `#Hacker News`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">AI 编码代理让自托管重获乐趣，但引发安全担忧</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

一位博主发表了一篇个人随笔，认为 AI 编码代理通过自动化繁琐的设置和部署任务，使自托管变得更加愉快和顺畅。该文章在 Hacker News 上引发了 333 分、180 条评论的讨论，辩论其中的利弊。 这反映了开发者处理基础设施方式的更广泛转变：AI 代理降低了部署和维护自托管服务的门槛，可能使 DevOps 对爱好者和小型团队更加民主化。然而，正如评论者指出的，这也将负担从手动设置转移到持续的安全警惕上。 评论者强调，虽然 AI 代理可以处理端到端部署（例如启动 VPS 和配置 Cloudflare 代理），但用户需要负责在关键 CVE 发布后 24 小时内打补丁，这种节奏有些人认为不可持续。其他人提到使用 AI 自动化重复性编码任务，甚至构建平台让代理部署到 Tailscale 后面的家庭服务器中。

🔗 [来源](https://janlukas.blog/posts/ai-self-hosting)

hackernews · jlelse · 11月26日 21:47 · [社区讨论](https://news.ycombinator.com/item?id=50660180)

**背景**: 自托管是指在自己的服务器（如 VPS 或家庭服务器）上运行服务，而不是使用托管平台。AI 编码代理是利用大型语言模型协助软件开发任务（从编写代码到部署）的工具。DevOps 是一组结合软件开发和 IT 运维的实践，旨在缩短开发生命周期并提供持续交付。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_coding_agent">AI coding agent</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-hosting_(network)">Self-hosting (network) - Wikipedia</a></li>
<li><a href="https://roadmap.sh/devops">DevOps Roadmap: Learn to become a DevOps Engineer or SRE</a></li>

</ul>
</details>

**社区讨论**: 讨论意见不一：一些评论者赞扬“凭感觉”部署和自动化繁琐工作的便利，而另一些人则警告安全负担增加，并需要质疑一个想法是否值得实施。一个共同的主题是，AI 使构建变得容易，但用户仍必须对维护和安全负责。

**标签**: `#self-hosting`, `#AI agents`, `#DevOps`, `#security`, `#automation`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">AMD 专用 llama.cpp 分支引发关于本地 LLM 推理优化的讨论</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

一个针对 AMD GPU 的 llama.cpp 分支被创建，旨在优化在廉价高带宽 AMD GPU（尤其是 gfx906 系列）上的本地 LLM 推理，并在 Hacker News 上引发了关于重新利用旧数据中心显卡的讨论。 这很重要，因为它使得在廉价硬件上本地运行大型语言模型成为可能，有望降低 LLM 推理的门槛并减少对昂贵现代 GPU 的依赖。 gfx906 系列（如 Radeon VII 和 MI50）以约 200 美元的价格提供高达 32GB 的显存和 1 TB/s 的内存带宽，但缺少张量核心和原生 bf16 支持，因此需要在该分支中进行自定义优化。

🔗 [来源](https://devnull.land/amd-specific-llama-cpp)

hackernews · julianlam · 11月26日 17:11 · [社区讨论](https://news.ycombinator.com/item?id=50657265)

**背景**: llama.cpp 是一个流行的开源库，用于在消费级硬件上高效地进行 LLM 推理。gfx906 架构是 AMD 约 2018 年推出的较旧 GPU 世代，最初为数据中心设计，因其相对于成本的高内存带宽而受到爱好者欢迎。ROCm 是 AMD 用于 GPU 计算的开源软件栈，类似于 NVIDIA 的 CUDA。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/janit/llama.cpp-gfx906">GitHub - janit/ llama . cpp - gfx 906 : llama . cpp fork targeting AMD ...</a></li>
<li><a href="https://github.com/thickprogrammer/llama.cpp-gfx906">thickprogrammer/ llama . cpp - gfx 906 : llama . cpp optimized for AMD ...</a></li>
<li><a href="https://forum.level1techs.com/t/glm-and-i-created-a-llama-cpp-fork-optimized-for-amd-gfx906-mi50-mi60-radeon-vii-gcn-hip/254257">GLM and I created a llama . cpp fork optimized for AMD GFX 906 ...</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了 gfx906 显卡以低成本提供高内存带宽的价值，分享了包括自定义分支和内核移植在内的个人优化工作，并讨论了 Radiance 和 Splash 等能显著提升速度的替代推理引擎。

**标签**: `#llama.cpp`, `#AMD`, `#local-llm-inference`, `#GPU-optimization`, `#hardware`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">RansomwareHelp 首席技术官因秘密支付赎金被控电信欺诈</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

RansomwareHelp.com 的首席技术官兼联合创始人被控电信欺诈。这家佛罗里达公司声称使用“高级加密工具”恢复被勒索软件锁定的数据，但 FBI 的钓鱼执法发现该公司秘密向攻击者支付赎金，同时却告诉客户它从不这样做。 此案凸显了勒索软件恢复行业中的法律和道德灰色地带，公司可能在支付赎金问题上欺骗客户，并可能为这类服务的监管和起诉树立先例。 检察官指控该首席技术官向勒索软件团伙支付赎金，然后向受害者收取远高于此的费用；FBI 的钓鱼执法涉及一个假的勒索软件团伙和受害者；起诉书的核心是该公司在“不支付赎金”政策上存在重大欺骗，构成电信欺诈。

🔗 [来源](https://krebsonsecurity.com/2026/11/cto-of-ransomwarehelp-indicted-for-wire-fraud/)

hackernews · Bender · 11月26日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=50657645)

**背景**: 勒索软件是一种恶意软件，它加密受害者的数据并要求支付赎金以获取解密密钥。恢复公司帮助受害者恢复数据，但有些公司可能秘密支付赎金，尽管声称不会这样做，这引发了围绕欺诈和制裁的法律问题。电信欺诈涉及利用电子通信实施诈骗计划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://krebsonsecurity.com/2026/11/cto-of-ransomwarehelp-indicted-for-wire-fraud/">CTO of ‘RansomwareHelp’ Indicted for Wire Fraud – Krebs on ...</a></li>
<li><a href="https://securityelites.com/news/ransomwarehelp-cto-indicted-wire-fraud-fbi-sting/">RansomwareHelp CTO Indicted For Wire Fraud - securityelites.com</a></li>

</ul>
</details>

**社区讨论**: 评论者争论该行为是否构成电信欺诈，一些人质疑欺诈意图，因为客户最终拿回了数据，而另一些人指出营销中存在重大欺骗。还有人建议可以通过在合同中披露支付赎金的可能性来避免欺诈。

**标签**: `#cybersecurity`, `#ransomware`, `#fraud`, `#legal`, `#industry-news`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Google Workspace MCP 服务器禁止 AI 代理发送 Gmail 邮件</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Google 为 Workspace 服务推出了 MCP（模型上下文协议）服务器，但 Gmail 服务器刻意不提供发送邮件的功能，仅允许经过批准的合作伙伴使用该能力。这一设计选择在 Hacker News 上引发了激烈讨论（251 分，214 条评论），争论该限制究竟是出于安全考虑还是商业决策。 这为大型平台如何限制 AI 代理访问核心服务树立了先例，可能迫使开发者寻求合作伙伴协议或采用浏览器自动化等变通方案。这也凸显了 MCP 等开放标准与平台变现策略之间的紧张关系，影响所有构建与邮件、日历或文档交互的 AI 代理的开发者。 MCP 已经包含“elicitation”原语，允许服务器在继续执行前暂停工具调用并请求用户确认，批评者认为这可以安全地控制发送邮件工具，而无需仅限合作伙伴使用。Google 的 Workspace MCP 服务器覆盖 Gmail、Drive 和 Calendar 等服务，但发送功能保留给合作伙伴，这为开源替代方案留下了填补空白的机会。

🔗 [来源](https://techstackups.com/articles/google-workspace-ai-agents-mcp/)

hackernews · ritzaco · 11月26日 09:44 · [社区讨论](https://news.ycombinator.com/item?id=50653477)

**背景**: 模型上下文协议（MCP）是由 Anthropic 于 2024 年 11 月推出的开放标准，旨在标准化大型语言模型等 AI 系统与外部工具和数据源的连接方式。MCP 服务器暴露工具、资源和提示等能力，客户端可以使用 elicitation 等原语请求用户确认。Google 的 Workspace MCP 服务器是其让 AI 代理与 Gmail、Drive、Calendar 等生产力服务交互的努力的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://developers.google.com/workspace/guides/configure-mcp-servers">Configure the Google Workspace MCP servers</a></li>
<li><a href="https://docs.mcp-agent.com/concepts/mcp-primitives">MCP Primitives - mcp-agent</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对 Google 的安全理由持怀疑态度，指出 MCP 的 elicitation 原语已经提供了确认机制，而仅限合作伙伴的限制看起来更像是商业决策。一些人警告用户会直接转向浏览器自动化，使该限制既无效又浪费，另一些人则认为这是 API 变现和平台控制收紧这一更广泛趋势的一部分。

**标签**: `#AI agents`, `#MCP`, `#Google Workspace`, `#API monetization`, `#platform policy`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Nextcloud 推出基于 Euro-Office 分支的桌面办公应用</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Nextcloud 发布了新的 Nextcloud Office 桌面应用，该应用基于 Euro-Office 构建，而 Euro-Office 是由 Nextcloud、Ionos、Proton 等欧洲公司组成的联盟创建的一个有争议的 ONLYOFFICE 分支。该应用将 Euro-Office 的文字处理、电子表格和演示编辑器带到桌面端，与现有的基于浏览器的 Nextcloud Office 形成互补。 此次发布为自托管的 Nextcloud 用户提供了原生桌面文档编辑选项，可能减少对 Microsoft Office 和 Google Workspace 的依赖。这也表明欧洲主导的开源办公替代方案势头渐长，不过该分支的治理和安全实践仍受到审视。 该桌面应用使用本地安装的字体，包括企业字体和操作系统默认字体（如 Windows 上的 Microsoft 字体），并允许用户无需管理员介入即可添加自定义字体。社区成员指出，该应用似乎使用 Chromium Embedded Framework 构建界面，核心为 C++，并担心 Euro-Office 分支可能缺少 ONLYOFFICE 10.0.0 中的安全修复。

🔗 [来源](https://nextcloud.com/blog/euro-office-comes-to-your-desktop-with-the-nextcloud-office-desktop-app/)

hackernews · e12e · 11月26日 11:50 · [社区讨论](https://news.ycombinator.com/item?id=50654289)

**背景**: Euro-Office 于 2026 年 3 月 27 日由九家欧洲公司组成的联盟宣布，作为开源 ONLYOFFICE 代码库的分支，旨在提供 Microsoft Office 的欧洲替代方案。ONLYOFFICE 是一款广泛使用的开源办公套件，其 2026 年 10 月发布的 10.0.0 版本包含了 40 多项安全修复。对活跃维护的项目进行分支会引发关于如何合并安全补丁和上游改进的问题，这也是社区争论的核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://itsfoss.com/news/onlyoffice-forked/">ONLYOFFICE Gets Forked as "Made in Europe", Sparks Licensing ...</a></li>
<li><a href="https://blog.elest.io/euro-office-vs-onlyoffice-the-fork-thats-splitting-the-self-hosted-office-world/">Euro-Office vs OnlyOffice: The Fork That's Splitting the Self ...</a></li>
<li><a href="https://nextcloud.com/blog/euro-office-comes-to-your-desktop-with-the-nextcloud-office-desktop-app/">Euro- Office comes to your desktop with the Nextcloud ... - Nextcloud</a></li>

</ul>
</details>

**社区讨论**: 评论者对该分支的联盟治理表示怀疑，并警告可能缺少来自 ONLYOFFICE 的安全补丁。不过，一些用户称赞电子表格编辑器的外观和手感，认为它优于 GridCraft 等替代品，并欢迎有更多选择来摆脱 OpenOffice。

**标签**: `#open-source`, `#office-software`, `#onlyoffice`, `#nextcloud`, `#security`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Hugging Face 推出面向 AMD Ryzen 和 Radeon 的 llama.cpp 基准测试仪表板</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Hugging Face 与 ggml-org 合作推出了一个新的基准测试仪表板，用于追踪 llama.cpp 在 AMD Ryzen CPU 和 Radeon GPU 上的性能表现。该仪表板为 AMD 硬件上的本地大语言模型推理提供了公开可访问的性能数据。 该仪表板为开发者和爱好者提供了可靠、集中的性能数据，以便在 AMD 平台上优化 llama.cpp 推理，而 AMD 硬件此前在基准测试透明度方面一直落后于 NVIDIA。它通过帮助用户做出明智的硬件和配置选择，支持了不断壮大的本地大语言模型社区。 该仪表板聚焦于 llama.cpp——这个驱动众多本地大语言模型工具的开源 C/C++ 推理库，覆盖 AMD Ryzen 处理器（包括配备专用 AI 引擎的 Ryzen AI 型号）和 Radeon GPU。它汇总了基准测试结果，具体指标和测试配置可在仪表板上查看。

🔗 [来源](https://huggingface.co/blog/ggml-org/llamacpp-amd-bench)

rss · Hugging Face Blog · 11月26日 11:37

**背景**: llama.cpp 是一个开源库，用于在消费级硬件上高效运行大语言模型，与 GGML 张量库共同开发。它已成为本地推理的事实标准，是 Ollama 和 LM Studio 等工具的基础。AMD 的 Ryzen CPU 和 Radeon GPU 在本地 AI 工作负载中很受欢迎，但其性能数据相比 NVIDIA GPU 一直不够集中。基准测试仪表板可帮助用户比较硬件和软件配置，以获得最佳推理速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/llama.cpp: LLM inference in C/C++</a></li>
<li><a href="https://www.amd.com/en/products/processors/consumer/ryzen-ai.html">AMD Ryzen™ AI - Windows PCs with AI Built In</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AMD`, `#benchmarking`, `#LLM inference`, `#hardware`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">NVIDIA 发布 Nemotron 3.5 Parse 的开放数据与微调方案</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

NVIDIA 在 Hugging Face 博客文章中详细介绍了开放的合成训练数据集、微调方案以及用于加速推理的 DFlash2 推测器，这些资源针对其 Nemotron 3.5 Parse 文档模型。此次发布基于原模型，为从业者提供了可复现的资源，以便对其进行专门化和优化。 这很重要，因为开放数据和方案降低了开发者针对特定领域任务微调文档解析模型的门槛，有望提升检索增强生成（RAG）和智能体工作流的准确性与效率。这也反映了 NVIDIA 围绕其 Nemotron 模型系列构建开放生态的努力。 该博客文章由 Ryan Chesler、Marek Wawrzos 和 Steve Han 撰写，包含合成训练数据集和微调方案，以及旨在加速推理的 DFlash2 推测器。模型本身是一个紧凑的文档模型，可从页面图像中提取文本、表格和布局，并可通过 Hugging Face 和 NVIDIA NIM 获取。

🔗 [来源](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin)

rss · Hugging Face Blog · 11月26日 05:05

**背景**: Nemotron 3.5 Parse 是 NVIDIA 推出的紧凑型文档解析模型，可将页面图像转换为结构化数据，用于检索增强生成（RAG）和 AI 智能体。微调是利用额外数据将预训练模型适配到特定领域，而推测解码（DFlash2）等推理优化技术旨在降低延迟。开放数据发布使研究人员和开发者能够复现并基于 NVIDIA 的成果进行构建。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin">Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning, and ...</a></li>
<li><a href="https://huggingface.co/nvidia/Nemotron-3.5-Parse">nvidia/ Nemotron - 3 . 5 - Parse · Hugging Face</a></li>
<li><a href="https://dev.to/delimitter/nvidia-opens-the-training-data-behind-nemotron-35-parse-1888m-synthetic-examples-fine-tuning-2h8k">NVIDIA opens the training data behind Nemotron 3.5 Parse - 18 ...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Nemotron`, `#fine-tuning`, `#inference-optimization`, `#open-data`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Hugging Face 详解多智能体系统的构建、训练与评估</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Hugging Face 发布了一篇题为《Swarms, Flocks, Gangs: How to build, train, and evaluate multi-agent systems》的技术博客，讲解了如何构建、训练和评估由多个交互式 AI 智能体组成的系统。文章引入了“swarms”“flocks”“gangs”等术语来描述不同的多智能体配置。 多智能体系统在 AI/ML 领域日益重要，能够解决单个智能体难以处理的复杂任务，而该博客提供的训练与评估实践指南有助于开发者避免常见陷阱。随着基于大语言模型的多智能体研究不断发展，这类方法论见解对构建生产系统的团队具有重要价值。 文章指出，增加智能体会改变智能体的上下文和预算，进而增加整个系统的复杂性，并借鉴了多智能体强化学习的研究——该领域早在语言模型被称为“swarms”之前就已研究合作与竞争。与单智能体评估相比，多智能体系统的评估面临独特挑战，需要在流程的每一步进行精心设计。

🔗 [来源](https://huggingface.co/blog/training-swarms)

rss · Hugging Face Blog · 11月26日 00:00

**背景**: 多智能体系统（MAS）是由多个交互式智能体组成的计算系统，能够解决单个智能体或单体系统难以或无法解决的问题。随着大语言模型（LLM）的进步，基于 LLM 的多智能体系统已成为新的研究领域，使智能体之间能够进行更复杂的交互与协调。与旨在解释自然系统中集体行为的基于智能体的模型（ABM）不同，MAS 侧重于解决实际工程问题。其应用包括在线交易、灾难响应、目标监视和社会结构建模等。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multi-agent_system">Multi-agent system</a></li>
<li><a href="https://huggingface.co/blog/training-swarms">Swarms , Flocks , Gangs : How to build, train, and evaluate...</a></li>
<li><a href="https://arize.com/docs/phoenix/evaluation/concepts-evals/evaluating-multi-agent-systems">Evaluating Multi - Agent Systems - Phoenix</a></li>

</ul>
</details>

**标签**: `#multi-agent systems`, `#AI`, `#machine learning`, `#training`, `#evaluation`

</details>


<a id="item-11"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">科学家界定 AI 智能体在研究中的使用边界</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

艾伦人工智能研究所（AI2）在 Hugging Face 上发布的一篇博客文章调查了科学家对使用 AI 智能体的界限，重点关注研究流程中的信任、自主性和实际边界。文章深入分析了研究人员如何决定哪些任务可以委托给自主 AI 系统，哪些任务需要保持人类控制。 随着 AI 智能体越来越能够自主执行多步骤研究任务，了解科学家在哪里划定界限对于负责任地采用和设计符合研究人员期望的工具至关重要。这一视角可以影响科学机构中 AI 智能体框架和政策的制定。 文章可能讨论了 AI 智能体不同级别的自主性，从辅助工具到完全自主系统，并指出科学家可能信任智能体进行常规数据处理，但对高风险决策仍保持谨慎。它强调了研究流程中透明度、可重复性和人类监督的必要性。

🔗 [来源](https://huggingface.co/blog/allenai/where-scientists-draw-the-line-on-ai-agents)

rss · Hugging Face Blog · 11月25日 18:52

**背景**: AI 智能体是使用人工智能代表用户追求目标并完成任务的软件系统，表现出推理、规划、记忆和一定程度的自主性。它们越来越多地用于科学研究中的文献综述、数据分析和实验设计等任务。Hugging Face 是一个流行的 AI 模型和数据集共享平台，而 AI2 是一家致力于 AI 造福人类的领先研究机构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/levels-of-autonomy-in-ai-agents">Autonomy Levels in AI Agents</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#scientific research`, `#AI adoption`, `#trust and autonomy`, `#Hugging Face`

</details>


<a id="item-12"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">SpaceX 的 Starmind AI 数据卫星星座获批</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

SpaceX 的 Starmind 星座已获得监管批准，计划部署多达一百万颗卫星，从轨道提供 AI 计算能力。该星座旨在以最具成本和能源效率的方式满足日益增长的 AI 计算需求。 这一批准标志着向太空 AI 基础设施迈出了重要一步，可能改变大规模计算的方式并减少对地面数据中心的依赖。它可能对 AI 行业、能源消耗和太空政策产生重大影响。 Starmind 卫星设计为在轨道上处理数据，而不仅仅是中继数据，这使其与 Starlink 以互联网为重点的架构区分开来。然而，卫星规格、轨道参数和部署时间表等技术细节仍然稀少。

🔗 [来源](https://www.bbc.co.uk/news/articles/cwp836l8n1jgo?at_medium=RSS&at_campaign=rss)

rss · BBC World · 11月26日 09:27

**背景**: Starlink 是 SpaceX 现有的卫星互联网星座，通过数千颗低地球轨道卫星提供宽带覆盖。Starmind 基于这一概念，但专注于 AI 计算，旨在创建利用太阳能和太空条件提高能效的轨道数据中心。太空计算的想法正日益受到关注，谷歌等公司也在探索类似概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.spacex.com/spacexai/starmind">SpaceX</a></li>
<li><a href="https://www.starmindx.space/">STARMIND — SpaceX 's AI Satellite</a></li>
<li><a href="https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/">Exploring a space- based , scalable AI infrastructure system design</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#satellite internet`, `#AI infrastructure`, `#space policy`, `#Starlink`

</details>


</section>