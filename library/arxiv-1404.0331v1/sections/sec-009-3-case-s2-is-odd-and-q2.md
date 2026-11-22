---
doc_id: arxiv-1404.0331v1
doc_title: "THE STRONG AJ CONJECTURE FOR CABLES OF TORUS KNOTS"
section_id: sec-009-3-case-s2-is-odd-and-q2
section_title: "Case s>2 is odd and q>2"
section_number: 3
pages: 6-7
source_pdf: 1404.0331v1.pdf
source_sha256: 53d7ce3afaf405e1
toc_source: outline
doc_brief: "THE STRONG AJ CONJECTURE FOR CABLES OF TORUS KNOTS — The AJ conjecture, formulated by Garoufalidis, relates the A-polynomial and the colored Jones polynomial of a knot in the 3-sphere."
---
From [Tr, Lemma 1.1] we have JT(n + 2) −t−4pq(n+1)JT(n) ∈R[t±2n], i.e.
(3.1)
(L2 −t−4pqM−2pq)JT ∈R[M±1].
Lemma 3.1. For all positive integers m, one has
(L2m −t−4pqm2M−2pqm)JT ∈R[M±1].
Proof. From (3.1) we have (L2M2pq −t4pq)JT ∈R[M±1]. It follows that
((L2M2pq)m −t4pqm)JT ∈R[M±1].
Since (L2M2pq)m = t−4pqm(m−1)L2mM2pqm, we have (L2mM2pqm −t4pqm2)JT ∈R[M±1].
The lemma follows since L2mM2pqm = t8pqm2M2pqmL2m.
□
Proposition 3.2. One has
(L2M2pqs2 + L−2M−2pqs2 −t4r−4pqs −t−4r+4pqs+8pqs2)G1
∈
R[M±1],
(L2M2pqs2 + L−2M−2pqs2 −t−4r+4pqs −t4r−4pqs+8pqs2)G2
∈
R[M±1].
Proof. From Lemma 3.1 we have
JT(s(n + 3) + 1) −t−4pqs(sn+2s+1)JT(s(n + 1) + 1) ∈R[t±2n].
It follows that G1(n + 2) −t4r−4pqs(sn+2s+1)G1(n) ∈R[t±2n]. Hence
(L2 −t4r−4pqs(2s+1)M−2pqs2)G1 ∈R[M±1],
which implies that (L2M2pqs2 −t4r−4pqs)G1 ∈R[M±1]. Hence
(1 −t−4r+4pqsL−2M−2pqs2)(L2M2pqs2 −t4r−4pqs)G1 ∈R[M±1].
The proof for G2 is similar.
□
Let
P1
:=
L2M2pqs2 + L−2M−2pqs2 −t4r−4pqs −t−4r+4pqs+8pqs2,
P2
:=
L2M2pqs2 + L−2M−2pqs2 −t−4r+4pqs −t4r−4pqs+8pqs2.
Note that σ(Pi) = Pi and P1P2 = P2P1. By Proposition 3.2, we have PiGi ∈R[M±1] for
i = 1, 2. Let P = P1P2. Then σ(P) = P and PGi ∈R[M±1].
By Lemma 2.3, we can choose Q ∈R[L±1] such that σ(Q) = Q, ε(Q) = (L+L−1 −2)m
for some m ≥1, and Q(PGi) = 0 for all i = 1, 2.
From (2.2) we have QPMrs(L2 −t−4rsM−2rs)JC = 0. Let
R := MrsQPMrs(L2 −t−4rsM−2rs) + M−rsQPM−rs(L−2 −t−4rsM2rs).
Then σ(R) = R. Since AC is invariant under σ (by [Ga1]), we have RJC = 0. Note that
ε(R)
=
(L2M2rs + L−2M−2rs −2)ε(QP)
=
(L2M2rs + L−2M−2rs −2)(L2M2pqs2 + L−2M−2pqs2 −2)2(L + L−1 −2)m.
STRONG AJ CONJECTURE
7
Let k := max{m, 2} and S := (L2M2rs + L−2M−2rs −2)k−1(L2M2pqs2 + L−2M−2pqs2 −
2)k−2(L + L−1 −2)k−m. We have σ(S) = S and
ε(SR)
=

(L2M2rs + L−2M−2rs −2)(L2M2pqs2 + L−2M−2pqs2 −2)(L + L−1 −2)
k
=
M2(r+pqs)skL−5k 
(L −1)(L2 −M−2pqs2)(L2 −M−2rs)
2k
.
Since SR ∈Aσ
C and ε(SR) = M2(r+pqs)skL−5k(AC)2k, Lemma 2.2 implies that p ⊂
p
ε(Aσ
C). This proves Theorem 1 in the case s > 2 is odd and q > 2.
