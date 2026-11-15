---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-044-93-analysis-of-the-first-term-in-the-pointwise-e
section_title: "Analysis of the first term in the pointwise estimate"
section_number: 9.3
pages: 34-35
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.892
latex_coverage_ratio: 0.953
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
In the sequel, $k$ is a *fixed nonegative integer*. To estimate the first term on the right-hand side of [\[glob1\]](#glob1){reference-type="eqref" reference="glob1"}, we use that $K^{\langle k\rangle}_{2,m}$ is a local reproducing kernel $\mathrm{mod}(m^{-k})$, which is expressed by [\[negliampeq2.b\]](#negliampeq2.b){reference-type="eqref" reference="negliampeq2.b"}. Before we go into that, we observe that if $u$ is biharmonic in ${\mathbb D}(z_0,r)$, then $$\begin{gathered}
\mathbf{I}^{\langle k\rangle}_{2,m}[u](z)=\int_\Omega u(w)\chi_0(w)
\Lfun^{\langle 2,k\rangle}(z,w)\,\mathrm{e}^{2mQ(z,w)-2mQ(w)}\mathrm{d}A(w)
\\
=\int_\Omega u(w)\chi_0(w)
\Rfun^{(2)}(z,w)\,\mathrm{e}^{2mQ(z,w)-2mQ(w)}\mathrm{d}A(w)
\\
+\int_\Omega u(w)\chi_0(w)
[{\mathbf M}_{\bar\partial_w\theta}\boldsymbol{\nabla}{\mathbf M}_{\bar\partial_w\theta}\boldsymbol{\nabla}
X^{\langle k+2\rangle}]^{\langle k\rangle}(z,w)\,\mathrm{e}^{2mQ(z,w)-2mQ(w)}\mathrm{d}A(w),
\label{eq-9.2.4}
\end{gathered}$$ for $z\in{\mathbb D}(z_0,\tfrac13r)$, where $X^{\langle k+2\rangle}$ is given by [\[eq-recoverX\]](#eq-recoverX){reference-type="eqref" reference="eq-recoverX"}, and $\Lfun^{\langle 2,k\rangle}(z,w)$ is determined uniquely by the criteria [\[negliampeq3.b\]](#negliampeq3.b){reference-type="eqref" reference="negliampeq3.b"} together with the requirement that $\Lfun^{\langle 2,k\rangle}(z,w)$ should be bianalytic in each of the variables $(z,\bar w)$, as worked out in Subsections [\[subsec-I\]](#subsec-I){reference-type="ref" reference="subsec-I"}, [\[subsec-II\]](#subsec-II){reference-type="ref" reference="subsec-II"}, and [\[subsec-III\]](#subsec-III){reference-type="ref" reference="subsec-III"}. We rewrite [\[eq-9.2.4\]](#eq-9.2.4){reference-type="eqref" reference="eq-9.2.4"} in the following form: $$\begin{gathered}
\mathbf{I}^{\langle k\rangle}_{2,m}[u](z)
=\int_\Omega u(w)\chi_0(w)
\Rfun^{(2)}(z,w)\,\mathrm{e}^{2mQ(z,w)-2mQ(w)}\mathrm{d}A(w)
\\
+\int_\Omega u(w)\chi_0(w)
[{\mathbf M}_{\bar\partial_w\theta}\boldsymbol{\nabla}{\mathbf M}_{\bar\partial_w\theta}\boldsymbol{\nabla}
X^{\langle k+2\rangle}]\,\mathrm{e}^{2mQ(z,w)-2mQ(w)}\mathrm{d}A(w)
\\
-m^{-k}\int_\Omega u(w)\chi_0(w)(Y_k+m^{-1}Z_k)\,\mathrm{e}^{2mQ(z,w)-2mQ(w)}\mathrm{d}A(w),
\label{eq-9.2.5}
\end{gathered}$$ where $Y_k,Z_k$ are the expressions $$Y_k:=
{\mathbf M}_{\bar\partial_w\theta}{\pmb{\partial}}_\theta{\mathbf M}_{\bar\partial_w\theta}{\pmb{\partial}}_\theta X_k
+2{\mathbf M}_{\bar\partial_w\theta}\big(
{\pmb{\partial}}_\theta{\mathbf M}_{\bar\partial_w\theta}{\mathbf M}_{z-w}
+{\mathbf M}_{\bar\partial_w\theta}^2{\mathbf M}_{z-w}{\pmb{\partial}}_\theta\big)X_{k+1}.$$ and $$Z_k:={\mathbf M}_{\bar\partial_w\theta}{\pmb{\partial}}_\theta{\mathbf M}_{\bar\partial_w\theta}{\pmb{\partial}}_\theta
X_{k+1}.$$ Here, we recall that $X^{\langle k+2\rangle}=\sum_{j=0}^{k+1}m^{-j}X_j$ is a finite asymptotic expansion (or abschnitt). If we use [\[Qtaylor2\]](#Qtaylor2){reference-type="eqref" reference="Qtaylor2"} to estimate the last term on the right-hand side of [\[eq-9.2.5\]](#eq-9.2.5){reference-type="eqref" reference="eq-9.2.5"}, and combine with Proposition [\[neglipropbi\]](#neglipropbi){reference-type="ref" reference="neglipropbi"} and [\[bianalnegliampli2\]](#bianalnegliampli2){reference-type="eqref" reference="bianalnegliampli2"}, [\[eq-RfunM\]](#eq-RfunM){reference-type="eqref" reference="eq-RfunM"} (just write $X^{\langle k+2\rangle}$ in place of $A$), $$\begin{gathered}
\mathbf{I}^{\langle k\rangle}_{2,m}[u](z)=u(z)
+\mathrm{O}\big(r^{-1}\mathrm{e}^{mQ(z)-\delta_0m}\|u\|_m
\big\{r\|\bar\partial_w X^{\langle k+2\rangle}\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}
\\
+[1+\|X^{\langle k+2\rangle}\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}]
[1+mr^2\|\bar\partial_w\theta\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}]\big\}+m^{-k-\frac12}
\mathrm{e}^{mQ(z)}\|u\|_m\|Y_k+m^{-1}Z_k\|_{L^\infty({\mathbb D}(z_0,\frac34r)^2)}\big),
\label{eq-9.2.6}
\end{gathered}$$ for $z\in{\mathbb D}(z_0,\frac13r)$, where the implied constant is absolute. Given our standing assumptions, all the involved norms are finite. If we accept an implied constant which may depend on the triple $(Q,z_0,r)$, then we can compress [\[eq-9.2.6\]](#eq-9.2.6){reference-type="eqref" reference="eq-9.2.6"} to $$\mathbf{I}^{\langle k\rangle}_{2,m}[u](z)=u(z)+\mathrm{O}(m^{-k-\frac12}
\mathrm{e}^{mQ(z)}\|u\|_m),\qquad z\in{\mathbb D}(z_0,\tfrac13r),
\label{eq-9.2.7}$$ for $m\ge1$. By a duality argument, [\[eq-9.2.7\]](#eq-9.2.7){reference-type="eqref" reference="eq-9.2.7"} implies that $$\big\Vert {\mathbf P}_{2,m}[K^{\langle k\rangle}_{2,m}(\cdot,z)\chi_0]-K_{2,m}(\cdot,z)
\big\Vert_m
=\mathrm{O}(m^{-k-\frac12}\mathrm{e}^{mQ(z)}),\qquad z\in{\mathbb D}(z_0,\tfrac13r).
\label{eq-9.2.7.1}$$

If we apply this estimate [\[eq-9.2.7\]](#eq-9.2.7){reference-type="eqref" reference="eq-9.2.7"} to the function $u(z)=K_{2,m}(z,w)$ (not the dummy variable $w$ used in the above integrals!), we find that (for $m\ge1$) $$\begin{gathered}
\mathbf{I}^{\langle k\rangle}_{2,m}[K_{2,m}(\cdot,w)](z)=K_{2,m}(z,w)
+\mathrm{O}(m^{-k-\frac12}\mathrm{e}^{mQ(z)}K_{2,m}(w,w)^{1/2})
\\
=K_{2,m}(z,w)+\mathrm{O}(m^{-k}\mathrm{e}^{mQ(z)+mQ(w)}),\qquad 
z\in{\mathbb D}(z_0,\tfrac13r),
\label{eq-9.2.7.1}
\end{gathered}$$ where again the implied constant depends on the triple $(Q,z_0,r)$. Note that in the first step, we used that $\|K_{2,m}(\cdot,w)\|_m^2=
K_{2,m}(w,w)$, and in the last step the estimate of Corollary [\[cor-8.2\]](#cor-8.2){reference-type="ref" reference="cor-8.2"} (with $z_0$ replaced by $z$ and with e.g. $\delta=\frac13r$). If we switch the roles of $z$ and $w$ in [\[eq-9.2.7.1\]](#eq-9.2.7.1){reference-type="eqref" reference="eq-9.2.7.1"}, so that e.g. $w\in{\mathbb D}(z_0,\frac13r)$ instead, we obtain an effective estimate of the first term on the right-hand side of [\[glob1\]](#glob1){reference-type="eqref" reference="glob1"}: $$\mathbf{I}^{\langle k\rangle}_{2,m}[K_{2,m}(\cdot,z)](w)
=K_{2,m}(w,z)+\mathrm{O}(m^{-k}\mathrm{e}^{mQ(z)+mQ(w)}),\qquad 
w\in{\mathbb D}(z_0,\tfrac13r).
\label{eq-9.2.8}$$
