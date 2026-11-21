---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-009-4-elliptic-4f-3-series
section_title: "Elliptic ${}_{4}F_{3}$-series"
section_number: 4
pages: 13-15
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 1.0
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
In view of how we have applied ${}_{4}F_{3}$-functions of the form $${}_{4}F_{3}\!\!\left[ \begin{matrix} 
 1, 1, \frac{1}{2}, \frac{1}{2} \vspace{1mm}\\ 
 b_1, b_2, b_3 \end{matrix} \ \Bigg| \ z \right],$$ this leads us to consider similar applications of ${}_{4}F_{3}$-functions of the form $$\label{alternativehypergeometric}
 {}_{4}F_{3}\!\!\left[ \begin{matrix} 
 1, \frac{1}{2}, \frac{1}{2}, \frac{1}{2} \vspace{1mm}\\ 
 b_1, b_2, b_3 \end{matrix} \ \Bigg| \ z \right].$$ However, the partial fraction decomposition-based methods applied above are not applicable with the use of hypergeometric functions of the form indicated in [\[alternativehypergeometric\]](#alternativehypergeometric){reference-type="eqref" reference="alternativehypergeometric"}. Informally, this is because a required integral may be elliptic for almost all choices of $z$. Using [\[integrandforsum2\]](#integrandforsum2){reference-type="eqref" reference="integrandforsum2"}, together with $$\int_{0}^{1} \frac{\arcsin (g \, x(1 - x^2))}{{g x}} dx = \int_{0}^{1} \frac{(-1 + 3x^2)\ln(x)}{\sqrt{1 - g^2 x^2(1 - x^2)^2}} \, dx = 
 \frac{2}{3}\sum_{n=0}^{\infty} \left( \frac{4g^2 }{27} \right)^{n} \left[ \begin{matrix} \frac{1}{2}, \frac{1}{2}, \frac{1}{2} \vspace{1mm} \\ 
 \frac{5}{6}, \frac{7}{6}, \frac{3}{2} \end{matrix} \right]_{n},$$ we then make use of $$\arcsin\left(\frac{3\sqrt{3}}{2} x(1 - x^2)\right) = 3 \arcsin\left(\frac{\sqrt{3}}{2} x\right), \quad \text{for } \frac{1}{\sqrt{3}} .\geq x 
 \geq 0,$$ noting that each side of the above equality is equal to $$\pi - 3 \arcsin\left(\frac{\sqrt{3}}{2} x\right), \quad \text{for } 
 1 \geq x \geq \frac{1}{\sqrt{3}}$$ Setting $g = \sqrt{\frac{27}{4}}$ we obtain that $$\int_{0}^{\frac{1}{\sqrt{3}}} \frac{3 \arcsin\left(\frac{\sqrt{3}}{2}x\right)}{x} \, dx + \int_{\frac{1}{\sqrt{3}}}^{1} \frac{\pi - 3 \arcsin\left(\frac{\sqrt{3}}{2}x\right)}{x} \, dx =2\rm{Cl}_2\big(\frac{\pi}3\big),$$ where $$\label{previously5p5}
 \text{Cl}_2\big(\frac{\pi}3\big) = 
 \frac{ \sqrt{3}}{ 2} \, {}_{4}F_{3}\!\!\left[ \begin{matrix} 
 1, \frac{1}{2}, \frac{1}{2}, \frac{1}{2} \vspace{1mm}\\ 
 \frac{3}{2}, \frac{5}{6}, \frac{7}{6} \end{matrix} \ \Bigg| \ 1 \right].$$ It is also possible to find a quartic analogue using a similar factoring approach. Using [\[integrandforsum2\]](#integrandforsum2){reference-type="eqref" reference="integrandforsum2"}, we set $a = 3$, $b = 1$, $d = 0$, $c = 0$ and $y = x^2$. We thus have that $$\sum_{n = 0}^{\infty} \left( \frac{27g^2}{256} \right)^{n} 
 \left[ \begin{matrix} \frac{1}{3}, \frac{1}{2}, \frac{2}{3} 
 \vspace{1mm} \\ 
 \frac{3}{4}, \frac{5}{4}, \frac{3}{2} \end{matrix} \right]_{n} 
 = 2 \int_0^1 \frac{x \left( 4x^2 - 1 \right)}{\sqrt{1 - g^2 \left( 1 - x^2 \right)^3 x^2}} \, dx.$$ Setting $g=\sqrt{\frac{256}{27}}$, we find that $$f(x)= \frac{2x \left( 4x^2 - 1 \right)}{\sqrt{1 - \frac{256}{27} \left(1 - x^2\right)^3 x^2}}$$ assumes negative values for $\frac{1}{2} \geq x \geq 0$ and assumes positive values for $1 \geq x \geq 1/2$, so that $$\begin{aligned}
\begin{split}
 \int_0^1 
 \frac{\text{sgn}(4x^2 - 1) \, 
 2\sqrt{27} \, x}{\sqrt{16x^4 - 40x^2 + 27}} \, dx 
 & = \frac{3}{4} \sqrt{3} \left( 2 \ln(4 + 3\sqrt{2}) + \ln\left(\frac{7}{2} - 2\sqrt{3}\right) \right) \\ 
 & = {}_{4}F_{3}\!\!\left[ \begin{matrix} 
 1, \frac{1}{2}, \frac{2}{3}, \frac{1}{3} \vspace{1mm}\\ 
 \frac{3}{2}, \frac{5}{4}, \frac{3}{4} \end{matrix} \ \Bigg| \ 1 \right]. 
\end{split}\label{previously5p8}
\end{aligned}$$ Little seems to be known about mixed-base ${}_{4}F_{3}$-series of elliptic type, motivating our closed-form evaluation in both [\[previously5p5\]](#previously5p5){reference-type="eqref" reference="previously5p5"} and [\[previously5p8\]](#previously5p8){reference-type="eqref" reference="previously5p8"}. To the best of our knowledge, the ${}_{4}F_{3}(1)$-evaluations are original.
