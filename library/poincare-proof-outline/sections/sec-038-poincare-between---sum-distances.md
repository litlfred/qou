---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-038-poincare-between---sum-distances
section_title: "Poincare between - sum distances"
section_number: null
pages: 89-94
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Another possible definition of the h-betweenness relation is given in terms of h-distances between pairs of points.
We prove it as a characterization equivalent to our cross-ratio based definition.

lemma poincare-between-sum-distances-x-axis-u0v:

assumes of-complez u' € unit-disc of-complex v' € unit-disc

assumes is-real u’ u’ 4 0 v' 4 0

shows poincare-distance (of-complex u') 0; + poincare-distance 0; (of-complex v') = poincare-distance (of-complex
u’) (of-complex v') —+

is-real v' \ Re u’ * Re v' < 0 (is ?P wu’ v' <> ?Qu' v’)

proof—

have Re u' 4 0

89
using <is-real uy «u' 4 0»
using complex-eq-if-Re-eq
by simp

let ?u = cmod u’ and ?v = cmod v' and ?uv = cmod (u’ — v’)
have disc: ?u? < 1 ?v? < 1
using wunit-disc-cmod-square-lt-1[OF assms(1)]
using unit-disc-cmod-square-lt-1[OF assms(2)]
by auto
have poincare-distance (of-complex u') 0;, + poincare-distance 0p, (of-complez v') =
arcosh (((1 + ?u?) * (1 4+ ?u?) + 4 * ?u* 2u) / ((1 — ?u?) * (1 — ?v7))) (is - = arcosh ?r1)
using poincare-distance-formula-zero-sum|[OF assms(1—2)]
by (simp add: Let-def)
moreover
have poincare-distance (of-complex u') (of-complex v’) =
arcosh (((1 — ?u?) * (1 — ?u?) + 2 ?uv?) / ((1 — ?u?) * (1 — ?v?))) (is - = arcosh ?r2)
using disc
using poincare-distance-formula|OF assms(1—2)]
by (subst add-divide-distrib) simp
moreover
have arcosh ?r1 = arcosh ?r2 <> ?Q u' v’
proof
assume arcosh ?r1 = arcosh ?r2
hence ?r1 = ?r2
proof (subst (asm) arcosh-eq-iff)
show ?r1 > 1
proof—
have (1 — ?u”) « (1 — ?v”) < (1 + ?u?) * (1 + 20?) + 4 * Pu x Pu
by (simp add: field-simps)
thus ?thesis
using disc
by simp
qed
next
show ?r2 > 1
using disc
by simp
qed
hence ({ + ?u?) * (1 + ?u*) + 4 * ?u* ?u = (1 — ?u) * (1 — P07) + 2 * Pur?
using disc
by auto
hence (cmod (u’ — v’))? = (cmod u’ + emod v’)?
by (simp add: field-simps power2-eq-square)
hence +: Re u’ * Re v’ + |Re u'| * sqrt ((Imv’)? + (Re v’)?) = 0
using <is-real u’>
unfolding cmod-power2 cmod-def
by (simp add: field-simps) (simp add: power2-eq-square field-simps)
hence sqrt ((Im v’)? + (Re v')?) = |Re v'|
using (Re u’ 4 0) «v' 4 0>
by (smt complex-neq-0 mult.commute mult-cancel-right mult-minus-left real-sqrt-gt-0-iff)
hence Im v' = 0
by (smt Im-eq-0 norm-complez-def )
moreover
hence Re u’ * Re v' = — |Re u'| « |Re v'|
using *
by simp
hence Re u’ * Rev’ < 0
using (Re u’ 4 0) «v' 4 0>
by (simp add: <is-real v'» complex-eq-if-Re-eq)
ultimately
show ?Q u' v'
by simp
next
assume ?Q u’ v’
hence is-real v’ Re u’ * Re v' < 0
by auto

90
have ?r1 = ?r2
proof (cases Re u' > 0)
case True
hence Re v' < 0
using «Re u’ « Rev’ < 0>
by (smt zero-le-mult-iff)
show ?thesis
using disc <is-real u’) <is-real v'»
using (Re u’ > 0) «Re v' < 0»
unfolding cmod-power2 cmod-def
by simp (simp add: power2-eq-square field-simps)
next
case False
hence Re u’ < 0
using (Re u’ 4 0>
by simp
hence Re v' > 0
using «Re u’ « Rev’ < 0>
by (smt zero-le-mult-iff)
show ?thesis
using disc <is-real u’> <is-real vy
using (Re u’ < 0> (Re v' > 0>
unfolding cmod-power2 cmod-def
by simp (simp add: power2-eq-square field-simps)
qed
thus arcosh ?r1 = arcosh ?r2
by metis
qed
ultimately
show ?thesis
by simp
qed

Different proof of the previous theorem relying on the cross-ratio definition, and not the distance formula. We
suppose that this could be also used to prove the triangle inequality.

lemma poincare-between-sum-distances-x-axis-u0v-different-proof :
assumes of-complez u' € unit-disc of-complex v' € unit-disc
assumes is-real u' u' £ 0 v' # 0 is-real v’
shows poincare-distance (of-complex u') 0; + poincare-distance 0; (of-complex v') = poincare-distance (of-complex
u’) (of-complex v') <>
Reu'* Rev’ < 0 (is ?P u! v' <> ?Qu'v’)
proof—
have —1 < Reu’ Reu'< 1 Reu' 40
using assms
by (auto simp add: cmod-eq-Re complex-eq-if-Re-eq)
have —1 < Rev’ Rev’ < 1Rev' £0
using assms
by (auto simp add: cmod-eq-Re complex-eq-if-Re-eq)

have |In (Re ((1 — u’) / (1 + w)))| + [In (Re (1 — 0’) / (1 + 0)))| =
[ln (Re ((1 + uw’) * (1 — v’) / ((1 — wu’) * (1 + 0’))))| —O Re u' * Rev’ < 0 (is |In Pal| + |In ?a2| = [In ?a3|
>)
proof—
have 1: 0 < fal In ?al > 0 +> Reu' < 0
using (Re u’ < 1) «Re u’ > —1)> ¢is-real u’>
using complex-is-Real-iff
by auto
have 2: 0 < ?a2 In ?a2 > 0 ++ Rev'< 0
using (Re v’ < 1) «Rev! > —1)> ¢is-real v’»
using complex-is-Real-iff
by auto
have 3: 0 < ?a3 In ?a3 > 0 ++ Rev'< Reu’
using ‘Re u’ < 1) «Re u’ > —1> ¢is-real wu’
using (Re v’ < 1) «Rev! > —1)> ¢is-real v’»
using complex-is-Real-iff
by auto (simp add: field-simps)+

91
show ?thesis
proof
assume «: Re u’ « Re v' < 0
show |In ?a1| + |ln ?a2| = |In 2a3|
proof (cases Re u' > 0)
case True
hence Re v' < 0
using *
by (smt mult-nonneg-nonneg)
show ?thesis
using 1 23 «(Re u'> 0) «Re v' < 0»
using (Re u’ < 1) (Re u’ > —1)> <is-real uy
using (Re v’ < 1) «Rev! > —1> ¢is-real v’>
using complex-is-Real-iff
using In-div In-mult
by simp
next
case False
hence Re v’ > 0 Re u'’ < 0
using *
by (smt zero-le-mult-iff )+
show ?thesis
using 1 23 «Re u' < 0) ‘Rev’ > 0»
using (Re u’ < 1> (Re u’ > —1> <is-real uy
using ‘Re v’ < 1) (Re v’ > —1» <is-real v’»
using complex-is-Real-iff
using In-div In-mult
by simp
qed
next
assume «: |In ?a1| + |In ?a2| = |In ?a3|
{
assume Re u’ > 0 Re v' > 0
hence False
using « 123
using (Re u’ < 1) «Re u’ > —1» <is-real u’
using (Re v’ < 1) «Rev! > —1> ¢is-real v’>
using complex-is-Real-iff
using In-mult In-div
by (cases Re v' < Re u’) auto

}

moreover
{
assume Re u’ < 0 Re v' < 0
hence False
using « 123
using (Re u’ < 1> (Re u’ > —1> <is-real uy
using ‘Re v’ < 1) (Re v’ > —1» <is-real v’»
using complex-is-Real-iff
using In-mult In-div
by (cases Re v' < Re u’) auto
}
ultimately
show Re u’* Rev’ < 0
using (Re u’ 4 0) ‘Re v' # 0»
by (smt divisors-zero mult-le-0-iff)
qed
qed
thus ?thesis
using assms
apply (subst poincare-distance-sym, simp, simp)
apply (subst poincare-distance-zero-x-axis, simp, simp add: circline-set-x-axis)
apply (subst poincare-distance-zero-x-axis, simp, simp add: circline-set-x-axis)
apply (subst poincare-distance-x-axis-x-axis, simp, simp, simp add: circline-set-x-axis, simp add: circline-set-x-axis)
apply simp
done

92
qed

lemma poincare-between-sum-distances:
assumes u € unit-disc and v € unit-disc and w € unit-disc
shows poincare-between uv w <->
poincare-distance uv + poincare-distance v w = poincare-distance uw (is ?P’ uv w)
proof (cases u = v)
case True
thus ?thesis
using assms
by simp
next
case False
have V w. w € unit-disc —+ (poincare-between uv w <—> poincare-distance uv + poincare-distance v w = poincare-distance
uw) (is ?P uv)
proof (rule wlog-positive-z-azis)
fix x
assume is-real x 0 < Rex Rex < 1
have of-complex x € circline-set x-axis
using <is-real x»
by (auto simp add: circline-set-x-azis)

have of-complex x € unit-disc
using <is-real z) (0 < Rex» (Rex < 1>
by (simp add: cmod-eq-Re)

have « # 0
using <is-real z» «Re x > 0»
by auto

show ?P (of-complez x) On
proof (rule alll, rule imp!)
fix w
assume w € unit-disc
then obtain w’ where w = of-complez w'
using inf-or-of-complez|of w]
by auto

show ?P’ (of-complex x) 0, w
proof (cases w = 0;)
case True
thus ?thesis
by simp
next
case False
hence w’ 4 0
using <w = of-complez w’>
by auto

show ?thesis
using <is-real 2» (x # 0> «w = of-complez wy «w' 4 0»
using <of-complex x € unit-discy «w € unit-discy
apply simp
apply (subst poincare-between-a-axis-u0v, simp-all)
apply (subst poincare-between-sum-distances-z-axis-u0v, simp-all)
done
qed
qed
next
show v € unit-disc u € unit-disc
using assms
by auto
next
show v 4 u
using <u 4 v)
by simp
next
fix Muv
assume *: unit-disc-fix M u € unit-disc v € unit-disc u # v and
ax: ?P (moebius-pt M v) (moebius-pt M u)
show ?P vu
proof (rule alll, rule imp!)
fix w
assume w € unit-disc
hence moebius-pt M w € unit-disc
using (unit-disc-fir My
by auto
thus ?P’ vuw
using <u € unit-discy «v € unit-discy (w € unit-disc» <unit-disc-fix M»>
using **[rule-format, of moebius-pt M wv]
by auto
qed
qed
thus ?thesis
using assms
by simp
qed
