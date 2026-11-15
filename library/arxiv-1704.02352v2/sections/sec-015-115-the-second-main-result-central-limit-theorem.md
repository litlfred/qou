---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-015-115-the-second-main-result-central-limit-theorem
section_title: "The second main result: Central Limit Theorem"
section_number: 1.15
pages: 9-10
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.976
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
[]{#sec:clt-simple label="sec:clt-simple"} We keep the notations from [\[theo:lln\]](#theo:lln){reference-type="ref" reference="theo:lln"}. The difference $$\label{eq:fluctuations-around-infty}
\Delta_n:= \sqrt{n} \left( \omega_{\Lambda_n}- \omega_{\Lambda_\infty} \right).$$ is a random function on the real line which quantifies the (suitably rescaled) discrepancy between the shape of the random (anisotropic) Young diagram $\Lambda_n$ and the limit shape. We will regard ${\Delta}_n$ as a Schwartz distribution on the real line $\mathbb{R}$ or, more precisely, as a *random vector* from this space.

The following result is a generalization of Kerov's CLT [@Kerov1993gaussian; @IvanovOlshanski2002] which concerned Plancherel measure in the special case $\alpha=1$ as well as a generalization of its extension by the first-named author and Féray [@DolegaFeray2014] for the generic *fixed* value of $\alpha>0$. Indeed, [\[example:plancherel\]](#example:plancherel){reference-type="ref" reference="example:plancherel"} shows that the assumptions of the following theorem are fulfilled for $\chi_n:=\chi_{\mathop{\mathrm{reg}}}$, thus CLT holds for Jack--Plancherel measure *in a wider generality, when $\alpha=\alpha(n)$ may vary with $n$*.

On the other hand the following result is also a generalization of the results of the second-named author [@Sniady2006c] who considered a setup similar to the one below in the special case $\alpha=1$.

::: theorem
[]{#theo:clt label="theo:clt"} We keep the assumptions and the notations from [\[theo:lln\]](#theo:lln){reference-type="ref" reference="theo:lln"}.

Then for $n\to\infty$ the random vector ${\Delta}_n$ converges in distribution to some (non-centered) Gaussian random vector $\Delta_\infty$ valued in the space $(\mathbb{R}[x])'$ of distributions, the dual space to polynomials.
:::

The above statement about the convergence of the random vector ${\Delta}_n$ should be understood in a rather specific sense, formulated with help of some suitable test functions. Namely, for each finite collection of polynomials $f_1,\dots,f_k \in \mathbb{C}[x]$ we claim that the joint distribution of the random variables $$\langle \Delta_n,f_i \rangle := \int_\mathbb{R}\Delta_n(x)f_i(x) \dif x \qquad \text{for }i\in\{1,\dots,k\}$$ converges to the Gaussian distribution.

Informally speaking: asymptotically, for $n\to\infty$ $$\omega_{\Lambda_n} \approx \omega_{\Lambda_\infty}+\frac{1}{\sqrt{n}} \Delta_\infty$$ where $\omega_{\Lambda_\infty}$ is a deterministic curve and $\Delta_\infty$ is a Gaussian process.

::: remark
[]{#remark:theo:clt label="remark:theo:clt"} In order to prove [\[theo:clt\]](#theo:clt){reference-type="ref" reference="theo:clt"} it is enough to show that the joint distribution of any finite family of random variables $(Y_k)_{k\geq 2}$ converges as $n\to\infty$ to a (non-centered) Gaussian distribution, where $$\label{eq:my-random-variables-2}   
    Y_k:= \frac{k-1}{2} \int  u^{k-2} \ \Delta_n(u) \dif u$$ is (up to a simple scalar factor) the value of the Schwartz distribution $\Delta_n$ evaluated on a suitable polynomial test function.
:::

The proof is postponed to [\[sec:proof-of-CLTCLT\]](#sec:proof-of-CLTCLT){reference-type="ref" reference="sec:proof-of-CLTCLT"}.
