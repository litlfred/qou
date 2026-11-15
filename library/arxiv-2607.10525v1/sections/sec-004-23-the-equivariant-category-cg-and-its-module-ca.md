---
doc_id: arxiv-2607.10525v1
doc_title: "Fiber Functors of Equivariantizations of Finite Tensor Categories"
section_id: sec-004-23-the-equivariant-category-cg-and-its-module-ca
section_title: "The equivariant category CG and its module categories"
section_number: 2.3
pages: 7-9
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.964
doc_brief: "Fiber Functors of Equivariantizations of Finite Tensor Categories — Let G be a finite group acting on a finite tensor category C."
---
Given a $G$-action on a tensor category $\mathcal{C}$, one forms the *equivariant category* $\mathcal{C}^G$.

Its objects are pairs $(X, u)$ where $X \in \mathcal{C}$ and $u = \{u_g: g_*(X) \to X\}_{g \in G}$ is a collection of isomorphisms satisfying $u_{gh} = u_g \circ g_*(u_h)$ for all $g, h \in G$ and $u_e = \operatorname{id}_X$. The tensor product is $(X, u) \otimes (Y, v) = (X \otimes Y, w)$, where $w_g = u_g \otimes v_g$, and the unit object is $(\mathbf{1}, \operatorname{id}_{\mathbf{1}})$.

By [@EGNO15 Section 4.15 and Example 7.12.25], if $\mathcal{C}$ is a finite tensor category with a $G$-action, then $\mathcal{C}^G$ is also a finite tensor category.

Let $H \subseteq G$ be a subgroup, and let $\mathcal{M}$ be an $H$-equivariant $\mathcal{C}$-module category with structure $\rho: \underline{H} \to \operatorname{Aut}_{\mathcal{C}}^{H}(\mathcal{M})$. Forgetting the module functor structures, the functors $U_h$ define an action of $H$ on the underlying abelian category $\mathcal{M}$. One can therefore form the equivariant category $\mathcal{M}^H$, and the tensor category $\mathcal{C}^G$ acts on it.

The category $\mathcal{M}^H$ is defined analogously to $\mathcal{C}^G$: objects are pairs $(M, v)$ where $M \in \mathcal{M}$ and $v = \{v_h: U_h(M) \to M\}_{h \in H}$ satisfy $v_e=\operatorname{id}_M$ and the equivariance condition $v_{h_1h_2} \circ (\mu_{h_1,h_2})_M = v_{h_1} \circ U_{h_1}(v_{h_2})$ for all $h_1,h_2 \in H$. Morphisms are defined similarly to preserve the equivariant structure.

It follows from [@GM11 Lemma 3.3] that $\mathcal{M}^H$ is a left $\mathcal{C}^G$-module category. The action of $(X,u) \in \mathcal{C}^G$ on $(M,v) \in \mathcal{M}^H$ is given by $(X,u) \overline{\otimes} (M,v) = (X \overline{\otimes} M, \widetilde{v})$, where $\widetilde{v}_h = (u_h \overline{\otimes} v_h) \circ c^h_{X,M}$ for $h \in H$.

We use the following description of exact module categories over equivariantizations, due to Galindo--Mombelli [@GM11 Proposition 3.4].

::: proposition
[]{#prop:mod_cat_equivariantization label="prop:mod_cat_equivariantization"} Let $G$ be a finite group acting on a finite tensor category $\mathcal{C}$. Then the following hold.

1.  If $\mathcal{M}$ is an $H$-equivariant $\mathcal{C}$-module category, then $\mathcal{M}^H$ is an exact $\mathcal{C}^G$-module category if and only if $\mathcal{M}$ is an exact $\mathcal{C}$-module category.

2.  If $\mathcal{N}$ is an indecomposable exact module category over $\mathcal{C}^G$, then there exists a subgroup $H \subseteq G$ and an $H$-equivariant $\mathcal{C}$-module category $\mathcal{M}$, whose underlying $\mathcal{C}$-module category is indecomposable and exact, such that $\mathcal{N}\simeq \mathcal{M}^H$.
:::

### Equivalence classes of equivariant module categories

We record when two equivariant $\mathcal{C}$-module categories produce equivalent $\mathcal{C}^G$-module categories.

Let $L\subseteq G$, and let $\mathcal{M}$ and $\mathcal{N}$ be two $L$-equivariant $\mathcal{C}$-module categories, with structure functors $U_\ell$ and $U'_\ell$, respectively. Recall that an $L$-equivariant equivalence is a $\mathcal{C}$-module functor $F:\mathcal{M}\to \mathcal{N}$ together with module natural isomorphisms $w^\ell: U'_\ell\circ F\to F\circ U_\ell$ satisfying the coherence condition $$w^{\ell m}_M\circ(\mu'_{\ell,m})_{F(M)}
=F((\mu_{\ell,m})_M)\circ w^\ell_{U_m(M)}\circ U'_\ell(w^m_M)$$ for all $\ell,m\in L$ and $M\in \mathcal{M}$. In the strict case this reduces to the usual formula $w^{\ell m}_M=w^\ell_{U_m(M)}\circ U'_\ell(w^m_M)$. This convention is compatible with the correspondence between $L$-equivariant $\mathcal{C}$-module categories and $(\mathcal{C}\rtimes L)$-module categories.

For $g\in G$, the rule $$\operatorname{Ad}_g([V,h])=[g_*(V),ghg^{-1}]$$ defines a tensor autoequivalence of $\mathcal{C}\rtimes G$ and restricts to $\mathcal{C}\rtimes K\simeq\mathcal{C}\rtimes gKg^{-1}$. If $\mathcal{N}$ is a $K$-equivariant $\mathcal{C}$-module category and $H=gKg^{-1}$, let ${}^g\mathcal{N}$ be the $H$-equivariant module category obtained by pulling the corresponding $(\mathcal{C}\rtimes K)$-module structure back along $\operatorname{Ad}_{g^{-1}}$. On the underlying category, $$V\bullet^g N=(g^{-1})_*(V)\triangleright N,
\qquad
U'_h=U_{g^{-1}hg},$$ with module constraints and coherence maps transported from those of $\mathcal{N}$.

::: definition
[]{#def:conjugate_equivariant_module_categories label="def:conjugate_equivariant_module_categories"} Two pairs $(H,\mathcal{M})$ and $(K,\mathcal{N})$, where $\mathcal{M}$ is an $H$-equivariant $\mathcal{C}$-module category and $\mathcal{N}$ is a $K$-equivariant $\mathcal{C}$-module category, are called *conjugate* if there exists $g \in G$ such that

1.  $H = gKg^{-1}$, and

2.  $\mathcal{M}$ is equivalent to ${}^g\mathcal{N}$ as $H$-equivariant $\mathcal{C}$-module categories.
:::

The equivalence relation among these equivariantized module categories is the following.

::: theorem
[]{#thm:conjugacy_equivariantization label="thm:conjugacy_equivariantization"} Let $G$ be a finite group acting on a finite tensor category $\mathcal{C}$. Let $H,K \subseteq G$ be subgroups. Let $\mathcal{M}$ be an $H$-equivariant $\mathcal{C}$-module category and let $\mathcal{N}$ be a $K$-equivariant $\mathcal{C}$-module category. Assume that the underlying $\mathcal{C}$-module categories of $\mathcal{M}$ and $\mathcal{N}$ are indecomposable and exact. Then the equivariantizations $\mathcal{M}^H$ and $\mathcal{N}^K$ are equivalent as $\mathcal{C}^G$-module categories if and only if $(H,\mathcal{M})$ and $(K,\mathcal{N})$ are conjugate.
:::

::: proof
*Proof.* Let $\mathcal{D}=\mathcal{C}\rtimes G$, with its canonical faithful $G$-grading, and use $\mathcal{D}_S$ for the sum of the homogeneous components indexed by a subset $S\subseteq G$. The $H$- and $K$-equivariant structures make $\mathcal{M}$ and $\mathcal{N}$ into $\mathcal{D}_H$- and $\mathcal{D}_K$-module categories. By [@GM11 Proposition 3.4(1)], they are indecomposable exact as $\mathcal{D}_H$- and $\mathcal{D}_K$-module categories, respectively. Their restrictions to the neutral component $\mathcal{D}_e=\mathcal{C}$ are the original indecomposable $\mathcal{C}$-module categories. Hence $(H,\mathcal{M})$ and $(K,\mathcal{N})$ are type-1 pairs in the terminology of [@MM20 Subsection 5.1].

By [@GM11 Proposition 3.4(3)] and the argument proving [@GM11 Proposition 3.4(5)] via Tambara's correspondence [@T01 Theorem 4.1], the categories $\mathcal{M}^H$ and $\mathcal{N}^K$ are equivalent as $\mathcal{C}^G$-module categories if and only if the induced $\mathcal{D}$-module categories $$\begin{aligned}
\mathop{\mathrm{Ind}}_{\mathcal{D}_H}^{\mathcal{D}}(\mathcal{M}) &:=
\mathcal{D}\boxtimes_{\mathcal{D}_H}\mathcal{M}, \\
\mathop{\mathrm{Ind}}_{\mathcal{D}_K}^{\mathcal{D}}(\mathcal{N}) &:=
\mathcal{D}\boxtimes_{\mathcal{D}_K}\mathcal{N}
\end{aligned}$$ are equivalent.

By [@MM20 Definition 5.10 and Proposition 5.12], applied to the $G$-graded tensor category $\mathcal{D}$, these induced module categories are equivalent if and only if there exists $g\in G$ such that:

1.  $H = gKg^{-1}$, and

2.  $\mathcal{D}_{gK}\boxtimes_{\mathcal{D}_K}\mathcal{N}\simeq \mathcal{M}$ as $\mathcal{D}_H$-module categories.

The functor $$\Phi_g:\mathcal{D}_{gK}\longrightarrow\mathcal{D}_K,
\qquad
[V,gk]\longmapsto[(g^{-1})_*(V),k],$$ induced by left tensoring with $[\mathbf{1},g^{-1}]$, is an equivalence of $(\mathcal{D}_H,\mathcal{D}_K)$-bimodule categories, where the left $\mathcal{D}_H$-action on $\mathcal{D}_K$ is transported along $\operatorname{Ad}_{g^{-1}}:\mathcal{D}_H\to\mathcal{D}_K$. Consequently, the relative tensor product is $\mathcal{N}$ with its $\mathcal{D}_H$-action pulled back along $\operatorname{Ad}_{g^{-1}}$, and hence $$\mathcal{D}_{gK}\boxtimes_{\mathcal{D}_K}\mathcal{N}\simeq{}^g\mathcal{N}$$ as $\mathcal{D}_H$-module categories. By construction, the right-hand side is precisely the $H$-equivariant $\mathcal{C}$-module category introduced above. Thus, by [@MM20 Def. 5.10, Prop. 5.12], this equivalence relation is precisely the conjugacy condition above. ◻
:::
