---
doc_id: arxiv-math-ph-0010012v1
doc_title: "arXiv:math-ph/0010012v1 10 Oct 2000"
section_id: sec-012-331-step-one-relating-correlations-and-joint-pro
section_title: "Step One: Relating correlations and joint probability distributions"
section_number: 3.3.1
pages: 5-5
source_pdf: 0010012v1.pdf
source_sha256: cd6eca5ccb81ff90
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.963
doc_brief: "arXiv:math-ph/0010012v1 10 Oct 2000 — We review some recent results on random polynomials and their generalizations in complex and symplectic geometry."
---
Following an idea due originally to Kac and Rice in the case of real polynomials of one variable, we express the correlation measures in terms of the joint probability distribution of the random variables $s(z^1),\dots,s(z^n),
\nabla s(z^1),\dots,\nabla s(z^n)$. This JPD is defined by $$\widetilde{\mathbf D}_{z}^N:=
\widetilde D_{n}^N(x,\xi,z)dxd\xi=(J_z)_*\nu_N\,,
\;\;J_{z}(s) = (s(z), \nabla s(z)),$$ i.e. it is the push-forward of the Gaussian measure $\gamma_N$ under the linear jet map $J(z)$.

The desired expression for correlations in terms of the JPD is given by the following generalization of the Kac-Rice formula [@K] to the geometric setting of this article:

::: theo
[]{#introdn label="introdn"} [@BSZ1; @BSZ3; @SZ2] In the case of correlations of complex zeros, we have: $$K_{2k}^N(z)=
\int d\xi\,\widetilde D_n^N(0,\xi,z)\prod_{p=1}^n
\det(\xi^{p}\xi^{p*})\,.$$
:::

Analogous formulae exist for critical points, but involve the jet maps $(\nabla s(z), \nabla^2 s(z))$. The real case is similar to the complex case, but is somewhat more complicated because $\Pi_N$ is oscillatory rather than exponentially decaying [@N].
