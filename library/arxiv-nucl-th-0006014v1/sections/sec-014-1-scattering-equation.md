---
doc_id: arxiv-nucl-th-0006014v1
doc_title: "The high-precision, charge-dependent Bonn nucleon-nucleon potential (CD-Bonn)"
section_id: sec-014-1-scattering-equation
section_title: "Scattering equation"
section_number: 1
pages: 15-18
source_pdf: 0006014v1.pdf
source_sha256: 208c7a6aaf628b30
doc_brief: "The high-precision, charge-dependent Bonn nucleon-nucleon potential (CD-Bonn) — 35 sections: Scattering equation . . . . . . . ; R-matrix and partial wave decompos; Phase shifts . . . . . . . . . . ."
---
Two-nucleon scattering is described covariantly by the Bet he-Salpeter (BS) equation [21]
which reads in operator notation
T = V + VGT (A1)
with T the invariant amplitude for the two-nucleon scattering pro cess, V the sum of all
connected two-particle irreducible diagrams, and G the relativistic two-nucleon propaga-
tor. Since this four-dimensional integral equation is very diﬃcult to solve, so-called three-
dimensional reductions have been proposed, which are more a menable to numerical solution.
15
Furthermore, it has been shown by Gross [96] that the full BS e quation in ladder approx-
imation (that is, the kernel V is restricted to the exchange of single particles as, e. g., i n
the OBE model) does not have the correct one-body limit (i. e. , when one of the particles
becomes very massive) while a large family of three-dimensi onal quasi-potential equations
does. These approximations to the BS equation are also covar iant and satisfy relativistic
elastic unitarity. Three-dimensional reductions are typi cally derived by replacing Eq. (A1)
with two coupled equations [97]:
T = W + WgT (A2)
and
W = V + V(G −g)W (A3)
where g is a covariant three-dimensional propagator with the same e lastic unitarity cut as
G in the physical region. In general, the second term on the r.h .s. of Eq. (A3) is dropped to
obtain a true simpliﬁcation of the problem.
More explicitly, the BS equation for an arbitrary frame read s [19]
T (q′;q|P ) = V(q′;q|P ) +
∫
d4k V(q′;k|P ) G(k|P ) T (k;q|P ) (A4)
with
G(k|P ) = i
2π
1
( 1
2 ⁄P + ⁄k −M +iǫ)(1)
1
( 1
2 ⁄P − ⁄k −M +iǫ)(2) (A5)
= i
2π
[ 1
2 ⁄P + ⁄k +M
( 1
2P +k)2 −M 2 +iǫ
] (1)[ 1
2 ⁄P − ⁄k +M
( 1
2P −k)2 −M 2 +iǫ
] (2)
(A6)
whereq,k, and q′ are the initial, intermediate, and ﬁnal relative four-mome nta, respectively,
and P = (P0, P) is the total four-momentum. For example, in the initial sta te we have:
q = 1
2(p1 −p2),P =p1 +p2, and p1/ 2 = 1
2P ±q withp1 andp2 the individual four-momenta
of particle 1 and 2. In the center-of-mass (c.m.) frame, we wi ll have P = ( √s, 0) with √s
the total energy. For all four-momenta, our notation is k = (k0, k); ⁄k ≡ γµkµ . M denotes
the nucleon mass. The superscripts in Eq. (A6) refer to parti cle (1) and (2). At this stage,
T, V, and G are operators in spinor space, i. e. they are 16 × 16 matrices which, when
sandwiched between Dirac spinors, yield the corresponding matrix elements.
It is common to the derivation of all three-dimensional redu ctions that the time compo-
nent of the relative momentum is ﬁxed in some covariant way, s o that it no longer appears
as an independent variable in the propagator.
Following Blankenbecler and Sugar (BbS) [20], one possible choice for g is (stated in
manifestly covariant form for an arbitrary frame)
gBbS (k,s ) = −
∫ ∞
4M 2
ds′
s′ −s −iǫδ(+)[ ( 1
2P ′ +k)2 −M 2 ]
×δ(+)[ ( 1
2P ′ −k)2 −M 2 ]
×[ 1
2 ⁄P ′+ ⁄k +M ](1)[ 1
2 ⁄P ′− ⁄k +M ](2) (A7)
16
with δ(+) indicating that only the positive energy root of the argumen t of the δ-function is
to be included; P 2 =s and P ′ ≡
√
s′
√sP . By construction, the propagator gBbS has the same
imaginary part as G and, therefore, preserves the unitarity relation satisﬁed by T . In the
c.m. frame, integration yields
gBbS (k,s ) = δ(k0) ¯gBbS (k,s ) (A8)
with
¯gBbS (k,s ) = M 2
Ek
Λ (1)
+ (k) Λ (2)
+ (−k)
1
4s −E2
k +iǫ (A9)
where
Λ (i)
+ (k) =
(
γ0Ek − γ · k +M
2M
) (i)
(A10)
=
∑
λ i
|u(k,λ i)⟩⟨¯u(k,λ i)| (A11)
represents the positive-energy projection operator for nu cleon i (i = 1 or 2) with u(k) a
positive-energy Dirac spinor of momentum k; ¯u ≡ u†γ0. λi denotes the helicity of the
respective nucleon, andEk ≡
√
M 2 + k2 withM the nucleon mass. The projection operators
imply that virtual anti-nucleon contributions are suppres sed.
Using the approximation W ≈ V [cf. Eq. (A3)], we obtain the explicit form of Eq. (A2)
by simply replacing G bygBbS in Eq. (A4). This yields in the c.m. frame
T (0, q′; 0, q|√s) = V(0, q′; 0, q) +
∫
d3k V(0, q′; 0, k) ¯gBbS (k,s ) T (0, k; 0, q|√s). (A12)
Note that four-momentum is conserved at each vertex, and tha t in the initial state the
nucleons are on their mass-shell, therefore q = (0, q). The total c.m. energy is
√s = 2Eq = 2
√
M 2 + q2. (A13)
With this we obtain, simplifying our notation,
T (q′, q) = V(q′, q) +
∫
d3k V(q′, k) M 2
Ek
Λ (1)
+ (k) Λ (2)
+ (−k)
q2 − k2 +iǫ T (k, q). (A14)
Taking matrix elements between positive-energy spinors yi elds an equation for the invariant
scattering amplitude
¯T (q′, q) = ¯V (q′, q) +
∫
d3k ¯V (q′, k) M 2
Ek
1
q2 − k2 +iǫ
¯T (k, q), (A15)
where helicity and isospin indices are suppressed.
Deﬁning
T (q′, q) =
√
M
Eq′
¯T (q′, q)
√
M
Eq
(A16)
17
and
V (q′, q) =
√
M
Eq′
¯V (q′, q)
√
M
Eq
, (A17)
which has become known as “minimal relativity” [98], we can r ewrite Eq. (A15) as
T (q′, q) = V (q′, q) +
∫
d3kV (q′, k) M
q2 − k2 +iǫT (k, q) (A18)
which has the form of the familiar Lippmann-Schwinger equat ion. The quantity T has the
usual (nonrelativistic) relation to phase shifts and NN observables. Thus, the NN potential
V deﬁned in Eq. (A17) and used in the above Lippmann-Schwinger equation can be applied
in the deuteron and in conventional nuclear structure physi cs in the same way as any other
(nonrelativistic) potential. This is the great virtue of th e (relativistic) BbS equation.
