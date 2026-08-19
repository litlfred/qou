---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-018-11-some-examples
section_title: "Some examples"
section_number: 11
pages: 35-35
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
In this section we give some examples of index computations for ideal triangulations with
2 tetrahedra, taken from the census of triangulations described in Section 12 below.
11.1. Solid torus. The (open) solid torus has a 1-eﬃcient triangulationT by 2 tetrahedra
with isomorphism signature ‘cMcabbgds’, and gluing equation/holonomy coeﬃcient matrix
(from SnapPy) given by:


2 1 2 2 2 2
0 1 0 0 0 0
0 1 0 0 −1 0
0 1 0 0 0 2


(Here the peripheral curvesµ,λ correspond to the meridian and longitude for the unknot in
S3.) Summing over integer weightsk on edge 2 gives the 3D-index
IT(xµ +yλ) =
∑
k∈Z
qkJ∆(0,k +x +y, 0)J∆(0,−x, 2y)
=J(0,−x, 2y)q−x−y
∑
k∈Z
qkJ(0,k, 0) = 0
since
∑
k∈Z
qkJ∆(0,k, 0) =
∑
k∈Z
I∆(0,k )qk =I(0,q,q ) = (qq−1;q)∞
(q)∞;q = 0
using equation (2).
It follows that the 3D-indexvanishes identicallyfor all 118753 1-eﬃcient ideal triangula-
tions of the solid torus with at most 6 tetrahedra, since we have checked that these are all
connected to T by 2-3, 3-2, 0-2 and 2-0 moves preserving 1-eﬃciency.
