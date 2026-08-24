---
doc_id: arxiv-1208.2521v1
doc_title: "On q-analogues of the Fourier and Hankel transforms"
section_id: sec-010-14-tom-h-koornwinder-and-ren-e-f-sw-arttouw
section_title: "TOM H. KOORNWINDER AND REN ´E F. SW ARTTOUW"
section_number: 14
pages: 14-16
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
doc_brief: "On q-analogues of the Fourier and Hankel transforms — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
Remark 4.3. Analogous to (4.2) we have
(4.9) (xs− 1t; q)∞ (−xst− 1; q)∞
(yt; q)∞ (−yt− 1; q)∞
=
∞∑
n=−∞
tn yn (s− 1xy− 1, q n+1; q)∞
(qns− 1xy− 1, q ; q)∞
× 2φ 1
[ qns− 1xy− 1, sxy − 1
qn+1 ; q, −y2
]
, |y| < |t| < |y|− 1.
The case s = 1 of (4.9) goes back to Heine [9, p.121] (see also Hahn [7, §8]). Its
special cases ( x, y, s ) = (0 , z, 1) and ( −z, 0, 1) are the formulas (2.12) and (2.13).
Like (4.2), formula (4.9) is a q-analogue of (1.4) with z and t replaced by 2( y −
s− 1x)1/ 2(y − sx)1/ 2 and t(y − s− 1x)1/ 2(y − sx)− 1/ 2, respectively. Similarly to (4.5)
we obtain from (2.12), (2.13) and (4.9) that, for |y| < 1:
(4.10) yn (s− 1xy− 1, q n+1; q)∞
(qns− 1xy− 1, q ; q)∞
2φ 1
[ qns− 1xy− 1, sxy − 1
qn+1 ; q, −y2
]
=
∞∑
k=−∞
sk yk+n
× (qk+n+1; q)∞
(q; q)∞
2φ 1(0, 0; qk+n+1; q, −y2) xk qk(k− 1)/ 2 (qk+1; q)∞
(q; q)∞
0φ 1(−; qk+1; q, −qkx2).
The special case n = 0 of this formula is the limit case ν ↓ 0 of Rahman’s addition
formula [12, (1.10)]. Like (4.5), formula (4.10) is a q-analogue of Graf’s addition
formula (4.6). The special case x = y, s = 1 of (4.10) gives the biorthogonality
relations (2.14).
5. q-Analogues of the Fourier-cosine and Fourier-sine transfor m
Put
cos(z; q2) := 1φ 1(0; q; q2, q 2 z2)
=
∞∑
k=0
(−1)k qk(k+1) z2k
(q; q)2k
(5.1)
= (q2; q2)∞
(q; q2)∞
z1/ 2 J− 1/ 2(z; q2)(5.2)
and
sin(z; q2) :=(1 − q)− 1 z 1φ 1(0; q3; q2, q 2 z2)
=
∞∑
k=0
(−1)k qk(k+1) z2k+1
(q; q)2k+1
(5.3)
= (q2; q2)∞
(q; q2)∞
z1/ 2 J1/ 2(z; q2).(5.4)
ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS 15
Here we have used the notation (3.3). (The functions introdu ced above should
not be confused with the functions cos q and sin q considered in [6, Exercise 1.14].)
Clearly we have the formal (termwise) limits
cos((1 − q)z; q2) − →cos z and sin((1 − q)z; q2) − →sin z
as q ↑ 1. By Proposition A.2 these limit transitions hold pointwis e, uniformly on
compacta. When we substitute (5.2) or (5.4) in (3.4) and repl ace f (qk), g(qn) by
q− k/ 2f (qk), q− n/ 2g(qn), we obtain the transform pairs
(5.5)















g(qn) = (q; q2)∞
(q2; q2)∞
∞∑
k=−∞
qk



cos(qk+n; q2)
or
sin(qk+n; q2)


 f (qk),
f (qk) = (q; q2)∞
(q2; q2)∞
∞∑
n=−∞
qn



cos(qk+n; q2)
or
sin(qk+n; q2)


 g(qn).
The transformations f ↦→g and g ↦→f of (5.5) establish an isometry of Hilbert
spaces:
∞∑
k=−∞
qk |f (qk)|2 =
∞∑
n=−∞
qn |g(qn)|2.
Now let q ↑ 1 under the side condition that log(1− q)
log q ∈ 2Z. Replace qk, qn in (5.5)
by (1 − q)1/ 2qk, (1 − q)1/ 2qn, and then f ((1 − q)1/ 2qk), g((1 − q)1/ 2qn) by f (qk),
g(qn). Then (5.5) takes the form















g(λ) = (1 + q)1/ 2
Γ q2(1/ 2)
∫ ∞
0
f (x)



cos((1 − q)λx; q2)
or
sin((1 − q)λx; q2)


 dqx,
f (x) = (1 + q)1/ 2
Γ q2(1/ 2)
∫ ∞
0
g(λ)



cos((1 − q)λx; q2)
or
sin((1 − q)λx; q2)


 dqλ.
Formally, as q ↑ 1, we obtain the classical Fourier pairs
g(λ) =
√
2/π
∫ ∞
0
f (x) cos( λx) dx, f (x) =
√
2/π
∫ ∞
0
g(λ) cos( λx) dλ
and
g(λ) =
√
2/π
∫ ∞
0
f (x) sin( λx) dx, f (x) =
√
2/π
∫ ∞
0
g(λ) sin( λx) dλ.
With the notation
(Dqf )(z) = Dq,z f (z) := f (z) − f (qz)
(1 − q)z
