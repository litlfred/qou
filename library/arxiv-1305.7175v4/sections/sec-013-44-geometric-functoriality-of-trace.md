---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-013-44-geometric-functoriality-of-trace
section_title: "Geometric functoriality of trace"
section_number: 4.4
pages: 29-29
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
doc_brief: "NONLINEAR TRACES — W e combine the theory of traces in homotopical algebra with s heaf theory in de- rived algebraic geometry to deduce general ﬁxed point and ch aracter formulas."
---
morphisms FZ : X→ X and FW : Y → Y in Corrk given by respective self-correspondences
X←Z→X and Y ←W→Y .
By an f -morphism from the pair ( X,FZ ) to the pair ( Y,FW ), we mean an identiﬁcation
s :Z ∼ /d47/d47X×Y W
of correspondences from X toY . This in turn induces an identiﬁcation of what might be called
relative traces
Z×Y ×Y Y ∼ /d47/d47X×Y ×Y W
generalizing the relative loop space LXY from the case of the identity correspondences Z =X,
W =Y . We thus obtain a map of traces
τ (f,s ) : Z|∆ X =Z×X×XX /d47/d47Z×Y ×Y Y ∼ /d47/d47X×Y ×Y W /d47/d47Y×Y ×Y W =W|∆ Y
Proposition 4.8. With the preceding setup, the trace map Tr(f,s ) : Tr( FZ )→ Tr(FW ) is
canonically identiﬁed with the geometric map
τ (f,s ) : Z|∆ X
/d47/d47W|∆ Y
Proof. Denote by F : X → Y the morphism given by the graph X ← Γf → Y , and by
Fr :Y →X its right adjoint. We must calculate
Tr(FZ ) /d47/d47 Tr(FrFFZ ) s /d47/d47 Tr(FrFWF )
m(F r,FWF ) /d47/d47 Tr(FWFF r) /d47/d47 Tr(FW )
We have seen that the ﬁrst and fourth morphisms correspond to t he natural geometric maps
Z|∆ X =Z×X×XX /d47/d47Z×X×X (X×Y X)
X×Y ×Y W /d47/d47Y×Y ×Y W =W|∆ Y
induced by the relative diagonal X→X×Y X and given map f :X→Y respectively.
Using associativity, the second map, induced by s, is the natural geometric identiﬁcation
Z×X×X (X×Y X)≃Z×Y ×Y Y ∼ /d47/d47W×Y ×Y X
By Lemma 4.4, the third map, given by the cyclic symmetry, is nothing m ore than the natural
identiﬁcation
W×Y ×Y X ∼ /d47/d47X×Y ×Y W
Thus assembling the above maps we arrive at the composition deﬁning τ (f,s ). □
