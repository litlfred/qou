---
doc_id: arxiv-1609.08719v1
doc_title: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE"
section_id: sec-008-23-the-bloch-group
section_title: "The Bloch group"
section_number: 2.3
pages: 4-7
source_pdf: 1609.08719v1.pdf
source_sha256: f61ff2111e9a97f9
toc_source: outline
---
Deﬁnition 2.3. For any ﬁeld F, the Pre-Bloch group on F, denoted P(F), is
deﬁned as
P(F) =
⟨{z ∈F | z̸ = 0F , 1F }⟩
[z1] −[z2] +
h
z2
z1
i
−
h
1−z2
1−z1
i
+
h
1−z−1
2
1−z−1
1
i.
The relation in the denominator is known as the Five Term Relation. The
variables z1 and z2 are to be understood as cross-ratios of hyperbolic simplices.
The relation encodes that the union of two simplices with volumes [z1] and [z2]
is also the union of three simplices with volumes [ z2
z1 ], [ 1−z2
1−z1 ], and [ 1−z−1
2
1−z−1
1 ]. This
equivalence is called the Pachner 2-3 move (see ﬁgure 1).
←→
0
1
∞
z1
z2
←→
Figure 1. The Pachner 2-3 move.
Deﬁnition 2.4. For any ﬁeld F, the Bloch group on F, denoted B(F), is the
kernel of the map d : P(F) →F ∗∧Z F ∗deﬁned by
d : [z] 7→z ∧(1 −z).
The map d is an analogue of the Dehn invariant map [Neu98], which (for F = C)
ﬁts into an exact sequence of scissors congruence described in e.g. [Dup01]. Thus,
understanding B(F) = ker d provides insight into scissors congruence groups and
generalizations of Hilbert’s third problem.
2.4. Gluing Equations. Given a hyperbolic 3-manifold M with cusps, the stan-
dard procedure for determining vol(M) is to ﬁrst triangulate M into a collection
of simplices {∆i} (together with face pairings), next to compute the cross ratio
zi of each ∆i, and ﬁnally to compute vol(M) by equation 2.0.2. The ﬁrst step is
well-understood: the manifolds included in the censuses of SnapPy include trian-
gulations. The third step is a matter of numerical approximation, but the second
step deserves more explanation. We present an overview of the gluing equations
here, and refer to [NZ85] for a more detailed description, including a treatment of
gluing equations for closed manifolds obtained by Dehn surgery.
INVESTIGATION OF NEUMANN’S CONJECTURE
5
Given a triangulation {∆i} of M, the standard method of ﬁnding {zi} is to
exploit the torus boundary components and local Euclidean nature of the manifold
to produce and solve a system of equations in {zi}. Equations 2.6.1, which arise
from torus boundary components, are the cusp equations, and equations 2.7.1,
which arise from local Euclideanness, are the edge equations. Together, they are
the gluing equations.
Since, in the triangulation of M, a link component appears at the vertices of
each simplex, a torus can be determined by truncating the simplices, then making
edge identiﬁcations to match face identiﬁcations, as in ﬁgure 2.
Figure 2. Piecing together a torus from a triangulation.
Since the meridian and the longitude of a torus are homotopically circles, it
should be possible to require that any path following a meridian or longitude winds
exactly once. In other words, it should be possible to construct a system of equa-
tions, with variables representing various angles of each ∆i, such that certain sums
are 2π.
By considering each ∆i as ideal, each segment of such a path can be viewed as
complex multiplication (recall that all cross-ratios are in C ∪{∞}. For example,
in ﬁgure 3, the rotation that takes a point from start to end of a bold arrow is the
same rotation that takes 1 to z: multiplication by z. By re-ordering the vertices of
∆i, other paths may be expressed as re-ordered cross-ratios.
0
1
z
∞
z =
[∞: 0 : 1 : z]
Figure 3. Identifying torus traversal with multiplication in C.
Deﬁnition 2.5. Let a triangulation be ﬁxed. To each simplex associate a variable
zi. For each edge eij in the simplex, transforming any point by rotating around
6
GILLES AND HUSTON
eij is equivalent to multiplication of that point by either zi, zi−1
zi , or
1
1−zi (ﬁx one
angle as zi, determine the rest by cross-ratio rearrangement).
Let p be a closed path in a triangulated surface, transverse to all edges. For every
consecutive pair of edges that p crosses, those edges must meet at an angle, which
is associated to some zi,
zi−1
zi , or
1
1−zi . The path monodromy of p, denoted
M(p), is the product of all these variables.
Deﬁnition 2.6. Let a triangulation of a manifold M be ﬁxed.
For each torus
boundary component Ti of M, choose meridian and longitude paths in the torus
(transverse to all edges) mi and ℓi respectively. The cusp equations are
(2.6.1)
M(mi) = 1
and
M(ℓi) = 1
There are two such equations for each torus boundary component.
One more piece of geometric information will be useful. For each edge in the
triangulation, consider all face identiﬁcations that contain that edge as an axis.
Such identiﬁcations identify the edges of neighboring faces, and these faces join to
form two polygons, one around each vertex of the edge. For example, see ﬁgure 4,
in which the shaded region is a polygon for the edge shown in bold. We arbitrarily
consider the polygon to be the one about the terminus point of the edge.
Figure 4. Piecing together a polygon from a triangulation.
Deﬁnition 2.7. Let a triangulation of a manifold M be ﬁxed. For each distinct
edge ei in the triangulation, let Pi be the polygon described above associated to
that edge. Let pi be a path in Pi circling the central point. The edge equations
are
(2.7.1)
M(pi) = 1
There are as many edge equations as there are distinct edges in the chosen trian-
gulation.
If two triangulations of M are both composed of non-degenerate, geometrically
viable simplices, by Mostow rigidity they must yield the same volume. Therefore,
given a triangulation {∆i} of M, if the cross-ratios zi all have positive imaginary
part, then computing P
i D(∆i) will yield vol(M). It is possible, however, for a
triangulation not to yield solutions that give a geometric volume. In software imple-
mentations, this is usually dealt with by re-triangulating using diﬀerent parameters.
As presented, the system of cusp and edge equations can be hard to solve by
hand, because their degree is unbounded. For example, the complement of the knot
61 (see ﬁgure 5), known as m032, has the triangulation given in ﬁgure 6, and admits
the boundary torus given in ﬁgure 7.
INVESTIGATION OF NEUMANN’S CONJECTURE
7
Figure 5. 61.
00 01
02
03
10 11
12
13
20 21
22
23
30 31
32
33
Figure 6. m032.
00
20
13
02
10
33
32
21
11
30
23
31
01
12
03
22
Figure 7. The torus boundary of m032.
A path through the torus from left to right (for example, from the single-arrow
edge of 22 to the corresponding edge of 10) would have to pass through at least
eleven faces, inducing a cusp equation with eleven terms. Computer programs such
as SnapPy [CDW] can solve these equations (numerically) quite eﬃciently.
