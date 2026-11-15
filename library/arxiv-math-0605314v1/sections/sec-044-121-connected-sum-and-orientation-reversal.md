---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-044-121-connected-sum-and-orientation-reversal
section_title: "Connected sum and orientation reversal"
section_number: 12.1
pages: 39-39
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.93
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:conn-sum-orient label="sec:conn-sum-orient"}

::: proposition
[]{#thm:43 label="thm:43"} (1) The invariant $J_M$ is multiplicative under connected sum, i.e., for any two integral homology spheres $M$ and $M'$ we have $J_{M\sharp M'}=J_M J_{M'}$, where $M\sharp M'$ denotes the connected sum of $M$ and $M'$. We also have $J_{S^3}=1$.

\(2\) If $-M$ denotes the mirror image of an integral homology sphere, then we have $J_{-M}=\overline{J_M}$. Here $\overline{J_M}\in \Zqh$ is the conjugate of $J_M$, i.e., the image of $J_M$ under the involutive ring automorphism $\Zqh\rightarrow \Zqh$, $f(q)\mapsto f(q^{-1})$.
:::

::: proof
*Proof.* The assertions follows from the corresponding, well-known properties of $\tau _\zeta (M)$ $$\begin{gathered}
    \tau _\zeta (M\sharp M')=\tau _\zeta (M)\tau _\zeta (M),\quad
    \tau _\zeta (S^3)=1,\quad
    \tau _\zeta (-M)=\tau _{\zeta ^{-1}}(M)
  
\end{gathered}$$ for any $\zeta \in \calZ$, and from Proposition [\[r85\]](#r85){reference-type="ref" reference="r85"}. (Alternatively, one can use the similar properties for the Ohtsuki series $\tau ^O(M)$ and the injectivity of $\iota _1\zzzcolon \Zqh\rightarrow \modZ [[q-1]]$. One can also prove the assertions directly using properties of the colored Jones polynomials.) ◻
:::
