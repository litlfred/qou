---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-038-103-some-remarks
section_title: "Some remarks"
section_number: 10.3
pages: 35-36
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.85
latex_coverage_ratio: 0.946
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:some-remarks label="sec:some-remarks"}

If $M$ and $L$ are as above, then we have the following formula for $J_M$: $$\label{e2}
  J_M
  = \sum_{k_1,\ldots,k_m=0}^\infty 
  \Bigl(\prod_{i=1}^m(-f_i)^{k_i}v^{\frac{-f_i}{2} k_i(k_i+3)}\Bigr)
  J_{L^0}(P'_{k_1},\ldots,P'_{k_m}).$$ In particular, if $L$ is a knot (i.e., $m=1$), then we have $$\label{eq:132}
    J_M
    = J_{L^0}(\omega ^{\mp1})
    = \sum_{k=0}^\infty (\mp1)^kv^{\mp\hf k(k+3)}
    \frac{\BB{2k+1}{k+1} }{\{1\}} J_{L^0}(P''_k).$$

In [\[e2\]](#e2){reference-type="eqref" reference="e2"}, the term for $k_1=\cdots=k_m=0$ is $$J_{L^0}(P'_0,\ldots,P'_0)=J_{L^0}(1,\ldots,1)=1.$$ It follows from Theorem [\[r29\]](#r29){reference-type="ref" reference="r29"} that the other terms are divisible by $(q^2-1)(q^3-1)/(q-1)$ in $\Zqq$. Hence, we have the following result, which we improve in Section [\[sec:divisibility-results\]](#sec:divisibility-results){reference-type="ref" reference="sec:divisibility-results"}.

::: lemma
[]{#r47 label="r47"} Let $M$ be an integral homology sphere. Then $J_M-1$ is divisible by $(q^2-1)(q^3-1)/(q-1)$ in $\Zqh$.
:::

::: remark
[]{#r24 label="r24"}It follows from Theorem [\[r29\]](#r29){reference-type="ref" reference="r29"} that $$J_M\mod I_k\in \Zqh/I_k\cong \modZ [q]/I_k,$$ where $I_k=\frac{\BBq{2k+1}{k+1}}{\{1\}_q}\Zqq$, is a finite linear combination of $J_{L^0}(P'_{k_1},\ldots,P'_{k_m})$ for $k_1,\ldots,k_m\in \{0,1,\ldots,k-1\}$, hence is a finite linear combination of the colored Jones polynomial $J_{L^0}(\V_{k_1},\ldots,\V_{k_m})$ for $k_1,\ldots,k_m\in \{0,1,\ldots,k-1\}$. In particular, for $k=2$, $J_M\mod
  I_2$ is a linear combination of the Jones polynomials (with colors $\V_1$) of all the sublinks of $L^0$.
:::
