---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-002-21-tensor-ideals
section_title: "Tensor ideals"
section_number: 2.1
pages: 3-4
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.974
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
Let ${\bold k}$ be a field and let $\mathcal{C}$ be a ${\bold k}-$linear monoidal category. Recall that a *tensor ideal* $I$ in $\mathcal{C}$ is a collection of subspaces $I(X,Y)\subset \mathrm{Hom}(X,Y)$ for all $X,Y\in \mathcal{C}$ such that for all $X,Y,Z,T \in \mathcal{C}$

\(1\) for $\alpha \in I(X,Y)$ and $\beta \in \mathrm{Hom}(Y,Z), \gamma \in \mathrm{Hom}(Z,X)$ we have $\alpha \circ \gamma \in I(Z,Y)$ and $\beta \circ \alpha \in I(X,Z)$;

\(2\) for $\alpha \in I(X,Y), \beta \in \mathrm{Hom}(Z,T)$ we have $\alpha \otimes\beta \in
I(X\otimes Z, Y\otimes T)$ and $\beta \otimes\alpha \in I(Z\otimes X, T\otimes Y)$.

If $I$ is a tensor ideal in $\mathcal{C}$ then one can define a new ${\bold k}-$linear monoidal category $\mathcal{C}'$ (the *quotient* of $\mathcal{C}$ by $I$) as follows: the objects of $\mathcal{C}'$ are the objects of $\mathcal{C}$; $\mathrm{Hom}_{\mathcal{C}'}(X,Y):=\mathrm{Hom}_\mathcal{C}(X,Y)/I(X,Y)$; the composition of morphisms is the same as in $\mathcal{C}$ (note that condition (1) ensures that the composition is well defined); the tensor product is the same as in $\mathcal{C}$ (well defined thanks to condition (2)).

Moreover, the identity map on the objects and morphisms induces a canonical quotient monoidal functor $\mathcal{C}\to \mathcal{C}'$.

It is clear that if $\mathcal{C}$ is rigid, pivotal, spherical, braided, symmetric then so is $\mathcal{C}'$.
