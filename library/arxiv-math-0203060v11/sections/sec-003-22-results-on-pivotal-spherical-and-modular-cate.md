---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-003-22-results-on-pivotal-spherical-and-modular-cate
section_title: "Results on pivotal, spherical, and modular categories"
section_number: 2.2
pages: 5-7
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
a pivotal fusion category. In such a category, one can deﬁne the dimension of an
object V by dim(V ) = TrV (i), and we have the following result which justiﬁes the
notation |V |2.
Proposition 2.9. In a pivotal fusion category one has |V |2 = dim(V ) dim(V ∗)
for any simple object V . Moreover, if k = C then dim(V ∗) = dim(V ), so |V |2 =
| dim(V )|2.
Proposition 2.9 is proved in Section 3.
This result can be further specialized to spherical (in particular, rib bon) cat-
egories, (see [Mu1]). Namely, recall from [Mu1] that a pivotal fusion category is
spherical if and only if dim( V ) = dim(V ∗) for all simple objects V . Thus we have
the following corollary.
Corollary 2.10. In a spherical category, |V |2 = dim(V )2. In particular, if k = C,
then dim(V ) is (totally) real.
Corollary 2.10 readily follows from Proposition 2.9.
Remark 2.11. We note that in [Mu1], the number |V |2 is called the squared di-
mension of V , and denoted d2(V ). We do not use this terminology for the following
reason. In a pivotal category over C, the dimensions of simple objects do not have
to be real numbers (it suﬃces to consider the category of repres entations of a ﬁnite
group G, where i is given by a nontrivial central element of G). Thus, in general
dim(V ∗) ⁄= dim(V ), and |V |2 ⁄= dim(V )2. Therefore, the term “squared dimen-
sion”, while being adequate in the framework of spherical categorie s of [Mu1], is no
longer adequate in our more general setting.
6 PA VEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
Now assume that C is a modular category (i.e., a ribbon fusion category with a
nondegenerateS-matrix, see [BaKi]). In this case one can deﬁne matrices S andT
of algebraic numbers, which yield a projective representation of th e modular group
SL2(Z) ([BaKi]). We note that the matrix S is deﬁned only up to a sign, since
in the process of deﬁning S it is necessary to extract a square root of the global
dimension of C. So to be more precise we should say that by a modular category
we mean the underlying ribbon category together with a choice of th is sign.
Proposition 2.12. If k = C then the projective representation of SL2(Z) associ-
ated to C is unitary in the standard hermitian metric (i.e. the matric es S and T
are unitary).
Proposition 2.12 is proved in Section 3.
Remark 2.13. As before, the proposition actually means that this representatio n
is totally unitary, i.e. the algebraic conjugates of this representat ion are unitary as
well.
Remark 2.14. It is interesting whether Proposition 2.12 generalizes to mapping
class groups of higher genus Riemann surfaces.
We note that the results of this subsection are known for hermitian categories
[BaKi]. Our results imply that these results are valid without this assu mption.
2.3. Module categories, the dual category , the Drinfeld center. Let M
be an indecomposable left module category over a rigid tensor categ ory C [O] (all
module categories we consider are assumed semisimple). This means, M is a module
category which cannot be split in a direct sum of two nonzero module s ubcategories.
In this case one can deﬁne the dual category C∗
M to be the category of module
functors from M to itself: C∗
M = FunC(M, M) [O]. This is a rigid tensor category
(the tensor product is the composition of functors, the right and left duals are the
right and left adjoint functors).
For example, let us consider C itself as a module category over C ⊗ C op, via
(X,Y ) ⊗Z =X ⊗Z ⊗Y . Then the dual category is the Drinfeld center Z(C) of C
(see [O1, Mu2]; for the basic theory of the Drinfeld center see [K]).
The following result was proved by M¨ uger [Mu1, Mu2] under the ass umption
dim(C) ⁄= 0 (which, as we have seen, is superﬂuous in zero characteristic) a nd
minor additional assumptions.
Theorem 2.15. For any indecomposable module category M over a fusion category
C, the category C∗
M is semisimple (so it is a fusion category), and dim(C∗
M) =
dim(C). In particular, for any fusion category C the category Z(C) is a fusion
category of global dimension dim(C)2.
In fact, we have the following more general results, which (as well a s the results
in the next subsection) are inspired by [Mu1, Mu2].
Theorem 2.16. For any module categories M1, M2 over a fusion category C, the
category of module functors FunC(M1, M2) is semisimple.
Theorems 2.15 and 2.16 are proved in Section 5.
ON FUSION CATEGORIES 7
