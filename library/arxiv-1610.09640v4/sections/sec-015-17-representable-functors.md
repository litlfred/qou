---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-015-17-representable-functors
section_title: "Representable Functors"
section_number: 1.7
pages: 29-30
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
to a functor
(1.7.1) YC(C) : Cop→Set, YC(C) := HomC(−,C ).
Explicitly, the functor YC(C) sends an object D ∈C to the set YC(C)(D) :=
HomC(D,C ), and a morphismψ:D0→D1 in C goes to the function
YC(C)(ψ) := HomC(ψ,idC) : HomC(D1,C )→HomC(D0,C ).
Now suppose we are given a morphismφ:C0→C1 in C. There is a morphism
of functors (a natural transformation)
(1.7.2) YC(φ) := HomC(−,φ) : YC(C0)→YC(C1).
Consider the category Fun(Cop, Set), whose objects are the functorsF : Cop→
Set, and whose morphisms are the morphisms of functorsη:F0→F1. There is a
set-theoretic diﬃculty here: the sets of objects and morphisms ofFun(Cop, Set) are
too big (unlessC is a small category), and this is not aU-category. Hence we must
enlarge the universe, as mentioned in Subsection 1.1.
Deﬁnition 1.7.3.The Yoneda functorof the categoryC is the functor
YC : C→Fun(Cop, Set)
described by formulas (1.7.1) and (1.7.2).
Theorem 1.7.4(Yoneda Lemma). The Yoneda functorYC is fully faithful.
See [102, Section III.2] or [76, Section 1.4] for a proof. The proof is not hard,
but it is very confusing.
A functor F : Cop→Set is called representable if there is an isomorphism of
functors η: F
≃
− →YC(C) for some object C ∈C. Such an object C is said to
representthe functorF. The Yoneda Lemma says thatYC is an equivalence from
29
Derived Categories | Amnon Yekutieli | 14 Apr 2019
C to the category of representable functors. Thus the pair(C,η) is unique up to a
unique isomorphism (if it exists). Note that the isomorphism of setsηC :F (C)
≃
− →
YC(C)(C) gives a special element˜η∈F (C) such thatηC(˜η) = idC.
Dually, any objectC∈C gives rise to a functor
(1.7.5) Y∨
C(C) : C→Set, Y∨
C(C) := HomC(C,−).
A morphismφ:C0→C1 in C induces a morphism of functors
(1.7.6) Y∨
C(φ) := HomC(φ,−) : Y∨
C(C1)→Y∨
C(C0).
Deﬁnition 1.7.7.The dual Yoneda functorof the categoryC is the functor
Y∨
C : Cop→Fun(C, Set)
described by formulas (1.7.5) and (1.7.6).
Theorem 1.7.8 (Dual Yoneda Lemma). The dual Yoneda functor Y∨
C is fully
faithful.
This is also proved in [102, Section III.2] and [76, Section 1.4].
A functor F : C→Set is called corepresentable if there is an isomorphism of
functorsη:F
≃
− →Y∨
C(C) for some objectC∈C. The objectC is said tocorepresent
the functorF. The dual Yoneda Lemma says that the functorY∨
C is an equivalence
from Cop to the category of corepresentable functors. The identity automorphism
idC corresponds to a special element˜η∈F (C).
