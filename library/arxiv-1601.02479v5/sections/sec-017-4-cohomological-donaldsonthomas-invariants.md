---
doc_id: arxiv-1601.02479v5
doc_title: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras"
section_id: sec-017-4-cohomological-donaldsonthomas-invariants
section_title: "Cohomological Donaldson–Thomas invariants"
section_number: 4
pages: 34-37
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and"
---
4.1. Approximation of pζ
d by proper maps. Recall from (43) (and the remark
following it) the morphism
pζ
d : Mζ -ss
d → Mζ -ss
d
taking aζ-semistable d-dimensional CQ-representation to the associated polystable
representation. We start this section by showing that there is a mo dule-theoretic
compactiﬁcation of Totaro’s construction relative to Mζ -ss
d , which we may use
as in Section 2.2 to deﬁne the direct image along pζ
d of the monodromic mixed
Hodge module of vanishing cycles from the stack of d-dimensional ζ-semistable
representations of CQ.
Recall the deﬁnition of ζ(µ )
f from Section 3.3. Recall from (52) the notation
Xf ,d :=X(Qf )(1,d)
Yζ
f ,d :=X
ζ (µ )
f -ss
f ,d .
We replaceζ(µ )
f by an equivalent King stability condition for Qf , as we always can,
by Remark 3.2. Then ζ(µ )
f deﬁnes a linearization of the natural G(1,d)-action on
Xf ,d and we have
Mζ
f ,d :=Xf ,d/ /χ G(1,d)
∼
=Yζ
f ,d/Gd
where G(1,d) = GL 1(C) × Gd. As a Gd-equivariant variety, Xf ,d admits a product
decomposition Xf ,d = Xd×Vf ,d, where Vf ,d :=⨁
i∈Q0 Hom(Cfi , Cdi), and the extra
GL1(C) factor acts by rescaling Vf ,d. We deﬁne Uf ,d ⊂ Vf ,d to be the subspace of
Q0-tuples of surjective maps. The group Gd acts freely on Uf ,d, and the quotient
is a product of Grassmannians, and is a ﬁbre bundle quotient in the ca tegory of
COHAS AND QUANTUM ENVELOPING ALGEBRAS 35
schemes. Therefore Gd also acts freely on Xζ -ss
d × Uf ,d, which is a ﬁbre bundle in
the category of schemes by [15, Prop.23]. Consider the commutativ e diagram
(Xζ -ss
d × Uf ,d)/Gd
i
/d43/d43
κζ
f , d
/d43/d43❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲❲
/d31 /d127 h /d47/d47
Yζ
f ,d/Gd
/d31 /d127 /d47/d47
πζ
f , d
/d39/d39❖❖❖❖❖❖❖❖❖❖❖❖ (Xζ -ss
d × Vf ,d)/Gd
/d15/d15
Mζ -ss
d .
All of the objects in the above diagram are algebraic varieties, with t he exception
of ( Xζ -ss
d × Vf ,d)/Gd, which is strictly an Artin stack. The diagram obtained by
deleting this stack and all arrows incident to it is a relative compactiﬁc ation of the
map κζ
f ,d.
In what follows we use the notation f ≫ 0 to mean that fi ≫ 0 for every i ∈ Q0.
Lemma 4.1. For ﬁxed n and f ≫ 0 the natural map
Hn
(
πζ
f ,d,∗φ mon
T r(W )ζ
f , d
QYζ
f , d/Gd
)
→ H n
(
κζ
f ,d,∗φ mon
T r(W )ζ
f , d
Q(Xζ -ss
d ×Uf , d)/Gd
)
is an isomorphism.
Proof. As in the proof of Proposition 2.16 it is enough to show that for ﬁxed n ∈ Z,
Hn
con
(
φ
T r(W )
ζ
f , d
QYζ
f , d
→
h∗h
∗
φ T r(W )
ζ
f , d
QYζ
f , d
)
is an isomorphism for f ≫ 0, whereh : Xζ -ss
d × Uf ,d → Yζ
f ,d
is the open inclusion and
T r(W )
ζ
f ,d : Yζ
f ,d → C
is the composition of T r(W )ζ
f ,d with the quotient map. On the other hand, the com-
plex of sheavesφ
T r(W )
ζ
f , d
QYζ
f , d
is given by restriction of the pullbackρ∗φ
T r(W )d
QXζ -ss
d
of φ T r(W )d
QXζ -ss
d
along the projection ρ : Xζ -ss
d × Vf ,d → Xζ -ss
d . It follows that
for each x ∈ Xζ -ss
d , the complex of constructible sheaves φ T r(W )
ζ
f , d
QYζ
f , d
|Yζ
f , d∩ρ −1(x)
is a constant complex, supported in degrees that are bounded inde pendently of x.
The codimension of the complement of ( Xζ -ss
d × Uf ,d) ∩ρ−1(x) inside Yζ
f ,d ∩ρ−1(x)
tends to inﬁnity as f ↦→ ∞, and so for suﬃciently large f
Hn
con
(
φ
T r(W )
ζ
f , d
QYζ
f , d
)
Yζ
f , d∩ρ −1(x)
→ H n
con
(
h∗h
∗
φ T r(W )
ζ
f , d
QYζ
f , d
)
Yζ
f , d∩ρ −1(x)
is an isomorphism for all x ∈ Xζ -ss
d , and the result follows. □
We deduce that for ﬁxed d ∈ NQ0 and n ∈ Z, and for f ≫ 0 there are isomor-
phisms
(54)
Φ f ,d,W : Hn
(
πζ
f ,d,∗φ mon
T r(W )ζ
f , d
QMζ
f , d
)
→ H n
(
κζ
f ,d,∗φ mon
T r(W )ζ
f , d
Q(Xζ -ss
d ×Uf , d)/Gd
)
and
(55)
Ψ f ,d,W : Hn
(
κζ
f ,d,!φ mon
T r(W )ζ
f , d
L−f ·d
(Xζ -ss
d ×Uf , d)/Gd
)
→ H n
(
πζ
f ,d,!φ mon
T r(W )ζ
f , d
L−f ·d
Mζ
f , d
)
where the argument that Ψ f ,d,W is an isomorphism is as in Lemma 4.1. On the other
hand, for f ≫ 0, the right hand side of (54) is by deﬁnition Hn(pζ
d,∗φ mon
Tr(W )ζ
d
QMζ -ss
d
),
while the left hand side of (55) is Hn(pζ
d,!φ mon
Tr(W )ζ
d
QMζ -ss
d
).
36 BEN DA VISON AND SVEN MEINHARDT
Remark 4.2. Put in words, we can say that the direct image of the vanishing cy-
cle monodromic mixed Hodge module along the non-representa ble map pζ
d : Mζ -ss
d →
Mζ -ss
d is approximated by the direct image along proper maps of sche mesπζ
f ,d : Mζ
f ,d →
Mζ -ss
d .
For f ≫ 0 we obtain isomorphisms
(56)
Φ
S
f ,d,W : H n(Mζ ,S
f ,d ,φ mon
T r(W )ζ
f , d
QMζ
f , d
) ∼
= Hn(Mζ -ss,S
d ,φ mon
Tr(W )ζ
d
QMζ -ss
d
)
and
(57)
Ψ
S
f ,d,W : H n
c (Mζ -ss,S
d ,φ mon
Tr(W )ζ
d
QMζ -ss
d
) ∼
= Hn
c (Mζ ,S
f ,d ,φ mon
T r(W )ζ
f , d
L−f ·d
Mζ
f , d
)
in the same way.
Since each map πζ
f ,d is proper, and φ mon
T r(W )ζ
d
is exact, we deduce the following
proposition.
Proposition 4.3. For every d ∈ NQ0 there are natural isomorphisms
(58) ν d : H(pζ
d,∗φ mon
Tr(W )ζ
d
QMζ -ss
d
) ∼
=φ mon
T r(W )ζ
d
H(pζ
d,∗QMζ -ss
d
).
Proof. The isomorphisms ν d are obtained by considering the left hand side of (54)
and using the natural isomorphisms
φ mon
T r(W )ζ
d
πζ
f ,d,∗QMζ
f , d
∼
=πζ
f ,d,∗φ mon
T r(W )ζ
f , d
QMζ
f , d
.
The isomorphisms ν d are well-deﬁned by commutativity of the square
πζ
f ′,d,∗φ mon
T r(W )ζ
f ′ , d
QMζ
f ′, d
/d47/d47
πζ
f ′,d,∗ιf ,f ′,∗φ mon
T r(W )ζ
f , d
QMζ
f , d
φ mon
T r(W )ζ
d
πζ
f ′,d,∗QMζ
f ′, d
/d79/d79
/d47/d47φ mon
T r(W )ζ
d
πζ
f ′,d,∗ιf ,f ′,∗QMζ
f , d
/d79/d79
where f ′ > f and ιf ,f ′ : Mζ
f ,d → Mζ
f ′,d is the natural inclusion obtained by extending
a framing by zero. The square commutes as it is obtained by applying t he natural
transformation
φ mon
T r(W )ζ
d
πζ
f ′,d,∗ →πζ
f ′,d,∗φ mon
T r(W )ζ
f ′, d
to the restriction map
QMζ
f ′, d
→ ιf ,f ′,∗QMζ
f , d
.
□
Similarly, the natural isomorphismsφ mon
T r(W )ζ
d
πζ
f ,d,!QMζ
f , d
∼
=πζ
f ,d,!φ mon
T r(W )ζ
f , d
QMζ
f , d
,
along with exactness of φ mon
T r(W )ζ
d
, induce natural isomorphisms
(59) ν c,d : H(pζ
d,!φ mon
Tr(W )ζ
d
QMζ -ss
d
) ∼
=φ mon
T r(W )ζ
d
H(pζ
d,!QMζ -ss
d
).
Proposition 4.4. With Q as above a ﬁnite quiver, d ∈ NQ0 a dimension vector,
and W a potential for Q, there are (non natural) isomorphisms
H
(
Mζ -ss
d ,φ mon
Tr(W )ζ
d
IC Mζ -ss
d
(Q)
)
∼
= H(dim∗ H(pζ
d,∗φ mon
Tr(W )ζ
d
IC Mζ -ss
d
(Q)))
Hc
(
Mζ -ss
d ,φ mon
Tr(W )ζ
d
IC Mζ -ss
d
(Q)
)
∼
= H(dim! H(pζ
d,!φ mon
Tr(W )ζ
d
IC Mζ -ss
d
(Q)))
Hc
(
Mζ -ss,S
d ,φ mon
Tr(W )ζ
d
IC Mζ -ss
d
(Q)
)
∼
= H(dim! ˜ωζ ,∗
d H(pζ
d,!φ mon
Tr(W )ζ
d
IC Mζ -ss
d
(Q)))
where ˜ωζ
d is as in (40).
COHAS AND QUANTUM ENVELOPING ALGEBRAS 37
Proof. Fix n ∈ Z. We prove the existence of the ﬁnal isomorphism, the proof of
the second follows from the special case Mζ -ss,S
d = Mζ -ss
d , and the proof of the ﬁrst
follows from commutativity of Verdier duality with φ mon
Tr(W )ζ
d
. For suﬃciently large
f we may write the degree n piece of the left hand side as
Hn
(
dim!πζ ,S
f ,d,! ˜ωζ ,∗
f ,dφ mon
T r(W )ζ
f , d
L(d,d)/2
Mζ
f , d
)
while the right hand side is written as
Hn
(
dim! ˜ωζ ,∗
d H
(
πζ
f ,d,!φ mon
T r(W )ζ
f , d
L(d,d)/2
Mζ
f , d
))
.
The result then follows from proper base change, and the following c hain of iso-
morphisms, coming from properness of πζ
f ,d, exactness of vanishing cycles functors,
and the decomposition theorem
H
(
πζ
d,f ,!φ mon
T r(W )ζ
f , d
L(d,d)/2
Mζ
f , d
)
∼
= H
(
φ mon
T r(W )ζ
f , d
πζ
d,f ,!L(d,d)/2
Mζ
f , d
)
∼
=φ mon
T r(W )ζ
f , d
H
(
πζ
d,f ,!L(d,d)/2
Mζ
f , d
)
∼
=φ mon
T r(W )ζ
f , d
πζ
d,f ,!L(d,d)/2
Mζ
f , d
∼
=πζ
f ,d,!φ mon
T r(W )ζ
f , d
L(d,d)/2
Mζ
f , d
.
□
Remark 4.5. Throughout the paper we work over the complex numbers, and in the
algebraic setting. For greater generality, we could instea d have considered analytic
mixed Hodge modules — by Saito’s work the same fundamental fa cts that we have
used regarding the vanishing cycle functor remain true in th e category of analytic
mixed Hodge modules (see [44, Sec.2]). In particular, if W is a formal potential such
that T r(W )ζ
d deﬁnes an analytic function in some neighbourhood Ud of 0 ∈ Mζ -ss
d ,
then Proposition 4.3 applies in the neighbourhood Ud. If, moreover, there is a Serre
subcategory U of the category of ζ-semistable CQ-modules of slope µ such that for
all d ∈Λζ
µ the inclusion Mζ -ss,U
d ⊂ Mζ -ss
d is an analytic open inclusion factoring
through an open set Ud as above, then the relative versions of Theorems A, B, C
and D hold with unmodiﬁed proofs. See [48] for results deﬁning such a subcategory
U of the category of coherent sheaves on a Calabi–Yau 3-fold.
