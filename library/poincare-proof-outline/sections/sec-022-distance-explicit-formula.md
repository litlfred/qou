---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-022-distance-explicit-formula
section_title: "Distance explicit formula"
section_number: null
pages: 48-54
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Instead of the h-distance itself, very frequently its hyperbolic cosine is analyzed.
abbreviation cosh-dist u v ≡ cosh (poincare-distance u v )
lemma cosh-poincare-distance-cross-ratio-average:
assumes u∈ unit-disc v ∈ unit-disc u ⁄= v ideal-points (poincare-line u v ) = {i1, i2}
shows cosh-dist u v =
((Re-cross-ratio u i1 v i2 ) + ( Re-cross-ratio v i1 u i2 )) / 2
proof−
let ?cr = cross-ratio u i1 v i2
let ?crRe = Re (to-complex ?cr )
have ?cr⁄=∞h is-real (to-complex ?cr ) ?crRe > 0
using distance-cross-ratio-real-positive[OF assms (1−3 )] assms(4 )
by simp-all
48
then obtain cr where∗: cross-ratio u i1 v i2 = of-complex cr cr ⁄= 0 is-real cr Re cr > 0
using inf-or-of-complex[of cross-ratio u i1 v i2 ]
by (smt to-complex-of-complex zero-complex.simps(1 ))
thus ?thesis
using∗
using assms cross-ratio-commute-13 [of v i1 u i2 ]
unfolding poincare-distance-I[OF assms ] calc-poincare-distance-def cosh-def
by (cases Re cr ≥ 1 )
(auto simp add : ln-div[of 0 ] exp-minus ﬁeld-simps Re-divide power2-eq-square complex .expand)
qed
deﬁnition poincare-distance-formula′ :: complex⇒ complex⇒ real where
[simp]: poincare-distance-formula′ u v = 1 + 2∗ ((cmod (u− v))2 / ((1− (cmod u )2)∗ (1− (cmod v )2)))
Next we show that the following formula expresses h-distance between any two h-points (note that the ideal
points do not ﬁgure anymore).
deﬁnition poincare-distance-formula :: complex⇒ complex⇒ real where
[simp]: poincare-distance-formula u v = arcosh (poincare-distance-formula′ u v )
lemma blaschke-preserve-distance-formula [simp]:
assumes of-complex k ∈ unit-disc u ∈ unit-disc v ∈ unit-disc
shows poincare-distance-formula (to-complex (moebius-pt (blaschke k ) u)) ( to-complex (moebius-pt (blaschke k ) v)) =
poincare-distance-formula (to-complex u ) ( to-complex v )
proof (cases k = 0 )
case True
thus ?thesis
by simp
next
case False
obtain u ′ v ′ where∗: u ′ = to-complex u v ′ = to-complex v
by auto
have cmod u ′< 1 cmod v ′< 1 cmod k < 1
using assms∗
using inf-or-of-complex[of u ] inf-or-of-complex[of v ]
by auto
obtain nu du nv dv d kk ddu ddv where
∗∗: nu = u ′− k du = 1− cnj k ∗u ′ nv = v ′− k dv = 1− cnj k ∗ v ′
d = u ′− v ′ ddu = 1− u ′∗cnj u ′ ddv = 1− v ′∗cnj v ′ kk = 1− k∗cnj k
by auto
have d: nu∗dv− nv∗du = d∗kk
by (subst∗∗)+ ( simp add : ﬁeld-simps)
have ddu: du∗cnj du − nu∗cnj nu = ddu∗kk
by (subst∗∗)+ ( simp add : ﬁeld-simps)
have ddv: dv∗cnj dv − nv∗cnj nv = ddv∗kk
by (subst∗∗)+ ( simp add : ﬁeld-simps)
have du⁄= 0
proof (rule ccontr )
assume¬ ?thesis
hence cmod (1− cnj k ∗ u ′) = 0
using ‹du = 1− cnj k ∗ u ′›
by auto
hence cmod (cnj k ∗ u ′) = 1
by auto
thus False
using ‹cmod k < 1 › ‹cmod u ′< 1 ›
using mult-strict-mono[of cmod k 1 cmod u ′ 1 ]
by (simp add : norm-mult)
qed
have dv⁄= 0
proof (rule ccontr )
assume¬ ?thesis
49
hence cmod (1− cnj k ∗ v ′) = 0
using ‹dv = 1− cnj k ∗ v ′›
by auto
hence cmod (cnj k ∗ v ′) = 1
by auto
thus False
using ‹cmod k < 1 › ‹cmod v ′< 1 ›
using mult-strict-mono[of cmod k 1 cmod v ′ 1 ]
by (simp add : norm-mult)
qed
have kk⁄= 0
proof (rule ccontr )
assume¬ ?thesis
hence cmod (1− k∗ cnj k ) = 0
using ‹kk = 1− k∗ cnj k ›
by auto
hence cmod (k∗ cnj k ) = 1
by auto
thus False
using ‹cmod k < 1 ›
using mult-strict-mono[of cmod k 1 cmod k 1 ]
using complex-mod-sqrt-Re-mult-cnj by auto
qed
note nz = ‹du⁄= 0 › ‹dv⁄= 0 › ‹kk⁄= 0 ›
have nu / du− nv / dv = ( nu∗dv− nv∗du) / (du∗ dv)
using nz
by (simp add : ﬁeld-simps)
hence (cmod (nu/du− nv/dv))2 = cmod ((d∗kk) / (du∗dv)∗ (cnj ((d∗kk) / (du∗dv)))) ( is ?lhs = -)
unfolding complex-mod-mult-cnj[symmetric]
by (subst (asm) d) simp
also have ... = cmod ((d∗cnj d∗kk∗kk) / (du∗cnj du∗dv∗cnj dv ))
by (simp add : ﬁeld-simps norm-mult norm-divide )
ﬁnally have 1 : ?lhs = cmod ((d∗cnj d∗kk∗kk)/ (du∗cnj du∗dv∗cnj dv )) .
have (1− ((cmod nu ) / (cmod du ))2)∗(1− ((cmod nv ) / (cmod dv ))2) =
(1− cmod((nu∗ cnj nu ) / (du∗ cnj du )))∗(1− cmod((nv∗ cnj nv ) / (dv∗ cnj dv ))) ( is ?rhs = -)
by (metis norm-divide complex-mod-mult-cnj power-divide )
also have ... = cmod(((du∗cnj du − nu∗cnj nu ) / (du∗ cnj du ))∗ ((dv∗cnj dv − nv∗cnj nv ) / (dv∗ cnj dv )))
proof−
have u ′⁄= 1 / cnj k v ′⁄= 1 / cnj k
using ‹cmod u ′< 1 › ‹cmod v ′< 1 › ‹cmod k < 1 ›
by (auto simp add : False norm-divide )
moreover
have cmod k ⁄= 1
using ‹cmod k < 1 ›
by linarith
ultimately
have cmod (nu/du) < 1 cmod (nv/dv) < 1
using∗∗(1−4 )
using unit-disc-ﬁx-discI [OF blaschke-unit-disc-ﬁx [OF ‹cmod k < 1 ›] ‹u∈ unit-disc›] ‹u ′ = to-complex u ›
using unit-disc-ﬁx-discI [OF blaschke-unit-disc-ﬁx [OF ‹cmod k < 1 ›] ‹v∈ unit-disc›] ‹v ′ = to-complex v ›
using inf-or-of-complex[of u ] ‹u∈ unit-disc› inf-or-of-complex[of v ] ‹v∈ unit-disc›
using moebius-pt-blaschke[of k u ′] using moebius-pt-blaschke[of k v ′]
by auto
hence (cmod (nu/du))2 < 1 (cmod (nv/dv))2 < 1
by (simp-all add : cmod-def )
hence cmod (nu∗ cnj nu / (du∗ cnj du )) < 1 cmod (nv∗ cnj nv / (dv∗ cnj dv )) < 1
by (metis complex-mod-mult-cnj norm-divide power-divide )+
moreover
have is-real (nu∗ cnj nu / (du∗ cnj du )) is-real (nv∗ cnj nv / (dv∗ cnj dv ))
using eq-cnj-iﬀ-real[of nu ∗ cnj nu / (du∗ cnj du )]
using eq-cnj-iﬀ-real[of nv ∗ cnj nv / (dv∗ cnj dv )]
50
by (auto simp add : mult.commute)
moreover
have Re (nu∗ cnj nu / (du∗ cnj du ))≥ 0 Re (nv∗ cnj nv / (dv∗ cnj dv ))≥ 0
using ‹du⁄= 0 › ‹dv⁄= 0 ›
unfolding complex-mult-cnj-cmod
by simp-all
ultimately
have 1− cmod (nu∗ cnj nu / (du∗ cnj du )) = cmod (1− nu∗ cnj nu / (du∗ cnj du ))
1− cmod (nv∗ cnj nv / (dv∗ cnj dv )) = cmod (1− nv∗ cnj nv / (dv∗ cnj dv ))
by (simp-all add : cmod-def )
thus ?thesis
using nz
by (simp add : diﬀ-divide-distrib norm-mult )
qed
also have ... = cmod(((ddu∗ kk) / (du∗ cnj du ))∗ ((ddv∗ kk) / (dv∗ cnj dv )))
by (subst ddu, subst ddv, simp)
also have ... = cmod((ddu∗ddv∗kk∗kk) / (du∗cnj du∗dv∗cnj dv ))
by (simp add : ﬁeld-simps)
ﬁnally have 2 : ?rhs = cmod((ddu∗ddv∗kk∗kk) / (du∗cnj du∗dv∗cnj dv ))
.
have ?lhs / ?rhs =
cmod ((d∗cnj d∗kk∗kk) / (du∗cnj du∗dv∗cnj dv )) / cmod((ddu∗ddv∗kk∗kk) / (du∗cnj du∗dv∗cnj dv ))
by (subst 1, subst 2, simp)
also have ... = cmod ((d∗cnj d )/(ddu∗ddv))
using nz by (simp add : norm-mult norm-divide )
also have ... = ( cmod d )2 / ((1− (cmod u ′)2)∗(1− (cmod v ′)2))
proof−
have (cmod u ′)2 < 1 (cmod v ′)2 < 1
using ‹cmod u ′< 1 › ‹cmod v ′< 1 ›
by (simp-all add : cmod-def )
hence cmod (1− u ′∗ cnj u ′) = 1− (cmod u ′)2 cmod (1− v ′∗ cnj v ′) = 1− (cmod v ′)2
by (auto simp add : cmod-eq-Re cmod-power2 power2-eq-square[symmetric])
thus ?thesis
using nz
by (simp add :∗∗(6 )∗∗(7 ) norm-divide norm-mult power2-eq-square )
qed
ﬁnally
have 3 : ?lhs / ?rhs = ( cmod d )2 / ((1− (cmod u ′)2)∗(1− (cmod v ′)2)) .
have cmod k ⁄= 1 u ′⁄= 1 / cnj k v ′⁄= 1 / cnj k u ⁄=∞h v⁄=∞h
using ‹cmod k < 1 › ‹u∈ unit-disc› ‹v∈ unit-disc›∗ ‹k⁄= 0 ›∗∗ ‹kk⁄= 0 › nz
by auto
thus ?thesis using assms
using∗∗∗ 3
using moebius-pt-blaschke[of k u ′]
using moebius-pt-blaschke[of k v ′]
by (simp add : norm-divide)
qed
To prove the equivalence between the h-distance deﬁnition and the distance formula, we shall employ the without
loss of generality principle. Therefore, we must show that the distance formula is preserved by h-isometries.
Rotation preserve poincare-distance-formula.
lemma rotation-preserve-distance-formula [simp]:
assumes u∈ unit-disc v ∈ unit-disc
shows poincare-distance-formula (to-complex (moebius-pt (moebius-rotationϕ) u)) (to-complex (moebius-pt (moebius-rotation
ϕ) v)) =
poincare-distance-formula (to-complex u ) ( to-complex v )
using assms
using inf-or-of-complex[of u ] inf-or-of-complex[of v ]
by (auto simp : norm-mult)
Unit disc ﬁxing Möbius preserve poincare-distance-formula.
lemma unit-disc-ﬁx-preserve-distance-formula [simp]:
assumes unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc
51
shows poincare-distance-formula (to-complex (moebius-pt M u )) ( to-complex (moebius-pt M v )) =
poincare-distance-formula (to-complex u ) ( to-complex v ) ( is ?P ′ u v M )
proof−
have∀ u∈ unit-disc.∀ v∈ unit-disc. ?P ′ u v M (is ?P M )
proof (rule wlog-unit-disc-ﬁx [OF assms (1 )])
ﬁx k
assume cmod k < 1
hence of-complex k ∈ unit-disc
by simp
thus ?P (blaschke k )
using blaschke-preserve-distance-formula
by simp
next
ﬁx ϕ
show ?P (moebius-rotationϕ)
using rotation-preserve-distance-formula
by simp
next
ﬁx M1 M2
assume∗: ?P M1 and∗∗: ?P M2 and u11 : unit-disc-ﬁx M1 unit-disc-ﬁx M2
thus ?P (M1 + M2 )
by (auto simp del : poincare-distance-formula-def)
qed
thus ?thesis
using assms
by simp
qed
The equivalence between the two h-distance representations.
lemma poincare-distance-formula:
assumes u∈ unit-disc and v∈ unit-disc
shows poincare-distance u v = poincare-distance-formula (to-complex u ) ( to-complex v ) ( is ?P u v )
proof (rule wlog-x-axis )
ﬁx x
assume∗: is-real x 0 ≤ Re x Re x < 1
show ?P 0 h (of-complex x ) ( is ?lhs = ?rhs)
proof−
have of-complex x ∈ unit-disc of-complex x ∈ circline-set x-axis cmod x < 1
using∗ cmod-eq-Re
by (auto simp add : circline-set-x-axis)
hence ?lhs =|ln (Re ((1− x) / (1 + x)))|
using poincare-distance-zero-x-axis[of of-complex x ]
by simp
moreover
have ?rhs =|ln (Re ((1− x) / (1 + x)))|
proof−
let ?x = 1 + 2∗ (cmod x )2 / (1− (cmod x )2)
have 0≤ 2∗ (cmod x )2 / (1− (cmod x )2)
by (smt ‹cmod x < 1 › divide-nonneg-nonneg norm-ge-zero power-le-one zero-le-power2 )
hence arcosh-real-gt: 1≤ ?x
by auto
have ?rhs = arcosh ?x
by simp
also have ... = ln ((1 + ( cmod x )2) / (1− (cmod x )2) + 2∗ (cmod x ) / (1− (cmod x )2))
proof−
have 1− (cmod x )2 > 0
using ‹cmod x < 1 ›
by (smt norm-not-less-zero one-power2 power2-eq-imp-eq power-mono )
hence 1 : ?x = ( 1 + ( cmod x )2) / (1− (cmod x )2)
by (simp add : ﬁeld-simps)
have 2 : ?x 2− 1 = ( 4∗ (cmod x )2) / (1− (cmod x )2)2
using ‹1− (cmod x )2 > 0 ›
apply (subst 1 )
unfolding power-divide
by (subst divide-diﬀ-eq-iﬀ , simp, simp add : power2-eq-square ﬁeld-simps)
show ?thesis
52
using ‹1− (cmod x )2 > 0 ›
apply (subst arcosh-real-def [OF arcosh-real-gt])
apply (subst 2 )
apply (subst 1 )
apply (subst real-sqrt-divide )
apply (subst real-sqrt-mult )
apply simp
done
qed
also have ... = ln (((1 + ( cmod x ))2) / (1− (cmod x )2))
apply (subst add-divide-distrib [symmetric])
apply (simp add : ﬁeld-simps power2-eq-square)
done
also have ... = ln ((1 + cmod x ) / (1− (cmod x )))
using ‹cmod x < 1 ›
using square-diﬀ-square-factored[of 1 cmod x ]
by (simp add : power2-eq-square)
also have ... =|ln (Re ((1− x) / (1 + x)))|
proof−
have∗: Re ((1− x) / (1 + x))≤ 1 Re ((1− x) / (1 + x)) > 0
using ‹is-real x › ‹Re x ≥ 0 › ‹Re x < 1 ›
using complex-is-Real-iﬀ
by auto
hence|ln (Re ((1− x) / (1 + x)))| =− ln (Re ((1− x) / (1 + x)))
by auto
hence|ln (Re ((1− x) / (1 + x)))| = ln (Re ((1 + x) / (1− x)))
using ln-div[of 1 Re ((1− x)/(1 + x))]∗ ‹is-real x ›
by (fastforce simp: complex-is-Real-iﬀ)
moreover
have ln ((1 + cmod x ) / (1− cmod x )) = ln ((1 + Re x ) / (1− Re x ))
using ‹Re x ≥ 0 › ‹is-real x ›
using cmod-eq-Re by auto
moreover
have (1 + Re x ) / (1− Re x ) = Re ((1 + x) / (1− x))
using ‹is-real x › ‹Re x < 1 ›
by (smt Re-divide-real eq-iﬀ-diﬀ-eq-0 minus-complex .simps one-complex.simps plus-complex.simps)
ultimately
show ?thesis
by simp
qed
ﬁnally
show ?thesis
.
qed
ultimately
show ?thesis
by simp
qed
next
ﬁx M u v
assume∗: unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc
assume ?P (moebius-pt M u ) ( moebius-pt M v )
thus ?P u v
using∗(1−3 )
by (simp del : poincare-distance-formula-def)
next
show u∈ unit-disc v ∈ unit-disc
by fact+
qed
Some additional properties proved easily using the distance formula.
poincare-distance is symmetric.
lemma poincare-distance-sym:
assumes u∈ unit-disc and v∈ unit-disc
shows poincare-distance u v = poincare-distance v u
53
using assms
using poincare-distance-formula[OF assms (1 ) assms(2 )]
using poincare-distance-formula[OF assms (2 ) assms(1 )]
by (simp add : mult.commute norm-minus-commute )
lemma poincare-distance-formula′-ge-1 :
assumes u∈ unit-disc and v∈ unit-disc
shows 1≤ poincare-distance-formula′ (to-complex u ) ( to-complex v )
using unit-disc-cmod-square-lt-1[OF assms (1 )] unit-disc-cmod-square-lt-1[OF assms (2 )]
by auto
poincare-distance is non-negative.
lemma poincare-distance-ge0:
assumes u∈ unit-disc and v∈ unit-disc
shows poincare-distance u v ≥ 0
using poincare-distance-formula′-ge-1 assms by (simp add : poincare-distance-formula)
lemma cosh-dist:
assumes u∈ unit-disc and v∈ unit-disc
shows cosh-dist u v = poincare-distance-formula′ (to-complex u ) ( to-complex v )
using poincare-distance-formula[OF assms ] poincare-distance-formula′-ge-1 [OF assms ]
by simp
poincare-distance is zero only if the two points are equal.
lemma poincare-distance-eq-0-iﬀ:
assumes u∈ unit-disc and v∈ unit-disc
shows poincare-distance u v = 0←→ u = v
using assms
apply auto
using poincare-distance-formula′-ge-1 [OF assms ]
using unit-disc-cmod-square-lt-1[OF assms (1 )] unit-disc-cmod-square-lt-1[OF assms (2 )]
apply (simp add : poincare-distance-formula)
by (simp add : unit-disc-to-complex-inj)
Conjugate preserve poincare-distance-formula.
lemma conjugate-preserve-poincare-distance [simp]:
assumes u∈ unit-disc and v∈ unit-disc
shows poincare-distance (conjugate u ) ( conjugate v ) = poincare-distance u v
proof−
obtain u ′ v ′ where∗: u = of-complex u ′ v = of-complex v ′
using assms inf-or-of-complex [of u ] inf-or-of-complex[of v ]
by auto
have∗∗: conjugate u ∈ unit-disc conjugate v ∈ unit-disc
using∗ assms
by auto
show ?thesis
using∗
using poincare-distance-formula[OF assms ]
using poincare-distance-formula[OF∗∗]
by (metis complex-cnj-diﬀ complex-mod-cnj conjugate-of-complex poincare-distance-def poincare-distance-formula ′-def
poincare-distance-formula-def to-complex-of-complex)
qed
