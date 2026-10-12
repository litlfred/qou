---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model"
section_id: sec-006-collinear-points
section_title: "Collinear points"
section_number: null
pages: 7-7
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
---
Points are collinear if they all belong to an h-line.
deﬁnition poincare-collinear :: complex-homo set ⇒bool where
poincare-collinear S ←→(∃p. is-poincare-line p ∧S ⊆circline-set p)
4.1.2
