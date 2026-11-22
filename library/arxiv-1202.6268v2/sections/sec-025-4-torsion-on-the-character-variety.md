---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-025-4-torsion-on-the-character-variety
section_title: "Torsion on the character variety"
section_number: 4
pages: 22-23
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.971
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.extensions label="sec.extensions"}

Having given a putative formula for the non-abelian torsion of a cusped hyperbolic manifold $M$ at the discrete faithful representation $\rho_0$, it is natural to ask whether the formula generalizes to other settings. In this section, we extend the torsion formula to general representations $\rho:\pi_1(M)\longrightarrow\text{(P)SL}(2,\mathbb C)$ for manifolds $M$ with torus boundary, essentially by letting the shapes $z$ be functions of $\rho$. We also find that some special results hold when $M$ is hyperbolic and the representations lie on the geometric component $X_M^{\rm geom}$ of the $SL(2,\mathbb{C})$ character variety.

We will begin with a short review of what it means for a combinatorial ideal triangulation to be *regular* with respect to a general representation $\rho$. We will also finally prove Proposition [\[prop.EP\]](#prop.EP){reference-type="ref" reference="prop.EP"} from the Introduction. Recall that Proposition [\[prop.EP\]](#prop.EP){reference-type="ref" reference="prop.EP"} identified a canonical connected subset $\mathcal X^{\mathrm{EP}}_M$ of the set of regular triangulations $\mathcal X_{\rho_0}$ of a hyperbolic 3-manifold $M$. This result allowed us to construct the topological invariant $\tau_M$.

We then proceed to define an enhanced Neumann-Zagier datum $\widehat\beta_\mathcal{T}=(z,\mathbf A,\mathbf B,f)$ suitable for a general representation $\rho$, and propose a generalization of the torsion formula:

$$\label{utor} 
\tau_\mathcal{T}(\rho) := \pm\frac12\det\big(\mathbf A\Delta_{z''}
+\mathbf B\Delta_z^{-1}\big)z^{f''}z''{}^{-f}  \,.$$

This formula looks identical to [\[torintro\]](#torintro){reference-type="eqref" reference="torintro"}. However, the shape parameters here are promoted to functions $z\to z(\rho)$ of the representation $\rho$, which satisfy a well known deformed version of the gluing equations. Moreover, the flattening $f$ is slightly more restricted than it was previously. We will prove in Section [\[sec.utorsion\]](#sec.utorsion){reference-type="ref" reference="sec.utorsion"} that

::: theorem
[]{#thm.utor label="thm.utor"} The formula for $\tau_\mathcal{T}(\rho)$ is independent of the choice of enhanced Neumann-Zagier datum, and is invariant under 2--3 moves connecting $\rho$-regular triangulations.
:::

When $M$ is hyperbolic, it turns out that $\rho_0$-regular triangulations are $\rho$-regular for all but finitely many representations $\rho\in X_M^{\rm geom}$. Then we can create a topological invariant $\tau_M$ that is a function on $X_M^{\rm geom}$ just as in Proposition [\[prop.EP\]](#prop.EP){reference-type="ref" reference="prop.EP"}, by evaluating $\tau_\mathcal{T}(\rho)$ on any triangulation in the canonical subset $\mathcal X^{\mathrm{EP}}_M\subseteq \mathcal X_{\rho_0}$.

In general, there is a rational map from the character variety $X_M$ to the zero-locus $Y_M$ of the A-polynomial $A_M(\ell,m)=0$ [@CCGLS], for any $M$ with torus boundary. Therefore, the shapes $z$ and the torsion $\tau_\mathcal{T}$ are algebraic functions on components of the A-polynomial curve $Y_M$. When $M$ is hyperbolic and $\rho\in X_M^{\rm geom}$, somewhat more is true: the shapes are *rational* function on the geometric component $Y_M^{\rm geom}$ (Proposition [\[prop.shapes\]](#prop.shapes){reference-type="ref" reference="prop.shapes"}). Then

$$\qquad  \tau_M \;\in\; C(Y_M^{\rm geom}) = \mathbb Q(m)[\ell]/\big(A_M^{\rm geom}(\ell,m)\big)\,,$$

where $A^{\rm geom}_M(\ell,m)$ is the geometric factor of the A-polynomial. We will give a simple example of the function $\tau_M$ for the figure-eight knot in Section [\[sec.utor41\]](#sec.utor41){reference-type="ref" reference="sec.utor41"}.
