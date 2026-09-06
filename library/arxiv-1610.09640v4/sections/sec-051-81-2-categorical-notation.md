---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-051-81-2-categorical-notation
section_title: "2-Categorical Notation"
section_number: 8.1
pages: 143-147
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
morphisms of functors (i.e. natural transformations). The language and notation
of ordinary category theory that we used so far is not adequate for this purpose.
Therefore we will now introduce notation from the theory of2-categories. (We will
not give a deﬁnition of a2-category here; but it is basically the structure ofCat
that is mentioned below.) For more details on2-categories the reader can look at
[102] or [171, Section 1].
Consider the setCat of all categories. The set-theoretical aspects are neglected,
as explained in Subsection 1.1. (Brieﬂy, the precise solution is this:Cat is the set
of all U-categories; so Cat is a subset of a bigger Grothendieck universe, sayV, and
it is aV-category.)
The set Cat is the set of objects of a2-category. This means that inCat there
are two kinds of morphisms:1-morphisms between objects, and 2-morphisms be-
tween 1-morphisms. There are several kinds of compositions, and these have several
properties. All this will be explained below.
Suppose C0, C1,... are categories, namely objects of Cat. The 1-morphisms
between them are the functors. The notation is as usual:F : C0→C1 denotes a
functor.
Suppose F,G : C0 →C1 are functors. The 2-morphisms from F to G are
the morphisms of functors (i.e. the natural transformations), and the notation is
η: F ⇒G. The double arrow is the distinguishing notation for 2-morphisms.
When specializing to an objectM ∈C0 we revert to the single arrow notation,
namely ηM : F (M)→G(M) is the corresponding morphism inC1. The diagram
depicting this is
C0
F
""
G
==
η


C1
We shall refer to such a diagram as a2-diagram.
Each object (category) C has its identity 1-morphism (functor) IdC : C→C.
Each 1-morphism F has its identity 2-morphism (natural transformation) idF :
F⇒F.
Now we consider compositions. For functors there is nothing new: given functors
F1 : C0→C1 and F2 : C1→C2, their composition, that we now callhorizontal
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
143
Derived Categories | Amnon Yekutieli | 14 Apr 2019
composition, is the functorF2◦F1 : C0→C2. The diagram is
C0
F1 //
F2◦F1
88C1
F2 // C2
Thiscanbeviewedasacommutative 1-diagram, orasashorthandforthe 2-diagram
C0
F1 //
F2◦F1
;;C1
F2 //
id


C2
in which id is the identity2-morphism ofF2◦F1.
The complication begins with compositions of 2-morphisms. Suppose we are
given 1-morphisms Fi,Gi : Ci−1 →Ci and 2-morphisms ηi : Fi ⇒Gi. In a
diagram:
C0
F1
""
G1
==
η1


C1
F2
""
G2
==
η2


C2
The horizontal compositionis the morphism of functorsη2◦η1 :F2◦F1⇒G2◦G1.
The diagram is
C0
F2◦F1
$$
G2◦G1
::
η2◦η1


C2
Exercise 8.1.1. For an objectM∈C0, give an explicit formula for the morphism
(η2◦η1)M : (F2◦F1)(M)→(G2◦G1)(M)
in the categoryC2.
Suppose we are given 1-morphisms E,F,G : C0 →C1, and 2-morphisms
ζ:E⇒F and η:F⇒G. The diagram depicting this is
C0
E

F
//
G
II
ζ


η


C1
The vertical compositionof ζand ηis the 2-morphism η∗ζ: E→G. Notice the
new symbol for this operation. The corresponding diagram is
C0
E
$$
G
::η∗ζ


C1
Exercise 8.1.2. For an objectM∈C0, give an explicit formula for the morphism
(η∗ζ)M :E(M)→G(M) in the categoryC1.
144
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Something intricate occurs in the situation shown in the next diagram.
C0
E1

F1
//
G1
II
ζ1


η1


C1
E2

F2
//
G2
II
ζ2


η2


C2
It turns out that
(η2∗ζ2)◦(η1∗ζ1) = (η2◦η1)∗(ζ2◦ζ1)
as morphismsE2◦E1⇒G2◦G1. This is called theexchange property.
Exercise 8.1.3. Prove the exchange property.
Just like abstract categories, we can talk about triangulated categories. There is
the 2-category TrCatof all (K-linear) triangulated categories. The objects here are
the triangulated categories (K, T); the 1-morphisms are the triangulated functors
(F,τ); and the2-morphisms are the morphisms of triangulated functorsη. This is
what we are going to use later in this section.
8.2. FunctorCategories. Inthissubsectionweisolateapartof 2-categorytheory.
This simpliﬁes the discussion greatly. All set theoretical issues (sizes of sets) are
neglected. As before, this can be treated by introducing a bigger universe.
Deﬁnition 8.2.1.Given categories C and D, let Fun(C, D) be the category whose
objects are the functorsF : C→D. Given objects F,G ∈Fun(C, D), the mor-
phisms η: F ⇒G in Fun(C, D) are the morphisms of functors, i.e. the natural
transformations.
For the caseD = Set this concept was already mentioned in Subsection 1.7.
In terms of the2-category Cat from the previous subsection,C and D are objects
of Cat; the objects of Fun(C, D) are 1-morphisms in Cat; and the morphisms of
Fun(C, D) are 2-morphisms in Cat. Thus we made a “reduction of order”, from2 to
1, by passing fromCat to Fun(C, D).
Suppose G : C′→C and H : D→D′are functors. There is an induced functor
(8.2.2) Fun(G,H ) : Fun(C, D)→Fun(C′, D′)
deﬁned byF(G,H )(F ) :=H◦F◦G.
Proposition 8.2.3. If G and H are equivalences, then the functorFun(G,H ) in
(8.2.2) is an equivalence.
Exercise 8.2.4. Prove Proposition 8.2.3.
Recall that for a categoryC and a multiplicatively closed set of morphismsS⊆C
we denote byCS the localization. It comes with the localization functorQ : C→CS,
which is the identity on objects. See Deﬁnition 6.1.2.
For a category E let E×⊆E be the category of isomorphisms; it has all the
objects, but its morphisms are just the isomorphisms inE.
Deﬁnition 8.2.5.Given categories C and E, a multiplicatively closed set of mor-
phisms S ⊆C, and a functor F : C →E, we say that F is localizable to S if
F (S)⊆E×. We denote by FunS(C, E) the full subcategory of Fun(C, E) on the
functors that are localizable toS.
Here is a useful formulation of the universal property of localization of categories
(see Deﬁnition 6.1.2). Recall that a functor is an isomorphism of categories iﬀ it is
an equivalence that is bijective on sets of objects.
145
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proposition 8.2.6. Let C and E be categories, and letS⊆C be a multiplicatively
closed set of morphisms. Then the functor
Fun(Q, IdE) : Fun(CS, E)→FunS(C, E)
is an isomorphism of categories.
Exercise 8.2.7. Prove Proposition 8.2.6.
By deﬁnition a bifunctorF : C×D→E is a functor from the product category
C×D. See Subsection 1.6. It will be useful to retain both meanings; so we shall
write
(8.2.8) BiFun(C×D, E) := Fun(C×D, E),
where in the ﬁrst expression we recall thatC×D is a product.
The next proposition describes bifunctors in a non-symmetric fashion.
Proposition 8.2.9. Let C, D and E be categories. There is an isomorphism of
categories
Ξ : Fun(C×D, E)→Fun(C, Fun(D, E))
with the following formula: for a functorF : C×D→E, the functor
Ξ(F ) : C→Fun(D, E)
is Ξ(F )(C) :=F (C,−).
Exercise 8.2.10. Prove Proposition 8.2.9.
Proposition 8.2.11. Let C and D be categories, and let S⊆C and T⊆D be
multiplicatively closed sets of morphisms. Then S×T is a multiplicatively closed
set of morphisms inC×D, and the canonical functor
Θ : ( C×D)S×T→CS×DT
is an isomorphism of categories.
Proof. It is clear thatS×T⊆C×D is closed under compositions. Let’s spell out
how the functorΘ arises. The functor
QS×T : C×D→(C×D)S×T
is universal for functorsF : C×D→E that invert S×T; namely functorsF such
that F (s,t )∈E×for alls∈S and t∈T. Since the functor
QS×QT : C×D→CS×DT
inverts S×T, we get the functorΘ. We will prove that the functorQS×QT has
the same universal property asQS×T; this will imply thatΘ is an isomorphism.
Consider an arbitrary categoryE. Invoking Propositions 8.2.9 and 8.2.6 we get
a commutative diagram
(8.2.12) Fun(CS×DT, E)
Fun(QS×QT,IdE)

∼= // Fun(CS, Fun(DT, E))
∼= // FunS(C, FunT(D, E))
f.f. emb.

Fun(C×D, E) Ξ
∼=
// Fun(C, Fun(D, E))
in which the right vertical arrow is a fully faithful embedding. Take any functorF
in the bottom left corner of (8.2.12), and letF′:= Ξ(F ), which lives in the bottom
right corner. NowF′belongs to the top right corner of (8.2.12) iﬀF′(s)(t)∈E×for
alls∈S andt∈T. ButF′(s)(t) =F (s,t ), so this happens iﬀF inverts S×T. □
146
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Denominator sets were introduced in Deﬁnition 6.2.14.
Proposition 8.2.13.In the situation of Proposition8.2.11, the following two con-
ditions are equivalent:
(i) The multiplicatively closed sets S⊆C and T⊆D are left (resp. right)
denominator sets.
(ii) The multiplicatively closed setS×T⊆C×D is a left(resp. right) denom-
inator set.
Exercise 8.2.14. Prove Proposition 8.2.13.
