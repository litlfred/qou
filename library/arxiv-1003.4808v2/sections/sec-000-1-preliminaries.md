---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-000-1-preliminaries
section_title: "Preliminaries"
section_number: 1
pages: 2-6
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
doc_brief: "Quantum Field Theory and the Volume Conjecture — 14 sections: Preliminaries; The many dimensions of the volume ; Parametrized VC"
---
2 The many dimensions of the volume conjecture 5
2.1 Parametrized VC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.2 Quantum VC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.3 Groups and representations . . . . . . . . . . . . . . . . . . . . . . . . 10
2.4 Links and 3-manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3 TQFT 13
3.1 Cutting and gluing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.2 Quantization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.2.1 Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.2.2 Simple examples . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.3 Chern-Simons theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.3.1 Quantization of Chern-Simons theory . . . . . . . . . . . . . . . 23
3.3.2 Synthesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
1 Preliminaries
Let K be an oriented knot (or link) in the three-sphere S3. The original volume
conjecture [1, 2] relates the N-colored Jones polynomial of K to the hyperbolic volume
of the knot complement S3\K:
N-colored Jones poly of K ←→ hyperbolic volume of S3\K
(combinatorial, rep. theory) (geometric) . (1.1)
We begin by reviewing some of the deﬁnitions and ingredients that enter on the two
sides here in order to make this statement more precise, and to serve as a precursor
for its subsequent generalization.
Jones polynomials
The (non-colored) Jones polynomial J(K;q) of a knot or link can be deﬁned combina-
torially via the skein relation
qJ (
 )−q−1J(
 ) = (q
1
2−q− 1
2 )J(
 ), (1.2)
1
along with the normalization 1
J(
 ) =q
1
2 +q− 1
2 for
 = unknot, (1.3)
and the rule
J(K1⊔K2) =J(K1)J(K2) (1.4)
for any disjoint union of knots or links. Thus, for example, the (right-handed) trefoil
and ﬁgure-eight knots have Jones polynomials
J(31) =q− 1
2 +q− 3
2 +q− 5
2−q− 9
2,
J(41) =q
5
2 +q− 5
2.
In general, J(K,q ) is a Laurent polynomial, J(K,q )∈ Z[q
1
2,q− 1
2 ].
The combinatorial construction of the Jones polynomial is intimately related to
representation theory of SU (2) — or the closely related representation theories of the
quantum group Uq(su(2)) or the aﬃne Lie algebra ˆsu(2). In particular, the classical
Jones polynomial above is obtained by “coloring” the knot (or link) K in S3 with the
2-dimensional representation of SU (2). More generally, such a knot or link can be
colored with any ﬁnite-dimensional representation R of SU (2), leading to a colored
Jones polynomial JR(K,q ). The N-colored Jones polynomial JN(K,q ) takes R to be
the irreducible N-dimensional representation [3, 4, 5]. The colored Jones polynomial
can again be computed in a purely algebraic/combinatorial manner, by using the two
rules
J⊕iRi(K;q) =
∑
i
JRi(K;q) (1.5a)
and
JR(Kn;q) =JR⊗n(K;q), (1.5b)
together with
JR(K1⊔K2) =JR(K1)JR(K2), (1.6)
and the fact that J1(K;q) =JR=⊘(K;q)≡ 1. The ﬁrst rule says that if R is reducible,
then JR splits as a sum over irreducible components. The second rule says that the
R-colored Jones polynomial for the n-cabling of a knot (formed by taking n copies of
the knot or link, slightly displaced away from one another 2) is equal to the colored
Jones polynomial of the original knot but in representation R⊗n.
For example, from (1.5a-b) and the fact thatJN=2(K,q ) =J(K,q ), it is easy to see
that
JN(
 ) = q
N
2−q−N
2
q
1
2−q− 1
2
. (1.7)
1The most common normalization for the unknot seen in the mathematics literature is J(
 ) = 1.
For the connection with topological quantum ﬁeld theory, however, (1.3) is much more natural.
2This displacement must be done in a way that produces zero linking number between the various
copies.
2
More generally, for any knot K, relations (1.5) can be used to reduce JN(K;q) to
ordinary Jones polynomials of K and its cablings. We have
J1(K;q) = 1,
J2(K;q) =J(K;q),
J3(K;q) =J(K2;q)− 1,
J4(K;q) =J(K3;q)− 2J(K;q),
...,
where the expressions for J3, J4, etc. follow from the rules for decomposing repre-
sentations of SU (2): 2⊗2 = 1⊕ 3 , 2⊗3 = ( 1⊕ 3)⊗ 2 = 2⊕ 2⊕ 4 , etc. Since
J(K;q)∈ Z[q
1
2,q− 1
2 ] for anyK, it is clear that the colored Jones polynomials JN(K;q)
will also be elements of Z[q
1
2,q− 1
2 ] .
We have explained the left side of (1.1), completely, if somewhat tersely, in terms
of algebra and combinatorics. The right side has a very diﬀerent interpretation.
Hyperbolic volumes
It was conjectured by Thurston [6] (and is now proved [7]) that every three-manifold
may be decomposed into pieces that admit exactly one of eight diﬀerent geometric
structures. The most common structure by far is hyperbolic. Indeed, in the case of
knot complements in S3 this statement can be made exact: a knot complement has a
hyperbolic structure if and only if it is not a torus or satellite knot [6]. By deﬁnition,
a “hyperbolic structure” refers to a geodesically-complete metric of constant curvature
−1. If a hyperbolic structure does exist on a manifold M, then it is unique, and the
corresponding hyperbolic volume Vol(M) is a well-deﬁned topological invariant.
In fact, there also exists a natural complexiﬁcation of the hyperbolic volume of a
three-manifold M, obtained as
Vol(M) +iCS(M), (1.8)
where CS(M) is the so-called Chern-Simons invariant of M. To understand this, sup-
pose that M allows a spin structure (as all knot/link complements in S3 do) and
consider ﬂat SL(2, C) connections on M in place of hyperbolic metrics. 3 There exists
a ﬂat connectionA whose real and imaginary parts can be interpreted, respectively, as
the vielbein and spin connection of the hyperbolic metric. The real part of the quantity
i
2ICS(A) = i
2
∫
M
(
A∧ dA + 2
3A∧A∧A
)
(1.9)
3Recall that a “G-connection” on a principalG-bundleE→M can be written locally as a g-valued
one-formA. The bundle E is typically taken to be trivial in the present context, E = G×M. A
gauge transformation (a change of coordinates on E) induced by an element g∈ Γ(E) acts locally on
the connection asA↦→ g−1Ag +g−1dg.
3
then reproduces Vol(M), while the imaginary part deﬁnes CS( M). The expression
ICS(A) is the so-called Chern-Simons functional of A. Further details can be found
e.g. in [8, 9] or [10, 11]. Under gauge transformations acting on A, the functional
ICS(A) is only well-deﬁned up to shifts of 8 π2, leading to an ambiguity of 4 π2 in
the deﬁnition of CS( M). Because of this, it is often convenient to exponentiate the
complexiﬁed volume (1.8), writing it in the unambiguous form
Z(M) =e
i
4πICS (A) =e
1
2π
(
Vol(M)+iCS(M)
)
. (1.10)
For hyperbolic knot complements, the full complexiﬁed volume Z(M) can be eﬃ-
ciently computed in terms of ideal hyperbolic triangulations, cf. [12, 13, 14].
The Volume Conjecture
We have not said much yet about the variable q appearing in the Jones polynomials.
Strictly speaking, this variable should be a root of unity 4
q =e
2πi
k , k ∈ Z+. (1.11)
At the special value k =N, all Jones polynomials JN(K;q) vanish, but the ratio
VN(K,q ) = JN(K;q)
JN(
 ;q) (1.12)
remains ﬁnite. The original volume conjecture [1, 2] then states that
lim
N→∞
2π log
⏐⏐VN(K;q =e
2πi
N )
⏐⏐
N = Vol(M). (1.13)
It is also possible to remove the absolute value and exponentiate to obtain the com-
plexiﬁed generalization (cf. [15])
VN(K;q =e
2πi
N )
N→∞
∼ Z(M)N =e
N
2π
(
Vol(M)+iCS(M)
)
. (1.14)
As an example, consider the ﬁgure-eight knot (Figure 1), the simplest hyperbolic
knot. The colored Jones polynomial (see e.g. [1] or [16]) is
VN(41;q =e
2πi
N ) =
N−1∑
m=0
(q)m(q−1)m, (x)m := (1−x)(1−x2)··· (1−xm). (1.15)
4In terms of representation theory, the integer k is identiﬁed as the level of the aﬃne Lie algebra
ˆsu(2)k. The representation theory of the quantum group Uq(su(2)) also (crucially) simpliﬁes greatly
when q is a root of unity, becoming essentially equivalent to the representation theory of ˆsu(2)k. See
also Sections 3.3.1-3.3.2.
4
Figure 1: The ﬁgure-eight knot, 41
The hyperbolic volume of the ﬁgure-eight knot complement is
Vol(S3\41) = 2 Vol(∆) = 2.02988..., (1.16)
where Vol(∆) = Im Li 2(eiπ
3 ) denotes the volume of a regular hyperbolic ideal tetra-
hedron. The Chern-Simons invariant CS( S3\41) vanishes. It is fairly straightforward
(and an informative exercise5) to show that in the limit N→∞ one has, as expected,
lim
N→∞
2π logVN(41;e
2πi
N )
N = Vol(S3\41). (1.17)
