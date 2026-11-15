---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-041-betweeness-of-x-axis-intersection
section_title: "Betweeness of x-axis intersection"
section_number: null
pages: 96-97
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
The intersection point of the h-line determined by points u and v and the x-axis is between u and v, then u
and v are in the opposite half-planes (one must be in the upper, and the other one in the lower half-plane).

lemma poincare-between-x-axis-intersection:
assumes wu € unit-disc and v € unit-disc and z € unit-disc and u # v
assumes u ¢ circline-set x-azis and v ¢ circline-set t-axis
assumes 2z € circline-set (poincare-line u v) M circline-set x-axis
shows poincare-between u z v <—> Arg (to-compler u) « Arg (to-complex v) < 0
proof—

have V uv. u € unit-disc \ v € unit-disc Au Av A

u € circline-set x-axis \ v ¢ circline-set x-axis

z € circline-set (poincare-line u v) M circline-set r-axis —>

(poincare-between uz v <—> Arg (to-complex u) * Arg (to-complez v) < 0) (is ?P z)
proof (rule wlog-real-zero)

show ?P 0,
proof ((rule all[)+, rule impI, (erule conjE)+)
fix uv
assume *: u € unit-disc v € unit-disc u # v
u € circline-set z-axis v ¢ circline-set x-axis
On € circline-set (poincare-line u v) M circline-set z-axis
obtain u’ v' where wv: u = of-complexr u' v = of-complex v'
using « inf-or-of-complez[of u] inf-or-of-complez|of v|
by auto

hence u 4 0, v4 On u' 4 O0v'F# 0
using *
by auto

hence Arg u' 4 0 Arg v' #0
using « arg-0-iff[of u'| arg-0-iff [of v'|
unfolding circline-set-x-axis uv
by auto

have poincare-collinear {On, u, v}
using *
unfolding poincare-collinear-def
by (rule-tac x=poincare-line u v in exI, simp)
have (Ak<0. u' = cor k x v’) + (Arg u' * Arg v' < 0) (is ?lhs <> ?rhs)
proof
assume ?/hs
then obtain k where k < 0 u’ = cork * v’
by auto
thus ?rhs
using arg-mult-real-negative|of k v'| arg-uminus-opposite-sign{of v']
using <u’ 4 0) «uv! £ 0) «Arg u' 4 0» (Arg v' # O>
by (auto simp add: mult-neg-pos mult-pos-neg)

next
assume ?rhs
obtain ru rv y where polar: u’ = cor ru * cis y v' = cor ru * cis p
using <poincare-collinear {0n, u, v}> poincare-collinear-zero-polar-form{of u' v'] uv * «ul £ 0» «v' ZO»
by auto

have ru * ru < 0
using polar <?rhs» <u’ 4 0) «vu! 4 Ov
using arg-mult-real-negative[of ru cis y| arg-mult-real-positive|of ru cis |
using arg-mult-real-negative[of rv cis y] arg-mult-real-positivelof rv cis ]
apply (cases ru > 0)
apply (cases rv > 0, simp, simp add: mult-pos-neg)
apply (cases rv > 0, simp add: mult-neg-pos, simp)
done
thus ?lhs
using polar
by (rule-tac c=ru / rv in exl, auto simp add: divide-less-0-iff mult-less-0-iff )

96
qed
thus poincare-between u 0, v = (Arg (to-complex u) * Arg (to-complex v) < 0)
using poincare-between-u0v[of uv] * <u # On cv # On» ww
by simp
qed
next
fix az
assume 1: is-real a cmod a < 1 z € unit-disc
assume 2: ?P (moebius-pt (blaschke a) z)
show ?P z
proof ((rule all[)+, rule impI, (erule conjE)+)
fix uv
let ?M = moebius-pt (blaschke a)
let ?Mu = ?Mu
let ?Mv = ?Mv
assume *: u € unit-disc v € unit-disc u # v u € circline-set x-axis v ¢ circline-set x-axis
hence u 4 oon, v # On
by auto

have ««: \ xy: real. x x y < 0 <> sgn (x xy) <0
by simp

assume z € circline-set (poincare-line u v) M circline-set x-axis
thus poincare-between uz v = (Arg (to-complex u) * Arg (to-complez v) < 0)
using * 1 2[rule-format, of ?Mu ?Mv| «cmod a < 1) ¢is-real ay blaschke-unit-disc-fix|of a]
using inversion-noteg-unit-disc|of of-complex a u] «u # n>
using inversion-noteg-unit-disc|of of-complex a v| «v # On?
apply auto
apply (subst (asm) **, subst **x, subst (asm) sgn-mult, subst sgn-mult, simp)
apply (subst (asm) **, subst (asm) **, subst (asm) sgn-mult, subst (asm) sgn-mult, simp)
done
qed
next
show z € unit-disc by fact
next
show is-real (to-complex z)
using assms inf-or-of-complex|of 2]
by (auto simp add: circline-set-x-azis)
qed
thus ?thesis
using assms
by simp
qed
