---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-021-112-a-sextic-two-term-identity
section_title: "A sextic two-term identity"
section_number: 11.2
pages: 31-33
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 1.0
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
Using Lemma [\[previously10p4\]](#previously10p4){reference-type="ref" reference="previously10p4"}, we set $k=\frac{1}{2}\sec \frac{2\pi}{7}$, and this allows the application of Watson's formula for $\operatorname{Li}_2(k) - \operatorname{Li}_2(k^2)$, so that $$\frac{-2k^2 + k - \sqrt{-3k^2 + 2k + 1} + 1}{2 - 2k^2}=r_2, \frac{-2k^2 + k + \sqrt{-3k^2 + 2k + 1} + 1}{2 - 2k^2}=r_1,$$ where $r_2 = -0.42812..., r_1=1.87316...$ Or exactly, $x^6 - 4 x^5 + 5 x^4 - 2 x^3 + x^2 - x - 1 =0$. Using Roger's L-function, we have that $$\frac{\pi^2}{7} = 
 \operatorname{Li}_2\left(\frac{1}{r_1}\right) + \operatorname{Li}_2\left(\frac{r_2}{r_2 - 1}\right) + 
 \frac{1}{2} \ln\left(\frac{1}{r_1}\right) \ln\left(1 - \frac{1}{r_1}\right) + \frac{1}{2} \ln\left(\frac{r_2}{r_2 - 
 1}\right) \ln\left(\frac{1}{1 - r_2}\right).$$ Now, if we were to set $x = \frac{1}{1-y}$, then we would yield Bytsko's two-term sextic dilogarithm identity [@Bytsko1999], which is composed of the two real roots of $y^6 - 7 y^5 + 19 y^4 - 28 y^3 + 20 y^2 - 7 y + 1=0$. He asks if it is related to the Watson identities, as his result was experimentally derived. We can now answer in the affirmative.

## A two-term identity over $\mathbb{Q}(\sqrt{2})$

Bytsko [@Bytsko1999] also conjectured a two-term identity over $\mathbb{Q}(\sqrt{2})$ through asymptotic analysis. As above, Bytsko noted that a proof is lacking. It can be proven by iterating Lemma [\[previously10p4\]](#previously10p4){reference-type="ref" reference="previously10p4"} again via Roger's five-term identity. We thus have a new dilogarithm identity composed of $$z(k) = \frac{k^2 + (k + 1) \sqrt{-3k^2 + 2k + 1} - 
 2k - 1}{2(k^2 - k - 1)}$$ and $$w(k) = \frac{k^2 - (k + 1) \sqrt{-3k^2 + 2k + 1} - 2k - 1}{2(k^2 - k - 1)}.$$ Now, we have to show that for $\operatorname{Li}_2(k) - \operatorname{Li}_2(k^2) - \operatorname{Li}_2\left( \frac{k^3}{(k - 1)(k + 1)^2} \right)$ the dilogarithm parts cancel, in which we let $k=2^{-1/2}$. Substituting into $z(k)$, we have $\frac{1}{2} \left( 3 - \sqrt{2} - \sqrt{2\sqrt{2} - 
 1} \right)$, which is a root of $x^4 - 6 x^3 + 13 x^2 - 10 x + 1=0$. This agrees with Bytsko's result.

## A ladder related to $\rm{Cl}_2\big(\tfrac{\pi}3\big)$

The Gieseking constant may be defined as the singular value of the Clausen function $\rm{Cl}_2\big(\tfrac{\pi}3\big)$. Using Lemma [\[previously10p3\]](#previously10p3){reference-type="ref" reference="previously10p3"}, we solve $$\label{previously13p7}
 \frac{(u-1) \left(2 u^3 - 4 u^2 + 3 u - \sqrt{u(4 - 3 u)}\right)}{2 \left(u^4 - 3 u^3 + 4 u^2 - 2 u + 1\right)} = \frac{1}{2}$$ We also have $\sqrt{u (4 - 3u)} = \frac{2u^3 - 5u^2 + 2u + 2}{2 - u}$. And noting that $\frac{2 u^3 - 6 u^2 + 
 4 u + 1}{(u - 2)(u - 1)^2} = e^{\pi i / 3}$ is equivalent to [\[previously13p7\]](#previously13p7){reference-type="eqref" reference="previously13p7"}. Thus, where $r_1=-0.141... - 0.215.. i$ or exactly as a root of $x^4 - 4 x^3 + 14 x^2 + 4 x + 1=0$: $$2 \space \Im\operatorname{Li}_2(r_1) - \frac{1}{2} \space\Im\operatorname{Li}_2(r_1^2) + \Im\operatorname{Li}_2\left(e^{i\pi/3}\right) = -2 \arg(1 - r_1) \ln|r_1| + \arg(1 - r_1^2) \ln|r_1|$$ Moreover, we have that $$4 \space\Im\operatorname{Li}_2(r_2) - 
 \frac{1}{2} \space\Im\operatorname{Li}_2(r_2^2) - 
 \frac{11}{6}\space \Im\operatorname{Li}_2\left(e^{i\pi/3}\right) = -4 \arg(1 - r_2) \ln|r_2| + \arg(1 - r_2^2) \ln|r_2|$$ Where $r_2=0.34861... + 0.20127... i$ or exactly as a root of $3 x^4 - 15 x^3 + 28 x^2 - 15 x + 3 = 0$. Technically, $\rm{Cl}_2\big(\tfrac{\pi}3\big)$ is a polylogarithmic value, so it is not a strict ladder.
