---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-061-143-surgeries-along-the-borromean-rings
section_title: "Surgeries along the Borromean rings"
section_number: 14.3
pages: 56-57
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.909
latex_coverage_ratio: 0.886
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:surg-borr-rings label="sec:surg-borr-rings"}

For $i,j,k\in \modZ$, we define $L_i$, $K_{i,j}$ and $M_{i,j,k}$ as follows. Let $A_1,A_2,A_3$ denote the components of the Borromean rings $A$.

-   $L_i=(A_1\cup A_2)_{A_3;-1/i}\subset S^3$, the two component link obtained from $A_1\cup A_2$ by surgery along $A_3$ with framing $-1/i$.

-   $K_{i,j}=(A_1)_{A_2\cup A_3;-1/i,-1/j}\subset S^3$, the knot obtained from $A_1$ by surgery along $A_2$ and $A_3$ with framings $-1/i$ and $-1/j$, respectively.

-   $M_{i,j,k}=(S^3)_{A_1\cup A_2\cup A_3;-1/i,-1/j,-1/k}$, the integral homology sphere obtained from $S^3$ by surgery along $A_1$, $A_2$, $A_3$ with framings $-1/i$, $-1/j$, $-1/k$, respectively.

::: proposition
[]{#r3 label="r3"} For $i,j,k\in \modZ$ and $l,m\ge 0$, we have $$\begin{gathered}
    \label{e5}
    J_{L_i}(P'_l,P'_m)
    =\delta _{l,m}\omega _{i,l}(-1)^l{\BB{2l+1}{l+1}}/{\{1\}},\\
    \label{e15}
    J_{K_{i,j}}(P'_l)
    =\omega _{i,l}\omega _{j,l}(-1)^l{\BB{2l+1}{l+1}}/{\{1\}},\\
    \label{e20}
    J_{M_{i,j,k}}=
    \sum_{l\ge 0}\omega _{i,l}\omega _{j,l}\omega _{k,l}(-1)^l{\BB{2l+1}{l+1}}/{\{1\}},\\
    \label{e18}
    J_{L_i}(\V_l,\V_m)
    =\sum_{s=0}^{\min(l,m)} \bb{l+s+1}{2s+1}\bb{m+s+1}{2s+1}\omega _{i,s}
    (-1)^s\{s\}!\{2s+1\}!/{\{1\}},
    \\
    \label{e19}
    \begin{split}
      J_{K_{i,j}}(\V_l)
      &=\sum_{s=0}^{l} \bb{l+s+1}{2s+1}\omega _{i,s}\omega _{j,s}
      (-1)^s\{2s+1\}!/{\{1\}}\\
      &=\sum_{s=0}^{l} (-1)^s\omega _{i,s}\omega _{j,s}
      \frac{\{l+s+1\}\{l+s\}\cdots\{l-s+1\}}{\{1\}}.
    \end{split}
  
\end{gathered}$$
:::

::: proof
*Proof.* The first three identities follows from $J_{L_i}(P'_l,P'_m)=J_A(P'_l,P'_m,\omega ^i)$, $J_{K_{i,j}}(P'_l)=J_A(P'_l,\omega ^i,\omega ^j)$, and $J_{M_{i,j,k}}=J_A(\omega ^i,\omega ^j,\omega ^k)$. Use [\[eq:100\]](#eq:100){reference-type="eqref" reference="eq:100"} for the others. ◻
:::

By [\[e15\]](#e15){reference-type="eqref" reference="e15"}, we have $$J_{K_{i,j}}(P''_l) =(-1)^l\omega _{i,l}\omega _{j,l}.$$

The special case of Proposition [\[r3\]](#r3){reference-type="ref" reference="r3"} for $K_{i,j}$, $M_{i,j,k}$ with $i,j,k\in \{\pm 1\}$ appeared in [@H:iias2000; @H:rims2001; @Le2] (without proofs). The case for $K_{i,\pm 1}$, $i\in \modZ$, (and essentially $L_{\pm 1}$) has been proved by Masbaum [@Masbaum] using skein theory.
