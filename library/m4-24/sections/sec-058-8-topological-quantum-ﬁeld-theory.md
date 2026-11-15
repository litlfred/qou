---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-058-8-topological-quantum-ﬁeld-theory
section_title: "Topological quantum ﬁeld theory"
section_number: 8
pages: 121-122
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
toc_source: inferred
---
The notion of topological quantum ﬁeld theory (TQFT) was introduced in
[16, 20], motivated by the operator formalism of a partition function in a quan-
tum ﬁeld theory which does not depend on the metric of the space. In the math-
ematical viewpoint, any quantum invariant of 3-manifolds can be formulated
by a TQFT, which enables us to compute the invariant by the cut-and-paste
method.
A TQFT is a functor which takes an oriented closed surface Σ to a ﬁnite dimen-
sional complex vector space V (Σ), and takes an oriented compact 3-manifold
M with boundary Σ to a vector Z(M) ∈V (Σ), satisfying the following 5
axioms.
(1)
V (−Σ) = V (Σ)⋆, where −Σ denotes Σ with the opposite orientation and
V (Σ)⋆denotes the dual vector space of V (Σ).
(2)
V (Σ1 ⊔Σ2) = V (Σ1) ⊗V (Σ2), where Σ1 ⊔Σ2 denotes the disjoint union
of two surfaces Σ1 and Σ2.
(3)
V (∅) = C, where ∅denotes the empty surface.
(4) For 3-cobordisms M1 and M2 with ∂M1 = (−Σ1) ⊔Σ2 and ∂M2 =
(−Σ2)⊔Σ3 we have that Z(M1 ∪
Σ2 M2) = Z(M2)◦Z(M1) as linear maps28
V (Σ1) →V (Σ3).
(5)
Z(Σ × I) is equal to the identity map of V (Σ).
To be precise, in many (but not in all) examples we need “extended 3-manifolds”
instead of 3-manifolds to formulate a TQFT, where an extended 3-manifold is
a 3-manifold M equipped with some kind of framing, e.g. a p1-structure α on
M (see [60])29. Namely, we extend the above deﬁnition of TQFT to a functor
from the category of extended 3-cobordisms in an appropriate way (see [60]).
Then, each quantum invariant can be formulated as a TQFT of the category
of extended 3-cobordisms. In the remaining part of this section we call such a
TQFT simply a TQFT.
The ﬁrst version of the introductory part of Chapter 8 and Sections 8.1–8.4 was written
by T. Ohtsuki, following seminar talks given by G. Masbaum. Based on it, G. Masbaum wrote
this introductory part and these sections. Section 8.5 was written by T. Kerler.
28For a 3-cobordism M with ∂M = (−Σ1)⊔Σ2 the vector Z(M) belongs to V (−Σ1⊔Σ2) =
V (−Σ1)⊗V (Σ2) = V (Σ1)⋆⊗V (Σ2) by the axioms (1) and (2). Hence, Z(M) can be regarded
as a linear map V (Σ1) →V (Σ2).
29There is another formulation of a “framing” of a 3-manifold using signature cocycle; see
[388].
Geometry & Topology Monographs, Volume 4 (2002)
494
T. Ohtsuki (Editor)
8.1
