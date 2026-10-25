---
layout: default
title: "Horizon Summary: 2026-10-25 (ZH)"
date: 2026-10-25
lang: zh
---

> 从 115 条内容中筛选出 7 条重要资讯。

---

<section class="cat cat-science" markdown="1">

## 🧪 科学 (1)

<a id="item-1"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">Moderna 与 Merck 的 mRNA 癌症疫苗将黑色素瘤死亡和复发率降低 42%</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

Moderna 和 Merck 报告称，其个性化 mRNA 癌症疫苗 intismeran autogene 与 Keytruda（pembrolizumab）联合使用，在高危黑色素瘤患者的 2 期试验中，与单独使用 Keytruda 相比，将死亡或复发风险降低了 42%。 这是个性化 mRNA 癌症疫苗的一个重大临床里程碑，验证了该平台方法，并可能开启定制化癌症免疫治疗的新时代。如果在 3 期试验中得到证实，它可能显著改变黑色素瘤和其他癌症的治疗方式，影响患者、制药公司和生物技术行业。 2 期试验显示，单独使用 Keytruda 的复发/死亡绝对风险为 30%，联合治疗降至 18%，意味着需治疗人数约为 8.3。该疫苗针对每位患者的肿瘤突变进行个性化定制，需要测序和生产，仍需 3 期结果来确认疗效和安全性。

🔗 [来源](https://arstechnica.com/health/2026/10/personalized-mrna-cancer-vaccine-cut-melanoma-death-recurrence-by-42/)

hackernews · _Microft · 10月25日 19:29 · [社区讨论](https://news.ycombinator.com/item?id=50235217)

**背景**: 个性化 mRNA 癌症疫苗通过测序患者肿瘤以识别独特突变，然后将这些新抗原编码在 mRNA 中，训练免疫系统攻击癌细胞。Keytruda 是一种 PD-1 抑制剂，有助于恢复针对肿瘤的 T 细胞免疫反应。2 期试验在 50-300 名患者中测试疗效，而 3 期试验规模更大，在监管批准前确认有效性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Personalized_mRNA_cancer_vaccine_therapy">Personalized mRNA cancer vaccine therapy - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pembrolizumab">Pembrolizumab - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Phases_of_clinical_research">Phases of clinical research - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者强调 Moderna 的商业模式是按需疫苗平台，类似于即时 3D 打印服务，并指出 BioNTech 正在开发类似的个性化癌症疫苗。一些人指出，当数据泄露时 Moderna 股价下跌，因为预期过高，而另一些人则强调从 30%到 18%的绝对风险降低是有意义的。

**标签**: `#mRNA`, `#cancer-vaccine`, `#biotech`, `#clinical-trial`, `#Moderna`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 科技 / AI (5)

<a id="item-2"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">10 年前的 CNN 在皮肤癌诊断上超越前沿 LLM</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Lynch Lab 的一篇博客文章报告称，一个已有 10 年历史的 Inception v3 卷积神经网络在来自 ISIC Archive 的 68,011 张皮肤镜和临床图像上进行了微调，在 200 个病变的测试集上诊断皮肤癌的表现优于两个前沿大型语言模型。 这一结果挑战了前沿 LLM 普遍更优的假设，并表明小型专用模型在狭窄的医学影像任务上可以更准确且更具成本效益，这可能影响医疗 AI 工具的构建和部署方式。 该 CNN 在单个 H100 GPU 上训练，并在完全留出的病变上测试（包括同一病变或患者的所有图像），以防止数据泄漏；然而，批评者认为比较可能不公平，因为 CNN 专门针对该任务进行了调优，而 LLM 则没有。

🔗 [来源](https://lynchlab.net/llm-skin-cancer)

hackernews · sungam · 10月25日 17:15 · [社区讨论](https://news.ycombinator.com/item?id=50233779)

**背景**: 卷积神经网络（CNN）是一类特别适合图像识别的深度学习模型，而 Inception v3 是 2015 年提出的著名架构。前沿 LLM 是在海量文本和多模态数据上训练的大型生成模型，但它们是通用的，并未针对医学图像分类进行专门优化。ISIC Archive 是用于皮肤病学研究的大型公共皮肤病变图像集合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convolutional_neural_network">Convolutional neural network - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/frontier-large-language-models-llms">Frontier Large Language Models - emergentmind.com</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为专用模型在狭窄任务上超越通用 LLM 是意料之中的，一些人认为可以利用 LLM 低成本地生成这类专用模型。其他人则对基准有效性提出质疑，指出 CNN 针对该任务进行了大量调优而 LLM 没有，这种比较可能类似于“刷榜”。

**标签**: `#machine-learning`, `#healthcare`, `#LLM`, `#CNN`, `#benchmarking`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Dan Luu 呼吁软件行业应更具雄心</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Dan Luu 发表了一篇文章，主张软件行业在构建软件时应更具雄心，这在 Hacker News 上引发了大规模讨论，获得 722 分和 668 条评论。 这篇文章和讨论凸显了关于工程文化、AI 对代码质量的影响以及科技泡沫内外软件差距的日益激烈的争论，这影响着开发者和用户。 评论者争论 AI 生成的代码是否会导致过拟合、难以维护的解决方案，分享了雄心勃勃的副项目案例，并指出科技行业之外的软件质量往往很差，以热泵等消费设备为例。

🔗 [来源](https://danluu.com/ambitious/)

hackernews · ltratt · 10月24日 21:47 · [社区讨论](https://news.ycombinator.com/item?id=50225695)

**背景**: Dan Luu 是一位知名的软件工程师和博主，经常撰写关于工程文化和软件质量的文章。Hacker News 是一个流行的技术讨论论坛，这类文章经常引发辩论。讨论反映了人们对 AI 在软件开发中的作用以及基础工具价值的更广泛担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者观点不一：一些人认为 AI 加速了开发，但产生了混乱、过拟合的代码，而另一些人则分享了 AI 支持的雄心勃勃的项目。几位评论者指出科技泡沫之外的软件质量很差，一些人质疑雄心应聚焦于基础工具而非花哨功能。

**标签**: `#software-engineering`, `#engineering-culture`, `#ai-coding`, `#software-quality`, `#hackernews-discussion`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">加州大学伯克利分校数学教授因 AI 停止批改作业</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

菲尔兹奖得主、加州大学伯克利分校教授理查德·博切兹在观察到许多学生使用 AI 工具持续获得高分后，已停止批改作业的正确性。他现在质疑批改作业是否还有意义。 这一决定凸显了学术界日益严峻的挑战：AI 工具使传统的作业评估变得不可靠，迫使教育者重新思考如何评估学生的学习并维护学术诚信。这可能加速向课堂考试或口试的转变。 博切兹是一位著名数学家，以证明“魔群月光”猜想而闻名，他的立场具有分量。然而，正如一些评论者指出的，他可能早已将批改工作交给助教，因此这一变化可能更具象征意义而非实际意义。

🔗 [来源](https://www.dailycal.org/news/campus/academics/ai-use-leads-uc-berkeley-math-professor-to-see-no-point-in-grading-homework/article_bdf1eae2-c08b-491f-b9f1-81a7cea177de.html)

hackernews · romanhn · 10月25日 16:28 · [社区讨论](https://news.ycombinator.com/item?id=50233304)

**背景**: 理查德·博切兹因在格、群论和无限维代数方面的工作于 1998 年获得菲尔兹奖。他证明的“魔群月光”猜想提出了模函数与魔群之间的深刻联系。像 ChatGPT 这样的 AI 工具越来越有能力解决作业问题，引发了对作弊和家庭作业有效性的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Richard_Borcherds">Richard Borcherds - Wikipedia</a></li>
<li><a href="https://www.dailycal.org/news/campus/academics/ai-use-leads-uc-berkeley-math-professor-to-see-no-point-in-grading-homework/article_bdf1eae2-c08b-491f-b9f1-81a7cea177de.html">AI use leads UC Berkeley math professor to see ‘no point’ in ...</a></li>

</ul>
</details>

**社区讨论**: 评论者就作业的目的展开辩论，一些人认为作业有助于学习，而 AI 消除了强制参与，另一些人则质疑批改作业是否有意义。一些人指出讽刺之处：博切兹可能多年未亲自批改作业；还有人建议高等教育应重新聚焦学术而非职业培训。

**标签**: `#AI in education`, `#academic integrity`, `#homework grading`, `#AI impact`, `#higher education`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Cerebras 在晶圆级硬件上部署万亿参数 AI 模型</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Cerebras 发布博客文章，详细介绍了如何在其晶圆级硬件上服务万亿参数的前沿 AI 模型，并声称能够以其标志性的高推理速度运行这些超大模型。这一公告标志着 AI 基础设施领域的一项技术里程碑，但博客并未具体说明正在服务哪些模型或其发布日期。 由于内存和计算需求巨大，服务万亿参数模型是一项重大的技术挑战，而 Cerebras 能够在其晶圆级引擎上实现这一点，可能使其成为针对最大模型的基于 GPU 的推理的有竞争力替代方案。这对于需要快速、低延迟访问前沿 AI 能力的企业和开发者至关重要，可能重塑 AI 推理市场。 Cerebras 的晶圆级引擎在单个硅晶圆上集成了大量核心，实现了高内存带宽和核心间的低延迟通信，这对于服务万亿参数模型至关重要。然而，博客未提供具体的基准测试、模型名称或定价细节，留下了关于实际性能和成本效益的疑问。

🔗 [来源](https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras)

hackernews · gmays · 10月25日 01:33 · [社区讨论](https://news.ycombinator.com/item?id=50227356)

**背景**: Cerebras Systems 是一家以其晶圆级引擎（WSE）芯片而闻名的公司，这些芯片比传统 GPU 芯片大得多，旨在加速 AI 训练和推理。例如，WSE-3 为 CS-3 超级计算机提供动力，并通过 Cerebras 的 AI 推理云提供对 Llama 等模型的 API 访问。万亿参数模型（如 GPT-4 的某些版本）需要巨大的内存和计算资源，高效地服务这些模型是 AI 基础设施提供商面临的关键挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cerebras">Cerebras Systems - Wikipedia</a></li>
<li><a href="https://www.cerebras.ai/chip">Cerebras WSE-3 Turbo | Wafer - Scale AI Chip</a></li>
<li><a href="https://www.cerebras.ai/inference">Fastest AI Inference Cloud and API | Cerebras</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映出对 Cerebras 技术的赞赏与对其商业可行性和模型新鲜度的怀疑并存。一些用户指出 Cerebras 提供的模型过时，且缺乏满足需求的资源，而另一些人则认为即使延迟 6-9 个月，Cerebras 也能以较低成本和更高速度提供接近前沿的模型。还有人担心公司团队质量以及其平台上当前可用模型的实际效用。

**标签**: `#AI infrastructure`, `#Cerebras`, `#LLM serving`, `#wafer-scale hardware`, `#model deployment`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">研究人员在三星电视上获取 root shell，发现 TensorFlow Lite 模型和蓝牙扫描</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

一位名为 log4j 的反向工程师在三星电视上获取了 root shell，并发现该设备在 960x540 图像上运行 TensorFlow Lite 模型，并通过蓝牙扫描附近的麦克风，对狗叫和婴儿哭等音频事件进行分类。这些发现被分享在 Twitter 上，并在 Hacker News 上引发了广泛讨论，评论者就这些发现的新颖性和伦理问题展开了辩论。 这凸显了智能电视上遥测和本地处理的程度，引发了关于收集哪些数据以及如何使用这些数据的隐私担忧。它还强调了负责任的反向工程的重要性以及制造商透明度的必要性。 据报道，TensorFlow Lite 模型是采用 INT8 量化的 AlexNet，用于游戏检测，但性能较差且 CPU 占用率高。蓝牙麦克风扫描是 SmartThings 集成的一部分，电视会将事件计数器报告给三星，包括狗叫和婴儿哭的计数。

🔗 [来源](https://twitter.com/log4j/status/2113014142600953868?s=46)

hackernews · testing22321 · 10月24日 05:49 · [社区讨论](https://news.ycombinator.com/item?id=50218633)

**背景**: 智能电视通常包含语音控制和环境感知等功能，这些功能依赖麦克风和摄像头，并且它们会收集观看数据用于定向广告。反向工程是分析软件或硬件以理解其设计和功能的过程，通常用于揭示隐藏行为或安全漏洞。TensorFlow Lite 是用于移动和嵌入式设备的轻量级机器学习框架，蓝牙扫描允许设备发现附近的传感器和外设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zeli.app/story/50230181">Samsung's TV Runs a TensorFlow Lite · Hacker News | Zeli</a></li>
<li><a href="https://zeli.app/story/50231189">Samsung TVs Scan Your Home via Bluetooth · Hacker News | Zeli</a></li>
<li><a href="https://news.ycombinator.com/item?id=50218633">Root shell on Samsung TV | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 评论者指出类似发现之前已经发布过，并且狗叫和婴儿哭检测等功能是 SmartThings 集成的 advertised 功能，建议首先阅读公开文档。一些人讨论了用假数据污染遥测，而另一些人批评 OpenAI 据称封禁了研究人员，认为此类封禁降低了 LLM 在反向工程中的价值。

**标签**: `#smart-tv`, `#reverse-engineering`, `#privacy`, `#telemetry`, `#samsung`

</details>


</section>

<section class="cat cat-other" markdown="1">

## 📌 其他 (1)

<a id="item-7"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">俄勒冈警方对一家新闻媒体索要 250 万美元以获取一名警察的记录</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

俄勒冈州尤金警察局要求一家当地新闻媒体支付约 2,484,599.04 美元，以获取与一名警察相关的公共记录，并声称检索和处理这些记录至少需要 44,816 小时的员工工作时间。《拦截者》将此报道为政府机构利用高昂费用和拖延手段阻碍透明度请求的更广泛模式的一部分。 此案表明，公共记录费用可能被武器化，从而实际上拒绝公众获取有关警察行为的信息，损害了问责新闻业和公众监督执法的能力。它突显了一种全国性趋势，即政府机构利用成本估算和程序性拖延来逃避审查。 所引用的 44,816 个员工小时相当于一个人全职工作约 21 年，这一数字被广泛认为对于涉及一名警察的记录而言是荒谬的。俄勒冈州法律允许机构在披露主要惠及公众时免除或降低费用，但该警察局在此案中并未这样做。

🔗 [来源](https://theintercept.com/2026/10/01/oregon-police-misconduct-public-records-cost-fee/)

hackernews · tdeck · 10月25日 18:04 · [社区讨论](https://news.ycombinator.com/item?id=50234232)

**背景**: 公共记录法，如联邦《信息自由法》（FOIA）及州级对应法律，赋予公众请求政府文件的权利。机构可以收取检索、审查和复制费用，但这些费用应反映实际成本，并且如果披露符合公共利益，可以予以免除。在俄勒冈州，公共记录法（ORS 192）包含当发布记录主要惠及公众时可免除费用的条款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://oregon.public.law/rules/oar_250-001-0020">OAR 250-001-0020 – Fees for Public Records - OregonLaws</a></li>
<li><a href="https://www.oregonlegislature.gov/lpro/Publications/Public-Records-Fees-and-Waivers-Background-Brief.pdf">PUBLIC RECORDS FEES AND WAIVERS - Oregon Legislative Assembly</a></li>
<li><a href="https://foiabuddy.com/how-public-agencies-deny-foia-requests-common-tactics-explained/">How Public Agencies Deny FOIA Requests: Common Tactics ... Common Denials – Public First Law Center How to Overcome Common Tactics Used to Deny FOIA Requests Successful Lawsuits Challenging High Fee Demands for Public ... 5. Have agencies imposed prohibitive fees to discourage ...</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了个人遭遇 FOIA 阻碍的经历，包括一个学区八个月来每月只提供少量记录，并指出了国际上的类似情况，如德国正在就拟议的高昂费用进行斗争。许多人对 44,816 小时的荒谬性表示愤怒，并将美国体系与英国 30 天回复要求进行了对比。

**标签**: `#public-records`, `#foia`, `#government-transparency`, `#journalism`, `#police-accountability`

</details>


</section>