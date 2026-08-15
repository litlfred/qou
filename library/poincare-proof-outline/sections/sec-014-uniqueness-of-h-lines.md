---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-014-uniqueness-of-h-lines
section_title: "Uniqueness of h-lines"
section_number: null
pages: 29-30
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
The only h-line between two points is the one obtained by the line-construction.
First we show this only for two diﬀerent points inside the disc.
lemma unique-poincare-line:
assumes in-disc: u⁄= v u ∈ unit-disc v ∈ unit-disc
assumes on-l: u∈ circline-set l v ∈ circline-set l is-poincare-line l
shows l = poincare-line u v
using assms
using unique-is-poincare-line[of u v l poincare-line u v ]
unfolding circline-set-def
by auto
The assumption that the points are inside the disc can be relaxed.
lemma unique-poincare-line-general:
assumes in-disc: u⁄= v u ⁄= inversion v
assumes on-l: u∈ circline-set l v ∈ circline-set l is-poincare-line l
shows l = poincare-line u v
using assms
using unique-is-poincare-line-general[of u v l poincare-line u v ]
unfolding circline-set-def
by auto
The explicit line construction enables us to prove that there exists a unique h-line through any given two
h-points (uniqueness part was already shown earlier).
First we show this only for two diﬀerent points inside the disc.
lemma ex1-poincare-line:
assumes u⁄= v u ∈ unit-disc v ∈ unit-disc
shows∃ ! l. is-poincare-line l∧ u∈ circline-set l ∧ v∈ circline-set l
proof (rule ex1I )
let ?l = poincare-line u v
show is-poincare-line ?l∧ u∈ circline-set ?l ∧ v∈ circline-set ?l
using assms
unfolding circline-set-def
by auto
next
ﬁx l
assume is-poincare-line l∧ u∈ circline-set l ∧ v∈ circline-set l
thus l = poincare-line u v
using unique-poincare-line assms
by auto
qed
The assumption that the points are in the disc can be relaxed.
lemma ex1-poincare-line-general:
assumes u⁄= v u ⁄= inversion v
shows∃ ! l. is-poincare-line l∧ u∈ circline-set l ∧ v∈ circline-set l
proof (rule ex1I )
29
let ?l = poincare-line u v
show is-poincare-line ?l∧ u∈ circline-set ?l ∧ v∈ circline-set ?l
using assms
unfolding circline-set-def
by auto
next
ﬁx l
assume is-poincare-line l∧ u∈ circline-set l ∧ v∈ circline-set l
thus l = poincare-line u v
using unique-poincare-line-general assms
by auto
qed
