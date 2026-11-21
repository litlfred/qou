---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-049-h-perpendicular-h-lines-in-the-poincaré-model
section_title: "H-perpendicular h-lines in the Poincaré model"
section_number: null
pages: 114-124
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
definition perpendicular-to-a-axis-cmat :: complea-mat = bool where
[simp]: perpendicular-to-z-axis-cmat H +—+ (let (A, B, C, D) = H in is-real B)

lift-definition perpendicular-to-x-axis-clmat :: circline-mat = bool is perpendicular-to-a-axis-cmat
done

lift-definition perpendicular-to-z-axis :: circline = bool is perpendicular-to-x-axis-clmat
by transfer auto

lemma perpendicular-to-x-axis:
assumes is-poincare-line H
shows perpendicular-to-z-axis H <—> perpendicular x-axis H
using assms
unfolding perpendicular-def
proof (transfer, transfer)
fix H
assume hh: hermitean H \ H # mat-zero is-poincare-line-cmat H
obtain A B C D where «: H = (A, B, C, D)
by (cases H, auto)
hence is-real A (cmod B)? > (cmod A)? H = (A, B, cnj B, A)
using hermitean-elems|of A B C D] hh
by auto

114
thus perpendicular-to-x-azis-cmat H =
(cos-angle-cmat (of-circline-cmat x-axis-cmat) (of-circline-cmat H) = 0)
using cmod-square|of B] cmod-square[of A]
by simp
qed

lemma perpendicular-to-x-axis-y-avis:
assumes perpendicular-to-x-axis (poincare-line 0; (of-complex z)) z # 0
shows is-imag z
using assms
by (transfer, transfer, simp)

lemma wlog-perpendicular-azes:
assumes in-disc: u € unit-disc v € unit-disc z € unit-disc
assumes perpendicular: is-poincare-line H1 is-poincare-line H2 perpendicular H1 H2
assumes z € circline-set H1 ™ circline-set H2 u € circline-set H1 v € circline-set H2
assumes azes: /\ x y. [is-real x; 0 < Re x; Re x < 1; is-imag y; 0 < Im y; Imy < 1] => P On» (of-complex z)
(of-complex y)
assumes mocbius: \ M uv w. [unit-disc-fiz M; u € unit-disc; v € unit-disc; w € unit-disc; P (moebius-pt M u)
(moebius-pt M v) (moebius-pt Mw) ] => Puvw
assumes conjugate: /\ uv w. [lu € unit-disc; v € unit-disc; w € unit-disc; P (conjugate u) (conjugate v) (conjugate
w) |= Puvw
shows Pzuv
proof—
have V v H1 H2. is-poincare-line H1 A is-poincare-line H2 \ perpendicular H1 H2 \
z € circline-set H1 Q circline-set H2 \ u € circline-set H1 A v € circline-set H2 \ v € unit-disc —> P
zuu (is ?P zu)
proof (rule wlog-z-axis;where P=?P})
fix x
assume z: is-realz Rex > 0 Rex < 1
have of-complex x € unit-disc
using x
by (simp add: cmod-eq-Re)

show ?P 0), (of-complex x)
proof safe
fix v H1 H2
assume v € unit-disc
then obtain y where y: v = of-complex y
using inf-or-of-complez{of v|
by auto

assume 1: is-poincare-line H1 is-poincare-line H2 perpendicular H1 H2
assume 2: 0» € circline-set H1 On € circline-set H2 of-complex x € circline-set H1 v € circline-set H2

show P 0», (of-complez x) v
proof (cases of-complex x = On)
case True
show P 0), (of-complez x) v
proof (cases v = 0p)
case True
thus ?thesis
using <of-complez x = On»
using azes[of 0 0]
by simp
next
case False
show ?thesis
proof (rule wlog-rotation-to-positive-y-azis)
show v € unit-disc v # On
by fact+
next
fix y
assume is-imag y 0 < InyImy <1
thus P 0), (of-complex x) (of-complex y)

115
using z azes[of x y|
by simp
next
fix pu
assume u € unit-disc u # On
P Op (of-complex x) (moebius-pt (moebius-rotation vy) u)
thus P 0), (of-complex x) u
using <of-compler x = On»
using moebius[of moebius-rotation p On On ul
by simp
qed
qed
next
case False
hence «: poincare-line 0» (of-complex x) = x-axis
using x poincare-line-0-real-is-x-axis|of of-complex |
unfolding circline-set-x-axis
by auto
hence H1 = z-axis
using wnique-poincare-line[of 0), of-complex x H1| 1 2
using <of-complex x € unit-discy False
by simp
have is-imag y
proof (cases y = 0)
case True
thus ?thesis
by simp
next
case False
hence 0;, 4 of-complex y
using of-complez-zero-iff [of y]
by metis
hence H2 = poincare-line 0; (of-complex y)
using 1 2 <v € unit-disc»
using unique-poincare-line|[of 0), of-complex y H2| y
by simp
thus ?thesis
using 1 <H1 = z-axis»
using perpendicular-to-z-axis-y-axis|of y] False
using perpendicular-to-z-axis|of H2]
by simp
qed
show P 0), (of-complez x) v
proof (cases Im y > 0)
case True
thus ?thesis
using azes|of x y| x y <is-imag y> (v € unit-disc»
by (simp add: cmod-eq-Im)
next
case False
show ?thesis
proof (rule conjugate)
have Im (cnj y) < 1
using <u € unit-disc) y <is-imag y> eq-minus-cnj-iff-imag|of y]
by (simp add: cmod-eq-Im)
thus P (conjugate 01) (conjugate (of-complex x)) (conjugate v)
using <is-real x» eq-cnj-iff-reallof x] y ‘is-imag y»
using azes[OF 2, of cnj y| False
by simp
show 0, € unit-disc of-compler x € unit-disc v € unit-disc
by (simp, fact+)
qed
qed
qed
qed
next

116
show z € unit-disc u € unit-disc
by fact+
next
fix Muv
assume *: unit-disc-fir M u € unit-disc v € unit-disc
assume *: ?P (moebius-pt M u) (moebius-pt M v)
show ?P uv
proof safe
fix w H1 H2
assume **«: is-poincare-line H1 is-poincare-line H2 perpendicular H1 H2
u € circline-set H1 u € circline-set H2
v € circline-set H1 w € circline-set H2 w € unit-disc
thus Puvw
using mocebius[of M uv wv *
using **[rule-format, of moebius-circline M H1 mocbius-circline M H2 mocbius-pt M w]|
by simp
qed
qed
thus ?thesis
using assms
by blast
qed

lemma wlog-perpendicular-foot:
assumes in-disc: u € unit-disc v € unit-disc w € unit-disc z € unit-disc
assumes perpendicular: u # v is-poincare-line H perpendicular (poincare-line uv) H
assumes 2z € circline-set (poincare-line u v)  circline-set H w € circline-set H
assumes azes: /\ u v w. [is-real u; 0 < Re u; Re u < 1; is-real v; —1 < Rev; Rev < 1; ReuF Re v; is-imag w; 0
< Im w; Im w < 1] => P On (of-complex u) (of-complex v) (of-complez w)
assumes moebius: (| M zu v w. [unit-disc-fiz M; u € unit-disc; v € unit-disc; w € unit-disc; z € unit-disc; P
(moebius-pt M z) (moebius-pt M u) (moebius-pt M v) (moebius-pt Mw) ] => Pzuvw
assumes conjugate: \\ z uv w. [u € unit-disc; v € unit-disc; w € unit-disc; P (conjugate z) (conjugate u) (conjugate
v) (conjugate w) |] => Pzuvw
assumes perm: Pzvuw=> Pzuvw
shows Pzuvw
proof—
obtain mn where mn: m=uVm=vn=uVn=vmMAnMFzZ
using <u 4 v)
by auto

have n € circline-set (poincare-line z m)
using <z € circline-set (poincare-line u v) M circline-set H»
using mn
using unique-poincare-line[of z m poincare-line u v, symmetric] in-disc
by auto

have V n. n € unit-disc Am # nA n € circline-set (poincare-line zm) \ m £4 z —>+ Pzmnvw (is ?Qzmvw)
proof (rule wlog-perpendicular-axes[where P=?Q])
show is-poincare-line (poincare-line u v)
using <u 4 v)
by auto
next
show is-poincare-line H
by fact
next
show m € unit-disc m € circline-set (poincare-line u v)
using mn in-disc
by auto
next
show w € unit-disc z € unit-disc
by fact+
next
show z € circline-set (poincare-line u v) M circline-set H
by fact
next
show perpendicular (poincare-line uv) H

117
by fact
next
show w € circline-set H
by fact
next
fix ry
assume zy: is-real x 0 < Rea Rex < 1 is-imagy 0 <ImyImy< 1
show ?Q 0, (of-complex x) (of-complex y)
proof safe
fix n
assume n € unit-disc of-compler x A n
assume n € circline-set (poincare-line On (of-complex x)) of-complex x # On
hence n € circline-set z-axis
using poincare-line-0-real-is-z-axis[of of-complex x] xy
by (auto simp add: circline-set-x-azis)
then obtain n’ where n’: n = of-complezr n’
using inf-or-of-complez|of n] «n € unit-disc»
by auto
hence is-real n’
using <n € circline-set x-axis»
using of-complez-inj
unfolding circline-set-x-azxis
by auto
hence —1 < Ren’ Ren’ < 1
using <n € unit-disc) n’
by (auto simp add: cmod-eq-Re)

have Ren’ #4 Rex
using complez.expand|of n’ x] <is-real n'y <is-real x» <of-complez x # n> n'
by auto

have Re xz > 0
using zy <of-complex x # On)
by (cases Re x = 0, auto simp add: complex.expand)

show P 0), (of-complex x) n (of-complex y)
using azes[of x n'y] ty n' «Rex > 0» <is-real n'y «<-1 < Ren’ (Re n’ < 1) (Re n' # Re a>
by simp
qed
next
fix Muvw
assume 1: unit-disc-fiz M u € unit-disc v € unit-disc w € unit-disc
assume 2: ?Q (moebius-pt M u) (moebius-pt M v) (moebius-pt M w)
show ?Quvuw
proof safe
fix n
assume n € unit-disc v 4 nn € circline-set (poincare-line uv) v # u
thus Puvnw
using mocbius[of Mv nw u] 1 2[rule-format, of moebius-pt M n]
by fastforce
qed
next
fix uvw
assume 1: u € unit-disc v € unit-disc w € unit-disc
assume 2: ?Q (conjugate u) (conjugate v) (conjugate w)
show ?Quvuw
proof safe
fix n
assume n € unit-disc v 4 nn € circline-set (poincare-line uv) v # u
thus Puvnw
using conjugatelof vn w ul 1 2[rule-format, of conjugate n]
using conjugate-inj
by auto
qed
qed
thus ?thesis

118
using mn in-disc (n € circline-set (poincare-line z m)> perm
by auto
qed

lemma perpendicular-to-x-axis-intersects-x-axis:
assumes is-poincare-line H perpendicular-to-x-aris H
shows intersects-x-axis H
using assms hermitean-elems
by (transfer, transfer, auto simp add: cmod-eq-Re)

lemma perpendicular-intersects:
assumes is-poincare-line H1 is-poincare-line H2
assumes perpendicular H1 H2
shows 3 z. z € unit-disc \ z € circline-set H1 ™ circline-set H2 (is ?P' H1 H2)
proof—
have V H2. is-poincare-line H2 A perpendicular H1 H2 —+ ?P' H1 H2 (is ?P H1)
proof (rule wlog-line-z-azis)
show ?P x-axis
proof safe
fix H2
assume is-poincare-line H2 perpendicular z-axis H2
thus dz. z € unit-disc A z € circline-set x-axis M circline-set H2
using perpendicular-to-z-axis|of H2]
using perpendicular-to-z-axis-intersects-r-axis|of H2]
using intersects-x-azis-iff [of H2]
by auto
qed
next
fix M
assume unit-disc-fix M
assume *: ?P (moebius-circline M H1)
show ?P H1
proof safe
fix H2
assume is-poincare-line H2 perpendicular H1 H2
then obtain z where z € unit-disc z € circline-set (moebius-circline M H1) A z € circline-set (moebius-circline
M H2)
using *{rule-format, of moebius-circline M H2] <unit-disc-fix M>
by auto
thus dz. z € unit-disc A z € circline-set H1  circline-set H2
using (unit-disc-fir My
by (rule-tac z=moebius-pt (—M) z in ex!)
(metis IntI add.inverse-inverse circline-set-moebius-circline-iff moebius-pt-comp-inv-left_ uminus-moebius-def
unit-disc-fix-discI unit-disc-fiz-moebius-uminus)
qed
next
show is-poincare-line H1
by fact
qed
thus ?thesis
using assms
by auto
qed

definition calc-perpendicular-to-z-axis-cmat :: complex-vec = complet-mat where
[simp]: calc-perpendicular-to-x-axis-cmat z =
(let (21, 22) =z
in if zl*xcnj 22 + z2xcnj z1 = 0 then
(0, 1, 1, 0)
else
let A = zlxcnj z2 + 22xcnj 21;
B= —(z1*cnj z1 + 22*cnj z2)
in (A, B, B, A)

119
lift-definition calc-perpendicular-to-x-azis-clmat :: complet-homo-coords => circline-mat is calc-perpendicular-to-a-axis-cmat
by (auto simp add: hermitean-def mat-adj-def mat-cnj-def Let-def split: if-split-asm)

lift-definition calc-perpendicular-to-x-axis :: complex-homo => circline is calc-perpendicular-to-x-axis-clmat
proof (transfer)
fix zw
assume z # vec-zero w # vec-zero
obtain z1 22 wl w2 where zw: z = (21, 22) w = (wl, w2)
by (cases z, cases w, auto)
assume z %y w
then obtain k where *: k 4 0 wl = kxz1 w2 = kxz2
using zw
by auto
have wi * cnj w2 + w2 * cnj wl = (k * cnj k) * (21 * cnj 22 + 22 * cnj 21)
using *
by (auto simp add: field-simps)
moreover
have wi * cnj wl + w2 * cnj w2 = (k * cnj k) * (21 * cnj 21 + 22 * cnj 22)
using *
by (auto simp add: field-simps)
ultimately
show circline-eq-cmat (calc-perpendicular-to-x-axis-cmat z) (calc-perpendicular-to-x-axis-cmat w)
using zw *
apply (auto simp add: Let-def)
apply (rule-tac c=Re (k * cnj k) in ezl, auto simp add: complex.expand field-simps)
done
qed

lemma calc-perpendicular-to-x-azis:
assumes z # of-complex 1 z # of-complex (—1)
shows z € circline-set (calc-perpendicular-to-a-axis z) \
is-poincare-line (calc-perpendicular-to-z-axis z) A
perpendicular-to-x-axis (calc-perpendicular-to-x-axis z)
using assms
unfolding circline-set-def perpendicular-def
proof (simp, transfer, transfer)
fix z :: complex-vec
obtain z/ 22 where z: z = (z1, 22)
by (cases z, auto)
assume **: 4 z %, of-complez-cvec 1 7 z %y of-complex-cvec (— 1)
show on-circline-cmat-cvec (calc-perpendicular-to-«-axis-cmat z) z A
is-poincare-line-cmat (calc-perpendicular-to-x-axis-cmat z) \
perpendicular-to-x-axis-cmat (calc-perpendicular-to-x-axis-cmat 2)
proof (cases z1*cnj 22 + z2xcnj z1 = 0)
case True
thus ?thesis
using z
by (simp add: vec-cnj-def hermitean-def mat-adj-def mat-cnj-def mult.commute)
next
case False
hence 22 4 0
using z
by auto
hence Re (z2 * cnj 22) 4 0
using <z2 # 0>
by (auto simp add: complex.expand)

have z1 4 —22 A 21 # 22
proof (rule ccontr)
assume — thesis
hence z %y of-complez-cvec 1 V z %y of-complex-cvec (—1)
using z (22 # 0»
by auto
thus False
using **

120
by auto
qed

let ?A = z1xcnj 22 + z2*cnj zl and ?B = —(z1*cnj z1 + 22x«cnj 22)
have Re(zl*cnj z1 + 22*cnj z2) > 0

by auto
hence Re ?B < 0

by (smt uminus-complex.simps(1))

hence abs (Re ?B) = — Re ?B
by auto
also have ... = (Re 12)? + (Im 12)? + (Re 22)? + (Im 22)?

by (simp add: power2-eq-square|symmetric])
also have ... > abs (Re ?A)
proof (cases Re ?A > 0)
case False
have (Re z1 + Re 22)? + (Im zl + Im 22)? > 0
using (zl 4 —22 A zl # 22)
by (metis add.commute add.inverse-unique complez-neq-0 plus-complex.code plus-complez.simps)
thus ?thesis
using False
by (simp add: power2-sum power2-eq-square field-simps)
next
case True
have (Re z1 — Re 22)? + (Im z1 — Im z2)? > 0
using (zl 4 —22 A zl # 22)
by (meson complex-eq-iff right-minus-eq sum-power2-gt-zero-iff )
thus ?thesis
using True
by (simp add: power2-sum power2-eq-square field-simps)
qed
finally
have abs (Re ?B) > abs (Re ?A)

moreover
have cmod ?B = abs (Re ?B) cmod ?A = abs (Re ?A)
by (simp-all add: cmod-eq-Re)
ultimately
have (cmod ?B)? > (cmod ?A)?
by (smt power2-le-imp-le)
thus ?thesis
using z False
by (simp-all add: Let-def hermitean-def mat-adj-def mat-cnj-def cmod-eq-Re vec-cnj-def field-simps)
qed
qed

lemma ex-perpendicular:
assumes is-poincare-line H z € unit-disc
shows 4 H’. is-poincare-line H' \ perpendicular H H' A z € circline-set H' (is ?P’ H z)
proof—
have V z. z € unit-disc —> ?P' H z (is ?P H)
proof (rule wlog-line-z-azis)
show ?P x-axis
proof safe
fix z
assume z € unit-disc
then have z # of-complex 1 z # of-complex (—1)
by auto
thus ?P’ z-axis z
using <z € unit-discy
using calc-perpendicular-to-x-axis|of z| perpendicular-to-x-axis
by (rule-tac x = calc-perpendicular-to-x-axis z in exI, auto)
qed
next
fix M
assume unit-disc-fix M
assume *: ?P (moebius-circline M H)

121
show ?P H
proof safe
fix z
assume z € unit-disc
hence moebius-pt M z € unit-disc
using (unit-disc-fir My
by auto
then obtain H’ where *: is-poincare-line H' perpendicular (moebius-circline MH) H' moebius-pt M z € circline-set
H!
using *
by auto
have h: H = moebius-circline (—M) (moebius-circline M H)
by auto
show ?P! H z
using * <unit-disc-fix M»
apply (subst h)
apply (rule-tac s=moebius-circline (—M) H’' in eal)
apply (simp del: moebius-circline-comp-inv-left)
done
qed
qed fact
thus ?thesis
using assms
by simp
qed

lemma ez-perpendicular-foot:
assumes is-poincare-line H z € unit-disc
shows 3 H’. is-poincare-line H' \ z € circline-set H' \ perpendicular H H' A
(4 2’ € unit-disc. z' € circline-set H' Q circline-set H)
using assms
using ex-perpendicular[OF assms]
using perpendicular-intersects|of H]
by blast

lemma Pythagoras:
assumes in-disc: u € unit-disc v € unit-disc w € unit-disc v # w
assumes distinct[u, v, w]) —> perpendicular (poincare-line u v) (poincare-line u w)
shows cosh (poincare-distance v w) = cosh (poincare-distance u v) * cosh (poincare-distance u w) (is ?P’ uv w)
proof (cases distinct [u, v, w])
case False
thus ?thesis
using in-disc
by (auto simp add: poincare-distance-sym)
next
case True
have distinct [u, v, w] — ?P'’uvw (is ?P uv w)
proof (rule wlog-perpendicular-axes[where P=?P])
show is-poincare-line (poincare-line u v) is-poincare-line (poincare-line u w)
using <distinct [u, v, w]>
by simp-all
next
show perpendicular (poincare-line u v) (poincare-line u w)
using True assms
by simp
next
show u € unit-disc v € unit-disc w € unit-disc
by fact+
next
show v € circline-set (poincare-line u v) w € circline-set (poincare-line u w)
u € circline-set (poincare-line u v) M circline-set (poincare-line u w)
using <distinct [u, v, w]>
by auto
next
fix ry
assume z: is-realz 0 < Rex Rex < 1

122
assume y: is-imag y 0 < ImyImy < 1

have of-complex x € unit-disc of-complex y € unit-disc
using x y
by (simp-all add: cmod-eq-Re cmod-eq-Im)

show ?P 0; (of-complex x) (of-complez y)
proof
assume distinct [On, of-complex x, of-complex y|
hence zr 4 0y#O
by auto

let ?den1 = 1 — (cmod x)? and ?den2 = 1 — (cmod y)?
have ?denl > 0 ?den2 > 0

using x y

by (simp-all add: cmod-eq-Re cmod-eq-Im abs-square-less-1)

let ?d1 = 1 + 2 « (emod 2)? / ?denl

have cosh (poincare-distance 0; (of-complex x)) = ?d1
using <?den1 > 0»
using poincare-distance-formulalof 0n of-complex x] <of-complex x € unit-disc»
by simp

moreover

let ?d2 = 1 + 2 « (cmod y)? / ?den2

have cosh (poincare-distance 0; (of-complex y)) = ?d2
using <?den2 > 0) <of-complex y € unit-disc»
using poincare-distance-formulalof On of-complex y|
by simp

moreover
let ?den = ?den1 * ?den2
let ?d? = 1 + 2 « (emod (x — y))? / ?den
have cosh (poincare-distance (of-complex x) (of-complex y)) = ?d3
using <of-compler x € unit-disc) ‘of-complex y € unit-disc»
using <?den1 > 0» «?den2 > 0»
using poincare-distance-formula|of of-complex x of-complex y]
by simp
moreover
have ?d1 * ?d2 = ?d3
proof—
have ?d3 = ((1 — (cmod x)”) * (1 — (emod y)?) + 2 * (emod (a — y))?) / 2den
using <?den1 > 0» «?den2 > 0»
by (subst add-num-frac, simp, simp)
also have ... = (Re ((1 — & * cnj xz) * (1 — y * enj y) + 2 * (a — y)xcnj (x — y)) / ?den)
using <is-real x) <is-imag y>
by ((subst cmod-square)+, simp)
also have ... = Re (1 + x * cnj xz * y * cnjy
+axcenjxr—2x*xyxcnjx—-2*xaxx*xcnjyty* cnjy) / ?den
by (simp add: field-simps)
also have ... = Re ((1 + y * cnj y) * (1 + @ * enjx)) / ?den
using <is-real x) <is-imag y>
by (simp add: field-simps)
finally
show ?thesis
using <?den1 > 0» «?den2 > 0»
apply (subst add-num-frac, simp)
apply (subst add-num-frac, simp)
apply simp
apply (subst cmod-square)+
apply (simp add: field-simps)
done
qed
ultimately
show ?P’ 0), (of-complex x) (of-complex y)

123
by simp
qed
next
fix Muvw
assume 1: unit-disc-fiz M u € unit-disc v € unit-disc w € unit-disc
assume 2: ?P (moebius-pt M u) (moebius-pt M v) (moebius-pt M w)
show ?Puvw
using 1 2
by auto
next
fix uvw
assume 1: u € unit-disc v € unit-disc w € unit-disc
assume 2: ?P (conjugate u) (conjugate v) (conjugate w)
show ?Puvw

using 1 2
by (auto simp add: conjugate-inj)
qed

thus ?thesis
using True
by simp
qed

end
