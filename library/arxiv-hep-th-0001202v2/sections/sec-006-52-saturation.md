---
doc_id: arxiv-hep-th-0001202v2
doc_title: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees"
section_id: sec-006-52-saturation
section_title: "Saturation"
section_number: 5.2
pages: 9-9
source_pdf: 0001202v2.pdf
source_sha256: b2e3e22ea3d51c0b
doc_brief: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees — The renormalization of quantum ﬁeld theory twists the antipode of a non- cocommutative Hopf algebra"
---
We now seek to prove that Hk(x) = [ H1(x)]k in the case that H = HR is the Hopf algebra
of undecorated rooted trees.
First we prove that deg p(XjXk) = deg p(Xj) + degp(Xk).
Proof: Suppose that Xj ∈ H j and Xk ∈ H k. Then
Uj+k−1(XjXk) = P ⊗(j+k)(∆ j+k−1(Xj)∆ j+k−1(Xk)) ⁄= 0 (26)
contains 1-primitives in all its slots, giving Uj+k(XjXk) = 0, by coassociativity. ✷
It is instructive to see how this works out for the product ZX , when Z is 1-primitive
and X is k-primitive. Then
∆ k(Z) =
k+1∑
j=1
e ⊗ . . . ⊗ Z|j− th place ⊗ . . . e (27)
consists of all k + 1 terms with a single Z and k empty trees. As X is k-primitive,
∆ k(X) =
k+1∑
j=1
∑
ij
X (1)
ij ⊗ . . . ⊗ e|j− th place ⊗ . . . X(k+1)
ij + . . . (28)
with the ﬁnal ellipsis denoting omission of terms that contain more tha n one e. The latter
make no contribution to
Uk(ZX ) =
k+1∑
j=1
∑
ij
X (1)
ij ⊗ . . . ⊗ X (j−1)
ij ⊗ Z|j− th place ⊗ X (j+1)
ij ⊗ . . . ⊗ X (k+1)
ij (29)
where Z replaces a single e. By construction (29) has all its entries, namely Z or X (r)
ij , in
H1. Hence Uk+1(ZX ) = 0 and deg p(ZX ) = k + 1.
Iterating this result one immediately concludes that deg p(X1 . . . Xk) = k, for 1-
primitive elements X1, . . . , Xk. This does not, of itself, allow us to conclude that Hk(x) =
[H1(x)]k, since the products are commutative. Thus there are fewer k-fold products of
1-primitives than there are k-primitives.
To appreciate what is needed in the next step, we pause to consider HCM. Its 1-
primitives are δ1 and ~δ2 = δ2 − 1
2δ2
