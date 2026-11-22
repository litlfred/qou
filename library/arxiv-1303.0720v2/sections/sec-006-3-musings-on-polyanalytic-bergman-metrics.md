---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-006-3-musings-on-polyanalytic-bergman-metrics
section_title: "Musings on polyanalytic Bergman metrics"
section_number: 3
pages: 4-5
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.955
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
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
