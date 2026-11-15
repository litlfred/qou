---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-014-114-the-first-main-result-law-of-large-numbers
section_title: "The first main result: Law of Large Numbers"
section_number: 1.14
pages: 8-9
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.928
latex_coverage_ratio: 0.955
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
The following theorem is a generalization of the results of Biane [@Biane2001] who considered the special case $\alpha=1$ and the corresponding representations of the symmetric groups.

::: theorem
[]{#theo:lln label="theo:lln"} Assume that $\alpha=\alpha(n)$ is such that [\[eq:double-scaling-refined\]](#eq:double-scaling-refined){reference-type="eqref" reference="eq:double-scaling-refined"} holds true. Assume that $\chi_n\colon\mathcal{P}_{n}\to\mathbb{R}$ is a reducible Jack character; we denote by $\lambda_n$ the corresponding random Young diagram with $n$ boxes distributed according to $\mathbb{P}^{(\alpha)}_{\chi_n}$. We assume also that the sequence $(\chi_n)$ of characters fulfills the enhanced approximate factorization property.

Then there exists some deterministic function $\omega_{\Lambda_\infty}\colon\mathbb{R}\to\mathbb{R}$ with the property that $$\label{eq:limit}
    \lim_{n\to\infty} \omega_{\Lambda_n} = \omega_{\Lambda_\infty},$$ where $$\label{eq:Lambda}
    \Lambda_n:= T_{\sqrt{\frac{\alpha}{n}},\sqrt{\frac{1}{\alpha n}}} \lambda_n$$

and the convergence in [\[eq:limit\]](#eq:limit){reference-type="eqref" reference="eq:limit"} holds true with respect to the supremum norm, in probability. In other words, for each $\epsilon>0$ $$\lim_{n\to\infty} \mathbb{P}\big( \|\omega_{\Lambda_n}-\omega_{\Lambda_\infty}   \|_\infty>
    \epsilon \big) =0 .$$
:::

::: remark
The concrete formula for the profile $\omega_{\Lambda_\infty}$ may be obtained by computing the corresponding $R$-transform and Cauchy transform, see for example [@Biane2001 Theorem 3].
:::

The proof is postponed to [\[sec:proof-of-LLN\]](#sec:proof-of-LLN){reference-type="ref" reference="sec:proof-of-LLN"}.
