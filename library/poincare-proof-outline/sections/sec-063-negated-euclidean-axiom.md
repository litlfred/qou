---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-063-negated-euclidean-axiom
section_title: "Negated Euclidean axiom"
section_number: null
pages: 143-150
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma negated-euclidean-axiom-auz:
assumes on-circline H (of-complex (1/2 + i/2)) and is-poincare-line H
assumes intersects-z-axis-positive H
shows -— intersects-y-axis-positive H
using assms
proof (transfer, transfer)
fix H
assume hh: hermitean H \ H # mat-zero is-poincare-line-cmat H
obtain A B C D where H = (A, B, C, D)
by (cases H, auto)
hence «: is-real A H = (A, B, enj B, A) (cmod B)? > (emod A)?
using hermitean-elems|of A B C D] hh
by auto

assume intersects-x-azis-positive-cmat H
hence Re A# 0 Re B/ Re A<- 1
using *
by auto

assume on-circline-cmat-cvec H (of-complex-cvec (1 / 2 +i/ 2))
hence 6*A + 4*Re B+ 4*Im B= 0

using *

unfolding of-real-mult

apply (subst Re-express-cnjlof B))

143
apply (subst Im-express-cnj{of B])
apply (simp add: vec-cnj-def)
apply (simp add: field-simps)
done
hence Re (6*A + 4*Re B+ 4*Im B) = 0
by simp
hence 3*Re A + 2xRe B + 2xIm B= 0
using <is-real A»
by simp

hence 3/2 + Re B/Re A+ Im B/Re A= 0
using «Re A # 0)
by (simp add: field-simps)

hence —Im B/Re A — 3/2 < -1
using (Re B / Re A < —1)
by simp

hence Im B/Re A > —1/2
by (simp add: field-simps)

thus — intersects-y-azis-positive-cmat H
using *
by simp

qed

lemma negated-euclidean-axiom:
shows J abcdt.
a € unit-disc \ b € unit-disc \ c € unit-disc A d € unit-dise A t € unit-disc A
poincare-between a d t A poincare-betweenbdcA\a#dA
(V vy. x € unit-disc A y € unit-disc \
poincare-between a b x A poincare-between x t y —+ — poincare-between ac y)
proof—
let ?a = On
let 2b = of-complez (1/2)
let 2c = of-complex (i/2)
let ?dl = (5 — sqrt 17) / 4
let ?d = of-complex (?dl + ix ?dl)
let ?t = of-complex (1/2 + i/2)

have ?dl 4 0
proof—
have (sqrt 172)? 4 5?
by simp
hence sqrt 17 4 5
by force
thus ?thesis
by simp
qed
have ?d # ?a

proof (rule ccontr)
assume — ?thesis
hence ?dl + ix?dl = 0
by simp
hence Re (?dl + ix?dl) = 0
by simp
thus False
using <?dl # 0)
by simp
qed

have ?dl > 0
proof—
have (sqrt 172)? < 5?
by (simp add: power2-eq-square)
hence sqrt 17 < 5
by (rule power2-less-imp-less, simp)

144
thus ?thesis
by simp
qed

have 7a # 7b
by (metis divide-eq-0-iff of-complex-zero-iff zero-neq-numeral zero-neq-one)

have 7a # ?c
by (metis complex-i-not-zero divide-eq-0-iff of-complex-zero-iff zero-neq-numeral)

show ?thesis
proof (rule-tac x= ?a in exl, rule-tac =?b in erl, rule-tac c=?c in exl, rule-tac c=?d in exl, rule-tac c= ?t in eal,

safe)

show 7a € unit-disc ?b € unit-disc ?c € unit-disc ?t € unit-disc
by (auto simp add: cmod-def power2-eq-square)

have cmod-d: cmod (?dl + ix?dl) = ?dl * sqrt 2
using <?dl > 0)
unfolding cmod-def
by (simp add: real-sqrt-mult)

show ?d € unit-disc
proof —
have ?dl < 1 / sqrt 2
proof—
have 172° < (5 « sqrt 172)?
by (simp add: field-simps)
hence 17 < 5 * sqrt 17
by (rule power2-less-imp-less, simp)
hence ?dl? < (1 / sqrt 2)?
by (simp add: power2-eq-square field-simps)
thus ?dl < 1 / sqrt 2
by (rule power2-less-imp-less, simp)
qed
thus ?thesis
using cmod-d
by (simp add: field-simps)
qed

have cmod-d: 1 — (cmod (to-complex ?d))? = (—17 + Sxsqrt 17) / 4 (is - = ?emod-d)
apply (simp only: to-complex-of-complex)
apply (subst cmod-d)
apply (simp add: power-mult-distrib)
apply (simp add: power2-eq-square field-simps)
done

have cmod-d-c: (cmod (to-complex ?d — to-complex ?c))? = (17 — 4xsqrt 17) / 4 (is - = ?cmod-de)
unfolding cmod-square
by (simp add: field-simps)

have cmod-c: 1 — (cmod (to-complex ?c))? = 3/4 (is - = ?cmod-c)
by (simp add: power2-eq-square)

have rz: A v:real. c+ x = 2xa
by simp

have cmod ((to-complez ?b) — (to-complex ?d)) = cmod ((to-complex ?d) — (to-complez ?c))
by (simp add: cmod-def power2-eq-square field-simps)

moreover

have cmod (to-complex ?b) = cmod (to-complex ?c)
by simp

ultimately

have *: poincare-distance-formula’ (to-complex ?b) (to-complex ?d) =

poincare-distance-formula' (to-complex ?d) (to-complex ?c)

145
unfolding poincare-distance-formula’-def
by simp

have *«: poincare-distance-formula’ (to-complex ?d) (to-complex ?c) = (sqrt 17) / 3
unfolding poincare-distance-formula’-def

proof (subst cmod-d, subst cmod-c, subst cmod-d-c)
have (sqrt 17 * 152)? # 512?

by simp

hence sqrt 17 * 15 # 51
by force

hence sqrt 17 « 15 — 51 #0
by simp

have (5 * sqrt 172)? 4 172°

by simp

hence 5 * sqrt 17 4 17
by force

hence ?cmod-d « ?cmod-c 4 0
by simp

hence 1 + 2 « (?cmod-de / (?cmod-d * ?cmod-c)) = (?cmod-d * ?cmod-c + 2 « ?emod-dc) / (?cmod-d * ?cmod-c)
using add-frac-num|of ?cmod-d * ?cmod-c 2 * ?cmod-dc 1]
by (simp add: field-simps)

also have ... = (64 * (85 — sqrt 17 « 17)) / (64 * (sqrt 17 * 15 — 51))
by (simp add: field-simps)

also have ... = (85 — sqrt 17 * 17) / (sqrt 17 * 15 — 51)
by (rule mult-divide-mult-cancel-left, simp)

also have ... = sqrt 17 / 3
by (subst frac-eq-eq, fact, simp, simp add: field-simps)

finally

show 1 + 2 « (?cemod-dc / (?cmod-d * ?cmod-c)) = sqrt 17 / 3
qed

have sqrt 17 > 3
proof —
have (sqrt 172)? > 3?
by simp
thus ?thesis
by (rule power2-le-imp-le, simp)
qed
thus poincare-between ?b ?d ?c
unfolding poincare-between-sum-distances|OF «?b € unit-disc» «?d € unit-disc» «?c € unit-disc»]
unfolding poincare-distance-formula[OF «?b € unit-disc» «?d € unit-disc»]
unfolding poincare-distance-formula[OF «?d € unit-discy «?c € unit-disc»]
unfolding poincare-distance-formula[OF «?b € unit-disc» «?c € unit-disc»]
unfolding poincare-distance-formula-def
apply (subst *, subst rx, subst **, subst arcosh-double)
apply (simp-all add: cmod-def power2-eq-square)
done

show poincare-between ?a ?d ?t
proof (subst poincare-between-Quv[OF «?d © unit-discy «?t € unit-discy «?d # ?a])
show ?t 4 0n
proof (rule ccontr)
assume 7— ?thesis
hence 1/2 + i/2 =0
by simp
hence Re (1/2 + i/2) = 0
by simp
thus False
by simp
qed
next
have 192? < (5 * sqrt 172)?
by simp
hence 19 < 5 * sqrt 17

146
by (rule power2-le-imp-le, simp)
hence cmod (to-complex ?d) < cmod (to-complex ?t)

by (simp add: Let-def cmod-def power2-eq-square field-simps)
moreover
have Arg (to-complex ?d) = Arg (to-complex ?t)
proof—

have 1: to-complex ?d = ((5 — sqrt 17) / 4) * (1 +i)

by (simp add: field-simps)

have 2: to-complex ?t = (cor (1/2)) * (1 + i)
by (simp add: field-simps)

have (sqrt 172)? < 5?

by simp
hence sqrt 17 < 5

by (rule power2-less-imp-less, simp)
hence 3: (5 — sqrt 17) /4>0

by simp

have 4: (L::real) / 2 > 0
by simp

show ?thesis
apply (subst 1, subst 2)
apply (subst arg-mult-real-positive|OF 3])
apply (subst arg-mult-real-positive|OF 4])
by simp
qed
ultimately
show let d' = to-complex ?d; t' = to-complex ?t in Arg d’ = Arg t' \ cmod d’ < cmod t’
by simp
qed

show ?a = ?d => False
using <(?d # ?a>
by simp

fix ry
assume z € unit-disc y € unit-disc

assume abz: poincare-between ?a ?b x

hence z € circline-set r-axis
using poincare-between-poincare-line-uvz[of 2a ?b x] «x € unit-discr «?a # 2b»
using poincare-line-0-real-is-z-axis|of ?b|
by (auto simp add: circline-set-x-axis)

have « # On,
using abzx poincare-between-sandwich|of ?a ?b] «?a # ?b»
by auto

have x € positive-x-axis
using <x € circline-set r-avis) (x # On) <x € unit-discy
using abz poincare-between-x-axis-Ouvlof 1/2 Re (to-complex x)|
unfolding circline-set-x-axis positive-x-axis-def
by (auto simp add: cmod-eq-Re abs-less-iff complex-eq-if-Re-eq)

assume acy: poincare-between ?a ?c y

hence y € circline-set y-axis
using poincare-between-poincare-line-uvz[of 2a ?c y| ‘y € unit-discr «?a # ?e>
using poincare-line-0-imag-is-y-axis|of ?c]
by (auto simp add: circline-set-y-azis)

have y 4 0n

using acy poincare-between-sandwich|of ?a ?c] «?a # ?cr
by auto

147
have y € positive-y-axis
proof —
have (xz. [x 4 0; poincare-between 0p (of-complex (i / 2)) (of-complex x); is-imag x; — 1 < Im x] = 0 < Imax
by (smt add.left-neutral complex.expand divide-complex-def complex-eq divide-less-0-1-iff divide-less-eq-1-pos imagi-
nary-unit.simps(1) mult.left-neutral of-real-1 of-real-add of-real-divide of-real-eq-0-iff one-add-one poincare-between-y-axis-Ouv
zero-complex.simps(1) zero-complex.simps(2) zero-less-divide-1-iff)
thus ?thesis
using <y € circline-set y-axis) (y A On> <y € unit-disc)
using acy
unfolding circline-set-y-axis positive-y-azis-def
by (auto simp add: cmod-eq-Im abs-less-iff)
qed

have « # y
using <x € positive-x-axis) <y € positive-y-axis)
unfolding positive-z-azis-def positive-y-azis-def circline-set-x-axis circline-set-y-azxis
by auto

assume zty: poincare-between x ?t y
let ?xy = poincare-line x y

have ?t € circline-set ?xy
using xty poincare-between-poincare-line-uzv|OF «x # y» (xz € unit-disc» <y € unit-discy «?t € unit-dise>]
by simp

moreover

have ?ry 4 z-axis
using poincare-line-circline-set|OF «x # y>] <y € positive-y-azis»
by (auto simp add: circline-set-x-axis positive-y-axis-def)
hence intersects-x-axis-positive ?xy
using intersects-z-axis-positive-iff [of ?xy] «x # y» (x € unit-disc» (x € positive-z-azis»
by auto

moreover

have ?ry # y-azis
using poincare-line-circline-set|OF «x # y>] «x € positive-z-axis»
by (auto simp add: circline-set-y-azis positive-z-axis-def )
hence intersects-y-azis-positive ?ry
using intersects-y-axis-positive-iff|of ?xy] «x # y> ‘y € unit-disc <y € positive-y-azis)
by auto

ultimately

show False
using negated-euclidean-ariom-auzlof fry] «x # y>
unfolding circline-set-def
by auto
qed
qed

Alternate form of the Euclidean axiom — this one is much easier to prove

lemma negated-euclidean-axiom':
shows J abc.
a € unit-disc \ b € unit-disc A c € unit-disc A 7(poincare-collinear {a, b, c}) A
(4 a. x € unit-dise A
poincare-distance a x = poincare-distance b x
poincare-distance a x = poincare-distance c x)
proof—
let 2a = of-complex (i/2)
let. 2b = of-complex (—i/2)
let 2c = of-complex (1/5)

have (i/2) 4 (-i/2)

148
by simp
hence ?a 4 7b

by (metis to-complex-of-complex)
have (i/2) 4 (1/5)

by simp
hence ?a 4 ?c

by (metis to-complex-of-complex)
have (—i/2) 4 (1/5)

by (simp add: minus-equation-iff)
hence ?b # ?c

by (metis to-complex-of-complex)

have 7a € unit-disc ?b € unit-disc ?c € unit-disc
by auto

moreover
have ~(poincare-collinear {?a, ?b, ?c})
unfolding poincare-collinear-def
proof (rule ccontr)
assume -— (fp. is-poincare-line p \ {?a, 2b, ?c} C circline-set p)
then obtain p where is-poincare-line p A {?a, ?b, ?c} C circline-set p
by auto
let ?ab = poincare-line ?a ?b
have p = ?ab
using <is-poincare-line p \ {?a, ?b, ?c} C circline-set p>
using unique-poincare-line[of ?a ?b] «?a # ?b» «?a € unit-disc» «?b € unit-dise»
by auto
have ?c ¢ circline-set ?ab
proof (rule ccontr)
assume — ?c ¢ circline-set ?ab
have poincare-between ?a On ?b
unfolding poincare-between-def
using cross-ratio-Oinf by auto
hence 0), € circline-set ?ab
using <?a £ 2b» <?a © unit-disc) «?b € unit-discy
using poincare-between-poincare-line-uzv zero-in-unit-disc
by blast
hence ?ab = poincare-line 0n ?a
using unique-poincare-line[of ?a ?b| «?a # 2b» «?a © unit-disc> «?b € unit-disc»
using <is-poincare-line p A {?a, ?b, ?c} C circline-set p>
using <p = ?ab» poincare-line-circline-set(1) unique-poincare-line
by (metis add.inverse-neutral divide-minus-left of-complex-zero-iff zero-in-unit-disc)
hence (i/2) * enj(1/5) = enj(i/2) * (1/5)
using poincare-collinear-zero-iff [of (i/2) (1/5)|
using (?a # ?c) (4 ?c € circline-set ?ab> «?a € unit-discr «?c € unit-disc> «p = ?ab»
using (On € circline-set ?ab) <is-poincare-line p \ {?a, ?b, ?c} C circline-set p»
using poincare-collinear-def by auto
thus False
by simp
qed
thus False
using <p = ?ab» <is-poincare-line p \ {?a, ?b, ?c} C circline-set p>
by auto
qed

moreover

have =(S a. x € unit-disc \
poincare-distance ?a % = poincare-distance 2b % A
poincare-distance ?a x = poincare-distance ?c 2)
proof (rule ccontr)
assume — ?thesis
then obtain z where z € wnit-disc poincare-distance ?a x = poincare-distance ?b ©
poincare-distance ?a x = poincare-distance ?c x
by blast
let ?x = to-complex x

149
have poincare-distance-formula’ (i/2) ?« = poincare-distance-formula’ (—i/2) ?x
using <poincare-distance ?a x = poincare-distance ?b x)
using <x € unit-disc> (2a € unit-disc» «2b € unit-discy
by (metis cosh-dist to-complez-of-complex)

hence (cmod (i / 2 — ?x))? = (emod (—i/ 2 — ?z))?
unfolding poincare-distance-formula’-def
apply (simp add:field-simps)
using <x € unit-disc) unit-disc-cmod-square-lt-1 by fastforce

hence Im ?x = 0
unfolding cmod-def
by (simp add: power2-eq-iff )

have 1 — (Re ?x)? £0
using <x € unit-disc> unit-disc-cmod-square-lt-1
using cmod-power2 by force

hence 24 — 24 * (Re ?x)? # 0
by simp

have poincare-distance-formula’ (i/2) 2x = poincare-distance-formula’ (1/5) ?x
using <poincare-distance ?a x = poincare-distance ?c x)
using <x € unit-disc» (2a € unit-disc» (2c € unit-discy
by (metis cosh-dist to-complez-of-complez)

hence (2 + 8 * (Re ?x)*) /(3 — 3 * (Re ?x)*) = 2 * (1 — Re ?x * 5)” / (24 — 24 * (Re ?x)°) (is ?lhs = ?rhs)
unfolding poincare-distance-formula’-def
apply (simp add:field-simps)
unfolding cmod-def
using <Im ?x = 0>
by (simp add:field-simps)

hence +: ?lhs « (24 — 24 « (Re ?x)”) = ?rhs * (24 — 24 * (Re ?x)*)
using «(24 — 24 * (Re ?x)*) 4 0
by simp

have ?lhs « (24 — 24 « (Re ?x)) = (2 + 8 « (Re ?x)”) * 8
using «(24 — 24 * (Re ?x)) # 0» «1 — (Re ?x)? £ 0»
by (simp add:field-simps)

have ?rhs * (24 — 24 * (Re ?x)?) = 2 * (1 — Re ?a « 5)?
using «(24 — 24 * (Re ?x)*) 4 0) «1 — (Re ?x)? 4 0»
by (simp add:field-simps)

hence (2 + 8 * (Re ?x)*) * 8 = 2% (1 — Re ?a * 5)?
using « (?lhs * (24 — 24 * (Re ?x)?) = (2 + 8 * (Re ?x)”) * 8
by simp

hence 7 * (Re ?x)? + 10 * (Re x) + 7=0
by (simp add:field-simps comm-ring-1-class.power2-diff )

thus False
using discriminant-iff[of 7 Re (to-complex x) 10 7| discrim-def|of 7 10 7)
by auto

qed

ultimately show ?thesis
apply (rule-tac r= ?a in ex!)
apply (rule-tac 2b in ez!)
apply (rule-tac c= ?c in ez)
by auto
qed
