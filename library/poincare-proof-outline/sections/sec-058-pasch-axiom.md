---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-058-pasch-axiom
section_title: "Pasch axiom"
section_number: null
pages: 127-138
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma Pasch-fun-mono:
fixes rl r2 :: real
assumes (0 < rl and rl < r2 and r2 < 1
shows rl + 1/r1 > r2 + 1/r2
proof (cases rl = r2)
case True
thus ?thesis
by simp
next
case False
hence r2 — rl > 0
using assms
by simp

have rl * r2 < 1
using assms
by (smt mult-le-cancel-left1)
hence 1 / (ri * r2) > 1
using assms
by simp
hence (r2 — rl) / (ri « r2) > (r2 — rl)
using (r2 — rl > 0»
using mult-less-cancel-left-pos[of r2 — rl 11 / (r1 * r2)]
by simp
hence 1 /ri—1/7r2>r2-r1
using assms
by (simp add: field-simps)
thus ?thesis
by simp

127
qed
Pasch axiom, non-degenerative case.

lemma Pasch-nondeg:
assumes « € unit-disc and y € unit-disc and z € unit-disc and u € unit-disc and v € unit-disc
assumes distinct [x, y, z, u, v]
assumes — poincare-collinear {x, y, z}
assumes poincare-between xz u z and poincare-between y v z
shows J a. a € unit-disc \ poincare-between u ay A poincare-between © av
proof—
have V yz u. distinct [z, y, z, u, uv] A 7 poincare-collinear {x, y, z} \ y € unit-disc \ z € unit-disc A u € unit-disc A
poincare-between x u z A poincare-between y v z —> (4 a. a € unit-disc A poincare-between ua y A
poincare-between x av) (is ?P x v)
proof (rule wlog-positive-x-azis[;where P=?P])
fix v
assume uv: is-real v 0 < Rev Rev < 1
hence of-complez v € unit-disc
by (auto simp add: cmod-eq-Re)
show ?P 0;, (of-complex v)
proof safe
fix yzu
assume distinct: distinct [On, y, 2, u, of-complex v|
assume in-disc: y € unit-disc z € unit-disc u € unit-disc
then obtain y’ 2’ u’
where «: y = of-complex y’ z = of-complex z' u = of-complex u'
using inf-or-of-complex inf-notin-unit-disc
by metis

have y'4A0z'A Ou AOVA OY Fz y Au 2 Aw yAzyAuzsu
using of-complez-inj distinct *
by auto

note distinct = distinct this
assume 7~ poincare-collinear {On, y, z}

hence nondeg-yz: y’*cnj z' # cnj y’ * 2’
using * poincare-collinear-zero-iff|of y' z'| in-disc distinct
by auto

assume poincare-between On uz

hence Arg u’ = Arg z' cmod u' < cmod z'
using * poincare-between-Ouvlof u z] distinct in-disc
by auto

then obtain y ru rz where
uz-polar: u' = cor ru * cis p z' = corrz * cise 0 < ruru<rz0 <rzand
y = Arg u! p = Arg z'
using « <u’ A 0) «z' A 0»
by (smt cmod-cis norm-le-zero-iff)

obtain 0 ry where
y-polar: y’ = cor ry * cis 0 ry > 0 and J = Arg y'
using «y’ 4 0»
by (smt cmod-cis norm-le-zero-iff)

from in-disc * <u’ = cor ru * cis yp» (z' = cor rz * cis p> <y’ = cor ry * cis 9)
have ru<1lrz<1lry<1
by (auto simp: norm-mult)
note polar = this y-polar uz-polar
have nondeg: cis 0 « cis (— vy) # cis (— V) * cis p

using nondeg-yz polar
by simp

128
let ?yz = poincare-line y z
let ?v = calc-z-azis-intersection ?yz

assume poincare-between y (of-complex v) z

hence of-complex v € circline-set ?yz
using in-disc <of-complex v € unit-disc»
using distinct poincare-between-poincare-collinear|of y of-complex v z|
using unique-poincare-line[of y z]
by (auto simp add: poincare-collinear-def )
moreover
have of-complex v € circline-set x-axis
using <is-real v)
unfolding circline-set-x-azxis
by auto
moreover
have ?yz # x-axis
proof (rule ccontr)
assume 7— ?thesis
hence {0n, y, z} C circline-set (poincare-line y z)
unfolding circline-set-def
using distinct poincare-linelof y 2]
by auto
hence poincare-collinear {On, y, z}
unfolding poincare-collinear-def
using distinct
by force
thus False
using (- poincare-collinear {On, y, z}>
by simp
qed
ultimately
have ?v = of-complez v intersects-z-azis ?yz
using unique-calc-a-azis-intersection|of poincare-line y z of-complex v]
using intersects-x-azis-iff[of ?yz]
using distinct <of-complex v € unit-disc»
by (metis Intl is-poincare-line-poincare-line) +

have intersects-x-azis-positive ?yz
using «Re v > 0» <of-complex v € unit-disc»
using <of-complex v € circline-set ?yz» <of-complex v € circline-set x-axis)
using intersects-x-azis-positive-iff [of ?yz| <y # z» <?yz # x-axis)
unfolding positive-x-azis-def
by force

have y ¢ circline-set x-axis
proof (rule ccontr)
assume 7— ?thesis
moreover
hence poincare-line y (of-complez v) = x-axis
using distinct <of-complex v € circline-set x-axis)
using in-disc <of-complex v € unit-disc»
using wnique-poincare-line[of y of-complex v x-axis]
by simp
moreover
have z € circline-set (poincare-line y (of-complez v))
using <of-complex v € circline-set ?yz)
using wnique-poincare-line[of y of-complex v poincare-line y 2]
using in-disc <of-complex v € unit-disc) distinct
using poincare-line[of y z]
unfolding circline-set-def
by (metis distinct-length-2-or-more is-poincare-line-poincare-line mem-Collect-eq)
ultimately
have y € circline-set z-axis z € circline-set x-axis
by auto

129
hence poincare-collinear {On, y, z}
unfolding poincare-collinear-def
by force
thus False
using (- poincare-collinear {On, y, z}>
by simp
qed

moreover

have z ¢ circline-set z-axis
proof (rule ccontr)
assume 7— ?thesis
moreover
hence poincare-line z (of-complex v) = z-axis
using distinct <of-complex v € circline-set x-axis)
using in-disc <of-complex v € unit-disc»
using wnique-poincare-line|of z of-complex v x-axis]
by simp
moreover
have y € circline-set (poincare-line z (of-complex v))
using <of-complex v € circline-set ?yz)
using wnique-poincare-line[of z of-complex v poincare-line y 2]
using in-disc <of-complex v € unit-disc) distinct
using poincare-line[of y z]
unfolding circline-set-def
by (metis distinct-length-2-or-more is-poincare-line-poincare-line mem-Collect-eq)
ultimately
have y € circline-set z-axis z € circline-set x-axis
by auto
hence poincare-collinear {On, y, z}
unfolding poincare-collinear-def
by force
thus False
using (- poincare-collinear {On, y, z}>
by simp
qed

ultimately

have yp «0 < 0
using <poincare-between y (of-complex v) z>
using poincare-between-z-axis-intersection|of y z of-complex v]
using in-disc <of-complex v € unit-disc) distinct
using <of-complex v € circline-set ?yz» <of-complex v € circline-set x-axis)
using «yg = Arg 2’) «) = Arg y’> *
by (simp add: field-simps)

have » 4 piy #0
using (z ¢ circline-set z-axis) « polar cis-pi
unfolding circline-set-x-azxis
by auto

have 0 4 pil #0
using <y ¢ circline-set x-axis) * polar cis-pi
unfolding circline-set-x-azxis
by auto

have phi-sin: p > 0 +> sing >09<0+¢— sing <0
using «yp = Arg z) «(p 4 0 «yp F pi»
using Arg-bounded|of z'|
by (smt sin-gt-zero sin-le-zero sin-pi-minus sin-0-iff-canon sin-ge-zero)+

have theta-sin: 0 > 0 <> sind>O00 <0 + + sind < 0

using «0 = Arg y’) «0 4 0) «OF pir
using Arg-bounded|of y’]

130
by (smt sin-gt-zero sin-le-zero sin-pi-minus sin-0-iff-canon sin-ge-zero)+

have sin y * sind < 0
using <p * 0 < 0» phi-sin theta-sin
by (simp add: mult-less-0-iff)

have sin (yp — 0) # 0
proof (rule ccontr)
assume 7— ?thesis
hence sin (py — J) = 0
by simp
have — 2% pix p-Vy-—V< 2x pi
using «yp = Arg z’) « = Arg y’> Arg-bounded|[of z'| Arg-bounded[of y'] «p 4 pi» «8 # pir
by auto
hence yp —-0=-piVp-V=0Vp-V=pi
using «sin (p — ¥) = 0»
by (smt sin-0-iff-canon sin-periodic-pi2)
moreover
{
assume y — J = — pi
hence y = #3 — pi
by simp
hence False
using nondeg-yz
using <y’ = cor ry * cis 0» (z' = cor rz * cis yp (rz > 0» «ry > O>
by auto

}

moreover
{
assume y — J = 0
hence y = 3
by simp
hence False
using <y’ = cor ry * cis 0» (z' = cor rz * cis yp (rz > 0» «ry > O>
using nondeg-yz
by auto

}

moreover
{
assume y — J = pi
hence y = 0 + pi
by simp
hence False
using <y’ = cor ry * cis J) <z' = cor rz * cis yy «rz > 0» «ry > O»
using nondeg-yz
by auto
}
ultimately
show False
by auto
qed

have u ¢ circline-set z-axis
proof—
have — is-real u’
using * polar in-disc
using «p 4 0) «(p = Arg u (yp # pir phi-sin(1) phi-sin(2)
by (metis is-real-arg2)
moreover
have u #4 oop
using in-disc
by auto
ultimately
show ?thesis
using * of-complez-inj[of u’|
unfolding circline-set-x-axis

131
by auto
qed

let ?yu = poincare-line y wu

have nondeg-yu: y’ * cnj u' # cnj u' *« u!
using nondeg-yz polar «ru > 0» «rz > 0» distinct
by auto

fix r:: real
assume r > 0

have den: cor ry *« cis 0 * cnj 1 * cnj (corr * cis y) * 1 — corr * cis p * cnj 1 * cnj (cor ry * cis 0) * 140
using (0 < Tr) <0 < ry» nondeg
by auto

let 7A = 2% r * ry * sin(y — V)
let 7B =i (r* cis yp * (1 + ry?) — ry * cis 0 * (1 + 1°))
let ?ReB = ry * (1 +r?) * sin ¥ — r* (1 + ry?) * sing

have Re (i * (r * cis (—y) * ry * cis (V) — ry * cis (—V) * r * cis (y))) = ?A
by (simp add: sin-diff field-simps)
moreover
have cor ry * cis (— 9) * (cor ry * cis 0) = ry? corr * cis (— vy) * (corr * cis y) = 1?
by (metis cis-inverse cis-neq-zero divide-complex-def cor-squared nonzero-mult-div-cancel-right power2-eq-square
semiring-normalization-rules(15))+
ultimately
have 1: poincare-line-cvec-cmat (of-complex-cvec (cor ry * cis 0)) (of-complex-cvec (cor r * cis y)) = (?A, ?B,
cnj ?B, 2A)
using den
unfolding poincare-line-cvec-cmat-def of-complex-cvec-def Let-def prod.case
by (simp add: field-simps)

have 2: is-real ?A
by simp
let ?mix = cis 0 * cis (— y) — cis (— ¥) * cis yp
have is-imag ?mix
using eq-minus-cnj-iff-imag|of ?miz]
by simp
hence Im ?mix # 0
using nondeg
using complez.expand|of ?mix 0]
by auto
hence 3: Re 7A 4 0
using <r > 0) «ry > 0»
by (simp add: sin-diff field-simps)

have ?A 4 0
using 2 3
by auto
hence 4: cor ?A # 0
using 2 3
by (metis zero-complex.simps(1))

have 5: ?ReB / ?A = (sin J) / (2 * sin(y — ¥)) * (1/r + r) — (sin y) / (2 * sin (py — B)) * (1/ry + ry)
using (ry > 0) (r > 0»
apply (subst diff-divide-distrib)
apply (subst add-frac-num, simp)
apply (subst add-frac-num, simp)
apply (simp add: power2-eq-square mult.commute)
apply (simp add: field-simps)
done

have poincare-line-cvec-cmat (of-complex-cvec (cor ry * cis 0)) (of-complex-cvec (cor r * cis p)) = (?A, ?B, enj
?B, 2A) A

132
is-real 7A A Re ?A ZO A ?AZOA cor?AFON

Re ?B = ?ReB \

?ReB / ?A = (sin V) / (2 * sin(y — ¥)) * (1/r +r) — (sin y) / (2 * sin (p — B)) * (1/ry + ry)
using 12345
by auto

}

note ** = this

let ?Ayz = 2 * rz * ry * sin (p — V)
let ?Byz =i * (rz * cis p * (1 + ry?) — ry * cis 0 * (1 + 12”))
let ?ReByz = ry * (1 + rz”) * sin 0 — rz * (1 + ry?) * sing
let ?Kz = (sin ¥) / (2 * sin(y — ¥)) * (1/rz + rz) — (sin y) / (2 * sin (p — ¥)) * (1/ry + ry)
have yz: poincare-line-cvec-cmat (of-complex-cvec (cor ry * cis 9)) (of-complez-cvec (cor rz * cis y)) = (?Ayz,
?Byz, cnj ?Byz, ?Ayz)
is-real ?Ayz Re ?Ayz # 0 ?Ayz # 0 cor ?Ayz # O Re ?Byz = ?ReByz and Kz: ?ReByz / ?Ayz = ?Kz
using **[OF <0 < rz>]
by auto

let ?Ayu = 2 * ru « ry * sin (p — ¥)
let ?Byu =i * (ru « cis py * (1 + ry?) — ry * cis 0 * (1 + ru’))
let ?ReByu = ry * (1 + ru?) * sin 0 — ru * (1 + ry’) * sing
let ?Ku = (sin 0) / (2 * sin(y — ¥)) * (1/ru + ru) — (sin y) / (2 * sin (p — B)) * (1/ry + ry)
have yu: poincare-line-cvec-cmat (of-complex-cvec (cor ry * cis 9)) (of-complex-cvec (cor ru * cis y)) = (?Ayu,
?Byu, cnj ?Byu, ?Ayu)
is-real ?Ayu Re ?Ayu # 0 ?Ayu # 0 cor ?Ayu # O Re ?Byu = ?ReByu and Ku: ?ReByu / ?Ayu = ?Ku
using **[OF «0 < ru]
by auto

have ?Ayz # 0
using ‘sin (p — 0) 4 0» (ry > 0» «rz > Or
by auto

have Re ?Byz / ?Ayz < -1
using <intersects-x-axis-positive ?yz)
« <y’ = cor ry * cis 9) <z' = cor rz * cis yy <u! = cor ru * cis y>
apply simp
apply (transfer fixing: ry rz ru 0 ~)
apply (transfer fixing: ry rz ru 0 ~)
proof—
assume intersects-x-axis-positive-cmat (poincare-line-cvec-cmat (of-complez-cvec (cor ry * cis 0)) (of-complex-cvec
(cor rz * cis y)))
thus (ry * sin 0 * (1 + rz”) — rz * sine * (1 + ry”)) / (2 * rz * ry * sin(p — 9)) <-1
using yz
by simp
qed

have ?ReByz / ?Ayz > ?ReByu / ?Ayu
proof (cases sin y > 0)
case True
hence sin J) < 0
using ‘sin y * sin 0 < 0)
by (smt mult-nonneg-nonneg)

have ?ReByz < 0
proof—
have ry * (1 + 12?) * sind < 0
using (ry > 0» (rz > 0»
using <sin 0 < 0»
by (smt mult-pos-neg mult-pos-pos zero-less-power)
moreover
have rz « (1 + ry’) * sing > 0
using (ry > 0» (rz > 0»
using (sin yp > 0>
by (smt mult-pos-neg mult-pos-pos zero-less-power)
ultimately
show ?thesis

133
by simp
qed
have ?Ayz > 0
using (Re ?Byz / ?Ayz < —1> «Re ?Byz = ?ReByz> «?ReByz < 0>
by (smt divide-less-0-iff)
hence sin (y — J) > 0
using (ry > 0> «rz > 0»
by (smt mult-pos-pos zero-less-mult-pos)

have 1 /ru+ru>1/rz+rz
using Pasch-fun-monolof ru rz] «0 < rur (ru < rz «rz < 1>
by simp
hence sin 3 « (1 / ru+ ru) < sind * (1 / rz + rz)
using <sin 3 < 0»
by auto
thus ?thesis
using (ru > 0) (rz > 0» «ru < rz) (rz < 1) (?Ayz > 0» «sin (p — ¥) > O>
using divide-right-mono[of sin 0 * (1 / ru + ru) sin 0 x (1 / rz + rz) 2 * sin (yp — ¥)]
by (subst Kz, subst Ku) simp
next
assume — sin yp > 0
hence sin y < 0
using ‘sin y * sin 0 < 0)
by (cases sin p = 0, simp-all)
hence sin ) > 0
using ‘sin y * sin 0 < 0)
by (smt mult-nonpos-nonpos)
have ?ReByz > 0
proof—
have ry * (1 + 127) * sind > 0
using (ry > 0» (rz > 0»
using <sin 0 > 0»
by (smt mult-pos-neg mult-pos-pos zero-less-power)
moreover
have rz « (1 + ry’) * sing <0
using (ry > 0» (rz > 0»
using (sin p < 0>
by (smt mult-pos-neg mult-pos-pos zero-less-power)
ultimately
show ?thesis
by simp
qed
have ?Ayz < 0
using ‘Re ?Byz / ?Ayz < —1> «?Ayz # 0» (Re ?Byz = ?ReByz) (?ReByz > 0»
by (smt divide-less-0-iff)
hence sin (y — 3) < 0
using (ry > 0> «rz > 0»
by (smt mult-nonneg-nonneg)

have 1 /ru+ru>1/rz+rz
using Pasch-fun-monolof ru rz] «0 < rur (ru < rz «rz < 1>
by simp
hence sin 3 « (1 / ru+ ru) > sind * (1 / rz + rz)
using <sin 3 > 0»
by auto
thus ?thesis
using (ru > 0) (rz > 0» «ru < rz) (rz < 1) (?Ayz < 0» «sin (p — ¥) < O>
using divide-right-mono-neg|of sin 0 * (1 / rz + rz) sin 0 * (1 / rut ru) 2 * sin (p — ¥)]
by (subst Kz, subst Ku) simp

qed

have intersects-x-axis-positive ?yu
using * <y’ = cor ry * cis 0» (z' = cor rz * cis yy <u! = cor ru * cis y>
apply simp

apply (transfer fixing: ry rz ru 0 ~)
apply (transfer fixing: ry rz ru 0 ~)

134
proof—
have Re ?Byu / ?Ayu < -1
using (Re ?Byz / ?Ayz < —1> «?ReByz / ?Ayz > ?ReByu / ?Ayu
by (subst (asm) «Re ?Byz = ?ReByz>, subst «Re ?Byu = ?ReByu») simp
thus intersects-x-azis-positive-cmat (poincare-line-cvec-cmat (of-complez-cvec (cor ry * cis 0)) (of-complex-cvec
(cor ru * cis y)))
using yu
by simp
qed

let ?a = calc-x-axis-intersection ?yu

have ?a € positive-x-axis 2a € circline-set ?yu ?a € unit-disc
using <intersects-x-axis-positive ?yu)
using intersects-x-azis-positive-iff ‘lof ?yu] «y # wu
by auto

then obtain a’ where a’: ?a = of-complez a’ is-real a’ Re a' > 0 Rea’ < 1
unfolding positive-x-axis-def circline-set-x-axis
by (auto simp add: cmod-eq-Re)

have intersects-r-azxis ?yz intersects-z-aris ?yu
using <intersects-x-axis-positive ?yz) <intersects-x-axis-positive ?yu>
by auto

show Ja. a € unit-disc \ poincare-between u a y A poincare-between 0, a (of-complex v)
proof (rule-tac c= ?a in exI, safe)
show poincare-between u ?a y
using poincare-between-z-axis-intersection|[of y u ?a]
using calc-z-azis-intersection| OF is-poincare-line-poincare-line|OF «y # wu] <intersects-x-axis ?yu>]
using calc-z-azis-intersection-in-unit-disc| OF is-poincare-line-poincare-line|OF <y # wu] <intersects-x-axis ?yu>]
using in-disc ‘y # u> <y ¢ circline-set z-axis» «u ¢ circline-set z-axis»
using « «(p = Arg u «= Argy? «px v0 < 0»
by (subst poincare-between-rev, auto simp add: mult.commute)
next
show poincare-between 0; ?a (of-complex v)
proof—
have —?ReByz / ?Ayz < —?ReByu / ?Ayu
using <?ReByz / ?Ayz > ?ReByu / ?Ayw

by linarith

have outward ?yz ?yu
using * (y! = cor ry * cis 0) (z' = cor rz * cis yp (u' = cor ru * cis y>
apply simp

apply (transfer fixing: ry rz ru 0 ~)
apply (transfer fixing: ry rz ru 0 ~)
apply (subst yz yu)+
unfolding outward-cmat-def
apply (simp only: Let-def prod.case)
apply (subst yz yu)+
using ‘(—?ReByz / ?Ayz < —?ReByu / ?Ayur
by simp

hence Re a’ < Rev
using <?v = of-complex v»
using ‘?a = of-complez a'»
using <intersects-x-axis-positive ?yz) <intersects-a-axis-positive ?yu>
using outward[OF is-poincare-line-poincare-line|OF <y # z»| is-poincare-line-poincare-line|OF «y # w»]]
by simp

thus ?thesis
using <?v = of-complex v»
using poincare-between-zr-axis-Ouvlof Re a’ Re v| a’ v
by simp

qed
next
show 7a € unit-disc
by fact
qed
qed

135
next
show x € unit-disc v € unit-disc  £ v
using assms
by auto
next
fix Marv
let ?Mzx = moebius-pt M x and ?Mv = moebius-pt M v
assume 1: unit-disc-fix M x € unit-disc v € unit-disc « £ v
assume 2: ?P ?Mx ?Mv
show ?P xv
proof safe
fix yzu
let ?My = moebius-pt M y and ?Mz = moebius-pt M z and ?Mu = moebius-pt M u
assume distinct [z, y, z, u, v} > poincare-collinear {z, y, z} y € unit-disc z € unit-disc u € unit-disc
poincare-between x u z poincare-between y v z
hence 5 Ma. Ma € unit-disc \ poincare-between ?Mu Ma ?My A poincare-between ?Mx Ma ?Mv
using 1 2[rule-format, of ?My ?Mz ?Mu]
by simp
then obtain Ma where Ma: Ma € unit-disc poincare-between ?Mu Ma ?My \ poincare-between ?Mx Ma ?Mv
by blast
let ?a = moebius-pt (—M) Ma
let ?Ma = moebius-pt M ?a
have ?Ma = Ma
by (metis moebius-pt-invert uminus-moebius-def )
hence ?Ma € unit-disc poincare-between ?Mu ?Ma ?My A poincare-between ?Mx ?Ma ?Mv
using Ma
by auto
thus da. a € unit-disc \ poincare-between ua y A poincare-between x av
using unit-disc-fiz-moebius-inu|OF <unit-disc-fix M»] «unit-disc-fix M> (Ma © unit-disc»
using <u € unit-disc) «v € unit-discy «x € unit-disc) <y € unit-discy
by (rule-tac x=?a in exl, simp del: moebius-pt-comp-inv-right)
qed
qed
thus ?thesis
using assms
by auto
qed

Pasch axiom, only degenerative cases.

lemma Pasch-deg:
assumes « € unit-disc and y € unit-disc and z € unit-disc and u € unit-disc and v € unit-disc
assumes ~— distinct [z, y, z, u, v| V poincare-collinear {x, y, z}
assumes poincare-between xz u z and poincare-between y v z
shows J a. a € unit-disc \ poincare-between u ay A poincare-between © av
proof(cases poincare-collinear {x, y, z})
case True
hence poincare-between x y z V poincare-between y x z V poincare-between y zx
using assms(1, 2, 3) poincare-collinear3-between poincare-between-rev by blast
show ?thesis
proof (cases poincare-between x y z)
case True
have poincare-between x y v
using True assms poincare-between-transitivity
by (meson poincare-between-rev)
thus ?thesis
using assms(2)
by (rule-tac z=y in exl, simp)
next
case False
hence poincare-between y £ z V poincare-between y z &
using <poincare-between x y z V poincare-between y x z V poincare-between y z x»
by simp
show ?thesis
proof (cases poincare-between y x z)
case True
hence poincare-between u x y

136
using assms
by (meson poincare-between-rev poincare-between-transitivity)
thus ?thesis
using assms
by (rule-tac x=x in exI, simp)
next
case False
hence poincare-between y zx
using <poincare-between y x z V poincare-between y z x)
by auto
hence poincare-between x z v
using assms
by (meson poincare-between-rev poincare-between-transitivity)
hence poincare-between x uv
using assms poincare-between-transitivity poincare-between-rev
by (smt poincare-between-sum-distances)
thus ?thesis
using assms
by (rule-tac x=u in exl, simp)
qed
qed
next
case False
hence 7~ distinct [x, y, z, u, v]
using assms(6) by auto
show ?thesis
proof (cases u=z)
case True
thus ?thesis
using assms
apply(rule-tac =v in ex!)
by(simp add:poincare-between-rev)
next
case False
hence x 4 z
using assms poincare-between-sandwich by blast
show ?thesis
proof (cases v=z)
case True
thus ?thesis
using assms
by (rule-tac x=u in exl, simp)
next
case False
hence y # z
using assms poincare-between-sandwich by blast
show ?thesis
proof(cases u = zx)
case True
thus ?thesis
using assms
by (rule-tac c=x in exl, simp)
next
case False
have x # y
using assms ‘7 poincare-collinear {x, y, z}>
by fastforce
have x #4 v
using assms ‘7 poincare-collinear {x, y, z}>
by (metis insert-commute poincare-between-poincare-collinear)
have u #4 y
using assms ‘7 poincare-collinear {x, y, z}>
using poincare-between-poincare-collinear by blast
have u # v
proof (rule ccontr)
assume 7 u #4 v

137
hence poincare-between x v z
using assms by auto
hence z € circline-set (poincare-line z v)
using poincare-between-rev|of x v 2]
using poincare-between-poincare-line-uvz|of z v 2]
using assms <v # z)>
by auto
have y € circline-set (poincare-line z v)
using assms (7 u # v>
using poincare-between-rev|of y v 2]
using poincare-between-poincare-line-uvz|of z v y]
using assms <v # z)>
by auto
have z € circline-set (poincare-line z v)
using ex-poincare-line-two-points|of z vu] «v # z>
by auto
have is-poincare-line (poincare-line z v)
using <v # z>
by auto
hence poincare-collinear {x, y, z}
using (x € circline-set (poincare-line z v)>
using <y € circline-set (poincare-line z v)>
using <z € circline-set (poincare-line z v)>
unfolding poincare-collinear-def
by (rule-tac x=poincare-line z v in el, simp)
thus False
using ‘7 poincare-collinear {x, y, z}» by simp
qed
have v = y
using uAzAuwuAzAyawAéAw czy Uu~An YAR Wz (TAZ UF zB
using (7 distinct [z, y, z, u, uv)
by auto
thus ?thesis
using assms
by (rule-tac c=y in exl, simp)
qed
qed
qed
qed

Axiom of Pasch

lemma Pasch:
assumes « € unit-disc and y € unit-disc and z € unit-disc and u € unit-disc and v € unit-disc
assumes poincare-between xz u z and poincare-between y v z
shows J a. a € unit-disc \ poincare-between u ay A poincare-between © av
proof(cases distinct [x, y, z, u, v] A — poincare-collinear {x, y, z})
case True
thus ?thesis
using assms Pasch-nondeg by auto
next
case False
thus ?thesis
using assms Pasch-deg by auto
qed
