---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-064-continuity-axiom
section_title: "Continuity axiom"
section_number: null
pages: 150-157
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
The set ¢ is on the left of the set

abbreviation set-order where
set-order A p W =V x€ unit-disc. V ye unit-disc. y x A wy y —> poincare-between A x y

The point B is between the sets ¢@ and w
abbreviation point-between-sets where

point-between-sets p Bw = ae€ unit-disc. V ye unit-disc. yp x \ wy y —>+ poincare-between x By

lemma _ continuity:
assumes J A € unit-disc. set-order A yp w
shows 4d B € unit-disc. point-between-sets p Bw
proof (cases (4 20 € unit-disc. p 20) \ (A yO € unit-disc. w y0))
case False
thus ?thesis
using assms by blast
next
case True
then obtain YO where ~ YO YO € unit-disc
by auto
obtain A where *: A € unit-disc set-order A p
using assms
by auto
show ?thesis
proof(cases V x € unit-disc. p © —+ « = A)
case True
thus ?thesis
using <A € unit-discy
using poincare-between-nonstrict(1) by blast
next
case False
then obtain X0 where y X0 X0 4 A XO € unit-disc
by auto
have YOA A
proof (rule ccontr)
assume — YO # A
hence V z € unit-disc. ~ « —> poincare-between A « A
using * «W YO»
by (cases A) force
hence V z € unit-disc. pt —7 r= A
using * poincare-between-sandwich by blast
thus False
using False by auto
qed

show ?thesis
proof (cases 3 B € unit-disc. p B A w B)
case True
then obtain B where B € unit-disc p By B
by auto
hence V z € unit-disc. ~ « —>+ poincare-between A x B
using * by auto
have V y € unit-disc. y) y —> poincare-between A B y
using * <B € unit-disc) «p By
by auto

show ?thesis
proof (rule+)
show B € unit-disc
by fact
next
fix vy
assume z € unit-disc y € unit-disc p x A Wy
hence poincare-between A x B poincare-between A B y
using <V x € unit-disc. y x —+ poincare-between A x By
using <V y € unit-disc. 7) y —> poincare-between A B y»
by simp+
thus poincare-between x B y
using ‘x € unit-disc) ‘y € unit-disc) «B € unit-discy «A € unit-discy
using poincare-between-transitivity[of A x B y|
by simp
qed
next
case False
have poincare-between A X0 YO
using «yp X0> «Wy YO» * «YO € unit-discy «XO € unit-discy
by auto
have V y. V w. set-order A yw A 7 (A B € unit-disc. p BAW B) Ay XO A
(4 y € unit-disc. w y) A (A x € unit-disc. y 2)
— (4 BE unit-disc. point-between-sets p B w)
(is ?P A X0)
proof (rule wlog-positive-x-azis[where P=?P])
show A € unit-disc
by fact
next
show X0 € unit-disc
by fact
next
show A # X0
using (X0 # A» by simp
next
fix Muv
let ?M = x. moebius-pt M x
let ?Mu = ?Muand ?Mv = ?Mv
assume hip: unit-disc-fiz M u € unit-disc v € unit-disc u 4 v
?P ?Mu ?Mv
show ?Puv
proof safe
fix pyry
assume set-order u p w 7 (4 BEunit-disc. p BA w B) pv
y € unit-disc w y x € unit-disc yp x

let ?My = X'".3 X.g XA PMX =X!
let ?Mp =A X35 Xb XA PMX =X!

obtain My where My = ?My by simp
obtain My where My) = ?Mw by simp

have My ?Mv
using (yp v> using (My = ?My»
by blast
moreover
have = (4 B €unit-disc. My B \ My B)
using (7 (4 Beunit-disc. yp B A w B)»
using (My = ?My) «My = ?Mw»
by (metis hip(1) moebius-pt-invert unit-disc-fiz-discl unit-disc-fiz-moebius-inv)
moreover
have 4 y € unit-disc. My y
using <y € unit-discy «py y» «My = ?My» <unit-disc-fix M)
by auto
moreover
have set-order ?Mu ?Mp ?Mw
proof ((rule balll)+, rule imp!)
fix Mz My
assume Mz € unit-disc My € unit-disc ?My Mz A ?MwW My
then obtain z y where py tA ?Max= MrypyA ?My = My
by blast

hence « € unit-disc y € unit-disc
using «Mz € unit-discy «My € unit-disc) (unit-disc-fix M>
by (metis moebius-pt-comp-inv-left unit-disc-fiz-discl wnit-disc-fiz-moebius-inv)+

hence poincare-between u x y
using <set-order u yp w»
using (Mz € unit-disc» «My © unit-discy) «p & A ?M ax = May oy A ?My = My
by blast

then show poincare-between ?Mu Mx My
using «pz A ?Max= Mx wyA ?My = My
using (x € unit-disc> (y € unit-disc> (u € unit-disc» «unit-disc-fix M»
using unit-disc-fir-moebius-preserve-poincare-between by blast

qed

hence set-order ?7Mu Mp My
using (My = ?My) «My = ?Mw»
by simp
ultimately
have 4 Mb € unit-disc. point-between-sets Mp Mb My
using hip(5)
by blast
then obtain Mb where bbb:
Mb € unit-disc point-between-sets ?My Mb ?Mw
using (My = ?My) «My = ?Mw»
by auto

let ?b = moebius-pt (moebius-inu M) Mb
show J 6b € unit-disc. point-between-sets p b w
proof (rule-tac z=?b in bexI, (rule balll)+, rule imp!)
fix ry
assume z € unit-disc y € unit-disc p x A Wy
hence poincare-between u x y
using <set-order u yp w»
by blast

let ?Mz = ?Maand ?My = ?My

have ?Myp ?Mx ?Mw ?My
using (p tA Ww y>
by blast+
have ?Mzx € unit-disc ?My € unit-disc
using (x € unit-disc> (unit-disc-fir M> <y € unit-disc»
by auto

hence poincare-between ?Mx Mb ?My
using «?My ?Ma> «?My ?My) <?Ma € unit-discy «?My € unit-discy bbb
by auto

then show poincare-between x ?b y
using <unit-disc-fix My
using <x € unit-disc) <y € unit-disc) «(Mb € unit-discy «?Max € unit-discy «?My € unit-disc»
using unit-disc-fiz-moebius-preserve-poincare-between|of M x ?b y]
by auto
next
show ?b € unit-disc
using bbb <unit-disc-fix M>
by auto
qed
qed
next
fix X
assume zu: is-real X 0 < Re X Re X < 1
let ?X = of-compler X
show ?P 0), ?X
proof ((rule alll)+, rule impl, (erule conjE)+)
fix py
assume set-order 0; y w 7 (4 BEunit-disc. p BA w B) py ?X
dyeunit-disc. w y dxeunit-disc. yp x
have ?X € unit-disc
using xx
by (simp add: cmod-eq-Re)

have ywpos: V y € unit-disc. W y —> (is-real (to-complex y) A Re (to-complex y) > 0)
proof(rule balll, rule imp!)

fix y

let ?y = to-complex y

assume y € unit-disc w y

hence poincare-between 0, ?X y
using <set-order 0n y w>
using <?X € unit-discy «p ?X»
by auto

thus is-real ?y A 0 < Re ?y
using rx (?X € unit-discy <y € unit-discy
by (metis (mono-tags, opaque-lifting) arg-0-iff of-complex-zero-iff poincare-between-Ouv poincare-between-sandwich
to-complex-of-complex unit-disc-to-complez-inj zero-in-unit-disc)
qed

have ynoneg: V x € unit-disc. yp x —+ (is-real (to-complex x) \ Re (to-complex x) > 0)
proof(rule balll, rule imp!)

fix x

assume z € unit-disc yp x

obtain y where y € unit-disc w y
using <3 y € unit-disc. w y» by blast

let ?x = to-compler x and ?y = to-complex y

have is-real ?y Re ?y > 0
using wpos «1 y> <y € unit-disc»
by auto

have poincare-between On xy
using <set-order 0n y w>
using (x € unit-disc) «p x» <yeunit-discy «Wy»
by auto

thus is-real ?x \ 0 < Re ?x
using (x € unit-disc» (y € unit-disc» <is-real (to-complex y)> «w y>
using <set-order 0n y w>
using «yp ?X> «?X © unit-disc» «Re ?y > 0)
by (metis arg-0-iff le-less of-complex-zero poincare-between-Ouv to-complex-of-complex zero-complex.simps(1)
zero-complex.simps(2))
qed

have ylessy): V re unit-disc. V yeunit-disc. p zx \ ~ y —> Re (to-complez x) < Re (to-complex y)
proof((rule balll)+, rule imp!)

fix ry

let ?x = to-compler x and ?y = to-complex y

assume z € unit-disc y € unit-disc p x A Wy

hence poincare-between On x y
using <set-order 0n y w>
by auto
moreover
have is-real ?x Re ?x > 0
using ynoneg
using <2 € unit-disc) «p « A w y> by auto

moreover
have is-real ?y Re ?y > 0

using wpos

using <y € unit-disc» (p A w y> by auto
ultimately

have Re ?x < Re ?y
using <x € unit-discy <y € unit-discy
by (metis Re-complex-of-real arg-0-iff le-less of-complex-zero poincare-between-OQuv rcis-cmod-Arg rcis-zero-arg
to-complex-of-complez)

have Re ?x # Re ?y
using «p z A w y> ¢is-real ?x» <is-real ?y>
using <7 (5 Beunit-disc. p B A w B)> (a € unit-disc> <y € unit-disc»
by (metis complex.expand unit-disc-to-complex-inj)

thus Re ?x < Re ?y
using (Re ?x < Re ?y» by auto
qed
have 4 b € unit-disc. V x € unit-disc. V y € unit-disc.
is-real (to-complex b) A
(p «Aw y — (Re (to-complex xr) < Re (to-complex b) \ Re (to-complex b) < Re (to-complex y)))
proof—
let ?Phi = {x. (of-complex (cor x)) € unit-disc \ yp (of-complex (cor x))}

have V z € unit-disc. p s —+ Re (to-compler x) < Sup ?Phi
proof (safe)
fix «
let ?z = to-complex x
assume z € unit-disc yp x
hence is-real ?z Re ?z > 0
using ynoneg
by auto
hence cor (Re ?x) = ?x
using complex-of-real-Re by blast
hence of-complex (cor (Re ?x)) € unit-disc
using <x € unit-disc)
by (metis inf-notin-unit-disc of-complex-to-complex)
moreover
have ¢ (of-complex (cor (Re ?x)))
using ‘cor (Re ’r) = ?x) «py ©) (ax € unit-disc»
by (metis inf-notin-unit-disc of-complex-to-complex)
ultimately
have Re ?x € ?Phi
by auto

have 3M.Vz € ?Phi. 4 < M
using ylessw
using <4 y € unit-disc. w y>
by (metis (mono-tags, lifting) Re-complez-of-real le-less mem-Collect-eq to-complez-of-complez)

thus Re ?x < Sup ?Phi
using cSup-upper|of Re ?x ?Phi|
unfolding bdd-above-def
using ‘Re ?x € ?Phi>
by auto
qed

have V y € unit-disc. y) y —> Sup ?Phi < Re (to-complex y)
proof (safe)
fix y
let ?y = to-complex y
assume w y y € unit-disc
show Sup ?Phi < Re ?y
proof (rule ccontr)
assume — ?thesis
hence Re ?y < Sup ?Phi
by auto

have J «. ¢ (of-complex (cor x)) A (of-complex (cor x)) € unit-disc
proof —
obtain x’ where x’ € unit-disc yp x’
using (5 x € unit-disc. yp x» by blast
let ?x’ = to-complex x’
have is-real ?x’
using (z’ € unit-discr «yp x’
using ynoneg
by auto
hence cor (Re ?2") = ?x'
using complex-of-real-Re by blast
hence x’ = of-complex (cor (Re ?x’))
using <x’ € unit-disc»
by (metis inf-notin-unit-disc of-complex-to-complez)
show ?thesis
apply (rule-tac s=Re ?x’' in ex!)

using <x’ € unit-disc»

apply (subst (asm) <a’ = of-complex (cor (Re ?x"))>, simp)

using «yp x

by (subst (asm) (2) <x’ = of-complex (cor (Re ?x'))>, simp)
qed

hence ?Phi # {}
by auto

then obtain x where y (of-complex (cor x)) Re ?y < x
(of-complex (cor x)) € unit-disc

using ‘Re ?y < Sup ?Phi»
using less-cSupE|of Re ?y ?Phi]
by auto

moreover

have Re ?y < Re (to-complex (of-complex (cor x)))
using ‘Re ?y < x)
by simp

ultimately

show False
using ylessy
using «w y> <y € unit-dise»
by (metis less-not-sym)

qed
qed

thus ?thesis

using ‘V z € unit-disc. p « —> Re (to-complez x) < Sup ?Phi»

apply (rule-tac «=(of-complex (cor (Sup ?Phi))) in bel, simp)

using (J yeunit-disc. w y» «p ?X» «?X € unit-disey

using (V yCunit-disc. W y —> is-real (to-complex y) A 0 < Re (to-complex y)>

by (smt complez-of-real-Re inf-notin-unit-disc norm-of-real of-complex-to-complex to-complex-of-complex
unit-disc-iff-cmod-lt-1 rx(2))
qed

then obtain B where B € unit-disc is-real (to-complex B)
VxEunit-disc. V yeunit-disc. p x \ w y —> Re (to-compler x) < Re (to-complex B) \
Re (to-complez B) < Re (to-complex y)
by blast

show J 6b € unit-disc. point-between-sets p b w
proof (rule-tac z=B in bez!)
show B € unit-disc
by fact
next
show point-between-sets p Bw
proof ((rule ballI)+, rule imp!)
fix vy
let ?z = to-complex x and ?y = to-complex y and ?B = to-complex B
assume z € unit-disc y € unit-disc p « A Wy

hence Re ?x < Re ?B \ Re ?B < Re ?y
using ‘V reunit-disc. V yeunit-disc. p x \ ~ y —> Re (to-compler x) < Re ?B A
Re (to-compler B) < Re (to-complex y)>
by auto
moreover
have is-real ?x Re ?x > 0
using ynoneg
using <x € unit-disc) (p x A wW y>
by auto
moreover
have is-real ?y Re ?y > 0
using wpos
using <y € unit-disc) (p x A wy»
by auto
moreover
have cor (Re ?x) = ?x
using complex-of-real-Re <is-real 2x» by blast
hence z = of-complex (cor (Re ?x))
using <x € unit-disc)
by (metis inf-notin-unit-disc of-complex-to-complex)
moreover
have cor (Re ?y) = ?y
using complex-of-real-Re <is-real ?y» by blast
hence y = of-complex (cor (Re ?y))
using <y € unit-disc)
by (metis inf-notin-unit-disc of-complex-to-complex)
moreover
have cor (Re ?B) = ?B
using complez-of-real-Re ‘is-real (to-complex B)» by blast
hence B = of-complex (cor (Re ?B))
using «B € unit-discy
by (metis inf-notin-unit-disc of-complex-to-complex)
ultimately
show poincare-between « B y
using <is-real (to-complex B)) «x € unit-disc» «y € unit-disc» «B € unit-disc»
using poincare-between-z-axis-uvwlof Re (to-compler x) Re (to-complez B) Re (to-complex y)]
by (smt Re-complez-of-real arg-0-iff poincare-between-nonstrict(1) rcis-cmod-Arg rcis-zero-arg unit-disc
qed
qed
qed
qed
thus ?thesis
using False «p XO» «w YO» * «YO € unit-discy (XO € unit-discy
by auto
qed
qed
qed

~cmod-lt-1)
