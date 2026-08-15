---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-015-102-degrees-of-index-terms
section_title: "Degrees of index terms"
section_number: 10.2
pages: 29-30
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
I([S]) in theq-series for the 3D-index is given by the expression
d(S) =d(S∗) =−χ(S∗) +δ(S∗),
30 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
where S∗ is the minimal positive coset representative for[S] =S + T. ThenS∗ is a normal
class with at most two quadrilateral types in each tetrahedron, and
d(S∗) =−χ(S∗) +
∑
i
piqi,
where pi,qi≥ 0 are the numbers of quadrilaterals forS∗ in theith tetrahedron, andχ(S∗)
denotes the formal Euler characteristic ofS∗.
Lemma 10.8. Let S∈Q(T; Z) be a Q-normal class and let˜S be the embedded generalised
normal surface ˜S corresponding toS∗. Then
d(S) =−χ( ˜S) +
∑
i
(piqi−pi−qi + gcd(pi,qi)),
wherepi,qi≥ 0 are the numbers of quadrilaterals forS∗ in theith tetrahedron.
Hence d(S)≥− χ( ˜S) with equality if and only if ˜S is a “special” embedded generalised
normal surface, i.e. in each tetrahedron one of the coeﬃcientspi or qi is either 0 or 1.
Proof. We can choose a generalised angle structure onT with vanishing rotational peripheral
holonomy by Proposition A.2, and use this to compare the Euler characteristic of˜S with the
formal Euler characteristic ofS∗, using Proposition A.4 and Deﬁnition A.6 from Appendix
A.
In both cases we get corner terms of(formal angles)/2π which add to1 for each vertex.
Moreover the number of edges in˜S is the same as forS∗, but the number of disks is reduced
from ∑
i(pi +qi) to ∑
i gcd(pi,pi). So χ( ˜S) = χ(S∗) +∑(gcd(pi,qi)−pi−qi). Hence
d(S∗) =−χ(S∗) +∑
ipiqi =−χ( ˜S) +∑
i(piqi−pi−qi + gcd(pi,qi)).
The ﬁnal result now follows from the observation that for any integersp,q≥ 0 we have
• pq−p−q + gcd(p,q ) = 0 if p or q is 0, and otherwise
• pq−p−q + gcd(p,q )≥pq−p−q + 1 = (p− 1)(q− 1)≥ 0 with equality if and only
if p or q is 1.
□
Remark 10.9. A very similar function is studied in [FKB08, Section 4.1].
Remark 10.10. We will be particularly interested in terms in the 3D-index sum which have
non-positive degrees.
