---
doc_id: arxiv-math-9905032v2
doc_title: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS"
section_id: sec-010-15-poissonization-and-depoissonization-we-obtain
section_title: "Poissonization and depoissonization. We obtain Theorems 3"
section_number: 1.5
pages: 10-11
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
doc_brief: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
and 4 from Theorem 1 using the so-called depoissonization te chniques.
We recall that the fundamental idea of depoissonization is t he following.
Given a sequence b1, b2, b3, . . . its poissonization is, by deﬁnition, the
function
B(θ) = e−θ
∞∑
k=1
θk
k! bk .(1.17)
Provided the bk’s grow not too rapidly this is an entire function of θ. In
combinatorics, it is usually called the exponential genera ting function
of the sequence {bk}. Various methods of extracting asymptotics of
sequences from their generating functions are classically known and
widely used, see for example [35] where such methods are used to obtain
the limit shape of a typical partition under various measure s on the set
of partitions.
A probabilistic way to look at the generating function (1.17 ) is the
following. If θ ≥ 0 then B(θ) is the expectation of bη where η ∈
{0, 1, 2, . . .} is a Poisson random variable with parameter θ. Because
η has mean θ and standard deviation
√
θ, one expects that
B(n) ≈ bn , n → ∞ ,(1.18)
provided the variations of bk for |k − n| ≤ const √
n are small. One
possible regularity condition on bn which implies (1.18) is monotonicity.
In a very general and very convenient form, a depoissonizati on lemma
for nonincreasing nonnegative bn was established by K. Johansson in
[14]. We use this lemma in Section 4 to prove Theorem 4.
Another approach to depoissonization is to use a contour int egral
bn = n!
2πi
∫
C
B(z) ez
zn
dz
z ,(1.19)
where C is any contour around z = 0. Suppose, for a moment, that
bn is constant b = bn = B(z). The function ez/zn = ez−n ln z has a
unique critical point z = n. If we choose |z| = n as the contour C,
then only neighborhoods of size |z − n| ≤ const √
n contribute to the
asymptotics of (1.19). Therefore, for general {bn}, we still expect that
provided the overall growth of B(z) is under control and the variations
ASYMPTOTICS OF PLANCHEREL MEASURES 11
of B(z) for |z − n| ≤ const √n are small, the asymptotically signiﬁcant
contribution to (1.19) will come from z = n. That is, we still expect
(1.18) to be valid. See, for example, [13] for a comprehensiv e discussion
and survey of this approach.
We use this approach to prove Theorem 3 in Section 3. The growt h
conditions on B(z) which are suitable in our situation are spelled out
in Lemma 3.1.
In our case, the functions B(θ) are combinations of the Bessel func-
tions. Their asymptotic behavior as θ ≈ n → ∞ can be obtained
directly from the classical results on asymptotics of Besse l functions
which are discussed, for example, in the fundamental Watson ’s treatise
[39]. These asymptotic formulas for Bessel functions are de rived using
the integral representations of Bessel functions and the st eepest descent
method. The diﬀerent behavior of the asymptotics in the bulk (−2, 2)
of the spectrum, near the edges ±2 of the spectrum, and outside of
[−2, 2] is produced by the diﬀerent location of the saddle point in these
three cases.
