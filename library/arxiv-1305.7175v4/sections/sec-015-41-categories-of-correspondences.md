---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-015-41-categories-of-correspondences
section_title: "Categories of correspondences"
section_number: 4.1
pages: 24-25
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.91
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
For concreteness, we fix a base commutative ring, and work in the symmetric monoidal $(\oo,1)$-category $Stacks_k$ of derived stacks over $\Spec k$. It is worth pointing out that the constructions of this section apply in any presentable $\oo$-category with the Cartesian symmetric monoidal structure.

Let $Corr_k$ denote the symmetric monoidal $\oo$-category of correspondences in $Stacks_k$. Thus morphisms are given by the classifying space of correspondences $$\xymatrix{X&\ar[l]\ar[r] Z & Y}$$ so all higher morphisms are isomorphisms. Composition of correspondences is given by the derived fiber product. The based loop category $$\Omega Corr_k=\End_{Corr_k}(\Spec k)\simeq Stacks_k$$ is again derived stacks, regarded as self-correspondences of the point $\Spec k$.

We will also enhance $Corr_k$ to the symmetric monoidal $(\oo,2)$-category $\ul{Corr}_k$ where we now allow noninvertible maps of correspondences $$\xymatrix{& Z \ar[ld]\ar[rd] \ar[dd] &\\
X & & Y\\
& W\ar[ul]\ar[ur] &}$$ In other words, the morphisms $\ul{Corr}_k(X,Y)$ now form the $\oo$-category $Stacks_{/X\times Y}$ of stacks over $X\times Y$ with arbitrary morphisms rather than isomorphisms as in $Corr_k(X,Y)$.

We will also have need to restrict the class of morphisms of correspondences to some subcategory of $Stacks_{/X\times Y}$. In particular, we will consider the subcategory $\ul{Corr}_k^{prop}$ in which we only allow proper maps of correspondences.
