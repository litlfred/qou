---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-024-63-approximate-local-reproducing-and-bergman-ker
section_title: "Approximate local reproducing and Bergman kernels"
section_number: 6.3
pages: 14-16
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.929
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
[]{#subsec-5.3 label="subsec-5.3"} In [@bbs], the point of departure is an approximate reproducing identity for functions in $\mathrm{A}^2_m$. To state the result, we define the kernel $$M_m(z,w) := \frac{2m}{\pi} \mathrm{e}^{2mQ(z,w)}\bar\partial_w\theta(z,w).
\label{eq-Mm}$$ This kernel is for obvious reasons only defined in some fixed neighborhood of the diagonal. We shall be concerned with the (small) bidisk ${\mathbb D}(z_0,r)\times{\mathbb D}(z_0,r)$ where $M_m(z,w)$ is well-defined, by our assumptions (A:i)--(A:iv) above.To extend the kernel beyond the bidisk, we multiply by a smooth cut-off function $\chi_0(w)$, and think of the product as $0$ off the support of $\chi_0$ (also where $M_m(z,w)$ is undefined). The function $\chi_0(w)$ is $C^\infty$-smooth with $0\le\chi_0\le1$ throughout ${\mathbb C}$, and vanishes off ${\mathbb D}(z_0,\frac34r)$, while it has $\chi_0=1$ on $\mathbb{D}(z_0, \frac23 r)$, and is a function of the distance $|w-z_0|$. We ask in addition that the norm $\|\bar\partial\chi_0\|_{L^2(\Omega)}$ is bounded by an absolute constant, which is possible to achieve. We will use the simplified notation $$\|u\|_{m}:=\|u\|_{L^2(\Omega,\mathrm{e}^{-2mQ})}=\bigg\{\int_\Omega|u|^2\mathrm{e}^{-2mQ}
\mathrm{d}A\bigg\}^{1/2}.
\label{eq-norm1}$$

::: prop
[]{#negliprop label="negliprop"} We have that for all $u\in\mathrm{A}^2_m$, $$u(z)=\int_{\Omega}u(w)\chi_0(w)M_m(z,w)\,\mathrm{e}^{-2mQ(w)}\mathrm{d}A(w) 
+\mathrm{O}(r^{-1}\|u\|_{m} \mathrm{e}^{mQ(z)-m\delta_0}),
\qquad z\in \mathbb{D}(z_0,\tfrac13 r),$$ where we write $\delta_0:=\frac{1}{18}r^2\epsilon_0>0$. The implied constant is absolute.
:::

To develop the necessary intuition, we supply the easy proof.

::: proof
*Proof of Proposition [\[negliprop\]](#negliprop){reference-type="ref" reference="negliprop"}.* Since the Cauchy kernel $1/(\pi z)$ is the fundamental solution to $\bar\partial$, we have by Cauchy-Green theorem (i.e., integration by parts) that $$\begin{gathered}
u(z) =\chi_0(z)u(z)=\int_{\Omega} \frac{1}{\pi(z-w)} \bar \partial_w \Big( u(w) 
\chi_0(w)\,\mathrm{e}^{2m(z-w)\theta(z,w)} \Big) \mathrm{d}A(w) 
\\
= \int_{\Omega} u(w) \chi_0(w) M_m(z,w) \,\mathrm{e}^{-2mQ(w)} \mathrm{d}A(w)  
\\
+ \frac{1}{\pi}\int_{\Omega} u(w) \frac{ \bar \partial_w \chi_0(w)}{z-w}
\mathrm{e}^{2m(z-w) \theta(z,w)}\mathrm{d}A(w),\qquad z\in{\mathbb D}(z_0,\tfrac13 r).
\label{reproeq1}
\end{gathered}$$ It will be enough to show that the last term on the right-hand side of [\[reproeq1\]](#reproeq1){reference-type="eqref" reference="reproeq1"} (the one which involves $\bar \partial_w \chi$) belongs to the error term. By [\[Qtaylor2\]](#Qtaylor2){reference-type="eqref" reference="Qtaylor2"} and the Cauchy-Schwarz inequality, we have that $$\begin{gathered}
\frac{1}{\pi}\int_{\Omega}\bigg|u(w) \frac{\bar\partial_w \chi_0(w)}{z-w}
\mathrm{e}^{2m(z-w)\theta}  \bigg|\mathrm{d}A(w) 
\leq  
\int_{\Omega} \bigg| u(w) \frac{\bar\partial_w \chi_0(w)}{z-w}\bigg| 
\,\mathrm{e}^{mQ(z)- mQ(w)- \frac12 m \varDelta Q(z) |w-z|^2} \mathrm{d}A(w) 
\\
\leq \|u\|_{m}\mathrm{e}^{mQ(z)} 
\bigg\{\int_{\Omega}\bigg|\frac{\bar\partial_w\chi_0(w)}{z-w} 
\bigg|^2 
\mathrm{e}^{-m\varDelta Q(z)|w-z|^2} \mathrm{d}A(w) \bigg\}^{1/2} 

\leq \frac{3}{r}\|\bar\partial\chi_0\|_{L^2(\Omega)} \|u\|_{m}
\mathrm{e}^{mQ(z)}\mathrm{e}^{-\frac{1}{18}m r^2\varDelta Q(z)}, 
\end{gathered}$$ again for $z\in{\mathbb D}(z_0,\frac13 r)$, and the desired conclusion is immediate. ◻
:::

We will interpret Proposition [\[negliprop\]](#negliprop){reference-type="ref" reference="negliprop"} as saying that the function $M_m(z,w)$ is an local reproducing kernel $\text{mod}(\mathrm{e}^{-\delta m})$, with $\delta=\delta_0>0$. More generally, a function $L_m(z,w)$ defined on ${\mathbb D}(z_0,r)$ and holomorphic in $z$ is a *a local reproducing kernel* $\text{mod}(\mathrm{e}^{-\delta m})$ if $$u(z)=\int_{\Omega}u(w)\chi_0(w)L_m(z,w)\,\mathrm{e}^{-2mQ(w)}\mathrm{d}A(w) 
+\mathrm{O}(\| u \|_{m} \mathrm{e}^{mQ(z)-m\delta}),
\qquad z\in \mathbb{D}(z_0,\tfrac13 r),$$ holds for large $m$ and all $u\in\mathrm{A}^2_m$. Here and in the sequel, it is implicit that $\delta$ should be positive. Analogously, a function $L_m(z,w)$ defined on ${\mathbb D}(z_0,r)$ and holomorphic in $z$ is a *a local reproducing kernel* $\text{mod}(m^{-k})$ if $$u(z)=\int_{\Omega}u(w)\chi_0(w)L_m(z,w)\,\mathrm{e}^{-2mQ(w)}\mathrm{d}A(w) 
+\mathrm{O}(\| u \|_{m} m^{-k}\mathrm{e}^{mQ(z)}),
\qquad z\in \mathbb{D}(z_0,\tfrac13 r),$$ holds for large $m$ and all $u\in\mathrm{A}^2_m$. We speak of *approximate local reproducing kernels* when it is implicit which of the above senses applies. The Bergman kernel $K_m(z,w)$ is of course an approximate local reproducing kernel in the above sense (no error term!), and it has the additional property of being holomorphic in $\bar w$. This suggests the term *approximate local Bergman kernel* for an approximate local reproducing kernel, which is holomorphic in $\bar w$. Starting with the local reproducing kernel $M_m$, Berman, Berndtsson, and Sjöstrand supply an algorithm to correct $M_m$ and obtain as a result an approximate local Bergman kernel $\text{mod} (m^{-k})$ for any given positive integer $k$. It is a nontrivial step -- which actually requires additional assumptions on the potential $Q$ -- to show that the approximate local Bergman kernels obtained algorithmically in this fashion are indeed close to the Bergman kernel $K_m$ near the diagonal. This is achieved by an argument based on Hörmander's $L^2$-estimates for the $\bar\partial$-operator. In this section, we only present the corrective algorithm.
