---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
toc_source: outline
---
Introduction
Markov chain Monte Carlo (MCMC) is widely used to estimate intractable integrals that represent expec-
tations with respect to complicated probability distributions. Let π : S →[0, ∞) be a probability density
function (pdf) with respect to a σ-ﬁnite measure µ, where (S, U, µ) is some measure space. Suppose we
Key words and phrases. Data augmentation algorithm, Eigenvalues, Hilbert-Schmidt operator, Markov chain, Monte Carlo
1
arXiv:1704.00850v3  [math.ST]  4 Apr 2019
want to approximate the integral
J :=
Z
S
f(u)π(u)µ(du)
for some function f : S →R. Then J can be estimated by ˆJm := m−1 Pm−1
k=0 f(Φk), where {Φk}m−1
k=0 are
the ﬁrst m elements of a well-behaved Markov chain with stationary density π(·). Unlike classical Monte
Carlo estimators, ˆJm is not based on iid random elements. Indeed, the elements of the chain are typically
neither identically distributed nor independent. Given varπf, the variance of f(·) under the stationary dis-
tribution, the accuracy of ˆJm is primarily determined by two factors: (i) the convergence rate of the Markov
chain, and (ii) the correlation between the f(Φk)s when the chain is stationary. These two factors are related,
and can be analyzed jointly under an operator theoretic framework.
The starting point of the operator theoretic approach is the Hilbert space of functions that are square
integrable with respect to the target pdf, π(·). The Markov transition function that gives rise to Φ = {Φk}∞
k=0
deﬁnes a linear (Markov) operator on this Hilbert space. (Formal deﬁnitions are given in Section 2.) If Φ is
reversible, then it is geometrically ergodic if and only if the corresponding Markov operator admits a positive
spectral gap (Roberts and Rosenthal, 1997; Kontoyiannis and Meyn, 2012). The gap, which is a real number
in (0, 1], plays a fundamental role in determining the mixing properties of the Markov chain, with larger
values corresponding to better performance. For instance, suppose Φ0 has pdf π0(·) such that dπ0/dπ is in
the Hilbert space, and let d(Φk; π) denote the total variation distance between the distribution of Φk and the
chain’s stationary distribution. Then, if δ denotes the spectral gap, we have
d(Φk; π) ≤C(1 −δ)k
for all positive integers k, where C depends on π0 but not on k (Roberts and Rosenthal, 1997). Furthermore,
(1 −δ)k gives the maximal absolute correlation between Φj and Φj+k as j →∞. It follows (see e.g. Mira
and Geyer, 1999) that the asymptotic variance of √m( ˆJm −J) as m →∞is bounded above by
2 −δ
δ
varπf .
Unfortunately, it is impossible to calculate the spectral gaps of the Markov operators associated with practi-
cally relevant MCMC algorithms, and even accurately approximating these quantities has proven extremely
difﬁcult. In this paper, we develop a method of estimating the spectral gaps of Markov operators correspond-
ing to a certain class of data augmentation (DA) algorithms (Tanner and Wong, 1987), and then show that
the method can be extended to handle a much larger class of reversible MCMC algorithms.
DA Markov operators are necessarily non-negative. Moreover, any non-negative Markov operator that is
compact has a pure eigenvalue spectrum that is contained in the set [0, 1], and 1 −δ is precisely the second
2
