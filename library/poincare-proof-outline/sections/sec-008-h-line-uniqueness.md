---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-008-h-line-uniqueness
section_title: "H-line uniqueness"
section_number: null
pages: 11-14
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
There is no more than one h-line that contains two diﬀerent h-points (in the disc).
lemma unique-is-poincare-line:
assumes in-disc: u∈ unit-disc v ∈ unit-disc u ⁄= v
assumes pl: is-poincare-line l1 is-poincare-line l2
assumes on-l:{u, v}⊆ circline-set l1 ∩ circline-set l2
shows l1 = l2
11
proof−
have u⁄= inversion u v ⁄= inversion u
using in-disc
using inversion-noteq-unit-disc[of u v ]
using inversion-noteq-unit-disc[of u u ]
by auto
thus ?thesis
using on-l
using unique-circline-set[of u inversion u v ] ‹u⁄= v›
using is-poincare-line-inverse-point[of l1 u ]
using is-poincare-line-inverse-point[of l2 u ]
using pl
by auto
qed
For the rest of our formalization it is often useful to consider points on h-lines that are not within the unit disc.
Many lemmas in the rest of this section will have such generalizations.
There is no more than one h-line that contains two diﬀerent and not mutually inverse points (not necessary in
the unit disc).
lemma unique-is-poincare-line-general:
assumes diﬀerent: u⁄= v u ⁄= inversion v
assumes pl: is-poincare-line l1 is-poincare-line l2
assumes on-l:{u, v}⊆ circline-set l1 ∩ circline-set l2
shows l1 = l2
proof (cases u ⁄= inversion u )
case True
thus ?thesis
using unique-circline-set[of u inversion u v ]
using assms
using is-poincare-line-inverse-point by force
next
case False
show ?thesis
proof (cases v ⁄= inversion v )
case True
thus ?thesis
using unique-circline-set[of u inversion v v ]
using assms
using is-poincare-line-inverse-point by force
next
case False
have on-circline unit-circle u on-circline unit-circle v
using ‹¬ u⁄= inversion u › ‹¬ v⁄= inversion v ›
using inversion-id-iﬀ-on-unit-circle
by fastforce+
thus ?thesis
using pl on-l ‹u⁄= v›
unfolding circline-set-def
apply simp
proof (transfer, transfer, safe)
ﬁx u1 u2 v1 v2 A1 B1 C1 D1 A2 B2 C2 D2 :: complex
let ?u = ( u1, u2 ) and ?v = ( v1, v2 ) and ?H1 = ( A1, B1, C1, D1 ) and ?H2 = ( A2, B2, C2, D2 )
assume∗: ?u⁄= vec-zero ?v⁄= vec-zero
on-circline-cmat-cvec unit-circle-cmat ?u on-circline-cmat-cvec unit-circle-cmat ?v
is-poincare-line-cmat ?H1 is-poincare-line-cmat ?H2
hermitean ?H1 ?H1 ⁄= mat-zero hermitean ?H2 ?H2 ⁄= mat-zero
on-circline-cmat-cvec ?H1 ?u on-circline-cmat-cvec ?H1 ?v
on-circline-cmat-cvec ?H2 ?u on-circline-cmat-cvec ?H2 ?v
¬ (u1, u2 )≈v (v1, v2 )
have∗∗: A1 = D1 A2 = D2 C1 = cnj B1 C2 = cnj B2 is-real A1 is-real A2
using ‹is-poincare-line-cmat ?H1 › ‹is-poincare-line-cmat ?H2 ›
using ‹hermitean ?H1 › ‹?H1⁄= mat-zero› ‹hermitean ?H2 › ‹?H2⁄= mat-zero›
using hermitean-elems
by auto
12
have uv: u1⁄= 0 u2 ⁄= 0 v1 ⁄= 0 v2 ⁄= 0
using∗(1−4 )
by (auto simp add : vec-cnj-def )
have u: cor ((Re (u1/u2 ))2) + cor ((Im (u1/u2 ))2) = 1
using ‹on-circline-cmat-cvec unit-circle-cmat ?u › uv
apply (subst of-real-add [symmetric])
apply (subst complex-mult-cnj [symmetric])
apply (simp add : vec-cnj-def mult.commute)
done
have v: cor ((Re (v1/v2 ))2) + cor ((Im (v1/v2 ))2) = 1
using ‹on-circline-cmat-cvec unit-circle-cmat ?v › uv
apply (subst of-real-add [symmetric])
apply (subst complex-mult-cnj [symmetric])
apply (simp add : vec-cnj-def mult.commute)
done
have
A1∗ (cor ((Re (u1/u2 ))2) + cor ((Im (u1/u2 ))2) + 1 ) + cor (Re B1 )∗ cor(2∗ Re (u1/u2 )) + cor (Im B1 )
∗ cor(2∗ Im (u1/u2 )) = 0
A2∗ (cor ((Re (u1/u2 ))2) + cor ((Im (u1/u2 ))2) + 1 ) + cor (Re B2 )∗ cor(2∗ Re (u1/u2 )) + cor (Im B2 )
∗ cor(2∗ Im (u1/u2 )) = 0
A1∗ (cor ((Re (v1/v2 ))2) + cor ((Im (v1/v2 ))2) + 1 ) + cor (Re B1 )∗ cor(2∗ Re (v1/v2 )) + cor (Im B1 )∗
cor(2∗ Im (v1/v2 )) = 0
A2∗ (cor ((Re (v1/v2 ))2) + cor ((Im (v1/v2 ))2) + 1 ) + cor (Re B2 )∗ cor(2∗ Re (v1/v2 )) + cor (Im B2 )∗
cor(2∗ Im (v1/v2 )) = 0
using circline-equation-quadratic-equation[of A1 u1 /u2 B1 D1 Re (u1/u2 ) Im (u1 / u2 ) Re B1 Im B1 ]
using circline-equation-quadratic-equation[of A2 u1 /u2 B2 D2 Re (u1/u2 ) Im (u1 / u2 ) Re B2 Im B2 ]
using circline-equation-quadratic-equation[of A1 v1 /v2 B1 D1 Re (v1/v2 ) Im (v1 / v2 ) Re B1 Im B1 ]
using circline-equation-quadratic-equation[of A2 v1 /v2 B2 D2 Re (v1/v2 ) Im (v1 / v2 ) Re B2 Im B2 ]
using ‹on-circline-cmat-cvec ?H1 ?u › ‹on-circline-cmat-cvec ?H2 ?u ›
using ‹on-circline-cmat-cvec ?H1 ?v › ‹on-circline-cmat-cvec ?H2 ?v ›
using∗∗ uv
by (simp-all add : vec-cnj-def ﬁeld-simps )
hence
A1 + cor (Re B1 )∗ cor(Re (u1/u2 )) + cor (Im B1 )∗ cor(Im (u1/u2 )) = 0
A1 + cor (Re B1 )∗ cor(Re (v1/v2 )) + cor (Im B1 )∗ cor(Im (v1/v2 )) = 0
A2 + cor (Re B2 )∗ cor(Re (u1/u2 )) + cor (Im B2 )∗ cor(Im (u1/u2 )) = 0
A2 + cor (Re B2 )∗ cor(Re (v1/v2 )) + cor (Im B2 )∗ cor(Im (v1/v2 )) = 0
using u v
by simp-all algebra +
hence
cor (Re A1 + Re B1 ∗ Re (u1/u2 ) + Im B1 ∗ Im (u1/u2 )) = 0
cor (Re A2 + Re B2 ∗ Re (u1/u2 ) + Im B2 ∗ Im (u1/u2 )) = 0
cor (Re A1 + Re B1 ∗ Re (v1/v2 ) + Im B1 ∗ Im (v1/v2 )) = 0
cor (Re A2 + Re B2 ∗ Re (v1/v2 ) + Im B2 ∗ Im (v1/v2 )) = 0
using ‹is-real A1 › ‹is-real A2 ›
by simp-all
hence
Re A1 + Re B1 ∗ Re (u1/u2 ) + Im B1 ∗ Im (u1/u2 ) = 0
Re A1 + Re B1 ∗ Re (v1/v2 ) + Im B1 ∗ Im (v1/v2 ) = 0
Re A2 + Re B2 ∗ Re (u1/u2 ) + Im B2 ∗ Im (u1/u2 ) = 0
Re A2 + Re B2 ∗ Re (v1/v2 ) + Im B2 ∗ Im (v1/v2 ) = 0
using of-real-eq-0-iﬀ
by blast+
moreover
have Re(u1/u2 )⁄= Re(v1/v2 )∨ Im(u1/u2 )⁄= Im(v1/v2 )
proof (rule ccontr )
assume¬ ?thesis
13
hence u1/u2 = v1/v2
using complex-eqI by blast
thus False
using uv ‹¬ (u1, u2 )≈v (v1, v2 )›
using∗(1 )∗(2 ) complex-cvec-eq-mix[OF∗(1 )∗(2 )]
by (auto simp add : ﬁeld-simps)
qed
moreover
have Re A1 ⁄= 0∨ Re B1 ⁄= 0∨ Im B1 ⁄= 0
using ‹?H1⁄= mat-zero›∗∗
by (metis complex-cnj-zero complex-of-real-Re mat-zero-def of-real-0 )
ultimately
obtain k where
k: Re A2 = k∗ Re A1 Re B2 = k∗ Re B1 Im B2 = k∗ Im B1
using linear-system-homogenous-3-2[of λx y z . 1∗ x + Re (u1 / u2 )∗ y + Im (u1 / u2 )∗ z 1 Re (u1/u2 ) Im
(u1/u2 )
λx y z . 1∗ x + Re (v1 / v2 )∗ y + Im (v1 / v2 )∗ z 1 Re (v1/v2 ) Im (v1/v2 )
Re A2 Re B2 Im B2 Re A1 Re B1 Im B1 ]
by (auto simp add : ﬁeld-simps)
have Re A2 ⁄= 0∨ Re B2 ⁄= 0∨ Im B2 ⁄= 0
using ‹?H2⁄= mat-zero›∗∗
by (metis complex-cnj-zero complex-of-real-Re mat-zero-def of-real-0 )
hence k⁄= 0
using k
by auto
show circline-eq-cmat ?H1 ?H2
using∗∗ k ‹k⁄= 0 ›
by (auto simp add : vec-cnj-def ) ( rule-tac x =k in exI, auto simp add : complex.expand)
qed
qed
qed
The only h-line that goes trough zero and a non-zero point on the x-axis is the x-axis.
lemma is-poincare-line-0-real-is-x-axis:
assumes is-poincare-line l 0 h∈ circline-set l
x∈ circline-set l ∩ circline-set x-axis x ⁄= 0 h x⁄=∞h
shows l = x-axis
using assms
using is-poincare-line-trough-zero-trough-infty[OF assms (1−2 )]
using unique-circline-set[of x 0 h∞h]
by auto
The only h-line that goes trough zero and a non-zero point on the y-axis is the y-axis.
lemma is-poincare-line-0-imag-is-y-axis:
assumes is-poincare-line l 0 h∈ circline-set l
y∈ circline-set l ∩ circline-set y-axis y ⁄= 0 h y⁄=∞h
shows l = y-axis
using assms
using is-poincare-line-trough-zero-trough-infty[OF assms (1−2 )]
using unique-circline-set[of y 0 h∞h]
by auto
