---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-015-7-mahler-volumes-of-every-funk-scale
section_title: "Mahler volumes of every Funk scale"
section_number: 7
pages: 22-26
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.961
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
---
[]{#sec:every_scale label="sec:every_scale"} Define the *Funk-Mahler volume of radius $0<r<\infty$ (around $q\in \mathop{\mathrm{int}}(K)$)* by $$M_r(K,q)=\omega_n r^{-n}\mathop{\mathrm{vol}}_K^F(B_r^F(q, K)), \quad  M_r(K)=\inf_{q\in \mathop{\mathrm{int}}(K)}M_r(K,q).$$

In Euclidean terms, we have $$M_r(K,q)=r^{-n}\int_{z\in q+(1-e^{-r})(K-q)}|K^z|dz,$$ where $K^z$ denotes the dual body with respect to $z$. Evidently, $M_r(K,q)$ is invariant under the full linear group with $q$ at the origin.

::: Lemma
[]{#lem:mahler_convex label="lem:mahler_convex"} For any convex $K$, $M_r(K, q)$ is a strictly convex function of $q$. In particular, if $K=-K$ then $M_r(K)=M_r(K, 0)$.
:::

The function $z\mapsto |K^z|$ is well-known to be strictly convex in $z\in \mathop{\mathrm{int}}(K)$. This follows at once by writing $$|K^z|=\omega_n\int_{S^{n-1}}\max_{x\in K}\langle \theta, x-z\rangle ^{-n}d\sigma(\theta),$$ where $\sigma$ is the rotation-invariant probability measure on $S^{n-1}$, and noticing that for any fixed $x,\theta$, the function $z\mapsto (\langle x,\theta\rangle -\langle z, \theta\rangle)^{-n}$ is strictly convex.

It follows that

$$M_r(K,q)=r^{-n}\int_{(1-e^{-r})K}|K^{e^{-r}q+w}|dw$$ is convex as well.

If $K=-K$ then $M_r(K, q)=M_r(K, -q)$, and so $q=0$ must be a minimum.

The Funk-Mahler volume enjoys invariance under duality, as follows.

::: Proposition
It holds for all $K\subset \mathbb{R}^n$ that $M_r(K, q)=M_r(K^q, q)$. In particular, if $K=-K$ then $M_r(K)=M_r(K^o)$.
:::

We may assume $q=0$. Put $\rho=1-e^{-r}$, so that $B_r^F=\rho K$ is the ball of radius $r$ in the Funk metric, centered at the origin. Then $$M_r(K,0)=\frac{\omega_n}{r^n}\mathop{\mathrm{vol}}_K^F(\rho K)=\frac{\omega_n}{r^n}\mathop{\mathrm{vol}}_{\rho^{-1} K^o}^F(K^o)=M_r(\rho^{-1}K^o,0)=M_r(K^o, 0),$$ where the second equality is due to Corollary [\[cor:dual_volumes\]](#cor:dual_volumes){reference-type="ref" reference="cor:dual_volumes"}, the penultimate equality holds since $K^o$ is the ball of radius $r$ around the origin in the Funk geometry of $\rho^{-1}K^o$, and the last equality is due to $\mathop{\mathrm{GL}}$-invariance.

The second statement now follows by Lemma [\[lem:mahler_convex\]](#lem:mahler_convex){reference-type="ref" reference="lem:mahler_convex"}.

::: Remark
In projective-invariant terms, this duality assumes the following form. For $K\subset\mathbb{P}$, $q\in \mathop{\mathrm{int}}(K)$ and $\eta\in\mathop{\mathrm{int}}(K^\vee)$, let $B^\eta_r(K, q)$ be the outward ball of radius $r$ centered at $q$ in $\mathop{\mathrm{Funk}}_\eta(K)$. Then $B^\eta_r(K, q)\subset \mathop{\mathrm{Funk}}_\eta(K)$ and $B_r^q(K^\vee, \eta)\subset \mathop{\mathrm{Funk}}_q(K^\vee)$ have equal volume.
:::

As $r\to0$, $M_r(K,q)\to M_0(K,q):=|K||K^q|$. Thus the Mahler volume $M_0(K):=\lim_{r\to 0} M_r(K)$ is recovered at infinitesimal scale.

On the opposite end of the scale, the asymptotics of $M_r(K,q)$ is governed by the regularity of the boundary of $K$. When $K$ is smooth and strictly convex, we recover the centro-affine surface area as $r\to\infty$, as established in [@berck_bernig_vernicos]. Recall that the *centro-affine surface area relative to $q\in \mathop{\mathrm{int}}(K)$* is given by

$$\label{eq:centro_affine}\Omega_n(K, q)=\int_{\partial K}\frac{k_p^{\frac 12}}{\langle p-q, \nu_p\rangle^{\frac{n+1}{2}}}d\mu_K(p;q)=\int_{\partial K}\frac{k_p^{\frac 12}}{\langle p-q, \nu_p\rangle^{\frac{n-1}{2}}}d\mathcal H^{n-1}(p),$$ where $k_p$ is the Gaussian curvature of $\partial K$ at $p$, $\nu_p$ the unit outward normal, and $\mu_K(p;q)$ the cone measure with the origin at $q$.

As [@berck_bernig_vernicos] focuses on the Hilbert metric with the Busemann volume, we provide for the sake of completenss the details of the computation in our case.

::: Lemma
[]{#lem:volume_ellipsoid label="lem:volume_ellipsoid"} Let $A$ be a positive-definite $n\times n$ matrix, and $Q_A=\{x\in\mathbb{R}^n:\langle Ax, x\rangle \leq 1\}$. Then for $p\in\partial Q_A$ and $0<\rho <1$, we have $$|Q_A^{\rho p}|=\omega_n\frac{(\det A)^{1/2}}{(1-\rho^2)^{\frac{n+1}{2}}}=\omega_n\frac{1}{(1-\rho^2)^{\frac{n+1}{2}}}\frac{k_p^{1/2}}{\langle p,\nu_p\rangle^{\frac{n+1}{2}}}.$$
:::

For the first equality, we compute that $Q_A^{\rho p}=\{ \xi: \langle B(\xi-c),\xi-c\rangle\leq 1\}$, where, denoting $B_0=A^{-1}-\rho^2pp^T$, we have $$\begin{aligned}
c&=\rho B_0^{-1}p, \qquad B=\frac{B_0}{1+\rho^2\langle B_0^{-1}p,p\rangle}.
\end{aligned}$$ Now by the Sherman-Morrison formula, $$B_0^{-1}=A+\frac{\rho^2}{1-\rho^2}App^TA\Rightarrow  \langle B_0^{-1}p,p\rangle =\frac{1}{1-\rho^2},$$ while by the matrix determinant lemma we h ave $$\det B_0 =(1-\rho^2)\det A^{-1}.$$

It follows that $$|Q_A^{\rho p}|=\omega_n\sqrt{\det B}^{-1}=\omega_n\sqrt{\frac{\det A}{1-\rho^2}}(1-\rho^2)^{-\frac{n}{2}}=\omega_n\frac{\sqrt{\det A}}{(1-\rho^2)^{\frac{n+1}{2}}}$$

For the second equality, recall that $\nu_x=\frac{Ax}{|Ax|}$. It follows that for $v\in T_pQ_A$, $$D_p\nu_x (v)=\frac{Av}{|Ap|}-\langle \frac{Av}{|Ap|}, \nu_p\rangle \nu_p=\frac{1}{|Ap|}\pi_{T_pQ_A}\circ A.$$

Take an orthonormal basis $v_1,\dots, v_{n-1}$ of $T_pQ_A$, and evaluate the volume of $A(v_1\wedge\dots\wedge v_{n-1}\wedge p)$ in two ways. We get $$|A(v_1\wedge\dots\wedge v_{n-1}\wedge p)|=\det A\cdot\langle p, \nu_p\rangle=\det(\pi_{T_pQ_A}\circ A)\cdot|Ap|.$$ Noting also that $\langle p, \nu_p\rangle=\frac{1}{|Ap|}$ since $\langle Ap, p\rangle =1$, we find $\det A=\frac{k_p}{\langle p, \nu_p\rangle^{n+1}}.$

::: Lemma
[]{#lem:dual_volume label="lem:dual_volume"} For $K\in\mathcal K_0(\mathbb{R}^n)$ smooth and strictly convex, and $p\in \partial K$, we have $$|K^{\rho p}|=  (1-\rho)^{-\frac{n+1}{2}}\left(2^{-\frac{n+1}{2}} \omega_n \frac{k_p^{1/2}}{\langle p,\nu_p\rangle^{\frac{n+1}{2}}}+err(p)\right),$$ where $err(p)\to 0$ as $\rho\to 1$, uniformly in $p\in\partial K$.
:::

Throughout the proof, $c,c'$ will be positive constants that are bounded away from $0$ and $\infty$, uniformly in $p\in\partial K$, and may change between occurrences.

As both $|K^{\rho p}|$ and the main term on the right hand side are $\mathop{\mathrm{SL}}(n)$-invariant, we may assume without loss of generality that $p=-e_n$ and $T_p\partial K=\mathop{\mathrm{Span}}(e_1,\dots,e_{n-1})$. We may further assume that $y_{n}=-1+\frac {a_p} 2|y'|^2$ is the quadratic approximation of $\partial K$ near $p$, where we write $y'=(y_1,\dots,y_{n-1})$. Let $Q$ be the ellipsoid $a_p|y'|^2 +y_n^2=1$, osculating $\partial K$ at $p$. Write $1-\rho =\epsilon^2$, and note that $c\leq a_p\leq c'$.

Let $\nu_x$ be the Euclidean normal at $x\in\partial K$. One has $$\|\nu_x\|_{K^{\rho p}}=h_K(\nu_x)-\langle \nu_x,\rho p\rangle=\langle x-\rho p, \nu_x\rangle.$$ We may therefore parametrize the points of $K^{\rho p}$ by $$\zeta_K:[0,1]\times\partial K\to K^{\rho p}, \quad \zeta_K(\alpha, x)=\alpha\frac{\nu_x}{\langle x-\rho p, \nu_x\rangle}.$$ Then by Cauchy-Schwartz, $$\langle x-\rho p, \nu_x\rangle\geq \langle x-p, \nu_x\rangle -(1-\rho)|\langle p, \nu_x\rangle| \geq  \langle x-p, \nu_x\rangle- \epsilon^2.$$

Let $H$ be the hyperplane parallel to $T_p\partial K$ at distance $\epsilon$ from it, and $H^+, H^-$ the half-spaces it defines, with $p\in H^+$. We claim that $|\zeta_K([0,1]\times \partial (K\cap H^-))|\leq c\epsilon^{-n}$.

Consider $x\in\partial K\cap H^-$, so $|x-p|\geq \epsilon$. If $\nu_x$ is proportional to $x-p$ then $\langle x-p, \nu_x\rangle |x-p|\geq \epsilon$, and $|\zeta_K(\alpha, x)| \leq \frac2 {\epsilon}$. Otherwise, consider the affine plane $P=p+\mathop{\mathrm{Span}}(x-p, \nu_x)$, and consider the planar convex body $K_P=K\cap P$. Using Euclidean cooridnates $(x_1,x_2)$ in which $T_pK_P=\mathbb{R}e_1$, $Q_P=Q\cap P$ is osculated at $p$ by the parabola $x_2=-1+\frac12 a_p x_1^2$.

![](centro_affine_2d){#fig:reflectionlaw width="0.4\\linewidth"}

We orient $\partial K$ in such a way that the tangent at $x$ makes an acute angle with $x-p$. Let $y\in H\cap \partial K_P$ belong to the oriented arc $[p,x]\subset\partial K_P$. It holds by the convexity of $K_P$ that $$\langle x-p, \nu_x\rangle\geq |x-p|\sin \measuredangle pxy=|p-y|\sin\measuredangle pyx\geq c\sqrt{\epsilon}\sin\measuredangle pyx.$$ Denoting by $v$ the tangent ray to $\partial K_P$ at $y$, we have $$c\sqrt \epsilon=\measuredangle pyz\leq \measuredangle pyx\leq \pi-\measuredangle(y-p, v)= \pi-c\sqrt \epsilon.$$ Therefore, $$\langle x-p, \nu_x\rangle\geq c\sqrt\epsilon  \sin\measuredangle pyx\geq c\epsilon.$$

Thus again we find that $|\zeta_K(\alpha, x)|\leq \frac c\epsilon$. That is, $\zeta_K([0,1]\times \partial K\cap H^-)\subset \frac{c}{\epsilon}B^n$, and so $$\label{eq:volume_bound}|\zeta_K([0,1]\times(\partial K\cap H^-))|\leq c\epsilon^{-n}.$$

Define $z_K(y'), z_Q(y'):\mathbb{R}^{n-1}\to \mathbb{R}$ for $|y'|<c\sqrt{\epsilon}$ by having $x_K(y'):=(y', z_K(y'))\in \partial K, x_Q(y'):=(y', z_Q(y'))\in \partial Q$, and let $\nu_K(y'), \nu_Q(y')$ be the correspondning unit normals. Then $z_K(y')=z_Q(y')+O(|y'|^3)=-1+\frac{a_p}{2}|y'|^2+O(|y'|^3)$.

![](centro_affine){#fig:reflectionlaw width="0.4\\linewidth"}

Define the ellipsoids $Q_{\pm} = \{y: \frac12 (a_p\pm 2\epsilon^{1/3})|y'|^2+y_n^2=1\}.$ It holds that $z_{Q_\pm}(y')=-1+\frac{1}{2}(a_p\pm 2\epsilon^{1/3})|y'|^2+O(|y'|^3),$ and so for $\epsilon\ll1$, $$Q_+\cap H^+\subset K\cap H^+\subset Q_-\cap H^+.$$ Moreover, as $|\nu_K(y')-\nu_Q(y')|=O(|y'|)$ and $|y'|\leq c \epsilon^{1/2}\ll\epsilon^{1/3}$, it is evident that $$\zeta_{Q_-}([0,1]\times Q_-\cap H^+)\subset  \zeta_{K}([0,1]\times K\cap H^+)\subset \zeta_{Q_+}([0,1]\times Q_+\cap H^+).$$ By estimate [\[eq:volume_bound\]](#eq:volume_bound){reference-type="eqref" reference="eq:volume_bound"} applied to $Q_\pm$ and combined with Lemma [\[lem:volume_ellipsoid\]](#lem:volume_ellipsoid){reference-type="ref" reference="lem:volume_ellipsoid"}, we have $$\zeta_{Q_\pm}([0,1]\times Q_\pm\cap H^+)=\epsilon^{-(n+1)}\left( 2^{-\frac{n+1}{2}} \omega_n \frac{k_p^{1/2}}{\langle p,\nu_p\rangle^{\frac{n+1}{2}}}+err_\pm(p)\right),$$ and applying [\[eq:volume_bound\]](#eq:volume_bound){reference-type="eqref" reference="eq:volume_bound"} for $K$, the claim follows.

::: Proposition
[]{#prop:centro_affine label="prop:centro_affine"} For $q\in \mathop{\mathrm{int}}(K)$, $$\lim_{R\to \infty}\frac{\mathop{\mathrm{vol}}^F_K(B_R^F(q, K))}{e^{\frac{n-1}{2}R}}=\frac{1}{n-1}2^{-\frac{n-1}{2}} \Omega_n(K,q).$$
:::

We may put $q=0$. Parametrize the outward Funk ball of radius $R$ around $0$ by $p\in\partial K$, $0\leq r\leq R$ using $\phi(p,r)=(1-e^{-r})p$. Then

$$\mathop{\mathrm{vol}}^F_K(B_R^F(0,K))=\int_0^R\int_{\partial K} |K^{\phi(p,r)}|\mathrm{Jac}(\phi(p,r))d\mathcal H^{n-1}(p)dr.$$ Now $\mathrm{Jac}(\phi(p,r))=(1-e^{-r})^{n-1}e^{-r}\langle p, \nu_p\rangle$, while by Lemma [\[lem:dual_volume\]](#lem:dual_volume){reference-type="ref" reference="lem:dual_volume"} $$|K^{\phi(p,r)}|= 2^{-\frac{n+1}{2}} \omega_n e^{\frac{n+1}{2}r} \frac{k_p^{1/2}}{\langle p,\nu_p\rangle^{\frac{n+1}{2}}}+o(e^{\frac{n+1}{2}r}),$$ where the error term is uniform in $p$. Applying l'Hospital's rule we find $$\begin{aligned}
\lim_{r\to \infty}\frac{\mathop{\mathrm{vol}}_K^F(B_r^F(0,K))}{e^{\frac{n-1}{2}r}}&=\lim_{r\to\infty}\frac{2}{n-1} \frac {(1-e^{-r})^{n-1}e^{-r}\int_{\partial K} |K^{\phi(p,r)}|\langle p, \nu_p\rangle  d\mathcal H^{n-1}(p)}{e^{\frac{n-1}{2}r}}
\\&=\frac{1}{n-1}2^{-\frac{n-1}{2}} \int_{\partial K}\frac{k_p^{1/2}}{\langle p,\nu_p\rangle^{\frac{n-1}{2}}}d\mathcal H^{n-1}(p).
\end{aligned}$$
