---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-060-five-segment-axiom
section_title: "Five segment axiom"
section_number: null
pages: 140-141
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
lemma five-segment-axiom:
assumes
in-disc:  € unit-disc y € unit-disc z € unit-disc u € unit-disc and
in-disc': x' € unit-disc y’ € unit-dise z' € unit-disc u’ € unit-disc and
x #yand
betw: poincare-between x y z poincare-between x’ y' z' and
xy: poincare-distance x y = poincare-distance x' y’ and
xu: poincare-distance x u = poincare-distance x’ u' and
yu: poincare-distance y u = poincare-distance y’ u’ and
yz: poincare-distance y z = poincare-distance y’ z'
shows
poincare-distance z u = poincare-distance z' u'
proof—
from assms obtain M where
M: unit-disc-fixz-f MMx=2'Mu=u'My=y’'
using unit-disc-fiz-f-congruent-triangles|of x y u]

by blast
have M z = z’
proof (rule unique-poincare-distance-on-ray[where u=x' and v=y’ and y=M z and z=z' and d=poincare-distance
2)

show 0 < poincare-distance x z
using poincare-distance-ge0 in-disc
by simp
next
show 2/4 y’
using M «x 4 y>
using in-disc in-disc’ poincare-distance-eq-0-iff xy
by auto
next
show poincare-distance x' (M z) = poincare-distance x z
using M in-disc
unfolding unit-disc-fix-f-def
by auto
next
show M z € unit-disc
using M in-disc
unfolding unit-disc-fix-f-def
by auto

140
next
show poincare-distance x’ z' = poincare-distance x z
using xy yz betw
using poincare-between-sum-distances|of x y 2]
using poincare-between-sum-distances|of x’ y’ z'|
using in-disc in-disc’
by auto
next
show poincare-between x’ y' (M z)
using M
using in-disc betw
unfolding unit-disc-fix-f-def
by auto
qed fact+
thus ?thesis
using <unit-disc-fiz-f M»
using in-disc in-disc’
(Mu=u’
unfolding unit-disc-fix-f-def
by auto
qed
