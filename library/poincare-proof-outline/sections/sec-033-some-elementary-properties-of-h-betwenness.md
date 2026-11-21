---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-033-some-elementary-properties-of-h-betwenness
section_title: "Some elementary properties of h-betwenness"
section_number: null
pages: 78-78
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma poincare-between-nonstrict [simp]:
shows poincare-between u u v and poincare-between u vv
by (simp-all add: poincare-between-def)

lemma poincare-between-sandwich:
assumes u € unit-disc and v € unit-disc
assumes poincare-between uv u
shows u = v
proof (rule ccontr)
assume 7— thesis
thus False
using assms
using inversion-noteg-unit-disc[of v u]
using cross-ratio-1[{of v u inversion v]
unfolding poincare-between-def Let-def
by auto
qed

lemma poincare-between-rev:
assumes u € unit-disc and v € unit-disc and w € unit-disc
shows poincare-between u v w <—> poincare-between wv u
using assms
using inversion-noteg-unit-disc|of v w]
using inversion-noteq-unit-disc|of v ul
using cross-ratio-commute-13[of uv w inversion v]
using cross-ratio-not-inf [of w inversion v v ul
using cross-ratio-not-zero|of w v u inversion v]
using inf-or-of-complez|of cross-ratio w v u (inversion v)]
unfolding poincare-between-def
by (auto simp add: Let-def Im-complex-div-eq-0 Re-divide divide-less-0-iff)
