---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-009-31-preliminaries
section_title: "Preliminaries"
section_number: 3.1
pages: 16-17
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.955
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
Our working setting is the higher category theory and algebra developed by J. Lurie [@topos; @HA; @SAG], see Chapter I.1 of [@GR] for an excellent overview.

Throughout what follows, we will fix once and for all a symmetric monoidal $(\oo, 2)$-category $\cA$ with unit object $1_\cA$. By forgetting non-invertible 2-morphisms we obtain a symmetric monoidal $(\oo,1)$-category $f(\cA)$, which we will abusively refer to as $\cA$ whenever only invertible higher morphisms are involved. Conversely, given a symmetric monoidal $(\oo, 1)$-category $\cC$, we can always regard it as a symmetric monoidal $(\oo, 2)$-category $i(\cC)$ with all $2$-morphisms invertible.[^1] Thus developments for higher $\oo$-categories equally well apply to the more familiar $(\oo,1)$-categories. In what follows, noninvertible 2-morphisms only play a significant role starting with Section [\[dim functorial section\]](#dim functorial section){reference-type="ref" reference="dim functorial section"}.

We will use $\otimes$ to denote the symmetric monoidal structure of $\cA$. We will write $\Omega\cA= \End_\cA(1_\cA)$ for the "based loops\" in $\cA$, or in other words, the symmetric monoidal $(\oo, 1)$-category of endomorphisms of the monoidal unit $1_\cA$. Note that the monoidal unit $1_{\Omega\cA}$ is nothing more than the identity $\id_{1_\cA}$ of the monoidal unit $1_\cA$.

::: example
Fix a symmetric monoidal $(\oo, 1)$-category $\cC$, and let $\cA = \Alg(\cC)$ denote the Morita $(\oo,2)$-category of algebras, bimodules, and intertwiners of bimodules within $\cC$. The forgetful map $\cA = \Alg(\cC) \to \cC$ is symmetric monoidal, and in particular, the monoidal unit $1_\cA$ is the monoidal unit $1_\cC$ equipped with its natural algebra structure. Finally, we have $\Omega\cA\simeq \cC$.

For a specific example, one could take $\cC =k\module=dgVect_k$ the $(\oo,
1)$-category of complexes of $k$-modules (with quasi-isomorphisms inverted). Then $\cA = \Alg(\cC)$ is the $(\oo, 2)$-category of $k$-algebras, bimodules, and intertwiners of bimodules.
:::

::: example
A natural source of $(\oo,2)$-categories is given by various theories of $(\oo,1)$-categories. For example, one could consider $\udg_k$, the $(\oo,2)$-category of $k$-linear stable presentable $\oo$-categories (or $k$-linear presentable dg categories), $k$-linear continuous functors, and natural transformations.

Observe that $\Alg(k\module)$ is a full subcategory of $\udg_k$, via the functor assigning to a $k$-algebra its stable presentable $\oo$-category of modules. The essential image consists of dg categories admitting a compact generator.
:::

[^1]: One can understand the above two operations as forming an adjoint pair $(i, f)$.
