---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS"
section_id: sec-105-42-existence-of-asymptotic-solutions-55
section_title: "EXISTENCE OF ASYMPTOTIC SOLUTIONS 55"
section_number: 4.2
pages: 61-62
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symm"
---
We agree that f−1≡ 0 and f0 = h0/a. Iterating the last relation (4.1)
above, we ﬁnd:
(4.2) ∀j∈ N∗, fj =−
j∑
ℓ=0
qµℓ(ℓ−1)/2zℓµσℓ
qhj−ℓa−ℓ−1.
Writef the function deﬁned on U by the relations f|Uj =fj, j∈ N; Clearly,
Lf =h on U. We are left to show that f∈ A0(U∞).
Letn∈ N and V a strict stable subset of U; let Vj :=Uj∩V and choose a
K >0 such that|z|≤ K|q|−j for all z∈Uj; one has|z|≤ K|q|−j on each Vj.
Bounding by above the right hand side of (4.2), one gets:
(4.3) ∀z∈Vj ,|fj(z)|≤ Cn,V
a Pj(|q|nα)|z|n,
where α := K µ/a and where Pj denotes the polynomial with positive coeﬃ-
cients:
Pj(X) :=
j∑
ℓ=0
|q|µℓ(ℓ−1)/2−jℓµ X ℓ.
Taking in account the relation
Pj+1(X) =Pj(|q|−µX) +|q|−µ(j+1)(j+2)/2 X j+1,
one ﬁnds that Pj(X)≤P (X;µ,q ) for all X >0, where we write P (z;µ,q ) the
entire function deﬁned by:
P (z;µ,q ) :=
∞∑
j=0
|q|−µj(j+1)/2 zj.
Said otherwise, (4.3) can be written in the form:
∀z∈Vj ,|fj(z)|≤ Cn,V
a P (|q|nα;µ,q )|z|n,
which allows us to conclude that f is ﬂat.
We now apply theorem 4.2.1 to a situation that we shall meet wh en we
prove theorem 4.4.1.
Let A0 ∈ GLn(C({z})) be the matrix of a pure module and let
A∈ GLn(C({z})) a matrix formally equivalent to A0. Let ˆF∈ GLn(C((z)))
be a gauge transformation proving this equivalence, i.e. ˆF[A0] = A. (Note
that we do not assume ˆF∈ G(C((z))).) The conjugation relation is equiva-
lent to σq ˆF = A ˆFA −1
0 , which we regard as a q-diﬀerence system of rank n2
in the space Mat n(C({z})) ≃ C({z})n2
. After theorem 4.2.1, there exists
56 CHAPTER 4. THE q-ANALOGS OF BIRKHOFF-MALGRANGE-SIBUYA THEOREMS
over each adequate open set U a solution FU∈ Matn(C({z})) of the system
σqF =AFA −1
0 that is asymptotic to ˆF. Since the latter is invertible, and since
detFU is obviously asymptotic to det ˆF, whence non zero, FU is invertible.
Now letU ′ another adequate open set which meetsU. Then U ′′ :=U∩U ′ is
adequate and the matrix G :=F −1
U FU ′ satisﬁes the two following properties:
1. It is an automorphism of A0, i.e. G[A0] =A0.
