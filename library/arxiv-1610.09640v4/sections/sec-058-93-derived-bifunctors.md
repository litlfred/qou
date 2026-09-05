---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-058-93-derived-bifunctors
section_title: "Derived Bifunctors"
section_number: 9.3
pages: 171-175
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
tors of triangulated bifunctors. The deﬁnitions and results are very similar to the
single-argument case. For the sake of simplicity, we shall mostly ignore the trans-
lation functors and the translation isomorphisms; enough was said about them in
the previous subsection.
The next setup will be used throughout this subsection.
Setup 9.3.1. The following are given:
•Triangulated categoriesK1, K2 and E.
•A triangulated bifunctorF : K1×K2→E.
•Denominator sets of cohomological originS1⊆K1 and S2⊆K2.
We writeDi := (Ki)Si, and Qi : Ki→Di are the localization functors.
The localized categoryDi := (Ki)Si is triangulated, and the localization functor
Qi : Ki→Di is triangulated. On the product categories we get a functor
Q1×Q2 : K1×K2→D1×D2.
Before embarking on the deﬁnitions of the derived bifunctors, we want to intro-
duce the relevant categories of functors. These are the bifunctor variants of what
we had in Subsection 8.2.
Deﬁnition 9.3.2.We denote byLinBiFun(K1×K2, E) the category whose objects
are the linear bifunctorsF : K1×K2→E. The morphisms are the obvious ones.
This is a linear category. Actually, this category is the same as the category
LinFun(K1⊗K2, E) of linear functorsF : K1⊗K2→E, only with the extra infor-
mation that the source is a product category.
Deﬁnition 9.3.3.We denote byTrBiFun(K1×K2, E) the category whose objects
are theK-linear triangulated bifunctors(F,τ1,τ2) : K1×K2→E. The morphisms
are those of T-additive bifunctors.
There is a functor
(9.3.4) TrBiFun(K1×K2, E)→LinBiFun(K1×K2, E)
that forgets (τ1,τ2). It is a faithful additive functor.
Suppose Ui : K′
i→Ki are triangulated functors between triangulated categories.
We get an induced additive functor
(9.3.5) Fun(U1×U2, IdE) : TrBiFun(K1×K2, E)→TrBiFun(K′
1×K′
2, E)
The formula isF↦→F◦(U1×U2).
Lemma 9.3.6. If the functors U1 and U2 are equivalences, then the functor in
(9.3.5) is an equivalence.
171
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. This is basically the same as the proof of Lemma 8.4.4. □
As in Deﬁnition 8.2.5 we denote by
TrBiFunS1×S2(K1×K2, E)⊆TrBiFun(K1×K2, E)
the full subcategory on the triangulated bifunctorsF such thatF (S1×S2)⊆E×.
Lemma 9.3.7. The functor
Fun(Q1×Q2, IdE) : TrBiFun(D1×D2, E)→TrBiFunS1×S2(K1×K2, E)
is an isomorphism of categories.
Proof. This is basically the same as the proof of Lemma 8.4.6, when combined
with the isomorphism of triangulated categories(K1×K2)S1×S2→D1×D2 from
Proposition 8.2.11. □
We are ready to talk about derived bifunctors.
Deﬁnition 9.3.8.Under Setup 9.3.1, atriangulated right derived bifunctor ofF
with respect toS1×S2 is a pair(RF,ηR), where
RF : D1×D2→E
is a triangulated bifunctor, and
ηR :F⇒RF◦(Q1×Q2)
is a morphism of triangulated bifunctors, such that the following universal property
holds:
(R) Given a pair(G,θ), consisting of a triangulated bifunctorG : D1×D2→E
and a morphism of triangulated bifunctorsθ: F ⇒G◦(Q1×Q2), there
is a unique morphism of triangulated bifunctorsµ: RF ⇒G such that
θ= (µ◦idQ1×Q2)∗ηR.
Here is a diagram showing property (R):
(9.3.9) K1×K2
F //
Q1×Q2

E
D1×D2
RF
::
ηR


G
MM
θ

µ ’
Proposition 9.3.10. If a triangulated right derived bifunctor exists, then it is
unique up to a unique isomorphism.
Proof. This is just like the proof of Proposition 8.4.8. We leave the small changes
to the reader. □
Existence in general is like Theorem 8.4.9, but a bit more complicated.
Theorem 9.3.11. Under Setup 9.3.1, assume there are full triangulated subcate-
gories J1⊆K1 and J2⊆K2 with these two properties:
(a) If φ1 : I1→J1 is a morphism inJ1∩S1 and φ2 : I2→J2 is a morphism
in J2∩S2, then
F (φ1,φ2) :F (I1,I 2)→F (J1,J 2)
is an isomorphism inE.
(b) For everyp∈{1, 2}and every objectMp∈Kp, there exists a morphism
ρp :Mp→Ip in Sp with targetIp∈Jp.
172
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Then the triangulated right derived bifunctor
(RF,ηR) : D1×D2→E
of F with respect toS1×S2 exists. Moreover, for every pair of objectsI1∈J1 and
I2∈J2 the morphism
ηR
I1,I2 :F (I1,I 2)→RF (I1,I 2)
in E is an isomorphism.
In applications we will see that eitherJ1 = K1 or J2 = K2; namely we will only
need to resolve in the second or in the ﬁrst argument, respectively.
Proof. It will be convenient to change notation. Forp = 1, 2 let’s deﬁneK′
p := Jp,
S′
p := K′
p∩Sp and D′
p := (K′
p)S′
p. The localization functors areQ′
p : K′
p→D′
p. The
inclusions areUp : K′
p→Kp, and their localizations are the functorsVp : D′
p→Dp.
By Lemma 8.3.8 the functorsVp are equivalences.
The situation is depicted in these diagrams. We have this commutative diagram
of products of triangulated functors between products of triangulated categories:
(9.3.12) K′
1×K′
2
U1×U2 //
Q′
1×Q′
2

K1×K2
Q1×Q2

D′
1×D′
2
V1×V2 // D1×D2
The arrow V1×V2 is an equivalence. Diagram (9.3.12) induces a commutative
diagram of linear categories:
(9.3.13) TrBiFun(K′
1×K′
2, E) TrBiFun(K1×K2, E)
Fun(U1×U2,Id)oo
TrBiFunS′
1×S′
2
(K′
1×K′
2, E)
f.f.emb
OO
TrBiFunS1×S2(K1×K2, E)
f.f.emb
OO
equiv
Fun(U1×U2,Id)oo
TrBiFun(D′
1×D′
2, E)
Fun(Q′
1×Q′
2,Id) isom
OO
TrBiFun(D1×D2, E)
Fun(V1×V2,Id)
equiv
oo
Fun(Q1×Q2,Id)isom
OO
According to Lemmas 9.3.6 and 9.3.7, the arrows in the diagram above that are
marked “isom” or “equiv” are isomorphisms or equivalences, respectively. By deﬁ-
nition the arrows marked “f.f. emb” are fully faithful embeddings.
We know that Sp⊆Kp are left denominator sets. Therefore (see Proposition
8.2.13) S1×S2 ⊆K1×K2 is a left denominator set. Condition (a) of Theorem
9.3.11 says thatF sends morphisms inS′
1×S′
2 to isomorphisms inE. Condition (b)
there says that there are enough right(K′
1×K′
2)-resolutions in K1×K2.
Thus we are in a position to use the abstract Theorem 8.3.3. It says that there
is an abstract right derived functor(RF,ηR) : D1×D2→E. However, going over
the proof of Theorem 8.3.3, we see that all constructions there can be made within
the triangulated setting, namely in diagram (9.3.13) instead of in diagram (8.3.11).
Therefore RF is an object of the category in the bottom right corner of (9.3.13),
and the morphismηR : F ⇒RF◦(Q1×Q2) is in the category in the top right
corner of (9.3.13). □
We now treat left derived bifunctors. Due to the similarity to the right derived
functors, we give only a few details here.
173
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 9.3.14.Under Setup 9.3.1, atriangulated left derived bifunctor ofF
with respect toS1×S2 is a pair(LF,ηL), where
LF : D1×D2→E
is a triangulated bifunctor, and
ηL : LF◦(Q1×Q2)⇒F
is a morphism of triangulated bifunctors, such that the following universal property
holds:
(L) Given a pair(G,θ), consisting of a triangulated bifunctorG : D1×D2→E
and a morphism of triangulated bifunctorsθ: G◦(Q1×Q2)⇒F, there
is a unique morphism of triangulated bifunctorsµ: G⇒LF such that
θ=ηL∗(µ◦idQ1×Q2).
Proposition 9.3.15.If a triangulated left derived bifunctor exists, then it is unique
up to a unique isomorphism.
Proof. This is the opposite of Proposition 9.3.10, and we leave it to the reader to
make the adjustments. □
Theorem 9.3.16. In the situation of Deﬁnition9.3.14, assume there are full tri-
angulated subcategoriesP1⊆K1 and P2⊆K2 with these two properties:
(a) If φ1 :P1→Q1 is a morphism inP1∩S1 and φ2 :P2→Q2 is a morphism
in P2∩S2, then
F (φ1,φ2) :F (P1,P 2)→F (Q1,Q 2)
is an isomorphism inE.
(b) For everyi∈{1, 2}and every objectMi∈Ki, there exists a morphism
ρi :Pi→Mi in Si with targetPi∈Pi.
Then the triangulated left derived bifunctor
(LF,ηL) : D1×D2→E
of F with respect toS1×S2 exists. Moreover, for every pair of objectsP1∈P1 and
P2∈P2 the morphism
ηL
P1,P2 : LF (P1,P 2)→F (P1,P 2)
in E is an isomorphism.
Exercise 9.3.17. Prove Theorem 9.3.16. (Hint: This is the opposite of Theorem
9.3.11. The proof is analogous.)
In applications we will see that eitherP1 = K1 or P2 = K2; namely we will only
need to resolve in the second or in the ﬁrst argument, respectively.
There are more specialized deﬁnitions of triangulated derived bifunctors whose
sources are categories of DG modules, like Deﬁnitions 8.4.16 and 8.4.26. We leave
them to the reader.
Remark 9.3.18.Deriving triangulated bifunctors that are contravariant in one or
two arguments involves passage to opposite categories; see Deﬁnition 9.2.9. Propo-
sition 7.6.3 tells us that whenKop
i ⊆K(Ai, Mi)op are full triangulated subcategories,
the sets Sop
i of quasi-isomorphisms in them are of cohomological origin. So we are
still within the conditions of Setup 9.3.1, and Theorems 9.3.11 and 9.3.16 can be
applied. We leave it to the reader to work out the details in the various cases. How-
ever, the important case of the bifunctorHom(−,−) will be given a full treatment
in Subsection 12.2.
174
Derived Categories | Amnon Yekutieli | 14 Apr 2019
10. Resolving Subcategories of K(A, M)
In this section we are back in the more concrete setting:A is a DG ring, andM is
an abelian category, both over the commutative base ringK; see Convention 1.2.4.
