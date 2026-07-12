---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> 从 105 条内容中筛选出 8 条重要资讯。

---

<section class="cat cat-science" markdown="1">

## 🧪 科学 (1)

<a id="item-1"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">带状疱疹疫苗或降低痴呆风险</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

一项利用自然年龄截止点的英国研究发现，符合带状疱疹疫苗接种条件的人在七年内患痴呆症的风险显著降低。 这一发现表明，一种简单且广泛可用的疫苗可能有助于预防痴呆症——这种疾病影响全球数百万人，且目前尚无治愈方法。 该研究利用了英国疫苗接种资格中的严格年龄截止点，形成了一个自然实验，增强了因果证据。这种效果是在含有佐剂的新型 Shingrix 疫苗中观察到的，佐剂可能增强免疫反应。

🔗 [来源](https://www.economist.com/leaders/2026/07/09/a-no-brainer-for-protecting-your-brain)

hackernews · saikatsg · 7月12日 15:23 · [社区讨论](https://news.ycombinator.com/item?id=48881874)

**背景**: 痴呆症（包括阿尔茨海默病）是一种进行性脑部疾病，会损害记忆和认知。以往的观察性研究曾暗示带状疱疹疫苗接种与较低的痴呆风险之间存在关联，但混杂因素使因果关系不确定。年龄截止点设计有助于分离疫苗的效果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2025/04/02/health/shingles-vaccine-dementia.html">Shingles Vaccine Can Decrease Risk of Dementia , Study Finds...</a></li>
<li><a href="https://www.theguardian.com/society/2025/apr/02/study-finds-strongest-evidence-yet-that-shingles-vaccine-helps-cut-dementia-risk">Study finds strongest evidence yet that shingles vaccine helps cut...</a></li>
<li><a href="https://medicalxpress.com/news/2026-06-shingles-vaccine-dementia.html">Shingles vaccine may lower dementia risk , study suggests</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了个人轶事和科学背景。一些人表示怀疑，指出可能存在检测偏倚：接种疫苗的人可能住院次数更少，从而偶然诊断出痴呆症的机会也更少。其他人则指出痴呆症有多种风险因素，并认为疫苗是一种值得的干预措施。

**标签**: `#dementia`, `#vaccine`, `#public health`, `#neuroscience`, `#epidemiology`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 科技 / AI (7)

<a id="item-2"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">vLLM v0.25.0：MRv2 成为默认，PagedAttention 被移除</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

vLLM v0.25.0 将 Model Runner V2 设为所有稠密模型的默认执行路径，移除了传统的 PagedAttention 实现，并引入了新的流式解析引擎。该版本包含来自 232 位贡献者的 558 次提交，新增了对 LLaVA-OneVision-2 和 GLM-5 等模型的支持，并将 Transformers 后端的性能提升至与原生 vLLM 相当。 此版本标志着 vLLM 架构的重大转变，统一了执行路径并移除了遗留代码，从而简化了维护并提升了性能。新的默认 MRv2 和 PagedAttention 的移除表明推理引擎已趋于成熟和精简，这将惠及整个 LLM 服务生态系统。 Model Runner V2 现在支持 EVS、实时嵌入、Mamba 混合模型的前缀缓存以及全 CUDA 图的动态推测解码。Transformers 后端达到了与原生 vLLM 相当的速度，并获得了 FP8 MoE 支持；新的流式解析引擎为工具调用和推理解析提供了统一框架。

🔗 [来源](https://github.com/vllm-project/vllm/releases/tag/v0.25.0)

github · khluu · 7月11日 20:06

**背景**: vLLM 是一个高吞吐量、内存高效的 LLM 推理和服务引擎，最初由加州大学伯克利分校开发。PagedAttention 是其核心创新，实现了注意力计算的高效内存管理。Model Runner V2 (MRv2) 是一个较新的执行后端，统一了模型执行并提升了性能。此版本将 MRv2 设为稠密模型的默认后端，并移除了较旧的 PagedAttention 代码，因为 V1/MRv2 后端现已覆盖所有用例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm-project/vllm</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>
<li><a href="https://vllm.ai/blog/2023-06-20-vllm">vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#open source`, `#release`, `#AI infrastructure`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Claude Code 在读取提示前使用 3.3 万 token，而 OpenCode 仅用 7 千</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Systima 的一项研究发现，Claude Code 在读取用户提示前发送约 3.3 万个 token，而 OpenCode 仅发送约 7 千个 token，token 开销相差 4.7 倍。 这种低效会显著增加用户成本，尤其是按 token 计费的用户，并引发对 AI 编码工具设计权衡的质疑。 开销来自系统提示、缓存写入、MCP 模式定义和子代理编排。但在多步骤任务中，Claude Code 的总 token 使用量可能因批处理而更低。

🔗 [来源](https://systima.ai/blog/claude-code-vs-opencode-token-overhead)

hackernews · systima · 7月12日 18:25 · [社区讨论](https://news.ycombinator.com/item?id=48883275)

**背景**: Claude Code 和 OpenCode 是基于 AI 的编码助手，使用大型语言模型帮助开发者编写代码。它们在处理用户输入前会向模型发送系统提示和上下文，消耗用户付费的 token。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://systima.ai/blog/claude-code-vs-opencode-token-overhead">Claude Code Sends 4.7x More Tokens Than OpenCode Before Reading Your Prompt | Systima Blog</a></li>
<li><a href="https://github.com/anthropics/claude-code/issues/26404">[Bug Report] Weekly token usage limit draining abnormally fast...</a></li>
<li><a href="https://www.truefoundry.com/blog/opencode-token-usage-how-it-works-and-how-to-optimize-it">OpenCode Token Usage: How It Works and How to Optimize It</a></li>

</ul>
</details>

**社区讨论**: 评论者指出子代理会快速消耗 token，有人怀疑 Anthropic 设计 Claude Code 使用更多 token 以盈利。作者承认了一个合理的批评，并计划添加定性比较和复现输入/输出。

**标签**: `#AI coding tools`, `#token efficiency`, `#Claude Code`, `#OpenCode`, `#cost analysis`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">陶哲轩谈用 LLM 编程代理开发应用</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

著名数学家陶哲轩分享了他使用基于 LLM 的现代编程代理为研究论文构建交互式可视化和应用的经验，强调了它们在非关键任务中的实用性。 这表明即使是顶尖研究人员也在采用 LLM 编程代理进行实际软件开发，标志着软件创建方式在各领域的转变，尤其是在非关键、探索性任务中。 陶哲轩指出，虽然这些代理在生成可视化等补充内容时很有用，但对于关键任务代码并不可靠，他认为在非必要组件中承担这种风险是可以接受的。

🔗 [来源](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/)

hackernews · subset · 7月12日 11:09 · [社区讨论](https://news.ycombinator.com/item?id=48880170)

**背景**: LLM 编程代理是使用大型语言模型生成或辅助编写代码的 AI 工具。它们在快速原型设计和构建简单应用方面越来越受欢迎，但在复杂或安全关键型软件中的可靠性仍存在争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opencode.ai/">OpenCode | The open source AI coding agent</a></li>
<li><a href="https://cursor.com/">Cursor: AI coding agent</a></li>

</ul>
</details>

**社区讨论**: 评论者对将 LLM 用于教育可视化表示兴奋，并指出传统技术领域之外存在巨大的潜在软件需求。有人幽默地将陶哲轩的经历比作厨师发现微波炉餐，而其他人则强调将 LLM 视为工具并设定适当的信任边界的重要性。

**标签**: `#LLM`, `#coding agents`, `#software development`, `#AI tools`, `#education`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">LLM 变革巨大，但炒作过头</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

George Hotz 认为，尽管 LLM 具有变革性，但前沿实验室无法捕获其创造的价值，生产力提升体现在私有的、一次性的软件中，而非可见的公共项目。 这一分析挑战了前沿 AI 实验室的高估值，并指出软件开发正向私有化、定制化解决方案转变，可能重塑开源生态和投资策略。 Hotz 指出，每月 100-200 美元的订阅费让前沿模型物超所值，但真正的生产力提升发生在私有家庭实验室和一次性脚本中，而非公共开源项目。

🔗 [来源](https://geohot.github.io//blog/jekyll/update/2026/07/12/i-love-llms.html)

hackernews · therepanic · 7月12日 18:31 · [社区讨论](https://news.ycombinator.com/item?id=48883343)

**背景**: 大型语言模型（如 GPT-4 和 Claude）在代码生成、写作和推理方面展现出卓越能力。OpenAI、Anthropic 等前沿实验室投入数十亿美元训练这些模型，期望通过订阅和 API 捕获价值。然而，开源替代方案和私有部署正在激增，引发了关于经济价值最终流向的疑问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/ai-value-capture-the-shift-to-model">AI Value Capture - The Shift To Model Labs</a></li>
<li><a href="https://grokipedia.com/page/AI_Value_Capture">AI Value Capture</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍赞同 Hotz 的观点，指出 LLM 开启了“随心所欲”的时代，分叉和定制软件比以往任何时候都容易。一些人担心开源项目的未来，因为在 LLM 辅助下维护分支变得轻而易举，向上游贡献的吸引力下降。

**标签**: `#LLMs`, `#AI hype`, `#open source`, `#productivity`, `#value capture`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Chromium 148 的 Math.tanh 可实现操作系统指纹识别</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Chromium 148 引入了依赖操作系统的 Math.tanh 实现，单次调用即可区分 Windows、macOS 和 Linux。这创造了一种新的浏览器指纹识别向量，能够揭示底层操作系统。 该技术使用户操作系统检测变得轻而易举，即使伪造 User-Agent 头也无济于事，从而损害用户隐私。它增加了反指纹识别工具必须对抗的指纹识别方法。 该指纹识别之所以有效，是因为 Math.tanh 的实现在不同平台上的舍入和精度不同。该技术还可以识别浏览器版本范围，因为行为可能随 Chromium 版本变化。

🔗 [来源](https://scrapfly.dev/posts/browser-math-os-fingerprint/)

hackernews · joahnn_s · 7月12日 21:12 · [社区讨论](https://news.ycombinator.com/item?id=48884853)

**背景**: 浏览器指纹识别通过收集设备和浏览器特征来识别用户，无需使用 Cookie。常见技术包括 Canvas 渲染、WebGL 和字体检测。Math.tanh 是 JavaScript 中的双曲正切函数；其实现并未标准化为跨平台一致，因此产生了依赖操作系统的行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Device_fingerprint">Device fingerprint - Wikipedia</a></li>
<li><a href="https://fingerprint.com/blog/browser-fingerprinting-techniques/">Browser Fingerprinting Techniques: 6 Top Methods Explained</a></li>
<li><a href="https://learn.microsoft.com/en-us/dotnet/api/system.math.tanh?view=net-10.0">Math.Tanh (Double) Method (System) | Microsoft Learn</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，该技术还可以识别浏览器版本范围，这比操作系统检测更有趣。一些人批评该文章可能是 AI 生成的，且动机来自作者的爬虫业务。另一些人则主张采用正确舍入的超越函数来消除此类指纹识别向量。

**标签**: `#browser fingerprinting`, `#privacy`, `#Chromium`, `#JavaScript`, `#OS detection`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">爱尔兰数据中心用电量已达全国 23%</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

根据最新数据，2025 年爱尔兰数据中心消耗了全国总计量电力的 23%，而 2015 年这一比例仅为 5%。 这一急剧增长凸显了数字基础设施日益增长的能源需求，引发了对电网压力和可持续性的担忧，并加剧了关于核能等能源解决方案的辩论。 到 2026 年，由于新建项目，数据中心可能占爱尔兰电力消耗的 32%。爱尔兰年总用电量约为 40 TWh，低于四座 EPR 反应堆的发电量。

🔗 [来源](https://www.theregister.com/on-prem/2026/07/11/irish-datacenters-now-guzzle-23-of-the-countrys-electricity/5270013)

hackernews · Bender · 7月12日 20:16 · [社区讨论](https://news.ycombinator.com/item?id=48884322)

**背景**: 由于优惠的企业税和凉爽的气候，爱尔兰已成为数据中心的主要枢纽，吸引了亚马逊、谷歌等科技巨头。快速扩张给国家电网带来压力，导致都柏林暂停新数据中心接入直至 2028 年。爱尔兰目前不使用核能，但有人提议将其作为基荷电力的解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacenterdynamics.com/en/news/global-data-center-electricity-use-to-double-by-2026-report/">Global data center electricity use to double by 2026 - IEA report - DCD</a></li>
<li><a href="https://extra.ie/2026/07/07/news/data-centres-consume-ireland-electricity">Data centres consume whopping amount of Irish electricity</a></li>
<li><a href="https://www.theregister.com/on-prem/2024/01/24/datacenters-could-draw-1/3-of-irelands-electricity-by-2026/1556307">Datacenters could draw 1/3 of Ireland 's electricity by 2026</a></li>

</ul>
</details>

**社区讨论**: 评论者就核能作为解决方案展开辩论，指出单个反应堆可为所有爱尔兰数据中心供电。其他人批评文章措辞有偏见，还有人将爱尔兰的人均数据中心能源使用量与加州进行比较。

**标签**: `#datacenter`, `#energy`, `#Ireland`, `#nuclear power`, `#sustainability`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">LLM 编程：类似 CGI 的转变正在贬低工匠精神？</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Fabien Sanglard 发表了一篇文章，将 LLM 在编程中的兴起与电影中 CGI 的转变进行类比，认为虽然 AI 提高了产出量，但可能贬低了工匠精神，并导致未来对人工编写代码的反弹。 这篇评论引起了许多开发者的共鸣，他们担心 AI 生成的代码重数量轻质量，可能侵蚀手工软件的价值，并引发长期的行业转变。 文章指出，拒绝使用 LLM 的人可能在产出量上落后，但强调阅读和理解代码架构的重要性。它还指出，编写测试现在更容易，但 LLM 生成的测试可能无法测试正确的行为。

🔗 [来源](https://fabiensanglard.net/extinct/index.html)

hackernews · zdw · 7月12日 15:17 · [社区讨论](https://news.ycombinator.com/item?id=48881830)

**背景**: 像 GPT-4 和 Claude 这样的大型语言模型（LLM）越来越多地被用于生成代码，承诺提高速度和生产力。电影行业也经历了类似的转变，CGI 最初提升了视觉效果，但后来因取代实际效果和贬低熟练劳动力而受到批评。现在一些人主张回归实际效果，如电影《拯救计划》所示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2506.16653">LLMs in Coding and their Impact on the Commercial Software ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computer-generated_imagery">Computer-generated imagery - Wikipedia</a></li>
<li><a href="https://www.nature.com/articles/s41599-025-04471-1">LLM-based collaborative programming: impact on students ...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多同意这个类比，指出 CGI 因非工会化的视觉特效公司而贬低了熟练劳动力，并预测对 AI 生成代码也会出现类似的反弹。一些人认为，基于数量的评估在软件工程中并不常见，而且 LLM 生成的测试可能遗漏行为正确性。

**标签**: `#LLM`, `#software engineering`, `#AI impact`, `#craftsmanship`, `#analogy`

</details>


</section>