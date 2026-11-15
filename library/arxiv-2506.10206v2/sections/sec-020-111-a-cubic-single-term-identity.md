---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-020-111-a-cubic-single-term-identity
section_title: "A cubic single-term identity"
section_number: 11.1
pages: 31-31
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.923
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
Using Lemma [\[previously10p2\]](#previously10p2){reference-type="ref" reference="previously10p2"}, set: $$\begin{aligned}
\frac{(u-1) \left(2 u^3 - 4 u^2 + 3 u - \sqrt{u(4 - 3 u)}\right)}{2 \left(u^4 - 3 u^3 + 4 u^2 - 2 u + 1\right)} = z
\\
\frac{2 u^2 - 3 u - \sqrt{u(4 - 3 u)}}{2 (u-1)^2} = 1 - z
\end{aligned}$$ The solution $u=r_1$ is the real root of $u^3 - 2 u^2 + u + 1=0$. And $z=1/r_2$, where $r_2$ is the complex root located in the fourth quadrant. Consequently, we obtain that $$\begin{aligned}
2 \ln\left(\frac{r_2 - 1}{r_2}\right) \ln\left(\frac{(r_1 - 1) r_2^2}{2 r_1 r_2 + r_1}\right) 
+ 3 \ln^2\left(\frac{1 - r_1}{r_2}\right) 
+ \ln^2(1 - r_1) 
+ \frac{\pi^2}{3} 
= -4 \Re \operatorname{Li}_2\left(r_1 - \frac{r_1}{r_2}\right)
\end{aligned}$$ Using Lemma [\[previously10p1\]](#previously10p1){reference-type="ref" reference="previously10p1"} and setting $u=p^3$, where $p$ is the real root of $u^3-u-1=0$ also gives the single-term dilogarithm in terms of the plastic constant/ratio: $$\begin{aligned}
\frac{\pi^2}{12} + 6 \ln^2(p) + \frac{1}{6} \left( \operatorname{arctan} \left( \frac{\sqrt{p (3 p - 1)}}{p^2 - 2 p^3} \right) \right)^2 
= \Re\mathrm{Li}_2\left( \frac{-p^4 + p^2 i \sqrt{p (3p - 1)}}{2} \right)
\end{aligned}$$
