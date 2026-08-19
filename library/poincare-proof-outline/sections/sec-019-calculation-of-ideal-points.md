---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-019-calculation-of-ideal-points
section_title: "Calculation of ideal points"
section_number: null
pages: 34-39
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
We decided to deﬁne ideal points constructively, i.e., we calculate the coordinates of ideal points for a given
h-line explicitly. Namely, if the h-line is determined by A and B, the two intersection points are
B
|B|2
(
−A ±i ·
√
|B|2 −A2
)
.
deﬁnition calc-ideal-point1-cvec :: complex⇒ complex⇒ complex-vec where
[simp]: calc-ideal-point1-cvec A B =
(let discr = Re ((cmod B )2− (Re A )2) in
(B∗(−A− i∗sqrt(discr)), (cmod B )2))
deﬁnition calc-ideal-point2-cvec :: complex⇒ complex⇒ complex-vec where
[simp]: calc-ideal-point2-cvec A B =
(let discr = Re ((cmod B )2− (Re A )2) in
(B∗(−A + i∗sqrt(discr)), (cmod B )2))
deﬁnition calc-ideal-points-cmat-cvec :: complex-mat⇒ complex-vec set where
[simp]: calc-ideal-points-cmat-cvec H =
(if is-poincare-line-cmat H then
let (A, B, C, D) = H
in{calc-ideal-point1-cvec A B, calc-ideal-point2-cvec A B}
else
{(−1, 1 ), (1, 1 )})
lift-deﬁnition calc-ideal-points-clmat-hcoords :: circline-mat⇒ complex-homo-coords set is calc-ideal-points-cmat-cvec
by (auto simp add : Let-def split : if-split-asm)
lift-deﬁnition calc-ideal-points :: circline⇒ complex-homo set is calc-ideal-points-clmat-hcoords
proof transfer
ﬁx H1 H2
assume hh: hermitean H1 ∧ H1⁄= mat-zero hermitean H2 ∧ H2⁄= mat-zero
obtain A1 B1 C1 D1 A2 B2 C2 D2 where∗: H1 = ( A1, B1, C1, D1 ) H2 = ( A2, B2, C2, D2 )
by (cases H1, cases H2, auto)
assume circline-eq-cmat H1 H2
then obtain k where k: k⁄= 0 H2 = cor k ∗sm H1
by auto
thus rel-set (≈v) ( calc-ideal-points-cmat-cvec H1 ) ( calc-ideal-points-cmat-cvec H2 )
proof (cases is-poincare-line-cmat H1 )
case True
hence is-poincare-line-cmat H2
using k∗ hermitean-mult-real[of H1 k ] hh
by (auto simp add : power2-eq-square norm-mult)
have∗∗: sqrt (|k|∗ cmod B1 ∗ (|k|∗ cmod B1 )− k∗ Re D1 ∗ (k∗ Re D1 )) =
|k|∗ sqrt(cmod B1 ∗ cmod B1 − Re D1 ∗ Re D1 )
proof−
have|k|∗ cmod B1 ∗ (|k|∗ cmod B1 )− k∗ Re D1 ∗ (k∗ Re D1 ) =
k 2∗ (cmod B1 ∗ cmod B1 − Re D1 ∗ Re D1 )
by (simp add : power2-eq-square ﬁeld-simps)
thus ?thesis
by (simp add : real-sqrt-mult)
qed
show ?thesis
using ‹is-poincare-line-cmat H1 › ‹is-poincare-line-cmat H2 ›
using∗ k
apply (simp add : Let-def )
apply safe
apply (simp add : power2-eq-square rel-set-def norm-mult )
apply safe
apply (cases k > 0 )
apply (rule-tac x =(cor k )2 in exI )
34
apply (subst∗∗)
apply (simp add : power2-eq-square ﬁeld-simps)
apply (erule notE, rule-tac x =(cor k )2 in exI )
apply (subst∗∗)
apply (simp add : power2-eq-square ﬁeld-simps)
apply (cases k > 0 )
apply (erule notE, rule-tac x =(cor k )2 in exI )
apply (subst∗∗)
apply (simp add : power2-eq-square ﬁeld-simps)
apply (rule-tac x =(cor k )2 in exI )
apply (subst∗∗)
apply (simp add : power2-eq-square ﬁeld-simps)
apply (cases k > 0 )
apply (rule-tac x =(cor k )2 in exI )
apply (subst∗∗)
apply (simp add : power2-eq-square ﬁeld-simps)
apply (erule notE, rule-tac x =(cor k )2 in exI )
apply (subst∗∗)
apply (simp add : power2-eq-square ﬁeld-simps)
apply (rule-tac x =(cor k )2 in exI )
apply (cases k > 0 )
apply (erule notE, rule-tac x =(cor k )2 in exI )
apply (subst∗∗)
apply (simp add : power2-eq-square ﬁeld-simps)
apply (subst∗∗)
apply (simp add : power2-eq-square ﬁeld-simps)
done
next
case False
hence¬ is-poincare-line-cmat H2
using k∗ hermitean-mult-real[of H1 k ] hh
by (auto simp add : power2-eq-square norm-mult)
have rel-set (≈v){(− 1, 1 ), (1, 1 )}{ (− 1, 1 ), (1, 1 )}
by (simp add : rel-set-def )
thus ?thesis
using ‹¬ is-poincare-line-cmat H1 › ‹¬ is-poincare-line-cmat H2 ›
using∗
by (auto simp add : Let-def )
qed
qed
Correctness of the calculation
We show that for every h-line its two calculated ideal points are diﬀerent and are on the intersection of that
line and the unit circle.
Calculated ideal points are on the unit circle
lemma calc-ideal-point-1-unit:
assumes is-real A (cmod B )2 > (cmod A )2
assumes (z1, z2 ) = calc-ideal-point1-cvec A B
shows z1∗ cnj z1 = z2∗ cnj z2
proof−
let ?discr = Re ((cmod B )2− (Re A )2)
have ?discr > 0
using assms
by (simp add : cmod-power2)
have (B∗(−A− i∗sqrt(?discr)))∗ cnj (B∗(−A− i∗sqrt(?discr))) = ( B∗ cnj B )∗ (A2 + cor (abs ?discr ))
using ‹is-real A› eq-cnj-iﬀ-real[of A ]
by (simp add : ﬁeld-simps power2-eq-square)
also have ... = ( B∗ cnj B )∗ (cmod B )2
using ‹?discr > 0 ›
using assms
using complex-of-real-Re[of (cmod B )2− (Re A )2] complex-of-real-Re[of A ] ‹is-real A›
by (simp add : power2-eq-square)
also have ... = ( cmod B )2∗ cnj ((cmod B )2)
using complex-cnj-complex-of-real complex-mult-cnj-cmod
35
by presburger
ﬁnally show ?thesis
using assms
by simp
qed
lemma calc-ideal-point-2-unit:
assumes is-real A (cmod B )2 > (cmod A )2
assumes (z1, z2 ) = calc-ideal-point2-cvec A B
shows z1∗ cnj z1 = z2∗ cnj z2
proof−
let ?discr = Re ((cmod B )2− (Re A )2)
have ?discr > 0
using assms
by (simp add : cmod-power2)
have (B∗(−A + i∗sqrt(?discr)))∗ cnj (B∗(−A + i∗sqrt(?discr))) = ( B∗ cnj B )∗ (A2 + cor (abs ?discr ))
using ‹is-real A› eq-cnj-iﬀ-real[of A ]
by (simp add : ﬁeld-simps power2-eq-square)
also have ... = ( B∗ cnj B )∗ (cmod B )2
using ‹?discr > 0 ›
using assms
using complex-of-real-Re[of (cmod B )2− (Re A )2] complex-of-real-Re[of A ] ‹is-real A›
by (simp add : power2-eq-square)
also have ... = ( cmod B )2∗ cnj ((cmod B )2)
using complex-cnj-complex-of-real complex-mult-cnj-cmod
by presburger
ﬁnally show ?thesis
using assms
by simp
qed
lemma calc-ideal-points-on-unit-circle:
shows∀ z∈ calc-ideal-points H. z∈ circline-set unit-circle
unfolding circline-set-def
apply simp
proof (transfer, transfer)
ﬁx H
assume hh: hermitean H ∧ H⁄= mat-zero
obtain A B C D where∗: H = ( A, B, C, D)
by (cases H, auto)
have∀ (z1, z2 )∈ calc-ideal-points-cmat-cvec H. z1∗ cnj z1 = z2∗ cnj z2
using hermitean-elems[of A B C D ]
unfolding calc-ideal-points-cmat-cvec-def
using calc-ideal-point-1-unit[of A B ]
using calc-ideal-point-2-unit[of A B ]
using hh∗
apply (cases calc-ideal-point1-cvec A B, cases calc-ideal-point2-cvec A B )
apply (auto simp add : Let-def simp del : calc-ideal-point1-cvec-def calc-ideal-point2-cvec-def)
done
thus Ball (calc-ideal-points-cmat-cvec H) ( on-circline-cmat-cvec unit-circle-cmat)
using on-circline-cmat-cvec-unit
by (auto simp del : on-circline-cmat-cvec-def calc-ideal-points-cmat-cvec-def)
qed
Calculated ideal points are on the h-line
lemma calc-ideal-point1-sq:
assumes (z1, z2 ) = calc-ideal-point1-cvec A B is-real A (cmod B )2 > (cmod A )2
shows z1∗ cnj z1 + z2∗ cnj z2 = 2∗ (B∗ cnj B )2
proof−
let ?discr = Re ((cmod B )2− (Re A )2)
have ?discr > 0
using assms
by (simp add : cmod-power2)
have z1∗ cnj z1 = ( B∗ cnj B )∗ (−A + i∗sqrt(?discr))∗(−A− i∗sqrt(?discr))
using assms eq-cnj-iﬀ-real [of A ]
by (simp)
36
also have ... = ( B∗ cnj B )∗ (A2 + ?discr)
using complex-of-real-Re[of A ] ‹is-real A› ‹?discr > 0 ›
by (simp add : power2-eq-square ﬁeld-simps)
ﬁnally
have z1∗ cnj z1 = ( B∗ cnj B )2
using complex-of-real-Re[of (cmod B )2− (Re A )2] complex-of-real-Re[of A ] ‹is-real A›
using complex-mult-cnj-cmod[of B ]
by (simp add : power2-eq-square)
moreover
have z2∗ cnj z2 = ( B∗ cnj B )2
using assms
by simp
ultimately
show ?thesis
by simp
qed
lemma calc-ideal-point2-sq:
assumes (z1, z2 ) = calc-ideal-point2-cvec A B is-real A (cmod B )2 > (cmod A )2
shows z1∗ cnj z1 + z2∗ cnj z2 = 2∗ (B∗ cnj B )2
proof−
let ?discr = Re ((cmod B )2− (Re A )2)
have ?discr > 0
using assms
by (simp add : cmod-power2)
have z1∗ cnj z1 = ( B∗ cnj B )∗ (−A + i∗sqrt(?discr))∗(−A− i∗sqrt(?discr))
using assms eq-cnj-iﬀ-real [of A ]
by simp
also have ... = ( B∗ cnj B )∗ (A2 + ?discr)
using complex-of-real-Re[of A ] ‹is-real A› ‹?discr > 0 ›
by (simp add : power2-eq-square ﬁeld-simps)
ﬁnally
have z1∗ cnj z1 = ( B∗ cnj B )2
using complex-of-real-Re[of (cmod B )2− (Re A )2] complex-of-real-Re[of A ] ‹is-real A›
using complex-mult-cnj-cmod[of B ]
by (simp add : power2-eq-square)
moreover
have z2∗ cnj z2 = ( B∗ cnj B )2
using assms
by simp
ultimately
show ?thesis
by simp
qed
lemma calc-ideal-point1-mix:
assumes (z1, z2 ) = calc-ideal-point1-cvec A B is-real A (cmod B )2 > (cmod A )2
shows B∗ cnj z1 ∗ z2 + cnj B ∗ z1∗ cnj z2 =− 2∗ A∗ (B∗ cnj B )2
proof−
have B∗cnj z1 + cnj B∗z1 =−2∗A∗B∗cnj B
using assms eq-cnj-iﬀ-real [of A ]
by (simp, simp add : ﬁeld-simps)
moreover
have cnj z2 = z2
using assms
by simp
hence B∗cnj z1∗z2 + cnj B∗z1∗cnj z2 = ( B∗cnj z1 + cnj B∗z1 )∗z2
by (simp add : ﬁeld-simps)
ultimately
have B∗cnj z1∗z2 + cnj B∗z1∗cnj z2 =−2∗A∗(B∗ cnj B )∗z2
by simp
also have ... =−2∗A∗(B∗ cnj B )2
using assms
using complex-mult-cnj-cmod[of B ]
by (simp add : power2-eq-square)
ﬁnally
37
show ?thesis
.
qed
lemma calc-ideal-point2-mix:
assumes (z1, z2 ) = calc-ideal-point2-cvec A B is-real A (cmod B )2 > (cmod A )2
shows B∗ cnj z1 ∗ z2 + cnj B ∗ z1∗ cnj z2 =− 2∗ A∗ (B∗ cnj B )2
proof−
have B∗cnj z1 + cnj B∗z1 =−2∗A∗B∗cnj B
using assms eq-cnj-iﬀ-real [of A ]
by (simp, simp add : ﬁeld-simps)
moreover
have cnj z2 = z2
using assms
by simp
hence B∗cnj z1∗z2 + cnj B∗z1∗cnj z2 = ( B∗cnj z1 + cnj B∗z1 )∗z2
by (simp add : ﬁeld-simps)
ultimately
have B∗cnj z1∗z2 + cnj B∗z1∗cnj z2 =−2∗A∗(B∗ cnj B )∗z2
by simp
also have ... =−2∗A∗(B∗ cnj B )2
using assms
using complex-mult-cnj-cmod[of B ]
by (simp add : power2-eq-square)
ﬁnally
show ?thesis
.
qed
lemma calc-ideal-point1-on-circline:
assumes (z1, z2 ) = calc-ideal-point1-cvec A B is-real A (cmod B )2 > (cmod A )2
shows A∗z1∗cnj z1 + B∗cnj z1∗z2 + cnj B∗z1∗cnj z2 + A∗z2∗cnj z2 = 0 (is ?lhs = 0 )
proof−
have ?lhs = A∗ (z1∗ cnj z1 + z2∗ cnj z2 ) + ( B∗ cnj z1 ∗ z2 + cnj B ∗ z1∗ cnj z2 )
by (simp add : ﬁeld-simps)
also have ... = 2∗A∗(B∗cnj B )2 + (−2∗A∗(B∗cnj B )2)
using calc-ideal-point1-sq[OF assms ]
using calc-ideal-point1-mix[OF assms ]
by simp
ﬁnally
show ?thesis
by simp
qed
lemma calc-ideal-point2-on-circline:
assumes (z1, z2 ) = calc-ideal-point2-cvec A B is-real A (cmod B )2 > (cmod A )2
shows A∗z1∗cnj z1 + B∗cnj z1∗z2 + cnj B∗z1∗cnj z2 + A∗z2∗cnj z2 = 0 (is ?lhs = 0 )
proof−
have ?lhs = A∗ (z1∗ cnj z1 + z2∗ cnj z2 ) + ( B∗ cnj z1 ∗ z2 + cnj B ∗ z1∗ cnj z2 )
by (simp add : ﬁeld-simps)
also have ... = 2∗A∗(B∗cnj B )2 + (−2∗A∗(B∗cnj B )2)
using calc-ideal-point2-sq[OF assms ]
using calc-ideal-point2-mix[OF assms ]
by simp
ﬁnally
show ?thesis
by simp
qed
lemma calc-ideal-points-on-circline:
assumes is-poincare-line H
shows∀ z∈ calc-ideal-points H. z∈ circline-set H
using assms
unfolding circline-set-def
apply simp
proof (transfer, transfer)
38
ﬁx H
assume hh: hermitean H ∧ H⁄= mat-zero
obtain A B C D where∗: H = ( A, B, C, D)
by (cases H, auto)
obtain z11 z12 z21 z22 where∗∗: ( z11, z12 ) = calc-ideal-point1-cvec A B (z21, z22 ) = calc-ideal-point2-cvec A B
by (cases calc-ideal-point1-cvec A B, cases calc-ideal-point2-cvec A B ) auto
assume is-poincare-line-cmat H
hence∀ (z1, z2 )∈ calc-ideal-points-cmat-cvec H. A∗z1∗cnj z1 + B∗cnj z1∗z2 + C∗z1∗cnj z2 + D∗z2∗cnj z2 = 0
using∗∗∗ hh
using hermitean-elems[of A B C D ]
using calc-ideal-point1-on-circline[of z11 z12 A B ]
using calc-ideal-point2-on-circline[of z21 z22 A B ]
by (auto simp del : calc-ideal-point1-cvec-def calc-ideal-point2-cvec-def)
thus Ball (calc-ideal-points-cmat-cvec H) ( on-circline-cmat-cvec H )
using on-circline-cmat-cvec-circline-equation∗
by (auto simp del : on-circline-cmat-cvec-def calc-ideal-points-cmat-cvec-def simp add : ﬁeld-simps)
qed
