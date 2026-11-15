---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-046-check-if-an-h-line-intersects-the-positive-part
section_title: "Check if an h-line intersects the positive part of the y-axis"
section_number: null
pages: 108-110
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
definition intersects-y-axis-positive-cmat :: complex-mat = bool where
[simp]: intersects-y-axis-positive-cmat H = (let (A, B, C, D) = Hin Re A# 0A ImB/ Re A < -1)

lift-definition intersects-y-azis-positive-clmat :: circline-mat = bool is intersects-y-axis-positive-cmat
done

lift-definition intersects-y-azis-positive :: circline = bool is intersects-y-axis-positive-clmat
proof (transfer)
fix H1 H2
assume hh: hermitean H1 A H1 4 mat-zero and hermitean H2 \ H2 4 mat-zero
obtain Ai B1 C1 D1 A2 B2 C2 D2 where *: H1 = (A1, B1, C1, D1) H2 = (A2, B2, C2, D2)
by (cases H1, cases H2, auto)
assume circline-eq-cmat H1 H2
then obtain k where k 4 0 \ H2 = cork *sm H1

108
by auto
thus intersects-y-axis-positive-cmat H1 = intersects-y-axis-positive-cmat H2
using *
by simp
qed

lemma intersects-x-axis-positive-intersects-y-axis-positive [simp]:
shows intersects-x-axis-positive (moebius-circline (moebius-rotation (—pi/2)) H) + intersects-y-axis-positive H
using hermitean-elems
unfolding moebius-rotation-def moebius-similarity-def
by simp (transfer, transfer, auto simp add: mat-adj-def mat-cnj-def)

lemma intersects-y-azis-positive-iff :
assumes is-poincare-line H H # y-axis
shows (4 y € unit-disc. y € circline-set H A positive-y-axis) —+ intersects-y-axis-positive H (is ?lhs + ?rhs)
proof—
let ?R = moebius-rotation (—pi / 2)
let ?H’ = moebius-circline ?R H
have 1: is-poincare-line ?H’
using assms
using wnit-circle-fiz-preserve-is-poincare-line|OF - assms(1), of ?R|
by simp

have 2: moebius-circline ?R H # x-axis
proof (rule ccontr)
assume — ?thesis
hence H = moebius-circline (moebius-rotation (pi/2)) x-axis
using mocebius-circline-comp-inv-left|of ?R H]|
by auto
thus False
using <(H F y-azis»
by auto
qed

show ?thesis
proof
assume ?/hs
then obtain y where y € unit-disc y € circline-set H \ positive-y-axis
by auto
hence moebius-pt ?R y € unit-dise moebius-pt ?R y € circline-set ?H' 1 positive-r-azis
using rotation-minus-pi-2-positive-y-axis
by auto
thus ?rhs
using intersects-z-axis-positive-iff[OF 1 2]
using intersects-z-axis-positive-intersects-y-azis-positive|of H|
by auto
next
assume intersects-y-axis-positive H
hence intersects-z-azis-positive ?H'
using intersects-z-axis-positive-intersects-y-azis-positive|of H|
by simp
then obtain z where «: x € unit-disc x € circline-set ?H' N positive-z-axis
using intersects-z-axis-positive-iff[OF 1 2]
by auto
let ?y = moebius-pt (—?R) x
have ?y € unit-disc \ ?y € circline-set H M positive-y-axis
using * rotation-minus-pi-2-positive-y-axis|symmetric]
by (metis Int-iff circline-set-moebius-circline-E image-eqI moebius-pt-comp-inv-image-left moebius-rotation-uminus
uminus-moebius-def unit-disc-fix-discI unit-disc-fix-rotation)
thus ?hs
by auto
qed
qed

109
