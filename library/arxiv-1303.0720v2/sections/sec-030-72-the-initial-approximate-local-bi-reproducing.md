---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-030-72-the-initial-approximate-local-bi-reproducing
section_title: "The initial approximate local bi-reproducing kernel"
section_number: 7.2
pages: 20-22
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.907
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
[]{#subsec-6.2 label="subsec-6.2"} We now turn our attention to the space $\mathrm{PA}^2_{q,m}$ with $q=2$ (the bianalytic case). The first step is to find the analogue in this setting of the kernel $M_m$ given by [\[eq-Mm\]](#eq-Mm){reference-type="eqref" reference="eq-Mm"}, and then to obtain an approximate reproducing identity similar to [\[reproeq1\]](#reproeq1){reference-type="eqref" reference="reproeq1"}.

We keep the assumptions on the potential $Q$ and the disk ${\mathbb D}(z_0,r)$ from Subsection [\[subsec-assQ\]](#subsec-assQ){reference-type="ref" reference="subsec-assQ"}, and the smooth cut-off function $\chi_0$ will be as in Subsection [\[subsec-5.3\]](#subsec-5.3){reference-type="ref" reference="subsec-5.3"}. We will need to add the requirement that $r\|\bar\partial^2\chi_0\|_{L^2(\Omega)}$ is uniformly bounded by an *absolute* constant, which is possible to achieve.

Suppose $u$ is *biholomorphic* (or *bianalytic*) in ${\mathbb D}(z_0,r)$, which means that $\bar\partial^2 u=0$ there. It is well-known that the fundamental solution to $\bar\partial_z^2$ is $\bar z/(\pi z)$. By integration by parts applied twice, we have that $$\begin{gathered}
\int_{\Omega} u(w) \chi_0(w)\bar\partial_w^2 \bigg\{\frac{\bar w-\bar z}{w-z}
\mathrm{e}^{2m(z-w)\theta} \bigg\}  \mathrm{d}A(w) 
=\int_{\Omega}\frac{\bar w - \bar z}{w-z}
\mathrm{e}^{2m(z-w)\theta}\bar\partial_w^2\{u(w)\chi_0(w)\}\mathrm{d}A(w) 
\\
=\int_{\Omega}\frac{\bar w-\bar z}{w-z}
\mathrm{e}^{2m(z-w)\theta}\big\{2\bar\partial_w u(w)\bar\partial_w\chi_0(w)+
 u(w)\bar\partial_w^2\chi_0(w)\big\}\mathrm{d}A(w)
\\
=\int_{\Omega}
\mathrm{e}^{2m(z-w)\theta}u(w)\bigg\{2\frac{\bar\partial_w\chi_0(w)}{z-w}
-\frac{\bar w-\bar z}{w-z}\bar\partial_w^2\chi_0(w)
-4m(\bar z-\bar w)\bar\partial_w\chi_0(w)\bar\partial_w\theta\bigg\}\mathrm{d}A(w). 
\label{eq-6.100.1}
\end{gathered}$$ Here, the integral on the left-hand side needs to be understood in the sense of distribution theory. If we combine [\[eq-6.100.1\]](#eq-6.100.1){reference-type="eqref" reference="eq-6.100.1"} with [\[Qtaylor2\]](#Qtaylor2){reference-type="eqref" reference="Qtaylor2"}, it follows that we obtain the estimate $$\begin{gathered}
\bigg|\int_{\Omega} u(w) \chi_0(w)\bar\partial_w^2 
\bigg\{\frac{\bar w-\bar z}{w-z}\mathrm{e}^{2m(z-w)\theta} \bigg\}\mathrm{d}A(w)\bigg| 
\\
\le\mathrm{e}^{mQ(z)-\frac{1}{18}mr^2\Delta Q(z)}\int_{\Omega}|u(w)|
\bigg\{2\bigg|\frac{\bar\partial_w\chi_0(w)}{z-w}\bigg|
+|\bar\partial_w^2\chi_0(w)|
+4m\big|(\bar z-\bar w)\bar\partial_w\chi_0(w)\bar\partial_w\theta\big|\bigg\}
\mathrm{e}^{-mQ(w)}\mathrm{d}A(w),
\end{gathered}$$ for $z\in{\mathbb D}(z_0,\tfrac13r)$. Next, if we assume that $u\in\mathrm{PA}^2_{q,m}$, with $q=2$, so that -- in particular -- $u$ extends biholomorphically to $\Omega$, then $$\begin{gathered}
\bigg|\int_{\Omega} u(w) \chi_0(w)\bar\partial_w^2 
\bigg\{\frac{\bar w-\bar z}{w-z}\mathrm{e}^{2m(z-w)\theta} \bigg\}\mathrm{d}A(w)\bigg| 
\\
\le
r^{-1}\mathrm{e}^{mQ(z)-\frac{1}{18}mr^2\epsilon_0}\|u\|_m\bigg\{



6\|\bar\partial\chi_0\|_ {L^2(\Omega)}
+r\|\bar\partial^2\chi_0\|_ {L^2(\Omega)}
+5mr^2\|\bar\partial\chi_0\|_ {L^2(\Omega)}
\|\bar\partial_w\theta\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}\bigg\},
\\
=\mathrm{O}\big(r^{-1}\mathrm{e}^{mQ(z)-\delta_0m}\|u\|_m
\big\{1+mr^{2}\|\bar\partial_w\theta\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}\big\}\big), 

\label{eq-6.101}
\end{gathered}$$ for $z\in{\mathbb D}(z_0,\tfrac13r)$, where we write as before $\delta_0=\frac{1}{18}r^2\epsilon_0$, and the implied constant is *absolute*.

We interpret [\[eq-6.101\]](#eq-6.101){reference-type="eqref" reference="eq-6.101"} as saying that the left-hand side decays exponentially small compared with the typical size $\mathrm{e}^{mQ(z)}$. Let $\boldsymbol{\delta}_0$ denote the distribution which corresponds to a unit point mass at $0$ in the complex plane ${\mathbb C}$. By a direct calculation, we find that $$\frac{1}{\pi}\bar\partial_w^2 \bigg\{\frac{\bar w-\bar z}{w-z}
\mathrm{e}^{2m(z-w)\theta} \bigg\}=\boldsymbol{\delta}_0(z-w)-M_{2,m}(z,w)\mathrm{e}^{-2mQ(w)},
\label{eq-6.103}$$ where $M_{2,m}$ is the kernel $$M_{2,m}(z,w):=
\bigg\{
\frac{4m}{\pi}\bar\partial_w\theta - \frac{2m}{\pi}
(\bar z-\bar w)\bar\partial_w^2 \theta - \frac{4m^2}{\pi}
|z-w|^2 (\bar \partial_w \theta)^2\bigg\}\,\mathrm{e}^{2mQ(z,w)}.
\label{eq-6.104}$$ The kernel $M_{2,m}$ is the bianalytic analogue of the kernel $M_m$ which was our staring point in Subsection [\[subsec-5.3\]](#subsec-5.3){reference-type="ref" reference="subsec-5.3"}.

It is also automatically bianalytic in $z$, but not necessarily in $\bar w$.

::: prop
[]{#neglipropbi label="neglipropbi"}

We have that for all $u\in\mathrm{PA}^2_{2,m}$, $$u(z)=\int_{\Omega}u(w)\chi_0(w)M_{2,m}(z,w)\,\mathrm{e}^{-2mQ(w)}\mathrm{d}A(w) 
+\mathrm{O}\big(r^{-1}\mathrm{e}^{mQ(z)-\delta_0m}\|u\|_m
\big\{1+mr^{2}\|\bar\partial_w\theta\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}\big\}\big),$$ for $z\in \mathbb{D}(z_0,\tfrac13 r)$, where $\delta_0=\frac{1}{18}r^2\epsilon_0>0$. The implied constant is absolute.
:::

::: proof
*Proof.* This is an immediate consequence of the relation [\[eq-6.103\]](#eq-6.103){reference-type="eqref" reference="eq-6.103"} and of the estimate [\[eq-6.101\]](#eq-6.101){reference-type="eqref" reference="eq-6.101"}. ◻
:::
