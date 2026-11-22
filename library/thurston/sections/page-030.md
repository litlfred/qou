---
doc_id: thurston
doc_title: "The Geometry and Topology of Three-Manifolds"
section_id: page-030
section_title: "Page 30"
section_number: null
pages: 30-30
source_pdf: Thurston.pdf
source_sha256: 6010919ed83edd81
toc_source: undetermined
doc_brief: "The Geometry and Topology of Three-Manifolds — 33 sections: Page 1; Page 2; Page 3"
---
2.6. TRIGONOMETRY.
There is one more case in which to interpret c(X, Y ):
2.6.6.
If X is a point in Hn and Y ? a hyperplane, then
c(X, Y ) = sinh
!
d (X, Y ?)
"
i
,
where d (X, Y ?) is the oriented distance.
2.17
The proof is left to the untiring reader.
With our dictionary now complete, it is easy to derive hyperbolic trigonometric
formulae from linear algebra. To solve triangles, note that the edges of a triangle
with vertices u, v and w in H2 are U ?, V ? and W ?, where U is a vector orthogonal
to v and w, etc. To ﬁnd the angles of a triangle from the lengths, one can ﬁnd
three vectors u, v, and w with the appropriate inner products, ﬁnd a dual basis, and
calculate the angles from the inner products of the dual basis. Here is the general
formula. We consider triangles in the projective model, with vertices inside or outside
the sphere at inﬁnity. Choose vectors v1, v2 and v3 of length i or 1 representing these
points. Let ✏i = vi · vi, ✏ij = p✏i✏j and cij = c(vi, vj). Then the matrix of inner
products of the vi is
C =
2
4
✏1
✏12c12
✏13c13
✏12c12
✏2
✏23c23
✏13c13
✏23c23
✏3
3
5 .
The matrix of inner products of the dual basis {v1, v2, v3} is C−1. For our pur-
2.18
poses, though, it is simpler to compute the matrix of inner products of the basis
Thurston — The Geometry and Topology of 3-Manifolds
21
