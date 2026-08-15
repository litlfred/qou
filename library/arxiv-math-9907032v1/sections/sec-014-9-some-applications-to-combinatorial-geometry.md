---
doc_id: arxiv-math-9907032v1
doc_title: "Mathematics Department, California Institute of Technolog y"
section_id: sec-014-9-some-applications-to-combinatorial-geometry
section_title: "SOME APPLICATIONS TO COMBINATORIAL GEOMETRY"
section_number: 9
pages: 22-23
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
A well-known theorem of Steinitz says that every three-connecte d planar graph
can be realized as the 1-skeleton of a convex polyhedron in R3, while a famous
theorem of Aleksandrov states that every Euclidean metric on S2 with positively
curved cone-points can be realized as the induced metric on the sur face of a convex
polyhedron in R3. Below, we show a negative result, which should be compared
with the ﬁnal example of [17]:
Theorem 9.1. There exist inﬁnitely many triangulations of S2 which can not be
realized as a Delaunay triangulation with respect to the con e-points of any Euclidean
metric on S2 with positively curved cone-points.
First a deﬁnition:
Definition 9.2. LetT be a triangulation. The stellation s(T ) of T is the com-
plex obtained by replacing each face ABC of T by three faces AOB, AOC, and
BOC .
Theorem 9.1 follows immediately from the following claim.
Claim 9.3. LetT be any triangulation of S2 with at least eight faces. Then the
stellation s(T ) of T is not combinatorially equivalent to the Delaunay triangul ation
of any Euclidean metric on S2 with positively curved cone-points, where the cone-
points correspond to vertices of s(T ).
Proof. Let an old vertex of s(T ) be one that was already a vertex of T , while a
new vertex be one that was added at stellation. The set N of new vertices of s(T )
corresponds to the set of faces of T . For any vertex v, recall that C(v) denotes the
cone angle at v. The Gauss-Bonnet theorem tells us that
∑
v∈V (s(T ))
(2π −C(v)) = 4π. (29)
Or, recombining the terms:
∑
v∈V (s(T ))
C(v) = 2π(|V (s(T ))| − 2). (30)
Note that every edge of s(T ) is incident to an old vertex, and to at most one new
vertex. Combining this observation with Lemma 1.2, we see that for a ny Delaunay
triangulation combinatorially equivalent to s(T ), it must be true that
∑
v∈{old vertices of s(T )}
C(v) ≥
∑
v∈{new vertices of s(T )}
C(v). (31)
· 23
Combining Eq. 31 with Eq. 30, it follows that
∑
v∈{old vertices of s(T )}
C(v) ≥π(|V (s(T )) − 2). (32)
Note now that |V (s(T ))| = |V (T )| + |F (T )|. By a standard computation using
Euler’s formula for triangulations of the sphere, we know that |V (T )| = 1
2 |F (T )|+2,
thus |F (T )| = 2|V (T )| − 4. Thus,
|V (s(T )) − 2| = 3|V (T )| − 6. (33)
Equations 33 and 32 together imply that the average cone angle at an old vertex
of s(T ) is at least π(3|V (T )| − 6)/|V (T )| = 3π − 6/|V (T )|. If |V (T )|> 6 it follows
that the average cone angle at an old vertex is greater than 2 π, which contradicts
the assumption that the cone angles were positively curved.
