---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-036-poincare-between---sum-distances
section_title: "Poincare between - sum distances"
section_number: null
pages: 89-94
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Another possible deﬁnition of the h-betweenness relation is given in terms of h-distances between pairs of points.
We prove it as a characterization equivalent to our cross-ratio based deﬁnition.
lemma poincare-between-sum-distances-x-axis-u0v:
assumes of-complex u ′∈ unit-disc of-complex v ′∈ unit-disc
assumes is-real u ′ u ′⁄= 0 v ′⁄= 0
shows poincare-distance (of-complex u ′) 0 h + poincare-distance 0 h (of-complex v ′) = poincare-distance (of-complex
u ′) ( of-complex v ′)←→
is-real v ′∧ Re u ′∗ Re v ′< 0 (is ?P u ′ v ′←→ ?Q u ′ v ′)
proof−
have Re u ′⁄= 0
89
using ‹is-real u ′› ‹u ′⁄= 0 ›
using complex-eq-if-Re-eq
by simp
let ?u = cmod u ′ and ?v = cmod v ′ and ?uv = cmod (u ′− v ′)
have disc: ?u2 < 1 ?v 2 < 1
using unit-disc-cmod-square-lt-1[OF assms (1 )]
using unit-disc-cmod-square-lt-1[OF assms (2 )]
by auto
have poincare-distance (of-complex u ′) 0 h + poincare-distance 0 h (of-complex v ′) =
arcosh (((1 + ?u2)∗ (1 + ?v2) + 4∗ ?u∗ ?v) / ((1− ?u2)∗ (1− ?v2))) ( is - = arcosh ?r1 )
using poincare-distance-formula-zero-sum[OF assms (1−2 )]
by (simp add : Let-def )
moreover
have poincare-distance (of-complex u ′) ( of-complex v ′) =
arcosh (((1− ?u2)∗ (1− ?v2) + 2∗ ?uv2) / ((1− ?u2)∗ (1− ?v2))) ( is - = arcosh ?r2 )
using disc
using poincare-distance-formula[OF assms (1−2 )]
by (subst add-divide-distrib ) simp
moreover
have arcosh ?r1 = arcosh ?r2 ←→ ?Q u ′ v ′
proof
assume arcosh ?r1 = arcosh ?r2
hence ?r1 = ?r2
proof (subst (asm) arcosh-eq-iﬀ)
show ?r1≥ 1
proof−
have (1− ?u2)∗ (1− ?v2)≤ (1 + ?u2)∗ (1 + ?v2) + 4∗ ?u∗ ?v
by (simp add : ﬁeld-simps)
thus ?thesis
using disc
by simp
qed
next
show ?r2≥ 1
using disc
by simp
qed
hence (1 + ?u2)∗ (1 + ?v2) + 4∗ ?u∗ ?v = ( 1− ?u2)∗ (1− ?v2) + 2∗ ?uv2
using disc
by auto
hence (cmod (u ′− v ′))2 = ( cmod u ′ + cmod v ′)2
by (simp add : ﬁeld-simps power2-eq-square)
hence∗: Re u ′∗ Re v ′ +|Re u ′|∗ sqrt ((Im v ′)2 + ( Re v ′)2) = 0
using ‹is-real u ′›
unfolding cmod-power2 cmod-def
by (simp add : ﬁeld-simps) ( simp add : power2-eq-square ﬁeld-simps)
hence sqrt ((Im v ′)2 + ( Re v ′)2) = |Re v ′|
using ‹Re u ′⁄= 0 › ‹v ′⁄= 0 ›
by (smt complex-neq-0 mult.commute mult-cancel-right mult-minus-left real-sqrt-gt-0-iﬀ )
hence Im v ′ = 0
by (smt Im-eq-0 norm-complex-def )
moreover
hence Re u ′∗ Re v ′ =−| Re u ′|∗| Re v ′|
using∗
by simp
hence Re u ′∗ Re v ′< 0
using ‹Re u ′⁄= 0 › ‹v ′⁄= 0 ›
by (simp add : ‹is-real v ′› complex-eq-if-Re-eq)
ultimately
show ?Q u ′ v ′
by simp
next
assume ?Q u ′ v ′
hence is-real v ′ Re u ′∗ Re v ′< 0
by auto
90
have ?r1 = ?r2
proof (cases Re u ′> 0 )
case True
hence Re v ′< 0
using ‹Re u ′∗ Re v ′< 0 ›
by (smt zero-le-mult-iﬀ )
show ?thesis
using disc ‹is-real u ′› ‹is-real v ′›
using ‹Re u ′> 0 › ‹Re v ′< 0 ›
unfolding cmod-power2 cmod-def
by simp (simp add : power2-eq-square ﬁeld-simps)
next
case False
hence Re u ′< 0
using ‹Re u ′⁄= 0 ›
by simp
hence Re v ′> 0
using ‹Re u ′∗ Re v ′< 0 ›
by (smt zero-le-mult-iﬀ )
show ?thesis
using disc ‹is-real u ′› ‹is-real v ′›
using ‹Re u ′< 0 › ‹Re v ′> 0 ›
unfolding cmod-power2 cmod-def
by simp (simp add : power2-eq-square ﬁeld-simps)
qed
thus arcosh ?r1 = arcosh ?r2
by metis
qed
ultimately
show ?thesis
by simp
qed
Diﬀerent proof of the previous theorem relying on the cross-ratio deﬁnition, and not the distance formula. We
suppose that this could be also used to prove the triangle inequality.
lemma poincare-between-sum-distances-x-axis-u0v-diﬀerent-proof:
assumes of-complex u ′∈ unit-disc of-complex v ′∈ unit-disc
assumes is-real u ′ u ′⁄= 0 v ′⁄= 0 is-real v ′
shows poincare-distance (of-complex u ′) 0 h + poincare-distance 0 h (of-complex v ′) = poincare-distance (of-complex
u ′) ( of-complex v ′)←→
Re u ′∗ Re v ′< 0 (is ?P u ′ v ′←→ ?Q u ′ v ′)
proof−
have−1 < Re u ′ Re u ′< 1 Re u ′⁄= 0
using assms
by (auto simp add : cmod-eq-Re complex-eq-if-Re-eq)
have−1 < Re v ′ Re v ′< 1 Re v ′⁄= 0
using assms
by (auto simp add : cmod-eq-Re complex-eq-if-Re-eq)
have|ln (Re ((1− u ′) / (1 + u ′)))| +|ln (Re ((1− v ′) / (1 + v ′)))| =
|ln (Re ((1 + u ′)∗ (1− v ′) / ((1− u ′)∗ (1 + v ′))))|←→ Re u ′∗ Re v ′< 0 (is|ln ?a1| +|ln ?a2| =|ln ?a3|
←→ -)
proof−
have 1 : 0 < ?a1 ln ?a1 > 0←→ Re u ′< 0
using ‹Re u ′< 1 › ‹Re u ′>−1 › ‹is-real u ′›
using complex-is-Real-iﬀ
by auto
have 2 : 0 < ?a2 ln ?a2 > 0←→ Re v ′< 0
using ‹Re v ′< 1 › ‹Re v ′>−1 › ‹is-real v ′›
using complex-is-Real-iﬀ
by auto
have 3 : 0 < ?a3 ln ?a3 > 0←→ Re v ′< Re u ′
using ‹Re u ′< 1 › ‹Re u ′>−1 › ‹is-real u ′›
using ‹Re v ′< 1 › ‹Re v ′>−1 › ‹is-real v ′›
using complex-is-Real-iﬀ
by auto (simp add : ﬁeld-simps)+
91
show ?thesis
proof
assume∗: Re u ′∗ Re v ′< 0
show|ln ?a1| +|ln ?a2| =|ln ?a3|
proof (cases Re u ′> 0 )
case True
hence Re v ′< 0
using∗
by (smt mult-nonneg-nonneg )
show ?thesis
using 1 2 3 ‹Re u ′> 0 › ‹Re v ′< 0 ›
using ‹Re u ′< 1 › ‹Re u ′>−1 › ‹is-real u ′›
using ‹Re v ′< 1 › ‹Re v ′>−1 › ‹is-real v ′›
using complex-is-Real-iﬀ
using ln-div ln-mult
by simp
next
case False
hence Re v ′> 0 Re u ′< 0
using∗
by (smt zero-le-mult-iﬀ )+
show ?thesis
using 1 2 3 ‹Re u ′< 0 › ‹Re v ′> 0 ›
using ‹Re u ′< 1 › ‹Re u ′>−1 › ‹is-real u ′›
using ‹Re v ′< 1 › ‹Re v ′>−1 › ‹is-real v ′›
using complex-is-Real-iﬀ
using ln-div ln-mult
by simp
qed
next
assume∗:|ln ?a1| +|ln ?a2| =|ln ?a3|
{
assume Re u ′> 0 Re v ′> 0
hence False
using∗ 1 2 3
using ‹Re u ′< 1 › ‹Re u ′>−1 › ‹is-real u ′›
using ‹Re v ′< 1 › ‹Re v ′>−1 › ‹is-real v ′›
using complex-is-Real-iﬀ
using ln-mult ln-div
by (cases Re v ′< Re u ′) auto
}
moreover
{
assume Re u ′< 0 Re v ′< 0
hence False
using∗ 1 2 3
using ‹Re u ′< 1 › ‹Re u ′>−1 › ‹is-real u ′›
using ‹Re v ′< 1 › ‹Re v ′>−1 › ‹is-real v ′›
using complex-is-Real-iﬀ
using ln-mult ln-div
by (cases Re v ′< Re u ′) auto
}
ultimately
show Re u ′∗ Re v ′< 0
using ‹Re u ′⁄= 0 › ‹Re v ′⁄= 0 ›
by (smt divisors-zero mult-le-0-iﬀ )
qed
qed
thus ?thesis
using assms
apply (subst poincare-distance-sym, simp, simp)
apply (subst poincare-distance-zero-x-axis, simp, simp add : circline-set-x-axis)
apply (subst poincare-distance-zero-x-axis, simp, simp add : circline-set-x-axis)
apply (subst poincare-distance-x-axis-x-axis, simp, simp, simp add : circline-set-x-axis, simp add : circline-set-x-axis)
apply simp
done
92
qed
lemma poincare-between-sum-distances:
assumes u∈ unit-disc and v∈ unit-disc and w∈ unit-disc
shows poincare-between u v w ←→
poincare-distance u v + poincare-distance v w = poincare-distance u w (is ?P ′ u v w )
proof (cases u = v)
case True
thus ?thesis
using assms
by simp
next
case False
have∀ w. w∈ unit-disc−→(poincare-between u v w←→poincare-distance u v + poincare-distance v w = poincare-distance
u w ) ( is ?P u v )
proof (rule wlog-positive-x-axis )
ﬁx x
assume is-real x 0 < Re x Re x < 1
have of-complex x ∈ circline-set x-axis
using ‹is-real x ›
by (auto simp add : circline-set-x-axis)
have of-complex x ∈ unit-disc
using ‹is-real x › ‹0 < Re x › ‹Re x < 1 ›
by (simp add : cmod-eq-Re)
have x⁄= 0
using ‹is-real x › ‹Re x > 0 ›
by auto
show ?P (of-complex x ) 0 h
proof (rule allI , rule impI )
ﬁx w
assume w∈ unit-disc
then obtain w ′ where w = of-complex w ′
using inf-or-of-complex[of w ]
by auto
show ?P ′ (of-complex x ) 0 h w
proof (cases w = 0 h)
case True
thus ?thesis
by simp
next
case False
hence w ′⁄= 0
using ‹w = of-complex w ′›
by auto
show ?thesis
using ‹is-real x › ‹x⁄= 0 › ‹w = of-complex w ′› ‹w ′⁄= 0 ›
using ‹of-complex x ∈ unit-disc› ‹w∈ unit-disc›
apply simp
apply (subst poincare-between-x-axis-u0v, simp-all )
apply (subst poincare-between-sum-distances-x-axis-u0v, simp-all )
done
qed
qed
next
show v∈ unit-disc u ∈ unit-disc
using assms
by auto
next
show v⁄= u
using ‹u⁄= v›
by simp
93
next
ﬁx M u v
assume∗: unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc u ⁄= v and
∗∗: ?P (moebius-pt M v ) ( moebius-pt M u )
show ?P v u
proof (rule allI , rule impI )
ﬁx w
assume w∈ unit-disc
hence moebius-pt M w ∈ unit-disc
using ‹unit-disc-ﬁx M ›
by auto
thus ?P ′ v u w
using ‹u∈ unit-disc› ‹v∈ unit-disc› ‹w∈ unit-disc› ‹unit-disc-ﬁx M ›
using∗∗[rule-format, of moebius-pt M w ]
by auto
qed
qed
thus ?thesis
using assms
by simp
qed
