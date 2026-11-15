---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-043-92-the-basic-pointwise-estimate
section_title: "The basic pointwise estimate"
section_number: 9.2
pages: 33-34
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.938
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
We let the potential $Q$, the point $z_0$, the radius $r$, and the cut-off function $\chi_0$ be as in Subsections [\[subsec-assQ\]](#subsec-assQ){reference-type="ref" reference="subsec-assQ"} and [\[subsec-5.3\]](#subsec-5.3){reference-type="ref" reference="subsec-5.3"}, with the additional requirement mentioned in Subsection [\[subsec-6.2\]](#subsec-6.2){reference-type="ref" reference="subsec-6.2"}. In particular, we have that ${\mathbb D}(z_0,r)\Subset\Omega$. We begin with a local weighted bianalytic Bergman kernel $\mathrm{mod}(m^{-k-1})$, $$K^{\langle k\rangle}_{2,m}(z,w)=\Lfun^{\langle2,k\rangle}(z,w)\,\mathrm{e}^{2mQ(z,w)},$$ where $$\Lfun^{\langle 2,k\rangle}:=m^2\Lfun^{2}_0+m\Lfun^{2}_1+\cdots+m^{-k+1}
\Lfun^{2}_{k+1}
\label{eq-9.2.1}$$ is a finite asymptotic expansion (here, it is assumed that $z,w\in\mathbb{D}(z_0, r)$ for the expression to make sense). The "coefficients" $\Lfun^2_j$ are biholomorphic separately in $(z,\bar w)$ in ${\mathbb D}(z_0,r)\times{\mathbb D}(z_0,r)$, and in principle they can be obtained from the criteria [\[negliampeq3.b\]](#negliampeq3.b){reference-type="eqref" reference="negliampeq3.b"}, but that is easy to say and hard to do. The first two "coefficients" were derived in Subsection [\[subsec-III\]](#subsec-III){reference-type="ref" reference="subsec-III"}, and the formula for the third "coefficient" was mentioned as well. Let us write $\mathbf{I}_{2,m}^{\langle k\rangle}$ for the integral operator $$\mathbf{I}^{\langle k\rangle}_{2,m} [f](z):=\int_{\Omega}f(w) K^{\langle k\rangle}_{2,m}
(z,w)\chi_0(w)\,\mathrm{e}^{-2mQ(w)}\mathrm{d}A(w).$$

We quickly check that $${\mathbf P}_{2,m}\big[K^{\langle k\rangle}_{2,m}(\cdot,w)\chi_0\big](z) = 
\overline{\mathbf{I}^{\langle k\rangle}_{2,m}[K_{2,m}(\cdot,z)](w)}, 
\label{eq-9.2.2}$$ where we recall that ${\mathbf P}_{2,m}$ stands for the orthogonal projection $L^2(\Omega,\mathrm{e}^{-2mQ})\to\mathrm{PA}^2_{2,m}$, and $K_{2,m}$ is as before the weighted bianalytic Bergman kernel on $\Omega$ with weight $\mathrm{e}^{-2mQ}$. We would like to show that $K_{2,m}^{\langle k\rangle}$ and $K_{2,m}$ are close pointwise. By [\[eq-9.2.2\]](#eq-9.2.2){reference-type="eqref" reference="eq-9.2.2"} and the triangle inequality, we have that

$$\begin{gathered}
\big| K_{2,m}(z,w)-K^{\langle k\rangle}_{2,m}(z,w)\chi_0(z)\big| 
\le\big|K_{2,m}(w,z)-\mathbf{I}^{\langle k\rangle}_{2,m}[K_{2,m}(\cdot,z)](w)\big| 
\\
+\big|K^{\langle k\rangle}_{2,m}(z,w) 
\chi_0(z)-{\mathbf P}_{2,m}[K^{\langle k\rangle}_{2,m}(\cdot,w)\chi_0](z)\big|.
\label{glob1}
\end{gathered}$$
