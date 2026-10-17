---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-004-23-module-categories-the-dual-category-the-drinf
section_title: "Module categories, the dual category, the Drinfeld center"
section_number: 2.3
pages: 6-7
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
Let ${\mathcal M}$ be an indecomposable left module category over a rigid tensor category ${\mathcal C}$ [@O] (all module categories we consider are assumed semisimple). This means, ${\mathcal M}$ is a module category which cannot be split in a direct sum of two nonzero module subcategories. In this case one can define the dual category ${\mathcal C}^*_{{\mathcal M}}$ to be the category of module functors from ${\mathcal M}$ to itself: ${\mathcal C}^*_{{\mathcal M}}={\rm Fun}_{\mathcal C}({\mathcal M},{\mathcal M})$ [@O]. This is a rigid tensor category (the tensor product is the composition of functors, the right and left duals are the right and left adjoint functors).

For example, let us consider ${\mathcal C}$ itself as a module category over ${\mathcal C}\otimes {\mathcal C}^{op}$, via $(X,Y)\otimes Z=X\otimes Z\otimes Y$. Then the dual category is the Drinfeld center $Z({\mathcal C})$ of ${\mathcal C}$ (see [@O1; @Mu2]; for the basic theory of the Drinfeld center see [@K]).

The following result was proved by Müger [@Mu1; @Mu2] under the assumption $\dim({\mathcal C})\ne 0$ (which, as we have seen, is superfluous in zero characteristic) and minor additional assumptions.

::: theorem
[]{#dualcat label="dualcat"} For any indecomposable module category ${\mathcal M}$ over a fusion category ${\mathcal C}$, the category ${\mathcal C}^*_{{\mathcal M}}$ is semisimple (so it is a fusion category), and $\dim({\mathcal C}^*_{{\mathcal M}})=\dim({\mathcal C})$. In particular, for any fusion category ${\mathcal C}$ the category $Z({\mathcal C})$ is a fusion category of global dimension $\dim({\mathcal C})^2$.
:::

In fact, we have the following more general results, which (as well as the results in the next subsection) are inspired by [@Mu1; @Mu2].

::: theorem
[]{#m1m2 label="m1m2"} For any module categories ${\mathcal M}_1,{\mathcal M}_2$ over a fusion category ${\mathcal C}$, the category of module functors ${\rm Fun}_{{\mathcal C}}({\mathcal M}_1,{\mathcal M}_2)$ is semisimple.
:::

Theorems [\[dualcat\]](#dualcat){reference-type="ref" reference="dualcat"} and [\[m1m2\]](#m1m2){reference-type="ref" reference="m1m2"} are proved in Section 5.
