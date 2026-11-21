---
doc_id: arxiv-math-0305275v1
doc_title: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds"
section_id: sec-003-volume-of-representations
section_title: "Volume of representations"
section_number: null
pages: 9-15
source_pdf: 0305275v1.pdf
source_sha256: 9b356a9d716a0d3e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.99
doc_brief: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds — Let W be a compact manifold and let ρ be a representation of its fundamental group into PSL(2, C)."
---
[]{#s 3 label="s 3"}

For this section we fix an ideally triangulated manifold $M$ and a representation $\rho:\pi_1(M)\to{\rm Isom}^+(\ensuremath{\mathbb H}^3)$.

In this section we recall the notion of volume of an equivariant map from $\widetilde{M}$ to $\ensuremath{\mathbb H}^3$. We prove that if we restrict to the class of pseudo-developing maps, then the volume of $\rho$ is well-defined. Namely the volume does not depend neither on the pseudo-developing map nor on the product structure of the cusps. Such a volume can be calculated using a straightening of any pseudo-developing map and it is exactly the algebraic sum of the volumes of the straightened tetrahedra.

::: defitit
Volume of pseudo-developing map[]{#d vdr label="d vdr"} Let $D_\rho$ be a pseudo-developing map for $\rho$. Let $\omega$ be the volume form of $\ensuremath{\mathbb H}^3$ and let $D_\rho^*\omega$ be the pull-back of $\omega$. Since $D_\rho$ is equivariant, then $D_\rho^*\omega$ projects to a $3$-form, that we still call $D_\rho^*\omega$, on $M$. The volume ${\rm vol}(D_\rho)$ of $D_\rho$ is defined by: $${\rm vol}(D_\rho)=\int_M D_\rho^*\omega.$$
:::

::: remark
We will see below that for pseudo-developing maps the volume is always finite. The same definition of volume does not work for any equivariant map from $\widetilde{M}$ to $\ensuremath{\mathbb H}^3$ because if the pull-back of the volume form is not in $L^1$, then the volume is not well-defined.
:::

::: defitit
Straight volume[]{#d strvol label="d strvol"} Let $D_\rho$ be a pseudo developing map for $\rho$. Let $\{\Delta_i\}$ be the set of the tetrahedra of the ideal triangulation of $M$ and $\{\ensuremath{\widetilde{\Delta}}_i\}$ be a set of lifts of the $\Delta_i's$. Let $v_i=0$ if ${\rm Str}(\ensuremath{\widetilde{\Delta}}_i)$ is a degenerate tetrahedron, and let $v_i$ be the algebraic volume of ${\rm Str}(\ensuremath{\widetilde{\Delta}}_i)$ otherwise.

We define the straight volume of $(D_\rho)$ as ${\rm Strvol}(D_\rho)=\sum_i v_i$.
:::

::: remark
Let $\Delta_1,\dots,\Delta_n$ be the tetrahedra of $\tau$. Let ${\bf z}=(z_1,\dots,z_n)\in\{\ensuremath{\mathbb C}\setminus\{0,1\}\}^n$ be a solution of Thurston's hyperbolicity equations (see [@BP], [@F3], [@NZ], [@PP], [@PW], [@Th1]). Then there exists a developing map $D_{\bf z}:\ensuremath{\widetilde{M}}\to \ensuremath{\mathbb H}^3$ for **z** that is a pseudo-developing map for some holonomy $\rho({\bf z})$. Such a map is already straight and we have ${\rm Strvol}(D_{\bf z})={\rm vol}(D_{\bf z})=\sum v_i={\rm vol}({\bf z})$, where $v_i$ is the volume of the geodesic ideal tetrahedron of modulus $z_i$.
:::

Let $C_p=T_p\times[0,\infty]/_\sim$ be a cusp of $M$ and let $N_{\ensuremath{\widetilde{p}}}=P_{\ensuremath{\widetilde{p}}}\times [0,\infty]/_\sim$ be one of its lifts in $\widetilde{M}$. Then we can identify $\pi_1(C_p)$ with ${\rm Stab}(\ensuremath{\widetilde{p}})$. Let $f:P_{\ensuremath{\widetilde{p}}}\times\{0\} \to \ensuremath{\mathbb H}^3$ be a ${\rm Stab}(\ensuremath{\widetilde{p}})$-equivariant map, let $\xi\in\partial\ensuremath{\mathbb H}^3$ be a fixed point of $\rho({\rm Stab}(\ensuremath{\widetilde{p}}))$ and let $F:N_{\ensuremath{\widetilde{p}}}:\to\overline{\ensuremath{\mathbb H}}^3$ be the cone-map obtained by coning $f$ to $\xi$. As above, let $F^*\omega$ be the pull-back of the volume-form on $C_p$. Similarly we can pull-back the metric. We call $A^p_t$ the area of the torus $T_p\times\{t\}$.

::: lemma
[]{#l at label="l at"} In the previous setting, for $t>r$ we have: $$A^p_t\leq A^p_r e^{-(t-r)}\qquad \textrm{ and } \qquad \int_{T_p\times
  [t,\infty)} |F^*\omega|\leq A^p_t.$$
:::

  Let $(x,y)$ be local coordinates on $P_{\ensuremath{\widetilde{p}}}$. Choose the half-space model $\ensuremath{\mathbb C}\times \ensuremath{\mathbb R}^+$ of $\ensuremath{\mathbb H}^3$ and assume that $\xi=\infty$. In such a model the hyperbolic metric at the point $(z,s)$ is the Euclidean one rescaled by the factor $1/s$. It follows that, called $\alpha+i\beta$ and $h$ the complex and real components of $F$, we have $$\alpha(x,y,t)+i\beta(x,y,t)=\alpha(x,y,r)+i\beta(x,y,r) 
\qquad h(x,y,t)=h(x,y,r)e^{(t-r)}.$$

The element of area at level $t$ is $d\sigma_t(x,y)=\sqrt{\det(^TJF_t\cdot H\cdot 
  JF_t)}$, where $F_t$ is the restriction of $F$ to $P_{\ensuremath{\widetilde{p}}}\times\{t\}$ and $H(x,y,t)=\frac{1}{h^2}{\rm Id}$ is the matrix of the hyperbolic metric. From direct calculations it follows that $d\sigma_t(x,y)\leq d\sigma_r(x,y)e^{-t+r}$ and the first inequality follows.

Now note that the volume element $|F^*\omega|$ at the point $(x,y,t)\in
C_p$ is bounded by the area element of the torus $T_p\times\{t\}$ multiplied by the length element of the ray $\{(x,y)\}\times[0,\infty]$. Since the parameter $t$ is exactly the arc-length, then the length element is exactly $dt$. It follows that $$\int_{T_p\times[t,\infty)}|F^*\omega|\leq\int_t^\infty
A^p_sds\leq\int_t^\infty A^p_t e^{-(s-t)}ds=A^p_t.$$ This completes the proof.\

::: remark
From Lemma [\[l at\]](#l at){reference-type="ref" reference="l at"} it follows in particular that $\int_{T_p\times [t,\infty)} |F^*\omega|\leq A^p_0e^{-t}$. This means that we have an estimate of $\int_{T_p\times [0,\infty)} |F^*\omega|$ not depending on the point $\xi=F(p)$ but only on the area of $T_p\times\{0\}$.
:::

::: remark
From Lemma [\[l at\]](#l at){reference-type="ref" reference="l at"} it follows that ${\rm vol}(D_\rho)$ is finite for any pseudo-developing map $D_\rho$.
:::

The following lemma is proved in [@D].

::: lemma
[]{#l f1 label="l f1"} If $D_\rho$ and $F_\rho$ are two pseudo-developing maps for $\rho$ that agree on the ideal points, then ${\rm vol}(D_\rho)={\rm vol}(F_\rho)$.
:::

This is because any two pseudo-developing maps are equivariantly homotopic. The fact that they coincide on the ideal points allows one to construct a homotopy $h$ that respects the cone structures of the cusps. Namely, for each ideal point $\widetilde{p}$ of $\widetilde{M}$ we choose any equivariant homotopy between the restrictions of $D_\rho$ and $F_\rho$ to $P_{\ensuremath{\widetilde{p}}}\times\{\bar t\}$, where $\bar t=$ max$\{t_{D_\rho},t_{F_\rho}\}$, we cone such a homotopy to $D_\rho(\ensuremath{\widetilde{p}})$ along geodesic rays, and we extend the homotopy outside the cusps in any equivariant way. For such a homotopy $h$ we can use the Stokes theorem on $M\times[0,1]$ for $h^*\omega$ to obtain the thesis. More precisely, let $K_t$ be $M\setminus\cup_p
(T_p\times(t,\infty))$, where $p$ varies on the set of the ideal points; then we have $$\label{e 1}0=\int_{K_t\times[0,1]}d(h^*\omega)=
\int_{\partial(K_t\times[0,1])}h^*\omega= \int_{K_t}
(D_\rho^*\omega-F_\rho^*\omega) + \int_{\partial K_t\times[0,1]}
h^*\omega$$ and, as in Lemma [\[l at\]](#l at){reference-type="ref" reference="l at"}, we can prove that the last integral goes to zero as $t\to \infty$.

We now prove that the claim of Lemma [\[l f1\]](#l f1){reference-type="ref" reference="l f1"} is true in general.

::: teo
[]{#t vndpd label="t vndpd"} Let $D_\rho$ and $F_\rho$ be two pseudo-developing maps for $\rho$. Then ${\rm vol}(D_\rho)={\rm vol}(F_\rho)$.
:::

 For $t\in[0,\infty)$, let $D_\rho^t$ be the map constructed as follows: $D_\rho^t$ coincides with $D_\rho$ until the level $t$ of each cusp. Then for each cusp $N_p$ we complete $D_\rho^t$ by coning $D|_{P_p\times\{t\}}$ to $F_\rho(p)$ along geodesic rays in such a way that the arc-length is the parameter $s-t$, where $s\in[t,\infty)$. Now, $D^t_\rho$ is a pseudo-developing map that agrees with $F_\rho$ on the ideal points. Thus by Lemma [\[l f1\]](#l f1){reference-type="ref" reference="l f1"} ${\rm vol}(D^t_\rho)={\rm vol}(F_\rho)$. Since $D^t_\rho$ and $D_\rho$ agree outside the cusps and where they differ they are cones on the same basis (and different vertices), from Lemma [\[l at\]](#l at){reference-type="ref" reference="l at"} we get $$|{\rm vol}(D_\rho)-{\rm vol}(D_\rho^t)|\leq 2\sum_p
A_t^p\leq2(\sum_p A_0^p)e^{-t}$$ where $p$ varies on the set of ideal points and $A^p_t$ is the area of the torus $T_p\times\{t\}$. As $t\to \infty$ we get the thesis.\

Similar techniques actually allow to prove the following theorem.

::: teo
[]{#t vsd label="t vsd"} For any pseudo-developing map $D_\rho$ for $\rho$ we have ${\rm vol}(D_\rho)=$ ${\rm Strvol}(D_\rho)$.
:::

Before proving Theorem [\[t vsd\]](#t vsd){reference-type="ref" reference="t vsd"}, we give the following definition.

::: defi
[]{#d cvxc label="d cvxc"} Let $f,g$ be two maps from a set $X$ respectively to $\ensuremath{\mathbb H}^n$ and $\overline{\ensuremath{\mathbb H}}^n$. For $t\in[0,\infty]$ the convex combination $\Phi_t$ from $f$ to $g$ is defined by: $$\Phi_t(x)=\left\{\begin{array}{lcl}
\gamma_x(t) &\ & t\leq{\rm dist}(f(x),g(x))\\
g(x)&\ &t\geq {\rm dist}(f(x),g(x))
\end{array}\right.$$ where $\gamma_x$ is the geodesic from $f(x)$ and $g(x)$, parametrized by arc-length.
:::

::: remark
In Definition [\[d cvxc\]](#d cvxc){reference-type="ref" reference="d cvxc"}, if $X$ is a topological space and $f$ and $g$ are continuous, then the convex combination from $f$ to $g$ is continuous on $X\times[0,\infty]$ because the function ${\rm dist}(f(x),g(x))$ is well-defined and continuous from $X$ to $[0,\infty]$.
:::

For the proof assume that $t_{D_\rho}=0$. We start by fixing a suitable homotopy $h$ between $D_\rho$ and ${\rm Str}(D_\rho)$. Define $h:\ensuremath{\widetilde{M}}\times [0,\infty]\to \ensuremath{\mathbb H}^3$ outside the cusps to be the convex combination from $D_\rho$ to ${\rm Str}(D_\rho)$ and then for each cusp $N_{\ensuremath{\widetilde{p}}}$ extend $h$ by coning $h((x,0),s)$ to $D_\rho(\ensuremath{\widetilde{p}})$ along geodesic rays in such a way that the parameter $t\in[0,\infty)$ of the cusp is the arc-length. Let $D_s(x)=h(x,s)$. By Lemma [\[l f1\]](#l f1){reference-type="ref" reference="l f1"} we have that $$\int_MD_\rho^*\omega=\int_MD_s^*\omega\qquad\textrm{ for } s\in(0,\infty).$$ So we only have to prove that $\int_MD_s^*\omega\to
{\rm Strvol}(D_\rho)$ as $s\to \infty$. Clearly, it suffices to prove that for any tetrahedron $\Delta$ we have $\int_\Delta D_s^*\omega\to v$ where $v$ is the volume of ${\rm Str}(\Delta)$. If $\Delta$ does not collapse in the straightening, then the distance from $D_\rho$ and ${\rm Str}(D_\rho)$ is bounded outside the cusps and so $D_s={\rm Str}(D_\rho)$ for $s>>0$; since ${\rm Str}(D_\rho)$ is a homeomorphism on $\Delta$, then $\int_\Delta D_s^*\omega$ is exactly the volume of the straight version of $\Delta$.

If $\Delta$ collapses in the straightening, then we have to show that $\int_\Delta D_s^*\omega\to 0$. This follows from direct calculations. We give only the lead-line of them because they are involved but use elementary techniques. Moreover, in the next section, we will give an alternative proof of this theorem (see Theorem [\[t sv\]](#t sv){reference-type="ref" reference="t sv"} and Remark [\[r difp\]](#r difp){reference-type="ref" reference="r difp"}).

Given the convex combination $\Phi_t$ from a map $f$ to a map $g$, it is possible to calculate the Jacobian of $\Phi_t$ as a function of the derivatives of $f$ and $g$, the time $t$ and the distance between $f$ and $g$. This is not completely trivial, for example think of a tetrahedron as a convex combination of two segments: the segments have zero area but in the middle we have quadrilaterals with non-zero area. Using these calculations, we can estimate $|D^*_s\omega|$ outside the cusps, showing that its integral goes to zero as $s$ goes to infinity. Looking inside the cusps, by Lemma [\[l at\]](#l at){reference-type="ref" reference="l at"} we reduce the estimate to the same estimate as above, made with 2-dimensional objects (the bases of the cusps).\

::: remark
Since ${\rm vol}(D_\rho)={\rm Strvol}(D_\rho)$ it follows that such a volume does not depend on the chosen cone structure of the cusps. Moreover, by Theorem [\[t vndpd\]](#t vndpd){reference-type="ref" reference="t vndpd"}, ${\rm vol}(D_\rho)$ does not depend on the developing map, but only on $\rho$. This allows us to give the following definition.
:::

::: defi
The volume ${\rm vol}(\rho)$ of $\rho$ is the volume of any pseudo-developing map for $\rho$.
:::

As the following corollary shows, for hyperbolic manifolds the volume of the holonomy is exactly the hyperbolic volume.

::: cor
[]{#c nat label="c nat"} Let $M$ be a complete hyperbolic manifold of finite volume. If $\rho$ is the holonomy of the hyperbolic structure then ${\rm vol}(\rho)=$ ${\rm vol}(M)$.
:::

  Consider $\ensuremath{\mathbb H}^3$ as the universal cover of $M$ and choose the arc length as the cone parameter of the cusps. Clearly the identity of $\ensuremath{\mathbb H}^3$ is a pseudo-developing map for $\rho$. Obviously we have $\int_M {\rm Id}^*(\omega)=$ ${\rm vol}(M)$.\

::: cor
Let $z_i$ be the modulus induced by a pseudo-developing map $D_\rho$ on the i$^{th}$ tetrahedron and let $v_i$ be the volume of a hyperbolic ideal geodesic tetrahedron of modulus $z_i$. Then we have ${\rm vol}(\rho)=\sum v_i$.
:::

::: remark
Even if $\sum v_i$ depends only on $\rho$, the moduli $z_i$ induced by a pseudo-developing map $D_\rho$ actually can depend on $D_\rho$. Namely, any ideal point $p$ is mapped to a fixed point of $\rho($Stab$(p))$ and, if this is not a parabolic group, we have more than one possibility for $D_\rho(p)$. Conversely, if each $\rho($Stab$(p))$ is a non-trivial parabolic group, then by Remark [\[r pip\]](#r pip){reference-type="ref" reference="r pip"} it follows that the moduli $z_i$ are uniquely determined by $\rho$.
:::

::: prop
[]{#p pos label="p pos"} Let $g$ be a reflection of $\ensuremath{\mathbb H}^3$ and let $\ensuremath{\overline{\rho}}$ be the representation $g\circ\rho\circ g^{-1}$. Then ${\rm vol}(\ensuremath{\overline{\rho}})=-{\rm vol}(\rho)$.
:::

 If $D_\rho$ is a pseudo-developing map for $\rho$, then $g\circ
D_\rho$ is a pseudo-developing map for $\ensuremath{\overline{\rho}}$ and it is easily checked that ${\rm vol}(g\circ D_\rho)=-{\rm vol}(D_\rho)$.\

We recall here two facts proved in [@D].

::: prop
Suppose that $\rho_t:\pi_1(M)\to{\rm Isom}^+(\ensuremath{\mathbb H}^3)$, $t\in[0,1]$ is a smooth one parameter family of representations. Then ${\rm vol}(\rho_0)={\rm vol}(\rho_1)$.
:::

This can be proved by using the one-parameter family $\rho_t$ to construct a one-parameter family of pseudo-developing maps. Some estimates on the derivative along the $t$-direction of the volume of such maps are needed.

::: prop
[]{#p f2 label="p f2"} Suppose that $\rho$ factors through the fundamental group of a Dehn filling N of M. Then the volume of $\rho$ w.r.t. N coincides with the volume of $\rho$ w.r.t. M.
:::

Theorem [\[t vsd\]](#t vsd){reference-type="ref" reference="t vsd"} extends from ideal to "classical" triangulations, namely to genuine triangulations $\cal T$ of $\overline M$. Consider such a $\cal T$ as a triangulation of $M$ with some simplices at infinity (those in $\partial \overline M$). Given a pseudo-developing map $D_\rho$ for $\rho$, define a straightening of $D_\rho$ relative to $\cal T$, exactly as in Section [\[s due\]](#s due){reference-type="ref" reference="s due"}, by considering the convex hulls of the images of the vertices of $\cal T$. Then, one can give the definition of the straight volume relative to $\cal T$ of a developing map $D_\rho$ exactly as in Definition [\[d strvol\]](#d strvol){reference-type="ref" reference="d strvol"}, with the unique difference that one has to use the tetrahedra of $\cal T$ instead of the ideal tetrahedra of an ideal triangulation of $M$. Call such a volume ${\rm Strvol}^{\ensuremath{\cal T}}(D_\rho)$.

Finally, exactly as in Theorem [\[t vsd\]](#t vsd){reference-type="ref" reference="t vsd"}, one can prove the following fact:

::: prop
[]{#p vsd label="p vsd"} Let $\cal T$ be a triangulation of $\overline M$ and $D_\rho$ be a pseudo-developing map for $\rho$. Then ${\rm vol}(\rho)={\rm Strvol}^{\ensuremath{\cal T}}(D_\rho)$.
:::
