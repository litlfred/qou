---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-039-b1-the-complete-structure
section_title: "B.1 The complete structure"
section_number: null
pages: 46-46
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.961
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
Let $M^3$ be a hyperbolic orientable 3-manifold and $$\varrho=\widetilde{\mathrm{hol}}\colon\pi_1M�\to\mathrm{SL}_2(\mathbb{C})$$ a lift of its holonomy. As before denote by $$\label{eqn:rhok1k2}
 \varrho^{k_1,k_2}:= \operatorname{Sym}^{k_1,k_2}\circ \varrho \colon\pi_1 M^3\to \mathrm{SL}_{(k_1+1)(k_2+1)}(\mathbb{C}).$$ Let $$\label{eqn:Ek1k2}
E_{k_1,k_2}= \widetilde M \times_{\varrho^{k_1,k_2}} \mathbb{C}^{(k_1+1)(k_2+1)}$$ be the flat bundle twisted by ${\varrho^{k_1,k_2}}$ as in [\[eqn:flabundle\]](#eqn:flabundle){reference-type="eqref" reference="eqn:flabundle"}. In particular its de Rham cohomology is isomorphic to the simplicial cohomology of $\varrho^{k_1,k_2}$ by de Rham theorem [\[eqn:deRham\]](#eqn:deRham){reference-type="eqref" reference="eqn:deRham"}.

Choosing a Hermitian metric on the fibre of the bundle $E_{k_1,k_2}\to M^3$ and a Riemannian metric on $M^3$, there is a product on $E_{k_1,k_2}$-valued differential forms $\Omega^*(M^3; E_{k_1,k_2})$ by integration on $M^3$, that we denote by $\langle\cdot,\cdot\rangle$. In particular it makes sense to talk about $L^2$-forms, as the forms with finite norm.

::: thm
[]{#thm:strong_acyclicity label="thm:strong_acyclicity"} For $k_1\neq k_2$, there exists a uniform constant $c_{k_1,k_2} > 0$ with the following property. For every hyperbolic orientable 3-manifold $M^3$, and every differential form $\omega\in\Omega^*(M^3; E_{k_1,k_2})$ with compact support, $$\langle \Delta \omega, \omega\rangle \geq c_{k_1,k_2} \langle \omega,\omega\rangle.$$
:::

This property implies *strong acyclicity*, as it yields that the spectrum of $\Delta$ is bounded below by the uniform constant $c_{k_1,k_2} > 0$.

::: cor
[]{#cor:acyclc label="cor:acyclc"} Let $M^3$ be a closed, orientable, hyperbolic 3-manifold, then ${\varrho^{k_1,k_2}}$ is acyclic for $k_1\neq k_2$.

In particular $\varrho^{k}=\operatorname{Sym}^{k}\circ \widetilde{\mathrm{hol}}$ is acyclic for $k\geq 1$.
:::

::: remark
This corollary does not hold true when $k_1=k_2$. Millson [@Millson85] showed that it fails when $k_1=k_2>0$ and $M^3$ contains a totally geodesic embedded surface, by means of bending.
:::
