---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-023-h-distance-in-the-poincaré-model
section_title: "H-distance in the Poincaré model"
section_number: null
pages: 44-48
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Informally, the h-distance between the two h-points is defined as the absolute value of the logarithm of the cross
ratio between those two points and the two ideal points.

abbreviation Re-cross-ratio where Re-cross-ratio z uv w = Re (to-complez (cross-ratio z u v w))

definition calc-poincare-distance :: complex-homo = complex-homo => complex-homo = complez-homo => real where
[simp]: calc-poincare-distance u il v i2 = abs (In (Re-cross-ratio u il v i2))

definition poincare-distance-pred :: complex-homo = complex-homo => real = bool where
[simp]: poincare-distance-pred u v d <—>
(u=vAd=0)V (u#vA(V il 22. ideal-points (poincare-line uv) = {il, i2} —> d = calc-poincare-distance
u il v i2))

definition poincare-distance :: complez-homo = complex-homo => real where
poincare-distance uv = (THE d. poincare-distance-pred u v d)

We shown that the described cross-ratio is always finite, positive real number.

lemma distance-cross-ratio-real-positive:
assumes u € unit-disc and v € unit-disc and u 4 v
shows V il i2. ideal-points (poincare-line u v) = {il, i2} —
cross-ratio u il v i2 # cop A is-real (to-complex (cross-ratio u il v i2)) \ Re-cross-ratio u il v i2 > 0
(is ?P wu v)
proof (rule wlog-positive-x-axis[OF assms])
fix x
assume *: is-real x 0 < Rex Rex < 1
hence x 4 -—1 44 1
by auto
hence ««: of-complez x # oop of-complex x # On of-complex x # of-complex (—1) of-complex 1 # of-complex x
of-complex x € circline-set z-axis
using *
unfolding circline-set--axis
by (auto simp add: of-complex-inj)

have *««: 0, 4 of-complex (—1) 0, 4 of-complex 1
by (metis of-complez-zero-iff zero-neq-neg-one, simp)

have ****: —c-140x-1#0
using (x # —1) «x@ # 1)
by (metis add.inverse-inverse eq-iff-diff-eq-0, simp)

have poincare-line 0; (of-complez x) = x-axis
using **
by (simp add: poincare-line-0-real-is-x-axis)

thus ?P 0), (of-complex x)
USING ¥ * KK FORK
using cross-ratio-not-inf|of 0, of-complex 1 of-complex (—1) of-complex x|
using cross-ratio-not-inf|of 0, of-complex (—1) of-complex 1 of-complex x]
using cross-ratio-real[of 0 —1 x 1] cross-ratio-real{of 0 1 « —1]

44
apply (auto simp add: poincare-line-0-real-is-x-axis doubleton-eq-iff circline-set-x-axis)
apply (subst cross-ratio, simp-all, subst Re-complex-div-gt-0, simp, subst mult-neg-neg, simp-all)+
done
next
fix Muv
let ?Mu = moebius-pt Mu and ?Mv = moebius-pt M v
assume *: unit-disc-fix M u € unit-disc v € unit-disc u # v
?P ?Mu ?Mv
show ?P uv
proof safe
fix il i2
let ?cr = cross-ratio u il v i2
assume %«: ideal-points (poincare-line uv) = {i1, i2}
have i1 Auil Avi2fAui2Arvil F i2
using ideal-points-different|OF *(2—3), of i1 i2] xx «uA vw
by auto
hence 0 < Re (to-complex ?cr) A is-real (to-complex ?cr) \ ?er # &h
using * **
apply (erule-tac c=moebius-pt M il in allE)
apply (erule-tac c=moebius-pt M i2 in allE)
apply (subst (asm) ideal-points-poincare-line-moebius|of M u v il i2], simp-all)
done
thus 0 < Re (to-complex ?cr) is-real (to-complex ?cr) ?cr = con => False
by simp-all
qed
qed

Next we can show that for every different points from the unit disc there is exactly one number that satisfies
the h-distance predicate.

lemma distance-unique:
assumes u € unit-disc and v € unit-disc
shows 3! d. poincare-distance-pred u v d
proof (cases u = v)
case True
thus ?thesis
by auto
next
case False
obtain if i2 where «: il 4 i2 ideal-points (poincare-line u v) = {il, i2}
using obtain-ideal-points|OF is-poincare-line-poincare-line| (u # v»
by blast
let ?d = calc-poincare-distance u il v i2
show ?thesis
proof (rule ex11)
show poincare-distance-pred uv ?d
using * <u # v>
proof (simp del: calc-poincare-distance-def, safe)
fix i1' i2’
assume {i1, i2} = {il’, i2'}
hence *«: (i1' = il A i2'= i2) v (i1' = i2 A i2' = il)
using doubleton-eq-iff [of i1 i2 i1' i2']
by blast
have all-different. uA iLuAWvAiUvA Duk il us i2'vAil' vs i2' il 4 i2
using ideal-points-different|OF assms, of i1 i2] * ** cu # uv»
by auto

show calc-poincare-distance u il v i2 = cale-poincare-distance u il’ v i2'
proof—

let ?cr = cross-ratio u il v i2

let ?cr’ = cross-ratio u il’ v i2'

have Re (to-complex ?cr) > 0 is-real (to-complex ?cr)
Re (to-complex ?cr') > 0 is-real (to-complex ?cr’)
using False distance-cross-ratio-real-positive|OF assms(1—2)] * **
by auto
thus ?thesis
using **
using cross-ratio-not-zero cross-ratio-not-inf all-different
by auto (subst cross-ratio-commute-24, subst reciprocal-real, simp-all add: In-div)
qed
qed
next
fix d
assume poincare-distance-pred uv d
thus d = ?d
using * <u # v>
by auto
qed
qed

lemma poincare-distance-satisfies-pred [simp]:
assumes u € unit-disc and v € unit-disc
shows poincare-distance-pred u v (poincare-distance u v)
using distance-unique[OF assms| thel [of poincare-distance-pred u v]
unfolding poincare-distance-def
by blast

lemma poincare-distance-I:
assumes u € unit-disc and v € unit-disc and u # v and ideal-points (poincare-line u v) = {i1, i2}
shows poincare-distance uv = calc-poincare-distance u il v i2
using assms
using poincare-distance-satisfies-pred|OF assms(1—2)|
by simp

lemma poincare-distance-refl [simp]:
assumes u € unit-disc
shows poincare-distance uu = 0
using assms
using poincare-distance-satisfies-pred|OF assms assms]
by simp

Unit disc preserving Mobius transformations preserve h-distance.

lemma unit-disc-fit-preserve-poincare-distance [simp|:
assumes unit-disc-fix M and u € unit-disc and v € unit-disc
shows poincare-distance (moebius-pt M u) (moebius-pt M v) = poincare-distance u v
proof (cases u = v)
case True
have moebius-pt M u € unit-disc moebius-pt M v € unit-disc
using wnit-disc-fiz-iff[OF assms(1), symmetric] assms
by blast+
thus ?thesis
using assms (u = v)
by simp
next
case False
obtain if i2 where »: ideal-points (poincare-line u v) = {i1, i2}
using <u 4 v)
by (rule obtain-ideal-points|OF is-poincare-line-poincare-line|of u v])
let ?Mu = moebius-pt Mu and ?Mv = moebius-pt Mv and ?Mil = moebius-pt M il and ?Mi2 = moebius-pt M i2

have **: ?Mu € unit-disc ?Mv € unit-disc
using assms
using unit-disc-fir-iff
by blast+

have «xx: ?Mu # ?Mv
using <u 4 v)
by simp
have poincare-distance uv = calc-poincare-distance u il v i2

using poincare-distance-I|OF assms(2—3) <u # v> *]

46
by auto

moreover

have unit-circle-fix M
using assms
by simp

hence ++: ideal-points (poincare-line ?7Mu ?Mv) = {?Mil, ?Mi2}
using <u # v) assms *
by simp

have poincare-distance ?Mu ?Mv = calc-poincare-distance ?Mu ?Mil ?Mv ?Mi2
by (rule poincare-distance-I[OF ** *** ++])

moreover

have calc-poincare-distance ?Mu ?Mil ?Mv ?Mi2 = calc-poincare-distance u il v i2
using ideal-points-different|OF assms(2—3) <u # v» *]
unfolding calc-poincare-distance-def
by (subst moebius-preserve-cross-ratio|symmetric], simp-all)

ultimately

show ?thesis
by simp

qed

Knowing ideal points for x-axis, we can easily explicitly calculate distances.

lemma poincare-distance-x-axis-x-axis:
assumes «x € unit-disc and y € unit-disc and « € circline-set x-axis and y € circline-set x-axis
shows poincare-distance x y =
(let x’ = to-complex x; y’ = to-complex y
in abs (In (Re (((1 +2’) * (1 — y’)) / (1-2) * (1 + y9)))))
proof—
obtain x’ y’ where *: x = of-complex x' y = of-complex y'
using inf-or-of-complez|of x] inf-or-of-complex|of y] «x € unit-discy <y € unit-disc»
by auto

have cmod x’ < 1 cmod y' < 1
using (x € unit-disc) <y € unit-discy *
by (metis unit-disc-iff-cmod-It-1)+
hence ««: 2’ A 1a’ A1y'A-1y'Al
by auto

have 1 + y'#0
using **
by (metis add.left-cancel add-neg-numeral-special(7))

show ?thesis
proof (cases t = y)
case True
thus ?thesis
using assms(1—2)
using wunit-disc-iff-cmod-lt-1|of to-complex x] * ** (1 + y’ # 0»
by auto

next
case False
hence poincare-line x y = z-axis
using poincare-line-x-axis| OF assms]
by simp
hence ideal-points (poincare-line x y) = {of-complex (—1), of-complex 1}
by simp
hence poincare-distance x y = calc-poincare-distance x (of-complex (—1)) y (of-complex 1)
using poincare-distance-I assms (x # y>
by auto
also have ... = abs (In (Re (((2’ + 1) * (y’— 1)) / ((x’ — 1) * (y’+ 1)))))
using * <cmod x’ < 1» «cmod y' < 1>
by (simp, transfer, transfer, auto)
finally
show ?thesis
using *
by (metis (no-types, lifting) add.commute minus-diff-eq minus-divide-divide mult-minus-left mult-minus-right

47
to-complex-of-complez)
qed
qed

lemma poincare-distance-zero-x-axis:
assumes «x € unit-disc and « € circline-set x-axis
shows poincare-distance 0, x = (let x’ = to-complex x in abs (In (Re ((1 — x’) / (4 + &')))))
using assms
using poincare-distance-z-axis-x-axis[of 0), 2]
by (simp add: Let-def)

lemma poincare-distance-zero:
assumes x € unit-disc
shows poincare-distance 0p x = (let x’ = to-complex x in abs (In (Re ((1 — cmod x’) / (1 + cmod x'))))) (is ?P 2)
proof (cases t = 0p)
case True
thus ?thesis
by auto
next
case False
show ?thesis
proof (rule wlog-rotation-to-positive-z-azis)
show «x € unit-disc « £ 0; by fact+
next
fix yu
assume wu € unit-disc u # On ?P (moebius-pt (moebius-rotation y) u)
thus ?P u
using unit-disc-fix-preserve-poincare-distance|of moebius-rotation y On ul
by (cases u = cop) (simp-all add: Let-def)
next
fix x
assume is-real x 0 < Rex Rex < 1
thus ?P (of-complex x)
using poincare-distance-zero-x-axis[of of-complex |
by simp (auto simp add: circline-set-z-axis cmod-eq-Re complex-is-Real-iff)
qed
qed

lemma poincare-distance-zero-opposite [simp]:
assumes of-compler z € unit-disc
shows poincare-distance 0 (of-compler (— z)) = poincare-distance Op (of-complex z)
proof—
have «: of-compler (—z) € unit-disc
using assms
by auto
show ?thesis
using poincare-distance-zero[OF assms]
using poincare-distance-zero[OF *]
by simp
qed
