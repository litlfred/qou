---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-046-b4-compositions-of-bps-automorphisms
section_title: "B.4. Compositions of BPS automorphisms"
section_number: null
pages: 47-48
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
ﬁx a convex sector ∆ ⊂ C∗. Fix ǫ > 0 and take R > 0 as in Lemma B.1. Recall the notion of the
height of a ray from Section 2.5. For each ray ℓ⊂ ∆ deﬁne M(ℓ) > 0 as in the proof of Proposition
B.3 so that ( 57) and ( 58) hold. Note that if a ray has height > H then by the second inequality
in ( 53) we have‖γ‖ > H/k 2 for all nonzero terms in the sum ( 57). It follows that by increasing R
we can assume that for all H > 0
∑
H(ℓ)>H
M(ℓ) < ǫ· e−H. (63)
The proof of Proposition B.3 shows that for each S > R and each ray ℓ⊂ ∆ the map S(ℓ)
gives a well-deﬁned embedding U∆ (S + M(ℓ))→ U∆ (S). For each H > 0, the composition in
anti-clockwise order of the ∆-map germs S(ℓ) corresponding to the ﬁnitely many rays ℓ⊂ ∆ of
height≤ H therefore gives a well-deﬁned map U∆ (R + ǫ)→ U∆ (R), and hence a bounded ∆-map
germ
S(∆) ≤H =
∏
H(ℓ)≤H
S(ℓ)∈ Aut∆ (T).
The remaining task is to make sense of the limit of this map germ as H→∞ .
Suppose that a ∆-map germ f is well-deﬁned on the open subset U∆ (R)⊂ T. We deﬁne the
R-norm of f to be the inﬁmum of the real numbers K > 0 such that for all β∈ Γ and all ξ∈ U∆ (R)
e−K·‖β‖|xβ(ξ)|≤| xβ(f (ξ))|≤ eK·‖β‖|xβ(ξ)|.
The proof of Proposition B.3 shows that the ∆-bounded map germ S(ℓ) is well-deﬁned on U∆ (R+ǫ)
and has norm < M (ℓ) there.
48 TOM BRIDGELAND
Lemma B.4. Suppose given a sequence of invertible ∆ -bounded map germs fn∈ G∆ (T), all deﬁned
on a ﬁxed U∆ (R), and such that the R-norm d(m, n) of the composite f −1
n ◦ fm goes to zero as
min(m, n)→∞ . Then the holomorphic maps fn have a uniform limit, which is itself an invertible
∆ -bounded map germ, and hence deﬁnes a limiting element f∞∈ G∆ (T).
Proof. By deﬁnition, for any ξ∈ U∆ (R) we have
e−d·‖β‖|xβ(fm(ξ))|≤| xβ(fn(ξ))|≤ ed·‖β‖|xβ(fm(ξ))|,
where d = d(m, n). Thus the xβ(fn(ξ)) converge uniformly on compact subsets. □
Proposition B.5. The ∆ -map germs S(∆) ≤H have a well-deﬁned limit
S(∆) = lim
H→∞
S(∆) ≤H∈ Aut∆ (T).
Proof. Let us consider two ﬁnite compositions P1 and P2 of the maps S(ℓ) with ℓ⊂ ∆ as above,
which diﬀer by the insertion of one extra term. Thus the two produc ts can be written in the form
P1 = AC and P2 = ABC with
A =
∏
i
S(ℓi), B = S(ℓj), C =
∏
k
S(ℓk).
The composite map germ X = P2P −1
1 is well-deﬁned on U∆ (R + 2ǫ). We claim that it has norm
< 2M(ℓj) there. Given heights H2 > H 1 > 0 we can apply the claim repeatedly and use ( 63) to
deduce that
S(∆) ≤H2 = S(∆) ≤H1◦ X(H1, H2),
where X(H1, H2) has norm at most 2 ǫ· e−H1. The result then follows from Lemma B.4.
To prove the claim, note ﬁrst that X = ABA−1 is also the time 1 ﬂow of a vector ﬁeld on T,
namely the Hamiltonian vector ﬁeld of the function DT( ℓj)◦ A−1 pushed forward by the map A.
We can therefore apply the same argument as in Proposition B.3 provided we can bound the norm
of this vector ﬁeld as in ( 61). To do this it is enough to bound the norm of the diﬀerence between
the derivative of the map A and the identity at points of U∆ (R). This in turn is achieved by the
same argument as Proposition B.3 using the p = 2 case of inequality ( 57). We leave the details to
the reader. □
