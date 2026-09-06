---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-049-76-the-opposite-derived-category-is-triangulated
section_title: "The Opposite Derived Category is Triangulated"
section_number: 7.6
pages: 140-143
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
a DGK-ring A and aK-linear abelian category M. In Subsection 5.6 we put a
canonical triangulated structure on the opposite homotopy category K(A, M)op.
This structure is such that the ﬂip functor
Flip : K(A, M)op→K(Aop, Mop) = K(A, M)ﬂip
is an isomorphism of triangulated categories. Here, unlike in Subsection 5.6, we are
omitting the overline decoration fromFlip. In the current subsection we push this
triangulated structure to the opposite derived categoryD(A, M)op.
But ﬁrst let us present two types of full subcategoriesK⊆K(A, M) that are
triangulated, and alsoKop⊆K(A, M)op is triangulated.
For any boundedness condition⋆(see Deﬁnition 7.3.1), we know thatK⋆(A, M)
is a full triangulated subcategory ofK(A, M). The notation K⋆(A, M)op refers to
the opposite category of K⋆(A, M); thus, K⋆(A, M)op is the full subcategory of
K(A, M)op on the DG modules satisfying the boundedness condition⋆.
Proposition7.6.1. For every boundedness condition⋆, the subcategoryK⋆(A, M)op
is triangulated inK(A, M)op.
Proof. Let’s write K := K⋆(A, M) and Kop := K⋆(A, M)op. Deﬁne Kﬂip
:= Flip( Kop) ⊆K(Aop, Mop). According to Theorem 3.9.16(2) we know that
Kﬂip = K−⋆(Aop, Mop), where−⋆is the reversed boundedness condition. Thus
Kﬂip is a full triangulated subcategory ofK(Aop, Mop). By deﬁnition of the trian-
gulated structure onK(A, M)op we conclude thatKop is triangulated. □
Let N⊆M be a thick abelian subcategory. ThenKN(M), see Deﬁnition 7.4.4,
is a full triangulated subcategory ofK(M). This is just like Proposition 7.4.5. The
opposite categoryKN(M)op, on the same set of objects, is a full additive subcategory
of K(M)op.
140
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proposition 7.6.2. Let N⊆M be a thick abelian subcategory. ThenKN(M)op is
a full triangulated subcategory ofK(M)op.
Proof. Let’s writeK := KN(M). Then Kﬂip := Flip(Kop)⊆K(Mop) is, by Theorem
3.9.16(4), the category KNop(Mop). Thus Kﬂip is a triangulated subcategory. By
deﬁnition of the triangulated structure onK(M)op we conclude that Kop is trian-
gulated. □
Later, in Section 10, we will see that severalresolving subcategoriesare also full
triangulated subcategories ofK(A, M)op. These are relevant to Theorems 8.4.9 and
8.4.23 below.
Taking intersections, we get more full triangulated subcategories ofK(A, M)op.
Recall that S(A, M) is the set of quasi-isomorphisms inK(A, M). Let S(A, M)op
bethesetofquasi-isomorphismsin K(A, M)op. Notethatbeingaquasi-isomorphism
has nothing to do with the triangulated structure. Since a morphismψin K(A, M)
is a quasi-isomorphism iﬀOp(ψ) is a quasi-isomorphism inK(A, M)op, we have a
bijection Op : S(A, M)
≃
− →S(A, M)op. We know that S(A, M) is a left and right
denominator set inK(A, M), by Proposition 7.1.1. Therefore, by Proposition 6.2.4,
S(A, M)op is left and right denominator set inK(A, M)op. We need to know more:
Proposition 7.6.3. Let Kop be a full triangulated subcategory ofK(A, M)op, and
deﬁneSop := Kop∩S(A, M)op, the set of quasi-isomorphisms inKop. Then:
(1) Sop is a denominator set of cohomological origin inKop.
(2) The localized categoryDop := (Kop)Sop has a unique triangulated structure
s.t. the localization functorQop : Kop→Dop is a triangulated functor.
Proof. On the ﬂip side, i.e. inK(Aop, Mop), we know that the set of quasi-iso-
morphisms S(Aop, Mop) is a denominator set of cohomological origin. But by The-
orem 3.9.16(4) we haveS(A, M)op = Flip−1(
S(Aop, Mop)
{
, so this too is a denomi-
nator set of cohomological origin. Now we can use Theorem 7.1.3. □
Observe that Dop = (KS)op, by Proposition 6.1.5. The situation is summarized
by the following commutative diagram of functors:
(7.6.4) Cop
str
Pop
// //
Flip ∼=

Kop Qop
//
Flip ∼=

Dop
Flip ∼=

Cﬂip
str
Pﬂip
// // Kﬂip Qﬂip
// Dﬂip
Here C is the full subcategory ofC(A, M) on the objects ofK, andCﬂip := Flip(C)⊆
C(A, M)ﬂip = C(Aop, Mop). All these functors are bijective on objects. The vertical
ones are bijective on morphisms too. The functors marked↠ are surjective on
morphisms (i.e. they are full). The ﬁrst vertical arrow is an isomorphism of abelian
categories, and the other two vertical arrows are isomorphisms of triangulated cat-
egories.
Warning: GivenKop like in Proposition 7.6.3, there is no reason for the canonical
triangulated functor Dop→D(A, M)op to be fully faithful; see Proposition 7.1.13
for suﬃcient conditions.
Deﬁnition 7.6.5.Let K⊆K(A, M) be a full additive subcategory s.t.Kop is a
triangulated subcategory of K(A, M)op, and let S := K∩S(A, M). The category
Dop := (Kop)Sop is given the triangulated structure from Proposition 7.6.3.
For K = K(A, M) we get a triangulated structure onDop = D(A, M)op.
141
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 7.6.6.Let K ⊆K(A, M) be a full additive subcategory s.t. Kop is
a triangulated subcategory of K(A, M)op. Deﬁne D := KS and Dop := ( Kop)Sop,
where S := K∩S(A, M). Let E be some triangulated category. A contravariant
triangulated functorfrom Dto Eis, by deﬁnition, a triangulate functorF : Dop→E,
where Dop has the canonical triangulated structure from Deﬁnition 7.6.5.
142
Derived Categories | Amnon Yekutieli | 14 Apr 2019
