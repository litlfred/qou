---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-039-52-triangulated-and-cohomological-functors
section_title: "Triangulated and Cohomological Functors"
section_number: 5.2
pages: 94-102
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
additive categories, with translation functorsTK and TL respectively. A T-additive
functor F : K→L was deﬁned in Deﬁnition 5.1.3. A morphism of T-additive
functors η:F→G was introduced in Deﬁnition 5.1.5.
Deﬁnition 5.2.1.Let K and L be triangulated categories.
(1) A triangulated functorfrom K to L is a T-additive functor(F,τ) : K→L
that satisﬁes this condition: for every distinguished triangle
L
α
− →M
β
− →N
γ
− →TK(L)
in K, the triangle
F (L)
F(α)
−−−→F (M)
F(β)
−−−→F (N)
τL◦F(γ)
−−−−−−−→TL(F (L))
is a distinguished triangle inL.
94
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(2) Suppose (G,ν) : K →L is another triangulated functor. A morphism
of triangulated functorsη: (F,τ)→(G,ν) is a morphism of T-additive
functors, as in Deﬁnition 5.1.5.
Sometimes we keep the translation isomorphismτimplicit, and refer toF as a
triangulated functor.
Deﬁnition 5.2.2.Let K be a triangulated category. Afull triangulated subcategory
of K is a subcategoryL⊆K satisfying these conditions:
(a) L is a full additive subcategory (see Deﬁnition 2.2.6).
(b) L is closed under translations, i.e.L∈L iﬀT(L)∈L.
(c) L is closed under distinguished triangles, i.e. ifL′→L→L′′∆
−−→is a
distinguished triangle inK s.t. L′,L∈L, then alsoL′′∈L.
Observe that L itself is triangulated, and the inclusionL→K is a triangulated
functor.
Proposition 5.2.3. For i = 0, 1, 2 let (Ki, Ti) be triangulated categories, and let
(Fi,τi) : ( Ki−1, Ti−1)→(Ki, Ti) be triangulated functors. Deﬁne the T-additive
functor (F,τ) := (F2,τ2)◦(F1,τ1) as in Deﬁnition5.1.4. Then (F,τ) : (K0, T0)→
(K2, T2) is a triangulated functor.
Exercise 5.2.4. Prove Proposition 5.2.3.
Deﬁnition 5.2.5.Let K be a triangulated category, and let M be an abelian
category.
(1) A cohomological functorF : K→M is an additive functor, such that for
every distinguished triangle
L
α
− →M
β
− →N
γ
− →T(L)
in K, the sequence
F (L)
F(α)
−−−→F (M)
F(β)
−−−→F (N)
is exact inM.
(2) A contravariant cohomological functorF : K→M is a contravariant addi-
tive functor, such that for every distinguished triangle
L
α
− →M
β
− →N
γ
− →T(L)
in K, the sequence
F (N)
F(β)
−−−→F (M)
F(α)
−−−→F (L)
is exact inM.
Proposition 5.2.6. LetF : K→M be a cohomological functor, and let
L
α
− →M
β
− →N
γ
− →T(L)
be a distinguished triangle inK. Then the sequence
···→F (Ti(L))
F(Ti(α))
−−−−−−→F (Ti(M))
F(Ti(β))
−−−−−−→F (Ti(N))
F(Ti(γ))
−−−−−−→F (Ti+1(L))
F(Ti+1(α))
−−−−−−−→F (Ti+1(M))→···
in M is exact.
95
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. By axiom (TR2) we have these distinguished triangles:
Ti(L)
(−1)i·Ti(α)
−−−−−−−−→Ti(M)
(−1)i·Ti(β)
−−−−−−−−→Ti(N)
(−1)i·Ti(γ)
−−−−−−−−→Ti+1(L),
Ti(M)
(−1)i·Ti(β)
−−−−−−−−→Ti(N)
(−1)i·Ti(γ)
−−−−−−−−→Ti+1(L)
(−1)i+1·Ti+1(α)
−−−−−−−−−−−→Ti+1(M),
Ti(N)
(−1)i·Ti(γ)
−−−−−−−−→Ti+1(L)
(−1)i+1·Ti+1(α)
−−−−−−−−−−−→Ti+1(M)
(−1)i+1·Ti+1(β)
−−−−−−−−−−−→Ti+1(N).
Now use the deﬁnition of a cohomological functor, noting that multiplying mor-
phisms in an exact sequence by−1 preserves exactness. □
Proposition 5.2.7. Let K be a triangulated category. For everyP∈K the functor
HomK(P,−) : K→ModK
is a cohomological functor, and the functor
HomK(−,P ) : K→ModK
is a contravariant cohomological functor.
Proof. We will prove the covariant statement. The contravariant statement is
proved similarly, and we leave this to the reader.
Consider a distinguished triangleL
α
− →M
β
− →N
γ
− →T(L) in K. We have to prove
that the sequence
HomK(P,L )
Hom(idP,α)
− −−−−−−− →HomK(P,M )
Hom(idP,β)
−−−−−−−→HomK(P,N )
in ModK is exact. In view of Proposition 5.3.1, all we need to show is that for
every ψ: P →M s.t. β◦ψ= 0, there is someφ: P →L s.t. ψ= α◦φ. In a
picture, we must show that the diagram below (solid arrows)
P id //
φ

P //
ψ

0 //

T(P )
T(φ)

L α //M
β //N
γ // T(L) .
can be completed (dashed arrow). This is true by (TR2) (= turning) and (TR3)
(= extending). □
Exercise 5.2.8. Prove the contravariant statement in the proposition above.
Question 5.2.9. Let K and L be triangulated categories, and letF : K→L be
an additive functor. Is it true that there is at most one isomorphism of functors
τ:F◦TK
≃
− →TL◦F such that the pair(F,τ) is a triangulated functor?
5.3. SomePropertiesofTriangulatedCategories. Inthissubsectionweprove
a few general results on triangulated categories. Recall that all triangulated cate-
gories, and all triangulated functors between them, are (implicitly)K-linear.
Proposition 5.3.1. Let K be a triangulated category. IfL
α
− →M
β
− →N
γ
− →T(L) is
a distinguished triangle inK, thenβ◦α= 0.
Proof. By axioms (TR1) and (TR3) we have a commutative diagram
L
idL //
idL

L //
α

0 //

T(L)
T(idL)

L α //M
β //N
γ // T(L) .
We see thatβ◦αfactors through 0. □
96
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proposition 5.3.2. Let K be a triangulated category, and let
L α //
φ

M
β //
ψ

N
γ //
χ

T(L)
T(φ)

L′ α′
//M′ β′
//N′ γ′
// T(L′) .
be a morphism of distinguished triangles. Ifφand ψare isomorphisms, thenχis
also an isomorphism.
Proof. Take an arbitraryP∈K, and letF := HomK(P,−). We get a commutative
diagram
F (L)
F(α) //
F(φ)

F (M)
F(β) //
F(ψ)

F (N)
F(γ) //
F(χ)

F (T(L))
F(T(φ))

F(T(α)) //F (T(M))
F(T(ψ))

F (L′)
F(α′) //F (M′)
F(β′) //F (N′)
F(γ′) //F (T(L′))
F(T(α′))//F (T(M′))
in ModK. By Proposition 5.2.7 the rows in the diagram are exact sequences. Since
the other vertical arrows are isomorphisms, it follows that
F (χ) : HomK(P,N )→HomK(P,N′)
is an isomorphism of abelian groups. By forgetting structure, we see thatF (χ) is
an isomorphism of sets.
Consider the Yoneda functorYK : K→Fun(Kop, Set) from Subsection 1.7. There
is a morphismYK(χ) : YK(N)→YK(N′) in Fun(Kop, Set). For every objectP∈K,
letting F := HomK(P,−) as above, we haveYK(N)(P ) =F (N) and YK(N′)(P ) =
F (N′). The calculation above shows that
F (χ) = YK(χ)(P ) : YK(N)(P )→YK(N′)(P )
is an isomorphism in Set. Therefore YK(χ) is an isomorphism in Fun(Kop, Set).
According to Yoneda Lemma (Theorem 1.7.4) the morphismχ: N→N′in K is
an isomorphism. □
Exercise 5.3.3. Try to prove the last proposition without the Yoneda Lemma.
Recall that ifη: F→G is a morphism of functorsK→L, then for an object
M∈K we denote byηM :F (M)→G(M) the corresponding morphism inL.
Corollary 5.3.4. Suppose F,G : K→L are triangulated functors between trian-
gulated categories, andη: F →G is a morphism of triangulated functors. Let
L
α
− →M
β
− →N
γ
− →T(L) be a distinguished triangle inK. If ηL and ηM are isomor-
phisms, thenηN is an isomorphism.
Proof. After applying the functorsF andG, and the morphisms of functorsτF,τG
and η, we obtain a commutative diagram
F (L)
F(α) //
ηL

F (M)
F(β) //
ηM

F (N)
τF,L◦F(γ) //
ηN

TL(F (L))
TL(ηL)

G(L)
G(α) //G(M)
G(β) //G(N)
τG,L◦G(γ) // TL(G(L))
in L in which the rows are distinguished triangles. According to Proposition 5.3.2
the morphismηN is an isomorphism. □
97
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Corollary 5.3.5. Let K be a triangulated category, and letL
α
− →M− →N
∆
−−→be a
distinguished triangle in it. The two conditions below are equivalent.
(i) α:L→M is an isomorphism.
(ii) N∼= 0.
Exercise 5.3.6. Prove Corollary 5.3.5. (Hint: Use Proposition 5.3.2 and axiom
(TR1)(c).)
Deﬁnition 5.3.7.Let K be a triangulated category, and letα: L→M be a
morphism in K. By axiom (TR1)(b) there exists a distinguished triangle
(†) L
α
− →M
β
− →N
γ
− →T(L)
in K. The objectN is called acone ofα, and the distinguished triangle (†) is called
a distinguished triangle built onα.
Corollary 5.3.8. In the situation of Deﬁnition5.3.7, the objectN and the distin-
guished triangle(†) are unique up to isomorphism.
Proof. Suppose
(†′) L
α
− →M
β′
−→N′γ′
−→T(L)
isanotherdistinguishedtrianglebuilton α. Byaxiom(TR3)thereisacommutative
diagram
L α //
idL

M
β //
idM

N
γ //
χ

T(L)
T(idL)

L α //M
β′
//N′ γ′
// T(L) .
in K. Proposition 5.3.2 says thatχis an isomorphism. □
Remark 5.3.9.In general the isomorphismχin the corollary above is not unique,
and thus the cone ofαis not functorial in the morphismα. However, in some
special casesχis unique – see Remark 5.3.26 below.
Note also that the standard cones and triangles in the DG categoryC(A, M) are
functorial, by Proposition 4.2.6. This implies that in the triangulated categories
K(A, M) and D(A, M) we can sometimes arrange to have functorial cones.
Proposition 5.3.10. Let K be a triangulated category, and letL
α
− →M
β
− →N
γ
− →
T(L) be a distinguished triangle in it. The two conditions below are equivalent.
(i) The morphismγis zero.
(ii) There exists a morphismτ:M→L such thatτ◦α= idL.
Proof.
(i)⇒(ii): By Propositions 5.2.7 the contravariant functorHomK(−,L ) is coho-
mological. Applying it to the given distinguished triangle, and using Proposition
5.2.6, we get an exact sequence ofK-modules
HomK(M,L )
Hom(α,idL)
−−−−−−−→HomK(L,L )
Hom(T−1(γ),idL)
−−−−−−−−−−−→HomK(T−1(N),L ).
Since the homomorphismHomK(T−1(γ), idL) is zero, there exists some morphism
τ∈HomK(M,L ) such that idL = HomK(α,idL)(τ) =τ◦α.
98
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(ii)⇒(i): Let us examine the commutative diagram
HomK(N,N )
Hom(id,γ)

HomK(N, T(L))
Hom(id,T(α))

Hom(id,id)
$$
HomK(N, T(M))
Hom(id,T(τ)) // HomK(N, T(L))
in ModK. Because the homomorphism HomK(id, id) is bijective, it follows that
HomK(id, T(α)) is injective. But the column is an exact sequence (by Proposi-
tions 5.2.7 and 5.2.6), and therefore HomK(idN,γ) = 0 . We conclude that γ=
HomK(idN,γ)(idN) = 0. □
Lemma 5.3.11. LetM,M′be objects in a triangulated categoryK. Consider the
canonical morphisms
M
e
− →M⊕M′p
− →M and M′e′
− →M⊕M′p′
−→M′.
Then
M
e
− →M⊕M′p′
−→M′0
− →T(M)
is a distinguished triangle inK.
Proof. By axiom (TR1)(c) and axiom (TR2) there is a distinguished triangle0
0
− →
M′idM′
−−−→M′0
− →0. By axiom (TR1)(b) there is a distinguished triangle
(5.3.12) M
e
− →M⊕M′β
− →N
γ
− →T(M)
in K, for some objectN. Becausep◦e = idM, Proposition 5.3.10 says thatγ= 0.
Next, sincep′◦e = 0, axiom (TR3) produces a morphism of triangles
(5.3.13) M e //
0

M⊕M′ β //
p′

N
γ=0 //
ψ

T(M)
0

0 0 //M′ idM′
//M′ 0 // 0
We claim thatψis an isomorphism. This is proved indirectly. For every object
L∈K there is a commutative diagram
(5.3.14) HomK(L,M ) // HomK(L,M⊕M′) //
Hom(idL,p′)

HomK(L,N ) //
Hom(idL,ψ)

0
0 // HomK(L,M′) id // HomK(L,M′) // 0
in ModK, that’s gotten by applying the functorHomK(L,−) to the left part of
diagram (5.3.13). The rows in (5.3.14) are exact sequences. Because
HomK(L,M⊕M′)∼= HomK(L,M )⊕HomK(L,M′)
we can replace (5.3.14) with the next commutative diagram
(5.3.15) 0 // HomK(L,M′) //
Hom(idL,idM′)

HomK(L,N ) //
Hom(idL,ψ)

0
0 // HomK(L,M′) id // HomK(L,M′) // 0
99
Derived Categories | Amnon Yekutieli | 14 Apr 2019
with exact rows. We see thatHom(idL,ψ) is an isomorphism ofK-modules. Hence
it is a bijection of sets. Using the Yoneda Lemma, like in the proof of Proposition
5.3.2, we conclude thatψis an isomorphism inK.
Finally, from the commutative diagram (5.3.13) we know thatψ◦β=p′. So we
have this isomorphism of triangles:
(5.3.16) M e //
id

M⊕M′ β //
id

N
γ=0 //
ψ∼=

T(M)
id

M e //M⊕M′ p′
//M′ 0 // T(M)
The ﬁrst triangle is distinguished. By axiom (TR1)(a) the second triangle is also
distinguished. □
Deﬁnition 5.3.17.Let K be a linear category, and letM,N ∈K.
(1) The objectM is called aretractofN if there are morphismsM
e
− →N
p
− →M
such thatp◦e = idM. The morphisme :M→N is called an embedding.
(2) The objectM is called adirect summandofN if there is an objectM′∈K
and an isomorphismM⊕M′∼=N. The corresponding morphisme :M→
N is called an embedding.
Note that in both items above the embeddinge : M→N is a monomorphism
in K.
Theorem 5.3.18. Let K be a triangulated category, and lete : M →N be a
morphism in K. The following two conditions are equivalent:
(i) There is a morphisme′:M′→N in K such that
(e,e′) :M⊕M′→N
is an isomorphism. In other words, M is a direct summand ofN, with
embeddinge :M→N.
(ii) There is a morphismp : N →M in K such that p◦e = idM. In other
words,M is a retract ofN, with embeddinge :M→N.
Proof.
(i)⇒(ii): This is trivial (and only requiresK to be a linear category).
(ii)⇒(i): Let M
e
− →N
β
− →M′γ
− →T(M) be a distinguished triangle in K built
on e. By Proposition 5.3.10 we know thatγ= 0. According to Lemma 5.3.11,
M
ϵ
− →M⊕M′π′
−→M′0
− →T(M) is also the distinguished triangle inK; hereϵis the
embedding andπ′is the projection. Turning these two distinguished triangles and
using axiom (TR3) we get a morphismθsuch that the diagram
T−1(M′) 0 //
id

M ϵ //
id

M⊕M′ π′
//
θ

M′
id

T−1(M′) 0 //M e //N
β //M′
is commutative. By Proposition 5.3.2, θis an isomorphism. Finally we deﬁne
e′:=θ◦ϵ′, whereϵ′:M′→M⊕M′is the embedding. □
Deﬁnition 5.3.19.Let K be a triangulated category. Asaturated full triangulated
subcategoryof K is a full triangulated subcategoryK′⊆K (Deﬁnition 5.2.2) which
is closed inK under taking direct summands and under isomorphisms.
100
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 5.3.20.Let K be a triangulated category and letZ⊆Ob(K) be a set
of objects. The saturated full triangulated subcategory ofK generated byZ is the
smallest saturated full triangulated subcategoryK′⊆K such thatZ⊆Ob(K′).
Proposition 5.3.21. Let K be a triangulated category, letZ⊆Ob(K) be a set of
objects, and letK′⊆K be the saturated full triangulated subcategory ofK generated
by Z. An objectM∈K belongs to K′if and only if there is a sequenceM0,...,Mr
of objects ofK, such thatMr =M, and for everyi≤r at least one of the following
conditions holds:
(a) Mi∈Z.
(b) There is an isomorphismMi∼= Tp(Mj) in K for somej <i and p∈Z.
(c) There is a distinguished triangle Mj →Mk →Mi
∆
−−→in K for some
j,k <i.
(d) Mi is a direct summand ofMj in K for somej <i.
Proposition 5.3.22. Let K and L be triangulated categories, letF,G : K→L be
triangulated functors, and letζ: F →G be a morphism of triangulated functors.
Denote by K′the full subcategory ofK on the objectsM such thatζM : F (M)→
G(M) is an isomorphism inL. Then K′is a saturated full triangulated subcategory
of K.
Corollary 5.3.23. Let K and L be triangulated categories, letF : K→L be a
triangulated functor, and letK′be the kernel ofF, i.e.K′⊆K is the full subcategory
on the objectsM∈K such thatF (M) = 0. Then K′is a saturated full triangulated
subcategory ofK.
Exercise 5.3.24. Prove Proposition 5.3.21, Proposition 5.3.22 and Corollary
5.3.23.
We end this subsection with two remarks.
Remark 5.3.25. The story of the concept “saturated full triangulated subcate-
gory” is convoluted. In the text [155] from 1977, J.-L. Verdier introducedépaisse
full triangulated subcategories (a rather messy deﬁnition). However, J. Rickard
proved (see [125, Proposition 1.3], published in 1989) that épaisse is equivalent to
saturated, as deﬁned above. Rickard did not give a name for this new and useful
property.
Verdier died in 1989. A few years later, in 1996, G. Maltsiniotis published
Verdier’s thesis [156]. In this thesis the word “épaisse” is absent, and instead we
ﬁndthedeﬁnitionofsaturatedcategories, identicaltoDeﬁnition5.3.19. Maltsiniotis
notes that Verdier was aware (although this is only implicit in his writing) of the
equivalencebetweenépaisseandsaturated; indeed, thesearepreciselythecategories
that occur as kernels of triangulated functors (see Corollary 5.3.23 above, and
Remark 7.1.14 on Verdier quotients and saturated denominator sets of morphisms).
Remark 5.3.26. As mentioned above, in Remark 5.3.9, the cone of a morphism
α: L→M in a triangulated categoryD is usually not functorial. However, ifD
is endowed with at-structure, then some cones can be made functorial. Here is a
quick explanation.
The concept of t-structure was introduced by A.A. Beilinson, J. Bernstein and
P. Deligne in the book [16]. A t-structure on a triangulated categoryD consists of
a pair(D≤0, D≥0) of full subcategories ofD, that satisfy a few axioms (see e.g. [75,
Chapter X] or [187, Deﬁnition 4.1]). The prototypical example is thestandard t-
structureon D := D(M), the derived category of an abelian categoryM (see Section
7 of the book). HereD≤0 is the full subcategory ofD(M) on the complexesM with
nonpositive cohomology, andD≥0 is the full subcategory ofD(M) on the complexes
101
Derived Categories | Amnon Yekutieli | 14 Apr 2019
M with nonnegative cohomology. Other t-structures onD = D(M) are often called
perverse t-structures.
The heart of the t-structure (D≤0, D≥0) is the category D0 := D≤0∩D≥0. In
the prototypical example above, the heart is the category of complexesM with
cohomology concentrated in degree0, so it is equivalent toM. Something similar
happens in general: the heart D0 is always an abelian category, and there is a
cohomological functor H0 : D→D0. The short exact sequences0→L
α
− →M
β
− →
N →0 in D0 are the distinguished trianglesL
α
− →M
β
− →N
∆
−−→in D such that
L,M,N ∈D0.
Here is how a t-structure(D≤0, D≥0) aﬀects functoriality of cones. Axiom (TR3)
guarantees that for a pair of distinguished triangles and morphismφ,ψas in the
solid diagram below, there isat least onemorphism χ(the dashed arrow) making
the whole diagram commutative.
L α //
φ

M
β //
ψ

N
γ //
χ

T(L)
T(φ)

L′ α′
//M′ β′
//N′ γ′
// T(L′)
According to [16, Proposition 1.1.9] (see also [187, Lemma 4.10]), ifL∈D≤0 and
T(N′)∈D≥0, then this morphismχis unique.
The idea of a t-structure emerged in the study of algebraic topology, microlocal
analysis and representations of Lie algebras. In that context the triangulated cat-
egory D was the full subcategory ofD(KX) on complexes with suitable ﬁniteness
and constructibility conditions. The base ringK was either a ﬁeld or thel-adic
integers ˆZl. The space (or site)X was either a topological space with a classical
metric topology, or a scheme with its étale topology. The objects of the heart where
called perverse sheaves. This theory is explained in the original book [16], and also
in [27] and in [75, Chapter X]. In algebraic geometry one can also considerperverse
coherent sheaves; see [187] and [4].
