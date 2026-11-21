---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves"
section_id: sec-036-the-weight-4-case-euler-complexes
section_title: "The weight 4 case: Euler complexes"
section_number: null
pages: 109-112
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
toc_source: outline
doc_brief: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves — On the Galois Action on Motivic Fundamental Groups of Punctured Elliptic and Rational Curves Nikolay"
---
The weight 4 case: Euler complexes
Let us show how the map in Theorem 3.13 generalizes those constructed by [GL, G8]. To be consistent with
those sources, we use the motivic language in this section, but the same results hold in the Hodge realization
as well.
The elements 휃퐸
For torsion points 푎, 푏, 푐∈퐸with 푎+ 푏+ 푐= 0, elements 휃퐸(푎, 푏, 푐) are constructed by [G8] as follows.
For 퐸an elliptic curve over a ﬁeld 푘, 픭⊂End퐸a prime over 푝, and 푧a nonzero 픭-torsion point of 퐸,
there are elements 휃퐸(푧), which are 푝-torsion elements in 푘
∗
푧⊗Z
h
1
푝
i
, where 푘푧is the extension generated
by the coordinates of 푧. They are identiﬁed with weight-2 elements in the mixed Tate Lie coalgebra Lie∨
MT/푘.
The real period of the motive 휃퐸(푧) is −log |휃퐸(푧)|.
The elements 휃퐸(푎: 푏: 푐) lie in the Bloch group of 푘, which is identiﬁed with the weight-4 part of
Lie∨
MT/푘. We also use the notation 휃퐸(푎, 푏, 푐) = 휃퐸(푎: 푎+ 푏: 푎+ 푏+ 푐), which is unambiguous when
푎+푏+푐= 0 because the 휃퐸(푎: 푏: 푐) are invariant under translation. They are characterized by the following
properties:
(1) The coproduct is given by
훿휃퐸(푎, 푏, 푐) = 휃퐸(푎) ∧휃퐸(푏) + 휃퐸(푏) ∧휃퐸(푐) + 휃퐸(푐) ∧휃퐸(푎).
(2) The real period of 휃퐸(푎: 푏: 푐) is given up to a constant multiple by the averaged Chow dilogarithm
([G7]). The latter can be rewritten as
1
푝5
Õ
푥∈퐸[푝]
∫
퐸(퐶)
log

 푓푎,푥

 푑C log

 푓푏,푥

 ∧푑C log

 푓푐,푥

 ,
(3.21)
where 푓푎,푏is a function on 퐸with div 푓푎,푏= 푝({푎} −{푏}).
The elements 휃퐸and motivic correlators
According to [G9], §10.5.5, for 푎, 푏∈퐸[푝], the elements 휃퐸(푎−푏) are equal up to a constant multiple to
Corav (푎, 푏). There is a version for the depth 2 elements.
Lemma 3.15. Let 퐸be an elliptic curve over a number ﬁeld. Then, for 푎, 푏, 푐∈퐸[픭] \ {0} with 푎+ 푏+ 푐= 0,
the elements 휃퐸(푎: 푏: 푐) are equal up to a constant multiple to Corav(푎, 푏, 푐).
Proof. The coproduct formulas for the 휃퐸and the Corav coincide ([G9], Lemma 10.9). It remains to see the
periods are equal. Indeed, we take 푓푎,푥such that log

 푓푎,푥(푧)

 = 푝퐺푥(푎, 푧), and likewise for 푏and 푐. Then
the formula (3.21) is evidently a constant multiple of the Hodge correlator
1
|퐸[픭]|
Õ
푥∈퐸[픭]
CorH,푥(푎, 푏, 푐),
where CorH,푥denotes the Hodge correlator function computed using the Green’s function with base point 푥,
as desired.
□
The map constructed by [G8], for O = Z[푖] or Z[휌] is:
휃′ : Z[Γ1(픭) \ GL2(O)] ⊗Γ1(픭) 푀•
2 →Lie∨
Mot(퐸, 퐸[픭]),
(훼1, 훼2) ⊗[푣1, 푣2] ↦→휃퐸(훼1, 훼2, −(훼1 + 훼2)),
(훼1, 훼2) ⊗([푣1] ∧[푣2]) ↦→휃퐸(훼1) ∧휃퐸(훼2).
Theorem 3.16. The map 휃′ is a constant multiple of the component of 휃◦휓corresponding to the constant
term of the local system 푇2.
Proof. After unraveling the deﬁnitions, in degree 1, this is exactly Lemma 3.15, while in degree 2 it amounts
to showing that
Corav(0, 푎) ∧Corav(0, 푏) =
1
|퐸[픭]|
Õ
푠∈퐸[픭]
Cor푠(0, 푎) ∧Cor푠(0, 푏).
Expanding the sums and using that Cor푠(푥, 푦) ∼휃퐸(푥−푦) −휃퐸(푥−푠) −휃퐸(푦−푠) (where we set 휃퐸(0) = 0),
this simpliﬁes to
Õ
푠
휃퐸(푠) ∧휃퐸(푏−푠) +
Õ
푠
휃퐸(푎−푠) ∧휃퐸(푠) +
Õ
푠
휃퐸(푎−푠) ∧휃퐸(푏−푠) = 0.
The three sums are both symmetric and antisymmetric under the involutions 푠↦→푏−푠, 푠↦→푎−푠, and
푠↦→푎+ 푏−푠, respectively, so the sum is 0.
□
A slight abuse of notation has taken place: 휃maps to gr퐷Lie∨
sym(퐸, 퐸[픭]) and 휃′ to Lie∨
MT(퐸, 퐸[픭]).
However, there is no discrepancy, as the second shuﬄe relation in weight 4 and depth 2 holds without the
lower-depth correction terms, and so the constant term of 휃can be viewed as a map to Lie∨
sym(퐸, 퐸[픭]), by
the following lemma.
Lemma 3.17. For 퐸any elliptic curve and 푎, 푏∈퐸[픭],
Corav(푎, 푏, 푆0,0 ∗푆0,0) = 0,
Corav(푎, 푆0,0 ∗푆0,0 ∗푆0,0) = 0.
Proof. For the ﬁrst equality, recall that
푆0,0 ∗푆0,0 = −1
2 (휔⊗휔−휔⊗휔).
It is easily veriﬁed that the coproduct is 0. For the periods, there are two trees contributing to the integral
expansion of the correlator. For the tree where 휔, 휔are not incident to a common interior vertex, the terms
with 휔⊗휔and with 휔⊗휔sum to 0. The other tree contributes a constant multiple of
Õ
푠∈퐸[픭]
∫
퐸
퐺푠(푧, 푤) 푑C퐺푠(푤, 푎) ∧푑C퐺푠(푤, 푏) ∧휔(푧) ∧휔(푧)
=
Õ
푠∈퐸[픭]
∫
퐸
퐺Ar(푠−푤) 푑C퐺푠(푤, 푎) ∧푑C퐺푠(푤, 푏)
=
Õ
푠∈퐸[픭]
∫
퐸
퐺Ar(푠−푤) 푑C(퐺Ar(푎−푤) −퐺Ar(푠−푤)) ∧푑C(퐺Ar(푏−푤) −퐺Ar(푠−푤))
= 0.
This follows from the distribution relations for the function 퐺Ar, which state that
Õ
푠∈퐸[픭]−0
퐺Ar(푠) = 0.
The second equality follows simply from dihedral symmetry.
□
