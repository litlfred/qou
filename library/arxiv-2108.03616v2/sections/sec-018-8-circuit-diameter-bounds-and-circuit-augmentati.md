---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-018-8-circuit-diameter-bounds-and-circuit-augmentati
section_title: "Circuit diameter bounds and circuit augmentation algorithms"
section_number: 8
pages: 28-29
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 1.0
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{sec:augment}
Consider an LP in standard equality form with upper  bounds, where $A\in \R^{m\times n}$, $b\in \R^m$, $u\in \R^n$:
\begin{equation}
\label{LP-augment}\tag{LP$(A,b,c,u)$}
\begin{aligned}
\min \; & \pr{c}{x} \\ 
Ax&=b \\
0\leq x&\leq u\,\\
\end{aligned}
\end{equation}

In Section~\ref{sec:delta} we briefly mentioned the Hirsch conj\-ecture and some progress towards the polynomial Hirsch conjecture; in Theorem~\ref{thm:kappa-diameter} shows a bound $O((n-m)^3m\Le_A\log(\Le_A+n))$ on the diameter of $\{x\in \R^n:\, Ax=b,x\ge 0\}$ for $A\in\R^{m\times n}$.

\emph{Circuit diameter bounds} were introduced by Borgwardt, Finhold, and Hemmecke~\cite{Borgwardt2015} as a relaxation of diameter bounds. Let $P$ denote the feasible region of \ref{LP-augment}.
A \emph{circuit walk} is a set of consecutive feasible points $x^{(1)},x^{(2)},\ldots,x^{(k+1)}\in P$ such that for each $t=1,\ldots,k$, $x^{(t+1)}=x^{(t)}+g^{(t)}$ for $g^{(t)}\in \EE(A)$, and further, 
$x^{(t)}+(1+\varepsilon) g^{(t)}\notin P$ for any $\varepsilon>0$, i.e., each consecutive circuit step is \emph{maximal}. The \emph{circuit diameter} of $P$ is the minimum length of a circuit walk between any two vertices $x,y\in P$. 

In contrast to walks in the vertex-edge graph, circuit walks are non-reversible and the minimum length from $x$ to $y$ may be different from the one from $y$ to $x$; this is due to the maximality requirement. The circuit-analogue of the Hirsch conjecture, formulated in \cite{Borgwardt2015}, asserts that the circuit diameter of a polytope in $d$ dimensions with $n$ facets is at most $n-d$; this  may be true even for unbounded polyhedra, see \cite{Borgwardt2018circuit}.

In this section we begin by showing a recent, improved bound on the circuit diameter with $\log \kappa_A$ dependence. Section~\ref{subsec:circ-diameter-algorithms} gives an overview of  circuit augmentations algorithms. We review existing algorithms for different augmentation rules (Theorem~\ref{thm:DLHL} and Theorem~\ref{thm:opt-augment}), and also show a new bound for the steepest-descent direction (Theorem~\ref{thm:steepest-main}). The bounds in these three theorems also translate directly to circuit diameter bounds, since they all consider algorithms with maximal augmentation sequences.
