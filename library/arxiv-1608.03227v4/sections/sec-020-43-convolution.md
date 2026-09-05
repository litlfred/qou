---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-020-43-convolution
section_title: "Convolution"
section_number: 4.3
pages: 21-22
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
construct a homomorphism from the braid group into this convolutio n algebra. This allows us to associate
a particular matrix factorization to a braid and in the section 13 we ex plain how one can extract knot
homology out of this matrix factorization.
We choose coordinates on X2 = g×(G×b)2 as (X,g 1,Y 1,g 2,Y 2) and consider a G×B2-invariant potential
on X2:
(4.7) W (X,g 1,Y 1,g 2,Y 2) = Tr(X(Adg1 (Y1)− Adg2 (Y2))).
The torus Tsc acts on X2 and deg TscW = t2. Consider the category of MF sc
B2 (X2,W ) of Tsc-graded
B2-equivariant matrix factorizations whose diﬀerentials have degree degTscD = t. The morphisms and
homotopies in the category are assumed to be Tsc-invariant.
Our main category is the subcategory MF sc
B2(X2,W )G of MF sc
B2 (X2,W ) that consists of the complexes
that are G-equivariant in the strong sense. The G-action on X2 is free and as we show in subsection 4.4 the
category MF sc
B2(X2,W )G is equivalent to the category of B2-equivariant matrix factorizations on X2/G. To
simplify notations, from now on we use notation MF sc
B2 (X2,W ) for MF sc
B2(X2,W )G.
We also use notation qktm for shift functor for the weights of the action of Tsc: if V is a vector space
with C∗
t× C∗
q action then qktm·V is the same vector space with q- and t-degrees shifted by k and m: for
v∈V and (λ,µ )∈ C∗
t× C∗
q we deﬁne (λ,µ )· (qktmv) = λkµmqktm((λ,µ )·v). Respectively we use notation
qktm·F∈ MFsc
B2 (X2,W ) for the matrix factorization with the same diﬀerentials as F∈ MFsc
B2 (X2,W ) but
the the twisted Tsc-equivariant structure of the underlying module.
Let us make a small clariﬁcation about the t-grading in our categories. Let F be a potential on the space
Z andZ has Tsc = C∗
t× C∗
q action such that F has the weight t2. Then we deﬁne MF sc(Z,F ) to the
homotopic category whose objects are 2-quasi-periodic complexe s:
...
D−1
−−−→M0
D0
−−→M1
D1
−−→M2
D2
−−→...,
such that Di+2 = Di and Mi+2 = t2·Mi and Di are of degree t. In particular, if F = 0 then for
F = (M•,D •)∈ MFsc(Z,F ) we have well deﬁned Tsc-equivariant modules:
Heven(F ) := H 0(M•,D •), Hodd(F ) := H 1(M•,D •).
21
4.3. Convolution. There are three natural projection maps π12,π 23,π 13 : X3 → X2 and π∗
12(W ) +
π∗
23(W ) = π∗
13(W ). If we extend the action of G×B2 on X2 to the action of G×B3 by natural projectors
πij :G×B3→G×B2 then the maps πij becomeG×B3-equivariant and hence for anyF,G∈ MFsc
B2 (X2,W )
we can deﬁne an object
π∗
12(F )⊗π∗
23(G)∈ MFsc
B3(X3,π ∗
13(W )).
Naively we could deﬁne the convolution between F andG as a quotient of the tensor product by the action
of the second copy B(2) of B inside G×B3. We deﬁne a derived quotient with the help of the Chevalley-
Eilenberg complex, we also explain how to deﬁne the convolution in a bigg er category MF sc
B2(Z,W ).
LetF,G∈ MFsc
B2(X2,W ),F = (M,D,∂ l,∂ r),G = ( ˜M, ˜D, ˜∂l, ˜∂r). The tensor product M⊗ ˜M is naturally
a module over B3 with the action (b1,b 2,b 3)(m⊗ ˜m) = (b1,b 2)·m⊗ (b2,b 3)· ˜m, hence we can deﬁne a tensor
product of pull backs π∗
12(F ) and π∗
23(G) as an object of MF sc
B3 (X3,π ∗
13(W )):
π∗
12(F )⊗π∗
23(G) = (π∗
12(M )⊗π∗
23( ˜M ),D + ˜D,∂ l,∂ r + ˜∂l, ˜∂r).
From here on we use notation n(1), n(2), n(3) for the ﬁrst, second and third copy of n on n3; respectively for
given n3 module M we denote by d(i)
ce the Chevalley-Eilenberg diﬀerential on CE n3⊗
∆
M corresponding i-th
copy of n.
The complex CE n is T -equivariant hence T (2)-invariant part CE n(2) (π∗
12(F )⊗π∗
23(G))T (2)
is the matrix
factorization from MF sc
B2(X3/B(2),π ∗
13(W )). In more details: CE n(2) (π∗
12(F )⊗B π∗
23(G))T (2)
is the matrix
factorization with underlying module
CEn(2) (π∗
12(M )⊗π∗
23( ˜M ))T (2)
:= Hom n(2) (CEn(2), CEn(2)⊗
∆ Ä
π∗
12(M )⊗π∗
23( ˜M )
ä
)T (2)
,
the matrix factorization diﬀerential D(2) := d(2)
ce +∂r + ˜∂l +D + ˜D and n(1)× n(2) equivariant structure
diﬀerentials are ∂l, ˜∂r.
In particular (CE n(2) (π∗
12(M )⊗π∗
23( ˜M ))T (2)
,D (2)) is a complex over the ring π∗
13(C[X2])⊂ C[X3]b(2) and
as such it is an object of MF sc
B2 (X,W ) which we denote π13∗(CEn(2) (π∗
12(F )⊗π∗
23(G))T
(2). The last complex
provides us a bilinear operation on MF sc
B2(X2,W ):
(4.8) F ⋆G :=π13∗(CEn(2) (π∗
12(F )⊗π∗
23(G))T (2)
) =
(CEn(2) (π∗
12(M )⊗π∗
23( ˜M ))T (2)
,D (2),∂ l, ˜∂r).
The proof of the following proposition is standard: it literally repeats the proof of the associativity of the
convolution from the book [7]:
Proposition 4.1. The binary operation ⋆ deﬁnes a strictures of associative algebra on MFsc
B2(X2,W ).
