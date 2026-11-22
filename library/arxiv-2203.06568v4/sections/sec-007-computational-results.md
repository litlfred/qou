---
doc_id: arxiv-2203.06568v4
doc_title: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra"
section_id: sec-007-computational-results
section_title: "computational results"
section_number: null
pages: 11-11
source_pdf: 2203.06568v4.pdf
source_sha256: 256fcfb588dac554
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Semideﬁnite programming bounds for binary codes from a split Terwilliger algebra — We study the upper bounds for A(n, d), the maximum size of codewords with length n and Hamming distance at least d."
---
We use the CVX toolbox [@GB14], [@GB08] in MATLAB with the MOSEK solver to run our SDP. Our main results are as follows. In our SDP, we have tested all possible values of splits $n_{1}$ and $n_{2}$. The computational results give us two improvements $A(18,4) \leq 6551$ and $A(19,4) \leq 13087$. However, using Gijswijt's method in the previous subsection, we are only able to ensure one of them is improved.

::: theorem
$A(18,4) \leq 6551$.
:::

::: proof
*Proof.* Using $n_{1} = 2$, we obtain $A(18,4)\leq 6551.93$ with an error term less than $10^{-16}$. Thus $A(18,4)\leq 6551$. ◻
:::

::: remark
$A(18,4) \leq 6551$ can be obtained by the split SDP with $n_{1} = 2$ and only the constraints ([\[sem1\]](#sem1){reference-type="ref" reference="sem1"}), ([\[sem2\]](#sem2){reference-type="ref" reference="sem2"}), ([\[le3\]](#le3){reference-type="ref" reference="le3"}) and ([\[le5\]](#le5){reference-type="ref" reference="le5"}). Then, we have $A(18,4) \leq 6551.98$ with an error term less than $10^{-16}$. All the above mentioned constraints are necessary in this case.
:::
