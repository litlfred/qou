---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-015-some-consequences-of-line-uniqueness
section_title: "Some consequences of line uniqueness"
section_number: null
pages: 30-31
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
H-line uv is the same as the h-line vu.
lemma poincare-line-sym:
assumes u∈ unit-disc v ∈ unit-disc u ⁄= v
shows poincare-line u v = poincare-line v u
using assms
using unique-poincare-line[of u v poincare-line v u ]
by simp
lemma poincare-line-sym-general:
assumes u⁄= v u ⁄= inversion v
shows poincare-line u v = poincare-line v u
using assms
using unique-poincare-line-general[of u v poincare-line v u ]
by simp
Each h-line is the h-line constructed out of its two arbitrary diﬀerent points.
lemma ex-poincare-line-points:
assumes is-poincare-line H
shows∃ u v. u∈ unit-disc∧ v∈ unit-disc∧ u⁄= v∧ H = poincare-line u v
using assms
using ex-is-poincare-line-points
using unique-poincare-line[where l=H ]
by fastforce
If an h-line contains two diﬀerent points on x-axis/y-axis then it is the x-axis/y-axis.
lemma poincare-line-0-real-is-x-axis:
assumes x∈ circline-set x-axis x ⁄= 0 h x⁄=∞h
shows poincare-line 0 h x = x-axis
using assms
using is-poincare-line-0-real-is-x-axis[of poincare-line 0 h x x ]
by auto
lemma poincare-line-0-imag-is-y-axis:
assumes y∈ circline-set y-axis y ⁄= 0 h y⁄=∞h
shows poincare-line 0 h y = y-axis
using assms
using is-poincare-line-0-imag-is-y-axis[of poincare-line 0 h y y ]
by auto
lemma poincare-line-x-axis:
assumes x∈ unit-disc y ∈ unit-disc x ∈ circline-set x-axis y ∈ circline-set x-axis x ⁄= y
shows poincare-line x y = x-axis
using assms
using unique-poincare-line
by auto
lemma poincare-line-minus-one-one [simp]:
shows poincare-line (of-complex (−1 )) ( of-complex 1 ) = x-axis
proof−
have 0 h∈ circline-set (poincare-line (of-complex (−1 )) ( of-complex 1 ))
30
unfolding circline-set-def
by simp (transfer, transfer, simp add : vec-cnj-def )
hence poincare-line 0 h (of-complex 1 ) = poincare-line (of-complex (−1 )) ( of-complex 1 )
by (metis is-poincare-line-poincare-line is-poincare-line-trough-zero-trough-infty not-zero-on-unit-circle of-complex-inj
of-complex-one one-neq-neg-one one-on-unit-circle poincare-line-0-real-is-x-axis poincare-line-circline-set(2 ) reciprocal-involution
reciprocal-one reciprocal-zero unique-circline-01inf′)
thus ?thesis
using poincare-line-0-real-is-x-axis[of of-complex 1 ]
by auto
qed
