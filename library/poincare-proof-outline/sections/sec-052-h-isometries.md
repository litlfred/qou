---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-052-h-isometries
section_title: "H-isometries"
section_number: null
pages: 125-126
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
H-isometries are functions that map the unit disc onto itself
typedef p-isometry ={f. unit-disc-ﬁx-f f}
125
by (rule-tac x =id in exI, simp add : unit-disc-ﬁx-f-def, rule-tac x =id-moebius in exI, simp)
setup-lifting type-deﬁnition-p-isometry
Action of an h-isometry on an h-point
lift-deﬁnition p-isometry-pt :: p-isometry⇒ p-point⇒ p-point is λ f p. f p
using unit-disc-ﬁx-f-unit-disc
by auto
Action of an h-isometry on an h-line
lift-deﬁnition p-isometry-line :: p-isometry⇒ p-line⇒ p-line is λ f l. unit-disc-ﬁx-f-circline f l
proof−
ﬁx f H
assume unit-disc-ﬁx-f f is-poincare-line H
then obtain M where unit-disc-ﬁx M and∗: f = moebius-pt M ∨ f = moebius-pt M ◦ conjugate
unfolding unit-disc-ﬁx-f-def
by auto
show is-poincare-line (unit-disc-ﬁx-f-circline f H )
using∗
proof
assume f = moebius-pt M
thus ?thesis
using ‹unit-disc-ﬁx M › ‹is-poincare-line H ›
using unit-disc-ﬁx-f-circline-direct[of M f H ]
by auto
next
assume f = moebius-pt M ◦ conjugate
thus ?thesis
using ‹unit-disc-ﬁx M › ‹is-poincare-line H ›
using unit-disc-ﬁx-f-circline-indirect[of M f H ]
by auto
qed
qed
An example lemma about h-isometries.
H-isometries preserve h-collinearity
lemma p-collinear-p-isometry-pt [simp]:
shows p-collinear (p-isometry-pt M ‘ A )←→ p-collinear A
proof−
have∗:∀ M A. ((λx. moebius-pt M (conjugate x )) ‘ A = moebius-pt M ‘ (conjugate ‘ A))
by auto
show ?thesis
by transfer (auto simp add : unit-disc-ﬁx-f-def ∗)
qed
