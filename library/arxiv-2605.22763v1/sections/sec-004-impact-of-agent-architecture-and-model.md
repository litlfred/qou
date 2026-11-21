---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-004-impact-of-agent-architecture-and-model
section_title: "Impact of Agent Architecture and Model"
section_number: null
pages: 8-10
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.734
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
Exploration of a large space of open problems is expensive, and we chose the full-featured agent (agent (D)) for this based on its strong performance on competition benchmarks. To understand which architectural components are necessary for its successes, we compared its performance against agents (A), (B), and (C) on the {\erdos} problem set in Table~\ref{tab:major_results}. 

We compared the agents by analyzing the solve rate against the cost (in US dollars) per successfully proven problem. 
We report computational cost in USD because it directly measures the barrier to reproducing this work and provides a natural common currency for comparing agents that allocate compute differently (e.g., agent (D) uses Gemini 3.0 Flash for rater subagents and Gemini 3.1 Pro for provers). We do not intend USD as a comparison of AI and human mathematical labor.

For agents (C) and (D), in which a single proof attempt requires 10 subagents, 
we executed 10 attempts per problem. In contrast, for the basic Agent (A) and its {\AP}-equipped extension (B), we ran 100 independent attempts, each with a single subagent. 

Because (A) and (B) consist of independent subagents, we simulated scenarios where they have $K$ subagents by grouping the attempts into chunks of size $100/K$; a chunk was considered successful if any attempt included in the chunk proved the statement. The overall solve rate was defined to be the fraction of successful chunks. To calculate the monetary cost for these successful chunks, we identified the earliest timestamp $T$ of a successful attempt and summed the costs of all attempts within that chunk up to $T$. Since 
agents (C) and (D) are more expensive, we used the independent attempts to obtain a single point estimate.

Fig.~\ref{fig:scaling_plot_erdos_main} compares the agents across six {\erdos} problems (results for the rest are in the supplementary material). 
Agents (A) and (B) perform similarly -- within the margin of error -- on four of the problems, though agent (B) is more efficient on problems 12(ii) and 125. Agent (D) outperforms (A) and (B) on problems 138 and 125, offering significant monetary savings (2x to 5x), but is roughly half as cost-efficient on the remaining problems. 
We also compared agents (A), (B), and (D) on the wall-clock time needed to solve the problems. The results broadly followed the inference cost trends, with (B) offering savings over (A) in several of the problems, and (D) substantially outperforming both (A) and (B) on problems 138 and 125.

Finally, we evaluated {\AP} in standalone tree-search mode and versions of agent (A) based on smaller models (Gemini 3.0 Flash, Gemini 3.1 Flash-Lite). These systems could not solve any of the problems.


\paragraph{Cost and Variance.} Per-problem inference costs exhibit high variance due to the stochastic nature of our agents. The reported costs also do not capture the full cost of discovery: we applied the full-featured agent to all 353 {\erdos} problems in Formal Conjectures, and identifying tractable problems was itself a significant computational investment. {\AP} cost approximately 27.5 TPU hours (\$60 USD) per problem on v6e TPUs.
