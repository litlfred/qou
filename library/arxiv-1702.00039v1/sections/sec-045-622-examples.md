---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-045-622-examples
section_title: "Examples"
section_number: 6.2.2
pages: 39-40
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.872
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
Suppose we are in the case $W=S_n$. In this case $R=\mathbb R[x_1,x_2, \ldots, x_n]$ and the group $W$ acts permuting the variables. We have that the simple reflections in $W$ are the $s_i$, the permutation switching the variables $i$ and $i+1$. For simplicity of notation we will denote by $f_{ij}$ the morphism $f_{s_is_j}$ and by $B_i$ the bimodule $B_{s_i}$. In this example we have three cases to consider.

1.  **First case:** $\vert i-j \vert>1$. The morphism $f_{ij}:B_iB_j\rightarrow B_jB_i$ is completeley determined by the formula $f_{ij}(1^{\otimes})=1^{\otimes},$ because the element $1^{\otimes}$ generates $B_iB_j$ as a bimodule.

2.  **Second case:** $j=i+1$. The morphism $f_{ij}:B_iB_{i+1}B_i\rightarrow B_{i+1}B_iB_{i+1}$ is completeley determined by the formulae $f_{ij}(1^{\otimes})=1^{\otimes}$ and $$f_{ij}(1\otimes x_i\otimes 1\otimes 1)=(x_i+x_{i+1})\otimes 1\otimes 1\otimes 1- 1\otimes 1\otimes 1\otimes x_{i+2}$$

3.  **Third case:** $j=i-1$. The morphism $f_{ij}:  B_{i+1}B_iB_{i+1}\rightarrow  B_iB_{i+1}B_i$ is completeley determined by the formulae $f_{ij}(1^{\otimes})=1^{\otimes}$ and $$f_{ij}(1\otimes x_{i+2}\otimes 1\otimes 1)=1\otimes 1\otimes 1\otimes (x_{i+1}+x_{i+2})- x_i\otimes 1\otimes 1\otimes 1.$$
