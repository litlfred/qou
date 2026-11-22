---
doc_id: bn
doc_title: "Braid groups and Hodge theory"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-9
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
toc_source: inferred
doc_brief: "Braid groups and Hodge theory — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cover- ings of P1, highlighting their"
---
Introduction
Every conﬁguration of distinct points (b1, . . . , bn) in C determines a compact
Riemann surface X by the equation
yd = (x −b1)(x −b2) · · · (x −bn).
(1.1)
This paper gives an account of the unitary representations of the braid group,
and the geometric structures on moduli space, that arise via this branched-
covering construction.
It also develops new connections with arithmetic
groups, Teichm¨uller curves and ergodic theory, and highlights open problems
in surface topology and complex reﬂection groups.
The general approach presented here pivots on the classiﬁcation of cer-
tain arithmetic subgroups of U(r, s) which envelop the image of the braid
group (§7). The case U(0, s) yields metrics of positive curvature on moduli
space, ﬁnite representations of the braid group, algebraic deﬁnite integrals
and rigid factors of the Jacobian of X. The case U(1, s) leads to the complex
hyperbolic metrics on moduli space considered by Picard, Deligne–Mostow
and Thurston.
Other unitary groups U(r, s) provide moduli space with
natural indeﬁnite metrics. In particular, the hyperelliptic case (§12) yields
an action of the braid group which, together with results of Ratner and
Kapovich, illuminates the topology and ergodic theory of the period map
and its connection with the foliation of M∗
0,n by Teichm¨uller geodesics.
This section presents a overview of the discussion.
Action of the braid group. We begin with topological considerations.
Let ζd = e2πi/d.
The braid group Bn is the fundamental group of the space C⟨n⟩of ﬁnite
sets B ⊂C with |B| = n.
Each point conﬁguration B determines, via
equation (1.1), a compact Riemann surface X, whose cohomology group
H1(X) forms the ﬁber of a ﬂat, complex vector bundle over C⟨n⟩.
The
natural monodromy representation
ρ : Bn ∼= π1(C⟨n⟩, B) →Aut(H1(X))
preserves the interesection form (√−1/2)
R
α ∧β, and commutes with the
action of the deck group Z/d of X/bC; thus it also preserves the eigenspace
decomposition
H1(X) =
M
qd=1
H1(X)q = Ker(T ∗−qI),
where T(x, y) = (x, ζdy).
1
As we will see in §3, the signature (r, s) of the Hermitian vector space
H1(X)q can be determined by drawing a line through 1 and q in C; then
r is the number of nth roots of unity strictly below the line, and s is the
number strictly above. The signature changes from deﬁnite to hyperbolic to
higher rank, and then back again, as q moves around the circle (Figure 1).
s
(0,0)
(3,1)
(2,2)
(1,3)
(0,4)
(4,0)
1
q
(3,2)
r
Figure 1. The signature of H1(X)q for n = 6.
Restricting attention to a single eigenspace, we obtain an irreducible
unitary representation
ρq : Bn →U(H1(X)q) ∼= U(r, s).
In fact, Bn acts by a complex reﬂection group of type An−1(q) (see §5); there
is a spanning set (ei)n−1
1
for H1(X)q adapted to the standard generators τi
of the braid group, such that
⟨ei, ej⟩=
√
−1






q −q
1 −q
0
. . .
0
q −1
q −q
1 −q
. . .
0
. . .
0
. . .
0
q −1
q −q






,
and
eτ ∗
i (x) = x −(q + 1) ⟨x, ei⟩
⟨ei, ei⟩ei
(for q̸ = ±1). In particular, the generating twists τi of Bn act with ﬁnite
order on H1(X)q.
Although purely topological, these results are conveniently established
using particular algebraic models such as yd = xn −1 for X. We also use
consistency of ρq under restriction to Bi ×Bn−i; geometrically, this amounts
to letting X degenerate to a stable curve where a given Dehn twist becomes a
holomorphic automorphism. (For a more algebraic approach to homological
representations of Bn, see e.g. [KT].)
2
The period map. Now ﬁx q = ζ−k
d
with 1/n < k/d < 1, let T ∗
0,n denote
the Teichm¨uller space of n points in the plane, and let Hr,s denote the space
of positive lines in PH1(X)q ∼= PCr,s. The period map
fq : T ∗
0,n →Hr,s
sends a point (C, B) in Teichm¨uller space to the positive line spanned by
the holomorphic form [dx/yk] ∈H1,0(X) ⊂H1(X). Thus it records a part
of the Hodge structure on X.
Using ideas familiar from polygonal billiards, in §6 we show that fq is a
local homeomorphism when qn̸ = 1. It is also equivariant with respect to the
action of Bn via the mapping-class group on T ∗
0,n and via the representation
ρq on Hr,s. Thus the period map gives the moduli space M∗
0,n the structure of
a (G, X)-manifold, where G = U(r, s) and X = Hr,s. A similar construction
applies to M0,n (the moduli space of n points in the sphere instead of in the
plane), when q = ζ−2
n . (For more on period mappings in general, see e.g.
[CMP].)
Arithmetic groups. It is a challenging problem to describe the image of
the braid group under ρq. In particular, it is unknown when An−1(q) ∼=
ρq(Bn) is a lattice in U(r, s).
To study the image of ρq in more detail, we begin by observing that the
action of Bn on H1(X)q preserves the module Λn,q = H1(X, Z[q])q. Thus
ρq(Bn) is contained in the countable subgroup
U(Λn,q) ⊂U(H1(X)) ∼= U(r, s)
of unitary automorphisms of this module.
In §7 we determine all pairs (n, q) such that U(Λn,q) is discrete (see
Table 9). When discreteness holds, ρq(Bn) is also discrete, and potentially
arithmetic. There are inﬁnitely many (n, q) such that U(Λn,q) is discrete, but
for n > 12 this only occurs when Z[q] is itself discrete (i.e. when d = 2, 3, 4
or 6).
Special cases. In §8—§13 we develop the interaction between fq, ρq(Bn)
and U(Λq,n) in more detail, in three special cases.
1. The ﬁnite case. Let q be a primitive dth root of unity. In §8 we show
that ρq(Bn) is ﬁnite iﬀU(Λn,q) is ﬁnite. Referring to Table 9, we ﬁnd there
are exactly 9 pairs (n, d) such that this ﬁniteness holds. In each case H1(X)q
has signature (0, s) or (s, 0), and the Hodge structure on the corresponding
part of H1(X) is rigid; equivalently, we have an isogeny
Jac(X) ∼J(X) × A
3
where A is independent of X. For example, when X is deﬁned by
y10 = (x −b1)(x −b2)(x −b3)
its Jacobian has a rigid factor isomorphic to (C2/Z[ζ5])2. In the other 7
cases, the rigid factor is a product of elliptic curves.
Certain instances of this rigidity can be seen in terms of conformal map-
pings.
For example, when all the (bi) are real, the case (n, d) = (3, 4)
is related to the fact that any (45,45,45,135)-degree quadrilateral can be
mapped conformally onto the complement of a symmetric slit in a right-
isosceles triangle (Figure 2). These polygons, when doubled, represent the
sphere with the metrics |dx/y3| and |(x −a)dx/y3| respectively. Since the
second polygon develops, under reﬂection through its sides, onto a periodic
pattern in the plane, the form (x −a)dx/y3 is pulled back from the square
torus, giving Jac(X) a factor of C/Z[√−1].
a
1
2
b
b3
2
b
b3
1
b
8
8
b
Figure 2. Quadrilaterals and squares.
By similar considerations, in §9 we determine 17 values of (n, µ) such
that the deﬁnite integral
I(b1, b2, . . . , bn) =
Z b2
b1
dx
((x −b1)(x −b2) · · · (x −bn))µ
is an algebraic function of its parameters. The integral is evaluated explicitly
for (n, µ) = (4, 3/4), as an example.
2. The complex hyperbolic case. In §10 we turn the case where H1(X)q
has signature (1, s). In this case the period map
fq : T ∗
0,n →H1,s ∼= CHs
is a holomorphic map to the complex hyperbolic ball. Using the Schwarz
lemma, we ﬁnd ρq(Bn) ⊂U(1, s) is a lattice whenever it is discrete. Exam-
ining Table 9, we obtain 24 cases where ρq(Bn) is an arithmetic lattice. In
4
particular we ﬁnd that for n = 4, 5, 6, 8 and 12, the period map
fq : M0,n →CHn−3/ρq(Bn)
at q = ζ−2
n
presents moduli space as the complement of a divisor in a ﬁnite-
volume, arithmetic, complex-hyperbolic orbifold. These results are special
cases of the work of Deligne–Mostow and Thurston, which we review in §10.
We also develop parallels between non-arithmetic lattices in U(1, 2) and the
known Teichm¨uller curves on Hilbert modular surfaces.
Next, consider the following purely topological problem. Let Sp(X)T ∼=
Sp2g(Z)T denote the centralizer of T ∗in the automorphism group of H1(X, Z),
and let
Sp(X)T
d = Sp(X)T | Ker Φd(T ∗)
where Φd(x) is the dth cyclotomic polynomial. We say a group homomor-
phism is almost onto if the image has ﬁnite index in the target.
Problem: Is the natural map Bn →Sp(X)T
d almost onto?
In §11 we connect this problem to arithmeticity of lattices. We show that
for n = 3, the answer is yes iﬀthe (2, 3, p) triangle group is arithmetic, where
p is the order of d−2 in Z/2d. (There are 16 such cases.) More generally, the
answer is yes whenever (d, n) appear in Table 9 with signature (0, s) or (1, s).
On the other hand, using a non-arithmetic lattice in U(1, 2) constructed by
Deligne and Mostow, we show the answer is no when (n, d) = (4, 18).
3. The hyperelliptic case. In §12 we discuss the hyperelliptic case, where
d = 2 and q = −1. In this case H1(X)q = H1(X), and ρq(Bn) has ﬁnite
index in U(Λn,q) ∼= Sp2g(Z) by [A’C].
For convenience, assume n = 2g + 1 is odd and g ≥2. Then there is
a natural Weierstrass foliation of Teichm¨uller space by complex geodesics,
each of which is sent into a straight line under the period map
fq : T ∗
0,n →Hg,g.
In fact there is an equivariant action of SL2(R) on suitable circle bundles
over the domain and range of fq. Using this action we ﬁnd:
1. The period map fq is an inﬁnite-to-one local homeomorphism, but not
a covering map to its image;
2. It transports the discrete action of Bn on T ∗
0,n to an ergodic action on
Hg,g; and
5
3. The complement of the image fq(T ∗
0,n) is contained in a countable
union of lines.
The last assertion is deduced using Ratner’s theorem as in [Kap].
The Weierstrass foliation descends to a foliation W of M∗
0,n. Although
almost every leaf of W is dense, Veech showed the special leaf V passing
through [(bi = ζi
n)] is a properly embedded algebraic curve.
In §13 we
discuss this Teichm¨uller curve V from the perspective of braid groups and
ﬂat metrics on the sphere. We ﬁrst show that π1(V ) is the (2, n, ∞) triangle
group generated by the images of the braids
α = τ1τ3 . . . τ2g−1
and
β = τ2τ4 . . . τ2g.
(Note that αβ is a lift of the Coxeter element for the An−1 diagram.) We
then describe the abstract Euclidean polygons Q = (bC, |ω|) associated to the
two orbifold points of V : one is obtained from a regular n-gon by folding its
vertices to a single point, while the other is the double of an immersed, right-
angled disk whose edge lengths form an eigenvector for the An−1 adjacency
matrix. These descriptions allow one to explicitly evaluate the period map
at the orbifold points of V .
Figure 3. Line conﬁguration associated to 5 points on a conic.
Remark: Cyclic multiple planes. One can also associate to each point
conﬁguration (b1, . . . , bn) ∈C⟨n⟩the cyclic covering X of P2 deﬁned by the
equation
zd = L1(x, y) · · · Ln(x, y)Q(x, y),
where Li(x, y) = y −2bix+b2
i and Q(x, y) = y −x2. This complex surface is
branched over the conic Q, its tangent lines Li at Pi = (bi, b2
i ), and (possibly)
the line at inﬁnity (Figure 3). After desingularizing X one obtains, for each
eigenspace, a unitary action of Bn on H2( e
X)q.
It would be interesting
6
to study the associated period maps as Hodge-theoretic counterparts to
the Lawrence–Krammer–Bigelow representations ξq of Bn [Law], [At], [Kr],
[Bg2].
Notes and references.
The hypergeometric functions of the form F =
R b2
b1
Qn
1(x −bi)−µi dx have been studied since the time of Euler; the present
discussion is closely connected to works of Schwarz and Picard [Sch], [Pic].
For more on the classical theory of hypergeometric functions, see e.g. [Kl],
[SG] and [Yo]. Deligne and Mostow developed a modern perspective on hy-
pergeometric functions, and used their monodromy to exhibit non-arithmetic
lattices in U(1, s) for certain s ≥2 [Mos1], [DM1], [DM2]; see also [Sau]
and the surveys [Mos2] and [Par].
Thurston recast the work of Deligne
and Mostow in terms of shapes of convex polyhedra, by observing that the
integrand of F determines a ﬂat metric on the sphere with cone-type singu-
larities. Convexity of the polyhedron corresponds to signature (1, s) for the
metric on moduli space [Th2]. For other perspectives, see [V3] and [Tr].
In this paper we have focused on the case where all µi assume a common
rational value k/d. This case leads directly to algebraic curves and their
Jacobians, and yields representations of the full braid group. At the same
time it allows for non-convex polyhedra (as in Figure 2) and non-hyperbolic
signatures (r, s), because |dx/yk| can be negatively curved at x = ∞.
Analogous Hodge-theory constructions have been used to study, instead
of ﬁnite sets in P1, hypersurfaces of low degree in P1 × P1 or Pn, n ≤4; see
e.g. [DK], [Ko], [ACT1], [ACT2], [Al2], [Lo2]. The action of the mapping-
class group of a closed surface on the homology of its ﬁnite abelian covers is
studied in [Lo1].
We note that ρq is essentially a specialization of the Burau representa-
tion (§5); as a representation of the Hecke algebra Hn(q), it corresponds to
the partition n = 1 + (n −1) [J], [KT]. The Lawrence–Krammer–Bigelow
representations ξq correspond to the next partition, n = 2 + (n −2). Our
investigation began with the observation that ρq coincides with the quantum
representations discussed in [AMU] when n = 3. It would be interesting to
understand more fully the connection between classical and quantum repre-
sentations.
Acknowledgements. I would like to thank D. Allcock, J. Andersen, B.
Gross, M. Kapovich, D. Margalit and J. Parker for useful conversations.
Notation. We use ⌊x⌋to denote the largest integer ≤x, and ⌈x⌉for the
smallest integer ≥x. We let U(V ) denote the unitary group of a Hermitian
vector space V over C. The unitary group of the standard Hermitian form
of signature (r, s) on Cr+s is denoted by U(r, s), and the corresponding
7
projective group by PU(r, s) ∼= U(r, s)/ U(1). The automorphism group of
a real symplectic vector space is denoted by Sp(V ) ∼= Sp2g(R).
