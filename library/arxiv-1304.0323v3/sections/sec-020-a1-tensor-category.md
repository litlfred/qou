---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS"
section_id: sec-020-a1-tensor-category
section_title: "A.1. Tensor category"
section_number: null
pages: 66-67
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
---
gory). In this paper, we mainly consider additive tensor categories.
A tensor category consists of the following data:
(i) a category T ,
(ii) a bifunctor •⊗ • :T ×T →T,
(iii) an isomorphism a(X,Y,Z ) : (X⊗Y )⊗Z ∼−→X⊗(Y⊗Z) which is functorial in
X,Y,Z ∈T ,
(iv) an object 1∈T (called a unit object ),
(v) an isomorphism ε : 1⊗ 1 ∼−→1
satisfying the following axioms:
(a) (the Pentagon axiom) the following diagram is commutative for an y X,Y,Z,W ∈
T :
((X⊗Y )⊗Z)⊗W
a(X,Y,Z )⊗W
/d15/d15
a(X⊗Y,Z,W ) /d47/d47 (X⊗Y )⊗(Z⊗W )
a(X,Y,Z⊗W )
/d15/d15
(X⊗(Y⊗Z))⊗W
a(X,Y⊗Z,W )
/d15/d15
X⊗((Y⊗Z)⊗W )
X⊗a(Y,Z,W )
/d47/d47X⊗(Y⊗(Z⊗W )),
(A.1.1)
(b) the functors from T toT given by X↦→1⊗X and X↦→X⊗ 1 are fully faithful.
We refer [ 22], for example, for the fundamental properties of tensor catego ries.
Note that the isomorphism 1⊗ 1⊗X ∼−−−→ε⊗X 1⊗X induces a canonical isomorphism
1⊗X ∼−→X. Similarly, there is a canonical isomorphism X⊗ 1 ∼−→X.
Note that a unit object 1 is unique up to a unique isomorphism. Namely, for an
object Z and an isomorphism e : Z⊗Z→ Z, if the functor X↦→Z⊗X is an auto-
equivalence of T , then there exists a unique isomorphism ϕ : Z ∼−→1 such that the
diagram
Z⊗Z
e /d47/d47
ϕ⊗ϕ
/d15/d15
Z
ϕ
/d15/d15
1⊗ 1
ε /d47/d47 1
is commutative.
LetT andT′ be tensor categories. A functor F :T →T′ is called a tensor functor if
it is endowed with an isomorphism F (X⊗Y )∼−→F (X)⊗F (Y ) functorial in X,Y ∈T
and an isomorphism F (1)∼−→1 which make the following diagrams commutative:
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 67
F (X⊗Y⊗Z) /d47/d47
/d15/d15
F (X⊗Y )⊗F (Z)
/d15/d15
F (X)⊗F (Y⊗Z) /d47/d47F (X)⊗F (Y )⊗F (Z),
F (1⊗ 1) /d47/d47
/d15/d15
F (1)⊗F (1) /d47/d47 1⊗ 1
/d15/d15
F (1) /d47/d47 1.
(A.1.2)
ForX∈T and n∈ Z≥0, we write X⊗n =X⊗···⊗ X/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
n-times
.
We say that an object X is invertible if the functors Z↦→X⊗Z and Z↦→Z⊗X
are equivalences of categories. If X is invertible, then there exist an object Y and
isomorphisms f : X⊗Y ∼−→1 and g : Y⊗X ∼−→1 such that the diagrams
X⊗Y⊗X
f⊗X /d47/d47
X⊗g
/d15/d15
1⊗X
/d15/d15
X⊗ 1 /d47/d47X
and Y⊗X⊗Y
g⊗Y /d47/d47
Y⊗f
/d15/d15
1⊗Y
/d15/d15
Y⊗ 1 /d47/d47Y
are commutative. The triple ( Y,f,g ) is unique up to a unique isomorphism. We write
Y =X⊗(−1) so that one may deﬁne X⊗n for any integer n.
We say that a tensor category T is an additive tensor category ifT is additive and
⊗ is an additive bifunctor. In the sequel, we consider an additive tenso r category.
