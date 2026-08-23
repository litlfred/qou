---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-035-some-properties-of-betweenness
section_title: "Some properties of betweenness"
section_number: null
pages: 87-89
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma poincare-between-transitivity:
assumes a∈ unit-disc and x∈ unit-disc and b∈ unit-disc and y∈ unit-disc and
poincare-between a x b and poincare-between a b y
shows poincare-between x b y
proof (cases a = b)
case True
thus ?thesis
using assms
using poincare-between-sandwich by blast
next
case False
87
have∀ x.∀ y. poincare-between a x b ∧ poincare-between a b y ∧ x∈ unit-disc
∧ y∈ unit-disc−→ poincare-between x b y (is ?P a b )
proof (rule wlog-positive-x-axis [where P=?P])
show a∈ unit-disc
using assms by simp
next
show b∈ unit-disc
using assms by simp
next
show a⁄= b
using False by simp
next
ﬁx M u v
assume∗: unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc u ⁄= v
∀ x y. poincare-between (moebius-pt M u ) x (moebius-pt M v )∧
poincare-between (moebius-pt M u ) ( moebius-pt M v ) y∧
x∈ unit-disc∧ y∈ unit-disc−→
poincare-between x (moebius-pt M v ) y
show∀ x y. poincare-between u x v ∧ poincare-between u v y ∧ x∈ unit-disc∧ y∈ unit-disc
−→ poincare-between x v y
proof safe
ﬁx x y
assume poincare-between u x v poincare-between u v y x ∈ unit-disc y ∈ unit-disc
have poincare-between (moebius-pt M u ) ( moebius-pt M x ) ( moebius-pt M v )
using ‹poincare-between u x v › ‹unit-disc-ﬁx M › ‹x∈ unit-disc› ‹u∈ unit-disc› ‹v∈ unit-disc›
by simp
moreover
have poincare-between (moebius-pt M u ) ( moebius-pt M v ) ( moebius-pt M y )
using ‹poincare-between u v y › ‹unit-disc-ﬁx M › ‹y∈ unit-disc› ‹u∈ unit-disc› ‹v∈ unit-disc›
by simp
moreover
have (moebius-pt M x )∈ unit-disc
using ‹unit-disc-ﬁx M › ‹x∈ unit-disc› by simp
moreover
have (moebius-pt M y )∈ unit-disc
using ‹unit-disc-ﬁx M › ‹y∈ unit-disc› by simp
ultimately
have poincare-between (moebius-pt M x ) ( moebius-pt M v ) ( moebius-pt M y )
using∗ by blast
thus poincare-between x v y
using ‹y∈ unit-disc›∗ ‹x∈ unit-disc› by simp
qed
next
ﬁx x
assume xx: is-real x 0 < Re x Re x < 1
hence of-complex x ∈ unit-disc
using cmod-eq-Re by auto
hence of-complex x ⁄=∞h
by simp
have of-complex x ⁄= 0 h
using xx by auto
have of-complex x ∈ circline-set x-axis
using xx by simp
show∀ m n. poincare-between 0h m (of-complex x )∧ poincare-between 0h (of-complex x ) n∧
m∈ unit-disc∧ n∈ unit-disc−→ poincare-between m (of-complex x ) n
proof safe
ﬁx m n
assume∗∗: poincare-between 0h m (of-complex x ) poincare-between 0h (of-complex x ) n
m∈ unit-disc n ∈ unit-disc
show poincare-between m (of-complex x ) n
proof (cases m = 0 h)
case True
thus ?thesis
using∗∗ by auto
next
88
case False
hence m∈ circline-set x-axis
using poincare-between-poincare-line-uzv[of 0 h of-complex x m ]
using poincare-line-0-real-is-x-axis[of of-complex x ]
using ‹of-complex x ∈ unit-disc› ‹of-complex x ⁄=∞h› ‹of-complex x ⁄= 0 h›
using ‹of-complex x ∈ circline-set x-axis › ‹m∈ unit-disc›∗∗(1 )
by simp
then obtain m ′ where m = of-complex m ′ is-real m ′
using inf-or-of-complex[of m ] ‹m∈ unit-disc›
unfolding circline-set-x-axis
by auto
hence Re m ′≤ Re x
using ‹poincare-between 0h m (of-complex x )› xx ‹of-complex x ⁄= 0 h›
using False∗∗ ‹of-complex x ∈ unit-disc›
using cmod-Re-le-iﬀ poincare-between-0uv by auto
have n⁄= 0 h
using∗∗(2, 4 ) ‹of-complex x ⁄= 0 h› ‹of-complex x ∈ unit-disc›
using poincare-between-sandwich by fastforce
have n∈ circline-set x-axis
using poincare-between-poincare-line-uvz[of 0 h of-complex x n ]
using poincare-line-0-real-is-x-axis[of of-complex x ]
using ‹of-complex x ∈ unit-disc› ‹of-complex x ⁄=∞h› ‹of-complex x ⁄= 0 h›
using ‹of-complex x ∈ circline-set x-axis › ‹n∈ unit-disc›∗∗(2 )
by simp
then obtain n ′ where n = of-complex n ′ is-real n ′
using inf-or-of-complex[of n ] ‹n∈ unit-disc›
unfolding circline-set-x-axis
by auto
hence Re x ≤ Re n ′
using ‹poincare-between 0h (of-complex x ) n› xx ‹of-complex x ⁄= 0 h›
using False∗∗ ‹of-complex x ∈ unit-disc› ‹n⁄= 0 h›
using cmod-Re-le-iﬀ poincare-between-0uv
by (metis Re-complex-of-real arg-0-iﬀ rcis-cmod-Arg rcis-zero-arg to-complex-of-complex )
have poincare-between (of-complex m ′) ( of-complex x ) ( of-complex n ′)
using ‹Re x ≤ Re n ′› ‹Re m ′≤ Re x ›
using poincare-between-x-axis-uvw[of Re m ′ Re x Re n ′]
using ‹is-real n ′› ‹is-real m ′› ‹n∈ unit-disc› ‹n = of-complex n ′›
using xx ‹m = of-complex m ′› ‹m∈ unit-disc›
by (smt complex-of-real-Re norm-of-real poincare-between-def unit-disc-iﬀ-cmod-lt-1 )
thus ?thesis
using ‹n = of-complex n ′› ‹m = of-complex m ′›
by auto
qed
qed
qed
thus ?thesis
using assms
by blast
qed
