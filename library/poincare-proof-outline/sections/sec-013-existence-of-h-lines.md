---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-013-existence-of-h-lines
section_title: "Existence of h-lines"
section_number: null
pages: 28-29
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
There is an h-line trough every point in the Poincaré model
lemma ex-poincare-line-one-point:
shows∃ l. is-poincare-line l∧ z∈ circline-set l
proof (cases z = 0 h)
case True
thus ?thesis
by (rule-tac x =x-axis in exI ) simp
next
case False
thus ?thesis
by (rule-tac x =poincare-line 0 h z in exI ) auto
qed
lemma poincare-collinear-singleton [simp]:
assumes u∈ unit-disc
shows poincare-collinear{u}
using assms
using ex-poincare-line-one-point[of u ]
by (auto simp add : poincare-collinear-def)
28
There is an h-line trough every two points in the Poincaré model
lemma ex-poincare-line-two-points:
assumes z⁄= w
shows∃ l. is-poincare-line l∧ z∈ circline-set l ∧ w∈ circline-set l
using assms
by (rule-tac x =poincare-line z w in exI, simp)
lemma poincare-collinear-doubleton [simp]:
assumes u∈ unit-disc v ∈ unit-disc
shows poincare-collinear{u, v}
using assms
using ex-poincare-line-one-point[of u ]
using ex-poincare-line-two-points[of u v ]
by (cases u = v) ( simp-all add : poincare-collinear-def)
