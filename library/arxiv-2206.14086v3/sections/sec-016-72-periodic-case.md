---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems"
section_id: sec-016-72-periodic-case
section_title: "Periodic case"
section_number: 7.2
pages: 10-10
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
toc_source: outline
text_source: latex
latex_prose_ratio: 0.848
latex_coverage_ratio: 0.968
doc_brief: "KPZ limit theorems — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
The formula of [@Baik-Liu19] is $$\label{eq:PKPZformula}
    F^{\mathrm{pKPZ}}_m(\mathsf{h}; \gamma, \tau)
    = \oint \cdots \oint  C(\zeta) \det(\mathsf{1}-\mathsf{K}_\zeta)   \mathrm{d}\zeta_1 \cdots \mathrm{d}\zeta_{m},$$ where this time there are $m$ integrals and $C(\zeta)$ is an explicit function expressed in terms of polylog functions. The kernel of the operator $\mathsf{K}_\zeta$ is of the same form as [\[eq:kpzKkernel\]](#eq:kpzKkernel){reference-type="eqref" reference="eq:kpzKkernel"} but $\mathsf{a}(z)$ and $\mathsf{b}(z)$ are slightly different. The key change is the space for $\mathsf{K}_{\zeta}$. It is $\ell^2(\mathsf{S})$, where $\mathsf{S}= \mathsf{S}_1\cup\cdots \cup \mathsf{S}_m$ and $\mathsf{S}_i$ is the discrete set of the roots of the equation $$\label{eq:Betheeqlimit}
    e^{-s^2/2}= \zeta_i ,$$ shown in Figure [\[fig:periodicKPZset\]](#fig:periodicKPZset){reference-type="ref" reference="fig:periodicKPZset"}. See the following subsection for how this equation arises.
