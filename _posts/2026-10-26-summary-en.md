---
layout: default
title: "Horizon Summary: 2026-10-26 (EN)"
date: 2026-10-26
lang: en
---

> From 108 items, 11 important content pieces were selected

---

<section class="cat cat-finance" markdown="1">

## 💹 Finance & Markets (1)

<a id="item-1"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">Anthropic Files S-1 for IPO, Revealing Huge Compute Commitments and Losses</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

Anthropic has publicly filed its S-1 registration statement with the SEC for a proposed initial public offering of Class A common stock. The filing discloses massive multi-year compute commitments, including $114 billion to Google, $110 billion to AWS, $161 billion to Broadcom, and $120 billion to SpaceX, alongside significant losses. This is one of the most consequential AI IPOs to date, potentially valuing Anthropic at up to $2 trillion and testing public-market appetite for a company with enormous fixed obligations. It also sets a transparency precedent for how AI labs disclose compute contracts and risk factors, influencing how investors assess the entire AI infrastructure buildout. The commitments total hundreds of billions of dollars across four suppliers, and even excluding fair-value changes on SAFE instruments, Anthropic reportedly lost roughly $8 billion in the first half of 2026. Community analysis notes that Q3 sales growth was modest and that convertible notes issued to compute suppliers may obscure true compute costs.

🔗 [Source](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm)

hackernews · SiNTEx · Oct 26, 13:04 · [Discussion](https://news.ycombinator.com/item?id=50242939)

**Background**: An S-1 is the registration statement a company files with the SEC before an IPO, disclosing financials, risk factors, and material contracts. Anthropic is an AI safety and research company behind the Claude models, and its compute needs are enormous because training and serving large language models requires massive data-center capacity. Many AI companies now sign long-term compute commitments with cloud providers and chipmakers, which can function like debt even when not recorded as such.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/s1-sec">Anthropic files S-1 with the SEC for proposed initial public ...</a></li>
<li><a href="https://www.investors.com/news/technology/anthropic-ipo-s1-release-ai-claude/">Anthropic IPO Filing Is Here. Here's What Investors Should ...</a></li>
<li><a href="https://presenc.ai/research/ai-compute-commitments-tracker-2026">AI Compute Commitments Tracker 2026 - Presenc AI</a></li>

</ul>
</details>

**Discussion**: Commenters focused on whether AI demand is durable enough to justify Anthropic's enormous commitments, with one noting that if growth continues the company could scale from $50 billion to $500 billion in revenue but that a downturn would hurt badly. Others raised concerns about accounting, including convertible notes to compute suppliers and costs shifted into sales and marketing, and some flagged open-weight models from Chinese labs as an underappreciated competitive risk.

**Tags**: `#Anthropic`, `#S-1`, `#AI`, `#business`, `#finance`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (9)

<a id="item-2"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">OpenAI announces AI-driven discoveries in math, CS, and physics</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

OpenAI announced three new discoveries in mathematics, computer science, and physics: local smoothing and the Kakeya conjecture, the falsity of the Exponential Time Hypothesis, and the existence of quantum chromodynamics and completions of the Standard Model. The company shared model results and invited researchers to verify and build on them. These are long-standing open problems in their fields, and AI producing results on them could significantly accelerate scientific discovery and change how research is conducted. The announcement also sparks debate about the reliability and role of AI in fundamental research. OpenAI describes the manuscripts as a form of raw research data and is experimenting with a new approach to convert this data into scientific understanding. The results are open for verification by the academic community.

🔗 [Source](https://openai.com/index/building-scientific-understanding-with-academic-communities/)

hackernews · OpenAI Blog · Oct 26, 21:35 · [Discussion](https://news.ycombinator.com/item?id=50251344)

**Background**: The Kakeya conjecture concerns the minimum area needed to rotate a needle in the plane and is connected to harmonic analysis. The Exponential Time Hypothesis posits that 3-SAT cannot be solved in subexponential time, and its falsity would have major implications for complexity theory. Quantum chromodynamics is the theory of the strong interaction, and proving its existence is a Millennium Prize Problem.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Quantum_field_theory">Quantum field theory - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/dsa/types-of-complexity-classes-p-np-conp-np-hard-and-np-complete/">P, NP, CoNP, NP hard and NP complete | Complexity Classes</a></li>
<li><a href="https://openai.com/science/">AI for Scientific Research and Discovery | OpenAI</a></li>

</ul>
</details>

**Discussion**: Commenters expressed amazement at the rapid pace of breakthroughs, with some wondering if the falsity of the Exponential Time Hypothesis updates priors toward P=NP. Others discussed whether AI excels in formally verifiable domains due to reinforcement learning and high-quality training data, and questioned the title's framing.

**Tags**: `#AI for science`, `#mathematics`, `#complexity theory`, `#quantum field theory`, `#OpenAI`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">OpenAI Releases GPT-6.1 Terra, a Mid-Tier Frontier Model</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

OpenAI announced GPT-6.1 Terra on October 26, 2026, a fast and efficient mid-tier model that improves on GPT-5.6 Terra with detailed visual reasoning, precise computer use, and more natural writing. It is positioned between the smaller Luna and the larger Sol models in OpenAI's lineup. The release intensifies competition in the mid-tier AI model market, where pricing and reasoning-cost tradeoffs are critical for enterprise adoption. It also highlights OpenAI's strategy of offering multiple tiers to match different task requirements and budgets. Terra is priced at half the cost of Sol, and like previous releases, it appears to follow a 75% price cut trajectory from its predecessor. Community testing showed that 'low' reasoning level sometimes used fewer tokens and cost less than 'none', while 'medium' used 496 reasoning tokens but did not return a visible reasoning trace.

🔗 [Source](https://openai.com/index/introducing-gpt-6-1-terra/)

hackernews · OpenAI Blog · Oct 26, 18:01 · [Discussion](https://news.ycombinator.com/item?id=50248124)

**Background**: OpenAI's model naming uses celestial bodies: Luna (small), Terra (medium), Sol (big), and Astra (bigger). However, overlapping capabilities and discontinuations have caused confusion, such as Sol-6.1 sometimes outperforming Astra and Terra being discontinued then reintroduced. Mid-tier models aim to balance cost and performance for everyday tasks like drafting proposals and interpreting technical drawings.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-6.1">GPT-6.1 - Wikipedia</a></li>
<li><a href="https://openai.com/index/introducing-gpt-6-1-terra/">Introducing GPT-6.1 Terra | OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-6.1-terra">GPT-6.1 Terra Model | OpenAI API</a></li>

</ul>
</details>

**Discussion**: Commenters expressed confusion over OpenAI's model naming and positioning, with some questioning the value of mid-tier models like Terra and Sonnet. They noted that going up a tier with lower reasoning or down a tier with higher reasoning often yields better results, and that Terra seems like a 'weird middle child' between Luna and Sol.

**Tags**: `#openai`, `#llm`, `#model-release`, `#ai-pricing`, `#hackernews`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Sebastian Raschka releases video course on building reasoning models from scratch</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Sebastian Raschka has released a new video course, 'Building Reasoning Models from the Ground Up,' which explains how reasoning models work, covering inference-time scaling, reinforcement learning, and distillation. The course is about 90 minutes long and is accompanied by a book, 'Build a Reasoning Model (From Scratch).' Reasoning models are a rapidly advancing area of AI, and this course provides an accessible, code-first introduction that lowers the barrier to understanding them. It is particularly valuable for developers and learners who want to grasp the internals without committing to a full math-heavy curriculum. The course focuses on the main ideas behind inference-time scaling, reinforcement learning, and distillation, and is designed as a sequel to Raschka's earlier 'Build a Large Language Model (From Scratch)' book. It is available via LinkedIn Learning and Raschka's Substack, and the companion book is published by Manning.

🔗 [Source](https://magazine.sebastianraschka.com/p/building-reasoning-models)

hackernews · sgiannopoulos · Oct 26, 15:11 · [Discussion](https://news.ycombinator.com/item?id=50245138)

**Background**: Reasoning models are large language models trained to solve tasks requiring multiple steps of reasoning, and they tend to outperform standard LLMs on logic, math, and programming tasks. They can revisit and revise earlier steps and benefit from extra computation at inference time. Raschka is a well-known machine learning educator and author of the 'LLMs from Scratch' project, which implements a ChatGPT-like LLM in PyTorch step by step.

<details><summary>References</summary>
<ul>
<li><a href="https://magazine.sebastianraschka.com/p/building-reasoning-models">Build Your Own Reasoning Model : A Full Video Course</a></li>
<li><a href="https://sebastianraschka.com/blog/2026/ai-reasoning-models-course.html">AI Reasoning Models Course | Sebastian Raschka, PhD</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reasoning_model">Reasoning model - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters largely praised Raschka's teaching style, with some recommending his book as highly readable. A key debate centered on the practicality of from-scratch tutorials: one commenter argued that the goal is understanding, not training a useful LLM, while another questioned the compute cost and whether such learning is worth it without a math-degree-level commitment.

**Tags**: `#LLM`, `#reasoning models`, `#education`, `#from-scratch`, `#machine learning`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Microsoft offers mass buyouts to a quarter of its workforce</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Microsoft is offering voluntary buyouts to approximately 60,000 employees, more than a quarter of its global workforce, across four countries. The offer comes six months after the company's first-ever voluntary retirement program and less than a week after Microsoft President Brad Smith publicly stated, 'We stand by our people.' This is one of the largest voluntary workforce reduction programs in tech history, affecting roughly 25% of Microsoft's employees and signaling a major shift in the company's cost structure and talent strategy. It could set a precedent for how large tech firms manage headcount amid AI-driven efficiency pushes, and it puts thousands of employees in a difficult position of choosing between a buyout or risking a layoff. The buyout is voluntary and covers employees across four countries, though specific terms such as severance packages and acceptance deadlines were not detailed in the reports. Employees who decline the offer may face layoffs if not enough people accept, creating a prisoner's dilemma dynamic among colleagues.

🔗 [Source](https://www.seattletimes.com/business/microsoft/microsoft-offers-mass-buyouts-for-roughly-a-quarter-of-its-workforce/)

hackernews · doctorzook · Oct 26, 15:35 · [Discussion](https://news.ycombinator.com/item?id=50245524)

**Background**: A buyout, also known as voluntary severance, is a program where employees receive benefits—typically pay for a period of time—in exchange for agreeing to resign. Companies use buyouts to reduce headcount without forced layoffs, often to cut costs or restructure. Microsoft's move follows a broader trend of tech companies trimming staff while investing heavily in AI infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/10/26/microsoft-msft-voluntary-buyouts.html">Microsoft offers voluntary buyouts as AI leads to efficiency push</a></li>
<li><a href="https://www.geekwire.com/2026/microsoft-makes-new-voluntary-exit-offer-to-more-than-a-quarter-of-its-workforce-including-some-execs/">Microsoft makes new ‘voluntary exit’ offer to about a quarter ...</a></li>
<li><a href="https://www.reuters.com/technology/microsoft-is-offering-buyouts-around-60000-employees-business-insider-reports-2026-10-26/">Microsoft offers buyouts to around 60,000 employees to ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism and concern, with one former Microsoft employee describing unproductive work conditions and constant reorgs, while others highlighted the dilemma of accepting a buyout and competing with many former colleagues for new jobs. Several criticized the timing of the offer relative to Microsoft President Brad Smith's recent 'we stand by our people' statement, and one commenter argued that buyouts tend to drive away the most employable employees.

**Tags**: `#microsoft`, `#layoffs`, `#tech-industry`, `#workforce`, `#corporate-strategy`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">CorridorKey 2.0: Neural Green Screen Keying Tool Released</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

CorridorKey 2.0 is a new version of a neural network-based green screen keying tool developed by Zachary Harris in collaboration with Niko and Corridor Digital. It offers professional-grade keying with time-aware analysis to eliminate flicker and chattering mattes, and is available for free to individuals and organizations with annual revenue under $20 million, with a beta price of $50 or full price of $100 for commercial use. This tool democratizes high-quality green screen removal for independent creators and small studios, potentially disrupting the professional VFX software market by offering comparable results at a fraction of the cost. Its time-aware approach addresses common issues like flicker, making it valuable for video production workflows. CorridorKey 2.0 predicts the color of semi-transparent foreground objects to handle motion blur, bokeh, and hair, and analyzes the entire video rather than individual frames to ensure temporal consistency. Licensing is based on annual revenue, with free use for individuals and small organizations, and paid tiers for larger entities.

🔗 [Source](https://corridorkey.com/)

hackernews · ravenical · Oct 26, 21:18 · [Discussion](https://news.ycombinator.com/item?id=50251127)

**Background**: Green screen keying (chroma keying) is the process of removing a solid color background from video to composite actors or objects into new scenes. Traditional methods rely on color thresholds and often struggle with fine details like hair and motion blur, requiring manual adjustments. Recent advances use neural networks to improve quality and automation, but real-time performance remains challenging.

<details><summary>References</summary>
<ul>
<li><a href="https://corridorkey.com/">CorridorKey 2.0 | Neural Green & Blue Screen Keyer</a></li>
<li><a href="https://github.com/nikopueringer/CorridorKey2.0">GitHub - nikopueringer/CorridorKey2.0: Corridor Key 2.0 for ...</a></li>

</ul>
</details>

**Discussion**: Commenters praised the tool's quality and pricing, with one noting it's a steal for video production work and comparing it favorably to Magnet Mask. Others discussed licensing confusion, clarified that it's free for individuals and small organizations, and expressed hope for real-time performance for live applications.

**Tags**: `#video-editing`, `#green-screen`, `#software-release`, `#licensing`, `#real-time`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Microsoft proposes Type Server Protocol for Python type checkers</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Microsoft published the Type Server Protocol (TSP), a JSON-RPC-based protocol that allows any editor or tool to integrate Python type checkers as first-class backends. TSP extends the Language Server Protocol (LSP) and is documented in the pylance-release repository. TSP aims to standardize how type checkers like Pyright, Pyrefly, and Ty communicate with editors, potentially reducing fragmentation and enabling consistent type analysis across IDEs. This could simplify tooling for Python developers and encourage broader adoption of advanced type checking. TSP is currently Python-specific but may become generic in the future; it defines requests for protocol version, snapshots, search paths, import resolution, and computed/declared/expected types. The protocol is licensed under MIT and is already supported by some tools like Astral's Ty, while others like basedpyright have expressed criticism.

🔗 [Source](https://github.com/microsoft/pylance-release/blob/main/docs/tsp/type-server-protocol.md)

hackernews · adamnemecek · Oct 26, 18:14 · [Discussion](https://news.ycombinator.com/item?id=50248371)

**Background**: The Language Server Protocol (LSP) standardizes communication between editors and language servers, providing features like autocomplete and diagnostics. However, LSP may not fully address the specific needs of type checkers, which require deeper type analysis. TSP builds on LSP to offer a dedicated protocol for type servers, which maintain type-analysis state for a workspace and answer type queries.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/microsoft/pylance-release/blob/main/docs/tsp/type-server-protocol.md">pylance-release/docs/tsp/type-server-protocol.md at main ...</a></li>
<li><a href="https://devblogs.microsoft.com/python/announcing-tsp/">Pylance + Pyrefly: bring your preferred type checker to ...</a></li>

</ul>
</details>

**Discussion**: Commenters debated the generic name 'Type Server Protocol' for a Python-specific protocol, questioned why LSP alone is insufficient, and highlighted fragmentation among Python type checkers (pyright, pylance, basedpyright, pyrefly). Some noted that basedpyright's maintainer has criticized TSP, while Astral's Ty plans to support it.

**Tags**: `#Python`, `#Type Checking`, `#LSP`, `#Developer Tools`, `#Protocols`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Oldest GUI app still running on Windows 11 is 1993's FreeCell</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A blog post by enlyth.com investigates the oldest unmodified GUI application that still runs on Windows 11, finding that FREECELL.EXE dated 22-Feb-1993 from an early Win32s release is fully playable on Windows 11, making it about 33 years and 8 months old. The author also discovered that a 1992 CD player application (CDPLAYER.EXE) runs on Windows 11, though it requires a DLL to emulate a CD-ROM drive for audio playback. This highlights Windows' exceptional backward compatibility, which allows decades-old software to run on modern systems, a key factor in Windows' dominance in enterprise and consumer markets. It also sparks discussion about software preservation and the evolution of GUI design. Windows 11 cannot run 16-bit Windows programs natively because 64-bit Windows lacks NTVDM, so the oldest applications must be 32-bit (Win32) or use compatibility layers. The FreeCell application is from an early Win32s release, which was a subset of the Win32 API for Windows 3.1, and it runs without modification or emulation.

🔗 [Source](https://blog.enlyth.com/posts/oldest-windows-gui-app-win-11/)

hackernews · enlyth · Oct 26, 17:56 · [Discussion](https://news.ycombinator.com/item?id=50248055)

**Background**: Backward compatibility is a core feature of Windows, allowing software written for older versions to continue working on newer ones. Win32s was a technology that allowed 32-bit applications to run on 16-bit Windows 3.1, bridging the gap between 16-bit and 32-bit computing. NTVDM (NT Virtual DOS Machine) is a component in 32-bit Windows that emulates DOS and 16-bit Windows environments, but it is not available in 64-bit versions of Windows.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.enlyth.com/posts/oldest-windows-gui-app-win-11/">Oldest GUI application that still runs on Windows 11</a></li>
<li><a href="https://daily.dev/posts/oldest-gui-application-that-still-runs-on-windows-11-lm1zlzkuw">Oldest GUI application that still runs on Windows 11</a></li>

</ul>
</details>

**Discussion**: Commenters shared nostalgic anecdotes about preserving legacy software, such as keeping a FreeCell score record across upgrades, and criticized modern UI trends like the loss of menu bars and increased reliance on non-native frameworks. Others discussed technical challenges in resurrecting 90s games and referenced a blog post calling Win32 'the only stable ABI'.

**Tags**: `#Windows`, `#backward compatibility`, `#legacy software`, `#GUI`, `#software preservation`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">SIMD-accelerated computer vision on $2 ESP32-S3 microcontroller</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A blog post by Shranav Palakurthi demonstrates using the ESP32-S3's SIMD vector instructions to accelerate FAST corner detection, achieving a 2.2x speedup from 5.1 MP/s to 11.2 MP/s. This shows that even low-cost microcontrollers can handle real-time computer vision tasks, enabling smarter edge devices and TinyML applications without relying on cloud computing. The ESP32-S3's Tensilica Xtensa LX7 core includes 128-bit SIMD instructions that are relatively unknown but well-suited for parallel pixel operations; the FAST algorithm efficiently rejects non-corner points, and the SIMD approach processes multiple pixels simultaneously.

🔗 [Source](https://shraiwi.com/blog/simd-fast-esp32s3/)

hackernews · zdw · Oct 25, 22:29 · [Discussion](https://news.ycombinator.com/item?id=50236681)

**Background**: SIMD (Single Instruction, Multiple Data) is a parallel computing technique that applies one operation to multiple data points simultaneously, commonly used in image processing. FAST (Features from Accelerated Segment Test) is a corner detection algorithm that identifies keypoints by comparing a circle of pixels around a candidate point. The ESP32-S3 is a low-cost microcontroller with Wi-Fi and Bluetooth, popular in IoT and embedded projects.

<details><summary>References</summary>
<ul>
<li><a href="https://www.hackster.io/news/shranav-palakurthi-taps-into-the-espressif-esp32-s3-s-simd-powers-doubles-tinyml-cv-performance-fd4fc92e8402">Shranav Palakurthi Taps into the Espressif ESP 32 - S 3 's SIMD Powers...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Corner_detection">Corner detection - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Single_instruction,_multiple_data">Single instruction , multiple data - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters praised the ESP32-S3's value, noting it is more powerful than vintage PCs like the Amstrad PC1512 and can be bought for as little as $2.80. Some questioned the practical usefulness of corner detection without seeing example outputs, while others pointed to RISC-V alternatives like the CH32V407 that offer more advanced vector extensions.

**Tags**: `#embedded-systems`, `#simd`, `#computer-vision`, `#esp32`, `#microcontrollers`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Leaked Audio: Flock CEO Tells Cops Backlash Isn't Real</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Leaked audio reveals Flock Safety CEO Garrett Langley telling police that public backlash against the company's surveillance cameras is not real and will eventually die down. Langley also acknowledged making mistakes but said he should not have to apologize, according to the recording. The remarks raise concerns about corporate accountability and surveillance ethics, as a major provider of automated license plate readers dismisses public privacy concerns. This could intensify scrutiny from lawmakers and civil liberties groups already questioning police use of Flock's technology. Flock Safety conducts about 20 billion license plate scans per month across the US, and its data is shared among thousands of law enforcement agencies in 49 states. The leaked audio specifically captures Langley dismissing opposition as not real and predicting the debate will eventually subside.

🔗 [Source](https://www.404media.co/in-leaked-audio-flock-ceo-tells-cops-backlash-to-the-company-isnt-real/)

hackernews · Frieren · Oct 26, 17:54 · [Discussion](https://news.ycombinator.com/item?id=50248005)

**Background**: Flock Safety is a company that deploys automated license plate reader (ALPR) cameras, which capture license plate numbers along with location, date, and time, and compare them against databases to generate alerts. ALPR technology has been used by law enforcement for over two decades, but Flock's widespread adoption and data-sharing practices have made it a focal point for privacy advocates. The company has faced reports of misuse by police officers, including one Kansas police chief who used Flock cameras 164 times to track an ex.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnet.com/home/security/when-flock-comes-to-town-how-these-ai-cameras-work-and-what-to-do-about-them/">When Flock Comes to Town: Everything You Should Know... - CNET</a></li>
<li><a href="https://sls.eff.org/technologies/automated-license-plate-readers-alprs">Automated license plate readers - Electronic Frontier Foundation</a></li>
<li><a href="https://apnews.com/article/flock-license-plate-cameras-surveillance-deflock-2a93bc075e2f7ffcca9e04a35d75a3fe">Surveillance tech company Flock announces platform changes ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed sharp criticism, with some noting the historical danger of delegitimizing dissent and others sarcastically suggesting that if the backlash isn't real, people who cut down cameras shouldn't be prosecuted. Several pointed out the irony of a company denying the public's reality being entrusted with privacy-sensitive surveillance technology.

**Tags**: `#surveillance`, `#privacy`, `#corporate-ethics`, `#law-enforcement`, `#community-discussion`

</details>


</section>

<section class="cat cat-other" markdown="1">

## 📌 Other (1)

<a id="item-11"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">EPA Quietly Deletes Online Archive, Raising Data Preservation Concerns</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

The Environmental Protection Agency (EPA) is quietly dismantling its online web archive, which housed historical environmental and climate data, without public announcement. The archive, previously accessible at archive.epa.gov, is no longer being updated and links may not function, according to the EPA's own notice. This removal threatens public access to decades of environmental and climate data, hindering scientific research, transparency, and historical accountability. It reflects a broader trend of government data being taken offline, raising concerns among scientists, journalists, and advocates about the erosion of open environmental information. The EPA's web archive contains materials that may serve as background documents or provide historical perspective, but it is no longer maintained. Community members have pointed to existing preservation efforts, such as the Internet Archive's Wayback Machine and the End of Term Web Archive, which capture federal websites at the end of presidential terms.

🔗 [Source](https://www.motherjones.com/environment/2026/10/epa-online-archive-deletion-zeldin-camp-lejeune-trump-clean-power/)

hackernews · robtherobber · Oct 26, 19:05 · [Discussion](https://news.ycombinator.com/item?id=50249275)

**Background**: Web archiving is the practice of capturing copies of websites to preserve their content, as the web is inherently ephemeral. Government agencies like the EPA are required to maintain records, but changes in policy or administration can lead to the removal or alteration of online information. The End of Term Web Archive is a collaborative project that archives U.S. federal government websites at the end of each presidential term to ensure preservation.

<details><summary>References</summary>
<ul>
<li><a href="https://archive.epa.gov/">Archives | US EPA</a></li>

</ul>
</details>

**Discussion**: Commenters expressed political frustration, with some accusing Republicans of prioritizing short-term profits over science and the environment. Others highlighted preservation efforts, sharing links to the Wayback Machine and the End of Term Web Archive, and asked whether the data had been scraped for offline use. One commenter noted that the EPA had planned to sunset its online archive as early as March 2022.

**Tags**: `#digital-preservation`, `#environmental-data`, `#government-transparency`, `#web-archiving`, `#politics`

</details>


</section>