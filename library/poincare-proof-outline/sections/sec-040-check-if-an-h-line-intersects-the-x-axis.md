---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-040-check-if-an-h-line-intersects-the-x-axis
section_title: "Check if an h-line intersects the x-axis"
section_number: null
pages: 97-100
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma x-axis-intersection-equation:
assumes
H = mk-circline A B C D and
(A, B, C, D)∈ hermitean-nonzero
shows of-complex z ∈ circline-set x-axis ∩ circline-set H ←→
A∗z 2 + 2∗Re B∗z + D = 0∧ is-real z (is ?lhs←→ ?rhs)
proof−
have ?lhs←→ A∗z 2 + ( B + cnj B )∗z + D = 0∧ z = cnj z
using assms
using circline-equation-x-axis[of z ]
using circline-equation[of H A B C D z ]
using hermitean-elems
by (auto simp add : power2-eq-square ﬁeld-simps)
thus ?thesis
using eq-cnj-iﬀ-real[of z ]
using hermitean-elems[of A B C D ]
by (simp add : complex-add-cnj complex-eq-if-Re-eq)
qed
Check if an h-line intersects x-axis within the unit disc - this could be generalized to checking if an arbitrary
97
circline intersects the x-axis, but we do not need that.
deﬁnition intersects-x-axis-cmat :: complex-mat⇒ bool where
[simp]: intersects-x-axis-cmat H = ( let (A, B, C, D) = H in A = 0∨ (Re B )2 > (Re A )2)
lift-deﬁnition intersects-x-axis-clmat :: circline-mat⇒ bool is intersects-x-axis-cmat
done
lift-deﬁnition intersects-x-axis :: circline⇒ bool is intersects-x-axis-clmat
proof (transfer)
ﬁx H1 H2
assume hh: hermitean H1 ∧ H1⁄= mat-zero and hermitean H2 ∧ H2⁄= mat-zero
obtain A1 B1 C1 D1 A2 B2 C2 D2 where∗: H1 = ( A1, B1, C1, D1 ) H2 = ( A2, B2, C2, D2 )
by (cases H1, cases H2, auto)
assume circline-eq-cmat H1 H2
then obtain k where k: k⁄= 0∧ H2 = cor k ∗sm H1
by auto
show intersects-x-axis-cmat H1 = intersects-x-axis-cmat H2
proof−
have k⁄= 0 =⇒ (Re A1 )2 < (Re B1 )2←→ (k∗ Re A1 )2 < (k∗ Re B1 )2
by (smt mult-strict-left-mono power2-eq-square semiring-normalization-rules (13 ) zero-less-power2)
thus ?thesis
using∗ k
by auto
qed
qed
lemma intersects-x-axis-mk-circline:
assumes is-real A and A⁄= 0∨ B⁄= 0
shows intersects-x-axis (mk-circline A B (cnj B ) A)←→ A = 0∨ (Re B )2 > (Re A )2
proof−
let ?H = ( A, B, (cnj B ), A)
have hermitean ?H
using ‹is-real A›
unfolding hermitean-def mat-adj-def mat-cnj-def
using eq-cnj-iﬀ-real
by auto
moreover
have ?H⁄= mat-zero
using assms
by auto
ultimately
show ?thesis
by (transfer, transfer, auto simp add : Let-def )
qed
lemma intersects-x-axis-iﬀ :
assumes is-poincare-line H
shows (∃ x∈ unit-disc. x∈ circline-set H ∩ circline-set x-axis )←→ intersects-x-axis H
proof−
obtain Ac B C Dc where ∗: H = mk-circline Ac B C Dc hermitean (Ac, B, C, Dc) ( Ac, B, C, Dc)⁄= mat-zero
using ex-mk-circline[of H ]
by auto
hence (cmod B )2 > (cmod Ac )2 Ac = Dc
using assms
using is-poincare-line-mk-circline
by auto
hence H = mk-circline (Re Ac) B (cnj B ) ( Re Ac) hermitean (cor (Re Ac), B, (cnj B ), cor (Re Ac)) ( cor (Re Ac),
B, (cnj B ), cor (Re Ac ))⁄= mat-zero
using hermitean-elems[of Ac B C Dc ]∗
by auto
then obtain A where
∗: H = mk-circline (cor A ) B (cnj B ) ( cor A ) ( cor A, B, (cnj B ), cor A )∈ hermitean-nonzero
by auto
show ?thesis
98
proof (cases A = 0 )
case True
thus ?thesis
using∗
using x-axis-intersection-equation[OF∗(1−2 ), of 0 ]
using intersects-x-axis-mk-circline[of cor A B ]
by auto
next
case False
show ?thesis
proof
assume∃ x∈ unit-disc. x∈ circline-set H ∩ circline-set x-axis
then obtain x where∗∗: of-complex x ∈ unit-disc of-complex x ∈ circline-set H ∩ circline-set x-axis
by (metis inf-or-of-complex inf-notin-unit-disc )
hence is-real x
unfolding circline-set-x-axis
using of-complex-inj
by auto
hence eq: A∗ (Re x )2 + 2∗ Re B ∗ Re x + A = 0
using∗∗
using x-axis-intersection-equation[OF∗(1−2 ), of Re x ]
by simp
hence (2∗ Re B )2− 4∗ A∗ A≥ 0
using discriminant-iﬀ [of A - 2 ∗ Re B A ]
using discrim-def [of A 2 ∗ Re B A ] False
by auto
hence (Re B )2≥ (Re A )2
by (simp add : power2-eq-square)
moreover
have (Re B )2⁄= ( Re A )2
proof (rule ccontr )
assume¬ ?thesis
hence Re B = Re A∨ Re B =− Re A
using power2-eq-iﬀ by blast
hence A∗ (Re x )2 + A∗ 2∗ Re x + A = 0∨ A∗ (Re x )2− A∗ 2∗ Re x + A = 0
using eq
by auto
hence A∗ ((Re x )2 + 2∗ Re x + 1 ) = 0∨ A∗ ((Re x )2− 2∗ Re x + 1 ) = 0
by (simp add : ﬁeld-simps)
hence (Re x )2 + 2∗ Re x + 1 = 0∨ (Re x )2− 2∗ Re x + 1 = 0
using ‹A⁄= 0 ›
by simp
hence (Re x + 1 )2 = 0∨ (Re x − 1 )2 = 0
by (simp add : power2-sum power2-diﬀ ﬁeld-simps )
hence Re x =−1∨ Re x = 1
by auto
thus False
using ‹is-real x › ‹of-complex x ∈ unit-disc›
by (auto simp add : cmod-eq-Re)
qed
ultimately
show intersects-x-axis H
using intersects-x-axis-mk-circline
using∗
by auto
next
assume intersects-x-axis H
hence (Re B )2 > (Re A )2
using∗ False
using intersects-x-axis-mk-circline
by simp
hence discr: ( 2∗ Re B )2− 4∗ A∗ A > 0
by (simp add : power2-eq-square)
then obtain x1 x2 where
eqs: A∗ x1 2 + 2∗ Re B ∗ x1 + A = 0 A ∗ x2 2 + 2∗ Re B ∗ x2 + A = 0 x1 ⁄= x2
using discriminant-pos-ex[OF ‹A⁄= 0 ›, of 2 ∗ Re B A ]
99
using discrim-def [of A 2 ∗ Re B A ]
by auto
hence x1∗ x2 = 1
using viette2 [OF ‹A⁄= 0 ›, of 2 ∗ Re B A x1 x2 ] discr ‹A⁄= 0 ›
by auto
have abs x1 ⁄= 1 abs x2 ⁄= 1
using eqs discr ‹x1∗ x2 = 1 ›
by (auto simp add : abs-if power2-eq-square)
hence abs x1 < 1∨ abs x2 < 1
using ‹x1∗ x2 = 1 ›
by (smt mult-le-cancel-left1 mult-minus-right )
thus∃ x∈ unit-disc. x∈ circline-set H ∩ circline-set x-axis
using x-axis-intersection-equation[OF∗(1−2 ), of x1 ]
using x-axis-intersection-equation[OF∗(1−2 ), of x2 ]
using eqs
by auto
qed
qed
qed
