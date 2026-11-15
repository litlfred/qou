---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-054-h-isometries
section_title: "H-isometries"
section_number: null
pages: 125-126
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
H-isometries are functions that map the unit disc onto itself

typedef p-isometry = {f. unit-disc-fix-f f}

125
by (rule-tac c=id in exI, simp add: unit-disc-fix-f-def, rule-tac x=id-moebius in exl, simp)
setup-lifting type-definition-p-isometry
Action of an h-isometry on an h-point

lift-definition p-isometry-pt :: p-isometry = p-point = p-point is X f p. f p
using unit-disc-fir-f-unit-disc
by auto

Action of an h-isometry on an h-line

lift-definition p-isometry-line :: p-isometry = p-line = p-line is X f l. unit-disc-fix-f-circline f |
proof—
fix f H
assume unit-disc-fit-f f is-poincare-line H
then obtain M where unit-disc-fix M and *: f = moebius-pt M V f = moebius-pt M o conjugate
unfolding unit-disc-fix-f-def
by auto
show is-poincare-line (unit-disc-fix-f-circline f H)
using *
proof
assume f = moebius-pt M
thus ?thesis
using <unit-disc-fiz M) ‘is-poincare-line H»
using unit-disc-fix-f-circline-direct|of M f H]
by auto
next
assume f = moebius-pt M o conjugate
thus ?thesis
using <unit-disc-fiz M) ‘is-poincare-line H»
using unit-disc-fiz-f-circline-indirect|of M f H]
by auto
qed
qed

An example lemma about h-isometries.
H-isometries preserve h-collinearity

lemma p-collinear-p-isometry-pt [simp]:
shows p-collinear (p-isometry-pt M ‘ A) > p-collinear A
proof—
have *: V M A. ((Aa. moebius-pt M (conjugate x)) ‘ A = moebius-pt M ‘ (conjugate ‘ A))
by auto
show ?thesis
by transfer (auto simp add: unit-disc-fix-f-def *)
qed
