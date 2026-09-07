---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS R-MATRICES OF QUANTUM AFFINE ALGEBRAS"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-6
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS R-MATRICES OF QUANTUM AFFINE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
---
Convention 6
1. Quantum groups and Khovanov-Lauda-Rouquier algebras 6
1.1. Cartan datum 6
1.2. Khovanov-Lauda-Rouquier algebras 8
1.3. R-matrices for Khovanov-Lauda-Rouquier algebras 11
Date: March 29, 2021.
2010 Mathematics Subject Classiﬁcation. 81R50, 16G, 16T25,17B37.
Key words and phrases. Quantum aﬃne algebra, Khovanov-Lauda-Rouquier algebra, Quan tum
group, R-matrix, Schur-Weyl duality.
1 This work was supported by NRF Grant # 2012-005700 and NRF Gran t # 2011-0027952.
2 This work was partially supported by Grant-in-Aid for Scientiﬁc Rese arch (B) 22340005, Japan
Society for the Promotion of Science.
3 This work was partially supported by NRF Grant # 2012-005700.
1
2 S.-J. KANG, M. KASHIW ARA, M. KIM
1.4. R-matrices with spectral parameters 14
1.5. R-matrices for one-dimensional modules 19
1.6. Uniqueness of R-matrices 21
2. Quantum aﬃne algebras and their representations 22
2.1. Quantum aﬃne algebras 22
2.2. R-matrices 25
3. Aﬃne Schur-Weyl duality via Khovanov-Lauda-Rouquier algebra s 27
3.1. Action of Khovanov-Lauda-Rouquier algebras on ˆV⊗β 27
3.2. The Functor F 31
3.3. Exactness of the functor F 33
4. Quantum aﬃne algebra U′
q(ˆslN ) and the category CJ 34
4.1. R-matrix for V (̟1) of U′
q(ˆslN ) 35
4.2. KLR-modules in A case 36
4.3. Properties of the functor F 43
4.4. Quotient of the category R-gmod 46
4.5. The category T′
J 47
4.6. Rigidity of the tensor categories T′
J andTJ 54
4.7. The Category CJ 61
Appendix A. Localization 65
A.1. Tensor category 66
A.2. Adjunction and Quasi-adjunction 67
A.3. Central objects 69
A.4. Commuting family of objects 70
A.5. Localization 71
A.6. Localization of tensor categories 72
A.7. Graded case 75
A.8. Variant 78
A.9. Twisting of tensor structure 79
Appendix B. Quotient categories 79
B.1. Serre category 79
References 81
Introduction
The Khovanov-Lauda-Rouquier algebras (sometimes called the quiver Hecke algebras)
are a family of Z-graded algebras which categoriﬁes the negative half of a quantum
group ([ 24, 25, 34]). More precisely, if Uq(g) is a quantum group associated with a
symmetrizable Cartan datum, then there exists a family of algebras {R(n)}n∈Z≥0 such
that the Grothendieck group of the direct sum ⨁
n∈Z≥0
R(n)-gproj of the categories of
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 3
ﬁnitely generated projective graded R(n)-modules is isomorphic to the integral form
U−
A(g) of the negative half of Uq(g). Here, the multiplication of the Grothendieck group
is given by the convolution product and the action of q is given by the grading shift
functor. Moreover, the cyclotomic quotient RΛ (n) of R(n) provides a categoriﬁcation
of the integrable highest weight module V (Λ) of Uq(g) ([ 15]).
One of the motivations of these categoriﬁcation theorems originat ed from the so-
called LLT-Ariki theory. In 1996, Lascoux-Leclerc-Thibon ([ 28]) conjectured that the
irreducible representations of Hecke algebras of type A are controlled by the upper
global basis ([ 17, 18]) (or dual canonical basis ([ 30])) of the basic representation of
the quantum aﬃne algebra Uq(A(1)
N−1). Soon after, Ariki ([
2]) proved this conjecture by
showing that the cyclotomic quotients of aﬃne Hecke algebras cate gorify the irreducible
highest weight modules over U(A(1)
N−1), the universal enveloping algebra of aﬃne Kac-
Moody algebra of type A(1)
N−1. In [
4, 34], Brundan-Kleshchev and Rouquier showed
that the aﬃne Hecke algebra of type A is isomorphic to the Khovanov-Lauda-Rouquier
algebra of type A or of type A∞ up to a specialization and a localization. Thus the
Khovanov-Lauda-Rouquier algebras can be understood as a grad ed version of the aﬃne
Hecke algebras of type A and Kang-Kashiwara’s cyclotomic categoriﬁcation theorem
is a generalization of Ariki’s theorem on type A and A∞ to all symmetrizable Cartan
datum.
The purpose of this paper is to show that the Khovanov-Lauda-Ro uquier algebra
can be regarded as a generalization of the aﬃne Hecke algebra of ty pe A in another
context: the quantum aﬃne Schur-Weyl duality . In [ 13], M. Jimbo extended the
classical Schur-Weyl duality to the quantum case: the duality betw een the category
of ﬁnite-dimensional modules over the Hecke algebra Hq(n) and the category of ﬁnite-
dimensional modules over the quantum group Uq(glN ). In [ 6, 7, 9], Chari-Pressley,
Cherednik and Ginzburg-Reshetikhin-Vasserot introduced a quan tum aﬃne version of
Schur-Weyl duality: they deﬁned a functor between the categor y of ﬁnite-dimensional
modules over the aﬃne Hecke algebra H aﬀ
q (n) and the category of ﬁnite-dimensional
integrable modules over U′
q(ˆslN ).
There are two key ingredients in deﬁning this functor: (1) the R-ma trices on the
n-fold tensor product of the fundamental representation V (̟1) which satisfy the Yang-
Baxter equations, (2) a set of elements in H aﬀ
q (n), called the intertwiners, which satisfy
the braid relations. Roughly speaking, by assigning intertwiners to R -matrices, we
obtain the quantum aﬃne Schur-Weyl duality functor.
Now it is quite natural to ask whether this functor can be generalize d to the case of
quantum aﬃne algebras U′
q(g) of other types or not. Our answer to this question can
be explained in the following way.
Let{Vs}s∈S be a family of good U′
q(g)-modules and let J be a subset of S× C(q)×.
An element i∈J is denoted by i = (S(i),X (i)). We deﬁne a quiver Γ J as follows:
4 S.-J. KANG, M. KASHIW ARA, M. KIM
1) The set of vertices is taken to be J.
2) For i,j ∈J, let
Rnorm
VS(i),VS(j) : (VS(i))u⊗(VS(j))v→ (VS(j))v⊗(VS(i))u
be the normalized R-matrix. We put d many arrows from i toj whered is the order
of poles of Rnorm
VS(i),VS(j)(v/u) at v/u =X(j)/X(i).
Then the quiver Γ J deﬁnes a Cartan datum ( A = (aij)i,j∈J,P, Π,P∨, Π∨), where A is
determined by (
3.1.4). Hence we obtain a Khovanov-Lauda-Rouquier algebra RJ (β)
(β∈ Q+) with the parameters Qi,j(u,v ) = δ(i⁄=j)(u−v)dij (v−u)dji∈ k[u,v ]. Here,
Q+ = ∑
i∈J Z≥0αi denotes the positive root lattice.
Let β = ∑
i∈Jkiαi∈ Q+ with|β| := ∑
i∈Jki = n and let Jβ ={ν = (ν1,...,ν n)∈
Jn ; αν1 +··· +ανn =β}. For each sequence ν = (ν1,...,ν n)∈Jβ, set
Vν = (VS(ν1))aﬀ⊗···⊗ (VS(νn))aﬀ
and let ˆV⊗β be a certain completion of ⨁
ν∈J β
Vν. Then ˆV⊗β is endowed with a structure
of (U′
q(g),RJ (β))-bimodule. Hence we can deﬁne a functor
Fβ : Mod gr(RJ (β))→ Mod(U′
q(g))
by
M↦−→ˆV⊗β⊗RJ (β)M,
where Mod gr(RJ (β)) denotes the category of graded RJ (β)-modules and Mod( U′
q(g))
denotes the category of U′
q(g)-modules. We would like to emphasize that, in general,
the type of the quiver Γ J is irrelevant to the type of the aﬃne Lie algebra g or its
underlying ﬁnite-dimensional simple Lie algebra g0.
We denote by RJ (β)-gmod the category of ﬁnite-dimensional graded RJ (β)-modules
and set RJ -gmod = ⨁
β∈Q+
RJ (β)-gmod. We also denote by Cg the category of ﬁnite-
dimensional integrable U′
q(g)-modules.
The functorFβ enjoys two important properties:
(1)F := ⨁
β∈Q+
Fβ is a tensor functor; i.e., F sends a convolution product of objects
in RJ -gmod to a tensor product of U′
q(g)-modules in Cg.
(2)Fβ is exact if RJ (β) is of ﬁnite type A,D,E .
One of the most important features of the functor F is that the category RJ -gmod,
domain of the functor, has a Z-grading. For many years, it has been asked if the
category Cg, the codomain of F , has a Z-grading or not. This question has arisen
after the works of Varagnolo-Vasserot [ 36], Nakajima [ 32] and Hernandez [ 10], in which
it was shown that the Grothendieck ring K(Cg) of Cg has interesting t-deformations.
In particular, Nakajima provided an algorithm of calculating q-characters of simple
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 5
representations [ 32] using t-deformation. Thus one would expect that there might be
a Z-graded tensor category whose Grothendieck ring is isomorphic to one of such t-
deformations of K(Cg). We will see in the last half of this paper that the functor F
helps us construct such a category in type A(1)
N−1 case.
Precisely speaking, this is the case when J ={(V (̟1),q 2i)|i∈ Z}, where V (̟1) is
the fundamental representation of U′
q(ˆslN ) of weight ̟1. Then, by the construction,
the corresponding Khovanov-Lauda-Rouquier algebra is of type A∞ and the functor
Fn := ⨁
|β|=n
Fβ recovers the quantum aﬃne Schur-Weyl duality functor if we ident ify the
objects in RJ (n)-gmod := ⨁
|β|=n
RJ (β)-gmod with ﬁnite-dimensional H aﬀ
q (n)-modules in
an appropriate way ([
26, 34]).
LetA = RJ -gmod and let CJ be the full subcategory of Cg consisting of U′
q(ˆslN )-
modules M such that every composition factor of M appears as a composition factor
of a tensor product of modules of the form V (̟1)q2s (s∈ Z). Then CJ is an abelian
category and is stable under taking submodules, quotients, exten sions and tensor prod-
ucts. Moreover, CJ contains all the modules of the form V (̟i)(−q)s for 1≤i≤N− 1
and s∈i− 1 + 2Z (see § 4.7). Then F restricts to a functor from A toCJ .
Next, we construct a tensor category TJ in two steps. Let S be the kernel of the
functorF . Then S is a Serre subcategory of A. The quotient category A/S has a
structure of a tensor category with the convolution as tensor pr oduct. Secondly, we
localize the category A/S one step further to obtain a category TJ , where the RJ -
modules mapped to the trivial representations of U′
q(ˆslN ) byF are isomorphic to the
unit object inTJ . We then show that the categoryTJ is an abelian rigid tensor category;
i.e., every object in TJ has a right dual and a left dual. To prove our assertions, we
develop a general process of localization of tensor categories thr ough a commuting
family of central objects . We summarize this process in Appendix A.
Moreover, the functor F :A→C J factors through the category TJ . Hence, roughly
speaking,TJ can be regarded as a graded version of CJ . Note that the category TJ
is Z-graded (i.e., endowed with a grading shift functor), while the categ oryCJ is not.
Thus the structure of the category TJ is deﬁnitely richer than that of CJ .
One of our main results is that F induces a ring isomorphism between K(TJ )q=1,
the Grothendieck ring of TJ forgetting the grading and the Grothendieck ring K(CJ )
of the category CJ . Indeed, as proved in Theorem 4.7.5, K(TJ ) is isomorphic to the
t-deformationKt of K(CJ ) introduced by Hernandez-Leclerc in [ 12] (cf. [ 36, 32, 10]).
ThereforeTJ provides a Z-graded lifting of CJ as a rigid tensor category.
As we have seen so far, even the simplest case yields many interestin g and deep
applications of the functor F . We expect that a lot more exciting developments will
follow as we take various choices of the aﬃne algebra g and J.
6 S.-J. KANG, M. KASHIW ARA, M. KIM
This paper is organized as follows. In the ﬁrst section, we recall the notions of
