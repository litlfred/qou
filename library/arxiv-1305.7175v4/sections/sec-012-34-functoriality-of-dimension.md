---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-012-34-functoriality-of-dimension
section_title: "Functoriality of dimension"
section_number: 3.4
pages: 21-23
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
objects and continuous or right dualizable morphisms (morphisms that are left duals).
Deﬁnition 3.19. Let Ψ : A →B denote a morphism in Acont with right adjoint Ψr : B →A.
We deﬁne the induced morphism of dimensions
dim(Ψ) : dim(A)
/ dim(B)
to be the composition
Tr(idA)
ηΨ / Tr(Ψr ◦Ψ)
m(Ψr,Ψ)
/ Tr(Ψ ◦Ψr)
ǫΨ / Tr(idB)
Remark 3.20. In other words, the morphism dim(Ψ) is deﬁned by the following diagram
A ⊗A∨
Ψ⊗idA∨

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
Ψr⊗idA
O
cΨ
/
idB∨⊗Ψr∨

1A
1A
Tr(ΨrΨ)≃Tr(ΨΨr)
/
dim(B)
dim(A)
1A
B ⊗B∨
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
22
DAVID BEN-ZVI AND DAVID NADLER
Following the top and bottom edge, we ﬁnd the respective deﬁnitions of dim(A) and dim(B).
The unit ηΨ deﬁnes a morphism from the top edge to the top zig-zag. The counit ǫΨ deﬁnes a
morphism from the bottom zig-zag to the bottom edge. The passage from the top to bottom
zig-zag is given by the construction m(Ψr, Ψ) and the identiﬁcation
Tr(Ψr∨◦Ψ∨) ≃Tr((Ψ ◦Ψr)∨) ≃Tr(Ψ ◦Ψr)
Proposition 3.21. For a diagram
A
Φ
/ B
Ψ
/ C
within Acont, there is a canonical equivalence
dim(Ψ ◦Φ) ≃dim(Ψ) ◦dim(Φ) : dim(A)
/ dim(C)
Proof. The equivalence is given by ﬁlling in the following diagram
dim(A)
ηΦ
/
ηΨ
&◆
◆
◆
◆
◆
◆
◆
◆
◆
◆
◆
Tr(ΦrΦ)
m
/
ηΨ

Tr(ΦΦr)
ǫΦ
/
ηΨ

dim(B)
ηΨ

Tr(ΦrΨrΨΦ)
m
/
m
(P
P
P
P
P
P
P
P
P
P
P
P
Tr(ΨrΨΦΦr)
ǫΦ
/
m

Tr(ΨrΨ)
m

Tr(ΨΦΦrΨr)
ǫΦ
/
ǫΨΦ
'❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
❖
Tr(ΨΨr)
ǫΨ

dim(C)
Along the three boundary edges, we ﬁnd the deﬁnitions of dim(Φ), dim(Ψ) and dim(ΨΦ)
respectively.
The two corner triangles are given by the composition identities for adjoints (for example,
at the top left, relating the adjoint of ΦΨ with the composition of adjoints of Ψ and Φ).
The middle triangle is given by the identity of Lemma 3.18.
The top right square is given by taking traces of the evident commutative diagram of endo-
morphisms
ΦΦr ⊗IdB∨

/ IdB ⊗IdB∨

ΦΦr ⊗(ΨrΨ)∨
/ IdB ⊗(ΨrΨ)∨
and using the canonical identiﬁcation Tr(F) = Tr(F ∨) for any dualizable morphism.
Finally, the two remaining commuting squares are given by the functoriality of the cyclic
rotation of the trace in its two arguments. For instance, in the top left square, we may either
rotate Tr(Φr ◦(IdA ◦Φ)) and then apply the unit ηΨ : IdA →ΨrΨ or ﬁrst apply the unit and
then rotate.
This concludes the construction.
□
Since we have an evident equivalence dim(1A) ≃1A for the unit 1A ∈A, we have the
following specialization of Proposition 3.21 in which we adopt suggestive notation.
NONLINEAR TRACES
23
Corollary 3.22 (Abstract Grothendieck-Riemann-Roch). Let A, B ∈Acont and V : 1A →A
and π∗: A →B morphisms in Acont. Then the following diagram naturally commutes
1A
dim(π∗V )
#●
●
●
●
●
●
●
●
●
dim(V )/ dim(A)
dim(π∗)

dim(B)
Remark 3.23. One can show along the same lines as the proposition that taking dimensions
extends to a symmetric monoidal functor
dim : Acont
/ ΩA.
