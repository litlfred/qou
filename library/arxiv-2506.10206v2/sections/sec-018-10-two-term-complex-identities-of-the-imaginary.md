---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-018-10-two-term-complex-identities-of-the-imaginary
section_title: "Two-term complex identities of the imaginary part"
section_number: 10
pages: 29-31
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 1.0
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
Similar to two-term real dilogarithms, two-term dilogarithms of only the imaginary part appear to be uncommon. Common examples of two-term identities of the complex part include $\operatorname{Li}_2\left(\frac{1}{2} - \frac{i}{2}\right) = -i G + \frac{5\pi^2}{96} - \frac{\ln^2 2}{8} + \frac{i \pi \ln 2}{8}$.

::: example
Using Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}, set $$\frac{2 u^2 - 3 u - \sqrt{u (-3 u + 4)}}{2 (u - 1)^2} = -u$$ The solution is given by $u^3-u-1=0$ (the Plastic constant cubic as before), where the complex root in the second quadrant is chosen. Performing the usual simplification gives: $$-4i \pi \ln(u) + \frac{5 \ln^2(u)}{2} - \frac{5\pi^2}{3} = \operatorname{Li}_2(u) + \frac{1}{2} \operatorname{Li}_2(u^2)$$ Here, the duplication formula for the dilogarithm is implicitly used.
:::

::: example
Using Theorem [\[previouslymaster\]](#previouslymaster){reference-type="ref" reference="previouslymaster"}, set: $$\frac{2 u^2 - 3 u - \sqrt{u (-3 u + 4)}}{2 (u - 1)^2} = 2 - u$$ The solution is given by $u^4 - 4 u^3 + 7 u^2 - 7 u +4=0$ where $u\approx0.45258 - 1.12087 i$. After much simplification, we have: $$\frac{1}{2} \operatorname{Li}_2(2u - u^2) + \operatorname{Li}_2\left(\frac{u - 2}{(u - 1)^2} + u\right) = -\frac{13}{2} \ln^2(u - 1) - 7 i \pi \ln(u - 1) - i \pi \ln(2 - u) + \frac{7\pi^2}{4}$$
:::

::: example
Using Lemma [\[previously10p3\]](#previously10p3){reference-type="ref" reference="previously10p3"}, set: $$\displaystyle \frac{\sqrt{u(4 - 3u)} + u}{4u - 2u^2} = \frac{1}{z}, \\[10pt] 
 \displaystyle \frac{1}{(u - 1)^2} = z$$ This has the solution: $u^6 - 7 u^5 + 19 u^4 - 24 u^3 + 13 u^2 - 2 u + 1=0$ in which the root approximated by $u= -0.00219275 - 0.295542i$ is chosen. The identity follows (using the Bloch-Wigner formula for brevity), where $a_1=\left(\frac{u^3 - 4u^2 + 5u - 1}{2 - u}\right), a_2=\left(\frac{u}{u - 1}\right)$. Thus: $$-\arg(1-a_1)\ln(|a_1|)-\arg(1-a_2)\ln(|a_2|)=\Im\operatorname{Li}_2(a_1) + \Im\operatorname{Li}_2(a_2)$$
:::

::: example
Using Lemma [\[previously10p2\]](#previously10p2){reference-type="ref" reference="previously10p2"}, set: $$\left\{
\begin{aligned}
\frac{(u-1) \left(2 u^3 - 4 u^2 + 3 u - \sqrt{u(4 - 3 u)}\right)}{2 \left(u^4 - 3 u^3 + 4 u^2 - 2 u + 1\right)} = z\\
\frac{u \left(u^2 - u + (u-1) \sqrt{u(4-3u)} + 2\right)}{2 \left(u^4 - 3 u^3 + 4 u^2 - 2 u + 1\right)} = \frac{1}{z}
\end{aligned}
\right.$$ Using the above procedure, we have that $$- \Im \operatorname{Li}_2(v_1) - \Im \operatorname{Li}_2(v_2) = \arg(1 - v_1) \ln(|v_1|) + \arg(1 - v_2) \ln(|v_2|).$$ Applying $u=1-y$ to the final result, we obtain $$v_1=\left( \frac{-(y - 1)^2 (y^3 + y^2 + 1)}{y (y^2 - y + 1)} \right),
v_2=\left( \frac{-(y - 1)^2 (y^3 + y + 1))}{y^2 (y^2 - y + 1)} \right),$$ where $y \approx 0.18866 - 0.83324 i$ is a root of $y^8 - y^7 + y^6 - y^4 + y^2 - y + 1 = 0$. We conjecture that this is the only 8th-degree, two-term dilogarithm combination that admits a closed form and that it is the highest degree identity of this form.
:::
