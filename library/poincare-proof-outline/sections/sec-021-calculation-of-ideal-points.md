---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-021-calculation-of-ideal-points
section_title: "Calculation of ideal points"
section_number: null
pages: 34-39
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
We decided to define ideal points constructively, i.e., we calculate the coordinates of ideal points for a given
h-line explicitly. Namely, if the h-line is determined by A and B, the two intersection points are

ee (-A+i- ViBP - a) .

definition calc-ideal-point1-cvec :: complex = complex = complez-vec where
[simp]: calc-ideal-point1-cvec A B =
(let diser = Re ((emod B)? — (Re A)*) in
(Bx(—A — ixsqrt(discr)), (emod B)*))

definition calc-ideal-point2-cvec :: complex = complex = compler-vec where
[simp]: calc-ideal-point2-cvec A B =
(let diser = Re ((emod B)? — (Re A)*) in
(Bx(—A + iksgrt(discr)), (emod B)*))

definition calc-ideal-points-cmat-cvec :: complex-mat = complez-vec set where
[simp]: calc-ideal-points-cmat-cvec H =
(if is-poincare-line-cmat H then
let (A, B, C, D) = H
in {calc-ideal-point1-cvec A B, calc-ideal-point2-cvec A B}
else

{(-1, 1), @, DY)

lift-definition calc-ideal-points-clmat-hcoords :: circline-mat = complet-homo-coords set is calc-ideal-points-cmat-cvec
by (auto simp add: Let-def split: if-split-asm)

lift-definition calc-ideal-points :: circline = complex-homo set is calc-ideal-points-clmat-hcoords
proof transfer
fix H1 H2
assume hh: hermitean H1 A H1 4 mat-zero hermitean H2 \ H2 # mat-zero
obtain Ai B1 C1 D1 A2 B2 C2 D2 where *: H1 = (A1, B1, C1, D1) H2 = (A2, B2, C2, D2)
by (cases H1, cases H2, auto)
assume circline-eq-cmat H1 H2
then obtain k where k: k # 0 H2 = cork *sm H1
by auto
thus rel-set (~,) (calc-ideal-points-cmat-cvec H1) (calc-ideal-points-cmat-cvec H2)
proof (cases is-poincare-line-cmat H1)
case True
hence is-poincare-line-cmat H2
using k * hermitean-mult-real[of H1 k] hh
by (auto simp add: power2-eq-square norm-mult)
have ««: sqrt (\k| * cmod B1 * (|\k| * cmod B1) — k * Re D1 * (k * Re D1)) =
|k| * sqrt(emod B1 * cmod B1 — Re D1 * Re D1)
proof —
have |k| * cmod B1 * (|k| * cmod B1) — k * Re D1 * (k * Re D1) =
k? * (cmod B1 * cmod B1 — Re D1 * Re D1)
by (simp add: power2-eq-square field-simps)
thus ?thesis
by (simp add: real-sqrt-mult)
qed
show ?thesis
using <is-poincare-line-cmat H1» <is-poincare-line-cmat H2>
using * k
apply (simp add: Let-def)
apply safe
apply (simp add: power2-eq-square rel-set-def norm-mult)
apply safe
apply (cases k > 0)
apply (rule-tac r=(cor k)? in ezl)
apply (subst **«)

apply (simp add: power2-eq-square field-simps)

apply (erule notE, rule-tac r=(cor k)? in eal)
(

apply (subst **)
apply (simp add: power2-eq-square field-simps)
apply (cases k > 0)
apply (erule notE, rule-tac x=(cor k)? in ex!)
apply (subst **)
apply (simp add: power2-eq-square field-simps)
apply (rule-tac r=(cor k)? in ez)

(

apply (subst **)
apply (simp add: power2-eq-square field-simps)
apply (cases k > 0)
apply (rule-tac =(cor k)? in ez!)
apply (subst **)
apply (simp add: power2-eq-square field-simps)
apply (erule notE, rule-tac r=(cor k)? in ezl)
apply (subst **)
apply (simp add: power2-eq-square field-simps)
apply (rule-tac =(cor k)* in ex!)
apply (cases k > 0)
apply (erule notE, rule-tac r=(cor k)? in ezl)
apply (subst **)
apply (simp add: power2-eq-square field-simps)
apply (subst «*)
apply (simp add: power2-eq-square field-simps)
done
next
case False
hence — is-poincare-line-cmat H2
using k * hermitean-mult-real[of H1 k] hh
by (auto simp add: power2-eq-square norm-mult)
have rel-set (~,) {(— 1, 1), (1, 1)} {(- 1, 1), (4, 1)}
by (simp add: rel-set-def)
thus ?thesis
using <- is-poincare-line-cmat H1) ‘- is-poincare-line-cmat H2»
using *
by (auto simp add: Let-def)
qed
qed

Correctness of the calculation

We show that for every h-line its two calculated ideal points are different and are on the intersection of that
line and the unit circle.

Calculated ideal points are on the unit circle

lemma calc-ideal-point-1-unit:
assumes is-real A (cmod B)? > (cmod A)?
assumes (21, 22) = calc-ideal-point1-cvec A B
shows z1 * cnj z1 = 22 * cnj 22
proof—
let ?discr = Re ((cmod B)? — (Re A)?)
have ?discr > 0
using assms
by (simp add: cmod-power2)
have (Bx(—A — ixsqrt(?discr))) * cnj (Bx(—A — ixsgrt(?discr))) = (B * cnj B) * (A? + cor (abs ?discr))
using <is-real Ay eq-cnj-iff-real|of A]
by (simp add: field-simps power2-eq-square)
also have ... = (B * cnj B) * (emod B)?
using <?discr > 0»
using assms
using comples-of-real-Re[of (cmod B)? — (Re A)?| complez-of-real-Re[of A] <is-real A»
by (simp add: power2-eq-square)
also have ... = (cmod B)? * cnj ((cmod B)?)
using complez-cnj-complez-of-real complez-mult-cnj-cmod

by presburger
finally show ?thesis
using assms
by simp
qed

lemma calc-ideal-point-2-unit:
assumes is-real A (cmod B)? > (cmod A)?
assumes (21, 22) = calc-ideal-point2-cvec A B
shows z1 * cnj z1 = 22 * cnj 22
proof—
let ?discr = Re ((cmod B)? — (Re A)?)
have ?discr > 0
using assms
by (simp add: cmod-power2)
have (Bx(—A + ixsgrt(?discr))) « enj (Bx(—A + ixsgrt(?discr))) = (B * cnj B) * (A? + cor (abs ?discr))
using <is-real Ay eq-cnj-iff-real|of A]
by (simp add: field-simps power2-eq-square)
also have ... = (B * cnj B) * (emod B)?
using <?discr > 0»
using assms
using comple-of-real-Re[of (cmod B)? — (Re A)?| complez-of-real-Re[of A] <is-real A»
by (simp add: power2-eq-square)
also have ... = (cmod B)? * cnj ((cmod B)?)
using complez-cnj-complez-of-real complez-mult-cnj-cmod
by presburger
finally show ?thesis
using assms
by simp
qed

lemma calc-ideal-points-on-unit-circle:
shows V z € calc-ideal-points H. z € circline-set unit-circle
unfolding circline-set-def
apply simp
proof (transfer, transfer)
fix H
assume hh: hermitean H \ H # mat-zero
obtain A B C D where «: H = (A, B, C, D)
by (cases H, auto)
have V (z1, 22) € calc-ideal-points-cmat-cvec H. 21 * cnj 21 = 22 * cnj 22
using hermitean-elems|of A B C D|
unfolding calc-ideal-points-cmat-cvec-def
using calc-ideal-point-1-unit[of A B]
using calc-ideal-point-2-unit[of A B]
using hh *
apply (cases calc-ideal-point1-cvec A B, cases calc-ideal-point2-cvec A B)
apply (auto simp add: Let-def simp del: calc-ideal-point1-cvec-def calc-ideal-point2-cvec-def )
done
thus Ball (calc-ideal-points-cmat-cvec H) (on-circline-cmat-cvec unit-circle-cmat)
using on-circline-cmat-cvec-unit
by (auto simp del: on-circline-cmat-cvec-def calc-ideal-points-cmat-cvec-def )
qed

Calculated ideal points are on the h-line

lemma calc-ideal-point1-sq:
assumes (21, 22) = calc-ideal-point1-cvec A B is-real A (cmod B)* > (emod A)?
shows 21 * cnj zl + 22 * cnj z2 = 2 * (B * cnj B)?
proof—
let ?discr = Re ((emod B)? — (Re A)?)
have ?discr > 0
using assms
by (simp add: cmod-power2)
have z1 * cnj zl = (B * cnj B) * (—A + ixsqrt(?discr))*(—A — ixsqrt( ?discr))
using assms eq-cnj-iff-real[of A]
by (simp)
also have ... = (B * cnj B) x (A? + ?discr)
using complez-of-real-Re[of A] <is-real Ay «?discr > 0»
by (simp add: power2-eq-square field-simps)

finally

have z1 * cnj z1 = (B * cnj B)?
using comples-of-real-Re[of (emod B)? — (Re A)?| complez-of-real-Re[of A] <is-real A»
using complez-mult-cnj-cmod|of B]
by (simp add: power2-eq-square)

moreover

have 22 * cnj 22 = (B * cnj B)?
using assms
by simp

ultimately

show ?thesis
by simp

qed

lemma calc-ideal-point2-sq:
assumes (21, 22) = calc-ideal-point2-cvec A B is-real A (cmod B)* > (cmod A)?
shows 21 * cnj zl + 22 * cnj 22 = 2 * (B * cnj B)?
proof—
let ?discr = Re ((cmod B)? — (Re A)?)
have ?discr > 0
using assms
by (simp add: cmod-power2)
have z1 * cnj zl = (B * cnj B) * (—A + ixsqrt(?discr))*(—A — ixsqrt( ?discr))
using assms eq-cnj-iff-real[of A]
by simp
also have ... = (B * cnj B) x (A? + ?discr)
using complez-of-real-Re[of A] <is-real Ay «?discr > 0»
by (simp add: power2-eq-square field-simps)
finally
have z1 * cnj z1 = (B * cnj B)?
using complez-of-real-Re[of (cmod B)? — (Re A)*] complez-of-real-Re[of A] <is-real Ay
using complez-mult-cnj-cmod|of B]
by (simp add: power2-eq-square)
moreover
have 22 * cnj 22 = (B * cnj B)?
using assms
by simp
ultimately
show ?thesis
by simp
qed

lemma calc-ideal-point1-miz:
assumes (21, 22) = calc-ideal-point1-cvec A B is-real A (cmod B)* > (emod A)?
shows B * cnj z1 * 22 + cnj B* z1 * cnj 22 = — 2 * A * (B * cnj B)?
proof—
have Bxcnj z1 + cnj Bxzl = —2*xA*xBxcnj B
using assms eq-cnj-iff-real[of A]
by (simp, simp add: field-simps)
moreover
have cnj z2 = 22
using assms
by simp
hence Bxcnj z1*z2 + cnj Bxz1*cnj 22 = (Bxcnj 21 + cnj Bxz1)*z2
by (simp add: field-simps)

ultimately

have Bxcnj z1*z2 + cnj Bxzl*cnj 22 = —2*Ax(Bx cnj B)xz2
by simp

also have ... = —2*Ax(B * cnj B)?

using assms

using complez-mult-cnj-cmod|of B]

by (simp add: power2-eq-square)
finally
show ?thesis
qed

lemma calc-ideal-point2-mia:
assumes (21, 22) = calc-ideal-point2-cvec A B is-real A (cmod B)* > (emod A)?
shows B * cnj z1 * 22 + cnj B* z1 * cnj 22 = — 2 * A * (B * cnj B)?
proof—
have Bxcnj z1 + cnj Bxzl = —2*xA*xBxcnj B
using assms eq-cnj-iff-real[of A]
by (simp, simp add: field-simps)
moreover
have cnj z2 = 22
using assms
by simp
hence Bxcnj z1*z2 + cnj Bxz1*cnj 22 = (Bxcnj 21 + cnj Bxz1)*z2
by (simp add: field-simps)

ultimately

have Bxcnj z1*z2 + cnj Bxzl*cnj 22 = —2*Ax(Bx cnj B)xz2
by simp

also have ... = —2*A*(B * cnj B)?

using assms
using complez-mult-cnj-cmod|of B]
by (simp add: power2-eq-square)
finally
show ?thesis

qed

lemma calc-ideal-point1-on-circline:
assumes (21, 22) = calc-ideal-point1-cvec A B is-real A (cmod B)* > (cmod A)?
shows Axz1xcnj z1 + Bxenj z1*z2 + cnj Bxz1*cnj 22 + Axz2xcnj z2 = 0 (is ?lhs = 0)
proof—
have ?lhs = A « (z1 * enj zl + 22 * cnj 22) + (B * cnj 21 * 22 + cnj B x 21 * cnj 22)
by (simp add: field-simps)
also have ... = 2*A«(Benj B)? + (—2xA*(Bxenj B)?)
using calc-ideal-point1-sq|OF assms]
using calc-ideal-point1-mix|OF assms]
by simp
finally
show ?thesis
by simp
qed

lemma calc-ideal-point2-on-circline:
assumes (21, 22) = calc-ideal-point2-cvec A B is-real A (cmod B)* > (emod A)?
shows Axz1xcnj z1 + Bxenj z1*z2 + cnj Bxz1*cnj 22 + Axz2xcnj z2 = 0 (is ?lhs = 0)
proof—
have ?lhs = A « (z1 * enj zl + 22 * cnj 22) + (B * cnj 21 * 22 + cnj B x 21 * cnj 22)
by (simp add: field-simps)
also have ... = 2*A*(Bxcnj B)? + (—2*Ax*(Bxcnj B)*)
using calc-ideal-point2-sq|OF assms]
using calc-ideal-point2-mix|OF assms]
by simp
finally
show ?thesis
by simp
qed

lemma calc-ideal-points-on-circline:
assumes is-poincare-line H
shows V z € calc-ideal-points H. z € circline-set H
using assms
unfolding circline-set-def
apply simp
proof (transfer, transfer)
fix H

assume hh: hermitean H \ H # mat-zero

obtain A B C D where «: H = (A, B, C, D)
by (cases H, auto)

obtain 211 212 z21 222 where +x: (z11, z12) = calc-ideal-point1-cvec A B (221, 222) = calc-ideal-point2-cvec A B
by (cases calc-ideal-point1-cvec A B, cases calc-ideal-point2-cvec A B) auto

assume is-poincare-line-cmat H
hence V (z1, 22) € calc-ideal-points-cmat-cvec H. Axz1*cnj z1 + Bxenj z1*2z2 + Cxz1x*cnj 22 + Dxz2xcnj 22 = 0
using * ** hh
using hermitean-elems|of A B C D|
using calc-ideal-point1-on-circline[of 211 z12 A B|
using calc-ideal-point2-on-circline[of 221 z22 A B|
by (auto simp del: calc-ideal-point1-cvec-def calc-ideal-point2-cvec-def )
thus Ball (calc-ideal-points-cmat-cvec H) (on-circline-cmat-cvec H)
using on-circline-cmat-cvec-circline-equation *
by (auto simp del: on-circline-cmat-cvec-def calc-ideal-points-cmat-cvec-def simp add: field-simps)
qed
