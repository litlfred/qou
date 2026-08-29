---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
Throughout this paper (except for Section 9), k denotes an algebraically closed
ﬁeld of characteristic zero. By a fusion category C over k we mean a k-linear
semisimple rigid tensor (=monoidal) category with ﬁnitely many simple ob jects
and ﬁnite dimensional spaces of morphisms, such that the endomor phism algebra
of the neutral object is k (see [BaKi]). Fusion categories arise in several areas of
mathematics and physics – conformal ﬁeld theory, operator algeb ras, representation
theory of quantum groups, and others.
This paper is devoted to the study of general properties of fusion categories. This
has been an area of intensive research for a number of years, and many remarkable
results have been obtained. However, many of these results were proved not in
general but under various assumptions on the category. The goa l of this paper is to
remove such assumptions, and to give an account of the theory of fusion categories
in full generality.
The structure of the paper is as follows.
In Section 2, we give our main results about squared norms, global d imensions,
weak Hopf algebras, and Ocneanu rigidity. This section contains man y results which
are partially or fully due to other authors, and our own results are b lended in at
appropriate places.
Sections 3-7 are mostly devoted to review of the technical tools an d to proofs of
the results of Section 2. Namely, in section 3, we prove one of the ma in theorems
of this paper, saying that any fusion category has a nonzero globa l dimension (in
fact, we show that for k = C, the dimension is positive). The proof relies in an
essential way on the theorem that in any fusion category, the iden tity functor is
isomorphic to ∗ ∗ ∗∗ :V ↦→V ∗∗∗∗ (where V ↦→V ∗ is the duality in C), as a tensor
functor, which is proved using the theory of weak Hopf algebras (m ore speciﬁcally,
the formula for the fourth power of the antipode from [N]). We also p rove that the
SL2(Z)-representation attached to any modular category over C is unitary.
1
2 PA VEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
In Section 4, we give a short review of the theory of weak Hopf algeb ras, which
are both a tool and an object of study in this paper, and prove the isomorphism
between the identity functor Id and ∗ ∗ ∗∗, which is crucial for the main theorem.
In Section 5, we prove a formula for the trace of squared antipode of a semisimple
connected regular weak Hopf algebra. Then we proceed to prove a number of results
(partially due to M¨ uger) about semisimplicity of the category of mod ule functors
between module categories over a fusion category, in particular of the dual and
the Drinfeld center. We also generalize these results to multi-fusion categories
(the notion obtained from that of a fusion category by relaxing the condition that
End(1) = k). In particular, we prove that a semisimple weak Hopf algebra over k
is cosemisimple. Finally, we prove a categorical version of the class eq uation of Kac
and Zhu.
In Section 6, we consider a pair of semisimple weak Hopf algebras B ⊂ A and
study the subcomplex of B-invariants in the co-Hochschild complex of A (this com-
plex is a weak analog of the complex considered in [Sch], [EG1] for Hopf a lgebras).
We prove that this complex is acyclic in positive degrees.
In Section 7, we show that the complex considered in Section 6 coincid es with
the deformation complex of a monodial functor between two multi-f usion categories
introduced independently by Yetter [Y1, Y2] and Davydov [Da]. Using this, we
establish “Ocneanu rigidity” (absence of deformations) for arbitr ary nondegenerate
multi-fusion categories and tensor functors between them. The id ea of the proof
of this result is due to Ocneanu-Blanchard-Wassermann, and the f usion category
case was worked out completely by Blanchard-Wassermann in [Wa, B Wa] under
the assumption that the global dimension is non-zero.
In Section 8 we discuss the notion of Frobenius-Perron dimensions o f objects in
a fusion category, show that they are additive and multiplicative, an d have similar
properties to categorical dimensions in a pivotal category. We pro ve a categorical
analogue of the Nichols-Zoeller freeness theorem (saying that a ﬁn ite dimensional
Hopf algebra is a free module over a Hopf subalgebra), in particular p rove the free-
ness theorem for semisimple quasi-Hopf algebras. We also show that the global
dimension of a fusion category is divisible by its Frobenius-Perron dime nsion (in
the ring of algebraic integers), and the ratio is ≤ 1. In particular, if the Frobenius-
Perron dimension of a fusion category is an integer, then it coincides with the global
dimension. This result may be regarded as a categorical version of t he well known
theorem of Larson and Radford, saying that the antipode of a sem isimple Hopf
algebra is involutive. Further, we show that the Frobenius-Perron dimension of a
fusion category is divisible by the Frobenius-Perron dimension of its f ull subcat-
egory, and use this result to show that any fusion category of Fro benius-Perron
dimension p (a prime) is the category of representations of a cyclic group with a
3-cocycle. We also classify fusion categories of dimension p2. Finally, we show
that the property of a fusion category to have integer Frobenius -Perron dimensions
(which is equivalent to being the representation category of a quas i-Hopf algebra) is
stable under basic operations with categories, in particular is “weak Morita invari-
ant” (i.e. invariant under passing to the the opposite of the dual ca tegory). At the
end of the section we deﬁne group-theoretical fusion categories , which is a subclass
of fusion categories with integer Frobenius-Perron dimensions; th ey are constructed
explicitly from ﬁnite groups.
ON FUSION CATEGORIES 3
Many of the results of this paper have analogs in positive character istic. These
generalizations are given in Section 9. In particular, we show that a f usion category
of nonzero global dimension over a ﬁeld of positive characteristic ca n be lifted to
characteristic zero.
Throughout the paper, we are going to freely use the theory of rig id tensor
categories. We refer the reader to the textbooks [K],[BaKi] for de tails. We also
recommend the reader the expository paper [CE], where much of th e content of
this paper is discussed in detail.
Acknowledgments. The research of P.E. was partially supported by the NSF
grant DMS-9988796, and was done in part for the Clay Mathematics Institute. The
research of D.N. was supported by the NSF grant DMS-0200202. T he research of
V.O. was supported by the NSF grant DMS-0098830. We are gratef ul to A. Davy-
dov, A. Kirillov Jr., M. M¨ uger, and A. Wassermann for useful discus sions, and to
E. Blanchard for giving us the formulation of the result of [BWa] bef ore publication.
