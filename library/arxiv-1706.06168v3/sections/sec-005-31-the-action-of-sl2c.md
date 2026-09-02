---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-005-31-the-action-of-sl2c
section_title: "The Action of SL2(C)"
section_number: 3.1
pages: 7-8
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
---
Given (α :β) ∈ CP1 and φ ∈ SL2(C), we deﬁne the usual action of SL 2(C) on CP1 via φ · (α :β) := φ
( α
β
)
.
That is, φ acts by matrix multiplication on the vector
( α
β
)
. Equivalently, φ acts as its corresponding M¨ obius
transformation on CP1. Note that, as with M¨ obius transformations, SL 2(C) acts transitively on circular
regions in CP1.
This then induces an action on V (n) by acting on the roots (in CP1) of polynomials in V (n). Given
p ∈V (n) and φ ∈ SL2(C), this action is deﬁned via:
(φ ·p)(x,y ) := p
(
φ−1
( x
y
))
≡ (p ◦φ−1)(x,y )
We can deﬁne a similar action of (SL 2(C))m on V (λ), for λ ∈ Nm
0 . Speciﬁcally, given p ∈ V (λ) and
(φ1,...,φ m) ∈ SL2(C)m, this action is deﬁned via:
(
(φ1,...,φ m) ·p
)
(x1,y 1,...,x m,y m) := p
(
φ−1
1
( x1
y1
)
,...,φ −1
m
( xm
ym
))
These actions turn V (n) and V (λ) into representations of SL 2(C) and (SL 2(C))m, respectively. These are
precisely the ﬁnite dimensional irreducible representations of SL 2(C) and (SL 2(C))m (see Lecture 11 of
[FH13]), and so they are the basic building blocks of the SL 2(C) representation theory. Actions on V (n) and
V (λ) can be extended to tensor products in the usual way, and in this p aper we will make use of both inner
and outer tensor products. We now brieﬂy discuss tensor produc t actions for those less familiar.
The outer tensor product of V (λk), denoted V (λ1) ⊠ · · · ⊠V (λm), is a representation of (SL 2(C))m with
action by (φ1,...,φ m) on simple tensors given as follows:
(φ1, · · ·,φ m) · (p1 ⊠ · · · ⊠pm) := (φ1 ·p1) ⊠ (φ2 ·p2) ⊠ · · · ⊠ (φm ·pm)
This implies that V (λ) and V (λ1) ⊠ · · ·⊠V (λm) are isomorphic as representations, and this fact will be used
when we deﬁne the symbol in §3.3.
The inner tensor product of V (λk), denoted V (λ1) ⊗ · · · ⊗ V (λm), is a representation of SL 2(C) with
action by φ on simple tensors given as follows:
φ · (p1 ⊗ · · · ⊗pm) := (φ ·p1) ⊗ (φ ·p2) ⊗ · · · ⊗ (φ ·pm)
While V (λ) and V (λ1) ⊗ · · · ⊗V (λm) are isomorphic as vector spaces, they are representations of d iﬀerent
groups ((SL 2(C))m and SL 2(C) respectively). The inner tensor product relates to invariants of multiple
7
polynomials with respect to a single SL 2(C) action. For instance, the apolarity form takes two distinct
polynomials as input, and it is a classical result that this form is invarian t with respect to a single action
by M¨ obius transformation. As it turns out, this form can be viewed as an SL 2(C)-invaiant map on an inner
tensor product of polynomial spaces. It will therefore be importa nt for us to understand these inner tensor
products in a little more detail.
