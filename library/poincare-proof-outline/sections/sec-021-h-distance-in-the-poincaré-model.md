---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-021-h-distance-in-the-poincaré-model
section_title: "H-distance in the Poincaré model"
section_number: null
pages: 44-48
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Informally, the h-distance between the two h-points is deﬁned as the absolute value of the logarithm of the cross
ratio between those two points and the two ideal points.
abbreviation Re-cross-ratio where Re-cross-ratio z u v w ≡ Re (to-complex (cross-ratio z u v w ))
deﬁnition calc-poincare-distance :: complex-homo⇒ complex-homo⇒ complex-homo⇒ complex-homo⇒ real where
[simp]: calc-poincare-distance u i1 v i2 = abs (ln (Re-cross-ratio u i1 v i2 ))
deﬁnition poincare-distance-pred :: complex-homo⇒ complex-homo⇒ real⇒ bool where
[simp]: poincare-distance-pred u v d ←→
(u = v∧ d = 0 )∨ (u⁄= v∧ (∀ i1 i2. ideal-points (poincare-line u v ) ={i1, i2}−→ d = calc-poincare-distance
u i1 v i2 ))
deﬁnition poincare-distance :: complex-homo⇒ complex-homo⇒ real where
poincare-distance u v = ( THE d. poincare-distance-pred u v d )
We shown that the described cross-ratio is always ﬁnite, positive real number.
lemma distance-cross-ratio-real-positive:
assumes u∈ unit-disc and v∈ unit-disc and u⁄= v
shows∀ i1 i2. ideal-points (poincare-line u v ) = {i1, i2}−→
cross-ratio u i1 v i2 ⁄=∞h∧ is-real (to-complex (cross-ratio u i1 v i2 ))∧ Re-cross-ratio u i1 v i2 > 0
(is ?P u v )
proof (rule wlog-positive-x-axis [OF assms ])
ﬁx x
assume∗: is-real x 0 < Re x Re x < 1
hence x⁄=−1 x ⁄= 1
by auto
hence∗∗: of-complex x ⁄=∞h of-complex x ⁄= 0 h of-complex x ⁄= of-complex (−1 ) of-complex 1 ⁄= of-complex x
of-complex x ∈ circline-set x-axis
using∗
unfolding circline-set-x-axis
by (auto simp add : of-complex-inj)
have∗∗∗: 0 h⁄= of-complex (−1 ) 0 h⁄= of-complex 1
by (metis of-complex-zero-iﬀ zero-neq-neg-one, simp)
have∗∗∗∗:− x− 1⁄= 0 x − 1⁄= 0
using ‹x⁄=−1 › ‹x⁄= 1 ›
by (metis add.inverse-inverse eq-iﬀ-diﬀ-eq-0, simp)
have poincare-line 0 h (of-complex x ) = x-axis
using∗∗
by (simp add : poincare-line-0-real-is-x-axis)
thus ?P 0 h (of-complex x )
using∗∗∗∗∗∗∗∗∗∗
using cross-ratio-not-inf[of 0 h of-complex 1 of-complex (−1 ) of-complex x ]
using cross-ratio-not-inf[of 0 h of-complex (−1 ) of-complex 1 of-complex x ]
using cross-ratio-real[of 0 −1 x 1 ] cross-ratio-real[of 0 1 x −1 ]
44
apply (auto simp add : poincare-line-0-real-is-x-axis doubleton-eq-iﬀ circline-set-x-axis)
apply (subst cross-ratio, simp-all, subst Re-complex-div-gt-0, simp, subst mult-neg-neg, simp-all )+
done
next
ﬁx M u v
let ?Mu = moebius-pt M u and ?Mv = moebius-pt M v
assume∗: unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc u ⁄= v
?P ?Mu ?Mv
show ?P u v
proof safe
ﬁx i1 i2
let ?cr = cross-ratio u i1 v i2
assume∗∗: ideal-points (poincare-line u v ) = {i1, i2}
have i1⁄= u i1 ⁄= v i2 ⁄= u i2 ⁄= v i1 ⁄= i2
using ideal-points-diﬀerent[OF∗(2−3 ), of i1 i2 ]∗∗ ‹u⁄= v›
by auto
hence 0 < Re (to-complex ?cr )∧ is-real (to-complex ?cr )∧ ?cr⁄=∞h
using∗∗∗
apply (erule-tac x =moebius-pt M i1 in allE )
apply (erule-tac x =moebius-pt M i2 in allE )
apply (subst (asm) ideal-points-poincare-line-moebius[of M u v i1 i2 ], simp-all )
done
thus 0 < Re (to-complex ?cr ) is-real (to-complex ?cr ) ?cr =∞h =⇒ False
by simp-all
qed
qed
Next we can show that for every diﬀerent points from the unit disc there is exactly one number that satisﬁes
the h-distance predicate.
lemma distance-unique:
assumes u∈ unit-disc and v∈ unit-disc
shows∃ ! d. poincare-distance-pred u v d
proof (cases u = v)
case True
thus ?thesis
by auto
next
case False
obtain i1 i2 where∗: i1⁄= i2 ideal-points (poincare-line u v ) = {i1, i2}
using obtain-ideal-points[OF is-poincare-line-poincare-line] ‹u⁄= v›
by blast
let ?d = calc-poincare-distance u i1 v i2
show ?thesis
proof (rule ex1I )
show poincare-distance-pred u v ?d
using∗ ‹u⁄= v›
proof (simp del : calc-poincare-distance-def, safe)
ﬁx i1 ′ i2 ′
assume{i1, i2} ={i1 ′, i2 ′}
hence∗∗: ( i1 ′ = i1∧ i2 ′ = i2 )∨ (i1 ′ = i2∧ i2 ′ = i1 )
using doubleton-eq-iﬀ [of i1 i2 i1 ′ i2 ′]
by blast
have all-diﬀerent : u⁄= i1 u ⁄= i2 v ⁄= i1 v ⁄= i2 u ⁄= i1 ′ u⁄= i2 ′ v⁄= i1 ′ v⁄= i2 ′ i1⁄= i2
using ideal-points-diﬀerent[OF assms, of i1 i2 ]∗∗∗ ‹u⁄= v›
by auto
show calc-poincare-distance u i1 v i2 = calc-poincare-distance u i1 ′ v i2 ′
proof−
let ?cr = cross-ratio u i1 v i2
let ?cr ′ = cross-ratio u i1 ′ v i2 ′
have Re (to-complex ?cr ) > 0 is-real (to-complex ?cr )
Re (to-complex ?cr ′) > 0 is-real (to-complex ?cr ′)
using False distance-cross-ratio-real-positive[OF assms (1−2 )]∗∗∗
by auto
45
thus ?thesis
using∗∗
using cross-ratio-not-zero cross-ratio-not-inf all-diﬀerent
by auto (subst cross-ratio-commute-24, subst reciprocal-real, simp-all add : ln-div)
qed
qed
next
ﬁx d
assume poincare-distance-pred u v d
thus d = ?d
using∗ ‹u⁄= v›
by auto
qed
qed
lemma poincare-distance-satisﬁes-pred [simp]:
assumes u∈ unit-disc and v∈ unit-disc
shows poincare-distance-pred u v (poincare-distance u v )
using distance-unique[OF assms ] theI ′[of poincare-distance-pred u v ]
unfolding poincare-distance-def
by blast
lemma poincare-distance-I:
assumes u∈ unit-disc and v∈ unit-disc and u⁄= v and ideal-points (poincare-line u v ) = {i1, i2}
shows poincare-distance u v = calc-poincare-distance u i1 v i2
using assms
using poincare-distance-satisﬁes-pred[OF assms (1−2 )]
by simp
lemma poincare-distance-reﬂ [simp]:
assumes u∈ unit-disc
shows poincare-distance u u = 0
using assms
using poincare-distance-satisﬁes-pred[OF assms assms ]
by simp
Unit disc preserving Möbius transformations preserve h-distance.
lemma unit-disc-ﬁx-preserve-poincare-distance [simp]:
assumes unit-disc-ﬁx M and u∈ unit-disc and v∈ unit-disc
shows poincare-distance (moebius-pt M u ) ( moebius-pt M v ) = poincare-distance u v
proof (cases u = v)
case True
have moebius-pt M u ∈ unit-disc moebius-pt M v ∈ unit-disc
using unit-disc-ﬁx-iﬀ [OF assms (1 ), symmetric] assms
by blast+
thus ?thesis
using assms ‹u = v›
by simp
next
case False
obtain i1 i2 where∗: ideal-points (poincare-line u v ) = {i1, i2}
using ‹u⁄= v›
by (rule obtain-ideal-points [OF is-poincare-line-poincare-line[of u v ]])
let ?Mu = moebius-pt M u and ?Mv = moebius-pt M v and ?Mi1 = moebius-pt M i1 and ?Mi2 = moebius-pt M i2
have∗∗: ?Mu∈ unit-disc ?Mv ∈ unit-disc
using assms
using unit-disc-ﬁx-iﬀ
by blast+
have∗∗∗: ?Mu⁄= ?Mv
using ‹u⁄= v›
by simp
have poincare-distance u v = calc-poincare-distance u i1 v i2
using poincare-distance-I[OF assms (2−3 ) ‹u⁄= v›∗]
46
by auto
moreover
have unit-circle-ﬁx M
using assms
by simp
hence ++: ideal-points (poincare-line ?Mu ?Mv ) = {?Mi1, ?Mi2}
using ‹u⁄= v› assms∗
by simp
have poincare-distance ?Mu ?Mv = calc-poincare-distance ?Mu ?Mi1 ?Mv ?Mi2
by (rule poincare-distance-I [OF∗∗∗∗∗ ++])
moreover
have calc-poincare-distance ?Mu ?Mi1 ?Mv ?Mi2 = calc-poincare-distance u i1 v i2
using ideal-points-diﬀerent[OF assms (2−3 ) ‹u⁄= v›∗]
unfolding calc-poincare-distance-def
by (subst moebius-preserve-cross-ratio[symmetric], simp-all )
ultimately
show ?thesis
by simp
qed
Knowing ideal points for x-axis, we can easily explicitly calculate distances.
lemma poincare-distance-x-axis-x-axis:
assumes x∈ unit-disc and y∈ unit-disc and x∈ circline-set x-axis and y∈ circline-set x-axis
shows poincare-distance x y =
(let x ′ = to-complex x ; y ′ = to-complex y
in abs (ln (Re (((1 + x ′)∗ (1− y ′)) / ((1− x ′)∗ (1 + y ′))))))
proof−
obtain x ′ y ′ where∗: x = of-complex x ′ y = of-complex y ′
using inf-or-of-complex[of x ] inf-or-of-complex[of y ] ‹x∈ unit-disc› ‹y∈ unit-disc›
by auto
have cmod x ′< 1 cmod y ′< 1
using ‹x∈ unit-disc› ‹y∈ unit-disc›∗
by (metis unit-disc-iﬀ-cmod-lt-1 )+
hence∗∗: x ′⁄= 1 x ′⁄= 1 y ′⁄=−1 y ′⁄= 1
by auto
have 1 + y ′⁄= 0
using∗∗
by (metis add.left-cancel add-neg-numeral-special(7 ))
show ?thesis
proof (cases x = y)
case True
thus ?thesis
using assms(1−2 )
using unit-disc-iﬀ-cmod-lt-1 [of to-complex x ]∗∗∗ ‹1 + y ′⁄= 0 ›
by auto
next
case False
hence poincare-line x y = x-axis
using poincare-line-x-axis[OF assms ]
by simp
hence ideal-points (poincare-line x y ) = {of-complex (−1 ), of-complex 1}
by simp
hence poincare-distance x y = calc-poincare-distance x (of-complex (−1 )) y (of-complex 1 )
using poincare-distance-I assms ‹x⁄= y›
by auto
also have ... = abs (ln (Re (((x ′ + 1 )∗ (y ′− 1 )) / ((x ′− 1 )∗ (y ′ + 1 )))))
using∗ ‹cmod x ′< 1 › ‹cmod y ′< 1 ›
by (simp, transfer, transfer, auto)
ﬁnally
show ?thesis
using∗
by (metis (no-types, lifting) add.commute minus-diﬀ-eq minus-divide-divide mult-minus-left mult-minus-right
47
to-complex-of-complex)
qed
qed
lemma poincare-distance-zero-x-axis:
assumes x∈ unit-disc and x∈ circline-set x-axis
shows poincare-distance 0 h x = ( let x ′ = to-complex x in abs (ln (Re ((1− x ′) / (1 + x ′)))))
using assms
using poincare-distance-x-axis-x-axis[of 0 h x]
by (simp add : Let-def )
lemma poincare-distance-zero:
assumes x∈ unit-disc
shows poincare-distance 0 h x = ( let x ′ = to-complex x in abs (ln (Re ((1− cmod x ′) / (1 + cmod x ′))))) ( is ?P x )
proof (cases x = 0 h)
case True
thus ?thesis
by auto
next
case False
show ?thesis
proof (rule wlog-rotation-to-positive-x-axis )
show x∈ unit-disc x ⁄= 0 h by fact+
next
ﬁx ϕ u
assume u∈ unit-disc u ⁄= 0 h ?P (moebius-pt (moebius-rotationϕ) u)
thus ?P u
using unit-disc-ﬁx-preserve-poincare-distance[of moebius-rotation ϕ 0 h u]
by (cases u =∞h) ( simp-all add : Let-def )
next
ﬁx x
assume is-real x 0 < Re x Re x < 1
thus ?P (of-complex x )
using poincare-distance-zero-x-axis[of of-complex x ]
by simp (auto simp add : circline-set-x-axis cmod-eq-Re complex-is-Real-iﬀ )
qed
qed
lemma poincare-distance-zero-opposite [simp]:
assumes of-complex z ∈ unit-disc
shows poincare-distance 0 h (of-complex (− z)) = poincare-distance 0 h (of-complex z )
proof−
have∗: of-complex (−z)∈ unit-disc
using assms
by auto
show ?thesis
using poincare-distance-zero[OF assms ]
using poincare-distance-zero[OF∗]
by simp
qed
