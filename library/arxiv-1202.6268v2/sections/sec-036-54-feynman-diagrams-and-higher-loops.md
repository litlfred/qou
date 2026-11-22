---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-036-54-feynman-diagrams-and-higher-loops
section_title: "Feynman diagrams and higher loops"
section_number: 5.4
pages: 33-35
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.964
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.diags label="sec.diags"}

The remainder of the invariants $S_{\mathcal{T},n}$ can be obtained by continuing the saddle-point (stationary phase) expansion of the state integral to higher order. The calculation can be systematically organized into a set of Feynman rules (*cf.* [@MirrorSym Ch.9], [@BIZ; @Polyak]). The resulting formulas --- summarized in the Introduction --- are explicit algebraic functions of the exponentiated shape parameters $z_i$, and belong to the invariant trace field $E_M$.

To proceed, we should first re-center the integration around a critical point. Thus, we replace $Z\to Z+\zeta$ and integrate over $\zeta$, assuming $Z$ to be a solution to [\[crit\]](#crit){reference-type="eqref" reference="crit"}. Using [@DGLZ Eqn.3.26], we expand as follows:

$$\begin{aligned}
 \notag
Z_{\mathcal{T}}(\hbar) 
&=  \sqrt{\frac{8\pi^3}{\hbar^3\det\mathbf B}}\int 
\frac{d^N\! \zeta}{(2\pi\hbar)^{N/2}} \prod_{i=1}^N \psi_{\hbar}(Z_i+\zeta_i) 
\\ &\hspace{.5in}\times 
e^{\tfrac1\hbar\big[ \tfrac1{2}\big(i\pi+\tfrac\hbar 2\big)^2f\cdot 
\mathbf B^{-1}\nu-\big(i\pi+\tfrac\hbar2\big)(Z+\zeta)\cdot\mathbf B^{-1}\nu
+\tfrac1{2}(Z+\zeta)\cdot\mathbf{B}^{-1}\mathbf A (Z+\zeta)\big]}
 \notag\\
&\sim \sqrt{\frac{8\pi^3}{\hbar^3\det\mathbf B}}\,e^{\Gamma^{(0)}(Z)}\int 
\frac{d^N\! \zeta}{(2\pi\hbar)^{N/2}}\exp\Big[-\frac{1}{2\hbar}
\zeta\cdot\mathcal{H}(Z)\cdot \zeta+\sum_{k=1}^\infty\sum_{i=1}^N 
\frac{\Gamma^{(k)}_i(Z)}{k!}\,\zeta_i^k\Big].
\label{Feyngen}
\end{aligned}$$

In this form, the first coefficient $\Gamma^{(0)}(Z)$ can be identified with an overall *vacuum energy*, while the rest of the $\Gamma_i^{(k)}(Z)$ are *vertex factors*.

Every $\Gamma^{(k)}(Z)$ here is a series in $\hbar$, in general starting with a $1/\hbar$ term. However, $\Gamma_i^{(1)}$ must vanish at leading order $\hbar^{-1}$ precisely because $Z$ is a solution to the leading-order critical point equations; and we have also already extracted the leading $\hbar^{-1}$ piece of $\Gamma_i^{(2)}$ as the Gaussian integration measure $-\tfrac{1}{2\hbar}\zeta\mathcal{H}\zeta$. Typically, 1-vertices and 2-vertices are absent from a Feynman calculus. Here, however, they appear because our critical point equation and the Hessian (respectively) are only accurate at leading order, and incur $\hbar$-corrections. (Note that the 1-vertices and 2-vertices are counted separately in [\[effloop\]](#effloop){reference-type="eqref" reference="effloop"} below.)

The vacuum energy $\Gamma^{(0)}$ contributes to every $S_{\mathcal{T},n}$, $n\geq 0$. Its leading-order $\hbar^{-1}$ term is just the complex volume [\[vol\]](#vol){reference-type="eqref" reference="vol"}, while the $\hbar^0$ piece contains the corrections [\[torcorr1\]](#torcorr1){reference-type="eqref" reference="torcorr1"}--[\[torcorr2\]](#torcorr2){reference-type="eqref" reference="torcorr2"} to the torsion. At higher order in $\hbar$, we have

$$\Gamma^{(0)}(Z) = \frac{1}{\hbar}S_0+\hbar^0(...)
+\frac{\hbar}{8}f\cdot\mathbf B^{-1}\mathbf A f + \sum_{n=2}^\infty 
\frac{\hbar^{n-1} B_{n}}{n!}\sum_{i=1}^N {\rm Li}_{2-n}(z_i^{-1})\quad\; 
\Big({\rm mod}\;\frac{\hbar}{24}\Big)\,.$$

Each $S_n$, $n\geq 2$, is calculated by taking the $\hbar^{n-1}$ part of $\Gamma^{(0)}$, and adding to it an appropriate sum of Feynman diagrams. The rules for the diagrams are derived from [\[Feyngen\]](#Feyngen){reference-type="eqref" reference="Feyngen"} as follows. There are vertices of all valencies $k=1,2,...$, with a vertex factor given by $\Gamma^{(k)}_i$. One draws all connected diagrams (graphs) with

$$\label{effloop}
\boxed{\text{\# loops + \# 1-vertices + \# 2-vertices $\leq n$}\,.}$$

Each $k$-vertex is assigned a factor $\Gamma_i^{(k)}$, and each edge is assigned a propagator

$$\label{prop}
\text{propagator}:\qquad \Pi_{ij}:= \hbar\,\mathcal{H}^{-1}_{ij} \,
=\, \hbar(-\mathbf B^{-1}\mathbf A+\Delta_{z'})^{-1}_{ij}\,.$$

The diagrams are then evaluated by contracting the vertex factors with propagators, and multiplying by a standard *symmetry factor*. In each diagram, one should restrict to the $\hbar^{n-1}$ term in its evaluation.

Explicitly, using the asymptotic expansion [\[qdlasymp\]](#qdlasymp){reference-type="eqref" reference="qdlasymp"} of the quantum dilogarithm, we find that the vertices are

$$\label{vx}
\begin{align}
\text{1-vertex:}\quad \Gamma^{(1)}_i &= -\frac12(\mathbf B^{-1}\nu)_i
-\sum_{n=1}^\infty \frac{\hbar^{n-1}B_n}{n!}{\rm Li}_{1-n}(z_i^{-1}) 
= -\frac12(\mathbf B^{-1}\nu)_i  +\frac{z'_i}{2}+\ldots\,,\\
\text{2-vertex:}\quad \Gamma^{(2)}_i &= \sum_{n=1}^\infty 
\frac{\hbar^{n-1}B_n}{n!}{\rm Li}_{-n}(z_i^{-1}) = \frac{z_iz_i'^2}{2}
-\frac\hbar{12}z_i(1+z_i)z_i'^3+\ldots\\
\text{$k$-vertex:}\quad\Gamma^{(k)}_i &= (-1)^k \sum_{n=0}^\infty 
\frac{\hbar^{n-1}B_n}{n!}{\rm Li}_{2-n-k}(z_i^{-1}) \qquad\qquad (k\geq 3)
\end{align}$$

Note that in $\Gamma_i^{(1)}$ we could also write $\mathbf B^{-1}\nu=\mathbf B^{-1}\mathbf Af+f''$. When the inequality [\[effloop\]](#effloop){reference-type="eqref" reference="effloop"} is saturated, only the leading-order ($\hbar^{-1}$ or $\hbar^0$) terms of the vertex factors [\[vx\]](#vx){reference-type="eqref" reference="vx"} need be considered. Otherwise, subleading $\hbar$-corrections may be necessary.

Examples of 2-loop and 3-loop Feynman diagrams were given in Figures [\[fig.diags2intro\]](#fig.diags2intro){reference-type="ref" reference="fig.diags2intro"}--[\[fig.diags3dot\]](#fig.diags3dot){reference-type="ref" reference="fig.diags3dot"} of the Introduction, along with the entire evaluated expression for $S_{\mathcal{T},2}$.
