---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-032-74-bi-negligible-amplitudes
section_title: "Bi-negligible amplitudes"
section_number: 7.4
pages: 22-23
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.873
latex_coverage_ratio: 0.889
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
We recall the definition of the differential operator $\boldsymbol{\nabla}$ in [\[nabladef\]](#nabladef){reference-type="eqref" reference="nabladef"}. By squaring the operator identity [\[eq-fundid0.1\]](#eq-fundid0.1){reference-type="eqref" reference="eq-fundid0.1"}, we arrive at $$\big\{{\mathbf M}_{\bar \partial_w \theta} \boldsymbol{\nabla}
{\mathbf M}_{\bar \partial_w \theta} \boldsymbol{\nabla}A(z,w) \big\}\, \mathrm{e}^{2m(z-w) \theta} 
=\bar \partial_w^2 \big\{ A(z,w) \mathrm{e}^{2m(z-w)\theta} \big\},$$ provided that $A(z,w)$ depends $C^\infty$-smoothly on the pair $(z,w)$. As a consequence, we have by integration by parts (applied twice) that $$\begin{gathered}
\label{bianalnegliampli}
\int_{\Omega} u(w) \chi_0(w) \big\{{\mathbf M}_{\bar \partial_w \theta} \boldsymbol{\nabla}
{\mathbf M}_{\bar \partial_w \theta} \boldsymbol{\nabla}A(z,w) \big\}\, \mathrm{e}^{2m(z-w) \theta}\mathrm{d}A(w)
\\
= \int_{\Omega} u(w) \chi_0(w) \bar \partial_w^2 \big\{A(z,w) \mathrm{e}^{2m(z-w) \theta} 
\big\} 
\mathrm{d}A(w) 
=\int_{\Omega} A(z,w) \mathrm{e}^{2m(z-w) \theta} \bar\partial_w^2\{u(w)\chi_0(w)\} 
\mathrm{d}A(w) 
\\
=\int_{\Omega} A(z,w) \mathrm{e}^{2m(z-w) \theta} \big\{2\bar\partial_w u(w)\,
\bar\partial_w\chi_0(w)+u(w)\bar\partial_w^2\chi_0(w)\big\} 
\mathrm{d}A(w)
\\
=-\int_{\Omega} u(w) \mathrm{e}^{2m(z-w) \theta} \big\{2\bar\partial_w A(z,w)
\bar\partial_w\chi_0(w)
+A(z,w)[4m(z-w)\bar\partial_w\chi_0(w)\bar\partial_w\theta
+\bar\partial_w^2\chi_0(w)]\big\} 
\mathrm{d}A(w),
\end{gathered}$$ provided $u$ is biholomorphic on ${\mathbb D}(z_0,r)$. If $u\in\mathrm{PA}^2_{2,m}$, we can now obtain the estimate (use [\[Qtaylor2\]](#Qtaylor2){reference-type="eqref" reference="Qtaylor2"}) $$\begin{gathered}
\label{bianalnegliampli2}
\bigg|\int_{\Omega} u(w) \chi_0(w) 
\big\{{\mathbf M}_{\bar \partial_w \theta} \boldsymbol{\nabla}
{\mathbf M}_{\bar \partial_w \theta} \boldsymbol{\nabla}A(z,w) \big\}\, 
\mathrm{e}^{2m(z-w) \theta}\mathrm{d}A(w)\bigg|
\le\mathrm{e}^{mQ(z)-\delta_0m}
\\
\times
\int_{\Omega} |u(w)|\, \mathrm{e}^{-mQ(w)} \big\{2|\bar\partial_w A(z,w)
\bar\partial_w\chi_0(w)|+|A(z,w)|[5mr
|\bar\partial_w\chi_0(w)\bar\partial_w\theta|+|\bar\partial_w^2\chi_0(w)|]
\big\}\mathrm{d}A(w)
\\
\le r^{-1}\mathrm{e}^{mQ(z)-\delta_0m}\|u\|_m\Big\{
2r\|\bar\partial_w A\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}\|\bar\partial\chi_0\|_{L^2(\Omega)}
+\|A\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}[r\|\bar\partial^2\chi_0\|_{L^2(\Omega)}
\\
+5mr^2\|\bar\partial_w\theta\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}
\|\bar\partial\chi_0\|_{L^2(\Omega)}]\Big\}
\\
=\mathrm{O}\big(r^{-1}\mathrm{e}^{mQ(z)-\delta_0m}\|u\|_m
\big\{r\|\bar\partial_w A\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}
+\|A\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}
[1+mr^2\|\bar\partial_w\theta\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}]\big\}\big),
\end{gathered}$$ for $z\in{\mathbb D}(0,\tfrac13r)$, where $\delta_0=\frac{1}{18}r^2\epsilon_0>0$, as before.

We note that the implied constant in [\[bianalnegliampli2\]](#bianalnegliampli2){reference-type="eqref" reference="bianalnegliampli2"} is absolute. If we allow the implied constant in "O" to depend on the triple $(A,z_0,r)$, then the right-hand side of [\[bianalnegliampli2\]](#bianalnegliampli2){reference-type="eqref" reference="bianalnegliampli2"} may be condensed to $\mathrm{O}(m\mathrm{e}^{mQ(z)-\delta_0m}\|u\|_m)$, for $m\ge1$.

Compared with the typical size $\mathrm{e}^{mQ(z)}$, [\[bianalnegliampli2\]](#bianalnegliampli2){reference-type="eqref" reference="bianalnegliampli2"} says that the estimated quantity decays exponentially in $m$. For this reason, we call expressions of the form ${\mathbf M}_{\bar \partial_w \theta} \boldsymbol{\nabla}
{\mathbf M}_{\bar \partial_w \theta} \boldsymbol{\nabla}A$ *bi-negligible amplitudes*.
