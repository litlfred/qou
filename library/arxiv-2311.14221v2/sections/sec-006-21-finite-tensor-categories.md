---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-006-21-finite-tensor-categories
section_title: "Finite tensor categories"
section_number: 2.1
pages: 6-7
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
rigid category, with simple unit object 1∈C . We refer to [ 10] for more details
on ﬁnite tensor categories. Without loss of generality, we s hall assume that
tensor categories in this work are strict.
IfC,D are monoidal categories, a monoidal functor is a functor F :C→D
equipped with natural isomorphisms
ξA,B :F (A)⊗F (B)→F (A⊗B),
such that
(2.1) ξA,B⊗C(id F (A)⊗ξB,C ) = ξA⊗B,C (ξA,B⊗id F (C)).
If (F,ξ ), ( ~F, ~ξ) : C → Dare two monoidal functors, a monoidal natural
transformation between F and ~F is a natural transformation α : F → ~F
such that
(2.2) αA⊗BξA,B = ~ξA,B(αA⊗αB),
for any A,B ∈C .
IfC is a category, for any X∈C we shall denote by
evX :X ∗⊗X→ 1, coevX : 1→X⊗X ∗
the evaluation and coevaluation. By abuse of notation, we sh all also denote
by
evX :X⊗∗X→ 1, coevX : 1→ ∗X⊗X
the evaluation and coevaluation for the left duals. We will u se the following
basic result. If f :X→Y is an isomorphism in C then
(id ∗X⊗f )coevX =(∗f⊗id Y )coevY,
evY (f⊗id Y ) =ev X(id X⊗∗f ).(2.3)
It is well known that for any pair of objects X,Y ∈C there are canonical
natural isomorphisms
(2.4) φr
X,Y :Y ∗⊗X ∗→ (X⊗Y )∗,
(2.5) φl
X,Y : ∗Y⊗∗X→ ∗(X⊗Y ).
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 7
These isomorphisms allow us to compute coevaluation and eva luation maps
of duals; more precisely we shall need the following identit y
(2.6) ev ∗V = ∗(coevX)φl
∗X,X.
We are going to make use, very often, of the canonical natural isomor-
phisms
ψZ
X,Y : HomB(X⊗∗Y,Z )→ HomB(X,Z⊗Y ),
ψZ
X,Y (f ) = (f⊗id Y )(id X⊗coevY ).
(2.7)
And its inverse
¯ψZ
X,Y : Hom B(X,Z⊗Y )→ HomB(X⊗∗Y,Z )
¯ψZ
X,Y (g) = (id Z⊗evY )(g⊗id ∗Y ).
(2.8)
We shall also need the following basic fact.
Lemma 2.1. For any pair V,W ∈C the evaluation of V⊗W is given by
(2.9) evV ⊗W = evV (id V⊗evW⊗id ∗V )(id V ⊗W⊗(φl
V,W )−1). □
