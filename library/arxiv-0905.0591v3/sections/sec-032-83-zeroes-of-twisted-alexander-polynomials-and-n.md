---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-032-83-zeroes-of-twisted-alexander-polynomials-and-n
section_title: "Zeroes of twisted Alexander polynomials and non–abelian representations"
section_number: 8.3
pages: 27-28
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.945
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
Let $N$ be a 3--manifold with one boundary component and $b_1(N)=1$.
Put differently, let  $N$ be the complement of a knot in a rational homology sphere.
Let $\alpha:\pi_1(N)\to \mathbb{C}^*=\mbox{GL}(1,\mathbb{C})$ be a one--dimensional representation.
Note that $\alpha$ necessarily factors through a representation
$H_1(N;\mathbb{Z})\to \mbox{GL}(1,\mathbb{C})$ which we also denote by $\alpha$.
Heusener and Porti \cite{HP05} ask when the abelian representation
\[ \begin{array}{rcl} \rho_{\alpha}: \pi_1(N) &\to & \mbox{PSL}(2,\mathbb{C}) \\
 g&\mapsto &\pm \begin{pmatrix} \alpha(g)^{1/2} &0 \\ 0&\alpha(g)^{-1/2}\end{pmatrix}\end{array} \]
can be deformed into an irreducible representation.

 Denote by $\phi\in \mbox{Hom}(\pi_1(N),\mathbb{Z})=H^1(N;\mathbb{Z})\cong \mathbb{Z}$ a generator.
Pick $\mu \in H_1(N;\mathbb{Z})$ with $\phi(\mu)=1$.
Denote by $\sigma(\alpha,\mu)$ the representation
\[ \begin{array}{rcl} \pi_1(N)&\to & \mbox{GL}(1,\mathbb{C})\\
g &\mapsto & \alpha(g\mu^{-\phi(g)}).\end{array} \]

Heusener and Porti then give necessary and sufficient conditions for $\rho_\alpha$
to be deformable into an irreducible representation in terms of
the order of vanishing of $\Delta_{N}^{\sigma(\alpha,\mu)\otimes \phi}(t)\in \mathbb{C}[t^{\pm 1}]$ at $\alpha(\mu)\in \mathbb{C}^*$.
We refer to \cite[Theorems~1.2~and~1.3]{HP05} for more precise formulations and more detailed results.

Note that this result is somewhat reminiscent of the earlier results of Burde \cite{Bu67} and de Rham \cite{dRh68}  who showed that zeroes of the (untwisted) Alexander polynomial give rise to metabelian representations of the knot group.
We also refer to \cite{SW09e} for another relationship between zeros of twisted Alexander polynomials and the representation theory of knot groups.
