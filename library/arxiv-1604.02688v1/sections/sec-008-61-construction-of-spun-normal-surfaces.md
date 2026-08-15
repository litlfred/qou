---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-008-61-construction-of-spun-normal-surfaces
section_title: "Construction of spun normal surfaces"
section_number: 6.1
pages: 11-13
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
construction of a spun normal surface from solutions to the Q-matching equations following
[DG12] and [Til08]. (This approach goes back to lectures of W. Thurston and was used by
J. Weeks in SnapPea.)
For a spun normal surface, there is a ﬁxed pattern of normal arcs in each ideal triangle,
consisting of three inﬁnite families of parallel arcs (one at each corner). Further there is a
well-deﬁned “middle” interval in each edge of the triangle separating two of these families.
The union of these three intervals with 3 normal arcs form a hexagon, as described in [DG12].
Figure 5. The hexagon H has three arcs which are normal arcs and three
arcs (labelled by double lines) that are not normal arcs and represent the
"middle" intervals.
12 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
Next consider the arc pattern on the boundary of a tetrahedron: Along each edge, there
is an integer “shear” or “shift” parameter which speciﬁes how the adjacent arc patterns ﬁt
together, and we choose a sign convention as shown in Figure 6 below (as viewed from outside
the tetrahedron).
Figure 6. A shift of -3 from Hr to Hl. (In general, shearing parameters
measure the oﬀset from right to left as viewed from outside the tetrahedron.)
We require that the sum of shear parameters along the three edges meeting at a vertex
is zero. This means that there is an inﬁnite family of parallel normal triangles at each
tetrahedron vertex, and also implies that the shear parameters on opposite edges are equal.
With our sign convention, quad coordinates(a,b,c ) for quad typesqA:01:23,qA:02:13,qA:03:12
in a tetrahedron correspond to shear parameters(c−b,a−c,b−a) along the edges of the
tetrahedron facingqA:01:23,qA:02:13,qA:03:12. (Figure 7 below shows the case of two quads of
type qA:01:23, separating vertices 0, 1 from vertices 2, 3.)
Figure 7. With two quads at the bottom edge of the left hexagon and top
edge of the right hexagon, we have a shear of +2 along the edge between. The
right ﬁgure gives all of the shearing coordinates on the tetrahedron.
THE 3D-INDEX AND NORMAL SURF ACES 13
Nowthereisauniquewaytogluetogetherthearcpatternsintwotetrahedrameetingalong
a common face, as the middle intervals in the faces must match up. The arc patterns from
all the tetrahedra in the triangulation then ﬁt together consistently (without any shearing)
around an edge class if and only the sum of the shear parameters over all edges in the edge
class vanishes. These conditions are precisely the Q-matching equations.
