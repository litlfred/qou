---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-035-h-betweeness-on-euclidean-segments
section_title: "H-betweeness on Euclidean segments"
section_number: null
pages: 79-86
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
If the three points lie on an h-line that is a Euclidean line (e.g., if it contains zero), h-betweenness can be
characterized much simpler than in the definition.

lemma poincare-between-x-axis-u0v:
assumes is-real u’ and u’ # 0 and uv’ 4 0
shows poincare-between (of-complez u') On (of-complex v') <—+ is-real v' \ Re u' * Re v' < 0
proof—
have Re u' 4 0
using <is-real uy «u' 4 0»
using complex-eq-if-Re-eq
by auto
have nz: of-complez u' # On of-complex v' # On
by (simp-all add: (u' 4 0) «v' 4 0»)
hence 0;, 4 of-complex v'
by metis

let ?cr = cross-ratio (of-complex u') On (of-complex v') oon
have is-real (to-complex ?cr) A Re (to-complex ?cr) < 0 <—+ is-real v' A Re u' * Re v' < 0
using cross-ratio-Oinf[of v' u'] «v' # 0» <u! # O» cis-real uy
by (metis Re-complex-div-lt-0 Re-mult-real complex-cnj-divide divide-cancel-left eq-cnj-iff-real to-complex-of-complex)
thus ?thesis
unfolding poincare-between-def inversion-zero
using <of-complex u' # On) ‘On # of-complex v'
by simp
qed

lemma poincare-between-u0v:
assumes u € unit-disc and v € unit-disc and u # 0, and v On
shows poincare-between u 0, v ++ (A k < 0. to-complex u = cor k * to-complex v) (is ?P u v)
proof (cases u = v)
case True
thus ?thesis
using assms

79
using inf-or-of-complez|of v]
using poincare-between-sandwich|[of u On]
by auto
next
case False
have V u. u € unit-dise \ u # On —> ?P wv (is ?P’ v)
proof (rule wlog-rotation-to-positive-z-azis)
fix pv
let ?M = moebius-pt (moebius-rotation y)
assume 1: v € unit-disc v # On
assume 2: ?P’ (?M v)
show ?P’v
proof (rule alll, rule impI, (erule conjE)+)
fix u
assume 38: u € unit-disc u # On
have poincare-between (?M u) On (?M v) <> poincare-between u On v
using <u € unit-disc) <v € unit-disc»
using unit-disc-fir-moebius-preserve-poincare-between unit-disc-fiz-rotation zero-in-unit-disc
by fastforce
thus ?P uv
using 1 2[rule-format, of ?M u] 3
using inf-or-of-complez|of u] inf-or-of-complez|of v]
by auto
qed
next
fix x
assume 1: is-real t 0 < Rex Rex < 1
hence z 4 0
by auto
show ?P’ (of-complex x)
proof (rule alll, rule impI, (erule conjE)+)
fix u
assume 2: u € unit-disc u # On
then obtain u’ where u = of-complex u'
using inf-or-of-complez|of u]
by auto
show ?P u (of-complex x)
using 1 2 «x A 0> <u = of-complez u’>
using poincare-between-revlof u 0, of-complex x]
using poincare-between-z-axis-u0v[of x u'| <is-real x»
apply (auto simp add: cmod-eq-Re)
apply (rule-tac t=Re u’ / Re x in exl, simp add: divide-neg-pos algebra-split-simps)
using mult-neg-pos mult-pos-neg
by blast
qed
qed fact+
thus ?thesis
using assms
by auto
qed

lemma poincare-between-u0v-polar-form:
assumes z € unit-disc and y © unit-disc and x # 0; and y # 0;, and
to-complex x = cor rz * cis ~ to-complez y = cor ry * cis p
shows poincare-between x On y <—> rz x ry < 0 (is ?P vy rz ry)
proof—
from assms have rx 4 0 ry 4 0
using inf-or-of-complez|of x] inf-or-of-complez|of y]
by auto

have (Ak<0. cor rx = cor k * cor ry ) = (rx * ry < 0)
proof
assume Jk<0. cor rx = cor k * cor ry
then obtain k where k < 0 cor rx = cor k * cor ry
by auto
hence rz = k * ry

80
using of-real-eq-iff
by fastforce
thus rz « ry < 0
using <k < 0) «rz # 0» «ry # O»
by (smt divisors-zero mult-nonneg-nonpos mult-nonpos-nonpos zero-less-mult-pos2)
next
assume rz * ry < 0
hence rz = (ra/ry)*ry rz / ry < 0
using (rz # 0) «ry # 0»
by (auto simp add: divide-less-0-iff algebra-split-simps)
thus 4k<0. cor rx = cor k * cor ry
using (rz # 0) «ry # 0»
by (rule-tac c=rx / ry in exI, simp)
qed
thus ?thesis
using assms
using poincare-between-u0v[OF assms(1—4)]
by auto
qed

lemma poincare-between-x-axis-Ouv:
fixes xy :: real
assumes —1 < x and x < 1 andz# 0
assumes —1 < y and y < 1 andy #4 0
shows poincare-between 0), (of-complex x) (of-complex y) <—>
(c<O0ANy<ONyK<2z)V(ze>OANYyY>OALK y) (is ?lhs <> ?rhs)
proof (cases z = y)
case True
thus ?thesis
using assms
unfolding poincare-between-def
by auto
next
case False
let 2x = of-complex x and ?y = of-complex y

have ?x € unit-disc ?y € unit-disc
using assms
by auto

have distinct: distinct [On, ?x, ?y, inversion ?z]
using (x # 0) <y # 0) (x A y» Pa E unit-discy «?y € unit-discy
using inversion-noteq-unit-disc|of 2x ?y]
using inversion-noteq-unit-disc|of ?x ?x]
using inversion-noteq-unit-disc|of 2x On]
using of-complez-inj[of x y]
by (metis distinct-length-2-or-more distinct-singleton of-complex-zero-iff of-real-eq-0-iff of-real-eq-iff zero-in-unit-disc)

let ?cr = cross-ratio On ?x fy (inversion ?x)
have Re (to-complex ?cr) = x? « (xxy — 1) / (x * (y — 2))
using (x # 0) «a F y>
unfolding inversion-def
by simp (transfer, transfer, auto simp add: vec-cnj-def power2-eq-square field-simps split: if-split-asm)
moreover
{
fix a b:: real
assume b # 0
hence a < 0 <> b? * a < (0::real)
by (metis mult.commute mult-eq-0-iff mult-neg-pos mult-pos-pos not-less-iff-gr-or-eq not-real-square-gt-zero power2-eq-square)
}
hence 2x? « (xky — 1) < 0
using assms
by (smt minus-mult-minus mult-le-cancel-left1 )
moreover
have x * (y — z) > 0 <> ?rhs
using («x 4 0) y# Oo xn Fy

81
by (smt mult-le-0-iff)

ultimately

have «: Re (to-complex ?cr) < 0 <> ?rhs
by (simp add: divide-less-0-iff)

show ?thesis
proof
assume ?/hs
have is-real (to-complex ?cr) Re (to-complex ?cr) < 0
using <?lhs» distinct
unfolding poincare-between-def Let-def
by auto
thus ?rhs
using *
by simp
next
assume ?rhs
hence Re (to-complex ?cr) < 0
using *
by simp
moreover
have {0;, of-complex (cor x), of-complex (cor y), inversion (of-complex (cor x))} C circline-set x-axis
using (xz # 0» is-real-inversion|of cor x]
using inf-or-of-complez|of inversion ?z]
by (auto simp del: inversion-of-complez)
hence is-real (to-complex ?cr)
using four-points-on-circline-iff-cross-ratio-real[OF distinct]
by auto
ultimately
show ?lhs
using distinct
unfolding poincare-between-def Let-def
by auto
qed
qed

lemma poincare-between-Ouv:
assumes u € unit-disc and v € unit-disc and u # 0, and v On
shows poincare-between 0; uv <—~>
(let u’ = to-complex u; v' = to-complez v in Arg u' = Arg v' A cmod u' < cmod v’) (is ?P uv)
proof (cases u = v)
case True
thus ?thesis
by simp
next
case False
have V v. v € unit-dise \ v A On A v 4 u —> (poincare-between On uv + (let u' = to-complezx u; v' = to-complex
v in Arg u' = Arg v' A cmod u’ < cmod v')) (is ?P’ u)
proof (rule wlog-rotation-to-positive-z-azis)
show u € unit-disc u # On
by fact+
next
fix x
assume *: is-real zr 0 < Rex Rex < 1
hence of-complez « € unit-disc of-complex « # 0; of-complex x € circline-set x-axis
unfolding circline-set-x-axis
by (auto simp add: cmod-eq-Re)
show ?P’ (of-complez x)
proof safe
fix v
assume v € unit-disc v # On v 4 of-complex x poincare-between 0}, (of-complex x) v
hence v € circline-set z-axis
using poincare-between-poincare-line-uvz|of On of-complex x v|
using poincare-line-0-real-is-z-axis|of of-complex 2]
using <of-compler x # On) (vu # On? (v F of-complex x) <of-complex x € unit-disc> <of-complex x € circline-set
x-axis)

82
by auto

obtain v’ where v = of-complex v'
using <u € unit-discy
using inf-or-of-complez{of v|
by auto

hence *: v = of-compler v' —1 < Rev’ Re v' < 1 Re v' # 0 is-real v'
using (uv € unit-disc) «v # Oy» <v € circline-set z-axis» of-complez-inj[of v'|
unfolding circline-set-x-azxis
by (auto simp add: cmod-eq-Re real-imag-0)

show let u’ = to-complex (of-complex x); v' = to-complex v in Arg u' = Arg v' \ emod u! < cmod v’
using poincare-between-z-axis-Ouvlof Re x Re v'| * **
using <poincare-between 0; (of-complex x) v>
using arg-complez-of-real-positive[of Re x] arg-complex-of-real-negative[of Re x]
using arg-complexz-of-real-positive|of Re v'| arg-complex-of-real-negative|of Re v']
by (auto simp add: cmod-eq-Re)

next

fix v

assume v € unit-disc v # On v & of-complex &

then obtain v’ where **: v = of-compler v' v' 4 0v' Aa
using inf-or-of-complez{of v|
by auto blast

assume let u’ = to-complex (of-complex x); v' = to-complez v in Arg u' = Arg v' \ cmod u' < emod v'

hence ***: Rex <0 A Rev'’< 0A Rev'< RextV0< RexA0 < Rev'A Rez < Rev’ is-real v'
using arg-pi-iff {of x] arg-pi-ifflof v’]
using arg-0-iff[of x] arg-0-iff lof v']
using * **
by (smt cmod-Re-le-iff to-complex-of-complex)+

have —1 < Rev’ Rev’ < 1 Re v' 4 0 is-real v’
using <v € unit-disc) ** <is-real v'>
by (auto simp add: cmod-eq-Re complex-eq-if-Re-eq)

thus poincare-between 0), (of-complex x) v
using poincare-between-z-axis-Ouvlof Re x Re v'] * %* xx
by simp

qed
next

fix yu
assume u € unit-disc u # On
let ?M = moebius-rotation p
assume *: ?P’ (mocbius-pt ?M u)
show ?P’u
proof (rule alll, rule impI, (erule conjE)+)
fix v
assume v € unit-discu 4 On v#U
have moebius-pt ?M v # moebius-pt ?M u
using <v # wu)
by auto
obtain u’ v’ where v = of-complez v' u = of-complez u' v' # 0.u' £0
using inf-or-of-complez|of u] inf-or-of-complez|of v]
using (vu € unit-discy <u € unit-disc) (v # On» (u # On?
by auto
thus ?P uv
using *{rule-format, of moebius-pt ?M v]
using <moebius-pt ?M v 4 moebius-pt ?M uy
using unit-disc-fiz-moebius-preserve-poincare-between|of ?M On u v|
using (vu € unit-discy <u € unit-disc) (v # On» (u # On?
using arg-mult-eq[of cis p u’ v']
by simp (auto simp add: arg-mult norm-mult)
qed
qed
thus ?thesis
using assms False
by auto
qed

lemma poincare-between-y-azis-Ouv:
fixes xy :: real
assumes —1 < x and x < 1 andz# 0

assumes —1 < y and y < 1 andy #4 0

shows poincare-between 0p (of-complex (i * x)) (of-complex (i * y)) <>
(c<O0ANy<ONyK<2z)V(ze>OANYyY>OALK y) (is ?lhs <> ?rhs)

using assms

using poincare-between-Ouv[of of-complex (i * x) of-complex (i * y)|

using arg-pi2-ifflof i * cor x] arg-pi2-iff[of i « cor y]

using arg-minus-pi2-iff [of i * cor x] arg-minus-pi2-iff [of i * cor y]

apply (simp add: norm-mult)

apply (smt (verit, best))

done

lemma poincare-between-x-avis-uvw:
fixes zy z:: real
assumes —/ < 2 and z < 1
assumes —1 < yand y < 1 andy#a
assumes —1 < zandz< 1andz42
shows poincare-between (of-complex x) (of-complex y) (of-complex z) <>
(y¥<tAz<tAz<yV(y>tAz>aAyK< 2) (is 2lhs <> ?rhs)
proof (casest=0Vy=0V2z=0)
case True
thus ?thesis
proof (cases t = 0)
case True
thus ?thesis
using poincare-between-x-axis-Ouv assms
by simp
next
case False
show ?thesis
proof (cases z = 0)
case True
thus ?thesis
using poincare-between-x-axis-Ouv assms poincare-between-rev
by (smt norm-of-real of-complez-zero of-real-0 poincare-between-nonstrict(2) unit-disc-iff-cmod-lt-1)
next
case False
have y = 0
using «t§ A Oo iz AO tm =OVy=O0Vz=0>
by simp

have poincare-between (of-complez x) On (of-complex z) = (is-real z A % * z < 0)
using (x # 0» «z 4 0» poincare-between-x-axis-u0v
by auto

moreover

have x ¥ z < 0 «> ?rhs
using True «x # 0) (z # 0»
by (smt zero-le-mult-iff)

ultimately

show ?thesis
using <y = 0>
by auto

qed

qed

next

case False

thus ?thesis

proof (cases z = y)
case True
thus ?thesis

using assms

unfolding poincare-between-def

by auto

next
case False
let ?x = of-complex x and ?y = of-complex y and ?z = of-complex z

84
have ?r € unit-disc ?y € unit-disc ?z € unit-disc
using assms
by auto

have distinct: distinct [?x, ?y, ?z, inversion ?y]
using (y # @ (z # «) False <?x € unit-discy «?y € unit-discy «?z € unit-disc»
using inversion-noteg-unit-disc[of ?y ?y]
using inversion-noteg-unit-disc[of ?y ?z]
using inversion-noteg-unit-disclof ?y ?z]
using of-complez-injlof x y| of-complez-injlof y z| of-complez-inj[of x z]
by auto

have cor y * corz # 1
using assms
by (smt minus-mult-minus mult-less-cancel-left2 mult-less-cancel-right2 of-real-1 of-real-eq-iff of-real-mult)

let ?cr = cross-ratio ?x ?y ?z (inversion ?y)
have Re (to-complex ?cr) = (x — y) * (zxy — 1)/ ((xxy — 1)*(z — y))
proof —
have Ayxz.[yAa;z242;2Ay; cory* corr A#l;¢40;y 40,24 0] =>
(yey ty*(y*(e*2)) —(ysaty*(y*(y*2))) /
(yey ty* (ys (e*2)) — (yee ty «(yx (y*2)))) =
(y + y * (uz) — (@ + y* (y* 2))) / (yt y® (w* 2) — (2 + y* (y * 2)))
by (metis (no-types, opaque-lifting) ab-group-add-class.ab-diff-conv-add-uminus distrib-left mult-divide-mult-cancel-left-if
mult-minus-right)
thus ?thesis
using (y 4 @ (z # a> False 4 (tx =OVy=0Vz=0)>
using ‘cor y * corz # 1>
unfolding inversion-def
by (transfer, transfer, auto simp add: vec-cnj-def power2-eq-square field-simps split: if-split-asm)
qed

moreover
have (xxy — 1) < 0
using assms
by (smt minus-mult-minus mult-less-cancel-right2 zero-less-mult-iff )
moreover
have (zxy — 1) < 0
using assms
by (smt minus-mult-minus mult-less-cancel-right2 zero-less-mult-iff )
moreover
have (x — y) / (z — y) < 0 ++ ?rhs
using (y #4 a (z # «) False (4 («@ =OVy=O0Vz=0)>
by (smt divide-less-cancel divide-nonneg-nonpos divide-nonneg-pos divide-nonpos-nonneg divide-nonpos-nonpos)
ultimately
have «: Re (to-complex ?cr) < 0 +> ?rhs
by (smt algebra-split-simps(24) minus-divide-left zero-less-divide-iff zero-less-mult-iff )
show ?thesis
proof
assume ?/hs
have is-real (to-compler ?cr) Re (to-complex ?cr) < 0
using <?lhs) distinct
unfolding poincare-between-def Let-def
by auto
thus ?rhs
using *
by simp
next
assume ?rhs
hence Re (to-complex ?cr) < 0
using *
by simp
moreover

have {of-complex (cor x), of-complex (cor y), of-complex (cor z), inversion (of-complex (cor y))} C circline-set
x-axis
using (7 (« = 0 Vy = 0 V z = 0)» is-real-inversion|of cor y]
using inf-or-of-complez|of inversion ?y]
by (auto simp del: inversion-of-complex)

hence is-real (to-complex ?cr)
using four-points-on-circline-iff-cross-ratio-real[OF distinct]
by auto

ultimately

show ?lhs
using distinct
unfolding poincare-between-def Let-def
by auto

qed
qed
qed
