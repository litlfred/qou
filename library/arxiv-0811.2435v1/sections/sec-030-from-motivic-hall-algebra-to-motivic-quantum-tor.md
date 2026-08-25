---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-030-from-motivic-hall-algebra-to-motivic-quantum-tor
section_title: "From motivic Hall algebra to motivic quantum torus"
section_number: null
pages: 95-102
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
torus
Assume thatC is an ind-constructible 3d Calabi-Yau category endowed with
polarization and orientation data
√
D. The Hall algebra of C is graded by
the corresponding lattice Γ: H(C) =⊕γ∈ΓH(C)γ. Main result of this section
is the following theorem.
95
Theorem 8 The map Φ : H(C)→R Γ given by the formula
Φ( ν) = (ν,w )ˆeγ, ν∈H(C)γ
is a homomorphism of Γ -graded Q-algebras. Here w is the motivic weight
and (•,•) is the pairing between motivic measures and functions.
In other words, the homomorphism H(C)→R Γ can be written as
[π :Y→Ob(C)]↦→
↦→
∫
Y
(1−MF (π(y))) (1−MF 0(Qπ(y))) L− 1
2 rkQπ (y) L
1
2 (π(y),π(y))≤1 ˆecl(π(y)) ,
where
∫
Y is understood as the direct image functor (see Section 4.2).
The natural extension of the above homomorphism to the compl etion of
ˆH(CV ) maps the element AHall
V to the element Amot
V deﬁned in Section 6.2.
Proof. For simplicity we will present the proof of the Theorem for
νE := [δE :pt→Ob(C)] ,
where δE(pt) = E∈Ob(C(k)) is the “delta-function”. The general proof for
equivariant constructible families is similar. We will als o assume that our
category is minimal on the diagonal.
The proof will consists of several steps.
Step 1.
We have:
νE1·νE2 = L−(E2,E1)≤0[π21 : Ext 1(E2,E 1)→Ob(C)] ,
the map π21 is the restriction of the cone map 21
tot(Ker(m1 :HOM0→HOM 1))→Ob(C)
to the ﬁber over the point ( E2[−1],E 1). Under this map the element α∈
Ext1(E2,E 1) is mapped to the object
Eα =Cone(α :E2[−1]→E1) .
21Recall that we pretend that such a map exists. In fact, it is de ﬁned only as a 1-
morphism of stacks.
96
Let us denote by γi the class cl(Ei)∈ Γ,i = 1, 2. Then we have:
Φ( νEi) = L
1
2 (Ei,Ei)≤1(1−MF 0(Wmin
Ei ))I(h(Ei)) ˆeγi, i = 1, 2 ,
where h(Ei) is the value at Ei of the element h∈ J2(C) (i.e. the image of
the restriction map to J2(C)) given by the super line bundle
√
D⊗D −1
≤1 with
trivialized tensor square.
We have:
Φ( νE1)Φ( νE2) = L
1
2 ((E1,E1)≤1+(E2,E2)≤1)×
× L
1
2 ((E1,E2)≤1−(E2,E1)≤1)(1−MF 0(Wmin
E1 ⊕Wmin
E2 ))I(h(E1))I(h(E2)) ˆeγ1+γ2 .
In order to obtain this formula we used the Calabi-Yau proper ty, which
implies that
⟨γ1,γ 2⟩= ∑
j∈Z(−1)j(E1,E 2)j = (E1,E 2)≤1 + (E1,E 2)/greaterorequalslant2 =
= ( E1,E 2)≤1− (E2,E 1)≤1 ,
where we employ the notation ( E1,E 2)/greaterorequalslantm =∑
j/greaterorequalslantm(−1)j(E1,E 2)j. Also we
used the motivic Thom-Sebastiani theorem for the Milnor ﬁbe rs and the
product formula for the basis elements in the motivic quantu m torusRΓ .
On the other hand, we can apply Φ to the product νE1·νE2 and obtain:
Φ( νE1·νE2) =
= L−(E2,E1)≤0
∫
α∈Ext1(E2,E1) L
1
2 (Eα ,Eα )≤1(1−MF 0(Wmin
Eα ))I(h(Eα))ˆeγ1+γ2 .
Using the identity ( E2,E 1)≤0 = (E2,E 1)≤1 + (E2,E 1)1 (and also recall
that (E2,E 1)1 = dim Ext1(E2,E 1)) and observing that
(E1⊕E2,E 1⊕E2)≤1 = (E1,E 1)≤1 + (E2,E 2)≤1 + (E1,E 2)≤1 + (E2,E 1)≤1
we arrive to the following equality which is equivalent to
Φ( νE1·νE2) = Φ( νE1)Φ( νE2)
and hence implies the Theorem:
L(E2,E1)1(1−MF 0(Wmin
E1 ⊕Wmin
E2 ))I(h(E1))I(h(E2)) =
=
∫
α∈Ext1(E2,E1)
L
1
2 ((Eα ,Eα )≤1−(E1⊕E2,E1⊕E2)≤1)(1−MF 0(Wmin
Eα ))I(h(Eα)) .
97
Step 2.
Now we would like to express the diﬀerence
(Eα,Eα)≤1− (E1⊕E2,E 1⊕E2)≤1
as the rank of a certain linear operator. Recall that the obje ct Eα can be
thought of as a deformation of the object E0 :=E1⊕E2. Therefore, there is
a spectral sequence which starts at Ext •(E1⊕E2,E 1⊕E2) and converges to
Ext•(Eα,Eα). Using the A∞-structure one can make it very explicit. Namely,
let us denote by dα : Ext•(E1⊕E2,E 1⊕E2)→ Ext•(E1⊕E2,E 1⊕E2) the
diﬀerential of degree +1 given by the formula
dα =m2(α,•) +m2(•,α ) +m3(α,•,α ) .
Then the graded vector space Ext •(Eα,Eα) is isomorphic to the cohomology
of dα (cf. e.g. [42], Remark 10.1.5).
It is clear that for any cohomological complex (C•,d ) of ﬁnite-dimensional
vector spaces we have the equality
∑
i≤1
(−1)i dimHi(C)−
∑
i≤1
(−1)i dimCi = rkd(1),
where d(1) : C 1→ C 2 is the component of d. Applying this observation to
our complex we obtain that
(Eα,Eα)≤1− (E1⊕E2,E 1⊕E2)≤1 = rkd(1)
α .
Step 3.
Let us introduce a
k-vector space
ME1,E2 = Ext 1(E1⊕E2,E 1⊕E2) =
= Ext 1(E1,E 1)⊕ Ext1(E2,E 1)⊕ Ext1(E1,E 2)⊕ Ext1(E2,E 2) .
It can be interpreted as the tangent space to the moduli space of formal
deformations of the object E1⊕E2. We choose coordinates ( x,α,β,y ) on
this space in such a way that x denotes the coordinates on Ext 1(E1,E 1),
α denotes the coordinates on Ext 1(E2,E 1), β denotes the coordinates on
Ext1(E1,E 2) and y denotes the coordinates on Ext 1(E2,E 2). Then the point
(0,α, 0, 0) corresponds (by abuse of notation) to the isomorphism cla ss α∈
Ext1(E2,E 1) of an exact triangle E1→Eα→E2. Later we are going to use
98
the integral identity from Section 4.4 applying it to the for mal neighborhood
of the subspace consisting of the points (0 ,α, 0, 0). In order to do that we
will relate the potential of the object Eα with a certain formal function on
ME1,E2.
We may assume that the full subcategory C(E1,E 2) consisting of the pair
of objects E1,E 2 is minimal. As in the case of one object the potential
ofC induces a formal power series WE1,E2 = W (x,α,β,y ) on ME1,E2. It
is deﬁned as the abelianization of a series ∑
n/greaterorequalslant3Wn/n in cyclic paths in
the quiver QE1,E2 with the vertices E1 and E2 and (Ei,Ej)1 edges between
vertices Ei and Ej for i,j ∈ {1, 2}. Since any cyclic path has the same
number of edges in the direction E1→ E2 as in the direction E2→ E1 we
conclude that the potential WE1,E2 is Gm-invariants with respect to the Gm-
action on the graded vector space ME1,E2 with the weights wtx =wty = 0
and wtα =−wtβ = 1. The potential WE1,E2 is obtained from the potential
WE1⊕E2 by a formal change of variables.
It follows from Gm-invariance of WE1,E2 that it belongs to k[α][[x,β,γ ]].
Therefore it deﬁnes a function on the formal neighborhood of the aﬃne sub-
space{(0,α, 0, 0)}⊂M E1,E2. In particular, for any α∈ Ext1(E2,E 1) we
obtain a formal power series WE1,E2,α onME1,E2 which is the Taylor expan-
sion of WE1,E2 at the point (0 ,α, 0, 0). Similarly to the Proposition 7 from
Section 3.3 the series WE1,E2,α becomes (after a formal change of coordinates)
a direct sum Wmin
Eα ⊕QEα ⊕NEα , where QEα is a non-degenerate quadratic
form, NEα is the zero function on a vector subspace, and Wmin
Eα does not
contain terms of degree less than 3 in its Taylor expansion. B y the motivic
Thom-Sebastiani theorem we have
(1−MF 0(WE1,E2,α)) = (1−MF (Eα))(1−MF 0(QEα )) .
Let us consider the quadratic form (( WE1,E2)′′)|(0,α,0,0) onME1,E2, where
(WE1,E2)′′ denotes the second derivative of the potential with respect to the
aﬃne coordinates. It follows from the above discussion that this quadratic
form is equal to the direct sum of QEα and the zero quadratic form.
It is easy to check that
(
((WE1,E2)′′)|(0,α,0,0)
)
(v) is equal to ( d(1)
α v,v ) for
any v∈M E1,E2. Hence QEα can be identiﬁed with the quadratic form on
Im(d(1)
α ) given by ( u, (d(1)
α )−1u).
Step 4.
Recall (see Section 5.2) that for any exact triangle E1→ Eα→ E2 we
have a super line bundle L with a canonically trivialized square:
99
LE1→Eα→E2 = (D≤1,Eα ⊗D−1
≤1,E1⊗D−1
≤1,E2)⊗ (sdet(Ext•(E1,E 2)))−1.
For a split triangle Eα≃E1⊕E2 (i.e. α = 0) this line bundle is canonically
trivialized since
• by deﬁnition, for Eα≃E1⊕E2 we have
D≤1,Eα ≃D≤1,E1⊗D≤1,E2⊗
⊗ sdet(Ext≤1(E1,E 2))⊗ sdet(Ext≤1(E2,E 1)) ,
• by the Calabi-Yau property we have
sdet(Ext≤1(E2,E 1))≃ sdet(Ext/greaterorequalslant2(E1,E 2)) .
Therefore, for any exact triangle E1→Eα→E2 we have an isomorphism
LE1→Eα→E2≃D≤1,Eα ⊗D−1
≤1,E1⊕E2 .
On the other hand, considerations similar to those in Step 2 g ive rise to a
canonical isomorphism
D≤1,Eα ⊗D−1
≤1,E1⊕E2≃ sdet(Im(d(1)
α )) .
One can see that the trivialization (sdet(Im( d(1)
α )))⊗2≃ 1 comes exactly from
the non-degenerate quadratic form QEα . Therefore, for an arbitrary exact
triangle E1→ Eα→ E2 we have an isomorphism of super lines compatible
with the trivializations of squares:
LE1→Eα→E2≃ sdet(Im(d(1)
α )) .
This implies that
I(QEα ) = I(l(E1→Eα→E2)) ,
where l∈J2(Funct (C3,C)) was deﬁned in Section 5.2.
Step 5.
Let us apply the integral identity from Section 4.4 to the pot entialWE1,E2.
We put
V1 := Ext 1(E2,E 1), V2 := Ext 1(E1,E 2), V3 := Ext 1(E1,E 1)⊕ Ext1(E2,E 2).
100
We have: ∫
α∈Ext1(E2,E1)
(1−MF (0,α,0,0)(WE1,E2)) =
= L(E2,E1)1(1−MF 0((WE1,E2)| Ext1(E1,E1)⊕Ext1(E2,E2))) .
On the other hand the LHS of the integral identity is equal to
∫
α∈Ext1(E2,E1)
(1−MF 0(QEα ))(1−MF (Wmin
Eα ) =
=
∫
α∈Ext1(E2,E1)
L
1
2 rkQEα I(QEα )(1−MF (Wmin
Eα )) .
Recall that rk QEα = rk(d(1)
α ) = ( Eα,Eα)≤1− (E1⊕E2,E 1⊕E2)≤1 by
Steps 2 and 3. Then the integral identity becomes the followi ng equality:
∫
α∈Ext1(E2,E1)
L
1
2 ((Eα ,Eα )≤1−(E1⊕E2,E1⊕E2)≤1)I(QEα )(1−MF (Wmin
Eα )) =
= L(E2,E1)1(1−MF 0(Wmin
E1 ⊕Wmin
E2 )) .
Comparing this formula with the one we wanted to prove on Step 1 we
see that they coincide if
I(QEα ) = I(h(Eα))
I(h(E1))I(h(E2)) .
Now using Step 4 we observe that this cocycle condition is equ ivalent to the
main property of the orientation data on exact triangles. Th is concludes the
proof of the Theorem. ■
Deﬁnition 18 LetC be an ind-constructible 3-dimensional Calabi-Yau cat-
egory endowed with polarization, σ∈ Stab(C, cl). We call the collection of
elements (Amot
V ∈R V ) of the completed motivic quantum tori (RV ) (for all
strict sectors V⊂ R2) the motivic Donaldson-Thomas invariant of C.
Let us consider the following unital Q-subalgebra of Q(q1/2):
Dq := Z[q1/2,q−1/2,
(
(qn− 1)−1)
n/greaterorequalslant1].
There is a homomorphism of rings
Dµ → Dq given by the twisted Serre
polynomial. Namely, it maps L1/2↦→q1/2, and on Mµ it is the composition
101
of the Serre polynomial with the involution q1/2 ↦→−q1/2. Therefore, we
have a homomorphism of algebras RΓ →R Γ,q, where RΓ,q is a Dq-algebra
generated by ˆeγ,γ ∈ Γ, subject to the relations
ˆeγ ˆeµ =q
1
2⟨γ,µ⟩ˆeγ+µ, ˆe0 = 1.
Similarly to the motivic case, we have the algebra RV,q associated with any
strict sector V .
The motivic DT-invariants give rise to stability data on the graded Lie
algebra associated with RΓ,q. We will denote by AV,q ∈R V,q the element
corresponding to Amot
V .
