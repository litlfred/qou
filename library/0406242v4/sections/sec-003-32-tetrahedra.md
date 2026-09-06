---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements FRANC¸ OIS GUÉRITAUD APPENDIX BY DA VIDFUTER"
section_id: sec-003-32-tetrahedra
section_title: "Tetrahedra"
section_number: 3.2
pages: 5-10
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
---
As before, letϕ be an element of SL2(Z) with two distinct eigenvalues in R∗
+. In the
proof of Proposition 2.1, we introduced the triangles t0, t1,... crossed by the axis D
ofϕ. In view of the above, this yields a nonbacktracking path of diagonal exchanges
between some triangulation (associated to t0) and its pushforward by ϕ (associated to
tm).
More precisely, when the oriented line D crosses an edge e of the Farey tessellation,
e comes with a transverse orientation. So we can deﬁne the top (resp. bottom)
triangulationτ+(e) (resp. τ−(e)) of the punctured torus T as being the one associated
with the Farey triangle crossed just after (resp. before) the edge e. A diagonal exchange
separates the triangulations τ−(e) and τ+(e). An ideal tetrahedron is by deﬁnition a
space diffeomorphic to an ideal hyperbolic tetrahedron (topologically it is a compact
tetrahedron with its vertices removed). We can immerse such an ideal tetrahedron ∆(e)
in T× R: the boundary of the immersed ∆(e) is made up of two pleated surfaces (top
and bottom) homotopic to T and triangulated according toτ+(e) and τ−(e) respectively
Geometry &Topology 10 (2006)
1244 Franc ¸ois Gu´eritaud and David Futer
Figure 1: Four copies of ∆(e) in the cover ( R2rZ2)× R of T× R
(Figure 1). The immersion is an embedding on the interior of ∆(e), but two pairs of
opposite edges undergo identiﬁcations.
Next, if D crosses the Farey edges ei, ei+1,... , we can glue the top of the tetrahedron
∆i := ∆(ei) onto the bottom of ∆i+1 in T× R, because τ+(ei) = τ−(ei+1). We
thus get a bi-inﬁnite stack of tetrahedra ( ∆i)i∈Z. For any nonnegative N the space
UN :=⋃N
i=−N ∆i is a strong deformation retraction of T× R. For N large enough,
UN is homeomorphic to T× [0, 1]: the only way this can fail is if all the ∆i for
−N≤ i≤ N have a common edge; but any edge of any tetrahedron ∆j is shared
by only ﬁnitely many other (consecutive) ∆i’s, because for any Farey vertexv, only
ﬁnitely many of the Farey edges ei bound triangles with v as a vertex (and these ei are
consecutive). Therefore, the space U =⋃
i∈Z ∆i is homeomorphic to T× R. If m is
the period of the word Ω, there is an orientation-preserving homeomorphism Φ of U,
acting like [ϕ] on the T –factor, that sends ∆i to ∆i+m for all i. The quotient U/Φ is a
manifold (homeomorphic to) Vϕ, naturally triangulated into m ideal tetrahedra.
Figure 2 also shows a way to interpret the standard transvection matrices R and L
directly as adjunctions of new tetrahedra (by performing diagonal exchanges on the top
faces). Similarly, to topologically triangulate a general pseudo-Anosov surface bundle,
we can always go by diagonal exchanges from some triangulation (of the surface) to its
pushforward by the monodromy map, an idea usually credited to Casson.
4 Combinatorics of the torus at inﬁnity
The manifold Vϕ is naturally homeomorphic to the interior of a compact manifold with
boundary, denoted by Vϕ and deﬁned as a bundle over the circle with ﬁber T−δ,
whereδ is a regular neighborhood of the puncture.
Geometry &Topology 10 (2006)
Canonical triangulations 1245
R D
 1 1
0 1

L D
 1 0
1 1

Figure 2
The torus at inﬁnity of the manifold Vϕ is the boundary of Vϕ, namely a topological
torus. The links of the vertices of the tetrahedra ∆i provide a tessellationA of the torus
at inﬁnity into topological triangles. In this section we investigate the combinatorics of
A.
Each vertex ofA corresponds to an edge of Vϕ shared by a few consecutive tetrahedra
∆i. This edge in turn corresponds to a Farey vertex shared by a few consecutive Farey
triangles. The union of all the Farey triangles adjacent to a given vertex v forms a fan.
If v arises as a vertex of triangles visited by the oriented line D, one of the following
two things must happen right after D enters the fan: either D makes a Right, then
a number of Lefts (possibly 0), then a Right and leaves the fan; or the same is true,
exchanging Right and Left.
Therefore, the vertices ofA correspond exactly to the subwords of Ω of the form RL∗R
or LR∗L (where∗≥ 0). Each such subword actually corresponds to two vertices of A,
because the edges of the tetrahedra ∆i have two ends.
Moreover, each tetrahedron ∆i, having four vertices, contributes exactly four triangles
toA. By looking at a vertex (puncture) of the cover ( R2rZ2)× R of T× R with
embedded ∆i, one checks (Figure 3) that each of the four triangles has exactly one vertex
not shared with any of the other three: we call this vertex the apex and the opposite
edge the base. The four bases form a broken line of four segments which is a closed
curve running around the puncture, and the four apices point alternatively up and down
in the R–factor. Such chains of four triangles must be stacked on top of one another
while respecting the previously described combinatorics of the vertices. The result is
shown in Figure 4, where the underlying word Ω was chosen to be... R4L4R4L4...
Geometry &Topology 10 (2006)
1246 Franc ¸ois Gu´eritaud and David Futer
Figure 3: The link of the puncture
(read from bottom to top). A few remarks are in order.
First remark We labeled by xi, yi, zi the angular sectors of the triangles corresponding
to the tetrahedron ∆i (in Figure 4, the subscript i is replaced by a number at the center
of the triangle, omitted after the ﬁrst few levels). Each angular sector corresponds
to a (topological) dihedral angle of ∆i. Opposite dihedral angles are equal in ideal
hyperbolic tetrahedra: this is why three different labels per level are enough (instead of
six, the total number of edges in a tetrahedron).
Second remark The design in Figure 4 of the vertices of the torus at inﬁnity, represented
as being “opened up”, is intended to emphasize the layered structure of the picture (each
layer corresponds to one tetrahedron ∆i).
Third remark Proving Theorem 1.1 by the method outlined in the Introduction
amounts to realizing Figure 4 geometrically in the plane by Euclidean triangles, making
same-layer angles with identical labels equal (Lemma 6.2 will make this statement more
precise).
Fourth remark The convention is that the pair of edges of ∆i that does not get
identiﬁed into one edge is labeled zi: so zi is the label at the apex (in the sense of
Figure 3). Equivalently, if a tetrahedron is seen as a diagonal exchange, zi is the label
common to the appearing and disappearing edges. The other edge pairs are labeled
in such a way that in each triangle the letters x, y, z appear clockwise in that order.
Therefore, if ei is a Farey edge and p (resp. q) its right (resp. left) end for the transverse
orientation, the dihedral angle of the tetrahedron ∆i at the edge of slope p (resp. q) is
xi (resp. yi).
Geometry &Topology 10 (2006)
Canonical triangulations 1247
z
x
x
x
z
z
x
z
z
z
x
z
xz
z
x
z
z x
z
z
x
z
z
z
yz
xy
x x
z
z
x
y
yy
y
z x
x
x x
x xz
x
z
yx
y
y
z
y
y
y
y
y
zz
zz yy
y
y y
y
x
L
R
R
R
L
R
xx
zyzy y
yy z
R
z
z
x
x
x
xx
L
L
L
L
L
L
R
R
R
x
x
zz y
x
x
xzx
x
x x
x
x
xx
x
x
z yy
x
x x z
z
z x
z
z
x x z
z
z
x
z
z
y
y
y
yx
y
x
x
y
z
x
z
y
x
z
x
z
yy
xx
x
zy
z
x
z z
z
y
y
3
2
0
2
3
1
1
4
4 3
2
0
2
3
1
1
4
x
zy
z
z
z z
z
y
x
z
z
y
zy
4
z
z
y
x x
z
z
y
z
yx
y
x
y
z
x
z
z
x
y
z
z
x
z
yy
xx
x
zy
y
yy
y
x
x
x x
x xz
x
y
y
z
yx
y
x
y
z
y
xx
zy
z
y
y
z
z
y
x
z
z
y
zx
Figure 4: The tessellationA
Fifth remark The tetrahedra ∆i are naturally indexed in Z/mZ. The letters R and L
live naturally on the pleated surfaces, or between the tetrahedra ∆i. In Figure 4 and
henceforth, the i–th layer is colored in grey if and only if the letters just before and
just after ∆i are different (here i = 2, 6,... ). Such indices i are called hinge indices,
because they are at the hinge between two nonempty subwords Rp and Lq. Hinge
tetrahedra (the associated ∆i) will play an important role later on.
Sixth remark While the fundamental domain of Figure 4 is supposed to have a
Geometry &Topology 10 (2006)
1248 Franc ¸ois Gu´eritaud and David Futer
horizontal length of four triangles (see Figure 3), we notice a horizontal period of length
only two. This corresponds to the “hyperelliptic” involution of the once-punctured
ﬁber torus (rotation of 180 ◦ around the puncture, central in SL2(Z) and therefore
well-deﬁned on Vϕ). This will simplify many of our computations.
Seventh remark The valence of a vertex s corresponding to a subword RLnR or LRnL
of Ω (where n≥ 0) is 2n+ 4. This is because exactly n+ 2 Farey triangles are adjacent
to the corresponding rational vs; each such Farey triangle deﬁnes a triangulated surface
(with an edge of slope vs), and each such surface contributes exactly two segments
issuing from s inA.
