---
doc_id: arxiv-hep-th-9211141v1
doc_title: "ITD 92/93–9"
section_id: sec-001-c-the-ordinary-diﬀerential-equations
section_title: "The Ordinary Diﬀerential Equations"
section_number: C
pages: 5-9
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
doc_brief: "ITD 92/93–9 — 13 sections: INTRODUCTION AND SUMMARY OF RESULT; The Ordinary Diﬀerential Equations; THE SYSTEM OF PARTIAL DIFFERENTIAL"
---
For the special case J = (s, ∞) the above equations can be used to show that q(s; λ)
(the quantity q of the last section corresponding to the end-point s) satisﬁes
q′′ = s q + 2q3 ,
(′= d
ds)
(1.11)
with
q(s; λ) ∼
√
λ Ai(s)
as s →∞.
(1.12)
This equation is a special case of the PII diﬀerential equation [1,16,18,25]. One can similarly
derive for R(s) := R(s, s), which in view of (1.1) equals
d
ds log D(J; λ) ,
the third-order equation
1
2
 R′′
R′
!′
−R
R′ + R′ = 0 .
(1.13)
5
It is also the case that
R′(s) = −q(s; λ)2
(1.14)
and this gives the following simple formula for D(J; λ) in terms of a PII transcendent:
D(J; λ) = exp

−
Z ∞
s (x −s)q(x; λ)2 dx

.
(1.15)
This is much simpler than the corresponding representation of D(J; λ) for the sine kernel
in terms of a PV transcendent. The fact that q(s; λ) satisﬁes (1.11) can also be obtained by
combining some results in [1,5,13]. Thus in this case of a semi-inﬁnite interval our results
connect with inverse scattering.
D. Asymptotics and the Commuting Diﬀerential Operator
Again we take J = (s, ∞) and consider asymptotics as s →−∞.
(Asymptotics as
s →∞can be obtained trivially from the Neumann series for (I −K)−1.) From the random
matrix point of view the interesting quantities are
E(n; s) := (−1)n
n!
∂n
∂λn D(I; λ)

λ=1 .
This is the probability that exactly n eigenvalues lie in J. Using our diﬀerential equations
plus the known asymptotics of q(s; 1) as s →−∞[13] we obtain the asymptotic expansions
R(s; 1) ∼1
4s2 −1
8 s +
9
64 s4 −
189
128 s7 + 21663
512 s10 + · · ·
(s →−∞).
(1.16)
(where R(s; 1) denotes R(s) corresponding to λ = 1) and
E(0; s) = D(J; 1) ∼
τ0
(−s)1/8 exp

s3/12

×

1 −
3
26 s3 + 2025
213 s6 −2470825
219 s9
+ · · ·

(s →−∞)
(1.17)
where τ0 is an undetermined constant.
The analogue of this formula for the sine kernel was obtained by Dyson [8]. The ana-
logue of our constant τ0 in the expansion was found to be equal to 21/12e3ζ′(−1) (ζ(s) is the
6
Riemann zeta function). This constant was obtained by scaling a result of the second author
[30] on Toeplitz matrices. Such a result is not available to us now. Using (1.16) and the fact
that R(s) is the logarithmic derivative of E(0; s), it is straightforward to derive an integral
representation for log τ0. This integral can be evaluated approximately by numerically inte-
grating (1.11) and using (1.14). This leads to the value log τ0 ≃−0.136540. We conjecture
that in fact
τ0 = eζ′(−1) 2
1
24 = 0.87237 14149 54127 . . . .
This agrees with the numerically computed value, up to its degree of accuracy.
For asymptotics of E(n; s) for general n we introduce
r(n; s) := E(n; s)
E(0; s) .
Successive diﬀerentiation of (1.11) with respect to λ, plus the known asymptotics of q(s; 1),
allows us to ﬁnd asymptotic expansions for the quantities
qn(s) := ∂nq
∂λn

λ=1
(1.18)
(for the analogue in the sine kernel case see [2]); and these in turn can be used to ﬁnd
expansions for r(n; s). One drawback of this approach is that yet another undetermined
constant factor enters the picture.
(In [2,31] Toeplitz and Wiener-Hopf techniques, not
available for the Airy kernel, ﬁxed this constant.)
Another drawback is that when one
expresses the r(n; s) in terms of the qn(s) a large amount of cancellation takes place, with
the result that even the ﬁrst-order asymptotics of r(n; s) are out of reach by this method
when n is large.
There is, however, another approach (brieﬂy indicated in [2], and with details in [28], for
the sine kernel case). We have
r(n; s) =
X
i1<···<in
λi1 · · · λin
(1 −λi1) · · · (1 −λin)
(1.19)
where λ0 > λ1 > · · · are the eigenvalues of the integral operator K (with λ = 1). Now just
as the operator with the sine kernel commutes with the diﬀerential operator for the prolate
7
spheroidal wave functions [14], so does the Airy operator commutes with the diﬀerential
operator L given by
Lf(x) = ((x −s) f ′(x))′ −x(x −s)f(x) .
(1.20)
An application of the WKB method, plus a trick allows us to derive the following asymptotic
formula for λi with i ﬁxed:
1 −λi ∼
√π
i! 25i+3 t3i/2+3/4 exp

−8
3t3/2

(s = −2t →−∞).
(1.21)
(The analogue of this for the sine kernel is in [11].) From this and (1.19) we deduce
r(n, −2t) ∼1!2! · · ·(n −1)!
πn/2 2(5n2+n)/2 t−3n2/4 exp
8
3nt3/2

.
(1.22)
(Note that this can be used to ﬁx the constant mentioned in the last paragraph.)
E. Probability Density for the nth Largest Eigenvalue
An elementary probability argument shows that if F(n; s) (n = 0, 1, · · ·) denotes the
probability density for the (scaled) position of the nth largest eigenvalue (n = 0 is the
largest), then
F(0; s) = dE(0; s)
ds
and for n ≥1
F(n; s) −F(n −1, s) = dE(n; s)
ds
.
From the preceding expressions for E(n; s) in terms of q(s; 1) and qn(s) we can derive
formulas for F(n; s) which can in turn be numerically evaluated to produce tables of values
for these probability densities. We have done this for n = 0 and n = 1 and in Fig. 1 we plot
E(0; s) and E(1; s) and in Fig. 2 we plot F(0; s) and F(1; s).
8
