---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-020-114-a-toroidal-example
section_title: "A toroidal example"
section_number: 11.4
pages: 36-37
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
signature ‘cPcbbbdei’ is not 1-eﬃcient. In fact it gives a manifold containing an incom-
pressible torus which splits the manifold in two Seifert ﬁbres piecesSFS [D2(2, 1)(3, 1)] and
THE 3D-INDEX AND NORMAL SURF ACES 37
SFS [A2(2, 1)]. The gluing equation/holonomy coeﬃcients (from SnapPy) are given by:


1 1 0 1 0 1
1 1 2 1 2 1
0 −1 0 1 0 0
0 0 2 0 0 0


Hence, summing over edge 1, the 3D-index is given by
IT(xµ +yλ) =
∑
k∈Z
qkJ∆(k,k−x, 2y)J∆(k +x, 0,k ) =
∑
k∈Z
I∆(x, 2y−k)I∆(−x,−k).
If x = 0,y = 0 then the above sum∑
kI∆(0,−k)2 is divergent, as expected by Theorem
5.2, since each term withk≤ 0 has degree 0.
However forx⁄= 0 the sum converges, and experimentation suggests the sum simpliﬁes to
the following geometric series:
IT(xµ +yλ) = (−1)xq|x|(|y+x/2|+1/2)
(1−q|x|) , for x⁄= 0.
Putting
xµ +yλ =aµ + (b−a/2)λ =a(µ−λ/2) +bλ =a¯µ +β¯λ
we have symmetriesIT(a¯µ +b¯λ) = IT(±a¯µ +±b¯λ) for a⁄= 0 (by the duality and triality
identities) and experimentally it seems that
IT(a¯µ +b¯λ) = (−1)aqa(b+1/2)
1−qa , for a> 0,b≥ 0.
