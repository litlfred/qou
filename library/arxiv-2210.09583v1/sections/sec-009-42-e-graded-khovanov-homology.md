---
doc_id: arxiv-2210.09583v1
doc_title: "A NEW PRESENTATION OF THE osp(1|2)-POL YNOMIAL LINK INVARIANT"
section_id: sec-009-42-e-graded-khovanov-homology
section_title: "e-graded Khovanov Homology"
section_number: 4.2
pages: 13-14
source_pdf: 2210.09583v1.pdf
source_sha256: 38fc6fa465a06a7b
doc_brief: "A NEW PRESENTATION OF THE osp(1|2)-POL YNOMIAL LINK INVARIANT — There is a known connection between the osp(1|2n) polynomial knot invariant J n K and the so(2n + 1) knot invariant soJ n K studied by"
---
a nearly identical manner. We can deﬁne an e-grading on 2Cob by adding formal objects Σ {(a, b)}
for every 1-manifold Σ and ( a, b) ∈ /CI × /CI
4, and deﬁning the degree deg(W ) of a cobordism W :
Σ 0{(m, m′)} → Σ 1{(n, n′)} by
deg(W ) = ( χ(W ) + n − m, −χ(W ) + n′ − m′)
Pants cobordisms have degree ( −1, 1) and caps and cups have degree (1 , −1).
Given an oriented link diagram L, construct a chain complex [ L] of cobordisms as follows. Replace
each crossing of L with the chain complex
[ ]
= {(0, 1)} → {(1, 0)}(4.1)
[ ]
= {(−1, 0)} → {(0, −1)}(4.2)
where the underlined term in each complex lives in cohomological degre e 0. The maps between the 0
and 1-resolution in each complex are given by a saddle cobordism just like before.
Then the complex [ L] is deﬁned by
[L]r−n− =
⨁
∑ zi=r
L′
z{(−n− + r, n+ − r)}(4.3)
d|L′z =
∑
α:z→w
ε(α)Dα(4.4)
14 MARK EBERT
where Dα = DXj is one of the two maps shown above. We then get the e-graded vers ion of the
Khovanov complex by shifting the degree of each term.
Deﬁnition 4.6. The chain complex eKh(L) is obtained by shifting the degree of each chain group by
{wr(L), 2wr(L)}
eKh(L) = [ L]{(wr(L), 2wr(L)}(4.5)
Let A = R[X]/(X 2) be the free e-graded R-module of rank 2 spanned by /BD and X in degrees
deg(/BD ) = (1 , −1) and deg(X) = ( −1, 1). We equip A with the following maps to make it a Frobenius
algebra.
ε : A → R
{
/BD → 0
X → 1(4.6)
η : R → A {1 → /BD(4.7)
m : A ⊗ A → A
{
/BD ⊗ /BD → /BD /BD ⊗ X → X
X ⊗ /BD → X X ⊗ X → 0(4.8)
∆ : A → A ⊗ A
{
/BD → /BD ⊗ X + X ⊗ /BD
X → X ⊗ X(4.9)
We have deg(m) = deg(∆) = ( −1, 1) and deg(ε) = deg(η) = (1 , −1).
Deﬁnition 4.7. Let F : 2Cob → R-emod be the TQFT corresponding to the Frobenius algebra A.
Denote Mn as the object in 2Cob consisting of n-disjoint circles. F sends a collection of k circles to
A⊗k and
• The two pair-of-pants cobordisms M2 → M1 and M1 → M2 to m and ∆ respectively.
• The birth M0 → M1 and death M1 → M0 to η and ε respectively.
It is easy to see that F is well deﬁned and degree preserving. Apply the TQFT F : 2Cob → R-emod
to turn the chain complex eKh[L] into a chain complex C(L) := F (eKh[L]) of e-graded R-modules.
Theorem 4.8. The homology H(C(L)) of the chain complex C(L) is an invariant of oriented links.
To show this, we need to show that the Reidemeister moves hold. Sinc e forgetting the /CI
4-grading
recovers Khovanov homology exactly, the arguments from [ 2] for why Khovanov homology is a link
