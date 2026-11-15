---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-051-h-points
section_title: "H-points"
section_number: null
pages: 124-124
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
those types are defined by lifting the functions defined on the carrier type (e.g., h-distance is defined by lifting
the distance function defined for elements of CP).

theory Poincare
imports Poincare-Lines Poincare-Between Poincare-Distance Poincare-Circles
begin
10.1 H-points
typedef p-point = {z. z € unit-disc}
using zero-in-unit-disc
by (rule-tac c=0;, in el, simp)
setup-lifting type-definition-p-point
Point zero

lift-definition p-zero :: p-point is On
by (rule zero-in-unit-disc)

Constructing h-points from complex numbers

lift-definition p-of-complex :: complex = p-point is X z. if cmod z < 1 then of-complex z else 0,
by auto
