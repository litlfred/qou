---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-007-33-the-first-polyanalytic-bergman-metric
section_title: "The first polyanalytic Bergman metric"
section_number: 3.3
pages: 5-6
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.956
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
We continue the setting of the preceding subsection. Following in the footsteps of Bergman (see Subsection [\[subsec-BM\]](#subsec-BM){reference-type="ref" reference="subsec-BM"}), we would like to introduce polyanalytic analogues of Bergman's first and second metrics, respectively. Let us first discuss a property of the weighted Bergman kernel $K=K_1$ (with $q=1$). *The function $K(z,w)$ on $\Omega\times\Omega$ is uniquely determined by its diagonal restriction $K(z,z)$*. This is so because because the diagonal $z=w$ is a set of uniqueness for functions holomorphic in $(z,\bar w)$. So, if we fix the weight $\omega$, the first and second Bergman metrics both retain all essential properties of the kernel $K(z,w)$ itself. The same can not be said for the weighted $q$-analytic Bergman kernel $K_q$. To remedy this, we consider the double-diagonal restriction $z=w$ and $z'=w'$ in the lifted kernel $\mathbf{E}_{\otimes2}[K_q]$ instead: $$\mathbf{E}_{\otimes2}[K_q](z,z';z,z')=
\sum_{j=1}^{+\infty}|\mathbf{E}[\phi_j](z,z')|^2,
\qquad (z,z')\in\Omega\times{\mathbb C}.
\label{eq-bk4}$$ If we know just the restriction to the double diagonal $z=w$ and $z'=w'$ of $\mathbf{E}_{\otimes2}[K_q]$ we are able to recover the full kernel lifted kernel $\mathbf{E}_{\otimes2}[K_q]$. If we put $z'=z+\epsilon$, where $\epsilon\in{\mathbb C}$, we may expand the extension of $\phi_j$ in a finite Taylor series: $$\mathbf{E}[\phi_j](z,z+\epsilon)=\sum_{k=0}^{q-1}\frac{1}{k!}\bar\partial_z^k\phi_j(z)
\bar\epsilon^k.
\label{eq-bk5}$$ As we insert [\[eq-bk5\]](#eq-bk5){reference-type="eqref" reference="eq-bk5"} into [\[eq-bk4\]](#eq-bk4){reference-type="eqref" reference="eq-bk4"}, the result is $$\mathbf{E}_{\otimes2}[K_q](z,z+\epsilon;z,z+\epsilon)=
\sum_{k,k'=0}^{q-1}\frac{\bar\epsilon^{k}\epsilon^{k}}{k!(k')!}
\sum_{j=1}^{+\infty}\bar\partial_z^{k}\phi_j(z)\partial_z^{k'}\bar\phi_j(z),
\qquad (z,\epsilon)\in\Omega\times{\mathbb C}.
\label{eq-bk6}$$ So, to generalize the first Bergman metric we consider the family of (possibly degenerate) metrics $$\mathrm{d}s_{q,\omega,\epsilon}^{\text{\ding{174}}}(z)^2:=
\mathbf{E}_{\otimes2}[K_q](z,z+\epsilon;z,z+\epsilon)\omega(z)|\mathrm{d}z|^2
=\sum_{k,k'=0}^{q-1}\frac{\bar\epsilon^{k}\epsilon^{k'}}{k!(k')!}
\sum_{j=1}^{+\infty}\bar\partial_z^{k}\phi_j(z)\partial_z^{k'}\bar\phi_j(z)
\omega(z)|\mathrm{d}z|^2,
\label{eq-bm101}$$ indexed by $\epsilon\in{\mathbb C}$. We observe that in [\[eq-bm101\]](#eq-bm101){reference-type="eqref" reference="eq-bm101"} we may think of $(\epsilon^0,\ldots,\epsilon^{q-1})$ as a general vector in ${\mathbb C}^q$, by forgetting about the interpretation of the superscript as a power, and [\[eq-bm101\]](#eq-bm101){reference-type="eqref" reference="eq-bm101"} still defines a (possibly degenerate) metric indexed by the ${\mathbb C}^q$-vector $(\epsilon^0,\ldots,\epsilon^{q-1})$; this should have an interpretation in terms of jet manifolds. In other words, the $q\times q$ matrix $$\omega(z)
\begin{pmatrix}
\mathbf{E}_{\otimes2}[K_q](z,z;z,z)
&\cdots&
\frac{1}{(q-1)!}
\partial_{z'}^{q-1}\mathbf{E}_{\otimes2}[K_q](z,z';z,z')\big|_{z':=z}
\\
 \vdots & \ddots & \vdots  \\
\frac{1}{(q-1)!}
\bar\partial_{z'}^{q-1}\mathbf{E}_{\otimes2}[K_q](z,z';z,z')\big|_{z':=z}
&\cdots&
\frac{1}{(q-1)!(q-1)!}
\bar\partial_{z'}^{q-1}\partial_{z'}^{q-1}\mathbf{E}_{\otimes2}[K_q](z,z';z,z')\big|_{z':=z}
\end{pmatrix}
,
\label{eq-varmat1}$$ which depends on $z\in\Omega$, is positive semi-definite.
