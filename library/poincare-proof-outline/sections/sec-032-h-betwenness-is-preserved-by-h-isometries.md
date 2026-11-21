---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-032-h-betwenness-is-preserved-by-h-isometries
section_title: "H-betwenness is preserved by h-isometries"
section_number: null
pages: 77-78
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Since they preserve cross-ratio and inversion, h-isometries (unit disc preserving Mobius transformations and
conjugation) preserve h-betweeness.

lemma unit-disc-fiz-moebius-preserve-poincare-between [simp]:
assumes unit-disc-fix M and u € unit-disc and v € unit-disc and w € unit-disc
shows poincare-between (moebius-pt M u) (moebius-pt M v) (moebius-pt M w) <>
poincare-between uv w
proof (cases u =v V v= w)
case True
thus ?thesis
using assms
unfolding poincare-between-def
by auto
next
case False
moreover
hence moebius-pt Mu 4 moebius-pt M v A moebius-pt M v 4 moebius-pt M w
by auto
moreover
have v # inversion v w ¥ inversion v
using inversion-noteq-unit-disc|of v w]
using inversion-noteq-unit-disc[of v v]
using <v € unit-discy (w € unit-discy
by auto
ultimately
show ?thesis
using assms
using wnit-circle-fiz-moebius-pt-inversion|of M v, symmetric]
unfolding poincare-between-def
by (simp del: unit-circle-fix-moebius-pt-inversion)
qed

lemma conjugate-preserve-poincare-between [simp]:
assumes u € unit-disc and v € unit-disc and w € unit-disc
shows poincare-between (conjugate u) (conjugate v) (conjugate w) <->
poincare-between uv w
proof (cases u =v V v= w)
case True
thus ?thesis
using assms
unfolding poincare-between-def
by auto
next
case False
moreover
hence conjugate u # conjugate v \ conjugate v # conjugate w
using conjugate-inj by blast
moreover
have v # inversion v w ¥ inversion v
using inversion-noteq-unit-disc|of v w]
using inversion-noteq-unit-disc[of v v]
using <v € unit-discy (w € unit-discy

77
by auto
ultimately
show ?thesis
using assms
using conjugate-cross-ratio[of v w inversion v ul
unfolding poincare-between-def
by (metis conjugate-id-iff conjugate-involution inversion-def inversion-sym o-apply)
qed
