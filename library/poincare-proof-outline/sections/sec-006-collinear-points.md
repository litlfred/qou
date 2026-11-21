---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-006-collinear-points
section_title: "Collinear points"
section_number: null
pages: 7-7
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Points are collinear if they all belong to an h-line.

definition poincare-collinear :: complez-homo set = bool where
poincare-collinear S <—+ (A p. is-poincare-line p \ S C circline-set p)
