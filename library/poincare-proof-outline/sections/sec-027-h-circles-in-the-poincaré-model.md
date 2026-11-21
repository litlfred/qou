---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-027-h-circles-in-the-poincaré-model
section_title: "H-circles in the Poincaré model"
section_number: null
pages: 67-71
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Circles consist of points that are at the same distance from the center.

definition poincare-circle :: compler-homo = real = complex-homo set where
poincare-circle zr = {z’. z' € unit-disc A poincare-distance z z' = r}

Each h-circle in the Poincaré model is represented by an Euclidean circle in the model — the center and radius
of that euclidean circle are determined by the following formulas.

definition poincare-circle-euclidean :: compler-homo => real => euclidean-circle where
poincare-circle-euclidean zr =
(let R = (cosh r — 1) / 2;
z' = to-complezx z;
cz = 1 — (emod z')?;
k=cz*R+1
in (z' / k, cz * sqrt(R * (R + 1)) / k))

That Euclidean circle has a positive radius and is always fully within the disc.

lemma poincare-circle-in-disc:
assumes r > 0 and z € unit-disc and (ze, re) = poincare-circle-euclidean zr
shows cmod ze < 1 re > 0V « € circle ze re. cmod x < 1
proof—
let ?R = (cosh r — 1) / 2
let ?z’ = to-complex z
let 2cz = 1 — (cmod ?z')?
let ?k = ?cz * PR+ 1
let ?2ze = ?z' / ?k
let ?re = ?cz * sqrt(?R * (?R + 1)) / ?k

67
from <z € unit-discy

obtain z’ where z’: z = of-complezx z'
using inf-or-of-complez|of z]
by auto

hence z’ = ?z'
by simp

obtain cz where cz: cz = (1 — (cmod z’)*)
by auto

have cz > 0cz < 1
using <z € unit-disc> 2’ cz
using unit-disc-cmod-square-lt-1
by fastforce+

obtain R where R: R = ?R
by blast

have R > 0
using cosh-gt-1[of r] «r > 0>
by (subst R) simp

obtain k where k: k = cz * R+ 1
by auto

have k > 1
using k «R > 0) «cz > 0»
by simp

hence cmod k = k
by simp

let ?RR = cz * sqrt(R*(R+1))/k

have cmod z' + cz * sqrt(R x (R+1))<k
proof—
have ((R+1)—R)? > 0
by simp
hence (R+1)? — 2«Rx(R+1) + R? > 0
unfolding power2-diff
by (simp add: field-simps)
hence (R+1)? + 2*R*(R+1) + R? — 4*Rx(R+1) > 0
by simp
hence (2*R+1)? / 4 > R*(R+1)
using power2-sum|of R+1 R]
by (simp add: field-simps)
hence sqrt(R*(R+1)) < (2*R+1) / 2
using «R > 0>
by (smt arith-geo-mean-sqrt power-divide real-sqrt-four real-sqrt-pow2 zero-le-mult-iff)
hence sqrt(R*(R+1)) — R < 1/2
by (simp add: field-simps)
hence (1 + (cmod z')) * (sqrt(R*(R+1)) — R) < (1 + (emod z’)) « (1 / 2)
by (subst mult-strict-left-mono, simp, smt norm-not-less-zero, simp)
also have ... < 1
using <z € unit-disc> z'
by auto
finally have (1 — cmod z') « ((1 + cmod z’) * (sqrt(R*x(R+1)) — R)) < (1 — cmod 2’) * 1
using (z € unit-discy z’
by (subst mult-strict-left-mono, simp-all)
hence cz * (sqrt (Rx(R+1)) — R) < 1 — cmod z’
using square-diff-square-factored[of 1 cmod z’|
by (subst cz, subst (asm) mult.assoc|symmetric], simp add: power2-eq-square field-simps)
hence cmod z' + cz * sqrt(Rx(R+1)) < 1+ Rx cz
by (simp add: field-simps)

68
thus ?thesis
using k
by (simp add: field-simps)
qed
hence cmod z' / k + cz * sqrt(R*(R+1))/k< 1
using «k > 1>
unfolding add-divide-distrib|symmetric]
by simp
hence cmod (z' / k) + cz * sqrt(R * (R+1))/k<1
using «k > 1>
by simp
hence cmod ?ze + ?re < 1
using k cz (R = ?R> z'
by simp

moreover

have cz * sqrt(R * (R+1))/k>0
using (cz > 0) (R> 0) «k > I>
by auto

hence ?re > 0
using k cz (R = ?R> z'
by simp

moreover

have cmod ?ze < 1
using <cmod ?ze + ?re < 1» <?re > 0»
by simp

moreover

have ze = ?ze re = ?re
using <(ze, re) = poincare-circle-euclidean z r>
unfolding poincare-circle-euclidean-def Let-def
by simp-all

moreover

have V a € circle ze re. cmod x < cmod ze + re
using norm-triangle-ineg2 [of - ze]
unfolding circle-def
by (smt mem-Collect-eq)

ultimately

show cmod ze < 1 re > 0V « € circle ze re. cmod & < 1
by auto
qed

The connection between the points on the h-circle and its corresponding Euclidean circle.

lemma poincare-circle-is-euclidean-circle:
assumes z € unit-disc and r > 0
shows let (Ze, Re) = poincare-circle-euclidean z r
in of-complex ‘ (circle Ze Re) = poincare-circle zr
proof—
{
fix x
let ?z = to-complex z

from assms obtain z’ where z’: z = of-complex z' cmod z' < 1
using inf-or-of-complez[of z|
by auto

have *: (x. cmod t < 1 => 1 — (emod x)? > 0

by (metis less-iff-diff-less-O0 minus-diff-eq mult. left-neutral neg-less-0-iff-less norm-mult-less norm-power power2-eq-square)

69
let ?R = (cosh r — 1) / 2
obtain R where R: R = ?R
by blast

let ?cx = 1 — (cmod x)? and ?cz = 1 — (cmod z')?

and ?czr = (cmod (z' — 2))?
let 2k = 1+ R* ?cz
obtain k where k: k = ?k
by blast
have R > 0
using R cosh-gt-1[OF «r > 0]
by simp

hence k > 1
using assms z' k x[of z’]
by auto

hence «*: cork 4 0
by (smt of-real-eq-0-iff)

have of-complex x € poincare-circle z r <—+ cmod « < 1 A poincare-distance z (of-complex x) = r
unfolding poincare-circle-def
by auto
also have ... <—> cmod x < 1 A poincare-distance-formula’ ?z x = cosh r
using poincare-distance-formula|of z of-complex x| cosh-dist{of z of-complex x]
unfolding poincare-distance-formula-def
using assms
using arcosh-cosh-real
by auto
also have ... + cmod a < 1 A ?czu / (?cz * cx) = ?R
using z’
by (simp add: field-simps)
also have ... <—+ cmod x < 1 A ?czx = ?R * ?cau * ?cz
using assms z' «lof z'] *[of z]
using nonzero-divide-eq-eqlof (1 — (emod «)”) * (1 — (emod z')?) (emod (z' — x))? ?R]
by (auto, simp add: field-simps)
also have ... ~—> cmod x < 1 A (2' — &) * (enjz' — enjx) = R * ?cz * (1 — x * cnj a) (is - <> - A 21 = 2r)
proof —
let 71 = (z' — x) * (enj z' — enj x) and ?r = R * (1 — Re (z' * enj z’)) * (1 — & * cnj x)
have is-real ?1
using eq-cnj-iff-real[of 71]
by simp
moreover
have is-real ?r
using eq-cnj-iff-real[of 1 — x * cnj x]
using Im-complez-of-reallof R « (1 — Re (z' * cnj z'))]
by simp
ultimately
show ?thesis
apply (subst R[symmetric])
apply (subst cmod-square)+
apply (subst complex-eq-if-Re-eq, simp-all add: field-simps)
done
qed
also have ... + cmod x < 1 A 2’ * enjz'— 2 * cnjz'— cnjxxz'+a*cenjx=Rx* ?cx— Rx Pez * x * CNT
unfolding right-diff-distrib left-diff-distrib
by (simp add: field-simps)
also have ... <> cmodz < 1 A k * ( * cnj x) — & * cnj 2’ — enj a * 2’ + 2’ * cnj z'= R * ?cz (is - +9 - A
?lhs = rhs)
by (subst k) (auto simp add: field-simps)
also have ... + cmodz < 1 A (kx a * enjz — 2 * cenjz’— enja*2z'+2'% cnjz')/k=(R* ?cz) /k
using **
by (auto simp add: Groups.mult-ac(1))
also have ... + cmoda < 1 Ax* cenjx—axcnjz'/k—enjxxz'/k+2'* enjz'’/k=(R* ?cz)/k
using **

70
unfolding add-divide-distrib diff-divide-distrib
by auto
also have ... <—> cmod  < 1 A (a — 2'/k) * enj(x — 2'/k) = (R * cz) / k + (2'/ k) * enj(z' / kb) — 2! * enj 2’

/k
by (auto simp add: field-simps diff-divide-distrib)
also have ... <—+ cmod x < 1 A (cmod (a — 2'/k))? = (R * ?cz) / k + (emod 2’)? / k? — (emod z')? / k
apply (subst complez-mult-cnj-cmod)+
apply (subst complex-eq-if-Re-eq)
apply (simp-all add: power-divide)
done
also have ... + cmod x < 1 A (emod (a — 2'/k))? = (R* ?cz * k + (emod z')? — (emod z')? * k) / k?
using **
unfolding add-divide-distrib diff-divide-distrib
by (simp add: power2-eq-square)
also have ... <—+ cmod x < 1 A (emod (a — 2'/k))? = ?cz? x Rx (R+ 1) / k? (is - + - A ?a? = 2b)
proof —
have *: R * (1 — (emod z')?) * k + (emod z')? — (emod z’)? * k = (1 — (emod z')?)? * R* (R+ 1)
by (subst k)+ (simp add: field-simps power2-diff)
thus ?thesis
by (subst *, simp)
qed
also have ... ~—+ cmod « < 1 A cmod (x — 2'/k) = ?cz * sqrt (R*(R+1))/k
using (R > 0> *[of z'] ** «k > 1) (z € unit-disc 2’
using real-sqrt-unique|of ?a ?b, symmetric]
by (auto simp add: real-sqrt-divide real-sqrt-mult power-divide power-mult-distrib)
finally
have of-complex x € poincare-circle zr <—+ cmod z < 1 A « € circle (z'/k) (?cz * sqrt(R * (R+1)) / k)
unfolding circle-def z' k R
by simp
hence of-complex x € poincare-circle z r <—+ (let (Ze, Re) = poincare-circle-euclidean zr in cmod x < 1 Ar €
circle Ze Re)
unfolding poincare-circle-euclidean-def Let-def circle-def
using z’ Rk
by (simp add: field-simps)
hence of-complex x € poincare-circle z r <—> (let (Ze, Re) = poincare-circle-euclidean zr in x € circle Ze Re)
using poincare-circle-in-disc|OF <r > 0» (z € unit-disc»]
by auto
} note « = this
show ?thesis
unfolding Let-def
proof safe
fix Ze Re x
assume poincare-circle-euclidean zr = (Ze, Re) x € circle Ze Re
thus of-complex x € poincare-circle zr
using *[of 2]
by simp
next
fix Ze Re x
assume *«: poincare-circle-euclidean z r = (Ze, Re) x € poincare-circle zr
then obtain zx’ where 2’: z = of-complez x’
unfolding poincare-circle-def
using inf-or-of-complez|of x]
by auto
hence x’ € circle Ze Re
using *[of z/] **
by simp
thus z € of-complex ‘ circle Ze Re
using x’
by auto
qed
qed
