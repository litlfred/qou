---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-015-52-some-natural-module-transformations
section_title: "Some natural module transformations"
section_number: 5.2
pages: 24-26
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
transformations between additive functors are additive. F or example, if
(F,ξ ) is an additive monoidal functor, then, natural isomorphis ms
ξA,B :F (A)⊗F (B)→F (A⊗B),
are additive in each variable. In this section, we shall stud y what happens
whenF is a monoidal module functor. We aim at proving that ξ is a module
natural transformation in the second variable.
Lemma 5.8. If B is a right monoidal C-module category, then for any
A∈B , the functor LA :B→B , LA(B) = A⊗B is a C-module functor.
Proof. For any B∈B ,V ∈C , the module structure of the functor LA is
given by
ηB,V :A⊗(B⊳V )→ (A⊗B)⊳V,
ηB,V =l−1
A⊗B,V (id A⊗lB,V )
Let us prove that η satisﬁes ( 2.18). Using that isomorphisms l satisfy dia-
gram ( 5.4), it follows that for any C∈B and any V,W ∈C we have that
(5.7) l−1
C,V ⊗W =l−1
C⊳V,W (l−1
C,V⊗id 1⊳W )(id C⊗l1⊳V,W ).
On one hand we have that
ηB,V ⊗W =l−1
A⊗B,V ⊗W (id A⊗lB,V ⊗W )
=l−1
(A⊗B)⊳V,W (l−1
A⊗B,V⊗id 1⊳W )(id A⊗B⊗l1⊳V,W )(id A⊗B⊗l−1
1⊳V,W )
(id A⊗lB,V⊗id 1⊳W )(id A⊗lB⊳V,W )
=l−1
(A⊗B)⊳V,W (l−1
A⊗B,V⊗id 1⊳W )(id A⊗lB,V⊗id 1⊳W )(id A⊗lB⊳V,W )
The second equation follows from using ( 5.7). On the other hand
(ηB,V ⊳ id W )ηB⊳V,W
is equal to
=(l−1
A⊗B,V ⊳ id W )(id A⊗lB,V⊗id 1⊳W )l−1
A⊗(B⊳V ),W (id A⊗lB⊳V,W )
=(l−1
A⊗B,V ⊳ id W )l−1
A⊗B⊗(1⊳V ),W (id A⊗lB,V⊗id 1⊳W )(id A⊗lB⊳V,W )
=l−1
(A⊗B)⊳V,W (l−1
A⊗B,V⊗id 1⊳W )(id A⊗lB,V⊗id 1⊳W )(id A⊗lB⊳V,W ).
The second and third equalities follow from the naturality o f l. □
Proposition 5.9. Assume that B is a monoidal right C-module category
and (F,c,ξ ) :B→C a monoidal module functor. The following assertions
hold.
(i) The categoryB has structure of C-bimodule category.
(ii) There areC-module funtors
H, ~H :B ⊠CB→C ,
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 25
such that
H(A ⊠B) = F (A⊗B), ~H(A ⊠B) = F (A)⊗F (B),
for any A,B∈B .
(iii) The monoidal structure of the functor F deﬁnes a natural module
isomorphism ξ : ~H→H.
Proof. (i). From Proposition 5.6 there is a section G :C→B of the functor
F . Deﬁne the left action ⊲ :C×B→B as V ⊲B = G(V )⊗B. With this
actionB becomes aC-bimodule category. Thus, we can consider the Deligne
tensor product overC,B ⊠CB. This category has an obvious right C-module
category structure.
One can prove that functors B×B→C given by
(A,B )↦→F (A⊗B), (A,B )↦→F (A)⊗F (B),
areC-balanced, thus deﬁning functors H and ~H. The (right) C-module
structure of the functor ~H is the one inherited from the functor F . The
module structure of the functor H is more involved. One can prove that
natural transformations
eA,B,V :F (A⊗(B⊳V ))→F (A⊗B)⊗V,
eA,B,V =cA⊗B,VF (l−1
A⊗B,V (id A⊗lB,V ))
areC-balanced, thus deﬁning natural transformations
eX,V :H(X⊳V )→H(X)⊳V,
for any X∈B ⊠CB, V ∈C . One can prove also that ( H,e ) is a module
functor. Note that e is the module structure resulting from the composition
of module structures of F and the functor LA, presented in Lemma 5.8. This
proves (ii).
(iii). To prove that ξ is a natural module transformation in the second
variable, we need to verify that the diagram
(5.8) ~H(A,B⊳V )
id F (A)⊗cB,V
/d15/d15
ξA,B⊳V /d47/d47H(A,B⊳V )
eA,B,V
/d15/d15
~H(A,B )⊗V
ξA,B ⊗id V
/d47/d47H(A,B )⊗V,
is commutative for any A,B∈B , V ∈C . Here
eA,B,V =cA⊗B,VF (l−1
A⊗B,V (id A⊗lB,V )).
26 LENTNER AND MOMBELLI
We have
eA,B,VξA,B⊳V =cA⊗B,VF (l−1
A⊗B,V (id A⊗lB,V ))ξA,B⊳V
= (id⊗c1,V )ξ−1
A⊗B,1⊳VF (id A⊗lB,V )ξA,B⊳V
= (id⊗c1,V )ξ−1
A⊗B,1⊳VξA,B⊗(1⊳V )(id F (A)⊗F (lB,V ))
= (id⊗c1,V )(ξA,B⊗id F (1⊳V ))(id F (A)⊗ξ−1
B,1⊳V )(id F (A)⊗F (lB,V ))
= (ξA,B⊗id V )(id F (A)⊗(id F (B)⊗c1,V )ξ−1
B,1⊳VF (lB,V ))
= (ξA,B⊗id V )(id F (A)⊗cB,V ).
The second equality follows from ( 5.5), the third equality follows from the
naturality of ξ, the fourth one follows from ( 2.1). The last equality follows
from ( 5.5). □
