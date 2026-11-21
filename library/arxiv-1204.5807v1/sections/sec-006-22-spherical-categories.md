---
doc_id: arxiv-1204.5807v1
doc_title: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES"
section_id: sec-006-22-spherical-categories
section_title: "Spherical Categories"
section_number: 2.2
pages: 7-7
source_pdf: 1204.5807v1.pdf
source_sha256: 4bf4f73b0c152b19
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.906
doc_brief: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES — This is a survey on spherical Hopf algebras. We give criteria to decide when a Hopf algebra is spherical and collect examples."
---
A monoidal rigid category ${\mathcal C}$ is pivotal when $X^{**}$ is monoidally isomorphic to $X$ [@FY-adv]; this implies that the left and right dualities coincide. For instance, if $H$ is a Hopf algebra and $\omega\in G(H)$ is a pivot, then $\operatorname{Rep}H$ is pivotal [@BaW-adv Proposition 3.6]. In a pivotal category ${\mathcal C}$, there are left and right traces $\operatorname{tr}_L, \operatorname{tr}_R: \operatorname{End}(X) \to \operatorname{End}({\bf 1})$, for any $X\in {\mathcal C}$. If ${\mathcal C}= \operatorname{Rep}H$ and $V\in \operatorname{Rep}H$, then these traces are defined by $$\begin{aligned}
\label{eq:tr-sph-Ha}
\operatorname{tr}_L(\vartheta) &= \operatorname{tr}_V(\vartheta \omega), & \operatorname{tr}_R(\vartheta)  &= \operatorname{tr}_V(\vartheta \omega^{-1}), & \vartheta &\in \operatorname{End}_H(V).
\end{aligned}$$ A spherical category is a pivotal one where the left and right traces coincide. Thus, $\operatorname{Rep}H$ is a spherical category, whenever $H$ is a spherical Hopf algebra.

::: Rem
[]{#obs:spherical-subcat label="obs:spherical-subcat"} If ${\mathcal D}$ is a rigid monoidal (full) subcategory of a spherical category ${\mathcal C}$, then ${\mathcal D}$ is also spherical.
:::
