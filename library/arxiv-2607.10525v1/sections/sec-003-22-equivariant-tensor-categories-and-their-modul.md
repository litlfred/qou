---
doc_id: arxiv-2607.10525v1
doc_title: "Fiber Functors of Equivariantizations of Finite Tensor Categories"
section_id: sec-003-22-equivariant-tensor-categories-and-their-modul
section_title: "Equivariant tensor categories and their module categories"
section_number: 2.2
pages: 4-7
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.945
doc_brief: "Fiber Functors of Equivariantizations of Finite Tensor Categories — Let G be a finite group acting on a finite tensor category C."
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
