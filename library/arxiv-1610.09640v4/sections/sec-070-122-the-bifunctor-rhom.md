---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-070-122-the-bifunctor-rhom
section_title: "The Bifunctor RHom"
section_number: 12.2
pages: 223-227
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
Like in Example 9.1.11 we get a DG bifunctor
F := HomA,M(−,−) : C(A, M)op×C(A, M)→C(K).
In Deﬁnition 5.6.4 we put a triangulated structure on the opposite homotopy cat-
egory K(A, M)op. According to Theorem 9.2.16, there is an induced triangulated
bifunctor
F = HomA,M(−,−) : K(A, M)op×K(A, M)→K(K).
Postcomposing with the localization functorQ : K(K)→D(K), we obtain a trian-
gulated bifunctor
F = HomA,M(−,−) : K(A, M)op×K(A, M)→D(K).
Next we pick full additive subcategoriesK1, K2⊆K(A, M) s.t. Kop
1 ⊆K(A, M)op
and K2 ⊆K(A, M) are triangulated. In practice this choice would be by some
boundedness conditions; for instanceK1 := K−(M) or K2 := K+(M), cf. Corollaries
11.3.19 and 11.5.26 respectively. We want to construct the right derived bifunctor
of the triangulated bifunctor
F = HomA,M(−,−) : Kop
1 ×K2→D(K).
This is done in the next theorem.
Theorem 12.2.1.LetA be a DGK-ring, let M be aK-linear abelian category, and
let K1, K2⊆K(A, M) be full additive subcategories, such thatKop
1 is a full triangu-
lated subcategory ofK(A, M)op, andK2 is a full triangulated subcategory ofK(A, M).
Assume either thatK1 has enough K-projectives, or thatK2 has enough K-injectives.
Let Di denote the localization ofKi with respect to the quasi-isomorphisms in it.
Then the triangulated bifunctor
HomA,M(−,−) : Kop
1 ×K2→D(K)
has a right derived bifunctor
RHomA,M(−,−) : Dop
1 ×D2→D(K).
Moreover, ifP1∈K1 is K-projective, or ifI2∈K2 is K-injective, then the morphism
ηR
P1,I2 : HomA,M(P1,I 2)→RHomA,M(P1,I 2)
223
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in D(K) is an isomorphism.
Proof. If K2 has enough K-injectives, then we can takeJ2 := K2,inj, the full sub-
category on the K-injectives insideK2. And we takeJ1 := K1. We claim that the
conditions of Theorem 9.3.11 are satisﬁed. Condition (b) is simply the assumption
that K2 has enough K-injectives. As for condition (a): this is Lemma 12.2.2 below,
with its condition (ii).
On the other hand, ifK1 has enough K-projectives, then we can takeJ1 := K1,prj,
thefullsubcategoryontheK-projectivesinside K1. Andwetake J2 := K2. Weclaim
that the conditions of Theorem 9.3.11 are satisﬁed forJop
1 ⊆Kop
1 . Condition (b)
is simply the assumption thatK1 has enough K-projectives: a quasi-isomorphism
ρ: P →M in K1 becomes a quasi-isomorphism Op(ρ) : Op( M) →Op(P ) in
Kop
1 , and Op(P )∈Jop
1 . As for condition (a): this is Lemma 12.2.2 below, with its
condition (i).
The last assertion also follows from 12.2.2. □
Lemma 12.2.2. Suppose φ1 :Q1→P1 and φ2 :I2→J2 are quasi-isomorphisms
in C(A, M), and either of the conditions below holds:
(i) Q1 and P1 are both K-projective.
(ii) I2 and J2 are both K-injective.
Then the homomorphism
HomA,M(φ1,φ2) : HomA,M(P1,I 2)→HomA,M(Q1,J 2)
in C(K) is a quasi-isomorphism.
Proof. We will only prove the case whereQ1,P 1 are both K-projective; the other
case is very similar.
The homomorphism in question factors as follows:
HomA,M(φ1,φ2) = HomA,M(φ1, idJ2)◦HomA,M(idP1,φ2).
It suﬃces to prove that each of the factors is a quasi-isomorphism. This can be done
by a messy direct calculation, but we will provide an indirect proof that relies on
properties of the homotopy categoryK := K(A, M) that were already established.
Let K2 be the standard cone on the homomorphismφ2 : I2→J2. So K2 is
acyclic. BecauseP1 is K-projective it follows thatHomA,M(P1,K 2) is acyclic. Thus
for every integerl we have
(12.2.3) HomK(P1[−l],K 2)∼= Hl(
HomA,M(P1,K 2)
{
= 0.
Next, there is a distinguished triangle
(12.2.4) I2
φ2
−→J2
β2
−→K2
γ2
−→I2[1]
in K. Applying the cohomological functor HomK(P1[−l],−) to the distinguished
triangle (12.2.4) yields a long exact sequence, as explained in Subsection 5.2. From
it we deduce that the homomorphisms
HomK(P1[−l],I 2)→HomK(P1[−l],J 2)
are bijective for alll. Using the isomorphisms like (12.2.3) forI2 andJ2 we see that
HomA,M(idP1,φ2) : HomA,M(P1,I 2)→HomA,M(P1,J 2)
is a quasi-isomorphism.
According to Corollary 10.2.14 the homomorphismφ1 : Q1→P1 is a homo-
topy equivalence; so it is an isomorphism inK. Therefore for every integerl the
homomorphism
HomK(Q1,J 2[l])→HomK(P1,J 2[l])
224
Derived Categories | Amnon Yekutieli | 14 Apr 2019
is bijective. As above we conclude that
HomA,M(φ1, idJ2) : HomA,M(Q1,J 2)→HomA,M(P1,J 2)
is a quasi-isomorphism. □
Remark 12.2.5. Theorem 12.2.1 should be viewed as a template. It has com-
mutative and noncommutative variants, that we shall study later. And there are
geometric variants in which the source and target are categories of sheaves.
We end this section with the connection between RHom and morphisms in the
derived category.
Deﬁnition 12.2.6.Under the assumptions of Theorem 12.2.1, for DG modules
M1∈K1 and M2∈K2, and for an integeri, we write
Exti
A,M(M1,M 2) := Hi(
RHomA,M(M1,M 2)
{
∈M(K).
Exercise 12.2.7. Let A be a ring. Prove that for modulesM1,M 2∈M(A) the
K-module Exti
A(M1,M 2) deﬁned above is canonically isomorphic to the module
in the classical deﬁnition. Moreover, this is true regardless of the choices of the
subcategories K1 and K2, as long asMi∈Ki.
Corollary 12.2.8. Under the assumptions of Theorem12.2.1, there is an isomor-
phism
Ext0
A,M(−,−)
≃
− →HomD(A,M)(−,−)
of additive bifunctorsDop
1 ×D2→M(K).
Exercise 12.2.9.Prove Corollary 12.2.8. (Hint: use Theorems 10.1.13 and 10.2.9.)
12.3. The Bifunctor⊗L. Consider a DG ringA. Like in Example 9.1.10 we get
a DG bifunctor
F := (−⊗A−) : C(Aop)×C(A)→C(K).
Passing to homotopy categories, and postcomposing withQ : K(K)→D(K), we
obtain a triangulated bifunctor
F = (−⊗A−) : K(Aop)×K(A)→D(K).
Next we pick full triangulated subcategories K1 ⊆K(Aop) and K2 ⊆K(A). In
practice this choice would be by some boundedness conditions; for instanceK1 :=
C−(Aop) or K2 := C−(A), cf. Corollary 11.3.19. We want to construct the left
derived bifunctor of the triangulated bifunctor
F = (−⊗A−) : K1×K2→D(K).
This is done in the next theorem.
Theorem 12.3.1. Let A be a DGK-ring, and let K1⊆K(Aop) and K2⊆K(A)
be full triangulated subcategories. Assume that eitherK1 or K2 has enough K-ﬂat
objects. Let Di denote the localization ofKi with respect to the quasi-isomorphisms
in it. Then the triangulated bifunctor
(−⊗A−) : K1×K2→D(K)
has a left derived bifunctor
(−⊗L
A−) : D1×D2→D(K).
Moreover, if eitherP1∈K1 or P2∈K2 is K-ﬂat, then the morphism
ηL
P1,P2 :P1⊗L
AP2→P1⊗AP2
in D(K) is an isomorphism.
225
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. If K2 has enough K-ﬂats, then we can takeP2 := K2,ﬂat, the full subcategory
on the K-ﬂats insideK2. And we takeP1 := K1. We claim that the conditions of
Theorem 9.3.16 are satisﬁed. Condition (b) is simply the assumption thatK2 has
enough K-ﬂats. As for condition (a): this is Lemma 12.3.2 below, with its condition
(ii).
The other case is proved the same way (but replacing sides). The last assertion
also follows from 12.3.2. □
Lemma 12.3.2. Supposeφ1 :P1→Q1 and φ2 :P2→Q2 are quasi-isomorphisms
in C(Aop) and C(A) respectively, and either of the conditions below holds:
(i) Q1 and P1 are both K-ﬂat.
(ii) P2 and Q2 are both K-ﬂat.
Then the homomorphism
φ1⊗φ2 :P1⊗AP2→Q1⊗AQ2
in C(K) is a quasi-isomorphism.
Proof. We will only prove the lemma under condition (i); the other case is very
similar. The homomorphism in question factors as follows:
φ1⊗φ2 = (φ1⊗idP2)◦(idP1⊗φ2).
It suﬃces to prove that each of the factors is a quasi-isomorphism. This can be
done by a messy direct calculation, but we will provide an indirect proof that relies
on properties of the DG categoriesC(Aop) and C(A) that were already established.
First we shall prove thatidP1⊗φ2 is a quasi-isomorphism. LetR2 be the stan-
dard cone on the strict homomorphismφ2 : P2 →Q2. So there is a standard
triangle
(12.3.3) P2
φ2
−→Q2→R2→P2[1]
in Cstr(A), andR2 is acyclic. Applying the DG functorP1⊗A (−) to the triangle
(12.3.3), and using Theorem 4.5.5, we see that there is a standard triangle
(12.3.4) P1⊗AP2
idP1⊗φ2
−−−−−−→P1⊗AQ2→P1⊗AR2→(P1⊗AP2)[1]
in C(K). This becomes a distinguished triangle in the triangulated categoryK(K).
Thus there is a long exact sequence in cohomology associated to (12.3.4). Because
P1 is K-ﬂat it follows thatP1⊗AR2 is acyclic. We conclude thatHi(idP1⊗φ2) is
bijective for alli.
Nowweshallprovethat φ1⊗idP2 isaquasi-isomorphism. Let R1∈C(Aop)bethe
standard cone on the homomorphismφ1 :P1→Q1. It is both acyclic and K-ﬂat.
Using standard triangles like (12.3.3) and (12.3.4) we reduce the problem to showing
that R1⊗AP2 is acyclic. According to Corollary 11.4.26 and Proposition 10.3.4
there is a quasi-isomorphism˜P2→P2 in C(A) from some K-ﬂat DG module˜P2. As
already proved in the previous paragraph, sinceR1 is K-ﬂat, the homomorphism
R1⊗A ˜P2→R1⊗A P2 is a quasi-isomorphism. But R1 is acyclic and ˜P2 is K-
ﬂat, and thereforeR1⊗A ˜P2 is acyclic. We conclude thatR1⊗AP2 is acyclic, as
required. □
Remark 12.3.5. Theorem 12.3.1 should be viewed as a template. It has commu-
tative and noncommutative variants, that we will talk about later. And there are
geometric variants where the source and target are categories of sheaves.
Deﬁnition 12.3.6.Under the assumptions of Theorem 12.3.1, for DG modules
M1∈K1 and M2∈K2, and for an integeri, we write
TorA
i (M1,M 2) := H−i(M1⊗L
AM2)∈M(K).
226
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Exercise 12.3.7. Let A be a ring. Prove that for modules M1∈M(Aop) and
M2∈M(A) theK-module TorA
i (M1,M 2) deﬁned above is canonically isomorphic
to the module in classical deﬁnition. Moreover, this is true regardless of the choices
of the subcategoriesK1 and K2, as long asMi∈Ki.
Recall that the categoryD(A) admits inﬁnite direct sums.
Proposition 12.3.8. For everyM∈D(Aop) the functor
M⊗L
A (−) : D(A)→D(K)
commutes with inﬁnite direct sums.
Proof. Fix a K-ﬂat resolutionP→M in Cstr(Aop), so we have an isomorphism of
functors M⊗L
A (−)∼=P⊗A (−). The functor
P⊗A (−) : Cstr(A)→Cstr(K)
commutes with inﬁnite direct sums. But by Theorem 10.1.26 the direct sums in
Cstr(−) and in D(−) are the same. □
