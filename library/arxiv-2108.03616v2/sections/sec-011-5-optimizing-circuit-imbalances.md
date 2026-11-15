---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-011-5-optimizing-circuit-imbalances
section_title: "Optimizing circuit imbalances"
section_number: 5
pages: 18-20
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.981
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
\label{subsec:def_chi_bar_star}
Recall that $\bD_n$ is the set of  $n\times n$ positive definite diagonal matrices. For  every $D\in \bD_n$, $AD$ represents a column rescaling. This is a natural symmetry in linear programming, and particularly relevant in the context of interior point algorithms, as discussed in Section~\ref{sec:LLS}.

 The condition number $\Le_{AD}$ may vastly differ from $\Le_{A}$. In terms of the subspace $W=\ker(A)$, this amounts to rescaling the subspace by $D^{-1}$; we denote this by $D^{-1}W$. It is natural to ask for the best possible value that can be achieved by rescaling:
\[
\Le_W^* = \inf\left\{ \Le_{DW}:\,  D \in \bD_n\right\}\, .
\]
In most algorithmic and polyhedral results in this paper, the $\Le_W$ dependence can be replaced by $\Le^*_W$ dependence. For example, the diameter bound in Theorem~\ref{thm:kappa-diameter} is true in the stronger form with $\Le^*_W$, since the diagonal rescaling maintains the geometry of the polyhedron.

Even the value $\Le^*_W$ can be arbitrarily large.
As an example, let $W\subseteq \R^4$ be defined as $W=\spn\{(0,1,1,M),(1,0,M,1)\}$. Both generating vectors are elementary, and we see that $\Le_W=M$. Rescaling the third and fourth coordinates have opposite effect on the two elementary vectors, therefore we also have $\Le_{W}^*=M$, i.e. the original subspace is already optimally rescaled.

A key result in  \cite{DHNV20} shows that an approximately optimal rescaling can be found:
\begin{theorem}[\cite{DHNV20}]\label{thm:bar-chi-star}
There is an $O(n^2m^2 + n^3)$ time algorithm that for any matrix $A\in\R^{m\times n}$, computes an estimate $\xi$ of $\kappa_A$ such that
\[
\xi \leq \kappa_A \leq  (\kappa_A^*)^2 \xi
\]
and a $D\in \bD_n$ such that
\[
\kappa^*_A\le \kappa_{AD}\le (\kappa_A^*)^3\, .
\]
\end{theorem}
This is in surprising contrast with the inapproximability result Theorem~\ref{thm:chi-inapprox}. 
Note that there is no contradiction since the approximation factor $(\kappa_A^*)^2$ is not bounded as $2^{\mathrm{poly}(n)}$ in general.

The key idea of the proof of Theorem~\ref{thm:bar-chi-star} is to analyze the pairwise imbalances $\Le_{ij}=\Le^W_{ij}$ introduced in Section~\ref{sec:self-dual}.
In the 4-dimensional example above, we have $\kappa_{34}=\kappa_{43}=M$. Let $D\in {\mathbf D}$ and let $d\in\R^n$ denote the diagonal elements; i.e. the rescaling multiplies the $i$-th coordinate of every $w\in W$ by $d_i$.
Then, we can see that $\Le^{DW}_{ij}=\Le_{ij}d_j/d_i$.
In particular, for any pair of variables $i$ and $j$, $\Le^{DW}_{ij}\Le^{DW}_{ji}=\Le_{ij}\Le_{ji}$. Consequently, we get a lower bound $\Le_{ij}\Le_{ji}\le(\Le^*_W)^2$.

Theorem~\ref{thm:bar-chi-star} is based on a 
combinatorial min-max characterization that extends this idea. For the rest of this section, let us assume that the matroid ${\cal M}(W)$ is non-separable. In case it is separable, we can obtain $\kappa^*_W$ by taking a maximum over the non-separable components. 

Let  $G=([n],E)$ be the complete directed graph on $n$ vertices with 
edge weights $\kappa_{ij}$. Since ${\cal M}(W)$ is assumed to be non-separable, Proposition~\ref{prop:conn} implies that $\kappa_{ij}>0$ for any $i,j\in [n]$.
We will refer to this weighted digraph as  the \emph{circuit ratio digraph}.

Let $H$ be a \emph{cycle} in $G$, that is, a sequence of indices
$i_1,i_2,\dots,i_k, i_{k+1} = i_1$. We use $|H|=k$ to denote the
length of the cycle. (In this terminology, \emph{cycles}  refer to objects in $G$, whereas
\emph{circuits} to objects in $\circuits_W$.)

We use the notation $\Le(H)=\Le_W(H)=\prod_{j=1}^k \Le^W_{i_j
  i_{j+1}}$. The observation for length-2 cycles remains valid in general: $\Le(H)$ is invariant under any rescaling. This leads to the lower bound $(\Le(H))^{1/|H|}\le \kappa^*_W$. The
 best of these bounds turns out to be tight:
\begin{theorem}[\cite{DHNV20}]\label{thm:circuit-min-max}
For a subspace $W\subseteq \R^n$, we have
\[
\Le_W^* = \max\left\{\Le_W(H)^{1/|H|}:\ \mbox{$H$ is a cycle in $G$}\right\}\, .
\]
\end{theorem}
The proof relies on the following formulation:
\begin{align}\label{eq:min-mean-cycle-mult}
\begin{aligned}
    \Le^*_W=&&\min \; & t \\
            &&\Le_{ij}d_j/d_i & \leq t \quad \forall (i,j) \in E, \\
            &&d &> 0.
\end{aligned}
\end{align}
Taking logarithms and substituting $z_i=\log d_i$, we can rewrite this problem equivalently as
\begin{equation}\label{eq:min-mean-cycle}
\begin{aligned}
\min \; & s \\
\log \Le_{ij} + z_j - z_i & \leq s \quad \forall (i,j) \in E, \\
z &\in \R^n.
\end{aligned}
\end{equation}
This is the dual of the minimum-mean cycle problem with weights $\log\Le_{ij}$, and can be solved in polynomial time (see e.g. \cite[Theorem 5.8]{amo}).

Whereas this formulation verifies Theorem~\ref{thm:circuit-min-max}, it does not give a polynomial-time algorithm to compute $\Le^*_W$. In fact, the values $\Le_{ij}$ are already NP-hard to approximate due to Theorem~\ref{thm:chi-inapprox}. Nevertheless, the bound $\Le_{ij}\Le_{ji}\le(\Le^*_W)^2$ implies that for any elementary vector $g^C$ with support $i,j\in C$, we have 
\begin{equation}\label{eq:hat-sandwich}
\frac{\Le_{ij}}{(\Le^*_W)^2}\le \frac{1}{\Le_{ji}} \le \left|\frac{g_j}{g_i}\right|\le \Le_{ij}\, .
\end{equation}

To find an efficient algorithm as in Theorem~\ref{thm:bar-chi-star},
we  replace the exact values $\Le_{ij}$ by estimates $\hat\Le_{ij}$ obtained as $|g^C_j/g^C_i|$ for an arbitrary circuit $C\in\circuits_W$ with $i,j\in C$; these can be obtained using standard techniques from linear algebra and matroid theory. 
Thus, we can return $\xi=\max_{(i,j)\in E}\hat\Le_{ij}$ as the estimate on the value of $\Le_A$. To estimate $\kappa^*_A$, we solve \eqref{eq:min-mean-cycle} with the estimates $\hat\Le_{ij}$ in place of the $\Le_{ij}$'s.
