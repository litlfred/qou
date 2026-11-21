---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-035-42-notations-for-categories
section_title: "Notations for categories"
section_number: 4.2
pages: 34-35
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.952
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#def:cat label="def:cat"}

In this subsection, we would like to collect all homological algebra notations, definitions and assumptions which will be frequently used below. Let $\mathcal{C}$ be an additive unital monoidal category with tensor product $\otimes$ and direct sum $\oplus$. The monoidal structure is not necessary symmetric. We will denote the unit object of $\mathcal{C}$ by $\mathbf{1}_{\mathcal{C}}$, or $\mathbf{1}$ if the category is clear from context. The endomorphism algebra $\mathrm{End}(\mathbf{1})$ is always commutative, and we assume that it is Noetherian. For any object $A\in \mathcal{C}$, the morphism space $\mathop{\mathrm{Hom}}(\mathbf{1},A)$ is a module over $\mathrm{End}(\mathbf{1})$, and we assume that it is finitely generated. We assume that all morphism spaces are positively graded. We denote by $K^b(\mathcal{C})$ the homotopy category of bounded complexes of objects in $\mathcal{C}$ and by $K^-(\mathcal{C})$ the homotopy category of bounded above complexes. Unless stated otherwise, we will work with bounded above complexes and abbreviate $K^-(\mathcal{C})$ to $K(\mathcal{C})$.

We will consider two types of "semi-infinite completions\" of the category $\mathcal{C}$. The first type is the homotopy category $K^{-}(\mathcal{C})$ of bounded above complexes of objects in $\mathcal{C}$ (which is well-known to also be a monoidal category). The other type is the category of certain infinite sums of objects in $\mathcal{C}$, as in the following definition.

::: definition
[]{#def:completion label="def:completion"}

Assume that $\mathcal{C}$ is graded, and the grading shift is denoted by $A \mapsto A(1)$. We define its **graded completion** $\mathcal{C}^{\uparrow}$ as follows. The objects are given by countable direct sums: $$\text{Ob}(\mathcal{C}^\uparrow) = \left\{ \bigoplus_{i=-\infty}^N A_i(i) \text{ for some }N \in \mathbb{Z}\right \}$$ and the morphisms $\phi: \oplus A_i(i)\rightarrow \oplus B_j(j)$ are collections of arrows $\{\phi_{ij}:A_i(i)\to B_j(j) \}$ for all $i,j$, such that for each $i$ there are only finitely many $j$ such that $\phi_{ij}\neq 0$.
:::

One can check that $\mathcal{C}^{\uparrow}$ and $K^{-}(\mathcal{C}^{\uparrow})$ inherit the tensor product from $\mathcal{C}$. Note that $K^{-}(\mathcal{C}^{\uparrow})$ is endowed with both the grading $(1)$ and the homological degree $[1]$.

Note that the category $\mathcal{C}$ may have multiple gradings, and the notion of completion depends on a specific choice of grading among these. For example, if $\mathcal{C}$ is graded by $\mathbb{Z}^r$, this accounts to choosing a one-dimensional direction in $\mathbb{Z}^r$. To clarify homological algebra over $\mathcal{C}^{\uparrow}$, we present some examples.

::: example
Let $\mathcal{C}$ be the category of graded finitely generated $\mathbb{C}[x]$-modules. Consider the following two-term complex in $K^{-}(\mathcal{C}^{\uparrow})$:

![](fig_7.png){#fig: model complex}

We can introduce an auxilary variable $y$ of degree $(-1)$ and rewrite the complex as following: $$\mathbb{C}[x,y] \xrightarrow{1+xy}   \mathbb{C}[x,y].$$ At first glance, one could think that since all horizontal arrows in Figure [1](#fig: model complex){reference-type="ref" reference="fig: model complex"} are isomorphisms, the complex is contractible. However, this is not the case, since a homotopy would be: $$\mathbb{C}[x,y]\xleftarrow{H}\mathbb{C}[x,y] \text{ such that } H(1+xy)=(1+xy)H=1$$ A natural choice for $H$ would be: $$H(x,y)=\frac{1}{1+xy}=1-xy+x^2y^2-x^3y^3+\ldots,$$ but this is not a valid morphism in $\mathcal{C}^{\uparrow}$ since there would be non-zero arrows from the top-most copy of $\mathbb{C}[x]$ to all infinitely many copies below it.
:::

::: remark
One can check that the homology of the complex in Figure [1](#fig: model complex){reference-type="ref" reference="fig: model complex"} is isomorphic to $\mathbb{C}[x,y]/(1+xy)=\mathbb{C}[x,x^{-1}]$.
:::
