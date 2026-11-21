---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction"
section_id: sec-005-4-combinatorics-of-the-torus-at-infinity
section_title: "Combinatorics of the torus at infinity"
section_number: 4
pages: 6-10
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
toc_source: outline
doc_brief: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction — 29 sections: Front matter; Introduction; Conjugacy in SL(2,Z) and the Farey"
---
Combinatorics of the torus at inﬁnity
The manifold Vϕ is naturally homeomorphic to the interior of a compact manifold with
boundary, denoted by Vϕ and deﬁned as a bundle over the circle with ﬁber T −δ,
where δ is a regular neighborhood of the puncture.
Geometry & Topology 10 (2006)
Canonical triangulations
1245
R D
 1
1
0
1

L D
 1
0
1
1

Figure 2
The torus at inﬁnity of the manifold Vϕ is the boundary of Vϕ, namely a topological
torus. The links of the vertices of the tetrahedra ∆i provide a tessellation A of the torus
at inﬁnity into topological triangles. In this section we investigate the combinatorics of
A.
Each vertex of A corresponds to an edge of Vϕ shared by a few consecutive tetrahedra
∆i. This edge in turn corresponds to a Farey vertex shared by a few consecutive Farey
triangles. The union of all the Farey triangles adjacent to a given vertex v forms a fan.
If v arises as a vertex of triangles visited by the oriented line D, one of the following
two things must happen right after D enters the fan: either D makes a Right, then
a number of Lefts (possibly 0), then a Right and leaves the fan; or the same is true,
exchanging Right and Left.
Therefore, the vertices of A correspond exactly to the subwords of Ωof the form RL∗R
or LR∗L (where ∗≥0). Each such subword actually corresponds to two vertices of A,
because the edges of the tetrahedra ∆i have two ends.
Moreover, each tetrahedron ∆i, having four vertices, contributes exactly four triangles
to A. By looking at a vertex (puncture) of the cover (R2∖Z2) × R of T × R with
embedded ∆i, one checks (Figure 3) that each of the four triangles has exactly one vertex
not shared with any of the other three: we call this vertex the apex and the opposite
edge the base. The four bases form a broken line of four segments which is a closed
curve running around the puncture, and the four apices point alternatively up and down
in the R–factor. Such chains of four triangles must be stacked on top of one another
while respecting the previously described combinatorics of the vertices. The result is
shown in Figure 4, where the underlying word Ωwas chosen to be . . . R4L4R4L4 . . .
Geometry & Topology 10 (2006)
1246
Franc¸ois Gu´eritaud and David Futer
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
Third remark
Proving Theorem 1.1 by the method outlined in the Introduction
amounts to realizing Figure 4 geometrically in the plane by Euclidean triangles, making
same-layer angles with identical labels equal (Lemma 6.2 will make this statement more
precise).
Fourth remark
The convention is that the pair of edges of ∆i that does not get
identiﬁed into one edge is labeled zi: so zi is the label at the apex (in the sense of
Figure 3). Equivalently, if a tetrahedron is seen as a diagonal exchange, zi is the label
common to the appearing and disappearing edges. The other edge pairs are labeled
in such a way that in each triangle the letters x, y, z appear clockwise in that order.
Therefore, if ei is a Farey edge and p (resp. q) its right (resp. left) end for the transverse
orientation, the dihedral angle of the tetrahedron ∆i at the edge of slope p (resp. q) is
xi (resp. yi).
Geometry & Topology 10 (2006)
Canonical triangulations 1247

N
N

y
: rw 0 |! INE ole
x y x ______~__-~y xe—yp
zy" ve 71* va 1

Figure 4: The tessellation A

Fifth remark The tetrahedra A; are naturally indexed in Z/mZ. The letters R and L
live naturally on the pleated surfaces, or between the tetrahedra A;. In Figure 4 and
henceforth, the i-th layer is colored in grey if and only if the letters just before and
just after Aj; are different (here i = 2,6,...). Such indices i are called hinge indices,
because they are at the hinge between two nonempty subwords R? and L1. Hinge
tetrahedra (the associated A;) will play an important role later on.

Sixth remark While the fundamental domain of Figure 4 is supposed to have a

Geometry & Topology 10 (2006)
1248
Franc¸ois Gu´eritaud and David Futer
horizontal length of four triangles (see Figure 3), we notice a horizontal period of length
only two. This corresponds to the “hyperelliptic” involution of the once-punctured
ﬁber torus (rotation of 180◦around the puncture, central in SL2(Z) and therefore
well-deﬁned on Vϕ). This will simplify many of our computations.
Seventh remark The valence of a vertex s corresponding to a subword RLnR or LRnL
of Ω(where n ≥0) is 2n+4. This is because exactly n+2 Farey triangles are adjacent
to the corresponding rational vs; each such Farey triangle deﬁnes a triangulated surface
(with an edge of slope vs), and each such surface contributes exactly two segments
issuing from s in A.
