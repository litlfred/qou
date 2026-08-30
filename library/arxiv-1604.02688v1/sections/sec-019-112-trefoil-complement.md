---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-019-112-trefoil-complement
section_title: "Trefoil complement"
section_number: 11.2
pages: 35-36
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
has a 2-tetrahedron triangulationT with gluing equation/holonomy coeﬃcients given by:


1 2 2 2 1 2
1 0 0 0 1 0
0 0 −1 1 0 0
1 0 −4 4 −1 0


36 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
Hence, summing over edge 2, the 3D-index is
IT(xµ +yλ) =
∑
k∈Z
J∆(k +y, 0,−x− 4y)J∆(x + 4y,k−y, 0)
=
∑
k
qkI∆(x + 4y,k +y)(−q1/2)−x−4yI∆(x + 4y,k−x− 5y)
=
∑
k′
qk′
(−q1/2)−x−6yI∆(m,k′)I∆(m,k′−x− 6y)
=
∑
(−q1/2)−x−6yδ0,−x−6y =δ0,x+6y.
where we putk′ =k +y and m =x + 4y and used the quadratic identity.
Note thatIT(γ) is non-trivial exactly whenγ is a multiple of the boundary curve−6µ +λ
of the essential annulus (and Möbius strip) in the trefoil knot exterior.
11.3. T2× I. There is a unique triangulation ofT 2×I with 3 tetrahedra. Regina’s isomor-
phism signature of the triangulation is ‘dLQacccbjkg’. This triangulation turns out to be
1-eﬃcient and has the following gluing equation/holonomy coeﬃcients (from SnapPy):


1 2 2 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1 1
0 0 0 0 0 1 1 0 0
−1 0 0 0 1 0 0 0 1
0 0 0 1 0 0 0 −1 0
0 0 0 0 0 1 −1 0 0


Because both this triangulation and the solid torus triangulation have a degree one edge,
the computation is very similar to that of Example 11.1.
Let ω = (x1µ1 +y1λ1,x 2µ2 +y2λ2). Then
IT(ω)(q) =
∑
k2∈Z
qk2J∆(k2−y1, 0, 0)J∆(x2,y 1,x 1 +y2)J∆(x1−y2,−x2,y 1)
=J∆(k2−y1, 0, 0)J∆(x2,y 1,x 1 +y2)qy1
∑
k2∈Z
qk2−y1J∆(k2−y1, 0, 0) = 0,
since
∑
𝓁∈Z
q𝓁J∆(𝓁, 0, 0) =
∑
𝓁∈Z
I∆(−𝓁, 0)q𝓁 =
∑
𝓁∈Z
I∆(0,𝓁 )q𝓁 =I(0,q,q ) = (qq−1;q)∞
(q)∞;q = 0.
