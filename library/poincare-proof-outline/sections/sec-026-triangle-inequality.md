---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-026-triangle-inequality
section_title: "Triangle inequality"
section_number: null
pages: 65-67
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma poincare-distance-formula-zero-sum:
assumes u € unit-disc and v € unit-disc
shows poincare-distance u 0; + poincare-distance 0, v =
(let u’ = cmod (to-complex u); v' = cmod (to-complez v)
in arcosh (((1 + uw?) * (1 + 0?) + 4 «ul v’) / ((1 — wu?) * (1 — v”))))
proof—
obtain wu’ v’ where wu: u’ = to-complex u v' = to-complex v
by auto
have uv’: u = of-complex u' v = of-complex v'
using wv assms inf-or-of-complez|of u] inf-or-of-complez|of v]
by auto

let ?u' = cmod u' and ?v' = cmod v’

have disc: ?u? < 1 ?v” < 1
using wnit-disc-cmod-square-lt-1[OF <u € unit-disc>]
using unit-disc-cmod-square-lt-1[OF <v € unit-discy] uv
by auto
thm arcosh-add
have arcosh (1 + 2 *« ?u? / (1 — ?u)) + arcosh (1 + 2 * ?u? / (1 — %0”)) =
arcosh (((1 + ?u”) * (1 + ?u?) + 4 * Pu’ * 20’) / ((1 — ?u?) * (1 — ?u”))) (is arcosh 2ll + arcosh ?rr =
arcosh ?r)
proof (subst arcosh-add)
show 71 > 1 ?rr>1
using disc
by auto
next
show arcosh ((1 + 2 * ?u? / (1 — ?u?)) * (1+ 2% Pu? / (1 — ?u)) +
sqrt (((1 + 2 * ?u? / (1 — ?u”))? — 1) * ((1 + 2 * Pu? / (1 — %v?))? — 1))) =

arcosh ?r (is arcosh ?l = -)
proof —

have 1 + 2 * ?u? / (1 — ?u?) = (1 + Pu?) / (1 — 20?)
using disc
by (subst add-divide-eq-iff , simp-all)

moreover

have 1 + 2% ?v? / (1 — %”) = (1 + ?u”) / (1 — ?0”)
using disc
by (subst add-divide-eq-iff , simp-all)

moreover

have sqrt (((1 + 2 * ?u? / (1 — ?u"))? — 1) * ((1 + 2 * 2? / (1 — %))? — 1)) =
(4 * ?u!* ?u') / ((1 — ?u") * (1 — ?0”)) (is sqrt ?s = ?t)

proof—
have ?s = ?t?
using disc

apply (subst add-divide-eq-iff, simp)+
apply (subst power-divide)+
apply simp
apply (subst divide-diff-eq-iff , simp)+
apply (simp add: power2-eq-square field-simps)
done
thus ?thesis

using disc
by simp

qed

ultimately

have #1 = ?r
using disc
by simp (subst add-divide-distrib, simp)
thus ?thesis
by simp
qed
qed
thus ?thesis
using wv’ assms
using poincare-distance-formula
by (simp add: Let-def)
qed

lemma poincare-distance-triangle-inequality:
assumes u € unit-disc and v € unit-disc and w € unit-disc
shows poincare-distance u v + poincare-distance v w > poincare-distance uw (is ?P’ uv w)
proof—
have V w. w € unit-disc —> ?P'uvw (is ?P v u)
proof (rule wlog-z-axis;where P=?P})
fix x
assume is-real zt 0 < Rex Rex < 1
hence of-complez « € unit-disc
by (simp add: cmod-eq-Re)

show ?P 0), (of-complex x)
proof safe
fix w
assume w € unit-disc
then obtain w’ where w: w = of-complex w’
using inf-or-of-complez|of w]
by auto

let ?2z = cmod x and ?w = cmod w' and ?xw = cmod (x — w’)

have disc: ?a? < 1 ?w? < 1
using unit-disc-cmod-square-lt-1[OF <of-complex x € unit-disc»|
using unit-disc-cmod-square-lt-1[OF «w € unit-disc>| w
by auto

have poincare-distance (of-complex x) On + poincare-distance 0, w =
arcosh (((1 + ?x7) * (1 + ?w?) + 4 * 2x * ?w) / ((1 — ?1*) * (1 — ?w?))) (is - = arcosh ?r1)
using poincare-distance-formula-zero-sum|[OF <of-complez x € unit-disc» «w € unit-discy| w
by (simp add: Let-def)
moreover
have poincare-distance (of-complez x) (of-compler w’) =
arcosh (((1 — ?1*) * (1 — ?w?) + 2 * ?ew?) / ((1 — 22) * (1 — ?w?))) (is - = arcosh ?r2)
using disc
using poincare-distance-formula|OF <of-complex x € unit-discy «w € unit-dise] w
by (subst add-divide-distrib) simp
moreover
have «: (1 — ?a?) « (1 — ?w?) + 2 * Paw? < (1 + 2a?) & (1 + ?w?) + 4 * Pa * Pw
proof—
have (cmod (a — w’))? < (emod « + cmod w')?
using norm-triangle-ineg4 [of x w’]
by (simp add: power-mono)
thus ?thesis
by (simp add: field-simps power2-sum)
qed
have arcosh ?r1 > arcosh ?r2
proof (subst arcosh-mono)
show ?r1 > 1
using disc
by (smt « le-divide-eq-1-pos mult-pos-pos zero-le-power2)
next
show ?r2 > 1
using disc
by simp

66
next
show ?rl > ?r2
using disc
using *
by (subst divide-right-mono, simp-all)
qed
ultimately
show poincare-distance (of-complex x) w < poincare-distance (of-complex x) On + poincare-distance 0; w
using <of-complex x € unit-discy «w © unit-discr w
using poincare-distance-formula
by simp
qed
next
show v € unit-disc u € unit-disc
by fact+
next
fix Muv
assume *: unit-disc-fir M u € unit-disc v € unit-disc
assume *: ?P (moebius-pt M u) (moebius-pt M v)
show ?P uv
proof safe
fix w
assume w € unit-disc
thus ?P’ vuw
by (metis « «* unit-disc-fix-discl unit-disc-fix-preserve-poincare-distance)
qed
qed
thus ?thesis
using assms
by auto
qed

end

theory Poincare-Circles
imports Poincare-Distance

begin
