---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-020-ideal-points
section_title: "Ideal points"
section_number: null
pages: 39-44
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma calc-ideal-points-cvec-diﬀerent [simp]:
assumes (cmod B )2 > (cmod A )2 is-real A
shows¬ (calc-ideal-point1-cvec A B ≈v calc-ideal-point2-cvec A B )
using assms
by (auto) ( auto simp add : cmod-def )
lemma calc-ideal-points-diﬀerent:
assumes is-poincare-line H
shows ∃ i1∈ (calc-ideal-points H ).∃ i2∈ (calc-ideal-points H ). i1⁄= i2
using assms
proof (transfer, transfer)
ﬁx H
assume hh: hermitean H ∧ H⁄= mat-zero is-poincare-line-cmat H
obtain A B C D where∗: H = ( A, B, C, D)
by (cases H, auto)
hence is-real A using hh hermitean-elems by auto
thus∃ i1∈calc-ideal-points-cmat-cvec H.∃ i2∈calc-ideal-points-cmat-cvec H.¬ i1≈v i2
using∗ hh calc-ideal-points-cvec-diﬀerent[of A B ]
apply (rule-tac x =calc-ideal-point1-cvec A B in bexI)
apply (rule-tac x =calc-ideal-point2-cvec A B in bexI)
by auto
qed
lemma two-calc-ideal-points [simp]:
assumes is-poincare-line H
shows card (calc-ideal-points H ) = 2
proof−
have ∃ x∈ calc-ideal-points H.∃ y∈ calc-ideal-points H.∀ z∈ calc-ideal-points H. z = x∨ z = y
by (transfer, transfer, case-tac H, simp del : calc-ideal-point1-cvec-def calc-ideal-point2-cvec-def)
then obtain x y where∗: calc-ideal-points H ={x, y}
by auto
moreover
have x⁄= y
using calc-ideal-points-diﬀerent[OF assms ]∗
by auto
ultimately
show ?thesis
by auto
qed
4.3.2 Ideal points
Next we give a genuine deﬁnition of ideal points – these are the intersections of the h-line with the unit circle
deﬁnition ideal-points :: circline⇒ complex-homo set where
ideal-points H = circline-intersection H unit-circle
39
Ideal points are on the unit circle and on the h-line
lemma ideal-points-on-unit-circle:
shows∀ z∈ ideal-points H. z∈ circline-set unit-circle
unfolding ideal-points-def circline-intersection-def circline-set-def
by simp
lemma ideal-points-on-circline:
shows∀ z∈ ideal-points H. z∈ circline-set H
unfolding ideal-points-def circline-intersection-def circline-set-def
by simp
For each h-line there are exactly two ideal points
lemma two-ideal-points:
assumes is-poincare-line H
shows card (ideal-points H ) = 2
proof−
have H⁄= unit-circle
using assms not-is-poincare-line-unit-circle
by auto
let ?int = circline-intersection H unit-circle
obtain i1 i2 where i1∈ ?int i2 ∈ ?int i1 ⁄= i2
using calc-ideal-points-on-circline[OF assms ]
using calc-ideal-points-on-unit-circle[of H ]
using calc-ideal-points-diﬀerent[OF assms ]
unfolding circline-intersection-def circline-set-def
by auto
thus ?thesis
unfolding ideal-points-def
using circline-intersection-at-most-2-points[OF ‹H⁄= unit-circle›]
using card-geq-2-iﬀ-contains-2-elems[of ?int ]
by auto
qed
They are exactly the two points that our calculation ﬁnds
lemma ideal-points-unique:
assumes is-poincare-line H
shows ideal-points H = calc-ideal-points H
proof−
have calc-ideal-points H ⊆ ideal-points H
using calc-ideal-points-on-circline[OF assms ]
using calc-ideal-points-on-unit-circle[of H ]
unfolding ideal-points-def circline-intersection-def circline-set-def
by auto
moreover
have H⁄= unit-circle
using not-is-poincare-line-unit-circle assms
by auto
hence ﬁnite (ideal-points H )
using circline-intersection-at-most-2-points[of H unit-circle ]
unfolding ideal-points-def
by auto
ultimately
show ?thesis
using card-subset-eq[of ideal-points H calc-ideal-points H ]
using two-calc-ideal-points[OF assms ]
using two-ideal-points[OF assms ]
by auto
qed
For each h-line we can obtain two diﬀerent ideal points
lemma obtain-ideal-points:
assumes is-poincare-line H
obtains i1 i2 where i1⁄= i2 ideal-points H ={i1, i2}
using two-ideal-points[OF assms ] card-eq-2-iﬀ-doubleton[of ideal-points H ]
by blast
40
Ideal points of each h-line constructed from two points in the disc are diﬀerent than those two points
lemma ideal-points-diﬀerent:
assumes u∈ unit-disc v ∈ unit-disc u ⁄= v
assumes ideal-points (poincare-line u v ) = {i1, i2}
shows i1⁄= i2 u ⁄= i1 u ⁄= i2 v ⁄= i1 v ⁄= i2
proof−
have i1∈ ocircline-set ounit-circle i2 ∈ ocircline-set ounit-circle
using assms(3 ) assms(4 ) ideal-points-on-unit-circle is-poincare-line-poincare-line
by fastforce+
thus u⁄= i1 u ⁄= i2 v ⁄= i1 v ⁄= i2
using assms(1−2 )
using disc-inter-ocircline-set[of ounit-circle ]
unfolding unit-disc-def
by auto
show i1⁄= i2
using assms
by (metis doubleton-eq-iﬀ is-poincare-line-poincare-line obtain-ideal-points )
qed
H-line is uniquely determined by its ideal points
lemma ideal-points-line-unique:
assumes is-poincare-line H ideal-points H ={i1, i2}
shows H = poincare-line i1 i2
by (smt assms (1 ) assms(2 ) calc-ideal-points-on-unit-circle circline-set-def ex-poincare-line-points ideal-points-diﬀerent(1 )
ideal-points-on-circline ideal-points-unique insertI1 insert-commute inversion-unit-circle mem-Collect-eq unique-poincare-line-general)
Ideal points of some special h-lines
Ideal points of x-axis
lemma ideal-points-x-axis
[simp]: ideal-points x-axis ={of-complex (−1 ), of-complex 1}
proof (subst ideal-points-unique, simp)
have calc-ideal-points-clmat-hcoords x-axis-clmat ={of-complex-hcoords (− 1 ), of-complex-hcoords 1}
by transfer auto
thus calc-ideal-points x-axis ={of-complex (− 1 ), of-complex 1}
by (simp add : calc-ideal-points.abs-eq of-complex.abs-eq x-axis-def )
qed
Ideal points are proportional vectors only if h-line is a line segment passing trough zero
lemma ideal-points-proportional:
assumes is-poincare-line H ideal-points H ={i1, i2} to-complex i1 = cor k ∗ to-complex i2
shows 0 h∈ circline-set H
proof−
have i1⁄= i2
using ‹ideal-points H ={i1, i2}›
using ‹is-poincare-line H › ex-poincare-line-points ideal-points-diﬀerent(1 ) by blast
have i1∈ circline-set unit-circle i2 ∈ circline-set unit-circle
using assms calc-ideal-points-on-unit-circle ideal-points-unique
by blast+
hence cmod (cor k ) = 1
using ‹to-complex i1 = cor k ∗ to-complex i2 ›
by (metis (mono-tags, lifting) circline-set-unit-circle imageE mem-Collect-eq mult.right-neutral norm-mult to-complex-of-complex
unit-circle-set-def )
hence k =−1
using ‹to-complex i1 = cor k ∗ to-complex i2 › ‹i1⁄= i2 ›
using ‹i1∈ circline-set unit-circle › ‹i2∈ circline-set unit-circle ›
by (smt (verit, best) mult-cancel-right1 norm-of-real not-inf-on-unit-circle ′′ of-complex-to-complex of-real-1 )
have∀ i1 ∈ calc-ideal-points H.∀ i2 ∈ calc-ideal-points H. is-poincare-line H ∧ i1 ⁄= i2 ∧ to-complex i1 =−
to-complex i2 −→
0 h∈ circline-set H
unfolding circline-set-def
proof (simp, transfer, transfer, safe)
41
ﬁx A B C D i11 i12 i21 i22 k
assume H :hermitean (A, B, C, D) ( A, B, C, D)⁄= mat-zero
assume line: is-poincare-line-cmat (A, B, C, D)
assume i1 : ( i11, i12 )∈ calc-ideal-points-cmat-cvec (A, B, C, D)
assume i2 :(i21, i22 )∈ calc-ideal-points-cmat-cvec (A, B, C, D)
assume¬ (i11, i12 )≈v (i21, i22 )
assume opposite: to-complex-cvec (i11, i12 ) = − to-complex-cvec (i21, i22 )
let ?discr = sqrt ((cmod B )2− (Re D )2)
let ?den = ( cmod B )2
let ?i1 = B∗ (− D− i∗ ?discr)
let ?i2 = B∗ (− D + i ∗ ?discr)
have i11 = ?i1∨ i11 = ?i2 i12 = ?den
i21 = ?i1∨ i21 = ?i2 i22 = ?den
using i1 i2 H line
by (auto split : if-split-asm)
hence i: i11 = ?i1∧ i21 = ?i2∨ i11 = ?i2∧ i21 = ?i1
using ‹¬ (i11, i12 )≈v (i21, i22 )›
by auto
have ?den⁄= 0
using line
by auto
hence i11 =− i21
using opposite ‹i12 = ?den› ‹i22 = ?den›
by (simp add : nonzero-neg-divide-eq-eq2)
hence ?i1 =− ?i2
using i
by (metis add.inverse-inverse)
hence D = 0
using ‹?den⁄= 0 ›
by (simp add : ﬁeld-simps)
thus on-circline-cmat-cvec (A, B, C, D) 0 v
by (simp add : vec-cnj-def )
qed
thus ?thesis
using assms ‹k =−1 ›
using calc-ideal-points-diﬀerent ideal-points-unique
by fastforce
qed
Transformations of ideal points
Möbius transformations that ﬁx the unit disc when acting on h-lines map their ideal points to ideal points.
lemma ideal-points-moebius-circline [simp]:
assumes unit-circle-ﬁx M is-poincare-line H
shows ideal-points (moebius-circline M H ) = ( moebius-pt M ) ‘ (ideal-points H ) ( is ?I ′ = ?M ‘ ?I )
proof−
obtain i1 i2 where∗: i1⁄= i2 ?I ={i1, i2}
using assms(2 )
by (rule obtain-ideal-points )
let ?Mi1 = ?M i1 and ?Mi2 = ?M i2
have ?Mi1∈ ?M ‘ (circline-set H )
?Mi2∈ ?M ‘ (circline-set H )
?Mi1∈ ?M ‘ (circline-set unit-circle )
?Mi2∈ ?M ‘ (circline-set unit-circle )
using∗
unfolding ideal-points-def circline-intersection-def circline-set-def
by blast+
42
hence ?Mi1∈ ?I ′
?Mi2∈ ?I ′
using unit-circle-ﬁx-iﬀ [of M ] assms
unfolding ideal-points-def circline-intersection-def circline-set-def
by (metis mem-Collect-eq moebius-circline )+
moreover
have ?Mi1⁄= ?Mi2
using bij-moebius-pt[of M ]∗
using moebius-pt-invert by blast
moreover
have is-poincare-line (moebius-circline M H )
using assms unit-circle-ﬁx-preserve-is-poincare-line
by simp
ultimately
have ?I ′ ={?Mi1, ?Mi2}
using two-ideal-points[of moebius-circline M H ]
using card-eq-2-doubleton[of ?I ′ ?Mi1 ?Mi2 ]
by simp
thus ?thesis
using∗(2 )
by auto
qed
lemma ideal-points-poincare-line-moebius [simp]:
assumes unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc u ⁄= v
assumes ideal-points (poincare-line u v ) = {i1, i2}
shows ideal-points (poincare-line (moebius-pt M u ) ( moebius-pt M v )) = {moebius-pt M i1 , moebius-pt M i2}
using assms
by auto
Conjugation also maps ideal points to ideal points
lemma ideal-points-conjugate [simp]:
assumes is-poincare-line H
shows ideal-points (conjugate-circline H ) = conjugate ‘ (ideal-points H ) ( is ?I ′ = ?M ‘ ?I )
proof−
obtain i1 i2 where∗: i1⁄= i2 ?I ={i1, i2}
using assms
by (rule obtain-ideal-points )
let ?Mi1 = ?M i1 and ?Mi2 = ?M i2
have ?Mi1∈ ?M ‘ (circline-set H )
?Mi2∈ ?M ‘ (circline-set H )
?Mi1∈ ?M ‘ (circline-set unit-circle )
?Mi2∈ ?M ‘ (circline-set unit-circle )
using∗
unfolding ideal-points-def circline-intersection-def circline-set-def
by blast+
hence ?Mi1∈ ?I ′
?Mi2∈ ?I ′
unfolding ideal-points-def circline-intersection-def circline-set-def
using circline-set-conjugate-circline circline-set-def conjugate-unit-circle-set
by blast+
moreover
have ?Mi1⁄= ?Mi2
using ‹i1⁄= i2 ›
by (auto simp add : conjugate-inj)
moreover
have is-poincare-line (conjugate-circline H )
using assms
by simp
ultimately
have ?I ′ ={?Mi1, ?Mi2}
using two-ideal-points[of conjugate-circline H ]
using card-eq-2-doubleton[of ?I ′ ?Mi1 ?Mi2 ]
by simp
thus ?thesis
using∗(2 )
43
by auto
qed
lemma ideal-points-poincare-line-conjugate [simp]:
assumesu∈ unit-disc v ∈ unit-disc u ⁄= v
assumes ideal-points (poincare-line u v ) = {i1, i2}
shows ideal-points (poincare-line (conjugate u ) ( conjugate v )) = {conjugate i1, conjugate i2}
using assms
by auto
end
theory Poincare-Distance
imports Poincare-Lines-Ideal-Points Hyperbolic-Functions
begin
