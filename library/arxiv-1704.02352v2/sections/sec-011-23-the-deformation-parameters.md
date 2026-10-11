---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-011-23-the-deformation-parameters
section_title: "The deformation parameters"
section_number: 2.3
pages: 17-18
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
text_source: latex
latex_prose_ratio: 0.904
latex_coverage_ratio: 0.974
---
In order to avoid dealing with the square root of the variable $\alpha$ which is ubiquitous in the subject of Jack deformation, we introduce an indeterminate $A := \sqrt{\alpha}$. The algebra of Laurent polynomials in the indeterminate $A$ will be denoted by $\mathbb{Q}\left[A,A^{-1}\right]$.

A special role will be played by the quantity $$\label{eq:gamma}
\gamma := -A +\frac{1}{A} \in \mathbb{Q}\left[A,A^{-1}\right]$$ which already appeared in the numerator on the left-hand side of [\[eq:double-scaling-refined\]](#eq:double-scaling-refined){reference-type="eqref" reference="eq:double-scaling-refined"}.

## The linear space of $\alpha$-polynomial functions {#sec:polynomial}

In a paper [@Sniady-AsymptoticsJack] the second-named author has defined a certain filtered linear space of *$\alpha$-polynomial functions*. This linear space consists of certain functions in the set $\mathbb{Y}$ of Young diagrams with values in the ring $\mathbb{Q}\left[A,A^{-1}\right]$ of Laurent polynomials and, among many equivalent definitions, one can define it using normalized Jack characters.

::: definition
[]{#def:polynomial-functions label="def:polynomial-functions"} The linear space of $\alpha$-polynomial functions is the linear span (with rational coefficients) of the functions

$$\label{eq:linear-span}
    \gamma^k \mathop{\mathrm{Ch}}_\pi \colon \mathbb{Y}\to \mathbb{Q}\left[A,A^{-1}\right]$$ over the integers $k\geq 0$ and over partitions $\pi\in\mathcal{P}$.

The filtration on this vector space is specified as follows: for an integer $n\geq 0$ the subspace of vectors of degree at most $n$ is the linear span of the elements [\[eq:linear-span\]](#eq:linear-span){reference-type="eqref" reference="eq:linear-span"} over integers $k\geq 0$ and over partitions $\pi\in\mathcal{P}$ such that $$k+|\pi|+\ell(\pi)\leq n .$$
:::

## Algebras $\mathscr{P}$ and $\mathscr{P}_\bullet$ of $\alpha$-polynomial functions {#sec:polynomial-disjoint}

The vector space of $\alpha$-polynomial functions can be equipped with a product in two distinct natural ways (which will be reviewed in the following). With each of these two products it becomes a commutative, unital filtered algebra.

Firstly, as a product we may take the *pointwise product of functions on $\mathbb{Y}$*. The resulting algebra will be denoted by $\mathscr{P}$ (the fact that the $\mathscr{P}$ is closed under such product was proved by Dołęga and Féray [@DolegaFeray2014 Theorem 1.4]).

Secondly, as a product we may take the *disjoint product $\bullet$*, see [@Sniady-AsymptoticsJack Section 2.3], which is defined on the linear base of Jack characters by *concatenation* (see [\[sec:concatenation\]](#sec:concatenation){reference-type="ref" reference="sec:concatenation"}) of the corresponding partitions $$\left( \gamma^p \mathop{\mathrm{Ch}}_\pi\right) \bullet\left( \gamma^q \mathop{\mathrm{Ch}}_\sigma\right):= \gamma^{p+q} \mathop{\mathrm{Ch}}_{\pi \sigma}.$$ The resulting algebra will be denoted by $\mathscr{P}_\bullet$.

## Two probabilistic structures on $\alpha$-polynomial functions {#sec:probabilistic-structures}

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
