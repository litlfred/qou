---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS"
section_id: sec-013-6-spans-of-spans
section_title: "Spans of Spans"
section_number: 6
pages: 29-30
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.892
doc_brief: "2-VECTOR SPACES AND GROUPOIDS — This paper describes a relationship between essentially ﬁnite groupoids and 2-vector spaces."
---
[]{#sec:spanspan label="sec:spanspan"}

The situation we are interested in can be represented as an equivalence class of spans of spans of the following sort: $$\label{eq:spanspan}
\xymatrix{
 & X_1 \ar[dl]_{s_1} \ar[dr]^{t_1} & \\
A_1 & Y \ar[u]_{s} \ar[d]^{t} & A_2  \\
 & X_2  \ar[ul]_{s_2} \ar[ur]^{t_2} & \\
}$$

Recall that we assume weak commutativity here - that is, that there are isomorphisms $\zeta_s : s_1 \circ s \mathop{\rightarrow}s_2 \circ t$ and $\zeta_t :
t_1 \circ s \mathop{\rightarrow}t_2 \circ t$.

Given this situation, which is a 2-morphism for the associated bicategory of spans, we want to get a 2-morphism in the bicategory $\boldsymbol{\operatorname{{2Vect}}}$. That is to say, a natural transformation $\alpha=\Lambda(Y)$ between a pair of 2-linear maps. In this section, we show how to construct $\Lambda(Y)$.
