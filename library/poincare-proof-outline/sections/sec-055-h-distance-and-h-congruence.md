---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-055-h-distance-and-h-congruence
section_title: "H-distance and h-congruence"
section_number: null
pages: 126-127
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lift-definition p-dist :: p-point => p-point = real is poincare-distance
done

definition p-congruent :: p-point = p-point => p-point > p-point = bool where
[simp]: p-congruent u vu! v' <—+ p-dist uv = p-dist u’ v’

lemma
assumes p-dist uv = p-dist u’ v’
assumes p-dist v w = p-dist v' w’
assumes p-dist u w = p-dist u’ w’
shows i f. p-isometry-pt fu = u' \ p-isometry-pt fv = v' A p-isometry-pt fw = w'
using assms
apply transfer
using unit-disc-fir-f-congruent-triangles
by auto

We prove that unit disc equipped with Poincaré distance is a metric space, i.e. an instantiation of metric-space
locale.

126
instantiation p-point :: metric-space
begin
definition dist-p-point = p-dist
definition (uniformity-p-point :: (p-point x p-point) filter) = (INF e€{0<..}. principal {(x, y). dist-class.dist x y <
e})
definition open-p-point (U :: p-point set) = (V x € U. eventually (A(2', y). x’ = x —> y € U) uniformity)
instance
proof
fix vy :: p-point
show (dist-class.dist x y = 0) = (x = y)
unfolding dist-p-point-def
by (transfer, simp add: poincare-distance-eq-0-iff )
next
fix vy z:: p-point
show dist-class.dist x y < dist-class.dist x z + dist-class.dist y z
unfolding dist-p-point-def
apply transfer
using poincare-distance-triangle-inequality poincare-distance-sym
by metis
qed (simp-all add: open-p-point-def uwniformity-p-point-def)
end
