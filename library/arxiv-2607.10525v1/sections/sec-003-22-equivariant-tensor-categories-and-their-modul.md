---
doc_id: arxiv-2607.10525v1
doc_title: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES"
section_id: sec-003-22-equivariant-tensor-categories-and-their-modul
section_title: "Equivariant tensor categories and their module categories"
section_number: 2.2
pages: 4-9
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
doc_brief: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES — LetGbe a finite group acting on a finite tensor categoryC."
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.675
---
### Group actions on tensor categories

Let $\underline G$ be the strict monoidal category associated with a group $G$. An action of $G$ on a tensor category $\mathcal{C}$ is a monoidal functor $$\underline G\longrightarrow \underline{\operatorname{Aut}_{\otimes}(\mathcal{C})}.$$ By the coherence theorem for tensor categories with $G$-action [@Gal17 Theorem 2.4], we may and do assume that the $G$-action is strict. We write $g_*$ for the tensor autoequivalence attached to $g$, so that $g_*h_*=(gh)_*$ and $e_*=\operatorname{id}_{\mathcal{C}}$. Equivariant module categories will not be strictified; their coherence maps are retained below.

### The semidirect product

For a tensor category $\mathcal{C}$ with a strict $G$-action, the *semidirect product* $\mathcal{C}\rtimes G$ is the monoidal category $$\mathcal{C}\rtimes G=\bigoplus_{g\in G}\mathcal{C}_g,$$ where each homogeneous component $\mathcal{C}_g$ is a copy of $\mathcal{C}$ [@T01; @Nik08]. We write $[X,g]$ for the object $X\in\mathcal{C}$ placed in degree $g$. The tensor product and unit are $$\label{eq:semidirect_product_tensor}
[X,g]\otimes[Y,h]=[X\otimes g_*(Y),gh],
\qquad
\mathbf 1_{\mathcal{C}\rtimes G}=[\mathbf 1,e],$$ with associativity and unit constraints induced from those of $\mathcal{C}$. When $G$ is finite, $\mathcal{C}\rtimes G$ is a finite tensor category. For an arbitrary subset $S\subseteq G$, we use the notation $$(\mathcal{C}\rtimes G)_S:=\bigoplus_{s\in S}\mathcal{C}_s.$$ If $S$ is a subgroup, this is the tensor subcategory $\mathcal{C}\rtimes S$. If $S=gK$ is a left coset, then $(\mathcal{C}\rtimes G)_{gK}$ is naturally a $((\mathcal{C}\rtimes G)_{gKg^{-1}},\mathcal{C}\rtimes K)$-bimodule category under tensor product. This notation will also be used for arbitrary faithfully graded tensor categories.

### $H$-equivariant module categories

We follow [@Gal11; @ENO11] for equivariant module categories and their use in constructing module categories over equivariantizations.

Let $H \subseteq G$ be a subgroup acting on a finite tensor category $\mathcal{C}$. Given a $\mathcal{C}$-module category $\mathcal{M}$, we *twist* the module structure by any element $g\in H$.

For each $g\in H$, let $\mathcal{M}^g$ be the category with the same underlying abelian category as $\mathcal{M}$ and with $\mathcal{C}$-action $$X\overline{\otimes}^{\,g}M:=g_*(X)\overline{\otimes}M.$$ The associativity and unit constraints are those induced from the module structure of $\mathcal{M}$ and the tensor structure of $g_*$. Since the action on $\mathcal{C}$ is strict, $(\mathcal{M}^g)^h=\mathcal{M}^{gh}$ as $\mathcal{C}$-module categories.

We now make explicit the monoidal category that records twisted module autoequivalences. Let $\operatorname{Aut}_{\mathcal{C}}^{H}(\mathcal{M})$ be the groupoid whose objects are pairs $(g,F)$, where $g\in H$ and $$(F,c^F):\mathcal{M}\longrightarrow\mathcal{M}^g$$ is a $\mathcal{C}$-module equivalence. There are no morphisms between objects of different degrees, and morphisms in degree $g$ are $\mathcal{C}$-module natural isomorphisms. If $(g,F)$ and $(h,E)$ are objects, define $$(g,F)\otimes(h,E):=(gh,F\circ E),$$ where the $\mathcal{C}$-module constraint on the composite is $$\label{eq:twisted_composite_constraint}
\begin{aligned}
c^{F\circ E}_{X,M}:F(E(X\overline\otimes M))
&\xrightarrow{\ F(c^E_{X,M})\ }
F(h_*(X)\overline\otimes E(M))\\
&\xrightarrow{\ c^F_{h_*(X),E(M)}\ }
(gh)_*(X)\overline\otimes F(E(M)).
\end{aligned}$$ With the usual horizontal product of module natural isomorphisms, composition makes this a strict monoidal groupoid with unit $(e,\operatorname{id}_{\mathcal{M}})$. The degree map $$\pi_1:\operatorname{Aut}_{\mathcal{C}}^{H}(\mathcal{M})\longrightarrow\underline H,
\qquad
(g,F)\longmapsto g,$$ is a strict monoidal functor.

An *$H$-equivariant $\mathcal{C}$-module category* is a $\mathcal{C}$-module category $\mathcal{M}$ together with a strong monoidal section $$\rho:\underline H\longrightarrow\operatorname{Aut}_{\mathcal{C}}^{H}(\mathcal{M}),
\qquad
\pi_1\circ\rho=\operatorname{id}_{\underline H}.$$ We work with normalized sections. Explicitly, the data consist of $\mathcal{C}$-module equivalences $$(U_h,c^h):\mathcal{M}\longrightarrow\mathcal{M}^h,
\qquad h\in H,$$ and module natural isomorphisms $$\mu_{g,h}:U_gU_h\xrightarrow{\sim}U_{gh}$$ such that $$\label{eq:equivariant_module_pentagon}
(\mu_{gh,k})_M\circ(\mu_{g,h})_{U_k(M)}
=(\mu_{g,hk})_M\circ U_g((\mu_{h,k})_M)$$ for all $g,h,k\in H$ and $M\in\mathcal{M}$, and such that each $\mu_{g,h}$ is a module natural transformation, equivalently $$\label{eq:equivariant_module_compatibility}
\begin{aligned}
&(\operatorname{id}_{(gh)_*(X)}\overline\otimes(\mu_{g,h})_M)
\circ c^g_{h_*(X),U_h(M)}\circ U_g(c^h_{X,M})\\
&\hspace{4cm}=
 c^{gh}_{X,M}\circ(\mu_{g,h})_{X\overline\otimes M}
\end{aligned}$$ for all $X\in\mathcal{C}$ and $M\in\mathcal{M}$. Normalization means $$\label{eq:equivariant_module_normalization}
U_e=\operatorname{id}_{\mathcal{M}},\qquad c^e=\operatorname{id},
\qquad \mu_{e,h}=\mu_{h,e}=\operatorname{id}_{U_h}.$$ Every strong monoidal section is monoidally isomorphic to a normalized one, so this convention does not change the equivalence classes under consideration.

Under these conventions, normalized $H$-equivariant $\mathcal{C}$-module structures on $\mathcal{M}$ are equivalent to $(\mathcal{C}\rtimes H)$-module structures extending the original $\mathcal{C}$-action. The correspondence is given explicitly by $$\label{eq:semidirect_product_module_action}
[X,h]\overline\otimes M:=X\overline\otimes U_h(M).$$ The associativity constraint for this action is built from $c^h$ and $\mu_{g,h}$; conversely, the action of $[\mathbf1,h]$ recovers $U_h$, and the module associativity recovers $c^h$ and $\mu_{g,h}$.

An $H$-equivariant $\mathcal{C}$-module category will be called indecomposable when its underlying $\mathcal{C}$-module category is indecomposable.

## The equivariant category $\mathcal{C}^G$ and its module categories

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

# Fiber functors for $\mathcal{C}^G$ {#sec:fiber-functors}
