---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-017-61-coalgebras-constructed-from-a-coend
section_title: "Coalgebras constructed from a coend"
section_number: 6.1
pages: 26-30
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
andB be a rightC-module category. For the rest of this section, ( F,c ) :B→
C will denote a right exact module functor.
Consider the functor
SF :Bop×B→C ,
SF (A,B ) = F (B)⊗∗F (A).
This functor has a canonical prebalancing, given by
βX
A,B :F (B)⊗∗F (A⊳X )→F (B⊳ ∗X)⊗∗F (A),
βX
A,B = (c−1
B,∗X⊗id ∗F (A))(id F (B)⊗(φl
F (A),X )−1∗(c−1
A,X )).
(6.1)
We deﬁne
C(F,c ) = C(F ) =
∮ B∈B
(SF,β ) =
∮ B∈B
F (B)⊗∗F (B).
LetπB :F (B)⊗∗F (B)→C(F ) be the associated dinatural transformations.
Existence of this coend follows from Corollary 3.8. The following Lemma is
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 27
a generalization of [ 22, Lemma 2.1.9]. Recall that, for any M,N ∈B ,X∈C
we have natural isomorphisms
ψV
F (M ),F (N ) : HomC(F (M )⊗∗F (N ),V )→ HomC(F (M ),V⊗F (N ))
described in ( 2.7).
Lemma 6.1. The functor V ↦→Natm(F,V⊗F ) is represented by C(F ).
That is, for any V ∈C there are natural isomorphisms
ω : Hom C(C(F ),V )→ Natm(F,V⊗F ),
ω(g)B = (g⊗id F (B))ψC(F )
F (B),F (B)(πB).(6.2)
Proof. Fix some object V ∈C . The functor V⊗F is a right module functor,
then we can consider the prebalancing of the functor
HomC(F (−),V⊗F (−)) :B×B op→ vect k,
given by
γX
B,N : Hom C(F (N ⊳∗X),V⊗F (B))→ HomC(F (N ),V⊗F (B⊳X )),
γX
N,B (f ) = (id V⊗cB,X )(f⊗id X)(c−1
N,∗X⊗id X)(id F (N )⊗coevX ).
Note that here we are considering Bop as a left C-module category, with
action X ⊲ B:= B ⊳∗X. Proposition 3.3 (ii) tells us that there is an
isomorphism
∮
B∈B
(HomC(F (B),V⊗F (B)),γ )≃ Natm(F,V⊗F ).
From the proof of Proposition 3.4, one can see that the dinatural transfor-
mations of the end
∮
B∈B HomC(F (B)⊗∗F (B),V ) are given by
ˆπB :
∮
B∈B
HomC(F (B)⊗∗F (B),V )→ HomC(F (B)⊗∗F (B),V ),
ˆπB(g) = g◦πB.
Here, we are using identiﬁcation
∮
B∈B
HomC(F (B)⊗∗F (B),V ) = Hom C(
∮ B∈B
F (B)⊗∗F (B),V ).
It follows by a straightforward computation that
γX
M,N (ψV
F (M ⊳∗X),F (N )(f )) = ψV
F (M ),F (N ⊳X)(f◦βX
N,M ),
for any M,N ∈B and any f∈ HomB(F (M⊳ ∗X)⊗∗F (N ),V ). This implies,
using Proposition 3.3 (i) that, for any V∈C , there exists an isomorphism
ˆψV :
∮
B∈B
HomC(F (B)⊗∗F (B),V )→
∮
B∈B
HomC(F (B),V⊗F (B)),
28 LENTNER AND MOMBELLI
such that µB◦ ˆψV =ψV
F (B),F (B)◦ ˆπB. For any V∈C we have that
HomC(C(F ),V )≃
∮
B∈B
HomC(F (B)⊗∗F (B),V )
≃
∮
B∈B
HomC(F (B),V⊗F (B))
≃ Natm(F,V⊗F ).
The ﬁrst isomorphism is Proposition 3.4. Tracing this chain of isomorphisms,
one can see that, the composition coincides with ω deﬁned by Equation
(6.2). □
Proposition 6.2. LetC be a tensor category, and B be a right C-module
category. Let (F,c ) : B→C be a right exact module functor. The object
C(F )∈C has a coalgebra structure ∆ : C(F )→C(F )⊗C(F ),ε :C(F )→ 1
determined by diagramms
(6.3) F (B)⊗∗F (B)
id ⊗coevF (B)⊗id
/d15/d15
πB /d47/d47C(F )
∆
/d15/d15
F (B)⊗∗F (B)⊗F (B)⊗∗F (B) πB⊗πB
/d47/d47C(F )⊗C(F ),
(6.4) F (B)⊗∗F (B)
πB /d47/d47
evF (B)
/d37/d37▲▲▲▲▲▲▲▲▲▲▲ C(F )
ε
/d125/d125③③③③③③③③
1,
for any B∈B .
Proof. It follows by a straightforward computation that, the maps
evF (B) :F (B)⊗∗F (B)→ 1,
(πB⊗πB)(id⊗coevF (B)⊗id ) :F (B)⊗∗F (B)→C(F )⊗C(F ),
are dinatural maps. It follows from Diagram ( 2.20) that ev F (B) satisﬁes
(3.5). It follows from Diagram ( 2.21) and the fact that π satisﬁes ( 3.5)
that, (πB⊗πB)(id⊗coevF (B)⊗id ) also satisﬁes Equation ( 3.5). Whence, the
existence of ∆ and ε follow from the universal property of the relative coend.
The proof that (C(F ), ∆ ,ε ) is a coalgebra is standard, and it follows from
Diagrams ( 6.3), ( 6.4). □
LetC be a tensor category and C∈C be a coalgebra. The category CC,
of left C-comodules in C, is a right C-module category. The action is given
as follows. If ( W,ρ )∈ CC, then W ⊳Y = W⊗Y , where the coaction on
W⊗Y is given by ρ⊗id Y. The forgetful functor f : CC→C is a C-module
functor. The next result says that the coalgebra reconstruc ted from the
forgetful functor f coincides with C.
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 29
In this case, the functor Sf has a prebalancing given by
βX
A,B = id B⊗(φl
A,X )−1,
for any A,B ∈ CC, X∈C .
Lemma 6.3. There exists an isomorphism of coalgebras C(f )≃C inC.
Proof. In this particular case, if T∈C is an object, and λW :W⊗∗W→T
is a dinatural transformation, Equation ( 3.5) writes as
(6.5) λW ⊗∗V (id W⊗(φl
W ⊗∗V,V )−1) = λW (id W⊗∗(id W⊗coevV )),
for any W∈ CC,V ∈C .
If W ∈ CC has comodule structure given by ρW → C⊗W , then we de-
ﬁne πW : W⊗∗W → C, the morphisms given by πW = ¯ψC
W,W (ρ). Recall
that, natural isomorphisms ¯ψ were deﬁned in ( 2.8). Maps πW are dinatural
transformations, and they satisfy Equation ( 6.5).
Let A∈C be another object, equipped with dinatural transformation s
λW : W⊗∗W → A such that they satisfy Equation ( 6.5). Deﬁne h as the
composition
h :C id C ⊗∗ε
−−−−−→C⊗∗C
λC
−−→A.
Since λ is dinatural, and it satisﬁes ( 6.5), one can see that h◦πW = λW .
This proves that, indeed, C(f )≃C. □
Proposition 6.4. LetB be a right C-module category, and (F,c ) : B→C
be a right exact module functor. Set C = C(F ) the coalgebra deﬁned in
Proposition 6.2.
1. The functor (F,c ) :B→C factorizes as
(6.6) CC
f
/d32/d32❆❆❆❆❆❆❆❆
B
ˆF
/d62/d62⑥⑥⑥⑥⑥⑥⑥⑥
F
/d47/d47C.
Here f : CC →C is the forgetful functor, and the functor ˆF is a
C-module functor.
2. If F is exact (respect. faithful) then ˆF is exact (respect. faithful).
Proof. 1. For any A∈B , deﬁne ˆF (A) = (F (A),ρ A), where
ρA =ψC
F (A),F (A)(πA) : F (A)→C⊗F (A).
Using diagrams ( 6.3), ( 6.4), one can prove that
(id C⊗ρA)ρA = (∆⊗id )ρA,
(ε⊗id )ρA = id F (A).
30 LENTNER AND MOMBELLI
2. Clearly, if F is faithful, then ˆF is faithful. Assume that F is left exact.
Let f : A→ B be a morphism in B with kernel k = kerf : K→ A. Since
F is left exact, then, F (k) = ker F (f ). We only need to prove that, the
morphismF (k) : F (K)→F (A) is a map of C-comodules. That is, we need
to prove the equality
(6.7) (id ⊗F (k))ψC
F (K),F (K)(πK ) = ψC
F (A),F (A)(πA)F (k).
Using the naturality of ψ, it follows that
ψC
F (A),F (A)(πA)F (k) = ψC
F (K),F (A)(πA(F (k)⊗id ))
=ψC
F (K),F (A)(πK (id⊗∗F (k)))
= (id⊗F (k))ψC
F (K),F (K)(πK).
The second equality follows from the dinaturality of π, the third equality
follows again by the naturality of ψ. The proof that, if F is right exact,
then ˆF is right exact, follows similarly. □
