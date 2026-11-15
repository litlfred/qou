---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-024-distance-explicit-formula
section_title: "Distance explicit formula"
section_number: null
pages: 48-54
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Instead of the h-distance itself, very frequently its hyperbolic cosine is analyzed.

abbreviation cosh-dist uv = cosh (poincare-distance wu v)

lemma cosh-poincare-distance-cross-ratio-average:
assumes wu € unit-disc v € unit-disc u # v ideal-points (poincare-line uv) = {i1, i2}
shows cosh-dist uv =
((Re-cross-ratio u il v i2) + (Re-cross-ratio v il u i2)) / 2
proof—
let ?cr = cross-ratio u il v i2
let ?crRe = Re (to-complex ?cr)
have ?cr # oop is-real (to-complex ?cr) ?crRe > 0
using distance-cross-ratio-real-positive|OF assms(1—3)] assms(4)
by simp-all

48
then obtain cr where *: cross-ratio u il v i2 = of-complex cr cr # 0 is-real cr Re cr > 0
using inf-or-of-complez|of cross-ratio u il v i2]
by (smt to-complex-of-complex zero-complex.simps(1))
thus ?thesis
using *
using assms cross-ratio-commute-13 [of v il u i2]
unfolding poincare-distance-I{OF assms] calc-poincare-distance-def cosh-def
by (cases Re cr > 1)
(auto simp add: In-div[of 0] exp-minus field-simps Re-divide power2-eq-square complex. expand)
qed

definition poincare-distance-formula' :: complet = complex = real where
[simp]: poincare-distance-formula’ uv = 1 + 2 * ((emod (u — v))? / ((1 — (emod u)?) * (1 — (emod v)?)))

Next we show that the following formula expresses h-distance between any two h-points (note that the ideal
points do not figure anymore).

definition poincare-distance-formula :: complex = complex = real where
[simp]: poincare-distance-formula uv = arcosh (poincare-distance-formula’ u v)

lemma blaschke-preserve-distance-formula [simp]:
assumes of-complex k € unit-disc u € unit-disc v € unit-disc
shows poincare-distance-formula (to-complex (moebius-pt (blaschke k) u)) (to-complex (moebius-pt (blaschke k) v)) =
poincare-distance-formula (to-complez u) (to-complex v)
proof (cases k = 0)
case True
thus ?thesis
by simp
next
case False
obtain u’ v’ where «: u’ = to-complex u v' = to-complex v
by auto

have cmod u' < 1 cmod v' < 1 cmodk < 1
using assms *
using inf-or-of-complez[of u] inf-or-of-complez|of v]
by auto

obtain nu du nv dv d kk ddu ddv where
xe nu =u’ —kdu=1— enjk eu’ nv =v'—kdv=1—-cnjkx*v'
d=u'—v' ddu=1 — u'xcnj u! ddv = 1 — v'xenj uv! kk = 1 — keenjk
by auto

have d: nuxdv — nvxdu = dxkk
by (subst *«)+ (simp add: field-simps)
have ddu: duxcnj du — nuxcnj nu = dduxkk
by (subst *«)+ (simp add: field-simps)
have ddv: dvxcnj dv — nvxcnj nv = dduxkk
by (subst *«)+ (simp add: field-simps)

have du # 0
proof (rule ccontr)
assume — ?thesis
hence cmod (1 — enjk * u') = 0
using (du = 1 — cnjk * uy
by auto
hence cmod (cnj k *« u') = 1
by auto
thus False
using (cmod k < 1> «cmod u' < 1>
using mult-strict-mono|of cmod k 1 cmod u’ 1]
by (simp add: norm-mult)
qed

have dv 4 0

proof (rule ccontr)
assume — ?thesis

49
hence cemod (1 — enjk * v') = 0
using (dv = 1 — cnjk * vy
by auto

hence emod (cnj k * v’) = 1
by auto

thus False
using <cmod k < 1» «cmod v' < 1»
using mult-strict-mono|of cmod k 1 cmod v' 1]
by (simp add: norm-mult)

qed

have kk # 0
proof (rule ccontr)
assume — ?thesis
hence cmod (1 — k « cnj k) = 0
using «kk = 1 — k x cnj ky
by auto
hence cmod (k * cnj k) = 1
by auto
thus False
using (cmod k < 1)
using mult-strict-mono|of cmod k 1 cmod k 1]
using complez-mod-sqrt-Re-mult-cnj by auto
qed

note nz = (du # 0» «du # 0» ‘kk F O»

have nu / du — nv / dv = (nuxdv — nuxdu) / (du « dv)
using nz
by (simp add: field-simps)
hence (cmod (nu/du — nv/dv))? = cemod ((d*kk) / (duxdu) * (enj ((d*kk) / (duxdv)))) (is 2lhs = -)
unfolding complez-mod-mult-cnj[symmetric]
by (subst (asm) d) simp
also have ... = cmod ((d«cnj dxkkxkk) / (duxcnj duxduxcnj dv))
by (simp add: field-simps norm-mult norm-divide)
finally have 1: ?lhs = cmod ((dxenj dxkkxkk) / (duxcnj duxduxcnj dv)) .

have (1 — ((emod nu) / (cmod du))?)*(1 — ((emod nv) / (emod dv))?) =
(1 — cmod((nu * cnj nu) / (du * enj du)))*(1 — emod((nv * enj nv) / (du * cnj dv))) (is ?rhs = -)
by (metis norm-divide complex-mod-mult-cnj power-divide)
also have ... = cmod(((duxcnj du — nuxcnj nu) / (du * cnj du)) * ((duxenj dv — nuxenj nv) / (du * cnj dv)))
proof—
have u’ 4 1 / enjkv' A 1 / cnjk
using <cmod u' < 1» «cmod v' < 1» «emod k < 1
by (auto simp add: False norm-divide)
moreover
have cmod k # 1
using (cmod k < 1)
by linarith
ultimately
have cmod (nu/du) < 1 cmod (nu/dv) < 1
using **(1—4)
using unit-disc-fir-discI[OF blaschke-unit-disc-fit[OF <cmod k < 1>| «u € unit-disc»] <u’ = to-complex wu
using unit-disc-fir-discl[OF blaschke-unit-disc-fix[|OF «cmod k < 1%] «v € unit-disc»] <v' = to-complez v»
using inf-or-of-complez[of u] <u € unit-discy inf-or-of-complex|of v] «v € unit-discr
using mocbius-pt-blaschke[of k u’| using moebius-pt-blaschke[of k v']
by auto
hence (cmod (nu/du))? < 1 (emod (nv/dv))? < 1
by (simp-all add: cmod-def)
hence cmod (nu * cnj nu / (du * enj du)) < 1 cmod (nv * cnj nv / (dv * cnj dv)) < 1
by (metis complex-mod-mult-cnj norm-divide power-divide)+
moreover
have is-real (nu « cnj nu / (du * enj du)) is-real (nv * cnj nv / (dv * cnj dv))
using eq-cnj-iff-real[of nu * cnj nu / (du * cnj du)|
using eq-cnj-iff-reallof nv * cnj nv / (du * enj dv)]
by (auto simp add: mult.commute)

moreover

have Re (nu * cnj nu / (du * cnj du)) > 0 Re (nv * cnj nv / (du * enj dv)) > 0
using (du # 0) «dv £ 0»
unfolding complex-mult-cnj-cmod
by simp-all

ultimately

have 1 — cmod (nu * cnj nu / (du « cnj du)) = cmod (1 — nu * cnj nu / (du * cnj du))

1 — cmod (nv * cnj nv / (du * cnj dv)) = cmod (1 — nv * cnj nv / (dv * enj dv))

by (simp-all add: cmod-def)

thus ?thesis

using nz
by (simp add: diff-divide-distrib norm-mult)
qed
also have ... = cmod(((ddu * kk) / (du * cnj du)) * ((ddv * kk) / (du * cnj dv)))
by (subst ddu, subst ddv, simp)
also have ... = cmod((dduxdduxkk«kk) / (duxcnj duxduxcnj dv))

by (simp add: field-simps)
finally have 2: ?rhs = cmod((dduxdduxkk«xkk) / (duxcnj duxdu«cnj dv))

have ?lhs / ?rhs =
cmod ((d*cnj dxkkxkk) / (duxcnj duxduxcnj dv)) / cmod((dduxdduxkk*kk) / (duxcnj duxduxcnj dv))

by (subst 1, subst 2, simp)

also have ... = cmod ((d*cnj d)/(dduxddv))

using nz by (simp add: norm-mult norm-divide)
also have ... = (cmod d)? / ((1 — (emod u')?)*(1 — (emod v')?))
proof—

have (cmod u’)? < 1 (cmod v’)? < 1
using <cmod u' < 1» «cmod v' < 1>
by (simp-all add: cmod-def)
hence cmod (1 — u' * enj u’) = 1 — (emod u’)? emod (1 — v! * enj v') = 1 — (emod v')?
by (auto simp add: cmod-eq-Re cmod-power2 power2-eq-square|symmetric])
thus ?thesis
using nz
by (simp add: **(6) **(7) norm-divide norm-mult power2-eq-square)
qed
finally
have 3: ?lhs / ?rhs = (emod d)? / ((1 — (emod u’)?)*(1 — (emod v')?)) «

have cmodk 4 1u' 41 / cnjkv' £1 / cnjkuF won vF Wn
using <cmod k < 1) <u € unit-disc» «v € unit-discy * (k A 0» ** «kk # Oy nz
by auto

thus ?thesis using assms
using * ** 3
using moebius-pt-blaschke|of k u'|
using moebius-pt-blaschke[of k v']
by (simp add: norm-divide)

qed

To prove the equivalence between the h-distance definition and the distance formula, we shall employ the without
loss of generality principle. Therefore, we must show that the distance formula is preserved by h-isometries.

Rotation preserve poincare-distance-formula.

lemma rotation-preserve-distance-formula [simp]:

assumes u € unit-disc v € unit-disc

shows poincare-distance-formula (to-complex (moebius-pt (moebius-rotation y) u)) (to-complex (moebius-pt (moebius-rotation
gy) vy) =

poincare-distance-formula (to-complez u) (to-complex v)

using assms

using inf-or-of-complez|of u] inf-or-of-complez|of v]

by (auto simp: norm-mult)

Unit disc fixing Mébius preserve poincare-distance-formula.

lemma unit-disc-fic-preserve-distance-formula [simp]:
assumes unit-disc-fix Mu € unit-disc v € unit-disc
shows poincare-distance-formula (to-complez (moebius-pt M u)) (to-complex (moebius-pt M v)) =
poincare-distance-formula (to-complez u) (to-complez v) (is ?P’ uv M)
proof—
have V u € unit-disc. V v € unit-disc. ?P' uv M (is ?P M)
proof (rule wlog-unit-disc-fix|OF assms(1)])
fix k
assume cmod k < 1
hence of-complez k € wnit-disc
by simp
thus ?P (blaschke k)
using blaschke-preserve-distance-formula
by simp
next
fix y
show ?P (moebius-rotation »)
using rotation-preserve-distance-formula
by simp
next
fix M1 M2
assume *: ?P M1 and *«*: ?P M2 and w11: unit-disc-fix M1 unit-disc-fix M2
thus ?P (M1 + M2)
by (auto simp del: poincare-distance-formula-def )
qed
thus ?thesis
using assms
by simp
qed

The equivalence between the two h-distance representations.

lemma poincare-distance-formula:
assumes u € unit-disc and v € unit-disc
shows poincare-distance u v = poincare-distance-formula (to-complex u) (to-complex v) (is ?P uv)
proof (rule wlog-x-azis)
fix x
assume *: is-real zr 0 < Rex Rex < 1
show ?P 0» (of-complex x) (is ?lhs = ?rhs)
proof—
have of-complex x € unit-disc of-complex x € circline-set x-axis cmod x < 1
using * cmod-eq-Re
by (auto simp add: circline-set-x-azis)
hence ?lhs = |In (Re ((1 — x) / (1 + 2)))|
using poincare-distance-zero-x-axis[of of-complex |
by simp
moreover
have ?rhs = |In (Re ((1 — 2) / (1 + 2)))|
proof —
let 2x = 1 + 2 * (emod x)? / (1 — (emod 2)?)
have 0 < 2 * (cmod x)? / (1 — (emod x)?)
by (smt <cmod x < 1) divide-nonneg-nonneg norm-ge-zero power-le-one zero-le-power2)
hence arcosh-real-gt: 1 < ?x

by auto
have ?rhs = arcosh ?x

by simp
also have ... = In ((1 + (cmod x)”) / (1 — (emod x)?) + 2 * (emod x) / (1 — (cmod x)?))
proof—

have 1 — (cmod x)? > 0

using (cmod x < 1»

by (smt norm-not-less-zero one-power2 power2-eq-imp-eq power-mono)
hence 1: 2x = (1 + (cmod x)”) / (1 — (emod x)?)

by (simp add: field-simps)
have 2: ?1? — 1 = (4 * (cmod x)”) / (1 — (emod x)*)?

using «1 — (cmod x)? > 0»

apply (subst 1)

unfolding power-divide

by (subst divide-diff-eq-iff, simp, simp add: power2-eq-square field-simps)
show ?thesis
using «1 — (cmod x)? > 0»
apply (subst arcosh-real-def|OF arcosh-real-gt])
apply (subst 2)
apply (subst 1)
apply (subst real-sqrt-divide)
apply (subst real-sqrt-mult)
apply simp
done
qed
also have ... = In (((1 + (emod x))*) / (1 — (emod x)?))
apply (subst add-divide-distrib|symmetric])
apply (simp add: field-simps power2-eq-square)
done
also have ... = In ((1 + cmod x) / (1 — (cmod z)))
using (cmod « < 1»
using square-diff-square-factored|of 1 cmod a]
by (simp add: power2-eq-square)
also have ... = |In (Re ((1 — z) / (1 + 2)))|
proof—
have «: Re ((1 — x) / (1 +2)) <1 Re ((1 — 2) / (1+ 2))>0
using <is-real z» «(Re x > 0) (Rea < 1»
using complex-is-Real-iff
by auto
hence |In (Re ((1 — x) / (1 + 2)))| = — In (Re ((1 — z) / (1 + 2)))
by auto
hence |In (Re ((1 — x) / (1 + 2)))| = In (Re ((1 +. z) / (1 — 2)))
using In-divlof 1 Re ((1 — x)/(1 + 2))] * <és-real x»
by (fastforce simp: complex-is-Real-iff)
moreover
have In ((1 + cmod x) / (1 — cmod x)) = In ((1 + Rez) / (1 — Re z))
using (Re x > 0)» <is-real x»
using cmod-eq-Re by auto
moreover
have (1 + Re x) / (1 — Re x) = Re ((1 +z) / (1 - 2))
using <is-real z» «Re x < 1>
by (smt Re-divide-real eq-iff-diff-eq-0 minus-complex.simps one-complez.simps plus-complex.simps)
ultimately
show ?thesis
by simp
qed
finally
show ?thesis

qed
ultimately
show ?thesis
by simp
qed
next
fix Muv
assume *: unit-disc-fir M wu € unit-disc v € unit-disc
assume ?P (mocbius-pt M u) (moebius-pt M v)
thus ?Puv
using *(1—3)
by (simp del: poincare-distance-formula-def )
next
show wu € unit-disc v € unit-disc
by fact+
qed

Some additional properties proved easily using the distance formula.

poincare-distance is symmetric.

lemma poincare-distance-sym:
assumes u € unit-disc and v € unit-disc
shows poincare-distance u v = poincare-distance v u
using assms

using poincare-distance-formula[OF assms(1) assms(2)]
using poincare-distance-formula[OF assms(2) assms(1)]
by (simp add: mult.commute norm-minus-commute)

lemma poincare-distance-formula'-ge-1:
assumes u € unit-disc and v € unit-disc
shows 1 < poincare-distance-formula’ (to-complex u) (to-complez v)
using unit-disc-cmod-square-lt-1|OF assms(1)| unit-disc-cmod-square-lt-1[OF assms(2)]
by auto

poincare-distance is non-negative.

lemma poincare-distance-ge0:
assumes u € unit-disc and v € unit-disc
shows poincare-distance uv > 0
using poincare-distance-formula'-ge-1 assms by (simp add: poincare-distance-formula)

lemma cosh-dist:
assumes u € unit-disc and v € unit-disc
shows cosh-dist uv = poincare-distance-formula’ (to-complex u) (to-complez v)
using poincare-distance-formula[OF assms| poincare-distance-formula'-ge-1[OF assms]
by simp

poincare-distance is zero only if the two points are equal.

lemma poincare-distance-eq-0-iff :
assumes u € unit-disc and v € unit-disc
shows poincare-distance uv = 0 +> u=v
using assms
apply auto
using poincare-distance-formula'-ge-1[OF assms]
using unit-disc-cmod-square-lt-1|OF assms(1)| unit-disc-cmod-square-lt-1[OF assms(2)]
apply (simp add: poincare-distance-formula)
by (simp add: unit-disc-to-complex-inj)

Conjugate preserve poincare-distance-formula.

lemma conjugate-preserve-poincare-distance [simp]:
assumes u € unit-disc and v € unit-disc
shows poincare-distance (conjugate u) (conjugate v) = poincare-distance u v
proof—
obtain u’ v' where «: u = of-complex u' v = of-complex v'
using assms inf-or-of-complez|of u] inf-or-of-complez|of v]
by auto

have **: conjugate u € unit-disc conjugate v € unit-disc
using * assms
by auto

show ?thesis
using *
using poincare-distance-formula|OF assms]
using poincare-distance-formula[OF x]
by (metis complez-cnj-diff complex-mod-cnj conjugate-of-complex poincare-distance-def poincare-distance-formula'-def
poincare-distance-formula-def to-complex-of-complex)
qed
