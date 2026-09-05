---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-012-43-geometric-functoriality-of-dimension
section_title: "Geometric functoriality of dimension"
section_number: 4.3
pages: 27-29
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
doc_brief: "NONLINEAR TRACES — W e combine the theory of traces in homotopical algebra with s heaf theory in de- rived algebraic geometry to deduce general ﬁxed point and ch aracter formulas."
---
Proposition 4.3. The graph X ← Γf → Y of any proper morphism f : X → Y gives a
continuous morphism F : X→ Y in Corrprop
k , with right adjoint Fr : Y → X identiﬁed with
the opposite correspondence Y ← Γf→X.
Proof. We construct the unit and counit of the adjunction as follows. Cons ider the composition
FrF :X→X of correspondences
X×Y X
/d122/d122✈✈✈✈✈✈✈✈✈
/d36/d36❍❍❍❍❍❍❍❍❍
Γf
/d126/d126⑥⑥⑥⑥⑥⑥⑥
/d36/d36❍❍❍❍❍❍❍❍❍❍ Γf
/d122/d122✈✈✈✈✈✈✈✈✈✈
/d32/d32❆❆❆❆❆❆❆
X Y X
The unit ηf : idX =X→FrF≃X×Y X is given by the relative diagonal map.
Consider the opposite composition of correspondences
X×XX
/d122/d122✈✈✈✈✈✈✈✈✈
/d36/d36❍❍❍❍❍❍❍❍❍
Γf
/d126/d126⑦⑦⑦⑦⑦⑦⑦
/d36/d36■■■■■■■■■■ Γf
/d122/d122✉✉✉✉✉✉✉✉✉✉
/d32/d32❅❅❅❅❅❅❅
Y X Y
The counit ǫf :FF r≃X→ idY =Y is given by f itself.
The standard identities are easily veriﬁed by identifying the resulting composite map
Γf /d47/d47 Γf×Y Γf×X Γf /d47/d47 Γf
of correspondences with the identity. □
Lemma 4.4. Let FZ : X→ Y and FW : Y → X be morphisms in Corrk given by respective
correspondencesX←Z→Y and Y←W→X. Then the canonical equivalence
m(FW,FZ ) : Tr(FW◦FZ ) ∼ /d47/d47 Tr(FZ◦FW )
is given by the composition of evident geometric identiﬁcat ions
(Z×Y W )×X×XX ∼ /d47/d47W×X×Y Z ∼ /d47/d47Z×Y ×X W ∼ /d47/d47 (W×XZ)×Y ×Y Y
28 DA VID BEN-ZVI AND DA VID NADLER
Proof. Returning to the deﬁnition and using our previous identiﬁcations, ob serve thatm(FZ,FW )
is calculated by commutativity of the diagram of correspondences
X×X
Z×X /d47/d47
X×W
/d28/d28✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽ Y×X
W ×X /d47/d47
Y ×W
/d28/d28✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽ X×X
X
/d35/d35●●●●●●●●●
pt
X
/d59/d59①①①①①①①①①
Y /d35/d35●●●●●●●●● pt
Y×Y W ×Y
/d47/d47X×Y X×Y
/d47/d47Y×Y
Y
/d59/d59①①①①①①①①①
Following the top edge, we see Tr(FW◦FZ )≃ (Z×YW )×X×XX. Following the bottom edge,
we see Tr(FZ◦FW )≃ (W×XZ)×Y ×YY . Moving from the top to bottom edge via the successive
equivalences of the three commuting squares, one ﬁnds the three successive equivalences in the
assertion of the lemma. □
Proposition 4.5. Suppose f : X→ Y is a proper morphism, and F : X→ Y denotes the
induced morphism in Corrprop
k given by the graph X← Γf→ Y . Then dim(F ) : dim( X)→
dim(Y ) is canonically identiﬁed with the S1-equivariant morphismLf :LX→LY .
Proof. Denote by Fr :Y →X the right adjoint to F . We must calculate
dim(X) /d47/d47 Tr(FrF )
m(F r,F ) /d47/d47 Tr(FF r) /d47/d47 dim(Y )
We have seen that the ﬁrst and third morphisms correspond to the natural geometric maps
LX≃X×X×XX /d47/d47 (X×Y X)×X×XX X ×Y ×Y Y /d47/d47Y×Y ×Y Y ≃LY
induced by the relative diagonal X → X×Y X and given map f : X → Y respectively.
Furthermore, by Lemma 4.4, the middle map is the natural geometric identiﬁcation
(X×Y X)×X×XX ∼ /d47/d47X×Y ×Y Y
Altogether, the composition is easily identiﬁed with the loop map Lf :LX→LY . □
Remark 4.6. It follows from the proposition that the loop map Lf :LX→LY must be proper
when the given map f :X→Y is proper. Let us note why this is true geometrically from the
factorizationLX→L XY→LY appearing in the proof.
First, the natural morphism LX→L XY is the restriction along the diagonal X→X×X
of the relative diagonal X→X×Y X. The relative diagonal is a closed embedding since f is
proper, and hence the natural morphism LX→L XY is as well. Second, the natural morphism
LXY→LY is the restriction along the diagonal Y→Y×Y of the proper morphism f :X→Y
and thus is proper as well. Altogether, we see that Lf :LX→LY is itself proper.
Remark 4.7. One can invoke the cobordism hypothesis with singularities to endow t he mor-
phism dim(F ) : dim(X)→ dim(Y ) with a canonical S1-equivariant structure, and it will agree
with the canonical geometric S1-equivariant structure on the map Lf :LX→L Y under the
identiﬁcation of the proposition.
NONLINEAR TRACES 29
