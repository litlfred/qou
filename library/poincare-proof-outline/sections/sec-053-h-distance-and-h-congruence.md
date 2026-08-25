---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-053-h-distance-and-h-congruence
section_title: "H-distance and h-congruence"
section_number: null
pages: 126-127
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lift-deﬁnition p-dist :: p-point⇒ p-point⇒ real is poincare-distance
done
deﬁnition p-congruent :: p-point⇒ p-point⇒ p-point⇒ p-point⇒ bool where
[simp]: p-congruent u v u ′ v ′←→ p-dist u v = p-dist u ′ v ′
lemma
assumes p-dist u v = p-dist u ′ v ′
assumes p-dist v w = p-dist v ′ w ′
assumes p-dist u w = p-dist u ′ w ′
shows∃ f. p-isometry-pt f u = u ′∧ p-isometry-pt f v = v ′∧ p-isometry-pt f w = w ′
using assms
apply transfer
using unit-disc-ﬁx-f-congruent-triangles
by auto
We prove that unit disc equipped with Poincaré distance is a metric space, i.e. an instantiation of metric-space
locale.
126
instantiation p-point :: metric-space
begin
deﬁnition dist-p-point = p-dist
deﬁnition (uniformity-p-point :: ( p-point× p-point) ﬁlter) = ( INF e∈{0<..}. principal{(x, y). dist-class.dist x y <
e})
deﬁnition open-p-point (U :: p-point set ) = (∀ x∈ U. eventually (λ(x ′, y). x ′ = x−→ y∈ U ) uniformity)
instance
proof
ﬁx x y :: p-point
show (dist-class.dist x y = 0 ) = ( x = y)
unfolding dist-p-point-def
by (transfer, simp add : poincare-distance-eq-0-iﬀ)
next
ﬁx x y z :: p-point
show dist-class.dist x y ≤ dist-class.dist x z + dist-class.dist y z
unfolding dist-p-point-def
apply transfer
using poincare-distance-triangle-inequality poincare-distance-sym
by metis
qed (simp-all add : open-p-point-def uniformity-p-point-def )
end
