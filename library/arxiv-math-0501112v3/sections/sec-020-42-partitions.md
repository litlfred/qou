---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-020-42-partitions
section_title: "Partitions"
section_number: 4.2
pages: 18-20
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.97
---
[]{#subsec:partitions label="subsec:partitions"} We recall that $\pi=\{\pi_1,\dots,\pi_r\}$ is a partition of a finite ordered set $X$ if sets $\pi_1,\dots,\pi_r$ are nonempty and disjoint and if $\pi_1\cup\cdots\cup\pi_r=X$.

We say that a partition $\pi$ is smaller (or finer) than a partition $\rho$ of the same set if every block of $\pi$ is a subset of some block of $\rho$ and we denote it by $\pi\leq\rho$. For partitions $\pi_1,\pi_2$ of the same set we denote by $\pi_1\vee \pi_2$ the minimal partition which is greater or equal than both $\pi_1$ and $\pi_2$. The set of all partitions of some given set $X$ has a maximal element, namely the partition with only one block equal to $X$.

## Algebra of conjugacy classes and its filtration {#subsec:algebraofconjugacy}

Ivanov and Kerov [@IvanovKerov1999] defined a partial permutation of a set $X$ as a pair $\alpha=(d,w)$, where $d$ (called support of $\alpha$) is any subset of $X$ and $w:X\rightarrow X$ is a bijection which equal to identity outside of $d$. The usual product of partial permutations is given by $$(d_1,w_1)(d_2,w_2)=(d_1\cup d_2,w_1 w_2)$$ and their disjoint product $\bullet$ was defined in [\[eq:definition-of-disjoint\]](#eq:definition-of-disjoint){reference-type="eqref" reference="eq:definition-of-disjoint"}. Partial permutations behave like the usual permutations (to a partial permutation we can canonically associate the usual permutation $w$) except that we can distinguish two kinds of fix-points $x$ for a partial permutations: true fix-points (i.e. $x\notin d$) and cycles of length one ($x\in d$, $w(x)=x$). Partial permutations form a semigroup; in this article we are interested also in the corresponding semigroup algebra which should be regarded as an analogue of the permutation group algebra ${\mathbb{C}}(S_q)$ equipped with some additional structure.

In fact, to define correctly the notion of the disjoint product $\bullet$ from Section [\[subsec:disjoint\]](#subsec:disjoint){reference-type="ref" reference="subsec:disjoint"} we must use the semigroup algebra corresponding to partial permutations and not the group algebra ${\mathbb{C}}(S_q)$. The reason for this is that we must distinguish two kinds of fix-points since, for example, $\Sigma_{1,1}$ and $\Sigma_1$ represent multiples of each other in ${\mathbb{C}}(S_q)$, but the disjoint product treats them differently.

One can show [@IvanovKerov1999; @SniadyGaussianFluctuationsAndGenus] that the family of normalized conjugacy classes $(\Sigma_{k_1,\dots,k_n})$ and the family of free cumulants $(R_i)$ generate the same filtered algebra, called algebra of conjugacy classes, when for the degrees of the generators we take $$\deg \Sigma_{k_1,\dots,k_n}=(k_1+1)+\cdots+(k_n+1),$$ $$\deg R_i=i.$$ The above statement holds true both when as the product we take the usual product of partial permutations (in this case we denote the resulting algebra by ${\mathfrak{A}}$) and when as the product we take the disjoint product (in this case we denote the resulting algebra by ${\mathfrak{A}}^{\bullet}$).

One can also show [@IvanovKerov1999; @SniadyGaussianFluctuationsAndGenus] that in the scaling considered in this article (i.e. a typical Young diagram has at most $O(\sqrt{q})$ rows and columns) so defined degree determines the asymptotic behavior of an element, namely $${\mathbb{E}}X = O\big( q^{\frac{\deg X}{2}}\big)$$ for any element $X$ of this algebra. Furthermore, the generators fulfill $$\label{eq:wolnekumulantyiklasy} R_i= \Sigma_{i-1} + \text{(terms of
degree at most $i-2$)}.$$
