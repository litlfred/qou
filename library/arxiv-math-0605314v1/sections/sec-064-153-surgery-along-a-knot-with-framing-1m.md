---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-064-153-surgery-along-a-knot-with-framing-1m
section_title: "Surgery along a knot with framing $1/m$"
section_number: 15.3
pages: 59-59
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 1.0
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:surgery-along-knot label="sec:surgery-along-knot"}

Kirby and Melvin proved periodicity results for the WRT invariant of integral homology spheres obtained from $S^3$ by surgery along a knot with framings $1/m$ (Corollaries 8.15 and 8.26 of [@Kirby-Melvin]). We have the following generalization.

::: theorem
[]{#r9 label="r9"} Let $K$ be a knot in an integral homology sphere $M$. Let $M'=M_{K;1/m}$ be the result of surgery from $M$ along $K$ with framing $1/m$ with $m\in \modZ$. Then we have $$J_{M'}\equiv J_M \pmod{(q^{2m}-1)}.$$
:::

::: proof
*Proof.* One way to prove the assertion is first to prove $\tau _\zeta (M')=\tau _\zeta (M)$ for all $\zeta \in \calZ$ with $\ord(\zeta )|2m$ and then to use Section [\[sec:divis-ring-zqh\]](#sec:divis-ring-zqh){reference-type="ref" reference="sec:divis-ring-zqh"}. The former is a natural generalization of Kirby and Melvin's result, and is not difficult to prove. Here we give a direct proof.

We express $M$ as the result of surgery $S^3_{L}$ along an admissible framed link $L=L_1\cup \cdots\cup L_l$ in $S^3$, with framings $f_1,\ldots,f_l\in \{\pm 1\}$. We may assume that $K$ corresponds to a knot $K'\subset S^3\setminus L$ such that $K'\cup L$ is algebraically split. By puncturing $S^3$ at a point of $K'$, we obtain a bottom knot $T$ and a link $L$ in a cube, so that closing $T$ yields $K'\cup L$. We have $$\begin{split}
      J_{M'}-J_M
      &= J_{K\cup L^0}(\omega ^{-m},\omega ^{-f_1},\ldots,\omega ^{-f_l})
      -J_{K\cup L^0}(1,\omega ^{-f_1},\ldots,\omega ^{-f_l})\\
      &= J_{K\cup L^0}(\omega ^{-m}-1,\omega ^{-f_1},\ldots,\omega ^{-f_l})\\
      &= \trq^{\omega ^{-m}-1}(J_{T\cup L^0}(\omega ^{-f_1},\ldots,\omega ^{-f_l})),
    \end{split}$$ where $L^0$ is $L$ with $0$ framings. In view of the last subsection, we have $$J_{T\cup L^0}(\omega ^{-f_1},\ldots,\omega ^{-f_l})=\sum_{k\ge 0}a_k\sigma _k,$$ where $a_k\in \Zqh$ for $k\ge 0$. It suffices to prove that $\trq^{\omega ^{-m}-1}(\sigma _k)\in (q^{2n}-1)\Zqh$ for each $k\ge 0$. We have $$\trq^{\omega ^{-m}-1}(\sigma _k)=\langle \omega ^{-m}-1,S_k\rangle 
    =\langle \omega ^{-m}-1,\sum_{i=0}^{k}b_{k,i}\V_{2i}\rangle ,$$ where $b_{k,i}\in \Zqq$. We have $$\langle \omega ^{-m}-1,\V_{2i}\rangle =(q^{-i(i+1)m}-1)[2i+1]\in (q^{2m}-1)\Zqq.$$ Hence, the assertion follows. ◻
:::
