---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-007-points-on-h-line
section_title: "Points on h-line"
section_number: null
pages: 8-11
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Each h-line in the Poincaré model contains at least two diﬀerent points within the unit disc.
First we prove an auxiliary lemma.
lemma ex-is-poincare-line-points′:
assumes i12 : i1∈ circline-set H ∩ unit-circle-set
i2∈ circline-set H ∩ unit-circle-set
i1⁄= i2
assumes a: a∈ circline-set H a /∈ unit-circle-set
shows∃ b. b⁄= i1∧ b⁄= i2∧ b⁄= a∧ b⁄= inversion a ∧ b∈ circline-set H
proof−
have inversion a /∈ unit-circle-set
using ‹a /∈ unit-circle-set›
unfolding unit-circle-set-def circline-set-def
by (metis inversion-id-iﬀ-on-unit-circle inversion-involution mem-Collect-eq )
have a⁄= inversion a
using ‹a /∈ unit-circle-set› inversion-id-iﬀ-on-unit-circle[of a ]
unfolding unit-circle-set-def circline-set-def
by auto
have a⁄= i1 a ⁄= i2 inversion a ⁄= i1 inversion a ⁄= i2
using assms ‹inversion a /∈ unit-circle-set›
by auto
then obtain b where cr2 : cross-ratio b i1 a i2 = of-complex 2
using ‹i1⁄= i2 ›
using ex-cross-ratio[of i1 a i2 ]
by blast
have distinct-b: b⁄= i1 b ⁄= i2 b ⁄= a
using ‹i1⁄= i2 › ‹a⁄= i1 › ‹a⁄= i2 ›
using ex1-cross-ratio[of i1 a i2 ]
using cross-ratio-0[of i1 a i2 ] cross-ratio-1[of i1 a i2 ] cross-ratio-inf[of i1 i2 a ]
using cr2
by auto
hence b∈ circline-set H
using assms four-points-on-circline-iﬀ-cross-ratio-real[of b i1 a i2 ] cr2
using unique-circline-set[of i1 i2 a ]
by auto
8
moreover
have b⁄= inversion a
proof (rule ccontr )
assume∗:¬ ?thesis
have inversion i1 = i1 inversion i2 = i2
using i12
unfolding unit-circle-set-def
by auto
hence cross-ratio (inversion a ) i1 a i2 = cross-ratio a i1 (inversion a ) i2
using∗ cross-ratio-inversion[of i1 a i2 b ] ‹a⁄= i1 › ‹a⁄= i2 › ‹i1⁄= i2 › ‹b⁄= i1 ›
using four-points-on-circline-iﬀ-cross-ratio-real[of b i1 a i2 ]
using i12 distinct-b conjugate-id-iﬀ [of cross-ratio b i1 a i2 ]
using i12 a ‹b∈ circline-set H ›
by auto
hence cross-ratio (inversion a ) i1 a i2 ⁄= of-complex 2
using cross-ratio-commute-13[of inversion a i1 a i2 ]
using reciprocal-id-iﬀ
using of-complex-inj
by force
thus False
using∗ cr2
by simp
qed
ultimately
show ?thesis
using assms ‹b⁄= i1 › ‹b⁄= i2 › ‹b⁄= a›
by auto
qed
Now we can prove the statement.
lemma ex-is-poincare-line-points:
assumes is-poincare-line H
shows∃ u v. u∈ unit-disc∧ v∈ unit-disc∧ u⁄= v∧{ u, v}⊆ circline-set H
proof−
obtain u v w where∗: u⁄= v v ⁄= w u ⁄= w{u, v, w}⊆ circline-set H
using assms is-poincare-line-iﬀ [of H ]
using circline-type-neg-card-gt3[of H ]
by auto
have¬{ u, v, w}⊆ unit-circle-set
using unique-circline-set[of u v w ]∗
by (metis assms insert-subset not-is-poincare-line-unit-circle unit-circle-set-def )
hence H⁄= unit-circle
unfolding unit-circle-set-def
using∗
by auto
show ?thesis
proof (cases (u∈ unit-disc∧ v∈ unit-disc)∨
(u∈ unit-disc∧ w∈ unit-disc)∨
(v∈ unit-disc∧ w∈ unit-disc))
case True
thus ?thesis
using∗
by auto
next
case False
have∃ a b. a ⁄= b∧ a ⁄= inversion b ∧ a ∈ circline-set H ∧ b∈ circline-set H ∧ a /∈ unit-circle-set∧ b /∈
unit-circle-set
proof (cases (u∈ unit-circle-set∧ v∈ unit-circle-set)∨
(u∈ unit-circle-set∧ w∈ unit-circle-set)∨
(v∈ unit-circle-set∧ w∈ unit-circle-set))
9
case True
then obtain i1 i2 a where∗:
i1∈ unit-circle-set∩ circline-set H i2 ∈ unit-circle-set∩ circline-set H
a∈ circline-set H a /∈ unit-circle-set
i1⁄= i2 i1 ⁄= a i2 ⁄= a
using∗ ‹¬{ u, v, w}⊆ unit-circle-set›
by auto
then obtain b where b∈ circline-set H b ⁄= i1 b ⁄= i2 b ⁄= a b ⁄= inversion a
using ex-is-poincare-line-points′[of i1 H i2 a ]
by blast
hence b /∈ unit-circle-set
using∗ ‹H⁄= unit-circle› unique-circline-set[of i1 i2 b ]
unfolding unit-circle-set-def
by auto
thus ?thesis
using∗ ‹b∈ circline-set H › ‹b⁄= a› ‹b⁄= inversion a ›
by auto
next
case False
then obtain f g h where
∗: f ⁄= g f ∈ circline-set H f /∈ unit-circle-set
g∈ circline-set H g /∈ unit-circle-set
h∈ circline-set H h ⁄= f h ⁄= g
using∗
by auto
show ?thesis
proof (cases f = inversion g )
case False
thus ?thesis
using∗
by auto
next
case True
show ?thesis
proof (cases h ∈ unit-circle-set)
case False
thus ?thesis
using∗ ‹f = inversion g ›
by auto
next
case True
obtain m where cr2 : cross-ratio m h f g = of-complex 2
using ex-cross-ratio[of h f g ]∗ ‹f ⁄= g› ‹h⁄= f › ‹h⁄= g›
by auto
hence m⁄= h m ⁄= f m ⁄= g
using ‹h⁄= f › ‹h⁄= g› ‹f ⁄= g›
using ex1-cross-ratio[of h f g ]
using cross-ratio-0[of h f g ] cross-ratio-1[of h f g ] cross-ratio-inf[of h g f ]
using cr2
by auto
hence m∈ circline-set H
using four-points-on-circline-iﬀ-cross-ratio-real[of m h f g ] cr2
using ‹h⁄= f › ‹h⁄= g› ‹f ⁄= g›∗
using unique-circline-set[of h f g ]
by auto
show ?thesis
proof (cases m ∈ unit-circle-set)
case False
thus ?thesis
using ‹m⁄= f › ‹m⁄= g› ‹f = inversion g ›∗ ‹m∈ circline-set H ›
by auto
next
case True
10
then obtain n where n⁄= h n ⁄= m n ⁄= f n ⁄= inversion f n ∈ circline-set H
using ex-is-poincare-line-points′[of h H m f ]∗ ‹m∈ circline-set H › ‹h∈ unit-circle-set› ‹m⁄= h›
by auto
hence n /∈ unit-circle-set
using∗ ‹H⁄= unit-circle› unique-circline-set[of m n h ]
using ‹m⁄= h› ‹m∈ unit-circle-set› ‹h∈ unit-circle-set› ‹m∈ circline-set H ›
unfolding unit-circle-set-def
by auto
thus ?thesis
using∗ ‹n∈ circline-set H › ‹n⁄= f › ‹n⁄= inversion f ›
by auto
qed
qed
qed
qed
then obtain a b where ab: a⁄= b a ⁄= inversion b a ∈ circline-set H b ∈ circline-set H a /∈ unit-circle-set b /∈
unit-circle-set
by blast
have∀ x. x ∈ circline-set H ∧ x /∈ unit-circle-set−→ (∃ x ′. x ′∈ circline-set H ∩ unit-disc∧ (x ′ = x ∨ x ′ =
inversion x ))
proof safe
ﬁx x
assume x: x∈ circline-set H x /∈ unit-circle-set
show∃ x ′. x ′∈ circline-set H ∩ unit-disc∧ (x ′ = x∨ x ′ = inversion x )
proof (cases x ∈ unit-disc)
case True
thus ?thesis
using x
by auto
next
case False
hence x∈ unit-disc-compl
using x in-on-out-univ [of ounit-circle ]
unfolding unit-circle-set-def unit-disc-def unit-disc-compl-def
by auto
hence inversion x ∈ unit-disc
using inversion-unit-disc-compl
by blast
thus ?thesis
using is-poincare-line-inverse-point[OF assms, of x ] x
by auto
qed
qed
then obtain a ′ b ′ where
∗: a ′∈ circline-set H a ′∈ unit-disc b ′∈ circline-set H b ′∈ unit-disc and
∗∗: a ′ = a∨ a ′ = inversion a b ′ = b∨ b ′ = inversion b
using ab
by blast
have a ′⁄= b ′
using ‹a⁄= b› ‹a⁄= inversion b ›∗∗∗
by (metis inversion-involution )
thus ?thesis
using∗
by auto
qed
qed
