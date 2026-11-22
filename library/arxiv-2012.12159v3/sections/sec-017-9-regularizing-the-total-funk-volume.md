---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-017-9-regularizing-the-total-funk-volume
section_title: "Regularizing the total Funk volume"
section_number: 9
pages: 34-41
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.974
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
---
[]{#sec:projective_total_volume label="sec:projective_total_volume"} We use the notation of subsection [\[sec:volume_funk\]](#sec:volume_funk){reference-type="ref" reference="sec:volume_funk"}. Recall that we use the standard Euclidean structure on $V=\mathbb{R}^{n+1}$, and identify the double cover of $\mathbb{P}$ and $\mathbb{P}^\vee$ with the unit sphere. Let $x_0\in x$ be a unit vector, well-defined up to sign. We write $\sigma_x, \sigma_\xi$ for the standard Euclidean measure on the corresponding copy of $S^2$.

::: Lemma
[]{#lem:lemma91 label="lem:lemma91"}For $g\in \mathop{\mathrm{PGL}}(V)$, set $\chi_g(x,\xi)=|gx_0||g^{-*}\xi_0|$. Then $$g_*(\sigma_x\sigma_\xi)=\chi_{g^{-1}}^{-n-1}\sigma_x\sigma_\xi$$
:::

Denote by $\mathop{\mathrm{Stab}}^+(x,\xi)\subset\mathop{\mathrm{Stab}}(x,\xi)$ the subgroup of the stabilzer in $\mathop{\mathrm{PGL}}(V)$ that has $\mathop{\mathrm{sign}}\det g|_x=\mathop{\mathrm{sign}}\det g^*|_\xi$. Then $\mathop{\mathrm{Stab}}^+(x,\xi)$-equivariantly we have $$\mathop{\mathrm{Dens}}(T_{x,\xi}(\mathbb{P}\times \mathbb{P}^\vee))=\mathop{\mathrm{Dens}}^*(x)^{n+1}\otimes\mathop{\mathrm{Dens}}^*(\xi)^{n+1}=x^{n+1}\otimes \xi^{n+1},$$ and so $$g_*(\sigma_x\sigma_\xi)(gx,g^{-*}\xi)=(|gx_0||g^{-*}\xi_0|)^{n+1}\sigma_x\xi=\chi_g(x,\xi)^{n+1}\sigma_x\sigma_\xi.$$ Hence $$g_*(\sigma_x\sigma_\xi)(x,\xi)=\chi_g(g^{-1}x,g^*\xi)^{n+1}\sigma_x\sigma_\xi=\chi_{g^{-1}}^{-n-1}(x,\xi)\sigma_x\sigma_\xi,$$ as claimed. Define $f_0\in C(\mathbb{P}\times\mathbb{P}^\vee)$ by $f_0(x,\xi)=|\langle x_0,\xi_0\rangle|$. It is easy to check that $$g^*f_0=\chi_g^{-1}f_0.$$ Define $\mu_z(x,\xi)=f_0(x,\xi)^z\sigma_x\sigma_\xi\in \mathcal M(\mathbb{P}\times\mathbb{P}^\vee\setminus \mathcal Z)$. For $\textrm{Re}z>-1$, it extends as an absolutely continuous measure on $\mathbb{P}\times\mathbb{P}^\vee$.

::: Lemma
[]{#lem:measure_push label="lem:measure_push"} $g_*\mu_z=\chi_{g^{-1}}^{-(n+1)-z}\mu_z$.
:::

It is easy to check that $g_*\mu_z=(g^{-1})^*f_0^z\cdot g_*(\sigma_x\sigma_\xi)$. It remains to put the previous computations together. As expected from Proposition [\[prop:invariant_measure\]](#prop:invariant_measure){reference-type="ref" reference="prop:invariant_measure"}, we see that $z=-(n+1)$ corresponds to the invariant measure $\mu$.

Henceforth we use the same notation for a point on $S^n$ and the corresponding line in $\mathbb{R}\mathbb{P}^n$. The action of $\mathop{\mathrm{GL}}(V)$ on $S^n$ is $g(x)=\frac{gx}{|gx|}$.

Let $K\subset S^n\subset V=\mathbb{R}^{n+1}$ be a proper convex compact set, and $K^\vee\subset S^n$ its polar body, namely $K^\vee=\{\xi\in S^{n}: \forall x\in K, \langle x,\xi\rangle\geq 0\}$. They correspond to a dual pair of convex sets in $\mathbb{P}$ and $\mathbb{P}^\vee$, also denoted $K, K^\vee$.

Define the *Beta function* of $K\subset S^n$ by $$\mathbb{C}\ni z\mapsto B_K(z)=\int_{K\times K^\vee}\langle x,\xi\rangle ^z\sigma_x\sigma_\xi =\langle  \mathbbm1_{K\times K^\vee}, \mu_z\rangle.$$ Clearly, $B_K(z)=B_{K^\vee}(z)$. Assume henceforth that $K$ is smooth and strictly convex.

::: Lemma
[]{#lem:convergence_domain label="lem:convergence_domain"} The integral $B_K(z)$ is convergent if and only if $\mathrm{Re} z>-\frac{n+3}{2}$.
:::

The zeros of $\langle x,\xi\rangle$ on $K\times K^\vee$ are $\mathcal Z\cap K\times K^\vee$, which is an $(n-1)$-dimensional submanifold in $\partial K\times\partial K^\vee$. Let $x_1,\dots,x_{n-1}$ be local coordinates on $\partial K$, and $\xi_1,\dots, \xi_{n-1}$ the Legendre-dual coordinates on $\partial K^\vee$, that is $\mathcal Z\cap (K\times K^\vee)=\{\xi_j=x_j\}$. Let $x_n$ be the remaining coordinate near $\partial K$, so that locally $K=\{x_n\geq 0\}$, and $K^\vee=\{\xi_n\geq 0\}$. We put $\xi=x+y$, and use the notation $v^j=(v_i)_{i=1}^{j}$. When restricted to $\{x_n=\xi_n=0\}$, $f_0( (x^{n-1},0), (\xi^{n-1},0)) =\langle A_x y^{n-1}, y^{n-1}\rangle+O(|y^{n-1}|^3)$, for some $A_x>0$. It follows that in general, $$f_0(x,\xi)=\langle A_{x}y^{n-1}, y^{n-1}\rangle+b_xx_n+c_x\xi_n +O(|y^{n-1}|^3+|y^{n-1}|(x_n+\xi_n)+x_n^2+\xi_n^2),$$ where $A_x, b_x, c_x>0$ are uniformly bounded from above and below by strict convexity.

Thus $\int_{K\times K^\vee} f_0(x,\xi)^z$ converges if and only if

$$\int_{y_1^2+\dots+y_{n-1}^2<1}\int_{x_n, \xi_{n}=0}^1 ( y_1^2+\dots+y_{n-1}^2+x_n+\xi_{n})^z<\infty,$$ which immediately reduces to $2(\mathrm{Re}z+2)+(n-2)>-1\iff \mathrm {Re}z>-\frac{n+3}{2}$.

*In all the following we assume $n=2$*, as already this case appears to be interesting and involved. We proceed to prove Theorem [\[main:beta\]](#main:beta){reference-type="ref" reference="main:beta"}.

Denote $D_+=\{(x,\xi); \langle x,\xi\rangle> 0\}\subset S^2\times S^2$. The group $\mathop{\mathrm{SO}}(3)$ acts diagonally on $S^2\times S^2$, leaving $D_+$ invariant. By $\Omega^{i,j}(S^2\times S^2)$ we denote the differential forms of bidegree $(i,j)$. We will use the function $R_z(t)=\frac{1-t^{z}}{1-t^2}$, which is smooth in $t>0$ and analytic in $z\in\mathbb C$.

::: Proposition
[]{#prop:primitive label="prop:primitive"} For $z\in \mathbb{C}$, $z\neq -1$, define $\omega_z\in{ \Omega^{1,1}(D_+)^{\mathop{\mathrm{SO}}(3)}  }$ by $$\omega_z:=\frac{1}{z+1}R_{z+1}(\langle x,\xi\rangle)\langle dx,\xi\rangle\wedge \langle x, d\xi\rangle.$$ Then $d_xd_\xi\omega_z=\langle x,\xi\rangle^z \sigma_x\sigma_\xi$.
:::

Rather than verify the claimed equality, we will construct from scratch the form $\omega_z$ with the required derivative. We write $S^2_x$, $S^2_\xi$ for the corresponding copies of the sphere.

Fix $\xi$ and use it as the North Pole with associated polar coordinates $\theta, \phi$ of $x\in S^2$, where $\cos\theta=\langle x,\xi\rangle$, and $\phi$ is the azimuth. We have $\sigma_x=\sin\theta d\theta d\phi$. It holds that $d\phi(u)=-\frac{1}{\sin\theta}d\theta(x\times u)$, and differentiating $\cos\theta=\langle x,\xi\rangle$ we find $$\label{eq:dphi} -\sin \theta d\theta=\langle dx, \xi\rangle\Rightarrow d\phi=\frac{1}{\sin^2\theta}\langle x\times dx, \xi\rangle=\frac{\langle x\times dx, \xi\rangle}{1-\langle x,\xi\rangle^2}$$ The forms $d\theta$, $\langle x\times dx,\xi\rangle=\sin^2\theta d\phi$ are linearly independent in $S^2\setminus \{\pm \xi\}$, and vanish at $\pm\xi$. Assume a 1-form $\zeta_z$ on $S^2_x$ of the form $\zeta_z=b_z(\theta)d\phi$ is given, such that $d_\xi\omega_z= \zeta_z \sigma_\xi.$ Then $$d\zeta_z=b_z'(\theta) d\theta d\phi+ c_0 b_z(0)\delta_\xi,$$ where $c_0=2\pi$ and $\delta_\xi$ is the delta measure at $\xi$. Thus if $b_z(0)=0$, and $b_z'(\theta)=\sin\theta\cos^z\theta$, the desired equation would be satisfied. For this we take $$b_z(\theta)=\frac{1-\cos^{z+1}\theta}{z+1 }$$

Now fix $x$. We should find an $\mathbb{R}^3$-valued $\mathop{\mathrm{Stab}}(x)=\mathop{\mathrm{SO}}(2)$-equivariant $1$-form $\eta_z$ on $S^2_\xi$ with $$\label{eqn:eta_differential}d_\xi\eta_z=\frac{1-\langle x,\xi\rangle^{z+1}}{1-\langle x,\xi\rangle^2}  \sigma_\xi \xi,$$ whence we may take $\omega_z= \frac{1}{z+1}  \langle x\times dx, \eta_z\rangle$. It is easy to verify that $$\eta_z=a_z(\theta)d\phi \cdot x+c_z(\theta)d\theta \cdot x\times\xi,$$ where $c_z(\theta)=\frac{1-\cos^{z+1}\theta}{\sin\theta}$ and $a_z(\theta)=\int_0^\theta c_z(\tau)\cos\tau d\tau$ satisfies [\[eqn:eta_differential\]](#eqn:eta_differential){reference-type="eqref" reference="eqn:eta_differential"}. The verification boils down to the equality $$\frac{1-\cos^{z+1}\theta}{\sin\theta}\cos\theta d\theta d\phi\cdot x-\frac{1-\cos^{z+1}\theta}{\sin\theta}d\theta \cdot x\times d\xi=\frac{1-\cos^{z+1}\theta}{\sin\theta}d\theta d\phi\cdot \xi,$$ which in turn follows from [\[eq:dphi\]](#eq:dphi){reference-type="eqref" reference="eq:dphi"} applied to $S^2_\xi$, by taking scalar products with $x,\xi$ and $x\times\xi$.

We find that $$\omega_z=-\frac{1}{z+1}\langle x\times dx, \eta_z\rangle=\frac{1}{z+1}\frac{1-\langle x,\xi\rangle^{z+1}}{1-\langle x,\xi\rangle^2}\langle dx,\xi\rangle\wedge \langle x,  d\xi\rangle.$$

It follows by the Stokes theorem and using continuity to pass to the boundary of $D_+$, that for $\mathrm {Re}z\geq 0$, $$\label{eq:stokes_beta}B_K(z) = \int_{ K\times K^\vee} \langle x,\xi\rangle^z = \int_{\partial K\times \partial K^\vee} \omega_z.$$

::: exmp
Let us compute $B_K(z)$ for the spherical disc $K=\{x_3\geq \frac{1}{\sqrt 2}\}$, satisfying $K=K^\vee$. Parametrize $\partial K$ by $x(\alpha)=\frac{1}{\sqrt 2}(\cos \alpha, \sin\alpha, 1)$, and $\partial K^o$ by $\xi(\beta)=\mathcal L(x(\beta))=\frac{1}{\sqrt 2}(-\cos \beta, -\sin\beta, 1)$, $0\leq \alpha,\beta\leq 2\pi$. Then: $$\langle x,\xi\rangle =\frac12(1-\cos(\alpha-\beta))=\sin^2\frac{\alpha-\beta}{2}$$ $$dx=\frac{1}{\sqrt 2}(-\sin\alpha,\cos\alpha,0)d\alpha,\quad  d\xi=\frac{1}{\sqrt 2}(\sin\beta,-\cos\beta,0)d\beta$$ $$\langle dx,\xi\rangle = \frac12\sin(\alpha-\beta)d\alpha,\quad \langle d\xi,x\rangle =\frac12\sin(\beta-\alpha)d\beta$$ Thus $$\begin{aligned}
 B_K(z)&=-\frac{1}{4(z+1)} \int_0^{2\pi}\int_0^{2\pi}\frac{1-(\sin^2\frac{\alpha-\beta}{2})^{z+1}}{1-\sin^4\frac{\alpha-\beta}{2}}\sin^2(\alpha-\beta)d\alpha d\beta 
\\& =-\frac{1}{2(z+1)}\int_{-\pi}^{\pi}(2\pi-2|\gamma|)\frac{1-(\sin^2\gamma)^{z+1}}{1-\sin^4\gamma}\sin^22\gamma d\gamma\\&=
-\frac{8}{z+1}\int_0^{\pi}(\pi-\gamma)\frac{1-(\sin^2\gamma)^{z+1}}{1+\sin^2\gamma}\sin^2\gamma d\gamma\\&=
-\frac{8}{z+1}\int_0^{\pi}\frac \pi 2\frac{1-(\sin^2\gamma)^{z+1}}{1+\sin^2\gamma}\sin^2\gamma d\gamma
\\&=
-\frac{8\pi}{z+1}\int_0^{\frac\pi2}\frac{1-(\sin^2\gamma)^{z+1}}{1+\sin^2\gamma}\sin^2\gamma d\gamma, 
\end{aligned}$$ where the penultimate equality is by symmetrizing the integrand around $\frac\pi 2$.

Putting $t=\sin^2\gamma$ we get $$\begin{aligned}
 B_K(z)&=-\frac{4\pi}{z+1}\int_0^1\frac{1-t^{z+1}}{1+t}\frac{\sqrt t}{\sqrt{1-t}}dt=-\frac{4\pi}{z+1}(\pi(1-\frac{1}{\sqrt 2})-\int_0^1 \frac{t^{z+\frac 32}dt}{(1+t)\sqrt{1-t}} ) 
\\&=-\frac{4\pi}{z+1}\left(\pi(1-\frac{1}{\sqrt 2})-\sqrt\pi \frac{\Gamma(z+\frac 52)}{\Gamma(z+3)}{}_2F_1(1,z+\frac52,z+3;-1)\right) 
.
\end{aligned}$$ In particular, $B_K(-3)=2\pi^2$.
:::

::: Proposition
For $K\subset S^2$ smooth and strictly convex, $B_K(z)$ extends as a meromorphic function with simple poles that are contained in $\{-\frac52, -\frac72,-\frac 92,\dots\}$.
:::

Let $\mathcal L:\partial K\to \partial K^\vee$ be the Legendre transform, defined by $\mathcal L x=\partial K^\vee\cap x^\perp$. It points in the unique direction perpendicular to both $x$ and $T_x\partial K$: since $\langle x,\xi\rangle:\partial K\times\partial K^\vee\to \mathbb{R}$ is smooth and non-negative, its zeros are all minima and hence critical points. That is, for fixed $\xi=\mathcal L x$, we have $\langle dx,\xi\rangle =0$. Parametrize $\partial K$ by arc-length, denoted $x(\alpha)$, and $\partial K^\vee$ by $\xi(\beta)=\mathcal L(x(\beta))$. It then holds that $$\langle x(\alpha), \xi(\beta)\rangle =(\beta-\alpha)^2 u(\alpha,\beta)$$ with $u$ smooth, and by strict convexity $u>0$. Similarly we have $$\langle x'(\alpha),\xi(\beta)\rangle =(\beta-\alpha) v_1(\alpha,\beta),\quad \langle \xi'(\beta),x(\alpha)\rangle =(\beta-\alpha) v_2(\alpha,\beta),$$ with $v_1,v_2$ smooth and non-zero when $|\alpha-\beta|\leq \epsilon$. Here $\epsilon>0$ is fixed, and depends on the lower bound on the curvatures of $K, K^\vee$.

Recall eq. [\[eq:stokes_beta\]](#eq:stokes_beta){reference-type="eqref" reference="eq:stokes_beta"}: $$B_K(z) =-\frac{1}{z+1}\int_{\partial K\times \partial K^\vee} \frac{1-\langle x,\xi\rangle^{z+1}}{1-\langle x,\xi\rangle^2}\langle dx,\xi\rangle\wedge \langle d\xi,x\rangle .$$ Writing $\beta=\alpha+\phi$, it follows that up to an addition of an entire function of $z$ and the factor $\frac{1}{z+1}$, $B_K(z)$ equals

$$\begin{aligned}
B^\epsilon_K(z)&:=\int_{-\epsilon}^\epsilon d\phi\int_{\alpha=0}^{2\pi}\frac{1-\langle x(\alpha),\xi(\alpha+\phi)\rangle^{z+1}}{1-\langle x(\alpha),\xi(\alpha+\phi)\rangle^{2}} \langle x'(\alpha), \xi(\alpha+\phi)\rangle
    \langle \xi'(\alpha+\phi), x(\alpha)\rangle  d\alpha 
    \\ &=h_\epsilon(K)-\int_{-\epsilon}^\epsilon|\phi|^{2z+4} d\phi\int_{\alpha=0}^{2\pi}  u(\alpha,\alpha+\phi)^{z+1}\tilde v(\alpha,\phi)d\alpha ,
\end{aligned}$$ where $h_\epsilon(K)$ is a constant depending only on $K$, and $\tilde v$ is a smooth non-zero function.

The inner integral, denoted $f_z(\phi)$, is an analytic family of smooth functions as $z\in\mathbb C$. The function $\int_{-\epsilon}^\epsilon|\phi|^{2z+4} f_z(\phi)d\phi$ is then meromorphic in $\mathbb{C}$, with simple poles that are contained in a subset of $\{-\frac52,-\frac 72,\dots\}$, corresponding to the simple poles of the meromorphic family $\{|\phi|^{2z+4}\}$ of even homogeneous distributions on $\mathbb{R}$. Also by Lemma [\[lem:convergence_domain\]](#lem:convergence_domain){reference-type="ref" reference="lem:convergence_domain"}, $z=-1$ is an analytic point of $B_K(z)$. This completes the proof of the meromorphic extendibility of $B_K(z)$ with poles as stated.

::: Proposition
The value $B_K(-3)$ is a projective invariant of $K\subset\mathbb{R}\mathbb{P}^2$.
:::

Recall the symbol $\chi_g(x,\xi)$ defined in Lemma [\[lem:lemma91\]](#lem:lemma91){reference-type="ref" reference="lem:lemma91"}. For any fixed $g\in \mathop{\mathrm{PGL}}(V)$, we have by Lemma [\[lem:measure_push\]](#lem:measure_push){reference-type="ref" reference="lem:measure_push"} the following equality for $\textrm{Re}z>-1$: $$\begin{aligned}
\label{eq:invariance}&\langle \mathbbm 1_{g^{-1}K\times (g^{-1}K)^\vee}, \mu_z\rangle=\langle g^*\mathbbm1_{K\times K^\vee},\mu_z\rangle=\langle \mathbbm1_{K\times K^\vee}, g_*\mu_z\rangle\\=&\langle \chi_{g^{-1}}^{-3-z}\mathbbm 1_{K\times K^\vee}, \mu_z\rangle.\nonumber
\end{aligned}$$ We already established that one end (and hence both) of this equation admits a meromorphic extension in $z\in \mathbb C$, which is analytic at $z=-3$. Let us verify that the value of the right hand side at $z=-3$ equals $B_K(-3)$, implying projective invariance.

Fix $g\in \mathop{\mathrm{PGL}}(3)$, and consider $h(z)=\langle \chi_{g^{-1}}^{-3-z} \mathbbm 1_{K\times K^\vee}, \mu_z\rangle=\int_{K\times K^\vee} \chi_{g^{-1}}^{-3-z} d\mu_z$. Write $\psi(x,\xi)=\chi_{g^{-1}}(x,\xi)$, and note $\psi$ is a smooth positive function. We now use Proposition [\[prop:primitive\]](#prop:primitive){reference-type="ref" reference="prop:primitive"} and the Stokes theorem to write

$$\begin{aligned}
h(z)&= \int_{K\times K^\vee} \psi(x,\xi)^{-z-3}d_xd_\xi\omega_z\\&=\int\limits_{\partial K\times K^\vee}\psi^{-z-3}d_\xi\omega_z+(z+3)\int\limits_{K\times K^\vee}\psi^{-z-4} d_x \psi\wedge d_\xi \omega_z 
    \\ &=\int\limits_{\partial K\times \partial K^\vee}\psi^{-z-3}\omega_z- (z+3)\int\limits_{K\times K^\vee} d_\xi(\psi^{-z-4}d_x \psi)\wedge\omega_z \\ &+(z+3)\int\limits_{\partial K\times K^\vee}\psi^{-z-4}d_\xi \psi\wedge\omega_z +(z+3)\int\limits_{ K\times \partial K^\vee}\psi^{-z-4}  d_x \psi\wedge \omega_z
\end{aligned}$$

The first summand admits a meromorphic extension by the same proof as that for $B_K$, and its value at $z=-3$ is $\int_{\partial K\times \partial K^\vee}\omega_{-3}=B_K(-3)$. Consider next the second summand; by Lemma [\[lem:convergence_domain\]](#lem:convergence_domain){reference-type="ref" reference="lem:convergence_domain"}, the form $\omega_z$ is $L^1$ in $K\times K^\vee$ for $\mathrm {Re}z>-\frac72$, implying the second summand is analytic in this range, and vanishes at $z=-3$.

The last two summands are treated similarly, so let us focus on the first one. Written explicitly, it is

$$\frac{z+3}{z+1}\int_{\partial K\times K^\vee} \frac{1-\langle x,\xi\rangle^{z+1}}{1-\langle x,\xi\rangle^2}\langle dx,\xi\rangle\wedge\langle x,d\xi\rangle\wedge  \psi^{-z-4}d_\xi\psi.$$ It is easy to see that up to a summand that is analytic near, and vanishes at, $z=-3$, the integral equals $$I=\frac{z+3}{z+1}\int_{\partial K\times K^\vee} \langle x,\xi\rangle^{z+1}\langle x,d\xi\rangle \wedge\langle dx,\xi\rangle\wedge \psi^{-z-4}d_\xi\psi.$$ It holds that $$\frac{1}{z+2}d(\langle x,\xi\rangle^{z+2})\wedge\langle dx,\xi\rangle\wedge \psi^{-z-4}d_\xi\psi=\langle x,\xi\rangle^{z+1}\langle x, d\xi\rangle \wedge \langle dx, \xi\rangle\wedge \psi^{-z-4}d_\xi\psi.$$ Consequently we can integrate by parts to obtain $$\begin{aligned}
I=I_1+I_2&=\frac{z+3}{(z+1)(z+2)}\int\limits_{\partial K\times\partial K^\vee}\langle x,\xi\rangle ^{z+2} \langle dx,\xi\rangle\wedge\psi^{-z-4}d_\xi\psi\\&-\frac{z+3}{(z+1)(z+2)}\int_{\partial K\times K^\vee} \langle x,\xi\rangle ^{z+2}  d(\langle dx,\xi\rangle \wedge\psi^{-z-4}d_\xi\psi). 
\end{aligned}$$

Let us rewrite the first summand as $$\begin{aligned}
\nonumber I_1&=\frac{1}{(z+1)(z+2)}\int\limits_{\partial K\times \partial K^\vee}d_x(\langle x,\xi\rangle^{z+3})\wedge \psi^{-z-4}d_\xi\psi\\&=- \frac{1}{(z+1)(z+2)}\int\limits_{\partial K\times\partial K^\vee} \langle x,\xi\rangle^{z+3}d_x(\psi^{-z-4}d_\xi\psi)\label{eq:I1_2}  
\end{aligned}$$

We use the arc-length parametrization $x(\alpha)$, $0\leq \alpha\leq L$ for $\partial K$, and $\xi (\beta)=\mathcal L(x(\beta))$, $0\leq \beta\leq L$ for $\partial K^\vee$. Recall that by strict convexity, $\langle x(\alpha), \xi(\beta)\rangle=|\beta-\alpha|^2u(\alpha, \beta)$ with $u>0$ smooth. We will use $C$ to denote a positive constant that only depends on $K$ and $g$, which may differ between occurrences.

Consider the integral in [\[eq:I1_2\]](#eq:I1_2){reference-type="eqref" reference="eq:I1_2"}. As $z\to-3$, the integrand is majorized by $C|\langle x, \xi\rangle|^{-1/4}$, which is integrable on $\partial K\times\partial K^\vee$. Thus by Lebesgue's dominated convergence theorem, $$\lim _{z\to -3} I_1=-\frac12\int_{\partial K\times\partial K^\vee}d_x(\psi^{-1}d_\xi\psi) =0.$$

Next we consider $I_2$. Let $P: S^2\to \partial K^\vee$ be the nearest-point projection, well-defined in some open neighborhood $U$ of $\partial K^\vee$. Define $K^\vee_\epsilon=\{\xi\in U: \langle \xi, \mathcal L(P\xi)\rangle \leq \epsilon\}$, which is a one-sided tube around $\partial K^\vee$. We parametrize $\partial K\times K^\vee_\epsilon$ by $(x(\alpha), \xi(\beta, s))$, $0\leq \alpha,\beta\leq L$, $0\leq s\leq \epsilon$, where $\xi=\xi(\beta, s)$ is the point that has $P(\xi)=\xi(\beta)$, $\langle \xi, \mathcal L (P(\xi))\rangle=s$.

Write $\eta=d(\langle dx,\xi\rangle \wedge\psi^{-z-4}d_\xi\psi)$. We claim that the integral $$\label{eq:integral}\int_{\partial K\times K^\vee}\langle x,\xi\rangle^{z+2}\eta$$ converges for $\mathrm {Re}z>-\frac 72$.

It is enough to consider the integral [\[eq:integral\]](#eq:integral){reference-type="eqref" reference="eq:integral"} in the smaller domain $\{|\alpha-\beta|\leq \epsilon, 0\leq s\leq \epsilon\}$. There $\langle x(\alpha), \xi(\beta, s)\rangle \geq C\max((\beta-\alpha)^2, s)\geq C((\beta-\alpha)^2+s)$. It remains to check that for $\mathrm {Re}z>-\frac72$, $$\int_0^\epsilon\int_0^\epsilon\frac{dsd\phi}{(s+\phi^2)^{-z-2}}<\infty,$$ which is clear. Consequently, $\lim_{z\to -3} I_2=0$ due to the $(z+3)$ factor. This concludes the proof of the statement.

Let us derive some equivalent expressions for $B_K(-3)$, working towards an explicit geometric formula. One has

$$\begin{aligned}
B_K(-3)&=-\frac12\left. \int_{\partial K\times\partial K^\vee}\frac{1-\langle x,\xi\rangle^{z+1}}{1-\langle x,\xi\rangle ^2}\langle dx,\xi\rangle\wedge\langle x,d\xi\rangle\right|_{z=-3} \\&=\frac12 \left.\int_{\partial K\times\partial K^\vee}\langle x,\xi\rangle^{z+1} \frac{1-\langle x,\xi\rangle^{-z-1}}{1-\langle x,\xi\rangle ^2}\langle dx,\xi\rangle\wedge\langle x,d\xi\rangle\right|_{z=-3}\\&=\frac12  \left.\int_{\partial K\times\partial K^\vee}\langle x,\xi\rangle^{z+1}\langle dx,\xi\rangle\wedge\langle x,d\xi\rangle\right|_{z=-3}
    \\&=\frac1{2(z+2)}\left.\int_{\partial K\times\partial K^\vee}\langle dx,\xi\rangle \wedge d(\langle x, \xi\rangle^{z+2})\right|_{z=-3}
    \\&=\frac1{2}\left.\int_{\partial K\times\partial K^\vee}\langle x,\xi\rangle^{z+2}\langle dx,d\xi\rangle\right|_{z=-3}.
\end{aligned}$$ $$\begin{aligned}
B_K(-3)&=\frac1{2}\left.\int_{\partial K\times\partial K^\vee}\frac{\langle dx,d\xi\rangle}{\langle x,\xi\rangle^z}\right|_{z=1}
    \label{eq:mahler_volume} 
    \\&=\frac12\left.\int_{\partial K\times\partial K^\vee} \frac{\langle dx,\xi\rangle\wedge \langle x,d\xi\rangle}{\langle x,\xi\rangle^z}\right|_{z=2}\label{eq:mahler_volume2} 
\end{aligned}$$

::: Proposition
Let $\partial K$ be parametrized by arc-length as $x(\alpha)$. The geodesic curvature of $\partial K$ is $\kappa(\alpha)=\det (x(\alpha), x'(\alpha), x''(\alpha))$. Then $$B_K(-3)= \frac12 \lim_{\epsilon\to 0}\int_{x\in\partial K, \xi\in \partial K^\vee, \langle x,\xi\rangle \geq\epsilon^2}\frac{\langle dx,\xi\rangle\wedge\langle x,d\xi\rangle}{\langle x,\xi\rangle^2}+\frac{2\sqrt 2}{\epsilon}\int_{\partial K}\sqrt {\kappa(\alpha )}d\alpha.$$
:::

We carry out the regularization explicitly, using formula [\[eq:mahler_volume2\]](#eq:mahler_volume2){reference-type="eqref" reference="eq:mahler_volume2"}. Put $L=\textrm{Length}(x(\alpha))$, $\xi(\beta)=\mathcal L(x(\beta))=x(\beta)\times x'(\beta)$, and let $\alpha,\beta\in\mathbb{R}$ be $L$-periodic parameters.

We will write $x(\alpha)>\xi(\beta)$ if $\beta<\alpha<\beta+\frac{L}{2}$. Define for small values $|t|\leq \epsilon$ $$g_K(t)=\left\{\begin{array}{cc}\int_{\langle x,\xi\rangle =t^2, x>\xi}\langle dx,\xi\rangle&,\qquad t\geq0 \\ \int_{\langle x,\xi\rangle =t^2, x<\xi}\langle dx,\xi\rangle&,\qquad t<0 \end{array}\right.$$ Clearly $g_K$ is smooth in $[-\epsilon,\epsilon]$, and $g_K(0)=0$.

Let $S(x,\xi)=\sqrt{\langle x,\xi\rangle}$ be a signed square root defined on $\partial K\times \partial K^\vee$ , which is non-negative for $x\geq \mathcal L(\xi)$, and non-positive for $x\leq L(\xi)$. Put $t=S(x,\xi)$, so $t^2=f_0(x,\xi)=\langle x,\xi\rangle$ and $2tdt=\langle dx,\xi\rangle +\langle x,d\xi\rangle$, and $\langle dx,\xi\rangle \wedge\langle x,d\xi\rangle=-2tdt\langle dx,\xi\rangle$.

It then holds that $$\begin{aligned}
B_K(-3)&= \frac12 \int_{\langle x,\xi\rangle \geq\epsilon^2}\frac{\langle dx,\xi\rangle\wedge\langle x,d\xi\rangle}{\langle x,\xi\rangle^2} -  \int_0^{\epsilon}\frac{g_K(t)-g_K(-t)-2g_K'(0)t}{t^3}dt +\frac{2}{\epsilon}g_K'(0) ,
 
\end{aligned}$$ and the middle summand approaches $0$ as $\epsilon\to 0$.

It remains to compute $g'_K(0)$. Note that $$g_K(-t)= \int_{S(x,\xi)=-t}\langle dx,\xi \rangle =- \int_{S(\xi,x)=t}\langle d\xi,x\rangle =-g_{K^\vee}(t).$$

Parametrizing $\alpha=\beta+s_t(\beta)$, we have $$t^2=\langle x(\alpha), \xi(\beta)\rangle =\frac12 s_t(\beta)^2\kappa(\beta)+O(s_t^3).$$ Thus $$s_t(\beta)=\frac{\sqrt2}{\sqrt{\kappa(\beta)}}t+ O(t^2),$$ and writing $$g_K(t)= \int_0^L \langle x'(\beta +s_t(\beta)),x(\beta)\times x'(\beta)\rangle d\beta,$$ $$\langle x'(\beta +s_t(\beta)),x(\beta)\times x'(\beta)\rangle= \sqrt{2\kappa(\beta)}t+O(t^2),$$ we find $$g_K'(0)=g_{K^\vee}'(0)= \sqrt 2\int_0^L\sqrt{\kappa(\beta)}d\beta.$$
