---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-037-some-more-properties-of-h-betweenness
section_title: "Some more properties of h-betweenness."
section_number: null
pages: 94-96
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Some lemmas proved earlier are proved almost directly using the sum of distances characterization.
lemma unit-disc-ﬁx-moebius-preserve-poincare-between′:
assumes unit-disc-ﬁx M and u∈ unit-disc and v∈ unit-disc and w∈ unit-disc
shows poincare-between (moebius-pt M u ) ( moebius-pt M v ) ( moebius-pt M w )←→
poincare-between u v w
using assms
using poincare-between-sum-distances
by simp
lemma conjugate-preserve-poincare-between′:
assumes u∈ unit-disc v ∈ unit-disc w ∈ unit-disc
shows poincare-between (conjugate u ) ( conjugate v ) ( conjugate w )←→ poincare-between u v w
using assms
using poincare-between-sum-distances
by simp
There is a unique point on a ray on the given distance from the given starting point
lemma unique-poincare-distance-on-ray:
assumes d≥ 0 u ⁄= v u ∈ unit-disc v ∈ unit-disc
assumes y∈ unit-disc poincare-distance u y = d poincare-between u v y
assumes z∈ unit-disc poincare-distance u z = d poincare-between u v z
shows y = z
proof−
have∀ d y z . d≥ 0∧
y∈ unit-disc∧ poincare-distance u y = d∧ poincare-between u v y ∧
z∈ unit-disc∧ poincare-distance u z = d∧ poincare-between u v z −→ y = z (is ?P u v )
proof (rule wlog-positive-x-axis [where P=?P])
ﬁx x
assume x: is-real x 0 < Re x Re x < 1
hence x⁄= 0
using complex.expand[of x 0 ]
by auto
hence∗: poincare-line 0 h (of-complex x ) = x-axis
using x poincare-line-0-real-is-x-axis[of of-complex x ]
unfolding circline-set-x-axis
by auto
have of-complex x ∈ unit-disc
using x
by (auto simp add : cmod-eq-Re)
have Arg x = 0
using x
94
using arg-0-iﬀ by blast
show ?P 0 h (of-complex x )
proof safe
ﬁx y z
assume y∈ unit-disc z ∈ unit-disc
then obtain y ′ z ′ where yz: y = of-complex y ′ z = of-complex z ′
using inf-or-of-complex[of y ] inf-or-of-complex[of z ]
by auto
assume betw: poincare-between 0h (of-complex x ) y poincare-between 0 h (of-complex x ) z
hence y⁄= 0 h z⁄= 0 h
using ‹x⁄= 0 › ‹of-complex x ∈ unit-disc› ‹y∈ unit-disc›
using poincare-between-sandwich[of 0 h of-complex x ]
using of-complex-zero-iﬀ [of x ]
by force+
hence Arg y ′ = 0 cmod y ′≥ cmod x Arg z ′ = 0 cmod z ′≥ cmod x
using poincare-between-0uv[of of-complex x y ] poincare-between-0uv[of of-complex x z ]
using ‹of-complex x ∈ unit-disc› ‹x⁄= 0 › ‹Arg x = 0 › ‹y∈ unit-disc› ‹z∈ unit-disc› betw yz
by (simp-all add : Let-def )
hence∗: is-real y ′ is-real z ′ Re y ′> 0 Re z ′> 0
using arg-0-iﬀ [of y ′] arg-0-iﬀ [of z ′] x ‹y⁄= 0 h› ‹z⁄= 0 h› yz
by auto
assume poincare-distance 0 h z = poincare-distance 0 h y 0 ≤ poincare-distance 0 h y
thus y = z
using∗ yz ‹y∈ unit-disc› ‹z∈ unit-disc›
using unique-x-axis-poincare-distance-positive[of poincare-distance 0 h y]
by (auto simp add : cmod-eq-Re unit-disc-to-complex-inj)
qed
next
show u∈ unit-disc v ∈ unit-disc u ⁄= v
by fact+
next
ﬁx M u v
assume∗: unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc u ⁄= v
assume∗∗: ?P (moebius-pt M u ) ( moebius-pt M v )
show ?P u v
proof safe
ﬁx d y z
assume∗∗∗: 0≤ poincare-distance u y
y∈ unit-disc poincare-between u v y
z∈ unit-disc poincare-between u v z
poincare-distance u z = poincare-distance u y
let ?Mu = moebius-pt M u and ?Mv = moebius-pt M v and ?My = moebius-pt M y and ?Mz = moebius-pt M z
have ?Mu∈ unit-disc ?Mv ∈ unit-disc ?My ∈ unit-disc ?Mz ∈ unit-disc
using ‹u∈ unit-disc› ‹v∈ unit-disc› ‹y∈ unit-disc› ‹z∈ unit-disc›
using ‹unit-disc-ﬁx M ›
by auto
hence ?My = ?Mz
using∗∗∗∗
using∗∗[rule-format, of poincare-distance ?Mu ?My ?My ?Mz ]
by simp
thus y = z
using bij-moebius-pt[of M ]
unfolding bij-def inj-on-def
by blast
qed
qed
thus ?thesis
using assms
by auto
qed
end
theory Poincare-Lines-Axis-Intersections
imports Poincare-Between
begin
95
