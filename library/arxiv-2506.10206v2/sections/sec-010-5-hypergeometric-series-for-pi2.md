---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-010-5-hypergeometric-series-for-pi2
section_title: "Hypergeometric series for $\pi^2$"
section_number: 5
pages: 15-16
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 1.0
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
In this section, a sextic analogue of our previous hypergeometric series is used to derive a new series $\pi^{2}$ . We begin with the relation $$\begin{gathered}
 \int_{0}^{1} \int_{0}^{g} \frac{\arctan\left(g \sqrt{y} (1-y)\right)}{y} \, dg \, dy = \\
 \int_{0}^{1} \left( \frac{\ln\left(g^2 y (1 - y)^2 + 1\right)}{2 (y - 1) y^{3/2}} + 
 \frac{g \operatorname{arctan}\left(g (1 - y) \sqrt{y}\right)}{y} \right) \, dy, 
\end{gathered}$$ and we find that the right-hand side may be written as $$\frac{2g^2}{3} \sum_{n=0}^{\infty} \left( \frac{-4g^2}{27} \right)^{n} 
 \frac{1}{n+1} 
 \left[ \begin{matrix} 1, \frac{1}{2}, \frac{1}{2} 
 \vspace{1mm} \\ 
 \frac{5}{6}, \frac{7}{6}, \frac{3}{2} \end{matrix} \right]_{n},$$ noting that $$\int_{0}^{1}\frac{g \, \operatorname{arctan}\left(g (1 - y) \sqrt{y}\right)}{y} \, dy=\frac{4s_1g^2}{3}.$$ Applying the substitution $y=x^2$, we find that $$\label{originally6p3}
 \int_{0}^{1} \ln\left(g^2x^2 (x^2-1)^2 +1 \right) \left(\frac{1}{x^2 - 1} - \frac{1}{x^2}\right) \, dx= 
 \frac{-2g^2}{3} \sum_{n=0}^{\infty} \left( \frac{-4g^2}{27} \right)^{n} 
 \left[ \begin{matrix} \frac{1}{2}, 1, 1 
 \vspace{1mm} \\ 
 \frac{5}{6}, \frac{7}{6}, 2 \end{matrix} \right]_{n}.$$ Using integration by parts, we rewrite the integral in [\[originally6p3\]](#originally6p3){reference-type="eqref" reference="originally6p3"} to obtain $$\int_{0}^{1} \frac{2g^2 \left(3x^5 - 4x^3 + x\right)}{1 + g^2x^2(x^2-1)^2} \left(\frac{-1}{x} + 
 \operatorname{arctanh}(x)\right)\, dx,$$ and we proceed to use the relation such that $$2g^2\ \int_{0}^{1} \frac{(x^2 - 1)(3x^2 - 1)}{1 + g^2x^2(1 - x^2)^2} \, dx = 
 \frac{8g^2}{15} \sum_{n=0}^{\infty} \left( \frac{-4g^2}{27} \right)^{n} 
 \left[ \begin{matrix} \frac{1}{2}, 1 
 \vspace{1mm} \\ 
 \frac{7}{6}, \frac{11}{6} \end{matrix} \right]_{n}.$$ This may be derived by using a variant involving $\operatorname{arctan}$ of the trigonometric integral used to express $s_{2}$. More specifically, our derivation is given by integrating about $g$ twice and by applying integration by parts twice, once for each iteration, and then subtracting [\[displayw2\]](#displayw2){reference-type="eqref" reference="displayw2"} so as to isolate the ${}_{3}F_{2}$ that is not reducible to a polylogarithm. This approach yields $$\begin{gathered}
 \frac{-2g^2}{3} \sum_{n=0}^{\infty} \left( \frac{-4g^2}{27} \right)^{n} \left[ \begin{matrix} \frac{1}{2}, 1, 1 
 \vspace{1mm} \\ 
 \frac{5}{6}, \frac{7}{6}, 2 \end{matrix} \right]_{n} = \\ 
 \int_{0}^{1} \frac{2g^2 \left(3x^5 - 4x^3 + 
 x\right)}{1 + g^2x^2(x^2-1)^2} \, \text{arctanh}(x)\, dx - 
 \frac{8g^2}{15} \sum_{n = 
 0}^{\infty} \left( \frac{-4g^2}{27} \right)^{n} 
 \left[ \begin{matrix} \frac{1}{2}, 1 
 \vspace{1mm} \\ 
 \frac{7}{6}, \frac{11}{6} \end{matrix} \right]_{n}. 
\end{gathered}$$ Combining the above two summations and reversing the application of integration by parts, this yields $$s_4=\frac{2g^2}{15} 
 {}_{4}F_{3}\!\!\left[ \begin{matrix} 
 1, 1, 1, \frac{3}{2} \vspace{1mm}\\ 
 \frac{7}{6}, \frac{11}{6}, 2 \end{matrix} \ \Bigg| \ -\frac{4g^2}{27} \right] 
 = \int_{0}^{1} \frac{\ln\left(g^2 x^2 (x^2 - 1)^2 + 1\right)}{1 - x^2} \, dx.$$ By writing $x^2 (x^2 - 1)^2 + 1/g^2=0$ as $(x^2+r_0)(x^2+r_1)(x^2+r_2)$, where $r_1=a_1+ia_2$ and $r_2=a_1-ia_2$, we obtain that $$s_4 = -u_1-u_2 + \frac{3\pi^{2}}{4}.$$ for $$\text{ { \footnotesize $ u_1=\frac{1}{4} \left( - \ln^2\left(\frac{2}{-1 + \sqrt{-r_0}}\right) 
 - \ln^2\left(\frac{-2}{1 + \sqrt{-r_0}}\right) + 2 \ln\left(\frac{1 - \sqrt{-r_0}}{2} \right) 
 \ln\left(\frac{1 + \sqrt{-r_0}}{2}\right) \right) $ } }$$ and $$\text{ { \footnotesize $ u_2=\frac{1}{2} \left( - \ln^2\left(\frac{2}{-1 + \sqrt{-r_1}}\right) 
 - \ln^2\left(\frac{-2}{1 + \sqrt{-r_1}}\right) + 2 \ln\left(\frac{1 - \sqrt{-r_1}}{2} \right) 
 \ln\left(\frac{1 + \sqrt{-r_1}}{2}\right) \right). $ } }$$ Now, setting $g := \frac{i}{u(1-u^2)}$, we obtain that $\sqrt{-r_0} = u$ and that $\sqrt{-r_1}=(-u+\sqrt{4-3u^2})/2$. After simplification, setting $u=ih$, we have (for $h \geq \alpha >0$ where $\frac{4}{27} \cdot \frac{1}{\alpha^2 (1 + \alpha^2)} = 1$): $$\begin{gathered}
 \frac{4}{15h^2(1+h^2)^2} 
 {}_{4}F_{3}\!\!\left[ \begin{matrix} 
 1, 1, 1, \frac{3}{2} \vspace{1mm}\\ 
 \frac{7}{6}, \frac{11}{6}, 2 \end{matrix} \ \Bigg| \ -\frac{4}{27h^2(1+h^2)^2} \right] = \\ 
 \frac{-3}{4} \left(\pi - 2\arctan(h)\right)^2 
 + \ln^2\left(\frac{h^2 + 2 + \sqrt{3h^2 + 4}}{h\sqrt{1 + h^2}}\right). 
\end{gathered}$$ Informally, the connection between $\sqrt{3}$ and $\sqrt{13}$ suggested above gives us that $$\label{previously6p12}
 \ln^2\left(\frac{5 + \sqrt{13}}{2\sqrt{3}}\right) - \frac{\pi^2}{12} = 
 \frac{1}{180} {}_{4}F_{3}\!\!\left[ \begin{matrix} 
 1, 1, 1, \frac{3}{2} \vspace{1mm}\\ 
 \frac{7}{6}, \frac{11}{6}, 2 \end{matrix} \ \Bigg| \ -\frac{1}{324} \right].$$ A hypergeometric identity related to the second-to-last displayed equality given by was found by Sun and Zhou in 2024 [@SunZhoupreprint], The closed-form evaluation in [\[previously6p12\]](#previously6p12){reference-type="eqref" reference="previously6p12"} appears to be new.
