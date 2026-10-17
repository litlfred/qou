---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-002-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 3-4
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
toc_source: outline
---
2.1. Tensor ideals. Let k be a ﬁeld and let C be a k−linear monoidal
category. Recall that a tensor ideal I in C is a collection of subspaces
I(X, Y ) ⊂Hom(X, Y ) for all X, Y ∈C such that for all X, Y, Z, T ∈C
(1) for α ∈I(X, Y ) and β ∈Hom(Y, Z), γ ∈Hom(Z, X) we have
α ◦γ ∈I(Z, Y ) and β ◦α ∈I(X, Z);
(2) for α ∈I(X, Y ), β ∈Hom(Z, T) we have α⊗β ∈I(X ⊗Z, Y ⊗T)
and β ⊗α ∈I(Z ⊗X, T ⊗Y ).
If I is a tensor ideal in C then one can deﬁne a new k−linear monoidal
category C′ (the quotient of C by I) as follows: the objects of C′ are the
objects of C; HomC′(X, Y ) := HomC(X, Y )/I(X, Y ); the composition
of morphisms is the same as in C (note that condition (1) ensures that
the composition is well deﬁned); the tensor product is the same as in
C (well deﬁned thanks to condition (2)).
Moreover, the identity map on the objects and morphisms induces a
canonical quotient monoidal functor C →C′.
3
It is clear that if C is rigid, pivotal, spherical, braided, symmetric
then so is C′.
