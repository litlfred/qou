---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-002-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 3-6
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
---
Concerning the former we are quite brief, since much of this material is almost universally known. Concerning
the latter we focus in particular on the discrete and compact cases and discuss the examples related to groups.
In Section 3 we treat the representation and corepresentation theory of discrete and compact aqg, respectively,
from a tensor ∗-category point of view. To this end, we recall the universal corepresentation due to Kustermans,
and we discuss conjugates in these categories. The special case of cocommutative discrete aqg is considered in
Section 4. Section 5 is the heart of this paper. There we construct a discrete quantum semigroup from a tensor
∗-category, deriving the coinverse from the conjugation and leading to a discrete aqg. The precise statement of
the generalized Tannaka-Krein theorem for quantum groups is then made in Theorem 5.25. In the ﬁnal Section
6 we establish the bijection between braidings and R-matrices. In the case of a symmetric tensor ∗-category
with symmetric embedding functor we recover the classical Tannaka-Krein theorem for compact groups.
2
Preliminaries
2.1
Tensor Categories
For the deﬁnitions of categories, functors and natural transformations we refer, e.g., to [24]. In this subsection
we brieﬂy recall some of the less standard notions of category theory which will be needed here, others will be
introduced as we proceed. We may occasionally say ‘arrows’ instead of ‘morphisms’ in order to avoid confusion
with algebra homomorphisms. All categories which we consider are essentially small, i.e. equivalent to a small
3
category. We mostly speak of ‘tensor categories’ rather than ‘monoidal categories’ but cannot avoid the adjective
‘monoidal’. In view of the coherence theorems for (braided, symmetric) tensor categories we may assume all
tensor categories to be strict, satisfying X ⊗(Y ⊗Z) = (X ⊗Y )⊗Z for all X, Y, Z. Following widespread use, we
also consider the tensor categories of vector spaces as strict, appealing to the canonical isomorphisms to identify
X ⊗(Y ⊗Z) with (X ⊗Y ) ⊗Z. We often write XY in the place of X ⊗Y . By H we mean the strictiﬁcation
of Hilb. (We also suppress all other canonical isomorphisms in Hilb, identifying B(H ⊗K) = B(H) ⊗B(K).)
Note, however, that one cannot assume all tensor functors to be strict without losing generality. Thus we need
the following.
Definition 2.1 Let C, D be (strict) tensor categories. A functor F : C →D is weakly monoidal if there exist
morphisms dX,Y : F(X) ⊗F(Y ) →F(X ⊗Y ) for all X, Y ∈C and a morphism e : 1D →F(1C) such that
1. The morphisms dX,Y are natural w.r.t. both arguments.
2. For all X, Y, Z ∈C the following diagram commutes:
F(X) ⊗F(Y ) ⊗F(Z)
dX,Y ⊗idF (Z)
✲F(X ⊗Y ) ⊗F(Z)
F(X) ⊗F(Y ⊗Z)
idF (X) ⊗dY,Z
❄
dX,Y ⊗Z
✲F(X ⊗Y ⊗Z)
dX⊗Y,Z
❄
3. The following compositions are the identity morphisms of F(X)
F(X) ≡F(X) ⊗1D
idF (X) ⊗e
✲F(X) ⊗F(1C) dX,1
✲F(X ⊗1C) ≡F(X)
F(X) ≡1D ⊗F(X)
e ⊗idF (X)
✲F(1C) ⊗F(X) d1,X
✲F(1C ⊗X) ≡F(X)
for all X ∈C.
The functor F is monoidal if e and all the dX,Y , X, Y ∈C are isomorphisms. If C, D are tensor ∗-categories
and F is ∗-preserving, the isomorphisms e, dX,Y are required to be unitary.
We will mainly be interested in linear categories over the complex ﬁeld. Viz., for all X, Y , Mor(X, Y ) is a
complex vector space, and the compositions ◦, ⊗of morphisms are bilinear. All functors are supposed C-linear.
A ∗-operation on a C-linear (tensor) category C is a map which assigns to an arrow s ∈Mor(X, Y ) another
arrow s∗∈Mor(Y, X). This map has to be antilinear, involutive (s∗∗= s), contravariant ((s ◦t)∗= t∗◦s∗)
and, if C is monoidal, monoidal ((s × t)∗= s∗× t∗). A ∗-operation is positive iﬀs∗◦s = 0 implies s = 0. A
(tensor) ∗-category is a C-linear (tensor) category with a positive ∗-operation. A morphism s : X →Y is an
isometry iﬀit satisﬁes s∗◦s = idX. A morphism s is unitary iﬀs and s∗are isometries. A functor F between
∗-categories is ∗-preserving if F(s∗) = F(s)∗for every morphism s.
An object Z is a direct sum of X1, X2, denoted Z ∼= X1 ⊕X2, if there are isometries si : Xi →Z, i = 1, 2
such that s1 ◦s∗
1 + s2 ◦s∗
2 = idZ. A ∗-category ‘has direct sums’ if for every pair X1, X2 there exists a direct
sum. An object Y is a subobject of X if there exists an isometry s : Y →X. A ∗-category ‘has subobjects’ if
for every p = p ◦p = p∗∈End(X) there exist Y and an isometry s : Y →X such that s ◦s∗= p. An object X
in a C-linear category is irreducible if it is non-zero and End X = C idX.
Definition 2.2 A ∗-category is semisimple if it has ﬁnite dimensional spaces of morphisms, a zero object,
direct sums and subobjects. A tensor ∗-category is semisimple if, in addition, the tensor unit 1 is irreducible.
4
In a semisimple ∗-category C, End(X) is a ﬁnite dimensional C∗-algebra for every X, and every object is a ﬁnite
direct sum of irreducible objects. (It is well-known that a category which is semisimple in our sense is abelian
and semisimple in the usual sense, i.e. all exact sequences split.)
Let C be a tensor ∗-category and X ∈C. A ‘solution of the conjugate equations’ is a triple (X, r, r), where
X ∈C and r : 1 →X ⊗X, r : 1 →X ⊗X satisfy
r∗⊗idX ◦idX ⊗r
=
idX,
r∗⊗idX ◦idX ⊗r
=
idX.
A tensor ∗-category C ‘has conjugates’ if there is a solution of the conjugate equations for every X ∈C. A
solution (X, r, r) is normalized iﬀr∗◦r = r∗◦r. It is a standard solution iﬀthere are irreducible objects
Xi, i ∈IX, solutions (Xi, ri, ri) of the conjugate equations and isometries vi : Xi →X, wi : Xi →X, i ∈IX
satisfying
v∗
i ◦vj = δij idXi,
X
i
vi ◦v∗
i = idX,
similar equations for wi, and we have
r =
X
i
wi ⊗vi ◦ri,
r =
X
i
vi ⊗wi ◦ri.
We deﬁne the (intrinsic or categorical) dimension d(X) ∈R+ of X by r∗◦r = d(X)id1 where (X, r, r) is a
normalized standard solution. One can prove the following facts, cf. [23]. The dimension is additive under
direct sums and multiplicative under tensor products. It takes values in the set {2 cos π
n, n = 3, 4, . . .} ∪[2, ∞),
in particular d(X) ≥1 with d(X) = 1 iﬀX ⊗X ∼= 1 iﬀX is invertible, i.e. there exists Y such that X ⊗Y ∼= 1.
If d(X) = 1 then X is irreducible. In the category H of Hilbert spaces we have dH(H) = dimC H.
We brieﬂy comment on a somewhat more general setting. A C∗-(tensor) category is a (tensor) ∗-category
where Mor(X, Y ) is a Banach space for every pair (X, Y ) of objects and the norms satisfy ∥X∗◦X∥= ∥X∥2.
A W ∗-category is a C∗-category where every Mor(X, Y ) is the dual of a Banach space for every pair (X, Y ).
In a C∗-category with conjugates and irreducible tensor unit all spaces of morphisms are ﬁnite dimensional.
This is useful in applications where this ﬁnite dimensionality is not known a priori, like in quantum ﬁeld theory.
Conversely, every ∗-category which is semisimple in our sense is a W ∗-category, cf. [25]. In a W ∗-category,
every morphism s : X →Y has a polar decomposition s = pu, where p is positive and u a partial isometry.
As a consequence, whenever Mor(X, Y ) contains a split monic (or isomorphism), it also contains an isometry
(respectively, unitary). This shows that most of the above deﬁnitions, e.g., of direct sums, are equivalent to the
the usual ones as given, e.g., in [24].
If C is a semisimple tensor ∗-category we denote the set of isomorphism classes of irreducible objects by IC.
Let (Xi, i ∈IC) be a complete set of irreducible objects and write di = d(Xi). We have 0 ∈IC such that X0 ∼= 1.
If C has conjugates, IC comes with an involution i 7→¯ı such that X¯ı is a conjugate of Xi. For i, j, k ∈IC we
deﬁne N k
ij = dim Mor(Xk, Xi ⊗Xj). These numbers satisfy the following properties.
1. For every pair (i, j) there are only ﬁnitely many k ∈IC such that N k
ij̸ = 0.
We have Xi ⊗Xj ∼=
L
k∈IC N k
ij Xk and thus didj = P
k N k
ijdk.
2.
X
l
N l
ijN m
lk =
X
n
N m
inN n
jk for all i, j, k, m ∈IC.
3. N k
ij = N i
k= N j
ık = N 
ki = N ı
jk = N k
,ı for all i, j, k ∈IC.
4. N 0
ij = δi,.
5. If C is braided, cf. Section 6, then N k
ij = N k
ji for all i, j, k ∈IC.
5
2.2
