---
doc_id: arxiv-1002.0126v1
doc_title: "AN INTRODUCTION TO THE VOLUME CONJECTURE"
section_id: sec-016-52-deformation-of-the-parameter
section_title: "Deformation of the parameter"
section_number: 5.2
pages: 29-38
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.985
doc_brief: "AN INTRODUCTION TO THE VOLUME CONJECTURE — This is an introduction to the Volume Conjecture and its gener- alizations for nonexperts."
---
In the Volume Conjecture (Conjecture [\[conj:VC\]](#conj:VC){reference-type="ref" reference="conj:VC"}) and its complexification (Conjecture [\[conj:CVC\]](#conj:CVC){reference-type="ref" reference="conj:CVC"}), the (possible) limit corresponds to the complete hyperbolic structure of $S^3\setminus{K}$ for a hyperbolic knot $K$. As described in [@Thurston:GT3M Chapter 4] the complete structure can be deformed to incomplete ones.

How can we perform this deformation in the colored Jones polynomial? If we deform the parameter $2\pi\sqrt{-1}$ in the Volume Conjecture, is the corresponding limits related to incomplete hyperbolic structures?

Let us consider the limit $$\lim_{N\to\infty}\frac{\log J_N\Bigl(K;\exp\bigl((u+2\pi\sqrt{-1})/N\bigr)\Bigr) }{N}.$$ Note that when $u=0$, this limit is considered in the (complexified) Volume Conjecture.

### Figure-eight knot

Before stating a conjecture for general knots, I will explain what happens in the case of the figure-eight knot.

::: theorem
[]{#thm:MY label="thm:MY"} Let $E$ be the figure-eight knot. There exists a neighborhood $\mathcal{O}\subset\mathbb{C}$ of $0$ such that if $u\in(\mathcal{O}\setminus\pi\sqrt{-1}\mathbb{Q})\cup\{0\}$, then the following limit exists: $$\lim_{N\to\infty}
  \frac{\log J_N(E;\exp\bigl((u+2\pi\sqrt{-1})/N\bigr))}{N}.$$ Moreover if we put $$\begin{aligned}
  H(u)
  &:=
  (u+2\pi\sqrt{-1})\times(\text{the limit above}),
  \\
  \intertext{and}
  v
  &:=
  2\dfrac{d\,H(u)}{d\,u}-2\pi\sqrt{-1}
\end{aligned}$$ then we have $$\begin{gathered}
  \operatorname{Vol}(E_{u})+\sqrt{-1}\operatorname{CS}(E_{u})
  \\
  \equiv
  -\sqrt{-1}H(u)
  -\pi{u}
  +u\,v\sqrt{-1}/4
  -\pi\kappa(\gamma_u)/2
  \pmod{\pi^2\sqrt{-1}\mathbb{Z}}.
\end{gathered}$$

Here $E_{u}$ is the closed hyperbolic three-manifold associated with the following representation of $\pi_1\left(S^3\setminus{E}\right)\to SL(2;\mathbb{C})$: $$\label{eq:meridian_longitude}
\begin{split}
  \mu
  &\mapsto
  \begin{pmatrix}\exp(u/2)&\ast\\0&\exp(-u/2)\end{pmatrix},
  \\[5mm]
  \lambda
  &\mapsto
  \begin{pmatrix}\exp(v/2)&\ast\\0&\exp(-v/2)\end{pmatrix}.
\end{split}$$ Here $\mu$ is the meridian of $E$ $($a loop in $S^3\setminus{E}$ that goes around the knot, which generates $H_1(S^3\setminus{E})\cong\mathbb{Z}$$)$, $\lambda$ is the longitude $($a loop in $S^3\setminus{E}$ that goes along the knot such that it is homologous to $0$ in $H_1(S^3\setminus{E})$$)$, and $\gamma_u$ is the loop attached to $S^3\setminus{E}$ when we complete the hyperbolic structure defined by $u$. We also put $\kappa(\gamma_{u}):=\operatorname{length}(\gamma_u)+\sqrt{-1}\operatorname{torsion}(\gamma_u)$, where $\operatorname{length}(\gamma_u)$ is the length of the attached loop $\gamma_u$, and $\operatorname{torsion}$ is its torsion, which is defined modulo $2\pi$ as the rotation angle when one travels along $\gamma_u$. See [@Neumann/Zagier:TOPOL85] for details $($see also [@Murakami:FUNDM2004]$)$.
:::

We will give a sketch of the proof in the following two subsections.

### Calculation of the limit

First we calculate the limit. Note that here I give just a sketch of the calculation but it can be done rigorously. For details see [@Murakami/Yokota:JREIA2007].

From [\[eq:Jones_fig8\]](#eq:Jones_fig8){reference-type="eqref" reference="eq:Jones_fig8"} we have $$J_N(E;q)
  =
  \sum_{j=0}^{N-1}
  q^{jN}
  \prod_{k=1}^{j}
  \left(1-q^{-N-k}\right)
  \left(1-q^{-N+k}\right).$$ Put $q:=\exp(\theta/N)$ for $\theta$ near $2\pi\sqrt{-1}$. If $\theta$ is not a rational multiple of $\pi\sqrt{-1}$ (but it can be $2\pi\sqrt{-1}$), we have $$\begin{split}
  &\log
  \left(
    \prod_{k=1}^{j}
    \left(1-q^{-N\pm k}\right)
  \right)
  \\
 =&
  \sum_{k=1}^{j}
  \log
  \big(1-\exp(\pm k\theta/N-\theta)\bigr)
  \\
  \underset{N\to\infty}{\approx}&
  N
  \int_{0}^{j/N}\log(1-\exp(\pm\theta s-\theta))\,ds
  \\
  =&
  \frac{\pm N}{\theta}
  \int_{\exp(-\theta)}^{\exp(\pm j\theta/N-\theta)}
  \frac{\log(1-t)}{t}dt
  \\
  =&
  \frac{\pm N}{\theta}
  \left(
    \operatorname{Li}_2\bigl(\exp(-\theta)\bigr)
    -
    \operatorname{Li}_2\bigl(\exp(\pm j\theta/N-\theta)\bigr)
  \right).
\end{split}$$ So we have $$\begin{split}
  &J_N\bigl(E;\exp(\theta/N)\bigr)
  \\
  \underset{N\to\infty}{\approx}&
  \sum_{j=0}^{N-1}
  \exp(j\theta)
  \exp
  \left[
    \frac{N}{\theta}
    \left(
      \operatorname{Li}_2\bigl(\exp(-j\theta/N-\theta)\bigr)
      -
      \operatorname{Li}_2\bigl(\exp(j\theta/N-\theta)\bigr)
    \right)
  \right]
  \\
  =&
  \sum_{j=0}^{N-1}
  \exp
  \left[
    \frac{N}{\theta}
    H\bigl(\exp(j\theta/N),\exp(\theta)\bigr)
  \right]
  \\
  \underset{N\to\infty}{\approx}&
  \int_{C}
  \exp
  \left[
    \frac{N}{\theta}
    H\bigl(x,\exp(\theta)\bigr)
  \right]
  \,dx
\end{split}$$ for a suitable contour $C$. Here we put $$\label{eq:H}
  H(\zeta,\eta)
  :=
  \operatorname{Li}_2(1/(\zeta\eta))-\operatorname{Li}_2(\zeta/\eta)+\log{\zeta}\log{\eta}.$$

To apply the steepest descent method (Theorem [\[thm:steepest_descent_method\]](#thm:steepest_descent_method){reference-type="ref" reference="thm:steepest_descent_method"}), we find the maximum of $\operatorname{Re}\left(H\bigl(x,\exp(\theta)\bigr)/\theta\right)$ over $x$. To do that we will find a solution $y$ to the equation $d\,H\bigl(x,\exp(\theta)\bigr)/d\,x=0$, which is $$\frac{\log\left[\exp(\theta)+\exp(-\theta)-x-x^{-1}\right]}{x}
  =0.$$ We can show that appropriately chosen $y$ gives the maximum and from the steepest descent method we have $$J_N\bigl(E;\exp(\theta/N)\bigr)
  \underset{N\to\infty}{\approx}
  \exp
  \left[
    \frac{N}{\theta}
    H\bigl(y,\exp(\theta)\bigr)
  \right],$$ that is, $$\label{eq:GVC_limit}
  \theta
  \lim_{N\to\infty}
  \frac{J_N\bigl(E;\exp(\theta/N)\bigr)}{N}
  =
  H\bigl(y,\exp(\theta)\bigr),$$ where $y$ satisfies $$y+y^{-1}
  =
  \exp(\theta)+\exp(-\theta)-1.$$

### Calculation of the volume

Next we will relate the limit to the volume of a three-manifold obtained by $S^3\setminus{E}$.

As described in § [\[subsubsec:geometry\]](#subsubsec:geometry){reference-type="ref" reference="subsubsec:geometry"}, $S^3\setminus{E}$ is obtained by gluing two ideal hyperbolic tetrahedra as in Figure [\[fig:fig8_tetra\]](#fig:fig8_tetra){reference-type="ref" reference="fig:fig8_tetra"}. Here we assume that they are parametrized by complex numbers $z$ and $w$. When $z=w=(1+\sqrt{-3})/2$, $S^3\setminus{E}$ has a complete hyperbolic structure as described in § [\[subsubsec:geometry\]](#subsubsec:geometry){reference-type="ref" reference="subsubsec:geometry"}. We assume that the left tetrahedron (with faces labeled with $A$, $B$, $C$ and $D$) and the right tetrahedron (with faces labeled with $A'$, $B'$, $C'$ and $D'$) in Figure [\[fig:fig8_tetra\]](#fig:fig8_tetra){reference-type="ref" reference="fig:fig8_tetra"} are $\Delta(z)$ and $\Delta(w)$ respectively.

The boundary torus, which is obtained from the shadowed triangles in Figure [\[fig:fig8_tetra\]](#fig:fig8_tetra){reference-type="ref" reference="fig:fig8_tetra"}, looks like Figure [1](#fig:torus){reference-type="ref" reference="fig:torus"}. Here the leftmost triangle is the one in the center of the picture of $\Delta(z)$ and the second leftmost one is the one in the center of the picture of $\Delta(w)$. Let $\alpha$, $\beta$ and $\gamma$ be the dihedral angle between $B$ and $C$, $A$ and $B$, and $C$ and $A$ respectively. Let $\alpha'$, $\beta'$ and $\gamma'$ be the dihedral angle between $B'$ and $D'$, $A'$ and $B'$, and $D'$ and $A'$ respectively.

![Identifying the sides as indicated by the circles, we get a triangulation of the boundary torus. Here the single circles denote the arrow head of the single arrow, the double circles denote the arrow head of the double arrow, the circles with $-$ denote the arrow tail of the single arrow, and the circles with $+$ denote the arrow tail of the double arrow in Figure [\[fig:fig8_tetra\]](#fig:fig8_tetra){reference-type="ref" reference="fig:fig8_tetra"}. Note that we view this torus from outside of $S^3\setminus{E}$.](torus_small.eps){#fig:torus}

As described in § [\[subsubsec:geometry\]](#subsubsec:geometry){reference-type="ref" reference="subsubsec:geometry"}, the sum of the dihedral angles around each edge should be $2\pi$. So from Figure [1](#fig:torus){reference-type="ref" reference="fig:torus"}, we have $$\begin{aligned}
  \beta+2\gamma+\beta'+2\gamma'&=2\pi\quad\text{from the single circles},
  \\
  2\alpha+\beta+2\alpha'+\beta'&=2\pi\quad\text{from the double circles},
  \\
  \beta+2\gamma+\beta'+2\gamma'&=2\pi\quad\text{from the circles with $-$},
  \\
  2\alpha+\beta+2\alpha'+\beta'&=2\pi\quad\text{from the circles with $+$},
\end{aligned}$$ which is equivalent to a single equation $$2\alpha+\beta+2\alpha'+\beta'=2\pi$$ since $\alpha+\beta+\gamma=\alpha'+\beta'+\gamma'=\pi$.

Assume that $\alpha=\arg{z}$ and $\alpha'=\arg{w}$. Since $\beta=\arg(1-1/z)$ and $\beta'=\arg(1-1/w)$ (see Figures [\[fig:top_view\]](#fig:top_view){reference-type="ref" reference="fig:top_view"} and [\[fig:tetrahedron_parameter\]](#fig:tetrahedron_parameter){reference-type="ref" reference="fig:tetrahedron_parameter"}) this turns out to be $$2\arg{z}+\arg(1-1/z)+2\arg{w}+\arg(1-1/w)=2\pi.$$ So we have $$\label{eq:hyperbolicity}
  zw(z-1)(w-1)=1.$$

::: remark
This is just a condition that $S^3\setminus{E}$ is hyperbolic. To make the metric complete we need to add the condition that the upper side and the lower side of the parallelogram in Figure [1](#fig:torus){reference-type="ref" reference="fig:torus"} are parallel.
:::

Now we introduce parameters $x$ and $y$ as $$\label{eq:xyzw}
\begin{split}
  x&:=w(1-z),
  \\
  y&:=-zw.
\end{split}$$ Note that the following equality holds from [\[eq:hyperbolicity\]](#eq:hyperbolicity){reference-type="eqref" reference="eq:hyperbolicity"}: $$\label{eq:xy}
  y+y^{-1}=x+x^{-1}-1.$$

Since $\Delta(z)$ and $\Delta(w)$ can also be parametrized as $\Delta(1-1/z)$ and $\Delta(1-1/w)$, we have $$\begin{gathered}
  \operatorname{Vol}(\Delta(z))+\operatorname{Vol}(\Delta(w))
  \\
  =
  \operatorname{Im}\operatorname{Li}_2(w')+\operatorname{Im}\operatorname{Li}_2(z')+\log|w'|\arg(1-w')+\log|z'|\arg(1-z'),
\end{gathered}$$ from [\[eq:tetra_vol\]](#eq:tetra_vol){reference-type="eqref" reference="eq:tetra_vol"}, where we put $z':=1-1/z$ and $w':=1-1/w$. Using the equation $$\operatorname{Li}_2(z')+\operatorname{Li}_2({z'}^{-1})
  =
  -\frac{\pi^2}{6}-\frac{1}{2}\bigl(\log(-z')\bigr)^2$$ (see for example [@Zagier:2007 § 1.2]), we have $$\label{eq:Vol_H1}
\begin{split}
  &\operatorname{Vol}(\Delta(z))+\operatorname{Vol}(\Delta(w))
  \\
  =&
  \operatorname{Im}\operatorname{Li}_2(w')-\operatorname{Im}\operatorname{Li}_2({z'}^{-1})
  +\log|w'|\arg(1-w')-\log|{z'}^{-1}|\arg(1-{z'}^{-1})
  \\
  &\text{(since $w'=1/(yx)$ and ${z'}^{-1}=y/x$)}
  \\
  =&
  \operatorname{Im}\operatorname{Li}_2(1/(yx))-\operatorname{Im}\operatorname{Li}_2(y/x)
  +\log|1/(yx)|\arg(1-1/(yx))-\log|y/x|\arg(1-y/x)
  \\
  &\text{(from \eqref{eq:xy})}
  \\
  =&
  \operatorname{Im}\operatorname{Li}_2(1/(yx))-\operatorname{Im}\operatorname{Li}_2(y/x)
  +\log|y|\arg{x}+\log|x|\arg\frac{1-y/x}{1-1/(yx)}
  \\
  &\text{(from \eqref{eq:xyzw} and \eqref{eq:hyperbolicity})}
  \\
  =&
  \operatorname{Im}\operatorname{Li}_2(1/(yx))-\operatorname{Im}\operatorname{Li}_2(y/x)
  +\log|y|\arg{x}+\log|x|\arg\frac{y}{z(z-1)}
  \\
  &\text{(from \eqref{eq:H})}
  \\
  =&
  \operatorname{Im}H(y,x)-\log|x|\arg(z(z-1)).
\end{split}$$

Putting $$\begin{aligned}
  u&:=\log{x}=\log(w(1-z)),
  \\
  v&:=2\log(z(1-z)),
  \\
  H(u)&:=H(y,x),
\end{aligned}$$ we have $$\label{eq:Vol_H2}
  \operatorname{Vol}(\Delta(z))+\operatorname{Vol}(\Delta(w))
  =
  \operatorname{Im}H(u)-\pi\operatorname{Re}{u}-\frac{1}{2}\operatorname{Re}{u}\operatorname{Im}{v}.$$ Moreover from [\[eq:GVC_limit\]](#eq:GVC_limit){reference-type="eqref" reference="eq:GVC_limit"}, we have $$(u+2\pi\sqrt{-1})
  \lim_{N\to\infty}
  \frac{\log{J_N\bigl(E;\exp((u+2\pi\sqrt{-1})/N)\bigr)}}{N}
  =
  H(u)$$ if we put $\theta=u+2\pi\sqrt{-1}$ since $x=\exp(u)=\exp(\theta)$. Note that $z$, $w$, $x$, $y$ and $v$ are functions of $u$. Note also that $v$ is given as $$v
  =
  2\frac{d\,H(u)}{d\,u}-2\pi\sqrt{-1}$$ since $\dfrac{d\,H(u)}{d\,u}=\log(z(z-1))$.

::: remark
We need to be more careful about the arguments of variables. For details see [@Murakami/Yokota:JREIA2007].
:::

I will give geometrical interpretation of $u$ and $v$ to relate the term $\operatorname{Re}{u}\operatorname{Im}{v}$ in [\[eq:Vol_H2\]](#eq:Vol_H2){reference-type="eqref" reference="eq:Vol_H2"} to the length of $\gamma_u$.

We first calculate $H_1(S^3\setminus{E})=H_1(\Delta(z)\cup\Delta(w))$. Since the interiors of three-simplices do not matter to the first homology, we can calculate it from the boundary torus, the edges of $\Delta(z)$ and $\Delta(w)$, and the faces $A=A'$, $B=B'$, $C=C'$, and $D=D'$ (see Figures [\[fig:fig8_tetra\]](#fig:fig8_tetra){reference-type="ref" reference="fig:fig8_tetra"} and [1](#fig:torus){reference-type="ref" reference="fig:torus"}). From Figures [\[fig:fig8_tetra\]](#fig:fig8_tetra){reference-type="ref" reference="fig:fig8_tetra"}, [1](#fig:torus){reference-type="ref" reference="fig:torus"} and [2](#fig:torus_edge){reference-type="ref" reference="fig:torus_edge"} one reads $$\begin{aligned}
  \partial A=\partial A'
  &=
   \raisebox{-1mm}{\rotatebox{45}{$\rightarrow$}}-e_{7}
  +\raisebox{-1mm}{\rotatebox{45}{$\twoheadrightarrow$}}+e_{10}
  -\raisebox{-1mm}{\rotatebox{45}{$\twoheadrightarrow$}}-e_{5},
  \\
  \partial B=\partial B'
  &=
  -\raisebox{-1mm}{\rotatebox{45}{$\rightarrow$}}-e_{11}
  -\raisebox{-1mm}{\rotatebox{45}{$\twoheadrightarrow$}}+e_{6}
  +\raisebox{-1mm}{\rotatebox{45}{$\twoheadrightarrow$}}-e_{9},
  \\
  \partial C=\partial C'
  &=
   \raisebox{-1mm}{\rotatebox{45}{$\twoheadrightarrow$}}+e_{4}
  +\raisebox{-1mm}{\rotatebox{45}{$\rightarrow$}}+e_{8}
  -\raisebox{-1mm}{\rotatebox{45}{$\rightarrow$}}+e_{1},
  \\
  \partial D=\partial D'
  &=
   \raisebox{-1mm}{\rotatebox{45}{$\rightarrow$}}+e_{3}
  -\raisebox{-1mm}{\rotatebox{45}{$\twoheadrightarrow$}}+e_{2}
  -\raisebox{-1mm}{\rotatebox{45}{$\rightarrow$}}+e_{12},
\end{aligned}$$ where and mean the single arrowed edge and the double arrowed edge in Figure [\[fig:fig8_tetra\]](#fig:fig8_tetra){reference-type="ref" reference="fig:fig8_tetra"} respectively, and the $e_i$ are the edges of the boundary torus as indicated in Figure [2](#fig:torus_edge){reference-type="ref" reference="fig:torus_edge"}. Since $$\begin{aligned}
  e_{7}&=e_{6}+e_{2},
  \\
  e_{10}&=e_{6},
  \\
  e_{5}&=e_{1}+e_{6},
  \\
  e_{11}&=e_{4}+e_{12}=e_{4}+e_{6},
  \\
  e_{9}&=e_{3}+e_{10}=e_{3}+e_{6},
  \\
  e_{8}&=e_{6},
  \\
  e_{12}&=e_{6}
\end{aligned}$$ in the first homology group, we have $$\begin{aligned}
  \raisebox{-1mm}{\rotatebox{45}{$\rightarrow$}}-e_1-e_2-e_6&=0,
  \\
  -\raisebox{-1mm}{\rotatebox{45}{$\rightarrow$}}-e_3-e_4-e_6&=0,
  \\
  \raisebox{-1mm}{\rotatebox{45}{$\twoheadrightarrow$}}+e_1+e_4+e_6&=0,
  \\
  -\raisebox{-1mm}{\rotatebox{45}{$\twoheadrightarrow$}}+e_2+e_3+e_6&=0.
\end{aligned}$$ So if we put $\mu:=e_6$, $\lambda:=e_1+e_2+e_3+e_4+2\mu$, then we see that the first homology group of the boundary torus is generated by $\mu$ and $\lambda$, that $H_1(S^3\setminus{E})\cong\mathbb{Z}$ is generated by $\mu$, and that $\lambda=0$ in $H_1(S^3\setminus{E})$. Therefore $\mu$ is the meridian and $\lambda$ is the longitude.

![The cycle $e_6$ is the meridian and the cycle $e_1+e_6+e_2+e_8+e_3+e_4$ is the longitude.](torus_edge_small.eps){#fig:torus_edge}

Now let us consider the universal cover $\widetilde{S^3\setminus{E}}$ of $S^3\setminus{E}=\Delta(z)\cup\Delta(w)$ which is $\mathbb{H}^3$. We can construct it by developing $\Delta(z)$ and $\Delta(w)$ isometrically in $\mathbb{H}^3$. Then each loop in $S^3\setminus{E}$ is regarded as a covering translation of $\widetilde{S^3\setminus{E}}$ and it defines an isometric translation of $\mathbb{H}^3$. This defines a representation (holonomy representation) of $\pi_1\bigl(S^3\setminus{E})$ at $PSL(2;\mathbb{C})$. Taking a lift to $SL(2;\mathbb{C})$, we can define a representation $\rho\colon\pi_1\bigl(S^3\setminus{E})\to SL(2;\mathbb{C})$.

We consider how $\rho(\mu)$ and $\rho(\lambda)$ act on $\partial\mathbb{H}^3=S^2=\mathbb{C}\cup\{\infty\}$. The image of the meridian $\rho(\mu)$ sends the top side to the bottom side. So it is the composition of a $-\alpha$-rotation around the circle with $+$ in the top (between $e_1$ and $e_2$) and a $\gamma'$-rotation around the single circle in the bottom (between $e_2$ and $e_3$), which means a multiplication by $1/z\times1/(1-w))=w(1-z)$ plus a translation from [\[eq:hyperbolicity\]](#eq:hyperbolicity){reference-type="eqref" reference="eq:hyperbolicity"}. Similarly $\rho(\lambda)$ acts as a multiplication by $z^2(1-z)^2$ plus a translation.

Therefore $u=\log(w(1-z))$ and $v=2\log(z(1-z))$ can be regarded as the logarithms of the actions by the meridian $\mu$ and the longitude $\lambda$, respectively.

Since the meridian and the longitude commute in $\pi_1(S^3\setminus{E})$, their images can be simultaneously triangularizable. Recalling that $\mu$ and $\lambda$ define multiplications by $\exp(u)$ and $\exp(v)$ plus translations on $\partial\mathbb{H}^3$, we may assume $$\begin{aligned}
  \rho(\mu)
  &=
  \begin{pmatrix}
    \exp(u/2)&\ast \\
    0        &\exp(-u/2)
  \end{pmatrix},
  \\
  \rho(\lambda)
  &=
  \begin{pmatrix}
    \exp(v/2)&\ast \\
    0        &\exp(-v/2)
  \end{pmatrix},
\end{aligned}$$ which is [\[eq:meridian_longitude\]](#eq:meridian_longitude){reference-type="eqref" reference="eq:meridian_longitude"}. This is a geometric interpretation of $u$ and $v$.

Since $u$ determines $z$ and $w$, it defines a hyperbolic structure of $S^3\setminus{E}$ as the union of $\Delta(z)$ and $\Delta(w)$. When $u\ne0$ this hyperbolic structure is incomplete. We can complete this incomplete structure by attaching either a point or a circle.

Since $v$ is not a real multiple of $u$ when $u$ is small, there exists a pair $(p,q)\in\mathbb{R}^2$ such that $pu+qv=2\pi\sqrt{-1}$. The pair $(p,q)$ is called the generalized Dehn surgery coefficient [@Thurston:GT3M]. If $p$ and $q$ are coprime integers, then the completion is given by attaching a circle $\gamma_{u}$ and the result is a closed hyperbolic three-manifold which we denote by $E_u$. (For other cases the completion is given by adding either a point or a circle. In the former case the regular neighborhood of the attached point is a cone over a torus, and in the latter case the regular neighborhood of the attached circle is topologically a solid torus but geometrically the angle around the core is not $2\pi$.)

If $p$ and $q$ are coprime integers, the completion is nothing but the $(p,q)$-Dehn surgery along the knot, that is, we attach a solid torus $D$ to $S^3\setminus\operatorname{Int}(N(E))$ so that the meridian of $D$ coincides with the loop on the boundary of the regular neighborhood $N(E)$ of $E\subset S^3$ presenting $p\mu+q\lambda\in H_1(S^3\setminus\operatorname{Int}(N(E)))$, where $\operatorname{Int}$ denotes the interior (Figure [3](#fig:Dehn_surgery){reference-type="ref" reference="fig:Dehn_surgery"}).

![$(2,1)$-Dehn surgery along the figure-eight knot](fig8_surgery1_small.eps){#fig:Dehn_surgery}

Then the circle $\gamma_u$ can be regarded as the core of $D$.

To complete the proof of Theorem [\[thm:MY\]](#thm:MY){reference-type="ref" reference="thm:MY"}, we want to describe the length of the attached circle $\gamma_u$ in terms of $u$ and $v$. We will show $$\label{eq:length}
  \operatorname{length}{\gamma}_{u}
  =
  -\frac{1}{2\pi}\operatorname{Im}\left(u\overline{v}\right).$$

When $u$ is small and non-zero, we can assume that $\exp(u)\ne1$ and $\exp(v)\ne1$. So we can also assume that $\rho(\mu)$ and $\rho(\lambda)$ are both diagonal. This means that the image of $\mu$ is a multiplication by $\exp(u)$ and that the image of $\lambda$ is a multiplication by $\exp(v)$ (with no translations). Note that now $\widetilde{S^3\setminus{E}}$ is identified with $\mathbb{H}^3$ minus the $z$-axis, and the completion is given by adding the $z$-axis.

Since $p$ and $q$ are coprime, we can choose integers $r$ and $s$ so that $ps-qr=1$. We push $\gamma_u\in D$ to the boundary of the solid torus $\partial D$ and denote the resulting circle by $\tilde{\gamma}_u$. Then we see that $[\tilde{\gamma}_u]=r\mu+s\lambda\in H_1(\partial(S^3\setminus\operatorname{Int}(N(E)));\mathbb{Z})$ since the meridian of $D$ is identified with $p\mu+q\lambda$, and the images of the meridian and $\tilde{\gamma}_u$ make a basis of $H_1(\partial(S^3\setminus\operatorname{Int}(N(E)));\mathbb{Z})$.

::: remark
Even if we use another pair $(r',s')$ such that $ps'-qr'=1$, we get the same manifold. This is because changing $(r,s)$ corresponds to changing of $\tilde{\gamma}_u\in\partial D$. Observe that ambiguity of the choice of $\tilde{\gamma}_u$ is given by a twist of $D$ and that it does not matter to the resulting manifold.
:::

Therefore $\rho(\gamma_u)$ corresponds to a multiplication by $\exp(\pm(ru+sv))$. This means that if we identify the completion of $\widetilde{S^3\setminus{E}}$ with $\mathbb{H}^3$, a fundamental domain of the lift of $\gamma_u$ is identified with the segment $[1,\exp\bigl(\pm\operatorname{Re}(ru+sv)\bigr)]$ in the $z$-axis. Since the metric is given by $\sqrt{dx^2+dy^2+dz^2}/z$, the length of $\gamma_u$ is given by $$\begin{split}
  \operatorname{length}(\gamma_u)
  &=
  \int_{1}^{\exp\bigl(\pm\operatorname{Re}(ru+sv)\bigr)}\frac{dz}{z}
  \\
  &=
  \pm\operatorname{Re}(ru+sv)
  \\
  &=
  \pm\left(\frac{ps-1}{q}\operatorname{Re}(u)+s\operatorname{Re}(v)\right)
  \\
  &=
  \pm\left(\frac{s}{q}(p\operatorname{Re}(u)+q\operatorname{Re}(v))-\frac{1}{q}\operatorname{Re}(u)\right)
  \\
  &=
  \mp\frac{\operatorname{Re}(u)}{q}
  \\
  &=
  \frac{\mp1}{2\pi}\left(\operatorname{Re}{u}\operatorname{Im}{v}-\operatorname{Im}{u}\operatorname{Re}{v}\right)
  \\
  &=
  \frac{\pm1}{2\pi}\operatorname{Im}(u\overline{v}),
\end{split}$$ where the fourth and the sixth equalities follow from $$\begin{pmatrix}
    \operatorname{Re}(u)&\operatorname{Re}(v) \\
    \operatorname{Im}(u)&\operatorname{Im}(v)
  \end{pmatrix}
  \begin{pmatrix}
    p\\q
  \end{pmatrix}
  =
  \begin{pmatrix}
    0\\2\pi
  \end{pmatrix}.$$ Since $v=u\times\dfrac{|v|^2}{u\overline{v}}$ and the orientation of $(u,v)$ should be positive on $\mathbb{C}$, we see that $\operatorname{Im}(u\overline{v})$ is negative (see [@Neumann/Zagier:TOPOL85] for details) and so [\[eq:length\]](#eq:length){reference-type="eqref" reference="eq:length"} follows.

Therefore from [\[eq:Vol_H2\]](#eq:Vol_H2){reference-type="eqref" reference="eq:Vol_H2"} we finally have $$\operatorname{Vol}(E_u)
  =
  \operatorname{Re}
  \left(
    -\sqrt{-1}H(u)
    -\pi u
    +\frac{1}{4}uv\sqrt{-1}
    -\frac{\pi}{2}\kappa(\gamma_u)
  \right).$$

The Chern--Simons invariant is obtained by Yoshida's formula [@Yoshida:INVEM85]. See [@Murakami/Yokota:JREIA2007] for details.

### General knots

Here I propose a generalization of the Volume Conjecture for general knots.

::: conjecture
[]{#conj:PVC label="conj:PVC"} For any knot $K$, there exists an open set $U\in\mathbb{C}$ such that if $u\in U$, then the following limit exists: $$\lim_{N\to\infty}
  \frac{\log J_N(K;\exp\bigl((u+2\pi\sqrt{-1})/N\bigr))}{N}.$$ Moreover if we put $$\begin{aligned}
  H(K;u)&:=(u+2\pi\sqrt{-1})\times(\text{the limit above}),
  \\
  \intertext{and}
  v&:=2\dfrac{d\,H(K;u)}{d\,u}-2\pi\sqrt{-1},
\end{aligned}$$ then we have $$\operatorname{Vol}(K;u)
  =
  \operatorname{Im}{H(K;u)}
  -\pi\operatorname{Re}{u}
  -\frac{1}{2}\operatorname{Re}{u}\operatorname{Im}{v}.$$ Here $\operatorname{Vol}(K;u)$ is the volume function corresponding to the representation of $\pi_1(S^3\setminus{K})$ to $SL(2;\mathbb{C})$ as in Theorem $\ref{thm:MY}$.
:::

::: remark
In the case of a hyperbolic knot, we can also propose a similar conjecture with the imaginary part as in the case of the figure-eight knot. For a general knot, a relation to the Chern--Simons invariant is also expected by using a combinatorial description of the Chern--Simons invariant by Zickert [@Zickert:DUKMJ2009].
:::

::: remark
Conjecture [\[conj:PVC\]](#conj:PVC){reference-type="ref" reference="conj:PVC"} is known to be true for the figure-eight knot [@Murakami/Yokota:JREIA2007] and for torus knots [@Murakami:ADVAM22007]. See also [@Murakami:ACTMV2008] and [@Hikami/Murakami:Bonn] for a possible relation to the Chern--Simons invariant.
:::

Finally note that Garoufalidis and Lê proved the following result, which should be compared with Conjecture [\[conj:PVC\]](#conj:PVC){reference-type="ref" reference="conj:PVC"}. (See also [@Murakami:JPJGT2007] for the case of the figure-eight knot.)

::: theorem
For any $K$, there exists $\varepsilon>0$ such that if $|\theta|<\varepsilon$, we have $$\lim_{N\to\infty}
  J_N(K;\exp(\theta/N))
  =
  \frac{1}{\Delta(K;\exp{\theta})},$$ where $\Delta(K;t)$ is the Alexander polynomial of $K$.
:::
