---
doc_id: arxiv-2607.10525v1
doc_title: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES"
section_id: sec-002-21-finite-tensor-categories-and-their-module-cat
section_title: "Finite tensor categories and their module categories"
section_number: 2.1
pages: 4-4
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
doc_brief: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES — LetGbe a finite group acting on a finite tensor categoryC."
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.81
---
A *finite tensor category* is a finite abelian category equipped with a rigid monoidal structure, bilinear tensor product, and simple unit [@EO04 Section 2.2]; a *fusion category* is a semisimple finite tensor category.

A left $\mathcal{C}$-module category is a finite abelian category $\mathcal{M}$ with an exact bilinear action $\overline\otimes:\mathcal{C}\times\mathcal{M}\to\mathcal{M}$ and the usual associativity and unit constraints. It is *exact* if $P\overline\otimes M$ is projective whenever $P$ is projective in $\mathcal{C}$, and *indecomposable* if it is not a direct sum of two nonzero module categories. A $\mathcal{C}$-module functor $F:\mathcal{M}\to\mathcal{N}$ is an exact functor equipped with coherent natural isomorphisms $$F(X\overline\otimes M)\xrightarrow{\sim}X\overline\otimes F(M).$$ We write $\operatorname{Fun}_{\mathcal{C}}(\mathcal{M},\mathcal{N})$ for the category of module functors and module natural transformations.

::: remark
If $\mathcal{M}$ is indecomposable and exact, then $$\mathcal{C}^*_{\mathcal{M}}:=\operatorname{Fun}_{\mathcal{C}}(\mathcal{M},\mathcal{M})$$ is a finite tensor category [@EO04 Theorem 3.27]. We use reverse composition, $F\otimes G:=G\circ F$, so that evaluation gives the right action $M\triangleleft F=F(M)$ and the double-dual equivalence $(\mathcal{C}^*_{\mathcal{M}})^*_{\mathcal{M}}\simeq\mathcal{C}$. In this situation $\mathcal{C}$ and $\mathcal{C}^*_{\mathcal{M}}$ are Morita equivalent.
:::
