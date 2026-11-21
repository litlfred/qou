---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-002-12-main-result
section_title: "Main result"
section_number: 1.2
pages: 5-5
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 1.0
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
The main result of this paper is the description of the first and second order asymptotics of the bulk of Young diagrams under Jack measure.

First, we prove a law of large numbers. If $\lambda$ is a Young diagram of size $n$, we denote by $\overline{A_\alpha(\lambda)}$ the (generalized) Young diagram obtained from $\lambda$ by an horizontal stretching of ratio $\sqrt{\alpha/n}$ and a vertical stretching of ratio $1/\sqrt{n\alpha}$ (a formal definition of generalized Young diagrams is given in Section [\[SubsectGeneralizedYD\]](#SubsectGeneralizedYD){reference-type="ref" reference="SubsectGeneralizedYD"}). We will prove in Section [\[sect:FirstOrder\]](#sect:FirstOrder){reference-type="ref" reference="sect:FirstOrder"} the following result.

::: theorem
[]{#theo:RYD-limit label="theo:RYD-limit"} For each $n$, let $\lambda_{(n)}$ be a random Young diagram of size $n$ distributed according to Jack measure. Then, in probability, $$\lim_{n \to \infty} \sup\limits_{x\in \mathbb{R}} \left| \omega\left(\overline{A_\alpha(\lambda_{(n)})}\right)(x)
 - \Omega(x) \right|  = 0.$$
:::

Note that the limiting curve is exactly the same as in the case $\alpha=1$.

Moreover, we establish a central limit theorem. Informally, it can be presented as follows: $$\label{eq:informal}
    \omega\left(\overline{A_\alpha(\lambda_{(n)})}\right)(x) \sim \Omega(x) +\frac{2}{\sqrt{n}} \Delta^{(\alpha)}_{\infty}(x),$$ where $\Delta^{(\alpha)}_{\infty}$ is the Gaussian process on $[-2,2]$ with values in $(\mathcal{C}^\infty(\mathbb{R}))'$ defined by: $$\Delta_\infty^{(\alpha)} (2 \cos(\theta) )=
 \frac{1}{\pi} \sum_{k=2}^\infty \frac{\Xi_k}{\sqrt{k}} \sin(k \theta) - \gamma/4 +\gamma \theta/2\pi.$$ Here, and throughout the paper, $\gamma$ is the difference $\sqrt{\alpha}^{-1}-\sqrt{\alpha}$. The formal version of this result is stated and proved in Section [\[sect:CLT2\]](#sect:CLT2){reference-type="ref" reference="sect:CLT2"}, while the explanation for the informal reformulation is given in Section [\[subsect:informal\]](#subsect:informal){reference-type="ref" reference="subsect:informal"}. Note that the random part of the second order asymptotics is independent of $\alpha$, while a deterministic term proportional to $\gamma$ (and, hence, vanishing for $\alpha=1$) appears.

Here again, the similarity with the G$\beta$E ensemble is striking. Indeed, for the bulk of the spectral measure of the G$\beta$E ensemble, we also have the following phenomena:

-   the first order asymptotics is independent of $\beta$ -- see equation [\[eq:first-order-GBE\]](#eq:first-order-GBE){reference-type="eqref" reference="eq:first-order-GBE"};

-   the second order asymptotics is the sum of two terms: a random one and a deterministic one. Moreover, the quotient of the deterministic one over the random one is proportional to $\gamma$ (see [@DumitriuEdelman2006 Theorem 1.2]).

Therefore our result is a new hint towards the deep connection between Jack measure and the G$\beta$E ensemble.
