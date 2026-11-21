---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS"
section_id: sec-003-13-entropy
section_title: "Entropy"
section_number: 1.3
pages: 3-3
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.835
latex_coverage_ratio: 1.0
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry between a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
Corollary [\[Cor:Faithful2\]](#Cor:Faithful2){reference-type="ref" reference="Cor:Faithful2"} is essentially equivalent to a related dynamical statement. For a symplectic manifold $X$ the (conjugation-invariant) *Floer-theoretic entropy* of a mapping class $\phi \in \operatorname{Symp}(X)/\operatorname{Ham}(X)$ is $$h_{Floer}(\phi) \ = \ \limsup \frac{1}{n} \log \operatorname{rk}\, HF(\phi^n).$$ This is a kind of robust version of the periodic entropy, robust in the sense that it depends on a symplectic diffeomorphism only through its mapping class; by contrast topological and periodic entropy are typically very sensitive to perturbation. For area-preserving diffeomorphisms of a surface $\Sigma$, the Floer-theoretic entropy (of the action on $\Sigma$ itself) co-incides with the minimum of topological or periodic entropy amongst representatives of the mapping class [@Cotton-Clay; @FLP; @Felshtyn]; moreover, $h_{Floer}(\phi)>0 \Leftrightarrow \phi$ has a pseudo-Anosov component. In this low dimension, these phenomena are basically detected by the fundamental group.

::: Theorem
[]{#Thm:Entropy label="Thm:Entropy"} A diffeomorphism $\phi \in \tilde{\Gamma}_g^{hyp}$ has a pseudo-Anosov component if and only if the induced map on $Q_0 \cap Q_1$ has positive Floer-theoretic entropy.
:::

This seems to be one of the few computations of non-zero Floer-theoretic entropy in a closed symplectic manifold which is not detected by classical topology. Analogous results for symplectomorphisms of certain $K3$ surfaces can be derived from combining [@Seidel:graded] and [@KhovanovSeidel].
