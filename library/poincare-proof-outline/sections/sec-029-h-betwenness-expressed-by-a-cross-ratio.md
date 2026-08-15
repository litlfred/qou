---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-029-h-betwenness-expressed-by-a-cross-ratio
section_title: "H-betwenness expressed by a cross-ratio"
section_number: null
pages: 77-77
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
---
The point v is h-between u and w if the cross-ratio between the pairs u and w and v and inverse of v is real
and negative.
deﬁnition poincare-between :: complex-homo⇒ complex-homo⇒ complex-homo⇒ bool where
poincare-between u v w ←→
u = v∨ v = w∨
(let cr = cross-ratio u v w (inversion v )
in is-real (to-complex cr )∧ Re (to-complex cr ) < 0 )
