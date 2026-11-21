---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-033-51-critical-points
section_title: "Critical points"
section_number: 5.1
pages: 30-32
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 0.582
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.saddle label="sec.saddle"}

We begin by showing that the critical points of [\[SIM\]](#SIM){reference-type="eqref" reference="SIM"} are indeed solutions to the gluing equations. For this purpose, we need to know the quantum dilogarithm $\psi_{\hbar}(Z)$. The latter is given by [@DGLZ Eqn.3.22]

$$\label{qdl} \psi_{\hbar}(Z) = \prod_{r=1}^\infty \frac{1-q^r e^{-Z}} {1-({}^Lq)^{-r+1}e^{-{}^LZ}}\,,$$

for $|q|<1$, where

$$q := \exp \hbar,\,\quad {}^L q := \exp \frac{-4\pi^2}{\hbar}\,,
\qquad {}^LZ := \frac{2\pi i}{\hbar}Z\,.$$

The quantum dilogarithm $\psi_{\hbar}(Z)$ coincides with the restriction to $|q|<1$ of Faddeev's quantum dilogarithm [@Fa], as follows from [@DGLZ Eqn.3.23]. $\psi_{\hbar}(Z)$ is the Chern-Simons wavefunction of a single tetrahedron [@D1]. The quantum dilogarithm has an asymptotic expansion as $\hbar\to 0$, given by (*cf.* [@DGLZ Eqn.3.26])

$$\begin{aligned}
 \label{qdlasymp}
\psi_{\hbar}(Z) &\overset{\hbar\to 0}{\sim} 
\exp \sum_{n=0}^\infty \frac{B_n\,\hbar^{n-1}}{n!} \widetilde{\rm Li}_{2-n}(e^{-Z}) \\
&= \exp\left[\frac{1}{\hbar}\widetilde{\rm Li}_2(e^{-Z})+\frac12\widetilde{\rm Li}_1(e^{-Z})
-\frac\hbar{12}z'+\frac{\hbar^3}{720}z(1+z)z'^3+\ldots\right]\,,  \notag
\end{aligned}$$

where $B_n$ is the $n^{\rm th}$ Bernoulli number, with $B_1=1/2$.

The coefficients of strictly positive powers of $\hbar$ (*i.e.* $n\geq 2$) in the expansion are rational functions of $z=e^{Z}$, but the two leading asymptotics --- the logarithm and dilogarithm --- are multivalued and have branch cuts. In contrast, the function $\psi_{\hbar}(Z)$ itself is a meromorphic function on $\mathbb{C}$ for any fixed $\hbar\neq 0$. Branch cuts in its asymptotics arise when families of poles collide in the $\hbar\to 0$ limit. In the case of purely imaginary $\hbar$ with $\mathrm{Im}\,\hbar>0$ (a natural choice in the analytic continuation of $\mathrm{SU}(2)$ Chern-Simons theory), a careful analysis of this pole-collision process leads to branch cuts for $\widetilde{\rm Li}_2$ and $\widetilde{\rm Li}_1$ that are different from the standard ones (Figure [1](#fig.cuts){reference-type="ref" reference="fig.cuts"}). We indicate the modified analytic structure of these two functions (really functions of $Z$ rather than $e^{-Z}$) with an extra tilde.

![Rotating the standard branch cuts of ${\rm Li}_2(e^{-Z})$ and ${\rm Li}_1(e^{-Z})$ to produce $\widetilde{\rm Li}_2(e^{-Z})$ and $\widetilde{\rm Li}_1(e^{-Z})$, as functions of $Z$. The shaded region indicates where the standard logarithms of shape parameters for the discrete faithful representation lie.](cuts){#fig.cuts width="5.5in"}

Now, the critical points of the integrand, at leading order

[^1]

in the $\hbar$ expansion, are solutions to

$$\begin{aligned}
 \notag
0 &= \frac{\partial}{\partial Z_i}\Big(-\frac{\pi^2}{2}f\cdot 
\mathbf B^{-1}\nu-i\pi Z\cdot\mathbf B^{-1}\nu+\frac1{2}Z\cdot\mathbf{B}^{-1}\mathbf A Z
+\sum_i\widetilde{{\rm Li}}_2(e^{-Z_i})\Big)  \\
&= -i\pi \big(\mathbf B^{-1}\nu)_i+\big(\mathbf B^{-1} \mathbf A Z)_i
-\widetilde{\rm Li}_1(e^{-Z_i})\,, \notag
\end{aligned}$$

in other words,

$$\mathbf A Z+\mathbf B (-\widetilde{\rm Li}_1(e^{-Z}))=i\pi \nu\,. \label{crit}$$

Since $\exp[-\widetilde{\rm Li}_1(e^{-Z_i})]=1-z_i^{-1}$, we see that every solution to [\[crit\]](#crit){reference-type="eqref" reference="crit"} is a particular logarithmic lift of a solution to the actual gluing equations $z^{\mathbf A}(1-z^{-1})^{\mathbf B}=(-1)^\nu$. It is a lift that precisely satisfies the logarithmic constraints [\[NZlin\]](#NZlin){reference-type="eqref" reference="NZlin"} of Section [\[sec.triang\]](#sec.triang){reference-type="ref" reference="sec.triang"}, with $Z_i''=-\widetilde{\rm Li}_1(e^{-Z_i})$.

When $0\leq {\rm Im}\,Z_i\leq \pi$, the branches of the standard logarithms and dilogarithms agree with those of the modified ones. In particular, given the discrete faithful solution to $z^{\mathbf A}(1-z^{-1})^{\mathbf B}=(-1)^n$, taking standard logarithms immediately produces a solution to [\[crit\]](#crit){reference-type="eqref" reference="crit"}. Therefore, the discrete faithful representation always corresponds to a critical point of the state integral.

[^1]: We treat all sub-leading terms as perturbations. The exact location of the critical point will acquire perturbative corrections, described in Section [\[sec.diags\]](#sec.diags){reference-type="ref" reference="sec.diags"}.
