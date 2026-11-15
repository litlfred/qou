---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-013-35-functoriality-of-traces
section_title: "Functoriality of traces"
section_number: 3.5
pages: 23-24
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
endomorphisms of dualizable objects. For this purpose we deﬁne a morphism between pairs
A ∈Acont
ΦA ∈EndA(A)
of an object and an endomorphism to consist of a pair
Ψ ∈HomAcont(A, B)
ψ : Ψ ◦ΦA
≃
/ ΦB ◦Ψ
of a morphism and a commuting structure.
Deﬁnition 3.24. For a morphism
(Ψ, ψ) : (A, ΦA) →(B, ΦB)
as above, we deﬁne the induced morphism of traces
Tr(Ψ, ψ) : Tr(ΦA)
/ Tr(ΦB)
to be the composition
Tr(ΦA)
ηΨ / Tr(ΨrΨΦA)
ψ
/ Tr(ΨrΦBΨ)
m(Ψr,ΦBΨ) / Tr(ΦBΨΨr)
ǫΨ / Tr(ΦB)
Remark 3.25. Note that we could alternatively deﬁne a morphism Tr(Ψ, ψ) by applying the
unit ηΨ to the right of ΦA, rotating the trace in the opposite direction, and again using the
counit on the right. It is elementary to give a natural equivalence of the two constructions using
nothing more than the dualizability of A.
Remark 3.26. In parallel with Remark 3.20 about the functoriality of dimensions, it is enlight-
ening to realize the functoriality of traces as a chase through the following diagram
A ⊗A∨
Ψ⊗idA∨

ΦA⊗idA∨
/ A ⊗A∨
ǫA
"❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
Ψ⊗idA∨

1A
ηA
<②
②
②
②
②
②
②
②
②
②
②
②
②
②
②
②
②
②
uΨ
/
ηB
"❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
❊
B ⊗A∨
Ψr⊗idA∨
O
ΦB⊗idA∨
/
idB∨⊗Ψr∨

B ⊗A∨
cΨ
/
idB∨⊗Ψr∨

Ψr⊗idA∨
O
1A
1A
Tr(ΨrΨΦA)≃
Tr(ΨrΦBΨ)≃Tr(ΦBΨΨr)
/
Tr(ΦB)
Tr(ΦA)
1A
B ⊗B∨
idB ⊗Ψ∨
O
ΦB⊗idB∨
/ B ⊗B∨
idB ⊗Ψ∨
O
ǫB
<②
②
②
②
②
②
②
②
②
②
②
②
②
②
②
②
②
24
DAVID BEN-ZVI AND DAVID NADLER
Proposition 3.27. Suppose given objects A, B, C ∈Acont, endomorphisms ΦA, ΦB, ΦC, a
commutative diagram of continuous morphisms
A
ΨAC
%
ΨAB
/ B
ΨBC
/ C
and commuting structures
sAB : ΨABΦA
∼
/ ΦBΨAB
sBC : ΨBCΦB
∼
/ ΦCΨBC
sAC : ΨACΦA
∼
/ ΦCΨAC
with an identiﬁcation sAC ≃sBCsAB. Then there is a canonical equivalence
Tr(ΨAC, sAC) ≃Tr(ΨBC, sBC) ◦Tr(ΨAB, sAB) : Tr(ΦA)
/ Tr(ΦC)
Proof. The construction is obtained from following a minor expansion of the diagram proving
Proposition 3.21. The additional moves needed are commuting the commuting structures past
the symmetry m of the trace and the unit and counits of the adjunctions. These all follow
immediately from the 2-categorical interchange law for natural transformations.
□
Remark 3.28. The full functoriality of the trace Tr takes roughly the following form, see [HSS]
for a detailed treatment. Deﬁne the loop category LcontA to be the symmetric monoidal ∞-
category with objects consisting of pairs (A, ΦA) of a dualizable object A ∈A equipped with a
(not necessarily continuous) endomorphism ΦA, and morphisms given by pairs (Ψ, ψ) as above
with Ψ continuous. Taking traces to extend to a symmetric monoidal functor
Tr : LcontA
/ ΩA
extending the dimension functor
dim : Acont
/ ΩA
for constant loops ΦA = idA, and trivial commuting structures ψ = idΨ.
In order to capture the full cyclic symmetry of the trace Tr, one should further extend it
to a homotopical trace valued in ΩA, or in other words, to the appropriate full cyclic bar
construction (of which the above forms only the one-simplices).
.
