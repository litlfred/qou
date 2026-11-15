---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-023-62-the-reduced-jones-polynomials-of-knots
section_title: "The reduced Jones polynomials of knots"
section_number: 6.2
pages: 21-22
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.877
latex_coverage_ratio: 0.912
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:basis-pn- label="sec:basis-pn-"}

We prove the following result in Section [\[sec:proof-prop-refr22\]](#sec:proof-prop-refr22){reference-type="ref" reference="sec:proof-prop-refr22"}.

::: proposition
[]{#r22 label="r22"} For $m,n\ge 0$ we have $$\begin{gathered}
    \trq^{P''_m}(\sigma _n) = \delta _{m,n}.
  
\end{gathered}$$
:::

Using Proposition [\[r22\]](#r22){reference-type="ref" reference="r22"} we obtain the following.

::: theorem
[]{#r18 label="r18"} For a bottom knot $T\in \BT_1$ with closure $K=\cl(T)$, we have $$\label{e9}
    J_T = \sum_{n\ge 0}J_K(P''_n)\sigma _n.$$
:::

::: proof
*Proof.* We express $J_T$ as in Theorem [\[thm:23\]](#thm:23){reference-type="ref" reference="thm:23"}. Then, applying $\trq^{P''_m}$ to [\[eq:74\]](#eq:74){reference-type="eqref" reference="eq:74"}, we have by Proposition [\[r22\]](#r22){reference-type="ref" reference="r22"} $$\trq^{P''_m}(J_T)= \sum_{p\ge 0} a_p(T)\trq^{P''_m}(\sigma _p)
    =a_p(T).$$ Therefore, we have [\[e9\]](#e9){reference-type="eqref" reference="e9"}. ◻
:::

Theorems [\[thm:23\]](#thm:23){reference-type="ref" reference="thm:23"} and [\[r18\]](#r18){reference-type="ref" reference="r18"} implies that for a knot $K$, we have $J_K(P''_n)\in \Zqq$ for $n\ge 0$. We call $J_K(P''_n)$ the *$n$th reduced Jones polynomial* of $K$. It is clear that $J_K(P''_0)=1$. For $n=1$, we have $$J_K(P''_1) = (J_K(\V_1)-[2])/\{2\}\{3\}.$$ The quantity $-q^{-2}J_K(P''_1)$ is known as the *reduced Jones polynomial* of $K$, and appears in the original paper of Jones [@Jones2 Proposition 12.5]. Some examples of $J_K(P''_n)$ are given in Section [\[sec:surg-borr-rings\]](#sec:surg-borr-rings){reference-type="ref" reference="sec:surg-borr-rings"}.

It is clear that the universal invariant $J_T$ determines the colored Jones polynomials $J_K(\V_n)$, hence the reduced Jones polynomials $J_K(P''_n)$. Conversely, Theorem [\[r18\]](#r18){reference-type="ref" reference="r18"} implies that the universal invariant $J_T$ is determined by the $J_K(P''_n)$, hence by the $J_K(\V_n)$ as is presumably well known.

By [\[eq:100\]](#eq:100){reference-type="eqref" reference="eq:100"}, we have $$\label{e89}
  J_K(\V_n) =
  \sum_{i=0}^n\frac{\BB{n+1+i}{2i+1}}{\{1\}}J_K(P''_i),$$ where the sum may be replaced with $\sum_{i=0}^\infty$ since $\BB{n+1+i}{2i+1}=0$ for $i>n$. (Conversely, one can use [\[eq:97\]](#eq:97){reference-type="eqref" reference="eq:97"} to obtain a formula for the reduced Jones polynomials in terms of the colored Jones polynomials.) [\[e89\]](#e89){reference-type="eqref" reference="e89"} implies the following.

::: proposition
[]{#r36 label="r36"} If $K$ is a knot, then for each $n\ge 0$ the $n$th colored Jones polynomial $J_K(\V_n)$ is determined modulo $(\{2n+1\}_{2n})$ by $J_K(\V_0),J_K(\V_1),\ldots,J_K(\V_{n-1})$.
:::
