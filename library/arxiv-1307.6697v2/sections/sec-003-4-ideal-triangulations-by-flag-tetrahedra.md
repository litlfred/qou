---
doc_id: arxiv-1307.6697v2
doc_title: "REPRESENTATIONS OF FUNDAMENTAL GROUPS OF 3-MANIFOLDS"
section_id: sec-003-4-ideal-triangulations-by-flag-tetrahedra
section_title: "Ideal triangulations by flag tetrahedra"
section_number: 4
pages: 8-9
source_pdf: 1307.6697v2.pdf
source_sha256: a3afaefdaebe0292
toc_source: outline
doc_brief: "REPRESENTATIONS OF FUNDAMENTAL GROUPS OF 3-MANIFOLDS — In this paper we are interested in computing representations of the funda- mental group of a 3-manifold into PGL(3, C) (in particular in PGL(2"
---
We use the deﬁnition of an ideal triangulation of a 3-manifold as it is used usually in
computations with SnapPea. It is a union of 3-simplices K = S
ν Tν with face identiﬁcations
(which are simplicial maps). We let K(0) be the union of vertices in K. The manifold
K −K(0) is, topologically, the interior of a compact manifold when the vertices K(0) are
deleted. In fact, K −K(0) is an (open) 3-manifold that retracts onto a compact 3-manifold
with boundary M (the boundary being the link of K(0)).
Given such a compact oriented 3-manifold M with boundary, we call a triangulation K
as above an ideal triangulation of M. A parabolic decoration of an ideal triangulation is the
data of a ﬂag for each vertex (equivalently a map from the 0-skeleton of the complex to Fl).
A parabolic decoration together with an ordering of the vertices of each 3-simplex equip
each tetrahedron with a set of coordinates as deﬁned in section 3.
From now on we ﬁx K a decorated oriented ideal triangulation of a 3-manifold together
with an ordering of the vertices of each 3-simplex of K. Denote by Tν, ν = 1, . . . , N, the
tetrahedra of K and zij(Tν) the corresponding z-coordinates (or cross-ratio coordinates).
We impose the following compatibility conditions which will imply the existence of a well
deﬁned representation of the fundamental group of the manifold M into PGL(3, C).
4.1. Consistency relations. (cf. [9, 2])
(Face equations) Let T and T ′ be two tetrahedra of K with a common face (ijk) (oriented
as a boundary of T ), then zijk(T )zikj(T ′) = 1.
For a ﬁxed edge e ∈K let Tν1, . . . , Tνne be the ne tetrahedra in K which contain an edge
which projects unto e ∈K (counted with multiplicity). For each tetrahedron in K as above
we consider its edge ij corresponding to e.
(Edge equations) zij(Tν1) · · · zij(Tνne) = zji(Tν1) · · · zji(Tνne) = 1.
The face equations are clearly necessary in order to match a triple of ﬂags from one face
to a triple of another face. The edge equations follow by considering the 1-dimensional
9
projective space of complex lines at each vertex. Indeed, take a vertex whose associated ﬂag
is (p1, l1) on the edge [(p1, l1), (p2, l2)]. Consider the projective space of all lines through p1.
The line l1 will be identiﬁed to ∞and the line [p1, p2] to 0. All the ﬂags (not coinciding
to ∞or 0) in the tetrahedra having this edge in common give rise to an ordered sequence
of points in this 1-dimensional projective space. Imposing that the the point corresponding
to the last vertex of the last tetrahedron coincides with the point corresponding to the ﬁrst
vertex of the ﬁrst tetrahedron amounts precisely to the ﬁrst edge condition. Analogously,
the second condition follows if we consider the projective space of lines at the other vertex
of the edge.
One should be aware that the compatibility conditions do not imply immediately the
existence of a geometric structure. One should think of these as suﬃcient conditions for
the existence of a 0-skeleton compatible with the side pairings. Certainly it implies the
existence of a representation of the fundamental group but one has yet to construct a
compatible extension of the side pairings to 3 simplices. In the hyperbolic case one has
the advantage of the existence of convex ideal tetrahedra but in PU(2, 1) there is no such
canonical construction (see the discussion in [10]).
4.2. Volume. We recall the deﬁnition of volume of a tetrahedron of ﬂags in [2]. The Bloch-
Wigner dilogarithm function is
D(x) = arg (1 −x) log |x| −Im(
Z x
0
log (1 −t) dt
t ),
= arg (1 −x) log |x| + Im(ln2(x)).
Here ln2(x) = −
R x
0 log (1 −t) dt
t is the dilogarithm function. The function D is well-deﬁned
and real analytic on C −{0, 1} and extends to a continuous function on CP 1 by deﬁning
D(0) = D(1) = D(∞) = 0.
Given a tetrahedron of ﬂags with coordinates (z1(T ), z2(T ), z3(T ), z4(T )), we deﬁne its
volume as
Vol(T ) = 1
4(D(z1) + D(z2) + D(z3) + D(z4)).
The volume of a triangulation is the sum of the volumes of its tetrahedra. If the tetrahedron
is hyperbolic this deﬁnition coincides with the volume of volume in hyperbolic geometry. If
the tetrahedron is real its volume is zero. Although CR tetrahedra have generically a non
zero volume, if a triangulation is such that all tetrahedra are CR then the total volume is
zero ([12]).
