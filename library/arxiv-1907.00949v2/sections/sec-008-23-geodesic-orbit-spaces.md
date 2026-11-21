---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-008-23-geodesic-orbit-spaces
section_title: "Geodesic orbit spaces"
section_number: 2.3
pages: 6-7
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.951
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
Let $M = G/H$ be a homogeneous space of $G$. If $M$ has a Riemannian metric $g$ such that every geodesic in $M$ is an orbit of a one-parameter subgroup of $G$, then we say that $(M,g)$ is a *geodesic orbit space*. The following result [@KS2000] will allow us to construct several interesting examples.

::: theorem
[]{#thm:GO label="thm:GO"} Let $G$ be a compact Lie group with a bi-invariant metric $g$ and $H$ be a subgroup such that $M = G/H$ is a smooth manifold (e.g., $H$ is closed subgroup). Then $M = G/H$ together with the metric $\widetilde{g}$ induced by $g$ is a geodesic orbit space.
:::

In general it is difficult if not impossible to determine closed form analytic expressions for geodesics on a Riemannian manifold. But in the case of a geodesic orbit space, since its geodesics are simply orbits of one-parameter subgroups of $G$, the task reduces to determining the latter. The next result [@GW2009 Theorem 1.3.5] will be helpful towards this end.

::: theorem
[]{#thm:1-parameter subgp label="thm:1-parameter subgp"} If $G$ is a matrix Lie group equipped with a bi-invariant metric, then every one-parameter subgroup $\gamma(t)$ of $G$ is of the form $$\gamma(t) = \exp (ta) \coloneqq \sum_{k=0}^\infty \frac{t^ka^k}{k!}$$ for some $a \in \mathfrak{g}$.
:::

So for example, every one-parameter subgroup of $\mathop{\mathrm{SO}}(n)$ must take the form $\gamma(t)  =\exp (ta)$ for some skew-symmetric matrix $a\in \mathfrak{so}(n)$.
