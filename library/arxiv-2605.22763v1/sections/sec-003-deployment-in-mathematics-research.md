---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-003-deployment-in-mathematics-research
section_title: "Deployment in Mathematics Research"
section_number: null
pages: 6-8
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
text_source: latex
latex_prose_ratio: 0.775
latex_coverage_ratio: 0.821
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
\paragraph{Optimization Theory.} Agent (D) resolved an open question in optimization: proving an exact $\mathcal{O}(1/t)$ convergence rate for the Anchored Gradient Descent-Ascent (GDA) algorithm for min-max convex-concave optimization, thereby tightening the slower bound established by \cite{ryu2019ode}. 
The proof departs from continuous-time ordinary differential equations (ODE) analysis used in previous work, instead using a discrete-time recurrence-based approach. The agent did not merely verify a fixed algorithm: we marked the learning schedule as a parameter within an \texttt{EVOLVE-VALUE} block in the input file, allowing the agent to simultaneously search for the schedule and the proof, ultimately discovering a novel parameter choice that yields the stronger guarantee. We previously released a deformalized version of the proof as a preprint \cite{surina2026improvedlastiterateconvergencerate}. 
Subsequent work \cite{cai2026last} has extended this result.

\paragraph{Graph Theory.} The \emph{graph reconstruction conjecture}
\cite{graphreconstruction} is one of the oldest open problems in combinatorics.
It asserts that every finite simple graph with at least three vertices is
determined, up to isomorphism, by the multiset of its vertex-deleted subgraphs,
known as its \emph{deck}.  AlphaEvolve \cite{novikov2025alphaevolve} experiments helped us 
formulate two bipartite variants of the graph reconstruction conjecture, along
with a proposed full reconstruction algorithm.  For
one of these variants, our agent produced a complete proof.  For the full
algorithmic reconstruction statement, the agent generated proof sketches and
strategies that helped clarify the structure of the problem and led to
simplified reformulations of the conjectures originally suggested by
AlphaEvolve.  A paper based on the results of this collaboration is currently
in preparation.

Separately, the agent proved an open graph theory conjecture regarding a bound on the maximum number of leaves over all spanning trees of a graph $G$, relating it to the maximum number, over all vertices $v \in G$, of independent sets in the neighborhood of $v$. The problem was posed by Graffiti \cite{Graffiti}, an automated conjecturing system, in 1996, and points to an interesting future opportunity to close the loop between AI-based conjecturing and proof. 



\paragraph{Algebraic Geometry.} 
We evaluated our full-featured agent on eight algebraic geometry problems, from textbook-style exercises to open research questions on Hilbert functions, solving two of the four open problems. One of these problems had been a well-known open question for approximately fifteen years. This problem concerned pure
$O$-sequences, equivalently the Hilbert functions of monomial Artinian level
algebras \cite{Stanley1978}.  Their shape and positivity properties have
been studied intensively in recent years \cite{BMMNZ2012}.  Although
log-concavity fails for broad families of pure $O$-sequences, the case of codimension $3$ and type $2$ was identified as the principal remaining
open case \cite{Zanello2024}.  The agent's proof establishes log-concavity in
this case; the argument is substantial, using a nontrivial
reformulation of the Hilbert function and a detailed case analysis of the
resulting second-difference inequalities.


\paragraph{Additive Combinatorics.} Our agent helped resolve problem \#57 from Green's well-known list of open conjectures \cite{green2024100}. The problem asks whether two specific quadratically structured function spaces coincide. The functions of interest map elements of an Abelian group $G$ to the complex numbers. Here, our agent autonomously solved a variant of the problem in which the functions are real-valued, but a personal communication from Green clarified that the complex-valued case was the intended challenge. While the agent could not immediately prove the intended version of the problem, numerical heuristics using floating-point arithmetic provided a candidate counterexample (the cyclic group $\mathbb{Z}/3\mathbb{Z}$ and a specific separating functional). We formalized the problem of whether this counterexample disproves the correct conjecture, and the agent autonomously proved that it indeed does. A paper on the result is in the works \cite{firsching2026strict}. 

\paragraph{Quantum Optics.} With Mario Krenn, we investigated a set of quantum optics problems concerning the existence of monochromatic quantum graphs with $N$ vertices and $d$ colors drawn from domains such as the reals, the complex numbers, and $\{-1, 0, 1\}$. These constructions correspond to $N$-particle quantum states with local Hilbert space dimension $d$ -- in particular, high-dimensional Greenberger–Horne–Zeilinger (GHZ) states realizable via linear optics \cite{Krenn_2017}. Our agent resolved multiple conjectures of this form, in particular with $N = d \in \{4,6,10\}$. A paper on these results is in preparation \cite{Krenn2026TensorAlgebraic}.   


\begin{figure}[htbp]
    \centering
    \includegraphics[width=1\textwidth]{assets/scaling_plot_erdos_main_with_labels.pdf} 
    \caption{\textbf{Solve rate versus mean inference cost (USD) across six {\erdos} problem instances.} The solve rates are evaluated for the four agents: (A) basic (blue circles), (B) basic with {\AP} (orange squares), (C) basic with evolution (green diamonds), and (D) full-featured (red triangles). Numeric annotations denote the number of independent attempts $K \in \{1,3,6,10\}$ grouped together; error bars indicate one standard error interval. Due to their higher costs, agents (C) and (D) lack variance estimates, as independent attempts were used to obtain a single point estimate (see main text for details). For agents (A) and (B), each curve traces the cost–performance Pareto frontier as $K$ increases, revealing diminishing marginal returns at higher budgets. Agent (B) generally matches or exceeds the solve rate of the basic configuration at comparable cost. Costs reported for (B) and (D) do not include the inference cost of {\AP}. While for most problems configuration (A) or (B) is the best, for some challenging problems like {\erdos} \#125, the full-featured configuration (D) performs significantly better. Note that accounting for the estimated {\AP} cost of 60 USD does not change the above outcomes beyond the margin of error.}
    \label{fig:scaling_plot_erdos_main}
\end{figure}
