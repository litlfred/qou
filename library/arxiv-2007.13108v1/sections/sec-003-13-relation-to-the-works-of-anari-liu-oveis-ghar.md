---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-003-13-relation-to-the-works-of-anari-liu-oveis-ghar
section_title: "Relation to the works of Anari, Liu, Oveis-Gharan and Vinzant"
section_number: 1.3
pages: 5-6
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
doc_brief: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube — It is well-known that measures whose density is the form e−V where V is a uniformly convex potential on Rn attain"
---
A seemingly related notion of log-concavity of measures on the discrete hypercube was given in
a series of works by Anari, Liu, Oveis-Gharan and Vinzant in [ 2, 3]. Given {−1, 1}-Bernoulli
random variables X1, . . . , X n distributed according to a law ν, which can be identiﬁed with a
random subset A ⊂ [n] by Xi = 21i∈A − 1, they consider the generating polynomial
pν(z1, ..., z n) = E
∏
i∈A
zi.
They show that if p is both log-concave on the positive orthant and homogeneous (which is
equivalent to the fact ∑
i Xi is supported on one point), then the law of X1, ...X n admits, among
other things, strong concentration properties in the form o f a spectral gap (with respect to the
Glauber dynamics).
It is not hard to check that the log-concavity of the polynomi al pν is equivalent to the con-
dition
∇2L[ν](x) ≼ 2 (diag (∇L[ν](x)) + In) , ∀x ∈ Rn. (7)
Since ∇L[ν](x) ∈ [−1, 1]n, the above condition is strictly stronger our semi-log-con cavity
condition (2) with β = 4.
On a ﬁrst glance it may seem that Theorem 2 is effectively simi lar to [2, Theorem 1.1] (and
could perhaps follow from the same methods), however we beli eve that this is not the case, and
the resemblance between the two results is mainly on a superﬁ cial level. A crucial difference
between the results is that our notion of log-concavity is in variant under reﬂections about the
coordinate axes, whereas in the latter notion, the directio n (1, ..., 1) has a special role. In cases
of interest, such as homogeneous distributions where |A| ≪ n, condition (7) is actually closer
to strict log-concavity.
Since the multi-linear polynomial pν is harmonic, its log-concavity implies that the Hessian
matrix can have only one non-negative eigenvalue. In this se nse, condition (7) is much more
rigid than our condition. Respectively, while our proof is b ased mainly on analytic methods,
the proof in [2] has a more algebraic ﬂavor (and is also based t he theory of high-dimensional
5
expanders). We do not know if there is a deeper connection bet ween the results, but it doesn’t
seem that any of the two follows from the other.
On the other hand, Theorem 5 seems rather closely related to [ 3, Theorem 5.2], and the
former can be thought of as a soft and modiﬁed version of the la tter: Indeed, condition (5),
compared to (7) is invariant under coordinate reﬂections an d softer in the sense that β can be
larger than 1, but otherwise rather similar. The proof of the latter is sim pler and basically
reduces to an application of Jensen’s inequality, whereas o ur proof (a small variation thereof
also implies the latter bound) is slightly more complicated and uses stochastic calculus; we do
not know if it can be attained by more elementary techniques.
Finally, in relation to Corollary 8, a result of a similar spi rit appears in [1]. A corollary of
the main theorem there shows that if ν is d-homogeneous and all measures obtainable from ν
by conditioning are pairwise-negatively correlated, then it has a spectral gap polynomial in n.
It seems however, that the assumption of homogeneouity is cr ucial in this case.
Acknowledgements
We’d like to thank Bo’az Klartag for a fruitful discussion, a s well as Nima Anari and Jan
V ondrak and Pranav Nuti for some enlightening comments on a p reliminary version of this
manuscript.
