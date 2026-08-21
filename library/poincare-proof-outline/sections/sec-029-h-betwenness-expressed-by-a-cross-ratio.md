---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-029-h-betwenness-expressed-by-a-cross-ratio
section_title: "H-betwenness expressed by a cross-ratio"
section_number: null
pages: 77-77
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
The point v is h-between u and w if the cross-ratio between the pairs u and w and v and inverse of v is real
and negative.
deﬁnition poincare-between :: complex-homo⇒ complex-homo⇒ complex-homo⇒ bool where
poincare-between u v w ←→
u = v∨ v = w∨
(let cr = cross-ratio u v w (inversion v )
in is-real (to-complex cr )∧ Re (to-complex cr ) < 0 )
