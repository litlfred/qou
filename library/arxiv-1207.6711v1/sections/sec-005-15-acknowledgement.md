---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-005-15-acknowledgement
section_title: "Acknowledgement"
section_number: 1.5
pages: 6-7
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
and Dylan Thurston for helpful comments.
2. Concrete triangulations
In all of the following M denotes a compact, oriented 3-manifold with (possibly empty)
boundary. Let ˆM be the space obtained from M by collapsing each boundary component of
M to a point. An ordered simplex is a simplex together with an ordering of its vertices.
Deﬁnition 2.1. An abstract triangulationT ofM is an identiﬁcation ofˆM with a space ob-
tained from a ﬁnite collection of 3-simplices by gluing together pairs of faces viaface-pairings,
i.e. aﬃne homeomorphisms. A concrete triangulation T of M is an abstract triangulation
together with a ﬁxed identiﬁcation of each 3-simplex with a standard ordered 3-simplex.
The advantage of a concrete triangulation is that each simplex inherits a vertex ordering
from the standard simplex. This extra datum gives us a concrete indexing scheme for the
GLUING EQUATIONS FOR PGL( n, C)-REPRESENTATIONS OF 3-MANIFOLDS 7
vertices and edges and allows us to concretely write down deﬁning equations for the gluing
equation variety and the Ptolemy variety. An abstract triangulation can be thought of as an
equivalence class of concrete triangulations under reordering. As we shall see, a reordering
changes the varieties by canonical isomorphisms. Hence, they only depend on the abstract
triangulation.
Note that the vertex ordering of each simplex induces an orientation, which may or may
not agree with the orientation inherited from M.
Deﬁnition 2.2. A concrete triangulation ofM is an oriented triangulation if the orientation
of each simplex agrees with the orientation ofM. A concrete triangulation of M is an ordered
triangulation if the face-pairings are order-preserving. An abstract triangulation is orderable
if it supports an ordered triangulation.
As we shall see, the shape coordinates are most conveniently expressed in terms oforiented
triangulations, whereas the Ptolemy coordinates are most conveniently expressed in terms of
ordered triangulations. Note that since M is assumed to be oriented, one can always order
the vertices making the triangulation oriented.
Remark 2.3. One can always obtain an orderable triangulations by performing a sequence
of 2-3 moves and 1-4 moves. One can do this systematically in such a way that the total
number of simplices is increased by at worst a factor of 6. Alternatively, a barycentric
subdivision always provides an ordered triangulation by ordering vertices by codimension.
A
C
B
DA
C
B
D
0 2
31
0 2
31
Figure 1. An ordered, but not oriented
triangulation of the ﬁgure 8 knot. No
vertex ordering exists making the trian-
gulation both ordered and oriented.
C
A
B
DA
C
B
D
0 2
31
0 2
31
Figure 2. An oriented, but not ordered
triangulation of the ﬁgure 8 knot sister.
The underlying abstract triangulation is
unorderable.
