---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-031-82-periodic-and-freely-periodic-knots
section_title: "Periodic and freely periodic knots"
section_number: 8.2
pages: 26-27
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.98
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:periodic}

A knot $K\subset S^3$ is called \emph{periodic of period $q$}, if there exists a smooth transformation of $S^3$ of order $q$ which leaves $K$ invariant and such that the fixed point set is a circle $A$ disjoint from $K$.
Note that $A\subset S^3$ is the trivial knot by the Smith conjecture. We refer to \cite[Section~10.1]{Ka96} for more details on periodic knots.

Now assume that $K\subset S^3$ is a periodic knot of period $q$ with $A$ the fixed point set of $f:S^3\to S^3$.
Note that $S^3/f$ is diffeomorphic to $S^3$. We denote by $\pi$ the projection map $S^3\to S^3/f=S^3$ and we  write $\overline{K}=\pi(K), \overline{A}=\pi(A)$.

The following two theorems of Hillman, Livingston and Naik \cite[Theorems~3~and~4]{HLN06}
generalize  results of Trotter \cite{Tr61} and Murasugi \cite{Mu71}.


\begin{theorem}
Let $K$ be a periodic knot of period $q$. Let $\pi, A, \overline{A}$ and $\overline{K}$ as above.
Let $\overline{\gamma}:\pi_1(S^3\setminus \nu \overline{K})\to \mbox{GL}(n,R)$ a representation with $R=\mathbb{Z}$ or $R=\mathbb{Q}$.  Write $\gamma =\overline{\gamma}\circ \pi_*$.
Then there exists a polynomial $F(t,s)\in R[t^{\pm 1}, s^{\pm 1}]$ such that
\[ \Delta_K^{\gamma}(t) \doteq \Delta_{\overline{K}}^{\overline{\gamma}}(t) \prod_{k=1}^{q-1} F(t,e^{2\pi ik/q}).\]
\end{theorem}

In the untwisted case the polynomial $F(t,s)$ is just the Alexander polynomial of the ordered link $\overline{K}\cup \overline{A}\subset S^3$. We refer to \cite[Section~6]{HLN06} for more information on $F(t,s)$.
The following theorem gives an often stronger condition when the period is a prime power.

\begin{theorem}
Let $K$ be a periodic knot of period $q=p^r$ where $p$ is a prime. Let $\pi, A, \overline{A}$ and $\overline{K}$ as above.
Let $\overline{\gamma}:\pi_1(S^3\setminus \nu \overline{K})\to \mbox{GL}(n,\mathbb{Z}_p)$ be a representation. Write $\gamma =\overline{\gamma}\circ \pi_*$. If $\Delta_{K}^\gamma(t)\ne 0$, then
\[ \Delta_{K}^\gamma(t) \cdot \left(\Delta_{K,0}^\gamma(t)\right)^{q-1} \doteq \Delta_{\overline{K}}^{\overline{\gamma}}(t)^q\,
\left(\det\left(\mbox{id}_n-\gamma(A)t^{lk(K,A)}\right)\right)^{q-1}\, \in \mathbb{Z}_p[t^{\pm 1}],  \]
where we view $A$ as an element in $\pi_1(S^3\setminus \nu K)$.
\end{theorem}

(Note that Elliot \cite{El08} gave an alternative proof for this theorem.)
These theorems are applied in \cite[Section~10]{HLN06} to give obstructions on the periodicity of the Kinoshita--Terasaka knot and the Conway knot. Note that both knots have trivial Alexander polynomial, in particular Murasugi's obstructions are satisfied trivially.

A knot $K\subset S^3$ is called \emph{freely periodic of period $q$} if there exists a free transformation $f$ of $S^3$ of order $q$ which leaves $K$ invariant. We refer to \cite[Section~10.2]{Ka96} for more information on freely periodic knots. Given  such a freely periodic knot $K$ we denote by $\pi$ the projection map $S^3\to \Sigma\mathrel{\mathop:}=S^3/f$ and we  write $\overline{K}=\pi(K)$.

The following theorem is \cite[Theorem~5]{HLN06}; the untwisted case was first proved by
 Hartley \cite{Hat81}.


\begin{theorem}
Let $K$ be a freely periodic knot of period $q$.
Let $\pi, \S$  and $\overline{K}$ as above.
Let $\overline{\gamma}:\pi_1(\S \setminus \overline{K})\to \mbox{GL}(k,R)$ be a representation with $R$ a Noetherian UFD.
Write $\gamma =\overline{\gamma}\circ \pi_*$.
Then
\[ \Delta_{K}^\gamma(t^q) \doteq \prod_{k=0}^{q-1} \Delta_{\overline{K}}^{\overline{\gamma}}(e^{2\pi ik/q}t).\]
\end{theorem}

We refer to \cite[Section~11]{HLN06} for an application of this theorem to a case which could not be settled with Hartley's theorem.
