---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-004-23-groups-and-representations
section_title: "Groups and representations"
section_number: 2.3
pages: 11-13
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 1.0
doc_brief: "Quantum Field Theory and the Volume Conjecture — 15 sections: Front matter; Preliminaries; The many dimensions of the volume"
---
So far, we have considered two continuous deformations of the volume conjecture, in $u$ and $\hbar$, as drawn schematically in Figure [1](#fig:uh){reference-type="ref" reference="fig:uh"}. In addition, there are two discrete generalizations that we can make.

![Continuous and discrete generalizations of the volume conjecture.](VCgens){#fig:uh width="3.5in"}

The first such generalization involves the "gauge groups" and representations that define colored Jones polynomials. Recall from Section [\[sec:basics\]](#sec:basics){reference-type="ref" reference="sec:basics"} that the $N$-colored Jones polynomial is a quantum $SU(2)$ invariant that corresponds to coloring a knot with the $N$-dimensional representation of $SU(2)$. More generally, one can consider "quantum $SU(n)$ invariants," or in fact invariants for any compact Lie group $G$. Knots or links should then be colored by finite-dimensional representations $R$ of $G$. For semisimple $G$ and irreducible $R$, the representation can be labelled by a highest weight $\lambda$ in the weight lattice $\Lambda_{wt}\subset {\frak{g}}^*$, where ${\frak{g}}= {\rm Lie}(G)$. The resulting quantum polynomial invariant of a knot in $S^3$ may be denoted

$$P^G_{R_\lambda}(K;q)\,.$$

Just like the colored Jones polynomial, $P^G_{R}(K;q)$ depends on a root of unity $q=e^{\frac{2\pi i}{k}}$. Also like the colored Jones, these invariants satisfy

$$P^G_{\oplus_i R_i}(K;q) = \sum_i P^G_{R_i}(K;q)\,,\qquad\text{and}\qquad P^G_{R^{\otimes n}}(K;q) = P^G_R(K^n;q)\,.\qquad$$

More general tensor products can also be produced by cabling a knot or link and coloring each component of the cable with a different representation. When $G=SU(n)$ and $R$ is the fundamental representation (or any of its conjugates), the polynomial $P^G_{R}(K;q)$ satisfies a skein relation similar to [\[skein\]](#skein){reference-type="eqref" reference="skein"}.

Using the positive nondegenerate trace form $-{\rm Tr}\,:\,{\frak{g}}\times{\frak{g}}\to{\mathbb{R}}$, the weight $\lambda$ can be identified with its dual element $\lambda^*$ in ${\frak{t}}$, the Cartan subalgebra of ${\frak{g}}$. Let us also define $\rho$ to be half the sum of positive roots, and $\rho^*\in{\frak{t}}\subset{\frak{g}}$ its dual. Then the interesting limit to consider for $P^G_{R_\lambda}(K,q)$ is

$$k\to \infty\,,\qquad \lambda^*\to\infty\,,\qquad u:=\frac{i\pi}{k}(\lambda^*+\rho^*)\;\;\text{fixed}\,,$$

or

$$q = e^{2\hbar}=e^{\frac{2\pi i}{k}}\to 1\,\quad (\hbar\to 0)\,,\qquad q^{\lambda^*+\rho^*}=e^{2u}\;\;\text{fixed}\,.$$

The parameter $u$ has now become a diagonal matrix, an element of ${\frak{t}}_{\mathbb{C}}$. Coming back to the case of $SU(2)$ and an $N$-dimensional representation, in this notation we have

$$\lambda^*=\begin{pmatrix} N-1 & 0 \\ 0 & -(N-1) \end{pmatrix}\,,
 \qquad \rho^* = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\,,
 \qquad u 
  = i\pi\begin{pmatrix} \frac{N}{k} & 0 \\ 0 & -\frac{N}{k}\end{pmatrix}\,.$$

The asymptotics of the invariant $P^G_{R}(K;q)$ should look very similar to those of the colored Jones polynomial, namely

$$\boxed{ P^G_{R_\lambda}(K;q) \;\overset{\hbar\to 0}{\sim}\; \exp\left( -\frac{1}{4\hbar}I_{CS}(u)-\frac{\delta}{2}\log\hbar+\frac12\log \frac{iT(u)}{4\pi}+\sum_{n=2}^\infty S_n(u)\hbar^{n-1} \right) } \,. \label{VCRG}$$

The leading term $I_{CS}(u)$ is now the Chern-Simons functional [\[ICS\]](#ICS){reference-type="eqref" reference="ICS"} evaluated at a flat $G_{\mathbb{C}}$ connection ${\cal A}(u)$ --- in other words, a connection taking values in the complexified Lie algebra ${\frak{g}}_{\mathbb{C}}$ --- whose holonomy around the meridian of the knot as in Figure [\[fig:lm\]](#fig:lm){reference-type="ref" reference="fig:lm"}a is

$${\rm Hol}(\mu) = m=e^u\,.$$

For generic $u$, this holonomy is an element of the complexified maximal torus $T_{\mathbb{C}}\subset G_{\mathbb{C}}$. Again, $I_{CS}(u)$ can be expressed as

$$I_{CS}(u) = \text{const.} + 4\int_{\gamma(u)} \theta\,,$$

where  $\theta \sim -\sum_{i=1}^r v_i\,du_i$ + exact   is a differential on an $r$-dimensional complex variety cut out by $r$ equations $A_j(e^{v},e^{u})=0$, with $r={\rm rank}(G)$. The equations $A_j(e^{v},e^{u})=0$ describe the moduli space of flat $G_{\mathbb{C}}$ connections on $S^3\backslash K$.

Subleading terms on the right side of [\[VCRG\]](#VCRG){reference-type="eqref" reference="VCRG"} also have a geometric interpretation. The function $T(u)$ is the Ray--Singer torsion of the knot complement twisted by the flat connection ${\cal A}(u)$, and the number $\delta$ is a fixed integer which can be computed in terms of cohomology of $S^3\backslash K$ with coefficients in the associated flat bundle, with structure group $G_{\mathbb{C}}$ and connection ${\cal A}(u)$ (*cf.* [@barnatan-1991w; @DGLZ]). More generally, the full asymptotic expansion can be written as a perturbative path integral just like [\[path2\]](#path2){reference-type="eqref" reference="path2"}, which takes into account the quantum fluctuations of a flat $G_{\mathbb{C}}$ connection.
