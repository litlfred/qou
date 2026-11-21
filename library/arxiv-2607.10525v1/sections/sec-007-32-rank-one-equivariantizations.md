---
doc_id: arxiv-2607.10525v1
doc_title: "Fiber Functors of Equivariantizations of Finite Tensor Categories"
section_id: sec-007-32-rank-one-equivariantizations
section_title: "Rank-one equivariantizations"
section_number: 3.2
pages: 9-11
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.953
doc_brief: "Fiber Functors of Equivariantizations of Finite Tensor Categories — Let G be a finite group acting on a finite tensor category C."
---
We next characterize when $\mathcal{M}^H$ has rank one. Since $H$ is finite and $\operatorname{char}({\Bbbk})=0$, Tambara's theorem gives $$\mathcal{M}^H\text{ semisimple}\quad\Longleftrightarrow\quad \mathcal{M}\text{ semisimple}$$ [@T01 Proposition 5.2]. We therefore assume that $\mathcal{M}$ is semisimple.

### Action on simple objects and obstruction cocycles

Let $H$ be a finite group acting on a semisimple ${\Bbbk}$-linear category $\mathcal{M}$ via autoequivalences $\{U_h\}_{h \in H}$ and normalized coherence isomorphisms $\mu_{h_1,h_2}:U_{h_1}U_{h_2}\xrightarrow{\sim}U_{h_1h_2}$. The group $H$ acts naturally on the set $\operatorname{Irr}(\mathcal{M})$ of isomorphism classes of simple objects by $h \cdot [X] := [U_h(X)]$.

For a simple object $X \in \mathcal{M}$, we denote by $\operatorname{St}_H(X) = \{h \in H \mid U_h(X) \cong X\}$ its *stabilizer subgroup*. For each $h \in \operatorname{St}_H(X)$, we choose an isomorphism $f_h: U_h(X) \xrightarrow{\sim} X$ with $f_e = \operatorname{id}_X$.

::: definition
[]{#def:obstruction_cocycle label="def:obstruction_cocycle"} The *obstruction 2-cocycle* $\alpha_X: \operatorname{St}_H(X) \times \operatorname{St}_H(X) \to {\Bbbk}^\times$ is defined by $$\alpha_X(h_1, h_2) \cdot \operatorname{id}_X =
    f_{h_1} \circ U_{h_1}(f_{h_2}) \circ
    (\mu_{h_1,h_2})_X^{-1}\circ f_{h_1 h_2}^{-1}.$$ The right-hand side is an endomorphism of the simple object $X$, hence a scalar multiple of $\operatorname{id}_X$. The cocycle is normalized because $f_e=\operatorname{id}_X$ and the equivariant structure is normalized. When the action is strict, this reduces to the formula with $\mu_{h_1,h_2}=\operatorname{id}$.
:::

::: proposition
[]{#prop:obstruction_cocycle_properties label="prop:obstruction_cocycle_properties"} The map $\alpha_X$ is a 2-cocycle in $Z^2(\operatorname{St}_H(X), {\Bbbk}^\times)$. Its cohomology class $[\alpha_X] \in H^2(\operatorname{St}_H(X), {\Bbbk}^\times)$ is independent of the choice of isomorphisms $\{f_h\}$. If $Y$ lies in the $H$-orbit of $X$, then the classes $[\alpha_X]$ and $[\alpha_Y]$ correspond under the conjugation identification of their stabilizers.
:::

::: proof
*Proof.* The defining equation can be written as $$\label{eq:obstruction_factor_set}
f_g\circ U_g(f_h)\circ(\mu_{g,h})_X^{-1}
=\alpha_X(g,h)f_{gh}$$ for $g,h\in\operatorname{St}_H(X)$. Compare the two composites from $U_gU_hU_k(X)$ to $X$ obtained by first applying [\[eq:obstruction_factor_set\]](#eq:obstruction_factor_set){reference-type="eqref" reference="eq:obstruction_factor_set"} to $(g,h)$ or to $(h,k)$. The pentagon identity [\[eq:equivariant_module_pentagon\]](#eq:equivariant_module_pentagon){reference-type="eqref" reference="eq:equivariant_module_pentagon"} gives $$\alpha_X(g,h)\alpha_X(gh,k)
=\alpha_X(g,hk)\alpha_X(h,k),$$ and normalization gives $\alpha_X(e,h)=\alpha_X(h,e)=1$. Thus $\alpha_X\in Z^2(\operatorname{St}_H(X),{\Bbbk}^\times)$.

If $f'_h=\lambda_hf_h$, where $\lambda_h\in{\Bbbk}^\times$ and $\lambda_e=1$, then substitution in Definition [\[def:obstruction_cocycle\]](#def:obstruction_cocycle){reference-type="ref" reference="def:obstruction_cocycle"} yields $$\alpha'_X(g,h)
=\frac{\lambda_g\lambda_h}{\lambda_{gh}}\,\alpha_X(g,h).$$ Hence $\alpha'_X$ and $\alpha_X$ differ by a coboundary.

Finally, suppose first that $Y=U_a(X)$. Conjugation $\iota_a(s)=asa^{-1}$ identifies $\operatorname{St}_H(X)$ with $\operatorname{St}_H(Y)$. For $s\in\operatorname{St}_H(X)$ define $$\label{eq:transported_stabilizer_isomorphism}
\widetilde f_{\iota_a(s)}
:=U_a(f_s)\circ(\mu_{a,s})_X^{-1}
\circ(\mu_{\iota_a(s),a})_X:
U_{\iota_a(s)}(Y)\longrightarrow Y.$$ A second application of the pentagon identity shows that, for these transported choices, $$\alpha_Y(asa^{-1},ata^{-1})=\alpha_X(s,t)
\qquad(s,t\in\operatorname{St}_H(X)).$$ If $Y$ is only isomorphic to $U_a(X)$, conjugating the maps in [\[eq:transported_stabilizer_isomorphism\]](#eq:transported_stabilizer_isomorphism){reference-type="eqref" reference="eq:transported_stabilizer_isomorphism"} by a chosen isomorphism $U_a(X)\xrightarrow{\sim}Y$ changes neither conclusion; a different choice changes the cocycle only by a coboundary. Therefore the two cohomology classes correspond under conjugation. ◻
:::

Recall that a cohomology class $[\alpha] \in H^2(G, {\Bbbk}^\times)$ is called *nondegenerate* if the corresponding twisted group algebra ${\Bbbk}_\alpha[G]$ is simple.

We also use the description of simple objects in equivariant semisimple categories, in the form recalled in [@GP17 Subsection 7.5.1].

::: proposition
[]{#prop:structure_MH label="prop:structure_MH"} Let $H$ be a finite group acting on a finite semisimple ${\Bbbk}$-linear category $\mathcal{M}$. If $\{X_1, \ldots, X_m\}$ is a set of representatives of the $H$-orbits of simple objects in $\mathcal{M}$, then there is a bijective correspondence between simple objects in $\mathcal{M}^H$ and pairs $(i, V)$ where $1 \leq i \leq m$ and $V$ is a simple right module over the twisted group algebra ${\Bbbk}_{\alpha_{X_i}}[\operatorname{St}_H(X_i)]$.
:::

::: corollary
[]{#cor:rank_one_MH label="cor:rank_one_MH"} Let $H$ be a finite group acting on a finite semisimple ${\Bbbk}$-linear category $\mathcal{M}$. The category $\mathcal{M}^H$ has rank one if and only if:

1.  The action of $H$ on $\operatorname{Irr}(\mathcal{M})$ is transitive.

2.  For a simple object $X \in \mathcal{M}$, the obstruction cocycle $[\alpha_X] \in H^2(\operatorname{St}_H(X), {\Bbbk}^\times)$ is nondegenerate.
:::

::: proof
*Proof.* By Proposition [\[prop:structure_MH\]](#prop:structure_MH){reference-type="ref" reference="prop:structure_MH"}, the number of simple objects of $\mathcal{M}^H$ is $$\sum_{\mathcal{O}\in H\backslash \operatorname{Irr}(\mathcal{M})}
\#\,\operatorname{Irr}\big({\Bbbk}_{\alpha_X}[\operatorname{St}_H(X)]\big),$$ where $X$ is any representative of the orbit $\mathcal{O}$. This number is one if and only if there is a single $H$-orbit and the twisted group algebra attached to the stabilizer has a single simple module. Since the algebra is finite-dimensional semisimple over the algebraically closed field ${\Bbbk}$, this is equivalent to the twisted group algebra being simple, which is the nondegeneracy condition for $[\alpha_X]$. ◻
:::
