---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "ThemainmotiveofthisthesisistostudytheactionofthemotivicGaloisgrouponthemotivicfundamental group of an algebraic curve- punctured at a ﬁnite set of points(: GalMot ⟳cMot 1 (-−(,E 0)"
section_id: sec-027-relating-the-modular-and-bianchi-complexes-to-th
section_title: "Relating the modular and Bianchi complexes to the Galois Lie coalgebra"
section_number: null
pages: 106-109
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
doc_brief: "ThemainmotiveofthisthesisistostudytheactionofthemotivicGaloisgrouponthemotivicfundamental group of an algebraic curve- punctured at a finite set of points(: GalMot ⟳cMot 1 (-−(,E 0). (1) — On the"
---
Motivic correlators at torsion points and averaged base point Hodge correlators
Let  be an elliptic curve,? a prime,p⊂ End a prime over?, and( = [p]. There is an canonical up
to root of unity choice of tangent vectorE0 at 0∈ , given by the Dedekind eta function. Extend it to a
translation-invariant vector ﬁeld on and takeEB to be its ﬁber atB.
Recall that we packaged the Lie coalgebrasCL∨
,(,EB into a coalgebraCL∨
,( = É
BCL∨
,(,EB. The
CL∨
,(,EB for diﬀerentB are canonically isomorphic, so there is a natural diagonal ⊂ CL∨
,(. The
image of under CorHod is the space ofaveraged base point correlators. Equivalently, it is the image
of the averaged base point correlator mapCorav = 1
|[p]|
˝
BCorB. The image of the restriction to the
space of symmetric correlators is called the coalgebra ofsymmetric averaged base point Hodge correlators
and denoted Lie∨
sym(,[p]). It is the dual to the quotient of LieHod(,[p]) induced by the quotient of
gr,cnil
1 (−[p],E 0) by the adjoint action of
1(; Z) and the translation action of[p] on.
Relaxed modular complexes and Hodge correlators
Suppose that is an elliptic curve, andO its endomorphism ring, and supposep is a prime inO.p.
Let ): denote the graded right GL:(O)-module Sym (
1(; Z)⊕:)⊗ Q, identiﬁed with the algebra
of polynomials in the variablesC1,C1,...,C :,C:, and letΓ1(p) ⊂GL:(O) be the stabilizer of the vector
(0,..., 0, 1)∈(O/ p):. We will deﬁne a map\ from the relaxed modular complex with coeﬃcients in): to
the depth: component of the standard cochain complex of the Lie coalgebra grLie∨
sym(,[p]):
\ :):⊗Γ1(p) ~"•
:→ CE•
(
grLie∨
sym(,[?])
)
=:
.
Fixanextendedbasis ⟨E1,...,E :,E 0⟩ of+:(O). Alsoﬁxanidentiﬁcationof Fp with[p].Wewillabuse
notation and identifyU∈ Fp withU∈[?]. Last, we identify the domain of\ with
(
Z[F:
p− 0]⊗ ):
)
⊗GL2(O) "•
:.
In the degree 1 component, deﬁne the map on the level of generating series by
Õ
=1,=′
1,...,=:,=′
:
(
(U1,...,U :)⊗ C=1
1 C
=′
1
1 ...C =:
: C
=′
:
:
)
⊗[E1,...,E :]
7→ 1
|[p]|
Õ
B∈[p]
Θ∗
B
(U1,...,U :,−(U1+···+ U:)|C1 :··· :C: : 0). (3.18)
98
The maps in higher degrees are given by
(Z[Fp− 0]⊗ ):
)⊗GL2(O) "=
:→
( =Û
grLie∨
sym(,[?])
)
=:
,
Õ
=1,=′
1,...,=:,=′
:
(
(U1,...,U :)⊗ C=1
1 C
=′
1
1 ...C =:
: C
=′
:
:
)
⊗ ([
E1,...,E :1
]
∧···∧
[
E:=−1+1,...,E :=
])
7→ 1
|[p]|
Õ
B∈[p]
Θ∗
B
(U1,...,U :1,−(U1+···+ U:1)| C1 :··· :C:1 : 0)∧···∧
∧Θ∗
B
(U:=−1+1,...,U :=,−(U:=−1+1+···+ U:=)| C:=−1+1 :··· :C:= : 0).
Theorem 3.12.The map\ is a well-deﬁned surjective morphism of complexes of gradedO-modules.
Proof. The map\ is a morphism of gradedGL:(O)-modules by construction (recall theC8,C8 are dual to the
cohomologygenerators l,l),andissurjectivebyconstruction. Weneedtoverifythatthemap \ respects(1)
the ﬁrst shuﬄe relations, (2) the dihedral symmetry relations, (3) the coproduct. We show the three in order.
The ﬁrst shuﬄe relation on the image holds termwise – for eachB∈ [?] – and is equivalent to the
relation on the dual generating series (Lemma 3.1(c)):
Õ
f∈Σ8,9
ΘB
(Vf−1(1) :··· :Vf−1(:) : 0|Df−1(1),D f−1(2),...,D f−1(8+9),−(D1+···+ D8+9)),
whereC8 = D1+···+ D8,U8 = V8−V8−1. This is the ﬁrst shuﬄe relation on the generating seriesΘB
( :|, ),
which holds a priori.
The images of the dihedral symmetry relations are exactly the relations of Corollary 3.6, which hold
modulo the correlators of elements that are independent ofB.
Finally, the map\ intertwines the coproduct. The general case follows from the degree 1. SetC0= 0. By
(3.10), we have
X\
( Õ
=1,=′
1,...,=:,=′
:
(
(U1,...,U :)⊗ C=1
1 C
=′
1
1 ...C =:
: C
=′
:
:
)
⊗[E1,...,E :]
)
=
= 1

p

Õ
B∈[p]
(Õ
cyc
:Õ
8=0
Θ∗
B
(U1,...,U 8,−(U1+···+ U8)| C1 :··· :C8 :C0
)∧
∧Θ∗
B
(U8+1,...,U :,−(U8+1+···+ U:)| C8+1 :··· :C: :C0
)+lower depth terms
)
,
(3.19)
where the lower-depth terms are correlators of elements independent ofB, and the cyclic sum is over indices
99
modulo:+ 1. On the other hand, we have
X
( Õ
=1,=′
1,...,=:,=′
:
(
(U1,...,U :)⊗ C=1
1 C
=′
1
1 ...C =:
: C
=′
:
:
)
⊗[E1,...,E :]
)
=
( Õ
=1,=′
1,...,=:,=′
:
(
(U1,...,U :)⊗ C=1
1 C
=′
1
1 ...C =:
: C
=′
:
:
)
⊗
Õ
cyc
:Õ
8=0
−[E1,...,E 8]∧[ E8+1,...,E :]
)
.
(3.20)
The cyclic shift inGL:(O), which mapsE07→E17→E27→···7→ E:7→E0, acts by the transpose action on
theC8 byC87→C8+1−C1 (indices modulo:+ 1; recallC:+1=C0= 0). Thus the image of (3.20) under\ agrees
with (3.19) in each summand of the cyclic sum, except with an additive shift of the arguments. It remains to
apply the homogeneity of theΘ∗
B. □
Remark
Why do we deﬁne the map\ using averaged base point correlators? It would have been possible to deﬁne the
map to Lie∨
Hod(,[p]) using the correlators with ﬁxed base point, CorB. However, this map would be zero.
Indeed, any correlator with base pointB vanishes modulo the depth ﬁltration in Lie∨
Hod(,[p]) induced by
CorB, since any correlator can be written modulo those of lower depth by the change of base point formula
(3.11). Those correlators of lower depth depend onB, so this does not imply the image of Corav is zero.
Ontheotherhand,themap \ canbemodiﬁed,replacing [p] byitssubgroupoforder ? (if|[p]|= ?2).
We will use this when we specialize\ to the nodal projective line.
Bianchi complexes and Hodge correlators in depth 2
Let : = 2 and  one of the CM elliptic curves with endomorphism ringO = Z[8] or Z[d]. According to
Lemma 3.11, there is an isomorphismk :•→"•
2 from the Bianchi complex to the modular complex. The
relaxedmodularcomplex ~"•
2 iscanonicallyisomorphictothemodularcomplex "•
2,sincethesecondshuﬄe
relations are equivalent to the dihedral symmetry relations. Thus we have a map
\◦k :)2⊗Γ1(p) •→ CE•
(
grLie∨
sym(,[p])
)
=2
.
The complex of the left side is the chain complex with coeﬃcients in the local system)2 on the orbifold
Γ1(p)\ H3. We arrive at the following important result:
100
Theorem 3.13.Let be one of the CM elliptic curves = C/Z[8] or = C/Z[d]. Then
\◦k : CE•
(
grLie∨
av(,[p])
)
=2
is a surjective morphism of complexes.
It is tempting to extend Theorem 3.12 to higher depth by showing the map\ descends to the modular
complex"•
:. ThisrequiresshowingthesecondshuﬄerelationsfortheaveragedbasepointHodgecorrelators
modulo the depth ﬁltration. The following would follow from Conjecture 3.9:
Conjecture 3.14.The map\ descends to a morphism of complexes
\ :):⊗Γ1(p) "•
:→ CE•
(
grLie∨
sym(,[p])
)
=:
.
