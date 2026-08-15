---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-004-31-gluing-equations
section_title: "Gluing equations"
section_number: 3.1
pages: 5-6
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
triangulation contained in Thurston’s gluing equations (compare [Thu77, Chapter 4]), while
also including notation for normal disks in a tetrahedron. First, in each tetrahedron there
are three pairs of opposite edges, which are disjoint from the three quadrilateral disks from
normal surface theory. We label these quadrilaterals by the pair of edges they face, as
in Regina [Bur]; Figure 1 shows the quads qA = qA:01:23, q′
A = qA:02:13, q′′
A = qA:03:12 in
a tetrahedron labelled A. As our discussion unfolds the quadrilaterals will be the focus,
however we also provide a labelling for the triangular disks for completeness:tA:j refers the
the triangle in tetrahedronA that cuts oﬀ vertexj.
Figure 1. The labelling of the 3 quadrilateral disk types of tetrahedronA.
Left: qA =qA:01:23, centre:q′
A =qA:02:13, right:q′′
A =qA:03:12.
Central to the construction of Thurston’s gluing equations is the observation that edges
in each tetrahedron form equivalence classes in the triangulation. In Thurston’s notes, a set
of logarithmic equations is associated to then edge classes of the triangulation. First, we
associate a complex tetrahedral parameterzj to the 01, 23 edges in tetrahedronj,z′
j = 1
1−zj
to the 02, 13 edges andz′′
j = zj−1
zj
to the 03, 12 edges.
Then we can build the followingedge equations:
∑
j
(
ai,j log(zj) +bi,j log(z′
j) +ci,j log(z′′
j )
)
= 0 + 2π
√
−1 for i∈{ 1,...,n }, (10)
where ai,j,bi,j,ci,j record the number of times the edges opposite quadsqj,q′
j,q′′
j of tetra-
hedron j appear in theith edge class. (Our convention is that arg(zj), arg(z′
j), arg(z′′
j )∈
(−π,π ].)
Note that the tetrahedral parameters also satisfy the relation
log(zj) + log(z′
j) + log(z′′
j ) =π
√
−1. (11)
6 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
We can also build2r cusp equationsusing the same tetrahedral parameters:
∑
j
(
ai,j log(zj) +bi,j log(z′
j) +ci,j log(z′′
j )
)
= 0 +π
√
−1 for i∈{n + 1,...,n + 2r}, (12)
however hereai,j,bi,j,ci,j record the number of times a peripheral curve winds anti-clockwise
(or minus the number of clockwise times) around the edges opposite the quadsqj,q′
j,q′′
j in
tetrahedron j.
The coeﬃcients in the edge and cusp equations deﬁne a(n + 2r)× 3n gluing matrix
[ai,j bi,j ci,j], which is also given by thegluing_equations() function in SnapPy [CDW].
Throughout the paper, we will write Ei for the vector of coeﬃcients in theith edge
equation, and we will also label the cusp equation coeﬃcients coming from thekth cusp by
Mk and Lk and the corresponding curvesµk and λk where it proves convenient.
3.2. Generalisedanglestructures. Consideringtheimaginarypartsofabovegluingequa-
tions allows us to deﬁne an angle structure on the triangulation. If we deﬁne□ to be the
set of quad types in a triangulationT, then ageneralised angle structureon T is a function
α : □→ R which assigns an “angle”α(q)∈ R to the pair of edges opposite a quadq and
satisﬁes the set of equations:
α(qj) +α(q′
j) +α(q′′
j ) =π for j∈{ 1,...,n } (13)
and ∑
j
(
ai,jα(qj) +bi,jα(q′
j) +ci,jα(q′′
j )
)
= 2π for i∈{ 1,...,n } (14)
whereai,j,bi,j,ci,j are deﬁned above. Astrict angle structuresatisﬁes the additional condition
that α(q)> 0 for all quadsq and asemi angle structuresatisﬁesα(q)≥ 0.
