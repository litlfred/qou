---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-038-9-fusion-categories-in-positive-characteristic
section_title: "Fusion categories in positive characteristic"
section_number: 9
pages: 43-44
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
In this section we will consider fusion and multi-fusion categories ove r an al-
gebraically closed ﬁeld k of positive characteristic p. We will show that many of
the results of the previous sections continue to hold in this case aft er very minor
modiﬁcations.
9.1. List of modiﬁcations. Fusion and multi-fusion categories in characteristic p
are deﬁned in the same way as in charactersitic zero. Below we will des cribe the
modiﬁcations which need to be made to validate the statements from the previous
sections in this case.
Section 2. The statements of subsections 2.1, 2.2 which make sense generalize
without changes, except the last statement of Theorem 2.3, which claims that the
global dimension of a fusion category is nonzero. This is in fact false in positive
characteristic. For example, if G is a ﬁnite group whose order is divisible by p, then
the category of modules over the function algebra Fun( G,k ) is a fusion category
of global dimension |G| = 0. This is the main diﬀerence between the zero and
positive characteristic case. To deal with this diﬀerence, we introd uce the following
deﬁnition.
Deﬁnition 9.1. A fusion category over k is said to be nondegenerate if its global
dimension is nonzero. An indecomposable multi-fusion category is non degenerate if
at least one of its component categories is nondegenerate. A multi- fusion category
is nondegenerate if all its indecomposable parts are nondegenerat e. A regular semi-
simple weak Hopf algebra over k is nondegenerate if its category of representations
is a nondegenrate multi-fusion category.
Theorems 2.15, 2.16, 2.18 remain valid if the category C is nondegenerate. Propo-
sition 2.17 remains true without any additional conditions.
In Section 2.5 (and at other places throughout), the algebra R has to be chosen in
such a way that its block sizes are not divisible by p (since only such algebras admit
a symmetric separability idempotent). Theorem 2.20 is valid for such R. Corollary
2.22 and Theorem 2.24 also remain valid. Theorem 2.26 is valid for nondeg enerate
weak Hopf algebras.
Theorems 2.27, 2.28, 2.30, 2.31, and Corollary 2.35 remain valid for non degener-
ate categories. More precisely, in Theorems 2.27, 2.31 one only need s nondegeneracy
of the category C.
Remark 9.2. We note that the nondegeneracy condition is essential. For example ,
ifA is the Hopf algebra Fun(G,k ), where the order of G is divisible by p, then The-
orem 2.15 is false for Rep( A), and Theorem 2.26 is false for A. Similarly, Theorem
2.27 is false for Rep( A) and the identity functor, since the corresponding cohomol-
ogy is Hi(G,k ), which may be nonzero if the order of G is divisible by p. However,
we do not know a counterexample to Theorem 2.28 in positive charact eristic.
Sections 3-7. While Section 3 makes no sense in positive characteristic, the
material of Section 4 generalizes without changes, as long as one co nsiders regular
weak Hopf algebras. The only change in Section 5 is that one should alw ays choose
44 PA VEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
nonzero block sizes for the algebra R (except subsections 5.8,5.9 where the char-
acteristic should be zero). Theorems 6.3 and 7.5 are valid for nondeg enerate weak
Hopf algebras.
Section 8. The results of Section 8.1 generalize without changes, since they
have nothing to do with the characteristic of the ground ﬁeld. So do the results of
Section 8.2, except Proposition 8.12, Corollary 8.14, and Proposition 8.15, which
are valid for nondegenerate categories. Finally, let us point out tha t Theorem 8.33
is valid in positive characteristic.
Example. A semisimple Hopf algebra H is nondegenerate if and only if it is
cosemisimple. Indeed, if H is nondegenerate, then so is Rep( H), and hence H ∗
is semisimple, since Rep( H ∗op) is a dual category to Rep( H). Conversely, if H
is cosemisimple, then Tr( S2) ⁄= 0 ([LR1]), so the global dimension of Rep( H) is
nonzero, and H is nondegenerate.
