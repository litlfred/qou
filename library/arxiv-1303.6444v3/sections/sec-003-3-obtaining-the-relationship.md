---
doc_id: arxiv-1303.6444v3
doc_title: "VIRIAL EXPANSION BOUNDS"
section_id: sec-003-3-obtaining-the-relationship
section_title: "Obtaining the Relationship"
section_number: 3
pages: 4-5
source_pdf: 1303.6444v3.pdf
source_sha256: 4f12ace2197f70ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 1.0
doc_brief: "VIRIAL EXPANSION BOUNDS — In the 1960s, the technique of using cluster expansion bounds in order to achieve bounds on the virial expansion was developed by Lebowitz and Penrose (1964) and Ruelle"
---
Lagrange Inversion techniques are the usual approach to obtaining the virial coefficients and this has a nice representation as a contour integral. If we want to compute the coefficient $c_n$, we can take the contour integral (around $0$) of $\frac{\partial P}{\partial \rho}$ divided by $n\rho^n$. This gives us the formula: $$c_n = \frac{1}{2\pi i}\oint_C \, \frac{\frac{\partial P}{\partial \rho}}{n\rho^n}\mathrm{d}\rho$$ We can manipulate this equation to get it in terms of the $z$-variable, since we know about the cluster expansion already. $$\begin{aligned}
 c_n &= \frac{1}{2 \pi i} \oint_{C'} \, \frac{\frac{\partial P}{\partial z}}{n\rho^n}\mathrm{d}z \notag \\
&= \frac{\beta^{-1}}{2n \pi i} \oint_{C'} \, \frac{z\frac{\partial \beta P}{\partial z}}{z\rho^n} \mathrm{d}z \notag \\
&= \frac{\beta^{-1}}{2n \pi i} \oint_{C'} \, \frac{\mathrm{d}z}{z\rho^{n-1}} \label{contourrep} 
\end{aligned}$$ This (implicit) relationship between the virial and the cluster coefficients is our starting point. The idea is that we can bound such an integral quite easily when we consider bounds on $|\rho|$, when we write it in terms of the fugacity $z$ as in [\[clusterexp2\]](#clusterexp2){reference-type="eqref" reference="clusterexp2"}.

Indeed this method is the one used by Ruelle [@R69] and Lebowitz and Penrose [@LPen64].
