---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-007-31-disk-algebras
section_title: "Disk algebras"
section_number: 3.1
pages: 14-18
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds , after Beilinson, Drinfeld and Lurie, are homology-type theories for topological"
---
Deﬁnition 3.1. The∞-category of DiskB
n -algebras in V
AlgDiskB
n
(V) := Fun⊗(DiskB
n , V)
is the∞-category of symmetric monoidal functors.
There is the restricted Yoneda functor
E : MﬂdB
n−→ PShv(MﬂdB
n )−→ PShv(DiskB
n ) .
Deﬁnition 3.2. Let M be a B-framed n-manifold. Let A be a DiskB
n -algebra in V. Factorization
homology (of M with coeﬃcients in A) is an object of V given by either of the equivalent expressions
(provided they exist)
∫
M
A := colim
(
DiskB
n/M→ DiskB
n
A
− →V
)
≃ EM
⨂
DiskB
M
A ,
where the latter is the coend.
14
Remark 3.3. The fact that one describes factorization homology as either a coe nd or a left Kan
extension is exactly analogous to a more familiar fact about the geom etric realizations of a simplicial
set X•: one can think of geometric realization as a coend (this is the usual d eﬁnition, given as a
quotient of ∐
i Xi×∆ i), or one can think of it as a left Kan extension (the colimit of the over category
of simplices in X• of the functor which sends the simplicial i-simplex ∆[ i] to the topological i-simplex
∆ i).
We will frequently make the following requirement of our target.
Deﬁnition 3.4. We say symmetric monoidal ∞-category V is⊗-presentable if it satisﬁes both of
the following conditions.
• V is presentable: with respect to an understood ﬁxed uncountable c ardinal, V admits colimits
and every object is a ﬁltered colimit of compact objects.
• The monoidal structure distributes over small colimits: for each ob ject V ∈ V, the functor
V⊗− : V→ V carries colimit diagrams to colimit diagrams.
Example 3.5. The Cartesian monoidal ∞-category ( Spaces,×) is ⊗-presentable. Likewise, for R
a ring then
(
ModR,⊗
)
, with tensor product relative R, is ⊗-presentable (though the opposite(
Modop
R ,⊗
)
is not).
Remark 3.6. The results of Section 3 (in particular, the Eilenberg–Steenrod axio ms for factorization
homology) only require that the monoidal structure distributes ov er sifted colimits; these results are
established in this generality, though with a smooth structure pres ent, in §2 of [AFT2]. However,
the calculations of Section 4 onwards require the monoidal structu re to distribute over all colimits,
so for simplicity of exposition we enforce this stronger hypothesis t hroughout.
The fully faithful symmetric monoidal functor ι : DiskB
n֒→MﬂdB
n gives the restriction functor
AlgDiskB
n
(V) ←− Fun⊗(
MﬂdB
n , V
)
: ι∗ .
The next result identiﬁes factorization homology as a left adjoint to this functor, provided V is
⊗-presentable.
Proposition 3.7. Provided V is⊗-presentable, there is a left adjoint
ι! : AlgDiskB
n
(V) ⇄ Fun⊗(
MﬂdB
n , V
)
: ι∗ ,
and its value on A evaluates as
ι!(A) : M↦→
∫
M
A .
Proof. Presentability of V grants the existence of the values
∫
M A. Lemma 4.3.2.13 of [Lu1] states
that these expressions deﬁne a functor, as indicated. Propositio n 4.3.3.7 of [Lu1] states that this
functor satisﬁes the universal property of being a left adjoint to the restriction ι∗. We thus have
the solid diagram among ∞-categories
AlgDiskB
n
(V)
/d15/d15
/d47/d47❴ ❴ ❴ ❴ ❴ ❴Fun⊗(
MﬂdB
n , V
)
/d15/d15
Fun(DiskB
n , V)
ι! /d47/d47 Fun(MﬂdB
n , V)
in which the downward functors are restriction to underlying ∞-categories, these downward functors
are fully faithful. It remains to explain how the ⊗-presentability of V grants the existence of the
dashed horizontal functor making the diagram commute.
15
We must show that, for each symmetric monoidal functor A : DiskB
n → V, and for each based
map among ﬁnite sets I+
f
− →J+, the diagram of ∞-categories
(MﬂdB
n )I
f∗
/d15/d15
(ι!A)I
/d47/d47 VI
f∗
/d15/d15
(MﬂdB
n )J (ι!A)J
/d47/d47 VJ
commutes. The map f : I+ → J+ is canonically a composition of a surjective active map f surj
followed by an injective active map f inj followed by an inert map f inrt, and so it is enough to verify
commutativity of the above diagram for each such class of maps. Th e case of inert maps is obvious,
because then f∗ is projection and ( ι!A)K is deﬁned as the K-fold product of functors, for K = I, J .
The case of injective active maps amounts to verifying that ι!A carries each monoidal unit to a
monoidal unit. This follows because A does so and because the over ∞-categories DiskB
n/∅ ={∅} =
MﬂdB
n/∅ consist solely of the empty manifold, which is the monoidal unity.
The case of surjective active maps follows from the case that f : I+→∗ + is given by + ⁄= i↦→∗,
so that f∗ = ⨂ I is the I-fold tensor product. Well, because A is symmetric monoidal, there is a
canonical arrow ι!A◦ ⨂ I−→ ⨂ I◦(ι!A)I between functors ( MﬂdB
n )I→ V that we will argue is an
equivalence. This arrow evaluates on ( Mi)i∈I as the horizontal one in the following natural diagram
in V:
colim
(
DiskB
n/ ⨆
i∈I
Mi→ DiskB
n
A
− →V
) /d47/d47 ⨂
i∈I
colim
(
DiskB
n/Mi→ DiskB
n
A
− →V
)
colim
( ∏
i∈I
DiskB
n/Mi→ (DiskB
n )I AI
−−→VI
⨂ I
−−→V
)
(∗)
/d79/d79
(†)
/d51/d51❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣❣
.
The arrow labeled by ( †) is an equivalence precisely because V⊗− : V→ V preserves colimits. By
inspection, the I-fold disjoint union functor ⨆ I : ∏
i∈I DiskB
n/Mi
≃
− →DiskB
n/ ⨆
i∈I
Mi is an equivalence
between∞-categories, for it is essentially surjective and fully faithful. It follo ws that the arrow
labeled by ( ∗) is an equivalence, after observing the following commutative diagra m among ∞-
categories:
∏
i∈I
DiskB
n/Mi
⨆ I
/d47/d47
/d15/d15
DiskB
n/ ⨆
i∈I
Mi
/d15/d15
(DiskB
n )I
⨆ I
/d47/d47
AI
/d15/d15
DiskB
n
A
/d15/d15
VI
⨂ I
/d47/d47 V .
□
Remark 3.8. Proposition 3.7 implies factorization homology can be expressed as sy mmetric monoidal
left Kan extension, at least when V is⊗-presentable. This is equivalent to operadic left Kan exten-
sion (after parsing Deﬁnitions 3.1.1.2 and 3.1.2.2 of [Lu2]), which is the de ﬁnition of factorization
homology, or topological chiral homology, given by Lurie (Deﬁnition 5 .5.2.6).
The following justiﬁes the notational omission of the space B from the notation
∫
M A.
16
Proposition 3.9. Given a map ϕ : B→ B′ of spaces over BTop(n) and M a B-framed n-manifold
and A a B′-framed n-disk algebra, composition with the map ϕ deﬁnes a B′-framed n-manifold ϕM ,
and restriction along ϕ deﬁnes a B-framed n-disk algebra ϕA. There is a natural equivalence∫
ϕM
A≃
∫
M
ϕA
between the B-framed and B′-framed factorization homologies.
Proof. It suﬃces to show that the forgetful functor DiskB
n/M → Diskn/M is an equivalence. By
deﬁnition, this functor is the projection from the double overcate gory:
DiskB
n/M := ( Diskn/B)/M−→ Diskn/M .
This functor is a pullback of the likewise functor
(
(Spaces/ BTop(n))/B
)
/M → (Spaces/ BTop(n))/M,
which is an equivalence by Lemma 2.5.
□
3.2. F actorization homology over oriented 1-manifolds with boundary . We show that fac-
torization homology of a closed interval is a two-sided bar construc tion.
The data of an oriented embedding֒→[−1, 1] from a ﬁnite disjoint union of oriented intervals,
determines a linear ordering of the connected components of U . This is organized as a monoidal
functor between∞-operads
(4) Disk∂,or
1/[−1,1]−→ AssocRL
to the standard multi-category corepresenting the datum of an a ssociative algebra A, together with
a unital right module T and a unital left module S. Because the space of oriented embeddings
between two oriented intervals is contractible, this functor (4) is a n equivalence of ∞-operads. In
summary, there is an equivalence of ∞-categories
(5) AlgRL(V)
≃
−−→Fun⊗(
Disk∂,or
1/[−1,1], V
)
where the lefthand ∞-category is that of algebras over AssocRL.
Example 3.10. Through (5), there is a functor Algaug
Assoc(V)→ Fun⊗(
Disk∂,or
1/[−1,1], V
)
from augmented
associative algebras in V.
The next result gives a functor from the simplicial category to 1-dis ks by a standard construction
of counting gaps. Our proof is terse; a lengthier treatment is availa ble in §2 of [AFT2].
Lemma 3.11. There is a functor ∆ op→ Disk∂,or
1/[−1,1] which is ﬁnal.
Proof. Let S⊂ Disk∂,or
1/[−1,1] be the full ∞-subcategory of embeddings from oriented intervals that
surject onto the endpoints. That is, S consists of oriented embeddings among 1-manifolds with
boundary of the form [−1, 0)⊔R⊔ℓ⊔(0, 1]֒→[−1, 1], for ℓ≥ 0. To show the inclusion S⊂ Disk∂,or
1/[−1,1]
is ﬁnal, by Quillen’s Theorem A, we can show the under∞-category SU/ has a contractible classifying
space for every ﬁnite disjoint union of subintervals U⊂ [−1, 1]. This is immediate, because SU/ has
an initial object, which is a disjoint union of U with connected open neighborhoods of the endpoints
not contained in U .
Lastly, the result follows because there is an equivalence S→ ∆ op. On objects this is given by
assigning to (֒→[−1, 1]) the set connected components of the complement
[
[−1, 1] /i⋉tegerdivideU
]
together
with the linear order inherited from that of [−1, 1]. That this assignment deﬁnes a functor is routine.
That this functor is an equivalence of ∞-categories follows because each comopnent of the space of
morphisms of Disk∂,or
1/[−1,1] is contractible.
□
This has an immediate corollary, which states that factorization hom ology over a closed interval
is a two-sided bar construction.
17
Corollary 3.12. For V a symmetric monoidal ∞-category which is ⊗-presentable, and for R :
Disk∂,or
1 → V a symmetric monoidal functor, there is a natural equivalenc e in V:
R
(
[−1, 1)
) ⨂
R
(
(−1,1)
) R
(
(−1, 1]
) ≃
−−→
∫
[−1,1]
R .
