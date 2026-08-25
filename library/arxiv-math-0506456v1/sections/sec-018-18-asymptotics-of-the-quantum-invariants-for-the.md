---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-018-18-asymptotics-of-the-quantum-invariants-for-the
section_title: "Asymptotics of the quantum invariants for the ﬁgure 8 knot"
section_number: 18
pages: 17-19
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
Therefore we write
J±(r,ε ) = ±
√
−1
∫
C±(ε)
gr(x)dx +
∫
C±(ε)
(tan(πrx) ∓
√
−1)gr(x)dx.
The estimates on tan( πrx) ± √−1 can be used (see Appendix B) to prove that
⏐
⏐
⏐
⏐
⏐
∑
µ=±1
∫
Cµ (ε)
(tan(πrx) −µ
√
−1)gr(x)dx
⏐
⏐
⏐
⏐
⏐ ≤K1
1
r, (4.28)
where K1 is a constant independent of r and ε. Let now
Φ(x) = 1
2π√−1
(
Li2(e−2π√−1x) − Li2(e2π√−1x)
)
. (4.29)
Note that Φ is analytic on D = C \ {x ∈ C | Re(x) ∈ Z } but not in the points Z, so
here we see the reason for using the small deformation parameter ε. We have
∫
C±(ε)
gr(x)dx =
∫
C±(ε)
erΦ(x)dx
+
∫
C±(ε)
(exp (Iγ(π − 2πx) −Iγ(−π + 2πx)) − 1)erΦ(x)dx.
However, as we will see in Appendix B, the estimate in Lemma 3 implies tha t
⏐
⏐
⏐
⏐
⏐
∫
Cµ (ε)
(exp (Iγ(π − 2πx) −Iγ(−π + 2πx)) − 1)erΦ(x)dx
⏐
⏐
⏐
⏐
⏐ ≤ K2Log(r)
r e
r
2π Vol(K)
(4.30)
forµ = ±1, where K2 is a constant independent of r andε. We will see below that
the estimates (4.28) and (4.30) imply that the leading order large r asymptotics of
J ′
K(r) is given by
J ′
K(r) ∼ r2
2
(∫
C−(ε)
erΦ(x)dx −
∫
C+(ε)
erΦ(x)dx
)
, (4.31)
to which we can apply the saddle point method, see e.g. [6, Chap. 5]. Fir st we
determine the stationary points of the phase function Φ. On D we have
Φ ′(x) = Log
(
1 −e2π√−1x
)
+ Log
(
1 −e−2π√−1x
)
.
If we put z =e2π√−1x, then Φ ′(x) = 0 implies that
z2 −z + 1 = 0. (4.32)
The equation (4.32) has the solutions z± =e±√−1π/3. We have 1 −z± = 1/2∓i
√
3/2
which both have norm 1 and are each others conjugate, so
Log (1 −z+) + Log (1 −z−) = 0.
18 Asymptotics of the quantum invariants for the ﬁgure 8 knot
We note that z± =e±2π√−1 1
6 correspond to the x–points ±1/6 + Z. These points
are non-degenerate critical points. In fact,
Φ ′′(x) = 2π
√
−1e2π√−1x + 1
e2π√−1x − 1
on D, so in particular Φ ′′(x±) = ±2π
√
3 for x± ∈ ± 1/6 + Z. The imaginary part
of Φ( x) is zero for x ∈ R and
Φ(x) = 1
2π Im
(
Li2(e−2π√−1x) − Li2(e2π√−1x)
)
= − 1
π Cl2(2πx),
by (4.24). Let x± ∈ ± 1/6 + Z. By (4.25) we have Cl 2(2πx−) = −Cl2(2πx+) =
−Cl2(π/3) = −Vol(K)/2, i.e.
Φ(x±) = ∓ 1
2π Vol(K).
By Cauchy’s theorem we have
∫
C−(ε)
erΦ(x)dx −
∫
C+(ε)
erΦ(x)dx = 2
∫
C−(ε)
erΦ(x)dx = −2
∫
C+(ε)
erΦ(x)dx.
Deform C−(ε) to [ε, 1 −ε] keeping the end points ﬁxed. This does not change the
integral
∫
C−(ε)erΦ(x)dx. Let x0 = 5/6. By terminology borrowed from [6, Sec. 5.4]
the axis of the saddle point x0 is the real axis (i.e. the directions of steepest descent
are along the real axis). From the analysis of [6, Sec. 5.7] it follows th at we can ﬁnd
aδ >0 (independent of r andε) such that [x0 −δ,x 0 +δ] ⊆ [1/(4r), 1 − 1/(4r)] and
such that we have an asymptotic expansion
∫ δ
−δ
erΦ(x0+t)dt ∼ 1
31/4√re
r
2π Vol(K)
(
1 +
∞∑
n=1
dnr−n
)
in the limit r → ∞ , where the dn’s are certain complex numbers. Finally we note
that ⏐
⏐
⏐
⏐
⏐
∫ x0−δ
ε
erΦ(t)dt +
∫ 1−ε
x0+δ
erΦ(t)dt
⏐
⏐
⏐
⏐
⏐ ≤erc,
wherec = max{−Cl2(2π(x0 −δ))/π, −Cl 2(2π(x0 +δ))/π}< Vol(K)/2π, see above
(4.25). We have shown
Lemma 4. The leading order large r asymptotics of J ′
K(r) is given by
J ′
K(r) ∼ 3−1/4r3/2 exp
(r
2π Vol(K)
)
. (4.33)
In fact
J ′
K(r) = 3 −1/4r3/2 exp
(r
2π Vol(K)
)
+ O
(
rLog(r) exp
(r
2π Vol(K)
))
in the limit r → ∞.
