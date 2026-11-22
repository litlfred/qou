---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-030-82-integrality-for-algebraically-split-0-framed
section_title: "Integrality for algebraically-split, $0$-framed links"
section_number: 8.2
pages: 29-29
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.895
latex_coverage_ratio: 1.0
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:maps-jlhphphaq label="sec:maps-jlhphphaq"} The following theorem is proved in Section [\[sec:proof-theorem-refr29\]](#sec:proof-theorem-refr29){reference-type="ref" reference="sec:proof-theorem-refr29"}.

::: theorem
[]{#r29 label="r29"} Let $L$ be an $m$-component, algebraically-split, $0$-framed link. For $i=1,\ldots,m$, let $x_i\in \modP _{k_i}$, $k_i\ge 0$. Then we have $$J_L(x_1,\ldots,x_m) \in \frac{\BBq{2k+1}{k+1}}{\{1\}_q}\Zqq,$$ where $k=\max(k_1,\ldots,k_m)$.
:::

Theorem [\[r29\]](#r29){reference-type="ref" reference="r29"} immediately implies the following.

::: corollary
[]{#r87 label="r87"} Let $L$ be an $m$-component, algebraically-split, $0$-framed link. Then the $\modQ (v)$-multilinear map $J_L\zzzcolon \modR _{\modQ (v)}\times \cdots\times \modR _{\modQ (v)}\rightarrow \modQ (v)$ restricts to a $\Zqq$-multilinear map $$J_L\zzzcolon \modP \times \cdots\times \modP \rightarrow \Zqq,$$ which induces a $\Zqq$-multilinear map $$J_L\zzzcolon \hP\times \cdots\times \hP\rightarrow \Zqh.$$
:::

::: remark
[]{#r30 label="r30"} It follows from [\[eq:100\]](#eq:100){reference-type="eqref" reference="eq:100"} that for an $m$-component, algebraically-split, $0$-framed link $L$, the colored Jones polynomial $J_L(\V_{n_1},\ldots,\V_{n_m})$, $n_1,\ldots,n_m\ge 0$, can be expressed as a linear combination of the $J_L(P'_{k_1},\ldots,P'_{k_m})$, $k_1,\ldots,k_m\ge 0$ as follows: $$\label{e37}
    \begin{split}
      &J_L(\V_{n_1},\ldots,\V_{n_m})
      =\sum_{k_1=0}^{n_1}\cdots\sum_{k_m=0}^{n_m}
      \prod_{i=1}^m\Bigl(\bb{n_i+k_i+1}{2k_i+1}\{k_i\}!\Bigr)
      J_L(P'_{k_1},\ldots,P'_{k_m}).
    \end{split}$$ Here the sums may be replaced with infinite sums $\sum_{k_i=0}^\infty$.
:::
