---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-022-ideal-points
section_title: "Ideal points"
section_number: null
pages: 39-44
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma calc-ideal-points-cvec-different [simp]:
assumes (cmod B)? > (cmod A)? is-real A
shows 7— (calc-ideal-point1-cvec A B %, calc-ideal-point2-cvec A B)
using assms
by (auto) (auto simp add: cmod-def)

lemma calc-ideal-points-different:
assumes is-poincare-line H
shows 3 il € (calc-ideal-points H). 4 i2 € (calc-ideal-points H). i1 # i2
using assms
proof (transfer, transfer)
fix H
assume hh: hermitean H \ H # mat-zero is-poincare-line-cmat H
obtain A B C D where «: H = (A, B, C, D)
by (cases H, auto)
hence is-real A using hh hermitean-elems by auto
thus 5 i1 €calc-ideal-points-cmat-cvec H. 3i2€calc-ideal-points-cmat-cvec H. 7 il Sy i2
using * hh calc-ideal-points-cvec-different|of A B]
apply (rule-tac x=calc-ideal-point1-cvec A B in bez!)
apply (rule-tac x=calc-ideal-point2-cvec A B in bex!)
by auto
qed

lemma two-calc-ideal-points [simp]:
assumes is-poincare-line H
shows card (calc-ideal-points H) = 2
proof—
have 4 z € calc-ideal-points H. A y € calc-ideal-points H. z € calc-ideal-points H.z=xVz2=y
by (transfer, transfer, case-tac H, simp del: calc-ideal-point1-cvec-def calc-ideal-point2-cvec-def )
then obtain z y where *: calc-ideal-points H = {x, y}
by auto
moreover
have z 4 y
using calc-ideal-points-different|OF assms| *
by auto
ultimately
show ?thesis
by auto
qed

4.3.2 Ideal points

Next we give a genuine definition of ideal points — these are the intersections of the h-line with the unit circle

definition ideal-points :: circline = complex-homo set where
ideal-points H = circline-intersection H unit-circle
Ideal points are on the unit circle and on the h-line

lemma ideal-points-on-unit-circle:
shows V z € ideal-points H. z € circline-set unit-circle
unfolding ideal-points-def circline-intersection-def circline-set-def
by simp

lemma ideal-points-on-circline:
shows V z € ideal-points H. z € circline-set H
unfolding ideal-points-def circline-intersection-def circline-set-def
by simp

For each h-line there are exactly two ideal points

lemma two-ideal-points:
assumes is-poincare-line H
shows card (ideal-points H) = 2
proof—
have H ¥ unit-circle
using assms not-is-poincare-line-unit-circle
by auto
let ?int = circline-intersection H unit-circle
obtain i1 i2 where i1 € ?int i2 € ?int il A i2
using calc-ideal-points-on-circline[OF assms]
using calc-ideal-points-on-unit-circle|of H|
using calc-ideal-points-different|OF assms|
unfolding circline-intersection-def circline-set-def
by auto
thus ?thesis
unfolding ideal-points-def
using circline-intersection-at-most-2-points|OF «H # unit-circle>]
using card-geq-2-iff-contains-2-elems|of ?int]
by auto
qed

They are exactly the two points that our calculation finds

lemma ideal-points-unique:
assumes is-poincare-line H
shows ideal-points H = calc-ideal-points H
proof—
have calc-ideal-points H C ideal-points H
using calc-ideal-points-on-circline[OF assms]
using calc-ideal-points-on-unit-circle|of H|
unfolding ideal-points-def circline-intersection-def circline-set-def
by auto
moreover
have H ¥ unit-circle
using not-is-poincare-line-unit-circle assms
by auto
hence finite (ideal-points H)
using circline-intersection-at-most-2-points|of H unit-circle]
unfolding ideal-points-def
by auto
ultimately
show ?thesis
using card-subset-eq|of ideal-points H calc-ideal-points H|
using two-calc-ideal-points|OF assms]
using two-ideal-points|OF assms]
by auto
qed

For each h-line we can obtain two different ideal points

lemma obtain-ideal-points:
assumes is-poincare-line H
obtains i1 i2 where il # i2 ideal-points H = {i1, i2}
using two-ideal-points|OF assms] card-eq-2-iff-doubleton|of ideal-points H]
by blast

40
Ideal points of each h-line constructed from two points in the disc are different than those two points

lemma ideal-points-different:
assumes u € unit-disc v € unit-disc u # v
assumes ideal-points (poincare-line uv) = {i1, i2}
shows il A i2ufilufi2vF ilvFZ i2
proof—
have il € ocircline-set ounit-circle i2 € ocircline-set ounit-circle
using assms(3) assms(4) ideal-points-on-unit-circle is-poincare-line-poincare-line
by fastforce+
thus u 4 ilu 4 i2vF¢ il vF i2
using assms(1—2)
using disc-inter-ocircline-set{of ownit-circle]
unfolding unit-disc-def
by auto
show il # i2
using assms
by (metis doubleton-eq-iff is-poincare-line-poincare-line obtain-ideal-points)
qed

H-line is uniquely determined by its ideal points

lemma ideal-points-line-unique:

assumes is-poincare-line H ideal-points H = {i1, i2}

shows H = poincare-line il i2

by (smt assms(1) assms(2) calc-ideal-points-on-unit-circle circline-set-def ex-poincare-line-points ideal-points-different(1)
ideal-points-on-circline ideal-points-unique insertI1 insert-commute inversion-unit-circle mem-Collect-eq unique-poincare-line-general)

Ideal points of some special h-lines

Ideal points of x-axis

lemma ideal-points-x-axis
[simp]: ideal-points x-axis = {of-complex (—1), of-complex 1}
proof (subst ideal-points-unique, simp)
have calc-ideal-points-clmat-hcoords z-axis-clmat = {of-complex-hcoords (— 1), of-complex-hcoords 1}
by transfer auto
thus calc-ideal-points z-axis = {of-complex (— 1), of-complex 1}
by (simp add: calc-ideal-points.abs-eq of-complex.abs-eq x-axis-def )
qed

Ideal points are proportional vectors only if h-line is a line segment p

sing trough zero

lemma ideal-points-proportional:
assumes is-poincare-line H ideal-points H = {i1, i2} to-complex i1 = cor k * to-complex i2
shows 0), € circline-set H
proof—
have il # i2
using <ideal-points H = {i1, i2}>
using <is-poincare-line H) ex-poincare-line-points ideal-points-different(1) by blast

have i1 € circline-set unit-circle i2 € circline-set unit-circle
using assms calc-ideal-points-on-unit-circle ideal-points-unique
by blast+

hence cmod (cor k) = 1
using <to-complex il = cor k * to-complex i2)
by (metis (mono-tags, lifting) circline-set-unit-circle imageE mem-Collect-eq mult.right-neutral norm-mult to-complex-of-complex
unit-circle-set-def )
hence k = —1
using <to-complex i1 = cor k « to-complex i2> «il # i2>

using <i1 € circline-set unit-circle (i2 € circline-set unit-circley
by (smt (verit, best) mult-cancel-right1 norm-of-real not-inf-on-unit-circle’’ of-complex-to-complex of-real-1)

have V il € calc-ideal-points H. V i2 € calc-ideal-points H. is-poincare-line H \ il # i2 A to-compler i1 = —
to-complex i2 —+>
On € circline-set H
unfolding circline-set-def
proof (simp, transfer, transfer, safe)

41
fix A BC D i11 i12 i21 i22k

assume H:hermitean (A, B, C, D) (A, B, C, D) # mat-zero

assume line: is-poincare-line-cmat (A, B, C, D)

assume if: (i11, i12) € calc-ideal-points-cmat-cvec (A, B, C, D)

assume 72:(i21, 122) € calc-ideal-points-cmat-cvec (A, B, C, D)

assume 7 (i11, i12) %, (i21, i22)

assume opposite: to-complez-cvec (i11, i12) = — to-complex-cvec (i21, i22)

let ?discr = sqrt ((emod B)? — (Re D)?)
let ?den = (cmod B)?

let 7:1 = Bx (— D —i x ?discr)

let 712 = Bx (— D+i * ?discr)

have i11 = ?i1 V i11 = 712 i12 = ?den
i21 = ?i1 V i21 = ?i2 i122 = ?den
using i1 i2 H line
by (auto split: if-split-asm)
hence 7: i11 = ?i1 A i21 = ?i2 V ill = 712 A i21 = Pil
using (7 (i11, i112) %y (i21, i22)>
by auto

have ?den 4 0
using line
by auto

hence i11 = — i21
using opposite <i12 = ?den) <i22 = ?den»
by (simp add: nonzero-neg-divide-eq-eq2)

hence ?i1 = — ?i2
using i
by (metis add.inverse-inverse)

hence D = 0
using <?den # 0>
by (simp add: field-simps)

thus on-circline-cmat-cvec (A, B, C, D) 0,
by (simp add: vec-cnj-def)
qed

thus ?thesis
using assms «k = —1>
using calc-ideal-points-different ideal-points-unique
by fastforce
qed

Transformations of ideal points
Mobius transformations that fix the unit disc when acting on h-lines map their ideal points to ideal points.

lemma ideal-points-moebius-circline [simp]:
assumes unit-circle-fix M is-poincare-line H
shows ideal-points (moebius-circline M H) = (moebius-pt M) ‘ (ideal-points H) (is ?I' = ?M ‘ ?1)
proof—
obtain if i2 where «: if 4 i2 ?J = {i1, i2}
using assms(2)
by (rule obtain-ideal-points)
let ?Mil = ?M il and ?Mi2 = ?M i2
have ?Mil € ?M ‘ (circline-set H)
?Mi2 € ?M ‘ (circline-set H)
?Mil € ?M ‘ (circline-set unit-circle)
?Mi2 € ?M ‘ (circline-set unit-circle)
using *
unfolding ideal-points-def circline-intersection-def circline-set-def
by blast+

42
hence ?Mil € ?I'
?Mi2 © PI’

using wnit-circle-fiz-iff|of M] assms
unfolding ideal-points-def circline-intersection-def circline-set-def
by (metis mem-Collect-eq moebius-circline)+

moreover

have ?Mil 4 ?Mi2
using bij-moebius-pt[of M] *
using moebius-pt-invert by blast

moreover

have is-poincare-line (moebius-circline M H)
using assms unit-circle-fiz-preserve-is-poincare-line
by simp

ultimately

have ?1'= {?Mil, ?Mi2}
using two-ideal-points|of mocbius-circline M H|
using card-eq-2-doubleton|of 71’ ?Mil ?Mi2]
by simp

thus ?thesis
using *(2)
by auto

qed

lemma ideal-points-poincare-line-moebius [simp]:
assumes unit-disc-fix M wu € unit-disc v € unit-disc u # v
assumes ideal-points (poincare-line uv) = {i1, i2}
shows ideal-points (poincare-line (moebius-pt M u) (moebius-pt M v)) = {moebius-pt M il, moebius-pt M i2}
using assms
by auto

Conjugation also maps ideal points to ideal points

lemma ideal-points-conjugate [simp]:
assumes is-poincare-line H
shows ideal-points (conjugate-circline H) = conjugate ‘ (ideal-points H) (is ?I'= ?M ‘ ?1)
proof—
obtain if i2 where «: if 4 i2 ?J = {i1, i2}
using assms
by (rule obtain-ideal-points)
let ?Mil = ?M il and ?Mi2 = ?M i2
have ?Mil € ?M ‘ (circline-set H)
?Mi2 € ?M ‘ (circline-set H)
?Mil € ?M ‘ (circline-set unit-circle)
?Mi2 € ?M ‘ (circline-set unit-circle)
using *
unfolding ideal-points-def circline-intersection-def circline-set-def
by blast+
hence ?Mil € ?I’
?Mi2 € 21’
unfolding ideal-points-def circline-intersection-def circline-set-def
using circline-set-conjugate-circline circline-set-def conjugate-unit-circle-set
by blast+
moreover
have ?Mil 4 ?Mi2
using <i1 4 i2>
by (auto simp add: conjugate-inj)
moreover
have is-poincare-line (conjugate-circline H)
using assms
by simp
ultimately
have ?1'= {?Mil, ?Mi2}
using two-ideal-points|of conjugate-circline H]
using card-eq-2-doubleton|of 71’ ?Mil ?Mi2]
by simp
thus ?thesis
using *(2)
by auto
qed

lemma ideal-points-poincare-line-conjugate [simp):
assumesu € unit-disc v € unit-disc u # vu
assumes ideal-points (poincare-line uv) = {i1, i2}
shows ideal-points (poincare-line (conjugate u) (conjugate v)) = {conjugate i1, conjugate i2}
using assms
by auto

end
theory Poincare-Distance

imports Poincare-Lines-Ideal-Points Hyperbolic-Functions
begin
