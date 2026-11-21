---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-027-123-a-six-term-ladder-relation
section_title: "A six-term ladder relation"
section_number: 12.3
pages: 35-37
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 1.0
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
An analogue of our approach from Section [\[section5term1\]](#section5term1){reference-type="ref" reference="section5term1"} leads us to construct and prove a new six-term ladder relation, as below.

::: theorem
[]{#theoremnew6term label="theoremnew6term"} Let $h$ denote the unique root in the interval $(0, 1)$ of $x^6-3 x^5+5 x^4-8 x^3+5 x^2-3 x+1 = 0$. Then the ladder relation $$\begin{gathered}
 \operatorname{Li}_2\left(h^8\right) + 3 \operatorname{Li}_2\left(h^6\right) - 
 8 \operatorname{Li}_2\left(h^4\right) - 8 \operatorname{Li}_2\left(h^3\right) + 
 3 \operatorname{Li}_2\left(h^2\right) - 8 \operatorname{Li}_2(h)-6 \ln ^2(h) = \\ 
 -5 \zeta(2) 
\end{gathered}$$ holds.
:::

::: proof
*Proof.* We exploit the property whereby the following equalities $$\label{commonsolutionfor6}
 \frac{u^2 - \sqrt{4 - 3u^2} - 2}{u(u - 1)} = \left( \frac{u + 1}{1 - u} \right)^4 
 \ \ \ \text{and} \ \ \ 
 \frac{u^2 + \sqrt{4 - 3u^2} - 2}{u(u + 1)} = \left( \frac{1 - u}{1 + u} \right)^4$$ have a common solution. In this direction, the six-term dilogarithm equation involved in our proof of Theorem [\[firstformatladder\]](#firstformatladder){reference-type="ref" reference="firstformatladder"} gives us a corresponding evaluation for $$\begin{gathered}
 \operatorname{Li}_2\left( \frac{u^2 + \sqrt{4 - 3u^2} - 2}{-u(u + 1)} \right) 
 - 3 \operatorname{Li}_2\left( \frac{u^2 + \sqrt{4 - 3u^2} - 2}{u(u + 1)} \right) 
 - 4 \operatorname{Li}_2\left( \frac{1 - u}{u + 1} \right) \\ 
 + \operatorname{Li}_2\left( \frac{u^2 - \sqrt{4 - 3u^2} - 2}{-u(u + 1)} \right) 
 - 3 \operatorname{Li}_2\left( \frac{u^2 - \sqrt{4 - 3u^2} - 2}{u(u + 1)} \right) 
 + \frac{3}{2} \operatorname{Li}_2\left( \left( \frac{1 - u}{u + 1} \right)^2 \right), 
\end{gathered}$$ yielding, from the common solutions for [\[commonsolutionfor6\]](#commonsolutionfor6){reference-type="eqref" reference="commonsolutionfor6"}, the equality of $$- \frac{1}{2} \operatorname{Li}_2(h^8) 
 - \frac{3}{2} \operatorname{Li}_2(h^6) 
 + 4 \operatorname{Li}_2(h^4) 
 + 4 \operatorname{Li}_2(h^3) 
 -\frac{3}{2} \operatorname{Li}_2(h^2) 
 + 4 \operatorname{Li}_2(h)$$ and $$\begin{gathered}
 \text{ { \footnotesize $ \frac{3}{4} \ln(h^2) \ln(1 - h^2)
 - 2 \ln(h) \ln(1 - h)
 - 2 \ln(h^4) \ln(1 - h^4) 
 - 2 \ln(h^3) \ln(1 - h^3) + $ } } \\ 
 \text{{ \footnotesize $ \frac{3}{4} \ln(h^6) \ln(1 - h^6) + \frac{1}{4} \ln(h^8) \ln(1 - h^8) + \frac{5\pi^2}{12} $ }}
\end{gathered}$$ for $h$ as specified, and this can be shown to provide an equivalent version of the desired result. ◻
:::

::: remark
Since the sexic polynomial in Theorem [\[theoremnew6term\]](#theoremnew6term){reference-type="ref" reference="theoremnew6term"} is symmetric, it can be reduced to a cubic case that has a fundamental discriminant of 13. This is the only cubic ladder with arguments in $\mathbb{Q}(\sqrt{13})$, to the best of our knowledge.
:::

By analogy with the ladder constructions due to Lewin and Campbell, is is possible to generate ladders for arbitrary powers with the base equation $$(h - 1) h^{2 m-1} = (h (h + 6) + 1) h^{m-1} +h - 1$$ The $m=4$ case recovers Theorem [\[theoremnew6term\]](#theoremnew6term){reference-type="ref" reference="theoremnew6term"} and the $m=3$ case recovers Theorem [\[firstformatladder\]](#firstformatladder){reference-type="ref" reference="firstformatladder"}. This base equation appears new and not seen the literature consulted and does not readily follow from the Lewin identities or others.
