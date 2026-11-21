---
doc_id: s0894-0347-00-00337-4
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4"
section_id: sec-005-15-poissonization-and-depoissonization
section_title: "Poissonization and depoissonization"
section_number: 1.5
pages: 7-8
source_pdf: S0894-0347-00-00337-4.pdf
source_sha256: 1c6848281fc2804c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4 — 22 sections: Front matter; Plancherel measures; Introduction"
---
Theorem 1 using the so-called depoissonization techniques.
We recall that the
fundamental idea of depoissonization is the following.
488
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
Given a sequence b1, b2, b3, . . . its poissonization is, by deﬁnition, the function
B(θ) = e−θ
∞
X
k=1
θk
k! bk .
(1.17)
Provided the bk’s grow not too rapidly this is an entire function of θ. In com-
binatorics, it is usually called the exponential generating function of the sequence
{bk}. Various methods of extracting asymptotics of sequences from their generating
functions are classically known and widely used (see for example [39] where such
methods are used to obtain the limit shape of a typical partition under various
measures on the set of partitions).
A probabilistic way to look at the generating function (1.17) is the following.
If θ ≥0, then B(θ) is the expectation of bη where η ∈{0, 1, 2, . . .} is a Poisson
random variable with parameter θ. Because η has mean θ and standard deviation
√
θ, one expects that
B(n) ≈bn ,
n →∞,
(1.18)
provided the variations of bk for |k −n| ≤const √n are small. One possible regu-
larity condition on bn which implies (1.18) is monotonicity. In a very general and
very convenient form, a depoissonization lemma for nonincreasing nonnegative bn
was established by K. Johansson in [16]. We use this lemma in Section 4 to prove
Theorem 4.
Another approach to depoissonization is to use a contour integral
bn = n!
2πi
Z
C
B(z) ez
zn
dz
z ,
(1.19)
where C is any contour around z = 0. Suppose, for a moment, that bn is constant,
b = bn = B(z). The function ez/zn = ez−n ln z has a unique critical point z = n.
If we choose |z| = n as the contour C, then only neighborhoods of size |z −n| ≤
const √n contribute to the asymptotics of (1.19).
Therefore, for general {bn},
we still expect that provided the overall growth of B(z) is under control and the
variations of B(z) for |z −n| ≤const √n are small, the asymptotically signiﬁcant
contribution to (1.19) will come from z = n. That is, we still expect (1.18) to
be valid. See, for example, [15] for a comprehensive discussion and survey of this
approach.
We use this approach to prove Theorem 3 in Section 3. The growth conditions
on B(z) which are suitable in our situation are spelled out in Lemma 3.1.
In our case, the functions B(θ) are combinations of the Bessel functions. Their
asymptotic behavior as θ ≈n →∞can be obtained directly from the classical
results on asymptotics of Bessel functions which are discussed, for example, in the
fundamental Watson’s treatise [43]. These asymptotic formulas for Bessel functions
are derived using the integral representations of Bessel functions and the steepest
descent method. The diﬀerent behavior of the asymptotics in the bulk (−2, 2) of
the spectrum, near the edges ±2 of the spectrum, and outside of [−2, 2] is produced
by the diﬀerent location of the saddle point in these three cases.
