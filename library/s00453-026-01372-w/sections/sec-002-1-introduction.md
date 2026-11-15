---
doc_id: s00453-026-01372-w
doc_title: "Concentration of Submodular Functions and Read-k Families Under Negative Dependence"
section_id: sec-002-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: s00453-026-01372-w.pdf
source_sha256: 98b569eff84fb489
toc_source: outline
doc_brief: "Concentration of Submodular Functions and Read-k Families Under Negative Dependence — We study the question of whether submodular functions of random variables satisfying various notions of negative"
---
Concentration inequalities are ubiquitous in discrete mathematics and theoretical com-
puter science [5, 6]. The most canonical examples are the Chernoff-Hoeffding bounds,
which show strong concentration for linear combinations of independent random vari-
ables [7, 8]. In some applications, the condition of independence is too restrictive, so
weaker notions have been considered [9–11]. Of interest to us is the setting where
the random variables are negatively correlated, which arises naturally, for example, in
This work was originally presented at ITCS 2025.
B George Z. Li
gzli929@gmail.com
B Renata Valieva
rvalieva@umd.edu
1
University of Maryland, College Park, MD, USA
2
Carnegie Mellon University, Pittsburgh, PA, USA
21
Page 2 of 19
Algorithmica (2026) 88 :21
designing approximation algorithms by solving a linear or semideﬁnite program and
applying some dependent randomized rounding algorithm [12]. For this setting, [13]
showed that the Chernoff-Hoeffding bounds can be shown under the weak notion of
negative cylinder dependence: this and other standard notions of negative dependence
are deﬁned in Section 2.1.
For some applications in combinatorial optimization, algorithmic game theory,
and machine learning, one needs to consider the more general class of submod-
ular functions f of the random variables, rather than simple linear combinations.
When the binary random variables X1, . . . , Xn are independent, it was shown that
f (X1, . . . , Xn) still satisﬁes Chernoff bounds exactly [2]. When there is dependence
between the random variables, the results are much weaker. The only known results
are for random variables that are output by speciﬁc dependent-rounding algorithms,
known as swap rounding and pipage rounding [2, 3]. These results showed that a
Chernoff-like lower-tail bound also holds for submodular functions for their speciﬁc
dependent rounding procedure. As noted in the work of [14], it is not clear how to
generalize either of these proofs to any general notion of negative dependence.
We introduce a new notion of negative dependence, called 1-negative association,
which is weaker than negative association and negative regression but stronger than
negative cylinder dependence, i.e., every distribution satisfying negative association or
negative regression also satisﬁes 1-negative association, which in turn implies negative
cylinder dependence.
Deﬁnition 1 A collection of random variables X1, . . . , Xn is said to satisfy 1-negative
association if for any two monotone functions f and g, where g depends on a single
random variable Xi and f depends on the remaining random variables {X j} j∈[n]\{i},
we have E[ f g] ≤E[ f ]E[g].
Importantly, while in general it is weaker than the notion of weak negative regres-
sion introduced by [1], 1-negative association is equivalent to it when the variables
X1, . . . , Xn are binary. Further details are provided in Section 3.1.
Our main result is that the Chernoff-like bound shown in [2, 3] also hold under
1-negative association (see Section 3.2). In particular, this implies the following:
Theorem 1.1 Let X1, . . . , Xn be binary random variables with mean x1, . . . , xn satis-
fying negative association (or negative regression). Let f be a non-negative monotone
submodular function with marginal values in [0, 1] and let F be the multilinear exten-
sion of f . If we let μ0 = F(x1, . . . , xn), then for any δ ∈(0, 1) we have
Pr[ f (X1, . . . , Xn) ≤(1 −δ) · μ0] ≤exp(−μ0δ2/2).
A few remarks are in order. First, we highlight that the concentration in the above
theorem is with respect to the value of the multilinear extension F(x1, . . . , xn), rather
than the true expected value E[ f (X1, . . . , Xn)]. In general, the true expected value can
be greater than the value of multilinear extension [1]. Nevertheless, this sufﬁces for
applications relating to submodular maximization, and is the same type of concentra-
tion result shown in previous work. Second, recall that negative cylinder dependence
Algorithmica (2026) 88 :21
Page 3 of 19
21
does not sufﬁce to show this concentration bound [2, p. 583]. As a result, our results are,
in some informal sense, almost tight in terms of the condition on negative dependence.
In addition to providing submodular concentration results for a wide class of round-
ing algorithms and distributions, our results also give a new path toward understanding
why pipage rounding and swap rounding satisfy the lower-tail Chernoff bound. By
proving that the rounding algorithms output random variables which are 1-negatively
associated, we immediately obtain a new proof of the lower tail bounds. This can be
viewed as evidence that the two rounding algorithms satisfy 1-negative association or
even negative association/regression. We leave this as an interesting open question.
Techniques.
We use the standard method of bounding the exponential moments for lower-tail
Chernoff bounds. Our idea is to show that the exponential moments for our negatively-
correlated random variables is upper bounded by the exponential moments for
independent copies of the random variables. Formally, let X1, . . . , Xn be random
variables satisfying 1-negative association and let X∗
1, . . . , X∗
n be independent copies
of the random variables. We show for any λ < 0, we have
E[exp(λ · f (X1, . . . , Xn))] ≤E[exp(λ · f (X∗
1, . . . , X∗
n))].
Since the exponential-moments method has been used to prove Chernoff bounds for
submodular functions in the independent case [2], we can then repeat their proof and
conclude with our desired result. We believe this proof idea may be of independent
interest. For example, the same ideas can show that for a supermodular function g and
any λ > 0, we have
E[exp(λ · g(X1, . . . , Xn))] ≤E[exp(λ · g(X∗
1, . . . , X∗
n))].
Inotherwords,wehavemorallyproventhefollowingstatement:anyupper-tailconcen-
tration bound which can be proven for a supermodular function g under independence
based on the exponential-moments method also holds when the underlying random
variables are negatively associated. As an example, we can apply this to a read-k family
of supermodular functions g1, . . . , gr for negatively associated random variables [4].
A read-k family is deﬁned as a set of functions where each variable appears in at most
k functions. This concept is particularly useful in scenarios where functions need to
model or manage overlapping sets of variables with constraints on their interaction.
We highlight that the proof of concentration for read-k families given in [4] doesn’t use
the exponential-moments method, but instead it is based on the entropy method. We
address this by giving a simpler proof of their results, this time using the exponential
moments method. This gives the ﬁrst concentration results for a class of supermodular
functions under negatively correlated random variables, and is detailed in Section 3.3.
Applications.
Our motivation for studying the problem comes from the randomized-rounding
paradigm in approximation algorithms for converting a fractional solution to a lin-
ear program into an integral one. In many such randomized-rounding schemes, the
output random variables have been shown to satisfy strong negative dependence prop-
erties, such as negative association [12, 15]. For all such rounding algorithms, our
21
Page 4 of 19
Algorithmica (2026) 88 :21
results immediately imply the submodular Chernoff lower-tail bound. It remains an
interesting open question to efﬁciently sample negatively dependent distributions for a
wider class of set systems. A particularly interesting algorithm is given in the work of
[16]; they show that a fractional point in a matroid polytope can be rounded to an inte-
gral one such that the resulting distribution preserves marginals and satisﬁes negative
association. However, a gap identiﬁed in their proof [1] complicates the application
of their approach. The implications of this issue for the applicability of our results
remain an area for further investigation.
As a concrete application, we consider the maximum coverage problem under group
fairness constraints. Here, we have a universe of elements {1, . . . , n}, a collection
S1, . . . , Sm of subsets of the universe, and a budget k. We are further given subsets
C1, . . . , Cℓ⊆[n] (which should be thought of as demographic groups) along with
thresholds w1, . . . , wℓ. Our goal is to choose k sets from the collection to maximize the
number of elements covered subject to the fairness constraint each demographic group
is sufﬁciently covered (i.e., at least w j elements from C j are covered). Since this is a
special case of multiobjective submodular maximization, there exists a (1 −1/e −ϵ)-
approximation to the problem such that each fairness constraint is approximately
satisﬁed [2, 17]. Unfortunately, these results rely on the randomized swap-rounding
algorithm due to its submodular concentration properties, which requires a super-linear
time complexity. While swap rounding can be implemented with poly-logarithmic
depth [18], a simpler dependent-rounding algorithm of [15] requires linear work and
only O(log n) depth, which improves the efﬁciency. Observe that the pre-processing
step in [17] only requires O(nℓ) time. Since we can solve the linear program for fair
maximum coverage in near-linear time [19], we obtain a near-linear time algorithm
for the problem after using the efﬁcient rounding algorithm of [15]. These same ideas
can be used to improve the time complexity of the algorithm by [20] for inﬂuence
maximization with group-fairness constraints. Since the proofs are similar to previous
work, we defer the details to a future version of the paper.
More generally, negatively-associated random variables show up naturally in many
settings (see e.g., the primer by [21]). [22] studied the canonical example of balls and
bins, and showed that it satisﬁed both negative association and negative regression.
Another example satisfying the negative-association conditions are any product mea-
sure over the set of bases of a balanced matroid, as shown by [23]. A ﬁnal setting
where such random variables occur are random spanning trees, which have been vital
in the recent improvements to approximation algorithms for the traveling salesperson
problem (see, e.g., [24]). Random spanning trees are known to be strongly Rayleigh,
which immediately implies that they are negatively associated. Our results may be
interesting here as well.
We also observe that the online rounding scheme of [25] has the strongly Rayleigh
property: we immediately get strong concentration (on the lower-tail side) for mono-
tone submodular functions, when the inputs for the function arrive online along with
their (Bernoulli) distributions as in the setup of [25].
Related Work.
The concentration of negatively-dependent random variables was ﬁrst formally stud-
ied by [26], which showed a central limit theorem for a certain notion of negative
dependence. Later on, [13] showed that cylinder negatively dependent random vari-
Algorithmica (2026) 88 :21
Page 5 of 19
21
ables yield the Chernoff-Hoeffding concentration inequalities, just like independent
random variables. In the context of our paper, these results are somewhat specialized
since they focus on linear combinations of random variables.
For non-linear functions of the random variables, the majority of work has focused
on the concentration of Lipschitz functions under various notions of negative depen-
dence. [27] showed that for strong Rayleigh measures, one has Gaussian concentration
for any Lipschitz function. Later on, [14] corrected an earlier proof of [22], showing
that McDiarmid-like concentration results hold for Lipschitz functions of random vari-
ables satisfying negative regression. These results are complementary to ours since
we are trying to give dimension-free concentration results.
