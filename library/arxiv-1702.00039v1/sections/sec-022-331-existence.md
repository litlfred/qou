---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-022-331-existence
section_title: "Existence"
section_number: 3.3.1
pages: 18-18
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.935
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
[]{#1 label="1"}

We prove it by induction on the Bruhat order. It is clear that $b_e=h_e=1$ and we have already seen in equation ([\[bs\]](#bs){reference-type="ref" reference="bs"}) that $b_s=h_s+v.$ The following equation is easy (see the important property in Section [\[imp\]](#imp){reference-type="ref" reference="imp"}) $$\label{cases}
    b_sh_x=
    \begin{cases}
      h_{sx}+vh_x & \text{if } sx > x\\
      h_{sx}+v^{-1}h_x & \text{if } sx < x.
    \end{cases}$$ Now suppose we have proved the existence for all elements lesser than $x$ in the Bruhat order and $x\neq e.$ Then we can find an $s\in S$ such that $sx<x$. By induction hypothesis and using equation ([\[cases\]](#cases){reference-type="ref" reference="cases"}) one has $$b_sb_{sx}=h_x+\sum_{y<x} p_{y}h_y,$$ for some $p_{y}\in \mathbb Z[v]$ (the $v^{-1}$ in equation ([\[cases\]](#cases){reference-type="ref" reference="cases"}) is the only problem). But if we define $$b_x=b_sb_{sx}-\sum_{y<x} p_{y}(0)b_y,$$ we still obtain a self-dual element (a $\mathbb Z$-linear combination of self-dual elements) and it clearly is of the prescribed form, so this proves the existence of $b_x.$
