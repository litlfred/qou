---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems"
section_id: sec-008-32-longest-increasing-subsequence
section_title: "Longest increasing subsequence"
section_number: 3.2
pages: 5-6
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
toc_source: outline
text_source: latex
latex_prose_ratio: 0.734
latex_coverage_ratio: 1.0
doc_brief: "KPZ limit theorems — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
The Poisson DLPP is particularly interesting due to its connection to longest increasing subsequences of random permutations. Note that finitely many points in a rectangle with distinct $x$ and $y$ coordinates can be associated with a permutation by considering the relative orderings of the coordinates.

For example, the points in Figure [\[fig:PoissonDLPP\]](#fig:PoissonDLPP){reference-type="ref" reference="fig:PoissonDLPP"} are associated with the permutation $\pi=475168293$. For this permutation, the subsequence $45689$ is an increasing subsequence. Furthermore, it is the longest increasing subsequence, and its length, $5$, is equal to the last passage time $L(t,s)$.

Let $\ell_N$ denote the length of longest increasing subsequences of a uniformly random permutation of size $N$.

Then, $L(t,s)$ has the same distribution as $\ell_N$, where $N$ is a Poisson random variable of mean $ts$. Using this connection, Theorem [\[thm:Poisson\]](#thm:Poisson){reference-type="ref" reference="thm:Poisson"} implies, after a de-Poissonization argument, that $\frac{\ell_N- 2\sqrt{N}}{N^{1/6}}$ converges in distribution to the Tracy--Widom distribution.

The problem of determining the large $N$ behavior of $\ell_N$ has a long history. The existence of the almost sure limit of $\ell_N/\sqrt{N}$ was proved by Hammersley in [@Hammersley72] using Kingman's ergodic subadditivity theorem. The fact that the limit is $2$, known as Ulam's problem, was proved independently by two famous papers of Veršik --Kerov [@Vershik-Kerov77] and Logan--Shepp [@Logan-Shepp77] in 1977.

However, the limiting distribution and the variance (which is of order $N^{2/3}$) remained an open problem until the work [@Baik-Deift-Johansson99].

Interested readers are encouraged to consult [@Aldous-Diaconis99; @Stanley07; @Romik15; @Baik-Deift-Suidan].

## Exponential DLPP

Soon after Theorem [\[thm:Poisson\]](#thm:Poisson){reference-type="ref" reference="thm:Poisson"} was proved, Johansson showed that the exponential DLPP model also satisfies a similar limit theorem [@Johansson00]. We state the result in terms of the height function of the TASEP.

::: theorem
[]{#thm:Johansson label="thm:Johansson"} Assume the step initial condition for the TASEP.

Then, for every $( \tau, \gamma, \mathsf{h}) \in \mathbb{R}_+\times \mathbb{R}\times \mathbb{R}$, $$\lim_{T\to \infty} \mathrm{P}\left(  \frac{\mathbf{h}(\gamma T^{2/3}, 2 \tau T) - \tau T}{-T^{1/3}} \le \mathsf{h}\right) 
    =  \mathrm{F}_{\mathrm{TW}}\left( \frac{\mathsf{h}}{\tau^{1/3}} + \frac{\gamma^2}{4\tau^{4/3}} \right) .$$
:::

Note from either side of the equation that the limit remains unchanged if we rescale $$\label{eq:rescale}
    (\mathsf{h}, \gamma, \tau) \mapsto (\alpha \mathsf{h}, \alpha^2 \gamma, \alpha^3 \tau)$$ for any $\alpha>0$.
