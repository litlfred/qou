---
doc_id: 2018sorus020
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-074-2-for-anyγ-γ
section_title: "For anyγ∈ Γ,"
section_number: 2
pages: 102-103
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "HAL Id: tel-02108892 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 78 sections: Introduction"
---
(
φ(γ) φ(αγ) φ(βγ) φ(αβγ)
)
and the
matrix M =


φ(e) φ(α) φ(β) φ(αβ)
φ(α) φ(α)2 φ(α)φ(β) φ(α)φ(αβ)
φ(β) φ(β)φ(α) φ(β)2 φ(β)φ(αβ)
φ(αβ) φ(αβ)φ(α) φ(αβ)φ(β) φ(αβ)2


. A computation gives
det(M) =−φ(∆α,β)2 henceM∈ GL4(R) in the following. We will denote byTt
γ the
column-vector transpose ofTγ.
LemmaA.0.6. Assume thatφ(∆α,β)∈R×, then for anyγ,δ ∈ Γ,φ (γδ) =TγM−1Tt
δ.
Proof. Forδ∈ Γ, we deﬁneHδ : Γ→R byHδ(γ) =φ(γδ)−TγM−1Tt
δ. ThenHδ is
a form sinceHδ(γη) +Hδ(γ−1η) = φ(γηδ) +φ(γ−1ηδ)− (Tγη +Tγ−1η)M−1Tt
δ, and
the trace relationφ(γγ′) +φ(γ−1γ′) =φ(γ)φ(γ′) implies thatHδ(γη) +Hδ(γ−1η) =
φ(γ)φ(ηδ) +φ(γ)TηM−1Tt
δ =φ(γ)Hδ(η).
Moreover, from


Te
Tα
Tβ
Tαβ


=M we deduce thatHδ(e) =Hδ(α) =Hδ(β) =Hδ(αβ) =
0, that isHδ is homogeneous and satisﬁes the hypothesis of Lemma A.0.5, hence for
any γ∈ Γ,φ (∆α,β)Hδ(γ) = 0 and we conclude thatHδ(γ) = 0 for allδ∈ Γ, thus
the lemma is proved.
Proof of Saito’s Theorem.Let us deﬁne
ρ : Γ→M 2(R)
γ↦→
(
Id A B AB
)
M−1Tt
γ
Here we consider the vectorM−1Tt
γ’s entries to be2× 2 scalar matrices. We need
to check that the map we deﬁned does satisfy all the requirements of the theorem.
101
1.
(
ρ(e) ρ(α) ρ(β) ρ(αβ)
)
=
(
Id A B AB
)
M−1
(
Tt
e Tt
α Tt
β Tt
αβ
)
but
the right hand matrix is exactly the matrixM, hence ρ(e) = Id ,ρ (α) =
A,ρ (β) =B,ρ (αβ) =AB.
2. For anyγ∈ Γ,


Tr(ρ(γ))
Tr(Aρ(γ))
Tr(Bρ(γ))
Tr(ABρ(γ))


=Tt
γ since by deﬁnition, we haveTr(ρ(γ)) =
(
Tr Id Tr A TrB TrAB
)
M−1Tt
γ and thus the left hand side term is pre-
cisely


TrI TrA TrB TrAB
TrA TrA2 TrAB TrA2B
TrB TrAB TrB2 TrAB2
TrAB TrA2B TrAB2 Tr(AB)2


M−1Tt
γ but item 1 implies that
the matrix


TrI TrA TrB TrAB
TrA TrA2 TrAB TrA2B
TrB TrAB TrB2 TrAB2
TrAB TrA2B TrAB2 Tr(AB)2


is nothing butM.
