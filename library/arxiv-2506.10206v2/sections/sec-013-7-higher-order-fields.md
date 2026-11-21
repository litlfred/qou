---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-013-7-higher-order-fields
section_title: "Higher-order fields"
section_number: 7
pages: 21-21
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 1.0
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
The algebraic arguments of the dilogarithmic expressions involved in the preceding sections were rational or in quadratic or quartic algebraic number fields. This leads us to turn our attention toward higher-order algebraic number fields.

::: example
Setting $u = r + i\sqrt{1-r^{2}}$, this leads us to apply the circle property above and [\[previously7p5\]](#previously7p5){reference-type="eqref" reference="previously7p5"}. Accordingly, we have to solve $$\begin{aligned}
 \frac{1}{2} = \Re \left( \frac{1}{2} \left( -i \sqrt{1 - r^2} - 
 \sqrt{(r + i \sqrt{1 - r^2}) (-3 i \sqrt{1 - r^2} - 3r + 4)} - r + 2 \right) \right). 
\end{aligned}$$ The solution is given by $8 r^3 - 8 r^2 - 2 r + 3 =0$. We want the negative real root, $r=-0.57395...$, which satisfies the domain of the circle property. Hence, two of the three dilogarithms of Theorem [\[generalforCampbell\]](#generalforCampbell){reference-type="ref" reference="generalforCampbell"} have a closed form, thus yielding a single-term identity as desired. The resulting single-term identity can be expressed as the root of a solvable sextic. This have be shown to produce $$\begin{aligned}
 -\frac{3}{4} \arctan^{2} \left( \frac{\sqrt{1 - z^2}}{z} \right) + \arctan^{2} \left( \frac{\sqrt{1 - z^2}}{z + 1} \right) 
 - \frac{1}{4} \ln^2(2(z + 1))\\ 
 + \arctan^2 \left( \frac{1}{\sqrt{8z + 3}} \right) + \frac{\pi^2}{4} - \ln^2(1 - x) = 3\Re\operatorname{Li}_2(x), 
 \end{aligned}$$ where $x^6 - 2 x^5 + 13 x^4 - 24 x^3 + 19 x^2 - 7 x + 1=0$ for $x\approx 0.4495...-0.1211...i$ and $z=|r|$.
:::
