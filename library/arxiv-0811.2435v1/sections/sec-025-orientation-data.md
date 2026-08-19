---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic"
section_id: sec-025-orientation-data
section_title: "Orientation data"
section_number: null
pages: 80-83
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
LetC be an ind-constructible k-linear 3-dimensional Calabi-Yau category. 17
Then we have a natural ind-constructible super line bundle D over Ob(C)
with the ﬁber over E given by DE = sdet(Ext•(E,E )). It follows that on
17There is a notion of Z/ 2Z-graded odd or even Calabi-Yau category, see [42]. Some
considerations of this section can be generalized to Z/ 2Z-graded case.
80
the ind-constructible stack of exact triangles E1→ E2→ E3 we have an
isomorphism of the pull-backed line bundles which ﬁberwise reads as
DE2⊗D−1
E1⊗D−1
E3≃ (sdet(Ext•(E1,E 3)))⊗2 .
Let us explain this isomorphism. The multiplicativity of su perdeterminants
on exact triangles gives rise to a canonical isomorphism
sdet(Ext•(E2,E 2))≃ sdet(Ext•(E1,E 1))⊗ sdet(Ext•(E1,E 3))⊗
⊗ sdet(Ext•(E3,E 1))⊗ sdet(Ext•(E3,E 3)) .
By the Calabi-Yau property we have
sdet(Ext•(E3,E 1))≃ sdet(Π(Ext •(E3,E 1)))∗≃ sdet(Ext•(E1,E 3))
which implies the desired formula. When Ob(C) =⊔i∈IYi is a decomposition
into the union of GL(Ni)-invariant constructible sets as at the end of 3.2,
then the restriction D|Yi is a GL(Ni)-equivariant super line bundle and the
above isomorphisms are also equivariant.
Deﬁnition 15 Orientation data onC consists of a choice of an ind-constructible
super line bundle
√
D on Ob(C) such that its restriction to each Yi,i∈ I is
GL(Ni)-equivariant, endowed on each Xi with GL(Ni)-equivariant isomor-
phisms (
√
D)⊗2 ≃ Dand such that for the natural pull-backs to the ind-
constructible stack of exact triangles E1→E2→E3 we are given equivariant
isomorphisms:
√
DE2⊗ (
√
DE1)−1⊗ (
√
DE3)−1≃ sdet(Ext•(E1,E 3))
such that the induced equivariant isomorphism
DE2⊗D−1
E1⊗D−1
E3≃ (sdet(Ext•(E1,E 3)))⊗2
coincides with the one which we have a priori.
We deﬁne the group J2(C) := ∏
i∈IJ2(Yi,GL (Ni)). We have a canonical
equivariant super line bundle D≤1 whose ﬁber at E∈Ob(C) is
D≤1,E := sdet(τ≤1(Ext•(E,E ))) ,
81
where τ≤i,i ∈ Z denotes the standard truncation functor. It is easy to see
that we have an equivariant isomorphism D⊗2
≤1≃D . Then on the space of
exact triangles E1→E2→E3 we have an equivariant isomorphism of super
line bundles ﬁberwise given by
(D≤1,E2⊗D−1
≤1,E1⊗D−1
≤1,E3)⊗2≃ (sdet(Ext•(E1,E 3)))⊗2.
Let nowFun (C3,C) be the ind-constructible category of A∞-functors from
the the category C3 considered in 3.1. Its objects can be thought of as exact
triangles
E1→E2→E3 =Cone(E1→E2)
inC. There are three functors Funct (C3,C)→C which associate to an exact
triangle E1→ E2→ E3 the objects E1,E 2,E 3 respectively. These functors
induce three homomorphisms
φi :J2(C)→J2(Funct (C3,C)),i = 1, 2, 3.
The super line bundle L with the ﬁber
LE1→E2→E3 = (D≤1,E2⊗D−1
≤1,E1⊗D−1
≤1,E3)⊗ (sdet(Ext•(E1,E 3)))−1
deﬁnes an element l∈ J2(Funct (A2,C)), since L⊗2≃ 1Funct (C3,C). Then a
choice of orientation data on C is equivalent to a choice of h∈ J2(C) such
that−φ1(h)+φ2(h)−φ3(h) = l. Indeed a choice of orientation data gives rise
to a super line bundle
√
D such that
√
D
⊗2
≃D ⊗2
≤1. Therefore the quotient
h =
√
D⊗D −1
≤1 deﬁnes an element in J2(C), and the condition for the tensor
squares of the super line bundles
√
DEi,i = 1, 2, 3 on the space of exact
triangles is equivalent to the equation −φ1(h) +φ2(h)−φ3(h) = l.
Remark 20 All the above considerations admit a straightforward gener al-
ization to the case of Calabi-Yau category of arbitrary odd d imension d. In
the case d = 1 (mod 4) we have canonical orientation data given by
√
DE := sdet(τ≤ d−1
2
(Ext•(E,E ))) .
This is due to the observation that in the explicit descripti on of the analog
of the obstruction element l deﬁned above in terms of a super vector bundle
endowed with a symmetric bilinear form, the super vector bun dle turns out to
be purely odd, hence the bilinear form is split. It follows th at the obstruction
element is trivial. In the case d = 3 considered in this paper the obstruction
does not have to vanish.
82
