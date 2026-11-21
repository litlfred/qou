---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-017-some-consequences-of-line-uniqueness
section_title: "Some consequences of line uniqueness"
section_number: null
pages: 30-31
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
H-line uv is the same as the h-line vu.

lemma poincare-line-sym:
assumes u € unit-disc v € unit-disc u # v
shows poincare-line u v = poincare-line v u
using assms
using unique-poincare-line|of u v poincare-line v ul
by simp

lemma poincare-line-sym-general:
assumes u # v u # inversion v
shows poincare-line u v = poincare-line v u
using assms
using unique-poincare-line-generallof u v poincare-line v u]
by simp

Each h-line is the h-line constructed out of its two arbitrary different points.

lemma ex-poincare-line-points:
assumes is-poincare-line H
shows J wv. u € unit-disc A v € unit-disc \ u # v A H = poincare-line uv
using assms
using ez-is-poincare-line-points
using unique-poincare-line|[where |= H]
by fastforce

If an h-line contains two different points on x-axis/y-axis then it is the x-axis/y-axis.

lemma poincare-line-0-real-is-a-azis:
assumes z € circline-set r-aris x # On © A Oh
shows poincare-line 0, x = x-axis
using assms
using is-poincare-line-0-real-is-t-axis|of poincare-line 0p & x]
by auto

lemma poincare-line-0-imag-is-y-axis:
assumes y € circline-set y-axis y # On y # Wn
shows poincare-line Oh y = y-axis
using assms
using is-poincare-line-0-imag-is-y-axis|of poincare-line On y y|
by auto

lemma poincare-line-x-axis:
assumes & € unit-disc y € unit-disc x € circline-set x-axis y € circline-set x-axis t A y
shows poincare-line x y = x-axis
using assms
using unique-poincare-line
by auto

lemma poincare-line-minus-one-one [simp]:

shows poincare-line (of-complex (—1)) (of-complex 1) = x-axis
proof—

have 0», € circline-set (poincare-line (of-complex (—1)) (of-complez 1))

30
unfolding circline-set-def
by simp (transfer, transfer, simp add: vec-cnj-def)
hence poincare-line On (of-complex 1) = poincare-line (of-complex (—1)) (of-complex 1)
by (metis is-poincare-line-poincare-line is-poincare-line-trough-zero-trough-infty not-zero-on-unit-circle of-complex-inj
of-complex-one one-negq-neg-one one-on-unit-circle poincare-line-0-real-is-z-axis poincare-line-circline-set(2) reciprocal-involution
reciprocal-one reciprocal-zero unique-circline-O1inf')
thus ?thesis
using poincare-line-0-real-is-z-axis|of of-complex 1]
by auto
qed
