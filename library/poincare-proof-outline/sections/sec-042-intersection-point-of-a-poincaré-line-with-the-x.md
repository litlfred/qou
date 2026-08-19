---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-042-intersection-point-of-a-poincaré-line-with-the-x
section_title: "Intersection point of a Poincaré line with the x-axis in the unit disc"
section_number: null
pages: 101-105
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
deﬁnition calc-x-axis-intersection-cvec :: complex⇒ complex⇒ complex-vec where
[simp]: calc-x-axis-intersection-cvec A B =
(let discr = ( Re B )2− (Re A )2 in
(−Re(B) + sgn (Re B )∗ sqrt(discr), A))
deﬁnition calc-x-axis-intersection-cmat-cvec :: complex-mat⇒ complex-vec where [simp]:
calc-x-axis-intersection-cmat-cvec H =
(let (A, B, C, D) = H in
if A ⁄= 0 then
calc-x-axis-intersection-cvec A B
else
(0, 1 )
)
lift-deﬁnition calc-x-axis-intersection-clmat-hcoords:: circline-mat⇒ complex-homo-coordsis calc-x-axis-intersection-cmat-cvec
by (auto split : if-split-asm)
lift-deﬁnition calc-x-axis-intersection :: circline⇒ complex-homo is calc-x-axis-intersection-clmat-hcoords
proof transfer
ﬁx H1 H2
assume∗: hermitean H1 ∧ H1⁄= mat-zero hermitean H2 ∧ H2⁄= mat-zero
obtain A1 B1 C1 D1 A2 B2 C2 D2 where hh: H1 = ( A1, B1, C1, D1 ) H2 = ( A2, B2, C2, D2 )
by (cases H1, cases H2, auto)
assume circline-eq-cmat H1 H2
then obtain k where k: k⁄= 0 H2 = cor k ∗sm H1
by auto
have calc-x-axis-intersection-cvec A1 B1 ≈v calc-x-axis-intersection-cvec A2 B2
using hh k
apply simp
apply (rule-tac x =cor k in exI )
apply auto
apply (simp add : sgn-mult power-mult-distrib )
apply (subst right-diﬀ-distrib [symmetric])
apply (subst real-sqrt-mult )
101
by (simp add : real-sgn-eq right-diﬀ-distrib )
thus calc-x-axis-intersection-cmat-cvec H1 ≈v
calc-x-axis-intersection-cmat-cvec H2
using hh k
by (auto simp del : calc-x-axis-intersection-cvec-def)
qed
lemma calc-x-axis-intersection-in-unit-disc:
assumes is-poincare-line H intersects-x-axis H
shows calc-x-axis-intersection H ∈ unit-disc
proof (cases is-line H )
case True
thus ?thesis
using assms
unfolding unit-disc-def disc-def
by simp (transfer, transfer, auto simp add : vec-cnj-def )
next
case False
thus ?thesis
using assms
unfolding unit-disc-def disc-def
proof (simp, transfer, transfer)
ﬁx H
assume hh: hermitean H ∧ H⁄= mat-zero
then obtain A B D where∗: H = ( A, B, cnj B, D) is-real A is-real D
using hermitean-elems
by (cases H ) blast
assume is-poincare-line-cmat H
hence∗: H = ( A, B, cnj B, A) is-real A
using∗
by auto
assume¬ circline-A0-cmat H
hence A⁄= 0
using∗
by simp
assume intersects-x-axis-cmat H
hence (Re B )2 > (Re A )2
using∗ ‹A⁄= 0 ›
by (auto simp add : power2-eq-square complex.expand)
hence Re B ⁄= 0
by auto
have Re A⁄= 0
using ‹is-real A› ‹A⁄= 0 ›
by (auto simp add : complex.expand)
have sqrt((Re B )2− (Re A )2) < sqrt((Re B )2)
using ‹Re A⁄= 0 ›
by (subst real-sqrt-less-iﬀ ) auto
also have ... = sgn (Re B )∗ (Re B )
by (smt mult-minus-right nonzero-eq-divide-eq real-sgn-eq real-sqrt-abs )
ﬁnally
have 1 : sqrt((Re B )2− (Re A )2) < sgn (Re B )∗ (Re B )
.
have 2 : ( Re B )2− (Re A )2 < sgn (Re B )∗ (Re B )∗ sqrt((Re B )2− (Re A )2)
using ‹(Re B )2 > (Re A )2›
using mult-strict-right-mono[OF 1, of sqrt ((Re B )2− (Re A )2)]
by simp
have 3 : ( Re B )2− 2∗sgn (Re B )∗Re B∗sqrt((Re B )2− (Re A )2) + ( Re B )2− (Re A )2 < (Re A )2
102
using mult-strict-left-mono[OF 2, of 2 ]
by (simp add : ﬁeld-simps)
have (sgn (Re B ))2 = 1
using ‹Re B ⁄= 0 ›
by (simp add : sgn-if )
hence (−Re B + sgn (Re B )∗ sqrt((Re B )2− (Re A )2))2 < (Re A )2
using ‹(Re B )2 > (Re A )2› 3
by (simp add : power2-diﬀ ﬁeld-simps )
thus in-ocircline-cmat-cvec unit-circle-cmat (calc-x-axis-intersection-cmat-cvec H )
using∗ ‹(Re B )2 > (Re A )2›
by (auto simp add : vec-cnj-def power2-eq-square split : if-split-asm)
qed
qed
lemma calc-x-axis-intersection:
assumes is-poincare-line H and intersects-x-axis H
shows calc-x-axis-intersection H ∈ circline-set H ∩ circline-set x-axis
proof (cases is-line H )
case True
thus ?thesis
using assms
unfolding circline-set-def
by simp (transfer, transfer, auto simp add : vec-cnj-def )
next
case False
thus ?thesis
using assms
unfolding circline-set-def
proof (simp, transfer, transfer)
ﬁx H
assume hh: hermitean H ∧ H⁄= mat-zero
then obtain A B D where∗: H = ( A, B, cnj B, D) is-real A is-real D
using hermitean-elems
by (cases H ) blast
assume is-poincare-line-cmat H
hence∗: H = ( A, B, cnj B, A) is-real A
using∗
by auto
assume¬ circline-A0-cmat H
hence A⁄= 0
using∗
by auto
assume intersects-x-axis-cmat H
hence (Re B )2 > (Re A )2
using∗ ‹A⁄= 0 ›
by (auto simp add : power2-eq-square complex.expand)
hence Re B ⁄= 0
by auto
show on-circline-cmat-cvec H (calc-x-axis-intersection-cmat-cvec H )∧
on-circline-cmat-cvec x-axis-cmat (calc-x-axis-intersection-cmat-cvec H ) ( is ?P1∧ ?P2 )
proof
show on-circline-cmat-cvec H (calc-x-axis-intersection-cmat-cvec H )
proof (cases circline-A0-cmat H )
case True
thus ?thesis
using∗ ‹is-poincare-line-cmat H › ‹intersects-x-axis-cmat H ›
by (simp add : vec-cnj-def )
next
case False
103
let ?x = calc-x-axis-intersection-cvec A B
let ?nom = fst ?x and ?den = snd ?x
have x: ?x = ( ?nom, ?den)
by simp
hence on-circline-cmat-cvec H (calc-x-axis-intersection-cvec A B )
proof (subst∗, subst x, subst on-circline-cmat-cvec-circline-equation)
have (sgn(Re B ))2 = 1
using ‹Re B ⁄= 0 › sgn-pos zero-less-power2 by fastforce
have (sqrt((Re B )2− (Re A )2))2 = ( Re B )2− (Re A )2
using ‹(Re B )2 > (Re A )2›
by simp
have (−(Re B ) + sgn(Re B )∗sqrt((Re B )2− (Re A )2))2 =
(−(Re B ))2 + ( sgn(Re B )∗sqrt((Re B )2− (Re A )2))2− 2∗(Re B )∗sgn(Re B )∗sqrt((Re B )2− (Re A )2)
by (simp add : power2-diﬀ )
also have ... = ( Re B )∗(Re B ) + ( sgn(Re B )∗sqrt((Re B )2− (Re A )2))2− 2∗(Re B )∗sgn(Re B )∗sqrt((Re B )2
− (Re A )2)
by (simp add : power2-eq-square)
also have ... = ( Re B )∗(Re B ) + ( sgn(Re B ))2∗(sqrt((Re B )2− (Re A )2))2− 2∗(Re B )∗sgn(Re B )∗sqrt((Re
B)2− (Re A )2)
by (simp add : power-mult-distrib)
also have ... = ( Re B )∗(Re B ) + ( Re B )2− (Re A )2− 2∗(Re B )∗sgn(Re B )∗sqrt((Re B )2− (Re A )2)
using ‹(sqrt((Re B )2− (Re A )2))2 = ( Re B )2− (Re A )2› ‹(sgn(Re B ))2 = 1 ›
by simp
ﬁnally have (−(Re B ) + sgn(Re B )∗sqrt((Re B )2− (Re A )2))2 =
(Re B )∗(Re B ) + ( Re B )2− (Re A )2− 2∗(Re B )∗sgn(Re B )∗sqrt((Re B )2− (Re A )2)
by simp
have is-real ?nom is-real ?den
using ‹is-real A›
by simp+
hence cnj (?nom) = ?nom cnj (?den) = ?den
by (simp add :eq-cnj-iﬀ-real)+
hence A∗?nom∗(cnj (?nom)) + B∗?den∗(cnj (?nom)) + ( cnj B )∗(cnj (?den))∗?nom + A∗?den∗(cnj (?den))
= A∗?nom∗?nom + B∗?den∗?nom + ( cnj B )∗?den∗?nom + A∗?den∗?den
by auto
also have ... = A∗?nom∗?nom + ( B + ( cnj B ))∗?den∗?nom + A∗?den∗?den
by (simp add :ﬁeld-simps)
also have ... = A∗?nom∗?nom + 2∗(Re B )∗?den∗?nom + A∗?den∗?den
by (simp add :complex-add-cnj)
also have ... = A∗?nom2 + 2∗(Re B )∗?den∗?nom + A∗?den∗?den
by (simp add :power2-eq-square)
also have ... = A∗(−(Re B ) + sgn(Re B )∗sqrt((Re B )2− (Re A )2))2
+ 2∗(Re B )∗A∗(−(Re B ) + sgn(Re B )∗sqrt((Re B )2− (Re A )2)) + A∗A∗A
unfolding calc-x-axis-intersection-cvec-def
by auto
also have ... = A∗((Re B )∗(Re B ) + ( Re B )2− (Re A )2− 2∗(Re B )∗sgn(Re B )∗sqrt((Re B )2− (Re A )2))
+ 2∗(Re B )∗A∗(−(Re B ) + sgn(Re B )∗sqrt((Re B )2− (Re A )2)) + A∗A∗A
using ‹(−(Re B ) + sgn(Re B )∗sqrt((Re B )2− (Re A )2))2 =
(Re B )∗(Re B ) + ( Re B )2− (Re A )2− 2∗(Re B )∗sgn(Re B )∗sqrt((Re B )2− (Re A )2)›
by simp
also have ... = A∗((Re B )∗(Re B ) + ( Re B )2− A2− 2∗(Re B )∗sgn(Re B )∗sqrt((Re B )2− (Re A )2))
+ 2∗(Re B )∗A∗(−(Re B ) + sgn(Re B )∗sqrt((Re B )2− (Re A )2)) + A∗A∗A
using ‹is-real A›
by simp
also have ... = 0
apply (simp add :ﬁeld-simps)
by (simp add : power2-eq-square)
ﬁnally have A∗?nom∗(cnj (?nom)) + B∗?den∗(cnj (?nom)) + ( cnj B )∗(cnj (?den))∗?nom + A∗?den∗(cnj
(?den)) = 0
by simp
thus circline-equation A B (cnj B ) A ?nom ?den
by simp
qed
thus ?thesis
104
using∗ ‹is-poincare-line-cmat H › ‹intersects-x-axis-cmat H ›
by (simp add : vec-cnj-def )
qed
next
show on-circline-cmat-cvec x-axis-cmat (calc-x-axis-intersection-cmat-cvec H )
using∗ ‹is-poincare-line-cmat H › ‹intersects-x-axis-cmat H › ‹is-real A›
using eq-cnj-iﬀ-real[of A ]
by (simp add : vec-cnj-def )
qed
qed
qed
lemma unique-calc-x-axis-intersection:
assumes is-poincare-line H and H⁄= x-axis
assumes x∈ unit-disc and x∈ circline-set H ∩ circline-set x-axis
shows x = calc-x-axis-intersection H
proof−
have∗: intersects-x-axis H
using assms
using intersects-x-axis-iﬀ [OF assms (1 )]
by auto
show x = calc-x-axis-intersection H
using calc-x-axis-intersection[OF assms (1 )∗]
using calc-x-axis-intersection-in-unit-disc[OF assms (1 )∗]
using assms
using unique-is-poincare-line[of x calc-x-axis-intersection H H x-axis ]
by auto
qed
