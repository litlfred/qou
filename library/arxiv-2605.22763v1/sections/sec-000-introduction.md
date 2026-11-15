---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing mathematics research with AI-driven formal proof search"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
doc_brief: "Advancing mathematics research with AI-driven formal proof search — 14 sections: Introduction; AlphaProof Nexus; Systematic Evaluation on Open Prob"
text_source: latex
latex_prose_ratio: 0.624
latex_coverage_ratio: 1.0
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





\section{{\systemlong}}

\paragraph{Lean.} Lean \cite{moura2021lean} is a proof assistant in which definitions, theorems, and proofs are all mechanically verified code. Proofs are constructed via a sequence of applications of \emph{tactics}, or elementary proof steps. Lean's compiler ``executes'' a proof tactic-by-tactic, tracking the proof goals pending after every tactic. A proof is correct if it leads the compiler to a state with no pending goals.

Lean includes a special $\mathtt{sorry}$ tactic, which immediately closes pending goals while passing the type checker. Proving a theorem thus amounts to the generation of type-safe code without $\mathtt{sorry}$ tactics. 

\paragraph{Input and Output.} {\systemlong} is a new framework for agents that query frontier LLMs and the Lean compiler. The agents take as input a Lean file consisting of a target theorem with $\mathtt{sorry}$ in place of a proof, along with definitions and library imports on which the theorem depends (we refer to such a file as a \emph{proof sketch}). Optionally, the user may input additional natural-language context and domain knowledge encoded in Lean. 

The input sketch is annotated with user-provided markers that delineate which code segments the agent may modify (see Fig.~\ref{fig:components}).
Within \texttt{EVOLVE-BLOCK} markers, the agent can introduce helper lemmas, definitions, and proof steps. \texttt{EVOLVE-VALUE} markers are used to enclose expressions (e.g., parameters) whose values the agent can change. On successful termination, the agent outputs a $\mathtt{sorry}$-free proof of the target theorem.

\paragraph{Agent Architecture.} 
The basic agent in {\systemlong} (agent (A)) consists of a set of \emph{prover subagents} that execute independently with no shared state. Each subagent 
is a ``Ralph loop''~\cite{huntley2025ralph} consisting of a sequence of \emph{episodes}: multi-turn LLM inference loops (based on Gemini 3.1 Pro) in which the subagent can reason via chain-of-thought and refine the sketch using a search-and-replace tool. After each turn, the subagent uses Lean to check that the current proof sketch compiles; if it does not, Lean's error message is used to direct the next turn. If the sketch contains \texttt{sorry} when the episode terminates, the subagent adds a comment to the sketch summarizing the lessons learned from the episode. The resulting sketch is the input to the next episode. 

We extended the basic agent into one (B) that can query {\AP} \cite{hubert2025olympiad} to fill out missing parts of sketches. Queries to {\AP} can return a proof, disproof (a proof that the submitted subgoal is false), or a failure message; proofs are directly substituted into the sketch, while disproofs and failure messages are fed into the prover's prompt.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{assets/system_design_centered.pdf} 
    \caption{\textbf{Design of the full-featured {\systemlong} agent.} The mathematician provides as input a Lean theorem with \texttt{sorry} for a proof, and optionally, natural language context and additional domain knowledge encoded in Lean. The agent architecture consists of a basic generation-validation pipeline and an optional evolutionary framework. An LLM-based prover subagent attempts to solve the problem by refining proof sketches \textbf{(2)}. The subagent may optionally call {\AP} as a tool; each invocation of {\AP} on a goal returns whether a proof or disproof was found, or whether it was unsuccessful in resolving the goal. The sketch produced in the end is checked by a validator to ensure the problem statement was not changed unsafely and the proof compiles. If all goals are successfully proved, the agent outputs the final Lean proof. This basic pipeline can be extended with an evolutionary population database and rating mechanism. In this configuration, validated sketches are admitted into the Population Database \textbf{(3)}. Simultaneously, rater subagents sample previous attempts \textbf{(4)}, which are then ranked by an LLM critic in matches. The match results are admitted back into the database \textbf{(5)} to update the Elo scores of the sketches. These scores are then used by the evolutionary algorithm to sample prior sketches from the database, constructing an overall prompt -- which includes any optional inputs from the mathematician -- to condition new episodes \textbf{(1)}.}
    \label{fig:detailed_system}
\end{figure}



Separately, we developed an evolutionary agent (C), inspired by AlphaEvolve \cite{novikov2025alphaevolve}, in which prover subagents sample from and contribute to a shared population database of sketches. A challenge here is the mismatch between evolutionary algorithms, which typically assume a graduated fitness landscape, and formal proof evaluation, which is inherently binary. To bridge this gap, we used a pool of \emph{rating agents} (based on the less expensive Gemini 3.0 Flash) to construct relative rankings of sketches based on their plausibility, clarity, and novelty. We aggregated these rankings into Elo ratings for the sketches and used a sampling procedure based on the P-UCB formula \cite{hubert2021learning,silver2017masteringchessshogiselfplay} to drive the search. 

Finally, we combined the {\AP} and evolution capabilities into a ``full-featured'' agent (D; see Fig.~\ref{fig:detailed_system}) in which prover subagents can use {\AP} as well as evolutionary search. We used this agent as the instrument in our exploration of open research problems.
