---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-025-41-refined-quantum-mirror-curves
section_title: "Refined quantum mirror curves"
section_number: 4.1
pages: 58-59
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.987
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
In this section we derive the refined quantum curves relevant in the context of the open BPS state counting (or topological string theory). They can be regarded as refined and quantum versions of mirror curves $A(x,y)=0$ which appear in the mirror geometry ([\[Amirror\]](#Amirror){reference-type="ref" reference="Amirror"}) for toric three-folds. Specifically, we consider open refined topological string amplitudes for branes along preferred directions, in general framing, for ${\mathbb C}^3$ and conifold geometries. It brings only some technical, but no conceptual challenges to generalize the computations below to the case of "generalized conifolds" (*i.e.* toric three-folds without compact 4-cycles). To find quantum curves in the present context, in this section we derive the refined open topological string amplitudes $Z_{\text{BPS}}^{\text{open}}$ and find difference equations which they satisfy. Then, in the next section we consider the classical limit $q_2 \to 1$ of the quantum curve, show that it is equivalent to the saddle point analysis of $Z_{\text{BPS}}^{\text{open}}$, and describe properties of the resulting refined mirror curves.

### ${\mathbb C}^3$ or tetrahedron

To start with, we consider the simplest toric geometry of ${\mathbb C}^3$, in arbitrary framing $f$. Its ordinary mirror curve -- which is equivalent to the "single tetrahedron" curve from the perspective of hyperbolic geometry and knot theory -- takes the form [@abmodel]: $$A^{\text{ref}} (x,y; q_1=1) \; = \; 1 - y + x(-y)^f = 0 \,.    \label{mirrorC3f}$$ To find the refined and quantum generalization of this curve we consider the refined BPS partition function in ${\mathbb C}^3$ geometry with a D-brane located along the preferred direction. In arbitrary framing such an amplitude reads $$Z_{\text{BPS}}^{\text{open}} \; = \; \sum_R   f_R(q_1,q_2)^{-f} C_{\bullet\bullet R}(q_1^{-1},q_2^{-1}) s_R(x) \,.$$ Performing the summation we get $$Z_{\text{BPS}}^{\text{open}} \; = \; \sum_{k=0}^{\infty} (-1)^{(f+1)k} q_2^{\frac{f}{2}k(k-1)} \Big(x \frac{q_1}{\sqrt{q_2}}\Big)^k \prod_{i=1}^k \frac{1}{1 - q_1 q_2^{i-1}} \,.     \label{Zopen-BPS-C3}$$ For $f=0$ this result reduces, as it should, to the brane amplitude in ${\mathbb C}^3$ in phase III found in [@Iqbal:2007ii] (after identifying $x=-Q$). If we write now $$Z_{\text{BPS}}^{\text{open}} = \sum_{k=0}^{\infty} a_k \,,$$ we can easily determine the ratio of the consecutive coefficients, $\frac{a_{k+1}}{a_k}$, so that $$(1 - q_1 q_2^k) a_{k+1} \; = \; -x (-1)^f q^{fk} \frac{q_1}{\sqrt{q_2}} a_k \,.$$ Performing the summation over $k$ on both sides of this equation we find that the open string amplitude satisfies the following inhomogeneous difference equation $$\Big(1 - \frac{q_1}{q_2} \widehat{y} + \frac{q_1}{\sqrt{q_2}} \widehat{x}(-\widehat{y})^f   \Big) Z_{\text{BPS}}^{\text{open}} \; = \; 1 - \frac{q_1}{q_2} \,.
\label{AquantumC3inhom}$$ This is the refined and quantum version of the ordinary mirror curve ([\[mirrorC3f\]](#mirrorC3f){reference-type="ref" reference="mirrorC3f"}). Because the inhomogeneous term is independent of $x$, acting on it by $\widehat{y}$ leaves it invariant. Therefore, if we multiply both sides of the above equation by $(1-\widehat{y})$, the inhomogeneity on the right hand side vanishes, while the degree in $\widehat{y}$ of the left hand side increases. Commuting all $\widehat{y}$ operators to the right we obtain the following homogeneous equation of a higher degree $$\Big(1 - \Big(1 + \frac{q_1}{q_2}\Big) \widehat{y} + \frac{q_1}{q_2}\widehat{y}^2 +
\frac{q_1}{\sqrt{q_2}} \, \widehat{x}(-\widehat{y})^f + q_1\sqrt{q_2} \widehat{x} (-\widehat{y})^{f+1}
  \Big) Z_{\text{BPS}}^{\text{open}} \; = \; 0 \,.$$ We note the similarity of the factor $(1-\widehat{y})$, which brings the equation to the homogeneous form, to the factor representing abelian flat connection in $SL(2,{\mathbb C})$ Chern-Simons theory.
