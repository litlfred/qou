---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-059-segment-construction-axiom
section_title: "Segment construction axiom"
section_number: null
pages: 138-140
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma segment-construction:
assumes «x € unit-disc and y € unit-disc
assumes a € unit-disc and b € unit-disc
shows J z. z € unit-disc A poincare-between x y z  poincare-distance y z = poincare-distance a b
proof—
obtain d where d: d = poincare-distance a b
by auto
have d > 0
using assms

138
by (simp add: d poincare-distance-ge0)

have 4 z. z € unit-disc \ poincare-between x y z /\ poincare-distance y z = d (is ?P x y)
proof (cases t = y)
case True
have 4 z. z € unit-disc \ poincare-distance « z = d
proof (rule wlog-zero)
show 4 z. z € unit-disc \ poincare-distance 0, z = d
using ex-2z-axis-poincare-distance-negative[of d| «d > 0»
by blast
next
show « € unit-disc
by fact
next
fix au
assume u € unit-disc cmod a < 1
assume Jz. z € unit-disc \ poincare-distance (moebius-pt (blaschke a) u) z = d
then obtain z where «: z € unit-disc poincare-distance (moebius-pt (blaschke a) u) z = d
by auto
obtain z’ where z’: z = moebius-pt (blaschke a) z' z' € unit-disc
using <z € unit-discy
using unit-disc-fiz-iff [of blaschke a] «cmod a < 1>
using blaschke-unit-disc-fiz|of a]
by blast

show Jz. z € unit-disc \ poincare-distance uz = d
using * 2’ (uw: unit-disc»
using blaschke-unit-disc-fiz[of a] «cmod a < 1»
by (rule-tac =z’ in exI, simp)
qed
thus ?thesis
using (x = y>
unfolding poincare-between-def
by auto
next
case False
show ?thesis
proof (rule wlog-positive-x-azis[where P=. y x. ?P x y])
fix x
assume is-real x 0 < Rex Rex < 1

then obtain z where z: is-real z Re z < 0 — 1 < Re z of-complex z € unit-disc
of-complexr z € unit-disc of-complez z € circline-set x-axis poincare-distance On (of-complez z) = d
using ex-2z-axis-poincare-distance-negative[of d| «d > 0»
by auto

have poincare-between (of-complex x) 0; (of-complex z)
proof (cases z = 0)
case True
thus ?thesis
unfolding poincare-between-def
by auto
next
case False
have x # 0
using <is-real z» «Re x > 0»
by auto
thus ?thesis
using poincare-between-z-axis-u0v|of x 2]
using z <is-real z) «x # 0) «Re x > 0» False
using complex-eq-if-Re-eq mult-pos-neg
by fastforce
qed
thus ?P (of-complex x) 0n
using <poincare-distance 0», (of-complex z) = d> (of-complex z € unit-disc»
by blast

139
next
show « € unit-disc y € unit-disc
by fact+
next
show y # x using (xz # y> by simp
next
fix Muv
assume unit-disc-fic M u € unit-disc v € unit-disc u # v
assume ?P (moebius-pt M v) (moebius-pt M u)
then obtain z where «: z € unit-disc poincare-between (moebius-pt M v) (moebius-pt M u) z poincare-distance
(moebius-pt Mu) z = d
by auto
obtain z’ where z’: z = moebius-pt M z' z' € unit-disc
using <z € unit-discy
using unit-disc-fiz-iff [of M] <unit-disc-fix M»
by blast
thus ?P vu
using * <u € unit-disc) (v € unit-disc) ‘unit-disc-fir M>
by auto
qed
qed
thus ?thesis
using assms d
by auto
qed
