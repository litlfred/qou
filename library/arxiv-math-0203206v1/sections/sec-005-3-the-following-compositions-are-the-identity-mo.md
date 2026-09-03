---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-005-3-the-following-compositions-are-the-identity-mo
section_title: "The following compositions are the identity morphisms of F (X)"
section_number: 3
pages: 4-5
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
F (X) ≡F (X) ⊗ 1D
idF (X) ⊗e✲ F (X) ⊗F (1C) dX,1✲ F (X ⊗ 1C) ≡F (X)
F (X) ≡ 1D ⊗F (X)
e ⊗ idF (X)✲ F (1C) ⊗F (X) d1,X✲ F (1C ⊗X) ≡F (X)
for all X ∈ C .
The functor F is monoidal if e and all the dX,Y, X,Y ∈ C are isomorphisms. If C, D are tensor ∗-categories
and F is ∗-preserving, the isomorphisms e,dX,Y are required to be unitary.
We will mainly be interested in linear categories over the complex ﬁeld. V iz., for all X,Y , Mor(X,Y ) is a
complex vector space, and the compositions ◦, ⊗ of morphisms are bilinear. All functors are supposed C-linear.
A ∗-operation on a C-linear (tensor) category C is a map which assigns to an arrow s ∈ Mor(X,Y ) another
arrow s∗ ∈ Mor(Y,X ). This map has to be antilinear, involutive ( s∗∗ = s), contravariant ((s ◦ t)∗ =t∗ ◦ s∗)
and, if C is monoidal, monoidal (( s ×t)∗ = s∗ ×t∗). A ∗-operation is positive iﬀ s∗ ◦ s = 0 implies s = 0. A
(tensor) ∗-category is a C-linear (tensor) category with a positive ∗-operation. A morphism s : X → Y is an
isometry iﬀ it satisﬁes s∗ ◦s = idX . A morphism s is unitary iﬀ s and s∗ are isometries. A functor F between
∗-categories is ∗-preserving if F (s∗) = F (s)∗ for every morphism s.
An object Z is a direct sum of X1,X 2, denoted Z ∼= X1 ⊕X2, if there are isometries si :Xi →Z,i = 1, 2
such that s1 ◦s∗
1 +s2 ◦s∗
2 = idZ . A ∗-category ‘has direct sums’ if for every pair X1,X 2 there exists a direct
sum. An object Y is a subobject of X if there exists an isometry s :Y →X. A ∗-category ‘has subobjects’ if
for every p =p ◦p =p∗ ∈ End(X) there exist Y and an isometry s :Y →X such that s ◦s∗ =p. An object X
in a C-linear category is irreducible if it is non-zero and End X = C idX .
Definition 2.2 A ∗-category is semisimple if it has ﬁnite dimensional spaces o f morphisms, a zero object,
direct sums and subobjects. A tensor ∗-category is semisimple if, in addition, the tensor unit 1 is irreducible.
4
In a semisimple ∗-category C, End(X) is a ﬁnite dimensional C∗-algebra for every X, and every object is a ﬁnite
direct sum of irreducible objects. (It is well-known that a category which is semisimple in our sense is abelian
and semisimple in the usual sense, i.e. all exact sequences split.)
Let C be a tensor ∗-category and X ∈ C . A ‘solution of the conjugate equations’ is a triple ( X,r, r), where
X ∈ C and r : 1 →X ⊗X, r : 1 →X ⊗X satisfy
r∗ ⊗ idX ◦ idX ⊗r = id X,
r∗ ⊗ idX ◦ idX ⊗r = id X.
A tensor ∗-category C ‘has conjugates’ if there is a solution of the conjugate equations f or every X ∈ C . A
solution (X,r, r) is normalized iﬀ r∗ ◦r = r∗ ◦r. It is a standard solution iﬀ there are irreducible objects
Xi,i ∈ IX , solutions ( Xi,ri,ri) of the conjugate equations and isometries vi : Xi → X,wi : Xi → X,i ∈ IX
satisfying
v∗
i ◦ vj =δij idXi,
∑
i
vi ◦ v∗
i = idX,
similar equations for wi, and we have
r =
∑
i
wi ⊗vi ◦ ri, r =
∑
i
vi ⊗wi ◦ ri.
We deﬁne the (intrinsic or categorical) dimension d(X) ∈ R+ of X by r∗ ◦r = d(X)id1 where (X,r, r) is a
normalized standard solution. One can prove the following facts, cf . [23]. The dimension is additive under
direct sums and multiplicative under tensor products. It takes valu es in the set {2 cosπ
n,n = 3, 4,... } ∪ [2, ∞),
in particular d(X) ≥ 1 with d(X) = 1 iﬀ X ⊗X ∼= 1 iﬀ X is invertible, i.e. there exists Y such that X ⊗Y ∼= 1.
If d(X) = 1 then X is irreducible. In the category H of Hilbert spaces we have dH(H) = dim CH.
We brieﬂy comment on a somewhat more general setting. A C∗-(tensor) category is a (tensor) ∗-category
where Mor(X,Y ) is a Banach space for every pair ( X,Y ) of objects and the norms satisfy ‖X ∗ ◦ X‖ = ‖X‖2.
A W ∗-category is a C∗-category where every Mor( X,Y ) is the dual of a Banach space for every pair ( X,Y ).
In a C∗-category with conjugates and irreducible tensor unit all spaces o f morphisms are ﬁnite dimensional.
This is useful in applications where this ﬁnite dimensionality is not known a priori, like in quantum ﬁeld theory.
Conversely, every ∗-category which is semisimple in our sense is a W ∗-category, cf. [25]. In a W ∗-category,
every morphism s : X → Y has a polar decomposition s = pu, where p is positive and u a partial isometry.
As a consequence, whenever Mor( X,Y ) contains a split monic (or isomorphism), it also contains an isometry
(respectively, unitary). This shows that most of the above deﬁnit ions, e.g., of direct sums, are equivalent to the
the usual ones as given, e.g., in [24].
If C is a semisimple tensor ∗-category we denote the set of isomorphism classes of irreducible o bjects by IC.
Let (Xi,i ∈IC) be a complete set of irreducible objects and write di =d(Xi). We have 0 ∈IC such that X0 ∼= 1.
If C has conjugates, IC comes with an involution i ↦→¯ı such that X¯ı is a conjugate of Xi. For i,j,k ∈ IC we
