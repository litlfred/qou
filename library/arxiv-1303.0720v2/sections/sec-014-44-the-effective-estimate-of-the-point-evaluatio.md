---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-014-44-the-effective-estimate-of-the-point-evaluatio
section_title: "The effective estimate of the point evaluation"
section_number: 4.4
pages: 9-10
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.923
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
The problem with Proposition [\[pointwiseneg\]](#pointwiseneg){reference-type="ref" reference="pointwiseneg"} as it stands is the need to assume that $\psi\le0$. We now show how to reduce the assumption to a minimum.

Given a positive Borel measure $\mu$ on ${\mathbb D}$ with finite *Riesz mass* $$\int_{\mathbb D}(1-|z|^2)\mathrm{d}\mu(z)<+\infty,$$ we associate the *Green potential* $\mathbf{G}(\mu)$, which is given by

$${\mathbf G}[\mu](z):= \frac{1}{\pi}\int_{{\mathbb D}}\log 
\bigg|\frac{z-w}{1-z\bar w}\bigg|^2\mathrm{d}\mu(w),\qquad z\in{\mathbb D}.$$ The Green potential of a positive measure is subharmonic. It is well-known that the Laplacian $\varDelta\psi$ of a subharmonic function $\psi$ is a positive distribution, which can be identified with a positive Borel measure on ${\mathbb D}$. Then, if $\varDelta\psi$ has finite Riesz mass, we may form the potential ${\mathbf G}[\varDelta\psi]$, which differs from $\psi$ by a harmonic function.

::: prop
[]{#pointwise1 label="pointwise1"} Let $\psi$ be subharmonic and $u$ bianalytic on ${\mathbb D}$. If $\varDelta\psi$ has finite Riesz mass, then $$|u(0)|^2\leq\frac{8}{\pi}\big[1+6|\mathbf{G}[\varDelta\psi](0)|^2 
\big]\, \mathrm{e}^{-2\psi(0)}\int_{\mathbb{D}} |u|^2 \mathrm{e}^{2\psi} \mathrm{d}A.$$
:::

::: proof
*Proof.* We decompose $\psi ={\mathbf G}[\varDelta\psi]+h$, where $h$ is a harmonic function. To the harmonic function $h$ we associate a zero-free analytic function $H$ such that $h =\log|H|$. As the Green potential has $\mathbf{G}[\varDelta\psi]\leq 0$ (this is trivial by computation; it also expresses a version of the maximum principle), we may invoke Proposition [\[pointwiseneg\]](#pointwiseneg){reference-type="ref" reference="pointwiseneg"} with ${\mathbf G}[\varDelta\psi]$ in place of $\psi$, and $uH$ in place of $u$ (The function $uH$ is bianalytic because $H$ is holomorphic and $u$ is bianalytic). The result is $$\begin{gathered}
|u(0)|^2\mathrm{e}^{2h(0)}=|u(0)H(0)|^2 
\leq \frac{8}{\pi}\big[1+6|{\mathbf G}\big[\varDelta\psi](0)|^2 \big] 
\,\mathrm{e}^{-2{\mathbf G}[\varDelta\psi](0)} 
\int_{{\mathbb D}} |u(w)H(w)|^2\mathrm{e}^{2{\mathbf G}[\varDelta\psi](w)} \mathrm{d}A(w) 
\\
=\frac{8}{\pi}\big[1+6|\mathbf{G}\big[\varDelta\Psi](0)|^2\big]
\,\mathrm{e}^{-2{\mathbf G}[\varDelta\psi](0)} 
\int_{{\mathbb D}}|u(w)|^2\mathrm{e}^{2h(w)+2{\mathbf G}{\varDelta\psi](w)}}\mathrm{d}A(w)
\\
=\frac{8}{\pi}\big[1+6|\mathbf{G}[\varDelta\psi](0)|^2\big]
\,\mathrm{e}^{-2{\mathbf G}[\varDelta\psi](0)}\int_{{\mathbb D}}|u(w)|^2\mathrm{e}^{2\psi(w)}\mathrm{d}A(w),
\end{gathered}$$ which is equivalent to the claimed inequality. ◻
:::

::: rem
As stated, the proposition is void unless $${\mathbf G}[\varDelta\psi](0)=\frac{1}{\pi}\int_{\mathbb D}\log|w|^2\mathrm{d}\mu(w)>-\infty.$$
:::
