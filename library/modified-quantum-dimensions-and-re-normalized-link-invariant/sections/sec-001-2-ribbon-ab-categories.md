---
doc_id: modified-quantum-dimensions-and-re-normalized-link-invariant
doc_title: "Modified quantum dimensions and re-normalized link invariants"
section_id: sec-001-2-ribbon-ab-categories
section_title: "Ribbon Ab-categories"
section_number: 2
pages: 3-4
source_pdf: modified-quantum-dimensions-and-re-normalized-link-invariants.pdf
source_sha256: 5447f6d5f5d6c8d7
toc_source: outline
doc_brief: "Modified quantum dimensions and re-normalized link invariants — 8 sections: Front matter; Introduction; Ribbon Ab-categories"
---
We describe the concept of a ribbon Ab-category (for details see [Tur94]). A tensor category C is
a category equipped with a covariant bifunctor ⊗: C × C →C called the tensor product, a unit
object I, an associativity constraint, and left and right unit constraints such that the triangle and
pentagon axioms hold. When the associativity constraint and the left and right unit constraints
are all identities we say that the category C is a strict tensor category. By Mac Lane’s coherence
theorem any tensor category is equivalent to a strict tensor category.
A tensor category C is said to be an Ab-category if for any pair of objects V , W of C the set
of morphisms Hom(V, W) is an additive abelian group and the composition and tensor product
of morphisms are bilinear.
Let C be a (strict) ribbon Ab-category, i.e. a (strict) tensor Ab-category with duality, a
braiding and a twist. Composition of morphisms induces a commutative ring structure on End(I).
This ring is called the ground ring of C and denoted by K. For any pair of objects V, W of C the
abelian group Hom(V, W) becomes a left K-module where the action is deﬁned by kf = k ⊗f
where k ∈K and f ∈Hom(V, W). An object V of C is simple if End(V ) = K IdV .
We denote the braiding in C by cV,W : V ⊗W →W ⊗V and duality morphisms in C by
bV : I →V ⊗V ∗,
b′
V : I →V ∗⊗V,
dV : V ∗⊗V →I,
d′
V : V ⊗V ∗→I.
N. Geer, B. Patureau-Mirand and V. Turaev
The trace of any endomorphism f ∈End(V ) of an object V of C is deﬁned by
trC(f) = d′
V ◦(f ⊗Id∗
V ) ◦bV ∈End(I) = K.
Deﬁne dimC : Ob(C) →K by dimC(V ) = trC(IdV ). We call dimC(V ) the dimension of V .
