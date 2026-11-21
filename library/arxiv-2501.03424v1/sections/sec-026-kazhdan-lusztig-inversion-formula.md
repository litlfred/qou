---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials"
section_id: sec-026-kazhdan-lusztig-inversion-formula
section_title: "Kazhdan-Lusztig Inversion Formula"
section_number: null
pages: 12-13
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.953
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials — This paper presents an exposition of Soergel bimodules, the categoriﬁcation of Hecke alge- bras, and their applications to various topics in"
---
Let $w_0 \in W$ be the longest eleemnt. For every $x,y \in W,$ we have the identity
$$\sum_{z \in W}(-1)^{l(y) + l(x)}h_{z,x}(v)h_{zw_0, yw_0}(v) = \begin{cases}
    1 \text{ if } x = y \\
    0 \text{ else}
\end{cases}$$

Along with the previous conjecture, this implies a similar identity in the Grothendieck group of $\mathcal{O}$:

$$[L_{(y\cdot 0)}] = \sum_{y \le x}(-1)^{l(y) + l(x)}h_{xw_0, yw_0}(1)[M_{(x\cdot 0)}].$$

At this point, we might find ourselves asking some questions about what exactly Kazhdan-Lusztig polynomials are. To try shedding some light, we turn to the following theorem of of Polo \ref{ref11}, stating roughly that any polynomial with positive coefficients is a Kazhdan-Lusztig polynomial in some symmetric group.
