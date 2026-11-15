---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-008-classification-of-h-lines-into-euclidean-segment
section_title: "Classification of h-lines into Euclidean segments and circles"
section_number: null
pages: 7-8
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
If an h-line contains zero, than it also contains infinity (the inverse point of zero) and is by definition an
Euclidean line.

lemma is-poincare-line-trough-zero-trough-infty [simp]:
assumes is-poincare-line | and 0), € circline-set |
shows cop, € circline-set |
using is-poincare-line-inverse-point|OF assms|
by simp

lemma is-poincare-line-trough-zero-is-line:
assumes is-poincare-line | and 0), € circline-set |

shows is-line |

using assms

using inf-in-circline-set is-poincare-line-trough-zero-trough-infty
by blast

If an h-line does not contain zero, than it also does not contain infinity (the inverse point of zero) and is by
definition an Euclidean circle.

lemma is-poincare-line-not-trough-zero-not-trough-infty [simp]:
assumes is-poincare-line |
assumes 0), ¢ circline-set |
shows co, ¢ circline-set |
using assms
using is-poincare-line-inverse-point|OF assms(1), of oon]
by auto

lemma is-poincare-line-not-trough-zero-is-circle:
assumes is-poincare-line | 0, ¢ circline-set |
shows is-circle |
using assms
using inf-in-circline-set is-poincare-line-not-trough-zero-not-trough-infty
by auto
