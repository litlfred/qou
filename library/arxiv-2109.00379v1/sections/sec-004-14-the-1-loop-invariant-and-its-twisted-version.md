---
doc_id: arxiv-2109.00379v1
doc_title: "TWISTED NEUMANN–ZAGIER MATRICES"
section_id: sec-004-14-the-1-loop-invariant-and-its-twisted-version
section_title: "The 1-loop invariant and its twisted version"
section_number: 1.4
pages: 7-8
source_pdf: 2109.00379v1.pdf
source_sha256: f0c9bd89312a761c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.98
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
---
[]{#sub.1loopt label="sub.1loopt"}

The adjoint Reidemeister torsion has a conjectural description in terms of the 1-loop invariant of [@DG1]. The latter depends on the NZ matrices of an ideal triangulation, its shapes, their flattenings and a peripheral curve $\gamma$. With the notation of Section [\[sub.tNZ\]](#sub.tNZ){reference-type="ref" reference="sub.tNZ"} the *1-loop invariant* is defined by $$\label{1loop}
\begin{aligned}
  \tau^\mathrm{CS}_\gamma(\mathcal T)
& := \frac{\det \left(  \widehat{\mathbf{A}}  \, \mathrm{diag}(\zeta) +
    \widehat{\mathbf{B}} \, \mathrm{diag}(\zeta'') \right)}{
2\prod_{j=1}^N\zeta_j^{f_j} \zeta_j'^{f_j'} \zeta_j''^{f_j''}} \\
& \,\,=
\frac{\det \left(  \widehat{\mathbf{G}}\, \mathrm{diag}(\zeta)
    +\widehat{\mathbf{G}}' \, \mathrm{diag}(\zeta')+\widehat{\mathbf{G}}'' \,
    \mathrm{diag}(\zeta'') \right)}{
    2\prod_{j=1}^N\zeta_j^{f_j} \zeta_j'^{f_j'} \zeta_j''^{f_j''}} 
 \in F/ (\pm1)
\end{aligned}$$ where the last equality follows from Equation [\[3GAB\]](#3GAB){reference-type="eqref" reference="3GAB"}. In [@DG1] it is conjectured that the 1-loop invariant $\tau^\mathrm{CS}_\gamma(\mathcal T)$ is equal to the adjoint torsion $\tau_\gamma(M)$ with respect to $\gamma$ $$\label{conj.DG}
\tau^\mathrm{CS}_\gamma(\mathcal T) \stackrel{?}{=}  \tau_\gamma(M)  \in F^\times / (\pm1)  .$$

Given the above conjecture and the discussion of Section [\[sub.tt\]](#sub.tt){reference-type="ref" reference="sub.tt"}, it is natural to predict the existence of a twisted version of the 1-loop invariant, defined in terms of the twisted NZ matrices. With the notation of Section [\[sub.tNZ\]](#sub.tNZ){reference-type="ref" reference="sub.tNZ"}, we define the *twisted 1-loop invariant* by $$\label{1loopt}
\begin{aligned}
\tau^\mathrm{CS}(\mathcal T,t)
&:=
\frac{\det\left(
\mathbf{A}(t)  \, \mathrm{diag}(\zeta) + \mathbf{B}(t) \, \mathrm{diag}(\zeta'')
\right)}{
\prod_{j=1}^N\zeta_j^{f_j} \zeta_j'^{f_j'} \zeta_j''^{f_j''}} \\
& := \frac{\det\left(
\mathbf{G}(t)\, \mathrm{diag}(\zeta)+\mathbf{G}'(t) \,
\mathrm{diag}(\zeta')+\mathbf{G}''(t) \,
\mathrm{diag}(\zeta'') \right)}{
\prod_{j=1}^N\zeta_j^{f_j} \zeta_j'^{f_j'} \zeta_j''^{f_j''}}
\in F[t^{\pm1}]/ (\pm t^\mathbbm Z)
\end{aligned}$$ where the second equality follows from the fact (analogous to Equation [\[3GAB\]](#3GAB){reference-type="eqref" reference="3GAB"}) $$\label{3GABt}
\mathbf{G}(t)\, \mathrm{diag}(\zeta)
+\mathbf{G}'(t) \, \mathrm{diag}(\zeta')
+ \mathbf{G}''(t) \, \mathrm{diag}(\zeta'')
= \mathbf{A}(t)  \, \mathrm{diag}(\zeta) + \mathbf{B}(t) \, \mathrm{diag}(\zeta'').$$

An elementary observation is that $\tau^\mathrm{CS}(\mathcal T,t)$ is well-defined up to multiplication by an element in $\pm t^\mathbbm Z$. Indeed, the computation in [@DG1 Sec.3.5] shows that up to sign, the twisted 1-loop invariant is independent of the choice of a combinatorial flattening. It also manifestly independent of the choice of a quad type of $\Delta_j$, as the definition [\[1loopt\]](#1loopt){reference-type="eqref" reference="1loopt"} is symmetric with respect to $\zeta,\zeta',$ and $\zeta''$. Finally, a different choice of lifts of the edges of $\mathcal T$ results to left multiplication of all of the matrices $\mathbf{G}^\square(t)$ by the same diagonal matrix $\mathrm{diag}(t^{c_1},t^{c_2},\dots,t^{c_N})$ for integers $c_1,c_2,\dots,c_N$, hence the observation follows.

By its very definition of $\tau^\mathrm{CS}(\mathcal T,t)$, it leads to a twisted version of Conjecture [\[conj.DG\]](#conj.DG){reference-type="eqref" reference="conj.DG"}, namely $$\label{TT}
\tau^\mathrm{CS}(\mathcal T,t) \stackrel{?}=  \tau(M,t) \in F[t^{\pm1}]/ (\pm t^\mathbbm Z)  .$$

We now list some properties of the twisted 1-loop invariant. The first concerns the topological invariance.

::: theorem
[]{#thm.top label="thm.top"} $\tau^\mathrm{CS}(\mathcal T,t)$ is invariant under Pachner 2--3 moves between ideal triangulations that support the geometric representation.
:::

Combining the above theorem with Proposition 1.7 of [@DG1], we conclude that the twisted 1-loop invariant defines a topological invariant of one-cusped hyperbolic 3-manifolds.

The next two theorems concern the properties [\[key1\]](#key1){reference-type="eqref" reference="key1"} and [\[key2\]](#key2){reference-type="eqref" reference="key2"} of the adjoint twisted Alexander polynomial.

::: theorem
[]{#thm.1 label="thm.1"} For all $n \geq 1$ we have $$\label{1loopcyclic}
  \tau^{\mathrm{CS}}(\mathcal T^{(n)},t^n)=\prod_{\omega^n=1}\tau^{\mathrm{CS}}(\mathcal T,\omega\, t)  .$$
:::

::: theorem
[]{#thm.2 label="thm.2"} We have $\tau^\mathrm{CS}(\mathcal T,1)=0$ and $\left. \frac{d}{dt}\right|_{t=1}
\tau^{\mathrm{CS}}(\mathcal T,t) = \tau_\lambda^{\mathrm{CS}}(\mathcal T)$ where $\lambda$ is the peripheral curve satisfying $\alpha(\lambda)=0$.
:::

A corollary of the above theorems is a relation between the twisted 1-loop invariant and the 1-loop invariant of [@DG1] for cyclic covers, namely $$\label{behavior2}
\frac{\tau^\mathrm{CS}_\mu(\mathcal T^{(n)})}{\tau^\mathrm{CS}_\mu(\mathcal T)}
=   \prod_{ \substack{\omega^n=1 \\ \omega \neq 1}} \tau^\mathrm{CS}(\mathcal T,w)  .$$

The next result concerns the symmetries of the twisted 1-loop invariant. Conjecture [\[conj.ABt\]](#conj.ABt){reference-type="ref" reference="conj.ABt"} implies a symmetry of the twisted 1-loop invariant which is known to hold for the adjoint twisted Alexander polynomial [@Kitano96; @KL99], namely $\tau(M,t)=\tau(M,1/t)$.

::: corollary
(assuming Conjecture [\[conj.ABt\]](#conj.ABt){reference-type="ref" reference="conj.ABt"}) []{#cor.sym label="cor.sym"} We have $$\label{1loopsymm}
\tau^\mathrm{CS}(\mathcal T,t) = \tau^\mathrm{CS}(\mathcal T,1/t) \in F[t^{\pm1}]/(\pm t^\mathbbm Z)  .$$
:::

We end our discussion on the twisted 1-loop invariant with a remark which suggests that the $t$-deformation variable is independent from the variable $\mathfrak{m}$ which is an eigenvalue of the meridian of an $\mathrm{SL}_2(\mathbbm C)$-representation of $\pi_1(M)$.

::: remark
[]{#rem.tcharacter label="rem.tcharacter"} By varying the representation, the adjoint Reidemeister torsion can be extended to a rational function on the geometric component $X_M$ of the $\mathrm{SL}_2(\mathbbm C)$-character variety of a knot complement $M$ [@Dubois-Garoufalidis], and consequently to a rational function of the geometric component of the $A$-polynomial curve. The same holds for the 1-loop invariant; see [@DG1 Sec.4]. Likewise, we can extend the twisted 1-loop invariant to a twisted rational function on the geometric component of the character variety, i.e., to an element of the ring $C(X_M)[t^{\pm1}]/(\pm t^\mathbbm Z)$, where $C(X_M)$ is the field of rational functions on $X_M$. Then, $\mathfrak{m} \in C(X_M)$ is a variable independent of $t$.
:::
