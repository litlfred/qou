---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-015-414-extension-of-scalars
section_title: "Extension of scalars"
section_number: 4.1.4
pages: 19-20
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 0.964
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
An extension difference field $(K',\sigma')$ of $(K,\sigma)$ consists in an extension $K'$ of $K$ and an automorphism $\sigma'$ of $K'$ which restricts to $\sigma$ on $K$. Any difference module $M = (E,\Phi)$ over $(K,\sigma)$ then gives rise to a difference module $M' = (E',\Phi')$ over $(K',\sigma')$, where $E' := K' \otimes_{K} E$ and $\Phi' := \sigma' \otimes \Phi$ is defined the same way as above. We then write $\Gamma_{K'}(M)$ the ${K'}^{\sigma'}$-vector space $\Gamma(M')$. The *functor of solutions (with values) in $K'$* is defined as $M \leadsto \Gamma(M')$; it is left exact and $K^{\sigma}$-linear. The functor $M \leadsto M'$ from $DiffMod(K,\sigma)$ to $DiffMod(K',\sigma')$ is compatible with unity, internal Hom, tensor product and dual. The image of $M =(K^{n},\Phi_{A})$ is $M' =({K'}^{n},\Phi_{A})$.

## $q$-difference modules

[]{#subsection:qdiffmods label="subsection:qdiffmods"}

[]{#not18 label="not18"} We now restrict our attention to the difference fields $\bigl({{\mathbf C}(\{z\})},\sigma_q\bigr)$ and $\bigl({{\mathbf C}((z))},\sigma_q\bigr)$, and to the corresponding categories of analytic, resp. formal, $q$-difference modules: they are ${\mathbf C}$-linear abelian categories since ${{\mathbf C}(\{z\})}^{\sigma_q} = {{\mathbf C}((z))}^{\sigma_q} = {\mathbf C}$. In both settings, we consider the $q$-difference module $M =(K^{n},\Phi_{A})$ as an abstract model for the linear $q$-difference system $\sigma_qX = A X$. Isomorphisms from (the system with matrix) $A$ to (the system with matrix) $B$ in either category correspond to analytic, resp. formal, gauge transformations, *i.e.* matrices $F \in {\text{GL}}_{n}({{\mathbf C}(\{z\})})$, resp. $F \in {\text{GL}}_{n}({{\mathbf C}((z))})$, such that $B = F[A] := (\sigma_qF) A F^{-1}$. We write ${{\mathcal{D}}_{q}}$ indifferently for ${\mathcal{D}}_{{{\mathbf C}(\{z\})},\sigma_q}$ or ${\mathcal{D}}_{{{\mathbf C}((z))},\sigma_q}$ when the distinction is irrelevant.

::: lemm
[]{#lemm:cyclicvector label="lemm:cyclicvector"} Any (analytic or formal) $q$-difference module is isomorphic to a module ${{\mathcal{D}}_{q}}/{{\mathcal{D}}_{q}}P$ for some unitary entire $q$-difference operator $P$.
:::

::: proof
*Proof.* See [@LDV], [@JSAIF]. ◻
:::

Note however that the ideal ${{\mathcal{D}}_{q}}P$, and thus its generator $P$, are by no means unique, since they depend on the choice of a cyclic vector. For instance, it is an easy exercice to show that the operators $P := \sigma_q- a$ and $P' := \sigma_q- a'$ (with $a,a' \in K^{*}$) give rise to isomorphic modules ${{\mathcal{D}}_{q}}/{{\mathcal{D}}_{q}}P \simeq {{\mathcal{D}}_{q}}/{{\mathcal{D}}_{q}}P'$ if, and only if, $a'/a$ belongs to the subgroup $\{\frac{\sigma b}{b} ~ | ~b \in K^{*}\}$ of $K^{*}$ ([@LDVS], exemple 3.9).

::: theo
[]{#theo:quasitannakiennes label="theo:quasitannakiennes"} The categories ${DiffMod({{\mathbf C}(\{z\})},\sigma_q)}$ and ${DiffMod({{\mathbf C}((z))},\sigma_q)}$ are abelian ${\mathbf C}$-linear rigid tensor categories.
:::

::: proof
*Proof.* See for instance [@vdPS], [@JSGAL]. (From proposition 3.1 of [@RS1], it actually follows that ${DiffMod({{\mathbf C}(\{z\})},\sigma_q)}$ is a neutral tannakian category, and the same is true for ${DiffMod({{\mathbf C}((z))},\sigma_q)}$ by [@vdPS] or [@vdPR], but we won't use these facts.) ◻
:::
