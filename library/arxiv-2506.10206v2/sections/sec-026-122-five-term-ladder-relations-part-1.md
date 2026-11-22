---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-026-122-five-term-ladder-relations-part-1
section_title: "Five-term ladder relations, part 1"
section_number: 12.2
pages: 34-35
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 0.957
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
[]{#section5term1 label="section5term1"} In this section we derive identities are are not as trivially verifiable as the above example. Some well-known dilogarithm bases include the basis such that $$u^6-3u^4-4u^3-3u^2+1=0$$ due to Lewin [@Lewin1991text], the basis such that $$u^6-u^5 - 
 u^3-u+1=0$$ due to Abouzahra and Lewin [@AbouzahraLewin1985]. These bases motivate the following dilogarithm identities. Since the sextic polynomial in Theorem [\[firstformatladder\]](#firstformatladder){reference-type="ref" reference="firstformatladder"} is symmetric, we obtain a reduction to a cubic polynomial identity with a fundamental discriminant of level $29$.

::: theorem
[]{#firstformatladder label="firstformatladder"} For the unique root $h$ in the interval $(0, 1)$ of $x^6-x^5-x^4-6 x^3-x^2-x+1 = 0$, the valid ladder relation $$\operatorname{Li}_{2}\left( h^{6} \right) + 3 \operatorname{Li}_{2}\left( h^{4} \right) 
 - 8 \operatorname{Li}_{2}\left( h^{3} \right) - 5 \operatorname{Li}_{2}\left( h^2 \right) 
 - 8 \operatorname{Li}_{2}(h) - 4 \ln^2(h) = - 5 \zeta(2)$$ holds.
:::

::: proof
*Proof.* From the the $A$- and $D$-expressions in Theorem [\[maintheorem\]](#maintheorem){reference-type="ref" reference="maintheorem"}, by applying the four-term relation in [\[wellknown4term\]](#wellknown4term){reference-type="eqref" reference="wellknown4term"} to the $K$-expression in Theorem [\[maintheorem\]](#maintheorem){reference-type="ref" reference="maintheorem"}, this gives us an evaluation for $$\begin{gathered}
 \text{ {\footnotesize $ \frac{1}{2} \operatorname{Li}_2\left(\left(\frac{u^2 + \sqrt{4 - 3 u^2} - 2}{u(u + 
 1)}\right)^2\right) - 4 \operatorname{Li}_2\left(\frac{u^2 + \sqrt{4 - 3 u^2} - 2}{u(u + 1)}\right) - 
 4 \operatorname{Li}_2\left(\frac{1 - u}{u + 1}\right) $} } \\ 
 \text{ { \footnotesize$ - \frac{1}{2} \operatorname{Li}_2\left(\left(\frac{u^2 + \sqrt{4 - 3 u^2} - 2}{(u - 1) u}\right)^2\right) + 
 4 \operatorname{Li}_2\left(\frac{u^2 + \sqrt{4 - 3 u^2} - 2}{(u - 1) u}\right) 
 + \frac{3}{2} \operatorname{Li}_2\left(\left(\frac{1 - u}{u + 1}\right)^2\right) 
 $}}. 
\end{gathered}$$ From this evaluation, by mimicking how the three-term $\operatorname{Li}_{2}$-relation in Section [\[subsection3ladder\]](#subsection3ladder){reference-type="ref" reference="subsection3ladder"} was used to construct a ladder, we set $$\frac{\left(u^2 + \sqrt{4 - 3u^2} - 2\right)^2}{u^2 (u + 1)^2} = \frac{u + 1}{1 - u} \ \ \ \text{and} \ \ \ 
 \frac{\left(u^2 + \sqrt{4 - 3u^2} - 2\right)^2}{(u - 1)^2 u^2} = \frac{(u + 1)^3}{(1 - u)^3},$$ yielding the same solutions. So, by setting $h = \sqrt{\frac{1 + u}{1 - u}}$, we obtain the root of $x^6 - x^5 - x^4 - 6 x^3 - x^2 - x + 1 =0$ specified. This gives us that $$\begin{gathered}
 \frac{5}{4} \ln(h^2)\ln(1 - h^2) + \frac{4}{2} \ln(h)\ln(1 - h) - \frac{3}{4} \ln(h^4)\ln(1 - h^4) + \frac{4}{2} \ln(h^3)\ln(1 - 
 h^3) - \\ 
 \frac{1}{4} \ln(h^6)\ln(1 - h^6) + \frac{5}{2} \operatorname{Li}_2(h^2) + 
 4 \operatorname{Li}_2(h) - \frac{3}{2} \operatorname{Li}_2(h^4) + 
 4 \operatorname{Li}_2(h^3) - \frac{1}{2} \operatorname{Li}_2(h^6) = \frac{5\pi^2}{12}, 
\end{gathered}$$ and, after much simplificatoin, this can be shown to be equivalent to the desired result. ◻
:::
