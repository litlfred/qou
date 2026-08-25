---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-008-23-the-internal-hom
section_title: "The internal Hom"
section_number: 2.3
pages: 9-10
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
module category. For any pair of objects M,N ∈M , the internal Hom is
an object Hom (M,N )∈C representing the left exact functor
HomM(−⊲M,N ) :Cop→ vect k.
10 LENTNER AND MOMBELLI
This means that, there are natural isomorphisms
HomC(X, HomM(M,N ))≃ HomM(X⊲M,N ).
The internal Hom for right C-module categories is deﬁned similarly.
The next technical result will be needed later. Recall natur al isomor-
phisms φl deﬁned in ( 2.5).
Lemma 2.2. LetM be a right C-module category with action given by
⊳ :M×C →M . If (F,c ) : M→C is a module functor, then, for any
B∈M , X∈C , the following diagrams commute.
(2.20)
(F (B)⊗X)⊗∗(F (B)⊗X)
F (B⊳X )⊗∗F (B⊳X ) ( F (B)⊗X)⊗(∗X⊗∗F (B))
1
id⊗(φl
F (B),X )−1cB,X ⊗∗c−1
B,X
evF (B⊳X ) evF (B)(id⊗evX ⊗id)
(2.21)
(∗X⊗∗F (B))⊗(F (B)⊗X)
∗F (B⊳X )⊗F (B⊳X ) ∗(X⊗F (B))⊗(F (B)⊗X)
1
∗cB,X ⊗c−1
B,X φl
F (B),X ⊗id
coevF (B⊳X ) (id⊗coevF (B)⊗id)coevX
Proof. The proof follows, by simply checking that morphisms
evF (B⊳X ) = ev F (B)
(
id⊗evX⊗id
)(
cB,X⊗(∗cB,Xφl
F (B),X )−1)
,
coevF (B⊳X ) =
( ∗cB,Xφl
F (B),X⊗c−1
B,X
)(
id⊗coevF (B)⊗id
)
coevX,
satisfy rigidity axioms. □
