---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I"
section_id: sec-015-43-planar-algebras-give-subfactors
section_title: "Planar algebras give subfactors"
section_number: 4.3
pages: 115-118
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
toc_source: inferred
doc_brief: "Planar Algebras, I — We introduce a notion of planar algebra, the simplest example of which is a vector space of tensors, closed under planar contractions."
---
The following theorem relies heavily on a result of Popa [Po2].
Theorem 4.3.1 Let (P, Φ) be a spherical C∗-planar algebra with invariant
Z and trace tr. Then there is a subfactor N ⊆M and isomorphisms Ω:
N′ ∩Mi →Pi with
(i) Ωis compatible with inclusions
(ii) tr(Ω(x)) = tr(x)
(iii) Ω(M′ ∩Mi) = P1,i (linear span of tangles with vertical ﬁrst
string)
(iv) Ω(ei) = 1
δ(Φ(
))
115
(v) [M : N] = δ2. If x ∈N′ ∩Mi, choose T ∈P with Φ(T) =
Ω(x).
(vi) Ω(EM′(x)) = 1
δΦ(
T )
(vii) Ω(EMi−1(x)) = 1
δΦ( T
)
Proof. By theorem 3.1 of [Po2], the pair N ⊆M exists given a system
(Aij), 0 ≤i < j < ∞of ﬁnite dimensional C∗-algebras with Ai,j ⊂Ak,ℓif
k ≤i, j ≤ℓand a faithful trace on S∞
n=0 A0n satisfying 1.1.1, 1.1.2, 1.3.3′
and 2.1.1 of [Po2]. We set Ai,j = Pi,j (Deﬁnition 1.20). Then Aii = C since
Z is multiplicative and non-degenerate. The conditions of [Po2] involve ei’s
and conditional expectations EAij. We deﬁne the ei’s in P to be what we
have called Ω(ei) (note our ei is Popa’s “ei+1”). The map EAij is deﬁned by
the relation tr(xEAij(y)) = tr(xy) for x in Aij and y arbitrary. Since Z is
an S2 invariant one easily checks that EAij is given by the element of A∥|(∅)
given in the ﬁgure below (for x ∈A0,k)
· · ·
· · ·
· · ·
· · ·
1
· · ·
2
i
EAij :
1
δi+k−j
· · ·
j
i + 1
Popa’s (1.1.1) and (1.1.2) and b)′ of (1.3.3) follow immediately from pictures
(note that the power of 1
δ is checked by applying EAij to 1). Condition a)′ of
1.3.3′ is dim Aij = dim Ai,j+1ej = dim Ai−1,j+1. But it is easy from pictures
that EAij deﬁnes a linear map from Ai,j+1ej onto Ai,j, whose inverse is to
embed in Ai,j+1 and multiply on the right by ej. Moreover th element of
A(∅) (illustrated for i=0) in Figure 1 deﬁnes a linear isomorphism from Ai,j
116
to Ai+1,j+1 — the inverse is a similar picture.
· · ·
· · ·
Finally the commutation relations 2.1.1, [Aij, Akℓ] = 0 for i ≤j ≤k ≤ℓare
trivial since they are true in P, involving non-overlapping strings.
It is standard theory for external subfactors that EM′ restricted to N′∩Mi
is EA1,i and EMi−1 = EA1,i−1. So (vi) and (vii) are clear.
□
Corollary 4.3.2 If (P, Φ) is as before, the Poincar´e series P∞
n=0 dim(Pn)zn
has radius of convergence ≥
1
δ2 .
This result could be proved without the full strength of Theorem 4.3.1
(as pointed out by D.Bisch), using the principal graph and the trace. The
Poincar´e series of planar subfactors enjoy many special properties as we shall
explore in future papers.
117
