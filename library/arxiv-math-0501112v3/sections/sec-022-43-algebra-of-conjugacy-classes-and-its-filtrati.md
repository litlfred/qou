---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-022-43-algebra-of-conjugacy-classes-and-its-filtrati
section_title: "Algebra of conjugacy classes and its filtration"
section_number: 4.3
pages: 19-20
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.991
doc_brief: "arXiv:math/0501112v3 [math.CO] 31 May 2005 — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
[]{#subsec:algebraofconjugacy label="subsec:algebraofconjugacy"} Ivanov and Kerov [@IvanovKerov1999] defined a partial permutation of a set $X$ as a pair $\alpha=(d,w)$, where $d$ (called support of $\alpha$) is any subset of $X$ and $w:X\rightarrow X$ is a bijection which equal to identity outside of $d$. The usual product of partial permutations is given by $$(d_1,w_1)(d_2,w_2)=(d_1\cup d_2,w_1 w_2)$$ and their disjoint product $\bullet$ was defined in [\[eq:definition-of-disjoint\]](#eq:definition-of-disjoint){reference-type="eqref" reference="eq:definition-of-disjoint"}. Partial permutations behave like the usual permutations (to a partial permutation we can canonically associate the usual permutation $w$) except that we can distinguish two kinds of fix-points $x$ for a partial permutations: true fix-points (i.e. $x\notin d$) and cycles of length one ($x\in d$, $w(x)=x$). Partial permutations form a semigroup; in this article we are interested also in the corresponding semigroup algebra which should be regarded as an analogue of the permutation group algebra ${\mathbb{C}}(S_q)$ equipped with some additional structure.

In fact, to define correctly the notion of the disjoint product $\bullet$ from Section [\[subsec:disjoint\]](#subsec:disjoint){reference-type="ref" reference="subsec:disjoint"} we must use the semigroup algebra corresponding to partial permutations and not the group algebra ${\mathbb{C}}(S_q)$. The reason for this is that we must distinguish two kinds of fix-points since, for example, $\Sigma_{1,1}$ and $\Sigma_1$ represent multiples of each other in ${\mathbb{C}}(S_q)$, but the disjoint product treats them differently.

One can show [@IvanovKerov1999; @SniadyGaussianFluctuationsAndGenus] that the family of normalized conjugacy classes $(\Sigma_{k_1,\dots,k_n})$ and the family of free cumulants $(R_i)$ generate the same filtered algebra, called algebra of conjugacy classes, when for the degrees of the generators we take $$\deg \Sigma_{k_1,\dots,k_n}=(k_1+1)+\cdots+(k_n+1),$$ $$\deg R_i=i.$$ The above statement holds true both when as the product we take the usual product of partial permutations (in this case we denote the resulting algebra by ${\mathfrak{A}}$) and when as the product we take the disjoint product (in this case we denote the resulting algebra by ${\mathfrak{A}}^{\bullet}$).

One can also show [@IvanovKerov1999; @SniadyGaussianFluctuationsAndGenus] that in the scaling considered in this article (i.e. a typical Young diagram has at most $O(\sqrt{q})$ rows and columns) so defined degree determines the asymptotic behavior of an element, namely $${\mathbb{E}}X = O\big( q^{\frac{\deg X}{2}}\big)$$ for any element $X$ of this algebra. Furthermore, the generators fulfill $$\label{eq:wolnekumulantyiklasy} R_i= \Sigma_{i-1} + \text{(terms of
degree at most $i-2$)}.$$
