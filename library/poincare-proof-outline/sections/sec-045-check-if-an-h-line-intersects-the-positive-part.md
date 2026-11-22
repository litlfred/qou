---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-045-check-if-an-h-line-intersects-the-positive-part
section_title: "Check if an h-line intersects the positive part of the x-axis"
section_number: null
pages: 105-108
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
definition intersects-x-axis-positive-cmat :: complez-mat => bool where
[simp]: intersects-x-axis-positive-cmat H = (let (A, B, C, D) = Hin Re A#0 A Re B/ Re A< -1)

lift-definition intersects-2-axis-positive-clmat :: circline-mat = bool is intersects-x-axis-positive-cmat
done

lift-definition intersects-x-axis-positive :: circline = bool is intersects-x-axis-positive-clmat
proof (transfer)
fix H1 H2
assume hh: hermitean H1 A H1 4 mat-zero and hermitean H2 \ H2 4 mat-zero
obtain Ai B1 C1 D1 A2 B2 C2 D2 where *: H1 = (A1, B1, C1, D1) H2 = (A2, B2, C2, D2)
by (cases H1, cases H2, auto)
assume circline-eq-cmat H1 H2
then obtain k where k 4 0 \ H2 = cork *sm H1
by auto
thus intersects-1-axis-positive-cmat H1 = intersects-x-axis-positive-cmat H2
using *
by simp
qed

lemma intersects-x-axis-positive-mk-circline:
assumes is-real Aand A#0V B40
shows intersects-x-axis-positive (mk-circline A B (cnj B) A) + Re B/ Re A < -1
proof—
let ?H = (A, B, (cnj B), A)
have hermitean ?H
using <is-real A»
unfolding hermitean-def mat-adj-def mat-cnj-def
using eq-cnj-iff-real
by auto
moreover
have ?H 4 mat-zero
using assms
by auto
ultimately

105
show ?thesis
by (transfer, transfer, auto simp add: Let-def)
qed

lemma intersects-x-axis-positive-intersects-z-axis [simp]:
assumes intersects-z-axis-positive H
shows intersects-x-axis H
proof—
have /\ a aa. [ Re a # 0; Re aa / Rea < — 1; 4 (Re a)? < (Re aa)? ] = aa=O0Aa=0
by (smt less-divide-eq-1-pos one-less-power pos2 power2-minus power-divide zero-less-power2)
thus ?thesis
using assms
apply transfer
apply transfer
apply (auto simp add: hermitean-def mat-adj-def mat-cnj-def)
done
qed

lemma add-less-abs-positive-iff:
fixes a b :: real
assumes abs b < abs a
showsa+b>0+—>+a>0
using assms
by auto

lemma calc-x-azis-intersection-positive-abs’:
fixes A B :: real
assumes B? > A? and A # 0
shows abs (sgn(B) * sqrt(B? — A) / A) < abs(—B/A)
proof—
from assms have B 4 0
by auto

have B? — A? < B?
using <A # 0>
by auto
hence sqrt (B? — A?) < abs B
using real-sqrt-less-iff [of B? — A? B?]
by simp
thus ?thesis
using assms (B # 0»
by (simp add: abs-mult divide-strict-right-mono)
qed

lemma calc-intersect-x-axis-positive-lemma:
assumes B? > A? and A # 0
shows (—B + sgn B « sqrt(B? — A*))/A>0+¢>+-B/A>1
proof—

have (—B + sgn B * sqrt(B? — A?)) / A= —B/ A+ (sgn B * sqrt(B? — A*)) / A
using assms
by (simp add: field-simps)

moreover

have —B / A + (sgn B * sqrt(B? — A*))/A>0¢>-B/A>0
using add-less-abs-positive-iff|OF calc-x-axis-intersection-positive-abs'|OF assms]]
by simp

moreover

hence (B/A)? > 1
using assms
by (simp add: power-divide)

hence B/A>1V B/A<-1
by (smt one-power2 pos2 power2-minus power-0 power-strict-decreasing zero-power2)

hence -B/A>0++-B/A>1
by auto

ultimately

show ?thesis

106
using assms
by auto
qed

lemma intersects-z-axis-positive-iff ':
assumes is-poincare-line H
shows intersects-z-axis-positive H —
calc-x-axis-intersection H € unit-disc \ calc-a-axis-intersection H € circline-set H M positive-x-axis (is ?lhs ~—>
rhs)
proof
let ?x = calc-z-axis-intersection H
assume ?/hs
hence ?x € circline-set x-axis ?x € circline-set H ?x € unit-disc
using calc-x-axis-intersection-in-unit-disc|OF assms] calc-x-axis-intersection|OF assms]
by auto
moreover
have Re (to-complex ?x) > 0
using <?lhs> assms
proof (transfer, transfer)
fix H
assume hh: hermitean H \ H # mat-zero
obtain A B C D where *: H = (A, B, C, D)
by (cases H, auto)
assume intersects-z-axis-positive-cmat H
hence **: Re B/ Re A<—1Re AAO
using *
by auto
have (Re B)? > (Re A)?
using **
by (smt divide-less-eq-1-neg divide-minus-left less-divide-eq-1-pos real-sqrt-abs real-sqrt-less-iff right-inverse-eq)
have is-real A A # 0
using hh hermitean-elems * «Re A # 0» complex.expand|of A 0|
by auto
have (cmod B)? > (cmod A)?
using «(Re B)? > (Re A)?» ¢is-real A»
by (smt cmod-power2 power2-less-0 zero-power2)
have *««: 0 < (— Re B + sgn (Re B) * sqrt ((Re B)? — (Re A)?)) / Re A
using calc-intersect-x-axis-positive-lemma|of Re A Re B] ** «(Re B)? > (Re A)?»
by auto

assume is-poincare-line-cmat H

hence A = D
using * hh
by simp

have Re ((cor (sgn (Re B)) * cor (sqrt ((Re B)? — (Re A)?)) — cor (Re B)) / A) = (sgn (Re B) * sqrt ((Re B)?
— (Re A)?) — Re B) / Re D
using <is-real A) «A = Dy
by (metis (no-types, lifting) Re-complez-of-real complex-of-real-Re of-real-diff of-real-divide of-real-mult)
thus 0 < Re (to-complex-cvec (calc-a-axis-intersection-cmat-cvec H))
using * hh «x *&* «(cmod B)? > (cmod A)?» «(Re B)? > (Re A)?» (A # 0) (A = Dy
by simp
qed
ultimately
show ?rhs
unfolding positive-x-azis-def
by auto
next
let ?x = calc-z-axis-intersection H
assume ?rhs
hence Re (to-compler ?x) > 0 ?x # wp ?x € circline-set x-axis ?x € unit-disc ?x € circline-set H
unfolding positive-x-azis-def
by auto
hence intersects-x-aris H
using intersects-x-avis-iff|OF assms|
by auto

107
thus ?lhs
using ‘Re (to-complex ?x) > 0> assms
proof (transfer, transfer)
fix H
assume hh: hermitean H \ H # mat-zero
obtain A B C D where *: H = (A, B, C, D)
by (cases H, auto)
assume 0) < Re (to-complex-cvec (calc-x-axis-intersection-cmat-cvec H)) intersects-t-axis-cmat H is-poincare-line-cmat
ve
hence **: A 4 0.0 < Re ((cor (sgn (Re B)) * cor (sqrt ((Re B)? — (Re A)”)) — cor (Re B)) / A) A= D is-real
A (Re B)? > (Re A)?
using * hh hermitean-elems
by (auto split: if-split-asm)

have Re A # 0
using complez.expand[of A 0] «A # 0» <is-real A>
by auto

have Re ((cor (sgn (Re B)) * cor (sqrt ((Re B)? — (Re D)”)) — cor (Re B)) / D) = (sgn (Re B) * sqrt ((Re B)?
— (Re D)?) — Re B) / Re D
using <is-real A) «A = Dy
by (metis (no-types, lifting) Re-complez-of-real complex-of-real-Re of-real-diff of-real-divide of-real-mult)

thus intersects-x-axis-positive-cmat H
using * *« (Re A # 0»
using calc-intersect-x-axis-positive-lemmal|of Re A Re B|
by simp
qed
qed

lemma intersects-x-axis-positive-iff:
assumes is-poincare-line H and H # s-azis
shows intersects-z-axis-positive H —
(A 2. « € unit-disc A x € circline-set H ( positive-x-axis) (is ?lhs > ?rhs)
proof
assume ?/hs
thus ?rhs
using intersects-x-axis-positive-iff [OF assms(1)]
by auto
next
assume ?rhs
then obtain z where zx € unit-disc x € circline-set H \ positive-a-axis
by auto
thus ?lhs
using unique-calc-z-azis-intersection[OF assms, of 2]
using intersects-x-axis-positive-iff [OF assms(1)]
unfolding positive-x-azis-def
by auto
qed
