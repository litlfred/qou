---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-003-13-main-results
section_title: "Main results"
section_number: 1.3
pages: 4-6
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
a universal K-matrix for every quantum symmetric pair coideal sub algebra Bc,s
of Uq(g) for g of ﬁnite type. This provides an analog of the universal R-matrix
for quantum symmetric pairs. Moreover, it shows that important p arts of Lusztig’s
book [Lus94, Chapters 4 & 32] translate to the setting of quantum symmetric pairs.
The construction in the present paper is signiﬁcantly inspired by the examples
(sl2N, s(glN × glN )) and ( sl2N +1, s(glN × glN +1)) considered by Bao and Wang in
[BW13]. The papers [BW13] and [ES13] both observed the existence o f a bar in-
volution for quantum symmetric pair coideal subalgebras Bc,s in this special case.
Bao and Wang then constructed an intertwiner Υ ∈ U between the new bar invo-
lution and Lusztig’s bar involution. The element Υ is hence an analog of t he quasi
R-matrix in Lusztig’s approach to quantum groups, see [Lus94, The orem 4.1.2].
Similar to the construction of the commutativity isomorphisms in [Lus 94, Chapter
32] Bao and Wang construct a Bc,s-module homomorphism TM :M →M for any
ﬁnite-dimensional representation M of Uq(slN ). If M is the vector representation
they show that TM satisﬁes the reﬂection equation and they establish Schur-Jimbo
duality between the coideal subalgebra and a Hecke algebra of type BN acting on
V ⊗N .
In the present paper we consider quantum symmetric pairs in full ge nerality and
formulate results in the Kac-Moody setting whenever possible. The existence of
the bar involution
B :Bc,s →Bc,s, x ↦→xB
for the quantum symmetric pair coideal subalgebra Bc,s was already established
in [BK15]. Following [BW13, Section 2] closely we now prove the existence of an
intertwiner between the two bar involutions. More precisely, we sho w in Theorem
6.10 that there exists a nonzero element X ∈ U which satisﬁes the relation
xB X = Xx for all x ∈Bc,s.(1.2)
We call the element X the quasi K-matrix for Bc,s. It corresponds to the intertwiner
Υ in the setting of [BW13].
Recall from [Kol14, Theorem 2.7] that the involutive automorphism θ : g → g
is determined by a pair ( X,τ ) up to conjugation. Here X is a subset of the set
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 5
of nodes of the Dynkin diagram of g and τ is a diagram automorphism. The Lie
subalgebra gX ⊂ g corresponding to X is required to be of ﬁnite type. Hence there
exists a longest element wX in the parabolic subgroup WX of the Weyl group W .
The Lusztig automorphism TwX may be considered as an element in the completion
U of Uq(g), see Section 3. We deﬁne
K′ = XξT −1
wX ∈ U(1.3)
where ξ ∈ U denotes a suitably chosen element which acts on weight spaces by a
scalar. The element K′ deﬁnes a linear isomorphism
K′
M :M →M(1.4)
for every integrable Uq(g)-module M in category O. In Theorem 7.5 we show that
K′
M is a Bc,s-module homomorphism if one twists the Bc,s-module structure on
both sides of (1.4) appropriately. The element K′ exists in the general Kac-Moody
case.
For g of ﬁnite type there exists a longest element w0 ∈W and a corresponding
family of Lusztig automorphisms Tw0 = (Tw0,M ) ∈ U . In this case we deﬁne
K = XξT −1
wXT −1
w0 ∈ U.(1.5)
For the symmetric pairs ( sl2N, s(glN × glN )) and ( sl2N +1, s(glN × glN +1)) the con-
struction of K coincides with the construction of the Bc,s-module homomorphisms
TM in [BW13] up to conventions. The longest element w0 induces a diagram auto-
morphismτ0 of g and of Uq(g). Any Uq(g)-moduleM can be twisted by an algebra
automorphism ϕ : Uq(g) → Uq(g) if we deﬁne u⊲m = ϕ(u)m for all u ∈ Uq(g),
m ∈ M . We denote the resulting twisted module by Mϕ. We show in Corollary
7.7 that the element K deﬁnes a Bc,s-module isomorphism
KM :M →Mττ 0(1.6)
for all ﬁnite-dimensional Uq(g)-modules M . Alternatively, this can be written as
Kb =τ0(τ (b))K for all b ∈Bc,s.
The construction of the bar involution for Bc,s, the intertwiner X, and the Bc,s-
module homomorphism K are three expected key steps in the wider program of
canonical bases for quantum symmetric pairs proposed in [BW13]. Th e existence
of the bar involution was explicitly stated without proof and referen ce to the pa-
rameters in [BW13, 0.5] and worked out in detail in [BK15]. Weiqiang Wang has
informed us that he and Huanchen Bao have constructed X and K′
M independently
in the case X = ∅, see [BW15].
In the ﬁnal Section 9 we address the crucial problem to determine t he coproduct
∆(K) in U (2). The main step to this end is to determine the coproduct of the
quasi K-matrix X in Theorem 9.4. Even for the symmetric pairs ( sl2N, s(glN ×
glN )) and ( sl2N +1, s(glN × glN +1)), this calculation goes beyond what is contained
in [BW13]. It turns out that if ττ 0 = id then the coproduct ∆(K) is given by
formula (1.1). Hence, in this case K is a universal K-matrix as deﬁned above for
the coideal subalgebra Bc,s. If ττ 0 ⁄= id then we obtain a slight generalization of the
properties (1) and (2) of a universal K-matrix. Motivated by this o bservation we
introduce the notion of a ϕ-universal K-matrix for B if ϕ is an automorphism of a
braided bialgebra H andB is a right coideal subalgebra, see Section 4.3. With this
terminology it hence turns out in Theorem 9.5 that in general K is aττ 0-universal K-
matrix for Bc,s. The fact that ττ 0 may or may not be the identity provides another
6 MARTINA BALAGOVI ´C AND STEF AN KOLB
conceptual explanation for the occurrence of two distinct reﬂec tion equations in the
Noumi-Sugitani-Dijkhuizen approach to quantum symmetric pairs.
