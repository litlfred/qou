---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-016-9-derivation-of-the-loxton--lewin-fracpi9-identi
section_title: "Derivation of the Loxton--Lewin $\frac{\pi}{9}$-identities"
section_number: 9
pages: 26-27
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 1.0
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
In this section, we derive an elementary proof to the trio of three and four-term Loxton-Lewin dilogarithm $\frac{\pi}{9}$-identities. For reference, the three-term is identity given by, where $h = \frac{1}{2} \sec\left(\frac{\pi}{9}\right)$: $$\begin{aligned}
 \left( \operatorname{Li}_2(h) + \frac{1}{2} \ln(h) \ln(1 - h) \right) 
 + \left( \operatorname{Li}_2(h^2) + \frac{1}{2} \ln(h^2) \ln(1 - h^2) \right) - \\ 
 \frac{1}{3} \left( \operatorname{Li}_2(h^3) + \frac{1}{2} \ln(h^3) \ln(1 - h^3) \right)=7\pi^2/54, 
\end{aligned}$$ Using the latter identity in Theorem [\[previously8p1\]](#previously8p1){reference-type="ref" reference="previously8p1"} and applying the Euler reflection identity in [\[Eulerreflectionidentity\]](#Eulerreflectionidentity){reference-type="eqref" reference="Eulerreflectionidentity"} and then letting $u=1-k$, we have to show that the expression below yields the sought three-term relation in terms of $h$: $$\begin{gathered}
 - \operatorname{Li}_2\left(\frac{2 k^2 - k - \sqrt{-3 k^2 + 2 k + 1} - 1}{2 k^2}\right) - \\ 
 \operatorname{Li}_2\left(\frac{2 k^2 - k + \sqrt{-3 k^2 + 2 k + 1} - 1}{2 k^2}\right) 
 - \operatorname{Li}_2(1-k). 
\end{gathered}$$ We then set $$\begin{aligned}
\frac{\sqrt{-3 k^2 + 2 k + 1}}{2 k^2 - k - 1} = -i \sqrt{3}
\end{aligned}$$ This gives the polynomial $3 k^3 - 3 k^1 - 1 =0$, which has the solution: $k=\frac{-2}{\sqrt{3}} \sin\left(\frac{\pi}{9}\right)$.

With reference to the polylogarithm multiplication formula $$\label{previously11p4}
\begin{aligned}
 \sum_{m=0}^{p-1} \operatorname{Li}_s(z e^{2\pi i m/p}) = p^{1-s} \operatorname{Li}_s(z^p), 
\end{aligned}$$ we may obtain that $$\label{previously11p5}
\begin{aligned}
 -\operatorname{Li}_2(r) + \frac{1}{3} \operatorname{Li}_2(r^3) = 
 \operatorname{Li}_2\left(r e^{2\pi i / 3}\right)+\operatorname{Li}_2\left(r e^{4\pi i / 3}\right) 
\end{aligned}$$ So now we derive $r$, which is the radius/norm, given by: $$\frac{\sqrt{(2 k^2 - k - 1)^2 - (-3 k^2 + 2 k + 1)}}{2 k^2} = \sqrt{\frac{k - 1}{k}}=\frac{1}{h}$$ To prove this, make a substitution $3 (1/(1-x^2))^3 - 3 (1/(1-x^2))^1 - 1 =0$. Here, $k= (1/(1-x^2))$ This factors as $(x^3 - 3 x - 1) (x^3 - 3 x + 1) = 0$. We choose the polynomial $(x^3 - 3 x - 1)$, which has a root $1.87...$ which is $1/h$. Using the dilogarithm relation in [\[sigmasumLi\]](#sigmasumLi){reference-type="eqref" reference="sigmasumLi"}, we find that $$\label{previously11p7}
 - \operatorname{Li}_2\left(\frac{2 k^2 - k- \sqrt{-3 k^2 + 2 k + 1} + 1}{2 k^2}\right) 
 - \operatorname{Li}_2\left(\frac{2 k^2 - k + \sqrt{-3 k^2 + 2 k + 1} - 1}{2 k^2}\right)$$ reduces to $$-\frac{1}{3} \operatorname{Li}_2(h^{-3}) + \operatorname{Li}_2(h^{-1}).$$ We then use the Landen identity in [\[Landenformula\]](#Landenformula){reference-type="eqref" reference="Landenformula"}, with $\operatorname{Li}_2(1-k)$. By inspection, $\frac{k-1}{k} = h^{-2}$, which is the squared term of the ladder, completing the proof, in so far that we have proven the existence of the identity. Additional simplifications of log terms are required to bring it to the familiar form. This is done in the second proof below.
