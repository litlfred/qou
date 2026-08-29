---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-013-5-monoidal-module-categories
section_title: "Monoidal module categories"
section_number: 5
pages: 20-22
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
GivenC,B tensor categories. We shall deﬁne what means that a tensor
categoryC acts onB.
Deﬁnition 5.1. We callB a monoidal left C-module category ifB is a left
C-module category, with action given by ⊲ :C×B→B , such that 1⊲ 1≃ 1,
and there are natural isomorphisms lX,B : X ⊲B ≃−−→(X ⊲1)⊗B, for any
X∈C , B∈B , such that
(5.1) l1,B = id B, l X,1 = id X⊲1,
(5.2)
X⊲ (Y ⊲B)
(X⊲ 1)⊗ (Y ⊲B)
(X⊲ 1)⊗ ((Y ⊲1)⊗B)
((X⊲ 1)⊗ (Y ⊲1))⊗B
(X⊲ (Y ⊲1))⊗B
((X⊗Y )⊲ 1)⊗B
(X⊗Y )⊲B
lX,Y ⊲B
idX⊲1⊗lY,B
∼
m−1
X,Y,B
lX⊗Y,B
mX,Y,1⊗idB
lX,Y ⊲1⊗id B
for any X,Y ∈C , B∈B . Similarly, we shall say that B is a monoidal
rightC-module category, with action ⊳ :B×C→B , such that
1⊳ 1≃ 1,
and there are natural isomorphisms lB,X : B⊳X → B⊗(1⊳X ), such that
for any X,Y ∈C , B∈B
(5.3) lB,1 = id B, l 1,X = id 1⊳X,
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 21
(5.4)
(B⊳X )⊳Y
(B⊳X )⊗ (1⊳Y )
(B⊗ (1⊳X ))⊗ (1⊳Y )
B⊗ ((1⊳X )⊗ (1⊳Y ))
B⊗ ((1⊳X )⊳Y ))
B⊗ (1⊳ (X⊗Y ))
B⊳ (X⊗Y )
lB⊳X,Y
lB,X ⊗id1⊳Y
∼
˜m−1
B,X,Y
lB,X ⊗Y
idB ⊗ ˜m1,X,Y
id B⊗l1⊳X,Y
Example 5.2. (i) Any tensor category C is a monoidal vect k-module
category, with the canonical action
• : vect k×C→C .
(ii) Let C be a tensor category. Any tensor subcategory D acts onC by
X⊲Y =X⊗Y.
In particular any tensor category acts on itself.
(iii) Let ( C,σ ) be a braided tensor category and D ⊆ Cbe a tensor
subcategory. Then Drev acts onC as
X⊲Y =Y⊗X.
In this case lX,B =σB,X .
(iv) Let C be a tensor category and C ∈C be a coalgebra. Then the
category CC, of left C-comodules inC, is a right C-module category.
The action is given as follows. If ( W,ρ )∈ CC, then W ⊳Y =W⊗Y ,
where the coaction on W⊗Y is given by ρ⊗id Y.
Deﬁnition 5.3. IfB,B′ are right monoidalC-module categories, a monoidal
module functor is a collection ( F,c,ξ ) :B→B ′ where (F,c ) is a C-module
functor, (F,ξ ) is a monoidal functor and equation
(5.5) lF (B),V cB,V = (id F (B)⊗c1,V )ξ−1
B,1⊳VF (lB,V ),
22 LENTNER AND MOMBELLI
is fulﬁlled, for any B∈B , V∈C .
