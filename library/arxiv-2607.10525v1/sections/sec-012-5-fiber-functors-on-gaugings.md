---
doc_id: arxiv-2607.10525v1
doc_title: "Fiber Functors of Equivariantizations of Finite Tensor Categories"
section_id: sec-012-5-fiber-functors-on-gaugings
section_title: "Fiber functors on gaugings"
section_number: 5
pages: 18-21
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.967
doc_brief: "Fiber Functors of Equivariantizations of Finite Tensor Categories — Let G be a finite group acting on a finite tensor category C."
---
[]{#sec:gauging label="sec:gauging"}

We now apply the classification to gaugings. Let $\mathcal{B}$ be a braided fusion category and let $$\mathcal{E}=\bigoplus_{g\in G}\mathcal{E}_g$$ be a faithful $G$-crossed braided fusion category with neutral component $\mathcal{E}_e=\mathcal{B}$. We denote by $\rho$ the crossed action of $G$ on $\mathcal{E}$. Following the formulation of gauging in [@CGPW16], based on the extension theory of [@ENO10], the gauging determined by the $G$-crossed extension $\mathcal{E}$ is the equivariantization $$\mathcal{E}^G.$$ The crossed braiding makes $\mathcal{E}^G$ a braided fusion category, but the fiber-functor problem below uses only the underlying tensor category $\mathcal{E}$ together with the action $\rho$.

::: definition
For a subgroup $S\subseteq G$, set $\mathcal{E}_S=\bigoplus_{s\in S}\mathcal{E}_s$. A *Clifford datum* for $\mathcal{E}$ is a triple $(S,\mathcal{N},\widetilde{\mathcal{N}})$, where $\mathcal{N}$ is an indecomposable semisimple $\mathcal{B}$-module category and $\widetilde{\mathcal{N}}$ is an indecomposable semisimple $\mathcal{E}_S$-module category on the same underlying finite semisimple category, whose restriction to $\mathcal{B}$ is equivalent to the given $\mathcal{B}$-module structure on $\mathcal{N}$. We call $\widetilde{\mathcal{N}}$ an $\mathcal{E}_S$-extension of $\mathcal{N}$.
:::

Given a Clifford datum $(S,\mathcal{N},\widetilde{\mathcal{N}})$, put $$\mathop{\mathrm{Ind}}(S,\widetilde{\mathcal{N}})
:=\mathop{\mathrm{Ind}}_{\mathcal{E}_S}^{\mathcal{E}}(\widetilde{\mathcal{N}})
\simeq \mathcal{E}\boxtimes_{\mathcal{E}_S}\widetilde{\mathcal{N}}.$$ The result is an indecomposable $\mathcal{E}$-module category. Conversely, by Clifford theory for graded fusion categories, every indecomposable $\mathcal{E}$-module category is of this form.

Let $\mathfrak d=(S,\mathcal{N},\widetilde{\mathcal{N}})$ be a Clifford datum and let $h\in G$. We define its $h$-twist by $$\mathfrak d^h=(h^{-1}Sh,\mathcal{N}^h,\widetilde{\mathcal{N}}^{\,h}),$$ where $\widetilde{\mathcal{N}}^{\,h}$ is the same underlying category as $\widetilde{\mathcal{N}}$, regarded as an $\mathcal{E}_{h^{-1}Sh}$-module category by $$X\overline{\otimes}^{\,h} N:=\rho_h(X)\overline{\otimes}N,
\qquad X\in \mathcal{E}_{h^{-1}Sh},\; N\in\widetilde{\mathcal{N}},$$ and $\mathcal{N}^h$ is its restriction to $\mathcal{B}=\mathcal{E}_e$. Then $$\mathop{\mathrm{Ind}}(S,\widetilde{\mathcal{N}})^h\simeq
\mathop{\mathrm{Ind}}(h^{-1}Sh,\widetilde{\mathcal{N}}^{\,h})$$ as $\mathcal{E}$-module categories.

::: definition
Let $\mathfrak d=(S,\mathcal{N},\widetilde{\mathcal{N}})$ be a Clifford datum. An *$H$-equivariant Clifford lift* of $\mathfrak d$ is a choice, for every $h\in H$, of an equivalence of induced $\mathcal{E}$-module categories $$\Phi_h:\mathop{\mathrm{Ind}}(S,\widetilde{\mathcal{N}})\xrightarrow{\sim}
\mathop{\mathrm{Ind}}(h^{-1}Sh,\widetilde{\mathcal{N}}^{\,h}),$$ together with coherence isomorphisms making the corresponding functors $$\mathop{\mathrm{Ind}}(S,\widetilde{\mathcal{N}})\longrightarrow
\mathop{\mathrm{Ind}}(S,\widetilde{\mathcal{N}})^h$$ an $H$-equivariant structure in the sense of Section [\[sec:preliminaries\]](#sec:preliminaries){reference-type="ref" reference="sec:preliminaries"}.
:::

::: remark
For each fixed $h\in H$, the equivalence criterion for induced module categories over graded fusion categories [@MM20 Definition 5.10 and Proposition 5.12] tests the existence of $\Phi_h$ by asking for an element $a_h\in G$ such that $$S=a_h(h^{-1}Sh)a_h^{-1}$$ and, writing $$\mathcal{E}_{a_h(h^{-1}Sh)}:=\bigoplus_{u\in a_h(h^{-1}Sh)}\mathcal{E}_u$$ for the corresponding $(\mathcal{E}_S,\mathcal{E}_{h^{-1}Sh})$-bimodule category, an equivalence of $\mathcal{E}_S$-module categories $$\mathcal{E}_{a_h(h^{-1}Sh)}
\boxtimes_{\mathcal{E}_{h^{-1}Sh}}
\widetilde{\mathcal{N}}^{\,h}
\simeq
\widetilde{\mathcal{N}}.$$ It remains to require these equivalences, as $h$ varies, to satisfy the equivariant coherence.
:::

::: theorem
[]{#thm:gauging_clifford_fiber_functors label="thm:gauging_clifford_fiber_functors"} Let $\mathcal{E}=\bigoplus_{g\in G}\mathcal{E}_g$ be a faithful $G$-crossed braided fusion category with neutral component $\mathcal{B}=\mathcal{E}_e$. Fiber functors on $\mathcal{E}^G$ correspond to equivalence classes of tuples $$(H,S,\mathcal{N},\widetilde{\mathcal{N}},\mathbf{u})$$ satisfying:

1.  $H$ and $S$ are subgroups of $G$;

2.  $(S,\mathcal{N},\widetilde{\mathcal{N}})$ is a Clifford datum for $\mathcal{E}$;

3.  $\mathbf{u}$ is an $H$-equivariant Clifford lift of $(S,\mathcal{N},\widetilde{\mathcal{N}})$;

4.  for $\mathcal{M}=\mathop{\mathrm{Ind}}(S,\widetilde{\mathcal{N}})$, the induced action of $H$ on $\operatorname{Irr}(\mathcal{M})$ is transitive;

5.  for some, hence every, simple object $X\in\mathcal{M}$, the stabilizer cocycle $$[\alpha_X]\in H^2(\operatorname{St}_H(X),{\Bbbk}^\times)$$ is nondegenerate.

Two tuples are identified when their associated equivariant $\mathcal{E}$-module categories are conjugate in the sense of Definition [[\[def:conjugate_equivariant_module_categories\]](#def:conjugate_equivariant_module_categories){reference-type="ref" reference="def:conjugate_equivariant_module_categories"}]{.upright}.
:::

::: proof
*Proof.* Apply Theorem [\[thm:main_classification\]](#thm:main_classification){reference-type="ref" reference="thm:main_classification"} to the crossed action $\rho:G\to\operatorname{Aut}_{\otimes}(\mathcal{E})$. By Clifford theory for graded fusion categories [@Gal12; @MM20], every indecomposable $\mathcal{E}$-module category has the form $$\mathcal{M}\simeq\mathop{\mathrm{Ind}}_{\mathcal{E}_S}^{\mathcal{E}}(\widetilde{\mathcal{N}})
\simeq\mathcal{E}\boxtimes_{\mathcal{E}_S}\widetilde{\mathcal{N}}$$ for a Clifford datum $(S,\mathcal{N},\widetilde{\mathcal{N}})$. Transporting the $H$-equivariant structure on $\mathcal{M}$ gives $\mathbf u$.

Conversely, such a tuple produces an $H$-equivariant indecomposable exact semisimple $\mathcal{E}$-module category. Items [(4)--(5)]{.upright} and Theorem [\[thm:main_classification\]](#thm:main_classification){reference-type="ref" reference="thm:main_classification"} give a fiber functor. The equivalence relation is exactly the conjugacy relation of Theorem [\[thm:conjugacy_equivariantization\]](#thm:conjugacy_equivariantization){reference-type="ref" reference="thm:conjugacy_equivariantization"}. ◻
:::

::: corollary
[]{#cor:prime_cyclic_gauging label="cor:prime_cyclic_gauging"} Let $G=C_p=\langle \tau\rangle$ be cyclic of prime order, and let $\mathcal{E}=\bigoplus_{g\in G}\mathcal{E}_g$ be a faithful $G$-crossed braided fusion category with neutral component $\mathcal{B}$. Then the data of Theorem [\[thm:gauging_clifford_fiber_functors\]](#thm:gauging_clifford_fiber_functors){reference-type="ref" reference="thm:gauging_clifford_fiber_functors"} reduce to the following possibilities.

1.  $H=\{e\}$, $S=G$, and $\widetilde{\mathcal{N}}$ is a rank-one $\mathcal{E}$-module category. These fiber functors are the $G$-orbits of fiber functors on $\mathcal{E}$ under the crossed action.

2.  $H=G$, and $\mathcal{M}=\mathop{\mathrm{Ind}}(S,\widetilde{\mathcal{N}})$ carries a $G$-equivariant Clifford lift whose generator acts on $\operatorname{Irr}(\mathcal{M})$ as a single $p$-cycle. This has two subcases:

    1.  $S=\{e\}$, $\widetilde{\mathcal{N}}=\mathcal{N}$, and $$\mathcal{M}=\mathcal{E}\boxtimes_{\mathcal{B}}\mathcal{N}
        =\bigoplus_{g\in G}\mathcal{M}_g,
        \qquad
        \mathcal{M}_g:=\mathcal{E}_g\boxtimes_{\mathcal{B}}\mathcal{N},$$ where every $\mathcal{M}_g$ has rank one and the generator of $G$ acts on their $p$ simple objects as a single $p$-cycle.

    2.  $S=G$, and $\widetilde{\mathcal{N}}$ is an $\mathcal{E}$-module category with $p$ simple objects, equipped with a $G$-equivariant structure whose generator acts as a $p$-cycle.
:::

::: proof
*Proof.* The only subgroups of $C_p$ are $\{e\}$ and $G$, and $H^2(L,{\Bbbk}^\times)=0$ for both. Hence Corollary [\[cor:cohomologically_trivial\]](#cor:cohomologically_trivial){reference-type="ref" reference="cor:cohomologically_trivial"} applies: the stabilizer condition in Theorem [\[thm:gauging_clifford_fiber_functors\]](#thm:gauging_clifford_fiber_functors){reference-type="ref" reference="thm:gauging_clifford_fiber_functors"} is equivalent to freeness of the $H$-action on $\operatorname{Irr}(\mathcal{M})$.

If $H=\{e\}$, freeness and transitivity mean that $\mathcal{M}$ has one simple object. If $S=\{e\}$, the restriction of $\mathop{\mathrm{Ind}}(S,\widetilde{\mathcal{N}})$ to $\mathcal{B}$ has one nonzero component for each element of $G$; hence its rank is at least $p$. Thus rank one forces $S=G$.

If $H=G$, a free transitive action of the cyclic group of order $p$ is exactly a single $p$-cycle. The two alternatives for $S$ are the only possible ones. For $S=\{e\}$, Clifford theory gives a decomposition $$\mathcal{M}=\bigoplus_{g\in G}\mathcal{M}_g,
\qquad
\mathcal{M}_g=\mathcal{E}_g\boxtimes_{\mathcal{B}}\mathcal{N},$$ into non-zero indecomposable $\mathcal{B}$-module subcategories; see [@Gal12 Proposition 4.1]. Consequently, $$\#\operatorname{Irr}(\mathcal{M})=\sum_{g\in G}\#\operatorname{Irr}(\mathcal{M}_g)\ge p,$$ and equality holds if and only if every $\mathcal{M}_g$ has rank one. In particular, equality implies that $\mathcal{N}=\mathcal{M}_e$ has rank one. This argument does not require an invertible $\mathcal{B}$-bimodule category to preserve rank. The case $S=G$ is immediate from $\mathcal{M}=\widetilde{\mathcal{N}}$. ◻
:::

::: remark
Two layers of data are not visible from the neutral-component module category alone. First, $\mathcal{N}$ must extend from $\mathcal{B}$ to $\mathcal{E}_S$. In the obstruction theory of [@MeMu12], if $\mathcal{N}\simeq\operatorname{Mod}_{\mathcal{B}}(A)$, this requires $S$-stability and a splitting of $$1\longrightarrow\operatorname{Aut}_{\mathcal{B}}(\mathcal{N})
\longrightarrow\Lambda\longrightarrow S\longrightarrow1,$$ where $\Lambda$ consists of invertible $A$-$A$-bimodules supported in $\mathcal{E}_S$. After a splitting is chosen, an obstruction in $H^3(S,{\Bbbk}^\times)$ governs associative multiplication on the resulting graded algebra $\widetilde A=\bigoplus_{s\in S}A_s$. Second, the induced $\mathcal{E}$-module category must be equivalent to its $h$-twists for $h\in H$, with compatible coherence. Thus the practical inputs are the $\mathcal{B}$-module category, its $\mathcal{E}_S$-extension, and the equivariant lift; the rank-one test is then supplied by Theorem [\[thm:gauging_clifford_fiber_functors\]](#thm:gauging_clifford_fiber_functors){reference-type="ref" reference="thm:gauging_clifford_fiber_functors"}.
:::
