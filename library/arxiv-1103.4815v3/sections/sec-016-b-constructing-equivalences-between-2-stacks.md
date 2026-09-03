---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-016-b-constructing-equivalences-between-2-stacks
section_title: "B Constructing Equivalences between 2-Stacks"
section_number: null
pages: 59-62
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
Let C be a bicategory (we assume that associators and uniﬁers are invertible 2-morphisms). We
ﬁx the following terminology: a 1- isomorphism f : X1 /d47/d47 X2 in C always includes the data of
an inverse 1-morphism ¯f : X2 /d47/d47 X1 and of 2-isomorphisms i : ¯f ◦f /d43/d51 id and j : id /d43/d51 f ◦ ¯f
satisfying the zigzag identities. Let D be another bicategory. A 2-functor F : C /d47/d47 D is assumed
to have invertible compositors and unitors.
The following lemma is certainly “well-known”, although we have not bee n able to ﬁnd a refer-
ence for exactly this statement.
– 59 –
Lemma B.1. LetF : C /d47/d47 D be a 2-functor that is fully faithful on Hom-categories. Sup pose one
has chosen:
1. for every object Y ∈ D an object GY ∈ C and a 1-isomorphism ξY :Y /d47/d47 F (GY ).
2. for all objects X1,X 2 ∈ C and all 1-morphisms g : F (X1) /d47/d47 F (X2), a 1-morphism Gg :
X1 /d47/d47 X2 in C together with a 2-isomorphism ηg :g /d43/d51 F (Gg). 1
Then, there is a 2-functor G : D /d47/d47 C and pseudonatural equivalences
a : id D /d43/d51 F ◦G and b :G ◦F /d43/d51 idC.
In particular, F is an equivalence of bicategories.
Proof. We recall our convention concerning 1-isomorphisms: the 1 -isomorphisms ξY include
choices of inverse 1-morphisms ¯ξY together with 2-isomorphisms iY : ¯ξY ◦ξY /d43/d51 id and jY :
id /d43/d51 ξY ◦ ¯ξY satisfying the zigzag identities.
First we explicitly construct the 2-functor G. On objects, we put G(Y ) := GY . We use the
notation ˜g := (ξY2 ◦g) ◦ ¯ξY1 for all 1-morphisms g : Y1 /d47/d47 Y2 in D, and deﬁne G(g) = G˜g. If
g,g ′ :Y1 /d47/d47 Y2 are 1-morphisms, and ψ :g /d43/d51 g′ is a 2-morphism, we consider the 2-morphism
˜ψ deﬁned by
F (G˜g)
η −1
˜g /d43/d51 (ξY2 ◦g) ◦ ¯ξY1
(id◦ψ )◦id /d43/d51 (ξY2 ◦g′) ◦ ¯ξY1
η ˜g′
/d43/d51F (G˜g′ ).
Since F is fully faithful on 2-morphisms, we may choose the unique 2-morphis m G(ψ) :
G(g) /d43/d51 G(g′) such that F (G(ψ)) = ˜ψ. In order to deﬁne the compositor of G we look at 1-
morphisms g12 :Y1 /d47/d47 Y2 and g23 :Y2 /d47/d47 Y3. We consider the 2-morphism
F (G(g23) ◦G(g12))
c−1
G(g12 ),G (g23 )
/d43/d51F (G˜g23 ) ◦F (G˜g12 )
η −1
˜g23 ◦η −1
˜g12/d11/d19
((ξY3 ◦g23) ◦ ¯ξY2 ) ◦ ((ξY2 ◦g12) ◦ ¯ξY1 )
a,i Y2
/d11/d19
(ξY3 ◦ (g23 ◦g12)) ◦ ¯ξY1 η ~g23 ◦g12
/d43/d51F (G(g23 ◦g12));
its unique preimage under the 2-functor F is the compositor
cg12,g 23 :G(g23) ◦G(g12) /d43/d51 G(g23 ◦g12).
In order to deﬁne the unitor of G we consider an object Y ∈ D and look at the 2-morphism
F (G(idY ))
η −1
~idY /d43/d51 (ξY ◦ idY ) ◦ ¯ξY
lξ Y,j −1
Y /d43/d51 idF (G(Y ))
u−1
G(Y )
/d43/d51F (idG(Y )).
1More accurately we should write GX1,X2,g and ηX1,X2,g, but we will suppress X1 and X2 in the notation.
– 60 –
Its unique preimage under the 2-functor F is the unitor uY :G(idY ) /d43/d51 idG(Y ). The second step
is to verify the axioms of a 2-functor. This is simple but extremely ted ious and can only be left as
an exercise. The third step is to construct the pseudonatural tr ansformation
a : id D /d43/d51 F ◦G.
Its component at an object Y in D is the 1-morphism a(Y ) := ξY :Y /d47/d47 F (G(Y )). Its component
at a 1-morphism g :Y1 /d47/d47 Y2 is the 2-morphism a(g) deﬁned by
a(Y2) ◦g ξY2 ◦g
id◦l−1
ξ Y2 ◦g
/d11/d19
(ξY2 ◦g) ◦ id
a,i −1
Y2/d11/d19
((ξY2 ◦g) ◦ ¯ξY1) ◦ξY1
η ˜g ◦id
/d11/d19
F (G˜g) ◦ξY1 F (G(g)) ◦a(Y1).
There are two axioms a pseudonatural transformation has to sat isfy, and their proofs are again left
as an exercise. It is easy to see that a is a pseudonatural equivalence, with an inverse transformation
given by ¯a(Y ) := ¯ξY . The fourth and last step is to construct the pseudonatural tra nsformation
b :G ◦F /d43/d51 idC.
Its component at an object X isb(X) := G ¯ξF (X) :G(F (X)) /d47/d47 X. Its component at a 1-morphism
f : X2 /d47/d47 X2 is the 2-morphism
b(f ) : b(X2) ◦G(F (f )) /d43/d51 f ◦b(X1)
given as the unique preimage under F of the 2-morphism
F (b(X2) ◦G(F (f ))) c−1
/d43/d51F (b(X2)) ◦F (G(F (f )))
η −1
¯ξ F (X2 )
◦η −1
F (f )
/d11/d19
¯ξF (X2) ◦ ((ξF (X2) ◦F (f )) ◦ξF (X1))
a,i F (X2 ),r
/d11/d19
F (f ) ◦ ¯ξF (X1)
idF (f )◦η ¯ξ F (X1 )
/d11/d19
F (f ) ◦F (b(X1)) c
/d43/d51F (f ◦b(X1)).
The proofs of the axioms are again left for the reader, and again it is easy to see that b is a
pseudonatural equivalence with an inverse transformation given by ¯b(X) := GξF (X) . □
As a consequence of Lemma B.1 we obtain the certainly well-known res ult:
– 61 –
Corollary B.2. Let F : C /d47/d47 D be essentially surjective, and an equivalence on all Hom-
categories. Then, F is an equivalence of bicategories.
Since we work with 2-stacks over manifolds, we need the following “st acky” extension of Lemma
B.1. For a pre-2-stack C, we denote by CM the 2-category it associates to a smooth manifold M , and
byψ∗ : CN /d47/d47 CM the 2-functor it associates to a smooth map ψ :M /d47/d47 N . The pseudonatural
equivalencesψ∗ ◦ϕ∗ ∼= (ϕ ◦ψ)∗ will be suppressed from the notation in the following. If C and D
are pre-2-stacks, a 1-morphism F : C /d47/d47 D associates 2-functors FM : CM /d47/d47 DM to a smooth
manifold M , pseudonatural equivalences
Fψ :ψ∗ ◦FN /d47/d47 FM ◦ψ∗
to smooth maps ψ : M /d47/d47 N , and certain modiﬁcations Fψ,ϕ that control the relation between
Fψ and Fϕ for composable maps ψ and ϕ.
Lemma B.3. Suppose C and D are pre-2-stacks over smooth manifolds, and F : C /d47/d47 D is a
1-morphism. Suppose that for every smooth manifold M
1. the assumptions of Lemma B.1 for the 2-functor FM are satisﬁed and
2. the data (GY,ξY ) and (Gg,ηg) is chosen for all objects Y and 1-morphisms g in DM .
Then, there is a 1-morphism G : D /d47/d47 C of pre-2-stacks together with 2-isomorphisms
a :F ◦G /d43/d51 idD and b :G ◦F /d43/d51 idC
such that for every smooth manifold M the 2-functor GM and the pseudonatural transformations
aM and bM are the ones of Lemma B.1. In particular, F is an equivalence of pre-2-stacks.
For the proof one constructs the required pseudonatural equiv alencesGψ and the modiﬁcations
Gψ,ϕ from the given ones, Fψ and Fψ,ϕ , respectively, in a similar way as explained in the proof of
Lemma B.1. Since these constructions are straightforward to do b ut would consume many pages,
and the statement of the lemma is not too surprising and certainly we ll-known to many people, we
leave these constructions for the interested reader.
