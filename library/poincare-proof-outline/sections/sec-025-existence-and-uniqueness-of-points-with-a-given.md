---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-025-existence-and-uniqueness-of-points-with-a-given
section_title: "Existence and uniqueness of points with a given distance"
section_number: null
pages: 54-65
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma ez-2-azis-poincare-distance-negative’:
fixes d :: real
assumes d > 0
shows let z = (1 — exp d) / (1 + exp d)
in is-realz \ Rez< 0A Rez>-1A
of-complex z € unit-disc \ of-complex z € circline-set x-axis A
poincare-distance 0, (of-complex z) = d
proof—
have exp d > 1
using assms
using one-le-exp-iff [of d, symmetric]
by blast

hence / + erp d 4 0
by linarith

let ?z = (1 — exp d) / (1 + exp d)

have ?z < 0
using ‘erp d > 1»
by (simp add: divide-nonpos-nonneg)

moreover

have ?z > -1
using exp-gt-zero[of d]
by (smt divide-less-eq-1-neg nonzero-minus-divide-right)

moreover

hence abs ?z < 1
using <?z < 0»
by simp
hence cmod ?z < 1
by (metis norm-of-real)
hence of-complex ?z € unit-disc
by simp

moreover
have of-complex ?z € circline-set z-axis
unfolding circline-set--axis
by simp

moreover
have (1 — ?z) / (1 + ?z) = expd
proof —
have 1 + ?z = 2 / (1 + eap d)
using </ + exp d # 0»
by (subst add-divide-eq-iff, auto)
moreover
have 1 — ?z = 2 « exp d/ (1 + exp d)
using </ + exp d # 0»
by (subst diff-divide-eq-iff, auto)
ultimately
show ?thesis
using </ + exp d # 0»
by simp
qed

ultimately
show ?thesis
using poincare-distance-zero-x-axis[of of-complex ?z]
using (d > 0) ‘erp d > 1»
by simp (simp add: cmod-eq-Re)
qed

lemma ex-x-axis-poincare-distance-negative:

assumes d > 0

shows 4 z. is-realz \ Rez < 0A Rez>-1A
of-complex z € unit-disc \ of-complex z € circline-set x-axis A
poincare-distance On (of-compler z) = d (is 3 z. ?P z)

using ex-z-axis-poincare-distance-negative’'|OF assms]

unfolding Let-def

by blast

on
an
For each real number d there is exactly one point on the positive x-axis such that h-distance between 0 and
that point is d.

lemma unique-x-avis-poincare-distance-negative:
assumes d > 0
shows 3! z. is-realz \ Rez <0 A Rez>-1A
poincare-distance On (of-complex z) = d (is 5! z. ?P z)
proof—
let ?z = (1 — exp d) / (1 + exp d)

have ?P ?z
using ex-z-axis-poincare-distance-negative'|OF assms]
unfolding Let-def
by blast

moreover

have V z’. ?P.z' —+ z'= ?z
proof—
let ?g = A 2’. |In (Re ((1 — 2’) / (1 + 2’)))|
let ?A = {z. is-realx \ Rex > —1 A Rex < O}
have inj-on (poincare-distance 0;, 0 of-compler) ?A
proof (rule comp-inj-on)
show inj-on of-complex ?A
using of-complez-inj
unfolding inj-on-def
by blast
next
show inj-on (poincare-distance 0) (of-complex ‘ ?A) (is inj-on ?f (of-complex ‘ ?A))
proof (subst inj-on-cong)
have *: of-compler ‘ ?A =
{z. z € unit-disc \ z € circline-set x-axis \ Re (to-complex z) < 0} (is - = ?B)
by (auto simp add: cmod-eq-Re circline-set-a-azis)

fix «

assume z € of-complex ‘ ?A

hence x € ?B
using *
by simp

thus poincare-distance 0; = (?g 0 to-complex) x
using poincare-distance-zero-x-axis
by (simp add: Let-def)

next

have x: to-complex ‘ of-compler ‘ ?A = ?A

by (auto simp add: image-iff)

show inj-on (?g 0 to-complex) (of-complex ‘ ?A)
proof (rule comp-inj-on)
show inj-on to-complex (of-complex ‘ ?A)
unfolding inj-on-def
by auto
next
have inj-on ?g ?A
unfolding inj-on-def
proof (safe)
fix ry
assume hh: is-real x is-real y— 1 < Rex Rex < 0
—1< Rey Rey < 0 |In (Re (1 — 2) / (1 + 2)))| = |In (Re (1 — y) / (1 + y)))|

have is-real ((1 — x)/(1 + 2))
using <is-real x» div-reals[of 1—x 1+<]
by auto

have is-real ((1 — y)/(1 + y))
using <is-real y> div-reals[of 1—y 1+-y]
by auto

have Re (1 + x) > 0
using «— 1 < Re x) by auto
hence 1 + 2 4 0
by force
have Re (1 — x) > 0
using (Re z < 0) by auto
hence Re ((1 — z)/(1 + z)) > 0
using Re-divide-real «0 < Re (1 + x)» complex-eq-if-Re-eq hh(1) hh(4) by auto
have Re(1 — x) > Re (1+ 2)
using hh by auto
hence Re ((1 — z)/(1 + z)) > 1
using (Re (1 + x) > 0» <is-real ((1 — x)/(1 + 2))>
by (smt Re-divide-real arg-0-iff hh(1) le-divide-eq-1-pos one-complex.simps(2) plus-complex.simps(2))

have Re (1 + y) > 0
using «— 1 < Re y» by auto
hence 1 + y 4 0
by force
have Re (1 — y) > 0
using ‘Re y < 0» by auto
hence Re ((1 — y)/(1 + y)) > 0
using Re-divide-real (0 < Re (1 + y)> complex-eq-if-Re-eq hh by auto
have Re(1 — y) > Re (1+ y)
using hh by auto
hence Re ((1 — y)/(1 + y)) > 1
using (Re (1 + y) > 0» <is-real ((1 — y)/(1 + y))>
by (smt Re-divide-real arg-0-iff hh le-divide-eq-1-pos one-complez.simps(2) plus-complex.simps(2))

have In (Re (1 = 2) / (1 + 2))) = In (Re ((1 — y) / (1 + y)))
using ‘Re ((1 — y)/(1 + y)) > 1» «Re ((1 — x)/(1 + z)) > 1> hh
by auto

hence Re ((1 — x) / (1 + z)) = Re (1 — y) / (1 + y))
using (Re ((1 — y)/(1 + y)) > 0» «Re ((1 — z)/(1 + 2)) >
by auto

hence (1 — x) /(1+2)=(1-y)/(1+y)
using <is-real ((1 — y)/(1 + y))> ‘is-real ((1 — x)/(1 + 2))>
using complex-eq-if-Re-eq by blast

hence (1 — z) * (1 + y) =(1 — y)* (1 +2)
using (1 +y #0 (1 +2440)
by (simp add:field-simps)

thus x = y
by (simp add:field-simps)

qed
thus inj-on ?g (to-complex ‘ of-complex ‘ ?A)
using *
by simp
qed
qed
qed
thus ?thesis
using <?P ?2z>
unfolding inj-on-def
by auto
qed
ultimately
show ?thesis
by blast
qed

lemma ex-x-axis-poincare-distance-positive:
assumes d > 0
shows J z. is-realz \ Rez >0A Rez< 1A
of-complex z € unit-disc \ of-complex z € circline-set x-axis A
poincare-distance On (of-complex z) = d (is J z. is-realz A Rez > 0 A Rez <1 A ?P z)
proof—
obtain z where *: is-real z Re z < 0 Rez > —1 ?Pz
using ex-z-axis-poincare-distance-negative|OF assms]
by auto

hence *«: of-complex z € unit-disc of-complez z € circline-set x-axis
by (auto simp add: cmod-eq-Re)

have is-real (—z) \ Re (—z) > 0 A Re (—z) < 1 A ?P (-2)
using * **
by (simp add: circline-set-x-axis)

thus ?thesis
by blast

qed

lemma unique-z-avis-poincare-distance-positive:
assumes d > 0
shows 3! z. is-realz \ Rez > 0A Rez< 1A
poincare-distance Op (of-complex z) = d (is J! z. is-real z \ Rez > 0 \ Rez <1 A ?P 2)
proof—
obtain z where *: is-real z Re z < 0 Rez > —1 ?Pz
using unique-x-axis-poincare-distance-negative|OF assms]
by auto
hence *«: of-complex z € unit-disc of-complez z € circline-set x-axis
by (auto simp add: cmod-eq-Re circline-set-x-azis)
show ?thesis
proof
show is-real (—z) \ Re (—z) > 0 A Re (—z) < 1 A ?P (-z)
using * **
by simp
next
fix z’
assume is-real z' \ Re z'> 0 \ Rez'< 1A ?P 2’
hence is-real (—z’) A Re (—z') < 0 A Re (—2') > -1 A ?P (-2’')
by (auto simp add: circline-set-x-axis cmod-eq-Re)
hence —z’ = z
using unique-x-axis-poincare-distance-negative|OF assms] *
by blast
thus 2' = —z
by auto
qed
qed

Equal distance implies that segments are isometric - this means that congruence could be defined either by two
segments having the same distance or by requiring existence of an isometry that maps one segment to the other.

lemma poincare-distance-eq-ex-moebius:
assumes in-disc: u € unit-disc and v € unit-disc and u’ € unit-disc and v' € unit-disc
assumes poincare-distance u v = poincare-distance u’ v'
shows 3 M. unit-disc-fiz M A moebius-pt Mu = u' A moebius-pt Mv = v' (is ?P' uv u' v’)
proof (cases u = v)
case True
thus ?thesis
using assms poincare-distance-eq-0-iff [of u' v'|
by (simp add: unit-disc-fix-transitive)
next
case False
have V u’v’..uZ#vuA uw’ € unit-disc A v' € unit-disc A poincare-distance u v = poincare-distance u' v'’ —>
2P' ul v' wv (is PP uv)
proof (rule wlog-positive-x-azis[;where P=?P])
fix x
assume is-real x 0 < Rex Rex < 1
hence of-complex « € unit-disc of-complez x € circline-set x-axis
unfolding circline-set-x-axis
by (auto simp add: cmod-eq-Re)

show ?P 0), (of-complex x)
proof safe
fix u/ v’
assume 0), 4 of-complez x and in-disc: u’ € unit-disc v’ € unit-disc and
poincare-distance 0, (of-complex x) = poincare-distance u' v’
hence u’ 4 v’ poincare-distance u' v' > 0
using poincare-distance-eq-0-iff|of On of-complex x| <of-complex x € unit-disc»
using poincare-distance-ge0[of 0, of-complex x]
by auto
then obtain M where M: unit-disc-fix M moebius-pt M u' = 0n moebius-pt M v' € positive-a-azis
using ex-unit-disc-fiz-to-zero-positive-z-azis[of u’ v'| in-disc
by auto

then obtain Mv’ where Mv’: moebius-pt M v' = of-complex Mv’
using inf-or-of-complez|{of moebius-pt M v'| in-disc unit-disc-fiz-iff[of M]
by (metis image-eqI inf-notin-unit-disc)

have moebius-pt M v' € unit-disc
using M(1) «v' € unit-disc»
by auto

have Re Mv’ > 0 is-real Mv’ Re Mv’ < 1
using M Mv’ of-complex-inj «moebius-pt M v' € unit-disey
unfolding positive-x-axis-def circline-set-x-axis
using cmod-eq-Re
by auto fastforce

have poincare-distance 0}, (moebius-pt M v') = poincare-distance u' v’
using M(1)
using in-disc
by (subst M(2)[symmetric], simp)

have Mv’ = 2

using <poincare-distance 0, (moebius-pt M v’) = poincare-distance u' v'» Mv’

using <poincare-distance 0, (of-compler x) = poincare-distance u’ v'y

using unique-z-axis-poincare-distance-positive|of poincare-distance u’ v'|
<poincare-distance u' v' > 0»

using (Re Mv’ > 0» «Re Mv’ < 1» <is-real Mv’

using <is-real x) (Rex > 0» (Rea < 1»

unfolding positive-x-azis-def

by auto

thus ?P’ wu’ v' On (of-complez x)
using M Mv’
by auto
qed
next
show u € unit-disc v € unit-disc u A v
by fact+
next
fix Muv
let ?Mu = moebius-pt Mu and ?Mv = moebius-pt M v
assume 1: unit-disc-fiz M u € unit-disc v € unit-disc u # v
hence 2: ?Mu # ?Mv ?Mu € unit-disc ?Mv € unit-disc
by auto
assume 3: ?P (moebius-pt M u) (moebius-pt M v)
show ?P uv
proof safe
fix u’ v’
assume 4: u’ € unit-disc v' € unit-disc poincare-distance uv = poincare-distance u' v'
hence poincare-distance ?Mu ?Mv = poincare-distance u v
using /
by simp
then obtain M' where 5: unit-disc-fix M' moebius-pt M' u' = ?Mu moebius-pt M' v' = ?Mv
using 2 3 4
by auto
let ?M = (—M) + M’
have unit-disc-fix ?M A moebius-pt ?M u’ = u A moebius-pt ?M v' = v
using 5 <unit-disc-fix M»
using unit-disc-fiz-moebius-comp[of —M M"|
using unit-disc-fiz-moebius-inv|[of M]
by simp
thus 3M. unit-disc-fiz M A moebius-pt M u' = u A moebius-pt M v' = v
by blast
qed
qed
then obtain M where unit-disc-fix M \ moebius-pt M u' = u A moebius-pt M v' = v
using assms (u # v)
by blast
hence unit-disc-fix (-M) A moebius-pt (-M) u = u' A moebius-pt (—M) v = v'
using wnit-disc-fiz-moebius-inv|of M]
by auto
thus ?thesis
by blast
qed

lemma unique-midpoint-x-axis:
assumes «: is-real 1 —1 < Rex Rex < 1 and
y: is-real y —1 < Rey Rey < 1 and
cH#y
shows 4! z. —1 < Rez A Rez < 1 A is-real z A poincare-distance (of-complex z) (of-compler x) = poincare-distance
(of-complex z) (of-complez y) (is 4! z. ?R z (of-complex x) (of-complez y))
proof—
let 2x = of-complex x and ?y = of-complex y
let ?P=Acy.dlz. ?Rzxey
have V 2. —1 < Rex A Rex < 1 A is-real x A of-complex x # ?y —> ?P (of-complex x) ?y (is ?Q (of-complex y))
proof (rule wlog-real-zero)
show ?y € unit-disc
using y
by (simp add: cmod-eq-Re)
next
show is-real (to-complex ?y)
using y
by simp
next
show 7Q 0;
proof (rule alll, rule impI, (erule conjE)+)
fix x
assume z: —1 < Rex Rex < 1 is-real x
let ?x = of-complex x
assume ?r 4 0),
hence z # 0
by auto
hence Re « # 0
using x
using complex-neq-0
by auto

have *:V a.-1 <aANa< 1—~
(poincare-distance (of-complex (cor a)) ?x = poincare-distance (of-complex (cor a)) 0p, +
(Rez) *a*a-—2*a+Rer=0)
proof (rule alll, rule imp1)
fix a :: real
assume —1 <aAa< 1
hence of-complex (cor a) € unit-disc
by auto
moreover
have (a — Re x)? / ((1 — a”) * (1 — (Re x)?)) = a? / (1 — a?) Ho
(Rex) *a*a-—2*a+ Rex=0 (is ?lhs ~~ ?rhs)
proof—
have 1 — a? 40
using (-1 <aAa< 1»
by (metis cancel-comm-monoid-add-class.diff-cancel diff-eq-diff-less less-numeral-extra(4) power2-eq-1-iff
right-minus-eq)
hence ?lhs <> (a — Re x)? / (1 — (Re 2)”) = a?
by (smt divide-cancel-right divide-divide-eq-left mult.commute)
also have ... <> (a — Re 2)? = a? (1 — (Re x)’)
proof—

60
have 1 — (Rex)? 40
using &
by (smt power2-eq-1-iff)
thus ?thesis
by (simp add: divide-eq-eq)
qed
also have ... <> a? * (Re x)? — 2xaxRe x + (Rex)? = 0
by (simp add: power2-diff field-simps)
also have ... + Re x *« (a? * Rea — 2x a+ Re2r)=0
by (simp add: power2-eq-square field-simps)
also have ... <> ?rhs
using ‘Re x # 0)
by (simp add: mult.commute mult.left-commute power2-eq-square)
finally
show ?thesis

qed

moreover

have arcosh (1 + 2 * ((a — Re x)? / ((1 — a”) * (1 — (Re x)”)))) = arcosh (1 + 2 * a? / (1 — a?)) <> Plhs
using «—1 < aA a< 1) x mult-left-cancellof 2::real (a — Re x)” / ((1 — a”) * (1 — (Re 2)*)) a? / (1 — a?)|
by (subst arcosh-eq-iff, simp-all add: square-le-1)

ultimately

show poincare-distance (of-complex (cor a)) (of-complez x) = poincare-distance (of-complex (cor a)) Oh <>

(Rez) *a*a-—2*a+Rex=0
using x
by (auto simp add: poincare-distance-formula cmod-eq-Re)
qed

show ?P ?z On
proof

let ?a = (1 — sqrt(1 — (Re x)?)) / (Re z)
let ?b = (1 + sqrt(1 — (Re 2)”)) / (Re x)

have is-real ?a
by simp
moreover
have 1 — (Re x)? > 0
using x
by (smt power2-eq-1-iff square-le-1)
have |?a| < 1
proof (cases Re « > 0)
case True
have (1 — Re 2)? < 1 — (Re x)?
using (Rex > 0) x
by (simp add: power2-eq-square field-simps)
hence 1 — Re x < sqrt (1 — (Re ))
using real-less-rsqrt by fastforce
thus ?thesis
using «1 — (Re x)? > 0) ‘Rex > 0»
by simp
next
case False
hence Re x < 0
using ‘Re x # 0)
by simp

have 1 + Rex > 0
using (Re x > —1>
by simp

hence 2xRe z + 2*Re xxRe xz < 0
using (Re xz < 0»

by (metis comm-semiring-class. distrib mult.commute mult-2-right mult-less-0-iff one-add-one zero-less-double-add-iff-zero-less-s'

hence (1 + Re x)? < 1 — (Rex)?
by (simp add: power2-eq-square field-simps)

hence 1 + Re x < sqrt (1 — (Re x))
using «1 — (Re x)? > 0»

61
using real-less-rsqrt by blast
thus ?thesis
using (Re xz < 0»
by (simp add: field-simps)
qed
hence —1 < ?a ?a < 1
by linarith+
moreover
have (Re r) * 2a * ?a — 2* 2a + Rex=0
using (Re « # 0) «1 — (Rex)? > 0»
by (simp add: field-simps power2-eq-square)
ultimately
show —1 < Re (cor ?a) A Re (cor ?a) < 1 A is-real ?a A poincare-distance (of-complex ?a) (of-complex x) =
poincare-distance (of-complex ?a) On
using *
by auto

fix z
assume **: — 1 < Rez A Rez < 1 A is-real z A
poincare-distance (of-complex z) (of-compler x) = poincare-distance (of-complez z) On
hence Re x * Rez * Rez— 2% Rez+ Rex =0
using *[rule-format, of Re z| x
by auto
moreover
have sqrt (4 — 4 * Rex * Rex) = 2 * sqrt(1 — Rex * Rez)
proof—
have sqrt (4 — 4 * Rex * Re x) = sqrt(4 * (1 — Rex * Re z))
by simp
thus ?thesis
by (simp only: real-sqrt-mult, simp)
qed
moreover
have (2 — 2 * sqrt (1 — Rex * Re x)) / (2 * Rex) = ?a
proof—
have (2 — 2 * sqrt (1 — Rex * Rex)) / (2 * Rex) =
(2 * (1 — sqrt (1 — Rex * Re x))) / (2 * Rex)
by simp
thus ?thesis
by (subst (asm) mult-divide-mult-cancel-left) (auto simp add: power2-eq-square)
qed
moreover
have (2 + 2 * sqrt (1 — Rex * Re x)) / (2 * Rex) = ?b
proof—
have (2 + 2 * sqrt (1 — Rex * Rex)) / (2 * Rex) =
(2 * (1 + sqrt (1 — Rea * Re x))) / (2 * Re x)
by simp
thus ?thesis
by (subst (asm) mult-divide-mult-cancel-left) (auto simp add: power2-eq-square)
qed
ultimately
have Re z = ?a V Rez = ?b
using discriminant-nonneg|of Re x —2 Re x Re 2] discrim-def|of Re x —2 Re x]
using «Re x # 0) (-1 < Rea ‘Rex < 1) «1 — (Rex)? > 0»
by (auto simp add:power2-eq-square)
have | ?b| > 1
proof (cases Re « > 0)
case True
have (Re x — 1)? < 1 — (Rex)?
using (Rex > 0) x
by (simp add: power2-eq-square field-simps)
hence Re x — 1 < sqrt (1 — (Re 2)”)
using real-less-rsqrt
by simp
thus ?thesis
using «1 — (Re x)? > 0) ‘Rex > 0»
by simp

62
next
case False
hence Re x < 0
using ‘Re x # 0)
by simp
have 1 + Rex > 0
using (Re x > —1>
by simp
hence 2xRe z + 2*Re xxRe xz < 0
using (Re xz < 0»
by (metis comm-semiring-class. distrib mult.commute mult-2-right mult-less-0-iff one-add-one zero-less-double-add-iff-zero-less-si
hence 1 — (Re x)? > (— 1 — (Re 2))”
by (simp add: field-simps power2-eq-square)
hence sqrt (1 — (Re x)?) > -1 — Rex
using real-less-rsqrt
by simp
thus ?thesis
using (Re xz < 0»
by (simp add: field-simps)
qed
hence ?b < —-1 V ?o>1
by auto

hence Re z = 7a
using (Re z = ?a V Re z = 2b» x
by auto
thus z = ?a
using **« complez-of-real-Re
by fastforce
qed
qed
next
fix au
let ?M = moebius-pt (blaschke a)
let ?Mu = ?Mu
assume wu € unit-disc is-real a cmod a < 1
assume «: ?Q ?Mu
show ?Qu
proof (rule alll, rule impI, (erule conjE)+)
fix x
assume wz: —1 < Rex Re x < 1 is-real x of-complex « # u
let ?Mz = ?M (of-complex x)
have of-complex x € unit-disc
using x cmod-eq-Re
by auto
hence ?Mz € unit-disc
using <is-real ay «cmod a < 1» blaschke-unit-disc-fiz|of a]
using unit-disc-fir-discl
by blast
hence ?Mz 4 con
by auto
moreover
have of-complex x € circline-set r-axis
using x
by auto
hence ?Mz € circline-set x-axis
using blaschke-real-preserve-x-axis|OF <is-real ay «cmod a < 1, of of-complex z]
by auto
hence —1 < Re (to-compler ?Mx) \ Re (to-compler ?Mzx) < 1 A is-real (to-complex ?Mzx)
using <?Mzx 4 oon) «?Max © unit-disc»
unfolding circline-set-x-azxis
by (auto simp add: cmod-eq-Re)
moreover
have ?Mz 4 ?Mu
using <of-compler x # u)
by simp
ultimately
have ?P ?Mx ?Mu
using *{rule-format, of to-complex ?Mz| «?Mz # con?
by simp
then obtain Mz where
?R Mz ?Max ?Mu
by blast
have of-compler Mz € unit-disc of-complex Mz € circline-set x-axis
using <?R Mz ?Mx ?Mu)
using cmod-eq-Re
by auto

let ?Minv = — (blaschke a)
let ?z = moebius-pt ?Minv (of-complex Mz)
have ?z € unit-disc
using <of-compler Mz € unit-discy «cmod a < 1»
by auto
moreover
have ?z € circline-set x-axis
using <of-compler Mz € circline-set x-axis»
using blaschke-real-preserve-x-axis <is-real ay «cmod a < 1»
by fastforce
ultimately
have z1: —1 < Re (to-complex ?z) Re (to-complex ?z) < 1 is-real (to-complex ?z)
using inf-or-of-complez|of ?z]
unfolding circline-set-x-azxis
by (auto simp add: cmod-eq-Re)

have 22: poincare-distance ?z (of-compler x) = poincare-distance ?z u
using «?R Mz ?Max ?Mu» «cmod a < 1) <?z € unit-disc> <of-complex x € unit-disc» <u € unit-discy
by (metis blaschke-preserve-distance-formula blaschke-unit-disc-fiz moebius-pt-comp-inv-right poincare-distance-formula
uminus-moebius-def unit-disc-fix-discI unit-disc-iff-cmod-lt-1)
show ?P (of-complez x) u
proof
show ?R (to-complex ?z) (of-complex x) u
using 21 22 (?z € unit-discy inf-or-of-complez[of ?z]
by auto
next
fix z’
assume ?R z’ (of-complex x) u
hence of-complex z' € unit-disc of-complex z' € circline-set x-axis
by (auto simp add: cmod-eq-Re)
let ?Mz' = ?M (of-complex z')
have ?Mz' € unit-disc ?Mz' € circline-set r-axis
using <of-complex z' € unit-discy <of-complex z' € circline-set x-axis) «cmod a < 1» <is-real ay
using blaschke-unit-disc-fix unit-disc-fix-discI
using blaschke-real-preserve-x-axis circline-set-x-axis
by blast+
hence —1 < Re (to-complex ?Mz') Re (to-complex ?Mz') < 1 is-real (to-complex ?Mz')
unfolding circline-set-x-axis
by (auto simp add: cmod-eq-Re)
moreover
have poincare-distance ?Mz' ?Mzx = poincare-distance ?Mz' ?Mu
using <?R z’ (of-complex x) w
using <cmod a < 1» <of-complex x € unit-disc <of-complex z' € unit-disc> «u € unit-discy
by auto
ultimately
have ?R (to-complex ?Mz') ?Mx ?Mu
using <?Mz!' € unit-discy inf-or-of-complex|of ?Mz'|
by auto
hence ?Mz’ = of-complex Mz
using <?P ?Mzx ?Mu) <?R Mz ?Max ?Muy
by (metis «moebius-pt (blaschke a) (of-complez z’) € unit-disc> «of-compler Mz € unit-disc» to-complex-of-complex
unit-disc-to-complez-inj)
thus z' = to-complex ?z
by (simp add: moebius-pt-invert)

64
qed
qed
qed
thus ?thesis
using assms
by (metis to-complex-of-complex)
qed
