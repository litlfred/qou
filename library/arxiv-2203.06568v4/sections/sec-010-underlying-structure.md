---
doc_id: arxiv-2203.06568v4
doc_title: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra"
section_id: sec-010-underlying-structure
section_title: "Underlying structure"
section_number: null
pages: 14-14
source_pdf: 2203.06568v4.pdf
source_sha256: 256fcfb588dac554
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra — We study the upper bounds for A(n, d), the maximum size of codewords with length n and Hamming distance at least d."
---
[]{#sec:struct label="sec:struct"}

Herein we describe a special structure for an association scheme, which is inspired by the split method used in this paper.

::: definition
($m$-split property) Let $S = (X, \{R_{i}\}_{i=0}^{k})$ be an association scheme. We say that $S$ is *$m$-split* for some $1 \leq m \leq \lvert X\rvert$ if there exist $m$ association schemes $S_{1} = (X_{1}, \{R_{i}^{(1)}\}_{i=0}^{k_{1}}), \dots, S_{m} = (X_{m}, \{R_{i}^{(m)}\}_{i=0}^{k_{m}})$ and a collection of maps $\{f_{i}\}$ such that $f_{i}: X \longrightarrow X_{i}$ is surjective for each $i$ and for $(x, y) \in X \times X$, $(x, y) \in R_{j}$ if and only if $\sum_{i = 1}^{m} d_{i} = j$, where $(f_{i}(x), f_{i}(y)) \in R_{d_{i}}^{(i)}$ for each $i$.
:::

Clearly, we have the following lemma.

::: lemma
Every association scheme is $1$-split.
:::

For an $m$-split association scheme $S$, we can define an $m$-split Bose-Mesner algebra by $\bigotimes_{i=1}^{m} {\cal B}(S_{i})$ and an $m$-split Terwilliger algebra by $\bigotimes_{i=1}^{m} {\cal T}(S_{i})$, where ${\cal B}(S_{i})$ is the Bose-Mesner algebra of $S_{i}$ and ${\cal T}(S_{i})$ is the Terwilliger algebra of $S_{i}$.

In our case of binary codes, $S = {\cal H}(n, 2)$ is the Hamming scheme of length $n$ over $\mathbb{F}_{2}$ and each $S_{i}$ is ${\cal H}(n_{i}, 2)$. Clearly, $S$ is $m$-split for $1 \leq m \leq n$. We may observe that $m$-split Bose-Mesner algebras induce the $m$-split generalized Delsarte's inequalities and $m$-split Terwilliger algebras induce $m$-split triple distances SDP. Moreover, there are ascending chains for algebras. $$\label{eq:chain_1}
    {\cal B}_{1} \leq {\cal B}_{2} \leq \cdots \leq {\cal B}_{n},$$ $$\label{eq:chain_2}
    {\cal T}_{1} \leq {\cal T}_{2} \leq \cdots \leq {\cal T}_{n}.$$ In here, ${\cal B}_{m}$ is an $m$-split Bose-Mesner algebra of $S$, and ${\cal T}_{m}$ is an $m$-split Terwilliger algebra of $S$ for $m = 1, \dots, n$. The chain ([\[eq:chain_1\]](#eq:chain_1){reference-type="ref" reference="eq:chain_1"}) allows us to combine an $l$-split generalized Delsarte's inequalities to an $m$-split generalized Delsarte's inequalities for $l \leq m$ by merging some partitions as the one. On the other hand, the chain ([\[eq:chain_2\]](#eq:chain_2){reference-type="ref" reference="eq:chain_2"}) allows us to add constraints in an $l$-split triple distances SDP to an $m$-split triple distances SDP for some $l \leq m$ without increasing the number of variables.
