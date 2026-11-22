---
doc_id: ki52
doc_title: "On the asymptotic expansion of the Kashaev invariant of the 5 2 knot Tomotada Ohtsuki Introduction"
section_id: sec-006-5-proof-of-theorem-11
section_title: "Proof of Theorem 1.1"
section_number: 5
pages: 28-30
source_pdf: ki52.pdf
source_sha256: 35ad4ee5a00d4a18
toc_source: inferred
doc_brief: "On the asymptotic expansion of the Kashaev invariant of the 5_2 knot — We give a presentation of the asymptotic expansion of the Kas haev invariant of the52 knot."
duplicate_of: "104171-qt-83"
---
Proof of Theorem 1.1
In this section, we give a proof of Theorem 1.1. In Section 5.1, we give a proof of the
theorem by using lemmas proved in Sections 5.2, 5.3 and 5.4. In Section 5.2, we show
lemmas which calculate the asymptotic expansion.
In Section 5.3, we show a lemma
which veriﬁes the assumption of the saddle point method. In Section 5.4, we show a
lemma which veriﬁes the assumption of the Poisson summation formula.
5.1
Proof of Theorem 1.1
In this section, we give a proof of Theorem 1.1, which presents the asymptotic expansion
of the Kashaev invariant ⟨52 ⟩N of the 52 knot. To obtain the asymptotic expansion, as
mentioned in Section 2.2, we rewrite the sum (14) of ⟨52 ⟩N by using an integral by the
Poisson summation formula (Proposition 4.6) and calculate the asymptotic expansion of
the integral by the saddle point method (Proposition 3.5).
Proof of Theorem 1.1. We recall that ⟨52 ⟩N is presented by the sum (14). By Proposition
4.6 (Poisson summation formula) (see also Remark 4.8 and Appendix B), this sum is
expressed by an integral,
⟨52 ⟩N = eNςN 5/2 q
( ∫
∆′ exp
(
N · V (t, s) −Nς
)
dt ds + O(e−Nε4)
)
(46)
for some ε4 > 0, noting that we verify the assumptions of Proposition 4.6 in Lemma 5.8
below.
In order to apply the saddle point method (Proposition 3.5, see also Remark 3.6 and
Appendix B) to (46), we consider a critical point of ˆV (t, s). From the deﬁnition of ˆV (t, s),
a critical point is a solution of the following equations,
∂
∂t
ˆV (t, s) = −log(1 −e−2π√−1 t) −2π
√
−1
(
t + s −1
2
)
= 0,
∂
∂s
ˆV (t, s) = −2 log(1 −e−2π√−1 s) −2π
√
−1
(
t + 2s −1
)
= 0.
(47)
Hence, putting x = e2π√−1 t and y = e2π√−1 s,
(
1 −1
x
)
xy = −1,
(
1 −1
y
)2xy2 = 1.
Therefore,
x = 1 −1
y ,
(y −1)3 = y.
Let (x0, y0) be the solution of these equations mentioned in the introduction. We consider
the critical point (t0, s0) such that (Re t0, Re s0) ∈∆′ and (e2π√−1 t0, e2π√−1 s0) = (x0, y0).
It is numerically given by
t0 = 0.22404487... −√−1 · 0.04475430... ,
s0 = 0.16393269... + √−1 · 0.06713145... .
28
Let (tc, sc) be the critical point of V (t, s) which goes to (t0, s0) as N →∞. We consider
to apply Proposition 3.5 to V (t −tc, s −sc). We consider the expansion
V (t, s) = V (tc, sc) + 1
2Vtt · (t −tc)2 + Vts · (t −tc)(s −sc) + 1
2Vss · (s −sc)2 + · · · (48)
at the critical point, where we put
Vtt = ∂2V
∂t2 (tc, sc),
Vts =
∂2V
∂t ∂s(tc, sc),
Vss = ∂2V
∂s2 (tc, sc).
As we show in Section 5.3, we can make a concrete homotopy which moves ∆′ to a new
domain containing the above critical point in such a way that it satisﬁes the assumption
of the saddle point method.6
Hence, we obtain the following expansion by applying
Proposition 3.5 (see also Remark 3.6 and Appendix B) to (46),
⟨52 ⟩N = N 5/2 q exp
(
N V (tc, sc)
)
· 2π
N
(
VttVss −V 2
ts
)−1/2(
1 +
d
∑
i=1
λiℏi + O(ℏd+1)
)
, (49)
where λi’s are given in the proposition, noting that we verify the assumptions of Propo-
sition 3.5 in Lemma 5.7 below. Here, we also note that eNς ×O(e−Nε4) in (46) is in-
cluded in exp
(
N V (tc, sc)
)
×O(ℏd+1) in (49); see Lemma 5.2 below for the behavior of
exp
(
N V (tc, sc)
)
.
We calculate the concrete form of (49), for simplicity, when d = 1. By Lemmas 5.2,
5.3 and 5.4 below, (49) is rewritten,
⟨52 ⟩N = N 5/2q × eNς e−π√−1/4(
1 −y0
)1/2 (
1 + (C1 + C2)ℏ+ O(ℏ2)
)
× 2π
N
×
1
2π√−1
(
−2y0 −1
)−1/2(
1 + C3ℏ+ O(ℏ2)
)
×
(
1 + (C4 + C5)ℏ+ O(ℏ2)
)
= eNς N 3/2 eπ√−1/4(2y0 + 1
y0 −1
)−1/2(
1 + ℏ
(
1 + C1 + C2 + C3 + C4 + C5
)
+ O(ℏ2)
)
,
where the constants C1, · · · , C5 are given in the lemmas. In particular, κ1 of the theorem
is given by
κ1 = 1 + C1 + C2 + C3 + C4 + C5
=
1
184(−16y2
0 + 33y0 + 9) + 1
24(2y2
0 −5y0) + 1
46
(
8y2
0 −17y0 + 9
)
+ 1
92(2y2
0 + 15y0) −
1
3174(197y2
0 + 127y0 + 227) + 1
=
1
12696(1650y2
0 −3498y0 + 2197) + 1.
Hence, we obtain the required formula for d = 1.
6That is, the new domain is in the area Re ˆV (t, s) ≤ςR −ε except for a neighborhood of the above critical point.
In order to obtain this new domain, it is suﬃcient to push the shaded part in Figure 1 into the imaginary direction by
(−√−1 · 0.04475430..., √−1 · 0.06713145...). For details, see Section 5.3.
29
For general d, each λi of the expansion (49) is given by a linear sum of higher coeﬃcients
of the expansion (48) by Proposition 3.5 (see also Remark 3.6 and Appendix B). In the
same way as the above case of d = 1, such coeﬃcients are given by some polynomials in y0
with rational coeﬃcients. Hence, each κi of the theorem can be given by some polynomial
in y0 with rational coeﬃcients.
