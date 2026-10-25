---
layout: default
title: "Horizon Summary: 2026-10-25 (EN)"
date: 2026-10-25
lang: en
---

> From 115 items, 7 important content pieces were selected

---

<section class="cat cat-science" markdown="1">

## 🧪 Science (1)

<a id="item-1"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">Moderna and Merck's mRNA cancer vaccine cuts melanoma death and recurrence by 42%</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

Moderna and Merck reported that their personalized mRNA cancer vaccine, intismeran autogene, combined with Keytruda (pembrolizumab) reduced the risk of death or recurrence by 42% compared to Keytruda alone in a Phase 2 trial of patients with high-risk melanoma. This is a major clinical milestone for personalized mRNA cancer vaccines, validating the platform approach and potentially opening a new era of tailored cancer immunotherapy. If confirmed in Phase 3 trials, it could significantly change treatment for melanoma and other cancers, impacting patients, drugmakers, and the biotech industry. The Phase 2 trial showed an absolute risk reduction from 30% recurrence/death with Keytruda alone to 18% with the combination, meaning a number needed to treat of about 8.3. The vaccine is personalized to each patient's tumor mutations, requiring sequencing and manufacturing, and Phase 3 results are still needed to confirm efficacy and safety.

🔗 [Source](https://arstechnica.com/health/2026/10/personalized-mrna-cancer-vaccine-cut-melanoma-death-recurrence-by-42/)

hackernews · _Microft · Oct 25, 19:29 · [Discussion](https://news.ycombinator.com/item?id=50235217)

**Background**: Personalized mRNA cancer vaccines work by sequencing a patient's tumor to identify unique mutations, then encoding these neoantigens in mRNA to train the immune system to attack cancer cells. Keytruda is a PD-1 inhibitor that helps restore T-cell immune responses against tumors. Phase 2 trials test efficacy in 50-300 patients, while Phase 3 trials are larger and confirm effectiveness before regulatory approval.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Personalized_mRNA_cancer_vaccine_therapy">Personalized mRNA cancer vaccine therapy - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pembrolizumab">Pembrolizumab - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Phases_of_clinical_research">Phases of clinical research - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted Moderna's business model as an on-demand vaccine platform, similar to a just-in-time 3D printing service, and noted that BioNTech is working on similar personalized cancer vaccines. Some pointed out that Moderna's stock dropped when the data leaked because expectations were overly high, while others emphasized the meaningful absolute risk reduction from 30% to 18%.

**Tags**: `#mRNA`, `#cancer-vaccine`, `#biotech`, `#clinical-trial`, `#Moderna`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (5)

<a id="item-2"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">10-year-old CNN beats frontier LLMs in skin cancer diagnosis</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A blog post by the Lynch Lab reports that a 10-year-old Inception v3 convolutional neural network, fine-tuned on 68,011 dermoscopic and clinical images from the ISIC Archive, outperformed two frontier large language models in diagnosing skin cancer on a test set of 200 lesions. The result challenges the assumption that frontier LLMs are universally superior and highlights that small, specialized models can be far more accurate and cost-effective for narrow medical imaging tasks, which could influence how healthcare AI tools are built and deployed. The CNN was trained on a single H100 GPU and tested on lesions that were completely held out, including all images of the same lesion or patient, to prevent data leakage; however, critics argue the comparison may be unfair because the CNN was specifically tuned for the task while the LLMs were not.

🔗 [Source](https://lynchlab.net/llm-skin-cancer)

hackernews · sungam · Oct 25, 17:15 · [Discussion](https://news.ycombinator.com/item?id=50233779)

**Background**: Convolutional neural networks (CNNs) are a class of deep learning models particularly effective for image recognition, and Inception v3 is a well-known architecture from 2015. Frontier LLMs are large generative models trained on vast text and multimodal data, but they are general-purpose and not specifically optimized for medical image classification. The ISIC Archive is a large public collection of skin lesion images used for dermatology research.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convolutional_neural_network">Convolutional neural network - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/frontier-large-language-models-llms">Frontier Large Language Models - emergentmind.com</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree that specialized models are expected to outperform general LLMs on narrow tasks, with some arguing that LLMs can be used to generate such specialized models cheaply. Others raise concerns about benchmark validity, noting that the CNN was heavily tuned for the task while LLMs were not, and that the comparison may be akin to 'benchmaxxing'.

**Tags**: `#machine-learning`, `#healthcare`, `#LLM`, `#CNN`, `#benchmarking`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Dan Luu argues software industry should aim higher</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Dan Luu published an essay arguing that the software industry should be more ambitious in what it builds, which sparked a large Hacker News discussion with 722 points and 668 comments. The essay and discussion highlight a growing debate about engineering culture, the impact of AI on code quality, and the gap between software inside and outside the tech bubble, which affects developers and users alike. Commenters debated whether AI-generated code leads to overfit, unmaintainable solutions, shared examples of ambitious side projects, and noted that software quality outside tech is often poor, citing consumer devices like heat pumps.

🔗 [Source](https://danluu.com/ambitious/)

hackernews · ltratt · Oct 24, 21:47 · [Discussion](https://news.ycombinator.com/item?id=50225695)

**Background**: Dan Luu is a well-known software engineer and blogger who often writes about engineering culture and software quality. Hacker News is a popular forum for technology discussion where essays like this frequently spark debate. The discussion reflects broader concerns about AI's role in software development and the value of foundational tools.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters had mixed views: some argued AI speeds up development but produces messy, overfit code, while others shared ambitious projects enabled by AI. Several noted that software quality outside the tech bubble is poor, and some questioned whether ambition should focus on foundational tools rather than flashy features.

**Tags**: `#software-engineering`, `#engineering-culture`, `#ai-coding`, `#software-quality`, `#hackernews-discussion`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">UC Berkeley math professor stops grading homework due to AI</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Richard Borcherds, a Fields Medalist and professor at UC Berkeley, has stopped grading homework for correctness after observing that many students used AI tools to consistently earn top marks. He now questions whether grading homework has any point. This decision highlights a growing challenge in academia: AI tools are making traditional homework assessment unreliable, forcing educators to rethink how to evaluate student learning and maintain academic integrity. It could accelerate the shift toward in-class exams or oral assessments. Borcherds is a renowned mathematician known for proving the Monstrous Moonshine conjecture, and his stance carries weight. However, as some commenters noted, he likely already delegated grading to teaching assistants, so the change may be more symbolic than practical.

🔗 [Source](https://www.dailycal.org/news/campus/academics/ai-use-leads-uc-berkeley-math-professor-to-see-no-point-in-grading-homework/article_bdf1eae2-c08b-491f-b9f1-81a7cea177de.html)

hackernews · romanhn · Oct 25, 16:28 · [Discussion](https://news.ycombinator.com/item?id=50233304)

**Background**: Richard Borcherds won the Fields Medal in 1998 for his work in lattices, group theory, and infinite-dimensional algebras. The Monstrous Moonshine conjecture, which he proved, posits a deep connection between modular functions and the Monster Group. AI tools like ChatGPT have become increasingly capable of solving homework problems, raising concerns about cheating and the effectiveness of take-home assignments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Richard_Borcherds">Richard Borcherds - Wikipedia</a></li>
<li><a href="https://www.dailycal.org/news/campus/academics/ai-use-leads-uc-berkeley-math-professor-to-see-no-point-in-grading-homework/article_bdf1eae2-c08b-491f-b9f1-81a7cea177de.html">AI use leads UC Berkeley math professor to see ‘no point’ in ...</a></li>

</ul>
</details>

**Discussion**: Commenters debated the purpose of homework, with some arguing it helps learning and that AI removes the forced engagement, while others questioned whether grading homework is meaningful at all. Some noted the irony that Borcherds likely hadn't graded homework himself in years, and others suggested higher education should refocus on academia rather than job training.

**Tags**: `#AI in education`, `#academic integrity`, `#homework grading`, `#AI impact`, `#higher education`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Cerebras Deploys Trillion-Parameter AI Models on Wafer-Scale Hardware</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Cerebras published a blog post detailing how it serves trillion-parameter frontier AI models on its wafer-scale hardware, claiming the ability to run these massive models with its characteristic high inference speed. The announcement highlights a technical milestone in AI infrastructure, though the blog does not specify which exact models are being served or their release dates. Serving trillion-parameter models is a significant technical challenge due to memory and compute requirements, and Cerebras's ability to do so on its wafer-scale engine could position it as a competitive alternative to GPU-based inference for the largest models. This matters for enterprises and developers who need fast, low-latency access to frontier AI capabilities, potentially reshaping the AI inference market. Cerebras's wafer-scale engine integrates a vast number of cores on a single silicon wafer, enabling high memory bandwidth and low-latency communication between cores, which is crucial for serving trillion-parameter models. However, the blog does not provide specific benchmarks, model names, or pricing details, leaving questions about real-world performance and cost-effectiveness.

🔗 [Source](https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras)

hackernews · gmays · Oct 25, 01:33 · [Discussion](https://news.ycombinator.com/item?id=50227356)

**Background**: Cerebras Systems is a company known for its wafer-scale engine (WSE) chips, which are dramatically larger than traditional GPU dies and are designed to accelerate AI training and inference. The WSE-3, for example, powers the CS-3 supercomputer and is offered through Cerebras's AI inference cloud, providing API access to models like Llama. Trillion-parameter models, such as versions of GPT-4, require immense memory and compute, and serving them efficiently is a key challenge for AI infrastructure providers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cerebras">Cerebras Systems - Wikipedia</a></li>
<li><a href="https://www.cerebras.ai/chip">Cerebras WSE-3 Turbo | Wafer - Scale AI Chip</a></li>
<li><a href="https://www.cerebras.ai/inference">Fastest AI Inference Cloud and API | Cerebras</a></li>

</ul>
</details>

**Discussion**: Community comments reflect a mix of admiration for Cerebras's technology and skepticism about its business viability and model recency. Some users note that Cerebras serves outdated models and lacks the resources to keep up with demand, while others argue that even with a 6-9 month delay, Cerebras could offer near-frontier models at a fraction of the cost and with much higher speed. Concerns were also raised about the company's team quality and the practical utility of the models currently available on its platform.

**Tags**: `#AI infrastructure`, `#Cerebras`, `#LLM serving`, `#wafer-scale hardware`, `#model deployment`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Researcher Gains Root Shell on Samsung TV, Finds TensorFlow Lite and Bluetooth Scanning</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A reverse engineer known as log4j gained a root shell on a Samsung TV and discovered that the device runs a TensorFlow Lite model on 960x540 images and scans for nearby microphones via Bluetooth, classifying audio events such as dog barking and baby crying. The findings were shared on Twitter and discussed extensively on Hacker News, where commenters debated the novelty and ethics of the discoveries. This highlights the extent of telemetry and local processing on smart TVs, raising privacy concerns about what data is collected and how it is used. It also underscores the importance of responsible reverse engineering and the need for transparency from manufacturers. The TensorFlow Lite model is reported to be AlexNet with INT8 quantization, used for game detection, but it exhibits poor performance and high CPU usage. The Bluetooth microphone scanning is part of SmartThings integration, and the TV reports event counters back to Samsung, including dog-barking and baby-crying tallies.

🔗 [Source](https://twitter.com/log4j/status/2113014142600953868?s=46)

hackernews · testing22321 · Oct 24, 05:49 · [Discussion](https://news.ycombinator.com/item?id=50218633)

**Background**: Smart TVs often include features like voice control and ambient sensing that rely on microphones and cameras, and they collect viewing data for targeted advertising. Reverse engineering is the process of analyzing software or hardware to understand its design and functionality, often to uncover hidden behaviors or security flaws. TensorFlow Lite is a lightweight machine learning framework for mobile and embedded devices, and Bluetooth scanning allows devices to discover nearby sensors and peripherals.

<details><summary>References</summary>
<ul>
<li><a href="https://zeli.app/story/50230181">Samsung's TV Runs a TensorFlow Lite · Hacker News | Zeli</a></li>
<li><a href="https://zeli.app/story/50231189">Samsung TVs Scan Your Home via Bluetooth · Hacker News | Zeli</a></li>
<li><a href="https://news.ycombinator.com/item?id=50218633">Root shell on Samsung TV | Hacker News</a></li>

</ul>
</details>

**Discussion**: Commenters noted that similar findings have been posted before and that features like dog barking and baby crying detection are advertised for SmartThings integration, suggesting the need to read public documentation first. Some discussed poisoning telemetry with fake data, while others criticized OpenAI for allegedly banning the researcher, arguing that such bans reduce the value of LLMs for reverse engineering.

**Tags**: `#smart-tv`, `#reverse-engineering`, `#privacy`, `#telemetry`, `#samsung`

</details>


</section>

<section class="cat cat-other" markdown="1">

## 📌 Other (1)

<a id="item-7"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Oregon Police Charge News Outlet $2.5M for Records on One Officer</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

The Eugene Police Department in Oregon has demanded approximately $2,484,599.04 from a local news outlet for public records related to a single officer, claiming the search and processing would require at least 44,816 hours of staff time. The Intercept reports this as part of a broader pattern of agencies using prohibitive fees and delays to obstruct transparency requests. This case illustrates how public records fees can be weaponized to effectively deny access to information about police conduct, undermining accountability journalism and the public's ability to oversee law enforcement. It highlights a national trend where agencies use cost estimates and procedural delays to shield themselves from scrutiny. The quoted 44,816 staff hours equate to roughly 21 years of full-time work for a single person, an amount that is widely seen as absurd for records concerning one officer. Oregon law allows agencies to waive or reduce fees when disclosure primarily benefits the general public, but the department has not done so here.

🔗 [Source](https://theintercept.com/2026/10/01/oregon-police-misconduct-public-records-cost-fee/)

hackernews · tdeck · Oct 25, 18:04 · [Discussion](https://news.ycombinator.com/item?id=50234232)

**Background**: Public records laws, such as the federal Freedom of Information Act (FOIA) and state-level equivalents, grant the public the right to request government documents. Agencies may charge fees for search, review, and duplication, but these fees are supposed to reflect actual costs and can be waived if disclosure serves the public interest. In Oregon, the public records law (ORS 192) includes provisions for fee waivers when releasing records primarily benefits the general public.

<details><summary>References</summary>
<ul>
<li><a href="https://oregon.public.law/rules/oar_250-001-0020">OAR 250-001-0020 – Fees for Public Records - OregonLaws</a></li>
<li><a href="https://www.oregonlegislature.gov/lpro/Publications/Public-Records-Fees-and-Waivers-Background-Brief.pdf">PUBLIC RECORDS FEES AND WAIVERS - Oregon Legislative Assembly</a></li>
<li><a href="https://foiabuddy.com/how-public-agencies-deny-foia-requests-common-tactics-explained/">How Public Agencies Deny FOIA Requests: Common Tactics ... Common Denials – Public First Law Center How to Overcome Common Tactics Used to Deny FOIA Requests Successful Lawsuits Challenging High Fee Demands for Public ... 5. Have agencies imposed prohibitive fees to discourage ...</a></li>

</ul>
</details>

**Discussion**: Commenters shared personal experiences with FOIA obstruction, including a school district that has been dribbling out records monthly for eight months, and noted international parallels such as Germany's ongoing battle over proposed prohibitive fees. Many expressed outrage at the absurdity of 44,816 hours and contrasted the U.S. system with the U.K.'s 30-day response requirement.

**Tags**: `#public-records`, `#foia`, `#government-transparency`, `#journalism`, `#police-accountability`

</details>


</section>