---
doc_id: 1-s20-s002212362200012x-main
doc_title: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-004-13-relation-to-the-works-of-anari-liu-oveis-ghar
section_title: "Relation to the works of Anari, Liu, Oveis-Gharan and Vinzant and possible extensions to spectral gap"
section_number: 1.3
pages: 6-8
source_pdf: 1-s2.0-S002212362200012X-main.pdf
source_sha256: 6fc7d28c8d40bf42
toc_source: outline
doc_brief: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube — V Article history: Received 17 December 2020 Accepted 13 January 2022 Available online"
---
extensions to spectral gap
A somewhat related notion of log-concavity of measures on the discrete hypercube 
was given in a series of works by Anari, Liu, Oveis-Gharan and Vinzant in [2,3,1]. Given 
{−1, 1}-Bernoulli random variables X1, . . . , Xn distributed according to a law ν, which 
can be identiﬁed with a random subset A ⊂[n] by Xi = 21i∈A −1, the work [2] considers 
the generating polynomial
pν(z1, ..., zn) = E

i∈A
zi.
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
7
They show that if p is both log-concave on the positive orthant and homogeneous (which 
is equivalent to the fact 
i Xi is supported on one point), then the law of X1, ...Xn
admits, among other things, strong concentration properties in the form of a spectral 
gap (with respect to the Glauber dynamics).
It is not hard to check that the log-concavity of the polynomial pν is equivalent to 
the condition
∇2L[ν](x) ⪯2 (diag (∇L[ν](x)) + In) ,
∀x ∈Rn.
(7)
Since ∇L[ν](x) ∈[−1, 1]n, the above condition is strictly stronger than our semi-log-
concavity condition (2) with β = 4.
Note that our notion of log-concavity is invariant under reﬂections about the coordi-
nate axes, whereas in the latter notion, the direction (1, ..., 1) has a special role. In cases 
of interest, such as homogeneous distributions where |A| ≪n, condition (7) is actually 
closer to strict log-concavity. Since the multi-linear polynomial pν is harmonic, its log-
concavity implies that the Hessian matrix can have only one non-negative eigenvalue. In 
this sense, condition (7) is much more rigid than our condition.
A perhaps more closely related work is [1], where it is shown that another related 
condition implies spectral gap. The main result in this work is roughly the following: 
Suppose that the covariance matrix of any restriction of the measure ν to a sub-cube 
(hence, a set of the form {x; xi = yi, ∀i ∈A} for some A ⊂[n] and y ∈{−1, 1}n) has 
operator norm O(1). Then, the measure admits a spectral gap of n−O(1). Such a bound, 
however, does not allow one to get any improvement for the concentration of 1-Lipschitz 
functions with respect to the trivial bound Varν[ϕ] ≤n2. In this respect, our theorem is 
complementary to [1].
On the other hand, it is not hard to check that our condition (2) as is, cannot be 
enough to imply a spectral gap for the Glauber dynamics. Indeed, if one considers the 
uniform measure on the points with even parity, then this measure is semi log-concave, 
but its spectral gap is zero (the Glauber dynamics is simply stuck at one point). Thus, 
there is no hope for spectral gap unless one adds some “local” connectivity condition. We 
suspect that this example is essentially the only obstacle in the sense that and β-semi 
log-concave measure has a spectral gap after applying a small noise, namely applying 
the heat semigroup for time O(1/n).
While our proof is based mainly on analytic methods, the proof in [2] (and in [1] which 
is based on the same techniques) has a more algebraic ﬂavor, and is based the theory 
of high-dimensional expanders. Let us mention that in the work [8] (which appeared in 
parallel with this work), it is shown that techniques which are related to the ones in our 
work can be used to obtain a spectral gap when the measure ν is of the form eV dμ with 
V quadratic.
In relation to Corollary 9, a result of a similar spirit appears in [1]. A corollary of the 
main theorem there shows that if ν is d-homogeneous and all measures obtainable from ν
8
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
by conditioning are pairwise-negatively correlated, then it has a spectral gap polynomial 
in n. It seems however, that the assumption of homogeneity is crucial in this case.
Finally, Theorem 6 seems rather closely related to [3, Theorem 5.2], and the former 
can be thought of as a soft and modiﬁed version of the latter: Indeed, condition (5), 
compared to (7) is invariant under coordinate reﬂections and softer in the sense that 
β can be larger than 1, but otherwise rather similar. The proof of the latter is simpler 
and basically reduces to an application of Jensen’s inequality, whereas our proof (a small 
variation thereof also implies the latter bound) is slightly more complicated and uses 
stochastic calculus; we do not know if it can be attained by more elementary techniques.
Acknowledgments
We’d like to thank Bo’az Klartag for a fruitful discussion, as well as Nima Anari, Jan 
Vondrak and Pranav Nuti for some enlightening comments on a preliminary version of 
this manuscript.
