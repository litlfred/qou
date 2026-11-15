---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-009-23-analytic-torsion
section_title: "Analytic torsion"
section_number: 2.3
pages: 14-15
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.992
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
[]{#sec:analytic label="sec:analytic"}

Consider now a smooth compact manifold $M$ and a representation $$\rho\colon\pi_1M\to \mathrm{SL}_n(\mathbb{R}).$$ The manifold $M$ has a unique $\mathcal C^1$-triangulation, so one can view it as a CW-complex and compute its torsion. Consider the associated flat bundle $$\label{eqn:flabundle}
E_\rho=\widetilde M\times \mathbb{R}^n/\pi_1M,$$ where $\pi_1M$ acts on the universal covering $\widetilde M$ by deck transformations and on $\mathbb{R}^n$ via $\rho$. The space of $E_\rho$-valuated differential forms is denoted by $\Omega^p(E_\rho)$, and its de Rham cohomology by $H^*(M;E_\rho)$. To simplify, we assume that $\rho$ is acyclic, namely, by de Rham theorem we assume that $$\label{eqn:deRham}
H^*(M;E_\rho)\cong H^*(M;\rho)=0.$$ We choose a Riemannian metric $g$ on $M$ and a metric $\mu$ on the bundle $E_\rho$ (notice that since we do not assume $\rho$ to be orthogonal, perhaps the metric $\mu$ cannot be chosen to be flat). This yields a metric on $\Omega^p(E_\rho)$. Using it, we may define the adjoint to the differential and the Laplacian $\Delta_p(\rho)$ on $\Omega^p(E_\rho)$. As it is an elliptic operator, it has a discrete spectrum $0 < 
\lambda_0\leq\lambda_1\leq\cdots\to\infty$. The zeta function is defined on the complex half-plane $\operatorname{Re}(s)\geq 
n/2$: $$\zeta_p(s)=\sum_{\lambda_i}\lambda_i^{-s}$$ and it extends to the a meromorphic function on the complex plane, homomorphic at $s=0$.

::: definition
The analytic torsion is defined as: $$\operatorname{tor}_{an}(M,\rho,g,h)=\exp\Big( \frac12 \sum_{p=0}^{\dim M} (-1)^p \,p 
\zeta_p'(0)  \Big).$$
:::

In [@Muller93] Müller proves that if $\dim M$ is odd and, as we assume $\rho$ is acyclic, then it is independent of $g$ and $h$. It can also be defined using the trace of the heat operator: $$\begin{gathered}
\label{eqn:traceheatkernel}
\operatorname{tor}_{an}(M,\rho)  =  \\ \exp\left(  \frac12 \sum_{p=0}^{\dim M} (-1)^p p 
\frac{d\phantom{s}}{d s} 
\left.\left( 
\frac{1}{\Gamma(s)}
\int_0^\infty 
\left(  \operatorname{Tr}( e^{-t \Delta_p(\rho)} )  t^{s-1}  d\, t \right)
\right) \right|_{s=0}  \right)\, .
\end{gathered}$$

In the following theorem notice that we use the convention for Reidemeister torsion opposite to the usual in analytic torsion.

::: thm
Let $M$ be a closed hyperbolic manifold of odd dimension and $\rho\colon\pi_1(M)\to \mathrm{SL}_n(\mathbb{R})$. Then $$\operatorname{tor}_{an}(M,\rho)=\frac{1}{\vert \operatorname{tor}(M,\rho)\vert}.$$
:::

This theorem was first proved by Cheeger [@Cheeger79] and Müller [@Muller78] independently for orthogonal representations, and later by Müller [@Muller93] for unimodular ones. In addition, aciclycity of $\rho$ is not required by choosing orthonormal harmonic basis in cohomology.

This subsection concludes recalling a theorem of Fried. Let $\rho\colon\pi_1 M\to \operatorname{SO}(n)$ be a representation of a hyperbolic manifold. For $s\in\mathbb{C}$ with $\operatorname{Re}(s)$ sufficiently large, consider $$R_\rho(s)=\prod_\gamma\det(\operatorname{Id}-\rho(\gamma) e^{-s \, l(\gamma)})$$ where the product runs over the prime, closed geodesics of $M$ and $l(\gamma)$ denotes the length of $\gamma$. This is called the Ruelle zeta function.

::: thm
[]{#thm:Fried label="thm:Fried"} Let $M$ be a closed hyperbolic manifold of odd dimension and assume that $\rho\colon\pi_1 M\to \operatorname{SO}(n)$ is acyclic. Then $R(s)$ extends meromorphically to $\mathbb{C}$ and $$R_\rho(0)=\operatorname{tor}_{an}(M,\rho)^2.$$
:::

This theorem has been extended by Wotzke [@Wot08] to other representations of hyperbolic manifolds, see also [@Muller12].
