---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-035-infrared-regularization
section_title: "Infrared regularization"
section_number: null
pages: 60-62
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
Let us now turn to a formal deﬁnition of the infrared singular and regular parts for arb itrary p2
[Becher and Leutwyler, 1999] which makes use of the Feynman p arametrization of Eq. (216). Introduc-
ing the dimensionless variables
α = M
m = O(q), Ω = p2 −m2 −M 2
2mM = O(q0), (218)
we rewrite A(z) as
A(z) = m2[z2 − 2αΩ z(1 −z) +α2(1 −z)2] ≡m2C(z),
so that H is now given by
H(p2,m 2,M 2;n) = κ(m;n)
∫ 1
0
dz[C(z) −i0+]
n
2 −2, (219)
where
κ(m;n) =
Γ
(
2 − n
2
)
(4π)
n
2
mn−4. (220)
The infrared singularity originates from small values of z, where the function C(z) goes to zero as
M → 0. In order to isolate the divergent part one scales the integ ration variable z ≡ αx so that the
upper limit z = 1 in Eq. (219) corresponds to x = 1/α → ∞ asM → 0. An integral I having the same
infrared singularity as H is then deﬁned which is identical to H except that the upper limit is replaced
by ∞:
I ≡κ(m;n)
∫ ∞
0
dz[C(z) −i0+]
n
2 −2 =κ(m;n)αn−3
∫ ∞
0
dx[D(x) −i0+]
n
2 −2, (221)
where
D(x) = 1 − 2Ω x +x2 + 2αx(Ω x − 1) +α2x2.
(The pion mass M is not sent to zero.) Accordingly, the regular part of H is deﬁned as
R ≡ −κ(m;n)
∫ ∞
1
dz[C(z) −i0+]
n
2 −2, (222)
so that
H =I +R. (223)
Let us verify that the deﬁnitions of Eqs. (221) and (222) inde ed reproduce the behavior of Eq. (217).
To that end we make use of Ω thr = 1, yielding
Ithr =κ(m;n)αn−3
∫ ∞
0
dx
{
[(1 +α)x − 1]2 −i0+
} n
2 −2
, (224)
which converges forn< 3. In order to continue the integral to n> 3, write [Becher and Leutwyler, 1999]
{
[(1 +α)x − 1]2 −i0+
} n
2 −2
= (1 +α)x − 1
(1 +α)(n − 4)
d
dx
{
[(1 +α)x − 1]2 −i0+
} n
2 −2
,
and make use of a partial integration
∫ ∞
0
dx
{
[(1 +α)x − 1]2 −i0+
} n
2 −2
=
[
(1 +α)x − 1
(1 +α)(n − 4)
{
[(1 +α)x − 1]2 −i0+
} n
2 −2
] ∞
0
− 1
n − 4
∫ ∞
0
dx
{
[(1 +α)x − 1]2 −i0+
} n
2 −2
.
60
Forn< 3, the ﬁrst expression vanishes at the upper limit and, at the lower limit, yields 1/[(1+α)(n−4)].
Bringing the second expression to the left-hand side, we may then continue the integral analytically as
∫ ∞
0
dx
{
[(1 +α)x − 1]2 −i0+
} n
2 −2
= 1
(n − 3)(1 +α), (225)
so that we obtain for Ithr
Ithr =κ(m;n)αn−3 1
(n − 3)(1 +α) =
Γ
(
2 − n
2
)
(4π)
n
2 (n − 3)
M n−3
m +M, (226)
which agrees with the infrared singular part I of Eq. (217).
The threshold value of the regular part of Eq. (222) is obtain ed by analytic continuation from n< 3
to n> 3:
Rthr = −
Γ
(
2 − n
2
)
(4π)
n
2
∫ ∞
1
dz[z(m +M) −Mπ]n−4
= −
Γ
(
2 − n
2
)
(4π)
n
2
1
(n − 3)(m +M) (∞n−3 −mn−3)
n< 3=
Γ
(
2 − n
2
)
(4π)
n
2 (n − 3)
mn−3
m +M, (227)
which is indeed the regular part R of Eq. (217).
What distinguishes I from R is that, for non-integer values of n, the chiral expansion of I gives
rise to non-integer powers of O(q), whereas the regular part R may be expanded in an ordinary Taylor
series. For the threshold integral, this can nicely be seen b y expanding Ithr and Rthr in the pion mass
counting as O(q). On the other hand, it is the regular part which does not sati sfy the counting rules.
The basic idea of the infrared renormalization consists of r eplacing the general integral H of Eq. (216)
by its infrared singular part I, deﬁned in Eq. (221), and dropping the regular part R, deﬁned in Eq.
(222). In the low-energy region H andI have the same analytic properties whereas the contribution of
R, which is of the type of an inﬁnite series in the momenta, can b e included by adjusting the coeﬃcients
of the most general eﬀective Lagrangian. This is the infrare d renormalization condition.
As discussed in detail in Ref. [Becher and Leutwyler, 1999], the method can be generalized to an
arbitrary one-loop graph (see also Ref. [Semke and Lutz, 200 6]). It is ﬁrst argued that tensor integrals
involving an expression of the type kµ1 · · ·kµ2 in the numerator may always be reduced to scalar loop
integrals of the form
−i
∫ dnk
(2π)n
1
a1 · · ·am
1
b1 · · ·bn
,
whereai = (qi +k)2 −M 2 +i0+ andbi = (pi −k)2 −m2 +i0+ are inverse meson and nucleon propagators,
respectively. Here, the qi refer to four-momenta of O(q) and the pi are four-momenta which are not
far oﬀ the nucleon mass shell, i.e., p2
i = m2 + O(q). Using the Feynman parametrization, all pion
propagators and all nucleon propagators are separately com bined, and the result is written in such a
way that it is obtained by applying ( m − 1) and (n − 1) partial derivatives with respect to M 2 andm2,
respectively, to a master formula. A simple illustration is given by
1
a1a2
=
∫ 1
0
dz 1
[a1z +a2(1 −z)]2 = ∂
∂M 2
∫ 1
0
dz 1
a1z +a2(1 −z),
whereai = (qi +k)2 −M 2 +i0+. Of course, the expressions become more complicated for lar ger numbers
of propagators. The relevant property of the above procedur e is that the result of combining the meson
61
propagators is of the type 1 /A withA = (k +q)2 −M 2 +i0+, where q is a linear combination of the m
momentaqi, with an analogous expression 1 /B for the nucleon propagators. Finally, the expression
−i
∫ dnk
(2π)n
1
AB
may then be treated in complete analogy to H of Eq. (214), i.e., the denominators are combined
as in Eq. (215), and the infrared singular and regular pieces are identiﬁed by writing
∫ 1
0 dz · · · =∫ ∞
0 dz · · · −
∫ ∞
1 dz · · ·.
