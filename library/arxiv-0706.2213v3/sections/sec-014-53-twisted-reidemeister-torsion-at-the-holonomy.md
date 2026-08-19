---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-014-53-twisted-reidemeister-torsion-at-the-holonomy
section_title: "Twisted Reidemeister torsion at the holonomy representation."
section_number: 5.3
pages: 26-28
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
consider the non–abelian Reidemeister torsion for hyperbolic twist knots at holonomy rep-
resentations. Formulas of the non–abelian Reidemeister to rsion associated to twist knots
are complicated. But we see here that formulas for the non–ab elian Reidemeister torsion
at holonomy representations are simpler.
Every twist knots except the trefoil knot are hyperbolic. Itis well known that an exterior
of a hyperbolic knot admits at most a complete hyperbolic str ucture and this hyperbolic
structure determines the holonomy representation of the knot group (see Section 3.3). With
Fact 9 in mind, we know that such lifts are λ-regular representations.
26
Remark 21. If we substitute s = 1 into Riley’s polynomialφJ(2,2m)(s, u) given in Eq. (34),
then
φJ(2,2m)(1, u) = (1− u)tm− tm−1 = (1− u) ξm
+− ξm
−
ξ+− ξ−
− ξm−1
+ − ξm−1
−
ξ+− ξ−
.
The SL2(C)-representations which lifts the holonomy representation correspond to roots
of Riley’s equationφJ(2,2m)(1, u) = 0. We let ρu denote such representations.
We are now ready to give a formula for the non–abelian Reidemeister torsion of J(2, 2m)
at the holonomy representation in terms of u, which is an algebraic number, deﬁned to be
the root of a computable algebraic equation.
Theorem 19. Let m > 0 and u denote one of the two complex conjugate roots of Riley’s
equation φJ(2,2m)(1, u) = 0 (resp. φJ(2,−2m)(1, u) = 0) corresponding to holonomy represen-
tations, then
(1) the non–abelian Reidemeister torsion TJ(2,2m)
λ (ρu) satisﬁes the following formula:
TJ(2,2m)
λ (ρu) = −τ0
u2 + 4
[(
4 + m(u2− 4u + 8)
)
tm(ξm
+ + ξm
− )
+
(
tm(ξm−1
+ + ξm−1
− )− 1
)
(u2− 4)m
+(−5u2− 8u + 4)t2
m
]
,
(2) similarly the Reidemeister torsion TJ(2,−2m)
λ (ρu) satisﬁes the following formula:
TJ(2,−2m)
λ (ρu) = −τ0
u2 + 4
[(
−4 + m(u2− 4u + 8)
)
tm(ξm
+ + ξm
− )
+
(
tm(ξm+1
+ + ξm+1
− ) + 1
)
(u2− 4)m
+(−5u2− 8u + 4)t2
m
]
.
Remark 22. Combining results of Theorem 19 with Eq. (12), the non–abelian Reidemeister
torsion of a (hyperbolic) twist knot at the holonomy is expressed in terms of the cusp shape
of the knot.
Proof. First we make the computations in the case of J(2, 2m), where m > 0. If we substi-
tute s = 1 in Eq. (42), then we obtain:
TJ(2,2m)
λ (ρ) =−τ0 lim
t→1
det(1 + Zm)
(t− 1)4
=−τ0
24
d4
dt4 det(1 + Zm)
⏐
⏐
⏐
⏐
⏐
⏐t=1
.
Next, using the splitting of det(1 + Zm) given in Eq. (43), we get:
(52) TJ(2,2m)
λ (ρ) =−τ0
24
d4
dt4 [1 + σ1(Zm) + σ2(Zm) + σ3(Zm)]
⏐
⏐
⏐
⏐
⏐
⏐t=1
.
It follows from Eq. (45) that ( t− 1)6 divides σ3(Zm) in the case of s = 1. Hence the term
d4
dt4 σ3(Zm)
⏐
⏐
⏐
⏐t=1
in Eq. (52) vanishes. By degrees of t in σ1(Zm) and σ2(Zm), we obtain the
following equation from direct computations of the above diﬀerentials:
TJ(2,2m)
λ (ρ) =−τ0[tr (X−1S m(W−1)) + 5σ2(X−1S m(W−1))(53)
− tr (X−1S m(W−1))tr ((1 + X−1Y)S m(W−1))
+ tr (X−1S m(W−1)(1 + X−1Y)S m(W−1))].
27
Note that ξ+ + ξ− = u2 + 2 and (ξ+− ξ−)2 = u2(u2 + 4). By Claims 16, 17 & 18 we have
tr (X−1S m(W−1)) = 1
u2 + 4
[
4(ξm
+ + ξm
− )tm− (u2− 4)m
]
σ2(X−1S m(W−1)) = 1
u2 + 4
[
4m(ξm
+ + ξm
− )tm− (u2− 4)t2
m
]
and
−tr (X−1S m(W−1))tr ((1 + X−1Y)S m(W−1)) + tr (X−1S m(W−1)(1 + X−1Y)S m(W−1))
=− 1
u2 + 4
[
8(u + 2)t2
m− m(u + 2)(u− 6)(ξm
+ + ξm
− )tm− m(u2− 4)(ξm−1
+ + ξm−1
− )tm
]
.
If we substitute these results into Eq. (53), then we obtain the wanted formula for J(2, 2m).
Similarly, in the case of twist knotsJ(2,−2m), m > 0, from computations of diﬀerentials
we have
TJ(2,−2m)
λ (ρu) =−τ0[−tr (X−1S m(W)W) + 5σ2(X−1S m(W)W)(54)
− tr (X−1S m(W)W)tr ((1 + X−1Y)S m(W)W)
+ tr (X−1S m(W)W(1 + X−1Y)S m(W)W)].
It follows from Claims 16, 17 & 18 that
tr (X−1S m(W)W) = 1
u2 + 4
[
4(ξm
+ + ξm
− )tm− (u2− 4)m
]
σ2(X−1S m(W)W) = 1
u2 + 4
[
4m(ξm
+ + ξm
− )tm− (u2− 4)t2
m
]
and
−tr (X−1S m(W)W)tr ((1 + X−1Y)S m(W)W) + tr (X−1S m(W)W(1 + X−1YS m(W)W))
=− 1
u2 + 4
[
8(u + 2)t2
m− m(u + 2)(u− 6)(ξm
+ + ξm
− )tm− m(u2− 4)(ξm+1
+ + ξm+1
− )tm
]
.
If we substitute these results into Eq. (54) , then we obtain t he wanted formula for
J(2,−2m). □
