---
doc_id: arxiv-2411.03801v2
doc_title: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS"
section_id: sec-006-31-octahedral-decomposition
section_title: "Octahedral decomposition"
section_number: 3.1
pages: 9-11
source_pdf: 2411.03801v2.pdf
source_sha256: a7f1f6fa74cb0949
doc_brief: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS — Motivated by the conjectured asymptotics of the Kashaev invariant, Dimofte and the first author introduced a power series associated to a suitable ideal"
---
of a planar projection of a knot and the state-sum formula for its Kashaev invariant, where
the shapes of 4 tetrahedra around a crossing of the knot match with the quantum factorials
in Kashaev’s R-matrix of his invariant. This connection was discussed by D. Thurston in
relation to the Kashaev invariant and its asymptotics [Thu99], and later by Yokota [Yok02],
see also [GL11, Sec.8.2].
The algorithm consists of two steps
˚D⇝ (OD,s )⇝T˚D (8)
which we next discuss in detail.
3.1. Octahedral decomposition. Let K be a knot in S3 and D be a knot diagram of K.
Viewing D as an embedded 4-valent graph in R 2, a segment refers to an edge of the graph
and a region refers to a connected component of the complement of the graph. If we add
over/under-pass information at every crossing as usual, the graph splits up into intervals,
which we call over-arcs. Reversing all the over/under-pass information, the graph splits up
into different intervals, which we call under-arcs.
Place an ideal octahedron at every crossing as in Figure 7 (left) and add an edge joining
the top and bottom vertices so that the octahedron is divided into four tetrahedra. Then
each tetrahedron is placed at a corner and has two faces glued to adjacent tetrahedra. We
record these information by triangles and dashed lines as in Figure 7 (right). Here a triangle
represents a tetrahedron, viewed from the top. We classify the edges of an octahedron into
four types:
• a C-edge is the edge joining the top and bottom vertices;
• an R-edge is an edge lying in the equator of the octahedron;
• an O-edge (resp., U-edge) is a non-equatorial edge, transverse to the overpass (resp.,
underpass) when viewed from the top.
Note that each (outer) face of an octahedron has one R-edge, one O-edge and one U-edge.
10 STA VROS GAROUF ALIDIS AND SEOKBEOM YOON
Figure 7. An octahedron at a crossing.
A segment joins two crossings, hence two octahedra. On each side of the segment, there is
a pair of faces that face each other along the segment. See Figure 8 (left) for the alternating
case. We glue those two faces so that edges of the same type are identified. In this way,
each segment determines two face-pairings. We record them with dashed lines having signs
at the ends, shown as in Figure 8 (right). Here the sign indicates whether the face lies in
the upper or lower part of the octahedron. Then every triangle is attached with four dashed
lines: one with +, another with −, and the others with no signs. Namely, all faces of the
tetrahedra are glued. This results in an ideal cell decomposition OD of S3\ (K∪{p,q})
(withp andq two points not inK) with cells being ideal octahedra, known as the octahedral
decomposition associated with D. We refer to [KKY18] for details.
+
−
+
−
Figure 8. Two face-pairings along a segment.
When we glue octahedra, edges are identified only if they have the same type. It follows
that we can classify edges of OD into four types: C, R, O and U-edges. In addition,
• a C-edge corresponds to a crossing of D;
• an R-edge corresponds to a region of D, i.e., two R-edges are identified if and only if
they lie in the same region, viewed from the top;
• an O-edge corresponds to an over-arc ofD, i.e., two O-edges are identified if and only
if they are attached to the same over-arc;
• a U-edge corresponds to an under-arc of D, i.e., two U-edges are identified if and
only if they are attached to the same under-arc.
Note that if D has n crossings, then we have
#(tetrahedra ofOD) = 4n, #(edges ofOD) = 4n + 2
1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS 11
with n C-edges, (n + 2) R-edges, n O-edges and n U-edges.
