---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-041-check-if-a-poincaré-line-intersects-the-y-axis
section_title: "Check if a Poincaré line intersects the y-axis"
section_number: null
pages: 100-101
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
deﬁnition intersects-y-axis-cmat :: complex-mat⇒ bool where
[simp]: intersects-y-axis-cmat H = ( let (A, B, C, D) = H in A = 0∨ (Im B )2 > (Re A )2)
lift-deﬁnition intersects-y-axis-clmat :: circline-mat⇒ bool is intersects-y-axis-cmat
done
lift-deﬁnition intersects-y-axis :: circline⇒ bool is intersects-y-axis-clmat
proof (transfer)
ﬁx H1 H2
assume hh: hermitean H1 ∧ H1⁄= mat-zero and hermitean H2 ∧ H2⁄= mat-zero
obtain A1 B1 C1 D1 A2 B2 C2 D2 where∗: H1 = ( A1, B1, C1, D1 ) H2 = ( A2, B2, C2, D2 )
by (cases H1, cases H2, auto)
assume circline-eq-cmat H1 H2
then obtain k where k: k⁄= 0∧ H2 = cor k ∗sm H1
by auto
show intersects-y-axis-cmat H1 = intersects-y-axis-cmat H2
proof−
have k⁄= 0 =⇒ (Re A1 )2 < (Im B1 )2←→ (k∗ Re A1 )2 < (k∗ Im B1 )2
by (smt mult-strict-left-mono power2-eq-square semiring-normalization-rules (13 ) zero-less-power2)
thus ?thesis
using∗ k
by auto
qed
qed
lemma intersects-x-axis-intersects-y-axis [simp]:
shows intersects-x-axis (moebius-circline (moebius-rotation (pi/2 )) H )←→ intersects-y-axis H
unfolding moebius-rotation-def moebius-similarity-def
by simp (transfer, transfer, auto simp add : mat-adj-def mat-cnj-def )
lemma intersects-y-axis-iﬀ :
assumes is-poincare-line H
shows (∃ y∈ unit-disc. y∈ circline-set H ∩ circline-set y-axis )←→ intersects-y-axis H (is ?lhs←→ ?rhs)
proof−
let ?R = moebius-rotation (pi / 2 )
let ?H ′ = moebius-circline ?R H
have 1 : is-poincare-line ?H ′
using assms
using unit-circle-ﬁx-preserve-is-poincare-line[OF - assms , of ?R ]
by simp
show ?thesis
proof
assume ?lhs
100
then obtain y where y∈ unit-disc y ∈ circline-set H ∩ circline-set y-axis
by auto
hence moebius-pt ?R y ∈ unit-disc∧ moebius-pt ?R y ∈ circline-set ?H ′∩ circline-set x-axis
using rotation-pi-2-y-axis
by (metis Int-iﬀ circline-set-moebius-circline-E moebius-circline-comp-inv-left moebius-pt-comp-inv-left unit-disc-ﬁx-discI
unit-disc-ﬁx-rotation)
thus ?rhs
using intersects-x-axis-iﬀ [OF 1 ]
using intersects-x-axis-intersects-y-axis[of H ]
by auto
next
assume intersects-y-axis H
hence intersects-x-axis ?H ′
using intersects-x-axis-intersects-y-axis[of H ]
by simp
then obtain x where∗: x∈ unit-disc x ∈ circline-set ?H ′∩ circline-set x-axis
using intersects-x-axis-iﬀ [OF 1 ]
by auto
let ?y = moebius-pt (−?R) x
have ?y∈ unit-disc∧ ?y∈ circline-set H ∩ circline-set y-axis
using∗ rotation-pi-2-y-axis[symmetric]
by (metis Int-iﬀ circline-set-moebius-circline-E moebius-pt-comp-inv-left moebius-rotation-uminus uminus-moebius-def
unit-disc-ﬁx-discI unit-disc-ﬁx-rotation )
thus ?lhs
by auto
qed
qed
