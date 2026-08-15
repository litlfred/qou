---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-058-upper-dimension-axiom
section_title: "Upper dimension axiom"
section_number: null
pages: 141-143
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma upper-dimension-axiom:
assumes in-disc: x∈ unit-disc y ∈ unit-disc z ∈ unit-disc u ∈ unit-disc v ∈ unit-disc
assumes poincare-distance x u = poincare-distance x v
poincare-distance y u = poincare-distance y v
poincare-distance z u = poincare-distance z v
u⁄= v
shows poincare-between x y z ∨ poincare-between y z x ∨ poincare-between z x y
proof (cases x = y∨ y = z∨ x = z)
case True
thus ?thesis
using in-disc
by auto
next
case False
hence x⁄= y x ⁄= z y ⁄= z
by auto
let ?cong = λ a b a ′ b ′. poincare-distance a b = poincare-distance a ′ b ′
have∀ z u v . z∈ unit-disc∧ u∈ unit-disc∧ v∈ unit-disc∧
?cong x u x v ∧ ?cong y u y v ∧ ?cong z u z v ∧ u⁄= v−→
poincare-collinear{x, y, z} (is ?P x y )
proof (rule wlog-positive-x-axis [where P=?P])
ﬁx x
assume x: is-real x 0 < Re x Re x < 1
hence x⁄= 0
by auto
have 0 h∈ circline-set x-axis
by simp
show ?P 0 h (of-complex x )
proof safe
ﬁx z u v
assume in-disc: z∈ unit-disc u ∈ unit-disc v ∈ unit-disc
then obtain z ′ u ′ v ′ where zuv: z = of-complex z ′ u = of-complex u ′ v = of-complex v ′
using inf-or-of-complex[of z ] inf-or-of-complex[of u ] inf-or-of-complex[of v ]
by auto
assume cong: ?cong 0 h u 0 h v ?cong (of-complex x ) u (of-complex x ) v ?cong z u z v u ⁄= v
let ?r0 = poincare-distance 0 h u and
?rx = poincare-distance (of-complex x ) u
have ?r0 > 0 ?rx > 0
using in-disc cong
141
using poincare-distance-eq-0-iﬀ[of 0 h u] poincare-distance-ge0[of 0 h u]
using poincare-distance-eq-0-iﬀ[of 0 h v] poincare-distance-ge0[of 0 h v]
using poincare-distance-eq-0-iﬀ[of of-complex x u ] poincare-distance-ge0[of of-complex x u ]
using poincare-distance-eq-0-iﬀ[of of-complex x v ] poincare-distance-ge0[of of-complex x v ]
using x
by (auto simp add : cmod-eq-Re)
let ?pc0 = poincare-circle 0 h ?r0 and
?pcx = poincare-circle (of-complex x ) ?rx
have u∈ ?pc0∩ ?pcx v ∈ ?pc0∩ ?pcx
using in-disc cong
by (auto simp add : poincare-circle-def)
hence u = conjugate v
using intersect-poincare-circles-x-axis[of 0 x ?r0 ?rx u v ]
using x ‹x⁄= 0 › ‹u⁄= v› ‹?r0 > 0 › ‹?rx > 0 ›
by simp
let ?ru = poincare-distance u z
have ?ru > 0
using poincare-distance-ge0[of u z ] in-disc
using cong
using poincare-distance-eq-0-iﬀ[of z u ] poincare-distance-eq-0-iﬀ[of z v ]
using poincare-distance-eq-0-iﬀ
by force
have z∈ poincare-circle u ?ru ∩ poincare-circle v ?ru
using cong in-disc
unfolding poincare-circle-def
by (simp add : poincare-distance-sym)
hence is-real z ′
using intersect-poincare-circles-conjugate-centers[of u v ?ru z ] ‹u = conjugate v › zuv
using in-disc ‹u⁄= v› ‹?ru > 0 ›
by simp
thus poincare-collinear{0 h, of-complex x, z}
using poincare-line-0-real-is-x-axis[of of-complex x ] x ‹x⁄= 0 › zuv ‹0 h∈ circline-set x-axis ›
unfolding poincare-collinear-def
by (rule-tac x =x-axis in exI, auto simp add : circline-set-x-axis)
qed
next
ﬁx M x y
assume 1 : unit-disc-ﬁx M x ∈ unit-disc y ∈ unit-disc x ⁄= y
assume 2 : ?P (moebius-pt M x ) ( moebius-pt M y )
show ?P x y
proof safe
ﬁx z u v
assume z∈ unit-disc u ∈ unit-disc v ∈ unit-disc
?cong x u x v ?cong y u y v ?cong z u z v u ⁄= v
hence poincare-collinear{moebius-pt M x , moebius-pt M y , moebius-pt M z}
using 1 2 [rule-format, of moebius-pt M z moebius-pt M u moebius-pt M v ]
by simp
then obtain p where is-poincare-line p{moebius-pt M x , moebius-pt M y , moebius-pt M z}⊆ circline-set p
unfolding poincare-collinear-def
by auto
thus poincare-collinear{x, y, z}
using ‹unit-disc-ﬁx M ›
unfolding poincare-collinear-def
by (rule-tac x =moebius-circline (−M ) p in exI, auto)
qed
qed fact+
thus ?thesis
using assms
using poincare-collinear3-between[of x y z ]
using poincare-between-rev
142
by auto
qed
