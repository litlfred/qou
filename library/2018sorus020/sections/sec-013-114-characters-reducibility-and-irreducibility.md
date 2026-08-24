---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-013-114-characters-reducibility-and-irreducibility
section_title: "Characters, reducibility and irreducibility"
section_number: 1.1.4
pages: 21-23
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "Reidemeister torsion on character varieties — 78 sections: Introduction; (−1)i+1; ByH∗(M, Ad◦ρ) (respectivelyH∗(M,ρ"
---
From the previous deﬁnition of the character variety through trace functions, we
have the following deﬁnition of points of the character variety, which enlightens on
the terminology.
Deﬁnition 1.1.12.Ak-character is ak-point of the character variety in the sense
of algebraic geometry, that means a morphismχ : B[Γ]→ k. Any representation
ρ : Γ→ SL2(k) induces a characterχρ :B[Γ]→k that sendsYγ to Tr(ρ(γ)).
Remark 1.1.13.This deﬁnition generalizes toR-characters for anyk-algebra R.
Deﬁnition 1.1.14.A representationρ : Γ→ SL2(k) is reducible if there exists an
invariant line ink2, andirreducible if not.
The following standard lemma tells us that this notion can be deﬁned at the level
of characters. For any elementsα,β ∈ Γ, we will denote the commutatorαβα−1β−1
by [α,β ].
Lemma 1.1.15. Let k⊂ K be a ﬁeld extension (we takeK to be eitherk, either
a transcendental extension ofk). A representationρ : Γ → SL2(K) is absolutely
irreducible (irreducible in an algebraic closure) iﬀ there existsα,β ∈ Γ such that
Tr(ρ(αβα−1β−1))⁄= 2.
20
δγ
γ δ
=−
 −
γ δ γ δ
=−
−Yγδ −YγYδ Yγδ−1
YγYδ Yγδ−1 Yγδ
γ γ
δ δ
−
Figure 1.2 –
Proof. If ρ is reducible on ¯K, then one can writeρ as a subgroup ofSL2( ¯K) with
every element ofΓ mapped to an upper-triangular matrix. It is clear thus that the
commutator of any two elements have trace equal to 2. Conversely, if any commu-
tator’s trace is 2, then any commutator ﬁxes a non trivial subspace of¯K2. Assume
[α,β ] and [δ,γ ] have two distinct ﬁxed lines, they provide a basis of¯K2 such that
ρ([α,β ]) = ( 1 x
0 1 ) and ρ([δ,γ ]) =
( 1 0
y 1
)
for some non-zerox,y∈ ¯K. Now we compute
Tr(ρ([[α,β ], [δ,γ ]])) = 2+(xy)2, a contradiction. Hence the image of the commutator
subgroup has an invariant subspace in¯K2. We prove that it implies thatρ is redu-
cible; denote byF the invariant subspace of[Γ, Γ], letα∈ Γ\ [Γ, Γ] and β∈ [Γ, Γ]
withρ(β)⁄= Id. Then[ρ(β)−1,ρ (α)−1].F =F andρ(β).F =F, henceρ(β) stabilizes
ρ(α).F, andρ(α).F =F.
Deﬁnition 1.1.16.
— For anyα,β ∈ Γ, we denote by∆α,β∈ B[Γ] the functionY 2
α +Y 2
β +Y 2
αβ−
YαYβYαβ−4 =Y[α,β]−2. For anyk-algebraR, we will say that anR-character
χ is irreducible if there existsα,β ∈ Γ such thatχ(∆α,β)⁄= 0. If not, we say
that it isreducible. A characterχ will be saidcentral if χ(Yγ)2 = 4 for any
γ∈ Γ.
— Since being reducible is a Zariski closed condition, any irreducible component
X⊂ X(Γ) that contains only reducible characters will be saidof reducible
type. A component that contains an irreducible character (equivalently, a
dense open subset of irreducible characters) will be saidof irreducible type.
21
