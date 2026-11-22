---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-022-61-the-elements-p-n-and-p-n
section_title: "The elements $P_n$ and $P''_n$"
section_number: 6.1
pages: 21-21
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 1.0
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:elements-pn-pn label="sec:elements-pn-pn"}

For each $n\ge 0$ set $$\begin{gathered}
  P_n = \prod_{i=0}^{n-1}(\V_1 - v^{2i+1}-v^{-2i-1}) \in \modR _{\Zvv},\\
  P''_n = P_n/\BB{2n+1}{2n}\in \modR _{\modQ (v)}.
\end{gathered}$$

Since $P_n$ is a monic polynomial in $\V_1$ of degree $n$ for each $n\ge 0$, it follows that the $P_n$ form a basis of $\modR _{\Zvv}$. We have the following base change formulas.

::: lemma
[]{#r16 label="r16"} For $n\ge 0$, we have $$\begin{gathered}
    \label{eq:97}
    P_n=\sum_{i=0}^n(-1)^{n-i}\frac{[2i+2]}{[n+i+2]}
    \bb{2n+1}{n+1+i}\V_i,\\
    \label{eq:100}
    \V_n =\sum_{i=0}^n \bb{n+i+1}{2i+1} P_i.
  
\end{gathered}$$
:::

::: remark
[]{#r17 label="r17"} A formula essentially the same as [\[eq:100\]](#eq:100){reference-type="eqref" reference="eq:100"} formulated using the Kauffman bracket skein module of a solid torus has appeared in [@H:iias2000 Proposition 5.1.], [@Masbaum Equation 47]. (The former contained an incorrect sign.)
:::

::: proof
*Proof.* The proofs of [\[eq:97\]](#eq:97){reference-type="eqref" reference="eq:97"} and [\[eq:100\]](#eq:100){reference-type="eqref" reference="eq:100"} are by inductions on $n$ using $$\begin{gathered}
    P_n=P_{n-1}(\V_1-(v^{2n-1}+v^{-2n+1}))\quad (n\ge 1),\\
    \V_n=\V_1\V_{n-1}-\V_{n-2}\quad (n\ge 2),
  
\end{gathered}$$ respectively. For an alternative proof of [\[eq:100\]](#eq:100){reference-type="eqref" reference="eq:100"}, see Remark [\[thm:91\]](#thm:91){reference-type="ref" reference="thm:91"}. ◻
:::
