---
doc_id: arxiv-q-alg-9709040v1
doc_title: "Deformation quantization of Poisson manifolds"
section_id: sec-036-62-diﬀerential-forms-on-conﬁguration-spaces
section_title: "Diﬀerential forms on conﬁguration spaces"
section_number: 6.2
pages: 22-23
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
toc_source: inferred
doc_brief: "Deformation quantization of Poisson manifolds — 75 sections: Front matter; Plans; Star-products"
---
The space C2,0 (the Eye) is homotopy equivalent to the standard circle S1 ≃R/2πZ. Moreover, one of
its boundary components, the space C2 = C2, is naturally S1. The other component of the boundary is the
union of two closed intervals (copies of C1,1) with identiﬁed end points.
Deﬁnition. An angle map is a smooth map φ : C2,0−→R/2πZ ≃S1 such that the restriction of φ to
C2 ≃S1 is the angle measured in the anti-clockwise direction from the vertical line, and φ maps the whole
upper interval C1,1 ≃[0, 1] of the Eye, to a point in S1.
We will denote φ([(x, y)]) simply by φ(x, y) where x, y ∈H ⊔R, x̸ = y. It follows from the deﬁnition
that dφ(x, y) = 0 if x stays in R.
For example, the special map φh used in the formula in section 2, is an angle map. In the rest of the
paper (except of the comments 9.5 and 9.8) we can use any φ, not necessarily harmonic.
We are now prepared for the analytic part of the universal formula. Let Γ be an admissible graph with
n vertices of the ﬁrst type, m vertices of the second type and with 2n + m −2 edges. We deﬁne the weight
of graph Γ by the following formula:
22
WΓ :=
n
Y
k=1
1
(#Star(k))!
1
(2π)2n+m−2
Z
C
+
n,m
^
e∈EG
dφe .
Let us explain what is written here. The domain of integration C
+
n,m is a connected component of Cn,m
which is the closure of conﬁgurations for which points qj, 1 ≤j ≤m on R are placed in the increasing order:
q1 < . . . < qm .
The orientation of Confn,m is the product of the standard orientation on the coordinate space Rm ⊃
{(q1, . . . , qm)| qj ∈R}, with the product of standard orientations on the plane R2 (for points pi ∈H ⊂R2).
The group G(1) is even-dimensional and naturally oriented because it acts freely and transitively on complex
manifold H. Thus, the quotient space Cn,m = Confn,m/G(1) carries again a natural orientation.
Every edge e of Γ deﬁnes a map from Cn,m to C2,0 or to C1,1 ⊂C2,0 (the forgetting map). Here we
consider inclusion C1,1 in C2,0 as the lower interval of the Eye. The pullback of the function φ by the map
Cn,m−→C2,0 corresponding to edge e is denoted by φe.
Finally, the ordering in the wedge product of 1-forms dφe is ﬁxed by enumeration of the set of sources
of edges and by the enumeration of the set of edges with a given source.
The integral giving WΓ is well-deﬁned because it is an integral of a smooth diﬀerential form over a
compact manifold with corners.
