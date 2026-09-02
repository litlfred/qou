---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-011-41-mixed-matrix-moments
section_title: "Mixed Matrix Moments"
section_number: 4.1
pages: 59-65
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
---
complex Ginibre ensemble, and we will emphasize the relation to spin glass techniques.
51
This formula is already known and we will give references.
In later sections, we will describe the relationship between the mixed matrix mo-
ments and the expected overlap functions of Chalker and Mehlig. This leads to some
new problems.
4.1 Mixed Matrix Moments
Given any n×n matrix A, any positive integer k, and any nonnegative integers
p(1),q (1),...,p (k),q (k), we may deﬁne
Mn(p; q) = 1
n tr[Ap(1)
n (A∗
n)q(1)··· Ap(k)
n (A∗
n)q(k)], (4.2)
for p = (p(1),...,p (k)), q = (q(1),...,q (k)). Notice that M0 = 1. As an example,
consider
Mn((2, 2); (2, 2)) =
1
n
n∑
j1,...,j8=1
an(j1,j 2)an(j2,j 3)an(j4,j 3)an(j5,j 4)an(j5,j 6)an(j6,j 7)an(j8,j 7)an(j1,j 8).
(4.3)
If we consider the Ginibre ensemble and let an(j,k ) = (X(j,k ) +iY (j,k ))/
√
2n as
before, then we have
E[an(j,k )an(j′,k′)] = E[an(j,k )an(j′,k′)], = 0 and E[an(j,k )an(j′,k′)] = n−1δj,j′δk,k′.
(4.4)
Recall that Wick’s rule says that for mean 0 Gaussian random variables X1,...,X n,
E(X1X2...X n) =
∑∏
i,j
(XiXj)
52
where the sum is over all distinct ways of dividing 1,...,n into pairs. Using this, and
deﬁning mn(p, q) = E[Mn(p, q)], gives us:
mn(p, q) =
∑
(p′,q′,p′′,q′′)∈S(p,q)
E[Mn(p′, q′)Mn(p′′, q′′)], (4.5)
whereS(p, q) is the set of all admissible pairs, which we describe now. Let R =
p(1) +··· +p(k) +q(1) +··· +q(k), and deﬁne σ = (σ(1),...,σ (R))∈{ +1,−1}R
asσ = ((+1)p(1), (−1)q(1),..., (+1)p(k), (−1)q(k)) viewed as spins on vertices arranged
on a circle. We will sometimes denote this as σp,q. Let Σ( p, q) denote pairs (σ′,σ′′)
as follows. We match up the ﬁrst +1 and any −1. Where these two are removed, we
pinch the circle into two smaller circles. Then the remaining spins on the two smaller
circles comprise σ′ and σ′′. E.g., for a particular example
σ = (+1, +1,−1,−1, +1, +1,−1,−1)↦→ (σ′,σ′′) = ((+1), (−1, +1, +1,−1,−1)).
(4.6)
The set Σ(p, q) is the set of all possible pairs (σ′,σ′′) obtainable in this way. We then
deﬁneS(p, q) to be the set of all pairs ( p′, q′) and ( p′′, q′′) by mapping backwards
Σ(p, q) from σ′ and σ′′, this way.
Using this, we wish to give the main ideas of the proof of the following theorem.
Theorem 4.1.1. For any k and any p, q, we have
lim
n→∞
mn(p, q) = m(p, q),
wherem(p, q) is as follows. Let CR denote the number of all non-crossing matchings
ofR vertices on a circle (Catalan’s number). Let m(p, q) denote the cardinality of all
such matchings satisfying the following constraint: assigning spins to the R vertices
by σp,q, each edge has two endpoints with one +1 spin and one −1 spin.
As an example, m((2, 2); (2, 2)) = 3 where the matchings are indicated diagram-
53
matically as
Theorem 4.1.1 is a well-known result. We refer to [Kemp et al., 2011] for a discussion.
We will motivate a proof of this result, without including all details, here. Our reason
is that we actually want to use this result to motivate the discussion of random
matrices and spin glasses further, which we indicated earlier.
4.1.1 Argument for the Proof of the Mixed Matrix Moments
The ﬁrst step in the argument for the proof of Theorem 4.1.1 is to use concentration
of measure (COM) to replace (4.5) with a nonlinear recurrence relation. Here what
we mean is non-linearity in the probability measure for the random entries of the
matrix. Since the expectation is linear, what we really mean is to obtain a product
of two expectations. If Mn(p′, q′) and Mn(p′′, q′′) were independent, then we could
replace the expectation by a product, but they are not exactly independent. Instead,
they satisfy COM, which means that they are approximately non-random. And, of
course, non-random variables are exactly independent of every other random variable
(as well as themselves).
The easiest version of COM is just L2-concentration. For example, the following
lemma is very easy to prove:
Lemma 4.1.2. Supposef : Rn→ R is a function such that
‖∇f‖2
∞ = sup x∈Rn
∑n
k=1
(
∂f
∂xk
(x)
)2
is ﬁnite. Then if U1,...,U n,V 1,...,V n are IID
54
N (0, 1) random variables then
E
[
(f(U)−f(V))2]
≤ 2‖∇f‖2
∞. (4.7)
This can be proved using the basic, but important method of “quadratic interpo-
lation,” which is sometimes called the “smart path method” by some mathematicians
working on spin glasses.
Proof. Let Z = (Z1,...,Z n) be an IID N (0, 1) vector, independent of U and V.
Then deﬁne ~U(θ) = sin( θ) U + cos(θ) Z and ~V(θ) = sin( θ) V + cos(θ) Z. Then
d
dθ
~U(θ) = ~U(θ + π
2 ), and E[~U(θ)~U(θ + π
2 )] = 0. This means that ~U(θ) is statistically
independent of its θ-derivative. Similar results hold for ~V(θ). On the other hand
E[~V(θ)~U(θ + π
2 )] =− sin(θ) cos(θ).
Next, using the fundamental theorem of calculus,
E
[
(f(U)−f(V))2]
=
∫ π/2
0
d
dθ E
[(
f(~U(θ))−f(~V(θ))
)2]
dθ, (4.8)
and an easy calculation using Gaussian integration by parts (and the covariance
formulas mentioned above) shows that
d
dθ E
[(
f(~U(θ))−f(~V(θ))
)2]
= 2 sin(2θ)E
[
∇f(~U(θ))·∇f(~V(θ))
]
. (4.9)
Then (4.7) follows by using the Cauchy-Schwarz inequality.
This is only the simplest Gaussian COM result. Notice that the method of proof is
similar to the method used to proved Talagrand’s Gaussian concentration of measure
inequality for Lipschitz functions as stated in chapter 2 Theorem 2.1.1
This lemma is a tool which can be applied to show that the various mixed matrix
momentsMn(p, q) do satisfy COM. We present this lemma here, because it is easier
to obtain concentration of measure for the matrix moments using this lemma than
55
with Theorem 2.1.1. It should be noted, that 2.1.1 will also work in this case and
will give a sharper concentration bound. Either way, it is an interesting calculation,
and much of the combinatorics, especially involving matchings related to Catalan’s
number, are ﬁrst visible in the grad-squared calculation.
Since the goal of this section is to give a general outline of the proof of the formula
for the mixed matrix moments and relate it to spin glass techniques, we will just state
that the desired concentration of measure result is true.
Then we are able to boost (4.5) to
lim
n→∞
mn(p, q)−
∑
(p′,q′,p′′,q′′)∈S(p,q)
mn(p′, q′)mn(p′′, q′′) = 0 . (4.10)
Another easy fact is that, due to symmetry, mn(p, q) = 0 unless p(1) +··· +p(k) =
q(1) +··· +q(k). And, of course, m0 = 1.
Using this, and the method of induction, one can then prove Theorem 4.1.1.
4.1.2 Commentary on Proof Technique
The quadratic interpolation technique is important in spin glasses. The ﬁrst major
use was by Guerra and Toninelli [Guerra and Toninelli, 2002] and Guerra [Guerra,
2003]. It is called the “smart path method” by Talagrand [Talagrand, 2011]. This is
the method which we used to prove Talagrand’s Gaussian concentration of measure
inequality in chapter 2.
Using Wick’s rule to obtain a recurrence relation is important in many subjects.
It is a standard approach to determining moments of random matrices. See, for
instance, [Anderson et al., 2010], chapter 1. In the context of Gaussian spin glasses,
this technique combined with stochastic stability leads to the Aizenman-Contucci
identities [Aizenman and Contucci, 1998]. When combined with concentration of
measure it leads to the Ghirlanda-Guerra identities [Ghirlanda and Guerra, 1998].
56
See, for instance, the review [Contucci and Giardina, 2007].
For random matrices, the problem of recombining the moments into useful infor-
mation about the limiting empirical spectral measure is also important. For Hermi-
tian random matrices, this is related to the classical moment method. The standard
approach is to put the moments together into the Stieltjes transform, and then to
proceed from there [Pastur, 1973]. Again, a good general reference is [Anderson et al.,
2010], chapter 1.
For spin glasses, the problem of integrating the Ghirlanda-Guerra identities into
a useful result for mean-ﬁeld models was solved only relatively recently. Panchenko
showed that the “extended Ghirlanda-Guerra identities” imply Parisi’s ultrametric
ansatz [Panchenko, 2011]. This is an important work. One element of his proof is
putting various terms together into a a new exponential type generating function.
This might be somewhat analogous to the Stieltjes transform step. But after that,
the proofs are very diﬀerent.
For non-Hermitian random matrices, getting useful information from the moments
is the topic we focus on next.
