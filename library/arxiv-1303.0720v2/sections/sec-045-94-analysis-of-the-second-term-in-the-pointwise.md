---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-045-94-analysis-of-the-second-term-in-the-pointwise
section_title: "Analysis of the second term in the pointwise estimate I"
section_number: 9.4
pages: 35-35
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.919
latex_coverage_ratio: 0.983
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
We proceed to estimate the second term on the right-hand side of [\[glob1\]](#glob1){reference-type="eqref" reference="glob1"}.

We write $$\label{eq-defv0}
v_0(z):=K^{\langle k\rangle}_{2,m}(w,z) 
\chi_0(z)-{\mathbf P}_{2,m}[K^{\langle k\rangle}_{2,m}(\cdot,w)\chi_0](z),$$ and realize that $v=v_0$ is the norm minimal solution in $L^2(\Omega,\mathrm{e}^{-2mQ})$ of the partial differential equation $$\bar\partial^2_z v(z) = \bar\partial^2_z [\chi_0(z)K^{\langle k\rangle}_{2,m}(z,w)].$$ For the $\bar\partial$-equation, there are the classical Hörmander $L^2$-estimates [@horm], [@horm2], which are based on integration by parts and a clever duality argument. Here, luckily we can just iterate the Hörmander $L^2$-estimates to control the solution to the $\bar\partial^2$-equation. We recall that the Hörmander $L^2$-estimate asserts that there exists a (norm-minimal) solution $u_0$ to $\bar\partial u_0=f$ with $$\int_{\Omega} |u_0|^2 \mathrm{e}^{-2\phi}\mathrm{d}A \le\frac12\int_{\Omega} |f|^2 
\frac{\mathrm{e}^{-2\phi}}{\varDelta\phi}\mathrm{d}A,$$ provided $f\in L^2_{\mathrm{loc}}(\Omega)$ and the right-hand side integral converges.

::: prop
Let $\Omega$ be a domain in ${\mathbb C}$ and suppose $\phi:\Omega\to{\mathbb R}$ is a $C^4$-smooth function with both $\varDelta\phi>0$ and $\varDelta\phi+\frac12\varDelta\log\varDelta\phi>0$ on $\Omega$. Assume that $f\in L^2_{\mathrm{loc}}(\Omega)$. Then there exists a (norm-minimal) solution $v_0$ to the problem $\bar\partial^2v_0=f$ with $$\int_{\Omega} |v_0|^2 \mathrm{e}^{-2\phi} \le\frac{1}{4}\int_{\Omega} |f|^2 
\frac{\mathrm{e}^{-2\phi}}{[\varDelta\phi][\varDelta\phi+\frac12\varDelta\log\varDelta\phi]}
\mathrm{d}A,$$ provided that the right-hand side is finite. []{#prop-hormiter label="prop-hormiter"}
:::

::: proof
*Proof.* We apply Hörmander's $L^2$-estimates for the $\bar\partial$-operator with respect to the two weights $\phi$ and $\phi+\frac12\log\varDelta\phi$. The details are quite straightforward and left to the reader. ◻
:::
