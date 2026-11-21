---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-003-22-the-weighted-bergman-spaces-and-kernels
section_title: "The weighted Bergman spaces and kernels"
section_number: 2.2
pages: 2-2
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 1.0
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
[]{#subsec-wB label="subsec-wB"}

Let $\Omega$ be a domain in ${\mathbb C}$, and let $\omega:\Omega\to{\mathbb R}_+$ be a continuous function ($\omega$ is frequently called a *weight*). Here, we write ${\mathbb R}_+:=]0,+\infty[$ for the positive half-axis. The space $L^2(\Omega,\omega)$ is the weighted $L^2$-space on $\Omega$ with finite norm $$\|f\|_{L^2(\Omega,\omega)}^2:=\int_\Omega |f(z)|^2\omega(z)\mathrm{d}A(z),
\label{eq-norm0}$$ and associated sesquilinear inner product $$\langle f,g\rangle_{L^2(\Omega,\omega)}:=\int_\Omega f(z)\overline{g(z)}
\omega(z)\mathrm{d}A(z).
\label{eq-innprod1}$$ The corresponding *weighted Bergman space* $\mathrm{A}^2(\Omega,\omega)$ is the linear subspace of $L^2(\Omega,\omega)$ consisting of functions holomorphic in $\Omega$, supplied with the inner product structure of $L^2(\Omega,\omega)$. Given the assumptions on the weight $\omega$, it is easy to check that point evaluations are locally uniformly bounded on $\mathrm{A}^2(\Omega,\omega)$, and, therefore, $\mathrm{A}^2(\Omega,\omega)$ is a norm-closed subspace of $L^2(\Omega,\omega)$. As $L^2(\Omega,\omega)$ is separable, so is $\mathrm{A}^2(\Omega,\omega)$, and we may find a countable orthonormal basis $\phi_1,\phi_2,\phi_3,\ldots$ in $\mathrm{A}^2(\Omega,\omega)$. We then form the function $K=K_{\Omega,\omega}$ -- called the *weighted Bergman kernel* -- given by $$K(z,w):=\sum_{j=1}^{+\infty}\phi_j(z)\overline{\phi_j(w)},\qquad
(z,w)\in\Omega\times\Omega,
\label{eq-bk1}$$ and observe that for fixed $w\in\Omega$, the function $K(\cdot,w)\in \mathrm{A}^2(\Omega,\omega)$ has the reproducing property $$f(w)=\langle f,K(\cdot,w)\rangle_{L^2(\Omega,\omega)},\qquad w\in\Omega.
\label{eq-reprprop1}$$ Here, it is assumed that $f\in \mathrm{A}^2(\Omega,\omega)$. In fact, the weighted Bergman kernel $K$ is uniquely determined by these two properties, which means that $K$ -- initially defined by [\[eq-bk1\]](#eq-bk1){reference-type="eqref" reference="eq-bk1"} in terms of an orthonormal basis -- actually is independent of the choice of basis. Note that above, we implicitly assumed that $\mathrm{A}^2(\Omega,\omega)$ is infinite-dimensional, which need not generally be the case. If it is finite-dimensional, the corresponding sums would range over a finite set of indices $j$ instead.
