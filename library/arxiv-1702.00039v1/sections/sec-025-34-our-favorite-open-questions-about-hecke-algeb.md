---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-025-34-our-favorite-open-questions-about-hecke-algeb
section_title: "Our favorite open questions about Hecke algebras"
section_number: 3.4
pages: 19-20
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.928
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
It is one of the most important achievements in the theory of Soergel bimodules the proof [@EW] by B. Elias and G. Williamson of the conjecture (stated by Kazhdan and Lusztig) that Kazhdan-Lusztig polynomials have positive coefficients. We will come back to this beautiful and fundamental result in a subsequent paper of this saga. For the moment, this theorem gives rise to the following question.

::: ques
Give a combinatorial formula for the coefficients of Kazhdan-Lusztig polynomials, i.e. express the coefficients of $p_{x,y}$ as the cardinality of some combinatorially defined set (even for the symmetric group this would be extremely interesting).
:::

For the second question we have to introduce the *Braid group* $B_W$ of a Coxeter system $(W,S)$. It is the group $$\langle \sigma_s, s\in S\ \vert \ (\sigma_s\sigma_r)^{m_{sr}}=e\ \ \mathrm{if}\  s\neq r \in S \ \mathrm{and}\  m_{sr} \ \mathrm{is}\ \ \mathrm{finite} \rangle.$$ The fact that we impose $s\neq r$ is equivalent to not ask that $s^2=e$ for all $s\in S.$ Thus the braid group of $W$ is infinite unless $W$ is trivial.

::: ques
[]{#braid label="braid"} Is the following group morphism $$\begin{aligned}
B_W&\rightarrow \mathcal H(W)\\
\sigma_s&\mapsto h_s
\end{aligned}$$ an injection?
:::

There is a categorical version of this question due to Rouquier. He conjectures that "the braid group injects in the 2-braid group". We will explain this conjecture in detail in a subsequent paper. But we must say that Question [\[braid\]](#braid){reference-type="ref" reference="braid"} implies the conjecture of Rouquier.
