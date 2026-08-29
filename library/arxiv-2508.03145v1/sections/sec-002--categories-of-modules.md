---
doc_id: arxiv-2508.03145v1
doc_title: "Θ-Categories and Tannakian duality"
section_id: sec-002--categories-of-modules
section_title: "-Categories of modules"
section_number: null
pages: 11-14
source_pdf: 2508.03145v1.pdf
source_sha256: 2bf03452cb503e96
doc_brief: "Θ-Categories and Tannakian duality — We introduce a notion ofΘ-categories, which is a refinement of the notion of symmetric monoidal∞-categories."
---
To conclude this part onΘ-categories, we will define a Θ-category of left
B-modules for a given Θ-algebra B∈ Θ-CAlg(T Θ). To this end, we first
consider the underlying commutative algebraB0 :=U Θ
E∞(B) and the corre-
sponding symmetric monoidal∞-category LModB0(T ) of leftB0-modules in
T endowed with its natural symmetric monoidal structure⊗B0. It will be
denoted byB0-Mod(T ).
We define aΘ-structure onB0-Mod(T ) by considering the composition
of forgetful∞-functors
B/Θ-CAlg(T Θ)−→B0/CAlg(T )≃ CAlg(B0-Mod(T ))−→B0-Mod(T ).
The above sequence of∞-functors defines an newΘ-category whose under-
lying∞-category is the∞-category ofB0-modules and whose∞-category
of Θ-algebras isB/Θ-CAlg(T Θ), the∞-category of Θ-algebras underB.
Definition 1.11. We will refer to theΘ-category constructed above
B/Θ-CAlg(T Θ)−→ CAlg(B0-Mod(T ))−→B0-Mod(T )
as the Θ-category ofB-modules inT, and denote it simply byB-Mod(T Θ).
The Θ-category of Θ-modules inT Θ receives a natural morphism from
T Θ by tensoring withB. This natural morphismT Θ→B-Mod(T Θ) can be
represented by the following commutative diagram of∞-categories
Θ-CAlg(T Θ) //
‘B

CAlg(T )
⊗B0

//T
⊗B0

B/Θ-CAlg(T Θ) //B0/CAlg(T ) //B0-Mod(T ).
Here the rows are right adjoints whereas the vertical morphisms are left
adjoints, whose right adjoints (forgetting the maps fromB orB0) commute
with the horizontal functors.
We can now state the following proposition, which is an extension to the
context of Θ-categories of the results [Lur22, Cor. 4.8.5.21] on symmetric
monoidal∞-categories and commutative algebras.
Proposition 1.12. Let T Θ be a Θ-category. The∞-functor sending a Θ-
algebra B∈ Θ-CAlg(T Θ) to T Θ→ B-Mod(T Θ) induces a fully faithful left
adjoint∞-functor
Θ-CAlg(T Θ)−→T Θ/∞-CatΘ
pr.
11
Proof. Unwinding the definitions, this is a consequence of the following two
statements.
(1) The∞-functor sending a commutative algebraB0∈ CAlg(T ) to T→
B0-Mod(T )inducesafullyfaithfulleftadjointfunctorof (2,∞)-categories
CAlg(T )−→T/∞-Cat⊗
pr.
(2) For any presentable∞-category C, the∞-functor
C→ (∞-CatR
pr/C)op
sending x∈ C to the comma∞-category x/C with the projection
x/C→C, and a morphismu: y→x to the compositionx/C→y/C
with u, defines a full embedding.
Note that the∞-category of mapsB-Mod(T )→ T′ in T/∞-Cat⊗
pr is
in fact a space: any natural transformationµ: f⇒ g between morphisms
f,g : B-Mod(T )→T′ inT/∞-Cat⊗
pr is an equivalence. Indeed, the classB-
modulesM such thatµM is an equivalence is closed under colimits and con-
tains the freeB-modules. In light of this, statement(1) is proven in [Lur22,
Thm. 4.8.5.11, Cor. 4.8.5.21], whereas statement(2) is simply a version of
the Yoneda lemma.
LetB∈ Θ-CAlg(T Θ)be aΘ-algebra inT Θ andg : T Θ→T Θ
2 a Θ-functor.
Let g∗(1)∈ Θ-CAlg(T Θ) be the image of1∈ Θ-CAlg(T Θ
2 ) under the right
adjoint g∗. We then have the following commutative square of mapping
spaces (rather than∞-categories, by Remark 1.10)
MapT Θ/∞-CatΘ
pr
(B-Mod(T Θ),T Θ
2 ) //

MapΘ-CAlg(T Θ)(B,g∗(1))

MapT/∞-Cat⊗
pr
(B0-Mod(T ),T 2) // MapCAlg(T )(B0,g∗(1)).
Here the top horizontal map sends aΘ-functorf : B-Mod(T Θ)→T Θ
2 to the
unit mapB→ f∗(1) in Θ-CAlg(B-Mod(T Θ)). This corresponds to a map
B→g∗(1) in Θ-CAlg(T Θ) under the equivalence
Θ-CAlg(B-Mod(T Θ))≃B/Θ-CAlg(T Θ).
The bottom horizontal map is defined similarly.
12
It now suffices to verify that the top horizontal map is an equivalence.
Indeed, this shows thatthe functorB7→B-Mod(T Θ)is aleft adjoint. Taking
T Θ
2 =B2-Mod(T Θ), so thatg∗(1) =B2, shows that it is fully faithful.
By property (1) above, the bottom horizontal map is an equivalence.
Let us therefore fix a symmetric monoidal∞-functor f : B-Mod(T )→ T2
under T, and compare the induced map between the fibers of the two ver-
tical maps. By Proposition 1.9, there is a canonical equivalence between
MapT Θ/∞-CatΘ
pr
(B-Mod(T Θ),T Θ
2 )f and the space of all possible limit pre-
serving∞-functors u filling up the diagram below in∞-CatR
pr
Θ-CAlg(T Θ
2 )
u
&&
g∗

// CAlg(T2)
f∗
##
g∗

Θ-CAlg(T Θ) // CAlg(T )
B/Θ-CAlg(T Θ) //
OO
B0/CAlg(T )
OO
such thatf∗◦U Θ
E∞⇒U Θ
E∞◦u∗ is an equivalence.
Note that there is an equivalence of∞-categories
Θ-CAlg(T Θ
2 )×Θ-CAlg(T Θ)B/Θ-CAlg(T Θ)≃g(B)/Θ-CAlg(T Θ
2 )
since g : Θ-CAlg(T Θ)→ Θ-CAlg(T Θ
2 ) is left adjoint tog∗, and similarly for
commutative algebras. Property (2) recalled at the start of the proof there-
fore identifies the space ofu filling the diagram with the fiber atf of the
natural morphism
MapΘ-CAlg(T Θ
2 )(g(B), 1)→ MapCAlg(T2)(g(B0), 1).
By adjunction, this is equivalent to the fiber atf of the natural morphism
MapΘ-CAlg(T Θ)(B,g∗(1))→ MapCAlg(T )(B0,g∗(1)).
The result now follows by noting that for each map ofΘ-algebrasB→g∗(1),
the natural transformation g∗(1)⊗B0 U Θ
E∞(−)⇒ U Θ
E∞(g∗(1)⨿B−) is an
equivalence sinceU Θ
E∞ preserves colimits.
Proposition 1.12 can be usefully combined with the following recognition
result. For this, we note that aΘ-functor f : T Θ
1 → T Θ
2 always induces an
adjunction on the level of the corresponding∞-categories of Θ-algebras
f : Θ-CAlg(T Θ
1 ) ⇆ Θ-CAlg(T Θ
2 ) :f∗
13
where f and f∗ commute with the forgetful∞-functors toT1 and T2. For
any B ∈ Θ-CAlg(T Θ
1 ), this yields a well-defined Θ-functor at the level of
modules
f : B-Mod(T Θ
1 )→f(B)-Mod(T Θ
2 ).
Applying this toB =f∗(1), and composing with the base change along the
counit f(f∗(1))→ 1, we obtain a naturalΘ-functor f∗(1)-Mod(T Θ
1 )→ T Θ
2
whose underlying adjunction of∞-categories takes the form
1⊗f(f∗(1))f(−): f∗(1)-Mod(T1) ⇆T2 :f∗.
Proposition 1.13. Let T Θ
1 → T Θ
2 be a Θ-functor and f : T1 → T2 the
underlying symmetric monoidal∞-functor. We assume that the right adjoint
f∗ : T2→T1 of f satisfies the following conditions.
(1) The∞-functorf∗ is conservative and preserves geometric realizations.
(2) Fory∈T2 and x∈T1, the natural morphism
x⊗f∗(y)→f∗(f(x)⊗y)
is an equivalence inT1.
Then the naturalΘ-functor
f∗(1)-Mod(T Θ
1 )−→T Θ
2
is an equivalence ofΘ-categories.
Proof. The underlying symmetric monoidal∞-functorf∗(1)-Mod(T1)→T2
is an equivalence by the second part of [Lur22, Cor. 4.8.5.21]. As forget-
ting the Θ-structure∞-CatΘ
pr→∞ -Cat⊗
pr is conservative, this implies the
proposition.
