---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-015-8-applications-of-rogers-identity
section_title: "Applications of Roger's identity"
section_number: 8
pages: 23-26
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 1.0
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
Our below applications of Roger's identity are useful in the construction of new dilogarithm ladder relations, as we later demonstrate.

::: lemma
[]{#previously10p1 label="previously10p1"} The equality of $$\begin{gathered}
 3 \operatorname{Li}_2\left(\frac{-2u^2 + 3u + \sqrt{-u (3u - 4)}}{4u - 2u^2}\right) + 
 3 \operatorname{Li}_2\left(\frac{-2u^2 + 3u - \sqrt{-u (3u - 4)}}{4u - 2u^2}\right) + \\ 
 3 \operatorname{Li}_2(u) + 3 \operatorname{Li}_2((u - 1)^2) 
\end{gathered}$$ and $$\begin{gathered}
 \text{ {\footnotesize $ - \frac{3}{2} \ln^2\left(\frac{2}{u - \sqrt{(4 - 3u) u} - 2}\right) 
 - \frac{3}{2} \ln^2\left(\frac{2}{u + \sqrt{(4 - 3u) u} - 2}\right) 
 + \ln^2\left(1 - \frac{2}{u + \sqrt{(4 - 3u) u}}\right) $ } } \\ 
 \text{ { \footnotesize $ + \ln^2\left(1 + \frac{2}{\sqrt{(4 - 3u) u} - u}\right) 
 - 3 \ln\left(\frac{u - \sqrt{-u (3u - 4)}}{4u - 2u^2}\right) 
 \ln\left(\frac{u + \sqrt{-u (3u - 4)}}{4u - 2u^2}\right) + $ } } \\ 
 \text{ { \footnotesize $ \ln^2(1 - u) - \frac{\ln^2(-u)}{2} - 2 \ln(-u) \ln(1 - u) - \frac{3 \pi^2 }{2}$. } } 
 
\end{gathered}$$ holds for complex $u$.
:::

::: proof
*Proof.* By setting $$w = \frac{-u - \sqrt{(4 - 3u)u} + 2}{2} \ \ \ \text{and} \ \ \ z = \frac{-u + \sqrt{(4 - 3u)u} + 2}{2},$$ the desired result follows from the application of Roger's identity to Theorem [\[generalforCampbell\]](#generalforCampbell){reference-type="ref" reference="generalforCampbell"}. ◻
:::

::: lemma
[]{#previously10p2 label="previously10p2"} The equality of $$\begin{gathered}
 \operatorname{Li}_2 \left( \frac{2 u^2 - 3 u - \sqrt{u(4-3u)}}{2 (u-1)^2} \right) 
 + \operatorname{Li}_2 \left( \frac{(u - 1) \left(2 u^3 - 4 u^2 + 3 u - \sqrt{u(4 - 
 3 u)} \right)}{2 \left(u^4 - 3 u^3 + 4 u^2 - 2 u + 1\right)} \right) \\ 
 + \operatorname{Li}_2 \left( \frac{u \left( u^2 - u + (u - 1) \sqrt{u(4-3u)} + 
 2 \right)}{2 \left(u^4 - 3 u^3 + 4 u^2 - 2 u + 1\right)} \right) 
 + \operatorname{Li}_2 \left( \frac{u \left(2 u^2 - 3 u + \sqrt{u(4-3u)}\right)}{2 (u-1)^2} \right) 
\end{gathered}$$ and the closed form $$\begin{gathered}
 \text{ { \footnotesize $ - \ln \left( \frac{u^2 - u + (u - 
 1) \sqrt{u(4 - 3 u)} + 2}{2 \left(u^4 - 3 u^3 + 4 u^2 - 2 u + 1\right)} \right) 
 \ln \left( \frac{(u - 1) \left(2 u^3 - 5 u^2 - u \sqrt{(4 - 3 u) u} + 4 u - 2\right)}{2 \left(u^4 - 3 u^3 + 
 4 u^2 - 2 u + 1\right)} \right) - $ } } \\ 
 \text{ { \footnotesize $ \frac{3}{2} \ln^2 \left( 1 - \frac{u - \sqrt{u(4-3u)}}{2(u-1)} \right) - 
 \frac{1}{2} \ln^2 (1 - u)$. } }
\end{gathered}$$ holds for complex $u$.
:::

::: proof
*Proof.* Setting $w = u$ and $$z = \frac{2u^2-3u \pm \sqrt{(4 - 3u)u} + 2}{2(u-1)^2},$$ the desired result follows from the application of Roger's identity to Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}. ◻
:::

::: lemma
[]{#previously10p3 label="previously10p3"} The equality of $$\begin{gathered}
 \operatorname{Li}_2\left(\frac{u - \sqrt{u(4 - 3u)}}{4u - 2u^2}\right) + 
 \operatorname{Li}_2\left(\frac{u + \sqrt{u(4 - 3u)}}{4u - 2u^2}\right) + \\ 
 \operatorname{Li}_2\left(\frac{1}{(u - 1)^2}\right) + \operatorname{Li}_2\left(\frac{u}{u - 1}\right) - \frac{\pi^2}{3} 
\end{gathered}$$ and the closed form $$\begin{gathered}
 \text{ { \footnotesize $ \frac{3}{2} \ln^2 \left(\frac{u - \sqrt{-u (3 u - 4)} - 2}{2 (u - 1)}\right) 
 - \ln \left(\frac{-2 u^2 + 3 u + \sqrt{-u (3 u - 4)}}{4 u - 2 u^2}\right) \ln \left(\frac{2 
 u^2 - 3 u + \sqrt{-u (3 u - 4)}}{2 (u - 2) u}\right) $ } } \\ 
 \text{ { \footnotesize $ - \ln \left(\frac{-u + \sqrt{(4-3 u) u} + 2}{2 (u - 
 1)^2}\right) \ln \left(\frac{2 u^2 - 3 u - \sqrt{-u (3u-4)}}{2(u-1)^2}\right) - $}} \\ 
 \text{ { \footnotesize $ \ln \left(\frac{-u - \sqrt{(4 - 3 u) u} + 2}{2 (u - 1)^2}\right) \ln \left(\frac{2 
 u^2 - 3 u + \sqrt{-u (3 u - 4)}}{2(u-1)^2}\right)$ } }
\end{gathered}$$ holds for complex $u$.
:::

::: proof
*Proof.* Setting $$w = \frac{-u + \sqrt{-u (3 u - 4)} + 2}{2 (u - 1)^2} \ \ \ \text{and} \ \ \ z = \frac{-u - \sqrt{-u (3 u - 4)} + 2}{2 (u - 
 1)^2},$$ the desired result follows through an application of Euler's identity and then Roger's identity to Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}. ◻
:::

::: lemma
[]{#previously10p4 label="previously10p4"} The equality of $$\begin{gathered}
 \operatorname{Li}_2(k) - \operatorname{Li}_2(k^2) 
 - \operatorname{Li}_2\left(\frac{-2k^2 + k - \sqrt{-3k^2 + 2k + 1} + 1}{2 - 2k^2}\right) - \\ 
 \operatorname{Li}_2\left(\frac{-2k^2 + k + \sqrt{-3k^2 + 2k + 1} + 1}{2 - 2k^2}\right) 
\end{gathered}$$ and the closed form $$\begin{gathered}
\frac{1}{2} \ln^2\left(\frac{-2}{-\sqrt{-3k^2 + 2k + 1} + k + 1}\right) 
+ \frac{1}{2} \ln^2\left(\frac{-2}{\sqrt{-3k^2 + 2k + 1} + k + 1}\right)\\ 
- \frac{1}{3} \ln^2\left(1 - \frac{2}{\sqrt{-3k^2 + 2k + 1} - k + 1}\right)
- \frac{1}{3} \ln^2\left(\frac{2}{\sqrt{-3k^2 + 2k + 1} + k - 1} + 1\right) \\
+ \ln\left(\frac{\sqrt{-3k^2 + 2k + 1} - k + 1}{2 - 2k^2}\right) 
\ln\left(\frac{\sqrt{-3k^2 + 2k + 1} + k - 1}{2k^2 - 2}\right)\\
+ \frac{1}{2} \pi^2 + \frac{1}{6} \ln^2(1 - k) - \frac{1}{3} \ln(1 - k) \ln k - \frac{1}{3} \ln^2 k
\end{gathered}$$ holds for complex $k$.
:::

::: proof
*Proof.* This follows from the application of Roger's identity to Theorem [\[generalforCampbell\]](#generalforCampbell){reference-type="ref" reference="generalforCampbell"}, with $$w=\left(\frac{-u + 
 \sqrt{(4 - 3u)u} + 2}{2}\right) \ \ \ 
 \text{and} \ \ \ 
 z=\left(\frac{-u - \sqrt{(4 - 3u)u} + 2}{2}\right),$$ and by enforcing the substituion $u=1-k$. ◻
:::

::: lemma
[]{#previously10p5 label="previously10p5"} The equality of $$\begin{gathered}
 - \operatorname{Li}_2 \left( (u - 1) u \right) 
 + \operatorname{Li}_2 \left( \frac{-u^3 + 5u^2 + \sqrt{u(4 - 3u)} (u^2 - u - 1) - 5u}{2(u - 1)^2} \right) 
 - \operatorname{Li}_2 \left( \frac{u}{u - 1} \right)\\ 
 + \operatorname{Li}_2 \left( \frac{-u^3 + 5u^2 - \sqrt{u(4 - 3u)} (u^2 - u - 1) - 5u}{2(u - 1)^2} \right) 
\end{gathered}$$ and the closed form $$\begin{gathered}
 - \frac{3}{2} \ln^2 \left( 1 - \frac{u - \sqrt{u(4 - 3u)}}{2(u - 1)} \right)\\ 
 + \ln \left( \frac{-u + \sqrt{-u(3u - 4)} + 2}{2(u - 1)^2} \right) 
 \ln \left( \frac{-(u + \sqrt{-u(3u - 4)} - 2)}{2(u - 1)^2} \right) 
\end{gathered}$$ holds for complex $u$.
:::

::: proof
*Proof.* This follows form the application of Abel's five-term identity to Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"} where $w = \frac{-u + \sqrt{-u (3 u - 4)} + 2}{2 (u - 1)^2}, z = \frac{-u - \sqrt{-u (3 u - 4)} + 2}{2 (u - 1)^2}$. ◻
:::
