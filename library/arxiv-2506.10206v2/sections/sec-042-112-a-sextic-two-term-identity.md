---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic dilogarithm identities"
section_id: sec-042-112-a-sextic-two-term-identity
section_title: "A sextic two-term identity"
section_number: 11.2
pages: 31-32
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
doc_brief: "Analytic dilogarithm identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 1.0
---
Using Lemma [\[previously10p4\]](#previously10p4){reference-type="ref" reference="previously10p4"}, we set $k=\frac{1}{2}\sec \frac{2\pi}{7}$, and this allows the application of Watson's formula for $\operatorname{Li}_2(k) - \operatorname{Li}_2(k^2)$, so that $$\frac{-2k^2 + k - \sqrt{-3k^2 + 2k + 1} + 1}{2 - 2k^2}=r_2, \frac{-2k^2 + k + \sqrt{-3k^2 + 2k + 1} + 1}{2 - 2k^2}=r_1,$$ where $r_2 = -0.42812..., r_1=1.87316...$ Or exactly, $x^6 - 4 x^5 + 5 x^4 - 2 x^3 + x^2 - x - 1 =0$. Using Roger's L-function, we have that $$\frac{\pi^2}{7} = 
 \operatorname{Li}_2\left(\frac{1}{r_1}\right) + \operatorname{Li}_2\left(\frac{r_2}{r_2 - 1}\right) + 
 \frac{1}{2} \ln\left(\frac{1}{r_1}\right) \ln\left(1 - \frac{1}{r_1}\right) + \frac{1}{2} \ln\left(\frac{r_2}{r_2 - 
 1}\right) \ln\left(\frac{1}{1 - r_2}\right).$$ Now, if we were to set $x = \frac{1}{1-y}$, then we would yield Bytsko's two-term sextic dilogarithm identity [@Bytsko1999], which is composed of the two real roots of $y^6 - 7 y^5 + 19 y^4 - 28 y^3 + 20 y^2 - 7 y + 1=0$. He asks if it is related to the Watson identities, as his result was experimentally derived. We can now answer in the affirmative.
