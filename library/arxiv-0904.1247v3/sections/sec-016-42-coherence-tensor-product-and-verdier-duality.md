---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-016-42-coherence-tensor-product-and-verdier-duality
section_title: "Coherence, tensor product, and Verdier duality"
section_number: 4.2
pages: 28-29
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.859
latex_coverage_ratio: 0.973
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
A ${\mathcal D}$-module on a scheme $X$ is coherent if its cohomology sheaves are locally finitely generated ${\mathcal D}_X$-modules. We denote by $\mathcal D_{coh}(X)\subset {\mathcal D}(X)$ the full subcategory of coherent ${\mathcal D}$-modules.

Coherent ${\mathcal D}$-modules are precisely the compact objects of ${\mathcal D}(X)$ and also generate ${\mathcal D}(X)$, so there is a canonical identification $$\xymatrix{
{\mathcal D}(X)\simeq \operatorname{Ind}\mathcal D_{coh}(X)
}$$ Since $f_*$ for proper morphisms is quasi-proper, it preserves coherence, and similarly since $f^*,f^!$ for smooth morphisms are quasi-proper, they preserve coherence. Moreover, the canonical objects $\omega_X, \mathbb C_X\in {\mathcal D}(X)$ are coherent.

External tensor product provides a natural equivalence $$\xymatrix{
\boxtimes:{\mathcal D}(X)\otimes {\mathcal D}(Y)\ar[r]^-\sim &  {\mathcal D}(X\times Y)
}$$ which restricts to an equivalence $$\xymatrix{
\boxtimes:\mathcal D_{coh}(X)\otimes \mathcal D_{coh}(Y)\ar[r]^-\sim &  \mathcal D_{coh}(X\times Y)
}$$

There is a symmetric monoidal structure on ${\mathcal D}(X)$ with multiplication $$\xymatrix{
\otimes: {\mathcal D}(X)\otimes{\mathcal D}(X) \ar[r]^-{\boxtimes} & {\mathcal D}(X \times X) \ar[r]^-{\Delta^!} & {\mathcal D}(X)}$$ where $\Delta:X\to X\times X$ is the diagonal map. The unit is $\omega_X\in {\mathcal D}(X)$. The pullback $f^!$ is symmetric monoidal.

Recall from Section [\[restricted op\]](#restricted op){reference-type="ref" reference="restricted op"} that for a category $\mathcal C= \operatorname{Ind}\mathcal C_{cpt}$, we denote by $\mathcal C_{cpt}^\diamondsuit$ the opposite category of $\mathcal C_{cpt}$, and that the category $\mathcal C'=\operatorname{Ind}(\mathcal C_{cpt}^\diamondsuit)$ is dual to $\mathcal C$.

Verdier duality is the unique involutive equivalence $$\xymatrix{\mathbb D_X:\mathcal D_{coh}(X)^\diamondsuit\ar[r]^-{\sim}& \mathcal D_{coh}(X)}$$ such that there is a functorial equivalence $$\label{Verdier}
\mathop{\mathrm{Hom}}_{{\mathcal D}(X)}(\mathbb D_X(\mathfrak M),\mathfrak N)\simeq \mathop{\mathrm{Hom}}_{{\mathcal D}(X)}(\mathbb C_X, \mathfrak M\otimes\mathfrak N) \qquad
\mathfrak M,\mathfrak N\in \mathcal D_{coh}(X)$$

Note that equation [\[Verdier\]](#Verdier){reference-type="eqref" reference="Verdier"} holds for any $\mathfrak N\in{\mathcal D}(X)$ by continuity.

The continuous extension of Verdier duality to all ${\mathcal D}$-modules provides a canonical self-duality $$\xymatrix{\mathbb D_X:{\mathcal D}(X)' \ar[r]^-{\sim}& {\mathcal D}(X) }$$ Note that equation [\[Verdier\]](#Verdier){reference-type="eqref" reference="Verdier"} now holds for any $\mathfrak M, \mathfrak N\in{\mathcal D}(X)$ by continuity. In particular, equation [\[Verdier\]](#Verdier){reference-type="eqref" reference="Verdier"} presents the counit of the canonical self-duality in the form $$\xymatrix{
{\mathcal D}(X)\otimes {\mathcal D}(X)\ar[r] & {\mathcal D}(X) & \mathfrak M\otimes \mathfrak N\ar@{|->}[r] & \Gamma_{dR}(\mathfrak M\otimes \mathfrak N)
}$$

For a smooth morphism $f:X\to Y$, there is a canonical equivalence $f^*\simeq\mathbb D_X f^! \mathbb D_Y$, and in particular, $\mathbb D_X$ exchanges $\mathbb C_X$ and $\omega_X$. For a proper morphism $f:X\to Y$, there is a canonical equivalence $f_*\simeq \mathbb D_Y f_* \mathbb D_X$.[^1]

[^1]: We thank N. Rozenblyum for pointing out this follows from the adjunction $(f_*,f^!)$ for proper maps together with the identification of $f^!$ with the transpose of $f_*$ for arbitrary maps.
