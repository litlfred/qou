---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-005-25-results-on-weak-hopf-algebras
section_title: "Results on weak Hopf algebras"
section_number: 2.5
pages: 7-9
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
fusion categories is using weak Hopf algebras (see Section 4 for the deﬁnitions).
Namely, let C be a multi-fusion category. Let R be a ﬁnite dimensional semisimple
k-algebra, and F a ﬁber functor (i.e. an exact, faithful tensor functor) from C to
R-bimod. Let A = Endk(F ) (i.e. the algebra of endomorphisms of the composition
of F with the forgetful functor to vector spaces).
Theorem 2.20. ([Sz])A has a natural structure of a semisimple weak Hopf algebra
with base R, and C is equivalent, as a tensor category, to the category Rep (A) of
ﬁnite dimensional representations of A.
Remark 2.21. In order to lift the naturally existing map A →A ⊗RA to a weak
Hopf algebra coproduct A →A ⊗kA, one needs to use a separability idempotent in
R ⊗R. We will always use the unique symmetric separability idempotent. In this
case, the weak Hopf algebra A satisﬁes an additional regularity condition, saying
that the squared antipode is the identity on the base of A.
One can show that for any multi-fusion category C, a ﬁber functor F exists for
a suitable R. Indeed, let M be any semisimple faithful module category over C,
8 PA VEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
i.e. such that any nonzero object of C acts by nonzero (for example, C itself).
Let R be a semisimple algebra whose blocks are labeled by simple objects of M:
R = ⊕M∈Irr(M)RM , and RM are simple. Now deﬁne a functor F : C → R − bimod
as follows: for any object X ∈ C set
F (X) = ⊕M,N ∈Irr(M)HomM(M,X ⊗N ) ⊗BNM,
whereBNM is the simple ( RN,RM )-bimodule. This functor has an obvious tensor
structure (coming from composition of morphisms), and it is clearly e xact and
faithful. So it is a ﬁber functor.
Therefore, we have
Corollary 2.22. ([H],[Sz]) Any multi-fusion category is equivalent to the category
of ﬁnite dimensional representations of a (non-unique) reg ular semisimple weak
Hopf algebra. This weak Hopf algebra is connected if and only if C is a fusion
category.
Remark 2.23. In particular, we can choose R to be a commutative algebra (i.e.,
all blocks have size 1). Thus, any multi-fusion category is equivalent to the category
of representations of a weak Hopf algebra with a commutative base . This result
was proved by Hayashi in [H], where weak Hopf algebras with commuta tive bases
appear under the name “face algebras”.
The language of weak Hopf algebras is convenient to visualize various categorical
constructions. One of them is that of a dual category. Indeed, le t C be the category
of representations of a weak Hopf algebra A. Let R be the base of A. Then we
have a natural ﬁber functor from C to the category of R-bimodules – the forgetful
functor. This functor deﬁnes a natural structure of a module ca tegory over C on
the category M = R − bimod. In this case, the dual category C∗
M is simply the
representation category of the dual weak Hopf algebra A∗cop with the opposite
coproduct (see [O]). Furthermore, as we just showed, this examp le is general, in
the sense that any faithful module category over a multi-fusion ca tegory can be
obtained in this way.
The global dimension of the category of representations of a conn ected weak
Hopf algebra is closely related to the trace of squared antipode in th is weak Hopf
algebra. This connection is expressed by the following theorem.
Let a fusion category C be the representation category of a regular semisimple
weak Hopf algebra A. Let S be the antipode of A. Let qi be the primitive idem-
potents of the center of the base At, and ni the block sizes of the matrix algebras
qiAt.
Theorem 2.24. One has Tr (S2|qjAS(qi)) = dim( C)n2
in2
j . In particular, over C one
always has Tr (S2|qjAS(qi))> 0.
Remark 2.25. Theorem 2.24 implies that Tr( S2|A) = dim(Rep(A)) dim(At)2.
We also have the following result, which generalizes the Larson-Radf ord theorem
for Hopf algebras [LR1].
Theorem 2.26. A semisimple weak Hopf algebra over k is also cosemisimple.
Theorem 2.24 is proved in Section 5. Theorem 2.26 follows from Theore m 2.18,
since the representation category of the dual weak Hopf algebra is the dual category.
ON FUSION CATEGORIES 9
2.6. V anishing of the Y etter cohomology . The cohomology theory that con-
trols deformations of tensor categories and tensor functors is t he cohomology theory
developed in [CY, Y1, Y2, Da], which we will call the Yetter cohomology t heory.
This theory associates to any tensor category C and a tensor functor F for C to
another tensor category C′, a sequence of cohomology spaces Hi
F (C) (See Section
7). If F is the identity functor, then these groups are simply denoted by Hi(C).
Namely, ﬁrst order deformations of C are elements of H 3(C), while ﬁrst order defor-
mations of a tensor structure on a given functor F between ﬁxed tensor categories
C, C′ are elements of H 2
F (C). Obstructions to such deformations lie, respectively, in
H 4(C) and H 3
F (C).
For multi-fusion categories, the Yetter cohomology often vanishe s. Namely, we
have the following result.
Theorem 2.27. Let C, C′ be multi-fusion categories, and F : C → C ′ be a (unital)
tensor functor from C to C′. Then Hi
F (C) = 0 for i> 0.
Theorem 2.27 is proved in Section 7, using weak Hopf algebras. The ide a of this
proof is due to Ocneanu, Blanchard, and Wassermann.
