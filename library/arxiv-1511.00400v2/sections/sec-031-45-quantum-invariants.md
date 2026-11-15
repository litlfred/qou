---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-031-45-quantum-invariants
section_title: "Quantum invariants"
section_number: 4.5
pages: 35-36
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.987
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
When $(k_1,k_2)=(2,0)$, $\operatorname{Sym}^2$ is the adjoint representation and its torsion occurs in the volume conjecture.

The role of the torsion in the expansion of the path integral is already mentioned in the work of Witten [@Witten89] and Bar-Natan Witten [@BNW91]. Of course the work of Kashaev [@Kashaev97] and Murakami-Murakami [@MM01] play a key role in the conjecture.

For a knot $\mathcal K$, let $J_N(\mathcal K;z)$ denote the colored Jones polynomial of $\mathcal K$. If the knot is hyperbolic, let $u$ denote Thurston's parameter of the Dehn filling space (Definition [\[def:cs\]](#def:cs){reference-type="ref" reference="def:cs"}). Denote the corresponding character by $\chi_u$ and let $\operatorname{CS}(\mathcal K,\chi_u)$ denote the $\mathbb{C}$-valued Chern-Simons invariant of a representation with character $\chi_u$, namely the real part is minus the Chern-Simons invariant and the imaginary part is the volume of the representation. The following version is taken from [@Murakami13] by H. Murakami, who attributes it to [@GM08; @DG11].

::: conj
Let $K$ be a hyperbolic knot. There exists a neighborhood $U\subset\mathbb{C}$ of the origin such that for $u\in U- \pi i \mathbb{Q}$, we have the following asymptotic equivalence: $$J_n(\mathcal K;e^{\frac{2\pi i+u}{N}}) \, \underset{N\to\infty}{\sim}\, 
\frac{\sqrt{-\pi}}{2\sinh(\frac{u}{2})} \left( {\mathbb{T}}^{2}_{\mathcal 
K,m}(\chi_{u}) \right)^{-\frac{1}{2}}
\, \left( \frac{N}{2\pi i+u}\right)^{\frac 12} \, e^{\frac{N}{2\pi i+u} 
\operatorname{CS}(\mathcal K,\chi_u)  }$$ where $m$ denotes the meridian of the knot.
:::

Again this paper uses a different convention for torsion from [@Murakami13] and the other references, as it is the opposite to the convention for analytic torsion. It has been checked for the figure eight knot and $u$ real, $0<  u < 
\log((3+\sqrt{5})/2)$ by Murakami in [@Murakami13]. For torus knots, the volume is zero, but not the Chern Simons invariant nor the torsion, and the asymptotic computations of Dubois-Kashaev [@DK07] and Hikami-Murakami [@HM11] support the corresponding conjecture for torus knots.

Related to this conjecture, the torsion is also involved in a potential function, introduced by Yokota [@Yokota03]. From a diagram of the projection of a knot $\mathcal K$, in [@OT15] Ohtsuki and Takata define $\omega_ 2(\mathcal K)^{-1}$ as the modified Hessian of the potential function of the diagram. They justify (formally) that $\sqrt{\omega_ 2(\mathcal K)}$ is the term that appears in the asymptotic development of the Kashaev invariant and therefore they conjecture $$\frac{1}{\omega_ 2(\mathcal K)}= \pm { 2\,i  \, {\mathbb{T}}^{2}_{\mathcal K,m}(\chi_{\varrho})}.$$ In [@OT15] they prove that the conjecture holds true for two bridge knots.

There is also a remarkable contribution of Dimofte and Garoufalidis [@DG13], that define an invariant from an ideal triangulation of a knot exterior and an enhanced Neumann-Zagier datum. Enhanced Neumann-Zagier datum means that, besides the complex collection shape parameters of the ideal hyperbolic tetrahedra, they use matrices with integer coefficients that describe how to glue the tetrahedra and a collection of integers that code a combinatorial flattening (introduced in [@Neumann90] by Neumann to calculate the Chern-Simons invariant combinatorially). Form these data, Dimofte and Garoufalidis construct an invariant of the hyperbolic manifold and they check numerically that it equals ${1}/{{\mathbb{T}}^{2}_{\mathcal K,m}(\chi_{\varrho})}$ up to some constant.
