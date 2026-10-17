---
doc_id: arxiv-2507.12454v1
doc_title: "Cohomology rings of character varieties"
section_id: sec-002-3-setup
section_title: "Setup"
section_number: 3
pages: 8-9
source_pdf: 2507.12454v1.pdf
source_sha256: 156fd9080847b4e7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.929
doc_brief: "Cohomology rings of character varieties — In this talk I give an introduction and present some recent progress towards understanding the cohomology rings of character varieties of Riemann surfaces"
---
After reviewing in detail the basic example, we turn to the general setup and precise definitions. There is no reason to consider only genus $0$ surfaces, and the classical motivation directly extends to the more general case, for instance ODEs can be studied on complex curves of arbitrary genus.

::: definition
Fix $g\geq 0$, $n, k\geq 1$ and Jordan forms $J_1, J_2, \ldots, J_k \in\mathrm{GL}_n$. The associated genus $g$ *character variety* $X=\mathrm{Char}_{g;J_1,\dots,J_k}$ is the space $$\{(A_1,\ldots,A_g,B_1\ldots,B_g,M_1, \cdots, M_k): M_i\sim J_i,$$ $$A_1 B_1 A_1^{-1} B_1^{-1} \cdots A_g B_g A_g^{-1} B_g^{-1} M_1 \cdots M_k = I\}/\sim,$$ where $\sim$ identifies tuples of matrices which are conjugate with respect to the $\mathop{\mathrm{GL}}_n(\mathbb C)$ action.
:::

::: definition
[]{#def:generic label="def:generic"} The data $J_1,\ldots J_k$ are *generic* if

1.  $\prod_{i=1}^k \det J_i=1$

2.  $\prod_{i=1}^k \det J_i'\neq 1$ for any $0<n'<n$ and any block-decomposition $\left(\begin{array}{c|c} J_i' & J_i''\\ \hline 0 & J_i'''\end{array}\right)\sim J_i$ ($J_i'\in \mathrm{GL}_{n'}$).
:::

::: theorem
For generic data $n, k, J_1, \ldots, J_k$, the quotient space $X=\mathrm{Char}_{g;J_1,\dots,J_k}$ has the structure of a smooth affine algebraic variety.
:::

In fact, considering functions on $X$ of the form $$\mathop{\mathrm{tr}}(M_{i_1}\text{or} A_{i_1} \text{or} B_{i_1} \cdots M_{i_m}\text{or} A_{i_m} \text{or} B_{i_m})$$ we can realize $X$ as an algebraic subset of $\mathbb{C}^N$ for suffuciently large $N$.

Basically, the same reasoning as in the Fricke-Klein situation can be applied in general. However, the number of traces one needs to consider is uncontrollably large, and it seems hopeless to be able to produce all equations by the elimination computation. Even if we do obtain a complete list of equations, it is not clear which interesting information we should be able to extract from such a list. For instance, equations in the case of genus $0$, rank $2$, $5$ punctures are given in [@simpson2017explicit]. We do hope, however, that computing the cohomology ring is an achievable goal.

::: problem
Compute the cohomology ring $H^*(X,\mathbb{C})$.
:::
