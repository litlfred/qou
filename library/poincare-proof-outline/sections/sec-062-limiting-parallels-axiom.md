---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-062-limiting-parallels-axiom
section_title: "Limiting parallels axiom"
section_number: null
pages: 157-170
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Auxiliary deﬁnitions
deﬁnition poincare-on-line where
poincare-on-line p a b ←→ poincare-collinear{p, a, b}
deﬁnition poincare-on-ray where
poincare-on-ray p a b ←→ poincare-between a p b ∨ poincare-between a b p
deﬁnition poincare-in-angle where
poincare-in-angle p a b c ←→
b⁄= a∧ b⁄= c∧ p⁄= b∧ (∃ x∈ unit-disc. poincare-between a x c ∧ x⁄= a∧ x⁄= c∧ poincare-on-ray p b x )
deﬁnition poincare-ray-meets-line where
poincare-ray-meets-line a b c d ←→ (∃ x∈ unit-disc. poincare-on-ray x a b ∧ poincare-on-line x c d )
All points on ray are collinear
lemma poincare-on-ray-poincare-collinear:
assumes p∈ unit-disc and a∈ unit-disc and b∈ unit-disc and poincare-on-ray p a b
shows poincare-collinear{p, a, b}
using assms poincare-between-poincare-collinear
unfolding poincare-on-ray-def
by (metis insert-commute )
H-isometries preserve all deﬁned auxiliary relations
lemma unit-disc-ﬁx-preserves-poincare-on-line [simp]:
assumes unit-disc-ﬁx M and p∈ unit-disc a ∈ unit-disc b ∈ unit-disc
shows poincare-on-line (moebius-pt M p ) ( moebius-pt M a ) ( moebius-pt M b )←→ poincare-on-line p a b
using assms
unfolding poincare-on-line-def
by auto
157
lemma unit-disc-ﬁx-preserves-poincare-on-ray [simp]:
assumes unit-disc-ﬁx M p ∈ unit-disc a ∈ unit-disc b ∈ unit-disc
shows poincare-on-ray (moebius-pt M p ) ( moebius-pt M a ) ( moebius-pt M b )←→ poincare-on-ray p a b
using assms
unfolding poincare-on-ray-def
by auto
lemma unit-disc-ﬁx-preserves-poincare-in-angle [simp]:
assumes unit-disc-ﬁx M p ∈ unit-disc a ∈ unit-disc b ∈ unit-disc c ∈ unit-disc
shows poincare-in-angle (moebius-pt M p ) ( moebius-pt M a ) ( moebius-pt M b ) ( moebius-pt M c )←→ poincare-in-angle
p a b c (is ?lhs←→ ?rhs)
proof
assume ?lhs
then obtain Mx where∗: Mx∈ unit-disc
poincare-between (moebius-pt M a ) Mx (moebius-pt M c )
Mx⁄= moebius-pt M a Mx ⁄= moebius-pt M c poincare-on-ray (moebius-pt M p ) ( moebius-pt M b ) Mx
moebius-pt M b ⁄= moebius-pt M a moebius-pt M b ⁄= moebius-pt M c moebius-pt M p ⁄= moebius-pt M b
unfolding poincare-in-angle-def
by auto
obtain x where Mx = moebius-pt M x x ∈ unit-disc
by (metis∗(1 ) assms(1 ) image-iﬀ unit-disc-ﬁx-iﬀ )
thus ?rhs
using∗ assms
unfolding poincare-in-angle-def
by auto
next
assume ?rhs
then obtain x where∗: x∈ unit-disc
poincare-between a x c
x⁄= a x ⁄= c poincare-on-ray p b x
b⁄= a b ⁄= c p ⁄= b
unfolding poincare-in-angle-def
by auto
thus ?lhs
using assms
unfolding poincare-in-angle-def
by auto (rule-tac x =moebius-pt M x in bexI, auto)
qed
lemma unit-disc-ﬁx-preserves-poincare-ray-meets-line [simp]:
assumes unit-disc-ﬁx M a ∈ unit-disc b ∈ unit-disc c ∈ unit-disc d ∈ unit-disc
shows poincare-ray-meets-line(moebius-pt M a ) (moebius-pt M b ) (moebius-pt M c ) (moebius-pt M d )←→poincare-ray-meets-line
a b c d (is ?lhs←→ ?rhs)
proof
assume ?lhs
then obtain Mx where∗: Mx∈ unit-disc poincare-on-ray Mx (moebius-pt M a ) ( moebius-pt M b )
poincare-on-line Mx (moebius-pt M c ) ( moebius-pt M d )
unfolding poincare-ray-meets-line-def
by auto
obtain x where Mx = moebius-pt M x x ∈ unit-disc
by (metis∗(1 ) assms(1 ) image-iﬀ unit-disc-ﬁx-iﬀ )
thus ?rhs
using assms∗
unfolding poincare-ray-meets-line-def poincare-on-line-def
by auto
next
assume ?rhs
then obtain x where∗: x∈ unit-disc poincare-on-ray x a b
poincare-on-line x c d
unfolding poincare-ray-meets-line-def
by auto
thus ?lhs
using assms∗
unfolding poincare-ray-meets-line-def poincare-on-line-def
by auto (rule-tac x =moebius-pt M x in bexI, auto)
158
qed
H-lines that intersect on the absolute do not meet (they do not share a common h-point)
lemma tangent-not-meet:
assumes x1∈ unit-disc and x2∈ unit-disc and x1⁄= x2 and¬ poincare-collinear{0 h, x1, x2}
assumes i∈ ideal-points (poincare-line x1 x2 ) a∈ unit-disc a ⁄= 0 h poincare-collinear{0 h, a, i}
shows¬ poincare-ray-meets-line 0h a x1 x2
proof (rule ccontr )
assume¬ ?thesis
then obtain x where x∈ unit-disc poincare-on-ray x 0 h a poincare-collinear{x, x1, x2}
unfolding poincare-ray-meets-line-def poincare-on-line-def
by auto
have poincare-collinear{0 h, a, x}
using ‹poincare-on-ray x 0 h a› ‹x∈ unit-disc› ‹a∈ unit-disc›
by (meson poincare-between-poincare-collinear poincare-between-rev poincare-on-ray-def poincare-on-ray-poincare-collinear
zero-in-unit-disc)
have x⁄= 0 h
using ‹¬ poincare-collinear{0 h, x1, x2}› ‹poincare-collinear{x, x1, x2}›
unfolding poincare-collinear-def
by (auto simp add : assms(2 ) assms(3 ) poincare-between-rev)
let ?l1 = poincare-line 0 h a
let ?l2 = poincare-line x1 x2
have i∈ circline-set unit-circle
using ‹i∈ ideal-points (poincare-line x1 x2 )›
using assms(3 ) ideal-points-on-unit-circle is-poincare-line-poincare-line by blast
have i∈ circline-set ?l1
using ‹poincare-collinear{0 h, a, i}›
unfolding poincare-collinear-def
using ‹a∈ unit-disc› ‹a⁄= 0 h›
by (metis insert-subset unique-poincare-line zero-in-unit-disc )
moreover
have x∈ circline-set ?l1
using ‹a∈ unit-disc› ‹a⁄= 0 h› ‹poincare-collinear{0 h, a, x}› ‹x∈ unit-disc›
by (metis poincare-collinear3-between poincare-between-poincare-line-uvz poincare-between-poincare-line-uzv poincare-line-sym
zero-in-unit-disc)
moreover
have inversion x ∈ circline-set ?l1
using ‹poincare-collinear{0 h, a, x}›
using poincare-line-inversion-full[of 0 h a x ] ‹a∈ unit-disc› ‹a⁄= 0 h› ‹x∈ unit-disc›
by (metis poincare-collinear3-between is-poincare-line-inverse-point is-poincare-line-poincare-line poincare-between-poincare-line-uvz
poincare-between-poincare-line-uzv poincare-line-sym zero-in-unit-disc)
moreover
have x∈ circline-set ?l2
using ‹poincare-collinear{x, x1, x2}› ‹x1⁄= x2 › ‹x1∈ unit-disc› ‹x2∈ unit-disc› ‹x∈ unit-disc›
by (metis insert-commute inversion-noteq-unit-disc poincare-between-poincare-line-uvz poincare-between-poincare-line-uzv
poincare-collinear3-iﬀ poincare-line-sym-general)
moreover
hence inversion x ∈ circline-set ?l2
using ‹x1⁄= x2 › ‹x1∈ unit-disc› ‹x2∈ unit-disc› ‹x∈ unit-disc›
using poincare-line-inversion-full[of x1 x2 x ]
unfolding circline-set-def
by auto
159
moreover
have i∈ circline-set ?l2
using ‹x1⁄= x2 › ‹x1∈ unit-disc› ‹x2∈ unit-disc›
using ‹i∈ ideal-points ?l2 ›
by (simp add : ideal-points-on-circline)
moreover
have x⁄= inversion x
using ‹x∈ unit-disc›
using inversion-noteq-unit-disc by fastforce
moreover
have x⁄= i
using ‹x∈ unit-disc›
using ‹i∈ circline-set unit-circle › circline-set-def inversion-noteq-unit-disc
by fastforce+
moreover
have inversion x ⁄= i
using ‹i∈ circline-set unit-circle › ‹x⁄= i› circline-set-def inversion-unit-circle
by fastforce
ultimately
have ?l1 = ?l2
using unique-circline-set[of x inversion x i ]
by blast
hence 0 h∈ circline-set ?l2
by (metis ‹a⁄= 0 h› poincare-line-circline-set(1 ))
thus False
using ‹¬ poincare-collinear{0 h, x1, x2}›
unfolding poincare-collinear-def
using ‹poincare-collinear{x, x1, x2}› ‹x1⁄= x2 › ‹x1∈ unit-disc› ‹x2∈ unit-disc› poincare-collinear-def unique-poincare-line
by auto
qed
lemma limiting-parallels:
assumes a∈ unit-disc and x1∈ unit-disc and x2∈ unit-disc and¬ poincare-on-line a x1 x2
shows∃ a1∈unit-disc.∃ a2∈unit-disc.
¬ poincare-on-line a a1 a2 ∧
¬ poincare-ray-meets-line a a1 x1 x2 ∧¬ poincare-ray-meets-line a a2 x1 x2 ∧
(∀ a ′∈unit-disc. poincare-in-angle a ′ a1 a a2 −→ poincare-ray-meets-line a a ′ x1 x2 ) ( is ?P a x1 x2 )
proof−
have¬ poincare-collinear{a, x1, x2}
using ‹¬ poincare-on-line a x1 x2 ›
unfolding poincare-on-line-def
by simp
have∀ x1 x2. x1∈ unit-disc∧ x2∈ unit-disc∧¬ poincare-collinear{a, x1, x2}−→ ?P a x1 x2 (is ?Q a )
proof (rule wlog-zero [OF ‹a∈ unit-disc›])
ﬁx a u
assume∗: u∈ unit-disc cmod a < 1
hence uf : unit-disc-ﬁx (blaschke a )
by simp
assume∗∗: ?Q (moebius-pt (blaschke a ) u)
show ?Q u
proof safe
ﬁx x1 x2
let ?M = moebius-pt (blaschke a )
assume xx: x1∈ unit-disc x2 ∈ unit-disc¬ poincare-collinear{u, x1, x2}
160
hence MM : ?M x1 ∈ unit-disc∧ ?M x2∈ unit-disc∧¬ poincare-collinear{?M u, ?M x1, ?M x2}
using∗
by auto
show ?P u x1 x2 (is∃ a1∈unit-disc.∃ a2∈unit-disc. ?P ′ a1 a2 u x1 x2 )
proof−
obtain Ma1 Ma2 where MM : Ma1∈ unit-disc Ma2 ∈ unit-disc ?P ′ Ma1 Ma2 (?M u ) ( ?M x1 ) ( ?M x2 )
using∗∗[rule-format, OF MM ]
by blast
hence MM ′:∀ a ′∈unit-disc. poincare-in-angle a ′ Ma1 (?M u ) Ma2 −→ poincare-ray-meets-line (?M u ) a ′ (?M
x1 ) ( ?M x2 )
by auto
obtain a1 a2 where a: a1∈ unit-disc a2 ∈ unit-disc ?M a1 = Ma1 ?M a2 = Ma2
using uf
by (metis ‹Ma1∈ unit-disc› ‹Ma2∈ unit-disc› image-iﬀ unit-disc-ﬁx-iﬀ )
have∀ a ′∈unit-disc. poincare-in-angle a ′ a1 u a2 −→ poincare-ray-meets-line u a ′ x1 x2
proof safe
ﬁx a ′
assume a ′∈ unit-disc poincare-in-angle a ′ a1 u a2
thus poincare-ray-meets-line u a ′ x1 x2
using MM (1−2 ) MM ′[rule-format, of ?M a ′]∗ uf a xx
by (meson unit-disc-ﬁx-discI unit-disc-ﬁx-preserves-poincare-in-angle unit-disc-ﬁx-preserves-poincare-ray-meets-line)
qed
hence ?P ′ a1 a2 u x1 x2
using MM∗ uf xx a
by auto
thus ?thesis
using ‹a1∈ unit-disc› ‹a2∈ unit-disc›
by blast
qed
qed
next
show ?Q 0 h
proof safe
ﬁx x1 x2
assume x1∈ unit-disc x2 ∈ unit-disc
assume¬ poincare-collinear{0 h, x1, x2}
show ?P 0 h x1 x2
proof−
let ?lx = poincare-line x1 x2
have x1⁄= x2
using ‹x1∈ unit-disc› ‹x2∈ unit-disc›‹¬ poincare-collinear {0 h, x1, x2}›
using poincare-collinear3-between
by auto
have lx: is-poincare-line ?lx
using is-poincare-line-poincare-line[OF ‹x1⁄= x2 ›]
by simp
obtain i1 i2 where ideal-points ?lx ={i1, i2}
by (meson ‹x1⁄= x2 › is-poincare-line-poincare-line obtain-ideal-points)
let ?li = poincare-line i1 i2
let ?i1 = to-complex i1
let ?i2 = to-complex i2
have i1∈ unit-circle-set i2 ∈ unit-circle-set
using lx ‹ideal-points ?lx ={i1, i2}›
unfolding unit-circle-set-def
by (metis ideal-points-on-unit-circle insertI1, metis ideal-points-on-unit-circle insertI1 insertI2 )
have i1⁄= i2
using ‹ideal-points ?lx ={i1, i2}› ‹x1∈ unit-disc› ‹x1⁄= x2 › ‹x2∈ unit-disc› ideal-points-diﬀerent(1 )
161
by blast
let ?a1 = of-complex (?i1 / 2 )
let ?a2 = of-complex (?i2 / 2 )
let ?la = poincare-line ?a1 ?a2
have ?a1∈ unit-disc ?a2 ∈ unit-disc
using ‹i1∈ unit-circle-set› ‹i2∈ unit-circle-set›
unfolding unit-circle-set-def unit-disc-def disc-def circline-set-def
by auto (transfer, transfer, case-tac i1, case-tac i2, simp add : vec-cnj-def )+
have ?a1⁄= 0 h ?a2⁄= 0 h
using ‹i1∈ unit-circle-set› ‹i2∈ unit-circle-set›
unfolding unit-circle-set-def
by auto
have ?a1⁄= ?a2
using ‹i1⁄= i2 ›
by (metis ‹i1 ∈ unit-circle-set› ‹i2 ∈ unit-circle-set› circline-set-def divide-cancel-right inversion-infty inver-
sion-unit-circle mem-Collect-eq of-complex-to-complex of-complex-zero to-complex-of-complex unit-circle-set-def zero-neq-numeral)
have poincare-collinear{0 h, ?a1, i1}
unfolding poincare-collinear-def
using ‹?a1⁄= 0 h›[symmetric] is-poincare-line-poincare-line[of 0 h ?a1 ]
unfolding circline-set-def
apply (rule-tac x =poincare-line 0 h ?a1 in exI, auto)
apply (transfer, transfer, auto simp add : vec-cnj-def )
done
have poincare-collinear{0 h, ?a2, i2}
unfolding poincare-collinear-def
using ‹?a2⁄= 0 h›[symmetric] is-poincare-line-poincare-line[of 0 h ?a2 ]
unfolding circline-set-def
apply (rule-tac x =poincare-line 0 h ?a2 in exI, auto)
apply (transfer, transfer, auto simp add : vec-cnj-def )
done
have¬ poincare-ray-meets-line 0h ?a1 x1 x2
using tangent-not-meet[of x1 x2 i1 ?a1 ]
using ‹x1∈ unit-disc› ‹x2∈ unit-disc› ‹?a1∈ unit-disc› ‹x1⁄= x2 › ‹¬ poincare-collinear{0 h, x1, x2}›
using ‹ideal-points ?lx ={i1, i2}› ‹?a1⁄= 0 h› ‹poincare-collinear{0 h, ?a1, i1}›
by simp
moreover
have¬ poincare-ray-meets-line 0h ?a2 x1 x2
using tangent-not-meet[of x1 x2 i2 ?a2 ]
using ‹x1∈ unit-disc› ‹x2∈ unit-disc› ‹?a2∈ unit-disc› ‹x1⁄= x2 › ‹¬ poincare-collinear{0 h, x1, x2}›
using ‹ideal-points ?lx ={i1, i2}› ‹?a2⁄= 0 h› ‹poincare-collinear{0 h, ?a2, i2}›
by simp
moreover
have∀ a ′∈ unit-disc. poincare-in-angle a ′ ?a1 0 h ?a2−→ poincare-ray-meets-line 0h a ′ x1 x2
unfolding poincare-in-angle-def
proof safe
ﬁx a ′ a
assume∗: a ′∈ unit-disc a ∈ unit-disc poincare-on-ray a ′ 0 h a a ′⁄= 0 h
poincare-between ?a1 a ?a2 a ⁄= ?a1 a ⁄= ?a2
show poincare-ray-meets-line 0h a ′ x1 x2
proof−
have∀ a ′ a1 a2 x1 x2 i1 i2 .
a ′∈ unit-disc∧ x1∈ unit-disc∧ x2∈ unit-disc∧ x1⁄= x2∧
¬ poincare-collinear{0 h, x1, x2}∧ ideal-points (poincare-line x1 x2 ) = {i1, i2}∧
a1 = of-complex (to-complex i1 / 2 )∧ a2 = of-complex (to-complex i2 / 2 )∧
i1⁄= i2∧ a1⁄= a2∧ poincare-collinear{0 h, a1, i1}∧ poincare-collinear{0 h, a2, i2}∧
162
a1∈ unit-disc∧ a2∈ unit-disc∧ i1∈ unit-circle-set∧ i2∈ unit-circle-set∧
poincare-on-ray a ′ 0 h a∧ a ′⁄= 0 h∧ poincare-between a1 a a2 ∧ a⁄= a1∧ a⁄= a2−→
poincare-ray-meets-line 0h a ′ x1 x2 (is∀ a ′ a1 a2 x1 x2 i1 i2 . ?R 0 h a ′ a1 a2 x1 x2 i1 i2 a )
proof (rule wlog-rotation-to-positive-x-axis [OF ‹a∈ unit-disc›])
let ?R ′ = λ a zero.∀ a ′ a1 a2 x1 x2 i1 i2 . ?R zero a ′ a1 a2 x1 x2 i1 i2 a
ﬁx xa
assume xa: is-real xa 0 < Re xa Re xa < 1
let ?a = of-complex xa
show ?R ′ ?a 0 h
proof safe
ﬁx a ′ a1 a2 x1 x2 i1 i2
let ?i1 = to-complex i1 and ?i2 = to-complex i2
let ?a1 = of-complex (?i1 / 2 ) and ?a2 = of-complex (?i2 / 2 )
let ?la = poincare-line ?a1 ?a2 and ?lx = poincare-line x1 x2 and ?li = poincare-line i1 i2
assume a ′∈ unit-disc x1 ∈ unit-disc x2 ∈ unit-disc x1 ⁄= x2
assume¬ poincare-collinear{0 h, x1, x2} ideal-points ?lx ={i1, i2}
assume poincare-on-ray a ′ 0 h ?a a ′⁄= 0 h
assume poincare-between ?a1 ?a ?a2 ?a ⁄= ?a1 ?a ⁄= ?a2
assume i1⁄= i2 ?a1 ⁄= ?a2 poincare-collinear{0 h, ?a1, i1} poincare-collinear{0 h, ?a2, i2}
assume ?a1∈ unit-disc ?a2 ∈ unit-disc
assume i1∈ unit-circle-set i2 ∈ unit-circle-set
show poincare-ray-meets-line 0h a ′ x1 x2
proof−
have ?lx = ?li
using ‹ideal-points ?lx ={i1, i2}› ‹x1⁄= x2 › ideal-points-line-unique
by auto
have lx: is-poincare-line ?lx
using is-poincare-line-poincare-line[OF ‹x1⁄= x2 ›]
by simp
have x1∈ circline-set ?lx x2 ∈ circline-set ?lx
using lx ‹x1⁄= x2 ›
by auto
have ?lx⁄= x-axis
using ‹¬ poincare-collinear{0 h, x1, x2}› ‹x1∈ circline-set ?lx › ‹x2∈ circline-set ?lx › lx
unfolding poincare-collinear-def
by auto
have 0 h /∈ circline-set ?lx
using ‹¬ poincare-collinear{0 h, x1, x2}› lx ‹x1∈ circline-set ?lx › ‹x2∈ circline-set ?lx ›
unfolding poincare-collinear-def
by auto
have xa⁄= 0 ?a ⁄= 0 h
using xa
by auto
hence 0 h⁄= ?a
by metis
have ?a∈ positive-x-axis
using xa
unfolding positive-x-axis-def
by simp
have ?a∈ unit-disc
using xa
by (auto simp add : cmod-eq-Re)
have ?a∈ circline-set ?la
using ‹poincare-between ?a1 ?a ?a2 ›
using ‹?a1⁄= ?a2 › ‹?a∈ unit-disc› ‹?a1∈ unit-disc› ‹?a2∈ unit-disc› poincare-between-poincare-line-uzv
by blast
163
have ?a1∈ circline-set ?la ?a2 ∈ circline-set ?la
by (auto simp add : ‹?a1⁄= ?a2 ›)
have la: is-poincare-line ?la
using is-poincare-line-poincare-line[OF ‹?a1⁄= ?a2 ›]
by simp
have inv: inversion i1 = i1 inversion i2 = i2
using ‹i1∈ unit-circle-set› ‹i2∈ unit-circle-set›
by (auto simp add : circline-set-def unit-circle-set-def )
have i1⁄=∞h i2⁄=∞h
using inv
by auto
have ?a1 /∈ circline-set x-axis ∧ ?a2 /∈ circline-set x-axis
proof (rule ccontr )
assume¬ ?thesis
hence ?a1∈ circline-set x-axis ∨ ?a2∈ circline-set x-axis
by auto
hence ?la = x-axis
proof
assume ?a1∈ circline-set x-axis
hence{?a, ?a1}⊆ circline-set ?la ∩ circline-set x-axis
using ‹?a∈ circline-set ?la › ‹?a1∈ circline-set ?la ›‹?a∈ positive-x-axis›
using circline-set-x-axis-I xa (1 )
by blast
thus ?la = x-axis
using unique-is-poincare-line[of ?a ?a1 ?la x-axis ]
using ‹?a1∈ unit-disc› ‹?a∈ unit-disc› la ‹?a⁄= ?a1 ›
by auto
next
assume ?a2∈ circline-set x-axis
hence{?a, ?a2}⊆ circline-set ?la ∩ circline-set x-axis
using ‹?a∈ circline-set ?la › ‹?a2∈ circline-set ?la › ‹?a∈ positive-x-axis›
using circline-set-x-axis-I xa (1 )
by blast
thus ?la = x-axis
using unique-is-poincare-line[of ?a ?a2 ?la x-axis ]
using ‹?a2∈ unit-disc› ‹?a∈ unit-disc› la ‹?a⁄= ?a2 ›
by auto
qed
hence i1∈ circline-set x-axis ∧ i2∈ circline-set x-axis
using ‹?a1∈ circline-set ?la › ‹?a2∈ circline-set ?la ›
by (metis ‹i1⁄=∞h› ‹i2⁄=∞h› ‹of-complex (to-complex i1 / 2 )∈ unit-disc› ‹of-complex (to-complex
i2 / 2 )∈ unit-disc› ‹poincare-collinear{0 h, of-complex (to-complex i1 / 2 ), i1}› ‹poincare-collinear{0 h, of-complex
(to-complex i2 / 2 ), i2}› divide-eq-0-iﬀ inf-not-of-complex inv (1 ) inv(2 ) inversion-noteq-unit-disc of-complex-to-complex
of-complex-zero-iﬀ poincare-collinear3-poincare-lines-equal-general poincare-line-0-real-is-x-axis poincare-line-circline-set(2 )
zero-in-unit-disc zero-neq-numeral)
thus False
using ‹?lx⁄= x-axis› unique-is-poincare-line-general[of i1 i2 ?li x-axis ] ‹i1⁄= i2 › inv ‹?lx = ?li›
by auto
qed
hence ?la⁄= x-axis
using ‹?a1⁄= ?a2 › poincare-line-circline-set(1 )
by fastforce
have intersects-x-axis-positive ?la
using intersects-x-axis-positive-iﬀ [of ?la ] ‹?la⁄= x-axis› ‹?a∈ circline-set ?la › la
using ‹?a∈ unit-disc› ‹?a∈ positive-x-axis›
by auto
have intersects-x-axis ?lx
164
proof−
have Arg (to-complex ?a1 )∗ Arg (to-complex ?a2 ) < 0
using ‹poincare-between ?a1 ?a ?a2 › ‹?a1∈ unit-disc› ‹?a2∈ unit-disc›
using poincare-between-x-axis-intersection[of ?a1 ?a2 of-complex xa ]
using ‹?a1 ⁄= ?a2 › ‹?a∈ unit-disc› ‹?a1 /∈ circline-set x-axis ∧ ?a2 /∈ circline-set x-axis › ‹?a∈
positive-x-axis›
using ‹?a∈ circline-set ?la ›
unfolding positive-x-axis-def
by simp
moreover
have ⋀ x y x ′ y ′ :: real. [ [sgn x ′ = sgn x ; sgn y ′ = sgn y ] ] =⇒ x∗y < 0←→ x ′∗y ′< 0
by (metis sgn-less sgn-mult )
ultimately
have Im (to-complex ?a1 )∗ Im (to-complex ?a2 ) < 0
using arg-Im-sgn[of to-complex ?a1 ] arg-Im-sgn[of to-complex ?a2 ]
using ‹?a1∈ unit-disc› ‹?a2∈ unit-disc› ‹?a1 /∈ circline-set x-axis ∧ ?a2 /∈ circline-set x-axis ›
using inf-or-of-complex[of ?a1 ] inf-or-of-complex[of ?a2 ] circline-set-x-axis
by (metis circline-set-x-axis-I to-complex-of-complex )
thus ?thesis
using ideal-points-intersects-x-axis[of ?lx i1 i2 ]
using ‹ideal-points ?lx ={i1, i2}› lx ‹?lx⁄= x-axis›
by simp
qed
have intersects-x-axis-positive ?lx
proof−
have cmod ?i1 = 1 cmod ?i2 = 1
using ‹i1∈ unit-circle-set› ‹i2∈ unit-circle-set›
unfolding unit-circle-set-def
by auto
let ?a1 ′ = ?i1 / 2 and ?a2 ′ = ?i2 / 2
let ?Aa1 = i ∗ (?a1 ′∗ cnj ?a2 ′− ?a2 ′∗ cnj ?a1 ′) and
?Ba1 = i ∗ (?a2 ′∗ cor ((cmod ?a1 ′)2 + 1 )− ?a1 ′∗ cor ((cmod ?a2 ′)2 + 1 ))
have ?Aa1⁄= 0∨ ?Ba1⁄= 0
using ‹cmod (to-complex i1 ) = 1 › ‹ cmod (to-complex i2 ) = 1 › ‹?a1⁄= ?a2 ›
by (auto simp add : power-divide complex-mult-cnj-cmod )
have is-real ?Aa1
by simp
have ?a1⁄= inversion ?a2
using ‹?a1∈ unit-disc› ‹?a2∈ unit-disc› inversion-noteq-unit-disc by fastforce
hence Re ?Ba1 / Re ?Aa1 <−1
using ‹intersects-x-axis-positive ?la › ‹?a1⁄= ?a2 ›
using intersects-x-axis-positive-mk-circline[of ?Aa1 ?Ba1 ] ‹?Aa1⁄= 0∨ ?Ba1⁄= 0 › ‹is-real ?Aa1 ›
using poincare-line-non-homogenous[of ?a1 ?a2 ]
by (simp add : Let-def )
moreover
let ?i1 ′ = to-complex i1 and ?i2 ′ = to-complex i2
let ?Ai1 = i ∗ (?i1 ′∗ cnj ?i2 ′− ?i2 ′∗ cnj ?i1 ′) and
?Bi1 = i ∗ (?i2 ′∗ cor ((cmod ?i1 ′)2 + 1 )− ?i1 ′∗ cor ((cmod ?i2 ′)2 + 1 ))
have ?Ai1⁄= 0∨ ?Bi1⁄= 0
using ‹cmod (to-complex i1 ) = 1 › ‹ cmod (to-complex i2 ) = 1 › ‹?a1⁄= ?a2 ›
by (auto simp add : power-divide complex-mult-cnj-cmod )
165
have is-real ?Ai1
by simp
have sgn (Re ?Bi1 / Re ?Ai1 ) = sgn (Re ?Ba1 / Re ?Aa1 )
proof−
have Re ?Bi1 / Re ?Ai1 = ( Im ?i1 ∗ 2− Im ?i2 ∗ 2 ) /
(Im ?i2 ∗ (Re ?i1 ∗ 2 )− Im ?i1 ∗ (Re ?i2 ∗ 2 ))
using ‹cmod ?i1 = 1 › ‹ cmod ?i2 = 1 ›
by (auto simp add : complex-mult-cnj-cmod ﬁeld-simps )
also have ... = ( Im ?i1 − Im ?i2 ) /
(Im ?i2 ∗ (Re ?i1 )− Im ?i1 ∗ (Re ?i2 )) ( is ... = ?expr)
apply (subst left-diﬀ-distrib [symmetric])
apply (subst semiring-normalization-rules (18 ))+
apply (subst left-diﬀ-distrib [symmetric])
by (metis mult.commute mult-divide-mult-cancel-left-if zero-neq-numeral )
ﬁnally have 1 : Re ?Bi1 / Re ?Ai1 = ( Im ?i1 − Im ?i2 ) / (Im ?i2 ∗ (Re ?i1 )− Im ?i1 ∗ (Re ?i2 ))
.
have Re ?Ba1 / Re ?Aa1 = ( Im ?i1 ∗ 20− Im ?i2 ∗ 20 ) /
(Im ?i2 ∗ (Re ?i1 ∗ 16 )− Im ?i1 ∗ (Re ?i2 ∗ 16 ))
using ‹cmod (to-complex i1 ) = 1 › ‹ cmod (to-complex i2 ) = 1 ›
by (auto simp add : complex-mult-cnj-cmod ﬁeld-simps )
also have ... = ( 20 / 16 )∗ ((Im ?i1 − Im ?i2 ) /
(Im ?i2 ∗ (Re ?i1 )− Im ?i1 ∗ (Re ?i2 )))
apply (subst left-diﬀ-distrib [symmetric])+
apply (subst semiring-normalization-rules (18 ))+
apply (subst left-diﬀ-distrib [symmetric])+
by (metis (no-types, opaque-lifting) ﬁeld-class.ﬁeld-divide-inverse mult.commute times-divide-times-eq)
ﬁnally have 2 : Re ?Ba1 / Re ?Aa1 = ( 5 / 4 )∗ ((Im ?i1 − Im ?i2 ) / (Im ?i2 ∗ (Re ?i1 )− Im ?i1
∗ (Re ?i2 )))
by simp
have ?expr⁄= 0
using ‹Re ?Ba1 / Re ?Aa1 <−1 ›
apply (subst (asm) 2 )
by linarith
thus ?thesis
apply (subst 1, subst 2 )
apply (simp only : sgn-mult)
by simp
qed
moreover
have i1⁄= inversion i2
by (simp add : ‹i1⁄= i2 › inv(2 ))
have (Re ?Bi1 / Re ?Ai1 )2 > 1
proof−
have ?Ai1 = 0∨ (Re ?Bi1 )2 > (Re ?Ai1 )2
using ‹intersects-x-axis ?lx ›
using ‹i1⁄= i2 › ‹i1⁄=∞h› ‹i2⁄=∞h› ‹i1⁄= inversion i2 ›
using intersects-x-axis-mk-circline[of ?Ai1 ?Bi1 ] ‹?Ai1⁄= 0∨ ?Bi1⁄= 0 › ‹is-real ?Ai1 ›
using poincare-line-non-homogenous[of i1 i2 ] ‹?lx = ?li›
by metis
moreover
have ?Ai1⁄= 0
proof (rule ccontr )
assume¬ ?thesis
hence 0 h∈ circline-set ?li
unfolding circline-set-def
apply simp
apply (transfer, transfer, case-tac i1, case-tac i2 )
166
by (auto simp add : vec-cnj-def ﬁeld-simps )
thus False
using ‹0 h /∈ circline-set ?lx › ‹?lx = ?li›
by simp
qed
ultimately
have (Re ?Bi1 )2 > (Re ?Ai1 )2
by auto
moreover
have Re ?Ai1 ⁄= 0
using ‹is-real ?Ai1 › ‹?Ai1⁄= 0 ›
by (simp add : complex-eq-iﬀ )
ultimately
show ?thesis
by (simp add : power-divide)
qed
moreover
{
ﬁx x1 x2 :: real
assume sgn x1 = sgn x2 x1 <−1 x2 2 > 1
hence x2 <−1
by (smt one-power2 real-sqrt-abs real-sqrt-less-iﬀ sgn-neg sgn-pos )
}
ultimately
have Re ?Bi1 / Re ?Ai1 <−1
by metis
thus ?thesis
using ‹i1⁄= i2 › ‹i1⁄=∞h› ‹i2⁄=∞h› ‹i1⁄= inversion i2 ›
using intersects-x-axis-positive-mk-circline[of ?Ai1 ?Bi1 ] ‹?Ai1⁄= 0∨ ?Bi1⁄= 0 › ‹is-real ?Ai1 ›
using poincare-line-non-homogenous[of i1 i2 ] ‹?lx = ?li›
by (simp add : Let-def )
qed
then obtain x where x: x∈ unit-disc x ∈ circline-set ?lx ∩ positive-x-axis
using intersects-x-axis-positive-iﬀ [OF lx ‹?lx⁄= x-axis›]
by auto
have poincare-on-ray x 0 h a ′∧ poincare-collinear{x1, x2, x}
proof
show poincare-collinear{x1, x2, x}
using x lx ‹x1∈ circline-set ?lx › ‹x2∈ circline-set ?lx ›
unfolding poincare-collinear-def
by auto
next
show poincare-on-ray x 0 h a ′
unfolding poincare-on-ray-def
proof−
have a ′∈ circline-set x-axis
using ‹poincare-on-ray a ′ 0 h ?a› xa ‹0 h⁄= ?a› ‹xa⁄= 0 › ‹a ′∈ unit-disc›
unfolding poincare-on-ray-def
using poincare-line-0-real-is-x-axis[of of-complex xa ]
using poincare-between-poincare-line-uvz[of 0 h of-complex xa a ′]
using poincare-between-poincare-line-uzv[of 0 h of-complex xa a ′]
by (auto simp add : cmod-eq-Re)
167
then obtain xa ′ where xa ′: a ′ = of-complex xa ′ is-real xa ′
using ‹a ′∈ unit-disc›
using circline-set-def on-circline-x-axis
by auto
hence−1 < Re xa ′ Re xa ′< 1 xa ′⁄= 0
using ‹a ′∈ unit-disc› ‹a ′⁄= 0 h›
by (auto simp add : cmod-eq-Re)
hence Re xa ′> 0 Re xa ′< 1 is-real xa ′
using ‹poincare-on-ray a ′ 0 h (of-complex xa )›
using poincare-between-x-axis-0uv[of Re xa ′ Re xa ]
using poincare-between-x-axis-0uv[of Re xa Re xa ′]
using circline-set-positive-x-axis-I[of Re xa ′]
using xa xa ′ complex-of-real-Re
unfolding poincare-on-ray-def
by (smt of-real-0, linarith, blast)
moreover
obtain xx where is-real xx Re xx > 0 Re xx < 1 x = of-complex xx
using x
unfolding positive-x-axis-def
using circline-set-def cmod-eq-Re on-circline-x-axis
by auto
ultimately
show poincare-between 0h x a ′∨ poincare-between 0h a ′ x
using ‹a ′ = of-complex xa ′›
by (smt ‹a ′∈ unit-disc› arg-0-iﬀ poincare-between-0uv poincare-between-def to-complex-of-complex
x(1 ))
qed
qed
thus ?thesis
using ‹x∈ unit-disc›
unfolding poincare-ray-meets-line-def poincare-on-line-def
by (metis insert-commute )
qed
qed
next
show a⁄= 0 h
proof (rule ccontr )
assume¬ ?thesis
then obtain k where k<0 to-complex ?a1 = cor k ∗ to-complex ?a2
using poincare-between-u0v[OF ‹?a1∈ unit-disc› ‹?a2∈ unit-disc› ‹?a1⁄= 0 h› ‹?a2⁄= 0 h›]
using ‹poincare-between ?a1 a ?a2 ›
by auto
hence to-complex i1 = cor k ∗ to-complex i2 k < 0
by auto
hence 0 h∈ circline-set (poincare-line x1 x2 )
using ideal-points-proportional[of poincare-line x1 x2 i1 i2 k ] ‹ideal-points (poincare-line x1 x2 ) = {i1,
i2}›
using is-poincare-line-poincare-line[OF ‹x1⁄= x2 ›]
by simp
thus False
using ‹¬ poincare-collinear{0 h, x1, x2}›
using is-poincare-line-poincare-line[OF ‹x1⁄= x2 ›]
unfolding poincare-collinear-def
by (meson ‹x1⁄= x2 › empty-subsetI insert-subset poincare-line-circline-set (1 ) poincare-line-circline-set(2 ))
qed
next
ﬁx ϕ u
let ?R ′ = λ a zero.∀ a ′ a1 a2 x1 x2 i1 i2 . ?R zero a ′ a1 a2 x1 x2 i1 i2 a
168
let ?M = moebius-pt (moebius-rotationϕ)
assume∗: u∈ unit-disc u ⁄= 0 h and∗∗: ?R ′ (?M u ) 0 h
have uf : unit-disc-ﬁx (moebius-rotationϕ)
by simp
have ?M 0 h = 0 h
by auto
hence∗∗: ?R ′ (?M u ) ( ?M 0 h)
using∗∗
by simp
show ?R ′ u 0 h
proof (rule allI )+
ﬁx a ′ a1 a2 x1 x2 i1 i2
have i1 : i1 ∈ unit-circle-set−→ moebius-pt (moebius-rotation ϕ) ( of-complex (to-complex i1 / 2 )) =
of-complex (to-complex (moebius-pt (moebius-rotationϕ) i1 ) / 2 )
using unit-circle-set-def by force
have i2 : i2 ∈ unit-circle-set−→ moebius-pt (moebius-rotation ϕ) ( of-complex (to-complex i2 / 2 )) =
of-complex (to-complex (moebius-pt (moebius-rotationϕ) i2 ) / 2 )
using unit-circle-set-def by force
show ?R 0 h a ′ a1 a2 x1 x2 i1 i2 u
using∗∗[rule-format, of ?M a ′ ?M x1 ?M x2 ?M i1 ?M i2 ?M a1 ?M a2 ] uf ∗
apply (auto simp del : moebius-pt-moebius-rotation-zero moebius-pt-moebius-rotation)
using i1 i2
by simp
qed
qed
thus ?thesis
using ‹a ′∈ unit-disc› ‹x1∈ unit-disc› ‹x2∈ unit-disc› ‹x1⁄= x2 ›
using ‹¬ poincare-collinear{0 h, x1, x2}› ‹ideal-points ?lx ={i1, i2}› ‹i1⁄= i2 ›
using ‹?a1⁄= ?a2 › ‹poincare-collinear{0 h, ?a1, i1}› ‹poincare-collinear{0 h, ?a2, i2}›
using ‹?a1∈ unit-disc› ‹?a2∈ unit-disc› ‹i1∈ unit-circle-set› ‹i2∈ unit-circle-set›
using ‹poincare-on-ray a ′ 0 h a› ‹a ′⁄= 0 h› ‹poincare-between ?a1 a ?a2 › ‹a⁄= ?a1 › ‹a⁄= ?a2 ›
by blast
qed
qed
moreover
have¬ poincare-on-line 0 h ?a1 ?a2
proof
assume∗: poincare-on-line 0 h ?a1 ?a2
hence poincare-collinear{0 h, ?a1, ?a2}
unfolding poincare-on-line-def
by simp
hence poincare-line 0 h ?a1 = poincare-line 0 h ?a2
using poincare-collinear3-poincare-lines-equal-general[of 0 h ?a1 ?a2 ]
using ‹?a1∈ unit-disc› ‹?a1⁄= 0 h› ‹?a2∈ unit-disc› ‹?a2⁄= 0 h›
by (metis inversion-noteq-unit-disc zero-in-unit-disc )
have i1∈ circline-set (poincare-line 0 h ?a1 )
using ‹poincare-collinear{0 h, ?a1, i1}›
using poincare-collinear3-poincare-line-general[of i1 0 h ?a1 ]
using ‹?a1∈ unit-disc› ‹?a1⁄= 0 h›
by (metis insert-commute inversion-noteq-unit-disc zero-in-unit-disc )
moreover
have i2∈ circline-set (poincare-line 0 h ?a1 )
using ‹poincare-collinear{0 h, ?a2, i2}›
using poincare-collinear3-poincare-line-general[of i2 0 h ?a2 ]
using ‹?a2∈ unit-disc› ‹?a2⁄= 0 h› ‹poincare-line 0 h ?a1 = poincare-line 0 h ?a2 ›
by (metis insert-commute inversion-noteq-unit-disc zero-in-unit-disc )
ultimately
have poincare-collinear{0 h, i1, i2}
using ‹?a1∈ unit-disc› ‹?a1⁄= 0 h› ‹poincare-collinear{0 h, ?a1, i1}›
169
by (smt insert-subset poincare-collinear-def unique-poincare-line zero-in-unit-disc )
hence 0 h∈ circline-set (poincare-line i1 i2 )
using poincare-collinear3-poincare-line-general[of 0 h i1 i2 ]
using ‹i1⁄= i2 › ‹i2∈ unit-circle-set› unit-circle-set-def
by force
moreover
have ?lx = ?li
using ‹ideal-points ?lx ={i1, i2}› ‹x1⁄= x2 › ideal-points-line-unique
by auto
ultimately
show False
using ‹¬ poincare-collinear{0 h, x1, x2}›
using ‹x1⁄= x2 › poincare-line-poincare-collinear3-general
by auto
qed
ultimately
show ?thesis
using ‹?a1∈ unit-disc› ‹?a2∈ unit-disc›
by blast
qed
qed
qed
thus ?thesis
using ‹x1∈ unit-disc› ‹x2∈ unit-disc› ‹¬ poincare-collinear{a, x1, x2}›
by blast
qed
