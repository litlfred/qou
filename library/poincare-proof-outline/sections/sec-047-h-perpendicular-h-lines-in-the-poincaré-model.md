---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-047-h-perpendicular-h-lines-in-the-poincaré-model
section_title: "H-perpendicular h-lines in the Poincaré model"
section_number: null
pages: 114-124
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
deﬁnition perpendicular-to-x-axis-cmat :: complex-mat⇒ bool where
[simp]: perpendicular-to-x-axis-cmat H ←→ (let (A, B, C, D) = H in is-real B )
lift-deﬁnition perpendicular-to-x-axis-clmat :: circline-mat⇒ bool is perpendicular-to-x-axis-cmat
done
lift-deﬁnition perpendicular-to-x-axis :: circline⇒ bool is perpendicular-to-x-axis-clmat
by transfer auto
lemma perpendicular-to-x-axis:
assumes is-poincare-line H
shows perpendicular-to-x-axis H ←→ perpendicular x-axis H
using assms
unfolding perpendicular-def
proof (transfer, transfer)
ﬁx H
assume hh: hermitean H ∧ H⁄= mat-zero is-poincare-line-cmat H
obtain A B C D where∗: H = ( A, B, C, D)
by (cases H, auto)
hence is-real A (cmod B )2 > (cmod A )2 H = ( A, B, cnj B, A)
using hermitean-elems[of A B C D ] hh
by auto
114
thus perpendicular-to-x-axis-cmat H =
(cos-angle-cmat (of-circline-cmat x-axis-cmat ) ( of-circline-cmat H ) = 0 )
using cmod-square[of B ] cmod-square[of A ]
by simp
qed
lemma perpendicular-to-x-axis-y-axis:
assumes perpendicular-to-x-axis (poincare-line 0 h (of-complex z )) z⁄= 0
shows is-imag z
using assms
by (transfer, transfer, simp)
lemma wlog-perpendicular-axes:
assumes in-disc: u∈ unit-disc v ∈ unit-disc z ∈ unit-disc
assumes perpendicular: is-poincare-line H1 is-poincare-line H2 perpendicular H1 H2
assumes z∈ circline-set H1 ∩ circline-set H2 u ∈ circline-set H1 v ∈ circline-set H2
assumes axes: ⋀ x y. [ [is-real x ; 0 ≤ Re x ; Re x < 1 ; is-imag y ; 0 ≤ Im y ; Im y < 1 ] ] =⇒ P 0 h (of-complex x )
(of-complex y )
assumes moebius: ⋀ M u v w . [ [unit-disc-ﬁx M ; u∈ unit-disc; v∈ unit-disc; w∈ unit-disc; P (moebius-pt M u )
(moebius-pt M v ) ( moebius-pt M w ) ] ] =⇒ P u v w
assumes conjugate: ⋀ u v w . [ [u∈ unit-disc; v∈ unit-disc; w∈ unit-disc; P (conjugate u ) ( conjugate v ) ( conjugate
w) ] ] =⇒ P u v w
shows P z u v
proof−
have∀ v H1 H2 . is-poincare-line H1 ∧ is-poincare-line H2 ∧ perpendicular H1 H2 ∧
z∈ circline-set H1 ∩ circline-set H2 ∧ u∈ circline-set H1 ∧ v∈ circline-set H2 ∧ v∈ unit-disc−→ P
z u v (is ?P z u )
proof (rule wlog-x-axis [where P=?P])
ﬁx x
assume x: is-real x Re x ≥ 0 Re x < 1
have of-complex x ∈ unit-disc
using x
by (simp add : cmod-eq-Re)
show ?P 0 h (of-complex x )
proof safe
ﬁx v H1 H2
assume v∈ unit-disc
then obtain y where y: v = of-complex y
using inf-or-of-complex[of v ]
by auto
assume 1 : is-poincare-line H1 is-poincare-line H2 perpendicular H1 H2
assume 2 : 0 h∈ circline-set H1 0 h∈ circline-set H2 of-complex x ∈ circline-set H1 v ∈ circline-set H2
show P 0 h (of-complex x ) v
proof (cases of-complex x = 0 h)
case True
show P 0 h (of-complex x ) v
proof (cases v = 0 h)
case True
thus ?thesis
using ‹of-complex x = 0 h›
using axes[of 0 0 ]
by simp
next
case False
show ?thesis
proof (rule wlog-rotation-to-positive-y-axis )
show v∈ unit-disc v ⁄= 0 h
by fact+
next
ﬁx y
assume is-imag y 0 < Im y Im y < 1
thus P 0 h (of-complex x ) ( of-complex y )
115
using x axes [of x y ]
by simp
next
ﬁx ϕ u
assume u∈ unit-disc u ⁄= 0 h
P 0 h (of-complex x ) ( moebius-pt (moebius-rotationϕ) u)
thus P 0 h (of-complex x ) u
using ‹of-complex x = 0 h›
using moebius[of moebius-rotation ϕ 0 h 0 h u]
by simp
qed
qed
next
case False
hence∗: poincare-line 0 h (of-complex x ) = x-axis
using x poincare-line-0-real-is-x-axis[of of-complex x ]
unfolding circline-set-x-axis
by auto
hence H1 = x-axis
using unique-poincare-line[of 0 h of-complex x H1 ] 1 2
using ‹of-complex x ∈ unit-disc› False
by simp
have is-imag y
proof (cases y = 0 )
case True
thus ?thesis
by simp
next
case False
hence 0 h⁄= of-complex y
using of-complex-zero-iﬀ [of y ]
by metis
hence H2 = poincare-line 0 h (of-complex y )
using 1 2 ‹v∈ unit-disc›
using unique-poincare-line[of 0 h of-complex y H2 ] y
by simp
thus ?thesis
using 1 ‹H1 = x-axis›
using perpendicular-to-x-axis-y-axis[of y ] False
using perpendicular-to-x-axis[of H2 ]
by simp
qed
show P 0 h (of-complex x ) v
proof (cases Im y ≥ 0 )
case True
thus ?thesis
using axes[of x y ] x y ‹is-imag y › ‹v∈ unit-disc›
by (simp add : cmod-eq-Im)
next
case False
show ?thesis
proof (rule conjugate )
have Im (cnj y ) < 1
using ‹v∈ unit-disc› y ‹is-imag y › eq-minus-cnj-iﬀ-imag[of y ]
by (simp add : cmod-eq-Im)
thus P (conjugate 0 h) ( conjugate (of-complex x )) ( conjugate v )
using ‹is-real x › eq-cnj-iﬀ-real[of x ] y ‹is-imag y ›
using axes[OF x, of cnj y ] False
by simp
show 0 h∈ unit-disc of-complex x ∈ unit-disc v ∈ unit-disc
by (simp, fact+)
qed
qed
qed
qed
next
116
show z∈ unit-disc u ∈ unit-disc
by fact+
next
ﬁx M u v
assume∗: unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc
assume∗∗: ?P (moebius-pt M u ) ( moebius-pt M v )
show ?P u v
proof safe
ﬁx w H1 H2
assume∗∗∗: is-poincare-line H1 is-poincare-line H2 perpendicular H1 H2
u∈ circline-set H1 u ∈ circline-set H2
v∈ circline-set H1 w ∈ circline-set H2 w ∈ unit-disc
thus P u v w
using moebius[of M u v w ]∗
using∗∗[rule-format, of moebius-circline M H1 moebius-circline M H2 moebius-pt M w ]
by simp
qed
qed
thus ?thesis
using assms
by blast
qed
lemma wlog-perpendicular-foot:
assumes in-disc: u∈ unit-disc v ∈ unit-disc w ∈ unit-disc z ∈ unit-disc
assumes perpendicular: u⁄= v is-poincare-line H perpendicular (poincare-line u v ) H
assumes z∈ circline-set (poincare-line u v )∩ circline-set H w ∈ circline-set H
assumes axes: ⋀ u v w . [ [is-real u ; 0 < Re u ; Re u < 1 ; is-real v ;−1 < Re v ; Re v < 1 ; Re u ⁄= Re v ; is-imag w ; 0
≤ Im w ; Im w < 1 ] ] =⇒ P 0 h (of-complex u ) ( of-complex v ) ( of-complex w )
assumes moebius: ⋀ M z u v w . [ [unit-disc-ﬁx M ; u ∈ unit-disc; v ∈ unit-disc; w ∈ unit-disc; z ∈ unit-disc; P
(moebius-pt M z ) ( moebius-pt M u ) ( moebius-pt M v ) ( moebius-pt M w ) ] ] =⇒ P z u v w
assumes conjugate: ⋀ z u v w . [ [u∈ unit-disc; v∈ unit-disc; w∈ unit-disc; P (conjugate z ) ( conjugate u ) ( conjugate
v) ( conjugate w ) ] ] =⇒ P z u v w
assumes perm: P z v u w =⇒ P z u v w
shows P z u v w
proof−
obtain m n where mn: m = u∨ m = v n = u∨ n = v m ⁄= n m ⁄= z
using ‹u⁄= v›
by auto
have n∈ circline-set (poincare-line z m )
using ‹z∈ circline-set (poincare-line u v )∩ circline-set H ›
using mn
using unique-poincare-line[of z m poincare-line u v , symmetric] in-disc
by auto
have∀ n. n∈ unit-disc∧ m⁄= n∧ n∈ circline-set (poincare-line z m )∧ m⁄= z−→ P z m n w (is ?Q z m w )
proof (rule wlog-perpendicular-axes [where P=?Q])
show is-poincare-line (poincare-line u v )
using ‹u⁄= v›
by auto
next
show is-poincare-line H
by fact
next
show m∈ unit-disc m ∈ circline-set (poincare-line u v )
using mn in-disc
by auto
next
show w∈ unit-disc z ∈ unit-disc
by fact+
next
show z∈ circline-set (poincare-line u v )∩ circline-set H
by fact
next
show perpendicular (poincare-line u v ) H
117
by fact
next
show w∈ circline-set H
by fact
next
ﬁx x y
assume xy: is-real x 0 ≤ Re x Re x < 1 is-imag y 0 ≤ Im y Im y < 1
show ?Q 0 h (of-complex x ) ( of-complex y )
proof safe
ﬁx n
assume n∈ unit-disc of-complex x ⁄= n
assume n∈ circline-set (poincare-line 0 h (of-complex x )) of-complex x ⁄= 0 h
hence n∈ circline-set x-axis
using poincare-line-0-real-is-x-axis[of of-complex x ] xy
by (auto simp add : circline-set-x-axis)
then obtain n ′ where n ′: n = of-complex n ′
using inf-or-of-complex[of n ] ‹n∈ unit-disc›
by auto
hence is-real n ′
using ‹n∈ circline-set x-axis ›
using of-complex-inj
unfolding circline-set-x-axis
by auto
hence−1 < Re n ′ Re n ′< 1
using ‹n∈ unit-disc› n ′
by (auto simp add : cmod-eq-Re)
have Re n ′⁄= Re x
using complex.expand[of n ′ x] ‹is-real n ′› ‹is-real x › ‹of-complex x ⁄= n› n ′
by auto
have Re x > 0
using xy ‹of-complex x ⁄= 0 h›
by (cases Re x = 0, auto simp add : complex.expand)
show P 0 h (of-complex x ) n (of-complex y )
using axes[of x n ′ y] xy n ′ ‹Re x > 0 › ‹is-real n ′› ‹−1 < Re n ′› ‹Re n ′< 1 › ‹Re n ′⁄= Re x ›
by simp
qed
next
ﬁx M u v w
assume 1 : unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc w ∈ unit-disc
assume 2 : ?Q (moebius-pt M u ) ( moebius-pt M v ) ( moebius-pt M w )
show ?Q u v w
proof safe
ﬁx n
assume n∈ unit-disc v ⁄= n n ∈ circline-set (poincare-line u v ) v⁄= u
thus P u v n w
using moebius[of M v n w u ] 1 2 [rule-format, of moebius-pt M n ]
by fastforce
qed
next
ﬁx u v w
assume 1 : u∈ unit-disc v ∈ unit-disc w ∈ unit-disc
assume 2 : ?Q (conjugate u ) ( conjugate v ) ( conjugate w )
show ?Q u v w
proof safe
ﬁx n
assume n∈ unit-disc v ⁄= n n ∈ circline-set (poincare-line u v ) v⁄= u
thus P u v n w
using conjugate[of v n w u ] 1 2 [rule-format, of conjugate n ]
using conjugate-inj
by auto
qed
qed
thus ?thesis
118
using mn in-disc ‹n∈ circline-set (poincare-line z m )› perm
by auto
qed
lemma perpendicular-to-x-axis-intersects-x-axis:
assumes is-poincare-line H perpendicular-to-x-axis H
shows intersects-x-axis H
using assms hermitean-elems
by (transfer, transfer, auto simp add : cmod-eq-Re)
lemma perpendicular-intersects:
assumes is-poincare-line H1 is-poincare-line H2
assumes perpendicular H1 H2
shows∃ z. z∈ unit-disc∧ z∈ circline-set H1 ∩ circline-set H2 (is ?P ′ H1 H2 )
proof−
have∀ H2. is-poincare-line H2 ∧ perpendicular H1 H2 −→ ?P ′ H1 H2 (is ?P H1 )
proof (rule wlog-line-x-axis )
show ?P x-axis
proof safe
ﬁx H2
assume is-poincare-line H2 perpendicular x-axis H2
thus∃ z. z∈ unit-disc∧ z∈ circline-set x-axis ∩ circline-set H2
using perpendicular-to-x-axis[of H2 ]
using perpendicular-to-x-axis-intersects-x-axis[of H2 ]
using intersects-x-axis-iﬀ [of H2 ]
by auto
qed
next
ﬁx M
assume unit-disc-ﬁx M
assume∗: ?P (moebius-circline M H1 )
show ?P H1
proof safe
ﬁx H2
assume is-poincare-line H2 perpendicular H1 H2
then obtain z where z∈ unit-disc z ∈ circline-set (moebius-circline M H1 )∧ z∈ circline-set (moebius-circline
M H2 )
using∗[rule-format, of moebius-circline M H2 ] ‹unit-disc-ﬁx M ›
by auto
thus∃ z. z∈ unit-disc∧ z∈ circline-set H1 ∩ circline-set H2
using ‹unit-disc-ﬁx M ›
by (rule-tac x =moebius-pt (−M ) z in exI )
(metis IntI add .inverse-inverse circline-set-moebius-circline-iﬀ moebius-pt-comp-inv-left uminus-moebius-def
unit-disc-ﬁx-discI unit-disc-ﬁx-moebius-uminus )
qed
next
show is-poincare-line H1
by fact
qed
thus ?thesis
using assms
by auto
qed
deﬁnition calc-perpendicular-to-x-axis-cmat :: complex-vec⇒ complex-mat where
[simp]: calc-perpendicular-to-x-axis-cmat z =
(let (z1, z2 ) = z
in if z1∗cnj z2 + z2∗cnj z1 = 0 then
(0, 1, 1, 0 )
else
let A = z1∗cnj z2 + z2∗cnj z1 ;
B =−(z1∗cnj z1 + z2∗cnj z2 )
in (A, B, B, A)
)
119
lift-deﬁnition calc-perpendicular-to-x-axis-clmat :: complex-homo-coords⇒ circline-mat is calc-perpendicular-to-x-axis-cmat
by (auto simp add : hermitean-def mat-adj-def mat-cnj-def Let-def split : if-split-asm)
lift-deﬁnition calc-perpendicular-to-x-axis :: complex-homo⇒ circline is calc-perpendicular-to-x-axis-clmat
proof (transfer)
ﬁx z w
assume z⁄= vec-zero w⁄= vec-zero
obtain z1 z2 w1 w2 where zw: z = ( z1, z2 ) w = ( w1, w2 )
by (cases z, cases w, auto)
assume z≈v w
then obtain k where∗: k⁄= 0 w1 = k∗z1 w2 = k∗z2
using zw
by auto
have w1∗ cnj w2 + w2∗ cnj w1 = ( k∗ cnj k )∗ (z1∗ cnj z2 + z2∗ cnj z1 )
using∗
by (auto simp add : ﬁeld-simps)
moreover
have w1∗ cnj w1 + w2∗ cnj w2 = ( k∗ cnj k )∗ (z1∗ cnj z1 + z2∗ cnj z2 )
using∗
by (auto simp add : ﬁeld-simps)
ultimately
show circline-eq-cmat (calc-perpendicular-to-x-axis-cmat z ) ( calc-perpendicular-to-x-axis-cmat w)
using zw∗
apply (auto simp add : Let-def )
apply (rule-tac x =Re (k∗ cnj k ) in exI, auto simp add : complex.expand ﬁeld-simps )
done
qed
lemma calc-perpendicular-to-x-axis:
assumes z⁄= of-complex 1 z ⁄= of-complex (−1 )
shows z∈ circline-set (calc-perpendicular-to-x-axis z )∧
is-poincare-line (calc-perpendicular-to-x-axis z )∧
perpendicular-to-x-axis (calc-perpendicular-to-x-axis z )
using assms
unfolding circline-set-def perpendicular-def
proof (simp, transfer, transfer)
ﬁx z :: complex-vec
obtain z1 z2 where z: z = ( z1, z2 )
by (cases z, auto)
assume∗∗:¬ z≈v of-complex-cvec 1 ¬ z≈v of-complex-cvec (− 1 )
show on-circline-cmat-cvec (calc-perpendicular-to-x-axis-cmat z ) z∧
is-poincare-line-cmat (calc-perpendicular-to-x-axis-cmat z )∧
perpendicular-to-x-axis-cmat (calc-perpendicular-to-x-axis-cmat z )
proof (cases z1∗cnj z2 + z2∗cnj z1 = 0 )
case True
thus ?thesis
using z
by (simp add : vec-cnj-def hermitean-def mat-adj-def mat-cnj-def mult .commute)
next
case False
hence z2⁄= 0
using z
by auto
hence Re (z2∗ cnj z2 )⁄= 0
using ‹z2⁄= 0 ›
by (auto simp add : complex.expand)
have z1⁄=−z2∧ z1⁄= z2
proof (rule ccontr )
assume¬ ?thesis
hence z≈v of-complex-cvec 1 ∨ z≈v of-complex-cvec (−1 )
using z ‹z2⁄= 0 ›
by auto
thus False
using∗∗
120
by auto
qed
let ?A = z1∗cnj z2 + z2∗cnj z1 and ?B =−(z1∗cnj z1 + z2∗cnj z2 )
have Re(z1∗cnj z1 + z2∗cnj z2 )≥ 0
by auto
hence Re ?B ≤ 0
by (smt uminus-complex.simps(1 ))
hence abs (Re ?B ) = − Re ?B
by auto
also have ... = ( Re z1 )2 + ( Im z1 )2 + ( Re z2 )2 + ( Im z2 )2
by (simp add : power2-eq-square[symmetric])
also have ... >abs (Re ?A )
proof (cases Re ?A ≥ 0 )
case False
have (Re z1 + Re z2 )2 + ( Im z1 + Im z2 )2 > 0
using ‹z1⁄=−z2∧ z1⁄= z2 ›
by (metis add.commute add.inverse-unique complex-neq-0 plus-complex.code plus-complex.simps)
thus ?thesis
using False
by (simp add : power2-sum power2-eq-square ﬁeld-simps )
next
case True
have (Re z1 − Re z2 )2 + ( Im z1 − Im z2 )2 > 0
using ‹z1⁄=−z2∧ z1⁄= z2 ›
by (meson complex-eq-iﬀ right-minus-eq sum-power2-gt-zero-iﬀ )
thus ?thesis
using True
by (simp add : power2-sum power2-eq-square ﬁeld-simps )
qed
ﬁnally
have abs (Re ?B ) > abs (Re ?A )
.
moreover
have cmod ?B = abs (Re ?B ) cmod ?A = abs (Re ?A )
by (simp-all add : cmod-eq-Re)
ultimately
have (cmod ?B )2 > (cmod ?A )2
by (smt power2-le-imp-le )
thus ?thesis
using z False
by (simp-all add : Let-def hermitean-def mat-adj-def mat-cnj-def cmod-eq-Re vec-cnj-def ﬁeld-simps )
qed
qed
lemma ex-perpendicular:
assumes is-poincare-line H z ∈ unit-disc
shows∃ H ′. is-poincare-line H ′∧ perpendicular H H ′∧ z∈ circline-set H ′ (is ?P ′ H z )
proof−
have∀ z. z∈ unit-disc−→ ?P ′ H z (is ?P H )
proof (rule wlog-line-x-axis )
show ?P x-axis
proof safe
ﬁx z
assume z∈ unit-disc
then have z⁄= of-complex 1 z ⁄= of-complex (−1 )
by auto
thus ?P ′ x-axis z
using ‹z∈ unit-disc›
using calc-perpendicular-to-x-axis[of z ] perpendicular-to-x-axis
by (rule-tac x = calc-perpendicular-to-x-axis z in exI, auto)
qed
next
ﬁx M
assume unit-disc-ﬁx M
assume∗: ?P (moebius-circline M H )
121
show ?P H
proof safe
ﬁx z
assume z∈ unit-disc
hence moebius-pt M z ∈ unit-disc
using ‹unit-disc-ﬁx M ›
by auto
then obtain H ′ where∗: is-poincare-line H ′ perpendicular (moebius-circline M H ) H ′ moebius-pt M z∈ circline-set
H ′
using∗
by auto
have h: H = moebius-circline (−M ) ( moebius-circline M H )
by auto
show ?P ′ H z
using∗ ‹unit-disc-ﬁx M ›
apply (subst h )
apply (rule-tac x =moebius-circline (−M ) H ′ in exI )
apply (simp del : moebius-circline-comp-inv-left)
done
qed
qed fact
thus ?thesis
using assms
by simp
qed
lemma ex-perpendicular-foot:
assumes is-poincare-line H z ∈ unit-disc
shows∃ H ′. is-poincare-line H ′∧ z∈ circline-set H ′∧ perpendicular H H ′∧
(∃ z ′∈ unit-disc. z ′∈ circline-set H ′∩ circline-set H )
using assms
using ex-perpendicular[OF assms ]
using perpendicular-intersects[of H ]
by blast
lemma Pythagoras:
assumes in-disc: u∈ unit-disc v ∈ unit-disc w ∈ unit-disc v ⁄= w
assumes distinct[u, v, w]−→ perpendicular (poincare-line u v ) ( poincare-line u w )
shows cosh (poincare-distance v w ) = cosh (poincare-distance u v )∗ cosh (poincare-distance u w ) ( is ?P ′ u v w )
proof (cases distinct [u, v, w])
case False
thus ?thesis
using in-disc
by (auto simp add : poincare-distance-sym)
next
case True
have distinct [u, v, w]−→ ?P ′ u v w (is ?P u v w )
proof (rule wlog-perpendicular-axes [where P=?P])
show is-poincare-line (poincare-line u v ) is-poincare-line (poincare-line u w )
using ‹distinct [u, v, w]›
by simp-all
next
show perpendicular (poincare-line u v ) ( poincare-line u w )
using True assms
by simp
next
show u∈ unit-disc v ∈ unit-disc w ∈ unit-disc
by fact+
next
show v∈ circline-set (poincare-line u v ) w∈ circline-set (poincare-line u w )
u∈ circline-set (poincare-line u v )∩ circline-set (poincare-line u w )
using ‹distinct [u, v, w]›
by auto
next
ﬁx x y
assume x: is-real x 0 ≤ Re x Re x < 1
122
assume y: is-imag y 0 ≤ Im y Im y < 1
have of-complex x ∈ unit-disc of-complex y ∈ unit-disc
using x y
by (simp-all add : cmod-eq-Re cmod-eq-Im)
show ?P 0 h (of-complex x ) ( of-complex y )
proof
assume distinct [0 h, of-complex x, of-complex y ]
hence x⁄= 0 y ⁄= 0
by auto
let ?den1 = 1− (cmod x )2 and ?den2 = 1− (cmod y )2
have ?den1 > 0 ?den2 > 0
using x y
by (simp-all add : cmod-eq-Re cmod-eq-Im abs-square-less-1 )
let ?d1 = 1 + 2∗ (cmod x )2 / ?den1
have cosh (poincare-distance 0 h (of-complex x )) = ?d1
using ‹?den1 > 0 ›
using poincare-distance-formula[of 0 h of-complex x ] ‹of-complex x ∈ unit-disc›
by simp
moreover
let ?d2 = 1 + 2∗ (cmod y )2 / ?den2
have cosh (poincare-distance 0 h (of-complex y )) = ?d2
using ‹?den2 > 0 › ‹of-complex y ∈ unit-disc›
using poincare-distance-formula[of 0 h of-complex y ]
by simp
moreover
let ?den = ?den1∗ ?den2
let ?d3 = 1 + 2∗ (cmod (x− y))2 / ?den
have cosh (poincare-distance (of-complex x ) ( of-complex y )) = ?d3
using ‹of-complex x ∈ unit-disc› ‹of-complex y ∈ unit-disc›
using ‹?den1 > 0 › ‹?den2 > 0 ›
using poincare-distance-formula[of of-complex x of-complex y ]
by simp
moreover
have ?d1∗ ?d2 = ?d3
proof−
have ?d3 = (( 1− (cmod x )2)∗ (1− (cmod y )2) + 2∗ (cmod (x− y))2) / ?den
using ‹?den1 > 0 › ‹?den2 > 0 ›
by (subst add-num-frac, simp, simp)
also have ... = ( Re ((1− x∗ cnj x )∗ (1− y∗ cnj y ) + 2∗ (x− y)∗cnj (x− y)) / ?den)
using ‹is-real x › ‹is-imag y ›
by ((subst cmod-square )+, simp)
also have ... = Re (1 + x∗ cnj x ∗ y∗ cnj y
+ x∗ cnj x − 2∗ y∗ cnj x − 2∗ x∗ cnj y + y∗ cnj y ) / ?den
by (simp add : ﬁeld-simps)
also have ... = Re ((1 + y∗ cnj y )∗ (1 + x∗ cnj x )) / ?den
using ‹is-real x › ‹is-imag y ›
by (simp add : ﬁeld-simps)
ﬁnally
show ?thesis
using ‹?den1 > 0 › ‹?den2 > 0 ›
apply (subst add-num-frac, simp)
apply (subst add-num-frac, simp)
apply simp
apply (subst cmod-square )+
apply (simp add : ﬁeld-simps)
done
qed
ultimately
show ?P ′ 0 h (of-complex x ) ( of-complex y )
123
by simp
qed
next
ﬁx M u v w
assume 1 : unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc w ∈ unit-disc
assume 2 : ?P (moebius-pt M u ) ( moebius-pt M v ) ( moebius-pt M w )
show ?P u v w
using 1 2
by auto
next
ﬁx u v w
assume 1 : u∈ unit-disc v ∈ unit-disc w ∈ unit-disc
assume 2 : ?P (conjugate u ) ( conjugate v ) ( conjugate w )
show ?P u v w
using 1 2
by (auto simp add : conjugate-inj)
qed
thus ?thesis
using True
by simp
qed
end
