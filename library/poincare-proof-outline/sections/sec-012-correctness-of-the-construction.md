---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-012-correctness-of-the-construction
section_title: "Correctness of the construction"
section_number: null
pages: 20-28
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
For ﬁnite points, our deﬁnition matches the classic algebraic deﬁnition for points in C (given in ordinary, not
homogenous coordinates).
lemma poincare-line-non-homogenous:
assumes u⁄=∞h v⁄=∞h u⁄= v u ⁄= inversion v
shows let u ′ = to-complex u ; v ′ = to-complex v ;
A = i ∗ (u ′∗ cnj v ′− v ′∗ cnj u ′);
B = i ∗ (v ′∗ ((cmod u ′)2 + 1 )− u ′∗ ((cmod v ′)2 + 1 ))
20
in poincare-line u v = mk-circline A B (cnj B ) A
using assms
unfolding unit-disc-def disc-def inversion-def
apply (simp add : Let-def )
proof (transfer, transfer, safe)
ﬁx u1 u2 v1 v2
assume uv: ( u1, u2 )⁄= vec-zero (v1, v2 )⁄= vec-zero
¬ (u1, u2 )≈v∞v¬ (v1, v2 )≈v∞v
¬ (u1, u2 )≈v (v1, v2 )¬ (u1, u2 )≈v conjugate-cvec (reciprocal-cvec(v1, v2 ))
let ?u = to-complex-cvec (u1, u2 ) and ?v = to-complex-cvec (v1, v2 )
let ?A = i ∗ (?u∗ cnj ?v − ?v∗ cnj ?u )
let ?B = i ∗ (?v∗ ((cor (cmod ?u ))2 + 1 )− ?u∗ ((cor (cmod ?v ))2 + 1 ))
let ?C =− (i∗ (cnj ?v ∗ ((cor (cmod ?u ))2 + 1 )− cnj ?u ∗ ((cor (cmod ?v ))2 + 1 )))
let ?D = ?A
let ?H = ( ?A, ?B, ?C, ?D)
let ?den = u1∗ cnj u2 ∗ cnj v1 ∗ v2− v1∗ cnj v2 ∗ cnj u1 ∗ u2
have u2⁄= 0 v2 ⁄= 0
using uv
using inf-cvec-z2-zero-iﬀ
by blast+
have¬ (u1, u2 )≈v (cnj v2, cnj v1 )
using uv(6 )
by (simp add : vec-cnj-def )
moreover
have (cnj v2, cnj v1 )⁄= vec-zero
using uv(2 )
by auto
ultimately
have∗: u1∗ cnj v1 ⁄= u2∗ cnj v2 u1 ∗ v2⁄= u2∗ v1
using uv(5 ) uv(1 ) uv(2 ) ‹u2⁄= 0 › ‹v2⁄= 0 ›
using complex-cvec-eq-mix
by blast+
show circline-eq-cmat (poincare-line-cvec-cmat (u1, u2 ) ( v1, v2 ))
(mk-circline-cmat ?A ?B ?C ?D )
proof (cases ?den ⁄= 0 )
case True
let ?nom = v1∗ cnj v2 ∗ (u1∗ cnj u1 + u2∗ cnj u2 )− u1∗ cnj u2 ∗ (v1∗ cnj v1 + v2∗ cnj v2 )
let ?H ′ = mk-poincare-line-cmat (Re (i∗ ?den)) (i ∗ ?nom)
have circline-eq-cmat ?H ?H ′
proof−
let ?k = ( u2∗ cnj v2 )∗ (v2∗ cnj u2 )
have is-real ?k
using eq-cnj-iﬀ-real
by fastforce
hence cor (Re ?k ) = ?k
using complex-of-real-Re
by blast
have Re (i∗ ?den) = Re ?k ∗ ?A
proof−
have ?A = cnj ?A
by (simp add : ﬁeld-simps)
hence is-real ?A
using eq-cnj-iﬀ-real
by fastforce
moreover
have i∗ ?den = cnj (i∗ ?den)
by (simp add : ﬁeld-simps)
hence is-real (i∗ ?den)
21
using eq-cnj-iﬀ-real
by fastforce
hence cor (Re (i∗ ?den)) = i ∗ ?den
using complex-of-real-Re
by blast
ultimately
show ?thesis
using ‹cor (Re ?k ) = ?k›
by (simp add : ﬁeld-simps)
qed
moreover
have i∗ ?nom = Re ?k ∗ ?B
using ‹cor (Re ?k ) = ?k› ‹u2⁄= 0 › ‹v2⁄= 0 › complex-mult-cnj-cmod[symmetric]
by (auto simp add : ﬁeld-simps)
moreover
have ?k⁄= 0
using ‹u2⁄= 0 › ‹v2⁄= 0 ›
by simp
hence Re ?k ⁄= 0
using ‹is-real ?k ›
by (metis ‹cor (Re ?k ) = ?k› of-real-0)
ultimately
show ?thesis
by simp (rule-tac x =Re ?k in exI, simp add : mult.commute)
qed
moreover
have poincare-line-cvec-cmat (u1, u2 ) ( v1, v2 ) = ?H ′
using ‹?den⁄= 0 ›
unfolding poincare-line-cvec-cmat-def
by (simp add : Let-def )
moreover
hence hermitean ?H ′∧ ?H ′⁄= mat-zero
by (metis mk-poincare-line-cmat-hermitean poincare-line-cvec-cmat-nonzero uv (1 ) uv(2 ))
hence hermitean ?H ∧ ?H⁄= mat-zero
using ‹circline-eq-cmat ?H ?H ′›
using circline-eq-cmat-hermitean-nonzero[of ?H ′ ?H ] symp-circline-eq-cmat
unfolding symp-def
by metis
hence mk-circline-cmat ?A ?B ?C ?D = ?H
by simp
ultimately
have circline-eq-cmat (mk-circline-cmat ?A ?B ?C ?D )
(poincare-line-cvec-cmat (u1, u2 ) ( v1, v2 ))
by simp
thus ?thesis
using symp-circline-eq-cmat
unfolding symp-def
by blast
next
case False
let ?d = v1∗ (u1∗ cnj u1 / (u2∗ cnj u2 ) + 1 ) / v2− u1∗ (v1∗ cnj v1 / (v2∗ cnj v2 ) + 1 ) / u2
let ?cd = cnj v1 ∗ (u1∗ cnj u1 / (u2∗ cnj u2 ) + 1 ) / cnj v2 − cnj u1 ∗ (v1∗ cnj v1 / (v2∗ cnj v2 ) + 1 ) / cnj
u2
22
have cnj ?d = ?cd
by (simp add : mult.commute)
let ?d1 = ( v1 / v2 )∗ (cnj u1 / cnj u2 )− 1
let ?d2 = u1 / u2− v1 / v2
have∗∗: ?d = ?d1∗ ?d2
using ‹¬ ?den⁄= 0 › ‹u2⁄= 0 › ‹v2⁄= 0 ›
by(simp add : ﬁeld-simps)
hence ?d⁄= 0
using ‹¬ ?den⁄= 0 › ‹u2⁄= 0 › ‹v2⁄= 0 ›∗
by auto (simp add : ﬁeld-simps)+
have is-real ?d1
proof−
have cnj ?d1 = ?d1
using ‹¬ ?den⁄= 0 › ‹u2⁄= 0 › ‹v2⁄= 0 ›∗
by (simp add : ﬁeld-simps)
thus ?thesis
using eq-cnj-iﬀ-real
by blast
qed
show ?thesis
proof (cases u1 ∗ cnj u2 ⁄= 0 )
case True
let ?nom = u1∗ cnj u2
let ?H ′ = mk-poincare-line-cmat 0 (i∗ ?nom)
have circline-eq-cmat ?H ?H ′
proof−
let ?k = ( u1∗ cnj u2 ) / ?d
have is-real ?k
proof−
have is-real ((u1∗ cnj u2 ) / ?d2 )
proof−
let ?rhs = ( u2∗ cnj u2 ) / (1− (v1∗u2 )/(u1∗v2 ))
have 1 : ( u1∗ cnj u2 ) / ?d2 = ?rhs
using ‹¬ ?den⁄= 0 › ‹u2⁄= 0 › ‹v2⁄= 0 ›∗ ‹u1∗ cnj u2 ⁄= 0 ›
by (simp add : ﬁeld-simps)
moreover
have cnj ?rhs = ?rhs
proof−
have cnj (1− v1∗ u2 / (u1∗ v2 )) = 1− v1∗ u2 / (u1∗ v2 )
using ‹¬ ?den⁄= 0 › ‹u2⁄= 0 › ‹v2⁄= 0 ›∗ ‹u1∗ cnj u2 ⁄= 0 ›
by (simp add : ﬁeld-simps)
moreover
have cnj (u2∗ cnj u2 ) = u2∗ cnj u2
by simp
ultimately
show ?thesis
by simp
qed
ultimately
show ?thesis
using eq-cnj-iﬀ-real
by fastforce
qed
thus ?thesis
23
using∗∗ ‹is-real ?d1 ›
by (metis complex-cnj-divide divide-divide-eq-left ′ eq-cnj-iﬀ-real)
qed
have ?k⁄= 0
using ‹?d⁄= 0 › ‹u1∗ cnj u2 ⁄= 0 ›
by simp
have cnj ?k = ?k
using ‹is-real ?k ›
using eq-cnj-iﬀ-real by blast
have Re ?k ⁄= 0
using ‹?k⁄= 0 › ‹is-real ?k ›
by (metis complex.expand zero-complex.simps(1 ) zero-complex.simps(2 ))
have u1∗ cnj u2 = ?k∗ ?d
using ‹?d⁄= 0 ›
by simp
moreover
hence cnj u1 ∗ u2 = cnj ?k ∗ cnj ?d
by (metis complex-cnj-cnj complex-cnj-mult )
hence cnj u1 ∗ u2 = ?k∗ ?cd
using ‹cnj ?k = ?k› ‹cnj ?d = ?cd›
by metis
ultimately
show ?thesis
using ‹∼ ?den⁄= 0 › ‹u1∗ cnj u2 ⁄= 0 › ‹u2⁄= 0 › ‹v2⁄= 0 › ‹Re ?k ⁄= 0 › ‹is-real ?k › ‹?d⁄= 0 ›
using complex-mult-cnj-cmod[symmetric, of u1 ]
using complex-mult-cnj-cmod[symmetric, of v1 ]
using complex-mult-cnj-cmod[symmetric, of u2 ]
using complex-mult-cnj-cmod[symmetric, of v2 ]
apply (simp add : power-divide norm-mult norm-divide )
apply (rule-tac x =Re ?k in exI )
apply simp
apply (simp add : ﬁeld-simps)
done
qed
moreover
have poincare-line-cvec-cmat (u1, u2 ) ( v1, v2 ) = ?H ′
using ‹¬ ?den⁄= 0 › ‹u1∗ cnj u2 ⁄= 0 ›
unfolding poincare-line-cvec-cmat-def
by (simp add : Let-def )
moreover
hence hermitean ?H ′∧ ?H ′⁄= mat-zero
by (metis mk-poincare-line-cmat-hermitean poincare-line-cvec-cmat-nonzero uv (1 ) uv(2 ))
hence hermitean ?H ∧ ?H⁄= mat-zero
using ‹circline-eq-cmat ?H ?H ′›
using circline-eq-cmat-hermitean-nonzero[of ?H ′ ?H ] symp-circline-eq-cmat
unfolding symp-def
by metis
hence mk-circline-cmat ?A ?B ?C ?D = ?H
by simp
ultimately
24
have circline-eq-cmat (mk-circline-cmat ?A ?B ?C ?D )
(poincare-line-cvec-cmat (u1, u2 ) ( v1, v2 ))
by simp
thus ?thesis
using symp-circline-eq-cmat
unfolding symp-def
by blast
next
case False
show ?thesis
proof (cases v1 ∗ cnj v2 ⁄= 0 )
case True
let ?nom = v1∗ cnj v2
let ?H ′ = mk-poincare-line-cmat 0 (i∗ ?nom)
have circline-eq-cmat ?H ?H ′
proof−
let ?k = ( v1∗ cnj v2 ) / ?d
have is-real ?k
proof−
have is-real ((v1∗ cnj v2 ) / ?d2 )
proof−
let ?rhs = ( v2∗ cnj v2 ) / ((u1∗v2 )/(u2∗v1 )− 1 )
have 1 : ( v1∗ cnj v2 ) / ?d2 = ?rhs
using ‹¬ ?den⁄= 0 › ‹u2⁄= 0 › ‹v2⁄= 0 ›∗ ‹v1∗ cnj v2 ⁄= 0 ›
by (simp add : ﬁeld-simps)
moreover
have cnj ?rhs = ?rhs
proof−
have cnj (u1∗ v2 / (u2∗ v1 )− 1 ) = u1∗ v2 / (u2∗ v1 )− 1
using ‹¬ ?den⁄= 0 › ‹u2⁄= 0 › ‹v2⁄= 0 ›∗ ‹v1∗ cnj v2 ⁄= 0 ›
by (simp add : ﬁeld-simps)
moreover
have cnj (v2∗ cnj v2 ) = v2∗ cnj v2
by simp
ultimately
show ?thesis
by simp
qed
ultimately
show ?thesis
using eq-cnj-iﬀ-real
by fastforce
qed
thus ?thesis
using∗∗ ‹is-real ?d1 ›
by (metis complex-cnj-divide divide-divide-eq-left ′ eq-cnj-iﬀ-real)
qed
have ?k⁄= 0
using ‹?d⁄= 0 › ‹v1∗ cnj v2 ⁄= 0 ›
by simp
have cnj ?k = ?k
using ‹is-real ?k ›
using eq-cnj-iﬀ-real by blast
have Re ?k ⁄= 0
using ‹?k⁄= 0 › ‹is-real ?k ›
by (metis complex.expand zero-complex.simps(1 ) zero-complex.simps(2 ))
25
have v1∗ cnj v2 = ?k∗ ?d
using ‹?d⁄= 0 ›
by simp
moreover
hence cnj v1 ∗ v2 = cnj ?k ∗ cnj ?d
by (metis complex-cnj-cnj complex-cnj-mult )
hence cnj v1 ∗ v2 = ?k∗ ?cd
using ‹cnj ?k = ?k› ‹cnj ?d = ?cd›
by metis
ultimately
show ?thesis
using ‹∼ ?den⁄= 0 › ‹v1∗ cnj v2 ⁄= 0 › ‹u2⁄= 0 › ‹v2⁄= 0 › ‹Re ?k ⁄= 0 › ‹is-real ?k › ‹?d⁄= 0 ›
using complex-mult-cnj-cmod[symmetric, of u1 ]
using complex-mult-cnj-cmod[symmetric, of v1 ]
using complex-mult-cnj-cmod[symmetric, of u2 ]
using complex-mult-cnj-cmod[symmetric, of v2 ]
apply (simp add : power-divide norm-mult norm-divide )
apply (rule-tac x =Re ?k in exI )
apply simp
apply (simp add : ﬁeld-simps)
done
qed
moreover
have poincare-line-cvec-cmat (u1, u2 ) ( v1, v2 ) = ?H ′
using ‹¬ ?den⁄= 0 › ‹¬ u1∗ cnj u2 ⁄= 0 › ‹v1∗ cnj v2 ⁄= 0 ›
unfolding poincare-line-cvec-cmat-def
by (simp add : Let-def )
moreover
hence hermitean ?H ′∧ ?H ′⁄= mat-zero
by (metis mk-poincare-line-cmat-hermitean poincare-line-cvec-cmat-nonzero uv (1 ) uv(2 ))
hence hermitean ?H ∧ ?H⁄= mat-zero
using ‹circline-eq-cmat ?H ?H ′›
using circline-eq-cmat-hermitean-nonzero[of ?H ′ ?H ] symp-circline-eq-cmat
unfolding symp-def
by metis
hence mk-circline-cmat ?A ?B ?C ?D = ?H
by simp
ultimately
have circline-eq-cmat (mk-circline-cmat ?A ?B ?C ?D )
(poincare-line-cvec-cmat (u1, u2 ) ( v1, v2 ))
by simp
thus ?thesis
using symp-circline-eq-cmat
unfolding symp-def
by blast
next
case False
hence False
using ‹¬ ?den⁄= 0 › ‹¬ u1∗ cnj u2 ⁄= 0 › uv
by (simp add : ‹u2⁄= 0 › ‹v2⁄= 0 ›)
thus ?thesis
by simp
qed
qed
26
qed
qed
Our construction (in homogenous coordinates) always yields an h-line that contain two starting points (this
also holds for all degenerate cases except when points are the same).
lemma poincare-line [simp]:
assumes z⁄= w
shows on-circline (poincare-line z w ) z
on-circline (poincare-line z w ) w
proof−
have on-circline (poincare-line z w ) z∧ on-circline (poincare-line z w ) w
using assms
proof (transfer, transfer)
ﬁx z w
assume vz: z⁄= vec-zero w⁄= vec-zero
obtain z1 z2 w1 w2 where
zw: ( z1, z2 ) = z (w1, w2 ) = w
by (cases z, cases w, auto)
let ?den = z1∗cnj z2∗cnj w1∗w2− w1∗cnj w2∗cnj z1∗z2
have∗: cor (Re (i∗ ?den)) = i ∗ ?den
proof−
have cnj ?den =−?den
by auto
hence is-imag ?den
using eq-minus-cnj-iﬀ-imag[of ?den ]
by simp
thus ?thesis
using complex-of-real-Re[of i∗ ?den]
by simp
qed
show on-circline-cmat-cvec (poincare-line-cvec-cmat z w ) z∧
on-circline-cmat-cvec (poincare-line-cvec-cmat z w ) w
unfolding poincare-line-cvec-cmat-def mk-poincare-line-cmat-def
apply (subst zw [symmetric])+
unfolding Let-def prod.case
apply (subst∗)+
by (auto simp add : vec-cnj-def ﬁeld-simps )
qed
thus on-circline (poincare-line z w ) z on-circline (poincare-line z w ) w
by auto
qed
lemma poincare-line-circline-set [simp]:
assumes z⁄= w
shows z∈ circline-set (poincare-line z w )
w∈ circline-set (poincare-line z w )
using assms
by (auto simp add : circline-set-def )
When the points are diﬀerent, the constructed line matrix always has a negative determinant
lemma poincare-line-type:
assumes z⁄= w
shows circline-type (poincare-line z w ) = −1
proof−
have∃ a b. a⁄= b∧{ a, b}⊆ circline-set (poincare-line z w )
using poincare-line[of z w ] assms
unfolding circline-set-def
by (rule-tac x =z in exI, rule-tac x =w in exI, simp)
thus ?thesis
using circline-type[of poincare-line z w ]
using circline-type-pos-card-eq0[of poincare-line z w ]
using circline-type-zero-card-eq1[of poincare-line z w ]
by auto
qed
27
The constructed line is an h-line in the Poincaré model (in all cases when the two points are diﬀerent)
lemma is-poincare-line-poincare-line [simp]:
assumes z⁄= w
shows is-poincare-line (poincare-line z w )
using poincare-line-type[of z w , OF assms ]
proof (transfer, transfer)
ﬁx z w
assume vz: z⁄= vec-zero w⁄= vec-zero
obtain A B C D where∗: poincare-line-cvec-cmat z w = ( A, B, C, D)
by (cases poincare-line-cvec-cmat z w ) auto
assume circline-type-cmat (poincare-line-cvec-cmat z w ) = − 1
thus is-poincare-line-cmat (poincare-line-cvec-cmat z w )
using vz∗
using poincare-line-cvec-cmat-hermitean[of z w ]
using poincare-line-cvec-cmat-nonzero[of z w ]
using poincare-line-cvec-cmat-AeqD[of z w A B C D ]
using hermitean-elems[of A B C D ]
using cmod-power2[of D ] cmod-power2[of C ]
unfolding is-poincare-line-cmat-def
by (simp del : poincare-line-cvec-cmat-def add: sgn-1-neg power2-eq-square)
qed
When the points are diﬀerent, the constructed h-line between two points also contains their inverses
lemma poincare-line-inversion:
assumes z⁄= w
shows on-circline (poincare-line z w ) ( inversion z )
on-circline (poincare-line z w ) ( inversion w )
using assms
using is-poincare-line-poincare-line[OF ‹z⁄= w›]
using is-poincare-line-inverse-point
unfolding circline-set-def
by auto
When the points are diﬀerent, the onstructed h-line between two points contains the inverse of its every point
lemma poincare-line-inversion-full:
assumes u⁄= v
assumes on-circline (poincare-line u v ) x
shows on-circline (poincare-line u v ) ( inversion x )
using is-poincare-line-inverse-point[of poincare-line u v x ]
using is-poincare-line-poincare-line[OF ‹u⁄= v›] assms
unfolding circline-set-def
by simp
