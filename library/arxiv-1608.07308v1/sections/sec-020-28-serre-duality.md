---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-020-28-serre-duality
section_title: "Serre duality"
section_number: 2.8
pages: 19-19
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.97
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:serre label="sub:serre"}

As explained in Subsection [\[sub:proj dg\]](#sub:proj dg){reference-type="ref" reference="sub:proj dg"} of the Appendix, we may embed the dg scheme $\mathrm{FHilb}_{n+1}^\text{dg}$ into an actual projective bundle: $$\includegraphics{2_39.png}
\label{eqn:triangle}$$ where we implicitly use the description [\[eqn:two step\]](#eqn:two step){reference-type="eqref" reference="eqn:two step"} of the complex of vector bundles $\mathcal{E}_n$. This allows us to compute the push-forward $\pi_*$ of sheaves by factoring them through the diagram [\[eqn:triangle\]](#eqn:triangle){reference-type="eqref" reference="eqn:triangle"}.

::: proposition
[]{#prop:serre label="prop:serre"}

Let $\pi:\mathrm{FHilb}^{\emph{dg}}_{n+1}(\mathbb{C}) \to \mathrm{FHilb}_n^{\emph{dg}}(\mathbb{C})\times \mathbb{C}$ be the projection. Then: $$\label{eqn:serre}
\pi_*(\mathcal{A})^\vee \cong \pi_*(\mathcal{A}^\vee\otimes \mathcal{L}_{n+1}^{-1})$$ for any $\mathcal{A}\in D^b(\mathrm{Coh}(\mathrm{FHilb}^{\emph{dg}}_{n+1}(\mathbb{C})))$. The functor $\pi_*$ is derived, and $\vee$ denotes Serre duality on the dg scheme $\mathrm{FHilb}_n^{\emph{dg}}(\mathbb{C})$, which is defined inductively by Proposition [\[prop:serre\]](#prop:serre){reference-type="ref" reference="prop:serre"}.
:::

This is a direct application of Proposition [\[prop:canonical\]](#prop:canonical){reference-type="ref" reference="prop:canonical"} in the Appendix, together with the fact that the determinant of the complex $\mathcal{E}_n(\mathbb{C})$ of [\[eqn:complex\]](#eqn:complex){reference-type="eqref" reference="eqn:complex"} is trivial. Applying formula [\[eqn:serre\]](#eqn:serre){reference-type="eqref" reference="eqn:serre"} to $\mathcal{A}= \mathcal{O}$ gives us the following formulas for all $k \geq 0$: $$\label{eqn:push negative}
\pi_{*}(\mathcal{L}_{n+1}^{-1-k}) = \pi_*(\mathcal{L}_{n+1}^{k})^{\vee}=S^{k}\mathcal{E}_n^{\vee} \qquad \text{concentrated in degree 0}$$

::: remark
The analogue of [\[eqn:serre\]](#eqn:serre){reference-type="eqref" reference="eqn:serre"} when $\mathbb{C}$ is replaced by $\mathbb{C}^2$ holds exactly as stated. Meanwhile, when $\mathbb{C}$ is replaced by point we must replace formula [\[eqn:serre\]](#eqn:serre){reference-type="eqref" reference="eqn:serre"} by the following equation: $$\label{eqn:serre2}
\widetilde{\pi}_*(\mathcal{A})^\vee \cong \widetilde{\pi}_*\left(\mathcal{A}^\vee\otimes \frac {qt \mathcal{L}_n}{\mathcal{L}_{n+1}^{2}} \right)[-1]$$ where $\widetilde{\pi}:\mathrm{FHilb}_{n+1}^\text{dg}\rightarrow \mathrm{FHilb}_n^\text{dg}$ is the standard projection.
:::
