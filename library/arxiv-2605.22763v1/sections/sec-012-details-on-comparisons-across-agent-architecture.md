---
doc_id: arxiv-2605.22763v1
doc_title: "2026-5-22 Advancing Mathematics Research with AI-Driven Formal Proof Search George Tsoukalas1† , Anton Kovsharov1† , Sergey Shirobokov1† , Anja Surina1, Moritz Firsching1, Gergely"
section_id: sec-012-details-on-comparisons-across-agent-architecture
section_title: "Details on Comparisons across Agent Architectures and Models"
section_number: null
pages: 27-30
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
doc_brief: "2026-5-22 Advancing Mathematics Research with AI-Driven Formal Proof Search George Tsoukalas1† , Anton Kovsharov1† , Sergey Shirobokov1† , Anja Surina1, Moritz Firsching1, Gergely — 14 sections: Intro"
---
Figure9reports, foreachErdősproblem, thedistributionofcomputationalcostsforsuccessful
runs, along with the solve rate for each agent. We note a large variance in the cost for most
problems and methods, which highlights the stochastic nature of the agent. This is especially
noticeable on problems such as Erdős 12(ii) and 152.
erdos_12(i) erdos_12(ii) erdos_125 erdos_138 erdos_152 erdos_26 erdos_741(i) erdos_741(ii) erdos_846
Problem
0
250
500
750
1000
1250
1500
1750Cost, USD
100%
100%
70%
80%
100%
100%
90%
90%
10%
20%
0%
50%
100%
100%
50%
100%
80%
80%30%
10%
100%
100%
100%
100%
100%
100%
90%
90%
100%100%100%100%
100%
100%
90%
100%
Cost per proof by method
Method
(A) basic (K=10)
(B) basic w/ AP (K=10)
(C) basic w/ evolution (K=1)
(D) full (K=1)
Figure 9| Box plots illustrating the distribution of a cost for successful proof for the
Erdős problems.Four distinct experimental configurations are compared: basic@K=10
(blue), basic with AlphaProof @K=10 (orange), basic with evolution (green), and full (red).
The solid horizontal line within each box denotes the median cost, while the upper and lower
box boundaries represent the third and first quartiles, respectively. Whiskers extend to the
rest of the distribution, and individual circles indicate outlier data points. Triangular markers
denote instances with a single data point where only one proof attempt was successful.
Figure 10 shows the solve rate versus mean inference cost (in USD) for all nine Erdős
problems. In addition to the plot in the main text, it also presents results for the full method
when run with varying numbers of asynchronous LLM agents. Interestingly, running the
full method with only one generator, but sampling from the database (instead of taking the
previous session’s output), underperformed in comparison to the basic setup. This suggests
that sampling is not beneficial unless one has an asynchronous pipeline and uses the database
as a way of coordinating agents. Having three or six asynchronous agents did not outperform
the full configuration with 10 agents on the most challenging problems; however, these
configurations were more efficient on the easier tasks. Given the high variance in the observed
27
Advancing Mathematics Research with AI-Driven Formal Proof Search
200 400 600 800 1000 1200 1400
Mean Cost, USD
0.0
0.2
0.4
0.6
0.8
1.0Solve Rate
erdos_12(i)
100 200 300 400 500 600
Mean Cost, USD
0.0
0.2
0.4
0.6
0.8
1.0
erdos_12(ii)
0 200 400 600 800
Mean Cost, USD
0.0
0.2
0.4
0.6
0.8
1.0
erdos_125
50 100 150 200 250 300 350
Mean Cost, USD
0.0
0.2
0.4
0.6
0.8
1.0Solve Rate
erdos_138
0 200 400 600 800 1000
Mean Cost, USD
0.0
0.2
0.4
0.6
0.8
1.0
erdos_152
50 100 150 200 250 300 350 400
Mean Cost, USD
0.0
0.2
0.4
0.6
0.8
1.0
erdos_26
50 100 150 200 250 300
Mean Cost, USD
0.0
0.2
0.4
0.6
0.8
1.0Solve Rate
erdos_741(i)
5.0 7.5 10.0 12.5 15.0 17.5 20.0 22.5
Mean Cost, USD
0.0
0.2
0.4
0.6
0.8
1.0
erdos_741(ii)
50 100 150 200 250 300
Mean Cost, USD
0.0
0.2
0.4
0.6
0.8
1.0
erdos_846
(A) basic (B) basic w/ AP (C) basic w/ evolution (D) full (D) full@1 (D) full@3 (D) full@6
Figure 10| Solve rate versus mean inference cost (USD) across nine Erdős problem
instances.Seven system configurations shown: basic (blue circles), basic with AlphaProof
(AP) (orange squares), basic with evolution (green diamonds), full (red triangles), full@1
(purple downward triangles), full@3 (brown pluses), and full@6 (pink x), where @S are the
variants of full system with a given number of parallel LLM generation threads. Connected
curves denote the number of independent attempts𝐾. Error bars indicate one standard
error interval. For the basic and basic with AlphaProof configurations, each curve traces the
cost–performance Pareto frontier as𝐾 increases, revealing diminishing marginal returns at
higher budgets. Note that basic with AlphaProof and full do not include the inference cost of
AlphaProof.
28
Advancing Mathematics Research with AI-Driven Formal Proof Search
erdos_12(i) erdos_12(ii) erdos_125 erdos_138 erdos_152 erdos_26 erdos_741(i) erdos_741(ii) erdos_846
Problem
0
10
20
30
40Time, hours
100%
100% 80%
100%
100%
90%
10%
20%
50%
100%
100%
100%
80%
80%
10%
100%
100%
100%
100%
100%
90%
100%
100%100%
100%100%
100%
Wall-clock time per proof by method
Method
basic (K=10)
basic w/ AP (K=10)
full (K=1)
Figure 11| Box plots illustrating the distribution of a wall-clock time for a successful
proof for the Erdős problems.Three distinct experimental configurations are compared:
basic@K=10 (blue), basic with AlphaProof @K=10 (orange), and full (red). The solid
horizontal line within each box denotes the median time, while the upper and lower box
boundaries represent the third and first quartiles, respectively. Whiskers extend to the rest
of the distribution, and individual circles indicate outlier data points. Triangular markers
denote instances with a single data point where only one proof attempt was successful. A
cut-off of 48 hours applied to all experiments.
results, one can conclude that setting𝐾=10is a strong default for the system.
We conducted two additional runs of our basic agent (A), differing only in the proving
LLMs used: Gemini 3.0 Flash and Gemini 3.1 Flash-Lite. We also ran the basic setup with
AlphaProof as a tool using Gemini 3.0 Flash as the prover model. All runs were executed
with 𝐾= 100and a 24-hour time budget. None of the three runs were able to solve any of
the Erdős problems.
To evaluate AlphaProof as a standalone baseline, we ran it in tree search inference mode
on all 9 Erdős problems. Even though we allowed a compute budget of approximately 64
v6e TPU hours per problem, the system could not resolve any of them. TPU pricing can be
found athttps://cloud.google.com/tpu/pricing.
29
Advancing Mathematics Research with AI-Driven Formal Proof Search
The LLM cost for each agent was computed as follows:
𝑡𝑜𝑡𝑎𝑙𝑐𝑜𝑚𝑝𝑜𝑛𝑒𝑛𝑡 =𝑖𝑛𝑝𝑢𝑡∗𝑝 𝑖𝑛𝑝𝑢𝑡+𝑐𝑎𝑐ℎ𝑒 𝑟𝑒𝑎𝑑∗𝑝 𝑐𝑎𝑐ℎ𝑒+𝑜𝑢𝑡𝑝𝑢𝑡∗𝑝 𝑜𝑢𝑡𝑝𝑢𝑡,
𝑡𝑜𝑡𝑎𝑙=𝑡𝑜𝑡𝑎𝑙 𝑠𝑘𝑒𝑡𝑐ℎ𝑒𝑟+𝑡𝑜𝑡𝑎𝑙 𝑟𝑎𝑡𝑒𝑟
where 𝑖𝑛𝑝𝑢𝑡 includes user prompt, agent session prefix, thoughts and tool calls outputs and
excludes cached tokens,𝑐𝑎𝑐ℎ𝑒𝑟𝑒𝑎𝑑 accounts for the input tokens read from cache and𝑜𝑢𝑡𝑝𝑢𝑡
includes model output and thoughts.𝑝 is the corresponding standard price per token as per
https://ai.google.dev/gemini-api/docs/pricing . Note that for all agent price
estimates, we applied the rate for prompts of 200k tokens or fewer.
