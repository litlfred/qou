---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing mathematics research with AI-driven formal proof search"
section_id: sec-005-discussion
section_title: "Discussion"
section_number: null
pages: 10-18
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
doc_brief: "Advancing mathematics research with AI-driven formal proof search — 14 sections: Introduction; AlphaProof Nexus; Systematic Evaluation on Open Prob"
---
We have provided a large-scale demonstration of the value of formal proof search agents on
research-level mathematical problems. Recently, some natural-language reasoning systems
have been shown to succeed in research-level mathematical tasks, including Erdős problems
[20, 4]. However, the use of AI-generated informal proofs, either as standalone products or
as inputs to a subsequent formalization stage, requires careful validation by human experts.
Formal verification can serve as a filter for determining which proofs merit human review.
The effectiveness of our basic agent in our post-hoc analysis was surprising. At the time
we were planning our large-scale exploration, simpler agentic loops did not show strong
performance on competition-level benchmarks, and this informed our decision to use the
full-featured agent. The LLM landscape has since shifted substantially. We attribute the
basic agent’s success to both this shift and the power of compiler feedback in grounding LLM
reasoning. The full-featured agent retains an advantage on the hardest problems for now.
However, as LLM capabilities grow, this advantage may diminish.
At present, our agents’ successes are concentrated in areas such as combinatorics, convex
optimization, and number theory, where Lean’s mathematics library [60] is mature and tasks
often decompose into tractable subgoals. Even most Erdős problems remain out of reach,
let alone problems that require extensive new theory. Additionally, our agents inherit the
biases of their underlying LLMs and exhibit high search variance. Characterizing the agents’
boundaries and expanding them is an important direction for future work.
We built AlphaProof Nexus with the belief that the future of mathematics lies in human-
machine partnership, where interactive AI tools serve to expand a mathematician’s creative
capacity. Our results support this vision. Our mathematician collaborators found that proof
attempts by our agents enhanced their understanding of a problem, even when an agent
could not prove the claim at hand. Because the sketches were formal, experts could focus
on the unresolved subgoals rather than re-verifying the entire argument. Moreover, the
10
Advancing Mathematics Research with AI-Driven Formal Proof Search
agents were powerful tools for detecting misformalizations. These experiences suggest that
AI-driven formal proof search can serve not only to solve problems but to deepen human
understanding.
References
[1] TudorAchim, AlexBest, AlbertoBietti, KevinDer, MathïsFédérico, SergeiGukov, Daniel
Halpern-Leistner, Kirsten Henningsgard, Yury Kudryashov, Alexander Meiburg, et al.
Aristotle: IMO-level automated theorem proving.arXiv preprint arXiv:2510.01346,
2025.
[2] BorisAlexeev,KevinBarreto,YanyangLi,JaredDukerLichtman,LiamPrice,JibranIqbal
Shah, Quanyu Tang, and Terence Tao. Primitive sets and von mangoldt chains: Erdős
problem #1196 and beyond, 2026.
[3] Boris Alexeev, Moe Putterman, Mehtaab Sawhney, Mark Sellke, and Gregory Valiant.
Short proofs in combinatorics and number theory.arXiv preprint arXiv:2603.29961,
2026.
[4] Boris Alexeev, Moe Putterman, Mehtaab Sawhney, Mark Sellke, and Gregory Valiant.
Short proofs in combinatorics, probability and number theory ii.arXiv preprint
arXiv:2604.06609, 2026.
[5] LeniAniva,ChuyueSun,BrandoMiranda,ClarkBarrett,andSanmiKoyejo. Pantograph:
A machine-to-machine interaction interface for advanced theorem proving, high level
reasoning, and data extraction in lean 4, 2025.
[6] Axiom. AXLE: Axiom lean engine, 2025. Accessed: 2025.
[7] Stephan Baier. A note on p-sets. 2004.
[8] Thomas Bloom. Erdosproblems.com. https://www.erdosproblems.com, 2026.
[9] Mats Boij, Juan C. Migliore, Rosa M. Miró-Roig, Uwe Nagel, and Fabrizio Zanello.On
the Shape of a Pure O-Sequence, volume 218 ofMemoirs of the American Mathematical
Society. American Mathematical Society, Providence, RI, 2012.
[10] J. A. Bondy and R. L. Hemminger. Graph reconstruction–a survey.Journal of Graph
Theory, 1(3):227–268, 1977.
[11] Jim Bryan, Balázs Elek, Freddie Manners, George Salafatinos, and Ravi Vakil. The
motivic class of the space of genus0maps to the flag variety.arXiv preprint
arXiv:2601.07222, 2026.
[12] S. A. Burr, P. Erdős, R. L. Graham, and W. Wen-Ching Li. Complete sequences of sets of
integer powers.Acta Arithmetica, 77(2):133–138, 1996.
[13] Yang Cai and Weiqiang Zheng. Last-iterate convergence of anchored gradient descent.
arXiv preprint arXiv:2604.12235, 2026.
11
Advancing Mathematics Research with AI-Driven Formal Proof Search
[14] François Caron and Arnaud Doucet. Efficient Bayesian inference for generalized
Bradley–Terry models.Journal of Computational and Graphical Statistics, 21(1):174–
196, 2012.
[15] Jiangjie Chen, Wenxiang Chen, Jiacheng Du, Jinyi Hu, Zhicheng Jiang, Allan Jie,
Xiaoran Jin, Xing Jin, Chenggang Li, Wenlei Shi, et al. Seed-prover 1.5: Mastering
undergraduate-level theorem proving via learning from experience.arXiv preprint
arXiv:2512.17260, 2025.
[16] DeepSeek-AI. Deepseek-v2: A strong, economical, and efficient mixture-of-experts
language model, 2024.
[17] Christian Elsholtz and Stefan Planitzer. On erdős and sárközy’s sequences with property
p.arXiv preprint arXiv:1609.07935, 2016.
[18] Paul Erdős and Alice Sárközi. On the divisibility properties of sequences of integers.
Proceedings of The London Mathematical Society, pages 97–101, 1970.
[19] Siemion Fajtlowicz. On conjectures of graffiti. In J. Akiyama, Y. Egawa, and H. Enomoto,
editors,Graph Theory and Applications, volume 38 ofAnnals of Discrete Mathematics,
pages 113–118. Elsevier, 1988.
[20] Tony Feng, Junehyuk Jung, Sang-hyun Kim, Carlo Pagano, Sergei Gukov, Chiang-
Chiang Tsai, David Woodruff, Adel Javanmard, Aryan Mokhtari, Dawsen Hwang, et al.
Aletheia tackles firstproof autonomously.arXiv preprint arXiv:2602.21201, 2026.
[21] Tony Feng, Trieu H. Trinh, Garrett Bingham, Dawsen Hwang, Yuri Chervonyi, Junehyuk
Jung,JoonkyungLee,CarloPagano,SanghyunKim,FedericoPasqualotto,SergeiGukov,
Jonathan N. Lee, Junsu Kim, Kaiying Hou, Golnaz Ghiasi, Yi Tay, YaGuang Li, Chenkai
Kuang, Yuan Liu, Hanzhao Lin, Evan Zheran Liu, Nigamaa Nayakanti, Xiaomeng Yang,
Heng-Tze Cheng, Demis Hassabis, Koray Kavukcuoglu, Quoc V. Le, and Thang Luong.
Towards autonomous mathematics research.arXiv preprint 2602.10177, 2026.
[22] Moritz Firsching and Bogdan Georgiev. A strict separation between two notions of
quadratically structured functions. In preparation, 2026.
[23] Moritz Firsching, Paul Lezeau, Salvatore Mercuri, Miklós Z. Horváth, Yaël Dillies, Calle
Sönne, Eric Wieser, Fred Zhang, Thomas Hubert, Blaise Agüera y Arcas, and Pushmeet
Kohli. Formal conjectures: An open and evolving benchmark for verified discovery in
mathematics, 2026.
[24] GasStationManager. Safeverify.https://github.com/GasStationManager/Saf
eVerify, 2025. [Accessed: 2026-05-12].
[25] Bogdan Georgiev, Javier Gómez-Serrano, Terence Tao, and Adam Zsolt Wagner. Mathe-
matical exploration and discovery at scale.arXiv preprint arXiv:2511.02864, 2025.
[26] Google DeepMind. Gemini 3.1 deep think, 2026. Accessed: 2026-04-30.
[27] Ben Green. 100 open problems. https://people.maths.ox.ac.uk/greenbj/papers/open-
problems.pdf, 2024.
12
Advancing Mathematics Research with AI-Driven Formal Proof Search
[28] Sidharth Hariharan, Christopher Birkbeck, Seewoo Lee, Ho Kiu Gareth Ma, Bhavik
Mehta, Auguste Poiroux, and Maryna Viazovska. A milestone in formalization: The
sphere packing problem in dimension 8.arXiv preprint arXiv:2604.23468, 2026.
[29] Thomas Hubert, Rishi Mehta, Laurent Sartran, Miklós Z Horváth, Goran Žužić, Eric
Wieser, Aja Huang, Julian Schrittwieser, Yannick Schroecker, Hussain Masoom, Ottavia
Bertolli, Tom Zahavy, Amol Mandhane, Jessica Yung, Iuliya Beloshapka, Borja Ibarz,
Vivek Veeriah, Lei Yu, Oliver Nash, Paul Lezeau, Salvatore Mercuri, Calle Sönne, Bhavik
Mehta, Alex Davies, Daniel Zheng, Fabian Pedregosa, Yin Li, Ingrid von Glehn, Mark
Rowland, Samuel Albanie, Ameya Velingker, Simon Schmitt, Edward Lockhart, Edward
Hughes, Henryk Michalewski, Nicolas Sonnerat, Demis Hassabis, Pushmeet Kohli,
and David Silver. Olympiad-level formal mathematical reasoning with reinforcement
learning.Nature, pages 1–3, 2025.
[30] Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Mohammadamin Barekatain,
Simon Schmitt, and David Silver. Learning and planning in complex action spaces. In
International Conference on Machine Learning, 2021.
[31] Geoffrey Huntley. Ralph wiggum as a "software engineer".https://ghuntley.com
/ralph, 2025. Blog post.
[32] Vishesh Jain and Clayton Mizgerd. Equality in fill’s spectral gap problem.arXiv preprint
arXiv:2604.03937, 2026.
[33] Uijeong Jang and Ernest K Ryu. Point convergence of nesterov’s accelerated gradient
method: An ai-assisted proof.arXiv preprint arXiv:2510.23513, 2025.
[34] Albert Q Jiang, Sean Welleck, Jin Peng Zhou, Wenda Li, Jiacheng Liu, Mateja Jamnik,
Timothée Lacroix, Yuhuai Wu, and Guillaume Lample. Draft, sketch, and prove:
Guiding formal theorem provers with informal proofs.arXiv preprint arXiv:2210.12283,
2022.
[35] Albert Qiaochu Jiang, Wenda Li, Szymon Tworkowski, Konrad Czechowski, Tomasz
Odrzygóźdź, Piotr Miłoś, Yuhuai Wu, and Mateja Jamnik. Thor: Wielding hammers
to integrate language models and automated theorem provers.Advances in Neural
Information Processing Systems, 35:8360–8373, 2022.
[36] Paul J. Kelly. A congruence theorem for trees.Pacific Journal of Mathematics, 7(1):961–
968, 1957.
[37] John R. Koza. Genetic programming as a means for programming computers by natural
selection.Statistics and Computing, 4(2):87–112, 1994.
[38] Mario Krenn, Moritz Firsching, George Tsoukalas, Rishikesh Gajjala, Xuemei Gu, and
Swarat Chaudhuri. A Tensor-Algebraic No-Go Theorem for High-Dimensional Photonic
GHZ States. In preparation, 2026.
[39] Mario Krenn, Xuemei Gu, and Anton Zeilinger. Quantum experiments and graphs:
Multiparty states as coherent superpositions of perfect matchings.Physical Review
Letters, 119(24), December 2017.
13
Advancing Mathematics Research with AI-Driven Formal Proof Search
[40] Yong Lin, Shange Tang, Bohan Lyu, Ziran Yang, Jui-Hui Chung, Haoyu Zhao, Lai
Jiang, Yihan Geng, Jiawei Ge, Jingruo Sun, et al. Goedel-prover-v2: Scaling formal
theorem proving with scaffolded data synthesis and self-correction.arXiv preprint
arXiv:2508.03613, 2025.
[41] R.D. Luce.Individual Choice Behavior: A Theoretical Analysis. Wiley, 1959.
[42] Math Inc. Gauss: An agent for autoformalization, 2026. Accessed: 2026.
[43] LeonardodeMouraandSebastianUllrich. Thelean4theoremproverandprogramming
language. InInternational Conference on Automated Deduction, pages 625–635. Springer,
2021.
[44] Ansh Nagda, Prabhakar Raghavan, and Abhradeep Thakurta. Reinforced generation of
combinatorial structures: Hardness of approximation.arXiv preprint arXiv:2509.18057,
2025.
[45] Ansh Nagda, Prabhakar Raghavan, and Abhradeep Thakurta. Reinforced generation of
combinatorial structures: Ramsey numbers.arXiv preprint arXiv:2603.09172, 2026.
[46] Alexander Novikov, Ngân V˜u, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang,
Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas
Mehrabian, M. Pawan Kumar, Abigail See, Swarat Chaudhuri, George Holland, Alex
Davies, Sebastian Nowozin, Pushmeet Kohli, and Matej Balog. Alphaevolve: A coding
agent for scientific and algorithmic discovery.arXiv preprint 2506.13131, 2025.
[47] R. L. Plackett. The analysis of permutations.Journal of the Royal Statistical Society.
Series C (Applied Statistics), 24(2):193–202, 1975.
[48] StanislasPoluandIlyaSutskever. Generativelanguagemodelingforautomatedtheorem
proving.arXiv preprint arXiv:2009.03393, 2020.
[49] Moe Putterman, Mehtaab Sawhney, and Gregory Valiant. On infinite sets with no3on
a line.arXiv preprint arXiv:2602.21275, 2026.
[50] Christian Reiher, Vojtěch Rödl, and Marcelo Sales. Colouring versus density in integers
and hales–jewett cubes.Journal of the London Mathematical Society, 110(5):e12987,
2024.
[51] Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexander Novikov, Matej
Balog, M. Pawan Kumar, Emilien Dupont, Francisco J. R. Ruiz, Jordan S. Ellenberg,
Pengming Wang, Omar Fawzi, Pushmeet Kohli, and Alhussein Fawzi. Mathematical
discoveries from program search with large language models.Nature, 625(7995):468–
475, 2024.
[52] Ernest K. Ryu, Kun Yuan, and Wotao Yin. Ode analysis of stochastic gradient methods
with optimism and anchoring for minimax problems.arXiv preprint arXiv:1905.10899,
2019.
14
Advancing Mathematics Research with AI-Driven Formal Proof Search
[53] Johannes Schmitt. Extremal descendant integrals on moduli spaces of curves:
An inequality discovered and proved in collaboration with ai.arXiv preprint
arXiv:2512.14575, 2025.
[54] Tomasz Schoen. On a problem of erdős and sárközy.Journal of Combinatorial Theory,
Series A, 94(1):191–195, 2001.
[55] David Silver, Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Matthew Lai,
Arthur Guez, Marc Lanctot, Laurent Sifre, Dharshan Kumaran, Thore Graepel, et al. A
general reinforcement learning algorithm that masters chess, shogi, and go through
self-play, 2018.
[56] Neil J. Sloane. The on-line encyclopedia of integer sequences. InProceedings of the
14th Symposium on Towards Mechanized Mathematical Assistants: 6th International
Conference, Calculemus ’07 / MKM ’07, page 130, Berlin, Heidelberg, 2007. Springer-
Verlag.
[57] Richard P. Stanley. Hilbert functions of graded algebras.Advances in Mathematics,
28(1):57–83, 1978.
[58] Anja Surina, Arun Suggala, George Tsoukalas, Anton Kovsharov, Sergey Shirobokov,
Francisco JR Ruiz, Pushmeet Kohli, and Swarat Chaudhuri. An improved last-iterate
convergencerateforanchoredgradientdescentascent.arXivpreprintarXiv:2604.03782,
2026.
[59] Terence Tao and contributors. Ai contributions to Erdős problems.https://github
.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-p
roblems, 2026. Accessed: 2026-04-23.
[60] The Mathlib Community. The Lean Mathematical Library. InProceedings of the 9th
ACM SIGPLAN International Conference on Certified Programs and Proofs, CPP 2020,
New Orleans, LA, USA, 2020. ACM.
[61] Stanislaw M. Ulam. A collection of mathematical problems.New York and London:
Interscience Publishers, 1960.
[62] Stanislaw M. Ulam.A Collection of Mathematical Problems, volume 8 ofInterscience
Tracts in Pure and Applied Mathematics. Interscience Publishers, New York, 1960.
[63] Sumanth Varambally, Thomas Voice, Yanchao Sun, Zhifeng Chen, Rose Yu, and Ke Ye.
Hilbert: Recursively building formal proofs with informal reasoning.arXiv preprint
arXiv:2509.22819, 2025.
[64] Haiming Wang, Mert Unsal, Xiaohan Lin, Mantas Baksys, Junqi Liu, Marco Dos Santos,
Flood Sung, Marina Vinyes, Zhenzhe Ying, Zekai Zhu, et al. Kimina-prover preview:
Towards large formal reasoning models with reinforcement learning.arXiv preprint
arXiv:2504.11354, 2025.
[65] David P Woodruff, Vincent Cohen-Addad, Lalit Jain, Jieming Mao, Song Zuo, Moham-
madHossein Bateni, Simina Branzei, Michael P Brenner, Lin Chen, Ying Feng, et al.
15
Advancing Mathematics Research with AI-Driven Formal Proof Search
Accelerating scientific research with gemini: Case studies and common techniques.
arXiv preprint arXiv:2602.03837, 2026.
[66] Kaiyu Yang, Gabriel Poesia, Jingxuan He, Wenda Li, Kristin Lauter, Swarat Chaudhuri,
and Dawn Song. Formal mathematical reasoning: A new frontier in ai.arXiv preprint
2412.16075, 2024.
[67] Kaiyu Yang, Aidan Swope, Alex Gu, Rahul Chalamala, Peiyang Song, Shixing Yu, Saad
Godil, Ryan J Prenger, and Animashree Anandkumar. Leandojo: Theorem proving
with retrieval-augmented language models.Advances in Neural Information Processing
Systems, 36:21573–21612, 2023.
[68] Fabrizio Zanello. Log-concavity of level Hilbert functions and pure o-sequences.Journal
of Commutative Algebra, 16(2):245–256, 2024.
[69] Daniel Zheng, Ingrid von Glehn, Yori Zwols, Iuliya Beloshapka, Lars Buesing, Daniel M.
Roy, Martin Wattenberg, Bogdan Georgiev, Tatiana Schmidt, Andrew Cowie, Fernanda
Viegas, Dimitri Kanevsky, Vineet Kahlon, Hartmut Maennel, Sophia Alj, George Holland,
Alex Davies, and Pushmeet Kohli. AI Co-Mathematician: Accelerating mathematicians
with agentic AI.arXiv preprint 2605.06651, 2026.
Acknowledgments
We thank Emilien Dupont, Dan Roy, and Daniel Zheng for their careful feedback on the paper,
Alexander Novikov for help with LLM infrastructure, Katerina Hristova for help with Lean
formalization, and Sebastian Nowozin and Taylan Cemgil for their guidance on designing an
Elo scoring mechanism for proof sketches.
Author contributions:SC, SS, and GT conceptualized and implemented the first version
of AlphaProof Nexus. AK led the engineering and infrastructure decisions. AK, SS, GT, and
A.Surina developed the final version of AlphaProof Nexus with inputs from FJR, AF, and SC.
AK and SS maintained the underlying infrastructure of AlphaProof Nexus.
GT initiated and led the use of the system in mathematics research tasks. AK, SS, GT,
A.Surina, LY, and SC coordinated the large-scale runs on open research problems. GT, MF,
GB, A.Suggala and AZW identified problems to solve and validated the generated solutions.
GB, in particular, was the first research mathematician to use AlphaProof Nexus. MF, GT,
A.Surina, FJR, HM, SC, and EW contributed to Lean formalizations of problems. SS led the
systematic evaluation of our agents, with additional contributions from AK, MZH and AH.
SC, SS, GT, FJR, and A.Surina wrote the paper with inputs from MF, AZW, HM, and AF.
SS, AF, and EW created the figures with inputs from SC, GT, A.Surina and FJR. GB, AZW, MF,
GT, A.Surina and CG wrote the natural language proofs, with HM providing agent-generated
drafts to facilitate the writing process. MZH and EW assisted with Lean setup and integration
with AlphaProof. AF coordinated the creation of the accompanying Github repository.
MB and TH provided technical advice throughout the project. SC led the overall effort,
with PK providing sponsorship and technical and strategic direction.
16
Advancing Mathematics Research with AI-Driven Formal Proof Search
Competing interests:There are no competing interests to declare.
Data and materials availability:All Lean proofs are available in the accompanying repos-
itory https://www.github.com/google-deepmind/alphaproof-nexus-results .
Natural language proofs of some key results are provided in the repository and the supple-
mentary text.
17
Advancing Mathematics Research with AI-Driven Formal Proof Search
