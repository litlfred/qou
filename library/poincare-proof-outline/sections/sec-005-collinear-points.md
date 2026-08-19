---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-005-collinear-points
section_title: "Collinear points"
section_number: null
pages: 7-7
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Points are collinear if they all belong to an h-line.
deﬁnition poincare-collinear :: complex-homo set ⇒ bool where
poincare-collinear S←→ (∃ p. is-poincare-line p∧ S⊆ circline-set p )
