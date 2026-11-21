---
doc_id: arxiv-2311.05446v3
doc_title: "New Brunn--Minkowski and functional inequalities via convexity of entropy"
section_id: sec-003-13-towards-the-best-possible-exponent-in-the-ent
section_title: "Towards the best possible exponent in the entropy inequality"
section_number: 1.3
pages: 5-6
source_pdf: 2311.05446v3.pdf
source_sha256: c5809730f598a56d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 0.978
doc_brief: "New Brunn--Minkowski and functional inequalities via convexity of entropy — We study the connection between the concavity properties of a measure ν and the convexity properties of the associated"
---
As mentioned, Theorem [\[thm:main-BM intro\]](#thm:main-BM intro){reference-type="ref" reference="thm:main-BM intro"} implies the Kolesnikov-Livshyts inequality [\[eq:gassian-BM-2n\]](#eq:gassian-BM-2n){reference-type="eqref" reference="eq:gassian-BM-2n"}, but not the result of Eskenazis--Moschidis with the optimal exponent $\frac{1}{n}$. Since this result is known to be true, one can hope for a version of Theorem [\[thm:main-entropy\]](#thm:main-entropy){reference-type="ref" reference="thm:main-entropy"} that will imply it, that is, a version with the sharp coefficient $\frac{1}{n}$, under suitable assumptions on the potential $V$ and the measures $\mu_0$ and $\mu_1$.

One natural way to approach this problem is to perform the local analysis directly on $D(\cdot \Vert \nu)$ instead of splitting it to two components. Indeed, the concavity of $e^{-a D(\mu_{t} \Vert \nu)}$ along a displacement interpolation $\{ \mu_{t} \}_{t \in [0,1]}$ amounts to the inequality $$\frac{\textnormal{ d}^{2}}{\textnormal{ d}t^{2}} D(\mu_{t} \Vert \nu) \geq a \left( \frac{\textnormal{ d}}{\textnormal{ d}t} D(\mu_{t} \Vert \nu)  \right)^{2}.$$ As we will see later, both sides of the above inequality can be explicitly written in terms of certain differential operators applied to the velocity field driving the optimal transport. This leaves us with an inequality of almost the same form as the sufficiency criteria of Kolesnikov--Livshyts discussed earlier.

In the case of $\nu = \gamma$, an auxiliary construction from [@EskenazisMoschidis21] allows us to prove the following theorem:

::: thm
[]{#thm: gaussianentintro label="thm: gaussianentintro"} Suppose $\{ \mu_{t} \}_{t \in [0,1]}$ is a displacement interpolation such that each $\mu_{t}$ is even and satisfies the odd Poincáre inequality with constant $1$, that is $\int f^{2} \textnormal{ d}\mu_{t} \leq \int \vert \nabla f \vert^{2} \textnormal{ d}\mu$, for every odd test function $f$. Then, $$\frac{\textnormal{ d}^{2}}{\textnormal{ d}t^{2}} D(\mu_{t} \Vert \gamma) \geq 2 \mathscr{W}_{2}^{2}(\mu_{0},\mu_{1}) + \frac{1}{n} \left( \frac{\textnormal{ d}}{\textnormal{ d}t} D(\mu_{t} \Vert \gamma)  \right)^{2},$$ where $\mathscr{W}_{2}(\mu_{0},\mu_{1})$ denotes the $2$-Wasserstein metric (induced by the optimal transport problem).
:::

Thus, as readers familiar with the curvature-dimension framework may notice, under these assumptions on the $\mu_{t}$, not only can the "dimensional" improvement to $\frac{1}{n}$ be obtained, but the "curvature" also improves to $2$. Note that, without any restrictions on the $\mu_{t}$, $\frac{\textnormal{ d}^{2}}{\textnormal{ d}t^{2}} D(\mu_{t} \Vert \gamma) \geq  \mathscr{W}_{2}^{2}(\mu_{0},\mu_{1})$ is always true, which is reflective of the fact that Gauss space satisfies properties akin to a complete Riemannian manifold with Ricci curvature lower bounded by the metric tensor.

When $K$ is a convex body, then the density of $\nu_{K}$ with respect to $\nu$ is a log-concave function. This is the property of $\nu_{K}$ that typically expresses itself in extensions of various phenomena from the geometry of sets to the geometry of measures. When $\nu$ is the Gaussian measure $\gamma$, measures having a log-concave density with respect to $\gamma$ are called strongly log-concave measures. Given that the Gaussian measure satisfies a Brunn--Minkowski inequality with exponent $\frac{1}{n}$ over origin-symmetric convex bodies, it is a natural question whether displacement interpolation between two even strongly log-concave probability measures satisfies the assumptions of Theorem [\[thm: gaussianentintro\]](#thm: gaussianentintro){reference-type="ref" reference="thm: gaussianentintro"}.

::: qstn
[]{#qstn: poincare label="qstn: poincare"} Suppose $\mu_{0}, \mu_{1}$ are even strongly log-concave probability measures on $\mathbb{R}^n$. Let $\{ \mu_{t} \}_{t \in [0,1]}$ denote the displacement interpolation between $\mu_{0}$ and $\mu_{1}$. Is it true that each $\mu_{t}$, $t\in (0,1)$, satisfies the Poincáre inequality for odd functions with constant $1$?
:::

Note that the Brascamp--Lieb inequality ([@BrascampLieb76 Theorem 4.1]) guarantees that $\mu_{0}$ and $\mu_{1}$ in the above setup satisfy a Poincáre inequality with constant $1$ for all functions. Also note, that a positive answer to Question [\[qstn: poincare\]](#qstn: poincare){reference-type="ref" reference="qstn: poincare"}, combined with our Theorem [\[thm: gaussianentintro\]](#thm: gaussianentintro){reference-type="ref" reference="thm: gaussianentintro"}, would yield an entropic proof of the Eskenazis--Moschidis result. We show that Question [\[qstn: poincare\]](#qstn: poincare){reference-type="ref" reference="qstn: poincare"} has an affirmative answer in several cases, namely when the dimension of the ambient space is one, or when both $\mu_{0}$ and $\mu_{1}$ are themselves Gaussian measures, or when one of $\{ \mu_{0}, \mu_{1} \}$ is the standard Gaussian $\gamma$.
