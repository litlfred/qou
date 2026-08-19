---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum"
section_id: sec-020-63-the-corepresentation-space
section_title: "The corepresentation space"
section_number: 6.3
pages: 51-53
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual ˆA as a von Neumann algebra."
---
Recall that W satisﬁes the pentagon equation and the coaction axiom (2.35). In a
more familiar form we see that W ′ =W21 := ΣW Σ∈M ( ˆA⊗A ) satisﬁes
(1⊗ ∆) W ′ =W ′
12W ′
13. (6.33)
Hence if we treat W ′ as an element in M (B(H)⊗A ) instead, we obtain the left
regular corepresentation
Π : H −→ H⊗M (A)
f ↦→ W ′(f⊗ 1) (6.34)
which satisﬁes
(1⊗ ∆) ◦ Π = (Π ⊗ 1)◦ Π. (6.35)
This corepresentation picture is useful when we study the corepr esentation of
the quantum double. Therefore we introduce the transformation fromH toHcorep
so that ˆA acts canonically. Similarly, by considering ˆW , we also describe the trans-
formation so that A acts canonically on ˆH.
Deﬁnition 6.12. We deﬁne the transformation Tco :H−→H corep by
Tco :f (s,t ) ↦→ f (−s,s−t + iQ
2 )Gb(Q
2−is +it)−1, (6.36)
T −1
co :f (s,t ) ↦→ f (−s,−t−s + iQ
2 )Gb(−it). (6.37)
Similarly, we deﬁne the transformation ˆTco : ˆH−→ ˆHcorep by
ˆTco : ˆf (s,t ) ↦→ f (−s,s−t + iQ
2 )Gb(Q
2 +is−it)e2πis(s−t+ iQ
2 ), (6.38)
ˆT −1
co : ˆf (s,t ) ↦→ f (−s,−t−s + iQ
2 )e2πistGb(Q +it)−1. (6.39)
Proposition 6.13. Under the transformation Tco, the action of ˆA onHcorep is
given by
ˆA =e−2πbs, ˆB =e2πbps. (6.40)
Under the transformation ˆTco, the action of A on ˆHcorep is given by
A =e2πbs, B =e2πbps. (6.41)
Furthermore, the L2 measure onHcorep and ˆHcorep becomes the standard Lebesgue
measure.
51
Proof. It suﬃces to see that the transformations can be written as
Tco = (t↦→t−s)◦ (−s,−t)◦ (t↦→t + iQ
2 )◦Gb(−it)−1, (6.42)
ˆTco = (t↦→t−s)◦ (−s,−t)◦ (t↦→t + iQ
2 )◦Gb(Q +it)e−2πist, (6.43)
followed by applying the transformation rules.
This choice allows us to reproduce the representation from the pair ing between
A and ˆA given by the corepresentation associated to the multiplicative unita ry.
Proposition 6.14. The left regular corepresentation associated toW ′ onA is given
by
f (s,t )↦→
∫
R+i0
f (s +τ,t )
Gb(Q +iτ )Bib−1τAib−1sdτ. (6.44)
Remark 6.15. Note that the left regular corepresentation is related to th e left
“fundamental” representation
∫
f (s)xb−1(− Q
2 +is)ds↦→
( ∫
f (s)(xA +B)b−1(− Q
2 +is)ds
)
δ− 1
2, (6.45)
i.e.
f (s)↦→
∫
f (s +τ )Gb(−iτ )Gb( Q
2−is)
Gb( Q
2−iτ−is)
Aib−1s− Q
2bBib−1τA
Q
2bdτ (6.46)
=
∫
f (s +τ ) Gb( Q
2 +is +iτ )
Gb(Q +iτ )Gb( Q
2 +is)
Bib−1τAib−1sdτ
by multiplication by Gb( Q
2 +is)−1. Here δ =A− Q
b is the modular element.
Proposition 6.16. Under the pairing ⟨1⊗A ∗
q,W ′(f⊗ 1)⟩, the left regular repre-
sentation of the quantum plane algebra Bq =A∗
q is given by the canonical action
X =e2πbs, Y =e2πb(ps+s). (6.47)
Similarly we can deﬁne the action of its modular double count erpart
~X =e2πb−1s, ~Y =e2πb−1(ps+s), (6.48)
so that it extends to a representation of the modular double Bq~q. Under a unitary
transform by multiplication by eπis2
onHcorep, the action becomes the canonical
action of Bq~q.
52
Proof. It follows directly from Proposition 5.11 since λ is the identity map, hence
the elements of ˆA are sent to the corresponding actions. Now the formula follows
from the deﬁnition X = ˆA−1,Y =q ˆB ˆA−1.
Similarly the corepresentation associated to ˆW ′ is given by
f (s)↦→
∫
f (s +τ )Gb(−iτ ) ˆBib−1τ ˆAib−1sdτ. (6.49)
For completeness, by composing Tco withT −1, we obtain the transformation
S :Hrep−→H corep
Proposition 6.17. The transformationS :Hrep−→H corep is given by
S :f (s,t ) ↦→
∫
R
f (α−s,α−t)Gb(Q
2−is +it)−1e2πi(α−s)sdα, (6.50)
S−1 :f (s,t ) ↦→
∫
R
f (α−s,α−t)Gb(Q
2 +is−it)e−2πi(α−s)sdα. (6.51)
Similarly we deﬁne the corresponding transformation for A using ˆS : ˆHrep−→
ˆHcorep by
ˆS : ˆf (s,t ) ↦→
∫
R
f (α−s,α−t)Gb(Q
2 +is−it)e−2πi(α−s)sdα, (6.52)
ˆS−1 : ˆf (s,t ) ↦→
∫
R
f (α−s,α−t)Gb(Q
2−is +it)−1e2πi(α−s)sdα. (6.53)
