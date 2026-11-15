---
doc_id: arxiv-1012.5432v4
doc_title: "Towards topological quantum computation? Knotting and fusing flux tubes"
section_id: sec-023-e-spin-and-the-t-matrix
section_title: "E Spin and the T-Matrix"
section_number: null
pages: 20-20
source_pdf: 1012.5432v4.pdf
source_sha256: ec5f6da1f813649e
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Towards topological quantum computation? Knotting and fusing flux tubes — 56 sections: Front matter; I Introduction; II (2+1)-dimensional Topological G"
---
The diagonal T-matrix records the information about the spins. Explicitly, the T matrix is given by:

$$T_{\alpha \beta}^{AB} := \delta_{\alpha,\beta} \delta^{A,B} e^{2\pi i s_{(A, \alpha)}}$$

Within each internal Hilbert space, all particles carry the same spin. Furthermore, the only particles which have nontrivial spin are dyons with both nontrivial flux and nontrivial charge. Note that in the construction for the quantum double, by definition the conjugacy class A representative element $^A h_1$ commutes with all elements in the centralizer $^A N$, so Schur's lemma yields:

$$\alpha(^A h_1) = e^{2 \pi i s_{(A, \alpha)}} \textbf{1}_{\alpha}$$

for every irreducible representation $\alpha$. This formula is implemented in the MAGMA program to yield the values of the spin for the various anyonic particles. While this does not distinguish between spin $s=0$ and $s=1$, it does the best that is possible in any superselection sector as it is always possible to add orbital angular momentum. In the specific groups discussed in the next section, a number of exotic spins are discovered.
