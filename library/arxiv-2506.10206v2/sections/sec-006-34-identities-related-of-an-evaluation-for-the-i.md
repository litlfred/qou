---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-006-34-identities-related-of-an-evaluation-for-the-i
section_title: "Identities related of an evaluation for the inverse tangent integral"
section_number: 3.4
pages: 12-18
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 1.0
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

## A series of convergence rate $\frac{1}{243}$

The $u = 
 2$ case of Theorem [\[maintheorem\]](#maintheorem){reference-type="ref" reference="maintheorem"} yields the ${}_{4}F_{3}$-evaluation such that $$\begin{gathered}
 \sum_{n=0}^{\infty} \left( \frac{1}{243} \right)^{n} 
 \left[ \begin{matrix} \frac{1}{2}, \frac{1}{2}, 1 
 \vspace{1mm} \\ 
 \frac{5}{6}, \frac{7}{6}, \frac{3}{2} \end{matrix} \right]_{n} 
 = \frac{9 \operatorname{Li}_2\left(\frac{1}{4}\right)}{4}-\frac{3 \pi ^2}{4}+\frac{9 \ln^2(2)}{2}-\frac{9 \ln ^2(3)}{8} + \\ 
 \frac{9}{2} \operatorname{arctan}^{2}\left(\frac{1}{\sqrt{2}}\right) + 
 9 \operatorname{arctan}\left(\frac{1}{\sqrt{2}}\right) \operatorname{arctan}\left(\sqrt{2}\right). 
\end{gathered}$$ This can be shown to follow from [\[MequalsAB\]](#MequalsAB){reference-type="eqref" reference="MequalsAB"}, as the right-hand side of the required dilogarithm identity may be verified using Roger's five-term identity.

# Elliptic ${}_{4}F_{3}$-series

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

# Hypergeometric series for $\pi^2$

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

# A proof of Campbell's conjecture

To solve an open problem recently given by Campbell [@Campbell2025], we begin with the following dilogarithm identity that we have obtained through our beta integral-based method.

::: theorem
[]{#generalforCampbell label="generalforCampbell"} For complex $u$, let $\mathcal{L}(u)$ denote the three-term dilogarithm combination $$\operatorname{Li}_{2}\left( \frac{ 2-\sqrt{4 - 
 3 u} \sqrt{u}-u }{2} \right) + \operatorname{Li}_{2}\left( \frac{2+\sqrt{4-3 u} \sqrt{u}-u}{2} \right) + 
 \operatorname{Li}_{2}(u)$$ and let $\mathcal{E}(u)$ denote the elementary expression $$\begin{gathered}
 \frac{1}{3} \ln^2\left(\frac{2}{\sqrt{4-3 u} \sqrt{u}-u} + 1\right) -\frac{1}{2} \ln ^2\left(-\frac{2}{-u+\sqrt{4-3 u} 
 \sqrt{u}+2}\right) - \\ 
 \frac{1}{2} \ln ^2\left(\frac{2}{u+\sqrt{4-3 u} \sqrt{u}-2}\right)+\frac{1}{3} \ln
 ^2\left(1-\frac{2}{u+\sqrt{4-3 u} \sqrt{u}}\right) - \\ 
 \frac{2}{3} \ln (1-u) \ln (-u) 
 + \frac{1}{3} \ln ^2(1-u) - \frac{1}{6} \ln ^2(-u) -\frac{\pi ^2}{2}. 
\end{gathered}$$ For all $u \in \mathbb{C} \setminus \mathbb{R}_{>0}$, we have that $\mathcal{L}(u) = \mathcal{E}(u)$. For $u \in \mathbb{R}_{>0}$, we have that $\Re\left(\mathcal{L}(u) \right) = \Re\left( \mathcal{E}(u) \right)$ and that $$\lim_{b \to 0} \Im\left(\mathcal{L}(u + bi) \right) = \lim_{b \to 0} \Im\left(\mathcal{L}(u + bi) \right).$$
:::

::: proof
*Proof.* Consider the cubic integrals $$\label{w1w2forCampbell}
w_1 = \int_{0}^{1} \frac{\ln\left(1 - \frac{1}{u(1-u)^2} x(1-x)^2\right)}{1-x} \, dx \text{ and } w_2 = \int_{0}^{1} \frac{\ln\left(1 - \frac{1}{u(1-u)^2} x(1-x)^2\right)}{x} \, dx$$ along with $$-\frac{z}{6} \sum_{n=0}^{\infty} \left( \frac{4z}{27} \right)^n 
 \left[ \begin{matrix} 
 1, 1, \frac{3}{2} 
 \vspace{1mm} \\ 
 \frac{4}{3}, \frac{5}{3}, 2 \end{matrix} \right]_{n} = 
 \int_0^1 \frac{\ln(1 - z x (1 - x)^2)}{x} \, dx.$$ Using the shifting method found in the first section, we have $\frac{w_2}{w_1}=2$. Eventuating the integrals and simplification using elementary dilogarithm identities, and we obtain the desired result. ◻
:::

::: example
Setting $u=-1$ we obtain a single-term complex dilogarithm evaluation, with $$\begin{gathered}
 \Re\mathrm{Li}_2\left(-\frac{1}{2} - \frac{i\sqrt{7}}{2}\right) 
 + \frac{\pi^2}{8} 
 + \frac{\ln^2(2)}{4} \\
 + \frac{1}{2} \left(\cot^{-1}\left(\frac{3}{\sqrt{7}}\right)\right)^2 
 - \frac{1}{3} \left(\cot^{-1}\left(\frac{5}{\sqrt{7}}\right)\right)^2 
 - \operatorname{arctan}(\sqrt{7}) \cot^{-1}\left(\frac{3}{\sqrt{7}}\right)=0. 
\end{gathered}$$
:::

::: example
Setting $u = \frac{1}{2}$, we obtain that $$\begin{gathered}
 3 \, \mathrm{Li}_2\left(\frac{3}{4} - \frac{\sqrt{5}}{4}\right) 
 + 3 \, \mathrm{Li}_2\left(\frac{3}{4} + \frac{\sqrt{5}}{4}\right) - \\ 
 \frac{3\pi^2}{4} + \frac{3}{2} \ln^2(3 - \sqrt{5}) 
 - \ln^2(\sqrt{5} - 2) - \ln^2(2 + \sqrt{5}) + \frac{3}{2} \ln^2(3 + \sqrt{5})=0, 
\end{gathered}$$ and this provides a proof of a two-term dilogarithm identity given by Adegoke and Frontczak [@AdegokeFrontczak2024].
:::

::: example
[]{#previously7p6 label="previously7p6"} Setting $u = \frac{1}{2} + bi$, and using the reflection formula for the dilogarithm, this leads us to $$\label{previously7p5}
 \Re \mathrm{Li}_2 \left(\frac{1}{2}+iu \right) = 
 \frac{{\pi}^{2}}{12} - 
 \frac{1}{8} \ln^{2}\left(\frac{1+4u^2}{4} \right) -\frac{({\arctan{(2u)})}^{2}}{2}.$$ If we then plug [\[previously7p5\]](#previously7p5){reference-type="eqref" reference="previously7p5"} into Theorem [\[generalforCampbell\]](#generalforCampbell){reference-type="ref" reference="generalforCampbell"}, we obtain a two-term identity for real $b$, where $r=\left(144 b^4 + 136 b^2 + 25\right)$. This gives us a closed form for $$\begin{gathered}
 \mathrm{Li}_2\left(\frac{3}{4} - \frac{2bi}{4} + \frac{r^{\frac{1}{4}}}{4} 
 \left(\cos\left(\frac{1}{2} \arctan\left(\frac{4b}{12b^2 + 5}\right)\right) 
 + i \sin\left(\frac{1}{2} \arctan\left(\frac{4b}{12b^2 + 5}\right)\right)\right)\right) + \\ 
 \mathrm{Li}_2\left(\frac{3}{4} - \frac{2bi}{4} - \frac{r^{\frac{1}{4}}}{4} 
 \left(\cos\left(\frac{1}{2} \arctan\left(\frac{4b}{12b^2 + 5}\right)\right) 
 + i \sin\left(\frac{1}{2} \arctan\left(\frac{4b}{12b^2 + 5}\right)\right)\right)\right). 
\end{gathered}$$
:::

::: example
Setting $u = \frac{1+\sqrt{5}}{2}$, we obtain a remarkable single-term identity is derived involving the golden ratio, using Theorem [\[generalforCampbell\]](#generalforCampbell){reference-type="ref" reference="generalforCampbell"}, namely $$\begin{aligned}
 \frac{\pi^2}{100} = \Re \operatorname{Li}_2 \left( \frac{1}{4} \left(3 - \sqrt{5} + i \sqrt{10 - 2\sqrt{5}} \right) \right). 
\end{aligned}$$ More compactly, we have that $\frac{\pi^2}{100} = 
 \Re \operatorname{Li}_2(r_o)$, where $r_o \approx 0.1909... + 
 0.5877\ldots{i}$ is a root of $$\label{polynomialCampbell}
 r^4 - 3r^3 + 4r^2 - 2r + 1 = 0.$$ This proves an identity conjectured by Campbell [@Campbell2025], because $1/(2\phi^2)- 1/2\sqrt{-1-1/\phi^2}$ is the same root of the polynomial in [\[polynomialCampbell\]](#polynomialCampbell){reference-type="eqref" reference="polynomialCampbell"}, letting $\phi = \frac{1 + \sqrt{5}}{2}$ denote the golden ratio.
:::
