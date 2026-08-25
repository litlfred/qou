---
doc_id: arxiv-2403.00360v2
doc_title: "CAUSAL FERMION SYSTEMS AND OCTONIONS"
section_id: sec-005-24-the-associative-multiplication-algebras-of-o
section_title: "The Associative Multiplication Algebras of O"
section_number: 2.4
pages: 7-8
source_pdf: 2403.00360v2.pdf
source_sha256: b0764ca18a83a84f
doc_brief: "CAUSAL FERMION SYSTEMS AND OCTONIONS — We compare the structures and methods in the theory of causal fermion systems with approaches to fundamental physics based on division algebras, in par- ticular"
---
means that the algebra is not representable as a matrix algebra (with the standard
matrix product). The algebra generated from the composition of left (and/or right)
actions of O on itself, however, is associative, since each such left (right) action corre-
sponds to a linear operator (endomorphism). Suppose that a,x are elements of some
algebra A, and define:
La[x] :=ax, R a[x] :=xa, ∀a,x∈ A.
It is clear that La and Ra denote linear operator corresponding to left and right mul-
tiplication of x∈ A by a∈ A, respectively. These maps send the element x∈ A to
some other element y∈ A, and thus La and Ra∈ End(A). The mappings a7→ La
1Another option is to consider the split octonions algebra, which is not a normed division algebra,
and does contain projectors. The split octonions differ from the octonions in that its quadratic form
has a split signature (4, 4) whereas the octonions quadratic form has a positive-definite signature (8, 0).
8 F. FINSTER, N.G. GRESNIGT, J.M. ISIDRO, A. MARCIAN `O, C.F. PAGANINI, AND T.P. SINGH
and a7→ Ra do not correspond to algebra homomorphisms. Instead, via composi-
tion each generates an associative algebra referred to as the associative multiplication
algebra.
Note in particular, that for a non-associative algebras such as O,
LaLb[x] =a(bx) ̸= Lab[x] = (ab)x,
RaRb[x] = (xb)a ̸= Rab[x] =x(ab), ∀a,b,x ∈ O.
We denoted by OL and OR, the left and right associative multiplication algebras of
octonions respectively, which we will henceforth refer to simply as the left (right)
multiplication algebra 2 These linear maps preserve the quadratic relations ⟨x,y⟩ =
1
2(xy +yx), where x,y∈ O
LxLy1 +LyLx1 = 2⟨x,y⟩1 =RxRy1 +RyRx1.
Since La (Ra) correspond to linear operators, they can be represented as 8 × 8 real
matrices acting on the vector space O written as a column vector.
Within OL, one finds the following identities [34, 59]:
Le1Le2Le3Le4Le5Le6x =Le7x,
...LebLeaLeaLec....x =−...LebLec....x,
...LeaLeb...x =−...LebLea...,
where a,b,c = 1,..., 7.
The non-associativity of O means that OL (OR) contains genuinely new maps which
are not captured by O itself. For example, e3(e4(e6 +e2))̸=y(e6 +e2) for any y∈ O.
There are a total of 64 distinct left-acting real linear maps from O to itself, and these
(due to the given identities above) provide a faithful representation of the real Clifford
algebra Cℓ(0, 6). Furthermore, any left (right) adjoint action can always be rewritten
as a right (left) adjoint action, so that OL = OR [34].
For the complex octonions, C⊗ O, the left (right) multiplication algebra is like-
wise complexified and becomes the complex Clifford algebra Cℓ(6), having complex
dimension 64.
