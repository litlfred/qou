---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-025-62-the-case-of-two-slopes
section_title: "The case of two slopes"
section_number: 6.2
pages: 31-32
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.891
latex_coverage_ratio: 0.964
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:thecaseoftwoslopes label="subsection:thecaseoftwoslopes"}

The case $k = 1$ is of course trivial. The case where $k = 2$ is "linear" or "abelian": the set of classes is naturally a finite dimensional vector space over ${\mathbf C}$. We call it "one level case", because the *$q$-Gevrey level* $\mu_{2} - \mu_{1}$ (see the paragraph [\[subsection:qGevreylevels\]](#subsection:qGevreylevels){reference-type="ref" reference="subsection:qGevreylevels"} of the general notations in the introduction for its definition) is the fundamental parameter. This will be illustrated in section [\[section:qGevreyinterpolation\]](#section:qGevreyinterpolation){reference-type="ref" reference="section:qGevreyinterpolation"}, in chapter [\[chapter:asymptotictheory\]](#chapter:asymptotictheory){reference-type="ref" reference="chapter:asymptotictheory"}. Let $P,P'$ be pure analytic $q$-difference modules with ranks $r,r'$ and slopes $\mu < \mu'$.

[]{#not27 label="not27"}

::: prop
[]{#prop:classesaunniveau=Ext label="prop:classesaunniveau=Ext"} There is a natural one-to-one correspondance: $${\mathcal{F}}(P,P') \rightarrow \text{Ext}(P',P).$$
:::

::: proof
*Proof.* Here, $\text{Ext}$ denotes the space of extension classes in the category of left ${{\mathcal{D}}_{q}}$-modules; the homological interpretation is discussed in the remark below.\
Note that an extension of ${{\mathcal{D}}_{q}}$-modules of finite length has finite length, so that an extension of $q$-difference modules is a $q$-difference module. To give $g: {\text{gr}}M \simeq P \oplus P'$ amounts to give an isomorphism $M_{\leq \mu} \simeq P$ and an isomorphism $M/M_{\leq \mu} \simeq P'$, *i.e.* a monomorphism $i: P \rightarrow M$ and an epimorphism $p: M \rightarrow P'$ with kernel $i(P)$, *i.e.* an extension of $P'$ by $P$. Reciprocally, for any such extension, one automatically has $M_{\leq \mu} = i(P)$, thus an isomorphism $g: {\text{gr}}M \simeq P \oplus P'$. The condition of equivalence of pairs $(M,g)$ is then exactly the condition of equivalence of extensions. ◻
:::

::: rema
By the classical identification of $\text{Ext}$ spaces with $\text{Ext}^{1}$ modules, we thus get a description of ${\mathcal{F}}(P,P')$ as a ${\mathbf C}$-vector space. We shall have use for an explicit description of this structure in terms of matrices: this will be given in section [\[section:extdiffmod\]](#section:extdiffmod){reference-type="ref" reference="section:extdiffmod"} of the appendix.
:::
