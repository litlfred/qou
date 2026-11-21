---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-012-mapping-h-lines-to-x-axis
section_title: "Mapping h-lines to x-axis"
section_number: null
pages: 16-17
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Each h-line in the Poincaré model can be mapped onto the x-axis (by a unit-disc preserving Mobius transfor-
mation).

lemma ez-unit-disc-fix-is-poincare-line-to-x-avis:
assumes is-poincare-line |
shows 3 M. unit-disc-fix M A moebius-circline M | = z-axis
proof—
from assms obtain u v where u # v u € unit-disc v € unit-disc and {u, v} C circline-set |
using ez-is-poincare-line-points
by blast
then obtain M where «: unit-disc-fix M moebius-pt M u = 0n moebius-pt M v € positive-x-axis
using ex-unit-disc-fix-to-zero-positive-z-azis[of u v]
by auto
moreover
hence {0;, moebius-pt M v} C circline-set z-axis

16
unfolding positive-x-azis-def
by auto

moreover

have moebius-pt Mv # On
using <u # v) *
by (metis moebius-pt-neg-1)

moreover

have moebius-pt Mv 4 on
using (unit-disc-fir M> (v © unit-discy
using unit-disc-fir-discl
by fastforce

ultimately

show ?thesis
using <is-poincare-line ly «{u, v} C circline-set ly <unit-disc-fix M>
using is-poincare-line-0-real-is-z-axis|of moebius-circline M 1 moebius-pt M v]
by (rule-tac c=M in eal, force)

qed

When proving facts about h-lines, without loss of generality it can be assumed that h-line is the x-axis (if the
property being proved is invariant under Mobius transformations that fix the unit disc).

lemma wlog-line-x-azis:
assumes is-line: is-poincare-line H
assumes «z-axis: P x-axis
assumes preserves: /\ M. [unit-disc-fix M; P (moebius-circline M H)] => P H
shows P H
using assms
using ex-unit-disc-fiz-is-poincare-line-to-x-axis|of H]
by auto
