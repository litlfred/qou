---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-040-82-estimation-of-the-weighted-bergman-kernel-on
section_title: "Estimation of the weighted Bergman kernel on the diagonal"
section_number: 8.2
pages: 33-33
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.905
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
We recall that $\mathrm{PA}^2_{2,m}$ is the weighted bianalytic Bergman space on the domain $\Omega$ in ${\mathbb C}$, supplied with the weight $\mathrm{e}^{-2mQ}$. The associated reproducing kernel is written $K_{2,m}$.

::: cor
[]{#cor-8.2 label="cor-8.2"} Suppose that $z_0\in\Omega$ is such that ${\mathbb D}(z_0,\delta)\Subset\Omega$ for some positive $\delta$. Suppose moreover that $Q$ is $C^{1,1}$-smooth and subharmonic in $\Omega$, with $$A:=
\mathrm{essup}_{z\in{\mathbb D}(z_0,\delta)}\varDelta Q(z)<+\infty.$$ For $m\ge1$, we then have the estimate $$K_{2,m}(z_0,z_0)\le\frac{8 m}{\pi\delta^2}(1+6A^2)\,\mathrm{e}^{2A\delta^2}\mathrm{e}^{2mQ(z_0)}.$$
:::

::: proof
*Proof.* This is a rather immediate consequence of Proposition [\[pointwise2\]](#pointwise2){reference-type="ref" reference="pointwise2"}, as it is well-known that $K_{2,m}(z_0,z_0)$ equals the square of the norm of the point evaluation functional at $z_0$. ◻
:::
