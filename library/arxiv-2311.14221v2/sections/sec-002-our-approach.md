---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-002-our-approach
section_title: "Our approach"
section_number: null
pages: 3-5
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
we shall work only with ﬁnite categories. Let k be an arbitrary ﬁeld, and
letB,C be ﬁnite k-linear abelian categories. Assume both C,B are rigid
monoidal categories, and F :B→C is a monoidal functor. If F has a section
G :C→B , that is F◦G≃ Id C as monoidal functors, then it is possible to
endowB with an action of C, such that F is a monoidal C-module functor.
This action behaves well together with the monoidal product ofB, in a sense
that we call monoidal module category .
Under these conditions, we aim at constructing a Hopf algebr aH∈C and
obtaining a kind of Radford projection Theorem in this categ orical setting.
The reconstruction of such Hopf algebra is given in some step s, that we
describe as follows. If B is a rightC-module category, F :B→C is an exact
faithful module functor, we construct a coalgebra C(F )∈C as
C(F ) =
∮ B∈B
F (B)⊗∗F (B).
Here
∮
stands for the relative coend, a new tool, developed in [ 3], in the
context of module categories. This tool is one of the new feat ures that we
incorporate in these reconstruction theorems. The coprodu ct and counit of
C(F ) are deﬁned using universal properties of the dinatural tra nsformations
4 LENTNER AND MOMBELLI
associated with the relative coend. See Proposition 6.2. Moreover, we show
that the functor F factorizes as
B
ˆF /d47/d47
F /d32/d32❆❆❆❆❆❆❆❆
CC
f/d126/d126⑥⑥⑥⑥⑥⑥⑥⑥
C.
Here f : CC→C is the forgetful functor, and ˆF :B→ CC is an equivalence
ofC-module categories. The existence of ˆF is stated in Proposition 6.4, and
the proof that it is an equivalence of categories is given in T heorem 6.7.
If in addition C is a braided rigid monoidal C-module category, B is a
rigid monoidal category, and F is a monoidal functor, then we endow the
coalgebra C(F ) with a product, turning it into a bialgebra in C. Rigidity
ofB allows to deﬁne an antipode on C(F ), making it into a braided Hopf
algebra. These results are stated in Theorem 6.11 and Corrollary 6.19.
The contents of the paper are the following. In Section 2 we give a brief
account of some basic facts about tensor categories and modu le categories
that will be used throughout the paper. In Section 3 we review the notion
of relative (co)end of a functor in the setting of module categories over a
tensor category C. This tool was developed by the second author in [ 3]
as generalization of the usual (co)end. Let C be a tensor category, M be
a left C-module category and A is some target category. If a functor S :
Mop×M→A has a prebalancing, that is natural isomorphisms
βX
M,N :S(M,X⊲N )→S(X ∗⊲M,N ),
then the relative coend ∮ M ∈M
(S,β )
is an object in A equipped with dinatural transformations πM :S(M,M ) ..− →∮ M ∈M(S,β ), such that it satisﬁes some extra condition, see for exampl e
(3.3), and it is universal with this property. When C = vect k, the relative
(co)end coincides with the usual (co)end.
Since relative (co)ends are objects deﬁned by a universal pr operty, they
may not exist in general. Section 3.1 is devoted to prove that all relative
coends, used in this work, actually exist. In this Section, i t is crucial that all
categories, the tensor category C and the module category M are ﬁnite. We
also require that the action C×M→M is exact in each variable, allowing
us to use [ 9, Thm 2.24], that says that there is an equivalence of module
categoriesM≃C A, for some algebra A∈C .
In Section 4 we review the deﬁnition of a Hopf algebra H in a braided
tensor categoryC and its tensor category of comodules HC. We also review
the deﬁnition of H-H-Yetter Drinfeld modules in this setting, which pro-
duces a braided tensor category H
HYD(C). Then we introduce a notion of a
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 5
C-module category B with a compatible tensor structure in the sense that
there is a natural isomorphism
lX,B :X⊲B ≃−−→(X⊲ 1B)⊗B,
for all X∈C , B∈B , satisfying certain axioms. Note that there is a second
reasonable notion of a monoidal module category, where the a ctionX⊲− is
a monoidal functor, and this deﬁnition is not equivalent. Un der the presence
of a monoidal functor F :B→C , compatibility of the monoidal product in
B and the action of C onB, is equivalent to the existence of a section to F ,
that is a monoidal functor G :C→B such that there is a monoidal natural
isomorphism F◦G≃ Id.
