---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-039-81-estimation-of-point-evaluations-for-local-wei
section_title: "Estimation of point evaluations for local weighted Bergman spaces"
section_number: 8.1
pages: 31-33
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.859
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
The spaces $\mathrm{PA}^2_{q,m}$ considered in this paper involve the weight $\mathrm{e}^{-2mQ}$, where (locally at least) $Q$ is subharmonic and smooth. The estimates we derived in Section [\[sec-interlude\]](#sec-interlude){reference-type="ref" reference="sec-interlude"} for $q=2$ do not apply immediately, as the weights considered there had rather the converse property of being exponentials of subharmonic functions. Nevertheless, this difficulty is easy to overcome. Compare with, e.g., [@ahm1] for the analytic case.

::: prop
[]{#pointwise2 label="pointwise2"} Let $u$ be bianalytic in the disk ${\mathbb D}(z_0,\delta m^{-1/2})$, where $\delta$ is a positive real parameter and $m\ge1$. Suppose $Q$ is $C^{1,1}$-smooth in $\bar{\mathbb D}(z_0,\delta)$ and subharmonic in ${\mathbb D}(z_0,\delta)$, with $$A:=
\mathrm{essup}_{z\in{\mathbb D}(z_0,\delta)}\varDelta Q(z)<+\infty.$$ We then have the estimate $$|u(z_0)|^2\le\frac{8m}{\pi\delta^2}(1+6A^2)\,\mathrm{e}^{2A\delta^2}\mathrm{e}^{2mQ(z_0)}
\int_{{\mathbb D}(z_0,\delta m^{-1/2})}|u|^2\mathrm{e}^{-2mQ}\mathrm{d}A.$$
:::

::: proof
*Proof.* Without loss of generality, we may assume that $z_0=0$. For $\xi\in{\mathbb D}$, we put $$\psi_m(\xi):=A\delta^2|\xi|^2-m Q(\delta m^{-1/2}\xi)\quad\text{and}
\quad u_m(\xi):=u(\delta m^{-1/2}\xi).$$ It is immediate that $$-m Q(\delta m^{-1/2}\xi)\le\psi_m(\xi)\le A\delta^2-m Q(\delta m^{-1/2}\xi),
\label{eq-8.1.1}$$ and we may also check that $$0\le\varDelta\psi_m(\xi)=A\delta^2-\delta^2(\varDelta Q)(\delta m^{-1/2}\xi)
\le A\delta^2,\qquad \xi\in{\mathbb D}.
\label{eq-8.1.2}$$ so that $\psi_m$ is subharmonic, and we obtain that $$0\ge{\mathbf G}[\varDelta\psi_m](0)=\frac{1}{\pi}\int_{\mathbb D}\log|\xi|^2\varDelta\psi_m
(\xi)\mathrm{d}A(\xi)\ge A\delta^2\int_{\mathbb D}\log|\xi|^2\mathrm{d}A(\xi)\ge-A\delta^2.
\label{eq-8.1.3}$$ Next, since $\psi$ is subharmonic with finite Riesz mass, we may apply Proposition [\[pointwise1\]](#pointwise1){reference-type="ref" reference="pointwise1"}: $$\begin{gathered}
|u(0)|^2\mathrm{e}^{-2mQ(0)} = |u_m(0)|^2\mathrm{e}^{2\psi_m(0)} \leq 
\frac{8}{\pi}\big[1+6|\mathbf{G}[\varDelta\psi_m](0)|^2\big] 
\int_{{\mathbb D}} |u_m|^2 \mathrm{e}^{2\psi_m} \mathrm{d}A 
\\ 
\leq \frac{8}{\pi}(1+6A^2\delta^4) 
\int_{{\mathbb D}} |u_m|^2 \mathrm{e}^{2\psi_m} \mathrm{d}A
\le \frac{8}{\pi}(1+6A^2\delta^4)\,\mathrm{e}^{2A\delta^2} \int_{{\mathbb D}} 
|u(\delta m^{-1/2}\xi)|^2 \mathrm{e}^{-2mQ(\delta m^{-1/2}\xi)} \mathrm{d}A(\xi)
\\
=\frac{8m}{\pi\delta^2}(1+6A^2\delta^4)\,\mathrm{e}^{2A\delta^2} \int_{{\mathbb D}(0,\delta m^{-1/2})} 
|u(z)|^2 \mathrm{e}^{-2mQ(z)} \mathrm{d}A(z),
\end{gathered}$$ and the claim follows. Note that we used the estimates [\[eq-8.1.1\]](#eq-8.1.1){reference-type="eqref" reference="eq-8.1.1"} and [\[eq-8.1.2\]](#eq-8.1.2){reference-type="eqref" reference="eq-8.1.2"}. The proof is complete. ◻
:::

We can also estimate the $\bar\partial$-derivative:

::: prop
[]{#pointwisederiv label="pointwisederiv"} Suppose we are in the setting of Proposition [\[pointwise2\]](#pointwise2){reference-type="ref" reference="pointwise2"}. We then have the estimate $$|\bar\partial u(z_0)|^2\le\frac{3m}{\pi\delta^2}\,\mathrm{e}^{2A\delta^2}\mathrm{e}^{2mQ(z_0)}
\int_{{\mathbb D}(z_0,\delta m^{-1/2})}|u|^2\mathrm{e}^{-2mQ}\mathrm{d}A.$$
:::

::: proof
*Proof.* The argument is analogous to that of the proof of Proposition [\[pointwise2\]](#pointwise2){reference-type="ref" reference="pointwise2"}, except that it is based on Proposition [\[pointwiseneg0\]](#pointwiseneg0){reference-type="ref" reference="pointwiseneg0"}. ◻
:::
