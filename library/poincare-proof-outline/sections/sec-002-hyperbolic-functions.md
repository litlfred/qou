---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-002-hyperbolic-functions
section_title: "Hyperbolic Functions"
section_number: null
pages: 3-4
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
In this section hyperbolic cosine and hyperbolic sine functions are introduced and some of their properties
needed for further development are proved.
theory Hyperbolic-Functions
imports Complex-Main Complex-Geometry.More-Complex
begin
lemma arcosh-eq-iﬀ:
ﬁxes x y ::real
assumes x≥ 1 y ≥ 1
shows arcosh x = arcosh y←→ x = y
by (smt (verit, best) arcosh-less-iﬀ-real arcosh-real-strict-mono assms)
lemma cosh-gt-1 [simp]:
ﬁxes x ::real
assumes x > 0
shows cosh x > 1
using assms cosh-real-strict-mono by force
lemma cosh-eq-iﬀ :
ﬁxes x y ::real
assumes x≥ 0 y ≥ 0
shows cosh x = cosh y ←→ x = y
by (simp add : assms)
lemma arcosh-mono:
ﬁxes x y ::real
assumes x≥ 1 y ≥ 1
shows arcosh x ≥ arcosh y←→ x≥ y
using arcosh-less-iﬀ-real assms linorder-not-le by blast
lemma arcosh-add:
ﬁxes x y ::real
assumes x≥ 1 y ≥ 1
shows arcosh x + arcosh y = arcosh (x∗y + sqrt((x 2− 1 )∗(y2− 1 )))
proof−
have sqrt ((x 2− 1 )∗ (y2− 1 ))≥ 0
3
using assms
by simp
moreover
have x∗ y≥ 1
using assms
by (smt mult-le-cancel-left1 )
ultimately
have∗∗: x∗ y + sqrt ((x 2− 1 )∗ (y2− 1 ))≥ 1
by linarith
hence 1 : 0≤ (x∗ y + sqrt ((x 2− 1 )∗ (y2− 1 )))2− 1
by simp
have 2 : x∗ sqrt (y2− 1 ) + y∗ sqrt (x 2− 1 )≥ 0
using assms
by simp
have (x∗sqrt(y2− 1 )+y∗sqrt(x 2−1 ))2 = ( sqrt((x∗y+sqrt((x 2−1 )∗(y2−1 )))2− 1 ))2
using assms
proof (subst real-sqrt-pow2 )
show 0≤ (x∗ y + sqrt ((x 2− 1 )∗ (y2− 1 )))2− 1
by fact
next
have (x∗ sqrt (y2− 1 ))2 = x 2∗ (y2− 1 )
by (simp add : ‹y≥ 1 › power-mult-distrib)
moreover
have (y∗ sqrt (x 2− 1 ))2 = y2∗ (x 2− 1 )
using assms by (simp add : power-mult-distrib)
ultimately show (x∗ sqrt (y2− 1 ) + y∗ sqrt (x 2− 1 ))2 = ( x∗ y + sqrt ((x 2− 1 )∗ (y2− 1 )))2− 1
using assms
unfolding power2-sum
apply (simp add : real-sqrt-mult power-mult-distrib)
apply (simp add : ﬁeld-simps)
done
qed
hence sqrt ((x∗ y + sqrt ((x 2− 1 )∗ (y2− 1 )))2− 1 ) = x∗ sqrt (y2− 1 ) + y∗ sqrt (x 2− 1 )
using power2-eq-iﬀ-nonneg[OF 2 real-sqrt-ge-zero [OF 1 ]]
by simp
thus ?thesis
using assms∗∗
apply (simp add : arcosh-real-def)
apply (subst ln-mult-pos [symmetric])
apply (smt one-le-power real-sqrt-ge-zero )
apply (smt (verit) one-le-power real-sqrt-ge-zero)
by (smt (verit) distrib-right mult.commute real-sqrt-mult)
qed
lemma arcosh-double:
ﬁxes x :: real
assumes x≥ 1
shows 2∗ arcosh x = arcosh (2∗x 2− 1 )
by (smt arcosh-add arcosh-mono assms one-power2 power2-eq-square real-sqrt-abs )
end
