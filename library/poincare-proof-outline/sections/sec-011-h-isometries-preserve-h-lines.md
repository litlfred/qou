---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-011-h-isometries-preserve-h-lines
section_title: "H-isometries preserve h-lines"
section_number: null
pages: 14-16
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
H-isometries are defined as homographies (actions of Mébius transformations) and antihomographies (compo-
sitions of actions of Mébius transformations with conjugation) that fix the unit disc (map it onto itself). They
also map h-lines onto h-lines

We prove a bit more general lemma that states that all Mébius transformations that fix the unit circle (not
necessary the unit disc) map h-lines onto h-lines

14
lemma unit-circle-fix-preserve-is-poincare-line [simp]:
assumes unit-circle-fix M is-poincare-line H
shows is-poincare-line (moebius-circline M H)
using assms
unfolding is-poincare-line-iff
proof (safe)
let ?H’ = mocbius-ocircline M (of-circline H)
let ?U' = moebius-ocircline M ounit-circle
assume ++: unit-circle-fix M perpendicular H unit-circle
have ounit: ounit-circle = moebius-ocircline M ounit-circle V
ounit-circle = moebius-ocircline M (opposite-ocircline ounit-circle)
using ++(1) unit-circle-fix-iff [of M|
by (simp add: inj-of-ocircline moebius-circline-ocircline)

show perpendicular (moebius-circline M H) unit-circle
proof (cases pos-oriented ?H')
case True
hence *: of-circline (of-ocircline ?H') = ?H’
using of-circline-of-ocircline-pos-oriented
by blast
from ounit show ?thesis
proof
assume **: ounit-circle = moebius-ocircline M ounit-circle
show ?thesis
using ++
unfolding perpendicular-def
by (simp, subst moebius-circline-ocircline, subst *, subst «*) simp
next
assume *«: ounit-circle = moebius-ocircline M (opposite-ocircline ounit-circle)
show ?thesis
using ++
unfolding perpendicular-def
by (simp, subst moebius-circline-ocircline, subst *, subst «*) simp
qed
next
case False
hence «: of-circline (of-ocircline ?H') = opposite-ocircline ?H'
by (metis of-circline-of-ocircline pos-oriented-of-circline)
from ounit show ?thesis
proof
assume **: ounit-circle = moebius-ocircline M ounit-circle
show ?thesis
using ++
unfolding perpendicular-def
by (simp, subst moebius-circline-ocircline, subst *, subst «*) simp
next
assume *«: ounit-circle = moebius-ocircline M (opposite-ocircline ounit-circle)
show ?thesis
using ++
unfolding perpendicular-def
by (simp, subst moebius-circline-ocircline, subst *, subst «*) simp
qed
qed
qed simp

lemma unit-circle-fit-preserve-is-poincare-line-iff [simp]:
assumes unit-circle-fix M
shows is-poincare-line (moebius-circline M H) «—+ is-poincare-line H
using assms
using unit-circle-fic-preserve-is-poincare-line|of M H]
using wnit-circle-fic-preserve-is-poincare-line|of moebius-inv M moebius-circline M H]
by (auto simp del: unit-circle-fir-preserve-is-poincare-line)

Since h-lines are preserved by transformations that fix the unit circle, so is collinearity.

lemma unit-disc-fiz-preserve-poincare-collinear [simp]:
assumes unit-circle-fix M poincare-collinear A
shows poincare-collinear (moebius-pt M ‘ A)

using assms

unfolding poincare-collinear-def

by (auto, rule-tac c=moebius-circline M p in exl, auto)

lemma unit-disc-fiz-preserve-poincare-collinear-iff [simp]:
assumes unit-circle-fix M
shows poincare-collinear (moebius-pt M ‘ A) <—> poincare-collinear A
using assms
using unit-disc-fiz-preserve-poincare-collinear|of M A]
using unit-disc-fiz-preserve-poincare-collinear|of moebius-inu M mocbius-pt M ‘ A]
by (auto simp del: unit-disc-fix-preserve-poincare-collinear)

lemma unit-disc-fiz-preserve-poincare-collinear3 [simp]:
assumes unit-disc-fix M
shows poincare-collinear {moebius-pt M u, moebius-pt M v, moebius-pt M w} <>
poincare-collinear {u, v, w}
using assms unit-disc-fiz-preserve-poincare-collinear-iff [of M {u, v, w}]
by simp

Conjugation is also an h-isometry and it preserves h-lines.

lemma is-poincare-line-conjugate-circline [simp]:
assumes is-poincare-line H
shows is-poincare-line (conjugate-circline H)
using assms
by (transfer, transfer, auto simp add: mat-cnj-def hermitean-def mat-adj-def )

lemma is-poincare-line-conjugate-circline-iff [simp]:
shows is-poincare-line (conjugate-circline H) <—+ is-poincare-line H
using is-poincare-line-conjugate-circline|of conjugate-circline H]
by auto

Since h-lines are preserved by conjugation, so is collinearity.

lemma conjugate-preserve-poincare-collinear [simp]:
assumes poincare-collinear A
shows poincare-collinear (conjugate ‘ A)
using assms
unfolding poincare-collinear-def
by auto (rule-tac «=conjugate-circline p in exI, auto)

lemma conjugate-conjugate [simp]: conjugate ‘ conjugate ‘A = A
by (auto simp add: image-iff)

lemma conjugate-preserve-poincare-collinear-iff [simp]:
shows poincare-collinear (conjugate ‘ A) <—+ poincare-collinear A
using conjugate-preserve-poincare-collinear|of A]
using conjugate-preserve-poincare-collinear|of conjugate ‘ A]
by (auto simp del: conjugate-preserve-poincare-collinear)
