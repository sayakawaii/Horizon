---
layout: default
title: "Horizon Summary: 2026-11-26 (EN)"
date: 2026-11-26
lang: en
---

> From 116 items, 16 important content pieces were selected

---

<section class="cat cat-science" markdown="1">

## 🧪 Science (1)

<a id="item-1"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Polynomial Hirsch Conjecture Disproved by New Preprint</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A new preprint posted on OpenAI's math repository proves that the polynomial Hirsch conjecture is false, demonstrating that simple polytopes can have superpolynomial graph diameter. This result rules out the existence of a polynomial-time simplex algorithm, impacting the theoretical understanding of linear programming and the simplex method's worst-case behavior. The proof shows that for simple polytopes, the graph diameter can grow faster than any polynomial in the number of facets, but it remains open whether the proof is constructive and whether it has practical implications for simplex variants.

🔗 [Source](https://github.com/openai/math/blob/main/preprints/Superpolynomial-graph-diameter-of-simple-polytopes-November-24-2026/paper.pdf)

hackernews · acossta · Nov 25, 17:34 · [Discussion](https://news.ycombinator.com/item?id=50644980)

**Background**: The Hirsch conjecture, proposed in 1957, stated that the diameter of a polytope with n facets in d dimensions is at most n-d. It was disproved in 2010 by Francisco Santos, but the polynomial version, which posits a polynomial upper bound, remained open until now. The simplex method, widely used for linear programming, relies on the polytope diameter for its worst-case analysis.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Polynomial_Hirsch_conjecture">Polynomial Hirsch conjecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hirsch_conjecture">Hirsch conjecture - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Simplex_algorithm">Simplex algorithm - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters clarified that this is a follow-up to the 2010 disproof of the original Hirsch conjecture and noted that it implies no polynomial-time simplex algorithm. Some asked whether the proof is constructive, while others discussed broader implications for complexity theory.

**Tags**: `#mathematics`, `#linear-programming`, `#complexity-theory`, `#polytopes`, `#research`

</details>


</section>

<section class="cat cat-tech" markdown="1">

## 🔬 Tech & AI (15)

<a id="item-2"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">Scott Aaronson Stunned by AI Math Breakthrough: Matrix Multiplication Exponent Is 9/4</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

Scott Aaronson published a blog post expressing astonishment at a major AI-driven breakthrough in mathematics, specifically the result that the matrix multiplication exponent is exactly 9/4 over every field, which refutes a long-standing conjecture. The post, titled with repeated expletives, sparked intense community debate about the implications of AI for mathematical research. This breakthrough, part of what Aaronson calls the 'mathocalypse,' demonstrates AI's growing ability to solve open problems in mathematics, potentially transforming how mathematical research is conducted and raising questions about AI's broader capabilities. The result itself is significant for theoretical computer science, as the matrix multiplication exponent determines the asymptotic complexity of one of the most fundamental computational operations. The paper, reportedly from OpenAI, gives the exact exponent 9/4 over every field, a quarter-power above the previous lower bound of 2, and Aaronson noted that no AI result with a Lean certificate has been retracted, lending credibility to the proof. The work was produced by a single experimental model using one prompt for each problem, according to available information.

🔗 [Source](https://scottaaronson.blog/?p=10379)

hackernews · Kotlopou · Nov 25, 19:11 · [Discussion](https://news.ycombinator.com/item?id=50646108)

**Background**: The matrix multiplication exponent, denoted omega, is the smallest number such that two n-by-n matrices can be multiplied in O(n^omega) time; the naive algorithm gives omega=3, and decades of work reduced it to about 2.37, with a long-standing conjecture that omega=2. Scott Aaronson is a prominent theoretical computer scientist at UT Austin and a leading blogger on quantum computing and AI. OpenAI recently released a large batch of mathematical papers solved by AI, an event Aaronson dubbed the 'mathocalypse,' which has fueled debate about AI's role in mathematics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_bulk_release_of_mathematical_papers">OpenAI bulk release of mathematical papers - Wikipedia</a></li>
<li><a href="https://www.youtube.com/watch?v=5dEK4lFa3gs">OpenAI Just Solved 370 Major Math Problems | Scott Aaronson Mathocalypse! Scott Aaronson on OpenAI's flood of AI math ... OpenAI bulk release of mathematical papers - Wikipedia Shtetl-Optimized AI is causing a ‘mathocalypse’ that could break the internet Did AI Just Help Solve A 167-Year-Old Math Problem? Here’s ... The 'mathpocalypse': Why AI's maths breakthrough has experts ...</a></li>
<li><a href="https://www.youtube.com/watch?v=StluAE0HQOM">Mathocalypse! Scott Aaronson on OpenAI's flood of AI math ... OpenAI bulk release of mathematical papers - Wikipedia Shtetl-Optimized AI is causing a ‘mathocalypse’ that could break the internet Did AI Just Help Solve A 167-Year-Old Math Problem? Here’s ... The 'mathpocalypse': Why AI's maths breakthrough has experts ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed a mix of awe and skepticism: some argued that humans are biologically incapable of appreciating the magnitude of change, while others cautioned that AI's success in axiomatic math does not imply it will solve other fields or pose existential risks. Some also questioned how much of the breakthrough would have been possible with just Lean, MathLib, and computing power without LLMs, suggesting the timing may be tied to corporate compute subsidies.

**Tags**: `#AI`, `#mathematics`, `#research breakthrough`, `#Scott Aaronson`, `#community discussion`

</details>


<a id="item-3"></a>
<details class="hz-item" data-score="9.0" markdown="1">
<summary><span class="hz-item-title">GPT-6 models demonstrate intrinsic protein-design capabilities</span> <span class="hz-item-score">⭐️ 9.0/10</span></summary>

OpenAI announced that its GPT-6 models can design protein structures and sequences using reasoning and code, without specialized protein-design tools. In laboratory tests conducted by partner Onava, 35 of 322 minibinders designed by GPT-6.2 successfully bound their intended targets, achieving a hit rate of 10.9% across five targets. This marks a significant step toward general-purpose AI models performing complex scientific design tasks, potentially democratizing protein engineering and accelerating drug discovery. It suggests that large language models can develop intrinsic scientific reasoning capabilities that rival specialized systems like AlphaFold. The results are from a preprint that has not yet been peer-reviewed, and the 10.9% hit rate, while promising, indicates room for improvement compared to established computational methods. The designs were validated experimentally by Onava, but details on the specific targets and binding affinities are not yet disclosed.

🔗 [Source](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities)

rss · OpenAI Blog · Nov 24, 13:00

**Background**: Protein design involves creating new proteins with specific functions, such as binding to targets for therapeutic purposes. Traditionally, this requires specialized computational tools and deep domain expertise. AI models like AlphaFold have revolutionized protein structure prediction, but designing novel proteins from scratch remains challenging. GPT-6's ability to use reasoning and code to design proteins suggests a more general approach that could be applied to other scientific domains.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/">GPT-6 models demonstrate intrinsic protein-design ... - OpenAI</a></li>
<li><a href="https://www.cryptopolitan.com/gpt-6-models-design-proteins-reasoning-code/">GPT-6 models design proteins using only reasoning and code</a></li>
<li><a href="https://en.wikipedia.org/wiki/Protein_structure_prediction">Protein structure prediction - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#protein design`, `#GPT-6`, `#biotechnology`, `#OpenAI`

</details>


<a id="item-4"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">1Password Discloses Security Incident Involving Compromised Employee Laptop</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

1Password disclosed a security incident in which an attacker compromised an employee laptop, used the account to access source code, and pushed malicious code to backend services that downloaded administrative data including customer names and email addresses. The company stated that customer vaults were not accessed and remain secure. This incident highlights the critical risk of supply-chain and CI/CD compromise for SaaS companies, where a single compromised employee laptop can lead to malicious code being deployed to production. For a password manager, such a breach undermines trust in the fundamental security of cloud-based vaults and raises questions about branch protection and code review safeguards. The attacker used the compromised employee account to access source code and push malicious code to backend services, which then downloaded administrative data including customer names, email addresses, and non-secret internal metadata. 1Password did not clarify whether branch protection rules were missing or bypassed, and did not explicitly state that encrypted vaults were not downloaded.

🔗 [Source](https://1password.com/blog/update-on-nov-2026-security-incident)

hackernews · lxhrstn · Nov 25, 17:18 · [Discussion](https://news.ycombinator.com/item?id=50644817)

**Background**: 1Password is a widely used password manager that stores user credentials in encrypted vaults, either locally or in the cloud. In a typical SaaS supply-chain attack, attackers compromise an employee's device or credentials to gain access to source code repositories and CI/CD pipelines, allowing them to inject malicious code into production services. Branch protection rules and mandatory code reviews are standard defenses to prevent unauthorized code pushes to main branches.

<details><summary>References</summary>
<ul>
<li><a href="https://1password.com/blog/update-on-nov-2026-security-incident">Update on a security incident involving 1Password’s backend ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=50645961">> push malicious code to backend services This is a huge red...</a></li>

</ul>
</details>

**Discussion**: Commenters like tptacek emphasized that compromised employee laptops are the single most important attack vector for SaaS companies, with the likelihood approaching 1 as employee count grows. ctidd criticized the announcement for not addressing whether branch protection rules were missing or bypassed, while others raised concerns about passkey implementations and the lack of explicit confirmation that encrypted vaults were not downloaded.

**Tags**: `#security`, `#supply-chain`, `#saas`, `#password-manager`, `#incident-response`

</details>


<a id="item-5"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Lean verification of GRH shrinks from 17M to 76k lines</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A much shorter and more readable Lean formalization of the Generalized Riemann Hypothesis (GRH) has been released, reducing the proof from approximately 17 million lines to about 76,000 lines. The new version includes clear documentation and explicitly separates known mathematics from new mathematics, making it far easier to digest. This dramatic reduction (over 99% smaller) addresses concerns that huge, opaque formal proofs provide little insight, and it demonstrates how LLM-assisted proof golfing can produce more human-readable formalizations. It could significantly lower the barrier for mathematicians to review and build upon machine-generated proofs. The reduction from ~17M to ~76k lines represents a 99.56% decrease, and the proof includes human-readable documentation throughout. A Zulip discussion and a tool called 'slim' are available to navigate the Lean source without setting up Lean locally.

🔗 [Source](https://github.com/lsernau/grh-lean)

hackernews · nb-t · Nov 25, 21:48 · [Discussion](https://news.ycombinator.com/item?id=50648050)

**Background**: The Generalized Riemann Hypothesis is a major unsolved conjecture in number theory concerning the zeros of Dirichlet L-functions, generalizing the classical Riemann Hypothesis. Lean is an interactive theorem prover used to formalize mathematical proofs and verify their correctness. Recent advances in large language models have enabled autoformalization, where AI assists in translating informal proofs into formal code, but such proofs can become extremely long and hard to understand.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis">Generalized Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://leanprover.github.io/theorem_proving_in_lean/introduction.html">1. Introduction — Theorem Proving in Lean 3 (outdated)...</a></li>
<li><a href="https://arxiv.org/html/2505.23486v1">Autoformalization in the Era of Large Language Models: A Survey</a></li>

</ul>
</details>

**Discussion**: Commenters praised the readability and the known-vs-new math split, with one noting the 99.56% reduction. Some discussed whether this addresses Terence Tao's earlier concern about huge proofs lacking insight, and whether smarter LLMs can now golf and explain proofs. A link to a Zulip discussion and a tool for navigating the Lean source were also shared.

**Tags**: `#Lean`, `#formal verification`, `#mathematics`, `#GRH`, `#LLM-assisted proofs`

</details>


<a id="item-6"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Google Research publishes Cogentic papers on integer factorization and discrete logs</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

Google Research has published a collection of 'Cogentic' research papers in its public GitHub repository, covering topics such as integer factorization, discrete logarithms, and edge reconstruction. The release has drawn intense attention on Hacker News, where the item reached 449 points and 336 comments. Integer factorization and discrete logarithms underpin widely used public-key cryptosystems like RSA and Diffie-Hellman, so any credible research progress in these areas could have major implications for cryptographic security. The release also fuels the broader debate about whether AI-driven methods are accelerating breakthroughs in pure mathematics. The GitHub directory contains individual paper PDFs, such as one on edge reconstruction, but the repository itself provides no summary or detailed analysis of the results. Community members caution that the papers may reflect a trend of splitting results into multiple publications, and rumors of larger implications remain unverified.

🔗 [Source](https://github.com/google-research/google-research/tree/master/cogentic_research_papers)

hackernews · rgwohlbold · Nov 25, 13:33 · [Discussion](https://news.ycombinator.com/item?id=50642086)

**Background**: Integer factorization is the decomposition of a number into its prime factors, and the difficulty of factoring large integers is what secures RSA encryption. The discrete logarithm problem is similarly hard to solve in general and forms the security basis for Diffie-Hellman and ElGamal key exchange. Google Research regularly publishes papers across computer science and AI, and its GitHub repository hosts many of these public artifacts.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50642086">Google releases Cogentic papers on integer... | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Integer_factorization">Integer factorization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Discrete_logarithm">Discrete logarithm - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters cited credible rumors that this release is 'the tip of something bigger,' and compared recent math discoveries to AlphaGo's search-based breakthroughs. Others debated the market's lukewarm reaction to daily breakthroughs and noted a shift in belief that money and compute can now solve hard mathematical problems.

**Tags**: `#cryptography`, `#integer-factorization`, `#discrete-log`, `#google-research`, `#AI-for-math`

</details>


<a id="item-7"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Rockbox ported to $9 undocumented AliExpress MP3 player using LLMs</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

A developer used large language models to reverse-engineer and port Rockbox, the open-source replacement firmware, to a $9 undocumented 'YP3' MP3 player sold on AliExpress. The project demonstrates a new LLM-assisted approach to embedded development on cheap, undocumented hardware. This shows how LLMs can lower the barrier to reverse engineering and firmware porting, potentially enabling hobbyists to revive ultra-cheap consumer hardware that would otherwise be locked to poor stock software. It could accelerate a wave of custom firmware projects for low-cost devices. The player is described as weighing 28g with a slim form factor, a large color screen, USB-C, and Bluetooth, and the author notes having several more sub-$20 players running Rockbox since the post. The port relied on LLMs to help understand undocumented hardware, though specific technical limitations of the port are not detailed in the provided content.

🔗 [Source](https://jayd.ml/2026/11/14/rockbox-on-yp3.html)

hackernews · jaydenmilne · Nov 24, 06:22 · [Discussion](https://news.ycombinator.com/item?id=50624446)

**Background**: Rockbox is a free, open-source replacement firmware for digital audio players that provides features beyond the original OEM firmware. Reverse engineering embedded systems traditionally requires deep expertise in low-level programming and hardware analysis, but recent research explores using LLMs to assist with tasks like decompilation and semantic recovery. The 'YP3' is an inexpensive, undocumented MP3 player from AliExpress, meaning no public technical documentation or SDK is available for it.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vn-os/reverser_ai_reverse-engineering-with-LLM">GitHub - vn-os/reverser_ai_reverse-engineering-with-LLM ...</a></li>
<li><a href="https://arxiv.org/html/2509.21821v2">Potential and Challenges of Large Language Models for Reverse ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed enthusiasm for the project, with some sharing related custom firmware efforts for other cheap players like Snowsky and describing their own experiments using LLMs to program low-cost dev kits. Several noted that ultra-cheap hardware is often more capable than its stock software suggests, and the author mentioned having multiple additional sub-$20 players running Rockbox.

**Tags**: `#Rockbox`, `#embedded systems`, `#reverse engineering`, `#LLM`, `#hardware hacking`

</details>


<a id="item-8"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">Simon Willison identifies three LLM inflection points in twelve months</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

In a keynote at the AI Engineer Code Summit, Simon Willison argued that LLM and coding-agent capabilities hit three major inflection points in the past twelve months, anchored by the one-year anniversary of Claude Opus 4.5 on November 24, 2026. He highlighted Opus 4.5's release as the first model that made Claude Code reliably useful by default, and later introduced the concept of 'Fable class models' that can solve problems with brute force when given a goal and tools. This retrospective from a highly credible practitioner offers a framework for understanding how quickly AI coding tools have matured, helping developers and companies calibrate expectations for agent reliability and adoption. It also signals that model releases like Opus 4.5 and the later Fable class have shifted coding agents from experimental aids to dependable productivity tools. Willison notes that Claude Code was only nine months old when Opus 4.5 launched, and that OpenAI's GPT-5.1 family (Instant, Thinking, Codex, Codex-Max) released around the same time made Codex reliably useful too. He defines Fable class models as those that, given a definable goal and necessary tools, can solve problems through brute force—exemplified by Claude Fable 5 spinning up its own pyobjc-framework-Quartz screenshot mechanism and a CORS-enabled localhost logging server to debug a Safari display glitch.

🔗 [Source](https://simonwillison.net/2026/Nov/24/llm-inflection-points/)

rss · Simon Willison · Nov 24, 23:02

**Background**: Claude Opus 4.5 is Anthropic's flagship large language model released on November 24, 2025, featuring state-of-the-art coding and agentic performance at lower pricing. Claude Code is Anthropic's terminal-based coding agent, introduced alongside Claude 3.7 Sonnet in February 2025, which acts as a harness that extends an LLM with tools and context to perform software engineering tasks. The AI Engineer Code Summit, held November 10–12, 2026 in San Francisco, gathers coding-agent builders and AI engineers to share breakthroughs in AI coding.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-opus-4-5">Introducing Claude Opus 4.5 - anthropic.com</a></li>
<li><a href="https://ai.engineer/code/2026">AI Engineer Code Summit 2026 Recordings: AI Engineering ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Opus_4.5">Claude Opus 4.5</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#coding-agents`, `#AI`, `#Claude`, `#industry-analysis`

</details>


<a id="item-9"></a>
<details class="hz-item" data-score="8.0" markdown="1">
<summary><span class="hz-item-title">GPT-6.2 Astra Solves 1808 Sketchbook Mystery in 22 Minutes</span> <span class="hz-item-score">⭐️ 8.0/10</span></summary>

History professor Mark Humphries reports that GPT-6.2 Astra, with minimal prompting, autonomously identified the creator of an anonymous 1808 sketchbook held at Yale's Beinecke Library in just 22 minutes using public sources. The model found a diary reference to a visit by the vicomte de Chabot and predicted that Chabot's travel journal, available only by order from Cleveland State University, would confirm the sketchbook was his work—a prediction that proved correct. This case study demonstrates that large language models can perform autonomous historical research, discovering a little-known archival source and formulating a testable hypothesis that led to a significant new find for Canadian and fur trade historians. It suggests AI could reshape research workflows in the humanities, much as it has begun to affect mathematics and other fields. The model located a diary reference to a visit by the vicomte de Chabot dated five days before a date mentioned in the sketchbook at a nearby river, then suggested that Chabot's journal—only available by order from Cleveland State University—might confirm the attribution. The sketchbook itself has been digitized and is available through Yale's online collections.

🔗 [Source](https://simonwillison.net/2026/Nov/24/astra-historical-mystery/)

rss · Simon Willison · Nov 24, 16:53

**Background**: The Beinecke Rare Book and Manuscript Library at Yale is one of the world's largest repositories of rare books and manuscripts, holding extensive special collections. In historical research, primary sources are original documents from the period under study, while secondary sources interpret or analyze them; AI models can now search and cross-reference both types at scale. GPT-6.2 Astra is a large language model released by OpenAI on November 17, 2026, designed for multi-step reasoning and document analysis.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Beinecke_Rare_Book_and_Manuscript_Library">Beinecke Rare Book and Manuscript Library - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6.2_Astra">GPT-6.2 Astra</a></li>
<li><a href="https://history.ucla.edu/primary-secondary-sources/">Primary & Secondary Sources - UCLA Department of History</a></li>

</ul>
</details>

**Discussion**: Commentary shared by Simon Willison highlights the case as a compelling example of AI's real-world research capability beyond typical benchmarks, though it remains a single anecdote rather than a peer-reviewed breakthrough. Mark Humphries predicts a mild 'crisis of confidence' for historians, similar to but less profound than mathematics' encounter with AI, because history embraces reinterpretation and humanistic writing rather than a single universal truth.

**Tags**: `#AI`, `#LLM`, `#historical research`, `#case study`, `#GPT-6.2 Astra`

</details>


<a id="item-10"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Ubuntu's slow security patching prompts users to switch to Debian</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A discussion on the oss-security mailing list highlights Ubuntu's slow response to severe security flaws, with users citing the recent NoisyTCP (CVE-2026-99288) remote memory corruption in the Linux kernel's TCP stack as an example. Some organizations have already migrated their server images from Ubuntu to Debian due to these delays. Ubuntu is one of the most widely used Linux distributions for servers and cloud workloads, so slow security turnaround can leave many production systems exposed to known vulnerabilities. The trend of users migrating to Debian could erode Ubuntu's position as the default choice for generic Linux VMs. Commenters note that security fixes sometimes appear in the -updates repository hours before reaching the security repository, complicating unattended security-only upgrades. Others point out that Debian also has limited QA resources and can introduce regressions, as illustrated by a recent Debian bug report.

🔗 [Source](https://www.openwall.com/lists/oss-security/2026/11/25/9)

hackernews · gslin · Nov 25, 20:38 · [Discussion](https://news.ycombinator.com/item?id=50647181)

**Background**: Ubuntu follows a six-month release cycle with LTS versions every two years, and Canonical provides security updates until each release's end-of-life. Debian is a community-driven distribution known for its stability and is often used as a base for Ubuntu. Security response time is a key factor for administrators choosing a server distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://www.openwall.com/lists/oss-security/2026/11/25/9">oss- security - Slow Ubuntu security response times</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ubuntu">Ubuntu - Wikipedia</a></li>
<li><a href="https://www.linuxteck.com/debian-vs-ubuntu/">Debian vs Ubuntu 2026: The Complete Comparison Guide</a></li>

</ul>
</details>

**Discussion**: The community sentiment is largely critical of Ubuntu, with several users reporting they have moved or are moving server workloads to Debian. However, some commenters offer a balanced view, noting that Debian's regression testing is not perfect and that Ubuntu's delays may stem from similar QA tradeoffs.

**Tags**: `#linux`, `#ubuntu`, `#security`, `#distributions`, `#debian`

</details>


<a id="item-11"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">NYT warns photographers against updating Photoshop over AI features</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

The New York Times has advised its freelance photographers not to update to the latest version of Adobe Photoshop, citing concerns that its AI features may compromise journalistic credibility. The warning comes as Adobe's generative AI tools, such as Generative Fill, become more deeply integrated into Photoshop. This move highlights a growing pushback from major institutions against generative AI due to credibility and social stigma concerns, potentially influencing how news organizations adopt AI tools and how software companies design their products. It also signals a broader industry shift toward transparency and provenance standards in digital content. The New York Times specifically warns that the latest Photoshop version uses AI 'in ways that may' affect the authenticity of images, and the concern extends to social media platforms automatically tagging AI-generated content, which can damage a brand's credibility. The article also references the C2PA Content Credentials standard, which provides cryptographically signed metadata to verify a digital asset's provenance and modification history.

🔗 [Source](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features)

hackernews · rmason · Nov 25, 21:18 · [Discussion](https://news.ycombinator.com/item?id=50647673)

**Background**: Adobe Photoshop has integrated generative AI features like Generative Fill, which allows users to add or remove objects using text prompts. The C2PA (Coalition for Content Provenance and Authenticity) is an open technical standard that uses Content Credentials to establish the origin and edits of digital content, helping combat misinformation. As AI-generated content becomes more prevalent, news organizations are increasingly concerned about maintaining trust with their audience.

<details><summary>References</summary>
<ul>
<li><a href="https://www.adobe.com/products/photoshop/generative-fill.html">Photoshop Generative Fill : Use AI to Fill in Images | Adobe</a></li>
<li><a href="https://en.wikipedia.org/wiki/Content_Credentials">Content Credentials - Wikipedia</a></li>
<li><a href="https://c2pa.org/">C2PA | Verifying Media Content Sources</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree that generative AI in creative work carries a social stigma, with one noting that few people enjoy encountering AI-generated content and that being associated with it is a liability. A creative tools developer points out the difficulty in distinguishing between fully AI-generated images and minor AI-assisted edits, especially when social media platforms tag content as AI-generated, which can be a 'death blow' to credibility. Others discuss the shift away from subscription software and question why journalistic photographers would use Photoshop at all, given ethical concerns about image manipulation.

**Tags**: `#AI ethics`, `#generative AI`, `#creative tools`, `#Adobe Photoshop`, `#content authenticity`

</details>


<a id="item-12"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Developer reverse-engineers Windows loudness equalization for PipeWire</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A developer reverse-engineered the loudness equalization algorithm used in Windows and ported it to PipeWire, releasing the project as pw-loudness-eq on GitHub. The project replicates Windows' hidden audio limiter behavior, which compresses peaks slightly in shared-mode audio paths. This brings a Windows-specific audio processing feature to Linux, potentially improving the listening experience for users who want consistent volume across different audio sources. It also highlights the often-overlooked audio processing that happens in Windows' shared-mode audio stack. The algorithm operates via audiodg.exe (CAudioLimiter in AudioEng.dll) in shared-mode WASAPI, DirectSound, and MME, but not in exclusive-mode WASAPI or ASIO. It applies a slight compression of about -0.1 dB at peaks, and the port may be susceptible to increasing gain of focused impulses like pure tones, requiring additional limiting.

🔗 [Source](https://github.com/xoxorwr/pw-loudness-eq)

hackernews · ThrowNotAway · Nov 25, 11:34 · [Discussion](https://news.ycombinator.com/item?id=50641171)

**Background**: PipeWire is a low-level multimedia framework for Linux that handles audio and video streams, designed to replace PulseAudio and JACK. Loudness equalization is a DSP technique that keeps volume levels consistent across different audio sources, commonly found in Windows audio drivers. Reverse-engineering involves analyzing compiled software to understand its algorithms, which can raise legal and ethical questions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PipeWire">PipeWire - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows-hardware/drivers/audio/loudness-equalization-dsp">Loudness Equalization DSP - Windows drivers | Microsoft Learn</a></li>
<li><a href="https://www.thewindowsclub.com/disable-or-enable-loudness-equalization-in-windows-10">How to disable or enable Loudness Equalization in Windows 11/10</a></li>

</ul>
</details>

**Discussion**: Commenters debated terminology, with one insisting the correct term is loudness normalization, not equalization. Some questioned the need to reverse-engineer a Windows DLL when simpler algorithms exist, raising ethical concerns, while others argued that a limiter is desired to cap loud peaks without harming dynamics.

**Tags**: `#audio`, `#pipewire`, `#reverse-engineering`, `#linux`, `#dsp`

</details>


<a id="item-13"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Developer uses Lean to audit Clojure core, finds unreported bugs</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A developer applied the Lean theorem prover to formally check Clojure's core library and reported finding previously unreported bugs, publishing the results in a blog post that sparked discussion on Hacker News. This demonstrates how formal verification tools like Lean can be used to audit widely-used language libraries, potentially improving reliability for critical infrastructure such as Clojure's core, which underpins systems at companies like Nubank. Some reported issues were disputed by commenters, who noted that certain examples (e.g., calling .indexOf on a byte array with a Long argument, or using get on a string with a float key) reflect expected type coercion behavior rather than bugs, highlighting the need to filter noise in such audits.

🔗 [Source](https://s.conao3.com/blog/2026/e4f733)

hackernews · encyclopedism · Nov 25, 14:56 · [Discussion](https://news.ycombinator.com/item?id=50642939)

**Background**: Lean is an open-source proof assistant and functional programming language based on dependent type theory, used for formal verification of software and mathematics. Clojure is a dynamic, functional Lisp dialect that runs on the JVM, and its core library (clojure.core) provides fundamental functions used by virtually all Clojure programs. Formal verification involves proving that a program meets a formal specification, and tools like Lean and Rocq (formerly Coq) are increasingly used to check real-world code.

<details><summary>References</summary>
<ul>
<li><a href="https://clojuredocs.org/clojure.core">clojure.core namespace | ClojureDocs - Community-Powered ...</a></li>

</ul>
</details>

**Discussion**: Commenters debated the methodology, with some pointing out that certain reported issues are not actual bugs but expected behavior, and others questioned whether Lean is now preferred over Rocq for such work. One commenter linked to a similar audit of Common Lisp implementations, and another expressed interest in learning Lean for testing.

**Tags**: `#Clojure`, `#Lean`, `#formal verification`, `#bug finding`, `#programming languages`

</details>


<a id="item-14"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Blog proposes entropy-based method to predict LoRA adapter size</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A blog post on engram.com proposes a method to predict the required size of a LoRA (Low-Rank Adaptation) adapter for any given dataset using entropy-based analysis. The post includes an interactive arithmetic coding widget that visualizes token probabilities as bits of entropy, and it has sparked discussion on overfitting, task learning versus memorization, and practical applications. If validated, this method could help practitioners avoid the costly trial-and-error of choosing LoRA rank by providing a principled estimate based on dataset entropy. It also contributes to the broader conversation about distinguishing between memorization and genuine task learning in fine-tuning, which is critical for building efficient and generalizable models. The method uses entropy analysis to estimate the information content of a dataset, which is then related to the number of parameters needed in a LoRA adapter. However, community members note that cross-entropy of a finite dataset includes both signal and noise (e.g., redundancy, quirks, typos), and that memorizing a dataset is not the same as learning a task, potentially leading to overfitting if the predicted size is used naively.

🔗 [Source](https://engram.com/blog/lora-size)

hackernews · jxmorris12 · Nov 24, 22:34 · [Discussion](https://news.ycombinator.com/item?id=50635783)

**Background**: LoRA is a parameter-efficient fine-tuning technique that freezes the pre-trained model weights and injects trainable low-rank matrices into each layer, drastically reducing the number of parameters to update. The rank of these matrices controls the adapter's capacity; choosing it appropriately is important for balancing performance and efficiency. Entropy, a measure of information content, is often used to quantify the complexity or unpredictability of data.

**Discussion**: Commenters highlighted the interactive arithmetic coding widget as a great visualization of token probabilities as bits of entropy. A key debate emerged around the distinction between memorizing a dataset and learning a task, with one commenter arguing that for tasks like math reasoning, the underlying pattern may have low entropy and require a much lower LoRA rank than memorizing the dataset would suggest, leading to overfitting if the predicted size is used. Others asked about metrics beyond size to describe a LoRA's usefulness and expressed interest in applying the method to image-generation models.

**Tags**: `#LoRA`, `#fine-tuning`, `#entropy`, `#machine-learning`, `#dataset-analysis`

</details>


<a id="item-15"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">Scientists Define Boundaries for AI Agents in Research</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

A new article on the Hugging Face blog, authored by Allen AI (AI2), explores where scientists draw the line on using AI agents in their workflows. It discusses trust, autonomy, and practical limits, offering a perspective on how the research community views AI agent adoption. As AI agents become more capable, understanding the boundaries scientists set is crucial for responsible adoption in research. This analysis highlights the need for balancing autonomy with human oversight, which could influence tool development and policy in scientific AI. The article is a commentary rather than a technical breakthrough, focusing on qualitative insights about trust and autonomy. It likely references frameworks for AI agent autonomy levels, such as those proposed in recent arXiv papers, to structure the discussion.

🔗 [Source](https://huggingface.co/blog/allenai/where-scientists-draw-the-line-on-ai-agents)

rss · Hugging Face Blog · Nov 25, 18:52

**Background**: AI agents are systems that autonomously perform tasks by designing workflows with available tools, as defined by IBM and Google Cloud. Hugging Face is a platform for sharing AI models and datasets, and Allen AI (AI2) is a research institute focused on AI. The concept of autonomy levels for AI agents has been discussed in recent literature, treating autonomy as a design decision separate from capability.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/discover/what-are-ai-agents">What are AI agents ? Definition , examples, and types | Google Cloud</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agents">What Are AI Agents ? | IBM</a></li>
<li><a href="https://arxiv.org/abs/2506.12469">[2506.12469] Levels of Autonomy for AI Agents - arXiv.org Levels of Autonomy for AI Agents | Knight First Amendment ... Levels of Autonomy for AI Agents | Knight First Amendment ... AI Agent Autonomy Levels: Controls by Level - nhimg.org Agentic AI Autonomy Levels and Control Framework AI Agent Autonomy Levels: 5 Stages Explained | BoldDesk</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#scientific research`, `#AI adoption`, `#trust and autonomy`, `#Hugging Face`

</details>


<a id="item-16"></a>
<details class="hz-item" data-score="7.0" markdown="1">
<summary><span class="hz-item-title">NVIDIA Blog Details Sim2Real Drone Obstacle Avoidance with Isaac Lab and Newton</span> <span class="hz-item-score">⭐️ 7.0/10</span></summary>

NVIDIA published a blog post presenting a complete simulation-to-reality (Sim2Real) workflow for training a microdrone to avoid obstacles using NVIDIA Isaac Lab and the Newton physics engine. The walkthrough covers the full pipeline from simulation setup to real-world deployment. This provides robotics practitioners with a concrete, reproducible example of using Isaac Lab and Newton for Sim2Real transfer, which can accelerate development of autonomous drones and other robots by reducing the need for physical prototyping. It also highlights NVIDIA's growing ecosystem for robotics simulation and reinforcement learning. The workflow leverages Isaac Lab, an open-source modular framework built on NVIDIA Isaac Sim, and the Newton physics engine, which is designed for high-fidelity simulation. The blog likely details the reinforcement learning training process, domain randomization techniques, and the challenges of transferring policies from simulation to a real microdrone.

🔗 [Source](https://huggingface.co/blog/nvidia/microduck-obstacle-avoidance)

rss · Hugging Face Blog · Nov 24, 16:34

**Background**: Sim2Real (simulation-to-reality) is a technique in robotics where control policies are trained in simulated environments and then deployed on physical robots, aiming to reduce the cost and risk of real-world training. Isaac Lab is an open-source framework for robot learning built on NVIDIA Isaac Sim, providing modular tools for reinforcement learning and simulation. Newton is a physics engine developed by NVIDIA in collaboration with partners, designed for high-performance, differentiable physics simulation in robotics.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/isaac/lab">Isaac Lab | NVIDIA Developer</a></li>
<li><a href="https://isaac-sim.github.io/IsaacLab/main/index.html">Welcome to Isaac Lab ! — Isaac Lab Documentation</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#sim2real`, `#reinforcement-learning`, `#simulation`, `#drone`

</details>


</section>