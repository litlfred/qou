---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-011-6-a-proof-of-campbells-conjecture
section_title: "A proof of Campbell's conjecture"
section_number: 6
pages: 16-18
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 1.0
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
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
