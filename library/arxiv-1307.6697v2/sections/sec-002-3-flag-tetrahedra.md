---
doc_id: arxiv-1307.6697v2
doc_title: "REPRESENTATIONS OF FUNDAMENTAL GROUPS OF 3-MANIFOLDS"
section_id: sec-002-3-flag-tetrahedra
section_title: "Flag tetrahedra"
section_number: 3
pages: 5-8
source_pdf: 1307.6697v2.pdf
source_sha256: a3afaefdaebe0292
toc_source: outline
doc_brief: "REPRESENTATIONS OF FUNDAMENTAL GROUPS OF 3-MANIFOLDS — In this paper we are interested in computing representations of the funda- mental group of a 3-manifold into PGL(3, C) (in particular in PGL(2"
---
In this section we recall the parametrization of conﬁgurations of four ﬂags in the projective
space CP2 (more details can be seen in [2]). Let V = C3. A ﬂag in V is usually seen as a
line and a plane, the line belonging to the plane. Using the dual vector space V ∗and the
projective spaces P(V ) and P(V ∗), deﬁne the spaces of ﬂags Fl by the following:
Fl
=
{([x], [f]) ∈P(V ) × P(V ∗) | f(x) = 0}.
The natural action of SL(3, C) on Fl makes us identify the space of ﬂags with the ho-
mogeneous space SL(3, C)/B, where B is the Borel subgroup of upper-triangular matrices
in SL(3, C). A generic conﬁguration of ﬂags ([xi], [fi]), 1 ≤i ≤n + 1 is given by n + 1
points [xi] in general position and n + 1 lines fi in P(V ) such that fj(xi)̸ = 0 if i̸ = j. A
conﬁguration of ordered points in P(V ) is said to be in general position when they are all
distinct and no three points are contained in the same line.
Up to the action of PGL(3, C), a generic conﬁguration of three ﬂags ([xi], [fi])1≤i≤3 has
only one invariant given by the triple ratio
X = f1(x2)f2(x3)f3(x1)
f1(x3)f2(x1)f3(x2) ∈C×
6
E. FALBEL, P.-V. KOSELEFF AND F. ROUILLIER
3.1. Coordinates for a tetrahedron of ﬂags. We recall the parametrization used in [2].
We refer to Figure 3.1 which displays the coordinates.
Let ([xi], [fi])1≤i≤4 be a generic tetrahedron. We deﬁne a set of 12 coordinates on the
edges of the tetrahedron (one for each oriented edge). To deﬁne the coordinate zij associated
to the edge ij, we ﬁrst deﬁne k and l such that the permutation (1, 2, 3, 4) 7→(i, j, k, l) is
even. The pencil of (projective) lines through the point xi is a projective line P1(C). We
have four points in this projective line: the line ker(fi) and the three lines through xi and
one of the xl for l̸ = i. We deﬁne zij as the cross-ratio of four ﬂags by
zij := [ker(fi), (xixj), (xixk), (xixl)].
Note that we follow the convention that the cross-ratio of four points x1, x2, x3, x4 on a line
is the value at x4 of a projective coordinate taking value ∞at x1, 0 at x2, and 1 at x3. So
we employ the formula
[x1, x2, x3, x4] := (x1 −x3)(x2 −x4)
(x1 −x4)(x2 −x3)
for the cross-ratio.
At each face (ijk) (oriented as the boundary of the tetrahedron (1234)), the 3-ratio is
the opposite of the product of all cross-ratios “leaving” this face:
zijk := fi(xj)fj(xk)fk(xi)
fi(xk)fj(xi)fk(xj) = −zilzjlzkl.
This follows from a direct computation (see [2]). Observe that if the same face (ikj)
(with opposite orientation) is common to a second tetrahedron T ′ then
zikj(T ) =
1
zijk(T ′).
Of course there are relations between the whole set of coordinates, namely, the three
cross-ratio leaving a vertex are algebraically related:
zik =
1
1 −zij
,
zil = 1 −1
zij
.
(3.1.1)
Observe that the relations follow a cyclic order around each vertex which is deﬁned by
the orientation of the tetrahedron. We also have
(3.1.2)
zij zik zil = −1.
The next proposition shows that a tetrahedron is uniquely determined, up to the action of
PGL(3, C), by four numbers. One can pick a variable at each vertex. In fact, the space
of ﬂags is a complex manifold (PGL(3, C)/B) and, therefore, conﬁgurations of ﬂags have a
natural complex structure.
3.2. Proposition. [2] The space of generic tetrahedra is biholomorphic to (C \ {0, 1})4.
One can use one cross-ratio coordinate at each vertex, for instance (z12, z21, z34, z43) or
(z13, z21, z32, z43).
7
zkl
zkj
zki
k
zlk
zlj
zli
l
zil
zij
zik
i
zjl
zji
zjk
j
Figure 1. The cross-ratio coordinates (or z-coordinates).
3.3. Hyperbolic ideal tetrahedra. An ideal hyperbolic tetrahedron is given by 4 points
on the boundary of H3
R, i.e. P1(C). Up to the action of PSL(2, C), these points are in
homogeneous coordinates [0, 1], [1, 0], [1, 1] and [1, z] – the complex number z being the
cross-ratio of these four points.
We may embed P1(C) into P2(C) via the Veronese map h, given in homogeneous coordi-
nates by
h : [x, y]
7→
[x2, xy, y2]
and therefore this map and its derivative deﬁne a map from P1(C) to the variety of ﬂags Fl.
Let T be the tetrahedron h([0, 1]), h([1, 0]), h([1, 1]) and h([1, z]). Its image in the variety
of ﬂags given by the above map has coordinates (see [2])
z12(T ) = z21(T ) = z34(T ) = z43(T ) = z.
(3.3.1)
Conversely, given parameters satisfying the equations above, they deﬁne a unique hyperbolic
tetrahedron.
3.4. The CR case. Recall that an element x ∈S3 gives rise to an element ([x], [f]) ∈
Fl(C) where [f] corresponds to the unique complex line tangent to S3 at x. The following
proposition describes the space of generic conﬁgurations of four points in S3.
3.5. Proposition ([10, 2]). Generic conﬁgurations (up to translations by PU(2, 1)) of four
points in S3 not contained in an R-circle are parametrized by generic conﬁgurations of four
ﬂags with coordinates zij, 1 ≤i̸ = j ≤4 satisfying the three complex equations
zijzji = zkl zlk
(3.5.1)
8
E. FALBEL, P.-V. KOSELEFF AND F. ROUILLIER
not all of them being real and such that zjizkizli̸ = 1 for each face with vertices {j, k, l}.
The conditions (3.5.1) together with relation (3.1.2) imply that the triple ratio of each
face satisﬁes |zijk| = 1. For the tetrahedron to be CR we need to verify the condition
zijk = −zjizkizli̸ = −1 for each face with vertices {j, k, l} (the triple ratio is never −1 for a
CR generic triple of ﬂags).
Conditions zijzji = zkl zlk ∈R might describe other conﬁgurations of four ﬂags which
are not CR. From zijkzilj = zlkzkl
zijzji
, we deduce that in this case zijkzilj = 1 and therefore
zijk = zilj = zikl = zjkl = ±1. If the cross-ratio invariants are all real, either one obtains
conﬁgurations contained in an R-circle (they coincide with the real hyperbolic ones with
real cross ratios, that is, z12(T ) = z21(T ) = z34(T ) = z43(T ) = x ∈R −{0, 1}) or one of the
triple ratios is −1 and, in that case, they are not CR.
3.6. The SL(3, R) case. Clearly, a conﬁguration contained in the space of real ﬂags is
characterized by having all its invariants zij real. Observe that the three cases intersect
precisely for conﬁgurations corresponding to degenerate real hyperbolic conﬁgurations.
