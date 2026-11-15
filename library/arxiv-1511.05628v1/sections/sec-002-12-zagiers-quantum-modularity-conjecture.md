---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-002-12-zagiers-quantum-modularity-conjecture
section_title: "Zagier's Quantum Modularity Conjecture"
section_number: 1.2
pages: 3-4
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.98
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
[]{#sub.QMC label="sub.QMC"}

The Kashaev invariant of a knot $K$ is a sequence of complex numbers $\langle K \rangle_N$ indexed by a positive integer $N$ [@Kashaev95]. Murakami-Murakami [@MM] identified the Kashaev invariant with an evaluation of the colored Jones polynomial $J_{K,N}(q) \in \mathbb Z[q^{\pm 1}]$ colored by the $N$-dimensional irreducible representation of $\mathfrak{sl}_2$: $$\langle K \rangle_N = J_{K,N}(e^{\frac{2 \pi i}{N}}) \,.$$ Identifying the set of complex roots of unity with $\mathbb Q/\mathbb Z$, the Kashaev invariant can be extended to a translation-invariant function on $\mathbb Q$ by $$J^0_K: \mathbb Q\longrightarrow\mathbb C, \qquad 
\alpha\mapsto J^0_K(\alpha)=J_{K,\mathrm{den}(\alpha)}(e^{2 \pi i \alpha})$$ where $\mathrm{den}(a/c)=c$ when $c>0$ and $a,c$ are coprime. Obviously, we have $J^0_K(\alpha)=J^0_K(\alpha+1)$ for $\alpha\in \mathbb Q$.

The Quantum Modularity Conjecture [@Za:QMF] predicts for each complex root of unity $\zeta$ the existence of a formal power series $\phi_{K,\zeta}(\hbar) \in \mathbb C[\![\hbar]\!]$ with the following property. Choose any $\begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathrm{SL}(2,\mathbb Z)$ with $c>0$ such that $\zeta = \exp(\frac{2\pi i a}{c})$. Let $X\to\infty$ in a fixed coset of $\mathbb Q/\mathbb Z$, and set $\hbar=2\pi i/(cX+d)$. Then there is an asymptotic expansion $$\label{eq.QMF}
J^0_K\left(\frac{aX+b}{cX+d}\right) \sim J^0_K(X) 
\big(\tfrac{2\pi i}{\hbar}\big)^{3/2} e^{V/(c\hbar)}
\phi_{K,\zeta}(\hbar)$$ where $V$ is the complex volume of $K$. Furthermore, the coefficients of $\phi_{K,\zeta}(\hbar)$ are conjectured to be algebraic integers of the following form:

-   The coefficients of $\phi^+_{K,\zeta}(\hbar)=\phi_{K,\zeta}(\hbar)/\phi_{K,\zeta}(0)$ should be elements of the field $F_K(\zeta)$, where $F_K$ is the trace field of $K$.

-   The constant term (under some mild assumptions on $F_K(\zeta)$) should factor as follows: $$\label{eq.phi0factor}
    \phi_{K,k}(0) = \phi_{K,1}(0) \sqrt[k]{\varepsilon_K} \beta_{K,k}$$ where $\phi_{K,1}(0)^2 \in F_K(\zeta)$, $\varepsilon_K$ is a unit (i.e., an algebraic integer of norm $\pm 1$) in $F_K(\zeta)$ that depends only on the element of the Bloch group of $K$ (and $\zeta$), and $\beta_{K,k} \in F_K(\zeta)$.

The above unit is studied in [@calegari]. For a detailed discussion of the Quantum Modularity Conjecture, we refer the reader to [@Za:QMF] and also [@GZ1] where a proof for the case of the $4_1$ knot (the simplest hyperbolic knot) is given.

The Quantum Modularity Conjecture includes the Volume Conjecture of Kashaev  [@Kashaev95] and its refinement to all orders of $1/N$ conjectured by Gukov [@Gu] and by the second author [@Ga:arithmetic]. Indeed, when $\left(\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}\right)  
= \left(\begin{smallmatrix} 0 & -1 \\ 1 & 0\end{smallmatrix}\right)$ and $X=N\in \mathbb N$, we obtain that $$\label{eq.GVC}
\overline{\langle K \rangle_N} = J^0_K\left(-\frac{1}{N}\right) \sim 
N^{3/2} e^{N V/(2 \pi i)}\phi_{K,1}\left(\frac{2 \pi i}{N}\right)\,.$$

The second author and Zagier numerically computed the Kashaev invariant and its asymptotics, exposing several coefficients of the series $\phi_{K,\zeta}(\hbar)$ for many knots, and giving numerical confirmation of the Modularity Conjecture. The results are summarized in [@GZ1].

A definition of the power series $\phi_{K,\zeta}(\hbar)$ in the Quantum Modularity Conjecture was missing, though. Motivated by this problem, in an earlier publication  [@DG] (inspired by [@DGLZ]) the authors assigned to a Neumann-Zagier datum $\gamma$ (i.e., to an ideal triangulation of the knot complement, a geometric solution to the gluing equations and a flattening) a power series $\phi_{\gamma,1}(\hbar)$ and conjectured that it coincides with the series $\phi_{K,1}(\hbar)$. One advantage of the series $\phi_{\gamma,1}(\hbar)$ is the exact computation of its coefficients using standard `SnapPy` methods [@snappy], together with finite sums of Feynman diagrams. In all cases we matched those coefficients with the numerically computed values of [@GZ1]. In [@DG], it was shown that the constant term of $\phi_{\gamma,1}(\hbar)$ is a topological invariant, but to date the full topological invariance of $\phi_{\gamma,1}(\hbar)$ is unknown.

Finally, we ought to point out a close connection between our series $\phi_{\gamma,\zeta}(\hbar)$ and

-   The radial asymptotics of Nahm sums at complex roots of unity. This connection was observed at $\zeta=1$ during conversations of the second author and Zagier in Bonn in the spring of 2012.

-   The evaluations of one-dimensional state-integrals at rational points [@GK1; @GK2].

-   The formula for an algebraic unit attached to an element of the Bloch group of a number field and a complex root of unity, appearing in [\[eq.phi0factor\]](#eq.phi0factor){reference-type="eqref" reference="eq.phi0factor"} [@calegari].

These connections are not a coincidence; rather, they close a circle of ideas motivated by several years of work on asymptotics of hypergeometric sums, quantum invariants, and their geometry and physics.
