---
doc_id: arxiv-1601.02479v5
doc_title: "COHOMOLOGICAL DONALDSON–THOMAS THEORY OF A"
section_id: sec-004-14-cohomological-wall-crossing
section_title: "Cohomological wall-crossing"
section_number: 1.4
pages: 8-9
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "COHOMOLOGICAL DONALDSON–THOMAS THEORY OF A — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and the associated cohomo logical Hall alge- bra"
---
homological lift of the following incarnation of the wall crossing formu la, with
∫
denoting the Kontsevich–Soibelman integration map:
(8)
∫
[MS,φ Tr(W )] =
∏
∞
µ
− →−∞
∫
[Mζ -ss,S
µ ,φ Tr(W )].
This is an identity in the completed motivic quantum torus of ﬁnite-dime nsional
modules of the Jacobi algebra for the pair ( Q, W ). Instead of deﬁning any of the
terms in (8) we refer the reader to [23] and [28] for more details on m otivic Hall
algebras and integration maps in the general theory of motivic Dona ldson–Thomas
invariants, or [13] for the speciﬁc case of the motivic Hall algebra of representations
of a Jacobi algebra.
We deﬁne
H(AW ) := H

 ⨁
d∈NQ0
(Md → M d)∗φ Tr(W )d QMd ⊗ L− dim(Md)/2

(9)
where Md is the stack of d-dimensional CQ-representations, and Md is the coarse
moduli space of d-dimensional CQ-representations, the closed points of which are
in bijection with d-dimensional semisimple CQ-representations.
Theorem B (Cohomological wall crossing theorem) . There is an isomorphism
(10) H(AW ) ∼
= ⊠
tw
⊕,∞
µ
− →−∞ H(Aζ
W,µ ).
inside D≥,lf (MMHM(M)). Here the product ⊠tw
⊕,∞
µ
− →−∞
is an ordered product,
taken over descending slopes. Similarly, there is an isomor phism
(11) H( AS
W ) ∼
= ⊠
tw
+,∞
µ
− →−∞ H(Aζ ,S
W,µ )
inside D≥,lf (MMHM(NQ0 )).
Note that in general, the individual terms in the tensor products on the right
hand sides of (10) and (11) will depend on the stability condition, while the terms
on the left hand side do not. The fact that very diﬀerent sheaves c an give rise to
the same tensor product is explained by the fact that in contrast w ith the product
⊠⊕, the product ⊠tw
⊕ is not symmetric; this is the categoriﬁcation of the fact that
the quantum torus utilized in [28] as the target of the integration ma p from the
motivic Hall algebra is generally not commutative.
1.5. The perverse ﬁltration. An advantage of considering constructions relative
to the base Mζ -ss
µ instead ofΛζ
µ is that it leads naturally to the introduction of the
perverse ﬁltration on H( Aζ ,S
W,µ ).
Let f ∈ NQ0 be a framing vector, and let πζ
f ,d : Mζ
f ,d → Mζ -ss
d , be the forgetful
map to the coarse moduli space of ζ-semistable Q-representations from the ﬁne
moduli space of f -framedζ-semistable representations, and let T r(W )ζ
f ,d : Mζ
f ,d →
COHAS AND QUANTUM ENVELOPING ALGEBRAS 9
C be the induced function. We show that for ﬁxed n, and suﬃciently large framing
vector f , there is a natural isomorphism
(12) H n(Aζ ,S
W,d) ∼
= Lf ·d −(d,d)/2 ⊗ Hn
c (Mζ -ss,S
f ,d ,φ mon
T r(W )ζ
f , d
QMζ
f , d
)∨,
in words, we can approximate the restricted vanishing cycle cohomo logy on the
stack M(Q)ζ -ss
d by considering restricted vanishing cycle compactly supported co-
homology on the moduli scheme Mζ
f ,d. This may remind the reader of Totaro’s
construction [49] for calculating equivariant intersection theory, and indeed, in a
sense that will become precise in Section 4.1, our setup is a relative co mpactiﬁca-
tion of Totaro’s construction, over the base Mζ -ss
d . In particular, since the maps
πζ
f ,d are proper, we can use the decomposition theorem along with funda mental
properties of the vanishing cycles functor to deduce that
πζ
f ,d,∗φ mon
T r(W )ζ
f , d
QMζ
f , d
∼
= H
(
πζ
f ,d,∗φ mon
T r(W )ζ
f , d
QMζ
f , d
)
which in turn implies that the hypercohomology of the right hand side ( and hence
the left hand side) of (12) carries a well-behaved perverse ﬁltratio n.
