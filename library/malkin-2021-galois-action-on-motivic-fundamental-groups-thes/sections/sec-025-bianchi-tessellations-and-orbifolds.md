---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "ThemainmotiveofthisthesisistostudytheactionofthemotivicGaloisgrouponthemotivicfundamental group of an algebraic curve- punctured at a ﬁnite set of points(: GalMot ⟳cMot 1 (-−(,E 0)"
section_id: sec-025-bianchi-tessellations-and-orbifolds
section_title: "Bianchi tessellations and orbifolds"
section_number: null
pages: 101-103
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
doc_brief: "ThemainmotiveofthisthesisistostudytheactionofthemotivicGaloisgrouponthemotivicfundamental group of an algebraic curve- punctured at a finite set of points(: GalMot ⟳cMot 1 (-−(,E 0). (1) — On the"
---
Deﬁnition
Let = Q[
√
−3] be an imaginary quadratic ﬁeld with lattice of integersO. TheBianchi tessellation([B4])
is an ideal polyhedral tessellation of the upper half-spaceH3 associated withO, whose cell complex has a
natural structure of a complex ofGL2(O)-modules. We deﬁne it now.
LetF be the space of positive semideﬁnite Hermitian forms on(O 2⊗O C)∗. The subsetF of positive
deﬁnite forms is a dense open subset ofF. We identifyH3 and its compactiﬁcationH
3
= H3∪ P1(C) with
therealprojectivizationsof F andF,respectively. Theactionof GL2(C) on C2 providesanactionon F that
descends to an action onH
3
.
EveryE∈O 2 provides a positive semideﬁnite form|⟨−,E⟩| 2∈mF. The convex hull of the set
{
|⟨−,E⟩| 2 :E a primitive vector inO2}
is a polyhedron inF with vertices on the boundary. The polyhedron projects to an ideal tessellation ofH3
with vertices onP1(O)⊂ P1(C). Let• be the polyhedral cell complex overZ of this ideal tessellation. We
will shift this complex in degree so that the space of8-dimensional cells it in degree3−8 (8= 0, 1, 2, 3). We
get a cohomological complex
0 m
− →1 m
− →2 m
− →3.
The group GL2(O) acts on the Bianchi tessellation, giving• the structure of a complex of leftGL2(O)
modules.
The quotientGL2(O)\ H3 is a ﬁnite-volume hyperbolic threefold with cusps in bijection with the ideal
class group ofO. If Γ is a ﬁnite-index subgroup ofGL2(O), the quotientΓ\ H3 is also a ﬁnite-volume
hyperbolic threefold with a ﬁnite map toGL2(O)\ H3.
93
A rightGL2(O)-module) provides a local system onΓ\ H3, which we also denote by). Then the chain
complex ofGL2(O)\ H3 with coeﬃcients in) is
)⊗Γ• (Z[Γ\ GL2(O)]⊗ ))⊗GL2(O) •. (3.14)
The Gaussian and Eisenstein cases
Following [G8], for3= 1(O= Z[8]) and3= 3(O= Z[d]) we have the following description of the Bianchi
complexes in degrees 1 and 2.
The action ofGL2(O) is transitive on the8-dimensional cells for each8. Choose GL2(O)-generators

8∈ 8: we may take

1= (the ideal triangle(1, 0,∞))

2= (the geodesic(0,∞))
where(E1,...,E =),E8∈ P1(O) = P(+ 2(O)), denotes the oriented cell with ideal vertices atE1,...,E = under
the identiﬁcation ofP1(C) with the boundary ofH
3
. Let8 be the subgroup ofGL2(O) stabilizing
8.
The group1 stabilizing the triangle(0, 1,∞) is isomorphic to
(3×O×.
Theﬁrstcomponent(3 actson(E,F)∈O⊕O bypermutationsofthetriple (E,F,−E−F),i.e.,thegenerators
of(3 are represented by
(123)7→
'››
«
0 −1
1 −1
“ﬁﬁ
‹
, (12)7→
'››
«
0 1
1 0
“ﬁﬁ
‹
.
The second component acts by scalars. There is a sign homomorphismj1 : 1→ Z keeping track of the
action of1 on the orientation, withj1(( 123)) = 1 andj1(( 12)) =−1. So the space of 2-cells is
1= Z[
! 2(O)]⊗ 1 j1.
The group2 stabilizing the geodesic(0,∞) is isomorphic to
(2 ⋉(O××O×),
with(2actingonO××O×bypermutationofthefactors. Thenontrivialelementof (2actsby(E,F)7→( F,E)
94
andO××O× acts diagonally. There is a sign homomorphismj2 :2→ Z, and the space of 1-cells is
2= Z[
! 2(Z[8])]⊗ 2 j2.
Letpbeaprimeidealin O. Thegroup GL2(O) actsonthequotient (Z[8]/p)2. LetΓ1(p) bethestabilizer
in GL2(O) of the vector(0, 1)∈ (Z[8]/p)2. The action on the vector(0, 1) provides an isomorphism of
GL2(O)-modules
Z[Γ1(p)\ GL2(O)]  Z[F2
p− 0], Fp=O/p.
The chain complex (3.14) ofΓ1(p)\ H3 with coeﬃcients in a local system) is then identiﬁed in degrees
1 and 2 with
)⊗Γ1(p) • (Z[Γ1(p)\ GL2(O)]⊗ ))⊗GL2(O) •

(
Z[F2
p− 0]⊗ )
)
⊗GL2(O)
(Z[GL2(O)]⊗ • j•
).
This space is generated in degree8 by elements
((U,V)⊗ C)⊗( 
8), (U,V)∈ F2
p− 0, C ∈).
