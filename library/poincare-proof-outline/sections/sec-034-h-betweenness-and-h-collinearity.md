---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-034-h-betweenness-and-h-collinearity
section_title: "H-betweenness and h-collinearity"
section_number: null
pages: 86-87
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
For three h-collinear points at least one of the three possible h-betweeness relations must hold.
lemma poincare-collinear3-between:
assumes u∈ unit-disc and v∈ unit-disc and w∈ unit-disc
assumes poincare-collinear{u, v, w}
shows poincare-between u v w ∨ poincare-between u w v ∨ poincare-between v u w (is ?P ′ u v w )
proof (cases u =v)
case True
thus ?thesis
using assms
by auto
next
case False
have∀ w. w∈ unit-disc∧ poincare-collinear{u, v, w}−→ ?P ′ u v w (is ?P u v )
proof (rule wlog-positive-x-axis [where P=?P])
ﬁx x
assume x: is-real x 0 < Re x Re x < 1
hence x⁄= 0
using complex.expand[of x 0 ]
by auto
hence∗: poincare-line 0 h (of-complex x ) = x-axis
using x poincare-line-0-real-is-x-axis[of of-complex x ]
unfolding circline-set-x-axis
by auto
have of-complex x ∈ unit-disc
using x
by (auto simp add : cmod-eq-Re)
have of-complex x ⁄= 0 h
using ‹x⁄= 0 ›
by auto
show ?P 0 h (of-complex x )
proof safe
ﬁx w
assume w∈ unit-disc
assume poincare-collinear{0 h, of-complex x, w}
hence w∈ circline-set x-axis
using∗ unique-poincare-line[of 0 h of-complex x ] ‹of-complex x ∈ unit-disc› ‹x⁄= 0 › ‹of-complex x ⁄= 0 h›
unfolding poincare-collinear-def
by auto
then obtain w ′ where w ′: w = of-complex w ′ is-real w ′
using ‹w∈ unit-disc›
using inf-or-of-complex[of w ]
unfolding circline-set-x-axis
by auto
hence−1 < Re w ′ Re w ′< 1
using ‹w∈ unit-disc›
by (auto simp add : cmod-eq-Re)
assume 1 :¬ poincare-between (of-complex x ) 0 h w
hence w⁄= 0 h w ′⁄= 0
using w ′
86
unfolding poincare-between-def
by auto
hence Re w ′⁄= 0
using w ′ complex.expand[of w ′ 0 ]
by auto
have Re w ′≥ 0
using 1 poincare-between-x-axis-u0v[of x w ′] ‹Re x > 0 › ‹is-real x › ‹x⁄= 0 › ‹w ′⁄= 0 › w ′
using mult-pos-neg
by force
moreover
assume¬ poincare-between 0h (of-complex x ) w
hence Re w ′< Re x
using poincare-between-x-axis-0uv[of Re x Re w ′]
using w ′ x ‹−1 < Re w ′› ‹Re w ′< 1 › ‹Re w ′⁄= 0 ›
by auto
ultimately
show poincare-between 0h w (of-complex x )
using poincare-between-x-axis-0uv[of Re w ′ Re x ]
using w ′ x ‹−1 < Re w ′› ‹Re w ′< 1 › ‹Re w ′⁄= 0 ›
by auto
qed
next
show u∈ unit-disc v ∈ unit-disc u ⁄= v
by fact+
next
ﬁx M u v
assume 1 : unit-disc-ﬁx M u ∈ unit-disc v ∈ unit-disc u ⁄= v
let ?Mu = moebius-pt M u and ?Mv = moebius-pt M v
assume 2 : ?P ?Mu ?Mv
show ?P u v
proof safe
ﬁx w
assume w∈ unit-disc poincare-collinear{u, v, w}¬ poincare-between u v w ¬ poincare-between v u w
thus poincare-between u w v
using 1 2 [rule-format, of moebius-pt M w ]
by simp
qed
qed
thus ?thesis
using assms
by simp
qed
lemma poincare-collinear3-iﬀ:
assumes u∈ unit-disc v ∈ unit-disc w ∈ unit-disc
shows poincare-collinear{u, v, w}←→ poincare-between u v w ∨ poincare-between v u w ∨ poincare-between v w u
using assms
by (metis poincare-collinear3-between insert-commute poincare-between-poincare-collinear poincare-between-rev)
