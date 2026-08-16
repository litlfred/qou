---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-002-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 3-5
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
2.1. Tensor ideals. Let k be a ﬁeld and let C be a k−linear monoidal
category. Recall that a tensor ideal I in C is a collection of subspaces
I(X,Y ) ⊂ Hom(X,Y ) for all X,Y ∈ C such that for all X,Y,Z,T ∈ C
(1) for α ∈ I(X,Y ) and β ∈ Hom(Y,Z ),γ ∈ Hom(Z,X ) we have
α ◦γ ∈I(Z,Y ) and β ◦α ∈I(X,Z );
(2) for α ∈I(X,Y ),β ∈ Hom(Z,T ) we haveα ⊗β ∈I(X ⊗Z,Y ⊗T )
and β ⊗α ∈I(Z ⊗X,T ⊗Y ).
IfI is a tensor ideal in C then one can deﬁne a new k−linear monoidal
category C′ (the quotient of C byI) as follows: the objects of C′ are the
objects of C; Hom C′(X,Y ) := Hom C(X,Y )/I(X,Y ); the composition
of morphisms is the same as in C (note that condition (1) ensures that
the composition is well deﬁned); the tensor product is the same as in
C (well deﬁned thanks to condition (2)).
Moreover, the identity map on the objects and morphisms induces a
canonical quotient monoidal functor C → C ′.
3
It is clear that if C is rigid, pivotal, spherical, braided, symmetric
then so is C′.
2.2. Semisimpliﬁcation of a spherical tensor category. We recall
the theory of semisimpliﬁcations of spherical tensor categories, d ue to
Barrett and Westbury, [BW]. We give proofs for reader’s convenien ce.
Let k be an algebraically closed ﬁeld, and C be a spherical tensor
category over k (see [EGNO], Subsection 4.7).
Deﬁnition 2.1. A morphism f :X →Y in C is called negligible if for
any morphism g :Y →X one has Tr(f ◦g) = 0.
Lemma 2.2. ([B2], Exercise 3(ii), Subsection 2.18) Let X = ⊕iXi
and Y = ⊕jYj be decompositions of X,Y into indecomposable objects,
and f = ⊕i,jfij be a morphism X → Y , where fij : Xi → Yj. Then
f is negligible if and only if for each i,j either dimYj = 0 or fij is
not an isomorphism (equivalently, either dimXi = 0 or fij is not an
isomorphism).
Proof. First let us prove the lemma when X,Y are indecomposable.
If f : X → Y is not an isomorphism, then for any g : Y → X, the
morphism f ◦g : Y → Y is not an isomorphism, either; otherwise f
is injective (hence not surjective) and X ∼
= Imf ⊕ Kerg, with both
summands nonzero, giving a contradiction. Hence, f ◦g is nilpotent
and Tr(f ◦g) = 0. Also, if f is an isomorphism (so dim X = dim Y )
then for any g : Y → X, one has f ◦g = λId + h, where λ ∈ k and
h : Y → Y is nilpotent. Hence Tr( f ◦g) = λ dimY = λ dimX. If
dimX = dimY = 0, this is always zero, while if dim X = dim Y ⁄= 0
then we can take g =f −1 (so that λ = 1), and Tr(f ◦g) = dim Y ⁄= 0,
as desired.
Now consider the general case. Suppose the condition of the lemma
is satisﬁed, and g :Y →X is a morphism, g = (gji). Then Tr(f ◦g) =∑
i,j Tr(fij ◦gji). If either dim Yj = 0 or fij is not an isomorphism
(equivalently, either dim Xi = 0 or fij is not an isomorphism) for all
i,j then by the indecomposable case, Tr( fij ◦gji) = 0 for all i,j , hence
Tr(f ◦g) = 0. However, if for some i,j this condition is violated,
then we can take gji = f −1
ij and gpq = 0 for ( p,q ) ⁄= (i,j ), so that
Tr(f ◦g) = dimXi = dimYj. This implies the lemma. □
Let N (C) be the collection of negligible morphisms of C.
Lemma 2.3. N (C) is a tensor ideal in C.
Proof. It is clear that a linear combination of negligible morphisms is
negligible. Also, it is easy to see that f ◦a,b ◦f are negligible for any
4
a,b (when these compositions make sense). It remains to show that th e
tensor productsa⊗f andf ⊗b are negligible. Let us prove this for a⊗f ,
wherea :Z →T ; the case of f ⊗b is similar. Let g :T ⊗Y →Z ⊗X.
Then Tr((a ⊗f ) ◦g) = Tr(f ◦g′), where g′ := TrT ((a ⊗ Id) ◦g). Hence
Tr((a ⊗f ) ◦g) = 0 and a ⊗f is negligible, as desired. □
Thus we can deﬁne a spherical tensor category C := C/N (C).
Proposition 2.4. The category C is a semisimple tensor category. The
simple objects of C are the indecomposable objects of C of nonzero di-
mension.
Proof. It is clear that indecomposable objects of
C are images of in-
decomposable objects of C. More precisely, if X,Y ∈ C are indecom-
posable then by Lemma 2.2, Hom C(X,Y ) = 0 if X ≇Y or dimX = 0 or
dimY = 0 (i.e., if dim X = 0, then X = 0 in C), and dim HomC(X,Y ) =
1 if X ∼=Y and dimX ⁄= 0. This implies the proposition. □
Deﬁnition 2.5. The category C is called the semisimpliﬁcation of C.
Note that the category C comes equipped with a natural monoidal
functor S : C → C, which we call the semisimpliﬁcation functor . This
functor, however, is not a tensor functor, since it is not left or rig ht
exact, in general. We will denote the image S(X) of an object X under
this functor by X.
