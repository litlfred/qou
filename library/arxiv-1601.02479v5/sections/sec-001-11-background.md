---
doc_id: arxiv-1601.02479v5
doc_title: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras"
section_id: sec-001-11-background
section_title: "Background"
section_number: 1.1
pages: 1-3
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and"
---
1.2. Absolute versus relative Donaldson–Thomas theory 3
1.3. Cohomological integrality 5
1.4. Cohomological wall-crossing 8
1.5. The perverse ﬁltration 8
1.6. Main results for cohomological Hall algebras 9
1.7. The BPS Lie algebra 12
1.8. Structure of the paper 12
1.9. Acknowledgements 12
2. Hodge theory and equivariant vanishing cycles 13
2.1. Monodromic mixed Hodge modules 13
2.2. Equivariant vanishing cycles 20
3. Moduli spaces of quiver representations 25
3.1. Basic notions 25
3.2. Monoidal products 28
3.3. Framed moduli spaces 32
3.4. Jacobi algebras and potentials 32
4. Cohomological Donaldson–Thomas invariants 34
4.1. Approximation of pζ
d by proper maps 34
4.2. The integrality isomorphism — Theorem A 37
4.3. The cohomological wall crossing isomorphism — Theorem B 40
5. Cohomological Hall algebras 43
5.1. The relative cohomological Hall algebra 43
1
2 BEN DA VISON AND SVEN MEINHARDT
5.2. The absolute cohomological Hall algebra 47
5.3. The ambient perverse ﬁltration 48
6. Structural results for cohomological Hall algebras 50
6.1. Symmetric monoidal structures, revisited 50
6.2. The perverse associated graded Hopf algebra 53
6.3. Proof of Theorem C and construction of the BPS Lie algebra 56
6.4. Proof of Theorem D 60
References 63
1. Introduction
1.1. Background. The critical cohomological Hall algebra H( AB,W ) associated to
a noncommutative smooth algebra B and potential W ∈ B/[B, B]vect was intro-
duced by Kontsevich and Soibelman in [30] as a way of categorifying th e theory
of Donaldson–Thomas invariants. The meaning of “critical” here is th at the Hall
algebra is built out of the hypercohomology of the sheaf of vanishing cycles of the
superpotential Tr( W ) on the stack of ﬁnite-dimensional B-modules. This sheaf
is supported on the critical locus of Tr( W ), which is identiﬁed with the stack of
representations of the Jacobi algebra associated to B and W . The critical coho-
mological Hall algebra can thus be thought of as the Hall algebra cat egorifying the
Donaldson–Thomas theory of representations of this Jacobi alge bra.
Donaldson–Thomas invariants, ﬁrst introduced in [47], already have an extensive
literature. We refer to the sequence of papers by Dominic Joyce [2 0, 21, 22, 24, 23]
for a comprehensive account, or the book [25] by Joyce and Song, and also [28, 29]
for the more general and abstract account by Kontsevich and So ibelman using
motivic vanishing cycles. In all of these treatments of Donaldson–T homas theory, a
key role is played by the integrality conjecture, as proven in [30] in th e case of quivers
with potential. In this paper we describe and prove the natural cat egoriﬁcation of
the integrality conjecture in the context of the cohomological Hall algebra for a
quiver with potential, and explain how this gives rise to a mathematical deﬁnition
of the Lie algebra of BPS states, for which the cohomological Hall alg ebra can be
thought of as the positive half of an associated quantum group. Se e [18] for a
Physics-oriented construction of Hall algebras of BPS states.
From now on we assume that B = CQ is the free path algebra of a quiver, that
we are given a Bridgeland stability condition ζ on the category of CQ-modules,
and that µ ∈ (−∞, ∞] is a slope. We denote by Λζ
µ ⊂ NQ0 the union of the zero
vector with the subset of dimension vectors of slope µ with respect to the stability
conditionζ. Let Mζ -ss
µ denote the stack ofζ-semistable CQ-modules with dimension
vector in Λζ
µ . For full generality, we consider a locally closed substack Mζ -ss,S
µ ⊂
Mζ -ss
µ , the closed points of which correspond to ζ-semistable CQ-modules in a Serre
subcategory S of the category of CQ-modules. When S is the entire full subcategory
of ﬁnite dimensional CQ-modules, we will omit all superscripts S.
Via natural correspondences there is an algebra structure on th e Λζ
µ -graded
Borel–Moore homology of the normalised vanishing cycle complex on Mζ -ss
µ , re-
stricted to Mζ -ss,S
µ , that we denote
(1) H
(
Aζ ,S
W,µ
)
:=
⨁
d∈Λ ζ
µ
Hc
(
Mζ -ss,S
d ,φ Tr(W )ζ
d
QMζ -ss
d
⊗ L− dim(Mζ -ss
d )/2
) ∨
as in [30]. These notions are properly deﬁned and explained in Section 3 . This al-
gebra categoriﬁes Donaldson–Thomas theory in the sense that Do naldson–Thomas
COHAS AND QUANTUM ENVELOPING ALGEBRAS 3
invariants for the category of ζ-semistable modules in S are obtained by consider-
ing the class in the Grothendieck group of the Λζ
µ -graded mixed Hodge structures
(equipped with a monodromy action) of the underlying mixed Hodge st ructure of
(1).
The main conclusion of this paper is that the introduction of the coho mological
Hall algebra structure associated to a quiver, a potential and a Se rre subcategory
S should be seen as a ﬁrst step towards forging a connection betwee n the theory
of reﬁned Donaldson–Thomas invariants and the theory of quantu m enveloping
algebras, and that the proof of the integrality conjecture is the m otivic shadow of
a Poincar´ e–Birkhoﬀ–Witt theorem for the associated quantum en veloping algebra.
In fact we reach this conclusion by providing all of the remaining step s, proving this
PBW type theorem, and deﬁning the associated Lie algebra of BPS co homology.
This programme was already articulated in [30] but several compone nts had yet to
be found.
Firstly, a coproduct turning the algebra H( Aζ ,S
W,µ ) into a Hopf algebra had to be
deﬁned. A localised coproduct was found in the ﬁrst author’s paper [10], reinforcing
the hope that H( Aζ ,S
W,µ ) could be turned into a quantum enveloping algebra. Mean-
while the integrality conjecture in the case of free path algebras of quivers with zero
potential was reproven by the second author and Markus Reineke in [35]. We recall
that, loosely speaking, the integrality theorem states that the cla ss of H( Aζ ,S
0,µ ) in
the Grothendieck group of graded monodromic mixed Hodge struct ures is equal
to that of the free supercommutative algebra generated by Sym
(
H(BC*)vir ⊗ Ω
)
for some element Ω for which the graded pieces are ﬁnite-dimensional. This is of
course much weaker than the claim that we have an isomorphism betw een these
two objects, which in turn is weaker than the existence of a PBW isom orphism.
Nevertheless, the proof of [35] has the attractive feature of e xplicitly constructing
Ω, in terms of intersection complexes. This at least gives us a natura l candidate
for a choice of Ω with which to try to upgrade equality in the Grothend ieck group
to a bona ﬁde isomorphism. In addition, it is proven in [13] that due to f ormal
properties of the vanishing cycle functor, the methods of [35] ar e enough to prove a
very general version of the integrality conjecture, even in the pr esence of a nonzero
potential. Similarly, the proof in [13] gives explicit formulae for the clas s of Ω,
and the construction lifts to cohomology, or mixed Hodge modules, w hich is the
lift that we develop in this paper. The claim that there is an isomorphism in
the category of Λζ
µ -graded monodromic mixed Hodge structures between H( Aζ ,S
W,µ )
and Sym
(
H(BC*)vir ⊗ Ω
)
for some Ω depending on W,µ ,ζ, S is what we call the
“cohomological integrality conjecture”. The proof of the cohomo logical integrality
conjecture, and the existence of a coproduct, are the main ingre dients of our proof
of the PBW theorem.
