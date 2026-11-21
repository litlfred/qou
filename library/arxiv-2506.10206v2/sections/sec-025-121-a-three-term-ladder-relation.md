---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-025-121-a-three-term-ladder-relation
section_title: "A three-term ladder relation"
section_number: 12.1
pages: 34-34
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.971
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
[]{#subsection3ladder label="subsection3ladder"} We can rewrite Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"} so that the three-term dilogarithm combination $$\begin{gathered}
 \operatorname{Li}_2\left(\frac{2u^2 - 3u - \sqrt{u(4-3u)}}{2(u - 1)u}\right) - \\ 
 \operatorname{Li}_2\left(\frac{2u^2 - 3u - \sqrt{u(4 - 3u)}}{2(u - 1)^2}\right) 
 + \operatorname{Li}_2\left(\frac{u}{u - 1}\right) 
\end{gathered}$$ admits the closed form $$- \frac{1}{2} \ln^2\left(\frac{2u^2 - 3u + \sqrt{u(4 - 3u)}}{-2(u - 1)^2}\right) - \frac{\pi^2}{6}
 + \frac{3}{2} \ln^2\left(1 - \frac{u - \sqrt{u(4 - 3u)}}{2(u - 1)}\right).$$ We proceed to apply the substitutions $$\begin{aligned}
\frac{2u^2 - 3u - \sqrt{-u(3u - 4)}}{2(u - 1)u} & = \left(\frac{u}{u - 1}\right)^m,\\
\frac{2u^2 - 3u + \sqrt{-u(3u - 4)}}{2(u - 1)^2} & = \left(\frac{u}{u - 1}\right)^{-m}, \ \text{and} \\
\frac{2u^2 - 3u - \sqrt{-u(3u - 4)}}{2(u - 1)^2} & = \left(\frac{u}{u - 1}\right)^{m + 1}. 
\end{aligned}$$ Substituting $u = \frac{h}{h-1}$, we have the ladder identity $$\begin{aligned}
- \mathrm{Li}_2(h^{-m}) - \mathrm{Li}_2(h^{m+1}) + \mathrm{Li}_2(h) = \frac{3}{2} \ln^2\left( \frac{1 - h^{-m}}{1 - h} \right)
\end{aligned}$$ for arbitrary powers, where $(h^m + h - 3) h^{m + 1} + 1 = 0$.

::: example
For $m=-4$ we have that $h^5 + 2 h^4 + 4 h^3 + 3 h^2 + 2 h + 1=0$. This can be proved by applying Roger's identity and then Landen's identity. A similar approach can be applied to many of Lewin's ladder identities.
:::
