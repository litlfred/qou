---
doc_id: arxiv-nucl-th-0006014v1
doc_title: "The high-precision, charge-dependent Bonn nucleon-nucleon potential (CD-Bonn)"
section_id: sec-009-a1-scattering-equation
section_title: "Scattering equation"
section_number: A.1
pages: 15-18
source_pdf: 0006014v1.pdf
source_sha256: 208c7a6aaf628b30
toc_source: inferred
doc_brief: "The high-precision, charge-dependent Bonn nucleon-nucleon potential (CD-Bonn) — 56 sections: Front matter; Introduction; The model"
---
Two-nucleon scattering is described covariantly by the Bethe-Salpeter (BS) equation [21]
which reads in operator notation
T = V + VGT
(A1)
with T the invariant amplitude for the two-nucleon scattering process, V the sum of all
connected two-particle irreducible diagrams, and G the relativistic two-nucleon propaga-
tor. Since this four-dimensional integral equation is very diﬃcult to solve, so-called three-
dimensional reductions have been proposed, which are more amenable to numerical solution.
Furthermore, it has been shown by Gross [96] that the full BS equation in ladder approx-
imation (that is, the kernel V is restricted to the exchange of single particles as, e. g., in
the OBE model) does not have the correct one-body limit (i. e., when one of the particles
becomes very massive) while a large family of three-dimensional quasi-potential equations
does. These approximations to the BS equation are also covariant and satisfy relativistic
elastic unitarity. Three-dimensional reductions are typically derived by replacing Eq. (A1)
with two coupled equations [97]:
T = W + WgT
(A2)
and
W = V + V(G −g)W
(A3)
where g is a covariant three-dimensional propagator with the same elastic unitarity cut as
G in the physical region. In general, the second term on the r.h.s. of Eq. (A3) is dropped to
obtain a true simpliﬁcation of the problem.
More explicitly, the BS equation for an arbitrary frame reads [19]
T (q′; q|P) = V(q′; q|P) +
Z
d4k V(q′; k|P) G(k|P) T (k; q|P)
(A4)
with
G(k|P) = i
2π
1
( 1
2̸ P+̸ k −M + iǫ)(1)
1
( 1
2̸ P−̸ k −M + iǫ)(2)
(A5)
= i
2π
"
1
2̸ P+̸ k + M
( 1
2P + k)2 −M2 + iǫ
#(1) "
1
2̸ P−̸ k + M
( 1
2P −k)2 −M2 + iǫ
#(2)
(A6)
where q, k, and q′ are the initial, intermediate, and ﬁnal relative four-momenta, respectively,
and P = (P0, P) is the total four-momentum. For example, in the initial state we have:
q = 1
2(p1 −p2), P = p1 + p2, and p1/2 = 1
2P ± q with p1 and p2 the individual four-momenta
of particle 1 and 2. In the center-of-mass (c.m.) frame, we will have P = (√s, 0) with √s
the total energy. For all four-momenta, our notation is k = (k0, k);̸ k ≡γµkµ. M denotes
the nucleon mass. The superscripts in Eq. (A6) refer to particle (1) and (2). At this stage,
T , V, and G are operators in spinor space, i. e. they are 16 × 16 matrices which, when
sandwiched between Dirac spinors, yield the corresponding matrix elements.
It is common to the derivation of all three-dimensional reductions that the time compo-
nent of the relative momentum is ﬁxed in some covariant way, so that it no longer appears
as an independent variable in the propagator.
Following Blankenbecler and Sugar (BbS) [20], one possible choice for g is (stated in
manifestly covariant form for an arbitrary frame)
gBbS(k, s) = −
Z ∞
4M2
ds′
s′ −s −iǫ δ(+)[ ( 1
2P ′ + k)2 −M2 ]
×δ(+)[ ( 1
2P ′ −k)2 −M2 ]
×[ 1
2̸ P ′+̸ k + M ](1)[ 1
2̸ P ′−̸ k + M ](2)
(A7)
with δ(+) indicating that only the positive energy root of the argument of the δ-function is
to be included; P 2 = s and P ′ ≡
√
s′
√s P. By construction, the propagator gBbS has the same
imaginary part as G and, therefore, preserves the unitarity relation satisﬁed by T . In the
c.m. frame, integration yields
gBbS(k, s) = δ(k0) ¯gBbS(k, s)
(A8)
with
¯gBbS(k, s) = M2
Ek
Λ(1)
+ (k) Λ(2)
+ (−k)
1
4s −E2
k + iǫ
(A9)
where
Λ(i)
+ (k) =
 γ0Ek −γ · k + M
2M
!(i)
(A10)
=
X
λi
|u(k, λi)⟩⟨¯u(k, λi)|
(A11)
represents the positive-energy projection operator for nucleon i (i = 1 or 2) with u(k) a
positive-energy Dirac spinor of momentum k; ¯u ≡u†γ0.
λi denotes the helicity of the
respective nucleon, and Ek ≡
√
M2 + k2 with M the nucleon mass. The projection operators
imply that virtual anti-nucleon contributions are suppressed.
Using the approximation W ≈V [cf. Eq. (A3)], we obtain the explicit form of Eq. (A2)
by simply replacing G by gBbS in Eq. (A4). This yields in the c.m. frame
T (0, q′; 0, q|√s) = V(0, q′; 0, q) +
Z
d3k V(0, q′; 0, k) ¯gBbS(k, s) T (0, k; 0, q|√s).
(A12)
Note that four-momentum is conserved at each vertex, and that in the initial state the
nucleons are on their mass-shell, therefore q = (0, q). The total c.m. energy is
√s = 2Eq = 2
q
M2 + q2.
(A13)
With this we obtain, simplifying our notation,
T (q′, q) = V(q′, q) +
Z
d3k V(q′, k) M2
Ek
Λ(1)
+ (k) Λ(2)
+ (−k)
q2 −k2 + iǫ
T (k, q).
(A14)
Taking matrix elements between positive-energy spinors yields an equation for the invariant
scattering amplitude
¯T(q′, q) = ¯V (q′, q) +
Z
d3k ¯V (q′, k) M2
Ek
1
q2 −k2 + iǫ
¯T(k, q),
(A15)
where helicity and isospin indices are suppressed.
Deﬁning
T(q′, q) =
s
M
Eq′
¯T(q′, q)
s
M
Eq
(A16)
and
V (q′, q) =
s
M
Eq′
¯V (q′, q)
s
M
Eq
,
(A17)
which has become known as “minimal relativity” [98], we can rewrite Eq. (A15) as
T(q′, q) = V (q′, q) +
Z
d3k V (q′, k)
M
q2 −k2 + iǫ T(k, q)
(A18)
which has the form of the familiar Lippmann-Schwinger equation. The quantity T has the
usual (nonrelativistic) relation to phase shifts and NN observables. Thus, the NN potential
V deﬁned in Eq. (A17) and used in the above Lippmann-Schwinger equation can be applied
in the deuteron and in conventional nuclear structure physics in the same way as any other
(nonrelativistic) potential. This is the great virtue of the (relativistic) BbS equation.
