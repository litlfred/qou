---
doc_id: arxiv-2605.22763v1
doc_title: "2026-5-22 Advancing Mathematics Research with AI-Driven Formal Proof Search George Tsoukalas1† , Anton Kovsharov1† , Sergey Shirobokov1† , Anja Surina1, Moritz Firsching1, Gergely"
section_id: sec-004-impact-of-agent-architecture-and-model
section_title: "Impact of Agent Architecture and Model"
section_number: null
pages: 8-10
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
doc_brief: "2026-5-22 Advancing Mathematics Research with AI-Driven Formal Proof Search George Tsoukalas1† , Anton Kovsharov1† , Sergey Shirobokov1† , Anja Surina1, Moritz Firsching1, Gergely — 14 sections: Intro"
---
Exploration of a large space of open problems is expensive, and we chose the full-featured
agent (agent (D)) for this based on its strong performance on competition benchmarks. To
understand which architectural components are necessary for its successes, we compared its
performance against agents (A), (B), and (C) on the Erdős problem set in Table 1.
We compared the agents by analyzing the solve rate against the cost (in US dollars)
per successfully proven problem. We report computational cost in USD because it directly
measures the barrier to reproducing this work and provides a natural common currency for
comparing agents that allocate compute differently (e.g., agent (D) uses Gemini 3.0 Flash
for rater subagents and Gemini 3.1 Pro for provers). We do not intend USD as a comparison
of AI and human mathematical labor.
Foragents(C)and(D),inwhichasingleproofattemptrequires10subagents,weexecuted
10 attempts per problem. In contrast, for the basic Agent (A) and its AlphaProof-equipped
extension (B), we ran 100 independent attempts, each with a single subagent.
Because (A) and (B) consist of independent subagents, we simulated scenarios where
they have𝐾 subagents by grouping the attempts into chunks of size100/𝐾; a chunk was
considered successful if any attempt included in the chunk proved the statement. The overall
solve rate was defined to be the fraction of successful chunks. To calculate the monetary cost
for these successful chunks, we identified the earliest timestamp𝑇 of a successful attempt
and summed the costs of all attempts within that chunk up to𝑇. Since agents (C) and (D)
are more expensive, we used the independent attempts to obtain a single point estimate.
Fig. 3 compares the agents across six Erdős problems (results for the rest are in the
supplementary material). Agents (A) and (B) perform similarly – within the margin of error
8
Advancing Mathematics Research with AI-Driven Formal Proof Search
100 200 300 400 500 600
Mean Cost, USD
0.0
0.2
0.4
0.6
0.8
1.0Solve Rate
1
3
6
10
1
3
6
10
1
1
erdos_12(i)
50 100 150 200 250 300 350 400
Mean Cost, USD
0.0
0.2
0.4
0.6
0.8
1.0
1
3
6 10
1
3
6 10
1 1
erdos_12(ii)
0 200 400 600
Mean Cost, USD
0.0
0.2
0.4
0.6
0.8
1.0
1 3 6
10
1
3
6
10
1
1
erdos_125
50 100 150 200 250 300 350
Mean Cost, USD
0.0
0.2
0.4
0.6
0.8
1.0Solve Rate
1
3
6
10
1
3
6
10
1
1
erdos_138
200 400 600 800 1000
Mean Cost, USD
0.0
0.2
0.4
0.6
0.8
1.0
1
3
6
10
1
3
6
10
1
1
erdos_152
50 100 150 200 250
Mean Cost, USD
0.0
0.2
0.4
0.6
0.8
1.0
1
3 6 10
1
3 6 101 1
erdos_26
(A) basic (B) basic w/ AP (C) basic w/ evolution (D) full
Figure 3| Solve rate versus mean inference cost (USD) across six Erdős problem
instances.The solve rates are evaluated for the four agents: (A) basic (blue circles), (B)
basic with AlphaProof (orange squares), (C) basic with evolution (green diamonds), and
(D) full-featured (red triangles). Numeric annotations denote the number of independent
attempts 𝐾∈{ 1, 3, 6, 10} grouped together; error bars indicate one standard error interval.
Duetotheirhighercosts, agents(C)and(D)lackvarianceestimates, asindependentattempts
were used to obtain a single point estimate (see main text for details). For agents (A) and (B),
each curve traces the cost–performance Pareto frontier as𝐾 increases, revealing diminishing
marginal returns at higher budgets. Agent (B) generally matches or exceeds the solve rate of
the basic configuration at comparable cost. Costs reported for (B) and (D) do not include
the inference cost of AlphaProof. While for most problems configuration (A) or (B) is the
best, for some challenging problems like Erdős #125, the full-featured configuration (D)
performs significantly better. Note that accounting for the estimated AlphaProof cost of 60
USD does not change the above outcomes beyond the margin of error.
9
Advancing Mathematics Research with AI-Driven Formal Proof Search
– on four of the problems, though agent (B) is more efficient on problems 12(ii) and 125.
Agent (D) outperforms (A) and (B) on problems 138 and 125, offering significant monetary
savings (2x to 5x), but is roughly half as cost-efficient on the remaining problems. We also
compared agents (A), (B), and (D) on the wall-clock time needed to solve the problems.
The results broadly followed the inference cost trends, with (B) offering savings over (A) in
several of the problems, and (D) substantially outperforming both (A) and (B) on problems
138 and 125.
Finally, we evaluated AlphaProof in standalone tree-search mode and versions of agent
(A) based on smaller models (Gemini 3.0 Flash, Gemini 3.1 Flash-Lite). These systems could
not solve any of the problems.
Cost and Variance.Per-problem inference costs exhibit high variance due to the stochastic
nature of our agents. The reported costs also do not capture the full cost of discovery:
we applied the full-featured agent to all 353 Erdős problems in Formal Conjectures, and
identifying tractable problems was itself a significant computational investment. AlphaProof
cost approximately 27.5 TPU hours ($60 USD) per problem on v6e TPUs.
