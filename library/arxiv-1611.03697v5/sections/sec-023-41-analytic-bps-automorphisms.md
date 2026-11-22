---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-023-41-analytic-bps-automorphisms
section_title: "Analytic BPS automorphisms"
section_number: 4.1
pages: 15-17
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.892
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
\label{ref}
We begin by summarising  some basic analytic facts which are proved in Appendix \ref{converge}. 
Let $(\Gamma, Z, \Omega)$ be a  BPS structure, let  $\bT$ be the associated twisted torus, and fix an acute sector $\Delta\subset \bC^*$. For each real number $R>0$ define the open subset $U_\Delta(R)\subset \bT$  to be the interior of the subset
\[\big\{g\in \bT: Z(\gamma)\in \Delta \text{ and } \Omega(\gamma)\neq 0\implies |g(\gamma)|<\exp(-R\|\gamma\|)\big\}\subset \bT.\]
It follows from the support property that the subset $U_\Delta(R)\subset \bT$ is non-empty (see Lemma \ref{dyl}).
Recall the definition of the height of a ray $\ell\subset \bC^*$ from Section \ref{raydiagram}. 
 
\begin{prop}
\label{propy}
Let $(\Gamma, Z, \Omega)$ be a convergent BPS structure, and $\Delta\subset \bC^*$ a convex sector.
For sufficiently large $R>0$ the following statements hold:
\begin{itemize}
\item[(i)] For each ray $\ell\subset \Delta$, the series \eqref{hamiltonian} defining $\DT(\ell)$ is absolutely convergent on $U_\Delta(R)$, and hence defines a holomorphic function \[\DT(\ell)\colon U_\Delta(R)\to \bC.\]
\item[(ii)] The time 1 Hamiltonian flow of the function $\DT(\ell)$  with respect to the Poisson structure $\{-,-\}$ on $\bT$ defines a holomorphic  embedding
\[\bS(\ell)\colon U_\Delta(R)\to \bT.\]
\item[(iii)] For each $H>0$, the composition in anti-clockwise order
\[\bS_{<H}(\Delta) = \bS_{\ell_1} \circ \bS_{\ell_2} \circ \cdots \circ \bS_{\ell_k},\]
 corresponding to the finitely many rays $\ell_i\subset \Delta$ of height $< H$ exists, and  the pointwise limit \[\bS(\Delta)=\lim_{H\to \infty} \bS_{<H}(\Delta) \colon U_\Delta(R)\to \bT\]
is a well-defined  holomorphic embedding. 
\end{itemize}
\end{prop}

\begin{proof}
See Appendix \ref{converge}, Proposition \ref{prop}.
\end{proof}

We think of the maps $\bS(\ell)$  of Proposition \ref{propy} as  being partially-defined automorphisms of the twisted torus $\bT$. We will usually restrict attention to BPS structures which, in the terminology of Section \ref{defns}, are ray-finite, generic and integral. The maps  $\bS(\ell)$ can then be computed using the following result.

\begin{prop}
\label{barneyy}
 Suppose that $(\Gamma, Z, \Omega)$ is ray-finite, generic and integral.  Then for any ray $\ell\subset \bC^*$ the   embedding  $\bS(\ell)$ of Proposition \ref{propy} extends to a birational automorphism of $\bT$, whose action on twisted characters is given by 
\begin{equation}\bS(\ell)^*(x_\beta)=x_\beta\cdot \prod_{Z(\gamma)\in \ell}(1-x_\gamma)^{\,\Omega(\gamma)\<\gamma,\beta\>}.\end{equation}
\end{prop}

\begin{proof}
See Appendix  \ref{converge}, Proposition \ref{barney}.
\end{proof}


Note that if the BPS structure $(\Gamma,Z,\Omega)$ satisfies the stronger condition of being finite, then there are only finitely many active rays, so for any acute sector $\Delta\subset \bC^*$ the map $\bS(\Delta)$ of Proposition \ref{propy} also extends to a birational automorphism of $\bT$.
