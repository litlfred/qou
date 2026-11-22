---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-014-3-hopf-monads
section_title: "Hopf monads"
section_number: 3
pages: 11-12
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.882
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
[]{#Sect-monad label="Sect-monad"}

In this section, we review some facts on Hopf monads [@BV2].

## Monads

Let $\mathcal{C}$ be a category. Recall that the category $\mathrm{End}(\mathcal{C})$ of endofunctors of $\mathcal{C}$ is strict monoidal with composition for monoidal product and identity functor $1_\mathcal{C}$ for unit object.

A *monad* on $\mathcal{C}$ (also called a *triple*) is an algebra in $\mathrm{End}(\mathcal{C})$, that is, a triple $(T,\mu,\eta)$, where $T\colon\mathcal{C}\to \mathcal{C}$ is a functor, $\mu\colon T^2 \to T$ and $\eta\colon 1_\mathcal{C}\to T$ are natural transformations, such that: $$\mu_X T(\mu_X)=\mu_X\mu_{T(X)} \quad \text{and} \quad \mu_X\eta_{T(X)}=\mathrm{id}_{T(X)}=\mu_X T(\eta_X)$$ for any object $X$ of $\mathcal{C}$.
