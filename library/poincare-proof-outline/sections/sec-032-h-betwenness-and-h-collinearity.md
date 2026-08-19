---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-032-h-betwenness-and-h-collinearity
section_title: "H-betwenness and h-collinearity"
section_number: null
pages: 78-79
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Three points can be in an h-between relation only when they are h-collinear.
lemma poincare-between-poincare-collinear[simp]:
assumes in-disc: u∈ unit-disc v ∈ unit-disc w ∈ unit-disc
assumes betw: poincare-between u v w
shows poincare-collinear{u, v, w}
proof (cases u = v∨ v = w)
case True
thus ?thesis
using assms
by auto
next
case False
hence distinct: distinct [u, v, w, inversion v ]
using in-disc inversion-noteq-unit-disc [of v v ] inversion-noteq-unit-disc[of v u ] inversion-noteq-unit-disc[of v w ]
using betw poincare-between-sandwich[of w v ]
by (auto simp add : poincare-between-def Let-def)
then obtain H where∗:{u, v, w, inversion v}⊆ circline-set H
using assms
unfolding poincare-between-def
using four-points-on-circline-iﬀ-cross-ratio-real[of u v w inversion v ]
by auto
78
hence H = poincare-line u v
using assms distinct
using unique-circline-set[of u v inversion v ]
using poincare-line[of u v ] poincare-line-inversion[of u v ]
unfolding circline-set-def
by auto
thus ?thesis
using∗ assms False
unfolding poincare-collinear-def
by (rule-tac x =poincare-line u v in exI ) simp
qed
lemma poincare-between-poincare-line-uvz:
assumes u⁄= v and u∈ unit-disc and v∈ unit-disc and
z∈ unit-disc and poincare-between u v z
shows z∈ circline-set (poincare-line u v )
using assms
using poincare-between-poincare-collinear[of u v z ]
using unique-poincare-line[OF assms (1−3 )]
unfolding poincare-collinear-def
by auto
lemma poincare-between-poincare-line-uzv:
assumes u⁄= v and u∈ unit-disc and v∈ unit-disc and
z∈ unit-disc poincare-between u z v
shows z∈ circline-set (poincare-line u v )
using assms
using poincare-between-poincare-collinear[of u z v ]
using unique-poincare-line[OF assms (1−3 )]
unfolding poincare-collinear-def
by auto
