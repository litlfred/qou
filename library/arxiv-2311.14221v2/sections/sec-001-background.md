---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-001-background
section_title: "Background"
section_number: null
pages: 1-3
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
Our approach 3
Acknowledgments 5
1. Preliminaries 5
2. Representations of tensor categories 6
2.1. Finite tensor categories 6
2.2. Module categories over tensor categories 7
2.3. The internal Hom 9
3. The (co)end for module categories 10
3.1. Existence of (co)ends 15
4. Hopf algebras in braided tensor categories 17
4.1. Hopf algebras in braided tensor categories 17
4.2. Yetter-Drinfeld modules 18
5. Monoidal module categories 20
5.1. Sections of monoidal functors 22
5.2. Some natural module transformations 24
6. Fiber functors and reconstruction results 26
6.1. Coalgebras constructed from a coend 26
Date: May 17, 2024.
2020 Mathematics Subject Classiﬁcation. 18D15, 18M15, 16T99.
1
2 LENTNER AND MOMBELLI
6.2. Some auxiliary results 30
6.3. Reconstruction results 32
6.4. Hopf algebras in C constructed from a coend 35
6.5. The antipode of H(F ) 40
7. Examples and Applications 44
7.1. Generic Example 44
7.2. Generic Consequences 45
7.3. Lifting and cocycles deformations 45
7.4. The logarithmic Kazhdan Lusztig conjecture 45
8. Questions 47
References 47
Introduction
Background. The main objective of the present paper is to present a ver-
sion of the Tannaka-Krein type reconstruction theorems. It is known that
ifB is a k-linear abelian locally ﬁnite category, F :B→ vect k is a ﬁbre
functor, that is an exact faithful functor, then the coend
C =
∫ B∈B
F (B)⊗kF (B)∗,
has structure of k-coalgebra, and the functor F factorizes as
B
ˆF /d47/d47
F /d39/d39❖❖❖❖❖❖❖❖❖❖❖❖❖❖ Comod(C)
f/d120/d120qqqqqqqqqq
vect k,
where f : Comod(C)→ vect k is the forgetful functor, and ˆF is a category
equivalence. We refer the reader to [ 12], [ 22] and references therein. If,
moreover,B is a monoidal rigid category, and F is a monoidal functor,
then it is possible to endow the coalgebra C with structure of Hopf algebra.
Succinctly, monoidality of B givesC a product, turning it into a bialgebra,
and rigidity of B endowsC with an antipode.
Some generalizations of this result appeared in the literat ure. We only
mention some of them. In these more general versions, a ﬁbre f unctor F :
B→C is considered, where C is an arbitrary monoidal category. In some
versions, the object C is not a Hopf algebra in C. For example in [ 4], it
is shown that if the functor F has a right adjoint G :C →B, then, the
associated monad to this adjunction T =F◦G :C→C is a bimonad, and
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 3
there is a commutative diagram
B
ˆF /d47/d47
F /d33/d33❇❇❇❇❇❇❇❇ CT
f/d125/d125⑤⑤⑤⑤⑤⑤⑤⑤
C.G
/d79/d79
Here f :CT →C is the forgeful functor. Beck’s monadicity Theorem
implies that the functor ˆF :B→C T is a monoidal equivalence. Rigidity of
both monoidal categories B,C imply that T has a Hopf monad structure. In
[13], [ 14] Lyubashenko reconstructed the object C as a coend
∫ B∈BF (B) ⊠
F (B)∗, belonging to some completion of the Deligne tensor product C ⊠C,
and it turns out to be a squared coalgebra. In the work of Majid [ 19], he
started with a monoidal functor F :B→C , where C is a braided monoidal
category, and he reconstructed a Hopf algebra C =
∫ B∈BF (B)∗⊗F (B), and
set up a commutative diagram
B
ˆF /d47/d47
F /d33/d33❇❇❇❇❇❇❇❇
CC
f/d125/d125⑤⑤⑤⑤⑤⑤⑤⑤
C.
With this generality, the functor ˆF no longer need to be an equivalence.
