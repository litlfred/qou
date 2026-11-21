---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-047-96-analysis-of-the-second-term-in-the-pointwise
section_title: "Analysis of the second term in the pointwise estimate II"
section_number: 9.6
pages: 36-37
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.889
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
As we apply Proposition [\[prop-hormiter\]](#prop-hormiter){reference-type="ref" reference="prop-hormiter"} to $\phi=mQ$, the result is the following.

::: prop
Let $\Omega$ be a domain in ${\mathbb C}$ and suppose $Q:\Omega\to{\mathbb R}$ is $C^4$-smooth with both $\varDelta Q>0$ on $\Omega$ and $$\kappa:=\sup_{\Omega}\frac{1}{2\varDelta Q}\varDelta
\log\frac{1}{\varDelta Q}<+\infty.$$ Assume that $f\in L^2_{\mathrm{loc}}(\Omega)$. Then there exists a (norm-minimal) solution $v_0$ to the problem $\bar\partial^2v_0=f$ with $$\int_{\Omega} |v_0|^2 \mathrm{e}^{-2mQ}\mathrm{d}A \le\frac{1}{4m(m-\kappa)}\int_{\Omega} |f|^2 
\frac{\mathrm{e}^{-2mQ}}{[\varDelta Q]^2}\mathrm{d}A,$$ provided that $m>\kappa$ and that the right-hand side is finite. []{#prop-hormiter2 label="prop-hormiter2"}
:::

We now apply the above proposition with $$\begin{gathered}
f(z):=\bar\partial_z^2[\chi_0(z)K^{\langle k\rangle}_{2,m}(z,w)]=
K^{\langle k\rangle}_{2,m}(z,w)\,\bar\partial^2\chi_0(z)+
2[\bar\partial\chi_0(z)][\bar\partial_zK^{\langle k\rangle}_{2,m}(z,w)]
\\
=\big\{\Lfun^{\langle2,k\rangle}(z,w)\,\bar\partial^2\chi_0(z)+
2[\bar\partial\chi_0(z)][\bar\partial_z\Lfun^{\langle2,k\rangle}(z,w)]\big\}
\mathrm{e}^{2mQ(z,w)},
\end{gathered}$$

and calculate that $$\begin{gathered}
|f(z)|\mathrm{e}^{-mQ(z)}\le\big\{|\bar\partial^2\chi_0(z)\Lfun^{\langle2,k\rangle}(z,w)|+
2|\bar\partial\chi_0(z)\bar\partial_w\Lfun^{\langle2,k\rangle}(z,w)|\big\}
\mathrm{e}^{m\mathop{\mathrm{Re}}[2Q(z,w)-Q(z)]}
\\
\le\big\{|\bar\partial^2\chi_0(z)\Lfun^{\langle2,k\rangle}(z,w)|+
2|\bar\partial\chi_0(z)\bar\partial_z\Lfun^{\langle2,k\rangle}(z,w)|\big\}
\mathrm{e}^{mQ(w)-\delta_0 m},
\end{gathered}$$ where as before $\delta_0=\frac{1}{18}r^2\epsilon_0$ and it is assumed that $w\in{\mathbb D}(z_0,\frac13r_0)$. Under the assumptions on $Q$ stated in Proposition [\[prop-hormiter2\]](#prop-hormiter2){reference-type="ref" reference="prop-hormiter2"}, we obtain from that proposition (recall the definition of [\[eq-defv0\]](#eq-defv0){reference-type="eqref" reference="eq-defv0"}) and the above calculation that $$\begin{gathered}
\big\|K^{\langle k\rangle}_{2,m}(\cdot,w) 
\chi_0-{\mathbf P}_{2,m}[K^{\langle k\rangle}_{2,m}(\cdot,w)\chi_0]\big\|_m
\\
\le \frac{[\epsilon_0]^{-1}}{2m^{1/2}(m-\kappa)^{1/2}}\mathrm{e}^{mQ(w)-\delta_0 m}
\big\{\|\bar\partial^2\chi_0\|_{L^2(\Omega)}
\,\|\Lfun^{\langle2,k\rangle}\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}+
2\|\bar\partial\chi_0\|_{L^2(\Omega)}
\|\bar\partial_z\Lfun^{\langle2,k\rangle}\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}\big\}
\\
=\mathrm{O}\bigg((m\epsilon_0)^{-1}\mathrm{e}^{mQ(w)-\delta_0 m}\big\{
r^{-1}\|\Lfun^{\langle2,k\rangle}\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}+
\|\bar\partial_z\Lfun^{\langle2,k\rangle}\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}\big\}\bigg),
\label{eq-9.6.1}
\end{gathered}$$ where the implied constant is absolute and $w\in{\mathbb D}(z_0,\frac13r_0)$, and we assume that $m\ge2\kappa$. If we accept a constant which depends on the triple $(Q,z_0,r)$, then we can simplify [\[eq-9.6.1\]](#eq-9.6.1){reference-type="eqref" reference="eq-9.6.1"} significantly: $$\big\|K^{\langle k\rangle}_{2,m}(\cdot,w) 
\chi_0-{\mathbf P}_{2,m}[K^{\langle k\rangle}_{2,m}(\cdot,w)\chi_0]\big\|_m
=\mathrm{O}(m\mathrm{e}^{mQ(w)-\delta_0 m}),
\label{eq-9.6.2}$$ because the two norms of $\Lfun^{\langle2,k\rangle}$ and $\bar\partial_z\Lfun^{\langle2,k\rangle}$ grow like $\mathrm{O}(m^2)$. Finally, we combine this norm estimate [\[eq-9.6.2\]](#eq-9.6.2){reference-type="eqref" reference="eq-9.6.2"} with control on the point evaluation at $z$ (see Proposition [\[pointwise2\]](#pointwise2){reference-type="ref" reference="pointwise2"}): $$\big|K^{\langle k\rangle}_{2,m}(z,w) 
\chi_0(z)-{\mathbf P}_{2,m}[K^{\langle k\rangle}_{2,m}(\cdot,w)\chi_0](z)\big|
=\mathrm{O}(m^{3/2}\mathrm{e}^{mQ(z)+mQ(w)-\delta_0 m}),\qquad z,w\in{\mathbb D}(z_0,\tfrac13r).
\label{eq-9.6.3}$$
