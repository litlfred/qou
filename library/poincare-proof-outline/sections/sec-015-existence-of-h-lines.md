---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-015-existence-of-h-lines
section_title: "Existence of h-lines"
section_number: null
pages: 28-29
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
There is an h-line trough every point in the Poincaré model

lemma ex-poincare-line-one-point:
shows 4 I. is-poincare-line | A z € circline-set |
proof (cases z = 0n)
case True
thus ?thesis
by (rule-tac c=2-avis in exI) simp
next
case False
thus ?thesis
by (rule-tac «=poincare-line 0; z in exl) auto
qed

lemma poincare-collinear-singleton [simp]:
assumes u € unit-disc
shows poincare-collinear {u}
using assms
using exz-poincare-line-one-point[of u|
by (auto simp add: poincare-collinear-def)

28
There is an h-line trough every two points in the Poincaré model

lemma ex-poincare-line-two-points:
assumes z 4 w
shows 4 l. is-poincare-line | A z € circline-set 1 A w € circline-set 1
using assms
by (rule-tac z=poincare-line z w in exI, simp)

lemma poincare-collinear-doubleton [simp]:
assumes u € unit-disc v € unit-disc
shows poincare-collinear {u, v}
using assms
using exz-poincare-line-one-point[of u|
using ex-poincare-line-two-points|of u v|
by (cases u = v) (simp-all add: poincare-collinear-def )
