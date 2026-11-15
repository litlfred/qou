---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-004-31-a-full-solution-to-a-problem-due-to-sun
section_title: "A full solution to a problem due to Sun"
section_number: 3.1
pages: 7-9
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 1.0
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
As it turns out, the $u = \frac{1}{\sqrt{3}}$ case Theorem [\[maintheorem\]](#maintheorem){reference-type="ref" reference="maintheorem"} can be used to formulate a full solution to a problem due to Sun [@Sun2021; @Sun2015] that was partially solved by Campbell [@Campbell2023], as later explained.

::: theorem
[]{#theoremSunCampbell label="theoremSunCampbell"} The closed-form evaluation $$8 \operatorname{Li}_2\left(2-\sqrt{3}\right)-\operatorname{Li}_2\left(4 \sqrt{3} - 7 \right) 
 = \frac{5 \pi ^2}{12}+\ln \left(2-\sqrt{3}\right) \ln \left(2+\sqrt{3}\right)$$ holds true.
:::

::: proof
*Proof.* For the $u = \frac{1}{\sqrt{3}}$ case Theorem [\[maintheorem\]](#maintheorem){reference-type="ref" reference="maintheorem"}, the left-hand side of [\[mainABCD\]](#mainABCD){reference-type="eqref" reference="mainABCD"} may be expressed in terms of $-2 \operatorname{Li}_2 \left( 7 - 4 \sqrt{3} \right) + 
 4 \operatorname{Li}_2 \left( \sqrt{3} - 2 \right)$ and a closed-form expression, and this follows from the known relation $$-2 \operatorname{Li}_2 \left( \frac{3 - \sqrt{3}}{6} \right) = 2 \operatorname{Li}_2 \left( \sqrt{3} - 2 \right) + 
 \ln^{2} \left( \frac{3 + \sqrt{3}}{6} \right).$$ The right-hand side of [\[mainABCD\]](#mainABCD){reference-type="eqref" reference="mainABCD"}, for the same input value $u = \frac{1}{\sqrt{3}}$ may be rewritten as $$K = \operatorname{Li}_2\left(-\sqrt{3}\right)-\frac{1}{2}
 \operatorname{Li}_2\left(-\frac{\sqrt{3}}{2}\right) + 
 \frac{\operatorname{Li}_2\left(\frac{\sqrt{3}}{2}\right)}{2}-\operatorname{Li}_2\left(\sqrt{3}\right).$$ Using the well known $4$- term functional equation $$\label{wellknown4term}
 \operatorname{Li}_2(z) - \operatorname{Li}_2(-z) + 
 \operatorname{Li}_2\left(\frac{1 - z}{1 + z}\right) - 
 \operatorname{Li}_2\left(\frac{-(1 - z)}{1 + z}\right) = \frac{\pi^2}{4} + \ln(z) \ln\left(\frac{1 + z}{1 - z}\right),$$ we obtain, by setting $z = \frac{\sqrt{3}}{2}$ and $z=\sqrt{3}$, that the right-hand side of [\[mainABCD\]](#mainABCD){reference-type="eqref" reference="mainABCD"} may be rewritten as $$\operatorname{Li}_2\left(7 - 4 \sqrt{3}\right) - \operatorname{Li}_2\left(4 \sqrt{3} - 7 \right) - 
 2 \, \operatorname{Li}_2\left(\sqrt{3} - 2\right) + 2 \, \operatorname{Li}_2\left(2 - \sqrt{3}\right).$$ Equating our equivalent expressions for the right-hand and left-hand sides of [\[mainABCD\]](#mainABCD){reference-type="eqref" reference="mainABCD"}, we obtain $$3 \, \operatorname{Li}_2\left(7 - 4 \sqrt{3}\right) - 
 \operatorname{Li}_2\left(4 \sqrt{3} - 7\right) - 
 6 \, \operatorname{Li}_2\left(\sqrt{3} - 2\right) + 2 \, \operatorname{Li}_2\left(2 - \sqrt{3}\right)$$ and $$3 \, \operatorname{Li}_2\left(7 - 4 \sqrt{3}\right) = 6 \, 
 \operatorname{Li}_2\left(2 - \sqrt{3}\right) + 6 \, \operatorname{Li}_2\left(\sqrt{3} - 2\right),$$ and this gives us an equivalent version of the desired result. ◻
:::

It was shown by Campbell [@Campbell2023] that the open problem due to Sun [@Sun2021; @Sun2015] given by proving the conjectured formula $$\label{Sunconjectureharmonic}
 \sum_{n=0}^{\infty} \frac{ \binom{2n}{n} }{ (2n+1) 8^{n} } \left( \sum_{0 \leq k < n} 
 \frac{(-1)^k}{2k+1} - \frac{(-1)^n}{2n+1} \right) = -\frac{\sqrt{2}}{16} \pi^2$$ is equivalent to the problem of proving the purported closed-form evaluation $$\label{discoveredwithAu}
 \operatorname{Li}_{2}\left( \frac{\sqrt{3} + 2}{4} \right) - 8 \operatorname{Li}_{2}(2 - \sqrt{3}) 
 = -\frac{\pi^2}{4} - 2 \ln^{2}(2) + \frac{5}{2} \ln^2(\sqrt{3} + 2) - 2 \ln(\sqrt{3} + 2) \ln 2$$ discovered experimentally using a Mathematica package given by Au, and referring to Campbell's work [@Campbell2023] for details. It can be shown that Theorem [\[theoremSunCampbell\]](#theoremSunCampbell){reference-type="ref" reference="theoremSunCampbell"} is equivalent to [\[discoveredwithAu\]](#discoveredwithAu){reference-type="eqref" reference="discoveredwithAu"}, thus providing a full proof of Sun's conjectured formula in [\[Sunconjectureharmonic\]](#Sunconjectureharmonic){reference-type="eqref" reference="Sunconjectureharmonic"}.
