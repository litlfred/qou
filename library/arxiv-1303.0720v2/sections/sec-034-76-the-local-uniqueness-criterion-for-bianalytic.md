---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-034-76-the-local-uniqueness-criterion-for-bianalytic
section_title: "The local uniqueness criterion for bianalytic kernels"
section_number: 7.6
pages: 24-25
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.895
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
For $F(z,w)$ holomorphic in $(z,\bar w)$ near the diagonal $z=w$ in ${\mathbb C}^2$, it is well-known that the diagonal is a set of uniqueness. In particular, the assumption $F\in{\mathbf M}_{z-w}{\mathfrak R}_1$ implies that $F(z,w)\equiv0$ holds near the diagonal. We need the analogous criterion for functions biholomorphic in each of the variables $(z,\bar w)$.

::: lem
Suppose $F\in{\mathfrak R}_2$, so that $F(z,w)$ is biholomorphic in $z$ and $C^\infty$-smooth in $w$ near the diagonal $z=w$. If $F(z,w)\in{\mathbf M}_{z-w}^2{\mathfrak R}_2$, and in addition, $F(z,w)$ is biholomorphic in $\bar w$, then $F(z,w)\equiv0$ holds near the diagonal. []{#lem-uniq1 label="lem-uniq1"}
:::

::: proof
*Proof.* We first decompose $F=F_0+\bar z F_1+wF_2+\bar z wF_3$, where each $F_j$ is holomorphic in $(z,\bar w)$ near the diagonal. Since $F$ is biholomorphic in $z$, the function $\bar\partial_z\partial_w F=F_3$ is holomorphic in $(z,\bar w)$, and the assumption $F\in{\mathbf M}_{z-w}^2{\mathfrak R}_2$ leads to $\bar\partial_z\partial_w F=F_3\in{\mathbf M}_{z-w}{\mathfrak R}_1$. But the diagonal is a set of uniqueness for $F_3$, and we find that $F_3(z,w)\equiv0$. So $F=F_0+\bar z F_1+wF_2$, and, consequently, $\bar\partial_z F=F_1\in
{\mathbf M}_{z-w}^2{\mathfrak R}_1$ is holomorphic in $(z,\bar w)$. Again the diagonal is a set of uniqueness for $F_1$, which implies that $F_1(z,w)\equiv0$. What remains of the decomposition is now $F=F_0+wF_2$. From $F\in{\mathbf M}_{z-w}^2{\mathfrak R}_2$ we get that $\partial_w F=F_2\in{\mathbf M}_{z-w}{\mathfrak R}_2$, and analogously we obtain that $F_2(z,w)\equiv0$. The final step, to show that $F$ vanishes if $F=F_0\in{\mathbf M}_{z-w}^2{\mathfrak R}_2$ is holomorphic in $(z,\bar w)$, is trivial. ◻
:::

::: rem
In the context of the lemma, it is not possible to weaken the assumption that $F\in{\mathbf M}_{z-w}^2{\mathfrak R}_2$ to just $F\in{\mathbf M}_{z-w}{\mathfrak R}_2$, as is clear from the example $F(z,w):=z-w$.
:::
