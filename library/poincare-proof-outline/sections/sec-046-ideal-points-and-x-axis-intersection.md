---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-046-ideal-points-and-x-axis-intersection
section_title: "Ideal points and x-axis intersection"
section_number: null
pages: 112-114
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma ideal-points-intersects-x-axis:
assumes is-poincare-line H and ideal-points H ={i1, i2} and H⁄= x-axis
shows intersects-x-axis H ←→ Im (to-complex i1 )∗ Im (to-complex i2 ) < 0
using assms
proof−
have i1⁄= i2
using assms(1 ) assms(2 ) ex-poincare-line-points ideal-points-diﬀerent(1 )
by blast
112
have calc-ideal-points H ={i1, i2}
using assms
using ideal-points-unique
by auto
have∀ i1∈ calc-ideal-points H.
∀ i2∈ calc-ideal-points H.
is-poincare-line H ∧ H ⁄= x-axis ∧ i1 ⁄= i2 −→ (Im (to-complex i1 )∗ Im (to-complex i2 ) < 0 ←→
intersects-x-axis H )
proof (transfer, transfer, (rule ballI )+, rule impI, (erule conjE )+, case-tac H, case-tac i1, case-tac i2 )
ﬁx i11 i12 i21 i22 A B C D H i1 i2
assume H : H = ( A, B, C, D) hermitean H H ⁄= mat-zero
assume line: is-poincare-line-cmat H
assume i1 : i1 = ( i11, i12 ) i1∈ calc-ideal-points-cmat-cvec H
assume i2 : i2 = ( i21, i22 ) i2∈ calc-ideal-points-cmat-cvec H
assume diﬀerent:¬ i1≈v i2
assume not-x-axis: ¬ circline-eq-cmat H x-axis-cmat
have is-real A is-real D C = cnj B
using H hermitean-elems
by auto
have (cmod A )2 < (cmod B )2 A = D
using line H
by auto
let ?discr = sqrt ((cmod B )2− (Re D )2)
let ?den = ( cmod B )2
let ?i1 = B∗ (− D− i∗ ?discr)
let ?i2 = B∗ (− D + i ∗ ?discr)
have i11 = ?i1∨ i11 = ?i2 i12 = ?den
i21 = ?i1∨ i21 = ?i2 i22 = ?den
using i1 i2 H line
by (auto split : if-split-asm)
hence i: i11 = ?i1∧ i21 = ?i2∨ i11 = ?i2∧ i21 = ?i1
using ‹¬ i1≈v i2 › i1 i2
by auto
have Im (i11 / i12 )∗ Im (i21 / i22 ) = Im (?i1 / ?den)∗ Im (?i2 / ?den)
using i ‹i12 = ?den› ‹i22 = ?den›
by auto
also have ... = Im (?i1 )∗ Im (?i2 ) / ?den2
by simp
also have ... = ( Im B ∗ (Im B ∗ (Re D ∗ Re D ))− Re B ∗ (Re B ∗ ((cmod B )2− (Re D )2))) / cmod B ^ 4
using ‹(cmod B )2 > (cmod A )2› ‹A = D›
using ‹is-real D › cmod-eq-Re[of A ]
by (auto simp add : ﬁeld-simps)
also have ... = (( Im B )2∗ (Re D )2− (Re B )2∗ ((Re B )2 + ( Im B )2− (Re D )2)) / cmod B ^ 4
proof−
have cmod B ∗ cmod B = Re B ∗ Re B + Im B ∗ Im B
by (metis cmod-power2 power2-eq-square )
thus ?thesis
by (simp add : power2-eq-square)
qed
also have ... = ((( Re D )2− (Re B )2)∗ ((Re B )2 + ( Im B )2)) / cmod B ^ 4
by (simp add : power2-eq-square ﬁeld-simps)
ﬁnally have Im-product: Im (i11 / i12 )∗ Im (i21 / i22 ) = (( Re D )2− (Re B )2)∗ ((Re B )2 + ( Im B )2) / cmod
B ^ 4
.
show Im (to-complex-cvec i1 )∗ Im (to-complex-cvec i2 ) < 0←→ intersects-x-axis-cmat H
proof safe
assume opposite: Im (to-complex-cvec i1 )∗ Im (to-complex-cvec i2 ) < 0
show intersects-x-axis-cmat H
proof−
113
have ((Re D )2− (Re B )2)∗ ((Re B )2 + ( Im B )2) / cmod B ^ 4 < 0
using Im-product opposite i1 i2
by simp
hence ((Re D )2− (Re B )2)∗ ((Re B )2 + ( Im B )2) < 0
by (simp add : divide-less-0-iﬀ )
hence (Re D )2 < (Re B )2
by (simp add : mult-less-0-iﬀ not-sum-power2-lt-zero )
thus ?thesis
using H ‹A = D› ‹ is-real D ›
by auto
qed
next
have∗: (∀ k. k∗ Im B = 1−→ k = 0 )−→ Im B = 0
apply (safe, erule-tac x =1 / Im B in allE )
using divide-cancel-left by fastforce
assume intersects-x-axis-cmat H
hence Re D = 0∨ (Re D )2 < (Re B )2
using H ‹A = D›
by auto
hence (Re D )2 < (Re B )2
using ‹is-real D › line H ‹C = cnj B ›
using not-x-axis∗
by (auto simp add : complex-eq-iﬀ )
hence ((Re D )2− (Re B )2)∗ ((Re B )2 + ( Im B )2) < 0
by (metis add-cancel-left-left diﬀ-less-eq mult-eq-0-iﬀ mult-less-0-iﬀ power2-eq-square power2-less-0 sum-squares-gt-zero-iﬀ )
thus Im (to-complex-cvec i1 )∗ Im (to-complex-cvec i2 ) < 0
using Im-product i1 i2
using divide-eq-0-iﬀ divide-less-0-iﬀ prod .simps(2 ) to-complex-cvec-def zero-complex.simps(1 ) zero-less-norm-iﬀ
by fastforce
qed
qed
thus ?thesis
using assms ‹calc-ideal-points H ={i1, i2}› ‹i1⁄= i2 ›
by auto
qed
end
theory Poincare-Perpendicular
imports Poincare-Lines-Axis-Intersections
begin
