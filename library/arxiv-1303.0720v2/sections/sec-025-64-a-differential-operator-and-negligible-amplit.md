---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-025-64-a-differential-operator-and-negligible-amplit
section_title: "A differential operator and negligible amplitudes"
section_number: 6.4
pages: 16-16
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 1.0
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
The corrective algorithm involves the differential operator $$\boldsymbol{\nabla}:= 
\frac{1}{\bar\partial_w\theta} \bar \partial_w + 2m{\mathbf M}_{z-w}
\label{nabladef}$$ and a (formal) diffusion operator ${\mathbf S}$ which will be described in detail later on. In [\[nabladef\]](#nabladef){reference-type="eqref" reference="nabladef"} and more generally in the sequel, ${\mathbf M}$ with a subscript stands for the operator of multiplication by the function in the subscript. The differential operator $\boldsymbol{\nabla}$ has the property that for smooth functions $A$ on ${\mathbb D}(z_0,r)\times{\mathbb D}(z_0,r)$, $$\frac{1}{\bar\partial_w\theta}
\bar\partial_w \big\{ A(z,w) \,\mathrm{e}^{2m(z-w) \theta(z,w)} \big\}
=\mathrm{e}^{2m(z-w) \theta(z,w)}\boldsymbol{\nabla}A(z,w),
\label{eq-fundid0}$$ which we may express in the more abstract (intertwining) form $${\mathbf M}_{\bar\partial_w\theta}
\boldsymbol{\nabla}={\mathbf M}_{\mathrm{e}^{-2m(z-w)\theta}}\bar\partial_w {\mathbf M}_{\mathrm{e}^{2m(z-w)\theta}}.
\label{eq-fundid0.1}$$ It follows from [\[eq-fundid0\]](#eq-fundid0){reference-type="eqref" reference="eq-fundid0"} that if $u$ is a holomorphic function on ${\mathbb D}(z_0,r)$, then $$\begin{gathered}
\label{nablanegli}
\int_{\Omega} u(w) \chi_0(w) [\bar\partial_w \theta(z,w)] 
[\boldsymbol{\nabla}A(z,w)]\, \mathrm{e}^{2m(z-w) \theta(z,w)} \mathrm{d}A(w) 
\\
= \int_{\Omega} u(w) \chi_0(w) \bar \partial_w 
\big\{ A(z,w) \,\mathrm{e}^{2m(z-w)\theta(z,w)} \big\} \mathrm{d}A(w) 
=\int_{\Omega} u(w) A(z,w) \,\mathrm{e}^{2m(z-w)\theta(z,w)} \bar\partial\chi_0(w)\mathrm{d}A(w) 
\end{gathered}$$ which we may estimate using [\[Qtaylor2\]](#Qtaylor2){reference-type="eqref" reference="Qtaylor2"}: $$\begin{gathered}
\label{nablanegli1.1}
\bigg|\int_{\Omega} u(w) \chi_0(w) [\bar\partial_w \theta(z,w)] 
[\boldsymbol{\nabla}A(z,w)]\, \mathrm{e}^{2m(z-w) \theta(z,w)} \mathrm{d}A(w) \bigg|
\\
\le
\mathrm{e}^{mQ(z)-\delta_0m}\int_{\Omega} |u(w) A(z,w)| \,\mathrm{e}^{-mQ(w)}|\bar\partial\chi_0(w)|\mathrm{d}A(w) 
\\
\le\mathrm{e}^{mQ(z)-\delta_0m}\|A\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}\|u\|_m
\|\bar\partial\chi_0\|_{L^2(\Omega)} =
\mathrm{O}\big(\mathrm{e}^{mQ(z)-\delta_0m}\|A\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}\|u\|_m\big),
\qquad z\in{\mathbb D}(z_0,\tfrac13r),
\end{gathered}$$ where the implied constant is absolute. Here, $\delta_0=\frac{1}{18}r^2\epsilon_0$ as before, and the norm of $A$ is the supremum norm on the bidisk ${\mathbb D}(z_0,\tfrac34r)^2=
{\mathbb D}(z_0,\tfrac34r)\times{\mathbb D}(z_0,\tfrac34r)$. Compared with the typical size $\mathrm{O}(\mathrm{e}^{mQ(z)})$, this means that we have exponential decay in $m$.

For this reason functions of the form ${\mathbf M}_{\bar\partial_w\theta}
\boldsymbol{\nabla}A$ are called *negligible amplitudes*.
