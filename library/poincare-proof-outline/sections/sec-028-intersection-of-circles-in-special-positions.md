---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-028-intersection-of-circles-in-special-positions
section_title: "Intersection of circles in special positions"
section_number: null
pages: 71-74
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Two h-circles centered at the x-axis intersect at mutually conjugate points

lemma intersect-poincare-circles-x-axis:

71
assumes 2: is-real z1 and is-real z2 and rl > 0 and r2 > 0 and
—1 < Re zl and Re z1 < 1 and —1 < Re 22 and Re z2 < 1 and
zl # 22
assumes 21: r1 € poincare-circle (of-complex z1) r1 M poincare-circle (of-complex 22) r2 and
x2: x2 € poincare-circle (of-complez z1) r1 M poincare-circle (of-complez z2) r2 and
vl # x2
shows r1 = conjugate 72
proof—
have in-disc: of-complex z1 € unit-disc of-complex z2 € unit-disc
using assms
by (auto simp add: cmod-eq-Re)

obtain x1’ 22’ where x’: x1 = of-complex x1‘ 12 = of-complex x2’
using x1 «2
using inf-or-of-complez|of x1] inf-or-of-complez|of x2]
unfolding poincare-circle-def
by auto

obtain Ze1 Rel where 1: (Ze1, Rel) = poincare-circle-euclidean (of-complex z1) r1
by (metis poincare-circle-euclidean-def )
obtain Ze2 Re2 where 2: (Ze2, Re2) = poincare-circle-euclidean (of-complex z2) r2
by (metis poincare-circle-euclidean-def )
have circle: x1’ € circle Ze1 Re1 M circle Ze2 Re2 x2' € circle Zel Rel M circle Ze2 Re2
using poincare-circle-is-euclidean-circle[of of-complex z1 r1]
using poincare-circle-is-euclidean-circle|of of-complex 22 r2]
using assms 1 2 <of-complex z1 € unit-disc» ‘of-complex z2 € unit-disc> x’
by auto (metis image-iff of-complez-inj)+

have is-real Ze1 is-real Ze2
using 1 2 <is-real z1) <is-real 22»
by (simp-all add: poincare-circle-euclidean-def Let-def )

have Rel > 0 Re2 > 0
using 1 2 in-disc (rl > 0» «r2 > 0»
using poincare-circle-in-disc(2)[of r1 of-complex z1 Ze1 Re1]
using poincare-circle-in-disc(2)|of r2 of-complex z2 Ze2 Re2]
by auto

have Zel # Ze2
proof (rule ccontr)
assume — ?thesis
hence eq: Zel = Ze2 Rel = Re2
using circle(1)
unfolding circle-def
by auto

let ?A = Zel — Rel and ?B = Zel + Rel
have ?A € circle Ze1 Rel ?B € circle Ze1 Rel
using (Rel > 0»
unfolding circle-def
by simp-all

hence of-compler ?A € poincare-circle (of-complex z1) r1 of-complex ?B € poincare-circle (of-complex z1) r1
of-complex ?A € poincare-circle (of-complex z2) r2 of-complex ?B € poincare-circle (of-complex z2) r2

using eq

using poincare-circle-is-euclidean-circle|OF ‘of-complex z1 € unit-disc» «rl > 0>]
using poincare-circle-is-euclidean-circle|OF ‘of-complex 22 € unit-disc» «r2 > 0>]
using 1 2

by auto blast+

hence poincare-distance (of-complex z1) (of-complex ?A) = poincare-distance (of-complex z1) (of-complex ?B)
poincare-distance (of-complex z2) (of-complex ?A) = poincare-distance (of-complex z2) (of-complex ?B)
—1 < Re (Ze1 — Rel) Re (Zel — Rel) < 1 -1 < Re (Zel + Rel) Re (Zel + Rel) < 1

using <is-real Ze1) <is-real Ze2>
unfolding poincare-circle-def
by (auto simp add: cmod-eq-Re)
hence z1 = 22
using unique-midpoint-x-axis|of Zel — Rel Ze1 + Rel]

72
using <is-real Ze1> <is-real z1) <is-real 22) «Rel > 0) «—1 < Re 21) «Re z1 < 1) ‘-1 < Re 22) (Re 22 < 1»
by auto
thus False
using (zl # 22>
by simp
qed

hence *: (Re x1’)? + (Im a1’)? — 2 * Re x1'* Zel + Zel * Zel — cor (Rel * Rel) = 0
(Re a1’)? + (Im x1’)? — 2 * Re xl’ * Ze2 + Ze2 * Ze2 — cor (Re2 * Re2) = 0

(Re 22')? + (Im 22")? — 2 * Re 12'* Zel + Zel * Zel — cor (Rel * Rel) = 0
(Re 22’)? + (Im 22")? — 2 * Re «2'* Ze2 + Ze2 * Ze2 — cor (Re2 * Re2) = 0
using circle-equation|of Re1 Ze1] circle-equation|of Re2 Ze2] circle
using eq-cnj-iff-real[of Ze1] <is-real Ze1» «Rel > 0»
using eq-cnj-iff-real[of Ze2] <is-real Ze2» «Re2 > 0»
using complez-add-cnjlof x1'| complex-add-cnj{of x2']
using distrib-left{of Ze1 x1' cnj x1'| distrib-left{of Ze2 x1’ cnj x1'|
using distrib-left[of Ze1 x2’ cnj x2'| distrib-left{of Ze2 12’ enj 12’
by (auto simp add: complex-mult-cnj power2-eq-square field-simps)
hence — 2 * Real’ * Ze1 + Zel « Zel — cor (Rel * Rel) = — 2 * Real’ * Ze2 + Ze2 * Ze2 — cor (Re2 * Re2)

— 2 Re x2'* Zel + Zel * Zel — cor (Rel * Rel) =— 2 * Re x2' * Ze2 + Ze2 * Ze2 — cor (Re2 * Re2)
by (smt add-diff-cancel-right' add-diff-eq eq-iff-diff-eq-0 minus-diff-eq mult-minus-left of-real-minus)+
hence 2 « Re x1’ * (Ze2 — Zel) = (Ze2 * Ze2 — cor (Re2 * Re2)) — (Zel * Zel — cor (Rel * Rel1))
2% Re x2'* (Ze2 — Zel) = (Ze2 * Ze2 — cor (Re2 * Re2)) — (Zel *« Zel — cor (Rel * Rel))
by simp-all (simp add: field-simps)+
hence 2 « Re w1' « (Ze2 — Zel) = 2 * Re x2' * (Ze2 — Zel)
by simp
hence Re r1' = Re x2
using (Zel # Ze2)
by simp
moreover
hence (Im x1’)? = (Im x2’)?
using *(1) *(3)
by (simp add: <is-real Ze1> complex-eq-if-Re-eq)

hence Im x1' = Im 22'V Im «1' = —Im 22’
using power2-eq-iff
by blast

ultimately

show ?thesis
using x’ (rl A 72>
using complez.expand
by (metis cnj.code complex-surj conjugate-of-complex)
qed

Two h-circles of the same radius centered at mutually conjugate points intersect at the x-axis

lemma intersect-poincare-circles-conjugate-centers:
assumes in-disc: z1 € unit-disc z2 € unit-disc and
z1 # 22 and 21 = conjugate z2 and r > 0 and
u: u € poincare-circle z1 r M poincare-circle 22 r
shows is-real (to-complex u)
proof—
obtain zle rle z2e r2e where
euclidean: (zle, rle) = poincare-circle-euclidean z1 r
(z2e, r2e) = poincare-circle-euclidean 22 r
by (metis poincare-circle-euclidean-def )
obtain z1’ 22’ where z’: z1 = of-complex z1' 22 = of-complex 22’
using inf-or-of-complez|of z1| inf-or-of-complez|of z2| in-disc
by auto
obtain u’ where wu’: u = of-complex u’
using w inf-or-of-complez|of u]
by (auto simp add: poincare-circle-def)
have 21! = cnj 22’
using (21 = conjugate 22> z’
by (auto simp add: of-complex-inj)
moreover
let ?cz = 1 — (cmod 22")?
let ?den = ?cz * (coshr — 1)/2+1
have ?cz > 0
using in-disc z’
by (simp add: cmod-def)
hence ?den > 1
using cosh-gt-1[OF «<r > 0>]
by auto
hence ?den 4 0
by simp
hence cor ?den # 0
using of-real-eq-0-iff
by blast
ultimately
have rile = re zle = cnj z2e zle # z2e
using z’ euclidean «z1 #4 22>
unfolding poincare-circle-euclidean-def Let-def
by simp-all metis

hence u’ € circle (cnj z2e) r2e N circle 22e r2e z2e A cnj z2e
using euclidean u u’
using poincare-circle-is-euclidean-circle[of 21 r]
using poincare-circle-is-euclidean-circle[of 22 r]
using in-disc «r > 0»
by auto (metis image-iff of-complez-inj)+

hence (cmod (u’ — 22e))? = (emod(u’ — enj z2e))?
by (simp add: circle-def)
hence (u’ — 22e) « (cnj u’ — cnj z2e) = (u’ — cnj z2e) * (enj u’ — z2e)

by (metis complex-cnj-cnj complex-cnj-diff complex-norm-square)
hence (z2e — cnj 22e) * (u’ — enj u') = 0
by (simp add: field-simps)
thus ?thesis
using wu’ (z2e # cnj z2e) eq-cnj-iff-reallof u’|
by simp
qed
