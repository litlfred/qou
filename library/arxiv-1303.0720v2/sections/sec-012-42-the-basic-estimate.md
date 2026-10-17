---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-012-42-the-basic-estimate
section_title: "The basic estimate"
section_number: 4.2
pages: 7-8
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.935
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
We begin with a lemma. We decompose the given bianalytic function as $u(z)= u_1(z)+c\bar z+|z|^2u_2(z)$, where $c$ is a constant and $u_j$ is holomorphic for $j=1,2$. Let $\mathrm{d}s(z)
:=|\mathrm{d}z|$ denote arc length measure.

::: lem
[]{#lem1 label="lem1"} If $u(z)= u_1(z)+c\bar z+|z|^2u_2(z)$ is bianalytic and $\psi$ is subharmonic in ${\mathbb D}$, then $$\int_0^1  \bigg| u_1(0) + r^2 u_2(0) + \frac{cr}{\pi} 
\int_{{\mathbb T}}\bar\zeta\psi(r \zeta)\mathrm{d}s(\zeta)  \bigg|^2 r \mathrm{d}r 
\leq \frac{\mathrm{e}^{-2\psi(0)}}{2\pi} \int_{{\mathbb D}} |u|^2 \mathrm{e}^{2\psi} \mathrm{d}A.$$
:::

::: proof
*Proof.* We write $\psi_r(\zeta):= \psi(r\zeta)$ for the dilation of $\psi$, and let $g_r$ be the holomorphic and zero-free function given by $$\log g_r(z) := \frac{1}{2\pi} \int_{{\mathbb T}} 
\frac{1+z\bar\zeta}{1-z\bar\zeta}\psi_r(\zeta)\mathrm{d}s(\zeta).$$ This of course defines $g_r$ uniquely, and also picks a suitable branch of $\log g_r$. Taking real parts, we see that $$\log|g_r| =\mathop{\mathrm{Re}}\log g_r ={\mathbf P}[\psi_r](z):=\frac{1}{2\pi} \int_{{\mathbb T}} 
\frac{1-|z|^2}{|1-z\bar\zeta|^2}\psi_r(\zeta)\mathrm{d}s(\zeta), 
\qquad z\in{\mathbb D},$$ where ${\mathbf P}[\psi_r]$ denotes the Poisson extension of $\psi_r$. Then, in the standard sense of boundary values, $|g_r|^2 = \mathrm{e}^{2\psi_r}$ on ${\mathbb T}$. By the mean value property, we have that $$\begin{gathered}
\frac{1}{2\pi}\int_{{\mathbb T}}u(r\zeta)g_r(\zeta) \mathrm{d}s(\zeta) 
= \frac{1}{2\pi}\int_{{\mathbb T}}\{u_1(r \zeta)+cr\bar\zeta+r^2u_2(r\zeta)\}\,
g_r(\zeta) \mathrm{d}s(\zeta) 
\\
=u_1(0) g_r(0) +cr g'_r(0)+  r^2 u_2(0) g_r(0)  
= g_r(0) \bigg\{u_1(0)+r^2u_2(0)+cr\frac{g_r'(0)}{g_r(0)}\bigg\}.
\label{eq-4.1.1}
\end{gathered}$$ Here, $$\frac{g_r'(z)}{g_r(z)}=\frac{\mathrm{d}}{\mathrm{d}z}\log g_r(z) = \frac{1}{\pi} 
\int_{{\mathbb T}}\frac{\bar\zeta}{(1-z\bar\zeta)^2} 
\psi_r(\zeta)\,\mathrm{d}s(\zeta),$$ so that in particular $$\label{Grformula}
\frac{g_r'(0)}{g_r(0)} =\frac{1}{\pi}\int_{{\mathbb T}}\bar\zeta\psi_r(\zeta) 
\mathrm{d}s(\zeta).$$ By [\[eq-4.1.1\]](#eq-4.1.1){reference-type="eqref" reference="eq-4.1.1"} combined with the Cauchy-Schwarz inequality, $$|g_r(0)|^2\bigg|u_1(0)+r^2u_2(0)+cr\frac{g_r'(0)}{g_r(0)}\bigg|^2 
\leq\frac{1}{2\pi}\int_{{\mathbb T}}|u(r\zeta)g_r(\zeta)|^2 \mathrm{d}s(\zeta) 
=\frac{1}{2\pi}\int_{{\mathbb T}} |u(r\zeta)|^2 \mathrm{e}^{2\psi_r(\zeta)}\mathrm{d}s(\zeta).$$ Next, we multiply both sides by $2r$ and integrate with respect to $r$: $$\int_0^1|g_r(0)|^2 \bigg|u_1(0)+r^2u_2(0)+cr\frac{g_r'(0)}{g_r(0)} 
\bigg|^22r\mathrm{d}r\leq 
\frac{1}{\pi} \int_{{\mathbb D}}|u(z)|^2\mathrm{e}^{2\psi(z)}\mathrm{d}A(z). 
\label{eq-4.1.4}$$ The sub-mean value property applied to $\psi$ gives that $\mathrm{e}^{2\psi(0)}\leq|g_r(0)|^2$, so we obtain from [\[eq-4.1.4\]](#eq-4.1.4){reference-type="eqref" reference="eq-4.1.4"} that $$\label{lemma1mainformula}
\mathrm{e}^{2\psi(0)}\int_0^1\bigg|u_1(0)+r^2u_2(0)+cr 
\frac{g_r'(0)}{g_r(0)}\bigg|^2 r\mathrm{d}r
\leq \frac{1}{2\pi}\int_{{\mathbb D}}|u(z)|^2\mathrm{e}^{2\psi(z)}\mathrm{d}A(z),$$ as claimed. ◻
:::
