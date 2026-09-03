---
doc_id: arxiv-2201.05665v1
doc_title: "HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY"
section_id: sec-005-42-random-permutations
section_title: "Random permutations"
section_number: 4.2
pages: 9-10
source_pdf: 2201.05665v1.pdf
source_sha256: bad7bde03d199a73
doc_brief: "HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY — This is a survey of Harold Widom’s work in random matrices."
---
bers 1, 2, ..., N. If 1 ≤i1 < i2 < ... < ik ≤N and π(i1) < π(i2) < ... < π(ik), we say
that π(i1), π(i2), ..., π(ik) is an increasing subsequence in π of length k. Denote by lN(π) the
maximal length of all of the increasing subsequences in π. Suppose that the permutations are
random and uniformly distributed. The principal interest is in the limiting statistics of the
random variable lN(π). This is a subject with a long history (see e.g. [AD]) which started in
the early 60’s with “Ulam’s problem”: prove that the following limit exists
lim
N→∞
E(lN)
√
N
= c,
(4.10)
where E(·) means mathematical expectation, and compute c. The proof of this result was
obtained independently in [VeKe] and [LoSh]: It turns out that c = 2. Further progress
was obtained only after 22 years in [BDJ], where it was shown that the random variable
χN := lN−2
√
N
N1/6
converges in distribution to the second Tracy-Widom distribution F2(x), i.e.
lim
N→∞Prob
 
lN −2
√
N
N1/6
≤t
!
= F2(t),
∀t ∈R.
(4.11)
In addition, the authors of [BDJ] proved convergence of moments:
lim
N→∞E

χm
N

= E

χm
,
∀m = 1, 2, ... .
(4.12)
10
IVAN Z. CORWIN, PERCY A. DEIFT, AND ALEXANDER R. ITS
It is worth noting that Harold Widom suggested in [14] an alternative proof of the conver-
gence of the moments (4.12) based on the Borodin-Okounkov Fredholm determinant formula
for Toeplitz determinants. The latter was ﬁrst derived in [BoOk], and has been proven ex-
tremely useful in the theory and application of Toeplitz determinants. There are now several
diﬀerent proofs of this formula and the ﬁrst one (after the original proof of Borodin and
Okounkov) was again suggested by Harold Widom jointly with Estelle Basor in [13]. It is
remarkable that this proof in turn is again based on one of the old papers of Widom [2].
We also refer to the article by Basor, B¨ottcher and Ehrhardt [BBE] in this volume for more
details on the Borodin-Okounkov formula and its history and connection with Widom’s work
on Toeplitz determinants. It is important to note that the Borodin-Okounkov formula was in
fact discovered earlier by Geronimo and Case in [GeCa], but its signiﬁcance was overlooked
at the time.
Random permutations appear in an enormous array of problems. Some of the most fun-
damental connections are with measures on Young diagrams, random growth processes, in-
teracting particle systems, last passage percolation models and with various tiling problems.
Formula (4.11) and its generalizations for more complex types of permutations, which involve
Fβ with β = 1 and 4 as well (see [BaRa]), paved the way that brought the Tracy-Widom
distribution functions into many areas of physics, mathematics and engineering. We refer to
the surveys [Dei3, Cor4] for a discussion of a wide variety of examples and a historical review.
We close this section by mentioning one remarkable generalization of the Ulam problem.
Consider N-independent standard one-dimensional Brownian motions B1(t), B2(t), . . . , BN(t),
for t ≥0. For 0 ≤a < b let Bi(a, b) = Bi(b)−Bi(a) denote the increment of the ith Brownian
motion on the time interval [a, b]. Deﬁne the last passage time MN
t
through the environment
of Brownian motions by
MN
t
:=
max
0≤s1≤···≤sN−1≤t (B1(0, s1) + B2(s1, s2) + · · · + BN(sN−1, t)) .
In joint work [4] with Janko Gravner and Craig Tracy, Harold Widom proved that MN
t /
√
t
has the same distribution as the largest eigenvalue of an N ×N GUE matrix. In fact, in their
work, they also study some discrete generalizations of the Ulam problem which are related
to growth models and last passage problems such as above.
