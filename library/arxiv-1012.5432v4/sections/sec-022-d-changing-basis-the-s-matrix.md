---
doc_id: arxiv-1012.5432v4
doc_title: "Towards topological quantum computation? Knotting and fusing flux tubes"
section_id: sec-022-d-changing-basis-the-s-matrix
section_title: "D Changing Basis: The S-Matrix"
section_number: null
pages: 19-20
source_pdf: 1012.5432v4.pdf
source_sha256: ec5f6da1f813649e
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Towards topological quantum computation? Knotting and fusing flux tubes — 56 sections: Front matter; I Introduction; II (2+1)-dimensional Topological G"
---
The S-matrix implements the change of basis between the given basis of the fusion algebra and the diagonal basis. (Such a matrix S must exist since the algebra is commutative and associative.) Explicitly, the S matrix can be written as:

$$S_{\alpha \beta}^{AB} := \dfrac{1}{|H|} tr \textrm{ }R^{-2}{ }^{AB}_{\alpha \beta}$$ $$= \dfrac{1}{|H|} \sum_{^Ah_i \in ^AC, ^Bh_j \in ^BC: [^Ah_i, ^Bh_j]=e} tr(\alpha(^Ax_i^{-1} { }^Bh_j ^Ax_i))^* tr (\beta(^Bx_j^{-1}{ }^Ah_i ^Bx_j))^*$$

In the appendices, a MAGMA program that computes the S matrix values is included.
