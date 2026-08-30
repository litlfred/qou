---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-043-check-if-an-h-line-intersects-the-positive-part
section_title: "Check if an h-line intersects the positive part of the x-axis"
section_number: null
pages: 105-108
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
deﬁnition intersects-x-axis-positive-cmat :: complex-mat⇒ bool where
[simp]: intersects-x-axis-positive-cmat H = ( let (A, B, C, D) = H in Re A ⁄= 0∧ Re B / Re A <−1 )
lift-deﬁnition intersects-x-axis-positive-clmat :: circline-mat⇒ bool is intersects-x-axis-positive-cmat
done
lift-deﬁnition intersects-x-axis-positive :: circline⇒ bool is intersects-x-axis-positive-clmat
proof (transfer)
ﬁx H1 H2
assume hh: hermitean H1 ∧ H1⁄= mat-zero and hermitean H2 ∧ H2⁄= mat-zero
obtain A1 B1 C1 D1 A2 B2 C2 D2 where∗: H1 = ( A1, B1, C1, D1 ) H2 = ( A2, B2, C2, D2 )
by (cases H1, cases H2, auto)
assume circline-eq-cmat H1 H2
then obtain k where k⁄= 0∧ H2 = cor k ∗sm H1
by auto
thus intersects-x-axis-positive-cmat H1 = intersects-x-axis-positive-cmat H2
using∗
by simp
qed
lemma intersects-x-axis-positive-mk-circline:
assumes is-real A and A⁄= 0∨ B⁄= 0
shows intersects-x-axis-positive (mk-circline A B (cnj B ) A)←→ Re B / Re A <−1
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
105
show ?thesis
by (transfer, transfer, auto simp add : Let-def )
qed
lemma intersects-x-axis-positive-intersects-x-axis [simp]:
assumes intersects-x-axis-positive H
shows intersects-x-axis H
proof−
have ⋀ a aa. [ [Re a ⁄= 0 ; Re aa / Re a <− 1 ;¬ (Re a )2 < (Re aa )2 ] ] =⇒ aa = 0∧ a = 0
by (smt less-divide-eq-1-pos one-less-power pos2 power2-minus power-divide zero-less-power2 )
thus ?thesis
using assms
apply transfer
apply transfer
apply (auto simp add : hermitean-def mat-adj-def mat-cnj-def )
done
qed
lemma add-less-abs-positive-iﬀ :
ﬁxes a b :: real
assumes abs b < abs a
shows a + b > 0←→ a > 0
using assms
by auto
lemma calc-x-axis-intersection-positive-abs′:
ﬁxes A B :: real
assumes B2 > A2 and A⁄= 0
shows abs (sgn(B)∗ sqrt(B2− A2) / A) < abs(−B/A)
proof−
from assms have B⁄= 0
by auto
have B2− A2 < B2
using ‹A⁄= 0 ›
by auto
hence sqrt (B2− A2) < abs B
using real-sqrt-less-iﬀ [of B 2− A2 B2]
by simp
thus ?thesis
using assms ‹B⁄= 0 ›
by (simp add : abs-mult divide-strict-right-mono )
qed
lemma calc-intersect-x-axis-positive-lemma:
assumes B2 > A2 and A⁄= 0
shows (−B + sgn B ∗ sqrt(B2− A2)) / A > 0←→− B/A > 1
proof−
have (−B + sgn B ∗ sqrt(B2− A2)) / A =−B / A + ( sgn B ∗ sqrt(B2− A2)) / A
using assms
by (simp add : ﬁeld-simps)
moreover
have−B / A + ( sgn B ∗ sqrt(B2− A2)) / A > 0←→− B / A > 0
using add-less-abs-positive-iﬀ [OF calc-x-axis-intersection-positive-abs ′[OF assms ]]
by simp
moreover
hence (B/A)2 > 1
using assms
by (simp add : power-divide)
hence B/A > 1∨ B/A <−1
by (smt one-power2 pos2 power2-minus power-0 power-strict-decreasing zero-power2 )
hence−B / A > 0←→− B / A > 1
by auto
ultimately
show ?thesis
106
using assms
by auto
qed
lemma intersects-x-axis-positive-iﬀ ′:
assumes is-poincare-line H
shows intersects-x-axis-positive H ←→
calc-x-axis-intersection H ∈ unit-disc∧ calc-x-axis-intersection H ∈ circline-set H ∩ positive-x-axis (is ?lhs←→
?rhs)
proof
let ?x = calc-x-axis-intersection H
assume ?lhs
hence ?x∈ circline-set x-axis ?x ∈ circline-set H ?x ∈ unit-disc
using calc-x-axis-intersection-in-unit-disc[OF assms ] calc-x-axis-intersection[OF assms ]
by auto
moreover
have Re (to-complex ?x ) > 0
using ‹?lhs› assms
proof (transfer, transfer)
ﬁx H
assume hh: hermitean H ∧ H⁄= mat-zero
obtain A B C D where∗: H = ( A, B, C, D)
by (cases H, auto)
assume intersects-x-axis-positive-cmat H
hence∗∗: Re B / Re A <− 1 Re A ⁄= 0
using∗
by auto
have (Re B )2 > (Re A )2
using∗∗
by (smt divide-less-eq-1-neg divide-minus-left less-divide-eq-1-pos real-sqrt-abs real-sqrt-less-iﬀ right-inverse-eq )
have is-real A A ⁄= 0
using hh hermitean-elems ∗ ‹Re A⁄= 0 › complex.expand[of A 0 ]
by auto
have (cmod B )2 > (cmod A )2
using ‹(Re B )2 > (Re A )2› ‹is-real A›
by (smt cmod-power2 power2-less-0 zero-power2 )
have∗∗∗: 0 < (− Re B + sgn (Re B )∗ sqrt ((Re B )2− (Re A )2)) / Re A
using calc-intersect-x-axis-positive-lemma[of Re A Re B ]∗∗ ‹(Re B )2 > (Re A )2›
by auto
assume is-poincare-line-cmat H
hence A = D
using∗ hh
by simp
have Re ((cor (sgn (Re B ))∗ cor (sqrt ((Re B )2− (Re A )2))− cor (Re B )) / A) = ( sgn (Re B )∗ sqrt ((Re B )2
− (Re A )2)− Re B ) / Re D
using ‹is-real A› ‹A = D›
by (metis (no-types, lifting) Re-complex-of-real complex-of-real-Re of-real-diﬀ of-real-divide of-real-mult)
thus 0 < Re (to-complex-cvec (calc-x-axis-intersection-cmat-cvec H ))
using∗ hh∗∗∗∗∗ ‹(cmod B )2 > (cmod A )2› ‹(Re B )2 > (Re A )2› ‹A⁄= 0 › ‹A = D›
by simp
qed
ultimately
show ?rhs
unfolding positive-x-axis-def
by auto
next
let ?x = calc-x-axis-intersection H
assume ?rhs
hence Re (to-complex ?x ) > 0 ?x ⁄=∞h ?x∈ circline-set x-axis ?x ∈ unit-disc ?x ∈ circline-set H
unfolding positive-x-axis-def
by auto
hence intersects-x-axis H
using intersects-x-axis-iﬀ [OF assms ]
by auto
107
thus ?lhs
using ‹Re (to-complex ?x ) > 0 › assms
proof (transfer, transfer)
ﬁx H
assume hh: hermitean H ∧ H⁄= mat-zero
obtain A B C D where∗: H = ( A, B, C, D)
by (cases H, auto)
assume 0 < Re (to-complex-cvec (calc-x-axis-intersection-cmat-cvec H)) intersects-x-axis-cmat H is-poincare-line-cmat
H
hence∗∗: A⁄= 0 0 < Re ((cor (sgn (Re B ))∗ cor (sqrt ((Re B )2− (Re A )2))− cor (Re B )) / A) A = D is-real
A (Re B )2 > (Re A )2
using∗ hh hermitean-elems
by (auto split : if-split-asm)
have Re A⁄= 0
using complex.expand[of A 0 ] ‹A⁄= 0 › ‹is-real A›
by auto
have Re ((cor (sgn (Re B ))∗ cor (sqrt ((Re B )2− (Re D )2))− cor (Re B )) / D) = ( sgn (Re B )∗ sqrt ((Re B )2
− (Re D )2)− Re B ) / Re D
using ‹is-real A› ‹A = D›
by (metis (no-types, lifting) Re-complex-of-real complex-of-real-Re of-real-diﬀ of-real-divide of-real-mult)
thus intersects-x-axis-positive-cmat H
using∗∗∗ ‹Re A⁄= 0 ›
using calc-intersect-x-axis-positive-lemma[of Re A Re B ]
by simp
qed
qed
lemma intersects-x-axis-positive-iﬀ :
assumes is-poincare-line H and H⁄= x-axis
shows intersects-x-axis-positive H ←→
(∃ x. x∈ unit-disc∧ x∈ circline-set H ∩ positive-x-axis) ( is ?lhs←→ ?rhs)
proof
assume ?lhs
thus ?rhs
using intersects-x-axis-positive-iﬀ ′[OF assms (1 )]
by auto
next
assume ?rhs
then obtain x where x∈ unit-disc x ∈ circline-set H ∩ positive-x-axis
by auto
thus ?lhs
using unique-calc-x-axis-intersection[OF assms, of x ]
using intersects-x-axis-positive-iﬀ ′[OF assms (1 )]
unfolding positive-x-axis-def
by auto
qed
