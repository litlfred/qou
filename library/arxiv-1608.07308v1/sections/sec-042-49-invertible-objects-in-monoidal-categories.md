---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-042-49-invertible-objects-in-monoidal-categories
section_title: "Invertible objects in monoidal categories"
section_number: 4.9
pages: 42-42
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.871
latex_coverage_ratio: 0.964
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:invertible label="sub:invertible"}

We summarize several important properties of invertible objects [\[eqn:def invertible\]](#eqn:def invertible){reference-type="eqref" reference="eqn:def invertible"} in arbitrary monoidal categories. The proofs are straightforward, and left as exercises to the interested reader.

::: proposition
[]{#prop:inv label="prop:inv"} For any invertible object $F\in \mathcal{C}$ and two arbitrary objects $C,C'\in \mathcal{C}$, there exist canonical isomorphisms: $$\mathop{\mathrm{Hom}}_{\mathcal{C}}(F \otimes C, F \otimes C') \cong \mathop{\mathrm{Hom}}_{\mathcal{C}}(C,C') \cong \mathop{\mathrm{Hom}}_{\mathcal{C}}(C \otimes F, C' \otimes F)$$
:::

::: corollary
[]{#cor:inv 1 label="cor:inv 1"}

Tensoring with an invertible object and with its inverse yield biadjoint functors, that is, we have canonical isomorphisms: $$\mathop{\mathrm{Hom}}_{\mathcal{C}}(C, F \otimes C') \cong \mathop{\mathrm{Hom}}_{\mathcal{C}}(F^{-1} \otimes C,C') \qquad \mathop{\mathrm{Hom}}_{\mathcal{C}}(C, C' \otimes F) \cong \mathop{\mathrm{Hom}}_{\mathcal{C}}(C \otimes F^{-1},C')$$
:::

::: corollary
[]{#cor:inv 2 label="cor:inv 2"}

For any invertible $F\in \mathcal{C}$ and any object $C\in \mathcal{C}$, we have: $$\mathop{\mathrm{Hom}}_{\mathcal{C}}(\mathbf{1}, F\otimes C) \cong \mathop{\mathrm{Hom}}_{\mathcal{C}}(1, C \otimes F)$$
:::
