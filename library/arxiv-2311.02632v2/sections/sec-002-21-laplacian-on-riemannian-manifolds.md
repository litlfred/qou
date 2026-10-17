---
doc_id: arxiv-2311.02632v2
doc_title: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE"
section_id: sec-002-21-laplacian-on-riemannian-manifolds
section_title: "Laplacian on Riemannian manifolds"
section_number: 2.1
pages: 4-5
source_pdf: 2311.02632v2.pdf
source_sha256: 0da5ba097b79340d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.912
doc_brief: "SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE — The Fricke-Macbeath surface is the unique Hurwitz surface of genus 7 with 504 conformal automorphisms."
---
In this subsection, we provide a brief review of the properties of the Laplacian on a Riemannian manifold. For a detailed discussion on this topic, see [@MR2742784]. Consider a Riemannian manifold $M$ with the metric given by $$ds^2 = \sum_{j,k} g_{jk} dx^j dx^k.$$ The Laplacian $\Delta$, acting on $C^\infty(M)$, can be locally expressed by: $$\Delta = -\sum_{j,k} \frac{1}{\sqrt{\det g}} \frac{\partial}{\partial x^j}
\left( \sqrt{\det g}\, g^{jk} \frac{\partial}{\partial x^k} \right),$$ where $g^{jk}$ are the entries of the inverse matrix of $(g_{jk})$ and $\det g$ stands for the determinant of the matrix $(g_{jk})$. For a compact connected manifold, $\Delta$ has non-negative discrete eigenvalues $$0=\la_0< \la_1 \leq \la_2 \leq \ldots \to \infty,$$ with corresponding $C^{\infty}$-eigenfunctions given by $$\Delta \phi_{i}=\la_{i} \phi_{i},$$ which together provide an orthonormal basis for $L^{2}(M)$.

For a Riemannian manifold, the Laplacian $\Delta$ commutes with isometries of $M$. This implies that for an eigenfunction $f$ of $\Delta$ and an isometry $g$, $f\circ g^{-1}$ is an eigenfunction with the same eigenvalue as $f$. Consequently, the complex vector space of eigenfunctions with a given eigenvalue becomes a representation for a group of isometries of $M$.
