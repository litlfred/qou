---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model"
section_id: sec-008-classification-of-h-lines-into-euclidean-segment
section_title: "Classification of h-lines into Euclidean segments and circles"
section_number: null
pages: 7-8
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
---
If an h-line contains zero, than it also contains inﬁnity (the inverse point of zero) and is by deﬁnition an
Euclidean line.
lemma is-poincare-line-trough-zero-trough-infty [simp]:
assumes is-poincare-line l and 0 h ∈circline-set l
shows ∞h ∈circline-set l
using is-poincare-line-inverse-point[OF assms]
by simp
lemma is-poincare-line-trough-zero-is-line:
7
assumes is-poincare-line l and 0 h ∈circline-set l
shows is-line l
using assms
using inf-in-circline-set is-poincare-line-trough-zero-trough-infty
by blast
If an h-line does not contain zero, than it also does not contain inﬁnity (the inverse point of zero) and is by
deﬁnition an Euclidean circle.
lemma is-poincare-line-not-trough-zero-not-trough-infty [simp]:
assumes is-poincare-line l
assumes 0 h /∈circline-set l
shows ∞h /∈circline-set l
using assms
using is-poincare-line-inverse-point[OF assms(1), of ∞h]
by auto
lemma is-poincare-line-not-trough-zero-is-circle:
assumes is-poincare-line l 0 h /∈circline-set l
shows is-circle l
using assms
using inf-in-circline-set is-poincare-line-not-trough-zero-not-trough-infty
by auto
4.1.4
