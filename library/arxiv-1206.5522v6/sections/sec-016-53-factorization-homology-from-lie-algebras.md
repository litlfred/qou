---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-016-53-factorization-homology-from-lie-algebras
section_title: "Factorization homology from Lie algebras"
section_number: 5.3
pages: 35-36
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.96
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds, after Beilinson, Drinfeld and Lurie, are homology-type theories for topological n-manifolds"
---
We now discuss factorization homology of $n$-disk algebras coming from Lie algebras. Our results are closely analogous to those above about the factorization homology of $n$-disk algebras coming from topological spaces. For simplicity, we assume our Lie algebras are defined over a fixed field $k$ of characteristic zero.

As we proceed, we make use of the fact that Lie algebras in ${\sf Mod}_k$ admit totalizations, and therefore the $\infty$-category of such is cotensored over pointed spaces in a natural and standard way: $(X,\mathfrak{g})\mapsto {\mathfrak{g}}^X$. For $M$ an $n$-manifold, we notate $\mathop{\mathrm{\sf Map}}_{\sf c}(M , \mathfrak{g}) := {\mathfrak{g}}^{M^+}$, where $M^+$ is the 1-point compactification. One can describe this as $\mathop{\mathrm{{\sf Map}_{\sf c}}}(M,\frak g)\simeq \mathsf C_{\sf c}^\ast(M,\frak g)$, the compactly supported cochains of $M$ with coefficients in $\frak g$. See also [@owen] and [@kevinowen] for a discussion of the following.

::: prop
[]{#env label="env"} For $\mathfrak{g}$ a Lie algebra over $k$, there is a natural equivalence of chain complexes over $k$, $$\int_M \mathsf C_\ast^{\mathop{\mathrm{\sf Lie}}}\bigl(\mathop{\mathrm{{\sf Map}_{\sf c}}}(\mathbb R^n,\mathfrak{g})\bigr)~ \simeq~ \mathsf C^{\mathop{\mathrm{\sf Lie}}}_\ast\bigl(\mathop{\mathrm{{\sf Map}_{\sf c}}}(M, \mathfrak{g})\bigr)~,$$ between the factorization homology of the Lie algebra chains of $\Omega^n {\mathfrak{g}}$ and the Lie algebra chains of the Lie algebra $\mathfrak{g}^{M^+}$.
:::

::: proof
*Proof.* Lie algebra chains defines a functor between $\infty$-categories $\mathsf C^{\mathop{\mathrm{\sf Lie}}}_\ast: \mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{\sf Lie}}}({\sf Mod}_k) \rightarrow{\sf Mod}_k$. This functor carries finite products of Lie algebras to finite tensor products of $k$-modules, which is to say that it is symmetric monoidal. Furthermore, this functor preserves geometric realizations, so Lemma [\[switch\]](#switch){reference-type="ref" reference="switch"} applies to give a natural identification: $\int_M \mathsf C_\ast^{\mathop{\mathrm{\sf Lie}}}\bigl(\mathop{\mathrm{{\sf Map}_{\sf c}}}(\mathbb R^n,\mathfrak{g})\bigr)\simeq  \mathsf C_\ast^{\mathop{\mathrm{\sf Lie}}}\bigl(\int_M\mathop{\mathrm{{\sf Map}_{\sf c}}}(\mathbb R^n,\mathfrak{g})\bigr)$. The equivalence $\int_M\mathop{\mathrm{{\sf Map}_{\sf c}}}(\mathbb R^n,\mathfrak{g})\simeq \mathop{\mathrm{{\sf Map}_{\sf c}}}(M,\mathfrak{g})$ now follows from the argument of nonabelian Poincaré duality (Corollary [\[non-abel\]](#non-abel){reference-type="ref" reference="non-abel"}), only here we apply it in the usual abelian setting.[^1] ◻
:::

::: remark
The $n$-disk algebra $\mathsf C_\ast^{\mathop{\mathrm{\sf Lie}}}\bigl(\mathop{\mathrm{{\sf Map}_{\sf c}}}(\mathbb R^n,\mathfrak{g})\bigr)$ has an interesting separate interpretation that we state here, and prove as a separate work. There is a forgetful functor from $\mathcal E_n$-algebras in chain complexes over $k$ to Lie algebras over $k$ (see [@cohen] for an account at the level of homology). The adjoint functor theorem (Corollary 5.5.2.9 of [@topos]) applies to this functor, and so there is an adjunction $$\mathsf U_n \colon \mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{\sf Lie}}}({\sf Mod}_k)~ \rightleftarrows~ \mathop{\mathrm{\mathsf{Alg}}}_{\mathop{\mathrm{{\mathcal D}\sf isk}}_n^{\sf fr}}({\sf Mod}_k)\colon {\sf fgt}~.$$ In the case $n=1$, this left adjoint $\mathsf U_1$ agrees with the familiar universal enveloping algebra functor. In general, there is an identification of $\mathop{\mathrm{{\mathcal D}\sf isk}}_n^{\sf fr}$-algebras, $$\mathsf U_n \mathfrak{g}~\simeq~  \mathsf C_\ast^{\mathop{\mathrm{\sf Lie}}}\bigl(\mathop{\mathrm{{\sf Map}_{\sf c}}}(\mathbb R^n, \mathfrak{g})\bigr)~,$$ through which Proposition [\[env\]](#env){reference-type="ref" reference="env"} can be reformulated as an equivalence of chain complexes over $k$: $$\int_M\mathsf U_n\mathfrak{g}~\simeq~ \mathsf C^{\mathop{\mathrm{\sf Lie}}}_\ast\bigl(\mathop{\mathrm{{\sf Map}_{\sf c}}}(M,\mathfrak{g})\bigr)~.$$
:::

[^1]: See [@af2] for a complete account, where nonabelian Poincaré duality is an instance of a version of Poincaré/Koszul duality for *Cartesian-presentable $\infty$-categories*.
