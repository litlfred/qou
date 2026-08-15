---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-049-h-points
section_title: "H-points"
section_number: null
pages: 124-124
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
those types are deﬁned by lifting the functions deﬁned on the carrier type (e.g., h-distance is deﬁned by lifting
the distance function deﬁned for elements of CP 1).
theory Poincare
imports Poincare-Lines Poincare-Between Poincare-Distance Poincare-Circles
begin
10.1 H-points
typedef p-point ={z. z∈ unit-disc}
using zero-in-unit-disc
by (rule-tac x =0 h in exI, simp)
setup-lifting type-deﬁnition-p-point
Point zero
lift-deﬁnition p-zero :: p-point is 0 h
by (rule zero-in-unit-disc )
Constructing h-points from complex numbers
lift-deﬁnition p-of-complex :: complex⇒ p-point is λ z. if cmod z < 1 then of-complex z else 0 h
by auto
