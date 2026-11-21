---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-032-5-the-state-integral-and-higher-loops
section_title: "The state integral and higher loops"
section_number: 5
pages: 29-30
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.714
latex_coverage_ratio: 0.973
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.SIM label="sec.SIM"}

Our explicit formulas for the torsion $\tau_\mathcal{T}$, as well as higher invariants $S_{\mathcal{T},n}$, have been obtained from a state integral model for analytically continued $\mathrm{SL}(2,\mathbb{C})$ Chern-Simons theory. In this section, we will review the state integral, and analyze its asymptotics in order to re-derive the full asymptotic expansion

$$\label{asympSIM}
\mathcal{Z}_\mathcal{T}(\hbar) = \hbar^{-\frac32}\exp\Big[\frac1\hbar S_{\mathcal{T},0}+S_{\mathcal{T},1}+\hbar S_{\mathcal{T},2}+\hbar^2 S_{\mathcal{T},3}+\ldots\Big]\,,$$

and to unify the formulas of previous sections. We should point out that this section is *not* analytically rigorous, but serves as a motivation for our definition of the all-loop invariants, and provides a glimpse into the calculus of (complex, finite dimensional) state-integrals.

The basic idea of a state integral is to cut a manifold $M$ into canonical pieces (ideal tetrahedra); to assign a simple partition function to each piece (a quantum dilogarithm); and then to multiply these simple partition functions together and integrate out over boundary conditions in order to obtain the partition function of the glued manifold $M$. A state integral provides a *finite-dimensional reduction* of the full Feynman path integral on $M$.

Currently, there are two flavors of $\mathrm{SL}(2,\mathbb{C})$ state integrals in the literature. The first, introduced in [@Hi; @Hi2], studied in [@DGLZ], and made mathematically rigorous in [@AK], is based on a 3-dimensional lift of the 2-dimensional quantum Teichmüller theory in Kashaev's formalism [@Kashaev-Teich]. It uses variables associated to faces of tetrahedra.

The second, developed in [@D1], explicitly uses shape parameters --- associated to edges of tetrahedra --- and constitutes a 3d lift of Teichmüller theory in the Fock-Chekhov formalism [@FC-Teich]. The two types of state integrals should be equivalent, though this has only been demonstrated in isolated examples so far [@SpirVar].

It is the second state integral that we employ in this paper, due to its explicit dependence on shape parameters. Indeed, suppose that $M$ is an oriented one-cusped hyperbolic manifold with a $\rho_0$--regular triangulation $\mathcal{T}$ and enhanced Neumann-Zagier datum $\widehat \beta_\mathcal{T}=(z,\mathbf A,\mathbf B,f)$, with $\mathbf Af+\mathbf Bf''=\nu$. We must also assume that $\mathbf B$ is non-degenerate, which (Lemma [\[lemma.B\]](#lemma.B){reference-type="ref" reference="lemma.B"}) is always possible. Then we will

[^1]

show in Appendix [\[app.SIM\]](#app.SIM){reference-type="ref" reference="app.SIM"} that the state integral of [@D1] takes the form

$$\begin{aligned}
\label{SIM}
\mathcal{Z}_{\mathcal{T}}(\hbar) &= \sqrt{\frac{8\pi^3}{\hbar^3\det\mathbf B}}\int 
\frac{d^N\!Z}{(2\pi\hbar)^{N/2}}\,
e^{\tfrac1\hbar\big[ 
\tfrac1{2}\big(i\pi+\tfrac\hbar 2\big)^2f\cdot \mathbf B^{-1}\nu
-\big(i\pi+\tfrac\hbar2\big)Z\cdot\mathbf B^{-1}\nu
+\tfrac1{2}Z\cdot\mathbf{B}^{-1}\mathbf A Z\big]}
\prod_{i=1}^N \psi_{\hbar}(Z_i)\,,  
\end{aligned}$$

where $\psi_\hbar(Z)$ is a non-compact quantum dilogarithm [@Ba; @Fa], the Chern-Simons partition function of a single tetrahedron. The integration variables $Z_i$ are, literally, the logarithmic shape parameters of $\mathcal{T}$.

The integration contour of [\[SIM\]](#SIM){reference-type="eqref" reference="SIM"} is unspecified. A complete, non-perturbative definition of $\mathcal{Z}_\mathcal{T}(\hbar)$ requires a choice of contour, and the choice leading to invariance under 2--3 moves (etc.) may be quite subtle. However, a formal asymptotic expansion of the state integral as in [\[asympSIM\]](#asympSIM){reference-type="eqref" reference="asympSIM"} *does not require* a choice of contour. It simply requires a choice of critical point for the integrand. Then the asymptotic series may be developed via *formal Gaussian integration* in an infinitesimal neighborhood of the critical point.

We will show in Section [\[sec.saddle\]](#sec.saddle){reference-type="ref" reference="sec.saddle"} that all the leading-order critical points of [\[SIM\]](#SIM){reference-type="eqref" reference="SIM"} are logarithmic solutions to the gluing equations

$$\label{glueSIM} \text{critical points}\qquad \longleftrightarrow \qquad  z{}^{\mathbf A}(1-z^{-1}){}^{\mathbf B} = (-1)^\nu\,,$$

with $z=\exp(Z)$. In particular, the critical points are isolated. Then, choosing the discrete faithful solution to [\[glueSIM\]](#glueSIM){reference-type="eqref" reference="glueSIM"}, we formally expand the state integral to find that

-   $S_{\mathcal{T},0}$, the evaluation of leading-order part of the integrand at the critical point, is the complex volume of $M$;

-   $\exp(-2S_{\mathcal{T},1})$ is expressed as the determinant of a Hessian matrix

    $$\notag
    \mathcal{H}= -\mathbf B^{-1}\mathbf A+\Delta_{1-z}^{-1}\,,$$

    with a suitable monomial correction, and reproduces the torsion [\[torintro\]](#torintro){reference-type="eqref" reference="torintro"}; and

-   the higher $S_{\mathcal{T},n}$ are obtained via a finite-dimensional Feynman calculus, and explicitly appear as rational functions of shape parameters.

It follows from the formalism of [@D1], reviewed in Appendix [\[app.SIM\]](#app.SIM){reference-type="ref" reference="app.SIM"}, that the state integral [\[SIM\]](#SIM){reference-type="eqref" reference="SIM"} is only well defined up to multiplicative prefactors of the form

$$\label{abc}
\exp\Big( \frac{\pi^2}{6\hbar}a+\frac{i\pi}{4}b+\frac{\hbar}{24}c\Big)\,,
\qquad a,\,b,\,c\,\in\mathbb{Z}\,.$$

This means that we only obtain $\big(S_{\mathcal{T},0},\tau_\mathcal{T}=4\pi^3e^{-2S_{\mathcal{T},1}},S_{\mathcal{T},2}\big)$ modulo $\big(\tfrac{\pi^2}{6}\mathbb{Z},\,i,\,\tfrac{1}{24}\mathbb{Z}\big)$, respectively; however, all the higher invariants $S_{\mathcal{T},n\geq 3}$ should be unambiguous. Moreover, in Section [\[sec.torsion\]](#sec.torsion){reference-type="ref" reference="sec.torsion"} we saw that the ambiguity in $\tau_\mathcal{T}$ could be lifted

[^2]

to a sign $\pm 1$. Although the construction of the asymptotic series [\[asympSIM\]](#asympSIM){reference-type="eqref" reference="asympSIM"} appears to depend on $\mathcal{T}$, we certainly expect that

::: conjecture
[]{#conj.Sn label="conj.Sn"} The invariants $\big\{S_{\mathcal{T},n}\big\}_{n=0}^\infty$ are independent of the choice of regular triangulation and Neumann-Zagier datum (including the choice of quad type with $\det \mathbf B\neq 0$, etc.), up to the ambiguity [\[abc\]](#abc){reference-type="eqref" reference="abc"}, and thus constitute topological invariants of $M$.
:::

We now proceed to analyze the critical points and asymptotics of [\[SIM\]](#SIM){reference-type="eqref" reference="SIM"} in greater detail. In Section [\[sec.uSIM\]](#sec.uSIM){reference-type="ref" reference="sec.uSIM"}, we will also generalize the state integral to arbitrary representations, with non-unit meridian eigenvalue $m=e^u\neq 1$, and give an example of $S_{\mathcal{T},2}(m)$, $S_{\mathcal{T},3}(m)$ as functions on the character variety $Y_M^{\rm geom}$ for the figure-eight knot.

[^1]: Here we multiply [\[appSIM\]](#appSIM){reference-type="eqref" reference="appSIM"} (at $u=0$) by an extra, canonical normalization factor $(2\pi/\hbar)^{3/2}$, in order to precisely match the asymptotics of the Kashaev invariant at the discrete faithful representation.

[^2]: It may also be possible to lift the ambiguities in $S_{\mathcal{T},0}$ and $S_{\mathcal{T},2}$ by using ordered triangulations, as in [@N] or [@Zickert-rep].
