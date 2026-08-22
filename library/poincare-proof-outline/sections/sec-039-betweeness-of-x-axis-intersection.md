---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-039-betweeness-of-x-axis-intersection
section_title: "Betweeness of x-axis intersection"
section_number: null
pages: 96-97
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
The intersection point of the h-line determined by points u and v and the x-axis is between u and v, then u
and v are in the opposite half-planes (one must be in the upper, and the other one in the lower half-plane).
lemma poincare-between-x-axis-intersection:
assumes u∈ unit-disc and v∈ unit-disc and z∈ unit-disc and u⁄= v
assumes u /∈ circline-set x-axis and v /∈ circline-set x-axis
assumes z∈ circline-set (poincare-line u v )∩ circline-set x-axis
shows poincare-between u z v ←→ Arg (to-complex u )∗ Arg (to-complex v ) < 0
proof−
have∀ u v. u∈ unit-disc∧ v∈ unit-disc∧ u⁄= v∧
u /∈ circline-set x-axis ∧ v /∈ circline-set x-axis ∧
z∈ circline-set (poincare-line u v )∩ circline-set x-axis −→
(poincare-between u z v ←→ Arg (to-complex u )∗ Arg (to-complex v ) < 0 ) ( is ?P z )
proof (rule wlog-real-zero)
show ?P 0 h
proof ((rule allI )+, rule impI, (erule conjE )+)
ﬁx u v
assume∗: u∈ unit-disc v ∈ unit-disc u ⁄= v
u /∈ circline-set x-axis v /∈ circline-set x-axis
0 h∈ circline-set (poincare-line u v )∩ circline-set x-axis
obtain u ′ v ′ where uv: u = of-complex u ′ v = of-complex v ′
using∗ inf-or-of-complex[of u ] inf-or-of-complex[of v ]
by auto
hence u⁄= 0 h v⁄= 0 h u ′⁄= 0 v ′⁄= 0
using∗
by auto
hence Arg u ′⁄= 0 Arg v ′⁄= 0
using∗ arg-0-iﬀ [of u ′] arg-0-iﬀ [of v ′]
unfolding circline-set-x-axis uv
by auto
have poincare-collinear{0 h, u, v}
using∗
unfolding poincare-collinear-def
by (rule-tac x =poincare-line u v in exI, simp)
have (∃ k<0. u ′ = cor k ∗ v ′)←→ (Arg u ′∗ Arg v ′< 0 ) ( is ?lhs←→ ?rhs)
proof
assume ?lhs
then obtain k where k < 0 u ′ = cor k ∗ v ′
by auto
thus ?rhs
using arg-mult-real-negative[of k v ′] arg-uminus-opposite-sign[of v ′]
using ‹u ′⁄= 0 › ‹v ′⁄= 0 › ‹Arg u ′⁄= 0 › ‹Arg v ′⁄= 0 ›
by (auto simp add : mult-neg-pos mult-pos-neg)
next
assume ?rhs
obtain ru rv ϕ where polar: u ′ = cor ru ∗ cis ϕ v ′ = cor rv ∗ cis ϕ
using ‹poincare-collinear{0 h, u, v}› poincare-collinear-zero-polar-form[of u ′ v ′] uv∗ ‹u ′⁄= 0 › ‹v ′⁄= 0 ›
by auto
have ru∗ rv < 0
using polar ‹?rhs› ‹u ′⁄= 0 › ‹v ′⁄= 0 ›
using arg-mult-real-negative[of ru cis ϕ] arg-mult-real-positive[of ru cis ϕ]
using arg-mult-real-negative[of rv cis ϕ] arg-mult-real-positive[of rv cis ϕ]
apply (cases ru > 0 )
apply (cases rv > 0, simp, simp add : mult-pos-neg)
apply (cases rv > 0, simp add : mult-neg-pos, simp)
done
thus ?lhs
using polar
by (rule-tac x =ru / rv in exI, auto simp add : divide-less-0-iﬀ mult-less-0-iﬀ )
96
qed
thus poincare-between u 0 h v = ( Arg (to-complex u )∗ Arg (to-complex v ) < 0 )
using poincare-between-u0v[of u v ]∗ ‹u⁄= 0 h› ‹v⁄= 0 h› uv
by simp
qed
next
ﬁx a z
assume 1 : is-real a cmod a < 1 z ∈ unit-disc
assume 2 : ?P (moebius-pt (blaschke a ) z)
show ?P z
proof ((rule allI )+, rule impI, (erule conjE )+)
ﬁx u v
let ?M = moebius-pt (blaschke a )
let ?Mu = ?M u
let ?Mv = ?M v
assume∗: u∈ unit-disc v ∈ unit-disc u ⁄= v u /∈ circline-set x-axis v /∈ circline-set x-axis
hence u⁄=∞h v⁄=∞h
by auto
have∗∗: ⋀ x y :: real. x∗ y < 0←→ sgn (x∗ y) < 0
by simp
assume z∈ circline-set (poincare-line u v )∩ circline-set x-axis
thus poincare-between u z v = ( Arg (to-complex u )∗ Arg (to-complex v ) < 0 )
using∗ 1 2 [rule-format, of ?Mu ?Mv ] ‹cmod a < 1 › ‹is-real a › blaschke-unit-disc-ﬁx[of a ]
using inversion-noteq-unit-disc[of of-complex a u ] ‹u⁄=∞h›
using inversion-noteq-unit-disc[of of-complex a v ] ‹v⁄=∞h›
apply auto
apply (subst (asm)∗∗, subst∗∗, subst (asm) sgn-mult, subst sgn-mult, simp)
apply (subst (asm)∗∗, subst (asm)∗∗, subst (asm) sgn-mult, subst (asm) sgn-mult, simp)
done
qed
next
show z∈ unit-disc by fact
next
show is-real (to-complex z )
using assms inf-or-of-complex [of z ]
by (auto simp add : circline-set-x-axis)
qed
thus ?thesis
using assms
by simp
qed
