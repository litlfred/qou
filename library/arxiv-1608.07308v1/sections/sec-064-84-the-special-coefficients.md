---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-064-84-the-special-coefficients
section_title: "The special coefficients"
section_number: 8.4
pages: 61-62
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 0.926
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:special label="sub:special"}

Note that the coefficients $x_i^i$ and $y_i^i$ in [\[eqn:chartx\]](#eqn:chartx){reference-type="eqref" reference="eqn:chartx"} and [\[eqn:charty\]](#eqn:charty){reference-type="eqref" reference="eqn:charty"} are precisely the eigenvalues of the matrices $(X,Y,v) \in \mathrm{FHilb}_n$. If we are in the case $* = \mathbb{C}$ or $* = \mathrm{point}$, then we must set $y_i^i = 0$ or $x_i^i = y_i^i = 0$ in [\[eqn:chartx\]](#eqn:chartx){reference-type="eqref" reference="eqn:chartx"} and [\[eqn:charty\]](#eqn:charty){reference-type="eqref" reference="eqn:charty"}, respectively.

::: definition
[]{#def:specialcoeffs label="def:specialcoeffs"}

The coefficients $x_i^j$ and $y_i^j$ which appear in [\[eqn:chartx\]](#eqn:chartx){reference-type="eqref" reference="eqn:chartx"} and [\[eqn:charty\]](#eqn:charty){reference-type="eqref" reference="eqn:charty"} will be called **special coefficients**. We also apply this terminology to the case when $k$ is an outer corner of the Young diagram of $T$, but in that case [\[eqn:chartx\]](#eqn:chartx){reference-type="eqref" reference="eqn:chartx"} and [\[eqn:charty\]](#eqn:charty){reference-type="eqref" reference="eqn:charty"} hold with $e_k = 0$.
:::

Note that the number of special coefficients corresponding to a standard Young tableau $T$ is: $$\label{eqn:numberofgens}
\sum_{i=1}^n \# \left( \text{of inner corners of the Young diagram consisting of the boxes labeled } 1,...,i \right)$$ Conjecture [\[conj:charts\]](#conj:charts){reference-type="ref" reference="conj:charts"} would suggest that the special coefficients generate the dg ring of functions $\mathring{\mathcal{A}}_T$ subject to a number of: $$\label{eqn:numberofrels}
\sum_{i=1}^n \# \left( \text{of outer corners of the Young diagram consisting of the boxes labeled } 1,...,i \right)$$ However, this is not true, because this would entail that all coefficients $x_i^j$ and $y_i^j$ could be written as polynomials in the special coefficients. We partially salvage this in the next Subsection, when we will show that the previous sentence holds if we replace the word "polynomials\" by "rational functions\". In other words, some open subset of $\mathrm{FHilb}_T$ can be described by [\[eqn:numberofgens\]](#eqn:numberofgens){reference-type="eqref" reference="eqn:numberofgens"} generators and [\[eqn:numberofrels\]](#eqn:numberofrels){reference-type="eqref" reference="eqn:numberofrels"} relations.

::: example
[]{#ex:symmetric label="ex:symmetric"} When $T= (n)$ and $* = \mathbb{C}$, only relations [\[eqn:chartx\]](#eqn:chartx){reference-type="eqref" reference="eqn:chartx"} come into play: $$Xe_i = e_{i+1} + x_i e_i$$ unless $i=1$, in which case we have: $$Y e_1 = \sum_{j=2}^n y_1^j e_j$$ Therefore, the special coefficients are $\{x_i, y_1^j\}^{1\leq i \leq n}_{2\leq j \leq n}$. The number of these coefficients is $2n-1$, and it matches [\[eqn:numberofgens\]](#eqn:numberofgens){reference-type="eqref" reference="eqn:numberofgens"} minus 1, where the minus one stems from the fact that $y_1^1 = 0$ for $* = \mathbb{C}$. The non-special coefficients are the $y_i^j$ with $i>1$, but they can be inferred from the special ones via the commutation relation $[X,Y]=0$, which in the case at hand reads: $$\label{eqn:above}
y^j_i (x_i-x_j) = y^j_{i+1} - y^{j-1}_i$$ for all $i<j$. Note that [\[eqn:above\]](#eqn:above){reference-type="eqref" reference="eqn:above"} is precisely [\[eqn:sym\]](#eqn:sym){reference-type="eqref" reference="eqn:sym"}. We make the convention that $y_i^j=0$ for $j\leq i$. After solving for $y^j_i$ in terms of $\{x_i, y_1^j\}$, we obtain the inductive formulas for any $\delta>0$: $$y_i^{i+\delta} = y_1^{\delta+1} + \sum_{s=1}^{i-1} y_{i-s}^{i-s+\delta+1} (x_{i-s}-x_{i-s+\delta+1})$$ The above relation also holds when $i+\delta=n+1$, in which case the left hand side is 0. We therefore obtain a relation among the special coefficients $\{x_i,y_1^j\}$ for all $\delta>0$. There are $n-1$ such relations, and their number matches [\[eqn:numberofrels\]](#eqn:numberofrels){reference-type="eqref" reference="eqn:numberofrels"} minus 1, where the minus one stems from the fact that $y_1^1 = 0$ for $* = \mathbb{C}$.
:::

::: example
[]{#ex:antisymmetric label="ex:antisymmetric"}

When $T= (1,...,1)$ and $* = \mathbb{C}$, only relations [\[eqn:charty\]](#eqn:charty){reference-type="eqref" reference="eqn:charty"} come into play: $$Ye_i = e_{i+1}$$ unless $i=1$, in which case we have: $$X e_1 = \sum_{j=1}^n x_1^j e_j$$ Therefore, the special coefficients are $x_1^j$ for all $j$. Note that the commutation relation $[X,Y]=0$ implies that: $$x_i^{j-1} = x_{i+1}^j \qquad \forall i<j$$ and therefore we conclude that $x_i^j = u_{j-i+1}$ for some variables $u_1,...,u_n$. Compare with [\[eqn:antisym\]](#eqn:antisym){reference-type="eqref" reference="eqn:antisym"}.
:::
