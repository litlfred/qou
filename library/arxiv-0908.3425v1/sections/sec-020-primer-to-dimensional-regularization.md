---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-020-primer-to-dimensional-regularization
section_title: "Primer to dimensional regularization"
section_number: null
pages: 33-35
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
If we want to use the Lagrangian of Eq. (114) beyond the tree le vel, we will encounter ultraviolet diver-
gences from loop integrals. For the regularization of the lo op diagrams we will make use of dimensional
regularization [’t Hooft and Veltman, 1972], [Leibbrandt, 1975], [’t Hooft and Veltman, 1979], because
it preserves algebraic relations between the Green functio ns (Ward identities). We will illustrate the
method by considering the following simple example,
I =
∫ d4k
(2π)4
i
k2 −M 2 +i0+, (130)
which shows up in the generic diagram of Fig. 4. Introducing a ≡
√
⃗k 2 +M 2 > 0, we deﬁne f (k0) =
{[k0 + (a −i0+)][k0 − (a −i0+)]}−1. In order to determine
∫ ∞
−∞ dk0f (k0) as part of the calculation of I,
we consider f in the complex k0 plane and make use of Cauchy’s theorem
∮
C dzf (z) = 0 for functions
33
a-i0+
-(a-i0+)
3
Re(k   )
Im(k   )
0
0
γ
γ
γ
1
2
4
γ
Figure 5: Path of integration in the complex k0 plane.
which are diﬀerentiable in every point inside the closed con tour C. Choosing the path as shown in
Fig. 5 and taking account of the fact that the quarter circles at inﬁnity do not contribute, we obtain
the so-called Wick rotation
∫ ∞
−∞
dtf (t) = −i
∫ −∞
∞
dtf (it) = i
∫ ∞
−∞
dtf (it). (131)
As an intermediate result, the integral of Eq. (130) reads
I =
∫ d4l
(2π)4
1
l2 +M 2,
where l2 = l2
1 +l2
2 +l2
3 +l2
4 denotes a Euclidian scalar product in four dimensions. Perf orming the
angular integration in four dimensions and introducing a cu toﬀ Λ for the radial integration, the integral
I diverges quadratically for large values of l (ultraviolet divergence):
I(Λ) = 1
8π2
∫ Λ
0
dl l3
l2 +M 2 = Λ 2
(4π)2 + M 2
(4π)2 ln
(
M 2
Λ 2 +M 2
)
= M 2
(4π)2
[ 1
x + ln(x) − ln(1 +x)
]
, (132)
where x =M 2/Λ 2 → 0 as Λ → ∞ . In dimensional regularization, we generalize the integra l from 4 to
n dimensions and introduce polar coordinates
l1 = l cos(θ1), l 2 =l sin(θ1) cos(θ2), l 3 =l sin(θ1) sin(θ2) cos(θ3),
.
.
.
ln−1 = l sin(θ1) sin(θ2) · · ·cos(θn−1), l n =l sin(θ1) sin(θ2) · · ·sin(θn−1),
where 0 ≤l, θi ∈ [0,π ] (i = 1, · · ·,n − 2), and θn−1 ∈ [0, 2π]. A general integral is then symbolically of
the form
∫
dnl · · · =
∫ ∞
0
dll n−1
∫ 2π
0
dθn−1
∫ π
0
dθn−2 sin(θn−2) · · ·
∫ π
0
dθ1 sinn−2(θ1) · · ·.
If the integrand does not depend on the angles, the angular in tegration can explicitly be carried out:
∫
dΩ n = 2 π
n
2
Γ
(
n
2
).
34
We deﬁne the integral for n dimensions (n integer) as
In(M 2,µ 2) = µ4−n
∫ dnk
(2π)n
i
k2 −M 2 +i0+,
where the scale µ (’t Hooft parameter, renormalization scale) has been intro duced so that the integral
has the same dimension for arbitrary n. The integral formally reads
In(M 2,µ 2) = µ4−n2 π
n
2
Γ
(
n
2
) 1
(2π)n
∫ ∞
0
dl ln−1
l2 +M 2
= µ4−n 2 π
n
2
Γ
(
n
2
) 1
(2π)n
1
2 (M 2)
n
2 −1 Γ
(
n
2
)
Γ
(
1 − n
2
)
Γ(1)
= µ4−n
(4π)
n
2
(M 2)
n
2 −1Γ
(
1 − n
2
)
. (133)
Since Γ( z) is an analytic function in the complex plane except for pole s of ﬁrst order in 0 , −1, −2, · · ·,
and az = exp[ln(a)z], a ∈ /CA
+ is an analytic function in /BV , the right-hand side of Eq. (133) can be
thought of as a function of a complex variablen which is analytic in /BV except for poles of ﬁrst order for
n = 2, 4, 6, · · ·. The analytic continuation for complex n reads
I(M 2,µ 2,n ) = M 2
(4π)2
(
4πµ2
M 2
)2− n
2
Γ
(
1 − n
2
)
= M 2
16π2
[
R + ln
(
M 2
µ2
)]
+O(n − 4), (134)
where
R = 2
n − 4 − [ln(4π) + Γ ′(1) + 1]. (135)
The comparison between Eqs. (134) and (132) illustrates the following general observations: in dimen-
sional regularization power-law divergences are analytically continued to zero and logarithmic ultraviolet
divergences of one-loop integrals show up as single poles in ǫ = 4 −n.
