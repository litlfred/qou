---
doc_id: arxiv-1208.2521v1
doc_title: "On q-analogues of the Fourier and Hankel transforms"
section_id: sec-004-6-tom-h-koornwinder-and-ren-e-f-sw-arttouw
section_title: "TOM H. KOORNWINDER AND REN ´E F. SW ARTTOUW"
section_number: 6
pages: 6-8
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
doc_brief: "On q-analogues of the Fourier and Hankel transforms — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
Remark 2.4. Because of (2.6), the behaviour of the two equal sides of (2.3 ) as
|w| → ∞ (cf. (2.4)) drastically improves when w runs over the values q1− n, n =
1, 2, . . . . For such w we can majorize these expressions by
qn(n− 1)/ 2 |z|n (−|z|; q)∞ (−q; q)∞ .
We will now restate Exton’s generating function (1.5) in ter ms of the notation
(2.2), and also give the short proof, for reasons of complete ness.
Proposition 2.5. For z, t ∈ C such that 0 < |t| < |z|− 1 there is the absolutely
convergent expansion
eq(tz) Eq(−t− 1z) = (t− 1z; q)∞
(tz; q)∞
=
∞∑
n=−∞
tn zn (qn+1; q)∞
(q; q)∞
1φ 1(0; qn+1; q, z 2)
(2.7)
=
∞∑
n=−∞
tn zn (z2; q)∞
(q; q)∞
1φ 1(0; z2; q, q n+1).(2.8)
Proof. Expansion of the left-hand side of (2.7) gives
∞∑
k=0
∞∑
l=0
(−1)k qk(k− 1)/ 2 tl− k zl+k
(q; q)k (q; q)l
=
∞∑
k=0
∞∑
l=−∞
(ql+1; q)∞ (−1)k qk(k− 1)/ 2 tl− k zl+k
(q; q)∞ (q; q)k
,
which is an absolutely convergent double sum for z, t ∈ C such that 0 < |t| < |z|− 1.
Now pass to new summation variables k, n by substituting l = k + n. This yields,
by substitution of (2.2), the right-hand side of (2.7). Form ula (2.8) follows by the
symmetry (2.3). □
In §3 we will show that (2.8) is a q-analogue of an inﬁnite integral of Weber and
Sonine. Replace in (2.7) t by t− 1 and multiply the new identity with the original
identity. The resulting formula
(2.9) 1 =
∞∑
n=−∞
∞∑
m=−∞
tn− mzn (qn+1; q)∞
(q; q)∞
1φ 1(0; qn+1; q, z 2)
× zm (qm+1; q)∞
(q; q)∞
1φ 1(0; qm+1; q, z 2)
is absolutely convergent for z, t ∈ C such that t ⁄= 0 and |z| < |t| < |z|− 1. So
equality of coeﬃcients of equal powers of t at both sides yields a q-analogue of the
orthogonality relations (1.8):
ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS 7
Proposition 2.6. For |z| < 1 and n, m ∈ Z we have
(2.10)
∞∑
k=−∞
zk+n (qn+k+1; q)∞
(q; q)∞
1φ 1(0; qn+k+1; q, z 2)
× zk+m (qm+k+1; q)∞
(q; q)∞
1φ 1(0; qm+k+1; q, z 2) = δnm
and
(2.11)
∞∑
k=−∞
zk+n (z2; q)∞
(q; q)∞
1φ 1(0; z2; q, q n+k+1)
× zk+m (z2; q)∞
(q; q)∞
1φ 1(0; z2; q, q m+k+1) = δnm,
where the sums at the left-hand sides are absolutely converg ent, uniformly on com-
pact subsets of the open unit disk.
Formula (2.11) follows from (2.10) by the symmetry (2.3). In §3 we will show
that (2.11) is a q-version of Hankel’s Fourier-Bessel integral (1.9).
Remark 2.7. Analogous to Proposition 2.5 there are the two generating fu nctions
for the q-Bessel functions J (1)
α (x; q) and J (2)
α (x; q) of Jackson and Ismail [10]:
(2.12) eq(tz) eq(−t− 1z) = 1
(tz; q)∞ (−t− 1z; q)∞
=
∞∑
n=−∞
tn zn (qn+1; q)∞
(q; q)∞
2φ 1(0, 0; qn+1; q, −z2), |z| < |t| < |z|− 1,
and
(2.13) Eq(tz) Eq(−t− 1z) = ( −tz; q)∞ (t− 1z; q)∞
=
∞∑
n=−∞
tn zn qn(n− 1)/ 2 (qn+1; q)∞
(q; q)∞
0φ 1(−; qn+1; q, −qn z2).
In a way similar to (2.10) we can now derive the biorthogonali ty relations
(2.14)
∞∑
k=−∞
zk+n (qn+k+1; q)∞
(q; q)∞
2φ 1(0, 0; qn+k+1; q, −z2)
× zk+m q(m+k)(m+k− 1)/ 2 (qm+k+1; q)∞
(q; q)∞
0φ 1(−; qm+k+1; q, −qm+k z2) = δnm,
valid for |z| < 1 and n, m ∈ Z. The case n = m of this result goes back to Jackson
(see also [7, §8]). Formula (2.14) can be rewritten in several ways by subst itution
of the transformations
0φ 1(−; c; q, cz ) = ( z; q)∞ 2φ 1(0, 0; c; q, z ) = 1
(c; q)∞
1φ 1(z; 0; q, c ).
However, this will not transform (2.14) into an orthogonali ty; it remains a biorthog-
onality.
