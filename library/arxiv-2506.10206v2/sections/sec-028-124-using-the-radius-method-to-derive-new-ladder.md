---
doc_id: arxiv-2506.10206v2
doc_title: "Analytic Dilogarithm Identities"
section_id: sec-028-124-using-the-radius-method-to-derive-new-ladder
section_title: "Using the ``radius method'' to derive new ladders"
section_number: 12.4
pages: 37-38
source_pdf: 2506.10206v2.pdf
source_sha256: d0631a9abd9b1da3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 1.0
doc_brief: "Analytic Dilogarithm Identities — We introduce dilogarithm identities through a beta integral-based technique that we apply to provide analytic proofs of previously conjectured dilogarithm relations"
---
The radius method, as described earlier to derive analytic proofs of the trio of $\frac{\pi}{9}$ identities, can be applied here as well. We apply the five-term dilogarithm identity involved in the proof of Theorem [\[theoremnew6term\]](#theoremnew6term){reference-type="ref" reference="theoremnew6term"}, setting $$\frac{\sqrt{4-3u^2}}{ u^2 - 2} = -i \sqrt{3}$$\
The radius is $r = \sqrt{\frac{u - 1}{u + 1}} \quad \text{proof:} \quad r^2 = \frac{(u - 1)^2}{u^2 - 1} = \frac{u - 1}{u + 1}$. Explicitly, we have that $$\label{radiusfornewladder1}
 r=\frac{1}{4} \left( -1 + \sqrt{33} - \sqrt{2 \left(9 - \sqrt{33} \right)} \right)$$ Consequently, we have that $$\begin{aligned}
\operatorname{Li}_2\left( \frac{u^2 - \sqrt{4 - 3 u^2} - 2}{-(u + 1) u} \right)
+ \operatorname{Li}_2\left( \frac{u^2 + \sqrt{4 - 3 u^2} - 2}{-(u + 1) u} \right)
= -\operatorname{Li}_2(r) + \frac{1}{3} \operatorname{Li}_2(r^3)\\
\operatorname{Li}_2\left( \frac{u^2 - \sqrt{4 - 3 u^2} - 2}{(u + 1) u} \right)
+ \operatorname{Li}_2\left( \frac{u^2 + \sqrt{4 - 3 u^2} - 2}{(u + 1) u} \right)
= -\operatorname{Li}_2(-r) + \frac{1}{3} \operatorname{Li}_2(-r^3)
\end{aligned}$$ The resultant ladder relation is such that $$\begin{gathered}
 -\frac{1}{2} \operatorname{Li}_2(r^6) - \frac{1}{2} \operatorname{Li}_2(r^4) + \frac{4}{3} \operatorname{Li}_2(r^3) + 
 \frac{11}{2} \operatorname{Li}_2(r^2) - 4 \operatorname{Li}_2(r) + 
 \frac{11}{4} \ln(r^2)\ln(1 - r^2) - \\ 
 2 \ln(r)\ln(1 - r) - \frac{1}{4} \ln(r^4)\ln(1 - r^4) + \frac{2}{3} \ln(r^3)\ln(1 - r^3) - \frac{1}{4} \ln(r^6)\ln(1 - r^6) = -\frac{\pi^2}{36} 
\end{gathered}$$ Using a mapping of $u^4 - 5 u^2 + \frac{16}{3} = 0$, where $u = \frac{1+r^2}{1 - r^2}$, we can determine that all possible radii $r$ for ladders derived in the above manner are positive solutions of $(r^4 - r^3 - 6 r^2 - r + 
 1) (r^4 + r^3 - 6 r^2 + r + 1) = 0$, so there are four possible ladders, corresponding to $r_1$, $r_2$, $r_3$, and $r_4$. These ladders may be thought of as being analogues of the trio of ladders related to the value $\frac{\pi}{9}$. Two of these are redundant, given that $r_1=r_3^{-1}$ and $r_2=r_4^{-1}$.

Setting $\frac{\sqrt{4 - 3u^2}}{2 - u^2} = \sqrt{3} \, i$, gives the second radius, with $$\label{radiusfornewladder2}
 r_2 = \frac{1}{4} \left(1 + \sqrt{33} - 
 \sqrt{2 \left(9 + \sqrt{33} \right)} \right)$$ The associated ladder relation is such that $$\begin{gathered}
 \frac{\operatorname{Li}_2(r_2^6)}{6} - \frac{\operatorname{Li}_2(r_2^4)}{2} - \frac{4 \operatorname{Li}_2(r_2^3)}{3} + \frac{7 
 \operatorname{Li}_2(r_2^2)}{2} + 4 \operatorname{Li}_2(r_2) 
 + \frac{7 \ln(r_2^2) \ln(1 - r_2^2) }{4} \\ 
 + 2 \ln(r_2) \ln(1 - r_2) 
 - \frac{\ln(r_2^4) \ln(1 - r_2^4) }{4} - \frac{2 \ln(r_2^3) \ln(1 - r_2^3) }{3} 
 + \frac{ \ln(r_2^6) \ln(1 - r_2^6) }{12} = \frac{11\pi^2}{36} 
 
\end{gathered}$$ We emphasize that our ladder relations involving the value $r$ in [\[radiusfornewladder1\]](#radiusfornewladder1){reference-type="eqref" reference="radiusfornewladder1"} and the value $r_{2}$ in [\[radiusfornewladder2\]](#radiusfornewladder2){reference-type="eqref" reference="radiusfornewladder2"} appear to be new and not in any of the literature consulted. Gordon and Mcintosh [@GordonMcIntosh1997] note the difficulty about finding dilogarithm ladders that are not of the typical Lewin format. Indeed, this may be seen as requiring innovative approaches, and we encourage further applications of our radius method.
