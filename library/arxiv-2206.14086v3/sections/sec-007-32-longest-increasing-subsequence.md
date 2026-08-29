---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems Jinho Baik∗"
section_id: sec-007-32-longest-increasing-subsequence
section_title: "Longest increasing subsequence"
section_number: 3.2
pages: 5-6
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
doc_brief: "KPZ limit theorems Jinho Baik∗ — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
The Poisson DLPP is particularly interesting due to its connection to longest increasing subsequences of
random permutations. Note that ﬁnitely many points in a rectangle with distinct x and y coordinates can
be associated with a permutation by considering the relative orderings of the coordinates. For example,
the points in Figure 7 are associated with the permutation π = 475168293.
For this permutation, the
subsequence 45689 is an increasing subsequence. Furthermore, it is the longest increasing subsequence, and
its length, 5, is equal to the last passage time L(t, s).
5
Let ℓN denote the length of longest increasing subsequences of a uniformly random permutation of size N.
Then, L(t, s) has the same distribution as ℓN, where N is a Poisson random variable of mean ts. Using this
connection, Theorem 3.1 implies, after a de-Poissonization argument, that ℓN−2
√
N
N1/6
converges in distribution
to the Tracy–Widom distribution.
The problem of determining the large N behavior of ℓN has a long history. The existence of the almost
sure limit of ℓN/
√
N was proved by Hammersley in [49] using Kingman’s ergodic subadditivity theorem.
The fact that the limit is 2, known as Ulam’s problem, was proved independently by two famous papers
of Verˇsik –Kerov [90] and Logan–Shepp [65] in 1977. However, the limiting distribution and the variance
(which is of order N 2/3) remained an open problem until the work [6]. Interested readers are encouraged to
consult [3,7,76,83].
3.3
Exponential DLPP
Soon after Theorem 3.1 was proved, Johansson showed that the exponential DLPP model also satisﬁes a
similar limit theorem [53]. We state the result in terms of the height function of the TASEP.
Theorem 3.2 ( [53]). Assume the step initial condition for the TASEP. Then, for every (τ, γ, h) ∈R+ ×
R × R,
lim
T →∞P
h(γT 2/3, 2τT) −τT
−T 1/3
≤h

= FTW
 h
τ 1/3 +
γ2
4τ 4/3

.
Note from either side of the equation that the limit remains unchanged if we rescale
(h, γ, τ) 7→(αh, α2γ, α3τ)
(3.1)
for any α > 0.
3.4
