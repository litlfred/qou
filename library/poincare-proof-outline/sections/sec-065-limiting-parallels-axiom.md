---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-065-limiting-parallels-axiom
section_title: "Limiting parallels axiom"
section_number: null
pages: 157-170
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Auxiliary definitions

definition poincare-on-line where
poincare-on-line p a b <—+ poincare-collinear {p, a, b}

definition poincare-on-ray where
poincare-on-ray p a b +—> poincare-between a p b V poincare-between a b p

definition poincare-in-angle where
poincare-in-angle pa bc+<—+
bAaNbACA PF DbHA (A TE unit-disc. poincare-between azc\«#aA\ «cA poincare-on-ray p b zx)

definition poincare-ray-meets-line where
poincare-ray-meets-line a b c d <—+ (4 a € unit-disc. poincare-on-ray x a b A poincare-on-line x c d)

All points on ray are collinear

lemma poincare-on-ray-poincare-collinear:
assumes p € unit-disc and a € unit-disc and b € unit-disc and poincare-on-ray p a b
shows poincare-collinear {p, a, b}
using assms poincare-between-poincare-collinear
unfolding poincare-on-ray-def
by (metis insert-commute)

H-isometries preserve all defined auxiliary relations

lemma unit-disc-fiz-preserves-poincare-on-line [simp]:
assumes unit-disc-fix M and p € unit-disc a € unit-disc b € unit-disc
shows poincare-on-line (moebius-pt M p) (moebius-pt M a) (moebius-pt M b) — poincare-on-line p a b
using assms
unfolding poincare-on-line-def
by auto
lemma unit-disc-fir-preserves-poincare-on-ray [simp]:
assumes unit-disc-fix M p € unit-disc a € unit-disc b € unit-disc
shows poincare-on-ray (moebius-pt M p) (moebius-pt M a) (moebius-pt M b) <—> poincare-on-ray p a b
using assms
unfolding poincare-on-ray-def
by auto

lemma unit-disc-fiz-preserves-poincare-in-angle [simp]:
assumes unit-disc-fix M p € unit-disc a € unit-disc b € unit-disc c € unit-disc
shows poincare-in-angle (moebius-pt M p) (moebius-pt M a) (moebius-pt M b) (moebius-pt M c) <—> poincare-in-angle
pabc (is ?lhs <—+ ?rhs)
proof
assume ?/hs
then obtain Mz where *: Mz € unit-disc
poincare-between (moebius-pt M a) Mx (moebius-pt M c)
Mz # moebius-pt M a Mz 4 moebius-pt M c poincare-on-ray (moebius-pt M p) (moebius-pt M b) Mx
moebius-pt M b #4 moebius-pt M a moebius-pt M b #4 moebius-pt M c moebius-pt M p # moebius-pt M b
unfolding poincare-in-angle-def
by auto
obtain « where Mz = moebius-pt M x x € unit-disc
by (metis «(1) assms(1) image-iff unit-disc-fix-iff)
thus ?rhs
using * assms
unfolding poincare-in-angle-def
by auto
next
assume ?rhs
then obtain z where *: x € unit-disc
poincare-between a xc
x#ax#c poincare-on-ray p bx
bAabzAcpHFdH
unfolding poincare-in-angle-def
by auto
thus ?lhs
using assms
unfolding poincare-in-angle-def
by auto (rule-tac =moebius-pt M x in berl, auto)
qed

lemma unit-disc-fit-preserves-poincare-ray-meets-line [simp]:
assumes unit-disc-fix M a € unit-disc b € unit-disc c € unit-disc d € unit-disc
shows poincare-ray-meets-line (moebius-pt M a) (moebius-pt M b) (moebius-pt M c) (moebius-pt M d) <—>+ poincare-ray-meets-line
abcd (is ?lhs <> ?rhs)
proof
assume ?/hs
then obtain Mz where +: Mz € unit-disc poincare-on-ray Mx (moebius-pt M a) (moebius-pt M b)
poincare-on-line Mx (moebius-pt M c) (moebius-pt M d)
unfolding poincare-ray-meets-line-def
by auto
obtain « where Mz = moebius-pt M x x € unit-disc
by (metis «(1) assms(1) image-iff unit-disc-fix-iff)
thus ?rhs
using assms *
unfolding poincare-ray-meets-line-def poincare-on-line-def
by auto
next
assume ?rhs
then obtain z where «: x € unit-disc poincare-on-ray x a b
poincare-on-line x c d
unfolding poincare-ray-meets-line-def
by auto
thus ?lhs
using assms *
unfolding poincare-ray-meets-line-def poincare-on-line-def
by auto (rule-tac =moebius-pt M x in berl, auto)
qed

H-lines that intersect on the absolute do not meet (they do not share a common h-point)

lemma tangent-not-meet:
assumes z1 € unit-disc and x2 € unit-disc and 21 # x2 and — poincare-collinear {0),, x1, x2}
assumes i € ideal-points (poincare-line x1 x2) a € unit-disc a # On poincare-collinear {0;,, a, i}
shows — poincare-ray-meets-line 0, a x1 x2
proof (rule ccontr)
assume 7— thesis
then obtain z where x € unit-disc poincare-on-ray 2 0, a poincare-collinear {x, 21, x2}
unfolding poincare-ray-meets-line-def poincare-on-line-def
by auto

have poincare-collinear {0n, a, x}
using <poincare-on-ray « On a) «x € unit-discy <a € unit-discy
by (meson poincare-between-poincare-collinear poincare-between-rev poincare-on-ray-def poincare-on-ray-poincare-collinear
zero-in-unit-disc)

have x 4 0;
using ‘~ poincare-collinear {On, 21, t2}> <poincare-collinear {x, x1, x2}>
unfolding poincare-collinear-def
by (auto simp add: assms(2) assms(3) poincare-between-rev)

let 211 = poincare-line 0; a
let 212 = poincare-line x1 x2

have i € circline-set unit-circle
using <i € ideal-points (poincare-line x1 x2)»
using assms(3) ideal-points-on-unit-circle is-poincare-line-poincare-line by blast

have i € circline-set ?l1
using <poincare-collinear {0n, a, i}>
unfolding poincare-collinear-def
using <a € unit-disc> «a # On»
by (metis insert-subset unique-poincare-line zero-in-unit-disc)

moreover

have z € circline-set 11
using <a € unit-discy (a # On) <poincare-collinear {On, a, x}> (x € unit-dise»
by (metis poincare-collinear3-between poincare-between-poincare-line-uvz poincare-between-poincare-line-uzv poincare-line-sym
zero-in-unit-disc)

moreover

have inversion x € circline-set ?11
using <poincare-collinear {0;,, a, x}>
using poincare-line-inversion-fulllof 0, a x| (a € unit-discy (a # Opn» «x € unit-disc»
by (metis poincare-collinear3-between is-poincare-line-inverse-point is-poincare-line-poincare-line poincare-between-poincare-line-uvz
poincare-between-poincare-line-uzv poincare-line-sym zero-in-unit-disc)

moreover

have « € circline-set 212
using <poincare-collinear {x, x1, x2} (a1 # x2» (al € unit-discy (x2 € unit-disc» «x € unit-disc»
by (metis insert-commute inversion-noteg-unit-disc poincare-between-poincare-line-uvz poincare-between-poincare-line-uzv
poincare-collinear3-iff poincare-line-sym-general)

moreover

hence inversion « € circline-set 212
using «x1 4 x2) «x1 € unit-disc> (x2 € unit-discy «x € unit-discy
using poincare-line-inversion-fulllof x1 x2 2]
unfolding circline-set-def
by auto
moreover

have i € circline-set 212
using (t1 # £2) «x1 € unit-disc) (#2 € unit-discy
using <i € ideal-points 712»
by (simp add: ideal-points-on-circline)

moreover

have x 4 inversion x
using (x € unit-disc»
using inversion-noteq-unit-disc by fastforce

moreover

have « #i
using (x € unit-disc»
using <i € circline-set unit-circle) circline-set-def inversion-noteg-unit-disc
by fastforce+

moreover

have inversion x 4 i
using <i € circline-set unit-circley «x # 1) circline-set-def inversion-unit-circle
by fastforce

ultimately

have 7/1 = 712
using unique-circline-set|of x inversion x i]
by blast

hence 0, € circline-set 712
by (metis «a # 0n» poincare-line-circline-set(1))

thus False
using ‘7— poincare-collinear {On, t1, t2}>
unfolding poincare-collinear-def
using <poincare-collinear {x, 21, x2}) (a1 # 2) (21 € unit-disc» «x2 € unit-disc» poincare-collinear-def unique-poincare-line
by auto
qed

lemma limiting-parallels:
assumes a € unit-disc and r1 € unit-disc and «2 € unit-disc and — poincare-on-line a «1 «2
shows Jal €unit-disc. 4 a2€unit-disc.
— poincare-on-line a al a2 A
— poincare-ray-meets-line a al x1 x2 A — poincare-ray-meets-line a a2 x1 x2 NA
(V a'Eunit-disc. poincare-in-angle a' al a a2 —+ poincare-ray-meets-line a a’ x1 x2) (is ?P a x1 x2)
proof—
have ~ poincare-collinear {a, x1, x2}
using (— poincare-on-line a x1 x2»
unfolding poincare-on-line-def
by simp

have V «1 x2. x1 € unit-disc A x2 € unit-disc A — poincare-collinear {a, r1, 12} —> ?P a xl x2 (is ?Q a)
proof (rule wlog-zero|OF <a € unit-disc»])
fix au
assume *: u € unit-disc cmod a < 1
hence uf: unit-disc-fix (blaschke a)
by simp
assume *«: ?Q (moebius-pt (blaschke a) u)
show ?Qu
proof safe
fix cl 12
let ?M = moebius-pt (blaschke a)
assume wz: t1 € unit-disc x2 € unit-disc — poincare-collinear {u, x1, x2}

160
hence MM: ?M «1 € unit-disc \ ?M x2€ unit-disc A — poincare-collinear {?M u, ?M x1, ?M 22}
using *
by auto
show ?P u xl x2 (is Jal€unit-disc. Ja2€unit-disc. ?P' al a2 u xl x2)
proof—
obtain Mai Ma2 where MM: Mai € unit-disc Ma2 € unit-disc ?P' Mal Ma2 (?M u) (?M a1) (?M 22)
using **[rule-format, OF MM]
by blast
hence MM’: V a'€unit-disc. poincare-in-angle a’ Mal (?M u) Ma2 —+ poincare-ray-meets-line (?M u) a’ (?M
x1) (?M x2)
by auto
obtain al a2 where a: al € unit-disc a2 € unit-disc ?M al = Mal ?M a2 = Ma2
using uf
by (metis «Mal € unit-disc» «Ma2 € unit-disc> image-iff unit-disc-fiz-iff)

have Y a’Eunit-disc. poincare-in-angle a’ al u a2 —+ poincare-ray-meets-line u a’ x1 «2
proof safe

fix a’

assume a’ € unit-disc poincare-in-angle a' al u a2

thus poincare-ray-meets-line u a’ x1 x2

using MM(1—2) MM "[rule-format, of ?M a‘) * uf a zx

by (meson unit-disc-fix-discl unit-disc-fix-preserves-poincare-in-angle unit-disc-fix-preserves-poincare-ray-meets-line)
qed

hence ?P‘ al a2 ual x2
using MM «x uf cra
by auto

thus ?thesis
using (al € unit-disc) «a2 € unit-disc»
by blast
qed
qed
next
show 7Q 0;
proof safe
fix x1 x2
assume z1 € unit-disc 72 € unit-disc
assume 7— poincare-collinear {0n, 21, 22}
show ?P 0; x1 «2
proof—
let ?la = poincare-line x1 x2

have «1 4 x2
using (zl © unit-disc» (x2 € unit-disc><— poincare-collinear {On, 21, x2}>
using poincare-collinear3-between
by auto

have Iz: is-poincare-line ?lx
using is-poincare-line-poincare-line[OF «x1 # x2)]
by simp

obtain i1 i2 where ideal-points ?lx = {i1, i2}
by (meson «x1 4 x2) is-poincare-line-poincare-line obtain-ideal-points)

let ?li = poincare-line il i2
let ?i1 = to-complex il
let ?i2 = to-complex i2

have il € unit-circle-set i2 € unit-circle-set
using Ix <ideal-points ?lz = {i1, i2}»
unfolding unit-circle-set-def
by (metis ideal-points-on-unit-circle insertI1, metis ideal-points-on-unit-circle insertI1 insertI2)

have il # i2
using <ideal-points ?lx = {i1, i2}) «a1 € unit-discy (a1 # 22) (a2 € unit-disc» ideal-points-different(1)

161
by blast

let ?a1 = of-complex (?i1 / 2)
let ?a2 = of-complex (?i2 / 2)
let ?la = poincare-line ?a1 ?a2

have ?a1 € unit-disc ?a2 € unit-disc
using <i1 € unit-circle-set) (i2 € unit-circle-set)
unfolding unit-circle-set-def unit-disc-def disc-def circline-set-def
by auto (transfer, transfer, case-tac i1, case-tac i2, simp add: vec-cnj-def)+

have ?al 4 On ?a2 4 On
using <i1 € unit-circle-set) (i2 € unit-circle-set)
unfolding unit-circle-set-def
by auto

have ?al # ?a2
using <i1  i2>
by (metis <i1 € unit-circle-set» (i2 € wnit-circle-set) circline-set-def divide-cancel-right inversion-infty inver-
sion-unit-circle mem-Collect-eq of-complez-to-complex of-complex-zero to-complex-of-complex unit-circle-set-def zero-neq-numeral)

have poincare-collinear {On, ?a1, i1}
unfolding poincare-collinear-def
using <?al 4 0);,>[symmetric] is-poincare-line-poincare-line[of 0), a1]
unfolding circline-set-def
apply (rule-tac z=poincare-line 0, ?a1 in exI, auto)
apply (transfer, transfer, auto simp add: vec-cnj-def)
done

have poincare-collinear {0n, ?a2, i2}
unfolding poincare-collinear-def
using <?a2 4 0);,>[symmetric] is-poincare-line-poincare-line[of 0), ?a2]
unfolding circline-set-def
apply (rule-tac z=poincare-line 0, ?a2 in exI, auto)
apply (transfer, transfer, auto simp add: vec-cnj-def)
done

have = poincare-ray-meets-line 0, ?a1 1 «2
using tangent-not-meet[of x1 x2 il ?a1]
using (21 © unit-disc» «x2 € unit-disc» «?a1 € unit-disc» (x1 4 x2» (> poincare-collinear {0;,, x1, x2}>
using <ideal-points ?lx = {i1, i2}) «?al # On» <poincare-collinear {0;, ?a1, i1}>
by simp

moreover

have — poincare-ray-meets-line On ?a2 x1 «2
using tangent-not-meet[of x1 x2 i2 ?a2]
using (21 © unit-disc» (x2 € unit-disc» «?a2 € unit-disc» (x1 # x2) (> poincare-collinear {0;,, x1, 2}>
using <ideal-points ?lx = {i1, i2}» «?a2 4 On» <poincare-collinear {0;, ?a2, i2}>
by simp

moreover

have Va’ € unit-disc. poincare-in-angle a’ ?a1 On ?a2 —+ poincare-ray-meets-line On a’ x1 x2
unfolding poincare-in-angle-def
proof safe
fix a’ a
assume +: a’ € unit-disc a € unit-disc poincare-on-ray a' On aa’ # On
poincare-between ?al a ?a2a 4 ?al a # ?a2
show poincare-ray-meets-line 0;, a’ 1 x2
proof—
have V a’ al a2 a1 22 i1 i2.
a’ € unit-disc \ x1 € unit-disc \ x2 € unit-disc A zl #4 22 A
7 poincare-collinear {On, x1, x2} A ideal-points (poincare-line x1 12) = {i1, i2} A
al = of-complex (to-complex il / 2) A a2 = of-complex (to-complex i2 / 2) \
il # i2 A al ¥ a2 A poincare-collinear {0n, a1, i1} A poincare-collinear {On, a2, i2} A

162
al € unit-disc \ a2 € unit-disc \ il € unit-circle-set \ i2 € unit-circle-set \
poincare-on-ray a’ On a \ a’ # On A poincare-between al aa2 Na#al Aa a2 —>
poincare-ray-meets-line On a’ x1 22 (isV a’ al a2 xl x2 i1 i2. ?R On a’ al a2 zl x2 il i2 a)
proof (rule wlog-rotation-to-positive-x-axis[OF «a € unit-disc»])
let ?R’= a zero. V a’ al a2 x1 x2 il i2. PR zero a’ al a2 c1 x2 il i2a
fix ra
assume za: is-real ra 0 < Re za Re za < 1
let ?a = of-complex xa
show ?R! ?a 0;
proof safe
fix a’ al a2 rl x2 il i2
let ?i1 = to-complex i1 and ?i2 = to-complex i2
let a1 = of-complex (?i1 / 2) and ?a2 = of-complex (?i2 / 2)
let ?la = poincare-line ?a1 ?a2 and ?lz = poincare-line x1 x2 and ?li = poincare-line i1 i2
assume a’ € unit-disc r1 € unit-disc 12 € unit-disc x1 # «2
assume — poincare-collinear {0,, 21, x2} ideal-points ?lx = {i1, i2}
assume poincare-on-ray a’ On 2a a' # On
assume poincare-between ?a1 ?a ?a2 ?a # ?al 2a # ?a2
assume il # i2 ?al # ?a2 poincare-collinear {0n, ?a1, i1} poincare-collinear {0;, ?a2, i2}
assume a1 € unit-disc ?a2 € unit-disc
assume il € unit-circle-set i2 € unit-circle-set
show poincare-ray-meets-line 0;, a’ x1 x2
proof—
have ?lx = ?li
using <ideal-points ?lx = {i1, i2}> «a1 4 22» ideal-points-line-unique
by auto

have Iz: is-poincare-line ?lx
using is-poincare-line-poincare-line[OF «11 # 22>]
by simp

have x1 € circline-set ?lz x2 € circline-set ?lx
using Iz «rl # x2)
by auto

have ?lx # z-axis
using ‘~ poincare-collinear {On, 21, 22}> «x1 € circline-set ?lx) «x2 € circline-set ?lx> lx
unfolding poincare-collinear-def
by auto

have 0» ¢ circline-set ?lx
using (~ poincare-collinear {On, 21, 22}> lx ‘21 © circline-set ?lay «x2 € circline-set ?lx>
unfolding poincare-collinear-def
by auto

have za # 0 2a 4 On
using za
by auto

hence 0; 4 ?a
by metis

have ?a € positive-r-axis
using za
unfolding positive-r-azis-def
by simp

have ?a € unit-disc

using za

by (auto simp add: cmod-eq-Re)
have ?a € circline-set ?la

using <poincare-between ?al ?a ?a2>

using <«?al # ?a2) <?a € unit-discy (?al © unit-disc) «?a2 € unit-disc> poincare-between-poincare-line-uzv

by blast

163
have ?a1 € circline-set ?la ?a2 € circline-set ?la
by (auto simp add: «?a1 # ?a2>)

have la: is-poincare-line ?la
using is-poincare-line-poincare-line{OF «?al # ?a2>|
by simp

have inv: inversion i1 = il inversion i2 = i2
using <i © unit-circle-set> <i2 € unit-circle-sety
by (auto simp add: circline-set-def unit-circle-set-def)

have il 4 oon i2 4 on
using inv
by auto

have ?al ¢ circline-set x-axis \ ?a2 ¢ circline-set x-axis
proof (rule ccontr)
assume — thesis
hence ?al € circline-set x-axis V ?a2 € circline-set x-axis
by auto
hence ?la = x-axis
proof
assume ?al1 € circline-set z-axis
hence {?a, ?a1} C circline-set ?la N circline-set z-axis
using <?a € circline-set ?lay <?a1 € circline-set ?lay<?a € positive-x-axis>
using circline-set-x-axis-I xa(1)
by blast
thus ?la = z-axis
using wnique-is-poincare-line[of ?a ?al ?la x-axis]
using <?al € unit-disc) «?a € unit-disc) la «?a # ?al>
by auto
next
assume 7a2 € circline-set z-axis
hence {?a, ?a2} C circline-set ?la M circline-set x-axis
using <?a € circline-set ?lay <?a2 € circline-set ?lay «?a € positive-x-axis)
using circline-set-x-axis-I xa(1)
by blast
thus ?la = z-axis
using wnique-is-poincare-line[of ?a ?a2 ?la x-axis]
using <?a2 € unit-disc) «?a € unit-disc) la <?a # ?a2>
by auto
qed

hence i1 € circline-set x-axis \ i2 € circline-set x-axis
using <?a1 € circline-set ?lay «?a2 € circline-set ?lay
by (metis <i1 4 con» i2 # on» <of-complex (to-complex i1 / 2) € unit-discy <of-complex (to-complex
i2 / 2) € unit-disc <poincare-collinear {0n, of-complex (to-complex il / 2), i1}> «poincare-collinear {0;,, of-complex
(to-complex i2 / 2), i2}» divide-eq-0-iff inf-not-of-complez inv(1) inv(2) inversion-noteg-unit-disc of-complez-to-complex
of-complex-zero-iff poincare-collinear3-poincare-lines-equal-general poincare-line-0-real-is-x-axis poincare-line-circline-set(2)
zero-in-unit-disc zero-neq-numeral)

thus False
using <?lz # z-axis» unique-is-poincare-line-generallof i1 i2 ?li z-axis] <i1 A i2> inv «Pla = Plir
by auto
qed

hence ?la # x-axis
using <?al # ?a2) poincare-line-circline-set(1)
by fastforce
have intersects-z-azis-positive ?la
using intersects-x-axis-positive-iff [of la] «?la # x-axis» <?a € circline-set ?la> la
using <?a € unit-disc> «?a € positive-x-azxisy

by auto

have intersects-a-axis ?la

164
proof —
have Arg (to-complex ?a1) * Arg (to-complez ?a2) < 0
using <poincare-between ?a1 ?a ?a2> (?al € unit-disc) (?a2 € unit-disc»
using poincare-between-z-axis-intersection|of ?a1 ?a2 of-complex xa]
using <?al # ?a2) <?a © unit-disc (?a1 ¢ circline-set z-axis \ ?a2 ¢ circline-set x-axis) (?a €
positive-x-axis)
using <?a € circline-set ?la)
unfolding positive-x-azis-def
by simp

moreover

have A zyx’ y's: real. [sgn x' = sgn x; sgn y’ = sgn yl] => rey < 0+ 2'xy’ <0
by (metis sgn-less sgn-mult)

ultimately

have Im (to-complex ?a1) * Im (to-complex ?a2) < 0
using arg-Im-sgn{of to-complex ?a1] arg-Im-sgn|of to-complex ?a2]
using (?a1 € unit-disc» «?a2 € unit-discy «?al ¢ circline-set x-axis \ ?a2 ¢ circline-set x-axis»
using inf-or-of-complez|of ?a1] inf-or-of-complez|of ?a2] circline-set-x-axis
by (metis circline-set-x-axis-I to-complex-of-complez)

thus ?thesis
using ideal-points-intersects-x-axis|of ?lx i1 i2]
using <ideal-points ?lx = {i1, i2}> lx «?lx # x-axis)
by simp
qed

have intersects-z-azis-positive ?lx
proof —
have cmod ?i1 = 1 cmod ?7i2 = 1
using <i1 € unit-circle-set» (i2 € unit-circle-set»
unfolding unit-circle-set-def
by auto

let ?a1'= ?i1 / 2 and ?a2'= 72 / 2
let ?Aal =i « (?al' * cnj a2’ — 2a’ * cnj 2a1') and
?Bal =i * (?a2' * cor ((emod ?al')? + 1) — ?al' * cor ((emod ?a2')? + 1))

have ?Aal #4 0 V ?Bal # 0
using <cmod (to-complex i1) = 1» <‘cmod (to-complex i2) = 1» «?a1l # ?a2>
by (auto simp add: power-divide complex-mult-cnj-cmod)

have is-real ?Aal
by simp

have ?al # inversion ?a2
using <?al € unit-disc» «?a2 € unit-disc> inversion-noteg-unit-disc by fastforce

hence Re ?Bal / Re ?Aal < —1
using <intersects-x-axis-positive ?lay «fal # ?a2>
using intersects-x-azis-positive-mk-circline[of ?Aal ?Ba1| «?Aal # 0 V ?Bal # 0» ‘is-real ?Aal>
using poincare-line-non-homogenous|of ?a1 ?a2]
by (simp add: Let-def)

moreover
let ?i1' = to-complez il and ?i2’ = to-complex i2
let ?Ail = i * (?i1' « cnj ?12' — 212’ * cnj i1') and

?Bil = i * (?i2' * cor ((emod ?i1’)? + 1) — 2i1' * cor ((emod ?i2')? + 1))
have ?Ail # 0 V ?Bil 40

using <cmod (to-complex i1) = 1» <‘cmod (to-complex i2) = 1» «?a1l # ?a2>
by (auto simp add: power-divide complex-mult-cnj-cmod)

165
have is-real ?Ail
by simp

have sgn (Re ?Bil / Re ?Ail) = sgn (Re ?Bal / Re ?Aa1)
proof—
have Re ?Bil / Re ?Ail = (Im ?i1l * 2 — Im ?i2 * 2) /
(Im ?i2 « (Re ?i1 * 2) — Im ?i1 = (Re 7i2 * 2))
using <cmod ?i1 = 1» <cmod ?i2 = 1)
by (auto simp add: complex-mult-cnj-cmod field-simps)
also have ... = (Im ?i1 — Im ?i2) /
(Im ?i2 « (Re ?i1) — Im ?i1 * (Re ?i2)) (is ... = Pexpr)
apply (subst left-diff-distrib|symmetric])
apply (subst semiring-normalization-rules(18))+
apply (subst left-diff-distrib|symmetric])
by (metis mult.commute mult-divide-mult-cancel-left-if zero-neg-numeral)
finally have 1: Re ?Bil / Re ?Ail = (Im ?i1 — Im ?i2) / (Im ?i2 * (Re ?i1) — Im ?i1 * (Re ?i2))

have Re ?Bal / Re ?Aal = (Im ?i1 * 20 — Im ?i2 * 20) /
(Im ?i2 * (Re ?i1 * 16) — Im ?il * (Re ?i2 * 16))
using <cmod (to-complex i1) = 1) <cmod (to-complex i2) = 1>
by (auto simp add: complex-mult-cnj-cmod field-simps)
also have ... = (20 / 16) « ((Im ?i1 — Im ?i2) /
(Im ?i2 « (Re ?i1) — Im ?i1 * (Re ?i2)))
apply (subst left-diff-distrib|symmetric] )+
apply (subst semiring-normalization-rules(18))+
apply (subst left-diff-distrib|symmetric] )+
by (metis (no-types, opaque-lifting) field-class. field-divide-inverse mult.commute times-divide-times-eq)
finally have 2: Re ?Bal / Re ?Aal = (5 / 4) * ((Im ?i1 — Im ?i2) / (Im ?i2 * (Re 2i1) — Im %i1
* (Re ?i2)))
by simp

have ?expr # 0
using ‘Re ?Bal / Re ?Aal < —1»
apply (subst (asm) 2)
by linarith

thus ?thesis
apply (subst 1, subst 2)
apply (simp only: sgn-mult)
by simp

qed

moreover

have il # inversion i2
by (simp add: <i1 4 i2> inv(2))

have (Re ?Bil / Re ?Ail)? > 1
proof—
have ?Ail = 0 V (Re ?Bi1l)? > (Re ?Ai1)?
using <intersects-x-axis ?lxy
using (il A i2> <i1 F Con? (i2 F con? dil F inversion i2>
using intersects-z-axis-mk-circline|of ?Ail ?Bi1] «?Ai1l #4 0 V ?Bil # O» <is-real ?Ail>
using poincare-line-non-homogenous|of il i2] «?lx = ?lir
by metis

moreover
have ?Ai1 4 0
proof (rule ccontr)
assume — ?thesis
hence 0;, € circline-set ?li
unfolding circline-set-def
apply simp
apply (transfer, transfer, case-tac i1, case-tac i2)

166
by (auto simp add: vec-cnj-def field-simps)
thus False
using (On € circline-set lx) «?lx = ?lir
by simp
qed

ultimately

have (Re ?Bil)? > (Re ?Ai1)?
by auto

moreover

have Re ?Ail 4 0
using <is-real ?Ai1» «?Ail # 0»
by (simp add: complex-eq-iff )

ultimately

show ?thesis
by (simp add: power-divide)
qed

moreover

{

fix r1 x2 :: real
assume sgn zl = sgn a2 x1 <—122?>1
hence x2 < —1
by (smt one-power? real-sqrt-abs real-sqrt-less-iff sgn-neg sgn-pos)

}

ultimately

have Re ?Bil / Re ?Ail < —-1
by metis

thus ?thesis
using <i1 A i2> <i1 F Con? (i2 F con? «il F inversion i2>
using intersects-x-azis-positive-mk-circline|of ?Ail ?Bi1l] «?Ail #4 0 V ?Bil # 0» <is-real ?Ail>
using poincare-line-non-homogenous|of i1 i2] «?lx = ?lir
by (simp add: Let-def)
qed

then obtain x where z: x € unit-disc x € circline-set ?lx N positive-x-axis
using intersects-z-axis-positive-iff[OF lx «?lx # 2-axis>|
by auto

have poincare-on-ray x 0;, a’ \ poincare-collinear {x1, x2, x}
proof
show poincare-collinear {x1, x2, x}
using z Ix ‘xl € circline-set ?lx» «x2 € circline-set ?lxy
unfolding poincare-collinear-def
by auto
next
show poincare-on-ray x 0, a’
unfolding poincare-on-ray-def
proof—
have a’ € circline-set x-axis
using <poincare-on-ray a’ On 2a» za (On # Par (za # 0» <a’ € unit-dise»
unfolding poincare-on-ray-def
using poincare-line-0-real-is-z-axis|of of-complex xa]
using poincare-between-poincare-line-uvz|of 01, of-complex xa a’
using poincare-between-poincare-line-uzv[of On of-complex xa a’|
by (auto simp add: cmod-eq-Re)

167
then obtain za’ where za’: a’ = of-complez 2a’ is-real xa’
using <a’ € unit-disc»
using circline-set-def on-circline-x-axis
by auto

hence —1 < Re xa’ Re xa’ < 1 2a' 4 0
using <a’ € unit-disc» <a’ # On»
by (auto simp add: cmod-eq-Re)

hence Re za’ > 0 Re xa’ < 1 is-real xa’
using <poincare-on-ray a’ On (of-complex za)»
using poincare-between-z-azis-Ouvlof Re za’ Re xa]
using poincare-between-z-azis-Ouv|of Re ta Re xa’
using circline-set-positive-x-axis-I[of Re xa’|
using xa xa’ complez-of-real-Re
unfolding poincare-on-ray-def
by (smt of-real-0, linarith, blast)

moreover

obtain zx where is-real «x Re xz > 0 Re rx < 1 & = of-complex xx
using x
unfolding positive-x-azis-def
using circline-set-def cmod-eq-Re on-circline-a-axis
by auto

ultimately

show poincare-between 0p x a’ V poincare-between On a’ x
using <a’ = of-complex xa’>
by (smt <a’ € unit-disc> arg-0-iff poincare-between-Ouv poincare-between-def to-complex-of-complex
2(1))
qed

qed

thus ?thesis
using (x € unit-discy
unfolding poincare-ray-meets-line-def poincare-on-line-def
by (metis insert-commute)
qed
qed
next
show a # 0;
proof (rule ccontr)
assume — ?thesis
then obtain k where k<0 to-complex ?a1 = cor k * to-complex ?a2
using poincare-between-u0v[OF <?al € unit-disc» «?a2 € unit-discr «?al # On» (?a2 F On>]
using <poincare-between ?a1 a ?a2>
by auto
hence to-complex il = cor k * to-complex i2 k < 0
by auto
hence 0), € circline-set (poincare-line x1 x2)
using ideal-points-proportionallof poincare-line x1 x2 il i2 k| <ideal-points (poincare-line x1 x2) = {i1,
i2}>
using is-poincare-line-poincare-line[OF «11 # x2)]
by simp
thus False
using ‘7~ poincare-collinear {On, c1, t2}>
using is-poincare-line-poincare-line[OF «11 # x2)]
unfolding poincare-collinear-def
by (meson «a1 # x2) empty-subsetl insert-subset poincare-line-circline-set(1) poincare-line-circline-set(2))
qed
next
fix yu
let ?R’= a zero. V a’ al a2 x1 x2 il i2. PR zero a’ al a2 c1 x2 il i2a

168
let ?M = moebius-pt (moebius-rotation )
assume *: u € unit-disc u # Op, and **: ?R'(?M u) On
have uf: unit-disc-fix (moebius-rotation ~)
by simp
have ?M 0n = On
by auto
hence «+: ?R’ (?M u) (2M 0n)
using **
by simp
show ?R’ u 0;
proof (rule alll)+
fix a’ al a2 rl x2 il i2
have if: il € unit-circle-set —+ moebius-pt (mocbius-rotation p) (of-complex (to-complez il / 2))
of-complex (to-complex (moebius-pt (moebius-rotation y) i1) / 2)
using wunit-circle-set-def by force

have i2: i2 € unit-circle-set —+ moebius-pt (mocbius-rotation p) (of-complex (to-complez i2 / 2))
of-complex (to-complex (moebius-pt (moebius-rotation y) i2) / 2)
using wunit-circle-set-def by force

show ?R 0; a’ al a2 21 72 il i2u
using **[rule-format, of ?M a’ ?M x1 ?M x2 ?M il ?M i2 2M al ?M a2] uf *
apply (auto simp del: moebius-pt-mocbius-rotation-zero moebius-pt-moebius-rotation)
using i1 i2
by simp
qed
qed
thus ?thesis
using ‘a’ € unit-discy (tl € unit-discy (22 € unit-disc> «x1 4 22>
using (7- poincare-collinear {0;,, x1, 22}» <ideal-points ?lx = {i1, i2}» «il # i2>
using <?a1 # ?a2> <poincare-collinear {0n, ?a1, i1}) «poincare-collinear {0;, ?a2, i2}>
using <?a1 € unit-discy «?a2 € unit-discy <i1 € unit-circle-sety «i2 € unit-circle-sety
using <poincare-on-ray a' 0; a> <a’ A On» <poincare-between ?al a ?a2> 1a A Pal» <a A 2a2>
by blast
qed
qed

moreover

have — poincare-on-line 0; ?a1 ?a2
proof
assume *: poincare-on-line 0; ?al ?a2
hence poincare-collinear {0;, ?a1, ?a2}
unfolding poincare-on-line-def
by simp
hence poincare-line On ?a1 = poincare-line 0; ?a2
using poincare-collinear3-poincare-lines-equal-general[of 0, ?a1 ?a2]
using <?al € unit-disc» «?al # On» «?a2 € unit-disc» «?a2 # On»
by (metis inversion-noteg-unit-disc zero-in-unit-disc)

have il € circline-set (poincare-line 0, ?a1)
using <poincare-collinear {On, ?a1, i1}>
using poincare-collinear3-poincare-line-general|of i1 On ?a1]
using (?al € unit-disc) «?al # On»
by (metis insert-commute inversion-noteg-unit-disc zero-in-unit-disc)
moreover
have i2 € circline-set (poincare-line 0, ?a1)
using <poincare-collinear {On, ?a2, i2}>
using poincare-collinear3-poincare-line-general|of i2 On ?a2]
using <?a2 € unit-disc) «?a2 4 On» <poincare-line 0, ?a1 = poincare-line On ?a2>
by (metis insert-commute inversion-noteg-unit-disc zero-in-unit-disc)

ultimately
have poincare-collinear {On, i1, i2}

using <?al € unit-disc) «?a1 # On» <poincare-collinear {On, ?a1, i1}>

169
by (smt insert-subset poincare-collinear-def unique-poincare-line zero-in-unit-disc)
hence 0);, € circline-set (poincare-line i1 i2)

using poincare-collinear3-poincare-line-general{of On i1 i2|

using <i1 4 i2> <i2 € unit-circle-set» unit-circle-set-def

by force

moreover

have ?lx = ?li
using <ideal-points ?lx = {i1, i2}> «a1 # x2» ideal-points-line-unique
by auto

ultimately

show False
using ‘7— poincare-collinear {On, t1, 22}>
using (zl # £2) poincare-line-poincare-collinear3-general
by auto
qed

ultimately

show ?thesis
using <?al € unit-disc» «?a2 € unit-discy
by blast
qed
qed
qed
thus ?thesis
using ‘zl € unit-disc» «x2 € unit-disc «- poincare-collinear {a, x1, x2}>
by blast
qed
