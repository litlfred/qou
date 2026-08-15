---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-044-check-if-an-h-line-intersects-the-positive-part
section_title: "Check if an h-line intersects the positive part of the y-axis"
section_number: null
pages: 108-110
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
deﬁnition intersects-y-axis-positive-cmat :: complex-mat⇒ bool where
[simp]: intersects-y-axis-positive-cmat H = ( let (A, B, C, D) = H in Re A ⁄= 0∧ Im B / Re A <−1 )
lift-deﬁnition intersects-y-axis-positive-clmat :: circline-mat⇒ bool is intersects-y-axis-positive-cmat
done
lift-deﬁnition intersects-y-axis-positive :: circline⇒ bool is intersects-y-axis-positive-clmat
proof (transfer)
ﬁx H1 H2
assume hh: hermitean H1 ∧ H1⁄= mat-zero and hermitean H2 ∧ H2⁄= mat-zero
obtain A1 B1 C1 D1 A2 B2 C2 D2 where∗: H1 = ( A1, B1, C1, D1 ) H2 = ( A2, B2, C2, D2 )
by (cases H1, cases H2, auto)
assume circline-eq-cmat H1 H2
then obtain k where k⁄= 0∧ H2 = cor k ∗sm H1
108
by auto
thus intersects-y-axis-positive-cmat H1 = intersects-y-axis-positive-cmat H2
using∗
by simp
qed
lemma intersects-x-axis-positive-intersects-y-axis-positive [simp]:
shows intersects-x-axis-positive (moebius-circline (moebius-rotation (−pi/2 )) H )←→ intersects-y-axis-positive H
using hermitean-elems
unfolding moebius-rotation-def moebius-similarity-def
by simp (transfer, transfer, auto simp add : mat-adj-def mat-cnj-def )
lemma intersects-y-axis-positive-iﬀ :
assumes is-poincare-line H H ⁄= y-axis
shows (∃ y∈ unit-disc. y∈ circline-set H ∩ positive-y-axis)←→ intersects-y-axis-positive H (is ?lhs←→ ?rhs)
proof−
let ?R = moebius-rotation (−pi / 2 )
let ?H ′ = moebius-circline ?R H
have 1 : is-poincare-line ?H ′
using assms
using unit-circle-ﬁx-preserve-is-poincare-line[OF - assms (1 ), of ?R ]
by simp
have 2 : moebius-circline ?R H ⁄= x-axis
proof (rule ccontr )
assume¬ ?thesis
hence H = moebius-circline (moebius-rotation (pi/2 )) x-axis
using moebius-circline-comp-inv-left[of ?R H ]
by auto
thus False
using ‹H⁄= y-axis›
by auto
qed
show ?thesis
proof
assume ?lhs
then obtain y where y∈ unit-disc y ∈ circline-set H ∩ positive-y-axis
by auto
hence moebius-pt ?R y ∈ unit-disc moebius-pt ?R y ∈ circline-set ?H ′∩ positive-x-axis
using rotation-minus-pi-2-positive-y-axis
by auto
thus ?rhs
using intersects-x-axis-positive-iﬀ [OF 1 2 ]
using intersects-x-axis-positive-intersects-y-axis-positive[of H ]
by auto
next
assume intersects-y-axis-positive H
hence intersects-x-axis-positive ?H ′
using intersects-x-axis-positive-intersects-y-axis-positive[of H ]
by simp
then obtain x where∗: x∈ unit-disc x ∈ circline-set ?H ′∩ positive-x-axis
using intersects-x-axis-positive-iﬀ [OF 1 2 ]
by auto
let ?y = moebius-pt (−?R) x
have ?y∈ unit-disc∧ ?y∈ circline-set H ∩ positive-y-axis
using∗ rotation-minus-pi-2-positive-y-axis[symmetric]
by (metis Int-iﬀ circline-set-moebius-circline-E image-eqI moebius-pt-comp-inv-image-left moebius-rotation-uminus
uminus-moebius-def unit-disc-ﬁx-discI unit-disc-ﬁx-rotation )
thus ?lhs
by auto
qed
qed
109
