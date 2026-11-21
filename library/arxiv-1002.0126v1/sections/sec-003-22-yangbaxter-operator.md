---
doc_id: arxiv-1002.0126v1
doc_title: "AN INTRODUCTION TO THE VOLUME CONJECTURE"
section_id: sec-003-22-yangbaxter-operator
section_title: "Yang–Baxter operator"
section_number: 2.2
pages: 4-5
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
toc_source: outline
text_source: latex
latex_prose_ratio: 0.885
latex_coverage_ratio: 0.949
doc_brief: "AN INTRODUCTION TO THE VOLUME CONJECTURE — This is an introduction to the Volume Conjecture and its gener- alizations for nonexperts."
---
Alexander's theorem (Theorem [\[thm:Alexander\]](#thm:Alexander){reference-type="ref" reference="thm:Alexander"}) and Markov's theorem (Theorem [\[thm:Markov\]](#thm:Markov){reference-type="ref" reference="thm:Markov"}) can be used to define link invariants. I will follow Turaev [@Turaev:INVEM88] to introduce a link invariant derived from a Yang-Baxter operator.

Let $V$ be an $N$-dimensional vector space over $\mathbb{C}$, $R$ an isomorphism from $V\otimes V$ to itself, $m$ an isomorphism from $V$ to itself, and $a$ and $b$ non-zero complex numbers.

::: definition
[]{#def:YB label="def:YB"} A quadruple $(R,\mu,a,b)$ is called an enhanced Yang--Baxter operator if it satisfies the following:

1.  $(R\otimes\operatorname{Id}_V)(\operatorname{Id}_V\otimes R)(R\otimes\operatorname{Id}_V)
    =(\operatorname{Id}_V\otimes R)(R\otimes\operatorname{Id}_V)(\operatorname{Id}_V\otimes R)$,

2.  $R(\mu\otimes\mu)=(\mu\otimes\mu)R$,

3.  $\operatorname{Tr}_2\bigl(R^{\pm1}(\operatorname{Id}_V\otimes\mu)\bigr)=a^{\pm1}b\operatorname{Id}_V$.

Here $\operatorname{Tr}_k\colon\operatorname{End}(V^{\otimes k})\to\operatorname{End}(V^{\otimes(k-1)})$ is defined by $$\operatorname{Tr}_k(f)(e_{i_1}\otimes e_{i_2}\dots\otimes e_{i_{k-1}})
  :=
  \sum_{j_1,j_2,\dots,j_{k-1},j=0}^{N-1}
  f_{i_1,i_2,\dots,i_{k-1},j}^{j_1,j_2,\dots,j_{k-1},j}
  (e_{j_1}\otimes e_{j_2}\otimes\dots\otimes e_{j_{k-1}}\otimes e_{j}),$$ where $f\in\operatorname{End}(V^{\otimes k})$ is given by $$f(e_{i_1}\otimes e_{i_2}\otimes\dots\otimes e_{i_k})
  =
  \sum_{j_1,j_2,\dots,j_k=0}^{N-1}
  f_{i_1,i_2,\dots,i_k}^{j_1,j_2,\dots,j_k}
  (e_{j_1}\otimes e_{j_2}\otimes\dots\otimes e_{j_k})$$ and $\{e_0,e_1,\dots,e_{N-1}\}$ is a basis of $V$.
:::

::: remark
The isomorphism $R$ is often called an $R$-matrix, and the equation (1) is known as the Yang--Baxter equation.
:::

Given an $n$-braid $\beta$, we can construct a homomorphism $\Phi(\beta)\colon V^{\otimes n}\to V^{\otimes n}$ by replacing a generator $\sigma_i$ with $\operatorname{Id}_V^{\otimes(i-1)}\otimes R\otimes\operatorname{Id}_V^{\otimes(n-i-1)}$, and its inverse $\sigma_i^{-1}$ with $\operatorname{Id}_V^{\otimes(i-1)}\otimes R^{-1}\otimes\operatorname{Id}_V^{\otimes(n-i-1)}$ (Figure [1](#fig:braid_homomorphism){reference-type="ref" reference="fig:braid_homomorphism"}).

<figure id="fig:braid_homomorphism">
<p><span class="math inline">⇒</span> , <span class="math inline">⇒</span></p>
<figcaption>Replace a generator with the <span class="math inline"><em>R</em></span>-matrix.</figcaption>
</figure>

::: example
For the braid $\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$ the corresponding homomorphism is give as follows (Figure [2](#fig:fig_8_homomorphism){reference-type="ref" reference="fig:fig_8_homomorphism"}): $$\Phi(\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1})
  =
  (R\otimes\operatorname{Id}_V)(\operatorname{Id}_V\otimes R^{-1})(R\otimes\operatorname{Id}_V)(\operatorname{Id}_V\otimes R^{-1}).$$

<figure id="fig:fig_8_homomorphism">
<p><embed src="braid_small.eps" /> <embed src="braid_R_small.eps" /></p>
<figcaption>A braid and the corresponding homomorhism</figcaption>
</figure>
:::
