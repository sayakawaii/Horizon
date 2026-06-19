---
layout: default
title: "Horizon Summary: 2026-06-19 (ZH)"
date: 2026-06-19
lang: zh
---

> 从 145 条内容中筛选出 14 条重要资讯。

---

<section class="cat cat-geopolitics" markdown="1">

## 🌐 国际局势 (1)

<a id="item-1"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">两党法案瞄准政府对在线言论的胁迫</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

参议员罗恩·怀登和特德·克鲁兹提出了一项两党法案——《JAWBONE 法案》，旨在遏制政府向在线平台施压以压制合法言论。电子前哨基金会（EFF）称赞该法案解决了这一关键问题。 该法案可以保护合法在线言论免受幕后政府胁迫，这种胁迫曾被用来不经正当程序压制异议。它解决了人们对政府影响平台内容审核日益增长的担忧。 该法案全称为《反对官僚机构过度干预网络表达的正义法案》（JAWBONE 法案）。其目的是防止联邦机构施压平台删除受第一修正案保护的内容。

🔗 [来源](https://www.eff.org/deeplinks/2026/06/new-bill-takes-aim-government-pressure-silence-lawful-online-speech)

hackernews · hn_acker · 6月19日 17:34 · [社区讨论](https://news.ycombinator.com/item?id=48600950)

**背景**: 政府越来越多地使用非正式压力（如信件和会议）来推动在线平台删除内容，从而绕过法律程序。EFF 一直反对这种胁迫，包括代表 ICEBlock（一款举报移民执法活动的应用）的创建者。该法案旨在正式确立针对此类行为的保护措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/02/platforms-bend-over-backward-to-help-dhs-censor-ice-critics-advocates-say/">Platforms bend over backward to help DHS censor ICE... - Ars Technica</a></li>

</ul>
</details>

**社区讨论**: 评论者注意到 JAWBONE 这个巧妙的缩写，并表达了谨慎的乐观，一些人质疑该法案是否会保护他们不同意的言论。其他人则强调了该法案的两党性质，指出克鲁兹和怀登都是共同提案人，并分享了相关隐私立法的链接。

**标签**: `#online speech`, `#government pressure`, `#bipartisan bill`, `#EFF`, `#privacy`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 科技 / AI (12)

<a id="item-2"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">Project Valhalla 值类型在 JDK 28 中到来</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

Project Valhalla 为 Java 引入了值类型，实现了紧凑的内存布局和性能提升，最终设计将在 JDK 28 中到来。 这代表了十年的工作和 JVM 内存管理的范式转变，使 Java 开发者能够编写更高效、更不易出错的代码。 值类型是放弃标识的引用类型，允许 JVM 在数组中紧凑地存储值，无需每个元素的头部或指针。

🔗 [来源](https://www.jvm-weekly.com/p/project-valhalla-explained-how-a)

hackernews · philonoist · 6月19日 06:35 · [社区讨论](https://news.ycombinator.com/item?id=48595511)

**背景**: 在 Java 中，对象通常是具有标识的引用类型，这会导致头部和指针的内存开销。值类型类似于基本类型但由用户定义，通过内联存储数据来消除这种开销。Project Valhalla 已开发十多年，旨在为 JVM 带来这一能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Valhalla_(Java_language)">Project Valhalla ( Java language) - Wikipedia</a></li>
<li><a href="https://practicaldev-herokuapp-com.freetls.fastly.net/adaumircosta/understanding-value-types-project-valhalla-faf">Understanding Value Types ( Project Valhalla ) - DEV Community</a></li>
<li><a href="https://www.baeldung.com/java-valhalla-project">Java Valhalla Project | Baeldung</a></li>

</ul>
</details>

**社区讨论**: 评论中情绪复杂：一些人赞赏性能提升，但批评复杂性和空安全权衡；另一些人则辩护设计选择，并指出 Java 已经显著进化。

**标签**: `#Java`, `#JVM`, `#Project Valhalla`, `#value types`, `#performance`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">GLM-5.2：753B 参数的开源权重最强 LLM</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

Z.ai 发布了 GLM-5.2，这是一款采用 MIT 许可证的 753B 参数开源权重 LLM，拥有 100 万 token 上下文窗口，并在基准测试中取得顶尖表现。 GLM-5.2 在 Artificial Analysis Intelligence Index 上领先所有开源权重模型，超越其他主要开源模型，并在 Code Arena WebDev 排行榜上排名第二，表明开源 AI 能够与专有模型竞争。 该模型采用混合专家架构，总参数 753B 中激活 40 个专家参数，模型大小 1.51TB。它仅支持文本输入，独立的视觉模型 GLM-5V-Turbo 未开源。通过 OpenRouter 的定价为输入每百万 token 1.40 美元，输出每百万 token 4.40 美元。

🔗 [来源](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything)

rss · Simon Willison · 6月17日 23:58

**背景**: 混合专家（MoE）是一种架构，每个 token 只激活部分参数（专家），从而以较低计算成本实现更大模型。开源权重模型允许任何人下载、修改和使用模型权重，促进透明度和定制化。100 万 token 上下文窗口使得单次处理超长文档（如整本书或代码库）成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tensorops.ai/post/what-is-mixture-of-experts-llm">LLM Mixture of Experts Explained</a></li>
<li><a href="https://medium.com/@UjjwalJain_/what-does-a-1-million-token-context-window-actually-change-for-everyday-users-62d94664f2df">What Does a 1 Million Token Context Window Actually... | Medium</a></li>
<li><a href="https://medium.com/@aruna.kolluru/exploring-the-world-of-open-source-and-open-weights-ai-aa09707b69fc">Exploring the World of Open Source and Open Weights AI | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区对 GLM-5.2 的基准测试表现和开放许可证印象深刻，但注意到其 token 使用量较高（每任务 43k 输出 token）。一些用户对 100 万上下文窗口感到兴奋，而另一些用户则对模型在某些提示下的 SVG 生成质量表示失望。

**标签**: `#LLM`, `#open-weights`, `#AI`, `#GLM-5.2`, `#benchmark`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">挪威禁止小学使用人工智能</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

挪威宣布在小学几乎全面禁止使用人工智能，6 至 13 岁的学生通常不得使用 AI，而 14 至 16 岁的学生可在教师监督下谨慎使用。 该政策为教育领域的 AI 监管树立了先例，引发了关于如何平衡 AI 潜在益处与保留基础学习技能需求的讨论。 该禁令适用于生成式 AI 工具，但允许在初中阶段进行有监督的使用。政府强调，13 岁以下儿童需要在没有 AI 辅助的情况下学习阅读、写作和理解能力。

🔗 [来源](https://www.reuters.com/technology/norway-imposes-near-ban-ai-elementary-school-2026-06-19/)

hackernews · ilreb · 6月19日 16:03 · [社区讨论](https://news.ycombinator.com/item?id=48600093)

**背景**: 生成式 AI（如 ChatGPT）能够生成类似人类的文本，并越来越多地被用于教育领域。然而，人们担心过度依赖 AI 可能会阻碍批判性思维和基本技能的发展。挪威的决定反映了类似早期关于计算器在课堂中使用的谨慎态度。

**社区讨论**: 评论者大多支持该禁令，将其类比为在理解算术之前不允许使用计算器。一些人担心教师使用 AI 生成错误的练习题，而另一些人则强调了在适当保障下 AI 作为一对一辅导工具的潜力。

**标签**: `#AI regulation`, `#education`, `#Norway`, `#policy`, `#generative AI`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">ATProto 没有实例，Dan Abramov 解释</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Dan Abramov 发表了一篇博客文章，解释 ATProto（Bluesky 背后的协议）没有像 Mastodon 那样的“实例”，而是采用由个人数据服务器（PDS）、中继（Relay）和应用视图（AppView）组成的模块化架构。 这一澄清解决了关于 ATProto 去中心化架构的常见误解，帮助开发者和用户理解它与基于 ActivityPub 的系统（如 Mastodon）的区别，这可能影响采用和工具选择。 Abramov 用 RSS 类比来说明关注点分离：PDS 托管用户数据，中继聚合数据流，应用视图为特定应用处理数据。他认为问“实例在哪里？”是一个源于 Mastodon 思维的范畴错误。

🔗 [来源](https://overreacted.io/there-are-no-instances-in-atproto/)

hackernews · danabramov · 6月19日 15:10 · [社区讨论](https://news.ycombinator.com/item?id=48599515)

**背景**: ATProto 是驱动 Bluesky 的去中心化协议，旨在实现可移植账户和可互操作的社交应用。与 Mastodon 基于实例的联邦不同，ATProto 将数据存储（PDS）、数据中继和应用逻辑（AppView）分离，以避免碎片化并实现全局聚合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>
<li><a href="https://atproto.wiki/en/wiki/reference/core-architecture/appview">AppViews | AT Protocol Community Wiki</a></li>
<li><a href="https://atproto.brussels/atproto-architecture">ATProto Architecture • atproto.brussels</a></li>

</ul>
</details>

**社区讨论**: 评论对 RSS 类比的准确性进行了辩论，一些人认为中继是关键依赖，与 RSS 阅读器不同。其他人则称赞架构清晰，但指出 PDS 仍然类似于客户端-服务器模型，并非完全点对点。

**标签**: `#ATProto`, `#decentralization`, `#social media`, `#protocols`, `#architecture`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">现代汽车从软银完全收购波士顿动力</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

现代汽车集团行使看跌期权，从软银手中收购波士顿动力的剩余股份，以约 11 亿美元的估值完成对该机器人公司的完全控股。 此次收购使现代汽车在先进机器人领域占据领先地位，有望将波士顿动力的人形和四足机器人整合到制造和物流中，应对劳动力短缺和自动化需求。 现代汽车最初于 2020 年 12 月以 8.8 亿美元收购了 80%的股份，对波士顿动力的估值为 11 亿美元。剩余的 9%股份（软银保留少量股份后）通过软银行使的看跌期权收购。

🔗 [来源](https://startupfortune.com/hyundai-takes-full-control-of-boston-dynamics-as-softbank-exits-for-325-million/)

hackernews · ck2 · 6月19日 16:28 · [社区讨论](https://news.ycombinator.com/item?id=48600312)

**背景**: 波士顿动力以 Atlas（人形机器人）和 Spot（四足机器人）等先进机器人闻名。现代汽车作为大型汽车制造商，旨在利用机器人技术提升制造和出行能力。韩国拥有全球最高的机器人密度，2024 年每万名员工配备 1220 台机器人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spectrum.ieee.org/hyundai-buys-boston-dynamics">Hyundai Buys Boston Dynamics for Nearly $1 Billion. - IEEE Spectrum</a></li>
<li><a href="https://en.wikipedia.org/wiki/Atlas_(robot)">Atlas ( robot ) - Wikipedia</a></li>
<li><a href="https://www.hyundaimotorgroup.com/en/story/CONT0000000000001671">[Op-ed] Robots Jump into the Mobility Industry | Hyundai Motor Group</a></li>

</ul>
</details>

**社区讨论**: 评论者就人形机器人与专用设计的价值展开辩论，有人认为人形形态在制造中效率低下。另一些人则将此次收购与韩国劳动年龄人口下降和高机器人密度联系起来，认为这是应对劳动力短缺的战略举措。

**标签**: `#robotics`, `#acquisition`, `#Hyundai`, `#Boston Dynamics`, `#manufacturing`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">业余研究者借助 AI 破解古代线形文字 A</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

业余研究者 Tom Di Mino 使用 Anthropic 的 Claude Code 构建 Python 脚本，系统分析线形文字 A 语料库，成功翻译了 300 多个单词。该成果目前正由罗格斯大学和剑桥大学的语言学专家进行学术评审。 线形文字 A 一个多世纪以来一直未被破译，这是首次可信的尝试翻译该文字的大量内容。如果得到验证，将可能揭示米诺斯语言和文化，同时展示了 AI 工具如何辅助复杂的语言学研究。 线形文字 A 的全部语料仅约 7500 个字符，分布在 1500 条铭文中，非常零碎。Di Mino 的方法以“奠酒公式”为起点，他的翻译还解决了线形文字 B 中的一些问题，增加了可信度。

🔗 [来源](https://aiclambake.com/clamtakes/linear-a/)

hackernews · Kosturdistan · 6月19日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=48600107)

**背景**: 线形文字 A 是米诺斯文明在公元前 1800 年至 1450 年间使用的书写系统，于 1900 年被重新发现，但至今未被破译。其衍生文字线形文字 B 在 1950 年代被成功解读，发现代表早期希腊语。该文字语料稀少且底层语言未知，阻碍了研究进展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Linear_A_script">Linear A script</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**社区讨论**: 社区持谨慎乐观态度，指出 Di Mino 的工作正在接受专家评审，其方法严谨，使用 AI 构建工具而非黑箱求解。一些评论者强调由于语料稀少，破译极其困难，但承认这是迄今为止最可信的尝试。

**标签**: `#Linear A`, `#AI`, `#linguistics`, `#Claude Code`, `#ancient scripts`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">AI 推理模型助力诊断罕见儿童遗传病</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

研究人员使用 OpenAI 推理模型，从先前未解决的病例中识别出 18 个新的罕见儿童遗传病诊断。 这展示了 AI 推理模型在医疗领域的实用价值，可能加速对常被多年漏诊的罕见病的诊断。 使用的模型是 OpenAI o1，一种推理模型，会在回答前花时间“思考”，使其更擅长分析临床和遗传数据等复杂任务。

🔗 [来源](https://openai.com/index/diagnose-rare-childhood-diseases)

rss · OpenAI Blog · 6月18日 08:00

**背景**: 罕见遗传病影响全球数百万儿童，但由于其罕见性和多样化的症状，诊断非常困难。AI 模型，尤其是推理模型，可以分析大量临床和遗传数据，提出人类医生可能遗漏的诊断。OpenAI 的 o1 是推理模型系列中的第一个，旨在提高复杂推理任务的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_o1">OpenAI o1 - Wikipedia</a></li>
<li><a href="https://www.nature.com/articles/d41586-026-00290-9">AI succeeds in diagnosing rare diseases</a></li>

</ul>
</details>

**标签**: `#AI`, `#healthcare`, `#rare diseases`, `#diagnosis`, `#OpenAI`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">MosaicLeaks：研究型智能体面临数据泄露风险</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

ServiceNow 的研究人员发现了一种名为 MosaicLeaks 的漏洞，该漏洞能够从类似马赛克的数据碎片中重建敏感信息，并提出了缓解策略。 该漏洞对 AI 智能体的安全构成严重威胁，因为研究型智能体经常处理机密数据；一旦被利用，可能导致大规模数据泄露。 该攻击利用了研究型智能体从多个来源聚合信息的方式，使攻击者能够将碎片拼凑成完整的秘密。研究人员在模拟的研究型智能体上演示了该攻击，并提供了检测代码。

🔗 [来源](https://huggingface.co/blog/ServiceNow/mosaicleaks)

rss · Hugging Face Blog · 6月18日 18:13

**背景**: 研究型智能体是自主收集和综合来自各种来源信息的 AI 系统，常用于文献综述或数据分析等任务。数据重建攻击是一类已知的隐私攻击，攻击者从模型输出中恢复训练数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/information-technology/2025/09/new-attack-on-chatgpt-research-agent-pilfers-secrets-from-gmail-inboxes/">New attack on ChatGPT research agent pilfers secrets... - Ars Technica</a></li>
<li><a href="https://aisecurityandsafety.org/en/glossary/data-reconstruction-attack/">Data Reconstruction Attack — Definition, Examples & Prevention in AI</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#security`, `#research agents`, `#data leakage`, `#vulnerability`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">超越 LoRA：探索更优微调方法</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Hugging Face 发布了一篇博客文章，研究超越 LoRA 的微调方法，比较它们的性能和效率。文章探讨了 (IA)³、Prefix Tuning 和 AdaLoRA 等替代方案，并提供了基准测试和实用见解。 LoRA 是最流行的参数高效微调技术，但替代方案可能在特定任务上提供更好的性能或效率。这项分析帮助从业者根据用例选择合适的方法，从而在降低成本的同时改进模型适配。 该博客比较了 (IA)³（缩放激活）和 AdaLoRA（动态分配秩）等方法。报告指出，(IA)³ 可以用更少的参数达到 LoRA 的性能，而 AdaLoRA 则按层调整秩以提高效率。

🔗 [来源](https://huggingface.co/blog/peft-beyond-lora)

rss · Hugging Face Blog · 6月18日 00:00

**背景**: 参数高效微调（PEFT）方法通过仅更新一小部分参数来适配大型预训练模型，从而降低计算成本。LoRA（低秩适配）是一种广泛使用的 PEFT 技术，它在模型层中注入可训练的低秩矩阵。然而，研究人员仍在继续开发可能提供更好性能与效率权衡的新方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/peft">Parameter-Efficient Fine-Tuning using 🤗 PEFT</a></li>
<li><a href="https://huggingface.co/learn/llm-course/chapter11/4">LoRA (Low-Rank Adaptation) · Hugging Face</a></li>
<li><a href="https://www.ibm.com/think/topics/parameter-efficient-fine-tuning">What is parameter-efficient fine-tuning (PEFT)? | IBM</a></li>

</ul>
</details>

**标签**: `#fine-tuning`, `#LoRA`, `#PEFT`, `#machine learning`, `#Hugging Face`

</details>


<a id="item-11"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">为智能体任务基准测试开源模型</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Hugging Face 发布了一份指南，介绍如何使用自定义工具对开源模型进行智能体任务的基准测试，重点强调评估方法和可重复性。 这解决了对开源模型智能体能力进行标准化评估的关键需求，随着基于智能体的 AI 系统激增，这一点至关重要。 该指南涵盖了如何设计衡量工具使用、多步推理和目标导向行为的基准测试，使用了如 Inspect 和 agent-eval 等框架。

🔗 [来源](https://huggingface.co/blog/is-it-agentic-enough)

rss · Hugging Face Blog · 6月18日 00:00

**背景**: AI 智能体是半自主或全自主的系统，能够感知、推理并使用工具行动。与传统机器学习模型不同，评估智能体需要评估决策和环境交互，而不仅仅是准确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://galileo.ai/learn/benchmark-ai-agents">How to Benchmark AI Agents Effectively - Galileo AI: The AI Observability and Evaluation Platform</a></li>
<li><a href="https://allenai.org/blog/astabench">AstaBench: Rigorous benchmarking of AI agents with a holistic scientific research suite | Ai2</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#benchmarking`, `#open-source models`, `#tooling`

</details>


<a id="item-12"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Google Workspace 可通过管理员策略屏蔽 Firefox</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Google Workspace 的上下文感知访问功能可以屏蔽 Firefox 用户，但这是管理员可配置的策略，并非 Google 的全局决定。 这凸显了企业安全中浏览器检测的日益普及，可能无意中限制用户选择，并引发对浏览器多样性的担忧。 该功能仅适用于 Google Workspace Enterprise 版本，而非 Business Plus，并由组织管理员通过管理控制台控制。

🔗 [来源](https://tales.fromprod.com/2026/169/google-workspace-threatening-to-block-firefox.html)

hackernews · birdculture · 6月19日 16:30 · [社区讨论](https://news.ycombinator.com/item?id=48600345)

**背景**: 上下文感知访问是 Google Workspace 的一项安全功能，允许管理员根据用户身份、设备安全状态、位置和其他属性创建细粒度的访问策略。它是零信任安全模型的一部分。浏览器检测可用于强制执行诸如要求使用 Chrome 才能访问等策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@heenashree2010/google-workspace-access-management-implementing-context-aware-access-the-right-way-73edfc3bb5b9">Google Workspace Access Management: Implementing... | Medium</a></li>
<li><a href="https://www.portnox.com/cybersecurity-101/context-aware-access/">Context - aware access - Portnox</a></li>

</ul>
</details>

**社区讨论**: 评论者澄清，屏蔽是由于管理员配置的上下文感知访问策略，而非 Google 的决定。博客作者确认他们没有使用 IAP，且使用的是 Business Plus 版本，因此屏蔽可能来自其他安全机制。一些人批评浏览器检测而非功能检测的做法。

**标签**: `#Google Workspace`, `#Firefox`, `#browser detection`, `#enterprise security`, `#context-aware access`

</details>


<a id="item-13"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Datasette Apps：在 Datasette 中托管自定义 HTML 应用</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

datasette-apps 插件允许用户在 Datasette 内部托管沙盒化的 HTML+JavaScript 应用程序，这些应用可以对底层数据执行只读和配置好的写入 SQL 查询。 该插件通过在平台内直接支持自定义交互式应用，显著扩展了 Datasette 的功能，使其成为数据探索和展示的更通用工具。 应用在受限的 <iframe sandbox="allow-scripts allow-forms"> 中运行，并带有注入的 CSP 头，阻止向外部主机发起 HTTP 请求，防止数据泄露。该插件注册了创建、查看、编辑、删除和管理应用访问的权限。

🔗 [来源](https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything)

rss · Simon Willison · 6月18日 23:58

**背景**: Datasette 是一个用于探索和发布数据的开源工具，提供 JSON API 用于自定义前端。datasette-apps 插件在此基础上允许用户嵌入直接与 API 交互的自定义 HTML/JS 应用，无需单独的服务器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/18/datasette-apps/">Datasette Apps : Host custom HTML applications inside Datasette</a></li>
<li><a href="https://pypi.org/project/datasette-apps/">Create apps that live inside Datasette</a></li>
<li><a href="https://docs.datasette.io/en/0.43/plugins.html">Plugins — Datasette documentation</a></li>

</ul>
</details>

**标签**: `#datasette`, `#plugin`, `#web-applications`, `#sql`, `#sandbox`

</details>


</section>

<section class="cat cat-other" markdown="1">

## 📌 其他 (1)

<a id="item-14"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">EFF 主张法院记录应免费开放</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

电子前哨基金会（EFF）发表文章，主张法院记录应免费开放，并批评当前的 PACER 收费系统。文章强调了《开放法院法案》，该立法提案旨在用现代化的统一平台取代老旧的 PACER 和 CM/ECF 系统。 公众获取法院记录是透明度和司法公正的基础，但当前的收费制度造成了障碍。如果《开放法院法案》获得通过，将大幅降低成本，并改善研究人员、记者和公众的访问条件。 《开放法院法案》将用现代化的统一平台取代老旧的 PACER 和 CM/ECF 系统，旨在改善公众访问、加强网络安全并降低长期成本。目前，PACER 按页收费，但贫困者、公益律师、学术研究人员和非营利组织可申请豁免。

🔗 [来源](https://www.eff.org/deeplinks/2026/06/court-records-should-be-free)

hackernews · hn_acker · 6月19日 17:34 · [社区讨论](https://news.ycombinator.com/item?id=48600946)

**背景**: PACER（公共法院电子记录访问系统）是美国联邦法院文件的电子公共访问服务，按页向用户收费。EFF 长期倡导免费获取法院记录，认为公众已通过税收为司法系统付费。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PACER_(law)">PACER (law) - Wikipedia</a></li>
<li><a href="https://pacer.uscourts.gov/pacer-pricing-how-fees-work">PACER Pricing: How fees work | PACER : Federal Court Records</a></li>
<li><a href="https://free.law/pacer-facts">Facts About PACER and CM/ECF | Free Law Project | Making the legal...</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对免费法院记录的支持，其中一人强调了 CourtListener 和 Recap 项目作为实用解决方案，可自动分享已购买的 PACER 文档。另一评论者指出，法院服务于公众，重复付费没有意义。

**标签**: `#legal`, `#public access`, `#EFF`, `#PACER`, `#open data`

</details>


</section>