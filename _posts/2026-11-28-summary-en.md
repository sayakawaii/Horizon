---
layout: default
title: "Horizon Summary: 2026-11-28 (EN)"
date: 2026-11-28
lang: en
---

> From 96 items, 8 important content pieces were selected

---

<section class="cat cat-science" markdown="1">

## 🧪 Science (1)

<a id="item-1"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">ESA's Hera mission returns first close-up images of DART impact site</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

The European Space Agency's Hera mission has returned the first close-up images of the chaotic aftermath of NASA's DART asteroid deflection experiment, showing the impact site on the asteroid Dimorphos. The images reveal a dramatically altered surface, though the spacecraft is not yet approaching closer while the team assesses the potential threat from the debris cloud ejected by the impact. This is the first detailed look at the aftermath of humanity's first successful test of asteroid deflection, a key planetary defense technique. The data will help scientists understand how kinetic impacts reshape small asteroids and refine models for future deflection missions. The Hera spacecraft is currently holding back from approaching the debris cloud, so higher-resolution images will have to wait. The impact site shows unexpected surface changes, highlighting how low-gravity bodies behave counterintuitively compared to Earth-based intuition.

🔗 [Source](https://arstechnica.com/space/2026/11/europes-hera-mission-returns-to-the-chaotic-scene-of-a-cosmic-smashup/)

hackernews · Bender · Nov 26, 17:24 · [Discussion](https://news.ycombinator.com/item?id=50657392)

**Background**: NASA's DART (Double Asteroid Redirection Test) mission intentionally crashed a spacecraft into the moonlet Dimorphos in 2022 to test whether a kinetic impact could change an asteroid's orbit. Dimorphos is about 160 meters wide and orbits the larger asteroid Didymos; neither poses a threat to Earth. ESA's Hera mission, launched in 2024, is a follow-up spacecraft designed to study the aftermath of the impact in detail, including the crater size, mass, and orbital changes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Double_Asteroid_Redirection_Test">Double Asteroid Redirection Test - Wikipedia</a></li>
<li><a href="https://www.planetary.org/space-missions/hera">Hera , ESA ’s asteroid investigator | The Planetary Society</a></li>
<li><a href="https://science.nasa.gov/planetary-defense-dart/">Planetary Defense - DART - NASA Science</a></li>

</ul>
</details>

**Discussion**: Commenters expressed confusion over the counterintuitive behavior of low-gravity bodies, with one asking why the physics can't be simulated. Others questioned why an observation satellite wasn't launched with DART and noted difficulty in distinguishing the crater in the images.

**Tags**: `#space`, `#asteroid-deflection`, `#science`, `#esa-hera`, `#planetary-defense`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (7)

<a id="item-2"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Convex skill plugin accused of uploading user app ideas without consent</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A GitHub issue on the convex-backend-skill repository alleges that Convex's skill plugin uploads users' app ideas to a remote server without informing them. Convex CEO Jamie responded, clarifying that the upload powers the Convex 'quickstart' feature and that the related Convex Chef product was recently shut down. This incident highlights growing privacy and trust concerns in AI-assisted developer tools, where prompts containing proprietary ideas may be sent to external servers by default. It could push developers toward self-hosted or open-weight models and prompt tool vendors to be more transparent about data handling. The plugin is part of Convex's official skills for coding agents, which let developers describe an app in one sentence and have the agent scaffold it. The controversy also touches on prompt injection risks, as community members noted that injected prompts are more common than models making malicious tool calls on their own.

🔗 [Source](https://github.com/convex/convex-backend-skill/issues/64)

hackernews · MickyTheMouse · Nov 27, 18:02 · [Discussion](https://news.ycombinator.com/item?id=50669765)

**Background**: Convex is a full-stack development platform that stores application data and code and offers an AI gateway for building software. Its skill plugins integrate with coding agents to streamline app creation. Prompt injection is a security exploit where crafted inputs cause LLMs to follow unintended instructions, and it is a known risk in AI tooling.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>

</ul>
</details>

**Discussion**: The discussion reflects diverse views: the CEO clarified the upload's purpose, some commenters argued for self-hosted open-weight models as a long-term solution, and others downplayed the issue by saying 'ideas are cheap.' One user also questioned the author's promotion of a personal media page in the comments.

**Tags**: `#privacy`, `#AI-tools`, `#prompt-injection`, `#developer-tools`, `#data-handling`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Google's DeepCrossAttention speeds transformer training up to 3x</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Google Research introduced DeepCrossAttention (DCA), a technique that enhances transformer residual connections by using learnable weights and depth-wise cross-attention to dynamically combine outputs from previous layers. This approach prevents information dilution in traditional residual connections and achieves comparable model quality up to 3x faster. Faster training with comparable quality could significantly reduce the computational cost and time required to develop large language models, making AI research and deployment more accessible and sustainable. This is particularly relevant as model sizes continue to grow and efficiency becomes a critical bottleneck. DCA generalizes self-attention by adding three independent instances of a Gated Residual Network (GRN) in each decoder block, with the GRN considered to be GRN-v3. The method is detailed in a paper (arXiv:2502.06785) from 2025, and the technique is part of a broader trend of applying attention-like primitives depthwise in transformers.

🔗 [Source](https://research.google/blog/supercharging-transformer-residual-connections/)

hackernews · ComputedCamp995 · Nov 27, 23:06 · [Discussion](https://news.ycombinator.com/item?id=50672565)

**Background**: Transformer models rely on residual connections (skip connections) to enable deep networks by mitigating the vanishing gradient problem. Traditional residual connections simply add the output of a layer to its input, but as networks deepen, this can lead to information dilution. DeepCrossAttention replaces this simple addition with a learned, input-dependent combination of previous layer outputs, similar to attention mechanisms but applied across depth rather than sequence.

<details><summary>References</summary>
<ul>
<li><a href="https://research.google/blog/supercharging-transformer-residual-connections/">Supercharging transformer residual connections - Google Research</a></li>
<li><a href="https://arxiv.org/html/2502.06785">DeepCrossAttention : Supercharging Transformer Residual Connections</a></li>
<li><a href="https://www.baeldung.com/cs/transformer-networks-residual-connections">Why Are Residual Connections Important in Transformer ...</a></li>

</ul>
</details>

**Discussion**: Commenters noted the technique's potential for further speedups, with one mentioning 10x token/sec gains from related methods and wondering about 30x. Others pointed out the paper is from 2025 and discussed related work like AttnRes, suggesting that combining DCA with looping layers could yield additional gains. Some also speculated about its impact on commercial models like Gemini.

**Tags**: `#transformers`, `#attention mechanisms`, `#model efficiency`, `#Google Research`, `#deep learning`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">WebRTC-based credit card skimmers found on popular shopping sites</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Security researchers discovered credit card skimming scripts that use WebRTC data channels to exfiltrate stolen payment data on the online stores of Lascana, Samsonite, American Tourister, Revolve, and FWRD in the week before Black Friday. All affected sites took action after being contacted, but the incident highlights a new attack vector that bypasses traditional defenses. This attack is significant because WebRTC data channels operate outside the connect-src directive of Content Security Policy (CSP), meaning even sites with strict CSP that block unauthorized HTTP connections remain vulnerable. It underscores the risks of embedding third-party scripts and may push e-commerce sites to re-evaluate their security posture and ad-blocking strategies. The skimmer's steps 5 to 7 run over the WebRTC data channel, but step 4 is an ordinary web request that connect-src can block; without those two requests the skimmer never loads. The attackers also targeted only mobile devices to make detection harder, and the use of WebRTC marks a significant evolution in skimmer attacks.

🔗 [Source](https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer)

hackernews · scanr · Nov 27, 15:40 · [Discussion](https://news.ycombinator.com/item?id=50668145)

**Background**: WebRTC (Web Real-Time Communication) is a browser technology that enables peer-to-peer real-time communication for audio, video, and data. Content Security Policy (CSP) is a security standard that helps prevent cross-site scripting and other code injection attacks by restricting the sources from which resources can be loaded. Credit card skimming scripts are malicious JavaScript injected into checkout pages to steal payment card details, often through compromised third-party scripts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer">Credit card skimming scripts using WebRTC found on popular ...</a></li>
<li><a href="https://thehackernews.com/2026/03/webrtc-skimmer-bypasses-csp-to-steal.html">WebRTC Skimmer Bypasses CSP to Steal Payment Data from E ...</a></li>
<li><a href="https://daily.dev/posts/credit-card-skimming-scripts-using-webrtc-found-on-popular-shopping-sites-mr8zgdbaf">Credit card skimming scripts using WebRTC found on...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong support for ad blocking as a defense, criticized the web's model of allowing third-party code execution, and questioned why ad providers don't sandbox ads to prevent JavaScript execution. Some noted that the issue isn't WebRTC's technical capabilities but its lack of monitoring, and others argued for using asymmetric cryptography in payments to avoid symmetric secrets.

**Tags**: `#security`, `#web`, `#WebRTC`, `#skimming`, `#privacy`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">State AGs sue SpaceX/xAI over Grok generating child sexual abuse material</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Virginia Attorney General Jay Jones and another state attorney general filed a lawsuit against SpaceX, the parent company of xAI and X, alleging that the Grok AI chatbot generated child sexual abuse material (CSAM) and non-consensual intimate imagery (revenge porn). The suit claims the platform created and promoted such content, marking a high-profile legal action against a major AI company over safety failures. This lawsuit could set a precedent for holding AI companies liable for harmful content generated by their models, testing the boundaries of legal protections like Section 230. It signals increasing scrutiny from state regulators over AI safety and content moderation, potentially leading to stricter compliance requirements for generative AI platforms. The lawsuit specifically targets SpaceX as the parent company of xAI and X, arguing that Grok's ability to produce CSAM and revenge porn violates laws against child exploitation and non-consensual imagery. The legal action comes amid a surge in AI-generated CSAM reports, with one NGO noting an 8,400% increase in such material.

🔗 [Source](https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform)

hackernews · DeepLogin · Nov 27, 19:42 · [Discussion](https://news.ycombinator.com/item?id=50670855)

**Background**: Grok is an AI chatbot developed by xAI, which is owned by SpaceX, and integrated into the X platform. Section 230 of the Communications Decency Act generally shields online platforms from liability for user-generated content, but its application to AI-generated content is legally untested. AI-generated CSAM is a growing concern, with reports of such material rising sharply as generative AI tools become more accessible.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2510.02978">AI Generated Child Sexual Abuse Material - What's the Harm?</a></li>
<li><a href="https://www.theguardian.com/technology/2026/nov/16/ai-related-child-sexual-abuse-material-rise-exploitation-deepfakes">Reports of AI-related child sexual abuse material rise 8,400% ...</a></li>
<li><a href="https://businesslawreview.uchicago.edu/print-archive/generative-ai-meets-section-230-future-liability-and-its-implications-startup">Generative AI Meets Section 230: The Future of Liability and ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed confusion over how Grok was able to generate such content, questioning whether it was easily accessible or required tricking the model. Some raised concerns about user accountability, while others highlighted the risk of linking a Twitter account to access Grok, suggesting that this requirement might deter abuse but also raises privacy issues.

**Tags**: `#AI safety`, `#content moderation`, `#legal`, `#xAI`, `#Grok`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">djb Argues Computer-Checked Proofs Can Be False; HN Pushes Back</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Daniel J. Bernstein (djb) published an article arguing that computer-checked proofs can be false due to soundness bugs in proof checkers. The piece sparked a Hacker News discussion where practitioners clarified that multi-verifier systems and informal review make such failures far less consequential than the article implies. This debate matters because formal verification is increasingly used in safety-critical software and mathematics, and overstating the risk of soundness bugs could undermine trust in proof assistants like Lean and Metamath. Conversely, understanding the real limitations helps the community prioritize high-assurance work without alarmism. Commenters noted that Metamath's main databases require proofs to pass five independently-created verifiers in different programming languages, and that all known soundness bugs in these systems could fit in a tweet. They also emphasized that a soundness bug must be exploited in a way that hides a further issue in the program being verified to actually cause harm.

🔗 [Source](https://cr.yp.to/proofs/falseccp.html)

hackernews · _tk_ · Nov 27, 15:26 · [Discussion](https://news.ycombinator.com/item?id=50667989)

**Background**: Proof assistants such as Lean and Metamath are software tools that let mathematicians and engineers write proofs in a formal language and have them mechanically checked by a small trusted kernel. A soundness bug is a flaw in that kernel that allows a false statement to be accepted as proven. Because the kernel is small, it is considered highly trustworthy, but it is not infallible.

<details><summary>References</summary>
<ul>
<li><a href="https://essamamdani.com/blog/lean-4-soundness-bug-14576-postmortem">Lean 4 Soundness Bug #14576: What Broke the Kernel | Essa Mamdani</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proof_assistant">Proof assistant - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion generally pushed back on the article's framing, with knowledgeable commenters (including Metamath and Lean practitioners) arguing that multi-verifier systems and informal review make soundness bugs far less dangerous than implied. Some acknowledged the value of high-assurance work but stressed that existing systems are already good enough for the vast majority of use cases.

**Tags**: `#formal-verification`, `#proof-assistants`, `#Lean`, `#Metamath`, `#soundness`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Hugging Face shows video generation with LTX-2.5 on AWS Trainium3</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Hugging Face published a blog post detailing how to generate videos using the LTX-2.5 model on AWS Trainium3 hardware. The post provides a technical walkthrough for running the open-source video generation model on Amazon's custom AI accelerator. This demonstrates that video generation models can run on alternative AI accelerators beyond Nvidia GPUs, potentially offering cost and supply chain benefits for practitioners. It signals growing ecosystem support for AWS Trainium in the generative AI space. LTX-2.5 is an open-weights video generation model built on a diffusion transformer architecture, featuring native multishot generation and a custom Gemma 4 12B text encoder. Trainium3 is AWS's 3-nanometer AI chip, available in UltraServer systems.

🔗 [Source](https://huggingface.co/blog/video-trainium3)

rss · Hugging Face Blog · Nov 27, 00:00

**Background**: AWS Trainium is a family of custom AI chips designed by Amazon's Annapurna Labs to provide cost-effective alternatives to Nvidia GPUs for training and inference. LTX-2.5 is an open-source video generation model from Lightricks that uses diffusion transformer techniques to create videos from text prompts. Hugging Face is a popular platform for sharing and deploying machine learning models, and its blog often provides practical guides for running models on various hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AWS_Trainium">AWS Trainium</a></li>
<li><a href="https://zoombangla.com/blog/2025/12/03/aws-unveils-trainium3-amazons-power-play-in-the-ai-chip-race/">AWS Unveils Trainium 3 : Amazon ’s Power Play in the... - ZoomBangla</a></li>
<li><a href="https://huggingface.co/tasks/text-to-video">What is Text-to- Video ? - Hugging Face</a></li>

</ul>
</details>

**Tags**: `#video-generation`, `#AWS Trainium`, `#LTX-2.5`, `#AI hardware`, `#Hugging Face`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">NVIDIA Nemotron 3.5 Parse: Open Data, Fine-Tuning, and Faster Inference Guide</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

Hugging Face and NVIDIA published a practical guide on building with NVIDIA's Nemotron 3.5 Parse, a compact document model that converts page images into structured data for retrieval-augmented generation (RAG) and agents. The guide covers open data, fine-tuning strategies, and inference speed optimizations. This guide helps practitioners efficiently deploy and customize a document-understanding model for RAG pipelines and agentic workflows, potentially lowering the barrier to building production-grade document AI systems. It reflects the growing trend of open, fine-tunable models accompanied by end-to-end optimization recipes. Nemotron 3.5 Parse is designed to extract text and metadata from images, and the guide emphasizes open data availability, fine-tuning approaches, and techniques to speed up inference. However, specific benchmarks, model size, and licensing details are not provided in the summary.

🔗 [Source](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin)

rss · Hugging Face Blog · Nov 26, 05:05

**Background**: Nemotron is NVIDIA's family of open models; Nemotron 3.5 Parse is a vision-language model specialized for document parsing, turning page images into structured outputs. Fine-tuning adapts a pre-trained model to a specific domain or task using additional data, while inference optimization techniques (e.g., quantization, speculative decoding) reduce latency and cost. RAG combines retrieval with generation to ground LLM outputs in external knowledge, and agents are LLM-driven systems that perform tasks autonomously.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin">Building on Nemotron 3 . 5 Parse : Open Data, Fine-Tuning, and Faster...</a></li>
<li><a href="https://build.nvidia.com/models">Models | Try NVIDIA NIM APIs</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#fine-tuning`, `#inference optimization`, `#open data`, `#NVIDIA`

</details>


</section>