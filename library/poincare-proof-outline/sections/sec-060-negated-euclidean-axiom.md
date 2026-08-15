---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-060-negated-euclidean-axiom
section_title: "Negated Euclidean axiom"
section_number: null
pages: 143-150
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma negated-euclidean-axiom-aux:
assumes on-circline H (of-complex (1/2 + i/2 )) and is-poincare-line H
assumes intersects-x-axis-positive H
shows¬ intersects-y-axis-positive H
using assms
proof (transfer, transfer)
ﬁx H
assume hh: hermitean H ∧ H⁄= mat-zero is-poincare-line-cmat H
obtain A B C D where H = ( A, B, C, D)
by (cases H, auto)
hence∗: is-real A H = ( A, B, cnj B, A) ( cmod B )2 > (cmod A )2
using hermitean-elems[of A B C D ] hh
by auto
assume intersects-x-axis-positive-cmat H
hence Re A⁄= 0 Re B / Re A <− 1
using∗
by auto
assume on-circline-cmat-cvec H (of-complex-cvec (1 / 2 + i / 2 ))
hence 6∗A + 4∗Re B + 4∗Im B = 0
using∗
unfolding of-real-mult
apply (subst Re-express-cnj [of B ])
143
apply (subst Im-express-cnj [of B ])
apply (simp add : vec-cnj-def )
apply (simp add : ﬁeld-simps)
done
hence Re (6∗A + 4∗Re B + 4∗Im B ) = 0
by simp
hence 3∗Re A + 2∗Re B + 2∗Im B = 0
using ‹is-real A›
by simp
hence 3/2 + Re B/Re A + Im B/Re A = 0
using ‹Re A⁄= 0 ›
by (simp add : ﬁeld-simps)
hence−Im B/Re A− 3/2 <−1
using ‹Re B / Re A <−1 ›
by simp
hence Im B/Re A >−1/2
by (simp add : ﬁeld-simps)
thus¬ intersects-y-axis-positive-cmat H
using∗
by simp
qed
lemma negated-euclidean-axiom:
shows∃ a b c d t .
a∈ unit-disc∧ b∈ unit-disc∧ c∈ unit-disc∧ d∈ unit-disc∧ t∈ unit-disc∧
poincare-between a d t ∧ poincare-between b d c ∧ a⁄= d∧
(∀ x y. x∈ unit-disc∧ y∈ unit-disc∧
poincare-between a b x ∧ poincare-between x t y −→¬ poincare-between a c y )
proof−
let ?a = 0 h
let ?b = of-complex (1/2 )
let ?c = of-complex (i/2 )
let ?dl = ( 5− sqrt 17 ) / 4
let ?d = of-complex (?dl + i∗?dl )
let ?t = of-complex (1/2 + i/2 )
have ?dl⁄= 0
proof−
have (sqrt 17 )2⁄= 5 2
by simp
hence sqrt 17 ⁄= 5
by force
thus ?thesis
by simp
qed
have ?d⁄= ?a
proof (rule ccontr )
assume¬ ?thesis
hence ?dl + i∗?dl = 0
by simp
hence Re (?dl + i∗?dl ) = 0
by simp
thus False
using ‹?dl⁄= 0 ›
by simp
qed
have ?dl > 0
proof−
have (sqrt 17 )2 < 5 2
by (simp add : power2-eq-square)
hence sqrt 17 < 5
by (rule power2-less-imp-less, simp)
144
thus ?thesis
by simp
qed
have ?a⁄= ?b
by (metis divide-eq-0-iﬀ of-complex-zero-iﬀ zero-neq-numeral zero-neq-one )
have ?a⁄= ?c
by (metis complex-i-not-zero divide-eq-0-iﬀ of-complex-zero-iﬀ zero-neq-numeral )
show ?thesis
proof (rule-tac x =?a in exI, rule-tac x =?b in exI, rule-tac x =?c in exI, rule-tac x =?d in exI, rule-tac x =?t in exI,
safe)
show ?a∈ unit-disc ?b ∈ unit-disc ?c ∈ unit-disc ?t ∈ unit-disc
by (auto simp add : cmod-def power2-eq-square)
have cmod-d: cmod (?dl + i∗?dl ) = ?dl∗ sqrt 2
using ‹?dl > 0 ›
unfolding cmod-def
by (simp add : real-sqrt-mult)
show ?d∈ unit-disc
proof−
have ?dl < 1 / sqrt 2
proof−
have 17 2 < (5∗ sqrt 17 )2
by (simp add : ﬁeld-simps)
hence 17 < 5∗ sqrt 17
by (rule power2-less-imp-less, simp)
hence ?dl 2 < (1 / sqrt 2 )2
by (simp add : power2-eq-square ﬁeld-simps)
thus ?dl < 1 / sqrt 2
by (rule power2-less-imp-less, simp)
qed
thus ?thesis
using cmod-d
by (simp add : ﬁeld-simps)
qed
have cmod-d: 1− (cmod (to-complex ?d ))2 = (−17 + 5∗sqrt 17 ) / 4 (is - = ?cmod-d)
apply (simp only : to-complex-of-complex)
apply (subst cmod-d )
apply (simp add : power-mult-distrib)
apply (simp add : power2-eq-square ﬁeld-simps)
done
have cmod-d-c: ( cmod (to-complex ?d − to-complex ?c ))2 = ( 17− 4∗sqrt 17 ) / 4 (is - = ?cmod-dc)
unfolding cmod-square
by (simp add : ﬁeld-simps)
have cmod-c: 1− (cmod (to-complex ?c ))2 = 3/4 (is - = ?cmod-c)
by (simp add : power2-eq-square)
have xx: ⋀ x::real. x + x = 2∗x
by simp
have cmod ((to-complex ?b )− (to-complex ?d )) = cmod ((to-complex ?d )− (to-complex ?c ))
by (simp add : cmod-def power2-eq-square ﬁeld-simps )
moreover
have cmod (to-complex ?b ) = cmod (to-complex ?c )
by simp
ultimately
have∗: poincare-distance-formula′ (to-complex ?b ) ( to-complex ?d ) =
poincare-distance-formula′ (to-complex ?d ) ( to-complex ?c )
145
unfolding poincare-distance-formula′-def
by simp
have∗∗: poincare-distance-formula′ (to-complex ?d ) ( to-complex ?c ) = ( sqrt 17 ) / 3
unfolding poincare-distance-formula′-def
proof (subst cmod-d, subst cmod-c, subst cmod-d-c )
have (sqrt 17 ∗ 15 )2⁄= 51 2
by simp
hence sqrt 17 ∗ 15⁄= 51
by force
hence sqrt 17 ∗ 15− 51⁄= 0
by simp
have (5∗ sqrt 17 )2⁄= 17 2
by simp
hence 5∗ sqrt 17 ⁄= 17
by force
hence ?cmod-d∗ ?cmod-c⁄= 0
by simp
hence 1 + 2∗ (?cmod-dc/ (?cmod-d∗ ?cmod-c)) = ( ?cmod-d∗ ?cmod-c + 2∗ ?cmod-dc)/ (?cmod-d∗ ?cmod-c)
using add-frac-num[of ?cmod-d ∗ ?cmod-c 2 ∗ ?cmod-dc 1 ]
by (simp add : ﬁeld-simps)
also have ... = ( 64∗ (85− sqrt 17 ∗ 17 )) / (64∗ (sqrt 17 ∗ 15− 51 ))
by (simp add : ﬁeld-simps)
also have ... = ( 85− sqrt 17 ∗ 17 ) / (sqrt 17 ∗ 15− 51 )
by (rule mult-divide-mult-cancel-left, simp)
also have ... = sqrt 17 / 3
by (subst frac-eq-eq, fact, simp, simp add : ﬁeld-simps)
ﬁnally
show 1 + 2∗ (?cmod-dc / (?cmod-d∗ ?cmod-c)) = sqrt 17 / 3
.
qed
have sqrt 17 ≥ 3
proof−
have (sqrt 17 )2≥ 3 2
by simp
thus ?thesis
by (rule power2-le-imp-le, simp)
qed
thus poincare-between ?b ?d ?c
unfolding poincare-between-sum-distances[OF ‹?b∈ unit-disc› ‹?d∈ unit-disc› ‹?c∈ unit-disc›]
unfolding poincare-distance-formula[OF ‹?b∈ unit-disc› ‹?d∈ unit-disc›]
unfolding poincare-distance-formula[OF ‹?d∈ unit-disc› ‹?c∈ unit-disc›]
unfolding poincare-distance-formula[OF ‹?b∈ unit-disc› ‹?c∈ unit-disc›]
unfolding poincare-distance-formula-def
apply (subst∗, subst xx, subst∗∗, subst arcosh-double )
apply (simp-all add : cmod-def power2-eq-square)
done
show poincare-between ?a ?d ?t
proof (subst poincare-between-0uv[OF ‹?d∈ unit-disc› ‹?t∈ unit-disc› ‹?d⁄= ?a›])
show ?t⁄= 0 h
proof (rule ccontr )
assume¬ ?thesis
hence 1/2 + i/2 = 0
by simp
hence Re (1/2 + i/2 ) = 0
by simp
thus False
by simp
qed
next
have 19 2≤ (5∗ sqrt 17 )2
by simp
hence 19≤ 5∗ sqrt 17
146
by (rule power2-le-imp-le, simp)
hence cmod (to-complex ?d )≤ cmod (to-complex ?t )
by (simp add : Let-def cmod-def power2-eq-square ﬁeld-simps )
moreover
have Arg (to-complex ?d ) = Arg (to-complex ?t )
proof−
have 1 : to-complex ?d = (( 5− sqrt 17 ) / 4 )∗ (1 + i)
by (simp add : ﬁeld-simps)
have 2 : to-complex ?t = ( cor (1/2 ))∗ (1 + i)
by (simp add : ﬁeld-simps)
have (sqrt 17 )2 < 5 2
by simp
hence sqrt 17 < 5
by (rule power2-less-imp-less, simp)
hence 3 : ( 5− sqrt 17 ) / 4 > 0
by simp
have 4 : ( 1 ::real) / 2 > 0
by simp
show ?thesis
apply (subst 1, subst 2 )
apply (subst arg-mult-real-positive[OF 3 ])
apply (subst arg-mult-real-positive[OF 4 ])
by simp
qed
ultimately
show let d ′ = to-complex ?d ; t ′ = to-complex ?t in Arg d ′ = Arg t ′∧ cmod d ′≤ cmod t ′
by simp
qed
show ?a = ?d =⇒ False
using ‹?d⁄= ?a›
by simp
ﬁx x y
assume x∈ unit-disc y ∈ unit-disc
assume abx: poincare-between ?a ?b x
hence x∈ circline-set x-axis
using poincare-between-poincare-line-uvz[of ?a ?b x ] ‹x∈ unit-disc› ‹?a⁄= ?b›
using poincare-line-0-real-is-x-axis[of ?b ]
by (auto simp add : circline-set-x-axis)
have x⁄= 0 h
using abx poincare-between-sandwich[of ?a ?b ] ‹?a⁄= ?b›
by auto
have x∈ positive-x-axis
using ‹x∈ circline-set x-axis › ‹x⁄= 0 h› ‹x∈ unit-disc›
using abx poincare-between-x-axis-0uv[of 1/2 Re (to-complex x )]
unfolding circline-set-x-axis positive-x-axis-def
by (auto simp add : cmod-eq-Re abs-less-iﬀ complex-eq-if-Re-eq )
assume acy: poincare-between ?a ?c y
hence y∈ circline-set y-axis
using poincare-between-poincare-line-uvz[of ?a ?c y ] ‹y∈ unit-disc› ‹?a⁄= ?c›
using poincare-line-0-imag-is-y-axis[of ?c ]
by (auto simp add : circline-set-y-axis)
have y⁄= 0 h
using acy poincare-between-sandwich[of ?a ?c ] ‹?a⁄= ?c›
by auto
147
have y∈ positive-y-axis
proof−
have ⋀x. [ [x⁄= 0 ; poincare-between 0h (of-complex (i / 2 )) ( of-complex x ); is-imag x ;− 1 < Im x ] ] =⇒ 0 < Im x
by (smt add.left-neutral complex.expand divide-complex-def complex-eq divide-less-0-1-iﬀ divide-less-eq-1-pos imagi-
nary-unit.simps(1 ) mult.left-neutral of-real-1 of-real-add of-real-divide of-real-eq-0-iﬀ one-add-one poincare-between-y-axis-0uv
zero-complex.simps(1 ) zero-complex.simps(2 ) zero-less-divide-1-iﬀ )
thus ?thesis
using ‹y∈ circline-set y-axis › ‹y⁄= 0 h› ‹y∈ unit-disc›
using acy
unfolding circline-set-y-axis positive-y-axis-def
by (auto simp add : cmod-eq-Im abs-less-iﬀ )
qed
have x⁄= y
using ‹x∈ positive-x-axis› ‹y∈ positive-y-axis›
unfolding positive-x-axis-def positive-y-axis-def circline-set-x-axis circline-set-y-axis
by auto
assume xty: poincare-between x ?t y
let ?xy = poincare-line x y
have ?t∈ circline-set ?xy
using xty poincare-between-poincare-line-uzv[OF ‹x⁄= y› ‹x∈ unit-disc› ‹y∈ unit-disc› ‹?t∈ unit-disc›]
by simp
moreover
have ?xy⁄= x-axis
using poincare-line-circline-set[OF ‹x⁄= y›] ‹y∈ positive-y-axis›
by (auto simp add : circline-set-x-axis positive-y-axis-def )
hence intersects-x-axis-positive ?xy
using intersects-x-axis-positive-iﬀ [of ?xy ] ‹x⁄= y› ‹x∈ unit-disc› ‹x∈ positive-x-axis›
by auto
moreover
have ?xy⁄= y-axis
using poincare-line-circline-set[OF ‹x⁄= y›] ‹x∈ positive-x-axis›
by (auto simp add : circline-set-y-axis positive-x-axis-def )
hence intersects-y-axis-positive ?xy
using intersects-y-axis-positive-iﬀ [of ?xy ] ‹x⁄= y› ‹y∈ unit-disc› ‹y∈ positive-y-axis›
by auto
ultimately
show False
using negated-euclidean-axiom-aux[of ?xy ] ‹x⁄= y›
unfolding circline-set-def
by auto
qed
qed
Alternate form of the Euclidean axiom – this one is much easier to prove
lemma negated-euclidean-axiom′:
shows∃ a b c .
a∈ unit-disc∧ b∈ unit-disc∧ c∈ unit-disc∧¬ (poincare-collinear{a, b, c}) ∧
¬(∃ x. x∈ unit-disc∧
poincare-distance a x = poincare-distance b x ∧
poincare-distance a x = poincare-distance c x )
proof−
let ?a = of-complex (i/2 )
let ?b = of-complex (−i/2 )
let ?c = of-complex (1/5 )
have (i/2 )⁄= (−i/2 )
148
by simp
hence ?a⁄= ?b
by (metis to-complex-of-complex )
have (i/2 )⁄= ( 1/5 )
by simp
hence ?a⁄= ?c
by (metis to-complex-of-complex )
have (−i/2 )⁄= ( 1/5 )
by (simp add : minus-equation-iﬀ )
hence ?b⁄= ?c
by (metis to-complex-of-complex )
have ?a∈ unit-disc ?b ∈ unit-disc ?c ∈ unit-disc
by auto
moreover
have¬(poincare-collinear{?a, ?b, ?c})
unfolding poincare-collinear-def
proof (rule ccontr )
assume ¬ (∄ p. is-poincare-line p∧{ ?a, ?b, ?c}⊆ circline-set p )
then obtain p where is-poincare-line p∧{ ?a, ?b, ?c}⊆ circline-set p
by auto
let ?ab = poincare-line ?a ?b
have p = ?ab
using ‹is-poincare-line p∧{ ?a, ?b, ?c}⊆ circline-set p ›
using unique-poincare-line[of ?a ?b ] ‹?a⁄= ?b› ‹?a∈ unit-disc› ‹?b∈ unit-disc›
by auto
have ?c /∈ circline-set ?ab
proof (rule ccontr )
assume¬ ?c /∈ circline-set ?ab
have poincare-between ?a 0 h ?b
unfolding poincare-between-def
using cross-ratio-0inf by auto
hence 0 h∈ circline-set ?ab
using ‹?a⁄= ?b› ‹?a∈ unit-disc› ‹?b∈ unit-disc›
using poincare-between-poincare-line-uzv zero-in-unit-disc
by blast
hence ?ab = poincare-line 0 h ?a
using unique-poincare-line[of ?a ?b ] ‹?a⁄= ?b› ‹?a∈ unit-disc› ‹?b∈ unit-disc›
using ‹is-poincare-line p∧{ ?a, ?b, ?c}⊆ circline-set p ›
using ‹p = ?ab› poincare-line-circline-set(1 ) unique-poincare-line
by (metis add.inverse-neutral divide-minus-left of-complex-zero-iﬀ zero-in-unit-disc )
hence (i/2 )∗ cnj(1/5 ) = cnj(i/2 )∗ (1/5 )
using poincare-collinear-zero-iﬀ[of (i/2 ) ( 1/5 )]
using ‹?a⁄= ?c› ‹¬ ?c /∈ circline-set ?ab › ‹?a∈ unit-disc› ‹?c∈ unit-disc› ‹p = ?ab›
using ‹0 h∈ circline-set ?ab › ‹is-poincare-line p∧{ ?a, ?b, ?c}⊆ circline-set p ›
using poincare-collinear-def by auto
thus False
by simp
qed
thus False
using ‹p = ?ab› ‹is-poincare-line p∧{ ?a, ?b, ?c}⊆ circline-set p ›
by auto
qed
moreover
have¬(∃ x. x∈ unit-disc∧
poincare-distance ?a x = poincare-distance ?b x ∧
poincare-distance ?a x = poincare-distance ?c x )
proof (rule ccontr )
assume¬ ?thesis
then obtain x where x∈ unit-disc poincare-distance ?a x = poincare-distance ?b x
poincare-distance ?a x = poincare-distance ?c x
by blast
let ?x = to-complex x
149
have poincare-distance-formula′ (i/2 ) ?x = poincare-distance-formula′ (−i/2 ) ?x
using ‹poincare-distance ?a x = poincare-distance ?b x ›
using ‹x∈ unit-disc› ‹?a∈ unit-disc› ‹?b∈ unit-disc›
by (metis cosh-dist to-complex-of-complex )
hence (cmod (i / 2− ?x))2 = ( cmod (− i / 2− ?x))2
unfolding poincare-distance-formula′-def
apply (simp add :ﬁeld-simps)
using ‹x∈ unit-disc› unit-disc-cmod-square-lt-1 by fastforce
hence Im ?x = 0
unfolding cmod-def
by (simp add : power2-eq-iﬀ )
have 1− (Re ?x )2⁄= 0
using ‹x∈ unit-disc› unit-disc-cmod-square-lt-1
using cmod-power2 by force
hence 24− 24∗ (Re ?x )2⁄= 0
by simp
have poincare-distance-formula′ (i/2 ) ?x = poincare-distance-formula′ (1/5 ) ?x
using ‹poincare-distance ?a x = poincare-distance ?c x ›
using ‹x∈ unit-disc› ‹?a∈ unit-disc› ‹?c∈ unit-disc›
by (metis cosh-dist to-complex-of-complex )
hence (2 + 8∗ (Re ?x )2) /(3− 3∗ (Re ?x )2) = 2∗ (1− Re ?x ∗ 5 )2 / (24− 24∗ (Re ?x )2) ( is ?lhs = ?rhs)
unfolding poincare-distance-formula′-def
apply (simp add :ﬁeld-simps)
unfolding cmod-def
using ‹Im ?x = 0 ›
by (simp add :ﬁeld-simps)
hence∗: ?lhs∗ (24− 24∗ (Re ?x )2) = ?rhs∗ (24− 24∗ (Re ?x )2)
using ‹(24− 24∗ (Re ?x )2)⁄= 0 ›
by simp
have ?lhs∗ (24− 24∗ (Re ?x )2) = ( 2 + 8∗ (Re ?x )2)∗ 8
using ‹(24− 24∗ (Re ?x )2)⁄= 0 › ‹1− (Re ?x )2⁄= 0 ›
by (simp add :ﬁeld-simps)
have ?rhs∗ (24− 24∗ (Re ?x )2) = 2∗ (1− Re ?x ∗ 5 )2
using ‹(24− 24∗ (Re ?x )2)⁄= 0 › ‹1− (Re ?x )2⁄= 0 ›
by (simp add :ﬁeld-simps)
hence (2 + 8∗ (Re ?x )2)∗ 8 = 2∗ (1− Re ?x ∗ 5 )2
using∗ ‹?lhs∗ (24− 24∗ (Re ?x )2) = ( 2 + 8∗ (Re ?x )2)∗ 8 ›
by simp
hence 7∗ (Re ?x )2 + 10∗ (Re ?x ) + 7 = 0
by (simp add :ﬁeld-simps comm-ring-1-class.power2-diﬀ )
thus False
using discriminant-iﬀ [of 7 Re (to-complex x ) 10 7 ] discrim-def [of 7 10 7 ]
by auto
qed
ultimately show ?thesis
apply (rule-tac x =?a in exI )
apply (rule-tac x =?b in exI )
apply (rule-tac x =?c in exI )
by auto
qed
