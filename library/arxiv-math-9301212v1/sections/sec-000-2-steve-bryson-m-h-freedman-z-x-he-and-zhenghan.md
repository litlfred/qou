---
doc_id: arxiv-math-9301212v1
doc_title: "APPEARED IN BULLETIN OF THE"
section_id: sec-000-2-steve-bryson-m-h-freedman-z-x-he-and-zhenghan
section_title: "STEVE BRYSON, M. H. FREEDMAN, Z.-X. HE, AND ZHENGHAN W ANG"
section_number: 2
pages: 2-4
source_pdf: 9301212v1.pdf
source_sha256: 029787800ddf73e5
doc_brief: "APPEARED IN BULLETIN OF THE — A physically natural potential energy for simple closed cur ves in R3 is shown to be invariant under M¨ obius transformations."
---
Theorem B. If K is a smooth prime (not a connected sum ) knot, then there exists
a simple closed rectiﬁable γK of knot type K with E(γK) ≤ E(γ) for all rectiﬁable
loops γ which are topologically ambient isotopic to K.
Theorem C. Any minimizer γK, as above, will enjoy some regularity. With an
arc length parametrization, γK will be in C1, 1.
Several results of [FH] can be improved quantitatively.
Theorem D. If γ is topologically tame, let c([γ]) denote the (topological) crossing
number of the knot type. We have
2πc ([γ]) + 4 ≤ E(γ).
(It was proved in [FH] that ﬁnite energy implies tame. )
Since an essential knot must have three or more crossings, we obt ain the following
Corollary. Any rectiﬁable loop with energy less than 6π + 4 ≈ 22. 84954 is unknot-
ted.
Computer experiments of [A] as reported in [O3] and independently b y the ﬁrst
author yield an essential knot (a trefoil) with energy ≈ 74.
It may be estimated [S,T,W] that the number K(n) of distinct knots of at most
n crossings satisﬁes
2n ≤ K(n) ≤ 2 · 24n.
Hence the number of knot types with representatives below a given energy threshold
can also be bounded by an exponential.
Theorem E. The number Ke(M ) of isomorphism classes of knots which have rep-
resentatives of energy less than or equal to M is bounded by 2(24−4/ 2π )(241/ 2π )M ≈
(0. 264)(1. 658)M. In particular, only ﬁnitely many knot types occur below any ﬁnite
energy threshold.
Note that there are competing candidates for the exponent = −2 in the deﬁnition
of E; for example, the Newtonian potential in R3 has exponent = −1. When the
exponent is strictly larger than −3, ﬁnite values are obtained for smooth simple
loops. Exponents smaller or equal to −2 yield energies which blow up as a simple
loop γ begins to acquire a double point, thus creating an inﬁnite energy bar rier to
a change of topology. Such a barrier would not exist for the Newton ian potential.
We refer to [O1–O3] for detailed discussions. Similarity and M¨ obius inv ariance are,
of course, special to the exponent −2.
Proof of Theorem A. Let T be a M¨ obius transformation sending a point of γ to
inﬁnity. The energy E(T (γ)) ≥ 0 with equality holding iﬀ T (γ) is a straight line.
Apply the M¨ obius invariant property to complete the proof. □
Proof of Theorem B. In [FH] it is shown that for prime knot types K minimizers
exist in the class of properly embedded rectiﬁable lines whose complet ion in R3 ∪∞
represent K. According to the M¨ obius Invariance Property, such lines may be
moved to a closed minimizer by any M¨ obius transformation T which moves the
completed line oﬀ inﬁnity. □
Sketch of Proof of Theorem C. Let γK be a closed minimizer in knot type K. An
inversion argument shows that, for suﬃciently small ε > 0, if γK meets a closed ball
M ¨OBIUS INV ARIANCE OF KNOT ENERGY 3
of radius ε, Bε, only in its boundary Sε, then γK ∩Sε consists of (at most) one point.
The idea is that if γK ∩ Sε is disconnected, inverting an arc of γK\Sε into Bε will
lower energy while preserving the knot type. Thus there is a continu ous projection
from the ε-neighborhood of γK to γK given by “closest point” π : Nε(γK) → γK.
We prove that the ﬁbers π −1(pt) are all geometric planar disks of radius ε. The
disjointness of these “normal” ﬁbers to distance ε is equivalent to the existence of
a continuously turning tangent to γk whose generalized derivative is in L∞. □
A detailed proof of Theorem C will appear elsewhere.
Proof of Theorem D. Theorem 2.5 of [FH] gives the inequality
c([γ]) ≤ c(γ) ≤ E(γ)/ 2π
for proper rectiﬁable lines. According to the M¨ obius Invariance Property, the energy
will increase by exactly 4 if a M¨ obius transformation is used to move t he line oﬀ
inﬁnity and into closed position. □
Proof of M¨ obius Invariance Property.It is suﬃcient to consider how I, an inversion
in a sphere, transforms energy. Let u be the arc length parameter of a rectiﬁable
closed curve γ, u ∈ R/l Z. Let
(1) Eε(γ) =
∫ ∫
|u−v|≥ε
( 1
|γ(u) − γ(v)|2 − 1
(D(γ(u), γ (v)))2
)
du dv
and
(2)
Eε(I ◦ γ) =
∫ ∫
|u−v|≥ε
( 1
|I ◦ γ(u) − I ◦ γ(v)|2 − 1
(D(I ◦ γ(u), I ◦ γ(v)))2
)
× ‖I ′(γ(u))‖ · ‖I ′(γ(v))‖ du dv.
Clearly E(γ) = lim ε→0 Eε(γ) and E(I ◦ γ) = lim ε→0 Eε(I ◦ γ).
It is a short calculation (using the law of cosines) that the ﬁrst term s transform
correctly, i.e.,
‖I ′(γ(u))‖ · ‖I ′(γ(v))‖
|I(γ(u)) − I(γ(v))|2 = 1
|γ(u) − γ(v)|2 .
Since u is arclength for γ, the regularization term of (1) is the elementary integral
(3)
∫ l
u=0
[
2
∫ l/ 2
v=ε
1
v2 dv
]
du = 4 − 2l
ε .
Let s be an arclength parameter for I ◦ γ. Then ds(u)/du = ‖I ′(γ(u))‖ where
‖I ′(γ(u))‖ = f (u) denotes the linear expansion factor of I ′. Since γ(u) is a lipschitz
function and I ′ is smooth, f (u) is lipschitz, hence, it has a generalized derivative
f ′(u) ∈ L∞.
(4)
regularization (2) =
∫
u∈R/l Z
[∫
|v−u|≥ε
|(I ◦ γ)′(v)| dv
D(I ◦ γ(u), I ◦ γ(v))2
]
|(I ◦ γ)′(u)| du
=
∫
R/l Z
[ 4
L − 1
ε+
− 1
ε−
]
ds,
