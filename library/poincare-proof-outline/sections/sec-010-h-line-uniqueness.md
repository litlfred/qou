---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-010-h-line-uniqueness
section_title: "H-line uniqueness"
section_number: null
pages: 11-14
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
There is no more than one h-line that contains two different h-points (in the disc).

lemma unique-is-poincare-line:
assumes in-disc: u € unit-disc v € unit-disc u # v
assumes pl: is-poincare-line l1 is-poincare-line 12
assumes on-l: {u, v} C circline-set l1 M circline-set 12
shows I] = 12

11
proof—
have u # inversion uv # inversion u
using in-disc
using inversion-noteg-unit-disc[of u v]
using inversion-noteq-unit-disclof u ul
by auto
thus ?thesis
using on-l
using unique-circline-set|of u inversion u v| <u # v>
using is-poincare-line-inverse-point|of l1 ul
using is-poincare-line-inverse-point|of 12 ul
using pl
by auto
qed

For the rest of our formalization it is often useful to consider points on h-lines that are not within the unit disc.
Many lemmas in the rest of this section will have such generalizations.

There is no more than one h-line that contains two different and not mutually inverse points (not necessary in
the unit disc).

lemma unique-is-poincare-line-general:
assumes different: u #4 v u 4 inversion v
assumes pl: is-poincare-line l1 is-poincare-line 12
assumes on-l: {u, v} C circline-set l1 M circline-set 12
shows li = 12
proof (cases u # inversion u)
case True
thus ?thesis
using unique-circline-set|of u inversion u v|
using assms
using is-poincare-line-inverse-point by force
next
case False
show ?thesis
proof (cases v # inversion v)
case True
thus ?thesis
using unique-circline-set[of u inversion v v]
using assms
using is-poincare-line-inverse-point by force
next
case False

have on-circline unit-circle u on-circline unit-circle v
using (7 u # inversion u) ‘7 v # inversion v>
using inversion-id-iff-on-unit-circle
by fastforce+
thus ?thesis
using pl on-l (u # v>
unfolding circline-set-def
apply simp
proof (transfer, transfer, safe)
fix ul u2 v1 v2 Al B1 Cl D1 A2 B2 C2 D2 :: complex
let ?u = (ul, u2) and ?v = (v1, v2) and ?H1 = (A1, B1, Cl, D1) and ?H2 = (A2, B2, C2, D2)
assume *: ?u 4 vec-zero ?v # vec-zero
on-circline-cmat-cvec unit-circle-cmat ?u on-circline-cmat-cvec unit-circle-cmat ?v
is-poincare-line-cmat ?H1 is-poincare-line-cmat ?H2
hermitean ?H1 ?H1 # mat-zero hermitean ?H2 ?H2 # mat-zero
on-circline-cmat-cvec ?H1 ?u on-circline-cmat-cvec ?H1 ?v
on-circline-cmat-cvec ?H2 ?u on-circline-cmat-cvec ?H2 ?v
a (ul, u2) &y (v1, v2)
have x*: Al = D1 A2 = D2 Cl = cnj B1 C2 = cnj B2 is-real Al is-real A2
using <is-poincare-line-cmat ?H1) <is-poincare-line-cmat ?H2)
using <hermitean ?H1» «?H1 4 mat-zeroy <hermitean ?H2) «?H2 4 mat-zeroy
using hermitean-elems
by auto

12
have wu: ul 4 0u2 4 0v1 F0v2 40
using *(1—/)
by (auto simp add: vec-cnj-def)

have u: cor ((Re (ul/u2))?) + cor ((Im (ul/u2))?) = 1
using <on-circline-cmat-cvec unit-circle-cmat ?ur uv
apply (subst of-real-add[symmetric])
apply (subst complex-mult-cnj|symmetric])
apply (simp add: vec-cnj-def mult.commute)
done

have v: cor ((Re (v1/v2))?) + cor ((Im (v1/v2))?) = 1
using (on-circline-cmat-cvec unit-circle-cmat ?v) uv
apply (subst of-real-add[symmetric])
apply (subst complex-mult-cnj|symmetric])
apply (simp add: vec-cnj-def mult.commute)
done

have

Al * (cor ((Re (ul/u2))?) + cor ((Im (ul/u2))?) + 1) + cor (Re B1) * cor(2 * Re (ul/u2)) + cor (Im B1)
«x cor(2 * Im (ul/u2)) = 0

A2 « (cor ((Re (ul/u2))?) + cor ((Im (ul/u2))?) + 1) + cor (Re B2) * cor(2 * Re (ul/u2)) + cor (Im B2)
«x cor(2 * Im (ul/u2)) = 0

Al « (cor ((Re (v1/v2))?) + cor ((Im (v1/v2))?) + 1) + cor (Re B1) * cor(2 * Re (v1/v2)) + cor (Im B1) *
cor(2 « Im (v1/v2)) = 0

A2 « (cor ((Re (v1/v2))?) + cor ((Im (v1/v2))?) + 1) + cor (Re B2) * cor(2 * Re (v1/v2)) + cor (Im B2) «
cor(2 « Im (v1/v2)) = 0

using circline-equation-quadratic-equation|of Al ul/u2 B1 D1 Re (ul/u2) Im (ul / u2) Re B1 Im B1]

using circline-equation-quadratic-equation|of A2 ul/u2 B2 D2 Re (ul/u2) Im (ul / u2) Re B2 Im B2]

using circline-equation-quadratic-equation|of Al v1/v2 B1 D1 Re (v1/v2) Im (v1 / v2) Re B1 Im B1]

using circline-equation-quadratic-equation|of A2 v1/v2 B2 D2 Re (v1/v2) Im (v1 / v2) Re B2 Im B2]

using (on-circline-cmat-cvec ?H1 ?u) ‘on-circline-cmat-cvec ?H2 ?uy

using (on-circline-cmat-cvec ?H1 ?v) <on-circline-cmat-cvec ?H2 ?uy

using ** wu

by (simp-all add: vec-cnj-def field-simps)

hence
Al + cor (Re B1) * cor(Re (ul/u2)) + cor (Im B1) * cor(Im (ul/u2)) = 0
Al + cor (Re B1) * cor(Re (v1/v2)) + cor (Im B1) * cor(Im (v1/v2)) = 0
A2 + cor (Re B2) * cor(Re (ul/u2)) + cor (Im B2) * cor(Im (ul/u2)) = 0
A2 + cor (Re B2) * cor(Re (v1/v2)) + cor (Im B2) * cor(Im (v1/v2)) = 0

using u v
by simp-all algebra+

hence
cor (Re Al + Re B1 * Re (ul/u2) + Im B1 * Im (ul/u2)) = 0
cor (Re A2 + Re B2 * Re (ul/u2) + Im B2 * Im (ul/u2)) = 0
cor (Re Al + Re B1 * Re (v1/v2) + Im B1 * Im (v1/v2)) = 0
cor (Re A2 + Re B2 * Re (v1/v2) + Im B2 * Im (v1/v2)) = 0
using <is-real A1) <is-real A2»
by simp-all

hence
Re Al + Re B1 * Re
Re Al + Re B1 * Re
Re A2 + Re B2 * Re
Re A2 + Re B2 * Re
using of-real-eq-0-iff
by blast+

ul/u2) + Im B1 * Im (ul/u2) =
v1/v2) + Im B1 * Im (v1/v2) =
ul/u2) + Im B2 * Im (ul/u2) =

0
0
0
v1/v2) + Im B2 « Im (v1/v2) = 0

moreover
have Re(ul/u2) 4 Re(v1/v2) V Im(ul/u2) 4 Im(v1/v2)

proof (rule ccontr)
assume 7 ?thesis

13
hence ul/u2 = v1/v2
using complez-eqI by blast
thus False
using wv (7 (ul, u2) %y (v1, v2)»
using *(1) *«(2) complex-cvec-eq-mix[OF *(1) *(2)]
by (auto simp add: field-simps)
qed

moreover

have Re Al #0 V Re B1 01 V ImB1 40
using <?H1 4 mat-zeroy **
by (metis complex-cnj-zero complez-of-real-Re mat-zero-def of-real-0)

ultimately

obtain k where
k: Re A2 =k * Re Al Re B2 = k * Re B1 Im B2 =k * Im B1
using linear-system-homogenous-3-2[of Ax y z. 1 * + Re (ul / u2) * y+ Im (ul / u2) * z1 Re (ul/u2) Im
(ul /u2)
Avy z. 1 * «a+ Re (vl / v2) * y+ Im (vl / v2) * 21 Re (v1/v2) Im (v1/v2)
Re A2 Re B2 Im B2 Re Al Re B1 Im B1|
by (auto simp add: field-simps)

have Re A2 40 V Re B2 40V Im B2 40

using <?H2 # mat-zero» **

by (metis complex-cnj-zero complez-of-real-Re mat-zero-def of-real-0)
hence k 4 0

using k

by auto

show circline-eq-cmat ?H1 ?H2
using ** k «k 4 0»
by (auto simp add: vec-cnj-def) (rule-tac s=k in exI, auto simp add: complex.expand)
qed
qed
qed

The only h-line that goes trough zero and a non-zero point on the x-axis is the x-axis.

lemma is-poincare-line-0-real-is-x-axis:
assumes is-poincare-line | 0; € circline-set |
x € circline-set 1M circline-set x-aris x # On © A On
shows | = z-axis
using assms
using is-poincare-line-trough-zero-trough-infty|OF assms(1—2)|
using unique-circline-set[of x On con)
by auto

The only h-line that goes trough zero and a non-zero point on the y-axis is the y-axis.
lemma is-poincare-line-0-imag-is-y-axis:

assumes is-poincare-line | 0; € circline-set |

y € circline-set 1 circline-set y-aris y # On y # On

shows | = y-axis

using assms

using is-poincare-line-trough-zero-trough-infty|OF assms(1—2)|

using unique-circline-set[of y On oon]

by auto
