---
doc_id: arxiv-math-0605314v1
doc_title: "arXiv:math/0605314v1 [math.GT] 11 May 2006"
section_id: sec-035-1242-divisibility-results
section_title: "Divisibility results"
section_number: 12.4.2
pages: 44-45
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.889
doc_brief: "arXiv:math/0605314v1 [math.GT] 11 May 2006 — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring Z[q] such that the evaluation at"
---
[]{#sec:divisibility-results label="sec:divisibility-results"}

::: proposition
[]{#thm:44 label="thm:44"} For any integral homology sphere $M$, $J_M-1$ is divisible by $q^6-1$ in $\Zqh$.
:::

::: proof
*Proof.* In Lemma [\[r47\]](#r47){reference-type="ref" reference="r47"}, we showed that $J_M-1$ is divisible by $$\frac{(q^2-1)(q^3-1)}{q-1}
    =\Phi _1(q)\Phi _2(q)\Phi _3(q)
    =\frac{q^6-1}{\Phi _6(q)}.$$ Kirby, Melvin and Zhang [@Kirby-Melvin-Zhang] proved that $\tau _6(M)=1$ for any integral homology sphere $M$. Therefore, $J_M-1$ is divisible by $\Phi _6(q)$, hence the assertion. ◻
:::

Set $$\tJ_M = q^{-\lambda _1(M)}J_M\in \Zqh,$$ where $\lambda _1(M)=6\lambda (M)\in 6\modZ$ is the first coefficient of the Ohtsuki series $\tau ^O(M)\in \modZ [[q-1]]$. Clearly, $\iota _1(\tJ_M-1)\in (q-1)^2\modZ [[q-1]]$. By Proposition [\[thm:44\]](#thm:44){reference-type="ref" reference="thm:44"}, $\tJ_M-1$ is divisible by $q^6-1=(q-1)(q+1)(q^2+q+1)(q^2-q+1)$. Kirby and Melvin [@Kirby-Melvin] proved that $\tau _4(M)=\tau _{\sqrt{-1}}(M)=(-1)^{\chi (M)}\in \{\pm 1\}$, where $\chi (M)\in \modZ /2\modZ$ is the Rochlin invariant of $M$, which is the mod $2$ reduction of $\lambda (M)$. Therefore, we have $\mods _{\sqrt{-1}}(\tJ_M-1)=0$. Hence, $\tJ_M-1$ is divisible by $q^2+1$. These divisibility properties of $\tJ_M-1$ imply the following.

::: proposition
[]{#r10 label="r10"} For any integral homology sphere $M$, $\tJ_M-1$ is divisible by $$\Phi _1(q)^2\Phi _2(q)\Phi _3(q)\Phi _4(q)\Phi _6(q)
    =(q-1)(q^6-1)(q^2+1).$$
:::
