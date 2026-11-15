---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-016-17-representable-functors
section_title: "Representable Functors"
section_number: 1.7
pages: 29-30
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
to a functor
(1.7.1)
YC(C) : Cop →Set,
YC(C) := HomC(−, C).
Explicitly, the functor YC(C) sends an object D ∈C to the set YC(C)(D) :=
HomC(D, C), and a morphism ψ : D0 →D1 in C goes to the function
YC(C)(ψ) := HomC(ψ, idC) : HomC(D1, C) →HomC(D0, C).
Now suppose we are given a morphism φ : C0 →C1 in C. There is a morphism
of functors (a natural transformation)
(1.7.2)
YC(φ) := HomC(−, φ) : YC(C0) →YC(C1).
Consider the category Fun(Cop, Set), whose objects are the functors F : Cop →
Set, and whose morphisms are the morphisms of functors η : F0 →F1. There is a
set-theoretic diﬃculty here: the sets of objects and morphisms of Fun(Cop, Set) are
too big (unless C is a small category), and this is not a U-category. Hence we must
enlarge the universe, as mentioned in Subsection 1.1.
Deﬁnition 1.7.3. The Yoneda functor of the category C is the functor
YC : C →Fun(Cop, Set)
described by formulas (1.7.1) and (1.7.2).
Theorem 1.7.4 (Yoneda Lemma). The Yoneda functor YC is fully faithful.
See [102, Section III.2] or [76, Section 1.4] for a proof. The proof is not hard,
but it is very confusing.
A functor F : Cop →Set is called representable if there is an isomorphism of
functors η : F
≃
−→YC(C) for some object C ∈C. Such an object C is said to
represent the functor F. The Yoneda Lemma says that YC is an equivalence from
29
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
C to the category of representable functors. Thus the pair (C, η) is unique up to a
unique isomorphism (if it exists). Note that the isomorphism of sets ηC : F(C)
≃
−→
YC(C)(C) gives a special element ˜η ∈F(C) such that ηC(˜η) = idC.
Dually, any object C ∈C gives rise to a functor
(1.7.5)
Y∨
C(C) : C →Set,
Y∨
C(C) := HomC(C, −).
A morphism φ : C0 →C1 in C induces a morphism of functors
(1.7.6)
Y∨
C(φ) := HomC(φ, −) : Y∨
C(C1) →Y∨
C(C0).
Deﬁnition 1.7.7. The dual Yoneda functor of the category C is the functor
Y∨
C : Cop →Fun(C, Set)
described by formulas (1.7.5) and (1.7.6).
Theorem 1.7.8 (Dual Yoneda Lemma). The dual Yoneda functor Y∨
C is fully
faithful.
This is also proved in [102, Section III.2] and [76, Section 1.4].
A functor F : C →Set is called corepresentable if there is an isomorphism of
functors η : F
≃
−→Y∨
C(C) for some object C ∈C. The object C is said to corepresent
the functor F. The dual Yoneda Lemma says that the functor Y∨
C is an equivalence
from Cop to the category of corepresentable functors. The identity automorphism
idC corresponds to a special element ˜η ∈F(C).
