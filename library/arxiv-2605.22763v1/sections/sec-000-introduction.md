---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing mathematics research with AI-driven formal proof search"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
text_source: latex
latex_prose_ratio: 0.735
latex_coverage_ratio: 0.92
doc_brief: "Advancing mathematics research with AI-driven formal proof search — 14 sections: Introduction; AlphaProof Nexus; Systematic Evaluation on Open Prob"
---
Large language models (LLMs) have recently shown remarkable promise in solving complex mathematics problems \cite{feng2026autonomous, woodruff2026accelerating}, but \emph{unreliability} remains a primary barrier to their integration into mathematics research. Because LLM-generated natural language proofs can contain subtle logical errors, or ``hallucinations,'' they require expensive expert review. Mistakes in unreviewed intermediate steps can cascade through a proof, limiting the complexity of tasks that can be delegated to AI. 

Recent efforts \cite{hubert2025olympiad, achim2025aristotle} mitigate these issues by using AI to generate proofs in formal languages like Lean \cite{moura2021lean}, in which a compiler automatically verifies every logical step. So far, successes of this paradigm have been concentrated in competition mathematics and the human-aided formalization of natural language arguments \cite{hariharan2026milestone}. 
In this paper, we demonstrate its broader potential through a large-scale evaluation on open research-level problems. 

To this end, we developed a framework, {\systemlong}, for LLM-aided proof generation and used it to build a basic agent in which a set of subagents independently searches for proofs with feedback from the Lean compiler. We also developed a ``full-featured'' agent in which subagents are coordinated using an evolutionary algorithm \cite{novikov2025alphaevolve} and can use {\AP}~\cite{hubert2025olympiad}, a system for olympiad-level Lean theorem-proving based on reinforcement learning, as a focused proof tool.

Our full-featured agent autonomously solved 9 {\erdos} problems out of 353 attempted, including two questions that had been open for 56 years \cite{SCHOEN2001191, Baier2004ANO, elsholtz2016erd}, at the inference cost of a few hundred dollars per problem. It also 
proved 44/492 open conjectures from the Online Encyclopedia of Integer Sequences (OEIS), resolved a 15-year-old open question on Hilbert functions in algebraic geometry, improved an open bound in convex optimization by discovering a novel algorithmic parameter schedule, identified several misformalizations in the literature, helped resolve an open problem from Ben Green's well-known list \cite{green2024100}, and is aiding ongoing research efforts on quantum optics and graph theory. 

To understand the impact of the agent design on these results, we did a post-hoc analysis of the performance of the full-featured and basic agents, as well as two agents with intermediate capabilities, on the 9 {\erdos} problems solved by the full-featured agent. Remarkably, the basic agent solved all 9 problems, though at a higher cost on the harder problems. 

Overall, our results demonstrate the utility of LLM-powered formal proof search as a tool for mathematics research, and point to an ongoing shift from specialized trained systems toward simple agentic loops as LLMs become more capable. All Lean proofs and select natural-language proofs are available in \url{https://www.github.com/google-deepmind/alphaproof-nexus-results}.

\begin{figure}[htbp]
      \centering
\includegraphics[width=0.9\textwidth]{assets/SP_erdos_125_fixed_efw.pdf} 
\caption{\textbf{Example inputs/outputs for an {\AP}-equipped agent (applied to {\erdos} \#125).}  The user provides a Lean file with a specification of the problem, and an empty proof body replaced with the \texttt{sorry} placeholder. \textbf{(a)} Modifications are permitted only within \texttt{EVOLVE-BLOCK} and \texttt{EVOLVE-VALUE} markers. 

\textbf{(b)} During sketch refinement, the prover subagent is shown an assembled prompt template with the current proof, and optionally prior attempts/sketches, their Elo ratings, and feedback from {\AP}'s attempts on unsolved goals. \textbf{(c)} The prover reasons about the problem informally and invokes 
tools.

In this example, the prover invoked {\AP} which resolved all but one goal. 
The prover then decomposed that goal into three simpler lemmas, and called {\AP} again, which then resolved all remaining goals. The agent also produced a natural language summary of its attempt at the end of generation. 

}
    \label{fig:components}
\end{figure}
