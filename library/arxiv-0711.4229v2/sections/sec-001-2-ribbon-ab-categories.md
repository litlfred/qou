---
doc_id: arxiv-0711.4229v2
doc_title: "MODIFIED QUANTUM DIMENSIONS AND RE-NORMALIZED LINK INVARIANTS"
section_id: sec-001-2-ribbon-ab-categories
section_title: "Ribbon Ab-categories"
section_number: 2
pages: 2-2
source_pdf: 0711.4229v2.pdf
source_sha256: 2e6cc61069016627
toc_source: outline
doc_brief: "MODIFIED QUANTUM DIMENSIONS AND RE-NORMALIZED LINK INVARIANTS — In this paper we give a re-normalization of the Reshetikhin-Turaev quantum invariants of links, by modiﬁed quantum dimensions."
---
We describe the concept of a ribbon Ab-category (for details see [9]). A tensor category C
is a category equipped with a covariant bifunctor ⊗: C × C →C called the tensor product,
a unit object I, an associativity constraint, and left and right unit constraints such that the
Triangle and Pentagon Axioms hold. When the associativity constraint and the left and right
unit constraints are all identities we say the category C is a strict tensor category. By Mac
Lane’s coherence theorem any tensor category is equivalent to a strict tensor category.
A tensor category C is said to be an Ab-category if for any pair of objects V, W of C the set
of morphisms Hom(V, W) is an additive abelian group and the composition and tensor product
of morphisms are bilinear.
Let C be a (strict) ribbon Ab-category, i.e. a (strict) tensor Ab-category with duality, a
braiding and a twist.
Composition of morphisms induces a commutative ring structure on
End(I). This ring is called the ground ring of C and denoted by K. For any pair of objects
V, W of C the abelian group Hom(V, W) becomes a left K-module where the action is deﬁned by
kf = k ⊗f where k ∈K and f ∈Hom(V, W). An object V of C is simple if End(V ) = K IdV .
We denote the braiding in C by cV,W : V ⊗W →W ⊗V and duality morphisms in C by
bV : I →V ⊗V ∗,
b′
V : I →V ∗⊗V,
dV : V ∗⊗V →I,
d′
V : V ⊗V ∗→I.
The trace of any endomorphism f ∈End(V ) of an object V of C is deﬁned by
trC(f) = d′
V ◦(f ⊗Id∗
V ) ◦bV ∈End(I) = K .
Deﬁne dimC : Ob(C) →K by dimC(V ) = trC(IdV ). We call dimC(V ) the dimension of V .
