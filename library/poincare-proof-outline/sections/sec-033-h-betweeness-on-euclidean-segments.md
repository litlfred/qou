---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-033-h-betweeness-on-euclidean-segments
section_title: "H-betweeness on Euclidean segments"
section_number: null
pages: 79-86
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
If the three points lie on an h-line that is a Euclidean line (e.g., if it contains zero), h-betweenness can be
characterized much simpler than in the deﬁnition.
lemma poincare-between-x-axis-u0v:
assumes is-real u ′ and u ′⁄= 0 and v ′⁄= 0
shows poincare-between (of-complex u ′) 0 h (of-complex v ′)←→ is-real v ′∧ Re u ′∗ Re v ′< 0
proof−
have Re u ′⁄= 0
using ‹is-real u ′› ‹u ′⁄= 0 ›
using complex-eq-if-Re-eq
by auto
have nz: of-complex u ′⁄= 0 h of-complex v ′⁄= 0 h
by (simp-all add : ‹u ′⁄= 0 › ‹v ′⁄= 0 ›)
hence 0 h⁄= of-complex v ′
by metis
let ?cr = cross-ratio (of-complex u ′) 0 h (of-complex v ′)∞h
have is-real (to-complex ?cr )∧ Re (to-complex ?cr ) < 0←→ is-real v ′∧ Re u ′∗ Re v ′< 0
using cross-ratio-0inf[of v ′ u ′] ‹v ′⁄= 0 › ‹u ′⁄= 0 › ‹is-real u ′›
by (metis Re-complex-div-lt-0 Re-mult-real complex-cnj-divide divide-cancel-left eq-cnj-iﬀ-real to-complex-of-complex )
thus ?thesis
unfolding poincare-between-def inversion-zero
using ‹of-complex u ′⁄= 0 h› ‹0 h⁄= of-complex v ′›
by simp
qed
lemma poincare-between-u0v:
assumes u∈ unit-disc and v∈ unit-disc and u⁄= 0 h and v⁄= 0 h
shows poincare-between u 0 h v←→ (∃ k < 0. to-complex u = cor k ∗ to-complex v ) ( is ?P u v )
proof (cases u = v)
case True
thus ?thesis
using assms
79
using inf-or-of-complex[of v ]
using poincare-between-sandwich[of u 0 h]
by auto
next
case False
have∀ u. u∈ unit-disc∧ u⁄= 0 h−→ ?P u v (is ?P ′ v)
proof (rule wlog-rotation-to-positive-x-axis )
ﬁx ϕ v
let ?M = moebius-pt (moebius-rotationϕ)
assume 1 : v∈ unit-disc v ⁄= 0 h
assume 2 : ?P ′ (?M v )
show ?P ′ v
proof (rule allI , rule impI, (erule conjE )+)
ﬁx u
assume 3 : u∈ unit-disc u ⁄= 0 h
have poincare-between (?M u ) 0 h (?M v )←→ poincare-between u 0 h v
using ‹u∈ unit-disc› ‹v∈ unit-disc›
using unit-disc-ﬁx-moebius-preserve-poincare-between unit-disc-ﬁx-rotation zero-in-unit-disc
by fastforce
thus ?P u v
using 1 2 [rule-format, of ?M u ] 3
using inf-or-of-complex[of u ] inf-or-of-complex[of v ]
by auto
qed
next
ﬁx x
assume 1 : is-real x 0 < Re x Re x < 1
hence x⁄= 0
by auto
show ?P ′ (of-complex x )
proof (rule allI , rule impI, (erule conjE )+)
ﬁx u
assume 2 : u∈ unit-disc u ⁄= 0 h
then obtain u ′ where u = of-complex u ′
using inf-or-of-complex[of u ]
by auto
show ?P u (of-complex x )
using 1 2 ‹x⁄= 0 › ‹u = of-complex u ′›
using poincare-between-rev[of u 0 h of-complex x ]
using poincare-between-x-axis-u0v[of x u ′] ‹is-real x ›
apply (auto simp add : cmod-eq-Re)
apply (rule-tac x =Re u ′/ Re x in exI, simp add : divide-neg-pos algebra-split-simps)
using mult-neg-pos mult-pos-neg
by blast
qed
qed fact+
thus ?thesis
using assms
by auto
qed
lemma poincare-between-u0v-polar-form:
assumes x∈ unit-disc and y∈ unit-disc and x⁄= 0 h and y⁄= 0 h and
to-complex x = cor rx ∗ cis ϕ to-complex y = cor ry ∗ cis ϕ
shows poincare-between x 0 h y←→ rx∗ ry < 0 (is ?P x y rx ry )
proof−
from assms have rx⁄= 0 ry ⁄= 0
using inf-or-of-complex[of x ] inf-or-of-complex[of y ]
by auto
have (∃ k<0. cor rx = cor k ∗ cor ry ) = ( rx∗ ry < 0 )
proof
assume∃ k<0. cor rx = cor k ∗ cor ry
then obtain k where k < 0 cor rx = cor k ∗ cor ry
by auto
hence rx = k∗ ry
80
using of-real-eq-iﬀ
by fastforce
thus rx∗ ry < 0
using ‹k < 0 › ‹rx⁄= 0 › ‹ry⁄= 0 ›
by (smt divisors-zero mult-nonneg-nonpos mult-nonpos-nonpos zero-less-mult-pos2 )
next
assume rx∗ ry < 0
hence rx = ( rx/ry)∗ry rx / ry < 0
using ‹rx⁄= 0 › ‹ry⁄= 0 ›
by (auto simp add : divide-less-0-iﬀ algebra-split-simps )
thus∃ k<0. cor rx = cor k ∗ cor ry
using ‹rx⁄= 0 › ‹ry⁄= 0 ›
by (rule-tac x =rx / ry in exI, simp)
qed
thus ?thesis
using assms
using poincare-between-u0v[OF assms (1−4 )]
by auto
qed
lemma poincare-between-x-axis-0uv:
ﬁxes x y :: real
assumes−1 < x and x < 1 and x⁄= 0
assumes−1 < y and y < 1 and y⁄= 0
shows poincare-between 0h (of-complex x ) ( of-complex y )←→
(x < 0∧ y < 0∧ y≤ x)∨ (x > 0∧ y > 0∧ x≤ y) ( is ?lhs←→ ?rhs)
proof (cases x = y)
case True
thus ?thesis
using assms
unfolding poincare-between-def
by auto
next
case False
let ?x = of-complex x and ?y = of-complex y
have ?x∈ unit-disc ?y ∈ unit-disc
using assms
by auto
have distinct: distinct [0 h, ?x, ?y, inversion ?x ]
using ‹x⁄= 0 › ‹y⁄= 0 › ‹x⁄= y› ‹?x∈ unit-disc› ‹?y∈ unit-disc›
using inversion-noteq-unit-disc[of ?x ?y ]
using inversion-noteq-unit-disc[of ?x ?x ]
using inversion-noteq-unit-disc[of ?x 0 h]
using of-complex-inj[of x y ]
by (metis distinct-length-2-or-more distinct-singleton of-complex-zero-iﬀ of-real-eq-0-iﬀ of-real-eq-iﬀ zero-in-unit-disc )
let ?cr = cross-ratio 0 h ?x ?y (inversion ?x )
have Re (to-complex ?cr ) = x 2∗ (x∗y− 1 ) / (x∗ (y− x))
using ‹x⁄= 0 › ‹x⁄= y›
unfolding inversion-def
by simp (transfer, transfer, auto simp add : vec-cnj-def power2-eq-square ﬁeld-simps split : if-split-asm)
moreover
{
ﬁx a b :: real
assume b⁄= 0
hence a < 0←→ b2∗ a < (0 ::real)
by (metis mult.commute mult-eq-0-iﬀ mult-neg-pos mult-pos-pos not-less-iﬀ-gr-or-eq not-real-square-gt-zero power2-eq-square)
}
hence x 2∗ (x∗y− 1 ) < 0
using assms
by (smt minus-mult-minus mult-le-cancel-left1 )
moreover
have x∗ (y− x) > 0←→ ?rhs
using ‹x⁄= 0 › ‹y⁄= 0 › ‹x⁄= y›
81
by (smt mult-le-0-iﬀ )
ultimately
have∗: Re (to-complex ?cr ) < 0←→ ?rhs
by (simp add : divide-less-0-iﬀ )
show ?thesis
proof
assume ?lhs
have is-real (to-complex ?cr ) Re (to-complex ?cr ) < 0
using ‹?lhs› distinct
unfolding poincare-between-def Let-def
by auto
thus ?rhs
using∗
by simp
next
assume ?rhs
hence Re (to-complex ?cr ) < 0
using∗
by simp
moreover
have{0 h, of-complex (cor x ), of-complex (cor y ), inversion (of-complex (cor x ))}⊆ circline-set x-axis
using ‹x⁄= 0 › is-real-inversion[of cor x ]
using inf-or-of-complex[of inversion ?x ]
by (auto simp del : inversion-of-complex)
hence is-real (to-complex ?cr )
using four-points-on-circline-iﬀ-cross-ratio-real[OF distinct ]
by auto
ultimately
show ?lhs
using distinct
unfolding poincare-between-def Let-def
by auto
qed
qed
lemma poincare-between-0uv:
assumes u∈ unit-disc and v∈ unit-disc and u⁄= 0 h and v⁄= 0 h
shows poincare-between 0h u v ←→
(let u ′ = to-complex u ; v ′ = to-complex v in Arg u ′ = Arg v ′∧ cmod u ′≤ cmod v ′) ( is ?P u v )
proof (cases u = v)
case True
thus ?thesis
by simp
next
case False
have∀ v. v∈ unit-disc∧ v⁄= 0 h∧ v⁄= u−→ (poincare-between 0h u v ←→ (let u ′ = to-complex u ; v ′ = to-complex
v in Arg u ′ = Arg v ′∧ cmod u ′≤ cmod v ′)) ( is ?P ′ u)
proof (rule wlog-rotation-to-positive-x-axis )
show u∈ unit-disc u ⁄= 0 h
by fact+
next
ﬁx x
assume∗: is-real x 0 < Re x Re x < 1
hence of-complex x ∈ unit-disc of-complex x ⁄= 0 h of-complex x ∈ circline-set x-axis
unfolding circline-set-x-axis
by (auto simp add : cmod-eq-Re)
show ?P ′ (of-complex x )
proof safe
ﬁx v
assume v∈ unit-disc v ⁄= 0 h v⁄= of-complex x poincare-between 0 h (of-complex x ) v
hence v∈ circline-set x-axis
using poincare-between-poincare-line-uvz[of 0 h of-complex x v ]
using poincare-line-0-real-is-x-axis[of of-complex x ]
using ‹of-complex x ⁄= 0 h› ‹v⁄= 0 h› ‹v⁄= of-complex x › ‹of-complex x ∈ unit-disc› ‹of-complex x ∈ circline-set
x-axis›
82
by auto
obtain v ′ where v = of-complex v ′
using ‹v∈ unit-disc›
using inf-or-of-complex[of v ]
by auto
hence∗∗: v = of-complex v ′−1 < Re v ′ Re v ′< 1 Re v ′⁄= 0 is-real v ′
using ‹v∈ unit-disc› ‹v⁄= 0 h› ‹v∈ circline-set x-axis › of-complex-inj[of v ′]
unfolding circline-set-x-axis
by (auto simp add : cmod-eq-Re real-imag-0)
show let u ′ = to-complex (of-complex x ); v ′ = to-complex v in Arg u ′ = Arg v ′∧ cmod u ′≤ cmod v ′
using poincare-between-x-axis-0uv[of Re x Re v ′]∗∗∗
using ‹poincare-between 0h (of-complex x ) v›
using arg-complex-of-real-positive[of Re x ] arg-complex-of-real-negative[of Re x ]
using arg-complex-of-real-positive[of Re v ′] arg-complex-of-real-negative[of Re v ′]
by (auto simp add : cmod-eq-Re)
next
ﬁx v
assume v∈ unit-disc v ⁄= 0 h v⁄= of-complex x
then obtain v ′ where∗∗: v = of-complex v ′ v ′⁄= 0 v ′⁄= x
using inf-or-of-complex[of v ]
by auto blast
assume let u ′ = to-complex (of-complex x ); v ′ = to-complex v in Arg u ′ = Arg v ′∧ cmod u ′≤ cmod v ′
hence∗∗∗: Re x < 0∧ Re v ′< 0∧ Re v ′≤ Re x ∨ 0 < Re x ∧ 0 < Re v ′∧ Re x ≤ Re v ′ is-real v ′
using arg-pi-iﬀ [of x ] arg-pi-iﬀ [of v ′]
using arg-0-iﬀ [of x ] arg-0-iﬀ [of v ′]
using∗∗∗
by (smt cmod-Re-le-iﬀ to-complex-of-complex )+
have−1 < Re v ′ Re v ′< 1 Re v ′⁄= 0 is-real v ′
using ‹v∈ unit-disc›∗∗ ‹is-real v ′›
by (auto simp add : cmod-eq-Re complex-eq-if-Re-eq)
thus poincare-between 0h (of-complex x ) v
using poincare-between-x-axis-0uv[of Re x Re v ′]∗∗∗∗∗∗
by simp
qed
next
ﬁx ϕ u
assume u∈ unit-disc u ⁄= 0 h
let ?M = moebius-rotationϕ
assume∗: ?P ′ (moebius-pt ?M u )
show ?P ′ u
proof (rule allI , rule impI, (erule conjE )+)
ﬁx v
assume v∈ unit-disc v ⁄= 0 h v⁄= u
have moebius-pt ?M v ⁄= moebius-pt ?M u
using ‹v⁄= u›
by auto
obtain u ′ v ′ where v = of-complex v ′ u = of-complex u ′ v ′⁄= 0 u ′⁄= 0
using inf-or-of-complex[of u ] inf-or-of-complex[of v ]
using ‹v∈ unit-disc› ‹u∈ unit-disc› ‹v⁄= 0 h› ‹u⁄= 0 h›
by auto
thus ?P u v
using∗[rule-format, of moebius-pt ?M v ]
using ‹moebius-pt ?M v ⁄= moebius-pt ?M u ›
using unit-disc-ﬁx-moebius-preserve-poincare-between[of ?M 0 h u v ]
using ‹v∈ unit-disc› ‹u∈ unit-disc› ‹v⁄= 0 h› ‹u⁄= 0 h›
using arg-mult-eq[of cis ϕ u ′ v ′]
by simp (auto simp add : arg-mult norm-mult )
qed
qed
thus ?thesis
using assms False
by auto
qed
lemma poincare-between-y-axis-0uv:
ﬁxes x y :: real
83
assumes−1 < x and x < 1 and x⁄= 0
assumes−1 < y and y < 1 and y⁄= 0
shows poincare-between 0h (of-complex (i∗ x)) ( of-complex (i∗ y))←→
(x < 0∧ y < 0∧ y≤ x)∨ (x > 0∧ y > 0∧ x≤ y) ( is ?lhs←→ ?rhs)
using assms
using poincare-between-0uv[of of-complex (i∗ x) of-complex (i∗ y)]
using arg-pi2-iﬀ [of i∗ cor x ] arg-pi2-iﬀ [of i∗ cor y ]
using arg-minus-pi2-iﬀ [of i∗ cor x ] arg-minus-pi2-iﬀ [of i∗ cor y ]
apply (simp add : norm-mult)
apply (smt (verit, best))
done
lemma poincare-between-x-axis-uvw:
ﬁxes x y z :: real
assumes−1 < x and x < 1
assumes−1 < y and y < 1 and y⁄= x
assumes−1 < z and z < 1 and z⁄= x
shows poincare-between (of-complex x ) ( of-complex y ) ( of-complex z )←→
(y < x∧ z < x∧ z≤ y)∨ (y > x∧ z > x∧ y≤ z) ( is ?lhs←→ ?rhs)
proof (cases x = 0∨ y = 0∨ z = 0 )
case True
thus ?thesis
proof (cases x = 0 )
case True
thus ?thesis
using poincare-between-x-axis-0uv assms
by simp
next
case False
show ?thesis
proof (cases z = 0 )
case True
thus ?thesis
using poincare-between-x-axis-0uv assms poincare-between-rev
by (smt norm-of-real of-complex-zero of-real-0 poincare-between-nonstrict (2 ) unit-disc-iﬀ-cmod-lt-1 )
next
case False
have y = 0
using ‹x⁄= 0 › ‹z⁄= 0 › ‹x = 0∨ y = 0∨ z = 0 ›
by simp
have poincare-between (of-complex x ) 0 h (of-complex z ) = ( is-real z ∧ x∗ z < 0 )
using ‹x⁄= 0 › ‹z⁄= 0 › poincare-between-x-axis-u0v
by auto
moreover
have x∗ z < 0←→ ?rhs
using True ‹x⁄= 0 › ‹z⁄= 0 ›
by (smt zero-le-mult-iﬀ )
ultimately
show ?thesis
using ‹y = 0 ›
by auto
qed
qed
next
case False
thus ?thesis
proof (cases z = y)
case True
thus ?thesis
using assms
unfolding poincare-between-def
by auto
next
case False
let ?x = of-complex x and ?y = of-complex y and ?z = of-complex z
84
have ?x∈ unit-disc ?y ∈ unit-disc ?z ∈ unit-disc
using assms
by auto
have distinct: distinct [?x, ?y, ?z, inversion ?y ]
using ‹y⁄= x› ‹z⁄= x› False ‹?x∈ unit-disc› ‹?y∈ unit-disc› ‹?z∈ unit-disc›
using inversion-noteq-unit-disc[of ?y ?y ]
using inversion-noteq-unit-disc[of ?y ?x ]
using inversion-noteq-unit-disc[of ?y ?z ]
using of-complex-inj[of x y ] of-complex-inj[of y z ] of-complex-inj[of x z ]
by auto
have cor y ∗ cor x ⁄= 1
using assms
by (smt minus-mult-minus mult-less-cancel-left2 mult-less-cancel-right2 of-real-1 of-real-eq-iﬀ of-real-mult )
let ?cr = cross-ratio ?x ?y ?z (inversion ?y )
have Re (to-complex ?cr ) = ( x− y)∗ (z∗y− 1 )/ ((x∗y− 1 )∗(z− y))
proof−
have ⋀y x z . [ [y⁄= x; z⁄= x; z⁄= y; cor y ∗ cor x ⁄= 1 ; x⁄= 0 ; y⁄= 0 ; z⁄= 0 ] ] =⇒
(y∗ y + y∗ (y∗ (x∗ z))− (y∗ x + y∗ (y∗ (y∗ z)))) /
(y∗ y + y∗ (y∗ (x∗ z))− (y∗ z + y∗ (y∗ (y∗ x)))) =
(y + y∗ (x∗ z)− (x + y∗ (y∗ z))) / (y + y∗ (x∗ z)− (z + y∗ (y∗ x)))
by (metis (no-types, opaque-lifting) ab-group-add-class.ab-diﬀ-conv-add-uminus distrib-left mult-divide-mult-cancel-left-if
mult-minus-right)
thus ?thesis
using ‹y⁄= x› ‹z⁄= x› False ‹¬ (x = 0∨ y = 0∨ z = 0 )›
using ‹cor y ∗ cor x ⁄= 1 ›
unfolding inversion-def
by (transfer, transfer, auto simp add : vec-cnj-def power2-eq-square ﬁeld-simps split : if-split-asm)
qed
moreover
have (x∗y− 1 ) < 0
using assms
by (smt minus-mult-minus mult-less-cancel-right2 zero-less-mult-iﬀ )
moreover
have (z∗y− 1 ) < 0
using assms
by (smt minus-mult-minus mult-less-cancel-right2 zero-less-mult-iﬀ )
moreover
have (x− y) / (z− y) < 0←→ ?rhs
using ‹y⁄= x› ‹z⁄= x› False ‹¬ (x = 0∨ y = 0∨ z = 0 )›
by (smt divide-less-cancel divide-nonneg-nonpos divide-nonneg-pos divide-nonpos-nonneg divide-nonpos-nonpos )
ultimately
have∗: Re (to-complex ?cr ) < 0←→ ?rhs
by (smt algebra-split-simps (24 ) minus-divide-left zero-less-divide-iﬀ zero-less-mult-iﬀ )
show ?thesis
proof
assume ?lhs
have is-real (to-complex ?cr ) Re (to-complex ?cr ) < 0
using ‹?lhs› distinct
unfolding poincare-between-def Let-def
by auto
thus ?rhs
using∗
by simp
next
assume ?rhs
hence Re (to-complex ?cr ) < 0
using∗
by simp
moreover
have{of-complex (cor x ), of-complex (cor y ), of-complex (cor z ), inversion (of-complex (cor y ))}⊆ circline-set
x-axis
85
using ‹¬ (x = 0∨ y = 0∨ z = 0 )› is-real-inversion[of cor y ]
using inf-or-of-complex[of inversion ?y ]
by (auto simp del : inversion-of-complex)
hence is-real (to-complex ?cr )
using four-points-on-circline-iﬀ-cross-ratio-real[OF distinct ]
by auto
ultimately
show ?lhs
using distinct
unfolding poincare-between-def Let-def
by auto
qed
qed
qed
