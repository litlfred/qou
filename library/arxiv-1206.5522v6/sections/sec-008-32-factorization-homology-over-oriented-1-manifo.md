---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-008-32-factorization-homology-over-oriented-1-manifo
section_title: "Factorization homology over oriented 1-manifolds with boundary"
section_number: 3.2
pages: 17-18
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.975
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds, after Beilinson, Drinfeld and Lurie, are homology-type theories for topological n-manifolds"
---
[]{#sec.interval label="sec.interval"} We show that factorization homology of a closed interval is a two-sided bar construction.

The data of an oriented embedding $U\hookrightarrow [-1,1]$ from a finite disjoint union of oriented intervals, determines a linear ordering of the connected components of $U$. This is organized as a monoidal functor between $\infty$-operads $$\label{interval-assoc}
\mathop{\mathrm{{\mathcal D}\sf isk}}^{\partial, {\sf or}}_{1/[-1,1]} \longrightarrow {\sf Assoc}_{\sf RL}$$ to the standard multi-category corepresenting the datum of an associative algebra $A$, together with a unital right module $T$ and a unital left module $S$. Because the space of oriented embeddings between two oriented intervals is contractible, this functor ([\[interval-assoc\]](#interval-assoc){reference-type="ref" reference="interval-assoc"}) is an equivalence of $\infty$-operads. In summary, there is an equivalence of $\infty$-categories $$\label{assoc-disk}
\mathop{\mathrm{\mathsf{Alg}}}_{\sf RL}(\mathcal V) \xrightarrow{~\simeq~} \mathop{\mathrm{\sf Fun}}^\otimes\bigl(\mathop{\mathrm{{\mathcal D}\sf isk}}_{1/[-1,1]}^{\partial, \sf or}, \mathcal V\bigr)$$ where the lefthand $\infty$-category is that of algebras over ${\sf Assoc}_{\sf RL}$.

::: example
[]{#ex.assoc label="ex.assoc"} Through ([\[assoc-disk\]](#assoc-disk){reference-type="ref" reference="assoc-disk"}), there is a functor $\mathop{\mathrm{\mathsf{Alg}}}^{\sf aug}_{\sf Assoc}(\mathcal V) \to\mathop{\mathrm{\sf Fun}}^\otimes\bigl(\mathop{\mathrm{{\mathcal D}\sf isk}}_{1/[-1,1]}^{\partial, \sf or}, \mathcal V\bigr)$ from augmented associative algebras in $\mathcal V$.
:::

The next result gives a functor from the simplicial category to 1-disks by a standard construction of counting gaps. Our proof is terse; a lengthier treatment is available in §2 of [@aft2].

::: lemma
There is a functor $\mathop{\mathrm{\boldsymbol{\Delta}}}^{\mathop{\mathrm{\mathsf{op}}}} \rightarrow\mathop{\mathrm{{\mathcal D}\sf isk}}^{\partial,{\sf or}}_{1/[-1,1]}$ which is final.
:::

::: proof
*Proof.* Let $S\subset \mathop{\mathrm{{\mathcal D}\sf isk}}^{\partial,{\sf or}}_{1/[-1,1]}$ be the full $\infty$-subcategory of embeddings from oriented intervals that surject onto the endpoints. That is, $S$ consists of oriented embeddings among 1-manifolds with boundary of the form $[-1, 0) \sqcup \mathbb R^{\sqcup \ell} \sqcup (0,1]\hookrightarrow [-1,1]$, for $\ell\geq 0$. To show the inclusion $S\subset \mathop{\mathrm{{\mathcal D}\sf isk}}^{\partial,{\sf or}}_{1/[-1,1]}$ is final, by Quillen's Theorem A, we can show the under $\infty$-category $S^{U/}$ has a contractible classifying space for every finite disjoint union of subintervals $U\subset[-1,1]$. This is immediate, because $S^{U/}$ has an initial object, which is a disjoint union of $U$ with connected open neighborhoods of the endpoints not contained in $U$.

Lastly, the result follows because there is an equivalence $S\to \mathop{\mathrm{\boldsymbol{\Delta}}}^{\mathop{\mathrm{\mathsf{op}}}}$. On objects this is given by assigning to $(U\hookrightarrow [-1,1])$ the set connected components of the complement $\bigl[ [-1,1]\smallsetminus U\bigr]$ together with the linear order inherited from that of $[-1,1]$. That this assignment defines a functor is routine. That this functor is an equivalence of $\infty$-categories follows because each comopnent of the space of morphisms of $\mathop{\mathrm{{\mathcal D}\sf isk}}^{\partial, \sf or}_{1/[-1,1]}$ is contractible. ◻
:::

This has an immediate corollary, which states that factorization homology over a closed interval is a two-sided bar construction.

::: cor
[]{#interval label="interval"} For $\mathcal V$ a symmetric monoidal $\mathop{\mathrm{\infty}}$-category which is $\otimes$-presentable, and for $R:  \mathop{\mathrm{{\mathcal D}\sf isk}}^{\partial,{\sf or}}_{1}\rightarrow\mathcal V$ a symmetric monoidal functor, there is a natural equivalence in $\mathcal V$: $$R\bigl([-1,1)\bigr)\underset{R\bigl((-1,1)\bigr)}\bigotimes R\bigl((-1,1]\bigr)  \xrightarrow{~\simeq~} \int_{[-1,1]} R~.$$
:::
