---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.979
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
Throughout this paper (except for Section 9), $k$ denotes an algebraically closed field of characteristic zero. By a *fusion category* ${\mathcal C}$ over $k$ we mean a $k$-linear semisimple rigid tensor (=monoidal) category with finitely many simple objects and finite dimensional spaces of morphisms, such that the endomorphism algebra of the neutral object is $k$ (see [@BaKi]). Fusion categories arise in several areas of mathematics and physics -- conformal field theory, operator algebras, representation theory of quantum groups, and others.

This paper is devoted to the study of general properties of fusion categories. This has been an area of intensive research for a number of years, and many remarkable results have been obtained. However, many of these results were proved not in general but under various assumptions on the category. The goal of this paper is to remove such assumptions, and to give an account of the theory of fusion categories in full generality.

The structure of the paper is as follows.

In Section 2, we give our main results about squared norms, global dimensions, weak Hopf algebras, and Ocneanu rigidity. This section contains many results which are partially or fully due to other authors, and our own results are blended in at appropriate places.

Sections 3-7 are mostly devoted to review of the technical tools and to proofs of the results of Section 2. Namely, in section 3, we prove one of the main theorems of this paper, saying that any fusion category has a nonzero global dimension (in fact, we show that for $k={\mathbb{C}}$, the dimension is positive). The proof relies in an essential way on the theorem that in any fusion category, the identity functor is isomorphic to ${****}: V \mapsto V^{****}$ (where $V \mapsto V^*$ is the duality in ${\mathcal C}$), as a tensor functor, which is proved using the theory of weak Hopf algebras (more specifically, the formula for the fourth power of the antipode from [@N]). We also prove that the $SL_2({\mathbb Z})$-representation attached to any modular category over ${\mathbb{C}}$ is unitary.

In Section 4, we give a short review of the theory of weak Hopf algebras, which are both a tool and an object of study in this paper, and prove the isomorphism between the identity functor ${\rm Id}$ and ${****}$, which is crucial for the main theorem.

In Section 5, we prove a formula for the trace of squared antipode of a semisimple connected regular weak Hopf algebra. Then we proceed to prove a number of results (partially due to Müger) about semisimplicity of the category of module functors between module categories over a fusion category, in particular of the dual and the Drinfeld center. We also generalize these results to multi-fusion categories (the notion obtained from that of a fusion category by relaxing the condition that $\text{End}(\mathbf 1)=k$). In particular, we prove that a semisimple weak Hopf algebra over $k$ is cosemisimple. Finally, we prove a categorical version of the class equation of Kac and Zhu.

In Section 6, we consider a pair of semisimple weak Hopf algebras $B\subset A$ and study the subcomplex of $B$-invariants in the co-Hochschild complex of $A$ (this complex is a weak analog of the complex considered in [@Sch], [@EG1] for Hopf algebras). We prove that this complex is acyclic in positive degrees.

In Section 7, we show that the complex considered in Section 6 coincides with the deformation complex of a monodial functor between two multi-fusion categories introduced independently by Yetter [@Y1; @Y2] and Davydov [@Da]. Using this, we establish "Ocneanu rigidity" (absence of deformations) for arbitrary nondegenerate multi-fusion categories and tensor functors between them. The idea of the proof of this result is due to Ocneanu-Blanchard-Wassermann, and the fusion category case was worked out completely by Blanchard-Wassermann in [@Wa; @BWa] under the assumption that the global dimension is non-zero.

In Section 8 we discuss the notion of Frobenius-Perron dimensions of objects in a fusion category, show that they are additive and multiplicative, and have similar properties to categorical dimensions in a pivotal category. We prove a categorical analogue of the Nichols-Zoeller freeness theorem (saying that a finite dimensional Hopf algebra is a free module over a Hopf subalgebra), in particular prove the freeness theorem for semisimple quasi-Hopf algebras. We also show that the global dimension of a fusion category is divisible by its Frobenius-Perron dimension (in the ring of algebraic integers), and the ratio is $\le 1$. In particular, if the Frobenius-Perron dimension of a fusion category is an integer, then it coincides with the global dimension. This result may be regarded as a categorical version of the well known theorem of Larson and Radford, saying that the antipode of a semisimple Hopf algebra is involutive. Further, we show that the Frobenius-Perron dimension of a fusion category is divisible by the Frobenius-Perron dimension of its full subcategory, and use this result to show that any fusion category of Frobenius-Perron dimension $p$ (a prime) is the category of representations of a cyclic group with a 3-cocycle. We also classify fusion categories of dimension $p^2$. Finally, we show that the property of a fusion category to have integer Frobenius-Perron dimensions (which is equivalent to being the representation category of a quasi-Hopf algebra) is stable under basic operations with categories, in particular is "weak Morita invariant" (i.e. invariant under passing to the the opposite of the dual category). At the end of the section we define group-theoretical fusion categories, which is a subclass of fusion categories with integer Frobenius-Perron dimensions; they are constructed explicitly from finite groups.

Many of the results of this paper have analogs in positive characteristic. These generalizations are given in Section 9. In particular, we show that a fusion category of nonzero global dimension over a field of positive characteristic can be lifted to characteristic zero.

Throughout the paper, we are going to freely use the theory of rigid tensor categories. We refer the reader to the textbooks [@K],[@BaKi] for details. We also recommend the reader the expository paper [@CE], where much of the content of this paper is discussed in detail.

**Acknowledgments.** The research of P.E. was partially supported by the NSF grant DMS-9988796, and was done in part for the Clay Mathematics Institute. The research of D.N. was supported by the NSF grant DMS-0200202. The research of V.O. was supported by the NSF grant DMS-0098830. We are grateful to A. Davydov, A. Kirillov Jr., M. Müger, and A. Wassermann for useful discussions, and to E. Blanchard for giving us the formulation of the result of [@BWa] before publication.
