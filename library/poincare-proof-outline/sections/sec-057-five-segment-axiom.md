---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry"
section_id: sec-057-five-segment-axiom
section_title: "Five segment axiom"
section_number: null
pages: 140-141
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
doc_brief: "Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma ﬁve-segment-axiom:
assumes
in-disc: x∈ unit-disc y ∈ unit-disc z ∈ unit-disc u ∈ unit-disc and
in-disc ′: x ′∈ unit-disc y ′∈ unit-disc z ′∈ unit-disc u ′∈ unit-disc and
x⁄= y and
betw: poincare-between x y z poincare-between x ′ y ′ z ′ and
xy: poincare-distance x y = poincare-distance x ′ y ′ and
xu: poincare-distance x u = poincare-distance x ′ u ′ and
yu: poincare-distance y u = poincare-distance y ′ u ′ and
yz: poincare-distance y z = poincare-distance y ′ z ′
shows
poincare-distance z u = poincare-distance z ′ u ′
proof−
from assms obtain M where
M : unit-disc-ﬁx-f M M x = x ′ M u = u ′ M y = y ′
using unit-disc-ﬁx-f-congruent-triangles[of x y u ]
by blast
have M z = z ′
proof (rule unique-poincare-distance-on-ray[where u=x ′ and v=y ′ and y=M z and z=z ′ and d=poincare-distance
x z ])
show 0≤ poincare-distance x z
using poincare-distance-ge0 in-disc
by simp
next
show x ′⁄= y ′
using M ‹x⁄= y›
using in-disc in-disc ′ poincare-distance-eq-0-iﬀ xy
by auto
next
show poincare-distance x ′ (M z ) = poincare-distance x z
using M in-disc
unfolding unit-disc-ﬁx-f-def
by auto
next
show M z ∈ unit-disc
using M in-disc
unfolding unit-disc-ﬁx-f-def
by auto
140
next
show poincare-distance x ′ z ′ = poincare-distance x z
using xy yz betw
using poincare-between-sum-distances[of x y z ]
using poincare-between-sum-distances[of x ′ y ′ z ′]
using in-disc in-disc ′
by auto
next
show poincare-between x ′ y ′ (M z )
using M
using in-disc betw
unfolding unit-disc-ﬁx-f-def
by auto
qed fact+
thus ?thesis
using ‹unit-disc-ﬁx-f M ›
using in-disc in-disc ′
‹M u = u ′›
unfolding unit-disc-ﬁx-f-def
by auto
qed
