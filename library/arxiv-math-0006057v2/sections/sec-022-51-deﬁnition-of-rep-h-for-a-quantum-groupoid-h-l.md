---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-022-51-deﬁnition-of-rep-h-for-a-quantum-groupoid-h-l
section_title: "Deﬁnition of Rep (H). For a quantum groupoid H let Rep(H) be the cat-"
section_number: 5.1
pages: 14-16
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
egory of representations of H, whose objects are H-modules of ﬁnite rank and
whose morphisms are H-linear homomorphisms. We show that, as in the case of
Hopf algebras, Rep(H) has a natural structure of a monoidal category with duality.
For objects V,W of Rep(H) set
V ⊗W = {x ∈V ⊗kW |x = ∆(1) ·x},(25)
with the obvious action of H via the comultiplication ∆ (here ⊗k denotes the usual
tensor product of vector spaces).
Since ∆(1) is an idempotent, V ⊗W = ∆(1) · (V ⊗kW ). The tensor product
of morphisms is the restriction of usual tensor product of homomo rphisms. The
FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS 15
standard associativity isomorphisms Φ U,V,W : (U ⊗V ) ⊗W → U ⊗ (V ⊗W ) are
functorial and satisfy the pentagon condition, since ∆ is coassocia tive. We will
suppress these isomorphisms and write simply U ⊗V ⊗W .
The target counital subalgebra Ht ⊂ H has an H-module structure given by
h ·z =εt(hz), where h ∈H, z∈Ht.
Lemma 5.1.1. Ht is the unit object of Rep (H).
Proof. Deﬁne a left unit homomorphism lV :Ht ⊗V →V by
lV (1(1) ·z ⊗ 1(2) ·v) = z ·v, z ∈Ht, v∈V.
It is an invertibleH-linear map with the inverse l−1
V (v) = S(1(1))⊗1(2)·v. Moreover,
the collection {lV }V gives a natural equivalence between the functor Ht ⊗ ( ) and
the identity functor. Similarly, the right unit homomorphism rV : V ⊗Ht → V
deﬁned by
rV (1(1) ·v ⊗ 1(2) ·z) = S(z) ·v, z ∈Ht, v∈V,
has the inverse r−1
V (v) = 1 (1) ·v ⊗1(2) and satisﬁes the necessary properties. Finally,
one can check the triangle axiom, i.e., that
(idV ⊗lW ) = (rV ⊗idW )
for all objects V,W of Rep(H) and v ∈V, w∈W ([NTV], 4.1).
Using the antipode S ofH, we can provide Rep(H) with a duality. For any object
V of Rep(H) deﬁne the action of H onV ∗ = Hom k(V, k) by (h ·φ)(v) = φ(S(h) ·v),
where h ∈H,v ∈V,φ ∈V ∗. For any morphism f :V →W let f ∗ :W ∗ →V ∗ be
the morphism dual to f (see [T], I.1.8).
For any V in Rep(H) deﬁne the duality homomorphisms
dV :V ∗ ⊗V →Ht, b V :Ht →V ⊗V ∗
as follows. For ∑
j φj ⊗vj ∈V ∗ ⊗V set
dV (
∑
j
φj ⊗vj) =
∑
j
φj(1(1) ·vj )1(2).(26)
Let {gi}i and {γi}i be bases of V and V ∗ respectively, dual to each other. The
element ∑
i gi ⊗γi does not depend on choice of these bases; moreover, for all
v ∈V,φ ∈V ∗ one has φ = ∑
i φ(gi)γi and v = ∑
i giγi(v). Set
bV (z) = z ·
∑
i
gi ⊗γi.(27)
Proposition 5.1.2. The category Rep (H) is a monoidal category with duality.
Proof. We know already that Rep( H) is monoidal. One can check ([NTV], 4.2)
thatdV and bV are H-linear. To show that they satisfy the identities
(idV ⊗dV )(bV ⊗ idV ) = id V, (dV ⊗ idV ∗ )(idV ∗ ⊗bV ) = id V ∗,
