---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-016-uniqueness-of-h-lines
section_title: "Uniqueness of h-lines"
section_number: null
pages: 29-30
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
The only h-line between two points is the one obtained by the line-construction.

First we show this only for two different points inside the disc.

lemma unique-poincare-line:
assumes in-disc: u # vu € unit-disc v € unit-disc
assumes on-l: u € circline-set lv € circline-set | is-poincare-line |
shows | = poincare-line u v
using assms
using unique-is-poincare-line[of u v | poincare-line u v]
unfolding circline-set-def
by auto

The assumption that the points are inside the disc can be relaxed.

lemma unique-poincare-line-general:
assumes in-disc: u #4 v u # inversion v
assumes on-l: u € circline-set lv € circline-set | is-poincare-line |
shows | = poincare-line u v
using assms
using unique-is-poincare-line-generallof u v | poincare-line u v|
unfolding circline-set-def
by auto

The explicit line construction enables us to prove that there exists a unique h-line through any given two
h-points (uniqueness part was already shown earlier).

First we show this only for two different points inside the disc.

lemma ex1-poincare-line:
assumes u # v u € unit-disc v € unit-disc
shows 3! 1. is-poincare-line | \ wu € circline-set | A v € circline-set |
proof (rule ex1I)
let 21 = poincare-line uv
show is-poincare-line ?1 A u € circline-set ?l A v € circline-set #1
using assms
unfolding circline-set-def
by auto
next
fix |
assume is-poincare-line | A u € circline-set 1 A v € circline-set |
thus | = poincare-line uv
using unique-poincare-line assms
by auto
qed

The assumption that the points are in the disc can be relaxed.

lemma ex1-poincare-line-general:

assumes u # v u # inversion v

shows 3! 1. is-poincare-line | \ wu € circline-set | A v € circline-set |
proof (rule ex1I)

29
let 21 = poincare-line uv
show is-poincare-line ?1 A u € circline-set ?l A v € circline-set #1
using assms
unfolding circline-set-def
by auto
next
fix |
assume is-poincare-line | A u € circline-set 1 A v € circline-set |
thus | = poincare-line uv
using unique-poincare-line-general assms
by auto
qed
