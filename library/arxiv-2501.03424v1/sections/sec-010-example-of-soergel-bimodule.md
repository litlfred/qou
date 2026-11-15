---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials"
section_id: sec-010-example-of-soergel-bimodule
section_title: "Example of Soergel bimodule"
section_number: null
pages: 7-8
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
toc_source: outline
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials — This paper presents an exposition of Soergel bimodules, the categoriﬁcation of Hecke alge- bras, and their applications to various topics in"
---
Example of Soergel bimodule
Consider the polynomial ring R = k[x, y, z] where k is a ﬁeld not of characteristic 2, and consider
the action of S3 on R, characterized by simple reﬂections s and r, where
s · µ(x, y, z) = µ(y, x, z)
and
r · µ(x, y, z) = µ(x, z, y).
Hence Rs is the polynomial ring k[x + y, xy, z], and Rr is k[x + y + z, xy + xz + yz, xyz]. We take
deg(x, y, z) = 2. Then R(1) is R shifted down by 1, which we obtain by declaring the degree of each
polynomial reduced by one. Speciﬁcally, if B = L
i∈Z Bi is a Z-graded object, we declare
B(m) =
M
i∈Z
B(m)i =
M
i∈Z
Bm+i.
Then the Z-graded R-bimodule R is a Soergel bimodule8.
Have you ever wondered, ”What are the morphisms like in the category of Soergel bimodules?”?
To satisfy this musing, we take for granted that any Soergel bimodule is graded free as a left or
right R-module, and the assumption that morphisms between Soergel bimodules are homogenous
with degree 0. Formally, we describe
HomSBim(B, B′) = HomR-gbim(B, B′)
where
HomSBim(B, B′) ≃HomSBim(B, B′(k)).
Notice how this juxtaposes Bott-Samelson bimodules, which are not closed under grading shifts, as
SBim is. To do some housekeeping, we introduce the category of Bott-Samelson bimodules, BSBim,
as a monoidal category which is not closed under grading shifts. Hence morphisms B →B′ in this
category are characterized
HomBSBim(B, B′) =
M
k∈Z
HomR-gbim(B, B′(k))
7
as a graded vector space, where the RHS summands are the spaces of homogenous bimodule maps
of degree k.
Recall what it means to be an indecomposable object M in an additive category A. Speciﬁcally,
if M is indecomposable, then it cannot be expressed as a direct sum
M = M ′ ⊕M ′′,
