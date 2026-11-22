---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-007-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 5-5
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.903
latex_coverage_ratio: 1.0
doc_brief: "arXiv:math/0501112v3 [math.CO] 31 May 2005 — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
[]{#sec:preliminaries label="sec:preliminaries"}

## Normalized conjugacy class indicators {#subsec:definicjasigma}

Let integer numbers $k_1,\dots,k_m\geq 1$ be given. We define the normalized conjugacy class indicator to be a central element in the group algebra ${\mathbb{C}}(S_q)$ given by

[@KerovOlshanski1994; @BianeCharacters; @Sniady2003pushing]

$$\label{eq:definicjasigma} \Sigma_{k_1,\dots,k_m}=

\sum_{a} (a_{1,1},a_{1,2},\dots,a_{1,{k_1}}) \cdots
(a_{m,1},a_{m,2},\dots,a_{m,k_m}),$$

where the sum runs over all one--to--one functions $$a:\big\{ \{r,s\}: 1\leq r\leq m, 1\leq s\leq {k_r}\big\}\rightarrow \{1,\dots,q\}$$ and $(a_{1,1},a_{1,2},\dots,a_{1,{k_1}}) \cdots
(a_{m,1},a_{m,2},\dots,a_{m,k_m})$ denotes the product of disjoint cycles. Of course, if $q<k_1+\cdots+k_m$ then the above sum runs over the empty set and $\Sigma_{k_1,\dots,k_m}=0$.

In other words, we consider a Young diagram with the rows of the lengths $k_1,\dots,k_m$ and all ways of filling it with the elements of the set $\{1,\dots,q\}$ in such a way that no element appears more than once. Each such a filling can be interpreted as a permutation when we treat the rows of the Young tableau as disjoint cycles.

It follows that $\Sigma_{k_1,\dots,k_m}$ is a linear combination of permutations which in the cycle decomposition have cycles of length $k_1,\dots,k_m$ (and, additionally, $q-(k_1+\cdots+k_m)$ fix-points). Each such a permutation appears in $\Sigma_{k_1,\dots,k_m}$ with some positive integer multiplicity depending on the symmetry of the tuple $k_1,\dots,k_m$.
