---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-035-10-interpolation-by-q-gevrey-classes
section_title: "Interpolation by $q$-Gevrey classes"
section_number: 10
pages: 48-49
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.878
latex_coverage_ratio: 0.973
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#section:qGevreyinterpolation label="section:qGevreyinterpolation"}

We shall now extend the previous results to $q$-Gevrey classification. We use here notations from paragraph [\[subsection:qGevreylevels\]](#subsection:qGevreylevels){reference-type="ref" reference="subsection:qGevreylevels"} of the general notations in the introduction.

## $q$-Gevrey extension spaces {#subsection:qGevreyExt}

### $q$-Gevrey extensions for arbitrary slopes

If one repaces the field ${{\mathbf C}(\{z\})}$ by the field ${{{\mathbf C}((z))}_{q;s}}$ of $q$-Gevrey series of level $s >0$ and ${{\mathcal{D}}_{q}}$ by ${{\mathcal{D}}_{q,s}}:= {{{\mathbf C}((z))}_{q;s}}\langle T,T^{-1} \rangle$, one gets the abelian category ${DiffMod({{{\mathbf C}((z))}_{q;s}},\sigma_q)}$ and the following extension of the results of [\[subsection:extensionsofqdifferencemodules\]](#subsection:extensionsofqdifferencemodules){reference-type="ref" reference="subsection:extensionsofqdifferencemodules"}.

::: prop
[]{#prop:dimensiondeuxpentesqGevrey label="prop:dimensiondeuxpentesqGevrey"} Let $M,N$ be pure modules of ranks $r,s \in {\mathbf N}^{*}$ and slopes $\mu < \nu \in {\mathbf Q}$ in ${DiffMod({{{\mathbf C}((z))}_{q;s}},\sigma_q)}$. Then one has: $$\dim_{{\mathbf C}} \text{Ext}^{1}(M,N) = \begin{cases}
0 \text{~if~} \nu - \mu \geq 1/s, \\
r s (\nu - \mu) \text{~if~} \nu - \mu < 1/s.
\end{cases}$$
:::

::: proof
*Proof.* This follows indeed, by the same arguments as before, from propositions 3.2 and 3.3 of [@Bezivin]. ◻
:::

This remains true in the extreme case that $s = \infty$, since, over the field ${{\mathbf C}((z))}$, the slope filtration splits and $\text{Ext}^{1}(M,N) = 0$; and also in the extreme case that $s = 0$, by theorem [\[theo:dimensiondeuxpentes\]](#theo:dimensiondeuxpentes){reference-type="ref" reference="theo:dimensiondeuxpentes"}. Therefore, the above proposition is an interpolation between the analytic and formal settings.

### $q$-Gevrey extensions for integral slopes

Here, we extend the results of [\[subsection:twointegralslopes\]](#subsection:twointegralslopes){reference-type="ref" reference="subsection:twointegralslopes"}. If one replaces ${{\mathbf C}(\{z\})}$ by ${{\mathbf C}((z))}$, one gets $V = 0$ in all relations $(F,V) = Red(\mu_{1},A_{1},\mu_{2},A_{2},U)$ and the corresponding space of classes has dimension $0$. The previous algorithm then produces $F = \hat{F}_{U}$ and the "formal normal form" $A_{0}$ of $A$. If one replaces ${{\mathbf C}(\{z\})}$ by ${{{\mathbf C}((z))}_{q;s}}$, one gets $V = 0$ and a matrix $F$ of $g$-Gevrey level $\mu_{2} - \mu_{1}$ if $\mu_{2} - \mu_{1} \geq 1/s$, and the same $Red(\mu_{1},A_{1},\mu_{2},A_{2},U)$ as before otherwise.
