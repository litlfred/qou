---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-010-mapping-h-lines-to-x-axis
section_title: "Mapping h-lines to x-axis"
section_number: null
pages: 16-17
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Each h-line in the Poincaré model can be mapped onto the x-axis (by a unit-disc preserving Möbius transfor-
mation).
lemma ex-unit-disc-ﬁx-is-poincare-line-to-x-axis:
assumes is-poincare-line l
shows ∃ M. unit-disc-ﬁx M ∧ moebius-circline M l = x-axis
proof−
from assms obtain u v where u⁄= v u ∈ unit-disc v ∈ unit-disc and{u, v}⊆ circline-set l
using ex-is-poincare-line-points
by blast
then obtain M where∗: unit-disc-ﬁx M moebius-pt M u = 0 h moebius-pt M v ∈ positive-x-axis
using ex-unit-disc-ﬁx-to-zero-positive-x-axis[of u v ]
by auto
moreover
hence{0 h, moebius-pt M v}⊆ circline-set x-axis
16
unfolding positive-x-axis-def
by auto
moreover
have moebius-pt M v ⁄= 0 h
using ‹u⁄= v›∗
by (metis moebius-pt-neq-I )
moreover
have moebius-pt M v ⁄=∞h
using ‹unit-disc-ﬁx M › ‹v∈ unit-disc›
using unit-disc-ﬁx-discI
by fastforce
ultimately
show ?thesis
using ‹is-poincare-line l› ‹{u, v}⊆ circline-set l › ‹unit-disc-ﬁx M ›
using is-poincare-line-0-real-is-x-axis[of moebius-circline M l moebius-pt M v ]
by (rule-tac x =M in exI, force)
qed
When proving facts about h-lines, without loss of generality it can be assumed that h-line is the x-axis (if the
property being proved is invariant under Möbius transformations that ﬁx the unit disc).
lemma wlog-line-x-axis:
assumes is-line: is-poincare-line H
assumes x-axis: P x-axis
assumes preserves: ⋀ M. [ [unit-disc-ﬁx M ; P (moebius-circline M H )] ] =⇒ P H
shows P H
using assms
using ex-unit-disc-ﬁx-is-poincare-line-to-x-axis[of H ]
by auto
