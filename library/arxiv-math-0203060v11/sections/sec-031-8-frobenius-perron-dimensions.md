---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-031-8-frobenius-perron-dimensions
section_title: "Frobenius-Perron dimensions"
section_number: 8
pages: 29-34
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
In this section we will give some applications of the Frobenius-Perron theorem
to the theory of fusion categories. We work with categories over C.
8.1. Deﬁnition of the F robenius-Perron dimensions. We start by recalling
the Frobenius-Perron theorem (see [Ga]).
Theorem 8.1. LetA be a square matrix with nonnegative entries.
(1) A has a nonnegative real eigenvalue. The largest nonnegative real eigenvalue
λ(A) of A dominates absolute values of all other eigenvalues of A.
(2) If A has strictly positive entries then λ(A) is a simple positive eigenvalue,
and the corresponding eigenvector can be normalized to have strictly positive
entries.
(3) IfA has an eigenvector f with strictly positive entries, then the correspond-
ing eigenvalue is λ(A).
30 PA VEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
Now let A be a unital based ring of ﬁnite rank in the sense of Lusztig (see, e.g.,
[O] for a deﬁnition). Let bi be the basis of A (b0 = 1), and [ bi] be the matrix of
multiplication by bi ∈A in the basis bj. This matrix has nonnegative entries. Let
λi be the largest nonnegative eigenvalue of [ bi]. Since bi is clearly not nilpotent,
this eigenvalue is actually positive.
We will call λi the Frobenius-Perron dimension of bi. We note that Frobenius-
Perron dimensions for commutative based rings were deﬁned and us ed in the book
[FK].
Theorem 8.2. The assignment bi → λi extends to a homomorphism of algebras
A → R.
Proof. For any j deﬁne zj = ∑
ibibjb∗
i . We claim that zj is central. Indeed, let
bibj = ∑
kNk
ijbk. Then Nk
ri =Ni∗
k∗r, so
brzj =br
∑
i
bibjb∗
i =
∑
k,i
Nk
ribkbjb∗
i =
∑
k,i
Ni∗
k∗rbkbjbi∗ =
∑
k
bkbjbk∗br =zjbr.
Let z = ∑
jzj. Since zj containbj as a summand, the matrix [ z] of multiplication
by z = ∑
jzj has strictly positive entries. Let f be the unique eigenvector of [ z]
with positive entries and f0 = 1 (its existence and uniqueness follows from the
Frobenius-Perron theorem). Then [ bj]f must be a multiple of f , since f has positive
entries and [ z][bj] = [ bj][z]. So by the Frobenius-Perron theorem, [ bj]f = λjf ,
whence the statement follows. □
We note that bi →λi is the unique homomorphism of A to R such that images
of the basis vectors are positive. This is demonstrated by the follow ing simple and
probably well known lemma.
Let A be a Z+-ring of ﬁnite rank with Z+-basis bi (see [O] for deﬁnition).
Lemma 8.3. If there exists a homomorphism φ : A → R such that φ(bi) > 0 for
all i, then φ is unique.
Proof. Let [bi] be the matrix of multiplication by bi in the basis bj, and f be the
column vector with entries φ(bj). Then [ bi]f = φ(bi)f . But [ bi] is a matrix with
nonnegative entries, and f has positive entries. Thus, by the Frobenius-Perron theo-
rem,φ(bi) is the largest positive eigenvalue of [bi], and hence is uniquely determined.
Lemma is proved. □
Remark 8.4. M. M¨ uger pointed out to us that for any i one has λi ≥ 1; moreover
if λi < 2 then λi = 2 cos(π/n) for some integer n ≥ 3 (this follows from the well
known Kronecker theorem on the eigenvalues of positive integer ma trices).
One can also deﬁne the Frobenius-Perron dimensions of basis elemen ts of a based
module over a unital based ring. Indeed, let M be an indecomposable based A-
module with basis mj (see [O] for deﬁnition).
Proposition 8.5. There exists a unique up to scaling common eigenvector m of
the matrices [bi]|M of the operators bi inM , which has strictly positive entries. The
corresponding eigenvalues are λi.
Proof. Let z be the element from the proof of Theorem 8.2. The matrix [ z]|M has
strictly positive entries. Let m be an eigenvector of [ z]|M with positive entries.
It exists and is unique up to a positive scalar, by the Frobenius-Perr on theorem.
Hence, it is an eigenvector of [ bi]|M , and the eigenvalues are λi by Lemma 8.3. □
ON FUSION CATEGORIES 31
Now let C be a fusion category. Let K(C) be the Grothendieck ring of C. For
any object X ∈ C , deﬁne the Frobenius-Perron dimension of X, FPdim(X), to be
the largest positive eigenvalue of the matrix [ X] of multiplication by X in K(C).
Since K(C) is a unital based ring of ﬁnite rank, Theorem 8.2 implies the following
result.
Theorem 8.6. The assignment X → FPdim(X) extends to a homomorphism of
algebrasK(C) → R.
Similarly, one can deﬁne Frobenius-Perron dimensions of simple objec ts of a
module category over a fusion category. Namely, let M be an indecomposable
module category over a fusion category C. For any X ∈ C let [X]M be the matrix
of action of X on the Grothendieck group of M. Since the Grothendieck group
K(M) is an indecomposable based module over K(C), Proposition 8.5 implies
Proposition 8.7. There exists a unique up to scaling common eigenvector m of the
matrices [X]M, which has strictly positive entries. The corresponding ei genvalues
are FPdim(X).
The entries µi of m are called the Frobenius-Perron dimensions of simple objects
Mi of M. Unlike Frobenius-Perron dimensions of objects of C, they are well deﬁned
only up to scaling.
8.2. F robenius-Perron dimension of a fusion category. Let C be a fusion
category. Deﬁne the Frobenius-Perron dimension FPdim( C) of C to be the sum of
squares of Frobenius-Perron dimensions of simple objects of C.
Also, deﬁne the regular representation RC to be the (virtual) object
⊕X∈Irr (C)FPdim(X)X, where Irr (C) is the set of isomorphism classes of simple
objects of C. It is clear that FPdim( C) = FPdim(RC).
Proposition 8.8. Let F : C → D be a surjective tensor functor between fusion
categories. Then F (RC) = FPdim(C)
FPdim(D)RD.
Proof. Let X be an object of C such that F (X) contains all simple objects of D.
It exists since F is surjective. The vectors of multiplicities of F (RC) and RD are
eigenvectors of the matrix of multiplication by F (X). The matrix and the vectors
have strictly positive entries. By the Frobenius-Perron theorem, this implies that
F (RC) and RD diﬀer by a positive scalar. This scalar is readily found to be the
claimed one by taking FPdim of F (RC) and RD. □
Corollary 8.9. LetA ⊂B be an inclusion of ﬁnite dimensional semisimple quasi-
Hopf algebras. Then B is free as a left A-module.
Proof. In this case Frobenius-Perron dimensions coincide with the usual on es, so if
C = Rep(B), D = Rep(A) then RC =B, RD =A, proving the claim. □
Remark 8.10. For Hopf algebras, Corollary 8.9 is the well known freeness theorem
of Nichols and Zoeller [NZ] (it is true in the nonsemisimple case as well). In the
quasi-Hopf case it was independently obtained by P. Schauenburg ( without the
semisimplicity assumption), [Scha].
Corollary 8.11. IfF : C → D is surjective then FPdim(C) is divisible by FPdim(D)
(i.e. the ratio is an algebraic integer).
32 PA VEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
Proof. Taking the multiplicity of the neutral object of D in Proposition 8.8, we ﬁnd∑
X∈Irr (C) FPdim(X)[F (X) : 1] = FPdim(C)
FPdim(D) , which yields the statement. □
Proposition 8.12. For any fusion category C, one has FPdim(Z(C)) = FPdim( C)2.
Remark 8.13. If C is a representation category of a quasi-Hopf algebra A, then
Proposition 8.12 is saying that the Frobenius-Perron dimension of Z(C) is dim(A)2.
This is a simple consequence of the result of Hausser and Nill [HN], who constructed
a quasi-Hopf algebra D(A) (the double of A), isomorphic to A ⊗A∗ as a vector
space, such that Z(C) = Rep(D(A)).
Proof. Recall from Section 5 that V → I(V ) denotes the induction functor. By
Proposition 5.4, we have
FPdim(I(V )) = ⊕X∈Irr (Z(C))FPdim(X)[I(V ) : X]
= ⊕X∈Irr (Z(C))FPdim(X)[X|C :V ]
= [ RZ(C) :V ] = FPdimZ(C)
FPdimC [RC :V ] = FPdimZ(C)
FPdimC FPdim(V ).
In particular, FPdim(I(1)) = FPdimZ(C)
FPdimC .
On the other hand, by Proposition 5.4, I(1) = ⊕Y ∈Irr (C)Y ⊗Y ∗, which implies
the desired statement (since the dimension of the right hand side is F Pdim(C)).
The proposition is proved. □
Corollary 8.14. Let C be a fusion category and C∗ be its dual with respect to an
indecomposable module category. Then FPdim(C) = FPdim( C∗).
Proof. This follows from Proposition 8.12 and the fact that Z(C) is equivalent to
Z(C∗) [O1, Mu2]. □
Proposition 8.15. Let C be a full tensor subcategory of a fusion category D. Then
FPdim(D)/FPdim(C) is an algebraic integer.
Proof. Consider the decomposition of D, as a left module category over C, in a
direct sum of indecomposables. We have D = ⊕r
i=1Mr. Let us consider the duals
of C and D with respect to this module category. We have D∗ = Dop, and C∗ is a
multi-fusion category C∗ = ⊕r
i,j=1C∗
ij, where C∗
ij := Fun( Mj, Mi). Note that the
Frobenius-Perron dimensions of C∗
ii are equal to FPdim( C) by Corollary 8.14.
Let Eij denote nonzero virtual objects of C∗
ij, which satisfy the condition
X ⊗Eij ⊗Y = FPdim(X)FPdim(Y )Eij, X ∈ C ∗
ii,Y ∈ C ∗
jj . Since the category
C∗
ij is an indecomposable bimodule over C∗
ii and C∗
jj , by the Frobenius-Perron theo-
rem, the object Eij is unique up to scaling. We require that the coeﬃcients in Eij
be positive, which determines it uniquely up to a positive scalar.
To ﬁx the scaling completely, we will require that Eii, which is a multiple of the
regular representation Rii in C∗
ii, be actually equal to FPdim( C)−1Rii. Further, we
normalize E1j arbitrarily, then normalize Ej1 by the condition Ej1 ⊗E1j = Ejj ,
and ﬁnally deﬁne Ejk as Ej1 ⊗E1k. It is easy to see that Eij satisfy the matrix
unit relations Eij ⊗Ekl =δjkEil.
Now let F : D∗ → C ∗ be the natural functor, R be the regular representation
of D∗, and consider F (R) ∈ C ∗. We claim that F (R) = ⊕i,jbijEij, where bij > 0.
Indeed,F (R)⊗2 = FPdim(D)F (R), so for any i the virtual object Li := ⊕jbijEij is
an eigen-object of the functor of right multiplication by F (R). Since the category
ON FUSION CATEGORIES 33
⊕jC∗
ij is an indecomoposable right module over C∗, by the Frobenius-Perron theorem
such eigen-object with positive coeﬃcients is unique up to scaling. Th us, for any
X ∈ C ∗
ii,X ⊗Li =c(X)Li, wherec(X) is a scalar. By the Frobenius-Perron theorem
c(X) = FPdim( X). Similarly, Pj := ⊕ibijEij satisﬁes Pj ⊗X = FPdim(X)Pj,
X ∈ C ∗
jj . This implies the claim.
Now letB be the matrix (bij). Since F (R)⊗2 = FPdim(D)F (R), and Eij behave
like matrix units, we have B2 = FPdim(D)B. Thus eigenvalues of B are FPdim(D)
and zero, and B is diagonalizable. Since bij > 0, by the Frobenius-Perron theorem
the multiplicity of the eigenvalue FPdim( D) is 1, so the rank of B is 1. Hence
Tr(B) = FPdim( D).
On the other hand, let us compute bii. We have
∑
X∈Irr (D)
FPdim(X)[F (X) : 1ii] = bii/FPdim(C)
(as Eii = Rii/FPdim(C)). Thus, bii/FPdim(C) is an algebraic integer. Summing
over all i, we ﬁnd that Tr( B)/FPdim(C) = FPdim( D)/FPdim(C) is an algebraic
integer, as desired. □
Remark 8.16. Since bii ≥ 1, we see that FPdim( D)/FPdim(C) dominates the
number of indecomposable blocks in D as a left C-module category.
Remark 8.17. Let M1 = C. Then C∗
i1 = Mi. It is easy to see that F (R)i1 =∑
X∈Irr (Mi) FPdim(X)X. By uniqueness of eigen-object of F (R) in ⊕jC∗
ji, we have
F (R)i1 ⊗F (R)1i = FPdim(C)F (R)ii. Thus,
[F (R)ii : 1ii] = dim End(F (R)i1,F (R)i1)/FPdim(C) = FPdim( Mi)/FPdim(C).
This implies the reﬁnement of Theorem 8.15 stating that FPdim( Mi)/FPdim(C)
is an algebraic integer.
Remark 8.18. We do not know if the global dimension of a fusion category is
divisible by the global dimension of its full tensor subcategory.
Example 8.19. The following example shows that Proposition 8.15 is a property
of tensor categories and not just of based rings.
Let G be a ﬁnite group and n a nonnegative integer. Consider the based ring
An(G) with basis G ∪ {X}, with multiplication given by the usual multiplication
in G and the relations gX =Xg =X,g ∈G, and X 2 =nX + ∑
g∈Gg. Such rings
for special n,G can arise as Grothendieck rings of fusion categories (for example,
the categories of [TY], or representation categories of aﬃne grou ps Aﬀ( Fq)). We
claim that if An(G) is categoriﬁable, then the number ( n +
√
n2 + 4|G|)2/4|G| is
an algebraic integer. In particular, for n ⁄= 0 one has |G| ≤ 2n2. (For n = 1 we
ﬁnd |G| = 1, 2, so G = 1 or G = Z/2Z, which was proved by T. Chmutova even
for non-rigid categories). Indeed, let C be a fusion category with Grothendieck ring
An(G). Then the Frobenius-Perron dimensions of elements of G are 1, while the
Frobenius-Perron dimension ofX is the largest root of the equation x2 −nx−m = 0,
wherem = |G|. Thus x = 1
2 (n +
√
n2 + 4m). By Proposition 8.15, x2/m should be
an algebraic integer.
Proposition 8.20. If a fusion category C is faithfully graded by a ﬁnite group G,
then the Frobenius-Perron dimensions of Cg are equal for all g ∈G. In particular,
|G| divides FPdim(C).
34 PA VEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
Proof. Let R be the regular object of C. Then R = ⊕Rg, where Rg is a virtual
object of Cg. We have R ⊗Rh = FPdim(Rh)R. Taking the gh-th component of this
equation, we ﬁnd Rg ⊗Rh = FPdim(Rh)Rgh. Similarly, Rg ⊗R = FPdim(Rg)R,
which yields Rg ⊗Rh = FPdim(Rg)Rgh. Since Rgh ⁄= 0, we get FPdim( Rg) =
FPdim(Rh), i.e. FPdim( Rg) = FPdim(X)/|G|. □
8.3. Comparison of the global and F robenius-Perron dimensions.
Proposition 8.21. Let C be a fusion category. Then for any simple object V of C
one has |V |2 ≤ FPdim(V )2, and hence dim(C) ≤ FPdim(C). Hence, if dim(C) =
FPdim(C) then |V |2 = FPdim(V )2 for all simple objects V .
Proof. Let Xi be the i-th simple object of C, and di = d(Xi) be its dimension
introduced in the proof of Theorem 2.3. Then |di|2 = |V |2, and di is an eigenvalue
of the matrix Ti. It follows from Section 3 that the absolute values of the entries of
Ti are dominated by the corresponding entries of the matrix Ni of multiplication
by Xi. Let fi be the Frobenius-Perron dimension of Xi, and consider a norm on
the Grothendieck group GrC(C) given by || ∑ aiXi|| = ∑ fi|ai|. Let us estimate
the norm of the operator Ti. We have
||Tia|| =
∑
j
fj|
∑
k
(Ti)jkak| ≤
∑
j,k
fj(Ni)jk |ak| =fi
∑
k
fk|ak| =fi||a||
Thus, ||Ti|| ≤ fi. This implies that |V |2 ≤f 2
i , which proves the proposition. □
Proposition 8.22. Let C be a fusion category of global dimension D and Frobenius-
Perron dimension ∆ . Then D/∆ is an algebraic integer, which is ≤ 1.
Proof. By Proposition 8.21, we only need to prove that D/∆ is an algebraic integer.
First of all, we can assume without loss of generality that C is a spherical category.
Indeed, if C is not spherical, then, as explained in Proposition 5.14, we can constr uct
a spherical fusion category ˜C which projects onto C. It is easy to see that this
category has global dimension 2D and Frobenius-Perron dimension 2∆, so the ratio
of dimensions is the same.
Now assume that C is spherical. Consider the Drinfeld center Z(C). This is a
modular category of global dimension D2, and by Proposition 8.12, its Frobenius-
Perron dimension is ∆ 2. Let S = (sij) be its S-matrix. It follows from Verlinde’s
formula (see [BaKi]) that the commuting matrices Ni of multiplication by simple
objects Xi of Z(C) have common eigenvectors vj with eigenvalues sij/s0j. In par-
ticular, there exists a unique (by nondegeneracy of S) distinguished label j =r such
that sir/s0r = fi, the Frobenius-Perron dimension of Xi. Since S is symmetric,
and S2 is the charge conjugation matrix, we have ∆ 2 = ∑
if 2
i = δrr ∗/s2
0r. Thus
r =r∗ and ∆ 2 = 1/s2
0r =D2/d2
r, where dr is the categorical dimension of the r-th
simple object. So D2/∆ 2 =d2
r is an algebraic integer. □
