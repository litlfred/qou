---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-017-73-the-curvature-of-the-central-path
section_title: "The curvature of the central path"
section_number: 7.3
pages: 28-28
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.978
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
The condition number $\bar\chi_A^*$ also has an interesting connection to the geometry of the central path. In this context, Sonnevend, Stoer, and Zhao~\cite{Sonnevend1991} introduced a primal-dual curvature notion. 
Monteiro and
Tsuchiya~\cite{Monteiro2008} reveal strong connections between the curvature integral, the Mizuno-Todd-Ye predictor-corrector algorithm, and the Vavasis-Ye algorithm. In particular, they prove a bound 
$O(n^{3.5} \log(\bar{\chi}^*_A+n))$ on the curvature integral.

Besides the above primal-dual curvature, one can also study the \emph{total curvature} of the central path, a standard notion in algebraic geometry. De Loera, Sturmfels, and Vinzant \cite{Loera2012} studied the \emph{central curve} defined as the solution of the polynomial equations
\begin{equation}\label{eq:central-curve}
Ax=b\, ,\quad A^\top y-s=c\, \quad x_i s_i=\lambda\, \quad \forall i\in[n],\quad 
\end{equation}
This includes the usual central path in the region $x,s>0$, but also includes the central path of all other LPs with objective $c$ in the hyperplane arrangement in $\{x\in\R^n:\, Ax=b\}$ defined by the hyperplanes $x_i=0$; i.e., all LPs where some nonnegativity constraints $x_i\ge 0$ are flipped to $x_i\le 0$.
 In fact, \cite{Loera2012} shows thato \eqref{eq:central-curve} defines the smallest algebraic variety containing the central path.
 
 They consider the average curvature taken over the bounded regions in the hyperplane arrangement, and show a bound $2\pi(n-m-1)$ for the primal central path (i.e., the projection of \eqref{eq:central-curve} to the $x$ space), and $2\pi(m-1)$ for the dual central path (the projection to the $s$ space). Their argument crucially relies on circuit polynomials defined via elementary vectors.
  See \cite{Loera2012} for further pointers to the literature on the total curvature of the central path.
