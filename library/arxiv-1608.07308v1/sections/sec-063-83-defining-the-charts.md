---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-063-83-defining-the-charts
section_title: "Defining the charts"
section_number: 8.3
pages: 59-61
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.893
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:defcharts label="sub:defcharts"}

In this Section, we will define affine charts on the flag Hilbert scheme which only satisfy Conjecture [\[conj:charts\]](#conj:charts){reference-type="ref" reference="conj:charts"} on the local rings around the fixed points. $\mathrm{FHilb}_n$ will henceforth refer to either of $\mathrm{FHilb}_n(*)$ for $* \in \{\mathbb{C}^2,\mathbb{C},\mathrm{point}\}$.

::: definition
[]{#def:chart label="def:chart"}

For any point $(X,Y,v) \in \mathrm{FHilb}_n$ and standard Young tableau $T$, consider the following algorithm to construct a basis $e_1 = v, e_2,...,e_n$ of $\mathbb{C}^n$. Suppose $e_1,...,e_{k-1}$ have been constructed and the $k$-th box looks as in the following picture:

::: picture
(100,90)(-170,-5) []{#pic:1 label="pic:1"}

(15,57)$i$ (57,17)$i'$ (53,57)$k$ (0,0)(1,0)80 (0,40)(1,0)80 (0,80)(1,0)80 (0,0)(0,1)80 (40,0)(0,1)80 (80,0)(0,1)80
:::

Define the vector $e_k \in \text{Ker}(\mathbb{C}^n \twoheadrightarrow \mathbb{C}^{k-1})$ by the following formula if $i>i'$: $$\label{eqn:chartx}
X e_{i} = e_k + \sum_{j=i}^{k-1} x^j_i e_j$$ where $x^j_i$ are coefficients, and by the following formula if $i<i'$: $$\label{eqn:charty}
Y e_{i'} = e_k + \sum_{j={i'}}^{k-1} y^j_{i'} e_j$$ where $y^j_{i'}$ are coefficients. If the process terminates after having constructed $e_n$, in a way such that $e_1,...,e_k$ form a basis of the quotient $\mathbb{C}^n \twoheadrightarrow \mathbb{C}^k$ for all $k$, then we set: $$(X,Y,v) \in \mathrm{FHilb}_T$$
:::

In either [\[eqn:chartx\]](#eqn:chartx){reference-type="eqref" reference="eqn:chartx"} or [\[eqn:charty\]](#eqn:charty){reference-type="eqref" reference="eqn:charty"}, it is clear that the vector $e_k$ is unique, since the coefficients $x_i^j$ or $y_i^j$ are uniquely determined by the fact that $e_k$ vanishes in the quotient $\mathbb{C}^n \twoheadrightarrow \mathbb{C}^{k-1}$. The fact that such an $e_k$ exists at each step, and that the resulting collection of vectors forms a basis, is an open condition and therefore: $$\mathrm{FHilb}_T \subset \mathrm{FHilb}_n$$ thus defined is an open subscheme. It is also an affine subscheme, simply because the basis $e_1,...,e_n$ is unique. We could therefore define $\mathrm{FHilb}_T$ alternatively as the affine space of matrices $X,Y$ of the form prescribed by [\[eqn:chartx\]](#eqn:chartx){reference-type="eqref" reference="eqn:chartx"} and [\[eqn:charty\]](#eqn:charty){reference-type="eqref" reference="eqn:charty"} in a fixed basis. It is also clear that the locus $\mathrm{FHilb}_T$ is $\mathbb{C}^{*} \times \mathbb{C}^*$ invariant and that the only fixed point it contains is: $$I_T = \left\{\mathbb{C}^n = \bigoplus_{i=1}^n \mathbb{C}\cdot e_i \quad \text{with} \quad  X\cdot e_i = e_{i \rightarrow}, \ Y\cdot e_i = e_{i\uparrow}, \ v = e_1 \right\}$$ In the above formula, for any box $i \in T$ we write $i \rightarrow$ and $i \uparrow$ for the boxes immediately right and above $\square$, respectively. If there is no box to the right or up of $\square$, we naturally set $e_{i \rightarrow}$ or $e_{i\uparrow}$ equal to 0. The fact that the open sets of Definition [\[def:chart\]](#def:chart){reference-type="ref" reference="def:chart"} cover the whole of $\mathrm{FHilb}_n$ follows from the following principle: $$\label{eqn:principletorus}
\textbf{any open torus invariant property which holds}$$ $$\textbf{near the fixed points of }\mathrm{FHilb}_n \textbf{ holds everywhere}$$ This is because the set of points which do not enjoy said property is closed, torus invariant and contains no fixed points: any such set must be empty. One must be careful here, because the argument is a priori only true for projective varieties, such as $\mathrm{FHilb}_n(\mathrm{point})$. However, it also applies to $\mathrm{FHilb}_n(\mathbb{C})$ and $\mathrm{FHilb}_n(\mathbb{C}^2)$ because the torus $\mathbb{C}^{*} \times \mathbb{C}^*$ contracts the affine directions $\mathbb{C}$ and $\mathbb{C}^2$ to the origin.
