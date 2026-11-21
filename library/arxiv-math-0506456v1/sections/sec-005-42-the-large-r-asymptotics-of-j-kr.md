---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-005-42-the-large-r-asymptotics-of-j-kr
section_title: "The large $r$ asymptotics of $J_{K}'(r)$"
section_number: 4.2
pages: 16-19
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
toc_source: inferred
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
K(r)
We calculate the leading term of the large r asymptotics of J′
K(r), using the saddle
point method like Kashaev [14]. Our calculation supplements the calculation of
Kashaev with the required analytic error estimates. Let
C2
r = C(ε)
=
[
√
−1 + ε, −
√
−1 + ε] + [−
√
−1 + ε, 1 −ε −
√
−1]
+[1 −ε −
√
−1, 1 −ε +
√
−1] + [1 −ε +
√
−1, ε +
√
−1],
where ε ∈]0, 1
4r[. We let C+(ε) be the part of the contour C(ε) above the real axes
and C−(ε) the part below the real axes. By (3.21) we have
J′
K(r) =
√−1r2
2
(J+(r, ε) + J−(r, ε)) ,
where
J±(r, ε) =
Z
C±(ε)
tan(πrx)gr(x)dx.
Away from the real axis, the factor tan(πrx) can be approximated by ±√−1 de-
pending on whether we are in the upper or lower half-plane. In fact we have
| tan(πrx) −
√
−1| ≤
(
4e−2πrIm(x),
Im(x) ≥
1
πr,
2e−2πrIm(x),
rRe(x) ∈Z, Im(x) ≥0
(4.26)
and
| tan(πrx) +
√
−1| ≤
(
4e2πrIm(x),
Im(x) ≤−1
πr,
2e2πrIm(x),
rRe(x) ∈Z, Im(x) ≤0.
(4.27)
Asymptotics of the quantum invariants for the ﬁgure 8 knot
17
Therefore we write
J±(r, ε) = ±
√
−1
Z
C±(ε)
gr(x)dx +
Z
C±(ε)
(tan(πrx) ∓
√
−1)gr(x)dx.
The estimates on tan(πrx) ± √−1 can be used (see Appendix B) to prove that

X
µ=±1
Z
Cµ(ε)
(tan(πrx) −µ
√
−1)gr(x)dx

 ≤K1
1
r ,
(4.28)
where K1 is a constant independent of r and ε. Let now
Φ(x) =
1
2π√−1

Li2(e−2π√−1x) −Li2(e2π√−1x)

.
(4.29)
Note that Φ is analytic on D = C \ { x ∈C | Re(x) ∈Z } but not in the points Z, so
here we see the reason for using the small deformation parameter ε. We have
Z
C±(ε)
gr(x)dx
=
Z
C±(ε)
erΦ(x)dx
+
Z
C±(ε)
(exp (Iγ(π −2πx) −Iγ(−π + 2πx)) −1) erΦ(x)dx.
However, as we will see in Appendix B, the estimate in Lemma 3 implies that

Z
Cµ(ε)
(exp (Iγ(π −2πx) −Iγ(−π + 2πx)) −1) erΦ(x)dx

 ≤K2Log(r)
r
e
r
2πVol(K)
(4.30)
for µ = ±1, where K2 is a constant independent of r and ε. We will see below that
the estimates (4.28) and (4.30) imply that the leading order large r asymptotics of
J′
K(r) is given by
J′
K(r) ∼r2
2
 Z
C−(ε)
erΦ(x)dx −
Z
C+(ε)
erΦ(x)dx
!
,
(4.31)
to which we can apply the saddle point method, see e.g. [6, Chap. 5]. First we
determine the stationary points of the phase function Φ. On D we have
Φ′(x) = Log

1 −e2π√−1x
+ Log

1 −e−2π√−1x
.
If we put z = e2π√−1x, then Φ′(x) = 0 implies that
z2 −z + 1 = 0.
(4.32)
The equation (4.32) has the solutions z± = e±√−1π/3. We have 1−z± = 1/2∓i
√
3/2
which both have norm 1 and are each others conjugate, so
Log (1 −z+) + Log (1 −z−) = 0.
18
Asymptotics of the quantum invariants for the ﬁgure 8 knot
We note that z± = e±2π√−1 1
6 correspond to the x–points ±1/6 + Z. These points
are non-degenerate critical points. In fact,
Φ′′(x) = 2π
√
−1e2π√−1x + 1
e2π√−1x −1
on D, so in particular Φ′′(x±) = ±2π
√
3 for x± ∈±1/6 + Z. The imaginary part
of Φ(x) is zero for x ∈R and
Φ(x) = 1
2π Im

Li2(e−2π√−1x) −Li2(e2π√−1x)

= −1
π Cl2(2πx),
by (4.24). Let x± ∈±1/6 + Z. By (4.25) we have Cl2(2πx−) = −Cl2(2πx+) =
−Cl2(π/3) = −Vol(K)/2, i.e.
Φ(x±) = ∓1
2πVol(K).
By Cauchy’s theorem we have
Z
C−(ε)
erΦ(x)dx −
Z
C+(ε)
erΦ(x)dx = 2
Z
C−(ε)
erΦ(x)dx = −2
Z
C+(ε)
erΦ(x)dx.
Deform C−(ε) to [ε, 1 −ε] keeping the end points ﬁxed. This does not change the
integral
R
C−(ε) erΦ(x)dx. Let x0 = 5/6. By terminology borrowed from [6, Sec. 5.4]
the axis of the saddle point x0 is the real axis (i.e. the directions of steepest descent
are along the real axis). From the analysis of [6, Sec. 5.7] it follows that we can ﬁnd
a δ > 0 (independent of r and ε) such that [x0 −δ, x0 + δ] ⊆[1/(4r), 1 −1/(4r)] and
such that we have an asymptotic expansion
Z δ
−δ
erΦ(x0+t)dt ∼
1
31/4√re
r
2πVol(K)
 
1 +
∞
X
n=1
dnr−n
!
in the limit r →∞, where the dn’s are certain complex numbers. Finally we note
that

Z x0−δ
ε
erΦ(t)dt +
Z 1−ε
x0+δ
erΦ(t)dt

 ≤erc,
where c = max{−Cl2(2π(x0 −δ))/π, −Cl2(2π(x0 + δ))/π} < Vol(K)/2π, see above
(4.25). We have shown
Lemma 4. The leading order large r asymptotics of J′
K(r) is given by
J′
K(r) ∼3−1/4r3/2 exp
 r
2πVol(K)

.
(4.33)
In fact
J′
K(r) = 3−1/4r3/2 exp
 r
2π Vol(K)

+ O

rLog(r) exp
 r
2πVol(K)

in the limit r →∞.
Asymptotics of the quantum invariants for the ﬁgure 8 knot
19
In particular
lim
r→∞
2πLog(J′
K(r))
r
= Vol(K)
as predicted by the volume conjecture of Kashaev [14] and Murakami, Murakami
[24] and as proven by Ekholm and others, see [22].
However, the arguments of
Ekholm and others can’t see the ﬁner details of the asymptotic behaviour (4.33),
namely the polynomial part 3−1/4r3/2.
Remark 2. The complement S3 \ K of the ﬁgure 8 knot can be decomposed into
two ideal hyperbolic tetrahedra each parametrized by a certain complex number.
This decomposition then deﬁnes a hyperbolic structure on this complement if and
only if a certain set of conditions is satisﬁed. In fact, if the complex parameters for
the two tetrahedra are respectively a and b, then these conditions are equivalent
to a = b and b2 −b + 1 = 0, which is equation (4.32) after substituting b for z.
We refer to [23, Sec. 3] for more details.
This phenomenon, that one ﬁnds the
hyperbolicity equation for the knot complement as the equation for the stationary
points of the phase function, seems to be a general principal for hyperbolic knots as
argued by Thurston and Yokota, cf. [32], [35]. However, there are major unsolved
analytic diﬃculties in their approach. Basically they conjecture that one can carry
out an asymptotic analysis similar to the one we carried out above for the ﬁgure 8
knot. To prove their conjecture one ﬁrst has to show how to give an exact (multi-
dimensional) contour integral formula for the Jones polynomial of a hyperbolic
knot like our (3.21). A main part consists of choosing a correct (multi-dimensional)
contour. Secondly, one has to carry out an asymptotic analysis similar to the one
leading to (4.31). This analysis is relatively simple for the ﬁgure 8 knot due to
the fact that we have a single (one-dimensional) contour in this case. In general
one gets a contour of dimension > 1 and the asymptotic analysis is expected to be
harder (as also illustrated by the asymptotic analysis of the double-contour integral
expression for the invariant ¯τr(Mp/q) in Lemma 2, see next section.)
