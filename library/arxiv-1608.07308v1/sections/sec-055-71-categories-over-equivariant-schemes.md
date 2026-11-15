---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-055-71-categories-over-equivariant-schemes
section_title: "Categories over equivariant schemes"
section_number: 7.1
pages: 52-53
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 0.898
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:equivcategories label="sub:equivcategories"}

We will now enhance the setup of Section [\[sec:geometry\]](#sec:geometry){reference-type="ref" reference="sec:geometry"} to schemes endowed with a torus action $T \curvearrowright X$.

::: definition
[]{#def:equivariantcategory label="def:equivariantcategory"}

A $T$--equivariant category $\mathcal{C}$ is one which the Hom spaces are representations of $T$. If the category is monoidal, we require the tensor product to preserve the $T$ action.
:::

::: definition
[]{#def:equivariant label="def:equivariant"}

Given a $T$--equivariant category $\mathcal{C}$, we will say that a map $\iota:\mathcal{C}\rightarrow X$ is $T$--equivariant if the defining functors: $$\mathcal{C}\xtofrom[\iota^*]{\iota_*} \mathrm{Coh}_T(X)$$ preserve the action of $T$ on all $\mathop{\mathrm{Hom}}$ spaces. The derived version is defined analogously.
:::

::: example
[]{#ex:equivspec label="ex:equivspec"} Suppose that $X = \mathrm{Spec}\ A$ with $A$ being a $T$--graded ring. Recall from Subsection [\[sub:aff\]](#sub:aff){reference-type="ref" reference="sub:aff"} that realizing $\mathcal{C}$ as a category over $X$ amounts to giving a ring homomorphism: $$A \stackrel{f}\longrightarrow \mathrm{End}_\mathcal{C}(\mathbf{1})$$ It is easy to see that $\mathcal{C}\rightarrow X$ is $T$--equivariant if and only if $f$ is $T$--equivariant.
:::

::: example
[]{#ex:equivproj label="ex:equivproj"}

Going one step further, suppose $A$ is a $T$--graded ring. Define: $$X = \mathbb{P}_A^n$$ where the $n+1$ coordinate directions of the projective spaces have $T$--equivariant characters $\lambda_0,...,\lambda_n$. As in Example [\[ex:projective\]](#ex:projective){reference-type="ref" reference="ex:projective"}, the map $\mathcal{C}\stackrel{\iota}\longrightarrow X$ is the same datum as a ring homomorphism: $$A \stackrel{f}\longrightarrow \mathrm{End}_\mathcal{C}(\mathbf{1})$$ together with an object $F \in K^b(\mathcal{C})$ and $n+1$ arrows: $$\left[ \lambda_0 \cdot \mathbf{1} \stackrel{\alpha_0}\longrightarrow F \right], ..., \left[ \lambda_n \cdot \mathbf{1} \stackrel{\alpha_n}\longrightarrow F \right]$$ whose tensor product is homotopic to 0. Then $\iota$ is $T$--equivariant if the homomorphism $f$ is $T$--equivariant, and moreover the arrows $\alpha_i, i\in \{0,...,n\}$ are all homogeneous with respect to the structure of $T$--modules of the vector spaces $\mathop{\mathrm{Hom}}_{K^b(\mathcal{C})}(\lambda_i \cdot \mathbf{1}, F)$.
:::

::: example
[]{#ex:equivrelative label="ex:equivrelative"}

Finally, let us treat the relative case of Subsection [\[sub:relative\]](#sub:relative){reference-type="ref" reference="sub:relative"}. Suppose we have a $T$--equivariant map: $\mathcal{C}\stackrel{\iota}\longrightarrow X$ and we wish to upgrade it to a $T$--equivariant map: $$\mathcal{C}\stackrel{\iota'}\longrightarrow \mathbb{P}\mathcal{V}^{\vee}$$ where $\mathcal{V}$ is a $T$--equivariant vector bundle on $X$. As we saw in Subsection [\[sub:relative\]](#sub:relative){reference-type="ref" reference="sub:relative"}, the existence of the map $\iota'$ is equivalent to the choice of an object $F \in \mathcal{C}$ together with an arrow: $$\iota^* \mathcal{V}\stackrel{\alpha}\longrightarrow F$$ in $\mathcal{C}$, whose Koszul complex is quasi-isomorphic to 0. It is easy to see that the map $\iota'$ is $T$--equivariant if and only if the map $\alpha$ is $T$--equivariant. The same picture applies when $\mathcal{V}$ is replaced by a coherent sheaf $\mathcal{Q}$ of homological dimension 1, as in Subsection [\[sub:one\]](#sub:one){reference-type="ref" reference="sub:one"}.
:::
