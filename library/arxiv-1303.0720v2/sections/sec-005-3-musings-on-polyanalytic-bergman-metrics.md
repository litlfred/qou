---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-005-3-musings-on-polyanalytic-bergman-metrics
section_title: "Musings on polyanalytic Bergman metrics"
section_number: 3
pages: 4-6
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.957
---
[]{#musing-BM label="musing-BM"}

## Bergman's first metric {#subsec-BM}

Stefan Bergman [@Berg] considered the Bergman kernel for the weight $\omega(z)\equiv1$ only. He also introduced the so-called *Bergman metric* in two different ways. We will now discuss the ramifications of Bergman's ideas in the presence of a non-trivial weight $\omega$. We interpret the introduction of the weight $\omega$ as equipping the domain $\Omega$ with the isothermal Riemannian metric and associated two-dimensional volume form $$\mathrm{d}s_\omega(z)^2:=\omega(z)|\mathrm{d}z|^2,\qquad \mathrm{d}A_\omega(z):=
\omega(z)\mathrm{d}A(z).
\label{eq-metric1}$$ *Bergman's first metric* on $\Omega$ is then given by $$\mathrm{d}s_\omega^{\text{\ding{172}}}(z)^2:=K(z,z)\mathrm{d}s_\omega(z)^2
=K(z,z)\omega(z)|\mathrm{d}z|^2,
\label{eq-Bmetric1}$$ where $K=K_{\Omega,\omega}$ is the weighted Bergman kernel given by [\[eq-bk1\]](#eq-bk1){reference-type="eqref" reference="eq-bk1"}.

## Bergman's second metric {#subsec-BM2}

The second metric is related to the Gaussian curvature. The curvature form for the original metric [\[eq-metric1\]](#eq-metric1){reference-type="eqref" reference="eq-metric1"} is (up to a positive constant factor) given by $$\varkappa:=-\varDelta\log\omega(z)\mathrm{d}A(z),
\label{eq-curv1}$$ The curvature form for Bergman's first metric [\[eq-Bmetric1\]](#eq-Bmetric1){reference-type="eqref" reference="eq-Bmetric1"} is similarly $$\varkappa^{\text{\ding{172}}}:=-\varDelta\log[K(z,z)\omega(z)]\mathrm{d}A(z)
=-[\varDelta\log K(z,z)+\varDelta\log\omega(z)]\mathrm{d}A(z),
\label{eq-curv2}$$ and we are led to propose the difference $$\varkappa-\varkappa^{\text{\ding{172}}}=(\varDelta\log K(z,z))\mathrm{d}A(z),
\label{eq-curv3}$$ as the two-dimensional volume form of a metric, *Bergman's second metric*: $$\mathrm{d}s_\omega^{\text{\ding{173}}}(z)^2:=\varDelta\log K(z,z)|\mathrm{d}z|^2.
\label{eq-Bmetric2}$$ We should remark that unless $K(z,z)\equiv0$, the function $z\mapsto\log K(z,z)$ is subharmonic in $\Omega$. This is easily seen from the identity $$K(z,z)=\sum_{j=1}^{+\infty}|\phi_j(z)|^2,
\label{eq-diagrestr1}$$ so $\varDelta\log K(z,z)\ge0$ holds throughout $\Omega$. This means that we can expect [\[eq-Bmetric2\]](#eq-Bmetric2){reference-type="eqref" reference="eq-Bmetric2"} to define a Riemannian metric in $\Omega$ except in very degenerate situations. Bergman's second metric appears to be the more popular metric the several complex variables setting (see, e.g., Chapter 3 of [@GKK]). In the case of the unit disk $\Omega={\mathbb D}$ and the constant weight $\omega(z)\equiv1/(2\pi)$, we find that $$K(z,w)=\frac{2}{(1-z\bar w)^2},$$ so that $$\mathrm{d}s_\omega^{\text{\ding{172}}}(z)^2=\frac{2|\mathrm{d}z|^2}{(1-|z|^2)^2}
\quad\text{and}\quad
\mathrm{d}s_\omega^{\text{\ding{173}}}(z)^2=\frac{2|\mathrm{d}z|^2}{(1-|z|^2)^2},$$ which apparently coincide. This means that the first and second Bergman metrics are the same in this model case (the reason is that the curvature of the first Bergman metric equals $-1$).

## The first polyanalytic Bergman metric

We continue the setting of the preceding subsection. Following in the footsteps of Bergman (see Subsection [0.1](#subsec-BM){reference-type="ref" reference="subsec-BM"}), we would like to introduce polyanalytic analogues of Bergman's first and second metrics, respectively. Let us first discuss a property of the weighted Bergman kernel $K=K_1$ (with $q=1$). *The function $K(z,w)$ on $\Omega\times\Omega$ is uniquely determined by its diagonal restriction $K(z,z)$*. This is so because because the diagonal $z=w$ is a set of uniqueness for functions holomorphic in $(z,\bar w)$. So, if we fix the weight $\omega$, the first and second Bergman metrics both retain all essential properties of the kernel $K(z,w)$ itself. The same can not be said for the weighted $q$-analytic Bergman kernel $K_q$. To remedy this, we consider the double-diagonal restriction $z=w$ and $z'=w'$ in the lifted kernel $\mathbf{E}_{\otimes2}[K_q]$ instead: $$\mathbf{E}_{\otimes2}[K_q](z,z';z,z')=
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
