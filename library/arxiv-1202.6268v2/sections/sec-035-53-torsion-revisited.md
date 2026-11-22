---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-035-53-torsion-revisited
section_title: "Torsion revisited"
section_number: 5.3
pages: 33-33
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.984
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.torsion2 label="sec.torsion2"}

Next, we can derive our torsion formula [\[torintro\]](#torintro){reference-type="eqref" reference="torintro"}. The torsion comes from the $\hbar^0$ part in the asymptotic expansion of the state integral, which has several contributions.

From formal Gaussian integration around a critical point [\[crit\]](#crit){reference-type="eqref" reference="crit"}, we get a determinant $(2\pi \hbar)^{N/2}\big(\det \mathcal{H}\big)^{-1/2}$, where

$$\begin{aligned}
 \mathcal{H}_{ij} &= -\frac{\partial^2}{\partial Z_i
\partial Z_j}\Big(-\frac{\pi^2}{2}f\cdot \mathbf B^{-1}\nu-i\pi Z\cdot
\mathbf B^{-1}\nu+\frac1{2}Z\cdot\mathbf{B}^{-1}\mathbf A Z+\sum_i\widetilde{{\rm Li}}_2(e^{-Z_i})\Big) 
\notag \\
 &= \boxed{ (-\mathbf B^{-1}\mathbf A+\Delta_{z'})_{ij}} \label{Hess}
\end{aligned}$$

is the Hessian matrix of the exponent (at leading order $\hbar^{-1}$). Here $\Delta_{z'}:=\text{diag}(z_1',...,z_N')$, with $z_i'=(1-z_i)^{-1}$ as usual. Multiplying the determinant is the $\hbar^0$ piece of the integrand, evaluated at the critical point. From the $\hbar^0$ part of the quadratic exponential, we get

$$\begin{aligned}
 \exp\Big(\frac{i\pi}{2}f\cdot \mathbf B^{-1}\nu
-\frac12 Z\cdot \mathbf B^{-1}\nu\Big)
 &= \exp\Big( \frac12 f\cdot (\mathbf B^{-1}\mathbf A Z+Z'')
-\frac12 Z\cdot (\mathbf B^{-1}\mathbf A f+f'')\Big) \notag \\
 &= \exp\Big(-\frac12 Z\cdot f''+\frac12 Z''\cdot f\Big) \notag \\
 & = \big(z^{f''}z''{}^{-f}\big)^{-1/2}\,, \label{torcorr1}
\end{aligned}$$

whereas from the quantum dilogarithm at order $\hbar^0$ we find

$$\exp\Big(\frac12\sum_i\widetilde{\rm Li}_1(e^{-Z_i})\Big) 
= \pm\prod_i \frac{1}{\sqrt{1-z_i^{-1}}}=\pm\det \Delta_{z''}^{-1/2}\,. 
\label{torcorr2}$$

Combining the determinant $(2\pi \hbar)^{N/2}\big(\det \mathcal{H}\big)^{-1/2}$, the corrections [\[torcorr1\]](#torcorr1){reference-type="eqref" reference="torcorr1"}--[\[torcorr2\]](#torcorr2){reference-type="eqref" reference="torcorr2"}, and the overall prefactor $\sqrt{\frac{8\pi^3}{\det \mathbf B}}(2\pi\hbar)^{-N/2}$ in the integral [\[SIM\]](#SIM){reference-type="eqref" reference="SIM"} itself, we finally obtain

$$e^{S_1} = \sqrt{\frac{8\pi^3}{ \det\mathbf B \det(-\mathbf B^{-1}\mathbf A
+\Delta_{z'})\det\Delta_{z''}z^{f''}z''{}^{-f}}} = 
\sqrt{\frac{-8\pi^3}{\det(\mathbf A\Delta_{z''}
+\mathbf B\Delta_z^{-1})z^{f''}z''{}^{-f}}}\,,$$

up to multiplication by a power of $i$; or

$$\tau_M := 4\pi^3e^{-2S_1} = \pm\frac12\det(\mathbf A\Delta_{z''}
+\mathbf B\Delta_z^{-1})z^{f''}z''{}^{-f}\,,$$

just as in [\[torintro\]](#torintro){reference-type="eqref" reference="torintro"}. Despite the fact that the original state integral only made sense for non-degenerate $\mathbf B$, the final formula for the torsion is well defined for any $\mathbf B$.
