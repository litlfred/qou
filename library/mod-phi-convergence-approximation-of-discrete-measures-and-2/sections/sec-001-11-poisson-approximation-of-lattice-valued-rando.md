---
doc_id: mod-phi-convergence-approximation-of-discrete-measures-and-2
doc_title: "ANNALES DE L’INSTITUT FOURIER"
section_id: sec-001-11-poisson-approximation-of-lattice-valued-rando
section_title: "Poisson approximation of lattice-valued random variables"
section_number: 1.1
pages: 3-5
source_pdf: mod-phi-convergence-approximation-of-discrete-measures-and-20yc5c6q3n.pdf
source_sha256: c563cc999000e75d
toc_source: outline
doc_brief: "ANNALES DE L’INSTITUT FOURIER — 27 sections: Front matter; Introduction; Poisson approximation of lattice-v"
---
Consider a sequence (Bi)i⩾1 of independent Bernoulli random variables,
with P[Bi = 1] = pi and P[Bi = 0] = 1 −pi. We set
Xn =
n
X
i=1
Bi.
The Poisson approximation ensures that if the pi’s are small but their sum
λn = Pn
i=1 pi is large, then the distribution of Xn is close to the distribution
of a Poisson random variable with parameter λn = Pn
i=1 pi. To make this
result quantitative, one can introduce the total variation distance between
two probability measures µ and ν on Z. Let us set
dTV(µ, ν) =
X
k∈Z
|µ({k}) −ν({k})| ;
this deﬁnition diﬀers by a multiplicative factor 2 from the usual conven-
tions, but otherwise we would have to keep track of a factor 1
2 in all our
estimates. A ﬁrst quantitative result regarding the Poisson approximation is
due to Prohorov and Kerstan (see [40, 49]): if pi = λ
n for all i ∈[[1, n]], then
dTV(Xn, P(λ)) =
X
k∈N

P[Xn = k] −e−λ λk
k!

 ⩽2λ
n .
More generally, with parameters pi that can be distinct and with λn =
Pn
i=1 pi, Le Cam showed that
X
k∈N

P[Xn = k] −e−λn (λn)k
k!

 ⩽2
n
X
i=1
(pi)2.
This is an immediate consequence of the inequality on total variation dis-
tances
dTV(µ1 ∗µ2, ν1 ∗ν2) ⩽dTV(µ1, ν1) + dTV(µ2, ν2)
which holds for any probability measures µ1, µ2, ν1, ν2 on Z (cf. [14]). By
using arguments derived from Stein’s method for the Gaussian approxi-
mation, Chen and later Barbour and Eagleson improved versions of this
inequality, e.g.,
X
k∈N

P[Xn = k] −e−λn (λn)k
k!

 ⩽2 (1 −e−Pn
i=1 pi)
Pn
i=1(pi)2
Pn
i=1 pi
,
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1117
see [5, 19, 54]. We also refer to [20] for an extension to possibly depen-
dent Bernoulli random variables, to [2] for results regarding the Poisson
processes, and to [6] for a survey of the theory of Poisson approximations.
More generally, consider random variables Xn⩾1 whose distributions are
supported by the lattice Zd ⊂Rd, and which stem from a common proba-
bilistic model. In many cases, the scaling properties of the model imply that
when n is large, Xn can be approximated by a discrete inﬁnitely divisible
law νn, the Lévy exponents of these reference laws being all proportional:
c
νn(ξ) :=
X
k∈Zd
νn(k) ei⟨ξ | k⟩= eλnφ(ξ),
λn →+∞.
To go beyond the classical Poisson approximation, one can try in this set-
ting to write bounds on the total variation distance dTV(Xn, νn), or on an-
other metric which measures the convergence in law (the local distance, the
Kolmogorov distance, the Wasserstein metric, etc.). A convenient frame-
work for this program is the notion of mod-φ convergence developed by Bar-
bour, Kowalski and Nikeghbali in [7], see also the papers [23, 26, 27, 35, 41].
The main idea is that, given a sequence of random variables (Xn)n∈N with
values in a lattice Zd, and a reference inﬁnitely divisible law φ on the same
lattice, if one has suﬃciently good estimates on the Fourier transform of
the law µn of Xn and on the ratio
bµn(ξ)
bνn(ξ) = E[eiξXn] e−λnφ(ξ),
then one can deduce from these estimates the asymptotics of the distribu-
tion of Xn: central limit Theorems [7, 35], local limit Theorems [23, 41],
large deviations [26], speed of convergence [27], etc. In this paper, we shall
use the framework of mod-φ convergence to compute the precise asymp-
totics of the distance between the law of Xn and the reference inﬁnitely
divisible law, for various distances.
When approximating lattice-distributed random variables, another ob-
jective that one can pursue consists in ﬁnding better approximations than
the one given by an inﬁnitely divisible law. A general principle is that,
if one allows signed measures instead of positive probability measures,
then simple deformations of the inﬁnitely divisible reference law can be
used to get smaller distances, i.e. faster convergences. In the setting of
the classical Poisson approximation of sums of independent integer-valued
random variables, this idea was used in [4, Theorem 5.1]. We also refer
to [8, 13, 16, 17, 18, 36, 42, 48] for other applications of the signed compound
Poisson approximation (SCP). For mod-Poisson convergent random vari-
ables (Xn)n∈N, an unconditional upper bound on the distance between the
TOME 70 (2020), FASCICULE 3
1118
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
law of Xn and a signed measure νn deﬁned by means of Poisson–Charlier
polynomials was proven in [7, Theorem 3.1]. A more general upper bound
with an arbitrary reference law also appears in [7, Theorem 5.1]. In our
paper, we shall set up a general approximation scheme for sequences of
lattice-valued random variables, which will allow us:
• to obtain signed measure approximations whose distances to the
laws of the variables Xn are arbitrary negative powers of the pa-
rameter λn;
• to compute the asymptotics of these distances (instead of an un-
conditional upper bound).
Thus, this paper can be regarded as a complement to [7], with an alternative
approach and an alternative goal (namely, obtaining the exact asymptotics
of the distances). In [26, Proposition 4.1.1], we also used signed measures in
order to approximate mod-φ convergent random variables, but with respect
to a continuous inﬁnitely divisible distribution φ, and using a ﬁrst-order
deformation of the Gaussian distribution.
In the remainder of this introductory section, we recall the main deﬁni-
tions from the theory of mod-φ convergence, and we explain the general
approximation scheme. In subsequent sections, this approximation scheme
will yield the main hypotheses of our Theorems (Sections 2 and 3), and we
shall apply it to various one-dimensional and multi-dimensional examples
coming from probability, analytic number theory, combinatorics, etc. (Sec-
tions 4 and 5). We also present in this introduction the main tool that we
shall use in this paper, namely, harmonic analysis in the Wiener algebra.
