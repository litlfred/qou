---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-024-triangle-inequality
section_title: "Triangle inequality"
section_number: null
pages: 65-67
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma poincare-distance-formula-zero-sum:
assumes u∈ unit-disc and v∈ unit-disc
shows poincare-distance u 0 h + poincare-distance 0 h v =
(let u ′ = cmod (to-complex u ); v ′ = cmod (to-complex v )
in arcosh (((1 + u ′2)∗ (1 + v ′2) + 4∗ u ′∗ v ′) / ((1− u ′2)∗ (1− v ′2))))
proof−
obtain u ′ v ′ where uv: u ′ = to-complex u v ′ = to-complex v
by auto
have uv ′: u = of-complex u ′ v = of-complex v ′
using uv assms inf-or-of-complex [of u ] inf-or-of-complex[of v ]
by auto
let ?u ′ = cmod u ′ and ?v ′ = cmod v ′
have disc: ?u ′2 < 1 ?v ′2 < 1
using unit-disc-cmod-square-lt-1[OF ‹u∈ unit-disc›]
using unit-disc-cmod-square-lt-1[OF ‹v∈ unit-disc›] uv
by auto
thm arcosh-add
have arcosh (1 + 2∗ ?u ′2 / (1− ?u ′2)) + arcosh (1 + 2∗ ?v ′2 / (1− ?v ′2)) =
arcosh (((1 + ?u ′2)∗ (1 + ?v ′2) + 4 ∗ ?u ′∗ ?v ′) / ((1 − ?u ′2)∗ (1 − ?v ′2))) ( is arcosh ?ll + arcosh ?rr =
arcosh ?r )
proof (subst arcosh-add )
show ?ll ≥ 1 ?rr ≥ 1
using disc
by auto
next
show arcosh ((1 + 2∗ ?u ′2 / (1− ?u ′2))∗ (1 + 2∗ ?v ′2 / (1− ?v ′2)) +
sqrt (((1 + 2∗ ?u ′2 / (1− ?u ′2))2− 1 )∗ ((1 + 2∗ ?v ′2 / (1− ?v ′2))2− 1 ))) =
arcosh ?r (is arcosh ?l = -)
proof−
have 1 + 2∗ ?u ′2 / (1− ?u ′2) = ( 1 + ?u ′2) / (1− ?u ′2)
using disc
by (subst add-divide-eq-iﬀ , simp-all )
moreover
have 1 + 2∗ ?v ′2 / (1− ?v ′2) = ( 1 + ?v ′2) / (1− ?v ′2)
using disc
by (subst add-divide-eq-iﬀ , simp-all )
moreover
have sqrt (((1 + 2∗ ?u ′2 / (1− ?u ′2))2− 1 )∗ ((1 + 2∗ ?v ′2 / (1− ?v ′2))2− 1 )) =
(4 ∗ ?u ′∗ ?v ′) / ((1− ?u ′2)∗ (1− ?v ′2)) ( is sqrt ?s = ?t)
proof−
have ?s = ?t2
using disc
apply (subst add-divide-eq-iﬀ , simp)+
apply (subst power-divide )+
apply simp
apply (subst divide-diﬀ-eq-iﬀ , simp)+
apply (simp add : power2-eq-square ﬁeld-simps)
done
thus ?thesis
using disc
by simp
qed
ultimately
have ?l = ?r
65
using disc
by simp (subst add-divide-distrib, simp)
thus ?thesis
by simp
qed
qed
thus ?thesis
using uv ′ assms
using poincare-distance-formula
by (simp add : Let-def )
qed
lemma poincare-distance-triangle-inequality:
assumes u∈ unit-disc and v∈ unit-disc and w∈ unit-disc
shows poincare-distance u v + poincare-distance v w ≥ poincare-distance u w (is ?P ′ u v w )
proof−
have∀ w. w∈ unit-disc−→ ?P ′ u v w (is ?P v u )
proof (rule wlog-x-axis [where P=?P])
ﬁx x
assume is-real x 0 ≤ Re x Re x < 1
hence of-complex x ∈ unit-disc
by (simp add : cmod-eq-Re)
show ?P 0 h (of-complex x )
proof safe
ﬁx w
assume w∈ unit-disc
then obtain w ′ where w: w = of-complex w ′
using inf-or-of-complex[of w ]
by auto
let ?x = cmod x and ?w = cmod w ′ and ?xw = cmod (x− w ′)
have disc: ?x 2 < 1 ?w 2 < 1
using unit-disc-cmod-square-lt-1[OF ‹of-complex x ∈ unit-disc›]
using unit-disc-cmod-square-lt-1[OF ‹w∈ unit-disc›] w
by auto
have poincare-distance (of-complex x ) 0 h + poincare-distance 0 h w =
arcosh (((1 + ?x 2)∗ (1 + ?w2) + 4∗ ?x∗ ?w) / ((1− ?x 2)∗ (1− ?w2))) ( is - = arcosh ?r1 )
using poincare-distance-formula-zero-sum[OF ‹of-complex x ∈ unit-disc› ‹w∈ unit-disc›] w
by (simp add : Let-def )
moreover
have poincare-distance (of-complex x ) ( of-complex w ′) =
arcosh (((1− ?x 2)∗ (1− ?w2) + 2∗ ?xw2) / ((1− ?x 2)∗ (1− ?w2))) ( is - = arcosh ?r2 )
using disc
using poincare-distance-formula[OF ‹of-complex x ∈ unit-disc› ‹w∈ unit-disc›] w
by (subst add-divide-distrib ) simp
moreover
have∗: ( 1− ?x 2)∗ (1− ?w2) + 2∗ ?xw2≤ (1 + ?x 2)∗ (1 + ?w2) + 4∗ ?x∗ ?w
proof−
have (cmod (x− w ′))2≤ (cmod x + cmod w ′)2
using norm-triangle-ineq4[of x w ′]
by (simp add : power-mono)
thus ?thesis
by (simp add : ﬁeld-simps power2-sum )
qed
have arcosh ?r1 ≥ arcosh ?r2
proof (subst arcosh-mono)
show ?r1≥ 1
using disc
by (smt∗ le-divide-eq-1-pos mult-pos-pos zero-le-power2 )
next
show ?r2≥ 1
using disc
by simp
66
next
show ?r1≥ ?r2
using disc
using∗
by (subst divide-right-mono, simp-all )
qed
ultimately
show poincare-distance (of-complex x ) w≤ poincare-distance (of-complex x ) 0 h + poincare-distance 0 h w
using ‹of-complex x ∈ unit-disc› ‹w∈ unit-disc› w
using poincare-distance-formula
by simp
qed
next
show v∈ unit-disc u ∈ unit-disc
by fact+
next
ﬁx M u v
assume∗: unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc
assume∗∗: ?P (moebius-pt M u ) ( moebius-pt M v )
show ?P u v
proof safe
ﬁx w
assume w∈ unit-disc
thus ?P ′ v u w
by (metis∗∗∗ unit-disc-ﬁx-discI unit-disc-ﬁx-preserve-poincare-distance)
qed
qed
thus ?thesis
using assms
by auto
qed
end
theory Poincare-Circles
imports Poincare-Distance
begin
