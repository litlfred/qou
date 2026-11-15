---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-002-systematic-evaluation-on-open-problems
section_title: "Systematic Evaluation on Open Problems"
section_number: null
pages: 4-6
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
text_source: latex
latex_prose_ratio: 0.787
latex_coverage_ratio: 0.77
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
\paragraph{{\erdos} Problems.} 

Bloom maintains an online catalog \cite{erdosproblems} of over 1200 open problems posed by Paul {\erdos} and his collaborators.
The open-source Formal Conjectures repository \cite{deepmind2026formalconjectures} contains Lean formalizations of a subset of these problems.
We ran Agent (D) on all these formal statements (353 at the time of the run), terminating the search if no proof was found within 3000 episodes. The agent solved 9/353 problems (Table~\ref{tab:major_results} and supplementary text); after each solve, experts on our team validated that the Lean statement faithfully captured the original conjecture. We have publicly shared the proofs, and our results have been logged on Terence Tao's wiki on AI contributions to {\erdos} problems \cite{TaoErdosWiki}. 

Several proofs require sophisticated constructions and the synthesis of distinct mathematical arguments. For example, problem \#12(i), posed by {\erdos} and S\'ark\"ozy in 1970 \cite{Erds1970OnTD}, asks if there is an infinite set $A$ that satisfies a restrictive divisibility constraint -- no element may divide the sum of two larger elements -- and which satisfies the density condition $\liminf_{N \to \infty} \frac{|A \cap [1, N]|}{\sqrt{N}} > 0$; this problem had received attention in multiple prior works \cite{elsholtz2016erd, SCHOEN2001191, Baier2004ANO}. Our agent constructed $A$ as an infinite union of disjoint ``blocks'' $B_i \subseteq [P_i, 1.1P_i]$ for a suitably rapidly growing sequence $(P_i)$. To satisfy the local divisibility conditions, the proof integrates the Chinese Remainder Theorem with the properties of sets that avoid length-3 arithmetic progressions. 

Problem \#125 concerns the sumset $A+B$, where $A$ is the set of non-negative integers whose base-3 representation uses only the digits 0 and 1, and $B$ is the analogous set in base 4.  
The question of whether the lower density of $(A + B)$ is positive was open since 1996 \cite{BurrErdos125}. 
Our agent resolved the conjecture by synthesizing an inductive thinning argument that exploits the Diophantine proximity of the two multiplicatively independent bases ($3^m \approx 4^k$). 




The agent also served as a tool for detecting and fixing misformalizations. For example, in {\erdos} problems \#125 and \#741(i), the interpretation of ``density'' in the original informal statements was amended to ``lower density'' and ``upper density'' respectively, after our full-featured agent found proofs using density as ``natural density.'' Following the correction of the ambiguity, the agent was still able to resolve the questions.

\noindent \textit{Failure Analysis.} We analyzed the highest-scoring sketches (measured by Elo) across a random sample of problems on which our agent failed. First, the agent frequently offloaded a problem's core difficulty into a single \texttt{sorry} within a helper lemma that reiterated the target statement in a slightly different form. Explicitly prompting against this behavior failed to prevent it. Second, for several problems, the top sketches relied on lemmas marked with \texttt{sorry} that the agent claimed were established results in the mathematical literature. Upon manual inspection, these lemmas proved to be hallucinations. These failure modes underscore the value of end-to-end formal verification.

\paragraph{OEIS.} We also applied the agent to systematically explore open problems in the OEIS \cite{oeis}, a massive repository of integer sequences and their known and open properties. We used Gemini to autoformalize 492 open questions from the OEIS and applied the agent to the resulting Lean statements. As a guard against misformalization, the agent was required to prove ``test lemmas'' verifying the first few terms of each sequence against its formal definition before attempting the target conjectures. The agent found proofs for 44 conjectures that a manual review found to be correctly formalized and previously unproven. Two of the proofs appear in the supplementary material.

\begin{table}[t]
\centering
\footnotesize
\renewcommand{\arraystretch}{1.4}
\setlength{\tabcolsep}{8pt}
\begin{tabular}{l p{6.5cm} p{6.5cm}}
\hline
\textbf{ID} & \textbf{Conjecture Summary} & \textbf{Proof Technique} \\ \hline
12\,(i) & (1970) Existence of $A \subset \mathbb{Z}^+$ s.t.\ $a \nmid (b+c)$ with $|A \cap [1,N]|/\sqrt{N} > \delta > 0$ infinitely often & Block-based construction via CRT and 3-AP avoiding sets \\
12\,(ii) & (1970) Existence of $A \subset \mathbb{Z}^+$ s.t.\ $a \nmid (b+c)$ with $|A \cap [1,N]| \gg N^{1-\epsilon}$ for any $\epsilon$ and $N$ sufficiently large & Block-based construction via CRT and 3-AP avoiding sets \\
125 & (1996) $\{ \sum \epsilon_k 3^k | \epsilon_k \in \{0,1\}\} + \{ \sum \epsilon_j 4^j | \epsilon_j \in \{0,1\}\}$ has lower density zero & Inductive thinning via Diophantine approx. $3^m \approx 4^k$  \\
138$^*$ & (1981) Van der Waerden numbers satisfy $W(k{+}1) - W(k) \to \infty$ & Greedy coloring extension with monochromatic intersection lemma \\
152 & (1994) Sufficiently large Sidon sets $A$ contain many isolated points in $A+A$ & Elementary argument by bounds on interior points, shifted neighbors and quadruples \\
741\,(i) & (1994) If $A + A$ has upper density, there exists a decomposition $A = A_1 \sqcup A_2$ s.t. $A_1 + A_1, A_2 + A_2$ have positive upper density & Bounding of upper density of $A_i + A_i$ via cases on upper density of $A$ \\
741\,(ii) & (1994) Existence of a basis $A$ of order $2$ with $A_1 + A_1$, $A_2 + A_2$ having bounded gaps for all $A_1, A_2$ such that $A = A_1 \sqcup A_2$ &  Explicit construction via rapidly growing sequence \\
846 & (1992) Existence of infinite set $A$ such that any finite subset contains many non-collinear points, but is not a finite union of non-collinear sets & Label $K_\infty$ vertices with terms from fast-growing sequence, apply map on edges $\{i,j\} \mapsto (x_i + x_j, x_i^2 + x_ix_j + x_j^2)$ to obtain $A$ \\
26$^{*, \dagger}$ & (1995) Existence of $A$ such that upper density of $A+k$ is $< 1 - \frac{1}{4}$ for all naturals $k$ & Block-based construction using increasing sequence of primes, CRT, and bounding u. density by cases \\
\hline
\end{tabular}
\caption{\textbf{Open problems from the ErdosProblems repository autonomously resolved by our full-featured agent.} The asterisk indicates a variant of the main problem with this number. Problem \#26 (annotated with $\dagger$) is a more general variant of a question posed by {\erdos}, but was not posed by {\erdos} himself.}
\label{tab:major_results}
\end{table}
