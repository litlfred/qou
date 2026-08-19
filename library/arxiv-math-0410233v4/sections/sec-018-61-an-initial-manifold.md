---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMA TION JESSICA S. PURCELL"
section_id: sec-018-61-an-initial-manifold
section_title: "An initial manifold"
section_number: 6.1
pages: 31-39
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION JESSICA S. PURCELL — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp sh ape."
---
the knot K. At each twist region of the diagram, add a closed curve en-
circling two strands, called a crossing circle. We now have a diagram of a
link, which we call J. The link complement S3 − J is homeomorphic to the
complement of the link L obtained from J by removing pairs of crossings
from each twist region. See Figure 5.
These links with crossing circles added have been studied by many peo-
ple, including Adams [1]; Lackenby, Agol and Thurston [16]. Many of the
properties of these links were addressed in previous papers (see [21], and
[12] with Futer).
The links are useful to us in the cone manifold setting becaus e ﬁrst, sym-
metries of the diagram of L allow us to determine the hyperbolic structure on
S3 −L explicitly. Secondly, S3 −L is related to the original knot complement
via Dehn ﬁlling. In particular, if 2 mi crossings were removed from the i-th
twist region to go from the diagram of J to that of L, then by performing
a 1 /mi Dehn ﬁlling on the corresponding i-th crossing circle of S3 − L, we
re-insert these crossings and put back the crossing circle, obtaining S3 − K
(see e.g. [22], Chapter 9).
Thus, starting with a hyperbolic augmented link L, we can determine
information including shapes of the cusps. Next, we can ﬁnd c onditions
which will ensure the Dehn ﬁlling above can be obtained by a hy perbolic
Dehn ﬁlling via cone deformation. Hence we will have the ﬁrst two pieces
needed to bound the normalized height of the cusp K: The initial manifold
32 JESSICA S. PURCELL
M with hyperbolic structure will be S3 − L. It will be connected by cone
deformation to S3 − K.
6.1.1. The geometry of S3 − L. We note in [12] that if K has at least 2 twist
regions, then the augmented link complement S3 − L will admit a complete,
ﬁnite volume hyperbolic structure. This can be shown by work of Adams
[1], using the geometrization of Haken manifolds. It can als o be shown more
directly using Andreev’s theorem. The proof using Andreev’ s theorem gives
a packing of circles related to S3 − L which we will need again in Section
6.4, so we include it here.
Theorem 6.1. If K has a prime, twist reduced diagram with at least 2 twist
regions, then the augmented link complement S3 − L will admit a complete,
ﬁnite volume hyperbolic structure.
Proof. We prove the lemma by ﬁnding the hyperbolic structure. To do s o,
we decompose S3 − L into two ideal polyhedra, as in [16] and [12]. We
then ﬁnd a hyperbolic structure on the polyhedra which gives a nonsingular
hyperbolic structure on S3 − L after gluing.
To ﬁnd the polyhedra, ﬁrst remove all remaining single cross ings at cross-
ing circles. That is, if the number of crossings in a twist reg ion of the
diagram of K was odd, then S3 − L will still have a single crossing at that
twist region. Remove it. The new link has components lying ﬂa t in the
projection plane bound together by crossing circles. Call i t L′.
Slice S3 − L′ along the projection plane. This cuts the manifold into
two identical pieces, one on either side of the plane. Each 2– punctured
disk encircled by a crossing circle has been sliced in half. S lice along these
remaining halves of disks, opening them up into two faces. Th is gives an
ideal polyhedral decomposition of the manifold. The edges a re given by the
intersection of the 2–punctured disks with the projection p lane. On each of
the two polyhedra, we have one face per planar region of the di agram of L′,
and two triangular faces per 2–punctured disk. Shade the fac es arising from
2–punctured disks, giving each polyhedron a checkerboard c oloring. The
edges meet in 4–valent ideal vertices. At each vertex, two wh ite faces are
separated by two shaded faces. (See [12] or [16] for pictures .)
The gluing pattern on the polyhedra is given by following the above pro-
cess in reverse: First, on each polyhedron fold the pairs of t riangular shaded
faces together at their common vertex. Then glue each white f ace to its
corresponding face on the opposite polyhedron via the ident ity map. This
gives back S3 − L′.
To obtain S3 − L, we use the same two polyhedra, but make the following
change in gluing. For crossing circles encircling a single c rossing of the
diagram of L, rather than glue shaded triangles across their common vert ex
on a single polyhedron, we insert a half–twist by gluing each triangle of one
polyhedron to the opposite triangle of the other. See Figure 6.
Now our goal is to ﬁnd a hyperbolic structure on these two poly hedra. We
show the two polyhedra actually have totally geodesic faces in H3, meeting
CUSP SHAPES UNDER CONE DEFORMATION 33
Figure 6. Left: Gluing 2–punctured discs with no crossings.
Right: Gluing 2–punctured discs with a single crossing.
in dihedral angles of π/2. Since faces are glued in pairs, and edges in 4’s,
the gluing will give a complete hyperbolic structure on S3 − L.
Note any totally geodesic plane in H3 extends to give a circle on the
boundary S2 at inﬁnity. Conversely, given a collection of circles on S2,
we can view those circles as boundaries of planes in H3. We obtain our
polyhedra by ﬁnding appropriate circle packings, then cutt ing away half–
spaces bounded by hemispheres in H3. Our tool is a corollary of Andreev’s
theorem noted by Thurston in [23]:
Theorem 6.2 (Andreev). Let γ be a triangulation of S2 such that each
edge has distinct ends and no two vertices are joined by more t han one edge.
Then there is a packing of circles in S2 whose nerve is isotopic to γ. This
circle packing is unique up to M¨ obius transformation.
Recall that the nerve of a circle packing is the graph obtained by adding
a vertex for each circle, and an edge connecting two vertices if and only if
the corresponding circles are tangent.
We begin by ﬁnding a triangulation of S2 associated with one of the
polyhedra described above. For each white face, take a verte x. Connect two
vertices by an edge if and only if the two corresponding white faces meet at
a vertex of the polyhedron. This gives a triangulation γ of S2. Note if we
draw vertices of γ on top of white faces of the polyhedron, and edges of γ
through the vertices of the polyhedron, that each triangle o f γ circumscribes
a shaded face of the polyhedron.
To apply Andreev’s theorem, we need to show this triangulation γ satisﬁes
the conditions: each edge has distinct ends, and no two verti ces are joined
by more than one edge. To show these conditions, we consider t he graph
dual to γ, as follows.
Consider the original link diagram. We view it as a 4–valent g raph. Re-
place each twist region of the graph by a single edge, as in Fig ure 7.
Since each crossing is part of some twist region, this gives a trivalent
graph Γ. Note the dual graph to Γ is isotopic to the triangulat ion γ. We use
properties of the dual Γ to show the triangulation γ satisﬁes the conditions
necessary for Andreev’s theorem.
Lemma 6.3. No edge of γ has a single vertex at both endpoints.
34 JESSICA S. PURCELL
Figure 7. Create a trivalent graph by replacing each twist
region with an edge.
(a)
e
(b)
D D ′
· · ·
Figure 8. (a.) Form of Γ if γ has an edge with a single ver-
tex at both endpoints. (b.) Corresponding form of original
link diagram.
Proof. Consider the graph Γ. If its dual γ has an edge with one vertex at
both endpoints, then the graph Γ must be of the form in Figure 8 (a).
Note then if the edge e was an original edge of the 4–valent link diagram,
then we have a simple closed curve intersecting the link diag ram transversely
in a single point. This is impossible.
If instead the edge e replaced a twist region in the original 4-valent link
diagram, then the original diagram had the form of Figure 8 (b ). How-
ever, note one of the subdiagrams D and D′ must contain crossings else the
original diagram has at most one twist region. Without loss o f generality,
say D contains crossings. Then the dashed simple closed curve enc losing D
intersects the link diagram transversely in two points, but both its interior
and its exterior contain crossings. This contradicts the fa ct that the original
diagram was prime. □
Lemma 6.4. No two vertices of γ are joined by more than one edge.
Proof. Suppose two vertices of γ are joined by two distinct edges. Then
consider the dual graph Γ. Γ must be of the form shown in Figure 9 (a),
where region B and region B′ are the same.
Give the edge e1 an orientation, say e1 points in the direction of the edge
a. This gives the region A an orientation, and hence assigns to the edge e2
an orientation. Now, trace a path of edges around the region B, listing the
edges in the order they occur. Our list begins with e1, then a, etc. Note
e2 must appear in the list before the edge d, else region B would be cut oﬀ
from region B′. Also, edge b must occur before edge c, by the orientation
on e2. Hence the graph Γ has the form illustrated in Figure 9 (b).
Case 1: Edges e1 and e2 both were edges of the original 4–valent link
diagram. Then there is a simple closed curve intersecting e1 and e2 trans-
versely in the original link diagram and intersecting the di agram in no other
CUSP SHAPES UNDER CONE DEFORMATION 35
(a)
a
B· · ·
d
· · ·
.
.
.
A.
.
.
b
· · · B′
c
· · ·
e1
e2
(b)
B e1
A
e2
Figure 9. Form of Γ when γ has two vertices connected by
two distinct edges. In (a), the edges of γ are the dashed lines,
with one of the vertices in A and the other at ∞.
(a)
D D ′
· · ·
· · ·
(b)
D D ′
· · ·
Figure 10. Possible forms of the original link diagram if γ
contains two vertices connected by two distinct edges.
points. Since the original diagram has crossings on either s ide of the region
A, this contradicts the fact that we started with a prime diagr am.
Case 2: Edges e1 and e2 both replaced twist regions in the original link
diagram. Then the original link diagram must have been of the form in
Figure 10 (a). Then since the original diagram was twist redu ced, either
the subdiagram D or D′ must be a string of bigons. But then rather than
two distinct twist regions, our diagram must have had only on e twist region.
Thus edges e1 and e2 would not have been distinct.
Case 3: One of edge e1 or e2 is from the original link diagram, the other
replaced a twist region. Then the original link diagram must have been
of the form shown in Figure 10 (b). Now note that the simple clo sed curve
bounding subdiagram D intersects the link transversely in only three points.
This is impossible.
Since these are the only three cases, these contradictions p rove the lemma.
□
Now Lemmas 6.3 and 6.4 are enough to show that Andreev’s theor em
applies, and there is a circle packing of S2 whose nerve is γ.
Complete the proof of Theorem 6.1 by slicing oﬀ half–spaces b ounded by
geodesic hemispheres in H3 corresponding to each circle in the circle packing.
These give the geodesic white faces of the polyhedron. The sh aded faces are
36 JESSICA S. PURCELL
obtained by slicing oﬀ hemispheres in H3 corresponding to each circle of
the dual circle packing. Note white and shaded hemispheres m eet at right
angles.
Thus the polyhedron for the ﬂat augmented link is totally geo desic in H3,
and hence the ﬂat augmented link is hyperbolic. □
6.1.2. Normalized lengths on cusps. To apply results on cone deformations,
we will need the following information on normalized length s of particular
curves on the cusps of S3 − L.
Proposition 6.5. Let K and L be as above. In the prime, twist reduced
diagram of K, let n be the number of twist regions. Let ci be the number of
crossings in the i-th twist region. Then on cusps of L, we have the following
normalized lengths.
(1) For a cusp corresponding to a crossing circle, let si be the slope such
that Dehn ﬁlling S3 − L along si re-inserts the ci crossings at that
twist region. Then the normalized length of si is at least √
ci.
(2) For the cusp corresponding to the link component in the proje ction
plane, the normalized height (i.e. the normalized length of the curve
orthogonal to a meridian) is at least √n, and at most
√
n(n − 1).
Proof. This can be deduced from results of [12]. However, given the c ircle
packing associated to S3 − L developed in the previous section, we are able
to streamline the proof somewhat.
First, recall the polyhedra obtained in the proof of Theorem 6.1. Note
each cusp will be tiled by rectangles given by the intersecti on of the cusp
with the totally geodesic white and shaded faces of the polyh edra. Two
opposite sides of each of these rectangles come from the inte rsection of the
cusp with shaded faces of the polyhedra, or from the 2–punctu red disks in
the diagram of L, and the other two sides come from white faces. Call the
sides shaded sides and white sides, respectively.
For part (1), note any crossing circle intersects a single 2– punctured disk
in a longitude. Half of the longitude is given by the intersec tion with one
polyhedron, the other half by intersection with the other. T he crossing circle
intersects no other shaded faces. Thus the crossing circle c usp is tiled by
exactly two identical rectangles.
When the crossing circle encircles no single crossing, or ha lf twist, then
two white faces intersect the cusp in meridians. In this case , ci is even,
ci = 2 mi, and the slope si is 1 /mi. It is given by one step along a white
side of a rectangle (a meridian), plus 2 mi = ci steps along shaded sides of
the rectangle.
When the crossing circle encircles a single crossing, then t he two rectangles
tiling the cusp are sheared. In this case, a meridian is given by one step along
a white side, plus (or minus) a step along a shaded side. Now ci = 2mi + 1 is
odd, and the slope si = 1/mi is given by a step along a white side, plus (or
CUSP SHAPES UNDER CONE DEFORMATION 37
Figure 11. The form of the packing of circles about any
vertex. Dashed circles correspond to the shaded faces of the
polyhedron at this vertex.
minus) a step along a shaded side, plus (or minus) 2 mi steps along shaded
sides.
In either case, the slope is given by a single step along a whit e side plus
(or minus) ci steps along a shaded side. Let w denote the length of a white
side, and let s denote the length of a shaded side. Thus the normalized
length of si is: √
w2 + c2
i s2
√
2ws =
√ w
2s + c2
i
s
2w .
Let u = w/(2s). Then for constant ci, this quantity is minimized when
u = ci/2, and the minimum value is √ci.
For part (2), we need to know more about the possible lengths o f the
white sides of rectangles tiling the cusp. For a given rectan gle, consider the
corresponding vertex in one of the polyhedra. On the sphere S2 at inﬁnity,
this vertex will look like a point of tangency of two circles i n the packing
given by Andreev’s theorem. Since the nerve of this circle pa cking is a
triangulation of S2, the point of tangency corresponds to an edge on two
distinct triangles of this nerve. Thus there are two additio nal circles tangent
to the two given circles, as in Figure 11.
Now, apply a M¨ obius transformation taking the vertex, or th e point of
tangency of the circle packing, to inﬁnity. This takes the tw o tangent circles
to two parallel lines. It takes the two additional tangent ci rcles to circles
tangent to both the parallel lines, as in Figure 12. Note this also gives the
similarity structure of the rectangle under consideration . If we normalize
so that the shaded side (coming from the intersection with a 2 –punctured
disk) has length 1, then the circle lying under the dashed lin e in Figure 12
has diameter 1. Since circles in the circle packing do not ove rlap, this forces
a white side (i.e. without dashes in the ﬁgure) to have length at least 1.
For an upper bound on the length of a white side, note it is long est when
all circles in the circle packing are lined up in a row, tangen t to the two
parallel lines. In this case, when a shaded side has length 1, the length of
the white side will be the number of circles between the paral lel lines, minus
38 JESSICA S. PURCELL
Figure 12. Result of taking point of tangency to inﬁnity.
1. To ﬁnd the number of circles possible, we use an Euler chara cteristic
argument. Note there will be 2 n shaded faces in one of the polyhedra,
coming from opening up n crossing circles. These each correspond to a
single face of the triangulation of S2 used in Andreev’s theorem. Because
it is a triangulation, the number of edges equals 3 /2 the number of faces,
or 3 n. Then by an Euler characteristic argument, there are n + 2 vertices.
Recall each vertex gave a circle in our circle packing. Since two of these
circles become our parallel lines, there are n circles packed between these.
Thus the maximum length of a white side is n − 1.
Now, note that the cusp in the projection plane intersects ea ch 2–punctured
disk 2n times, each time in a meridian. Half of this meridian will com e from
the intersection of one polyhedron (the “top” half), the oth er half from the
intersection of the other polyhedron. Thus the meridian run s along two
shaded sides of rectangles. Still normalizing so each shade d side has length
1, this implies a meridian has length 2. The curve giving the h eight H
of the cusp runs along 2 n white sides of the rectangles (one for each 2–
punctured disk of intersection). The normalized height wil l be given by
H/
√
2H =
√
H/2. The height H will be minimal when each of the 2 n white
sides it runs along are of minimal length, or length 1. Thus th e minimal
normalized height is √n.
Similarly, the height H will be maximal when each white side is of max-
imal length, or length n − 1. Thus the maximal normalized height is√
n(n − 1). □
6.1.3. Hyperbolic cone deformation on S3 − L. If the normalized lengths of
the slopes on which Dehn ﬁlling was performed were suﬃcientl y large, then
Hodgson and Kerckhoﬀ showed that the Dehn ﬁlling could be rea lized by a
hyperbolic cone deformation [14]. Proposition 6.5 indicat es that to attain
these minimal normalized slope lengths, we need only ensure that there
are suﬃciently many crossings in each twist region. In parti cular, by [14],
provided √cj ≥ 10.6273, or provided that there are at least 113 crossings
per twist region of the prime, twist reduced diagram of K, then the Dehn
ﬁlling of S3 − L can be realized by a hyperbolic cone deformation.
Actually, we will see that the number of crossings in each twi st region
needs to be larger than 113 to apply Theorem 4.6. For now, howe ver, note
CUSP SHAPES UNDER CONE DEFORMATION 39
that we may ensure a hyperbolic cone deformation does exist f rom S3 − L
to S3 − K by putting conditions on the diagram of K.
