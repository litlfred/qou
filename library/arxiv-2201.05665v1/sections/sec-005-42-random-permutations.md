---
doc_id: arxiv-2201.05665v1
doc_title: "HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY"
section_id: sec-005-42-random-permutations
section_title: "Random permutations"
section_number: 4.2
pages: 9-10
source_pdf: 2201.05665v1.pdf
source_sha256: bad7bde03d199a73
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.965
doc_brief: "HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY — This is a survey of Harold Widom’s work in random matrices."
---
Let $\pi = (\pi(1), \pi(2), ..., \pi(N))$ be a permutation of the numbers $1, 2, ..., N$. If $1 \leq i_1 <  i_2 < ... < i_k \leq N$ and $\pi( i_1) < \pi( i_2) < ... < \pi(i_k)$, we say that $\pi( i_1), \pi( i_2), ...,\pi(i_k)$ is an *increasing subsequence* in $\pi$ of length $k$. Denote by $l_{N}(\pi)$ the maximal length of all of the increasing subsequences in $\pi$. Suppose that the permutations are random and uniformly distributed. The principal interest is in the limiting statistics of the random variable $l_{N}(\pi)$. This is a subject with a long history (see e.g. [@AD]) which started in the early 60's with "Ulam's problem": prove that the following limit exists $$\label{ulam}
\lim_{N\to \infty}\frac{{\Bbb E}(l_N)}{\sqrt{N}} = c,$$ where ${\Bbb E (\cdot)}$ means mathematical expectation, and compute $c$. The proof of this result was obtained independently in [@VK] and [@logan]: It turns out that $c=2$. Further progress was obtained only after 22 years in [@BDJ], where it was shown that the random variable $\chi_{N} := \frac{l_N - 2\sqrt{N}}{N^{1/6}}$ converges in distribution to the *second Tracy-Widom distribution $F_2(x)$*, i.e. $$\label{bdj}
\lim_{N \to \infty}\textrm{Prob}\left(\frac{l_N - 2\sqrt{N}}{N^{1/6}} \leq t\right) = F_2(t),
\quad \forall t \in {\Bbb R}.$$ In addition, the authors of [@BDJ] proved convergence of moments: $$\label{bdj2}
\lim_{N\to \infty}{\Bbb E}\Bigl(\chi_{N}^{m}\Bigr) = {\Bbb E}\Bigl(\chi^{m}\Bigr),
\quad \forall m = 1, 2, ...\,.$$

It is worth noting that Harold Widom suggested in [@wmoments] an alternative proof of the convergence of the moments ([\[bdj2\]](#bdj2){reference-type="ref" reference="bdj2"}) based on the Borodin-Okounkov Fredholm determinant formula for Toeplitz determinants. The latter was first derived in [@BoOk], and has been proven extremely useful in the theory and application of Toeplitz determinants. There are now several different proofs of this formula and the first one (after the original proof of Borodin and Okounkov) was again suggested by Harold Widom jointly with Estelle Basor in [@wb]. It is remarkable that this proof in turn is again based on one of the old papers of Widom [@wbo]. We also refer to the article by Basor, Böttcher and Ehrhardt [@BBE] in this volume for more details on the Borodin-Okounkov formula and its history and connection with Widom's work on Toeplitz determinants. It is important to note that the Borodin-Okounkov formula was in fact discovered earlier by Geronimo and Case in [@GC], but its significance was overlooked at the time.

Random permutations appear in an enormous array of problems. Some of the most fundamental connections are with measures on Young diagrams, random growth processes, interacting particle systems, last passage percolation models and with various tiling problems. Formula ([\[bdj\]](#bdj){reference-type="ref" reference="bdj"}) and its generalizations for more complex types of permutations, which involve $F_{\beta}$ with $\beta = 1$ and $4$ as well (see [@BR]), paved the way that brought the Tracy-Widom distribution functions into many areas of physics, mathematics and engineering. We refer to the surveys [@deift2; @CorwinBAMS] for a discussion of a wide variety of examples and a historical review.

We close this section by mentioning one remarkable generalization of the Ulam problem. Consider $N$-independent standard one-dimensional Brownian motions $B_1(t),B_2(t),\ldots, B_N(t)$, for $t\geq 0$. For $0\leq a<b$ let $B_i(a,b) = B_i(b)-B_i(a)$ denote the increment of the $i^{th}$ Brownian motion on the time interval $[a,b]$. Define the last passage time $M^N_t$ through the environment of Brownian motions by $$M^N_t := \max_{0\leq s_1\leq \cdots\leq s_{N-1}\leq t} \left(B_1(0,s_1)+B_2(s_1,s_2)+\cdots + B_{N}(s_{N-1},t)\right).$$ In joint work [@105] with Janko Gravner and Craig Tracy, Harold Widom proved that $M^N_t/\sqrt{t}$ has the same distribution as the largest eigenvalue of an $N\times N$ GUE matrix. In fact, in their work, they also study some discrete generalizations of the Ulam problem which are related to growth models and last passage problems such as above.
