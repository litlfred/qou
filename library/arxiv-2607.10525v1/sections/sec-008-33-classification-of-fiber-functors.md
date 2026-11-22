---
doc_id: arxiv-2607.10525v1
doc_title: "Fiber Functors of Equivariantizations of Finite Tensor Categories"
section_id: sec-008-33-classification-of-fiber-functors
section_title: "Classification of fiber functors"
section_number: 3.3
pages: 11-12
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.969
doc_brief: "Fiber Functors of Equivariantizations of Finite Tensor Categories — Let G be a finite group acting on a finite tensor category C."
---
::: theorem
[]{#thm:main_classification label="thm:main_classification"} Let $G$ act on a finite tensor category $\mathcal{C}$. Fiber functors on $\mathcal{C}^G$ are in bijection with conjugacy classes of pairs $(H,\mathcal{M})$ such that:

1.  $H\leq G$;

2.  $\mathcal{M}$ is an $H$-equivariant $\mathcal{C}$-module category whose underlying $\mathcal{C}$-module category is indecomposable, exact, and semisimple;

3.  $H$ acts transitively on $\operatorname{Irr}(\mathcal{M})$;

4.  for some, equivalently every, simple $X\in\mathcal{M}$, the class $[\alpha_X]\in H^2(\operatorname{St}_H(X),{\Bbbk}^\times)$ is nondegenerate.
:::

::: proof
*Proof.* By Proposition [\[prop:fiber_rank_one\]](#prop:fiber_rank_one){reference-type="ref" reference="prop:fiber_rank_one"}, a fiber functor on $\mathcal{C}^G$ determines an exact $\mathcal{C}^G$-module category $\mathcal{N}$ of rank one. In particular, $\mathcal{N}$ is indecomposable and semisimple. Proposition [\[prop:mod_cat_equivariantization\]](#prop:mod_cat_equivariantization){reference-type="ref" reference="prop:mod_cat_equivariantization"} gives a subgroup $H\subseteq G$ and an $H$-equivariant $\mathcal{C}$-module category $\mathcal{M}$, with indecomposable exact underlying $\mathcal{C}$-module category, such that $\mathcal{N}\simeq\mathcal{M}^H$. Since $H$ is finite and $|H|$ is invertible in ${\Bbbk}$, Tambara's semisimplicity theorem [@T01 Proposition 5.2] implies that $\mathcal{M}$ is semisimple. Corollary [\[cor:rank_one_MH\]](#cor:rank_one_MH){reference-type="ref" reference="cor:rank_one_MH"} then gives transitivity of the action on $\operatorname{Irr}(\mathcal{M})$ and nondegeneracy of the stabilizer cocycle.

Conversely, let $(H,\mathcal{M})$ satisfy the conditions in the statement. Part (1) of Proposition [\[prop:mod_cat_equivariantization\]](#prop:mod_cat_equivariantization){reference-type="ref" reference="prop:mod_cat_equivariantization"} shows that $\mathcal{M}^H$ is an exact $\mathcal{C}^G$-module category. Since $\mathcal{M}$ is semisimple, items [(3)--(4)]{.upright} and Corollary [\[cor:rank_one_MH\]](#cor:rank_one_MH){reference-type="ref" reference="cor:rank_one_MH"} imply that $\mathcal{M}^H$ has rank one. Proposition [\[prop:fiber_rank_one\]](#prop:fiber_rank_one){reference-type="ref" reference="prop:fiber_rank_one"} therefore produces a fiber functor on $\mathcal{C}^G$.

Finally, Theorem [\[thm:conjugacy_equivariantization\]](#thm:conjugacy_equivariantization){reference-type="ref" reference="thm:conjugacy_equivariantization"} says that two such pairs yield equivalent $\mathcal{C}^G$-module categories, and hence equivalent fiber functors, exactly when they are conjugate. This proves both directions and the asserted bijection. ◻
:::

::: corollary
[]{#cor:cohomologically_trivial label="cor:cohomologically_trivial"} Assume that $H^2(L,{\Bbbk}^\times)=0$ for every subgroup $L\leq G$. Then fiber functors on $\mathcal{C}^G$ are classified by conjugacy classes of pairs $(H,\mathcal{M})$ satisfying items [(1)--(2)]{.upright} of Theorem [\[thm:main_classification\]](#thm:main_classification){reference-type="ref" reference="thm:main_classification"} and such that $H$ acts freely and transitively on $\operatorname{Irr}(\mathcal{M})$. This applies in particular when every subgroup of $G$ is cyclic, hence when $G$ is cyclic.
:::

::: proof
*Proof.* Under the hypothesis, every stabilizer cocycle is cohomologically trivial. Its twisted group algebra is therefore an ordinary group algebra, which is simple over ${\Bbbk}$ exactly when the stabilizer is trivial. Theorem [\[thm:main_classification\]](#thm:main_classification){reference-type="ref" reference="thm:main_classification"} gives the result. ◻
:::
