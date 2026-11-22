---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-039-some-more-properties-of-h-betweenness
section_title: "Some more properties of h-betweenness."
section_number: null
pages: 94-96
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Some lemmas proved earlier are proved almost directly using the sum of distances characterization.

lemma unit-disc-fix-moebius-preserve-poincare-between’:
assumes unit-disc-fix M and u € unit-disc and v € unit-disc and w € unit-disc
shows poincare-between (moebius-pt M u) (moebius-pt M v) (moebius-pt M w) <>
poincare-between uv w
using assms
using poincare-between-sum-distances
by simp

lemma conjugate-preserve-poincare-between':
assumes u € unit-disc v € unit-disc w € unit-disc
shows poincare-between (conjugate u) (conjugate v) (conjugate w) — poincare-between uv w
using assms
using poincare-between-sum-distances
by simp

There is a unique point on a ray on the given distance from the given starting point

lemma unique-poincare-distance-on-ray:
assumes d > 0 u # v u € unit-disc v € unit-disc
assumes y € unit-disc poincare-distance u y = d poincare-between u v y
assumes z € unit-disc poincare-distance u z = d poincare-between u v z
shows y = z
proof—
have V dyz.d>0A
y € unit-disc \ poincare-distance uy = d A poincare-between uv y A
z € unit-dise \ poincare-distance u z = d A poincare-between uv z —> y = z (is ?P uv)
proof (rule wlog-positive-x-azis[;where P=?P])
fix x
assume 2: is-real tr 0 < Rex Rex < 1
hence z 4 0
using complez.expand[of x 0]
by auto
hence *: poincare-line 0; (of-complex x) = x-axis
using 2 poincare-line-0-real-is-x-axis|of of-complex «|
unfolding circline-set-x-axis
by auto
have of-complex x € unit-disc
using x
by (auto simp add: cmod-eq-Re)
have Arg x = 0
using x

94
using arg-0-iff by blast
show ?P 0), (of-complex x)
proof safe
fix yz
assume y € unit-disc z € unit-disc
then obtain y’ z’ where yz: y = of-complex y’ z = of-complex z'
using inf-or-of-complez|of y| inf-or-of-complez|of z]
by auto
assume betw: poincare-between 0), (of-complex x) y poincare-between On (of-compler x) z
hence y 4 0n z 4 On
using <x # 0» <of-complex x € unit-disc» <y € unit-disc)
using poincare-between-sandwich|of 0; of-complex |
using of-complez-zero-iff [of x]
by force+

hence Arg y’ = 0 cmod y’ > cmod x Arg z' = 0 cmod z' > cmod «
using poincare-between-Ouvlof of-complex x y| poincare-between-Ouv| of of-complex x 2]
using <of-complex x € unit-discy «x # 0» (Arg x = 0» <y € unit-disc» «z € unit-disc> betw yz
by (simp-all add: Let-def)
hence *: is-real y’ is-real z’ Re y' > 0 Re z' > 0
using arg-0-iff[of y'| arg-0-iff[of z'] x (y # On> (2 # On»? yz
by auto
assume poincare-distance 0; z = poincare-distance 0; y 0 < poincare-distance On y
thus y = z
using * yz <y € unit-discy «z € unit-disc»
using unique-z-axis-poincare-distance-positive|of poincare-distance On y]
by (auto simp add: cmod-eq-Re unit-disc-to-complez-inj)
qed
next
show u € unit-disc v € unit-disc u A v
by fact+
next
fix Muv
assume *: unit-disc-fix M u € unit-disc v € unit-disc u # v
assume *: ?P (moebius-pt M u) (moebius-pt M v)
show ?P uv
proof safe
fix dyz
assume ¥**: 0 < poincare-distance u y
y € unit-disc poincare-between uv y
z € unit-disc poincare-between uv z
poincare-distance u z = poincare-distance u y
let ?Mu = moebius-pt Mu and ?Mv = moebius-pt Mv and ?My = moebius-pt M y and ?Mz = moebius-pt M z
have ?Mu € unit-disc ?Mv € unit-disc ?My € unit-disc ?Mz € unit-disc
using <u € unit-disc) «v € unit-discy «y € unit-disc> «z € unit-disc»
using (unit-disc-fir My
by auto
hence ?My = ?Mz
using * ***
using **[rule-format, of poincare-distance ?Mu ?My ?My ?Mz]
by simp
thus y = z
using bij-moebius-pt[of M]
unfolding bij-def inj-on-def
by blast
qed
qed
thus ?thesis
using assms
by auto
qed

end

theory Poincare-Lines-Axis-Intersections
imports Poincare-Between

begin
