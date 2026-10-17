---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-001-2-markov-operators
section_title: "Markov operators"
section_number: 2
pages: 3-5
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
toc_source: outline
---
are trace-class, i.e. compact with summable eigenvalues. While compact operators were once thought to be
rare in MCMC problems with uncountable state spaces (Chan and Geyer, 1994), a string of recent results
suggests that trace-class DA Markov operators are not at all rare (see e.g. Qin and Hobert, 2018; Chakraborty
and Khare, 2017; Choi and Rom´an, 2017; Pal et al., 2017). Furthermore, by exploiting a simple trick, we
are able to broaden the applicability of our method well beyond DA algorithms. Indeed, if a reversible
Monte Carlo Markov chain has a Markov transition density (Mtd), and the corresponding Markov operator
is Hilbert-Schmidt, then our method can be utilized to estimate its spectral gap. This is because the square
of such a Markov operator can be represented as a trace-class DA Markov operator. A detailed explanation
is provided in Section 4.
Of course, there is a large literature devoted to developing theoretical bounds on the second largest
eigenvalue of a Markov operator (see e.g. Lawler and Sokal, 1988; Sinclair and Jerrum, 1989; Diaconis and
Stroock, 1991). However, these results are typically not useful in situations where the state space, S, is
uncountable or multi-dimensional, which is our main focus. There also exist a number of computational
methods for approximating the eigenvalues of a Hilbert-Schmidt operator (see e.g. Garren and Smith, 2000;
Koltchinskii and Gin´e, 2000; Ahues et al., 2001; Chakraborty and Khare, 2019+). Some such methods
require sampling directly from π(·), which is impossible in an MCMC context. The others require the user
to simulate the Markov chain of interest until it is nearly stationary. Unfortunately, we cannot know if a
chain has converged unless we have some information on its convergence rate, which is essentially what
these methods are trying to acquire in the ﬁrst place. The classical Monte Carlo estimator that we introduce
is calculated by simulating many copies of the Markov chain, each of a short length. These short chains need
not be close to stationarity in order for the estimator to be valid. Although powerful, this method is quite
expensive from a computational standpoint. Indeed, it works well only when the underlying dataset of the
Bayesian model is small. On the other hand, it is important as a “proof of concept” that it is actually possible
to get a handle on the spectral gaps of Markov operators corresponding to MCMC algorithms on continuous
state spaces, which, until now, have proven to be extremely elusive quantities.
The rest of the paper is organized as follows. The notion of Markov operator is formalized in Section 2.
In Section 3, it is shown that the second largest eigenvalue of a non-negative trace-class operator can be
bounded above and below by functions of the power sums of the operator’s eigenvalues. In Section 4, DA
Markov operators are formally deﬁned, and the sum of the kth (k ∈N) power of the eigenvalues of a
trace-class DA Markov operator is related to a functional of its Mtd. This functional is usually a multi-
dimensional integral, and a classical Monte Carlo estimator of it is developed in Section 5. The efﬁciency
3
of the Monte Carlo estimator is studied in Section 6. Finally, in Section 7 we apply our method to a few
well-known MCMC algorithms. Our examples include Albert and Chib’s (1993) DA algorithm for Bayesian
probit regression, and a DA algorithm for Bayesian linear regression with non-Gaussian errors (Liu, 1996).
Further application of the method can be found in Zhang et al. (2019).
2
Markov operators
Assume that the Markov chain Φ has a Markov transition density, p(u, ·), u ∈S, such that, for any measur-
able A ⊂S and u ∈S,
P(Φk ∈A|Φ0 = u) =
Z
A
p(k)(u, u′) µ(du′) ,
where
p(k)(u, ·) :=



p(u, ·)
k = 1
R
S p(k−1)(u, u′)p(u′, ·) µ(du′)
k > 1
is the k-step Mtd corresponding to p(u, ·). We will assume throughout that Φ is Harris ergodic, i.e. irre-
ducible, aperiodic and Harris recurrent. Deﬁne a Hilbert space consisting of complex valued functions on S
that are square integrable with respect to π(·), namely
L2(π) :=
n
f : S →C

Z
S
|f(u)|2π(u) µ(du) < ∞
o
.
For f, g ∈L2(π), their inner product is given by
⟨f, g⟩π =
Z
S
f(u)g(u)π(u) µ(du) .
We assume that U is countably generated, which implies that L2(π) is separable and admits a countable
orthonormal basis (see e.g. Billingsley, 1995, Theorem 19.2). The transition density p(u, ·), u ∈S deﬁnes
the following linear operator P. For any f ∈L2(π),
Pf(u) =
Z
S
p(u, u′)f(u′) µ(du′) .
The spectrum of a linear operator L is deﬁned to be
σ(L) =

λ ∈C

 (L −λI)−1 doesn’t exist or is unbounded
	
,
where I is the identity operator. It is well-known that σ(P) is a closed subset of the unit disk in C. Let
f0 ∈L2(π) be the normalized constant function, i.e. f0(u) ≡1, then Pf0 = f0. (This is just a fancy way of
saying that 1 is an eigenvalue with constant eigenfunction, which is true of all Markov operators deﬁned by
4
ergodic chains.) Denote by P0 the operator such that P0f = Pf −⟨f, f0⟩πf0 for all f ∈L2(π). Then the
spectral gap of P is deﬁned as
δ = 1 −sup
n
|λ|

 λ ∈σ(P0)
o
.
For the remainder of this section, we assume that P is non-negative (and thus self-adjoint) and compact.
This implies that σ(P) ⊂[0, 1], and that any non-vanishing element of σ(P) is necessarily an eigenvalue
of P. Furthermore, there are at most countably many eigenvalues, and they can accumulate only at the
origin. Let λ0, λ1, . . . , λκ be the decreasingly ordered strictly positive eigenvalues of P taking into account
multiplicity, where 0 ≤κ ≤∞. Then λ0 = 1 and λ1 is what we previously referred to as the “second largest
eigenvalue” of the Markov operator. If κ = 0, we set λ1 = 0 (which corresponds to the trivial case where
{Φk}∞
k=0 are iid). Since Φ is Harris ergodic, λ1 must be strictly less than 1. Also, the compactness of P
implies that of P0, and it’s easy to show that σ(P0) = σ(P)\{1}. Hence, Φ is geometrically ergodic and the
spectral gap is
δ = 1 −λ1 > 0 .
For further background on the spectrum of a linear operator, see e.g. Helmberg (2014) or Ahues et al. (2001).
