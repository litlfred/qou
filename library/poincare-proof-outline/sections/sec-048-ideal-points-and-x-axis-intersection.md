---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-048-ideal-points-and-x-axis-intersection
section_title: "Ideal points and x-axis intersection"
section_number: null
pages: 112-114
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma ideal-points-intersects-x-azis:
assumes is-poincare-line H and ideal-points H = {i1, i2} and H # z-axis
shows intersects-t-axis H <—> Im (to-complex i1) « Im (to-complez i2) < 0
using assms
proof—
have il # i2
using assms(1) assms(2) ex-poincare-line-points ideal-points-different(1)
by blast

112
have calc-ideal-points H = {i1, i2}
using assms
using ideal-points-unique
by auto

have V il € calc-ideal-points H.
V i2 € calc-ideal-points H.
is-poincare-line H \ H # x-axis \ i1 # i2 —+ (Im (to-complex i1) * Im (to-complez i2) < 0 ++
intersects-x-axis H)
proof (transfer, transfer, (rule ballI)+, rule impI, (erule conjE)+, case-tac H, case-tac il, case-tac i2)
fix i11 i112 i21 122 ABCD Hil i2
assume H: H = (A, B, C, D) hermitean H H # mat-zero
assume line: is-poincare-line-cmat H
assume if: il = (i11, i12) il € calc-ideal-points-cmat-cvec H
assume 72: i2 = (i21, i22) i2 € calc-ideal-points-cmat-cvec H
assume different: 4 il Xv i2
assume not-zx-azis: — circline-eq-cmat H x-axis-cmat

have is-real A is-real D C = cnj B
using H hermitean-elems
by auto

have (cmod A)? < (cmod B)? A= D
using line H
by auto

let ?discr = sqrt ((emod B)? — (Re D)?)
let ?den = (cmod B)?

let 7:1 = Bx (— D —i x ?discr)

let 712 = Bx (— D+i * ?discr)

have i11 = ?i1 V i11 = 712 i12 = ?den
i21 = 711 V i21 = ?i2 122 = ?den
using i1 i2 H line
by (auto split: if-split-asm)
hence 7: i11 = ?i1 A i21 = ?i2 V ill = 712 A i21 = Pil
using (7 il %y i2> il i2
by auto

have Im (i11 / i12) * Im (i21 / i22) = Im (?i1 / ?den) * Im (#2 / ?den)
using i <i12 = ?den> (122 = ?den)
by auto
also have ... = Im (?i1) * Im (?i2) / ?den?
by simp
also have ... = (Im B * (Im B * (Re D * Re D)) — Re B * (Re B * ((cmod B)* — (Re D)”))) / cmod B ~ 4
using <(cmod B)*? > (emod A)? «A = D»
using <is-real D) cmod-eq-Re|of A]
by (auto simp add: field-simps)
also have ... = ((Im B)? * (Re D)? — (Re B)? * ((Re B)? + (Im B)? — (Re D)*)) / emod B~ 4
proof —
have cmod B * cmod B= Re B * Re B+ Im Bx ImB
by (metis cmod-power2 power2-eq-square)
thus ?thesis
by (simp add: power2-eq-square)
qed
also have ... = (((Re D)? — (Re B)*) « ((Re B)? + (Im B)?)) / cmod B~ 4
by (simp add: power2-eq-square field-simps)
finally have Im-product: Im (i11 / i12) * Im (i21 / i22) = ((Re D)? — (Re B)*) « ((Re B)? + (Im B)?) / cmod
Br4

show Im (to-complez-cvec i1) * Im (to-complez-cvec i2) < 0 <—+ intersects-z-axis-cmat H
proof safe

assume opposite: Im (to-complex-cvec i1) * Im (to-complex-cvec i2) < 0

show intersects-x-axis-cmat H

proof—

113
have ((Re D)? — (Re B)”) * ((Re B)? + (Im B)?) / cmod B~4 < 0
using Im-product opposite il i2
by simp
hence ((Re D)? — (Re B)”) * ((Re B)? + (Im B)?) < 0
by (simp add: divide-less-0-iff)
hence (Re D)? < (Re B)?
by (simp add: mult-less-0-iff not-sum-power2-lt-zero)
thus ?thesis
using H (A = D) <is-real Dy
by auto
qed
next
have «: (Vk. k * ImB=1—+k=0) — ImB=0
apply (safe, erule-tac z=1 / Im B in allE)
using divide-cancel-left by fastforce
assume intersects-x-axis-cmat H
hence Re D = 0 V (Re D)? < (Re B)?
using H <A = D>
by auto
hence (Re D)? < (Re B)?
using <is-real Dy line H «C = cnj By
using not-z-azis *
by (auto simp add: complex-eq-iff )
hence ((Re D)? — (Re B)*) * ((Re B)? + (Im B)?) < 0
by (metis add-cancel-left-left diff-less-eq mult-eq-0-iff mult-less-0-iff power2-eq-square power2-less-0 sum-squares-gt-zero-iff )
thus Im (to-complex-cvec i1) * Im (to-complez-cvec i2) < 0
using Im-product il i2
using divide-eq-0-iff divide-less-0-iff prod.simps(2) to-complez-cvec-def zero-complez.simps(1) zero-less-norm-iff
by fastforce
qed
qed
thus ?thesis
using assms <calc-ideal-points H = {i1, i2}» «il # i2>
by auto
qed

end
theory Poincare-Perpendicular

imports Poincare-Lines-Azxis-Intersections
begin
