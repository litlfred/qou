---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-036-43-categories-over-schemes
section_title: "Categories over schemes"
section_number: 4.3
pages: 35-36
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.911
latex_coverage_ratio: 0.909
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:spec label="sub:spec"}

In this section, we will develop a general setup relating a category $\mathcal{C}$ with a scheme $X$, with the goal of reducing Conjecture [\[conj:1\]](#conj:1){reference-type="ref" reference="conj:1"} to Conjecture [\[conj:main\]](#conj:main){reference-type="ref" reference="conj:main"}. Though we will not always say this explicitly, $X$ should be thought of as a dg scheme.

::: definition
[]{#def:morphism label="def:morphism"}

A **morphism** from the category $\mathcal{C}$ to the scheme $X$, written as: $$\mathcal{C}\stackrel{\iota}\longrightarrow X$$ consists of a pair of functors: $$\label{eqn:functors}
\mathcal{C}\xtofrom[\iota^*]{\iota_*} \mathrm{Coh}(X)$$ such that:

-   $\iota^*$ is a monoidal functor

-   $\iota_*$ is the right adjoint of $\iota^*$

-   the following **projection formula** holds: $$\label{eqn:projection}
    \iota_*(\iota^*M_1 \otimes C \otimes \iota^*M_2) = M_1 \otimes \iota_*(C) \otimes M_2$$ for all $M_1,M_2 \in \mathrm{Coh}(X)$ and $C \in \mathcal{C}$.
:::

The above definition is modeled on the situation when $\mathcal{C}= \mathrm{Coh}(Y)$ for a scheme $Y$, in which case the functors $\iota_*$ and $\iota^*$ play the roles of direct and inverse image functors associated to a map of schemes $\iota:Y \rightarrow X$.

::: definition
[]{#def:birational label="def:birational"}

We call the map $\mathcal{C}\stackrel{\iota}\longrightarrow X$ **birational** if: $$\label{eqn:birational}
\iota_* \mathbf{1} = \mathcal{O}_X$$
:::

This terminology, albeit imprecise, is motivated by the important case when $\mathcal{C}= \mathrm{Coh}(Y)$ where $Y$ is endowed with a proper birational map to $X$.

::: proposition
[]{#prop: proper hom label="prop: proper hom"} Suppose that $\mathcal{C}\stackrel{\iota}\longrightarrow X$ is birational. Then $\iota^*$ is fully faithful, and moreover: $$\label{eqn:RGamma}
\mathop{\mathrm{Hom}}_{\mathcal{C}}(\mathbf{1},\iota^* M) = \Gamma(X,M)$$ for all $M\in \mathrm{Coh}(X)$.
:::

::: proof
*Proof.* The adjunction implies that: $$\mathop{\mathrm{Hom}}_{\mathcal{C}}(\iota^*M',\iota^*M) = \mathop{\mathrm{Hom}}_X(M',\iota_*\iota^*M) = \mathop{\mathrm{Hom}}_X(M',M)$$ where the last equality follows from [\[eqn:projection\]](#eqn:projection){reference-type="eqref" reference="eqn:projection"} and [\[eqn:birational\]](#eqn:birational){reference-type="eqref" reference="eqn:birational"}. When $M'=\mathcal{O}_X$ we obtain precisely [\[eqn:RGamma\]](#eqn:RGamma){reference-type="eqref" reference="eqn:RGamma"}. ◻
:::

Most of the time we will consider a derived version of this construction.

::: definition
A **derived morphism** from the category $\mathcal{C}$ to the scheme $X$, written as: $$\mathcal{C}\stackrel{\iota}{\longrightarrow} X$$ is a pair of mutually adjoint functors: $$\label{eqn:derfunctors}
K(\mathcal{C}) \xtofrom[\iota^*]{\iota_*} D(\mathrm{Coh}(X))$$ All other properties and requirements remain unchanged.
:::
