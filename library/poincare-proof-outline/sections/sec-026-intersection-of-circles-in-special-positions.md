---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-026-intersection-of-circles-in-special-positions
section_title: "Intersection of circles in special positions"
section_number: null
pages: 71-74
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Two h-circles centered at the x-axis intersect at mutually conjugate points
lemma intersect-poincare-circles-x-axis:
71
assumes z: is-real z1 and is-real z2 and r1 > 0 and r2 > 0 and
−1 < Re z1 and Re z1 < 1 and−1 < Re z2 and Re z2 < 1 and
z1⁄= z2
assumes x1 : x1∈ poincare-circle (of-complex z1 ) r1∩ poincare-circle (of-complex z2 ) r2 and
x2 : x2∈ poincare-circle (of-complex z1 ) r1∩ poincare-circle (of-complex z2 ) r2 and
x1⁄= x2
shows x1 = conjugate x2
proof−
have in-disc: of-complex z1 ∈ unit-disc of-complex z2 ∈ unit-disc
using assms
by (auto simp add : cmod-eq-Re)
obtain x1 ′ x2 ′ where x ′: x1 = of-complex x1 ′ x2 = of-complex x2 ′
using x1 x2
using inf-or-of-complex[of x1 ] inf-or-of-complex[of x2 ]
unfolding poincare-circle-def
by auto
obtain Ze1 Re1 where 1 : ( Ze1, Re1) = poincare-circle-euclidean (of-complex z1 ) r1
by (metis poincare-circle-euclidean-def)
obtain Ze2 Re2 where 2 : ( Ze2, Re2) = poincare-circle-euclidean (of-complex z2 ) r2
by (metis poincare-circle-euclidean-def)
have circle: x1 ′∈ circle Ze1 Re1 ∩ circle Ze2 Re2 x2 ′∈ circle Ze1 Re1 ∩ circle Ze2 Re2
using poincare-circle-is-euclidean-circle[of of-complex z1 r1 ]
using poincare-circle-is-euclidean-circle[of of-complex z2 r2 ]
using assms 1 2 ‹of-complex z1 ∈ unit-disc› ‹of-complex z2 ∈ unit-disc› x ′
by auto (metis image-iﬀ of-complex-inj )+
have is-real Ze1 is-real Ze2
using 1 2 ‹is-real z1 › ‹is-real z2 ›
by (simp-all add : poincare-circle-euclidean-def Let-def)
have Re1 > 0 Re2 > 0
using 1 2 in-disc ‹r1 > 0 › ‹r2 > 0 ›
using poincare-circle-in-disc(2 )[of r1 of-complex z1 Ze1 Re1 ]
using poincare-circle-in-disc(2 )[of r2 of-complex z2 Ze2 Re2 ]
by auto
have Ze1⁄= Ze2
proof (rule ccontr )
assume¬ ?thesis
hence eq: Ze1 = Ze2 Re1 = Re2
using circle(1 )
unfolding circle-def
by auto
let ?A = Ze1− Re1 and ?B = Ze1 + Re1
have ?A∈ circle Ze1 Re1 ?B ∈ circle Ze1 Re1
using ‹Re1 > 0 ›
unfolding circle-def
by simp-all
hence of-complex ?A∈ poincare-circle (of-complex z1 ) r1 of-complex ?B ∈ poincare-circle (of-complex z1 ) r1
of-complex ?A∈ poincare-circle (of-complex z2 ) r2 of-complex ?B ∈ poincare-circle (of-complex z2 ) r2
using eq
using poincare-circle-is-euclidean-circle[OF ‹of-complex z1 ∈ unit-disc› ‹r1 > 0 ›]
using poincare-circle-is-euclidean-circle[OF ‹of-complex z2 ∈ unit-disc› ‹r2 > 0 ›]
using 1 2
by auto blast +
hence poincare-distance (of-complex z1 ) ( of-complex ?A ) = poincare-distance (of-complex z1 ) ( of-complex ?B )
poincare-distance (of-complex z2 ) ( of-complex ?A ) = poincare-distance (of-complex z2 ) ( of-complex ?B )
−1 < Re (Ze1− Re1) Re (Ze1− Re1) < 1−1 < Re (Ze1 + Re1) Re (Ze1 + Re1) < 1
using ‹is-real Ze1 › ‹is-real Ze2 ›
unfolding poincare-circle-def
by (auto simp add : cmod-eq-Re)
hence z1 = z2
using unique-midpoint-x-axis[of Ze1 − Re1 Ze1 + Re1]
72
using ‹is-real Ze1 › ‹is-real z1 › ‹is-real z2 › ‹Re1 > 0 › ‹−1 < Re z1 › ‹Re z1 < 1 › ‹−1 < Re z2 › ‹Re z2 < 1 ›
by auto
thus False
using ‹z1⁄= z2 ›
by simp
qed
hence∗: ( Re x1 ′)2 + ( Im x1 ′)2− 2∗ Re x1 ′∗ Ze1 + Ze1∗ Ze1− cor (Re1∗ Re1) = 0
(Re x1 ′)2 + ( Im x1 ′)2− 2∗ Re x1 ′∗ Ze2 + Ze2∗ Ze2− cor (Re2∗ Re2) = 0
(Re x2 ′)2 + ( Im x2 ′)2− 2∗ Re x2 ′∗ Ze1 + Ze1∗ Ze1− cor (Re1∗ Re1) = 0
(Re x2 ′)2 + ( Im x2 ′)2− 2∗ Re x2 ′∗ Ze2 + Ze2∗ Ze2− cor (Re2∗ Re2) = 0
using circle-equation[of Re1 Ze1 ] circle-equation[of Re2 Ze2 ] circle
using eq-cnj-iﬀ-real[of Ze1 ] ‹is-real Ze1 › ‹Re1 > 0 ›
using eq-cnj-iﬀ-real[of Ze2 ] ‹is-real Ze2 › ‹Re2 > 0 ›
using complex-add-cnj[of x1 ′] complex-add-cnj[of x2 ′]
using distrib-left[of Ze1 x1 ′ cnj x1 ′] distrib-left[of Ze2 x1 ′ cnj x1 ′]
using distrib-left[of Ze1 x2 ′ cnj x2 ′] distrib-left[of Ze2 x2 ′ cnj x2 ′]
by (auto simp add : complex-mult-cnj power2-eq-square ﬁeld-simps )
hence− 2∗ Re x1 ′∗ Ze1 + Ze1∗ Ze1− cor (Re1∗ Re1) =− 2∗ Re x1 ′∗ Ze2 + Ze2∗ Ze2− cor (Re2∗ Re2)
− 2∗ Re x2 ′∗ Ze1 + Ze1∗ Ze1− cor (Re1∗ Re1) = − 2∗ Re x2 ′∗ Ze2 + Ze2∗ Ze2− cor (Re2∗ Re2)
by (smt add-diﬀ-cancel-right ′ add-diﬀ-eq eq-iﬀ-diﬀ-eq-0 minus-diﬀ-eq mult-minus-left of-real-minus )+
hence 2∗ Re x1 ′∗ (Ze2− Ze1 ) = ( Ze2∗ Ze2− cor (Re2∗ Re2))− (Ze1∗ Ze1− cor (Re1∗ Re1))
2∗ Re x2 ′∗ (Ze2− Ze1 ) = ( Ze2∗ Ze2− cor (Re2∗ Re2))− (Ze1∗ Ze1− cor (Re1∗ Re1))
by simp-all (simp add : ﬁeld-simps)+
hence 2∗ Re x1 ′∗ (Ze2− Ze1 ) = 2∗ Re x2 ′∗ (Ze2− Ze1 )
by simp
hence Re x1 ′ = Re x2 ′
using ‹Ze1⁄= Ze2 ›
by simp
moreover
hence (Im x1 ′)2 = ( Im x2 ′)2
using∗(1 )∗(3 )
by (simp add : ‹is-real Ze1 › complex-eq-if-Re-eq)
hence Im x1 ′ = Im x2 ′∨ Im x1 ′ =−Im x2 ′
using power2-eq-iﬀ
by blast
ultimately
show ?thesis
using x ′ ‹x1⁄= x2 ›
using complex.expand
by (metis cnj.code complex-surj conjugate-of-complex )
qed
Two h-circles of the same radius centered at mutually conjugate points intersect at the x-axis
lemma intersect-poincare-circles-conjugate-centers:
assumes in-disc: z1∈ unit-disc z2 ∈ unit-disc and
z1⁄= z2 and z1 = conjugate z2 and r > 0 and
u: u∈ poincare-circle z1 r ∩ poincare-circle z2 r
shows is-real (to-complex u )
proof−
obtain z1e r1e z2e r2e where
euclidean: ( z1e, r1e) = poincare-circle-euclidean z1 r
(z2e, r2e) = poincare-circle-euclidean z2 r
by (metis poincare-circle-euclidean-def)
obtain z1 ′ z2 ′ where z ′: z1 = of-complex z1 ′ z2 = of-complex z2 ′
using inf-or-of-complex[of z1 ] inf-or-of-complex[of z2 ] in-disc
by auto
obtain u ′ where u ′: u = of-complex u ′
using u inf-or-of-complex [of u ]
by (auto simp add : poincare-circle-def)
have z1 ′ = cnj z2 ′
using ‹z1 = conjugate z2 › z ′
by (auto simp add : of-complex-inj)
moreover
let ?cz = 1− (cmod z2 ′)2
73
let ?den = ?cz∗ (cosh r − 1 ) / 2 + 1
have ?cz > 0
using in-disc z ′
by (simp add : cmod-def )
hence ?den≥ 1
using cosh-gt-1[OF ‹r > 0 ›]
by auto
hence ?den⁄= 0
by simp
hence cor ?den ⁄= 0
using of-real-eq-0-iﬀ
by blast
ultimately
have r1e = r2e z1e = cnj z2e z1e ⁄= z2e
using z ′ euclidean ‹z1⁄= z2 ›
unfolding poincare-circle-euclidean-def Let-def
by simp-all metis
hence u ′∈ circle (cnj z2e ) r2e∩ circle z2e r2e z2e ⁄= cnj z2e
using euclidean u u ′
using poincare-circle-is-euclidean-circle[of z1 r ]
using poincare-circle-is-euclidean-circle[of z2 r ]
using in-disc ‹r > 0 ›
by auto (metis image-iﬀ of-complex-inj )+
hence (cmod (u ′− z2e))2 = ( cmod(u ′− cnj z2e ))2
by (simp add : circle-def )
hence (u ′− z2e)∗ (cnj u ′− cnj z2e ) = ( u ′− cnj z2e )∗ (cnj u ′− z2e)
by (metis complex-cnj-cnj complex-cnj-diﬀ complex-norm-square )
hence (z2e− cnj z2e )∗ (u ′− cnj u ′) = 0
by (simp add : ﬁeld-simps)
thus ?thesis
using u ′ ‹z2e⁄= cnj z2e › eq-cnj-iﬀ-real[of u ′]
by simp
qed
