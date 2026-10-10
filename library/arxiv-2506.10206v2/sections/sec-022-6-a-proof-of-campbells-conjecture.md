---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic dilogarithm identities"
section_id: sec-022-6-a-proof-of-campbells-conjecture
section_title: "A proof of Campbell’s conjecture"
section_number: 6
pages: 16-18
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
text_source: latex
latex_prose_ratio: 0.655
latex_coverage_ratio: 0.975
doc_brief: "Analytic dilogarithm identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
To solve an open problem recently given by Campbell [@Campbell2025], we begin with the following dilogarithm identity that we have obtained through our beta integral-based method.

::: theorem
[]{#generalforCampbell label="generalforCampbell"} For complex $u$, let $\mathcal{L}(u)$ denote the three-term dilogarithm combination $$\operatorname{Li}_{2}\left( \frac{ 2-\sqrt{4 - 
 3 u} \sqrt{u}-u }{2} \right) + \operatorname{Li}_{2}\left( \frac{2+\sqrt{4-3 u} \sqrt{u}-u}{2} \right) + 
 \operatorname{Li}_{2}(u)$$ and let $\mathcal{E}(u)$ denote the elementary expression $$\begin{multline*}
 \frac{1}{3} \ln^2\left(\frac{2}{\sqrt{4-3 u} \sqrt{u}-u} + 1\right) -\frac{1}{2} \ln ^2\left(-\frac{2}{-u+\sqrt{4-3 u} 
 \sqrt{u}+2}\right) - \\ 
 \frac{1}{2} \ln ^2\left(\frac{2}{u+\sqrt{4-3 u} \sqrt{u}-2}\right)+\frac{1}{3} \ln
 ^2\left(1-\frac{2}{u+\sqrt{4-3 u} \sqrt{u}}\right) - \\ 
 \frac{2}{3} \ln (1-u) \ln (-u) 
 + \frac{1}{3} \ln ^2(1-u) - \frac{1}{6} \ln ^2(-u) -\frac{\pi ^2}{2}.
\end{multline*}$$ For all $u \in \mathbb{C} \setminus \mathbb{R}_{>0}$, we have that $\mathcal{L}(u) = \mathcal{E}(u)$. For $u \in \mathbb{R}_{>0}$, we have that $\Re\left(\mathcal{L}(u) \right) = \Re\left( \mathcal{E}(u) \right)$ and that $$\lim_{b \to 0} \Im\left(\mathcal{L}(u + bi) \right) = \lim_{b \to 0} \Im\left(\mathcal{L}(u + bi) \right).$$
:::

::: proof
*Proof.* Consider the cubic integrals $$\begin{equation}
\label{w1w2forCampbell}
w_1 = \int_{0}^{1} \frac{\ln\left(1 - \frac{1}{u(1-u)^2} x(1-x)^2\right)}{1-x} \, dx \text{ and } w_2 = \int_{0}^{1} \frac{\ln\left(1 - \frac{1}{u(1-u)^2} x(1-x)^2\right)}{x} \, dx
\end{equation}$$ along with $$-\frac{z}{6} \sum_{n=0}^{\infty} \left( \frac{4z}{27} \right)^n 
 \left[ \begin{matrix} 
 1, 1, \frac{3}{2} 
 \vspace{1mm} \\ 
 \frac{4}{3}, \frac{5}{3}, 2 \end{matrix} \right]_{n} = 
 \int_0^1 \frac{\ln(1 - z x (1 - x)^2)}{x} \, dx.$$ Using the shifting method found in the first section, we have $\frac{w_2}{w_1}=2$. Eventuating the integrals and simplification using elementary dilogarithm identities, and we obtain the desired result. ◻
:::

::: example
Setting $u=-1$ we obtain a single-term complex dilogarithm evaluation, with $$\begin{multline*}
 \Re\mathrm{Li}_2\left(-\frac{1}{2} - \frac{i\sqrt{7}}{2}\right) 
 + \frac{\pi^2}{8} 
 + \frac{\ln^2(2)}{4} \\
 + \frac{1}{2} \left(\cot^{-1}\left(\frac{3}{\sqrt{7}}\right)\right)^2 
 - \frac{1}{3} \left(\cot^{-1}\left(\frac{5}{\sqrt{7}}\right)\right)^2 
 - \operatorname{arctan}(\sqrt{7}) \cot^{-1}\left(\frac{3}{\sqrt{7}}\right)=0.
\end{multline*}$$
:::

::: example
Setting $u = \frac{1}{2}$, we obtain that $$\begin{multline*}
 3 \, \mathrm{Li}_2\left(\frac{3}{4} - \frac{\sqrt{5}}{4}\right) 
 + 3 \, \mathrm{Li}_2\left(\frac{3}{4} + \frac{\sqrt{5}}{4}\right) - \\ 
 \frac{3\pi^2}{4} + \frac{3}{2} \ln^2(3 - \sqrt{5}) 
 - \ln^2(\sqrt{5} - 2) - \ln^2(2 + \sqrt{5}) + \frac{3}{2} \ln^2(3 + \sqrt{5})=0,
\end{multline*}$$ and this provides a proof of a two-term dilogarithm identity given by Adegoke and Frontczak [@AdegokeFrontczak2024].
:::

::: example
[]{#previously7p6 label="previously7p6"} Setting $u = \frac{1}{2} + bi$, and using the reflection formula for the dilogarithm, this leads us to $$\begin{equation}
\label{previously7p5}
 \Re \mathrm{Li}_2 \left(\frac{1}{2}+iu \right) = 
 \frac{{\pi}^{2}}{12} - 
 \frac{1}{8} \ln^{2}\left(\frac{1+4u^2}{4} \right) -\frac{({\arctan{(2u)})}^{2}}{2}.
\end{equation}$$ If we then plug [\[previously7p5\]](#previously7p5){reference-type="eqref" reference="previously7p5"} into Theorem [\[generalforCampbell\]](#generalforCampbell){reference-type="ref" reference="generalforCampbell"}, we obtain a two-term identity for real $b$, where $r=\left(144 b^4 + 136 b^2 + 25\right)$. This gives us a closed form for $$\begin{multline*}
 \mathrm{Li}_2\left(\frac{3}{4} - \frac{2bi}{4} + \frac{r^{\frac{1}{4}}}{4} 
 \left(\cos\left(\frac{1}{2} \arctan\left(\frac{4b}{12b^2 + 5}\right)\right) 
 + i \sin\left(\frac{1}{2} \arctan\left(\frac{4b}{12b^2 + 5}\right)\right)\right)\right) + \\ 
 \mathrm{Li}_2\left(\frac{3}{4} - \frac{2bi}{4} - \frac{r^{\frac{1}{4}}}{4} 
 \left(\cos\left(\frac{1}{2} \arctan\left(\frac{4b}{12b^2 + 5}\right)\right) 
 + i \sin\left(\frac{1}{2} \arctan\left(\frac{4b}{12b^2 + 5}\right)\right)\right)\right).
\end{multline*}$$
:::

::: example
Setting $u = \frac{1+\sqrt{5}}{2}$, we obtain a remarkable single-term identity is derived involving the golden ratio, using Theorem [\[generalforCampbell\]](#generalforCampbell){reference-type="ref" reference="generalforCampbell"}, namely $$\begin{equation*}
\begin{aligned}
 \frac{\pi^2}{100} = \Re \operatorname{Li}_2 \left( \frac{1}{4} \left(3 - \sqrt{5} + i \sqrt{10 - 2\sqrt{5}} \right) \right). 
\end{aligned}
\end{equation*}$$ More compactly, we have that $\frac{\pi^2}{100} = 
 \Re \operatorname{Li}_2(r_o)$, where $r_o \approx 0.1909... + 
 0.5877\ldots{i}$ is a root of $$\begin{equation}
\label{polynomialCampbell}
 r^4 - 3r^3 + 4r^2 - 2r + 1 = 0.
\end{equation}$$ This proves an identity conjectured by Campbell [@Campbell2025], because $1/(2\phi^2)- 1/2\sqrt{-1-1/\phi^2}$ is the same root of the polynomial in [\[polynomialCampbell\]](#polynomialCampbell){reference-type="eqref" reference="polynomialCampbell"}, letting $\phi = \frac{1 + \sqrt{5}}{2}$ denote the golden ratio.
:::

## Related dilogarithm identities

In this section, we provide some further dilogarithm identities that we have obtained following a similar approach, relative to the material given above, and we encourage further explorations based on this material. To begin with, we consider some identities that are related to Theorem [\[generalforCampbell\]](#generalforCampbell){reference-type="ref" reference="generalforCampbell"} and that may be derived in a similar way, relative to Theorem [\[generalforCampbell\]](#generalforCampbell){reference-type="ref" reference="generalforCampbell"}.

::: theorem
[]{#previously8p1 label="previously8p1"} The three-term dilogarithm combination $$- 3\mathrm{Li}_2(u) + 3\mathrm{Li}_2\left(\frac{2}{-u - \sqrt{(4 - 3u) u} + 2}\right) 
+ 3\mathrm{Li}_2\left(\frac{2}{-u + \sqrt{(4 - 3u) u} + 2}\right)$$ admits the closed form $$\begin{multline*}
 -\ln^2(1 - u) + \frac{1}{2} \ln^2(-u) + 2\ln(-u) \ln(1 - u) + \frac{\pi^2}{2}\\
- \ln^2\left(1 - \frac{2}{u + \sqrt{4 - 3u} \sqrt{u}}\right) 
- \ln^2\left(\frac{2}{\sqrt{4 - 3u} \sqrt{u} - u} + 1\right).
\end{multline*}$$ Equivalently, the three-term dilogarithm combination $$-3 \operatorname{Li}_2(u) 
 + 3 \operatorname{Li}_2\left(\frac{-u + \sqrt{(4 - 3 u) u} + 2}{2 (u - 1)^2}\right) 
 + 3 \operatorname{Li}_2\left(\frac{-u - \sqrt{(4 - 3 u) u} + 2}{2 (u - 1)^2}\right)$$ admits the closed form $$\begin{multline*}
 - \ln^2(1 - u) + \frac{1}{2} \ln^2(-u) + 2 \ln(-u) \ln(1 - u) + \frac{\pi^2}{2} \\ 
 - \ln^2\left(\frac{2 u^2 - 3 u + \sqrt{u (4-3u)}}{2 (u - 1) u}\right) 
- \ln^2\left(\frac{2 u^2 - 3 u - \sqrt{u (4-3u)}}{2 (u - 1) u}\right).
\end{multline*}$$
:::

::: proof
*Proof.* This can be established following a similar approach relative to the proof of Theorem [\[generalforCampbell\]](#generalforCampbell){reference-type="ref" reference="generalforCampbell"}. ◻
:::

This leads us toward the following result.

::: theorem
[]{#previouslymaster label="previouslymaster"} For $|u|<1$, we have that $$\begin{multline*}
 - \operatorname{Li_2} \left( \frac{2 u^2 - 3 u + \sqrt{ u (4-3u)}}{2 (u-1)^2} \right) 
 - \operatorname{Li_2} \left( \frac{2 u^2 - 3 u - \sqrt{ u (4-3u)}}{2 (u-1)^2} \right) \\ 
 = \frac{3}{2} \ln^2 \left( 1 - \frac{u - \sqrt{(4 - 3 u) u}}{2 (u-1)} \right) 
 - \operatorname{Li_2} \left( \frac{u}{u - 1} \right).
\end{multline*}$$
:::

::: proof
*Proof.* By Roger's five-term identity, we have that $$w = \frac{2u^2 - 3u + \sqrt{(4 - 3u)u}}{2(u - 1)^2} \ \ \ \text{and} \ \ \ 
 z = \frac{2u^2 - 3u - \sqrt{(4 - 3u)u}}{2(u - 1)^2}.$$ By then applying the Landen identity, we obtain that $$\operatorname{Li}_2 \left(\frac{u + \sqrt{(4 - 3u) u}}{2 (u - 1)}\right) + \operatorname{Li}_2\left(\frac{u - 
 \sqrt{(4 - 3u) u}}{2 (u - 1)}\right) = -\frac{1}{2} \ln^2\left(1 - \frac{u + \sqrt{(4 - 3u) u}}{2 (u - 1)}\right).$$ Similarly, for $|u|<1$, we obtain the vanishing of $$\begin{multline*}
 \ln\left(\frac{-u + \sqrt{u (4-3u)} + 2}{2 - 2 u}\right) \ln\left(\frac{u + \sqrt{u (4-3u)} - 2}{2 (u - 1)}\right) + \\ 
 \ln^2\left(1 - \frac{u + \sqrt{(4 - 3 u) u}}{2 (u - 1)}\right) = 0.
\end{multline*}$$ This may be obtained by setting $$a = \frac{2 - u + \sqrt{u(4 - 3u)}}{2 - 2u} \ \ \ \text{and} \ \ \ b = \frac{-2 + u + \sqrt{u(4 - 
 3u)}}{-2 + 2u},$$ since the above equalities yield $(\ln(a)+\ln(b))^2-\ln^2(a)-\ln(a)\ln(b)=\ln^2(b) + 
 \ln(a)\ln(b)$. Because $ab=1$, we have that $(\ln(a)+\ln(b))^2=0$, so we have that $0= \ln^2(b)+\ln(a)\ln(b) + 
 \ln^2(a)+\ln(a)\ln(b)=(\ln(a)+\ln(b))^2=0$. ◻
:::

::: example
Setting $u=-1$ in Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}, this yields $$\begin{equation*}
\frac{\pi^2}{24} - \frac{ \ln^2(2)}{4} + \frac{1}{3} \left(\operatorname{arctan} 
 \left(\frac{\sqrt{7}}{5}\right) \right)^2 = \Re\mathrm{Li}_2 \left(\frac{3 - i \sqrt{7}}{8} \right),
\end{equation*}$$ and this evaluation appears to be original.
:::

::: example
Setting $u = \frac{1}{2} + \frac{3i\sqrt{7}}{14}$ in Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}, with $b= \frac{3\sqrt{7}}{14}$, we find that $$\begin{multline*}
 \frac{3\pi^2}{8} - \frac{\ln^2(8)}{2} + \frac{3}{8} \ln\left(\frac{49}{8}\right) \ln(8) 
 - \pi \operatorname{arctan} \left(\frac{3}{\sqrt{7}}\right) 
 + \operatorname{arctan} \left(\frac{3}{\sqrt{7}}\right)^2 + \\ 
 \operatorname{arctan} \left(\frac{\sqrt{7}}{11}\right)^2 
 + \operatorname{arctan} (\sqrt{7})^2 
 = \frac{3 }{4} \mathrm{Li}_2\left(\frac{1}{8}\right)+ 3 \, \Re \, \mathrm{Li}_2 \left(\frac{21 + i \sqrt{7}}{32} \right).
\end{multline*}$$
:::

::: example
Setting $u=-7$ in Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}, this yields $$\begin{equation*}
\begin{aligned}
\frac{3}{4} \operatorname{Li}_2\left(\frac{1}{8}\right)= - \frac{1}{2} \left(\operatorname{arctan} \left(\frac{5}{17 \sqrt{7}}\right)\right)^2 + \frac{3}{2}\Re\operatorname{Li}_2\left(\frac{9 - 5 i \sqrt{7}}{128}\right). 
\end{aligned}
\end{equation*}$$
:::

::: example
Using Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}, we have also discovered the ladder relation such that $$\begin{equation}
\label{previously8p8}
 \operatorname{Li}_2(r^{-6}) - 2 \operatorname{Li}_2(r^{-3}) 
 + 2 \operatorname{Li}_2\left(r^{-2}\right) = \arctan^2\left(\frac{\sqrt{7}}{11}\right) 
 - \frac{\ln^2(2)}{4},
\end{equation}$$ writing $r=\left(\frac{1 + i \sqrt{7}}{2}\right)$. This can be obtained with the use of the relations such that $$\left( \frac{1 + i \sqrt{7}}{2} \right)^3 = -\frac{5}{2} + \frac{i \sqrt{7}}{2},$$ and such that $$\operatorname{Li}_2\left( \left( -\frac{5}{2} + \frac{i \sqrt{7}}{2} \right)^{-1} \right)
+ \operatorname{Li}_2\left( \left( \frac{5}{2} + \frac{i \sqrt{7}}{2} \right)^{-1} \right)
- \frac{1}{2} \operatorname{Li}_2\left( \left( \frac{1}{2}(1 + i \sqrt{7}) \right)^{-6} \right) = 0,$$ and such that $$\operatorname{Li}_2\left( \left( \frac{5}{2} + \frac{i \sqrt{7}}{2} \right)^{-1} \right)
 = -\frac{1}{2} \ln^2\left( 1 - \left( \frac{1 + i \sqrt{7}}{2} \right)^{-2} \right) 
 - \operatorname{Li}_2\left( \left( \frac{1 + i \sqrt{7}}{2} \right)^{-2} \right).$$
:::

::: example
Setting $u = \frac{3-\sqrt{5}}{2}$ in Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}, this can be used to obtain an evaluation for the two-term dilogarithm combination $$- 3 \mathrm{Li}_2\left(\frac{2 + \sqrt{5} - \sqrt{3 + 2 \sqrt{5}}}{2} \right) - 3 \mathrm{Li}_2\left(\frac{2 + 
 \sqrt{5} + \sqrt{3 + 2 \sqrt{5}}}{2} \right)$$ previously derived by Bytsko [@Bytsko1999].
:::
