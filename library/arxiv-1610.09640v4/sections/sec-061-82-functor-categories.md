---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-061-82-functor-categories
section_title: "Functor Categories"
section_number: 8.2
pages: 145-147
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
This simpliﬁes the discussion greatly. All set theoretical issues (sizes of sets) are
neglected. As before, this can be treated by introducing a bigger universe.
Deﬁnition 8.2.1. Given categories C and D, let Fun(C, D) be the category whose
objects are the functors F : C →D. Given objects F, G ∈Fun(C, D), the mor-
phisms η : F ⇒G in Fun(C, D) are the morphisms of functors, i.e. the natural
transformations.
For the case D = Set this concept was already mentioned in Subsection 1.7.
In terms of the 2-category Cat from the previous subsection, C and D are objects
of Cat; the objects of Fun(C, D) are 1-morphisms in Cat; and the morphisms of
Fun(C, D) are 2-morphisms in Cat. Thus we made a “reduction of order”, from 2 to
1, by passing from Cat to Fun(C, D).
Suppose G : C′ →C and H : D →D′ are functors. There is an induced functor
(8.2.2)
Fun(G, H) : Fun(C, D) →Fun(C′, D′)
deﬁned by F(G, H)(F) := H ◦F ◦G.
Proposition 8.2.3. If G and H are equivalences, then the functor Fun(G, H) in
(8.2.2) is an equivalence.
Exercise 8.2.4. Prove Proposition 8.2.3.
Recall that for a category C and a multiplicatively closed set of morphisms S ⊆C
we denote by CS the localization. It comes with the localization functor Q : C →CS,
which is the identity on objects. See Deﬁnition 6.1.2.
For a category E let E× ⊆E be the category of isomorphisms; it has all the
objects, but its morphisms are just the isomorphisms in E.
Deﬁnition 8.2.5. Given categories C and E, a multiplicatively closed set of mor-
phisms S ⊆C, and a functor F : C →E, we say that F is localizable to S if
F(S) ⊆E×.
We denote by FunS(C, E) the full subcategory of Fun(C, E) on the
functors that are localizable to S.
Here is a useful formulation of the universal property of localization of categories
(see Deﬁnition 6.1.2). Recall that a functor is an isomorphism of categories iﬀit is
an equivalence that is bijective on sets of objects.
145
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proposition 8.2.6. Let C and E be categories, and let S ⊆C be a multiplicatively
closed set of morphisms. Then the functor
Fun(Q, IdE) : Fun(CS, E) →FunS(C, E)
is an isomorphism of categories.
Exercise 8.2.7. Prove Proposition 8.2.6.
By deﬁnition a bifunctor F : C × D →E is a functor from the product category
C × D. See Subsection 1.6. It will be useful to retain both meanings; so we shall
write
(8.2.8)
BiFun(C × D, E) := Fun(C × D, E),
where in the ﬁrst expression we recall that C × D is a product.
The next proposition describes bifunctors in a non-symmetric fashion.
Proposition 8.2.9. Let C, D and E be categories. There is an isomorphism of
categories
Ξ : Fun(C × D, E) →Fun(C, Fun(D, E))
with the following formula: for a functor F : C × D →E, the functor
Ξ(F) : C →Fun(D, E)
is Ξ(F)(C) := F(C, −).
Exercise 8.2.10. Prove Proposition 8.2.9.
Proposition 8.2.11. Let C and D be categories, and let S ⊆C and T ⊆D be
multiplicatively closed sets of morphisms. Then S × T is a multiplicatively closed
set of morphisms in C × D, and the canonical functor
Θ : (C × D)S × T →CS × DT
is an isomorphism of categories.
Proof. It is clear that S × T ⊆C × D is closed under compositions. Let’s spell out
how the functor Θ arises. The functor
QS × T : C × D →(C × D)S × T
is universal for functors F : C × D →E that invert S × T; namely functors F such
that F(s, t) ∈E× for all s ∈S and t ∈T. Since the functor
QS × QT : C × D →CS × DT
inverts S × T, we get the functor Θ. We will prove that the functor QS × QT has
the same universal property as QS × T; this will imply that Θ is an isomorphism.
Consider an arbitrary category E. Invoking Propositions 8.2.9 and 8.2.6 we get
a commutative diagram
(8.2.12)
Fun(CS × DT, E)
Fun(QS × QT,IdE)

∼
=
/ Fun(CS, Fun(DT, E))
∼
= / FunS(C, FunT(D, E))
f.f. emb.

Fun(C × D, E)
Ξ
∼
=
/ Fun(C, Fun(D, E))
in which the right vertical arrow is a fully faithful embedding. Take any functor F
in the bottom left corner of (8.2.12), and let F ′ := Ξ(F), which lives in the bottom
right corner. Now F ′ belongs to the top right corner of (8.2.12) iﬀF ′(s)(t) ∈E× for
all s ∈S and t ∈T. But F ′(s)(t) = F(s, t), so this happens iﬀF inverts S × T.
□
146
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Denominator sets were introduced in Deﬁnition 6.2.14.
Proposition 8.2.13. In the situation of Proposition 8.2.11, the following two con-
ditions are equivalent:
(i) The multiplicatively closed sets S ⊆C and T ⊆D are left (resp. right)
denominator sets.
(ii) The multiplicatively closed set S × T ⊆C × D is a left (resp. right) denom-
inator set.
Exercise 8.2.14. Prove Proposition 8.2.13.
