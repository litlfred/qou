---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-061-upper-dimension-axiom
section_title: "Upper dimension axiom"
section_number: null
pages: 141-143
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma upper-dimension-axiom:
assumes in-disc: x € unit-disc y € unit-disc z € unit-disc u € unit-disc v € unit-disc
assumes poincare-distance x u = poincare-distance x v
poincare-distance y u = poincare-distance y v
poincare-distance z u = poincare-distance z v
uZxu
shows poincare-between x y z V poincare-between y z x V poincare-between z x y
proof (cases z= yVy=zV 4= 2)
case True
thus ?thesis
using in-disc
by auto
next
case False
hencex Ayr A#zyF#z
by auto
let ?cong = \ a b a’ b’. poincare-distance a b = poincare-distance a’ b’
have V zuv. z € unit-disc \ u € unit-disc A v € unit-disc \
?congzuxu A ?congyuyudA econgzuzv Aufxv—+
poincare-collinear {x, y, z} (is ?P x y)
proof (rule wlog-positive-x-azis[;where P=?P])
fix x
assume 2: is-real tr 0 < Rex Rex < 1
hence z 4 0
by auto
have 0), € circline-set z-axis
by simp
show ?P 0p (of-complex x)
proof safe
fix zuv
assume in-disc: z € unit-disc u € unit-disc v € unit-disc
then obtain z’ u’ v'! where zuv: z = of-compler z' u = of-complex u' v = of-complex v'
using inf-or-of-complez|of z| inf-or-of-complex|of u] inf-or-of-complez(of v]
by auto

assume cong: ?cong On u 0; v ?cong (of-complex x) u (of-complex x) v ?congzuzuvufx#u

let ?r0 = poincare-distance 0, u and
’rxz = poincare-distance (of-complex x) u

have ?r0 > 0 ?ra > 0
using in-disc cong

141
of On ul poincare-distance-ge0|of On ul
of On v) poincare-distance-ge0 [of 0), v|
of of-complex x u] poincare-distance-ge0[of of-complex x u]
of of-complex x v| poincare-distance-ge0 [of of-complex x v|

using poincare-distance-eq-0-iff
using poincare-distance-eq-0-iff
using poincare-distance-eq-0-iff
using poincare-distance-eq-0-iff
using x

by (auto simp add: cmod-eq-Re)

let ?pc0 = poincare-circle 0; ?r0 and
?pcx = poincare-circle (of-complex x) ?rx
have u € ?pc0 M ?pcxv € ?pcO ON ?pcx
using in-disc cong
by (auto simp add: poincare-circle-def )
hence u = conjugate v
using intersect-poincare-circles-x-axis|of 0 x ?r0 ?rx u v|
using xz «x # 0) (u # vy (?r0 > Oy «?rx > 0»
by simp

let ?ru = poincare-distance u z
have ?ru > 0
using poincare-distance-ge0[of u z] in-disc
using cong
using poincare-distance-eq-0-iff [of z u| poincare-distance-eq-0-iff lof z v]
using poincare-distance-eq-0-iff
by force

have z € poincare-circle u ?ru M poincare-circle v ?ru
using cong in-disc
unfolding poincare-circle-def
by (simp add: poincare-distance-sym)

hence is-real z’
using intersect-poincare-circles-conjugate-centers[of uv ?ru z] <u = conjugate v» zuv
using in-disc «u # v> «?ru > 0»
by simp

thus poincare-collinear {0n, of-complex x, z}
using poincare-line-0-real-is-z-azis[of of-complex x] x (x # 0» zuv ‘On € circline-set x-axis»
unfolding poincare-collinear-def
by (rule-tac x=x-azis in exl, auto simp add: circline-set-x-azis)
qed
next
fix Mry
assume 1: unit-disc-fiz M x € unit-disc y € unit-disc x # y
assume 2: ?P (moebius-pt M x) (moebius-pt M y)
show ?P ry
proof safe
fix zuv
assume z € unit-disc u € unit-disc v € unit-disc
’congxruxy ?congyuyv ?congzuzvuxzyu
hence poincare-collinear {moebius-pt M x, moebius-pt M y, moebius-pt M z}
using 1 2[rule-format, of moebius-pt M z moebius-pt M u moebius-pt M v|
by simp
then obtain p where is-poincare-line p {moebius-pt M x, moebius-pt M y, moebius-pt M z} C circline-set p
unfolding poincare-collinear-def
by auto
thus poincare-collinear {x, y, z}
using (unit-disc-fir My
unfolding poincare-collinear-def
by (rule-tac x=moebius-circline (—M) p in eal, auto)
qed
qed fact+

thus ?thesis
using assms
using poincare-collinear3-between|of x y 2]
using poincare-between-rev

142
by auto
qed
