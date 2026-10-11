---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-004-24-complex-structure
section_title: "Complex structure"
section_number: 2.4
pages: 8-9
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a sin gle real"
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.992
---
Any of the Clifford generators $E^i$ squares to minus the identity, and so is a complex structure on ${\mathbb O}$. Thus, a choice of a unit $u\in{\rm Im}({\mathbb O})$ gives rise to the complex structure $J := L_u$. Our octonion multiplication encoded in ([\[C\]](#C){reference-type="ref" reference="C"}) is such that $e^4$ is treated as a preferred element, and so we choose $u=e^4$ and $J= E^4$.

It is interesting to describe the subalgebra of ${\mathfrak so}(7)$ that commutes with $J$. It is clear that all products $E^i E^j$ that do not contain $E^4$ commute with it. Thus, the subalgebra of ${\mathfrak so}(7)$ that commutes with $J$ is ${\mathfrak so}(6)$ that corresponds to rotations in the $e^{1,2,3, 5,6,7}$ plane.

Given that this ${\mathfrak so}(6)$ commutes with a complex structure, it admits a complex description. In this description it is the Lie algebra of the group that acts by unitary transformations in e.g. the $(1,0)$ eigenspace of $J$. Indeed, the complex structure allows to identify ${\mathbb O}={\mathbb C}^4$, and transformations commuting with the complex structure preserve the $(1,0)$ and $(0,1)$ eigenspaces of $J$. In our conventions the $(1,0)$ eigenspace is the one that corresponds to the eigenvalue $-{\rm i\,}$. All in all, we get ${\mathfrak so}(6)={\mathfrak su}(4)$.

## A different complex structure

There is a different choice of the complex structure on ${\mathbb O}$, which is also parametrised by a unit imaginary octonion. This leads to a different but very interesting commutant in ${\mathfrak so}(7)$. This has been described in [@Krasnov:2019auj].

Instead of using the operator $L_u$ of left multiplication by a unit imaginary octonion, one can use the complex structure $J':= R_u$ given by the operator of the right multiplication $R_u$. This gives a complex structure, but one different from $L_u$. The operator $R_u$ agrees with $L_u$ on the copy of ${\mathbb C}$ spanned by ${\mathbb I},u$, but acts with the opposite sign on the rest of ${\mathbb O}$. It is easy to check that the commutant of $R_u$ in ${\mathfrak so}(7)$ is the subalgebra ${\mathfrak su}(3)\times {\mathfrak u}(1)\subset {\mathfrak su}(4)$. Thus, this complex structure breaks ${\mathfrak so}(7)$ even further, and produces the very relevant for physics algebra ${\mathfrak su}(3)$ of the strong force and the \"hypercharge\" ${\mathfrak u}(1)$.[^1]

We can also describe the $R_u$ complex structure in a way that strongly mimics what happens in the ${\mathfrak so}(4,3)$ setting of the next section. Let us introduce the operator $\rho$ that acts as the identity on ${\rm Span}({\mathbb I},u)$ and changes the sign of the 6-dimensional orthogonal to ${\mathbb I},u$ space. In other words, let $\rho$ be the reflection in the ${\mathbb I},u$ plane. This operator squares to $+{\mathbb I}$, and commutes with $L_u$. Their product is precisely $R_u$. Thus, we consider $$\begin{aligned}
\label{J-right}
J' := R_u = E^4 \rho.
\end{aligned}$$ As we already mentioned, the commutant of $J'$ in ${\mathfrak so}(7)$ is the direct sum ${\mathfrak su}(3)\oplus{\mathfrak u}(1)$.

[^1]: When we describe the left/right symmetric model below, it will become clear that the right interpretation of this ${\mathfrak u}(1)$ is that corresponding to ${\rm U}(1)_{B-L}$ symmetry.
