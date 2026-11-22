---
doc_id: arxiv-math-ph-0010012v1
doc_title: "arXiv:math-ph/0010012v1 10 Oct 2000"
section_id: sec-007-23-sequences-of-random-polynomials
section_title: "Sequences of random polynomials"
section_number: 2.3
pages: 3-4
source_pdf: 0010012v1.pdf
source_sha256: cd6eca5ccb81ff90
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.965
doc_brief: "arXiv:math-ph/0010012v1 10 Oct 2000 — We review some recent results on random polynomials and their generalizations in complex and symplectic geometry."
---
We are often interested in sequences of polynomials $\{s_N\}$ chosen independently and at random from ${\mathcal H}_N$ from either a Gaussian or spherical ensemble. We thereform form the product probability space $({\mathcal H}_{\infty}, \mu_{\infty})$, defined by $${\mathcal H}_{\infty} = {\mathcal H}_1 \times {\mathcal H}_2 \times \cdots \times {\mathcal H}_N \times \cdots,\;\;\; \mu_{\infty} = \times_{N = 1}^{\infty} \mu_N, \;\; (\mu_N = \gamma_N\;
\mbox{or}\; \nu_N).$$ When we say that a sequence of polynomials $\{s_N\}$ of increasing degerees does something almost surely, we mean that the set of such sequences has measure one in this product ensemble.

## Szegö kernels

Our results depend on the fact that certain statistical properties of polynomials can be expressed in terms of the reproducing kernels $\Pi_N(x,y)$ (orthogonal projections) of the Hilbert spaces ${\mathcal H}_N$. They are known as Szego kernels, and are essentially the same as the 'coherent states' of the physics literature. The local structure of the Szegö kernel is given by the following scaling asymptotics:

::: theo
As $N \to \infty$, we have:

-   [@BSZ2; @SZ2] Complex case: $$\Pi_N(z_0 + \frac{u}{\sqrt{N}}, \frac{\theta}{N}, z_0 + 
    \frac{v}{\sqrt{N}}, \frac{\varphi}{N})
    \sim \frac{1}{\pi^m} e^{i (\theta - \varphi)}
    e^{u \cdot \bar{v} -{\frac{1}{2}}(|u|^2 + |v|^2)} \{1 + \frac{1}{\sqrt{N}}
    p_{1}(u,v; z_0)
    + \cdots \}\,.$$ The leading order term is the Szegö kernel for the reduced Heisenberg group, whence the name 'Heisenberg class.'

-   Real case: $$N^{-m + 1} \Pi_N(x_0 + \frac{u}{N},  x_0 + 
    \frac{v}{N})
    \sim \Gamma(\frac{m - 1}{2}) (\frac{|u - v|}{2})^{\frac{m - 2}{2}} J_{\frac{m - 2}{2}}(|u - v|) + \cdots \,,$$ where $J_{\nu}$ is the Bessel function of the first kind of order $\nu$ (whence the name 'Euclidean class'.)
:::

The proof of the scaling asymptotics in the complex holomorphic case [@BSZ2] is based on the Boutet-de-Monvel- Sjostrand parametrix for the Szegö kernel, which is valid for positive line bundles. A similar parametrix was constructed in the symplectic almost-complex case [@SZ2], and the scaling asymptotics were derived from it. In the real case of $S^m$, the scaling asymptotics are closely related to the 'Mehler-Heine formula'. The terms 'Heisenberg class' and 'Euclidean class' suggest infinite dimensional Gaussian ensembles related to representations of the Heisenberg and Euclidean motion groups.
