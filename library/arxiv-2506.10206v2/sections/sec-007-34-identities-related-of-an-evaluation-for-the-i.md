---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-007-34-identities-related-of-an-evaluation-for-the-i
section_title: "Identities related of an evaluation for the inverse tangent integral"
section_number: 3.4
pages: 12-13
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.908
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
Setting $u= i\sqrt{3}$ it is possible to derive a relation between $\mathbb{Q}(\sqrt{13})$ and $\mathbb{Q}(\sqrt{3})$ that gives a fast series for $\rm{Cl}_2\big(\tfrac{\pi}3\big)$ that bypasses the summation of the multiple angle formula.

For the right-hand side, we obtain $$\label{equivalentTi}
 \Im \left(\operatorname{Li}_2\left(\frac{i}{\sqrt{3}}\right) 
 - \operatorname{Li}_2\left(\frac{-i}{\sqrt{3}}\right)\right)= \frac{5}{3} \, \Im\operatorname{Li}_2\left(\frac{1 + i\sqrt{3}}{2}\right) - \frac{\pi \ln(3)}{6},$$ noting that the left-hand side of [\[equivalentTi\]](#equivalentTi){reference-type="eqref" reference="equivalentTi"} may be expressed in an equivalent way with $\Im \text{Ti}_{2}\left( \frac{1}{\sqrt{3}} \right)$, and that the formula in [\[equivalentTi\]](#equivalentTi){reference-type="eqref" reference="equivalentTi"} may be proved in an equivalent way using Ramanujan's identity [@Ramanujan1915] such that $$\sum_{n=0}^{\infty} \frac{ \left( \frac{1}{2} \right)_{n} }{n!} \frac{ \cos^{2n+1} x 
 + \sin^{2n+1} x }{(2n+1)^2} = \text{Ti}_{2}(\tan x) + \frac{1}{2} \pi \ln(2 \cos x),$$ as noted in an equivalent way by Campbell [@Campbell2022]. From [\[equivalentTi\]](#equivalentTi){reference-type="eqref" reference="equivalentTi"} we obtain that $$\begin{aligned}
 \operatorname{Li}_2\left(-\frac{1}{12} \left(3 + i\sqrt{3}\right)\left(5 + \sqrt{13}\right)\right) - \operatorname{Li}_2\left(\frac{1}{12}\left(3 + 
 i\sqrt{3}\right)\left(5 + \sqrt{13}\right)\right) \\ 
 = \operatorname{Li}_2\left(-\frac{2i + \sqrt{3} + i\sqrt{13}}{-2i + \sqrt{3} + i\sqrt{13}}\right) - \operatorname{Li}_2\left(\frac{2i + \sqrt{3} + 
 i\sqrt{13}}{-2i + \sqrt{3} + i\sqrt{13}}\right). 
\end{aligned}$$ For the left-hand side, the two-term dilogarithm combination given by the $A$-expression in Theorem [\[maintheorem\]](#maintheorem){reference-type="ref" reference="maintheorem"} is used. Consequently, we obtain the equality of $$\begin{gathered}
 2\Im \, \operatorname{Li}_2\left(\frac{5 - \sqrt{13}}{\sqrt{12}} e^{\frac{\pi i}{6}}\right) - \Im\operatorname{Li}_2\left(\frac{1 + i\sqrt{3}}{2}\right) + \\ 
 \frac{\pi}{12} \ln\left(\frac{4}{3}\right) + \text{arccosh}\left(\frac{19}{6}\right) \operatorname{arctan}\left(\frac{\sqrt{13} - 2}{\sqrt{27}}\right) 
\end{gathered}$$ and $$\begin{gathered}
 \Im \text {Li}_2\left(\frac{ \sqrt{13}-5}{\sqrt{12}} e^{\frac{\pi i}{6}}\right) - 
 \Im \operatorname{Li}_2\left(\frac{5 - \sqrt{13}}{\sqrt{12}} e^{\frac{\pi i}{6}} 
 \right) + \frac{5}{6}\Im\operatorname{Li}_2\left(\frac{1 + i\sqrt{3}}{2}\right) \\ 
 + \, \frac{\pi}{6} \ln(2) - \frac{1}{2} \operatorname{arctan}\left(\sqrt{\frac{3}{13}}\right) \ln\left(\frac{1}{6}(19 + 5\sqrt{13})\right) 
 - \frac{\pi}{12} \ln(3), 
\end{gathered}$$ and, in turn, the above expression is equal to $$\frac{1}{6\sqrt{3}}\sum_{n=0}^{\infty} \left( \frac{-1}{324} \right)^{n} \left[ 
 \begin{matrix} \frac{1}{2}, \frac{1}{2}, 1 \vspace{1mm} \\ \frac{5}{6}, \frac{7}{6}, \frac{3}{2} \end{matrix} \right]_{n} =4 
 \sqrt{3} \int_{0}^{1} \frac{(3x^2 - 1)\ln(x)}{48 + x^2(1 - x^2)^2} \, dx.$$ We can then use the duplication formula for $\operatorname{Li}_{2}$, and this has the effect of a series acceleration, because, by taking the imaginary part of $e^{\frac{n\pi i}{3}}$ for positive integers $n$, every third term is ignored. This gives us that $$\begin{gathered}
 \pi \ln\left(\frac{4}{3}\right) + 3\ln\left(\frac{19 + 5\sqrt{13}}{6} \right)\left( \operatorname{arctan}\left(\frac{3\sqrt{3}}{16 + 
 5\sqrt{13}}\right)\right) + \\ 
 3\cdot\Im\left[\operatorname{Li}_2\left(\frac{1}{12}(5 - \sqrt{13})^2 e^{\frac{\pi i}{3}}\right)\right] - \rm{Cl}_2\big(\frac{\pi}3\big) = 
 \frac{2}{\sqrt{3}}\sum_{n=0}^{\infty} \left( \frac{-1}{324} \right)^{n} \left[ \begin{matrix} \frac{1}{2}, \frac{1}{2}, 1 \vspace{1mm} \\ 
 \frac{5}{6}, \frac{7}{6}, \frac{3}{2} \end{matrix} \right]_{n} 
\end{gathered}$$ and that $$\begin{aligned}
\Im\left[\operatorname{Li}_2\left(\frac{1}{12}(5 - \sqrt{13})^2 e^{\frac{\pi i}{3}}\right)\right] = 
 \sqrt{3}\sum_{n=1}^{\infty} \frac{(19 - 5 \sqrt{13})^{3n - 2} }{(-216)^n} \left( \frac{5 \sqrt{13} - 
 19}{(1 - 3n)^2} - \frac{6}{(2 - 3n)^2} \right)
\end{aligned}$$
