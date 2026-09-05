---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-009-35-functoriality-of-traces
section_title: "Functoriality of traces"
section_number: 3.5
pages: 23-24
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
doc_brief: "NONLINEAR TRACES — W e combine the theory of traces in homotopical algebra with s heaf theory in de- rived algebraic geometry to deduce general ﬁxed point and ch aracter formulas."
---
A⊗A∨
Ψ ⊗idA∨
/d15/d15
Φ A⊗idA∨
/d47/d47A⊗A∨
ǫA
/d34/d34❊❊❊❊❊❊❊❊❊❊❊❊❊❊❊❊❊❊
Ψ ⊗idA∨
/d15/d15
1A
ηA
/d60/d60②②②②②②②②②②②②②②②②②② uΨ /d47/d47
ηB
/d34/d34❊❊❊❊❊❊❊❊❊❊❊❊❊❊❊❊❊ B⊗A∨
Ψ r ⊗idA∨
/d79/d79
Φ B ⊗idA∨
/d47/d47
idB∨ ⊗Ψ r∨
/d15/d15
B⊗A∨ cΨ /d47/d47
idB∨ ⊗Ψ r∨
/d15/d15
Ψ r ⊗idA∨
/d79/d79
1A 1A
Tr(Ψ rΨΦ A)≃
Tr(Ψ rΦ B Ψ) ≃Tr(Φ B ΨΨ r)
/d47/d47
Tr(Φ B )
Tr(Φ A)
1A
B⊗B∨
idB ⊗Ψ ∨
/d79/d79
Φ B ⊗idB∨
/d47/d47B⊗B∨
idB ⊗Ψ ∨
/d79/d79
ǫB
/d60/d60②②②②②②②②②②②②②②②②②
24 DA VID BEN-ZVI AND DA VID NADLER
Proposition 3.27. Suppose given objects A,B,C ∈ Acont, endomorphisms ΦA, ΦB, ΦC , a
commutative diagram of continuous morphisms
A
Ψ AC
/d37/d37Ψ AB /d47/d47B
Ψ BC /d47/d47C
and commuting structures
sAB : Ψ ABΦA
∼ /d47/d47 ΦBΨ AB sBC : Ψ BC ΦB
∼ /d47/d47 ΦC Ψ BC sAC : Ψ ACΦA
∼ /d47/d47 ΦC Ψ AC
with an identiﬁcation sAC≃sBCsAB. Then there is a canonical equivalence
Tr(ΨAC,sAC)≃ Tr(ΨBC,sBC )◦ Tr(ΨAB,sAB) : Tr(Φ A) /d47/d47 Tr(ΦC )
Proof. The construction is obtained from following a minor expansion of the d iagram proving
Proposition 3.21. The additional moves needed are commuting the co mmuting structures past
the symmetry m of the trace and the unit and counits of the adjunctions. These all follow
immediately from the 2-categorical interchange law for natural tr ansformations. □
Remark 3.28. The full functoriality of the trace Tr takes roughly the following for m, see [HSS]
for a detailed treatment. Deﬁne the loop categoryLcontA to be the symmetric monoidal ∞-
category with objects consisting of pairs ( A, ΦA) of a dualizable object A∈A equipped with a
(not necessarily continuous) endomorphism Φ A, and morphisms given by pairs (Ψ ,ψ ) as above
with Ψ continuous. Taking traces to extend to a symmetric monoidal functor
Tr :LcontA /d47/d47 ΩA
extending the dimension functor
dim :Acont /d47/d47 ΩA
for constant loops Φ A = idA, and trivial commuting structures ψ = id Ψ .
In order to capture the full cyclic symmetry of the trace Tr, one s hould further extend it
to a homotopical trace valued in Ω A, or in other words, to the appropriate full cyclic bar
construction (of which the above forms only the one-simplices).
.
