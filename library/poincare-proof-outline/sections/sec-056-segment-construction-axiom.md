---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-056-segment-construction-axiom
section_title: "Segment construction axiom"
section_number: null
pages: 138-140
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma segment-construction:
assumes x∈ unit-disc and y∈ unit-disc
assumes a∈ unit-disc and b∈ unit-disc
shows∃ z. z∈ unit-disc∧ poincare-between x y z ∧ poincare-distance y z = poincare-distance a b
proof−
obtain d where d: d = poincare-distance a b
by auto
have d≥ 0
using assms
138
by (simp add : d poincare-distance-ge0 )
have∃ z. z∈ unit-disc∧ poincare-between x y z ∧ poincare-distance y z = d (is ?P x y )
proof (cases x = y)
case True
have∃ z. z∈ unit-disc∧ poincare-distance x z = d
proof (rule wlog-zero )
show∃ z. z∈ unit-disc∧ poincare-distance 0 h z = d
using ex-x-axis-poincare-distance-negative[of d ] ‹d≥ 0 ›
by blast
next
show x∈ unit-disc
by fact
next
ﬁx a u
assume u∈ unit-disc cmod a < 1
assume∃ z. z∈ unit-disc∧ poincare-distance (moebius-pt (blaschke a ) u) z = d
then obtain z where∗: z∈ unit-disc poincare-distance (moebius-pt (blaschke a ) u) z = d
by auto
obtain z ′ where z ′: z = moebius-pt (blaschke a ) z ′ z ′∈ unit-disc
using ‹z∈ unit-disc›
using unit-disc-ﬁx-iﬀ [of blaschke a ] ‹cmod a < 1 ›
using blaschke-unit-disc-ﬁx[of a ]
by blast
show∃ z. z∈ unit-disc∧ poincare-distance u z = d
using∗ z ′ ‹u : unit-disc›
using blaschke-unit-disc-ﬁx[of a ] ‹cmod a < 1 ›
by (rule-tac x =z ′ in exI, simp)
qed
thus ?thesis
using ‹x = y›
unfolding poincare-between-def
by auto
next
case False
show ?thesis
proof (rule wlog-positive-x-axis [where P=λ y x. ?P x y ])
ﬁx x
assume is-real x 0 < Re x Re x < 1
then obtain z where z: is-real z Re z ≤ 0− 1 < Re z of-complex z ∈ unit-disc
of-complex z ∈ unit-disc of-complex z ∈ circline-set x-axis poincare-distance 0 h (of-complex z ) = d
using ex-x-axis-poincare-distance-negative[of d ] ‹d≥ 0 ›
by auto
have poincare-between (of-complex x ) 0 h (of-complex z )
proof (cases z = 0 )
case True
thus ?thesis
unfolding poincare-between-def
by auto
next
case False
have x⁄= 0
using ‹is-real x › ‹Re x > 0 ›
by auto
thus ?thesis
using poincare-between-x-axis-u0v[of x z ]
using z ‹is-real x › ‹x⁄= 0 › ‹Re x > 0 › False
using complex-eq-if-Re-eq mult-pos-neg
by fastforce
qed
thus ?P (of-complex x ) 0 h
using ‹poincare-distance 0 h (of-complex z ) = d› ‹of-complex z ∈ unit-disc›
by blast
139
next
show x∈ unit-disc y ∈ unit-disc
by fact+
next
show y⁄= x using ‹x⁄= y› by simp
next
ﬁx M u v
assume unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc u ⁄= v
assume ?P (moebius-pt M v ) ( moebius-pt M u )
then obtain z where∗: z ∈ unit-disc poincare-between (moebius-pt M v ) ( moebius-pt M u ) z poincare-distance
(moebius-pt M u ) z = d
by auto
obtain z ′ where z ′: z = moebius-pt M z ′ z ′∈ unit-disc
using ‹z∈ unit-disc›
using unit-disc-ﬁx-iﬀ [of M ] ‹unit-disc-ﬁx M ›
by blast
thus ?P v u
using∗ ‹u∈ unit-disc› ‹v∈ unit-disc› ‹unit-disc-ﬁx M ›
by auto
qed
qed
thus ?thesis
using assms d
by auto
qed
