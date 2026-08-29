---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-012-42-yetter-drinfeld-modules
section_title: "Yetter-Drinfeld modules"
section_number: 4.2
pages: 18-20
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
HYD(vect k) is a left
H-module· :H⊗kV→V , and a left H-comoduleλ :V →H⊗kV such that
(4.8) λ(h·v) = h(1)v(−1)S(h(3))⊗h(2)·v(0),
for any h∈H,v ∈V . If V ∈ H
HYD(vect k), the map σX :V⊗kX→X⊗kV ,
given by σX (v⊗x) = v(−1)·x⊗v(0) is a half-braiding for V .
This notion had been generalized in [ 5] to Hopf algebrasH inside a braided
tensor categoryC:
Deﬁnition 4.4. Let H be a Hopf algebra in a braided tensor category C.
Then an H-H-Yetter-Drinfeld module V is an object V ∈C , together with
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 19
a structure of H-module m : H⊗V → V and structure of H-comodule in
ρ :V →H⊗V in the tensor category C, compatible in the following way
H
H
V
V
=
H
H
V
V
The category H
HYD(C) consists of Yetter-Drinfeld modules and of H-linear
and H-colinear morphisms. It becomes a tensor category with the u sual
tensor product of H-modules and H-comodules V⊗W . An useful feature
of this tensor category is that, it admits, by construction, a braiding
c(V,mV ,ρV ),(W,mW ,ρW ) :V⊗W→W⊗V
which is given on objects ( V,m V,ρ V ) and (W,m W,ρ W ) by
c(V,mV ,ρV ),(W,mW ,ρW ) := (ρW⊗ id V )◦ (id H⊗cV,W )◦ (ρV⊗ id W )
and is invertible if H has a bijective antipode
(c(V,mV ,ρV ),(W,mW ,ρW ))−1 :=c−1
V,W◦ (mW⊗ id V )◦ (c−1
H,W⊗ id V )
◦ (id W⊗S−1⊗ id V )◦ (id W⊗ρV ).
IfC is rigid, then the dual object in C with the standard dual action and
coaction gives a dual object in H
HYD(C). The structure is summarized in
the following statement proven in [ 5]:
Theorem 4.5. LetH be a Hopf algebra in C. The Yetter-Drinfeld modules
over H inC have a natural structure of a braided tensor category H
HYD(C).
IfC is rigid, then so is H
HYD(C).
Recall that the Drinfeld center Z(B) is a braided tensor category associ-
ated to any tensor category B. The construction of Yetter-Drinfeld modules
gives a realization of a special case of the construction of a relative Drinfeld
centerZC(B), a braided tensor category associated to any tensor catego ry
B with a braided subcategory C֒Z (B). More precisely we have
H
HYD(C) =ZC(HC)
20 LENTNER AND MOMBELLI
