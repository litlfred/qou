---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY"
section_id: sec-004-22-weyl-modules-dual-weyl-modules-and-simple-mod
section_title: "Weyl modules, dual Weyl modules and simple modules"
section_number: 2.2
pages: 6-8
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on"
---
Deﬁnition 2.5. (Weyl, dual Weyl and simple modules) Let i ∈ Z≥0 and denote by ∆ q(i) the i-th
Weyl module. This is the Q(q)-vector space with basis m0, . . . , mi and an Uq-action deﬁned by
Km k = qi−2kmk, E (j)mk =
[
i − k + j
j
]
mk−j, F (j)mk =
[
k + j
j
]
mk+j,
with the convention that m<0 = m>i = 0 . The i-th dual Weyl module , denoted by ∇q(i), is
obtained from ∆ q(i) by taking the dual, that is, HomQ(q)(∆ q(i), Q(q)) = (∆ q(i))∗ = ∇q(i). ▲
It is easy to check directly that ∆ q(i) has a unique simple head Lq(i) which is also the unique
simple socle of ∇q(i). See also [5, Section 4].
4The square is only important for roots of unity of even order, but not for roots of unity of odd order (for these the
order of q2 is the same as the order of q), e.g. we have l = 3 for third as well as for sixth roots of unity.
6
Example 2.6. Let q = −1+√−3
2 (we use this q in all examples with l = 3 in what follows).
The Weyl module ∆ q(3) can be visualized as
(2) m3
+1 /d47/d47
q−3
/d4/d4
m20
/d111/d111
−1 /d47/d47
q−1
/d4/d4
m1
0 /d47/d47
−1
/d111/d111
q+1
/d4/d4
m0.
+1
/d111/d111
q+3
/d4/d4
Here the action of E points right, the action of F left, E(3)m3 = m0, F (3)m0 = m3, K acts as
a loop and all other actions are zero. Thus, the A-span of {m1, m2} is now, in contrast to the
classical case, stable under the action of Uq. The complement however is not an Uq-submodule.
Another example (where we have excluded the actions of the divided powers) is ∆ q(4):
(3) m4
+1 /d47/d47
q−4
/d4/d4
m3+1
/d111/d111
−1 /d47/d47
q−2
/d4/d4
m2
0 /d47/d47
0
/d111/d111
q0
/d4/d4
m1
+1 /d47/d47
−1
/d111/d111
q+2
/d4/d4
m0.
+1
/d111/d111
q+4
/d4/d4
We note that ∆ q(4) has the trivial Uq-module spanned by m2 as a Uq-submodule. ▲
K acts on ∆ q(i) via the eigenvalues q−i, q−i+2, . . . , qi−2, q+i. Thus, by (1), the same is true for
∇q(i). Moreover, the Lq(i) are self-dual, see e.g. [5, Section 4].
Proposition 2.7. We have the following.
(a) ∆ q(i) ∼= Lq(i) iff i < l or i ≡ −1 mod l.
(b) Suppose i = al + b for some a, b ∈ Z≥0 with b ≤ l − 2. Set i′ = ( a + 2)l − b − 2. Then
there exists a short exact sequence
0 − →Lq(i)֒− →∆ q(i′) −։ Lq(i′) − →0.
Moreover, Lq(i′) is the head and Lq(i) is the socle of ∆ q(i′). □
Proof. This is [5, Corollary 4.6]. ■
Corollary 2.8. We have the following.
(a) ∇q(i) ∼= Lq(i) iff i < l or i ≡ −1 mod l.
(b) Suppose i = al + b for some a, b ∈ Z≥0 with b ≤ l − 2. Set i′ = ( a + 2)l − b − 2. Then
there exists a short exact sequence
0 − →Lq(i′)֒− → ∇q(i′) −։ Lq(i) − →0.
Moreover, Lq(i′) is the socle and Lq(i) is the head of ∇q(i′). □
Proof. This follows fromLq(i) ∼= (Lq(i))∗ and the fact that ∗ is an exact, contravariant functor. ■
Example 2.9. For i = 0 and l = 3 we have i′ = 4 . The trivial Uq-module Lq(0) appears as a
submodule of ∆ q(4), compare to (3). ▲
We should note here that there are two different types of Uq-modules known as type 1 and −1,
see for example [5, Section 1]. For us the difference between the two types is not important in this
paper and we only consider Uq-modules of type 1. The (more general) treatment in [5, Section 1]
ensures that the consideration of only type 1 is still enough to get results for both types.
Corollary 2.10. The set {Lq(i) | i ∈ Z≥0} is a complete set of simple, pairwise non-isomorphic,
ﬁnite-dimensional Uq-modules (of type 1). □
Proof. See [5, Corollary 6.3]. ■
7
Remark 2.11. The category of Uq-modules is far from being semisimple: Proposition 2.7 says
that ∆ q(i) is never simple whenever we are in the case (b). See also (2). ▲
