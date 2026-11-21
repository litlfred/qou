---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-018-transformations-of-constructed-lines
section_title: "Transformations of constructed lines"
section_number: null
pages: 31-32
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Unit dics preserving Mobius transformations preserve the h-line construction

lemma unit-disc-fit-preserve-poincare-line |simp|:
assumes unit-disc-fix M u € unit-disc v € unit-disc u # v
shows poincare-line (moebius-pt M u) (moebius-pt M v) = moebius-circline M (poincare-line u v)
proof (rule unique-poincare-line[symmetric])
show moebius-pt M u 4 moebius-pt Mv
using <u 4 v)
by auto
next
show moebius-pt M u € circline-set (moebius-circline M (poincare-line u v))
moebius-pt M v € circline-set (moebius-circline M (poincare-line u v))
unfolding circline-set-def
using mocbius-circline[of M poincare-line uv] «u # v>
by auto
next
from assms(1) have unit-circle-fix M
by simp
thus is-poincare-line (moebius-circline M (poincare-line u v))
using wnit-circle-fiz-preserve-is-poincare-line assms
by auto
next
show moebius-pt M u € unit-disc moebius-pt M v € unit-disc
using assms(2—3) unit-disc-fiz-iff|OF assms(1)]
by auto
qed

Conjugate preserve the h-line construction

lemma conjugate-preserve-poincare-line [simp]:
assumes u € unit-disc v € unit-disc u # v
shows poincare-line (conjugate u) (conjugate v) = conjugate-circline (poincare-line wu v)
proof—
have conjugate u # conjugate v
using <u 4 v)
by (auto simp add: conjugate-inj)
moreover
have conjugate u € unit-disc conjugate v € unit-disc
using assms
by auto
moreover
have conjugate u € circline-set (conjugate-circline (poincare-line u v))
conjugate v € circline-set (conjugate-circline (poincare-line u v))
using <u 4 v)
by simp-all
moreover
have is-poincare-line (conjugate-circline (poincare-line u v))
using is-poincare-line-poincare-line|OF <u # v>]
by simp
ultimately
show ?thesis
using unique-poincare-line|of conjugate u conjugate v conjugate-circline (poincare-line u v)|
by simp
qed
