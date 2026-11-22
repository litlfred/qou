---
doc_id: arxiv-math-ph-0010012v1
doc_title: "arXiv:math-ph/0010012v1 10 Oct 2000"
section_id: sec-006-22-gaussian-measures-and-spherical-measures
section_title: "Gaussian measures and spherical measures"
section_number: 2.2
pages: 3-3
source_pdf: 0010012v1.pdf
source_sha256: cd6eca5ccb81ff90
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.986
doc_brief: "arXiv:math-ph/0010012v1 10 Oct 2000 — We review some recent results on random polynomials and their generalizations in complex and symplectic geometry."
---
We will restrict attention to two related ensembles:

-   *Gaussian ensembles*: We fix an orthonormal basis $\{f_j\}$ of ${\mathcal H}_N$ and write functions as orthonormal sums $f = \sum_{j = 1}^{d_N} c_j f_j$. We then define the (complex) Gaussian measure by $$\gamma = e^{- ||f||^2} {\mathcal D}f,\;\; \mbox{i.e.} \;\; \gamma = e^{- |c|^2} dc.$$ More generally we fix a symmetric matrix $\Delta$ on ${\mathbb C}^{d_N}$ with positive (semi-)definite imaginary part and define: $$\gamma_\Delta= \frac{e^{- \langle\Delta^{-1}
    c,c\rangle}}{(2\pi)^{p/2}\det\Delta}
    dc\,,\label{gaussian}$$ Gaussian ensembles come in both real and complex flavors. In the real case, the exponents acquire factors of $1/2$ and the denominator acquires a square root.

-   *Spherical ensembles*: We denote by $S{\mathcal H}_N = \{f \in {\mathcal H}_N: ||f|| = 1\}.$ We then equip $S{\mathcal H}_N$ with the uniform (Haar) probability measure $\nu_N.$

We will denote the expected value of a random variable $X$ with respect to the Gaussian ensemble by ${\bf E}_{\gamma}(X)$ (resp. ${\bf E}_{\nu}(X)$ for the spherical ensemble).

These two ensembles are *equivalent* in the sense that the two large dimension limits give equivalent results when scaled properly. A more precise formulation goes as follows:

*[]{#spherical-vs-gaussian label="spherical-vs-gaussian"} Let $T_N: {\mathbb R}^{d_N} \to R^k$, $N=1,2,\dots$, be a sequence of linear maps, where $d_N
\to \infty$. Suppose that $\frac{1}{d_N}T_N T_N^*
\to
\Delta$. Then $T_{N*} \nu_{d_N} \to \gamma_{\Delta}$.*
