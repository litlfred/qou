---
doc_id: arxiv-2007.10190v2
doc_title: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS"
section_id: sec-011-52-the-41-knot
section_title: "The 41 knot"
section_number: 5.2
pages: 13-16
source_pdf: 2007.10190v2.pdf
source_sha256: 37bcbd3a343bb21a
toc_source: outline
doc_brief: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS — The asymptotic expansion of quantum knot invariants in complex Chern-Simons theory gives rise to factorially divergent formal power series."
---
series ϕ1,2(τ) of the 41 knot is shown in Fig. 1. Points in each vertical line are 2πi apart, and
the two points in the real axis correspond to
ι± = ±
V (σ1)
2π
−V (σ2)
2π

= ±V
π ,
(69)
where V is deﬁned in (9). Since each singularity in the Borel plane leads to a discontinuity
in the Borel resummation, one has the structure of Stokes rays shown in Fig. 2 (where we
took into account both series). Note that there is an inﬁnite dense set of rays accumulating
towards the imaginary axis.
We already hinted at the end of Section 4.2 that the asymptotic expansion (38) can be
upgraded to an exact expression. To do this, one has to upgrade the optimal truncation of
Φ(τ) to its Borel resummation. Simultaneously we have to promote the matrix of constants
appearing in (38), to a matrix whose entries are power series in ˜q with integer coeﬃcients:
 1
√τ g0
0(τ)
√τg1
0(τ)

= MR(˜q) sR(Φ)(τ).
(70)
The index R labels a sector in the τ-plane, since due to presence of Stokes rays, both the
matrix MR(˜q) and the Borel resummed vector Φ depend on the sector of the τ-plane. In
view of the structure of the Stokes rays, convenient sectors to perform the analysis are the
angular wedges (i.e., pointed open cones in the complex plane) denoted by I, II, III and
IV in Fig. 2.
14
STAVROS GAROUFALIDIS, JIE GU, AND MARCOS MARI˜NO
It is a challenge to numerically compute the matrix MR(˜q) given only a few hundred
terms of Φ(τ), since the volume of 41 (about 2.02 . . . ) is so much smaller than the instanton
corrections (appearing at 4π2 = 39.47 . . . ). This can be done however, and with 300 terms
of Φ(τ) it is possible to compute the ﬁrst twelve terms in the series appearing in MR(˜q). One
ﬁnds for example, in region I,
MI(q) =

1 −q −2q2 −2q3 −2q4
−1 + 2q + 3q2 + 2q3 + q4
1 −7q −14q2 −8q3 −2q4
1 + 10q + 15q2 −2q3 −19q4

+ O(q5).
(71)
Our Conjecture 1 suggests that these q-series can be expressed in terms of solutions to the
linear q-diﬀerence equation (11). Indeed, one has, at this order,
MI(q) =

G0
0(q)
−G0
0(q) −G0
−1(q)
G1
0(q)
−G1
0(q) −G1
−1(q)

= W−1(q)T

0
−1
1
−1

.
(72)
We conjecture that this is in fact the exact expression for this matrix.
I
II
III
IV
Figure 2. Stokes rays in the τ-plane for Φ(τ).
An important consequence of the relation (70) is that, by inverting it, one can express the
Borel resummations of Φσj for j = 1, 2 in a given sector, in terms of the descendants of the
state integral introduced in (4.3), which are holomorphic functions of τ on C′. Indeed, let
us consider the “reduced” descendant
eI1,2,λ,µ(b) = τ 1/2
2 G1
λ(q)G0
µ(˜q) −τ −1/2
2
G0
λ(q)G1
µ(˜q).
(73)
THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS
15
This diﬀers from the descendant (53) in a manifestly holomorphic factor, so it is holomorphic
on C′. Then, one ﬁnds, in region I,
sI(Φσ1)(τ) = eI1,2,0,0(τ) + eI1,2,0,−1,(τ),
sI(Φσ2)(τ) = eI1,2,0,0(τ).
(74)
This procedure can be done in the other sectors appearing in Fig. 2: one calculates MR(q),
express it in terms of fundamental solutions, and represent the Borel resummation sR(Φ) in
terms of holomorphic functions on C′. By comparing the diﬀerent expressions for the Borel
resummations in diﬀerent sectors, one deduces the Stokes automorphisms relating them, and
from a composition of the Stokes automorphisms one deduces the promised S matrices.
The results for MR(q) are the following:
MII(q) =

G0
0(q) + G0
−1(q)
−G0
0(q)
−G1
0(q) −G1
−1(q)
G1
0(q)

=

1
0
0
−1

W−1(q)T

1
0
1
−1

,
MIII(q) =

G0
0(q−1) + G0
−1(q−1)
G0
0(q−1)
G1
0(q−1) + G1
−1(q−1)
G1
0(q−1)

= W−1(q−1)T

1
0
1
1

,
MIV (q) =

G0
0(q−1)
G0
0(q−1) + G0
−1(q−1)
−G1
0(q−1)
−G1
0(q−1) −G1
−1(q−1)

=

1
0
0
−1

W−1(q−1)T

0
1
1
1

.
(75)
From these values one deduces the Stokes automorphisms
sII(Φ) = SI→II(˜q)sI(Φ),
sIV (Φ) = SIII→IV (˜q−1)sIII(Φ)
sI(Φ) = SIV 7→IsIV (Φ),
sIII(Φ) = SII7→IIIsIII(Φ),
(76)
where
SI→II(q) = MII(q)−1MI(q)
SIII→IV (q) = MIV (q−1)−1MIII(q−1)
(77a)
SIV →I = MI(q)−1MIV (q)
SII→III = MIII(q)−1MII(q) .
(77b)
and
S+(q) = SI→II(q)SIV →I,
S−(q) = SIII→IV (q)SII→III .
(78)
Substituting the conjectured values for MR and using symmetry and the orthogonality re-
lations (15) and (16) one obtains (18a), (18b).
In the q 7→0 limit the Stokes matrices
read
S+(0) =

1
3
0
1

,
S−(0) =

1
0
−3
1

.
(79)
The oﬀ–diagonal entries ±3 are Stokes constants associated to the singularities ι± on the
positive and negative real axis respectively. They agree with the matrix of integers obtained
in [GH18],[GZc]. Note that the Stokes matrices S±(q) can also be factorized according to
(67) in order to extract all the other Stokes constants. This will be studied in [GGMn20a].
Let us ﬁnally note that
S+
σ1σ1(q) = G0
0(q)G1
0(q) = 1 −8q −9q2 + 18q3 + 46q4 + O(q5) = Indrot
41 (q),
(80)
in agreement with Conjecture 2 (the fact that G0
0(q)G1
0(q) equals the rotated index was
pointed out in [GZb]).
16
STAVROS GAROUFALIDIS, JIE GU, AND MARCOS MARI˜NO
