---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-024-26-two-probabilistic-structures-on--polynomial-f
section_title: "Two probabilistic structures on -polynomial functions"
section_number: 2.6
pages: 18-18
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.873
latex_coverage_ratio: 1.0
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
[]{#sec:probabilistic-structures label="sec:probabilistic-structures"}

Assume that $\chi\colon\mathcal{P}_{n}\to\mathbb{R}$ is a reducible Jack character and let $\mathbb{P}_\chi$ be the corresponding probability measure [\[eq:proba-linearcomb-A\]](#eq:proba-linearcomb-A){reference-type="eqref" reference="eq:proba-linearcomb-A"} on the set $\mathbb{Y}_{n}$ of Young diagrams with $n$ boxes. With this setup, functions on $\mathbb{Y}_{n}$ can be viewed as random variables; we denote by $\mathbb{E}_\chi$ the corresponding expectation.

Let us fix a partition $\pi\in\mathcal{P}_{n}$; we denote by $\chi^{(\alpha)}_\# (\pi)$ the random variable $\mathbb{Y}_{n}\ni\lambda\mapsto \chi^{(\alpha)}_\lambda (\pi)$ given by irreducible Jack character [\[eq:character-Jack-unnormalized-zmiana\]](#eq:character-Jack-unnormalized-zmiana){reference-type="eqref" reference="eq:character-Jack-unnormalized-zmiana"}. From the way the probability measure $\mathbb{P}_\chi$ was defined in [\[eq:proba-linearcomb-A\]](#eq:proba-linearcomb-A){reference-type="eqref" reference="eq:proba-linearcomb-A"} it follows immediately that $$\label{eq:mean-value-simple}
\mathbb{E}_\chi\left[ \chi^{(\alpha)}_\# (\pi) \right] =  \chi(\pi).$$

Any $\alpha$-polynomial function $F$ can be restricted to the set $\mathbb{Y}_{n}$ of Young diagrams with $n$ boxes; thus it makes sense to speak about its expected value $\mathbb{E}_\chi F$. In the case when $F=\mathop{\mathrm{Ch}}_\pi$ is a Jack character, this expected value can be explicitly calculated thanks to [\[eq:mean-value-simple\]](#eq:mean-value-simple){reference-type="eqref" reference="eq:mean-value-simple"}:

$$\label{eq:what-is-normalized-character}
\mathbb{E}_\chi \mathop{\mathrm{Ch}}_{\pi}=
\begin{cases}
n^{\underline{|\pi|}}\ \chi(\pi) & \text{if }n < |\pi|, \\
0                                        & \text{otherwise.}
\end{cases}$$

By considering the multiplicative structure on $\alpha$-polynomial functions given by the pointwise product, we get in this way a conditional expectation $\mathbb{E}_\chi\colon \mathscr{P}\to \mathbb{R}$; the corresponding cumulants will be denoted by $\kappa_{\ell}^{\chi}$.

On the other hand, by considering the disjoint product, we get a conditional expectation $\mathbb{E}_\chi\colon \mathscr{P}_\bullet\to \mathbb{R}$; the corresponding cumulants will be denoted by $\kappa_{\bullet\ell}^{\chi}$.
