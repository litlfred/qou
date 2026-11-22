---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-002-hyperbolic-functions
section_title: "Hyperbolic Functions"
section_number: null
pages: 3-4
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
In this section hyperbolic cosine and hyperbolic sine functions are introduced and some of their properties
needed for further development are proved.

theory Hyperbolic-Functions
imports Complez-Main Complex-Geometry. More-Complex
begin

lemma arcosh-eq-iff:
fixes x y::real
assumes z > 1 y > 1
shows arcosh x = arcosh y+— «= y
by (smt (verit, best) arcosh-less-iff-real arcosh-real-strict-mono assms)

lemma cosh-gt-1 [simp]:
fixes x ::real
assumes x > 0
shows cosh « > 1
using assms cosh-real-strict-mono by force

lemma cosh-eq-iff:
fixes x y::real
assumes rt > 0y > 0
shows cosh t = cosh y+ t= y
by (simp add: assms)

lemma arcosh-mono:
fixes x y::real
assumes z > 1 y > 1
shows arcosh x > arcosh y+— «> y
using arcosh-less-iff-real assms linorder-not-le by blast

lemma arcosh-add:

fixes x y::real

assumes z > 1 y > 1

shows arcosh x + arcosh y = arcosh (xxy + sqrt((x? — 1)*(y*? — 1)))
proof—

have sqrt ((x? — 1) * (y? — 1))>0
using assms
by simp
moreover
have sz * y> 1
using assms
by (smt mult-le-cancel-left1)
ultimately
have **: « * y + sqrt ((2* — 1) *(y?— 1))>1
by linarith
hence 1: 0 < (x * y + sqrt ((x? — 1) * (y? — 1)))? - 1
by simp

have 2: x * sqrt (y? — 1) + y * sqrt (a? — 1) > 0
using assms
by simp

have (xr*sqrt(y? — 1)+y*sqrt(x? —1))? = (sqrt((axy+sqrt((2?—1)*(y?—1)))? — 1))?
using assms
proof (subst real-sqrt-pow2)
show 0 < (x * y + sqrt ((x” — 1) * (y? — 1)))? — 1
by fact
next
have (a * sqrt (y? — 1))? = 2? * (y? — 1)
by (simp add: <y > 1» power-mult-distrib)
moreover
have (y * sqrt (a? — 1))? = y? * (a? — 1)
using assms by (simp add: power-mult-distrib)
ultimately show (a * sqrt (y? — 1) + y * sqrt (a? — 1))? = (a * y + sqrt ((x? — 1) * (y? — 1)))? - 1
using assms
unfolding power2-sum
apply (simp add: real-sqrt-mult power-mult-distrib)
apply (simp add: field-simps)
done
qed
hence sqrt ((x * y + sqrt ((2* — 1) * (y? — 1)))? — 1) = 2 * sqrt (y° — 1) + y * sqrt (x? — 1)
using power2-eq-iff-nonneg|OF 2 real-sqrt-ge-zero[OF 1]]
by simp
thus ?thesis
using assms **
apply (simp add: arcosh-real-def )
apply (subst In-mult-pos[symmetric])
apply (smt one-le-power real-sqrt-ge-zero)
apply (smt (verit) one-le-power real-sqrt-ge-zero)
by (smt (verit) distrib-right mult.commute real-sqrt-mult)
qed

lemma arcosh-double:
fixes x :: real
assumes z > 1
shows 2 * arcosh x = arcosh (2«x? — 1)
by (smt arcosh-add arcosh-mono assms one-power2 power2-eq-square real-sqrt-abs)

end
