---
doc_id: arxiv-math-0604057v2
doc_title: "Volume conjecture, regulator and SL2(C)-character variety of a knot"
section_id: sec-013-5-an-example-the-figure-eight-knot
section_title: "An Example: The Figure Eight Knot"
section_number: 5
pages: 12-18
source_pdf: 0604057v2.pdf
source_sha256: 649fad141dc34eb9
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.975
doc_brief: "Volume conjecture, regulator and SL2(C)-character variety of a knot — In this paper, by using the regulator map of Beilinson-Deligne, we show that the quan- tization condition posed by Gukov is true"
---
Throughout this section, we shall denote by $M$ the complement of the figure-eight knot in $S^3$. we compute its character variety and give some applications.

It is well-known that $\pi_1(M)$ is given by two generators and one relation: $$\label{8gp}
  \pi_1(M)=<\alpha,\beta|R(\alpha,\beta)>,\;
  R(\alpha,\beta)=\beta^{-1}\alpha^{-1}\beta\alpha\beta^{-1}\alpha\beta\alpha^{-1}\beta^{-1}\alpha,$$

where $\alpha$, $\beta$ are meridians, and they are conjugate to each other $\beta=\delta\alpha\delta^{-1}$ with $\delta=\alpha^{-1}\beta\alpha\beta^{-1}$.

Set $\tau=\alpha\beta^{-1}\alpha^{-1}\beta$, we have a peripheral subgroup $\pi_1(\partial M)$ $$\label{8bgp}
 \pi_1(\partial M)=<\alpha,\lambda>; \;
 \lambda=\tau^{-1}\delta=\beta^{-1}\alpha\beta\alpha^{-1}\alpha^{-1}\beta\alpha\beta^{-1},$$

where $\alpha$ is the meridian and $\lambda$ is the longitude. Note in this section, we use $\alpha$ for the meridian instead of $\mu$.

Let us consider its character variety $X(M)$. We use ([\[8gp\]](#8gp){reference-type="ref" reference="8gp"}) for the presentation of $\pi_1(M)$. For a $SL_2(\mathbb{C})$-representation $\rho\in R(M)$, its character $\chi$ is determined by $\chi(\alpha)$, $\chi(\beta)$, and $\chi(\alpha\beta)$. We have the morphism $t:R(M)\rightarrow
\mathbb{C}^3$, $t(\rho)=(\chi(\alpha),
\chi(\beta),\chi(\alpha\beta))$ and $X(M)$ is the image $t(R(M))$. Let $(x,y,z)$ be the affine coordinate for $\mathbb{C}^3$.

::: proposition
[]{#8cha label="8cha"} The affine variety $X(M)\subset \mathbb{C}^3$ is defined by the following equations: $$\label{8d1}
  x=y,$$ $$\label{8d2}
 (x^2-z-2)(z^2-(1+x^2)z+2x^2-1)=0.$$ In particular, we can identify $X(M)$ with the affine plane curve $\{(x,z)\in \mathbb{C}^2|(x^2-z-2)(z^2-(1+x^2)z+2x^2-1)=0\}$. It has two irreducible components.
:::

::: proof
*Proof.* Since $\alpha$ is conjugate to $\beta$, $x=\chi(\alpha)=\chi(\beta)=y$. Hence ([\[8d1\]](#8d1){reference-type="ref" reference="8d1"}) follows. For the second equation, by [@Wh Theorem 1], the factor $x^2-z-2$ corresponds to characters of abelian representations, and the other one corresponds to the characters of non-abelian representations. ◻
:::

By the preceding proposition, the component defined by the equation $z^2-(1+x^2)z+2x^2-1=0$ consists of the characters of non-abelian representations, in particular, it contains the discrete faithful representations of the complete hyperbolic metric of $M$. We denote this component $X_0$. Hence we have :

::: corollary
[]{#8-cor1 label="8-cor1"} The component $X_0$ is an irreducible smooth curve in $\mathbb{C}^2$ with the defining equation: $$\label{8d3}
   z^2-(1+x^2)z+2x^2-1=0.$$
:::

::: proof
*Proof.* We only need to check that ([\[8d3\]](#8d3){reference-type="ref" reference="8d3"}) defines a smooth curve. Let $f(x,z)=z^2-(1+x^2)z+2x^2-1$. Then $\frac{\partial f}{\partial
x}=-2xz+4x$ and $\frac{\partial f}{\partial z}=2z-1-x^2$. It is straightforward to check that their is no common solution to the equations $\frac{\partial f}{\partial x}=\frac{\partial
f}{\partial z}=f(x,z)=0$. Hence, the curve is smooth. ◻
:::

::: corollary
[]{#8-cor2 label="8-cor2"} There are exactly two reducible characters on $X_0$ and they correspond to the points $(\pm \sqrt{5},3)$.
:::

::: proof
*Proof.* Let $\rho$ be a reducible representation whose character lies on $X_0$. Let $m$ be the eigenvalue of $\rho(\alpha)$. By [@CCGLS Proposition 6.2], $m^2$ must be a root of the Alexander polynomial $\Delta(t)=t^2-3t+1$ of the figure-eight knot. Thus, $$m=\pm \sqrt{\frac{3\pm \sqrt{5}}{2}}=\frac{\pm \sqrt{5}\pm
  1}{2}; \, \text{and}\; x=\sigma(\rho(\alpha))=m+m^{-1}=\pm \sqrt{5}.$$

Plug in ([\[8d3\]](#8d3){reference-type="ref" reference="8d3"}), we get $z=3$ with multiplicity two. Now it is easy to check that $(\pm \sqrt{5},3)$ are exactly the intersection points of $X_0$ and the component $x^2-z-2=0$. Since the latter component consists of abelian characters, the result follows. ◻
:::

::: remark
Two inequivalent reducible representations may have the same character. The points $(\pm \sqrt{5},3)$ above are such examples. They are the characters of both some abelian representation and non-abelian reducible representation which are clearly not equivalent.
:::

::: proposition
[]{#8cha-1 label="8cha-1"} Suppose that $\chi\in X_0$ and $\chi(\alpha)=\pm 2$. Then $\chi$ is the character of a discrete faithful representation.
:::

::: proof
*Proof.* Plug $x=\pm 2$ in ([\[8d3\]](#8d3){reference-type="ref" reference="8d3"}), we get $z^2-5z+7=0$ and hence $z=\frac{5 \pm \sqrt{-3}}{2}$. The following representation $\theta:\pi_1(M)\rightarrow PSL_2(\mathbb{C})$ was given in [@Ril2]: $$\theta(\alpha)=\pm
  \left[
  \begin{matrix}
    1 & 1\\
    0 & 1
  \end{matrix}
  \right], \;\;
\theta(\beta)=\pm
  \left[
  \begin{matrix}
    1 & 0\\
    -\omega & 1
  \end{matrix}
  \right];$$ where $\omega=\frac{-1+\sqrt{-3}}{2}$ is a primitive cube root of unity. By [@Ril2 Theorem 1], $\theta$ is an isomorphism. Thus, $\theta$ is a discrete faithful representation of $\pi_1(M)$. Let $\overline{\theta}$ be the complex conjugation of $\theta$. It is straightforward to check that the four points $(\pm 2, \frac{5 \pm \sqrt{-3}}{2})$ correspond to the $SL_2(\mathbb{C})$ characters of the lifts of $\theta$ and $\overline{\theta}$. The result follows. ◻
:::

Denote by $\mathbb{CP}^2$ the complex projective plane. We use $[X:Y:Z]$ to represent its homogenous coordinates. We will identify $\mathbb{C}^2$ with the open subset $\{[x:1:z]|(x,z)\in
\mathbb{C}^2\}$. Note this is different from the standard notation.

Let $\widetilde{X_0}$ be a smooth projective model of $X_0$. We have the following explicit description of $\widetilde{X_0}$ in $\mathbb{CP}^2$.

::: proposition
[]{#8-smo label="8-smo"} $\widetilde{X_0}$ is an elliptic curve and defined by the equation in $\mathbb{CP}^2$: $$\label{8sm}
   YZ^2-Y^2Z-X^2Z+2X^2Y-Y^3=0.$$
:::

::: proof
*Proof.* Equation ([\[8d3\]](#8d3){reference-type="ref" reference="8d3"}) is the defining equation of $X_0$. Substitute $x=\frac{X}{Y}$, $z=\frac{Z}{Y}$, and we get ([\[8sm\]](#8sm){reference-type="ref" reference="8sm"}). That is, it is the projective closure of $X_0$ in $\mathbb{CP}^2$. It suffices to show that it is smooth. Let $F(X,Y,Z)$ be the left-hand side of ([\[8sm\]](#8sm){reference-type="ref" reference="8sm"}). It is elementary to check that except $(0,0,0)$, there is no common solution to the equations $\frac{\partial F}{\partial X}=\frac{\partial F}{\partial
Y}=\frac{\partial F}{\partial Z}=0$. Hence, it is smooth. Since ([\[8sm\]](#8sm){reference-type="ref" reference="8sm"}) is a cubic equation in $\mathbb{CP}^2$, $\widetilde{X_0}$ has genus $1$. ◻
:::

::: corollary
[]{#8-ide label="8-ide"} $X_0$ has exactly two ideal points $[1:0:0]$ and $[0:0:1]$.
:::

::: proof
*Proof.* The ideal points correspond to $Y=0$. This gives $X^2Z=0$. Thus, $X=0$ or $Z=0$. ◻
:::

Next, we explicitly construct the restriction map $r:X_0\rightarrow X(\partial M)$ induced by the inclusion $i:\pi_1(\partial M)\rightarrow \pi_1(M)$.

::: theorem
[]{#8res label="8res"} The map $r:X_0\rightarrow X(\partial M)\in \mathbb{C}^3$ is given by the formulas: $$r(x,z)=(x,F(x,z),G(x,z));$$ where $F(x,z)=x^4-5x^2+2$ is the trace of the longitude $\lambda$, and $G(x,z)=(4x-x^3)z+(x^5-4x^3-x)$ is the trace of $\alpha
\lambda$.
:::

We will postpone the proof of Theorem [\[8res\]](#8res){reference-type="ref" reference="8res"} to the end of this section. Instead, we first discuss its applications. The reason is that the proof itself is elementary and lengthy, and probably is known to the experts. However, we can not find it in the literature. So we include here for completeness.

Denote by $x_0=[0:0:1]$ and $x_1=[1:0:0]$. By Corollary [\[8-ide\]](#8-ide){reference-type="ref" reference="8-ide"}, they are the only ideal points of $X_0$.

::: lemma
[]{#l-norm label="l-norm"} (1) Both $x_0$ and $x_1$ are poles of the meromorphic functions $f_{\alpha}$ and $f_{\lambda}$. Their orders are: $v_{x_0}(f_{\alpha})=v_{x_1}(f_{\alpha})=2$, and $v_{x_0}(f_{\lambda})=v_{x_1}(f_{\lambda})=8$.\
(2) The Culler-Shalen norm $|(1,0)|=4$ and $|(0,1)|=16$.
:::

::: proof
*Proof.* (1) By Theorem [\[8res\]](#8res){reference-type="ref" reference="8res"}, for $\chi=(x,z)\in X_0$, $I_{\alpha}(x,z)=x$ and $I_{\lambda}(x,z)=F(x,z)=x^4-5x^2+2$. Since $f_{\alpha}=I_{\alpha}^2-4$ and $f_{\lambda}=I_{\lambda}^2-4$, it is sufficient to show that $v_{x_0}(I_{\alpha})=v_{x_1}(I_{\alpha})=1$, and $v_{x_0}(I_{\lambda})=v_{x_1}(I_{\lambda})=4$.

On $\widetilde{X_0}$, substitute $x=\frac{X}{Y}$, $z=\frac{Z}{Y}$, we get for $[X:Y:Z]\in \widetilde{X_0}$, $$I_{\alpha}([X:Y:Z])=\frac{X}{Y},\, \text{and}\,\,
   I_{\lambda}([X:Y:Z])=\frac{X^4-5X^2Y^2+2Y^4}{Y^4}.$$ First, we consider $x_0=[0:0:1]$. Let $U_3=\{[X:Y:Z]|Z\ne 0\}$. Then it is an open subset containing $x_0$. $U_3$ is identified with $\mathbb{C}^2$ via $x=\frac{X}{Z}$ and $y=\frac{Y}{Z}$, where $(x,y)$ are affine coordinates of $\mathbb{C}^2$. Dividing by $Z^3$ the both sides of the equation ([\[8sm\]](#8sm){reference-type="ref" reference="8sm"}) of $\widetilde{X_0}$ and substituting $x=\frac{X}{Z}$ and $y=\frac{Y}{Z}$, we get the affine equation in $U_3=\mathbb{C}^2$: $$g(x,y)=y-y^2-x^2+2x^2y-y^3=0.$$ Under this identification, $x_0$ is the origin $(0,0)$, $I_{\alpha}(x,y)=\frac{x}{y}$ and $I_{\lambda}(x,y)=(\frac{x}{y})^4-5(\frac{x}{y})^2+2$. Since $\frac{\partial g}{\partial y}=1-2y+2x^2-3y^2$ and $\frac{\partial
g}{\partial y}(0,0)\ne 0$, the function $x$ is a local parameter of the local ring of regular functions at $(0,0)$. Solve $g(x,y)=0$, we get $$I_{\alpha}(x,y)=\frac{x}{y}=x^{-1}u(x,y),\, \text{where}\,
  u(x,y)=\frac{y^2+y-1}{2y-1},\, u(0,0)\ne 0;$$ and $$I_{\lambda}(x,y)=x^{-4}w(x,y),\, \text{where}\,
  w(x,y)=u^4-5x^2u^2+2x^4
  ,\, w(0,0)\ne 0.$$ Therefore, $x_0$ is a pole of $I_{\alpha}$ of order $1$, and it is a pole of $I_{\lambda}$ of order $4$.

For $x_1=[1:0:0]$. Let $U_1=\{[X:Y:Z]|X\ne 0\}$. $U_1$ is identified with $\mathbb{C}^2$ via $y=\frac{Y}{X}$ and $z=\frac{Z}{X}$, where $(y,z)$ are affine coordinates of $\mathbb{C}^2$. Similarly, we obtain the affine equation in $U_1=\mathbb{C}^2$: $$h(x,y)=yz^2-y^2z-z+2y-y^3=0.$$ Now $x_0$ is the origin $(0,0)$, $I_{\alpha}(x,y)=y^{-1}$ and $I_{\lambda}(x,y)=y^{-4}-5y^{-1}+2$. Since $\frac{\partial
h}{\partial z}(0,0)\ne 0$, the function $y$ is a local parameter of the local ring of regular functions at $(0,0)$. Thus, $x_0$ is a pole of $I_{\alpha}$ of order $1$, and it is a pole of $I_{\lambda}$ of order $4$.

\(2\) By definition, $|(1,0)|=\text{deg}f_{\alpha}=v_{x_0}(f_{\alpha})+v_{x_1}(f_{\alpha})$, by (1), $|(1,0)|=2+2=4$. Similarly, $|(0,1)|=8+8=16$. ◻
:::

Use this lemma, we can compute the Culler-Shalen norm $|(p,q)|$ for any $\gamma=p\alpha+q\lambda\in H_1(\partial M,\mathbb{Z})$.

::: proposition
[]{#p-8norm label="p-8norm"} For each $\gamma=p\alpha+q\lambda\in H_1(\partial M,\mathbb{Z})$, the Culler-Shalen norm $|\gamma|=|(p,q)|=2(|p+4q|+|p-4q|)$.
:::

::: proof
*Proof.* By Lemma [@CGLS  1.4.1, 1.4.2], for each ideal point $x$, there is a homomorphism $\phi_x:H_1(\partial
M,\mathbb{Z})\rightarrow \mathbb{Z}$, such that, for each $\gamma=p\alpha+q\lambda$, $$v_x(f_{\gamma})=|\phi_x(\gamma)|,\, \text{and}\, |\gamma|=\sum_{x:\,\text{ideal
  point}}|\phi_x(\gamma)|;$$ where $v_x(f_{\gamma})$ denotes the order of pole of $f_{\gamma}$ at $x$. For our case, we have two ideal points $x_0$ and $x_1$. By Lemma [\[l-norm\]](#l-norm){reference-type="ref" reference="l-norm"}, we get $|\phi_{x_0}(\alpha)|=2$, $|\phi_{x_0}(\lambda)|=8$, $|\phi_{x_1}(\alpha)|=2$ and $|\phi_{x_1}(\lambda)|=8$. Since $\phi_{x_i}$ are homomorphisms, we obtain that $|\phi_{x_{i}}(\gamma)|=|\pm 2p \pm 8q|$, $i=1,2$. Therefore, we obtain that either $$|\phi_{x_{0}}(\gamma)|+|\phi_{x_{1}}(\gamma)|=|2p+8q|+|2p+8q|,$$ or $$|\phi_{x_{0}}(\gamma)|+|\phi_{x_{1}}(\gamma)|=|2p+8q|+|2p-8q|.$$ We claim that the first case can not happen. Suppose not. Take $\gamma=-4\alpha+\lambda$, then $|\gamma|=|\phi_{x_{0}}(\gamma)|+|\phi_{x_{1}}(\gamma)|=0$. Hence $\text{deg}f_{\gamma}=|\gamma|=0$. This is impossible because $f_{\gamma}$ is not constant. Thus the claim is proved and $|\gamma|=|(p,q)|=2(|p+4q|+|p-4q|)$. ◻
:::

Next let $M(0)$ be the closed $3$-manifold obtained by the Dehn surgery of $M$ along the longitude $\lambda$. It is known that $M(0)$ admits an essential torus [@Boy Page 200]. By Theorem [\[8res\]](#8res){reference-type="ref" reference="8res"}, we show that $M(0)$ has non-abelian infinite fundamental group.

::: proposition
[]{#0sur label="0sur"} The fundamental group $\pi_1(M(0))$ is a non-abelian, infinite group.
:::

::: proof
*Proof.* Suppose that $\rho\in R(M)$ with the property that its trace $\sigma(\rho(\lambda))=2$. Now by Proposition [\[8res\]](#8res){reference-type="ref" reference="8res"}, we have: $$x^4-5x^2+2=2$$ where $x=\sigma(\rho(\alpha))$. Solve this equation, we get $x=0$ or $x=\pm \sqrt{5}$. By Proposition [\[8cha\]](#8cha){reference-type="ref" reference="8cha"}, there exists $\rho_0\in R(M)$, such that $\sigma(\rho_0(\alpha))=0$ and $\sigma(\rho_0(\lambda))=2$. In particular the eigenvalues of $\rho_0(\alpha)$ is $\pm i$. By [@CCGLS Proposition 6.2], $\rho_0$ is an irreducible representation. On the other hand, since $\rho_0(\alpha)$ and $\rho_0(\lambda)$ commute and $\rho_0(\alpha)$ is not parabolic, $\rho_0(\lambda)$ must be the identity matrix. Hence $\rho_0$ induce a representation of $\pi_1(M(0))$. The irreducibility of $\rho_0$ implies that $\pi_1(M(0))$ is not abelian.

Similarly, let $\rho_{\sqrt{5}}\in R(M)$, such that $\sigma(\rho_{\sqrt{5}}(\alpha))=\sqrt{5}$ and $\sigma(\rho_{\sqrt{5}}(\lambda))=2$. By the same reason, $\rho_{\sqrt{5}}(\lambda)$ equals the identity matrix. Hence $\rho_{\sqrt{5}}$ induces a representation of $\pi_1(M(0))$. We can check that the image of $\rho_{\sqrt{5}}$ in $SL_2(\mathbb{C})$ is torsion-free. Therefore, $\pi_1(M(0))$ is not finite. ◻
:::

::: remark
We know that $M(0)$ is not a hyperbolic manifold. $0/1$ is the one of the ten exceptional surgery slopes of the figure-eight knot. It is interesting to know that we can prove its fundamental group is non-cyclic, non-abelian and infinite just from the elementary computations.
:::

Let $M(3)$ be the closed $3$-manifold obtained by the Dehn surgery of $M$ along the simple closed curve $\gamma=3\alpha+\lambda$.

::: lemma
[]{#3/1-irre label="3/1-irre"} $M(3)$ has exactly three irreducible $SL_2(\mathbb{C})$ characters.
:::

::: proof
*Proof.* Since $\pi_1(M(3))=\langle \pi_1(M)|\alpha^3\lambda=1\rangle$, we have an embedding of character varieties $X(M(3))\hookrightarrow X(M)$. On the other hand, $X_0$ is the only component of $X(M)$ containing characters of non-abelian representations. Thus, the irreducible characters of $M(3)$ are contained in the set $S=\{\chi|\chi\in X_0,
 \chi(\alpha^3\lambda)=2\}$. By ([\[tf3\]](#tf3){reference-type="ref" reference="tf3"}), we have $$\chi(\alpha^2\lambda)=\chi(\alpha)\chi(\alpha\lambda)-\chi(\lambda),$$ and $$\label{3/1-t}
    \begin{aligned}
      \chi(\alpha^3\lambda)=&\chi(\alpha)\chi(\alpha^2\lambda)-\chi(\alpha\lambda)\\
                           =&(\chi(\alpha)^2-1)\chi(\alpha\lambda)-\chi(\alpha)\chi(\lambda).
    \end{aligned}$$ By Theorem [\[8res\]](#8res){reference-type="ref" reference="8res"}, we obtain $$\label{3/1-eq1}
  (x^2-1)[(4x-x^3)z+x^5-4x^3-x]-x(x^4-5x^2+2)=2.$$ It is clear that the set $S$ is exactly the common solutions to equations ([\[3/1-eq1\]](#3/1-eq1){reference-type="ref" reference="3/1-eq1"}) and ([\[8d3\]](#8d3){reference-type="ref" reference="8d3"}). Note when $x=1$, ([\[3/1-eq1\]](#3/1-eq1){reference-type="ref" reference="3/1-eq1"}) holds and is independent of the values of $z$. From ([\[8d3\]](#8d3){reference-type="ref" reference="8d3"}), when $x=1$, $z=1$. So $(1,1)\in S$.

We solve $z$ in terms of $x$ from ([\[3/1-eq1\]](#3/1-eq1){reference-type="ref" reference="3/1-eq1"}), then plug in ([\[8d3\]](#8d3){reference-type="ref" reference="8d3"}) and simplify the expression, we get $$\label{3/1-eq2}
  C(x)=x^4-4x^3+2x^2+4x+1=(x^2-2x-1)^2=0.$$ It has two solutions $x=1\pm \sqrt{2}$. Hence the set $S$ has three elements. They are not equal to $\pm 2$ or $\pm \sqrt{5}$. By Corollary [\[8-cor2\]](#8-cor2){reference-type="ref" reference="8-cor2"}, $x\ne \pm \sqrt{5}$ implies that each one is an irreducible character. By Proposition [\[8cha-1\]](#8cha-1){reference-type="ref" reference="8cha-1"} and [\[kin\]](#kin){reference-type="ref" reference="kin"}, $x\ne \pm 2$ means that each one is also a character of $M(3)$. The result follows. ◻
:::

Let $sl_2(\mathbb{C})$ be the Lie algebra of $SL_2(\mathbb{C})$. Then we have the adjoint representation $Ad:
SL_2(\mathbb{C})\rightarrow Aut(sl_2(\mathbb{C}))$. For a representation $\rho:\pi_1(M(3))\rightarrow SL_2(\mathbb{C})$, let $H^1(M(3); sl_2(\mathbb{C})_\rho)$ be the first cohomology group with coefficients in $sl_2(\mathbb{C})$ twisted by the composition $Ad\circ \rho$.

::: proposition
[]{#3/1-prop1 label="3/1-prop1"} Suppose that $\rho:\pi_1(M(3))\rightarrow SL_2(\mathbb{C})$ is irreducible.\
Then $H^1(M(3);sl_2(\mathbb{C})_\rho)=0$.
:::

::: proof
*Proof.* By [@BW Theorem 1.1], $M(3)$ is not toroidal. Since $H_1(M(3);\mathbb{Z})$ is finite, $M(3)$ is a small Seifeit fibered space. By the preceding Lemma [\[3/1-irre\]](#3/1-irre){reference-type="ref" reference="3/1-irre"}, $M(3)$ has irreducible representations, so $\pi_1(M(3))$ is not cyclic. By [@BZ1 Proposition 7], $H^1(M(3); sl_2(\mathbb{C})_\rho)=0$. ◻
:::

::: remark
For the other eight exceptional surgery slopes $\pm 1$, $\pm 2$, $\pm 3$, $\pm 4$, we also have the explicit irreducible representations with infinite images. Hence their fundamental groups are all non-abelian and infinite. We omit the details here. Hence, Proposition [\[3/1-prop1\]](#3/1-prop1){reference-type="ref" reference="3/1-prop1"} holds also for $M(\pm1)$, $M(\pm2)$ and $M(-3)$.
:::

Now we turn to the proof of Theorem [\[8res\]](#8res){reference-type="ref" reference="8res"}. We need to find explicit expressions of the traces $F(x,z)$, $G(x,z)$ of $\rho(\lambda)$ and $\rho(\alpha\lambda)$ respectively in terms of traces of $\rho(\alpha)$ and $\rho(\alpha\beta)$.

We need some preliminary lemmas. For $A$, $B$, $C\in
SL_2(\mathbb{C}))$, we have the following identities on their traces [@Wh]: $$\label{tf1}
  \sigma(AB)=\sigma(BA);$$ $$\label{tf2}
 \sigma(A)=\sigma(A^{-1});$$ $$\label{tf3}
  \sigma(AB)=\sigma(A)\sigma(B)-\sigma(AB^{-1});$$ $$\label{tf4}
 \sigma(ABC)=\sigma(A)\sigma(BC)+\sigma(B)\sigma(AC)+\sigma(C)\sigma(AB)-\sigma(A)\sigma(B)\sigma(C)-\sigma(ACB);$$ $$\label{tf5}
 \text{For}\, m\geq 2,
 \sigma(A^m)=\sigma(A^{m-1})\sigma(A)-\sigma(A^{m-2}).$$

Notice that ([\[tf1\]](#tf1){reference-type="ref" reference="tf1"}) is true for any $n\times n$ matrices. It is easy to see that ([\[tf4\]](#tf4){reference-type="ref" reference="tf4"}) and ([\[tf5\]](#tf5){reference-type="ref" reference="tf5"}) follow from ([\[tf3\]](#tf3){reference-type="ref" reference="tf3"}). Equations ([\[tf2\]](#tf2){reference-type="ref" reference="tf2"}) and ([\[tf3\]](#tf3){reference-type="ref" reference="tf3"}) can be checked by direct computations.\
Now for $\rho\in R(M)$, set $a=\rho(\alpha)$, $b=\rho(\beta)$, $x=\sigma(a)=\sigma(b)$ and $z=\sigma(ab)=\sigma(\rho(\alpha\beta))$.

::: lemma
[]{#tr1 label="tr1"} (i) $\sigma(a^2)=x^2-2$.\
(ii) $\sigma(a^{-1}b)=\sigma(ba^{-1})=\sigma(b^{-1}a)=\sigma(ab^{-1})=x^2-z$.\
(iii) $\sigma(b^{-1}aba^{-1})=\sigma(a^{-1}bab^{-1})=z^2-x^2z+2x^2-2$.
:::

::: proof
*Proof.* (i) By ([\[tf5\]](#tf5){reference-type="ref" reference="tf5"}), $\sigma(a^2)=\sigma(a)^2-\sigma(I)$, where $I$ is the $2\times 2$ identity matrix.

\(ii\) By ([\[tf1\]](#tf1){reference-type="ref" reference="tf1"}), $\sigma(a^{-1}b)=\sigma(ba^{-1})$ and $\sigma(b^{-1}a)=\sigma(ab^{-1})$ ; by ([\[tf2\]](#tf2){reference-type="ref" reference="tf2"}), $\sigma(ab^{-1})=\sigma(ba^{-1})$; by ([\[tf3\]](#tf3){reference-type="ref" reference="tf3"}), $\sigma(ab^{-1})=x^2-z$.

\(iii\) By the subdivision $(b^{-1}a)ba^{-1}$ and ([\[tf4\]](#tf4){reference-type="ref" reference="tf4"}), we have $$\sigma(b^{-1}aba^{-1})=\sigma(b^{-1}a)\sigma(ba^{-1})+\sigma(b)\sigma(b^{-1})
  +\sigma(a^{-1})\sigma(b^{-1}ab)-\sigma(b^{-1}a)\sigma(b)\sigma(a^{-1})-\sigma(I).$$ Therefore, $$\sigma(b^{-1}aba^{-1})=(x^2-z)^2+x^2+x^2-(x^2-z)x^2-2=z^2-x^2z+2x^2-2.$$ The proof for $\sigma(a^{-1}bab^{-1})$ is the same by the subdivision $(a^{-1}b)ab^{-1}$, and we omit it. ◻
:::

::: lemma
[]{#tr2 label="tr2"} (i) $\sigma(a^{-1}a^{-1}b)=x(x^2-z)-x$;\
(ii) $\sigma(ba^{-1}a^{-1}b)=x^4-zx^2-2x^2+2$;\
(iii) $\sigma(ba^{-1}a^{-1}bab^{-1})=x^2-z$.
:::

::: proof
*Proof.* (i) By ([\[tf3\]](#tf3){reference-type="ref" reference="tf3"}), we have $$\sigma(a^{-1}(a^{-1}b))=\sigma(a^{-1})\sigma(a^{-1}b)-\sigma(a^{-1}b^{-1}a)$$ By Lemma [\[tr1\]](#tr1){reference-type="ref" reference="tr1"}, each term of the right-hand side is known. Hence, $$\sigma(a^{-1}a^{-1}b)=x(x^2-z)-x.$$

\(ii\) By ([\[tf3\]](#tf3){reference-type="ref" reference="tf3"}), $$\sigma(b(a^{-1}a^{-1}b))=\sigma(b)\sigma(a^{-1}a^{-1}b)-\sigma(bb^{-1}aa)=\sigma(b)\sigma(a^{-1}a^{-1}b)-\sigma(a^2)$$ The formula follows.

\(iii\) By ([\[tf4\]](#tf4){reference-type="ref" reference="tf4"}), we have $$\begin{aligned}
  \begin{split}
    \sigma((ba^{-1})(a^{-1}b)(ab^{-1}))&=\sigma(ba^{-1})\sigma(a^{-1}bab^{-1})+\sigma(a^{-1}b)\sigma(1)+\sigma(ab^{-1})\sigma(ba^{-1}a^{-1}b)-\\
                                       & \sigma(ba^{-1})\sigma(a^{-1}b)\sigma(ab^{-1})-\sigma(a^{-1}b)
  \end{split}
\end{aligned}$$

Plug in what we know on the right-hand side and simplify, we obtain the formula. ◻
:::

::: lemma
[]{#tr3 label="tr3"} (i) $\sigma(ab^{-1}a)=\sigma(aab^{-1})=x^3-zx-x$;\
(ii) $\sigma(aab)=xz-x$;\
(iii) $\sigma(ab^{-1}aba^{-1})=x$
:::

::: proof
*Proof.* (i) $\sigma(a(b^{-1}a))=\sigma(a)\sigma(b^{-1}a)-\sigma(b)$, and $\sigma(a(ab^{-1}))=\sigma(a)\sigma(ab^{-1})-\sigma(aba^{-1})$;\
(ii) $\sigma(a(ab))=\sigma(a)\sigma(ab)-\sigma(ab^{-1}a^{-1})$\
(iii) $\sigma(a(b^{-1}aba^{-1}))=\sigma((b^{-1}aba^{-1})a)=\sigma(b^{-1}ab)=x$. ◻
:::

::: proof
*Proof of Theorem [\[8res\]](#8res){reference-type="ref" reference="8res"}.* First, let us compute $F(x,z)=\sigma(\rho(\lambda))$, the trace of $\rho(\lambda)$. By ([\[tf4\]](#tf4){reference-type="ref" reference="tf4"}), we have $$\begin{aligned}
  \begin{split}
     \sigma((b^{-1}a)(ba^{-1})(a^{-1}bab^{-1}))&=\sigma(b^{-1}a)\sigma(ba^{-1}a^{-1}bab^{-1})+\sigma(ba^{-1})\sigma(ab^{-1})+\\
                                               & \sigma(a^{-1}bab^{-1})\sigma(b^{-1}aba^{-1})
                   -\sigma(b^{-1}a)\sigma(ba^{-1})\sigma(a^{-1}bab^{-1})-\sigma(I)
  \end{split}
\end{aligned}$$

By Lemmas [\[tr1\]](#tr1){reference-type="ref" reference="tr1"} and [\[tr2\]](#tr2){reference-type="ref" reference="tr2"}, we know all the terms on the right-hand side. Notice that $(x,z)\in X_0$, hence $z^2-(1+x^2)z+2x^2-1=0$. Now divide the right-hand side by $z^2-(1+x^2)z+2x^2-1$, the remainder is $F(x,z)$. we calculate that $F(x,z)=x^4-5x^2+2$.\
For the trace of $\rho(\alpha\lambda)$, we have $$\begin{aligned}
  \begin{split}
     \sigma((ab^{-1}a)(ba^{-1})(a^{-1}bab^{-1}))&=\sigma(ab^{-1}a)\sigma(ba^{-1}a^{-1}bab^{-1})+\sigma(ba^{-1})\sigma(aab^{-1})+\\
                                                & \sigma(a^{-1}bab^{-1})\sigma(ab^{-1}aba^{-1})-\sigma(ab^{-1}a)\sigma(ba^{-1})\sigma(a^{-1}bab^{-1})
                                                -\sigma(a).
  \end{split}
\end{aligned}$$

By Lemmas [\[tr1\]](#tr1){reference-type="ref" reference="tr1"}, [\[tr2\]](#tr2){reference-type="ref" reference="tr2"} and [\[tr3\]](#tr3){reference-type="ref" reference="tr3"}, we have all the terms on the right-hand side. Then we divide the result of the right-hand side by the polynomial $z^2-(1+x^2)z+2x^2-1=0$ and $G(x,z)$ equals the remainder. We calculate that it is $(4x-x^3)z+(x^5-4x^3-x)$. ◻
:::
