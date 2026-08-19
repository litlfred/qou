---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-023-existence-and-uniqueness-of-points-with-a-given
section_title: "Existence and uniqueness of points with a given distance"
section_number: null
pages: 54-65
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma ex-x-axis-poincare-distance-negative′:
ﬁxes d :: real
assumes d≥ 0
shows let z = ( 1− exp d ) / (1 + exp d )
in is-real z ∧ Re z ≤ 0∧ Re z >−1∧
of-complex z ∈ unit-disc∧ of-complex z ∈ circline-set x-axis ∧
poincare-distance 0 h (of-complex z ) = d
proof−
54
have exp d ≥ 1
using assms
using one-le-exp-iﬀ [of d, symmetric]
by blast
hence 1 + exp d ⁄= 0
by linarith
let ?z = ( 1− exp d ) / (1 + exp d )
have ?z≤ 0
using ‹exp d ≥ 1 ›
by (simp add : divide-nonpos-nonneg)
moreover
have ?z >−1
using exp-gt-zero[of d ]
by (smt divide-less-eq-1-neg nonzero-minus-divide-right )
moreover
hence abs ?z < 1
using ‹?z≤ 0 ›
by simp
hence cmod ?z < 1
by (metis norm-of-real )
hence of-complex ?z ∈ unit-disc
by simp
moreover
have of-complex ?z ∈ circline-set x-axis
unfolding circline-set-x-axis
by simp
moreover
have (1− ?z) / (1 + ?z) = exp d
proof−
have 1 + ?z = 2 / (1 + exp d )
using ‹1 + exp d ⁄= 0 ›
by (subst add-divide-eq-iﬀ , auto)
moreover
have 1− ?z = 2∗ exp d / (1 + exp d )
using ‹1 + exp d ⁄= 0 ›
by (subst diﬀ-divide-eq-iﬀ , auto)
ultimately
show ?thesis
using ‹1 + exp d ⁄= 0 ›
by simp
qed
ultimately
show ?thesis
using poincare-distance-zero-x-axis[of of-complex ?z ]
using ‹d≥ 0 › ‹exp d ≥ 1 ›
by simp (simp add : cmod-eq-Re)
qed
lemma ex-x-axis-poincare-distance-negative:
assumes d≥ 0
shows∃ z. is-real z ∧ Re z ≤ 0∧ Re z >−1∧
of-complex z ∈ unit-disc∧ of-complex z ∈ circline-set x-axis ∧
poincare-distance 0 h (of-complex z ) = d (is∃ z. ?P z )
using ex-x-axis-poincare-distance-negative′[OF assms ]
unfolding Let-def
by blast
55
For each real number d there is exactly one point on the positive x-axis such that h-distance between 0 and
that point is d.
lemma unique-x-axis-poincare-distance-negative:
assumes d≥ 0
shows∃ ! z. is-real z ∧ Re z ≤ 0∧ Re z >−1∧
poincare-distance 0 h (of-complex z ) = d (is∃ ! z. ?P z )
proof−
let ?z = ( 1− exp d ) / (1 + exp d )
have ?P ?z
using ex-x-axis-poincare-distance-negative′[OF assms ]
unfolding Let-def
by blast
moreover
have∀ z ′. ?P z ′−→ z ′ = ?z
proof−
let ?g = λ x ′.|ln (Re ((1− x ′) / (1 + x ′)))|
let ?A ={x. is-real x ∧ Re x >−1∧ Re x ≤ 0}
have inj-on (poincare-distance 0 h◦ of-complex) ?A
proof (rule comp-inj-on )
show inj-on of-complex ?A
using of-complex-inj
unfolding inj-on-def
by blast
next
show inj-on (poincare-distance 0 h) ( of-complex ‘ ?A) ( is inj-on ?f (of-complex ‘ ?A))
proof (subst inj-on-cong )
have∗: of-complex ‘ ?A =
{z. z∈ unit-disc∧ z∈ circline-set x-axis ∧ Re (to-complex z )≤ 0} (is - = ?B)
by (auto simp add : cmod-eq-Re circline-set-x-axis)
ﬁx x
assume x∈ of-complex ‘ ?A
hence x∈ ?B
using∗
by simp
thus poincare-distance 0 h x = ( ?g◦ to-complex) x
using poincare-distance-zero-x-axis
by (simp add : Let-def )
next
have∗: to-complex ‘ of-complex ‘ ?A = ?A
by (auto simp add : image-iﬀ )
show inj-on (?g◦ to-complex) ( of-complex ‘ ?A)
proof (rule comp-inj-on )
show inj-on to-complex (of-complex ‘ ?A)
unfolding inj-on-def
by auto
next
have inj-on ?g ?A
unfolding inj-on-def
proof (safe)
ﬁx x y
assume hh: is-real x is-real y − 1 < Re x Re x ≤ 0
− 1 < Re y Re y ≤ 0|ln (Re ((1− x) / (1 + x)))| =|ln (Re ((1− y) / (1 + y)))|
have is-real ((1− x)/(1 + x))
using ‹is-real x › div-reals[of 1−x 1 +x]
by auto
have is-real ((1− y)/(1 + y))
using ‹is-real y › div-reals[of 1−y 1 +y]
by auto
have Re (1 + x) > 0
56
using ‹− 1 < Re x › by auto
hence 1 + x⁄= 0
by force
have Re (1− x)≥ 0
using ‹Re x ≤ 0 › by auto
hence Re ((1− x)/(1 + x)) > 0
using Re-divide-real ‹0 < Re (1 + x)› complex-eq-if-Re-eq hh(1 ) hh(4 ) by auto
have Re(1− x)≥ Re ( 1 + x)
using hh by auto
hence Re ((1− x)/(1 + x))≥ 1
using ‹Re (1 + x) > 0 › ‹is-real ((1− x)/(1 + x))›
by (smt Re-divide-real arg-0-iﬀ hh (1 ) le-divide-eq-1-pos one-complex.simps(2 ) plus-complex.simps(2 ))
have Re (1 + y) > 0
using ‹− 1 < Re y › by auto
hence 1 + y⁄= 0
by force
have Re (1− y)≥ 0
using ‹Re y ≤ 0 › by auto
hence Re ((1− y)/(1 + y)) > 0
using Re-divide-real ‹0 < Re (1 + y)› complex-eq-if-Re-eq hh by auto
have Re(1− y)≥ Re ( 1 + y)
using hh by auto
hence Re ((1− y)/(1 + y))≥ 1
using ‹Re (1 + y) > 0 › ‹is-real ((1− y)/(1 + y))›
by (smt Re-divide-real arg-0-iﬀ hh le-divide-eq-1-pos one-complex .simps(2 ) plus-complex.simps(2 ))
have ln (Re ((1− x) / (1 + x))) = ln (Re ((1− y) / (1 + y)))
using ‹Re ((1− y)/(1 + y))≥ 1 › ‹Re ((1− x)/(1 + x))≥ 1 › hh
by auto
hence Re ((1− x) / (1 + x)) = Re ((1− y) / (1 + y))
using ‹Re ((1− y)/(1 + y)) > 0 › ‹Re ((1− x)/(1 + x)) > 0 ›
by auto
hence (1− x) / (1 + x) = ( 1− y) / (1 + y)
using ‹is-real ((1− y)/(1 + y))› ‹is-real ((1− x)/(1 + x))›
using complex-eq-if-Re-eq by blast
hence (1− x)∗ (1 + y) = ( 1− y)∗ (1 + x)
using ‹1 + y⁄= 0 › ‹1 + x⁄= 0 ›
by (simp add :ﬁeld-simps)
thus x = y
by (simp add :ﬁeld-simps)
qed
thus inj-on ?g (to-complex ‘ of-complex ‘ ?A)
using∗
by simp
qed
qed
qed
thus ?thesis
using ‹?P ?z ›
unfolding inj-on-def
by auto
qed
ultimately
show ?thesis
by blast
qed
lemma ex-x-axis-poincare-distance-positive:
assumes d≥ 0
shows∃ z. is-real z ∧ Re z ≥ 0∧ Re z < 1∧
of-complex z ∈ unit-disc∧ of-complex z ∈ circline-set x-axis ∧
poincare-distance 0 h (of-complex z ) = d (is∃ z. is-real z ∧ Re z ≥ 0∧ Re z < 1∧ ?P z )
proof−
obtain z where∗: is-real z Re z ≤ 0 Re z >−1 ?P z
using ex-x-axis-poincare-distance-negative[OF assms ]
57
by auto
hence∗∗: of-complex z ∈ unit-disc of-complex z ∈ circline-set x-axis
by (auto simp add : cmod-eq-Re)
have is-real (−z)∧ Re (−z)≥ 0∧ Re (−z) < 1∧ ?P (−z)
using∗∗∗
by (simp add : circline-set-x-axis)
thus ?thesis
by blast
qed
lemma unique-x-axis-poincare-distance-positive:
assumes d≥ 0
shows∃ ! z. is-real z ∧ Re z ≥ 0∧ Re z < 1∧
poincare-distance 0 h (of-complex z ) = d (is∃ ! z. is-real z ∧ Re z ≥ 0∧ Re z < 1∧ ?P z )
proof−
obtain z where∗: is-real z Re z ≤ 0 Re z >−1 ?P z
using unique-x-axis-poincare-distance-negative[OF assms ]
by auto
hence∗∗: of-complex z ∈ unit-disc of-complex z ∈ circline-set x-axis
by (auto simp add : cmod-eq-Re circline-set-x-axis)
show ?thesis
proof
show is-real (−z)∧ Re (−z)≥ 0∧ Re (−z) < 1∧ ?P (−z)
using∗∗∗
by simp
next
ﬁx z ′
assume is-real z ′∧ Re z ′≥ 0∧ Re z ′< 1∧ ?P z ′
hence is-real (−z ′)∧ Re (−z ′)≤ 0∧ Re (−z ′) >−1∧ ?P (−z ′)
by (auto simp add : circline-set-x-axis cmod-eq-Re)
hence−z ′ = z
using unique-x-axis-poincare-distance-negative[OF assms ]∗
by blast
thus z ′ =−z
by auto
qed
qed
Equal distance implies that segments are isometric - this means that congruence could be deﬁned either by two
segments having the same distance or by requiring existence of an isometry that maps one segment to the other.
lemma poincare-distance-eq-ex-moebius:
assumes in-disc: u∈ unit-disc and v∈ unit-disc and u ′∈ unit-disc and v ′∈ unit-disc
assumes poincare-distance u v = poincare-distance u ′ v ′
shows∃ M. unit-disc-ﬁx M ∧ moebius-pt M u = u ′∧ moebius-pt M v = v ′ (is ?P ′ u v u ′ v ′)
proof (cases u = v)
case True
thus ?thesis
using assms poincare-distance-eq-0-iﬀ [of u ′ v ′]
by (simp add : unit-disc-ﬁx-transitive)
next
case False
have∀ u ′ v ′. u⁄= v∧ u ′∈ unit-disc∧ v ′∈ unit-disc∧ poincare-distance u v = poincare-distance u ′ v ′−→
?P ′ u ′ v ′ u v (is ?P u v )
proof (rule wlog-positive-x-axis [where P=?P])
ﬁx x
assume is-real x 0 < Re x Re x < 1
hence of-complex x ∈ unit-disc of-complex x ∈ circline-set x-axis
unfolding circline-set-x-axis
by (auto simp add : cmod-eq-Re)
show ?P 0 h (of-complex x )
proof safe
ﬁx u ′ v ′
assume 0 h⁄= of-complex x and in-disc: u ′∈ unit-disc v ′∈ unit-disc and
poincare-distance 0 h (of-complex x ) = poincare-distance u ′ v ′
hence u ′⁄= v ′ poincare-distance u ′ v ′> 0
58
using poincare-distance-eq-0-iﬀ[of 0 h of-complex x ] ‹of-complex x ∈ unit-disc›
using poincare-distance-ge0[of 0 h of-complex x ]
by auto
then obtain M where M : unit-disc-ﬁx M moebius-pt M u ′ = 0 h moebius-pt M v ′∈ positive-x-axis
using ex-unit-disc-ﬁx-to-zero-positive-x-axis[of u ′ v ′] in-disc
by auto
then obtain Mv ′ where Mv ′: moebius-pt M v ′ = of-complex Mv ′
using inf-or-of-complex[of moebius-pt M v ′] in-disc unit-disc-ﬁx-iﬀ [of M ]
by (metis image-eqI inf-notin-unit-disc )
have moebius-pt M v ′∈ unit-disc
using M (1 ) ‹v ′∈ unit-disc›
by auto
have Re Mv ′> 0 is-real Mv ′ Re Mv ′< 1
using M Mv ′ of-complex-inj ‹moebius-pt M v ′∈ unit-disc›
unfolding positive-x-axis-def circline-set-x-axis
using cmod-eq-Re
by auto fastforce
have poincare-distance 0 h (moebius-pt M v ′) = poincare-distance u ′ v ′
using M (1 )
using in-disc
by (subst M (2 )[symmetric], simp)
have Mv ′ = x
using ‹poincare-distance 0 h (moebius-pt M v ′) = poincare-distance u ′ v ′› Mv ′
using ‹poincare-distance 0 h (of-complex x ) = poincare-distance u ′ v ′›
using unique-x-axis-poincare-distance-positive[of poincare-distance u ′ v ′]
‹poincare-distance u ′ v ′> 0 ›
using ‹Re Mv ′> 0 › ‹Re Mv ′< 1 › ‹is-real Mv ′›
using ‹is-real x › ‹Re x > 0 › ‹Re x < 1 ›
unfolding positive-x-axis-def
by auto
thus ?P ′ u ′ v ′ 0 h (of-complex x )
using M Mv ′
by auto
qed
next
show u∈ unit-disc v ∈ unit-disc u ⁄= v
by fact+
next
ﬁx M u v
let ?Mu = moebius-pt M u and ?Mv = moebius-pt M v
assume 1 : unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc u ⁄= v
hence 2 : ?Mu⁄= ?Mv ?Mu ∈ unit-disc ?Mv ∈ unit-disc
by auto
assume 3 : ?P (moebius-pt M u ) ( moebius-pt M v )
show ?P u v
proof safe
ﬁx u ′ v ′
assume 4 : u ′∈ unit-disc v ′∈ unit-disc poincare-distance u v = poincare-distance u ′ v ′
hence poincare-distance ?Mu ?Mv = poincare-distance u v
using 1
by simp
then obtain M ′ where 5 : unit-disc-ﬁx M ′ moebius-pt M ′ u ′ = ?Mu moebius-pt M ′ v ′ = ?Mv
using 2 3 4
by auto
let ?M = (−M ) + M ′
have unit-disc-ﬁx ?M ∧ moebius-pt ?M u ′ = u∧ moebius-pt ?M v ′ = v
using 5 ‹unit-disc-ﬁx M ›
using unit-disc-ﬁx-moebius-comp[of −M M ′]
using unit-disc-ﬁx-moebius-inv[of M ]
by simp
59
thus∃ M. unit-disc-ﬁx M ∧ moebius-pt M u ′ = u∧ moebius-pt M v ′ = v
by blast
qed
qed
then obtain M where unit-disc-ﬁx M ∧ moebius-pt M u ′ = u∧ moebius-pt M v ′ = v
using assms ‹u⁄= v›
by blast
hence unit-disc-ﬁx (−M )∧ moebius-pt (−M ) u = u ′∧ moebius-pt (−M ) v = v ′
using unit-disc-ﬁx-moebius-inv[of M ]
by auto
thus ?thesis
by blast
qed
lemma unique-midpoint-x-axis:
assumes x: is-real x −1 < Re x Re x < 1 and
y: is-real y−1 < Re y Re y < 1 and
x⁄= y
shows∃ ! z.−1 < Re z ∧ Re z < 1∧ is-real z∧ poincare-distance (of-complex z ) ( of-complex x ) = poincare-distance
(of-complex z ) ( of-complex y ) ( is∃ ! z. ?R z (of-complex x ) ( of-complex y ))
proof−
let ?x = of-complex x and ?y = of-complex y
let ?P = λ x y.∃ ! z. ?R z x y
have∀ x.−1 < Re x ∧ Re x < 1∧ is-real x ∧ of-complex x ⁄= ?y−→ ?P (of-complex x ) ?y (is ?Q (of-complex y ))
proof (rule wlog-real-zero)
show ?y∈ unit-disc
using y
by (simp add : cmod-eq-Re)
next
show is-real (to-complex ?y )
using y
by simp
next
show ?Q 0 h
proof (rule allI , rule impI, (erule conjE )+)
ﬁx x
assume x:−1 < Re x Re x < 1 is-real x
let ?x = of-complex x
assume ?x⁄= 0 h
hence x⁄= 0
by auto
hence Re x ⁄= 0
using x
using complex-neq-0
by auto
have∗:∀ a.−1 < a∧ a < 1−→
(poincare-distance (of-complex (cor a )) ?x = poincare-distance (of-complex (cor a )) 0 h←→
(Re x )∗ a∗ a− 2∗ a + Re x = 0 )
proof (rule allI , rule impI )
ﬁx a :: real
assume−1 < a∧ a < 1
hence of-complex (cor a )∈ unit-disc
by auto
moreover
have (a− Re x )2 / ((1− a2)∗ (1− (Re x )2)) = a2 / (1− a2)←→
(Re x )∗ a∗ a− 2∗ a + Re x = 0 (is ?lhs←→ ?rhs)
proof−
have 1− a2⁄= 0
using ‹−1 < a∧ a < 1 ›
by (metis cancel-comm-monoid-add-class.diﬀ-cancel diﬀ-eq-diﬀ-less less-numeral-extra (4 ) power2-eq-1-iﬀ
right-minus-eq)
hence ?lhs←→ (a− Re x )2 / (1− (Re x )2) = a2
by (smt divide-cancel-right divide-divide-eq-left mult .commute)
also have ...←→ (a− Re x )2 = a2∗ (1− (Re x )2)
proof−
60
have 1− (Re x )2⁄= 0
using x
by (smt power2-eq-1-iﬀ )
thus ?thesis
by (simp add : divide-eq-eq)
qed
also have ...←→ a2∗ (Re x )2− 2∗a∗Re x + ( Re x )2 = 0
by (simp add : power2-diﬀ ﬁeld-simps )
also have ...←→ Re x ∗ (a2∗ Re x − 2∗ a + Re x ) = 0
by (simp add : power2-eq-square ﬁeld-simps)
also have ...←→ ?rhs
using ‹Re x ⁄= 0 ›
by (simp add : mult.commute mult.left-commute power2-eq-square)
ﬁnally
show ?thesis
.
qed
moreover
have arcosh (1 + 2∗ ((a− Re x )2 / ((1− a2)∗ (1− (Re x )2)))) = arcosh (1 + 2∗ a2 / (1− a2))←→ ?lhs
using ‹−1 < a∧ a < 1 › x mult-left-cancel [of 2 ::real (a− Re x )2 / ((1− a2)∗ (1− (Re x )2)) a2 / (1− a2)]
by (subst arcosh-eq-iﬀ, simp-all add : square-le-1)
ultimately
show poincare-distance (of-complex (cor a )) ( of-complex x ) = poincare-distance (of-complex (cor a )) 0 h←→
(Re x )∗ a∗ a− 2∗ a + Re x = 0
using x
by (auto simp add : poincare-distance-formula cmod-eq-Re)
qed
show ?P ?x 0 h
proof
let ?a = ( 1− sqrt(1− (Re x )2)) / (Re x )
let ?b = ( 1 + sqrt(1− (Re x )2)) / (Re x )
have is-real ?a
by simp
moreover
have 1− (Re x )2 > 0
using x
by (smt power2-eq-1-iﬀ square-le-1 )
have|?a| < 1
proof (cases Re x > 0 )
case True
have (1− Re x )2 < 1− (Re x )2
using ‹Re x > 0 › x
by (simp add : power2-eq-square ﬁeld-simps)
hence 1− Re x < sqrt (1− (Re x )2)
using real-less-rsqrt by fastforce
thus ?thesis
using ‹1− (Re x )2 > 0 › ‹Re x > 0 ›
by simp
next
case False
hence Re x < 0
using ‹Re x ⁄= 0 ›
by simp
have 1 + Re x > 0
using ‹Re x >−1 ›
by simp
hence 2∗Re x + 2∗Re x∗Re x < 0
using ‹Re x < 0 ›
by (metis comm-semiring-class.distrib mult.commute mult-2-right mult-less-0-iﬀ one-add-one zero-less-double-add-iﬀ-zero-less-single-add )
hence (1 + Re x )2 < 1− (Re x )2
by (simp add : power2-eq-square ﬁeld-simps)
hence 1 + Re x < sqrt (1− (Re x )2)
using ‹1− (Re x )2 > 0 ›
61
using real-less-rsqrt by blast
thus ?thesis
using ‹Re x < 0 ›
by (simp add : ﬁeld-simps)
qed
hence−1 < ?a ?a < 1
by linarith+
moreover
have (Re x )∗ ?a∗ ?a− 2∗ ?a + Re x = 0
using ‹Re x ⁄= 0 › ‹1− (Re x )2 > 0 ›
by (simp add : ﬁeld-simps power2-eq-square)
ultimately
show−1 < Re (cor ?a )∧ Re (cor ?a ) < 1 ∧ is-real ?a ∧ poincare-distance (of-complex ?a ) ( of-complex x ) =
poincare-distance (of-complex ?a ) 0 h
using∗
by auto
ﬁx z
assume∗∗:− 1 < Re z ∧ Re z < 1∧ is-real z ∧
poincare-distance (of-complex z ) ( of-complex x ) = poincare-distance (of-complex z ) 0 h
hence Re x ∗ Re z ∗ Re z − 2∗ Re z + Re x = 0
using∗[rule-format, of Re z ] x
by auto
moreover
have sqrt (4− 4∗ Re x ∗ Re x ) = 2∗ sqrt(1− Re x ∗ Re x )
proof−
have sqrt (4− 4∗ Re x ∗ Re x ) = sqrt(4∗ (1− Re x ∗ Re x ))
by simp
thus ?thesis
by (simp only : real-sqrt-mult, simp)
qed
moreover
have (2− 2∗ sqrt (1− Re x ∗ Re x )) / (2∗ Re x ) = ?a
proof−
have (2− 2∗ sqrt (1− Re x ∗ Re x )) / (2∗ Re x ) =
(2∗ (1− sqrt (1− Re x ∗ Re x ))) / (2∗ Re x )
by simp
thus ?thesis
by (subst (asm) mult-divide-mult-cancel-left) ( auto simp add : power2-eq-square)
qed
moreover
have (2 + 2∗ sqrt (1− Re x ∗ Re x )) / (2∗ Re x ) = ?b
proof−
have (2 + 2∗ sqrt (1− Re x ∗ Re x )) / (2∗ Re x ) =
(2∗ (1 + sqrt (1− Re x ∗ Re x ))) / (2∗ Re x )
by simp
thus ?thesis
by (subst (asm) mult-divide-mult-cancel-left) ( auto simp add : power2-eq-square)
qed
ultimately
have Re z = ?a∨ Re z = ?b
using discriminant-nonneg[of Re x −2 Re x Re z ] discrim-def [of Re x −2 Re x ]
using ‹Re x ⁄= 0 › ‹−1 < Re x › ‹Re x < 1 › ‹1− (Re x )2 > 0 ›
by (auto simp add :power2-eq-square)
have|?b| > 1
proof (cases Re x > 0 )
case True
have (Re x − 1 )2 < 1− (Re x )2
using ‹Re x > 0 › x
by (simp add : power2-eq-square ﬁeld-simps)
hence Re x − 1 < sqrt (1− (Re x )2)
using real-less-rsqrt
by simp
thus ?thesis
using ‹1− (Re x )2 > 0 › ‹Re x > 0 ›
by simp
62
next
case False
hence Re x < 0
using ‹Re x ⁄= 0 ›
by simp
have 1 + Re x > 0
using ‹Re x >−1 ›
by simp
hence 2∗Re x + 2∗Re x∗Re x < 0
using ‹Re x < 0 ›
by (metis comm-semiring-class.distrib mult.commute mult-2-right mult-less-0-iﬀ one-add-one zero-less-double-add-iﬀ-zero-less-single-add )
hence 1− (Re x )2 > (− 1− (Re x ))2
by (simp add : ﬁeld-simps power2-eq-square)
hence sqrt (1− (Re x )2) >−1− Re x
using real-less-rsqrt
by simp
thus ?thesis
using ‹Re x < 0 ›
by (simp add : ﬁeld-simps)
qed
hence ?b <−1∨ ?b > 1
by auto
hence Re z = ?a
using ‹Re z = ?a∨ Re z = ?b›∗∗
by auto
thus z = ?a
using∗∗ complex-of-real-Re
by fastforce
qed
qed
next
ﬁx a u
let ?M = moebius-pt (blaschke a )
let ?Mu = ?M u
assume u∈ unit-disc is-real a cmod a < 1
assume∗: ?Q ?Mu
show ?Q u
proof (rule allI , rule impI, (erule conjE )+)
ﬁx x
assume x:−1 < Re x Re x < 1 is-real x of-complex x ⁄= u
let ?Mx = ?M (of-complex x )
have of-complex x ∈ unit-disc
using x cmod-eq-Re
by auto
hence ?Mx∈ unit-disc
using ‹is-real a › ‹cmod a < 1 › blaschke-unit-disc-ﬁx[of a ]
using unit-disc-ﬁx-discI
by blast
hence ?Mx⁄=∞h
by auto
moreover
have of-complex x ∈ circline-set x-axis
using x
by auto
hence ?Mx∈ circline-set x-axis
using blaschke-real-preserve-x-axis[OF ‹is-real a › ‹cmod a < 1 ›, of of-complex x ]
by auto
hence−1 < Re (to-complex ?Mx )∧ Re (to-complex ?Mx ) < 1∧ is-real (to-complex ?Mx )
using ‹?Mx⁄=∞h› ‹?Mx∈ unit-disc›
unfolding circline-set-x-axis
by (auto simp add : cmod-eq-Re)
moreover
have ?Mx⁄= ?Mu
using ‹of-complex x ⁄= u›
by simp
63
ultimately
have ?P ?Mx ?Mu
using∗[rule-format, of to-complex ?Mx ] ‹?Mx⁄=∞h›
by simp
then obtain Mz where
?R Mz ?Mx ?Mu
by blast
have of-complex Mz ∈ unit-disc of-complex Mz ∈ circline-set x-axis
using ‹?R Mz ?Mx ?Mu ›
using cmod-eq-Re
by auto
let ?Minv =− (blaschke a )
let ?z = moebius-pt ?Minv (of-complex Mz )
have ?z∈ unit-disc
using ‹of-complex Mz ∈ unit-disc› ‹cmod a < 1 ›
by auto
moreover
have ?z∈ circline-set x-axis
using ‹of-complex Mz ∈ circline-set x-axis ›
using blaschke-real-preserve-x-axis ‹is-real a › ‹cmod a < 1 ›
by fastforce
ultimately
have z1 :−1 < Re (to-complex ?z ) Re (to-complex ?z ) < 1 is-real (to-complex ?z )
using inf-or-of-complex[of ?z ]
unfolding circline-set-x-axis
by (auto simp add : cmod-eq-Re)
have z2 : poincare-distance ?z (of-complex x ) = poincare-distance ?z u
using ‹?R Mz ?Mx ?Mu › ‹cmod a < 1 › ‹?z∈ unit-disc› ‹of-complex x ∈ unit-disc› ‹u∈ unit-disc›
by (metis blaschke-preserve-distance-formula blaschke-unit-disc-ﬁx moebius-pt-comp-inv-right poincare-distance-formula
uminus-moebius-def unit-disc-ﬁx-discI unit-disc-iﬀ-cmod-lt-1 )
show ?P (of-complex x ) u
proof
show ?R (to-complex ?z ) ( of-complex x ) u
using z1 z2 ‹?z∈ unit-disc› inf-or-of-complex[of ?z ]
by auto
next
ﬁx z ′
assume ?R z ′ (of-complex x ) u
hence of-complex z ′∈ unit-disc of-complex z ′∈ circline-set x-axis
by (auto simp add : cmod-eq-Re)
let ?Mz ′ = ?M (of-complex z ′)
have ?Mz ′∈ unit-disc ?Mz ′∈ circline-set x-axis
using ‹of-complex z ′∈ unit-disc› ‹of-complex z ′∈ circline-set x-axis › ‹cmod a < 1 › ‹is-real a ›
using blaschke-unit-disc-ﬁx unit-disc-ﬁx-discI
using blaschke-real-preserve-x-axis circline-set-x-axis
by blast+
hence−1 < Re (to-complex ?Mz ′) Re (to-complex ?Mz ′) < 1 is-real (to-complex ?Mz ′)
unfolding circline-set-x-axis
by (auto simp add : cmod-eq-Re)
moreover
have poincare-distance ?Mz ′ ?Mx = poincare-distance ?Mz ′ ?Mu
using ‹?R z ′ (of-complex x ) u›
using ‹cmod a < 1 › ‹of-complex x ∈ unit-disc› ‹of-complex z ′∈ unit-disc› ‹u∈ unit-disc›
by auto
ultimately
have ?R (to-complex ?Mz ′) ?Mx ?Mu
using ‹?Mz ′∈ unit-disc› inf-or-of-complex[of ?Mz ′]
by auto
hence ?Mz ′ = of-complex Mz
using ‹?P ?Mx ?Mu › ‹?R Mz ?Mx ?Mu ›
by (metis ‹moebius-pt (blaschke a ) (of-complex z ′)∈ unit-disc› ‹of-complex Mz∈ unit-disc› to-complex-of-complex
unit-disc-to-complex-inj)
thus z ′ = to-complex ?z
by (simp add : moebius-pt-invert)
64
qed
qed
qed
thus ?thesis
using assms
by (metis to-complex-of-complex )
qed
