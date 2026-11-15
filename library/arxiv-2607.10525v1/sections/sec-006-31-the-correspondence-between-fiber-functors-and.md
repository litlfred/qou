---
doc_id: arxiv-2607.10525v1
doc_title: "Fiber Functors of Equivariantizations of Finite Tensor Categories"
section_id: sec-006-31-the-correspondence-between-fiber-functors-and
section_title: "The correspondence between fiber functors and rank-one module categories"
section_number: 3.1
pages: 9-9
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.978
doc_brief: "Fiber Functors of Equivariantizations of Finite Tensor Categories — Let G be a finite group acting on a finite tensor category C."
---
A *fiber functor* on a finite tensor category $\mathcal{C}$ is an exact faithful tensor functor $F:\mathcal{C}\to\mathop{\mathrm{Vec}}_{{\Bbbk}}$. We use the monoidal constraints $$F_2:F(X)\otimes F(Y)\xrightarrow{\sim}F(X\otimes Y),
\qquad
F_0:{\Bbbk}\xrightarrow{\sim}F(\mathbf1),$$ and identify fiber functors that are monoidally naturally isomorphic. A $\mathcal{C}$-module category has *rank one* if its underlying abelian category is equivalent to $\mathop{\mathrm{Vec}}_{{\Bbbk}}$.

::: proposition
[]{#prop:fiber_rank_one label="prop:fiber_rank_one"} There is a bijection between equivalence classes of fiber functors on $\mathcal{C}$ and equivalence classes of exact $\mathcal{C}$-module categories of rank one.
:::

::: proof
*Proof.* Module structures on $\mathop{\mathrm{Vec}}_{{\Bbbk}}$ correspond to tensor functors $\mathcal{C}\to\mathop{\mathrm{Vec}}_{{\Bbbk}}$ [@EGNO15 Proposition 7.3.3 and Example 7.4.6]. Such functors are exact and faithful, and the module category is exact because $\mathop{\mathrm{Vec}}_{{\Bbbk}}$ is semisimple. Transport along an equivalence with $\mathop{\mathrm{Vec}}_{{\Bbbk}}$ gives the converse, while module equivalences correspond to monoidal natural isomorphisms. ◻
:::
