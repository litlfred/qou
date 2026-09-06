---
doc_id: arxiv-1210.5756v1
doc_title: "Contact Graphs of Unit Sphere Packings Revisited ∗"
section_id: sec-008-61-an-upper-bound-on-touching-triplets-on-s2
section_title: "An upper bound on touching triplets on S2"
section_number: 6.1
pages: 13-16
source_pdf: 1210.5756v1.pdf
source_sha256: c7546a79a85b8dd5
doc_brief: "Contact Graphs of Unit Sphere Packings Revisited ∗ — The contact graph of an arbitrary ﬁnite packing of unit balls in Euclidean 3-space is the (simple) graph whose vertices correspond to the packing"
---
Our main goal is to show that the number of touching triplets in an arbitrary packing of spherical caps of
angular radius π/6 on S2 is at most 11.
Let X ={x1,..., xN} be a point set on S2 with N≤ 12 and minimum spherical distance π/3 between
any two points in X. Taking the Delaunay triangulation DX of X on S2, we let f be the number of faces,
e be the number of edges, and N be the number of vertices. Since DX is a triangulation of X on S2, every
13
face is a triangle, and so 3 f = 2e. Using Euler’s formula N−e +f = 2, it is straightforward to see that
f = 2N− 4.
Assume to the contrary that there exist at least 12 touching triplets in a packing of N spherical caps of
angular radius π/6 on S2 with the center points forming X and with N≤ 12.
Assume that N = 12. Then f = 2N− 4 = 2(12)− 4 = 20, so there are 20 triangles in DX. We then
have thatDX consists of at least 12 regular triangles (of side length π
3 ) and at most 8 irregular triangles.
(Actually, for the purpose of the proof below, any regular triangle of DX having side length > π
3 is listed
among the irregular ones.) In what follows we assume that the number of irregular triangles is 8. Namely,
if we have fewer than 8, then the analysis of the cases is a simpler version of what we do here, so we
leave it to the reader. Now, we can determine the possible cases for the union of the irregular triangles as
8 = 4 + 4 = 3 + 5 = 2 + 6 = 2 + 3 + 3 = 2 + 2 + 4 = 2 + 2 + 2 + 2, where each number represents a
(dashed)side-to-(dashed)side union of that many irregular triangles. We then have the following cases: (1) 12
One decagon (2) 12 Two hexagons, (3) 12 One pentagon and one heptagon, (4) 12 One quadrilateral and one
octagon, (5) 12 One quadrilateral and two pentagons, (6) 12 Two quadrilaterals and one hexagon, and (7) 12
Four quadrilaterals.
For (1)12, we have that there are 10 vertices of the decagon, so there exists two vertices in X which are
entirely surrounded by regular triangles. This contradicts Remark 1.
For (2)12, we have that there are 12 vertices cumulatively from the two hexagons, so since we have assumed
N = 12, they are pairwise disjoint (see Remark 1). Applying the Hexagon Lemma to either hexagon, we
have a contradiction since both hexagons are assumed to be entirely surrounded by regular triangles.
For (3)12, we have that there are 12 vertices cumulatively from the pentagon and the heptagon, so since
we have assumed N = 12, they are pairwise disjoint (see Remark 1). Applying the Pentagon Lemma to
the pentagon, we have a contradiction since the pentagon is assumed to be entirely surrounded by regular
triangles.
For (4)12, we have that there are 12 vertices cumulatively from the quadrilateral and the octagon, so since
we have assumed N = 12, they are pairwise disjoint (see Remark 1). Applying the Quadrilateral Lemma to
the quadrilateral, we have a contradiction since the quadrilateral is assumed to be entirely surrounded by
regular triangles.
For (5)12, we have that there are 14 vertices cumulatively from the quadrilateral and the two pentagons.
If two of the polygons share an edge, then there is either a quadrilateral or a pentagon which is entirely
surrounded by regular triangles, leading to a contradiction by the Quadrilateral Lemma or Pentagon Lemma.
If the three polygons share precisely one vertex in common, then the Quadrilateral Lemma leads to a
contradiction. So, the only possible conﬁguration left is to have one polygon C to share one vertex with
another polygon C′ with the last polygon C′′ sharing a vertex with C′ (and with the two shared vertices
being distinct). Now, if C or C′′ is a quadrilateral or if C′ is a quadrilateral with the two shared vertices
being adjacent in C′, then the Quadrilateral Lemma leads to a contradiction.
α
γ
θ
α
β
β
C
C
C
`
``
u v w
x
y
Figure 11: The conﬁguration described in case (5) 12.
14
Thus, we are left with the following conﬁguration: C and C′′ are pentagons (of side length π
3 ) and C′ is
a quadrilateral (of side length π
3 ) with the two shared vertices u and v being opposite in C′. Referring to
Figure 11 for this conﬁguration, we let a be the distance between the vertices w and x andb be the distance
between the vertices w and y. Then by the proof of the Quadrilateral Lemma, we have that α = 1.359 and
β = 2.373. Given that the triangles at u and v in Figure 11 are assumed to be regular, we can compute b
as follows. Using the spherical law of cosines, we compute the following where θ = 2π− (arccos 1
3 +β +γ)
as seen in Figure 11,
a = arccos
(1 + 3 cos(2 arccos1
3)
4
)
= 1.91...
γ = arccos
(cos π
3− cos π
3 cosa
sin π
3 sina
)
= 0.615...
b = arccos
(
cosa
2 +
√
3 sina
2 cosθ
)
= 2.15...
Therefore, since b> 2π/3 = 2.09..., we have that this conﬁguration cannot exist as w must be identiﬁed,
without loss of generality, with a vertex of the pentagon C contradicting the rather obvious fact that the
spherical diameter of any pentagon with side lengths equal to π/3 is at most 2π/3.
For (6)12, we have that there are 14 vertices cumulatively from the two quadrilaterals and the hexagon.
If two of the polygons share an edge, then there is either a quadrilateral or a hexagon which is entirely
surrounded by regular triangles, leading to a contradiction by the Quadrilateral Lemma or Hexagon Lemma.
If the three polygons share precisely one vertex in common, then the Quadrilateral Lemma leads to a
contradiction. So, the only possible conﬁguration left is to have one polygon C to share one vertex with
another polygon C′ with the last polygon C′′ sharing a vertex with C′ (and with the two shared vertices
being distinct). Here either C or C′′ must be a quadrilateral and so by applying the Quadrilateral Lemma
we are led to a contradiction.
For (7)12, we show that the total spherical area of the 12 regular triangles (of side length π
3 ) and of the
four quadrilaterals (of side length π
3 ) is < 4π, a contradiction. Indeed, the discrete isoperimetric inequality
of spherical polygons (see for example [4]) implies that the spherical area of a quadrilateral of side length π
3
in S2 is maximal when it is regular. Thus, the total spherical area of the 12 regular triangles and of the 4
quadrilaterals in question is at most
12
(
6 arcsin 1√
3−π
)
+ 4
(
8 arctan
√
2− 2π
)
= 12.052...< 4π = 12.566...
which is a contradiction.
Since the cases (1) 12, (2)12, (3)12, (4)12, (5)12, (6)12, and (7) 12 all lead to a contradiction, we have that
the number of touching triplets in an arbitrary packing of 12 spherical caps of angular radius π/6 on S2 is
at most 11.
Assume that N = 11, then f = 2N− 4 = 2(11)− 4 = 18, so there are 18 triangles in DX. Hence, by our
indirect assumption,DX consists of at least 12 regular triangles and at most 6 irregular triangles. (Just as
above, any regular triangle ofDX having side length> π
3 is listed among the irregular ones.) In what follows
we assume that the number of irregular triangles is 6 and leave the analysis of the simpler case of less than
6 irregular triangles to the reader. So, we can determine the possible cases for the union of the irregular
triangles as 6 = 3 + 3 = 2 + 4 = 2 + 2 + 2, where each number represents a (dashed)side-to-(dashed)side
union of that many irregular triangles. We then have the following cases: (1) 11 One octagon, (2) 11 Two
pentagons, (3)11 One quadrilateral and one hexagon, and (4) 11 Three quadrilaterals.
For (1)11, we have that there are 8 vertices of the octagon, so since we have assumed N = 11, there are
three vertices in X entirely surrounded by regular triangles which is a contradiction (see Remark 1).
For (2)11 and (3)11, we have that there are 10 vertices cumulatively from the two pentagons or from the
quadrilateral and the hexagon, so since we have assumed N = 11, this is a contradiction since there is one
vertex in X entirely surrounded by regular triangles (see Remark 1).
15
For (4)11, we have that there are 12 vertices cumulatively from the three quadrilaterals, so since we have
assumed N = 11, exactly one vertex is shared by the polygons. By applying the Quadrilateral Lemma to
the quadrilateral which does not share a vertex with any other quadrilateral, we arrive at a contradiction.
Since the cases (1) 11, (2) 11, (3) 11, and (4) 11 all lead to a contradiction, we have that the number of
touching triplets in an arbitrary packing of 11 spherical caps with angular radius π/6 on S2 is at most 11.
Assume that N = 10. Then f = 2N− 4 = 2(10)− 4 = 16 and so, there are 16 triangles in DX. Hence,
by our indirect assumption, DX consists of at least 12 regular triangles and at most 4 irregular triangles.
Based on 4 = 2 + 2 we can determine the possible cases for the union of the irregular triangles (by leaving
the study of the simplier case of less than 4 irregular triangles to the reader): (1) 10 One hexagon, and (2) 10
Two quadrilaterals.
For (1)10 as well as (2) 10, we have that there is a vertex in X which is entirely surrounded by regular
triangles contradicting to Remark 1.
Since Case (1)10 and (2)10 both lead to a contradiction, we have that the number of touching triplets in
an arbitrary packing of 10 spherical caps with angular radius π/6 on S2 is at most 11.
Finally, assume thatN≤ 9. Hence, f≤ 2(9)− 4 = 14, and by our indirect assumption there are at least
12 regular triangles (of side length π
3 ) inDX and at most two irregular ones whose union then must be a
quadrilateral (of side length π
3 ). This case is clearly impossible by the spherical area estimate of (7) 12.
This ﬁnishes our indirect proof on the number of touching triplets in Theorem 3.
