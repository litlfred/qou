---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-054-h-betweennes
section_title: "H-betweennes"
section_number: null
pages: 127-127
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lift-deﬁnition p-between :: p-point⇒ p-point⇒ p-point⇒ bool is poincare-between
done
end
11 Poincaré model satisﬁes Tarski axioms
theory Poincare-Tarski
imports Poincare Poincare-Lines-Axis-Intersections Tarski
begin
