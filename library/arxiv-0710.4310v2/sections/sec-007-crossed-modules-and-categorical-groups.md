---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-007-crossed-modules-and-categorical-groups
section_title: "Crossed modules and categorical groups"
section_number: null
pages: 11-12
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
[]{#CCG label="CCG"}

::: Definition
A categorical group $\mathcal{C}$ is a groupoid provided with a strict monoidal structure $\C \times \C \ra{\tn} \C$, as well as a "group inversion" functor ${^{-1}}\colon C  \to C$ such that both the set of objects $C_0$ of $\C$ and the set of morphisms $C_1$ of $\C$ are groups under the tensor product, and both the source and target maps $\sigma,\tau \colon C_1 \to C_0$ are group morphisms. A Lie categorical group is defined analogously by replacing groups by Lie groups and group morphisms by Lie group morphisms.
:::

See [@BM; @BL] for more details.

::: Definition
A morphism of categorical groups is given by a strict monoidal functor; see [@ML].
:::

It is well-known that the category of crossed modules and the category of categorical groups are equivalent; see for example [@BL; @BM; @BHS]. Let us explain how to define a categorical group $\C(\Gc)$ from a crossed module $\Gc$. This construction is an old one.

Let ${\Gc=(\d \colon E \to  G,\tr )}$ be a crossed module. The set of objects $C_0$ of $\C(\Gc)$ is given by all elements of $G$. The set of morphisms $C_1$ of $\C(\Gc)$ is given by the set of all pairs $(X,e)$ where $X \in G$ and $e \in E$. The source and the target of $(X,e) \in C_1$ are given by $\sigma(X,e)=X$ and $\tau(X,e)=\d(e)^{-1}X$, respectively. In other words, a morphism in $C(\Gc)$ "looks like" $X \ra{(X,e)} \d(e)^{-1} X$, which we will sometimes abbreviate as $X \ra{e} \d(e)^{-1} X$. Given $X \in G$ and $e,f \in E$ the composition $$X \ra{e} \d(e)^{-1}X  \ra{ f}   \d(f)^{-1}\d(e)^{-1} X$$ is $$X \ra{ef}  \d(ef)^{-1}X.$$

The tensor product has the form:

$$\label{Catmon}
\begin{CD}
\begin{CD}  \d(e)^{-1}X \\ @AA eA \\ X\\\end{CD} \tn \begin{CD}  \d(f)^{-1}Y \\ @AAfA \\ Y \end{CD}\quad  =\quad\begin{CD}\d(e)^{-1}X\d(f)^{-1}Y \\ @AA (X\tr f)e A \\ XY  \end{CD}
\end{CD},$$ where $X,Y \in G$ and $e,f \in E$. Therefore, the set of morphisms of $\C(\Gc)$ is a group under the tensor product. This group is isomorphic to the semidirect product $G \ltimes E$ of $G$ and $E$.

From the definition of a crossed module, it is easy to see that we have indeed defined a strict monoidal category which, furthermore, is a categorical group.

We will recall in [\[TCM\]](#TCM){reference-type="ref" reference="TCM"} how to define a crossed module from a categorical group.
