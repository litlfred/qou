---
doc_id: arxiv-math-0110119v1
doc_title: "Idempotents of the Hecke algebra become Schur functions in the skein of the annulus"
section_id: sec-001-2-young-diagrams-and-symmetric-functions
section_title: "Young diagrams and symmetric functions"
section_number: 2
pages: 2-3
source_pdf: 0110119v1.pdf
source_sha256: 4904a86e8a340f59
toc_source: inferred
doc_brief: "Idempotents of the Hecke algebra become Schur functions in the skein of the annulus — The Hecke algebra Hn contains well known idempotents Eλ which are indexed by Young diagrams with n cells."
---
Young diagrams and symmetric functions
2.1
Young diagrams
We consider partitions of non-negative integers where the summands are in non-
strictly decreasing order. We consider partitions to be equal if they diﬀer only
by a number of zero-summands at the end.
A Young diagram is a graphical depiction of a partition. A partition λ =
(λ1, λ2, . . . , λk) becomes a ﬂush-left arrangement of square cells with λ1 cells in
the ﬁrst row, λ2 cells in the second row, ... and λk cells in the k-th row.
We deﬁne λ ⊂µ for partitions λ = (λ1, . . . , λk) and µ = (µ1, . . . , µm) if λi ≤µi
for all 1 ≤i ≤k (where µi = 0 for m < i ≤k). This relation coincides in the
graphical depiction with λ being a subset of µ.
We deﬁne |λ| to be the number of cells of λ, i.e. for λ = (λ1, . . . , λk) we have
|λ| = λ1 + · · · + λk.
2.2
Symmetric functions
Following Macdonald [8], we consider the polynomial ring in variables x1, . . . , xn.
For a partition λ = (λ1, . . . , λk) with k ≤n we deﬁne
sλ(x1, . . . , xn) = det(x
λj+n−j
i
)1≤i,j≤n
det(xn−j
i
)1≤i,j≤n
.
This quotient is a symmetric polynomial in x1, . . . , xn. In the inverse limit of
the polynomial rings Z[x1, . . . , xn] for n →∞we can deﬁne an element sλ,
called the λ-Schur function for any Young diagram λ. This element specializes
to sλ(x1, . . . , xn) when we set xi = 0 for all i ≥n+1 provided that λ has at most
n non-zero summands.
The most basic Young diagrams are on the one hand a row diagram with, say,
n cells and on the other hand a column diagram with, say, k cells. One can check
that s(n) is the n-th complete symmetric function hn and that s(1k) is the k-th
elementary symmetric function ek.
2
3
The skein Rn
