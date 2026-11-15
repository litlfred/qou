---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL (2)"
section_id: sec-009-the-automorphism-group-of-a-slq-2
section_title: "the automorphism group of A( SLq (2))"
section_number: null
pages: 9-10
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.962
doc_brief: "Twisted homology of quantum SL (2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra of the quan- tum SL(2) group"
---
For $\lambda,\mu \in k^\times$ there are unique automorphisms $\sigma_{\lambda, \mu},\tau_{\lambda, \mu}$ of $\mathcal{A}$ with $$\sigma_{\lambda, \mu}(a)=\lambda a,\quad
    \sigma_{\lambda, \mu}(b)=\mu b,\quad
    \sigma_{\lambda, \mu}(c)=\mu^{-1} c,\quad
    \sigma_{\lambda, \mu}(d)=\lambda^{-1} d,$$ $$\label{defn_lambda_tau}
 \tau_{\lambda, \mu}(a)=\lambda a,\quad
    \tau_{\lambda, \mu}(b)=\mu^{-1} c,\quad
    \tau_{\lambda, \mu}(c)=\mu b,\quad
    \tau_{\lambda, \mu}(d)=\lambda^{-1} d.$$ It is easy to check that this list is complete, although we do not know a reference where this was pointed out explicitly:

::: prop
[]{#autos label="autos"} If $\sigma$ is an automorphism of $\mathcal{A}(SL_q (2))$, then either $\sigma=\sigma_{\lambda, \mu}$ or $\sigma=\tau_{\lambda, \mu}$ for some $\lambda,\mu$.
:::

::: pf
Using the $\mathbb{Z}$-grading and the $\mathbb{N}$-filtrations mentioned above it is a straightforward calculation to check that up to rescaling and exchanging $b$ and $c$ the original generators are the only elements of the algebra that fulfill the defining relations.
:::

The $\sigma_{\lambda,\mu}$ act diagonally with respect to the generators $a,b,c,d$. The $\tau_{\lambda,\mu}$ are also diagonalizable. For fixed $\lambda, \mu$ define $x_\pm = c \pm \mu b$. Then $\tau_{\lambda,\mu} ( x_{\pm} ) = \pm x_{\pm}$, and $a, x_+ , x_- ,d$ generate $\mathcal{A}$. So by Proposition [\[tatata\]](#tatata){reference-type="ref" reference="tatata"}:

::: cor
[]{#crucial_isomorphism label="crucial_isomorphism"} For $\mathcal{A}= \mathcal{A}( SL_q (2))$, and for each $n$ and every automorphism $\sigma$, we have $HH_n^\sigma(\mathcal{A}) \cong H_n (\mathcal{A}, {}_\sigma\mathcal{A})$.
:::
