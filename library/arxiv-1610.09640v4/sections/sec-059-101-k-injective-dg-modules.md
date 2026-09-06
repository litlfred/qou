---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-059-101-k-injective-dg-modules
section_title: "K-Injective DG Modules"
section_number: 10.1
pages: 175-179
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
modules form full triangulated subcategories ofK(A, M), and are concrete versions
of the abstract categoriesP and J, that played important roles in Subsection 8.4.
For K(A) we also deﬁneK-ﬂat DG modules.
10.1. K-Injective DG Modules.For every integerp we have thep-th cohomol-
ogy functor Hp : Cstr(A, M)→M. There is equalityHp = H0◦Tp, where T is the
translation functor of C(A, M). The functors Hp pass to the homotopy category,
and H0 : K(A, M)→M is a cohomological functor, in the sense of Deﬁnition 5.2.5.
Deﬁnition 10.1.1.A DG moduleN∈C(A, M) is calledacyclic if Hp(N) = 0 for
all p.
Deﬁnition 10.1.2.A DG moduleI∈C(A, M) is called K-injective if for every
acyclic DG moduleN∈C(A, M), the DGK-module HomA,M(N,I ) is acyclic.
The deﬁnition above characterizes K-injectives as objects ofC(A, M). The next
proposition shows that being K-injective is intrinsic to the triangulated category
K(A, M), with the cohomological functor H0 (that tells us which are the acyclic
objects).
Proposition 10.1.3. A DG module I ∈K(A, M) is K-injective if and only if
HomK(A,M)(N,I ) = 0 for every acyclic DG moduleN∈K(A, M).
Proof. This is because for every integerp we have
Hp(
HomA,M(N,I )
{∼= H0(
HomA,M(T−p(N),I )
{
= HomK(A,M)(T−p(N),I ),
and N is acyclic iﬀT−p(N) is acyclic. □
Deﬁnition 10.1.4.Let M∈C(A, M). A K-injective resolutionof M is a quasi-
isomorphism ρ:M→I in Cstr(A, M), whereI is a K-injective DG module.
Remark 10.1.5. Let ρ: M →I be a K-injective resolution in Cstr(A, M). By
a slight abuse of notation, we shall often refer to the induced quasi-isomorphism
P(ρ) :M→I in K(A, M) as a K-injective resolution ofM. Cf. Deﬁnitions 10.1.11
and 10.1.21 below.
In the next section we will prove existence of K-injective resolutions in several
contexts. Here is an easy example of a K-injective complex.
Exercise 10.1.6. Let I∈K(M) be a complex of injective objects ofM, with zero
diﬀerential. Prove thatI is K-injective.
Deﬁnition 10.1.7.Let K be a full subcategory ofK(A, M). The full subcategory
of K on the K-injective DG modules in it is denoted by Kinj. In other words,
Kinj = K(A, M)inj∩K.
Remark 10.1.8. Warning: the property of a DG moduleI∈K being K-injective
is in general not intrinsic to the subcategoryK⊆K(A, M). This is because the
condition in Proposition 10.1.3 (and in Deﬁnition 10.1.2) has to be tested against
all acyclic DG modulesN∈K(A, M).
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
175
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proposition 10.1.9. If K is a full triangulated subcategory ofK(A, M), then Kinj
is a full triangulated subcategory ofK.
Proof. It suﬃces to prove thatK(A, M)inj is a triangulated subcategory ofK(A, M).
It is easy to see thatK(A, M)inj is closed under translations. SupposeI→J→
K
∆
−−→is a distinguished triangle in K(A, M) such that I,J are K-injective DG
modules. We have to show thatK is also K-injective. Take any acyclic DG module
N∈K(A, M). There is an exact sequence
HomK(A,M)(N,J )→HomK(A,M)(N,K )→HomK(A,M)(N, T(I))
in ModK. BecauseJ and T(I) are K-injectives, Proposition 10.1.3 says that
HomK(A,M)(N,J ) = 0 = HomK(A,M)(N, T(I)).
Therefore HomK(A,M)(N,K ) = 0. ButN is an arbitrary acyclic DG module, soK
is K-injective. □
Example 10.1.10. Let ⋆be some boundedness condition (namely b, + or−).
We know that K⋆(A, M) is a full triangulated subcategory of K(A, M). Hence
K⋆(A, M)inj is a triangulated subcategory too.
Deﬁnition 10.1.11.Let K be a full triangulated subcategory ofK(A, M). We say
that K has enough K-injectivesif every DG moduleM∈K admits a K-injective
resolution inside K. I.e. there is a quasi-isomorphismρ:M→I where I∈Kinj.
Here is the crucial fact regarding K-injectives.
Lemma 10.1.12. Lets :I→M be a quasi-isomorphism inK(A, M), and assume
I is K-injective. Thens has a left inverse, namely there is a morphismt :M→I
in K(A, M) such thatt◦s = idI. Moreover, this morphismt is unique.
Proof. Consider a distinguished triangleI
s
− →M→N
∆
−−→in K(A, M) that’s built
ons. The long exact cohomology sequence tells us thatN is an acyclic DG module.
Therefore HomK(A,M)(Tp(N),I ) = 0 for allp. The exact sequence
HomK(A,M)(N,I )→HomK(A,M)(M,I )
→HomK(A,M)(I,I )→HomK(A,M)(T−1(N),I )
shows that the homomorphism
(−)◦s : HomK(A,M)(M,I )
≃
− →HomK(A,M)(I,I )
is a bijection. We taket :M→I to be the unique morphism inK(A, M) such that
t◦s = idI. □
Theorem 10.1.13.LetA be a DG ring, letM be an abelian category, and letK be
a full triangulated subcategory ofK(A, M). Write S := K∩S(A, M), and letD := KS
be the localization, with localization functorQ : K→D. Then for everyM∈K and
I∈Kinj the homomorphism
QM,I : HomK(M,I )→HomD(M,I )
is bijective.
Proof. We know that Q : K →D is a left Ore localization with respect to S.
Suppose q : M→I is a morphism inD = KS. Let us presentq as a left fraction:
q = Q(s)−1◦Q(a), wherea :M→N and s :I→N are morphisms inK, ands is
a quasi-isomorphism. By Lemma 10.1.12,s has a left inverset :M→I in K. We
get a morphismt◦a :M→I in K, and an easy calculation shows thatQ(t◦a) =q
in D. This proves surjectivity of the functionQM,I.
176
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Now let’s prove injectivity ofQM,I. Ifa :M→I is a morphism inK such that
QM,I(a) = 0 , then by axiom (LO4) of left Ore localization (see Deﬁnition 6.2.2)
there is a quasi-isomorphisms :I→L in K such thats◦a = 0 in K. Lett be the
left inverse ofs. Thena =t◦s◦a = 0 in K. □
Corollary 10.1.14. In the situation of Theorem10.1.13, the localization functor
Q : Kinj→D is fully faithful.
Proof. Since Kinj is a full subcategory ofK, for everyJ,I ∈Kinj we have bijections
HomKinj(J,I )
≃
− →HomK(J,I )
QJ,I
−−−→HomD(J,I ),
where the bijectionQJ,I is by the theorem above. □
Corollary 10.1.15. In the situation of Theorem 10.1.13, if K has enough K-
injectives, then the localization functorQ : Kinj→D is an equivalence.
Proof. By Corollary 10.1.14 the functor Q is fully faithful. The extra condition
guarantees that Q is essentially surjective on objects. □
Corollary 10.1.16. Let⋆be any boundedness condition. IfK⋆(A, M) has enough
K-injectives, then the triangulated functor
Q : K⋆(A, M)inj→D⋆(A, M)
is an equivalence.
Proof. Since K⋆(A, M)is a full triangulated subcategory ofK(A, M), this is a special
case of the Corollary 10.1.15. □
Remark 10.1.17. These last results are of tremendous importance, both theo-
retically and practically. In the theory, Corollary 10.1.16 shows that the localized
category D⋆(A, M), which is too big to lie inside the original universeU (see Remark
6.2.20), isequivalent toa U-category. Onthe practicalside, Corollary 10.1.14means
that among K-injective objects we do not need fractions to represent morphisms.
Corollary 10.1.18. Let K ⊆K′be full triangulated subcategories of K(A, M).
DeﬁneS := K∩S(A, M), S′:= K′∩S(A, M), D := KS and D′:= K′
S′. If K and K′
have enough K-injectives, then the canonical functorD→D′is fully faithful.
Proof. Combine Corollary 10.1.15 with the fact that the canonical functorK→K′
is fully faithful. □
Corollary10.1.19. Letφ:I→J be a morphism inCstr(A, M) between K-injective
objects. Thenφis a homotopy equivalence if and only if it is a quasi-isomorphism.
Proof. One implication is trivial. For the reverse implication, if φis a quasi-
isomorphism then it is an isomorphism inD(A, M), and by Corollary 10.1.14 for
K = K(A, M) we see thatφis an isomorphism inK(A, M). □
Theorem 10.1.20.In the situation of Theorem10.1.13, assume thatK has enough
K-injectives. Let E be a triangulated category, and letF : K→E be a triangulated
functor. Then F has a right derived functor(RF,ηR) : D→E. Furthermore, for
every I∈Kinj the morphismηR
I :F (I)→RF (I) in E is an isomorphism.
Proof. We will use Theorem 8.4.9. In the notation of that theorem, letJ := Kinj.
Condition (a) of that theorem holds (this is the “enough K-injectives” assumption).
Next, Corollary 10.1.19 implies that every quasi-isomorphismφ: I →J in Kinj
is actually an isomorphism. Therefore F (φ) is an isomorphism in E, and this is
condition (b) of Theorem 8.4.9. □
Here is another useful deﬁnition. It is a variant of Deﬁnition 8.3.4.
177
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 10.1.21.Let K be a full triangulated subcategory of K(A, M), and
assume K has enough K-injectives. A system of K-injective resolutionsin K is a
pair (I,ρ), whereI : Ob(K)→Ob(Kinj) is a function, andρ={ρM}M∈Ob(K) is a
collection of quasi-isomorphismsρM :M→I(M) in K. Moreover, ifM∈Ob(Kinj),
then I(M) =M and ρM = idM.
Example 10.1.22. Let A be any DG ring. We will prove later thatK(A) has
enough K-injectives. Therefore, given a triangulated functorF : K(A)→E into
a triangulated category E, the right derived functor(RF,ηR) : D(A)→E exists.
Suppose we choose a system of K-injective resolutions(I,ρ) in K(A). Then we get
a presentation of(RF,ηR) as follows: RF (M) :=F (I(M)) and ηR
M :=F (ρM).
The proposition below is a variant of Lemma 8.3.9.
Proposition 10.1.23. In the situation of Theorem10.1.13, suppose K has enough
K-injectives, and let (I,ρ) be a system of K-injective resolutions inK. Then the
function I extends uniquely to a triangulated functor I : D →Kinj, such that
IdKinj =I◦Q|Kinj, andρ: IdD⇒Q◦I is an isomorphism of triangulated functors.
Proof. The proof is the same as that of Lemma 8.3.9, except that here we use
Corollary 10.1.15. □
The next corollary is a categorical interpretation of the last proposition.
Corollary 10.1.24 (Functorial K-Injective Resolutions). Let K be a full triangu-
lated subcategory ofK(A, M), and assumeK has enough K-injectives.
(1) There is a triangulated functorI : K→K and a morphism of triangulated
functors ρ: IdK⇒I, such that for every objectM∈K the objectI(M) is
K-injective, and the morphismρM :M→I(M) is a quasi-isomorphism.
(2) If (I′,ρ′) is another such pair, then there is a unique isomorphism of tri-
angulated functorsζ:I
≃
=⇒I′such thatρ′=ζ◦ρ.
Exercise 10.1.25. Prove Corollary 10.1.24.
Inﬁnite direct sums inCstr(A, M) were discussed in Proposition 3.8.15. Their
existence depends only on the existence of inﬁnite direct sums inM.
Theorem 10.1.26. Let A be a DG ring, let M be an abelian category, and let
{Mx}x∈X be a collection of objects ofC(A, M). Assume that C(A, M) has enough
K-injectives, and that the direct sumM :=⨁
x∈XMx exists in Cstr(A, M). Then
M is the direct sum of the collection{Mx}x∈X in D(A, M).
Proof. Let’s use these shorthands:Cstr := Cstr(A, M), K := K(A, M) and D :=
D(A, M). For each indexx there is a morphismex :Mx→M in Cstr, that passes
to a morphism Q(ex) : Mx→M in D. We need to verify that the collection of
morphisms{Q(ex)}x∈X has the universal property of a coproduct.
Take any objectN ∈D, and choose a K-injective resolutionN →J in Cstr.
There is an isomorphism of DGK-modules
(10.1.27)
HomA,M(M,J ) = HomA,M
(⨁
x∈X
Mx, J
{
∼=

x∈X
HomA,M(Mx,J ).
178
Derived Categories | Amnon Yekutieli | 14 Apr 2019
From it we obtain isomorphisms ofK-modules
(10.1.28)
HomD(M,N )∼=†HomK(M,J ) = H0(
HomA,M(M,J )
{
∼=‡H0
(
x∈X
HomA,M(Mx,J )
{
∼=♯
x∈X
H0(
HomA,M(Mx,J )
{
=

x∈X
HomK(Mx,J )∼=†
x∈X
HomD(Mx,N ).
The isomorphisms∼=†are due to Theorem 10.1.13; the isomorphism∼=‡is from
formula(10.1.27); andtheisomorphism ∼=♯isbecausethefunctor H0 commuteswith
products. Since the composed isomorphism in (10.1.28) is induced by the collection
of morphisms{Q(ex)}x∈X, we see that the universal property of a coproduct holds.
□
Remark 10.1.29. The concept of a K-injective complex (i.e. a K-injective object
of C(M)), as well as the similar concepts of K-projective and K-ﬂat complexes that
will be discussed below, were introduced by N. Spaltenstein [143] in 1988. At about
the same time other authors (B. Keller [79], M. Bockstedt and A. Neeman [23], J.
Bernstein and V. Lunts [20]) discovered this concept independently, with other
names (such ashomotopically injective complex). The texts [20] and [79] already
talk about DG modules over DG rings.
