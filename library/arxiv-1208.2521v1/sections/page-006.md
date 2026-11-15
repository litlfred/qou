---
doc_id: arxiv-1208.2521v1
doc_title: "ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS"
section_id: page-006
section_title: "Page 6"
section_number: null
pages: 6-6
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
toc_source: undetermined
doc_brief: "ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
6
TOM H. KOORNWINDER AND REN´E F. SWARTTOUW
Remark 2.4. Because of (2.6), the behaviour of the two equal sides of (2.3) as
|w| →∞(cf. (2.4)) drastically improves when w runs over the values q1−n, n =
1, 2, . . .. For such w we can majorize these expressions by
qn(n−1)/2 |z|n (−|z|; q)∞(−q; q)∞.
We will now restate Exton’s generating function (1.5) in terms of the notation
(2.2), and also give the short proof, for reasons of completeness.
Proposition 2.5. For z, t ∈C such that 0 < |t| < |z|−1 there is the absolutely
convergent expansion
eq(tz) Eq(−t−1z) = (t−1z; q)∞
(tz; q)∞
=
∞
X
n=−∞
tn zn (qn+1; q)∞
(q; q)∞
1φ1(0; qn+1; q, z2)
(2.7)
=
∞
X
n=−∞
tn zn (z2; q)∞
(q; q)∞
1φ1(0; z2; q, qn+1).
(2.8)
Proof. Expansion of the left-hand side of (2.7) gives
∞
X
k=0
∞
X
l=0
(−1)k qk(k−1)/2 tl−k zl+k
(q; q)k (q; q)l
=
∞
X
k=0
∞
X
l=−∞
(ql+1; q)∞(−1)k qk(k−1)/2 tl−k zl+k
(q; q)∞(q; q)k
,
which is an absolutely convergent double sum for z, t ∈C such that 0 < |t| < |z|−1.
Now pass to new summation variables k, n by substituting l = k + n. This yields,
by substitution of (2.2), the right-hand side of (2.7). Formula (2.8) follows by the
symmetry (2.3).
□
In §3 we will show that (2.8) is a q-analogue of an inﬁnite integral of Weber and
Sonine. Replace in (2.7) t by t−1 and multiply the new identity with the original
identity. The resulting formula
(2.9)
1 =
∞
X
n=−∞
∞
X
m=−∞
tn−mzn (qn+1; q)∞
(q; q)∞
1φ1(0; qn+1; q, z2)
× zm (qm+1; q)∞
(q; q)∞
1φ1(0; qm+1; q, z2)
is absolutely convergent for z, t ∈C such that t̸ = 0 and |z| < |t| < |z|−1. So
equality of coeﬃcients of equal powers of t at both sides yields a q-analogue of the
orthogonality relations (1.8):
