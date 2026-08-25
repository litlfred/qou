---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-025-h-circles-in-the-poincaré-model
section_title: "H-circles in the Poincaré model"
section_number: null
pages: 67-71
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Circles consist of points that are at the same distance from the center.
deﬁnition poincare-circle :: complex-homo⇒ real⇒ complex-homo set where
poincare-circle z r ={z ′. z ′∈ unit-disc∧ poincare-distance z z ′ = r}
Each h-circle in the Poincaré model is represented by an Euclidean circle in the model — the center and radius
of that euclidean circle are determined by the following formulas.
deﬁnition poincare-circle-euclidean :: complex-homo⇒ real⇒ euclidean-circle where
poincare-circle-euclidean z r =
(let R = ( cosh r − 1 ) / 2 ;
z ′ = to-complex z ;
cz = 1− (cmod z ′)2;
k = cz∗ R + 1
in (z ′/ k, cz∗ sqrt(R∗ (R + 1 )) / k))
That Euclidean circle has a positive radius and is always fully within the disc.
lemma poincare-circle-in-disc:
assumes r > 0 and z∈ unit-disc and (ze, re) = poincare-circle-euclidean z r
shows cmod ze < 1 re > 0∀ x∈ circle ze re. cmod x < 1
proof−
let ?R = ( cosh r − 1 ) / 2
let ?z ′ = to-complex z
let ?cz = 1− (cmod ?z ′)2
let ?k = ?cz∗ ?R + 1
let ?ze = ?z ′/ ?k
let ?re = ?cz∗ sqrt(?R∗ (?R + 1 )) / ?k
67
from ‹z∈ unit-disc›
obtain z ′ where z ′: z = of-complex z ′
using inf-or-of-complex[of z ]
by auto
hence z ′ = ?z ′
by simp
obtain cz where cz: cz = ( 1− (cmod z ′)2)
by auto
have cz > 0 cz ≤ 1
using ‹z∈ unit-disc› z ′ cz
using unit-disc-cmod-square-lt-1
by fastforce+
obtain R where R: R = ?R
by blast
have R > 0
using cosh-gt-1[of r ] ‹r > 0 ›
by (subst R ) simp
obtain k where k: k = cz∗ R + 1
by auto
have k > 1
using k ‹R > 0 › ‹cz > 0 ›
by simp
hence cmod k = k
by simp
let ?RR = cz∗ sqrt(R∗ (R + 1 )) / k
have cmod z ′ + cz∗ sqrt(R∗ (R + 1 )) < k
proof−
have ((R+1 )−R)2 > 0
by simp
hence (R+1 )2− 2∗R∗(R+1 ) + R2 > 0
unfolding power2-diﬀ
by (simp add : ﬁeld-simps)
hence (R+1 )2 + 2∗R∗(R+1 ) + R2− 4∗R∗(R+1 ) > 0
by simp
hence (2∗R+1 )2 / 4 > R∗(R+1 )
using power2-sum[of R +1 R ]
by (simp add : ﬁeld-simps)
hence sqrt(R∗(R+1 )) < (2∗R+1 ) / 2
using ‹R > 0 ›
by (smt arith-geo-mean-sqrt power-divide real-sqrt-four real-sqrt-pow2 zero-le-mult-iﬀ )
hence sqrt(R∗(R+1 ))− R < 1/2
by (simp add : ﬁeld-simps)
hence (1 + ( cmod z ′))∗ (sqrt(R∗(R+1 ))− R) < (1 + ( cmod z ′))∗ (1 / 2 )
by (subst mult-strict-left-mono, simp, smt norm-not-less-zero, simp)
also have ... <1
using ‹z∈ unit-disc› z ′
by auto
ﬁnally have (1− cmod z ′)∗ ((1 + cmod z ′)∗ (sqrt(R∗(R+1 ))− R)) < (1− cmod z ′)∗ 1
using ‹z∈ unit-disc› z ′
by (subst mult-strict-left-mono, simp-all )
hence cz∗ (sqrt (R∗(R+1 ))− R) < 1− cmod z ′
using square-diﬀ-square-factored[of 1 cmod z ′]
by (subst cz, subst (asm) mult.assoc[symmetric], simp add : power2-eq-square ﬁeld-simps)
hence cmod z ′ + cz∗ sqrt(R∗(R+1 )) < 1 + R∗ cz
by (simp add : ﬁeld-simps)
68
thus ?thesis
using k
by (simp add : ﬁeld-simps)
qed
hence cmod z ′/ k + cz∗ sqrt(R∗ (R + 1 )) / k < 1
using ‹k > 1 ›
unfolding add-divide-distrib[symmetric]
by simp
hence cmod (z ′/ k) + cz∗ sqrt(R∗ (R + 1 )) / k < 1
using ‹k > 1 ›
by simp
hence cmod ?ze + ?re < 1
using k cz ‹R = ?R› z ′
by simp
moreover
have cz∗ sqrt(R∗ (R + 1 )) / k > 0
using ‹cz > 0 › ‹R > 0 › ‹k > 1 ›
by auto
hence ?re > 0
using k cz ‹R = ?R› z ′
by simp
moreover
have cmod ?ze < 1
using ‹cmod ?ze + ?re < 1 › ‹?re > 0 ›
by simp
moreover
have ze = ?ze re = ?re
using ‹(ze, re) = poincare-circle-euclidean z r ›
unfolding poincare-circle-euclidean-def Let-def
by simp-all
moreover
have∀ x∈ circle ze re. cmod x ≤ cmod ze + re
using norm-triangle-ineq2[of - ze ]
unfolding circle-def
by (smt mem-Collect-eq )
ultimately
show cmod ze < 1 re > 0∀ x∈ circle ze re. cmod x < 1
by auto
qed
The connection between the points on the h-circle and its corresponding Euclidean circle.
lemma poincare-circle-is-euclidean-circle:
assumes z∈ unit-disc and r > 0
shows let (Ze, Re) = poincare-circle-euclidean z r
in of-complex ‘ (circle Ze Re ) = poincare-circle z r
proof−
{
ﬁx x
let ?z = to-complex z
from assms obtain z ′ where z ′: z = of-complex z ′ cmod z ′< 1
using inf-or-of-complex[of z ]
by auto
have∗: ⋀ x. cmod x < 1 =⇒ 1− (cmod x )2 > 0
by (metis less-iﬀ-diﬀ-less-0 minus-diﬀ-eq mult .left-neutral neg-less-0-iﬀ-less norm-mult-less norm-power power2-eq-square)
69
let ?R = ( cosh r − 1 ) / 2
obtain R where R: R = ?R
by blast
let ?cx = 1− (cmod x )2 and ?cz = 1− (cmod z ′)2 and ?czx = ( cmod (z ′− x))2
let ?k = 1 + R∗ ?cz
obtain k where k: k = ?k
by blast
have R > 0
using R cosh-gt-1 [OF ‹r > 0 ›]
by simp
hence k > 1
using assms z ′ k∗[of z ′]
by auto
hence∗∗: cor k ⁄= 0
by (smt of-real-eq-0-iﬀ )
have of-complex x ∈ poincare-circle z r ←→ cmod x < 1∧ poincare-distance z (of-complex x ) = r
unfolding poincare-circle-def
by auto
also have ...←→ cmod x < 1∧ poincare-distance-formula′ ?z x = cosh r
using poincare-distance-formula[of z of-complex x ] cosh-dist[of z of-complex x ]
unfolding poincare-distance-formula-def
using assms
using arcosh-cosh-real
by auto
also have ...←→ cmod x < 1∧ ?czx / (?cz∗ ?cx) = ?R
using z ′
by (simp add : ﬁeld-simps)
also have ...←→ cmod x < 1∧ ?czx = ?R∗ ?cx∗ ?cz
using assms z ′∗[of z ′]∗[of x ]
using nonzero-divide-eq-eq[of (1− (cmod x )2)∗ (1− (cmod z ′)2) ( cmod (z ′− x))2 ?R]
by (auto, simp add : ﬁeld-simps)
also have ...←→ cmod x < 1∧ (z ′− x)∗ (cnj z ′− cnj x ) = R∗ ?cz∗ (1− x∗ cnj x ) ( is -←→ -∧ ?l = ?r)
proof−
let ?l = ( z ′− x)∗ (cnj z ′− cnj x ) and ?r = R∗ (1− Re (z ′∗ cnj z ′))∗ (1− x∗ cnj x )
have is-real ?l
using eq-cnj-iﬀ-real[of ?l ]
by simp
moreover
have is-real ?r
using eq-cnj-iﬀ-real[of 1 − x∗ cnj x ]
using Im-complex-of-real[of R ∗ (1− Re (z ′∗ cnj z ′))]
by simp
ultimately
show ?thesis
apply (subst R [symmetric])
apply (subst cmod-square )+
apply (subst complex-eq-if-Re-eq, simp-all add : ﬁeld-simps)
done
qed
also have ...←→ cmod x < 1∧ z ′∗ cnj z ′− x∗ cnj z ′− cnj x ∗ z ′ + x∗ cnj x = R∗ ?cz− R∗ ?cz∗ x∗ cnj x
unfolding right-diﬀ-distrib left-diﬀ-distrib
by (simp add : ﬁeld-simps)
also have ...←→ cmod x < 1 ∧ k∗ (x∗ cnj x )− x∗ cnj z ′− cnj x ∗ z ′ + z ′∗ cnj z ′ = R∗ ?cz (is -←→ -∧
?lhs = ?rhs)
by (subst k ) ( auto simp add : ﬁeld-simps)
also have ...←→ cmod x < 1∧ (k∗ x∗ cnj x − x∗ cnj z ′− cnj x ∗ z ′ + z ′∗ cnj z ′) / k = ( R∗ ?cz) / k
using∗∗
by (auto simp add : Groups.mult-ac(1 ))
also have ...←→ cmod x < 1∧ x∗ cnj x − x∗ cnj z ′/ k− cnj x ∗ z ′/ k + z ′∗ cnj z ′/ k = ( R∗ ?cz) / k
using∗∗
70
unfolding add-divide-distrib diﬀ-divide-distrib
by auto
also have ...←→ cmod x < 1∧ (x− z ′/k)∗ cnj(x− z ′/k) = ( R∗ ?cz) / k + ( z ′/ k)∗ cnj(z ′/ k)− z ′∗ cnj z ′
/ k
by (auto simp add : ﬁeld-simps diﬀ-divide-distrib )
also have ...←→ cmod x < 1∧ (cmod (x− z ′/k))2 = ( R∗ ?cz) / k + ( cmod z ′)2 / k 2− (cmod z ′)2 / k
apply (subst complex-mult-cnj-cmod )+
apply (subst complex-eq-if-Re-eq)
apply (simp-all add : power-divide)
done
also have ...←→ cmod x < 1∧ (cmod (x− z ′/k))2 = ( R∗ ?cz∗ k + ( cmod z ′)2− (cmod z ′)2∗ k) / k 2
using∗∗
unfolding add-divide-distrib diﬀ-divide-distrib
by (simp add : power2-eq-square)
also have ...←→ cmod x < 1∧ (cmod (x− z ′/k))2 = ?cz 2∗ R∗ (R + 1 ) / k 2 (is -←→ -∧ ?a2 = ?b)
proof−
have∗: R∗ (1− (cmod z ′)2)∗ k + ( cmod z ′)2− (cmod z ′)2∗ k = ( 1− (cmod z ′)2)2∗ R∗ (R + 1 )
by (subst k )+ ( simp add : ﬁeld-simps power2-diﬀ )
thus ?thesis
by (subst∗, simp)
qed
also have ...←→ cmod x < 1∧ cmod (x− z ′/k) = ?cz∗ sqrt (R∗ (R + 1 )) / k
using ‹R > 0 ›∗[of z ′]∗∗ ‹k > 1 › ‹z∈ unit-disc› z ′
using real-sqrt-unique[of ?a ?b , symmetric]
by (auto simp add : real-sqrt-divide real-sqrt-mult power-divide power-mult-distrib )
ﬁnally
have of-complex x ∈ poincare-circle z r ←→ cmod x < 1∧ x∈ circle (z ′/k) ( ?cz∗ sqrt(R∗ (R+1 )) / k)
unfolding circle-def z ′ k R
by simp
hence of-complex x ∈ poincare-circle z r ←→ (let (Ze, Re) = poincare-circle-euclidean z r in cmod x < 1 ∧ x∈
circle Ze Re )
unfolding poincare-circle-euclidean-def Let-def circle-def
using z ′ R k
by (simp add : ﬁeld-simps)
hence of-complex x ∈ poincare-circle z r ←→ (let (Ze, Re) = poincare-circle-euclidean z r in x ∈ circle Ze Re )
using poincare-circle-in-disc[OF ‹r > 0 › ‹z∈ unit-disc›]
by auto
} note ∗ = this
show ?thesis
unfolding Let-def
proof safe
ﬁx Ze Re x
assume poincare-circle-euclidean z r = ( Ze, Re) x∈ circle Ze Re
thus of-complex x ∈ poincare-circle z r
using∗[of x ]
by simp
next
ﬁx Ze Re x
assume∗∗: poincare-circle-euclidean z r = ( Ze, Re) x∈ poincare-circle z r
then obtain x ′ where x ′: x = of-complex x ′
unfolding poincare-circle-def
using inf-or-of-complex[of x ]
by auto
hence x ′∈ circle Ze Re
using∗[of x ′]∗∗
by simp
thus x∈ of-complex ‘ circle Ze Re
using x ′
by auto
qed
qed
