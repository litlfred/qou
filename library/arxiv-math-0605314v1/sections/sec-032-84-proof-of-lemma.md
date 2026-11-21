---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-032-84-proof-of-lemma
section_title: "Proof of Lemma"
section_number: 8.4
pages: 30-31
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
Lemma 8.7. If y, y′ ∈RQ(v) and x ∈Uh, then we have
tryy′
q
(x) =
X
try
q(x(1))try′
q (x(2)),
where ∆(x) = P x(1) ⊗x(2).
Proof. The assertion follows from the well-known identity for any two ﬁnite-dimensional
representations W, W ′
trW⊗W ′
q
(x) = (trW
q ⊗trW ′
q
)∆(x).
Lemma 8.8. (1) If n, l, l′ ≥0, l̸ = l′ and j ∈Z, then we have trPn
q ( ˜F (l)K2jel′) = 0.
(2) If 0 ≤n < l and j ∈Z, then we have trPn
q ( ˜F (l)K2jel) = 0.
(3) If 0 ≤l ≤n and j ∈Z, then we have
trPn
q ( ˜F (l)K2jel) = vnq−nj+2lj+l2−ln{n}q!{n −l}q!
j + n −1
n −l

q
j −1
n −l

q
.
(8.6)
Proof. The assertion (1) follows from the fact that l̸ = l′ implies that ˜F (l)K2jel′
acts nilpotently on each Vn, n ≥0.
The assertion (2) follows from the fact that Pn is a linear combination of V0, . . . , Vn,
and that if 0 ≤n < l, then el acts as 0 on V0, . . . , Vn.
We prove (3) by induction on n. The case n = l = 0 follows from
trP0
q (K2j) = ǫ(K2j) = 1.
A UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANT
31
Let n ≥1. Set pn = V1 −v2n−1 −v−2n+1, so that Pn = Pn−1pn. Using Lemma
8.7, we have
trPn
q ( ˜F (l)K2jel) = trPn−1pn
q
( ˜F (l)K2jel) =
X
trPn−1
q
(x(1))trpn
q (x(2)),
(8.7)
where
X
x(1) ⊗x(2) = ∆( ˜F (l)K2jel)
=
l
X
r=0
l
X
s=0

l
s

q
( ˜F (l−r)KrK2jel−sKs ⊗˜F (r)K2jes).
Since pn is a linear combination of V0 and V1, we have trpn
q (F (r)K2jes) = 0 unless
(r, s) = (0, 0) or (1, 1). Therefore, the right-hand side of (8.7) equals
trPn−1
q
( ˜F (l)K2jel)trpn
q (K2j) + q−l+1[l]qtrPn−1
q
( ˜F (l−1)K2j+2el−1)trpn
q ( ˜F (1)K2je).
(8.8)
By straightforward computation,
trpn
q (K2j) = v−2j+1{j −n}q{j + n −1}q,
trpn
q ( ˜F (1)K2je) = v2j+1{1}q.
Using these identities and the inductive hypothesis, we can verify that (8.8) equals
the right-hand side of (8.6). This completes the proof.
Proof of Lemma 8.5. It suﬃces to prove that if n ≥0 and x ∈Uev
q , then we have
trP ′
n
q (x) ∈v
1
2 n(n−1)Z[q, q−1]. We may assume without loss of generality that x =
˜F (l)K2jek with j ∈Z, k, l ≥0. By Lemma 8.8, trPn
q (x) ∈vn{n}q!Z[q, q−1] =
v
1
2 n(n−1){n}!Z[q, q−1]. Therefore, we have the assertion.
