---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-073-104-opposite-resolving-subcategories
section_title: "Opposite Resolving Subcategories"
section_number: 10.4
pages: 182-185
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
K-injective and K-projective DG modules in K(A, M) behave in the opposite cate-
gory K(A, M)op, and then use this to prove existence of contravariant triangulated
derived functors.
Recall the ﬂipping operation from Subsections 3.9, 5.6 and 7.6.
There is an
isomorphism of DG categories
(10.4.1)
Flip : C(A, M)op
≃
−→C(A, M)ﬂip = C(Aop, Mop),
and the corresponding isomorphisms of the homotopy categories
(10.4.2)
Flip : K(A, M)op
≃
−→K(A, M)ﬂip = K(Aop, Mop)
and on the derived categories
(10.4.3)
Flip : D(A, M)op
≃
−→D(A, M)ﬂip = D(Aop, Mop).
By deﬁnition of the triangulated structure on K(A, M)op, the isomorphisms (10.4.2)
and (10.4.3) are of triangulated categories.
The objects of C(A, M) and C(A, M)op are the same, and the property of a DG
module M being acyclic is the same in both categories.
Lemma 10.4.4. A DG module M ∈C(A, M) is acyclic iﬀthe DG module
Flip(M) ∈C(Aop, Mop) is acyclic.
Proof. This follows from Theorem 3.9.16(4).
□
Lemma 10.4.5. A DG module P ∈K(A, M) is K-projective iﬀthe DG module
I := Flip(P) ∈K(Aop, Mop) is K-injective.
Proof. According to Lemma 10.4.4, the functor Flip gives a bijection between the
set of acyclic DG modules M ∈K(A, M) and the set of acyclic DG modules N :=
Flip(M) ∈K(Aop, Mop). Since the functor (10.4.2) is an equivalence, we have an
equality and an isomorphism
(10.4.6)
HomK(A,M)(P, M) = HomK(A,M)op(M, P) ∼= HomK(Aop,Mop)(N, I)
in M(K).
By Proposition 10.1.3, the DG module I is K-injective in K(Aop, Mop) iﬀfor
every acyclic DG module N ∈K(Aop, Mop) we have HomK(Aop,Mop)(N, I) = 0.
Similarly, by Proposition 10.2.3, the DG module P is K-projective in K(A, M) iﬀ
for every acyclic DG module M ∈K(A, M) we have HomK(A,M)(P, M) = 0. In view
of (10.4.6) we conclude that I is K-injective iﬀP is K-projective.
□
Here are the contravariant modiﬁcations of Theorems 10.1.20 and 10.2.15.
Setup 10.4.7. We are given:
• A full additive subcategory K ⊆K(A, M), s.t. Kop ⊆K(A, M)op is triangu-
lated. The localization of Kop at the quasi-isomorphisms in it is denoted
by Dop.
• A triangulated category E and a triangulated functor F : Kop →E.
Theorem 10.4.8. Under Setup 10.4.7, assume that K has enough K-projectives.
Then the triangulated right derived functor (RF, ηR) : Dop →E of F exists. Further-
more, for every K-projective DG module P ∈K, the morphism ηR
P : F(P) →RF(P)
in E is an isomorphism.
Proof. Let Kﬂip := Flip(Kop) ⊆K(Aop, Mop). This is a triangulated category. Its
localization w.r.t. the quasi-isomorphisms is denoted by Dﬂip.
We have isomor-
phisms of triangulated categories Flip : Kop
≃
−→Kﬂip and Flip : Dop
≃
−→Dﬂip. Let
F ﬂip := F ◦Flip−1 : Kﬂip →E. This is a triangulated functor.
182
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Since Flip sends quasi-isomorphisms to quasi-isomorphisms, and by Lemma
10.4.5, each K-projective resolution ρ : P →M of M in K goes to a K-injective
resolution Flip(ρ) : Flip(M) →Flip(P) of N := Flip(M) in Kﬂip. We are given
that K has enough K-projectives. Therefore Kﬂip has enough K-injectives.
Now we can apply Theorem 10.1.20 to deduce that the right derived functor
(RF ﬂip, ηﬂip) : Dﬂip →E of F ﬂip exists. Then
(RF, ηR) := (RF ﬂip, ηﬂip) ◦Flip : Dop →E
is a right derived functor of F.
The assertion about the morphism ηR
P is clear from the discussion above.
□
Theorem 10.4.9. Under Setup 10.4.7, assume that K has enough K-injectives.
Then the left derived functor (LF, ηL) : Dop →E of F exists. Furthermore, for
every K-injective DG module I ∈K, the morphism ηL
I : LF(I) →F(I) in E is an
isomorphism.
Proof. The same as that of the previous theorem, except that now we use Lemma
10.4.5 and Theorem 10.2.15.
□
183
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
