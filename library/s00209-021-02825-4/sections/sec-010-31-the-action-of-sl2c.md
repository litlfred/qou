---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-010-31-the-action-of-sl2c
section_title: "The action of SL2(C)"
section_number: 3.1
pages: 8-9
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
Given(α : β) ∈CP1 andφ ∈SL2(C),wedeﬁnetheusualactionofSL2(C)onCP1 viaφ·(α :
β) := φ
α
β
	
. That is, φ acts by matrix multiplication on the vector
α
β
	
. Equivalently, φ acts as
its corresponding Möbius transformation on CP1. Note that, as with Möbius transformations,
SL2(C) acts transitively on circular regions in CP1.
This then induces an action on V (n) by acting on the roots (in CP1) of polynomials in
V (n). Given p ∈V (n) and φ ∈SL2(C), this action is deﬁned via:
(φ · p)(x, y) := p

φ−1
x
y

≡(p ◦φ−1)(x, y)
We can deﬁne a similar action of (SL2(C))m on V (λ), for λ ∈Nm
0 . Speciﬁcally, given
p ∈V (λ) and (φ1, . . . , φm) ∈SL2(C)m, this action is deﬁned via:

(φ1, . . . , φm) · p
	
(x1, y1, . . . , xm, ym) := p

φ−1
1
x1
y1

, . . . , φ−1
m
xm
ym

These actions turn V (n) and V (λ) into representations of SL2(C) and (SL2(C))m, respec-
tively. These are precisely the ﬁnite dimensional irreducible representations of SL2(C) and
(SL2(C))m (see Lecture 11 of [6]), and so they are the basic building blocks of the SL2(C)
representation theory. Actions on V (n) and V (λ) can be extended to tensor products in the
usual way, and in this paper we will make use of both inner and outer tensor products. We
now brieﬂy discuss tensor product actions for those less familiar.
A representation theoretic explanation...
1367
The outer tensor product of V (λk), denoted V (λ1) ⊠· · · ⊠V (λm), is a representation of
(SL2(C))m with action by (φ1, . . . , φm) on simple tensors given as follows:
(φ1, · · · , φm) · (p1 ⊠· · · ⊠pm) := (φ1 · p1) ⊠(φ2 · p2) ⊠· · · ⊠(φm · pm)
This implies that V (λ) and V (λ1) ⊠· · · ⊠V (λm) are isomorphic as representations, and this
fact will be used when we deﬁne the symbol in Sect. 3.3.
The inner tensor product of V (λk), denoted V (λ1) ⊗· · · ⊗V (λm), is a representation of
SL2(C) with action by φ on simple tensors given as follows:
φ · (p1 ⊗· · · ⊗pm) := (φ · p1) ⊗(φ · p2) ⊗· · · ⊗(φ · pm)
While V (λ)and V (λ1)⊗· · ·⊗V (λm)areisomorphicasvectorspaces,theyarerepresentations
of different groups ((SL2(C))m and SL2(C) respectively). The inner tensor product relates
to invariants of multiple polynomials with respect to a single SL2(C) action. For instance,
the apolarity form takes two distinct polynomials as input, and it is a classical result that this
form is invariant with respect to a single action by Möbius transformation. As it turns out,
this form can be viewed as an SL2(C)-invaiant map on an inner tensor product of polynomial
spaces. It will therefore be important for us to understand these inner tensor products in a
little more detail.
