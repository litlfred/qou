---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-031-311-mirror-braids
section_title: "Mirror braids"
section_number: 3.11
pages: 30-31
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 0.827
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:mirror label="sub:mirror"}

In this section, we will relate the operation of mirroring braids (i.e. looking at them from behind) with Verdier duality on the category of coherent sheaves on $\mathrm{FHilb}_n$.

::: proposition
[]{#prop:mirror label="prop:mirror"}

For any $\mathcal{F}\in D^b\mathrm{Coh}(\mathrm{FHilb}^\emph{dg}_n)$ one has: $$\int_{\mathrm{FHilb}_n^\emph{dg}} \mathcal{F}\otimes \wedge^\bullet \mathcal{T}_n^\vee \cong \left[\int_{\mathrm{FHilb}_n^\emph{dg}}\mathcal{F}^{\vee} \otimes \wedge^\bullet \mathcal{T}_n \right]^{\vee}$$ where the $a$-grading in the right hand side is reversed from $i$ to $n-i$.
:::

The Proposition is obvious, since it's just stating that a proper push-forward commutes with Verdier duality. It is natural to conjecture, therefore, that mirroring the braid $\sigma$ simply corresponds to dualizing the complex of sheaves $\mathcal{B}(\sigma)$ on $\mathrm{FHilb}_n^\text{dg}$:

::: conjecture
[]{#eqn:mirror label="eqn:mirror"}

For any braid $\sigma$, we have: $$\mathcal{B}(\sigma^{\vee})=\mathcal{B}(\sigma)^{\vee},$$ where $\beta^{\vee}$ denotes the mirror of $\beta$.
:::

The following example shows that the computation of a dual sheaf can be nontrivial.

::: example
[]{#ex:mirror label="ex:mirror"}

As we will see in Section [\[sec:n=2\]](#sec:n=2){reference-type="ref" reference="sec:n=2"} (and also from Section [\[sub:markov\]](#sub:markov){reference-type="ref" reference="sub:markov"}), the braid $\sigma_1\in \mathrm{SBim}_2$ corresponds to the structure sheaf of $\mathrm{FHilb}_2(\mathrm{point})\times \mathbb{C}\subset \mathrm{FHilb}_2(\mathbb{C})$, while $\sigma_1^{-1}\in \mathrm{SBim}_2$ corresponds to $\mathcal{O}(-1)$ on $\mathrm{FHilb}_2(\mathrm{point})\times \mathbb{C}$. The fact that the objects $$\mathcal{B}(\sigma_1) = \mathcal{O}_{\mathrm{FHilb}_2(\mathrm{point})\times \mathbb{C}} \qquad \text{and} \qquad \mathcal{B}(\sigma^{-1}_1) = \mathcal{O}_{\mathrm{FHilb}_2(\mathrm{point})\times \mathbb{C}}(-1)$$ are dual to each other follows from the fact that the exact sequence: $$\mathcal{O}_{\mathrm{FHilb}_2(\mathrm{point})\times \mathbb{C}}\xleftarrow{} \mathcal{O}_{\mathrm{FHilb}_2(\mathbb{C})}\xleftarrow{x_1-x_2}\mathcal{O}_{\mathrm{FHilb}_2(\mathbb{C})}\xleftarrow{w} \mathcal{O}(-1)_{\mathrm{FHilb}_2(\mathrm{point})\times \mathbb{C}}$$ is self-dual.
:::
