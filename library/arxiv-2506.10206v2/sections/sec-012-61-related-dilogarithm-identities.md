---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-012-61-related-dilogarithm-identities
section_title: "Related dilogarithm identities"
section_number: 6.1
pages: 18-21
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 1.0
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
In this section, we provide some further dilogarithm identities that we have obtained following a similar approach, relative to the material given above, and we encourage further explorations based on this material. To begin with, we consider some identities that are related to Theorem [\[generalforCampbell\]](#generalforCampbell){reference-type="ref" reference="generalforCampbell"} and that may be derived in a similar way, relative to Theorem [\[generalforCampbell\]](#generalforCampbell){reference-type="ref" reference="generalforCampbell"}.

::: theorem
[]{#previously8p1 label="previously8p1"} The three-term dilogarithm combination $$- 3\mathrm{Li}_2(u) + 3\mathrm{Li}_2\left(\frac{2}{-u - \sqrt{(4 - 3u) u} + 2}\right) 
+ 3\mathrm{Li}_2\left(\frac{2}{-u + \sqrt{(4 - 3u) u} + 2}\right)$$ admits the closed form $$\begin{gathered}
 -\ln^2(1 - u) + \frac{1}{2} \ln^2(-u) + 2\ln(-u) \ln(1 - u) + \frac{\pi^2}{2}\\
- \ln^2\left(1 - \frac{2}{u + \sqrt{4 - 3u} \sqrt{u}}\right) 
- \ln^2\left(\frac{2}{\sqrt{4 - 3u} \sqrt{u} - u} + 1\right). 
\end{gathered}$$ Equivalently, the three-term dilogarithm combination $$-3 \operatorname{Li}_2(u) 
 + 3 \operatorname{Li}_2\left(\frac{-u + \sqrt{(4 - 3 u) u} + 2}{2 (u - 1)^2}\right) 
 + 3 \operatorname{Li}_2\left(\frac{-u - \sqrt{(4 - 3 u) u} + 2}{2 (u - 1)^2}\right)$$ admits the closed form $$\begin{gathered}
 - \ln^2(1 - u) + \frac{1}{2} \ln^2(-u) + 2 \ln(-u) \ln(1 - u) + \frac{\pi^2}{2} \\ 
 - \ln^2\left(\frac{2 u^2 - 3 u + \sqrt{u (4-3u)}}{2 (u - 1) u}\right) 
- \ln^2\left(\frac{2 u^2 - 3 u - \sqrt{u (4-3u)}}{2 (u - 1) u}\right). 
\end{gathered}$$
:::

::: proof
*Proof.* This can be established following a similar approach relative to the proof of Theorem [\[generalforCampbell\]](#generalforCampbell){reference-type="ref" reference="generalforCampbell"}. ◻
:::

This leads us toward the following result.

::: theorem
[]{#previouslymaster label="previouslymaster"} For $|u|<1$, we have that $$\begin{gathered}
 - \operatorname{Li_2} \left( \frac{2 u^2 - 3 u + \sqrt{ u (4-3u)}}{2 (u-1)^2} \right) 
 - \operatorname{Li_2} \left( \frac{2 u^2 - 3 u - \sqrt{ u (4-3u)}}{2 (u-1)^2} \right) \\ 
 = \frac{3}{2} \ln^2 \left( 1 - \frac{u - \sqrt{(4 - 3 u) u}}{2 (u-1)} \right) 
 - \operatorname{Li_2} \left( \frac{u}{u - 1} \right). 
\end{gathered}$$
:::

::: proof
*Proof.* By Roger's five-term identity, we have that $$w = \frac{2u^2 - 3u + \sqrt{(4 - 3u)u}}{2(u - 1)^2} \ \ \ \text{and} \ \ \ 
 z = \frac{2u^2 - 3u - \sqrt{(4 - 3u)u}}{2(u - 1)^2}.$$ By then applying the Landen identity, we obtain that $$\operatorname{Li}_2 \left(\frac{u + \sqrt{(4 - 3u) u}}{2 (u - 1)}\right) + \operatorname{Li}_2\left(\frac{u - 
 \sqrt{(4 - 3u) u}}{2 (u - 1)}\right) = -\frac{1}{2} \ln^2\left(1 - \frac{u + \sqrt{(4 - 3u) u}}{2 (u - 1)}\right).$$ Similarly, for $|u|<1$, we obtain the vanishing of $$\begin{gathered}
 \ln\left(\frac{-u + \sqrt{u (4-3u)} + 2}{2 - 2 u}\right) \ln\left(\frac{u + \sqrt{u (4-3u)} - 2}{2 (u - 1)}\right) + \\ 
 \ln^2\left(1 - \frac{u + \sqrt{(4 - 3 u) u}}{2 (u - 1)}\right) = 0. 
\end{gathered}$$ This may be obtained by setting $$a = \frac{2 - u + \sqrt{u(4 - 3u)}}{2 - 2u} \ \ \ \text{and} \ \ \ b = \frac{-2 + u + \sqrt{u(4 - 
 3u)}}{-2 + 2u},$$ since the above equalities yield $(\ln(a)+\ln(b))^2-\ln^2(a)-\ln(a)\ln(b)=\ln^2(b) + 
 \ln(a)\ln(b)$. Because $ab=1$, we have that $(\ln(a)+\ln(b))^2=0$, so we have that $0= \ln^2(b)+\ln(a)\ln(b) + 
 \ln^2(a)+\ln(a)\ln(b)=(\ln(a)+\ln(b))^2=0$. ◻
:::

::: example
Setting $u=-1$ in Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}, this yields $$\frac{\pi^2}{24} - \frac{ \ln^2(2)}{4} + \frac{1}{3} \left(\operatorname{arctan} 
 \left(\frac{\sqrt{7}}{5}\right) \right)^2 = \Re\mathrm{Li}_2 \left(\frac{3 - i \sqrt{7}}{8} \right),$$ and this evaluation appears to be original.
:::

::: example
Setting $u = \frac{1}{2} + \frac{3i\sqrt{7}}{14}$ in Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}, with $b= \frac{3\sqrt{7}}{14}$, we find that $$\begin{gathered}
 \frac{3\pi^2}{8} - \frac{\ln^2(8)}{2} + \frac{3}{8} \ln\left(\frac{49}{8}\right) \ln(8) 
 - \pi \operatorname{arctan} \left(\frac{3}{\sqrt{7}}\right) 
 + \operatorname{arctan} \left(\frac{3}{\sqrt{7}}\right)^2 + \\ 
 \operatorname{arctan} \left(\frac{\sqrt{7}}{11}\right)^2 
 + \operatorname{arctan} (\sqrt{7})^2 
 = \frac{3 }{4} \mathrm{Li}_2\left(\frac{1}{8}\right)+ 3 \, \Re \, \mathrm{Li}_2 \left(\frac{21 + i \sqrt{7}}{32} \right). 
\end{gathered}$$
:::

::: example
Setting $u=-7$ in Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}, this yields $$\begin{aligned}
\frac{3}{4} \operatorname{Li}_2\left(\frac{1}{8}\right)= - \frac{1}{2} \left(\operatorname{arctan} \left(\frac{5}{17 \sqrt{7}}\right)\right)^2 + \frac{3}{2}\Re\operatorname{Li}_2\left(\frac{9 - 5 i \sqrt{7}}{128}\right). 
\end{aligned}$$
:::

::: example
Using Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}, we have also discovered the ladder relation such that $$\label{previously8p8}
 \operatorname{Li}_2(r^{-6}) - 2 \operatorname{Li}_2(r^{-3}) 
 + 2 \operatorname{Li}_2\left(r^{-2}\right) = \arctan^2\left(\frac{\sqrt{7}}{11}\right) 
 - \frac{\ln^2(2)}{4},$$ writing $r=\left(\frac{1 + i \sqrt{7}}{2}\right)$. This can be obtained with the use of the relations such that $$\left( \frac{1 + i \sqrt{7}}{2} \right)^3 = -\frac{5}{2} + \frac{i \sqrt{7}}{2},$$ and such that $$\operatorname{Li}_2\left( \left( -\frac{5}{2} + \frac{i \sqrt{7}}{2} \right)^{-1} \right)
+ \operatorname{Li}_2\left( \left( \frac{5}{2} + \frac{i \sqrt{7}}{2} \right)^{-1} \right)
- \frac{1}{2} \operatorname{Li}_2\left( \left( \frac{1}{2}(1 + i \sqrt{7}) \right)^{-6} \right) = 0,$$ and such that $$\operatorname{Li}_2\left( \left( \frac{5}{2} + \frac{i \sqrt{7}}{2} \right)^{-1} \right)
 = -\frac{1}{2} \ln^2\left( 1 - \left( \frac{1 + i \sqrt{7}}{2} \right)^{-2} \right) 
 - \operatorname{Li}_2\left( \left( \frac{1 + i \sqrt{7}}{2} \right)^{-2} \right).$$
:::

::: example
Setting $u = \frac{3-\sqrt{5}}{2}$ in Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}, this can be used to obtain an evaluation for the two-term dilogarithm combination $$- 3 \mathrm{Li}_2\left(\frac{2 + \sqrt{5} - \sqrt{3 + 2 \sqrt{5}}}{2} \right) - 3 \mathrm{Li}_2\left(\frac{2 + 
 \sqrt{5} + \sqrt{3 + 2 \sqrt{5}}}{2} \right)$$ previously derived by Bytsko [@Bytsko1999].
:::
