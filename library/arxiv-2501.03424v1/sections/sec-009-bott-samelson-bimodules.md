---
doc_id: arxiv-2501.03424v1
doc_title: "Soergel bimodules and Kazhdan-Lusztig polynomials"
section_id: sec-009-bott-samelson-bimodules
section_title: "Bott-Samelson bimodules"
section_number: null
pages: 6-7
source_pdf: 2501.03424v1.pdf
source_sha256: 53e00a30fd850a5b
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.979
doc_brief: "Soergel bimodules and Kazhdan-Lusztig polynomials — This paper presents an exposition of Soergel bimodules, the categoriﬁcation of Hecke alge- bras, and their applications to various topics in"
---
Let $B_s$ for $s \in S$ denote the graded $R$-bimodule
$$B_s = R \otimes_{R^s}R(1),$$
where $R(1)$ is obtained by shifting down by 1. That is, $M(1)^i \equiv M^{i-1}.$ Elements in $B_s$ are expressable as sums 
$$\sum_i f_i \otimes g_i, \text{ }f_i, g_i \in R.$$
Given a reduced expression $\underbar{$w$} = (s_1, \ldots s_n).$ We define the Bott-Samelson bimodule to be the graded $R$-bimodule 
$$BS(\underbar{$w$}) = B_{s_1}B_{s_2}\cdots B_{s_n},$$
equivalently, 
$$BS(\underbar{$w$}) = R \otimes_{R^{S_1}}R \otimes_{R^{S_2}} \cdots \otimes_{R^{S_n}} R(l(w)).$$
Thus, we express our elements of $BS(\underbar{$w$})$ as 
$$\sum_i f_i \otimes g_i \otimes \cdots \otimes h_i,$$
with of course, $f_i, g_i, \ldots h_i \in R.$ We can now define the titular bimodule of this paper: A \textit{Soergel bimodule} is a direct summand of a finite direct sum of grading shifts of Bott-Samelson bimodules. The category of Soergel bimodules $\mathbb{S}$Bim is the strictly full smallest subcategory of $R$-gbim\ref{app3} (the category of graded $R$-bimodules) containing both $R$ and $B_s$ for every $s \in S$, and is closed under tensor products, direct sums/summands, and grade shifting.
