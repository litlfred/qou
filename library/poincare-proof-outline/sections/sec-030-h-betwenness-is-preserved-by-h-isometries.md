---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-030-h-betwenness-is-preserved-by-h-isometries
section_title: "H-betwenness is preserved by h-isometries"
section_number: null
pages: 77-78
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Since they preserve cross-ratio and inversion, h-isometries (unit disc preserving Möbius transformations and
conjugation) preserve h-betweeness.
lemma unit-disc-ﬁx-moebius-preserve-poincare-between[simp]:
assumes unit-disc-ﬁx M and u∈ unit-disc and v∈ unit-disc and w∈ unit-disc
shows poincare-between (moebius-pt M u ) ( moebius-pt M v ) ( moebius-pt M w )←→
poincare-between u v w
proof (cases u = v∨ v = w)
case True
thus ?thesis
using assms
unfolding poincare-between-def
by auto
next
case False
moreover
hence moebius-pt M u ⁄= moebius-pt M v ∧ moebius-pt M v ⁄= moebius-pt M w
by auto
moreover
have v⁄= inversion v w ⁄= inversion v
using inversion-noteq-unit-disc[of v w ]
using inversion-noteq-unit-disc[of v v ]
using ‹v∈ unit-disc› ‹w∈ unit-disc›
by auto
ultimately
show ?thesis
using assms
using unit-circle-ﬁx-moebius-pt-inversion[of M v , symmetric]
unfolding poincare-between-def
by (simp del : unit-circle-ﬁx-moebius-pt-inversion)
qed
lemma conjugate-preserve-poincare-between[simp]:
assumes u∈ unit-disc and v∈ unit-disc and w∈ unit-disc
shows poincare-between (conjugate u ) ( conjugate v ) ( conjugate w )←→
poincare-between u v w
proof (cases u = v∨ v = w)
case True
thus ?thesis
using assms
unfolding poincare-between-def
by auto
next
case False
moreover
hence conjugate u ⁄= conjugate v ∧ conjugate v ⁄= conjugate w
using conjugate-inj by blast
moreover
have v⁄= inversion v w ⁄= inversion v
using inversion-noteq-unit-disc[of v w ]
using inversion-noteq-unit-disc[of v v ]
using ‹v∈ unit-disc› ‹w∈ unit-disc›
77
by auto
ultimately
show ?thesis
using assms
using conjugate-cross-ratio[of v w inversion v u ]
unfolding poincare-between-def
by (metis conjugate-id-iﬀ conjugate-involution inversion-def inversion-sym o-apply )
qed
