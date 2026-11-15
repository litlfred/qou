---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-012-4-funk-billiards-and-duality
section_title: "Funk billiards and duality"
section_number: 4
pages: 13-18
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.981
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
---
[]{#sec:billiards label="sec:billiards"}

Let $K\subset \mathop{\mathrm{int}}(L)$ in $\mathbb{P}^n$ be a pair of convex bodies. Using the $L$-Funk metric on $K$, we can consider the corresponding billiard dynamics inside $K$ following [@gutkin_tabachnikov], which we call the $L$-Funk billiard in $K$. As it is a non-reversible Finsler structure, some care should be taken, however the results we need go through unaltered. In particular, using [@gutkin_tabachnikov Lemma 3.3] we get the following description of the reflection law, illustrated in figure [1](#fig:reflectionla){reference-type="ref" reference="fig:reflectionla"}.

Assume $q_1\in\partial K$, and $v\in S_{q_1}K$ is an incoming ray. Extend the ray until its first intersection $p_0$ with $\partial L$. Let $Q_1$ be a hyperplane tangent to $\partial K$ at $q_1$, and $P_0$ the hyperplane tangent to $L$ at $p_0$. Let $z_1=\mathbb{R}\mathbb{P}^{n-2}$ be the intersection $Q_1\cap P_0$, and note that $z_1\subset\mathbb \mathbb{R}\mathbb{P}^n\setminus L$. Let $P_1$ be the other tangent hyperplane to $\partial L$ through $z_1$, and $p_1\in\partial L$ the tangency point. The vector $v'\in S_{q_1}K$ pointing towards $p_1$ is then the outgoing ray.

![Funk billiard reflection law](reflectionlaw2.pdf){#fig:reflectionla width="0.4\\linewidth"}

::: Remark
[]{#rem:proper label="rem:proper"} It is clear from this description that a proper Funk billiard trajectory when $K, L$ are smooth and strictly convex, will extend indefinitely, in terms of bounces, as a proper billiard trajectory.
:::

One can also consider the billiard defined by the reverse Funk metric $\mathop{\mathrm{RFunk}}_L(K)$. Its billiard trajectories coincide with the time-reversed Funk billiard trajectories of $\mathop{\mathrm{Funk}}_L(K)$.

The same billiard can also be considered from an outer perspective: the phase space then consists of all $(n-2)$-dimensional planes $z\subset\mathbb{P}^n$ that do not intersect $L$, and the billiard map mapping $z_0$ to $z_1$ is defined by the same diagram, which is reproduced in figure [2](#fig:outer_billiard){reference-type="ref" reference="fig:outer_billiard"} from the outer billiard perspective. By analogy with the affine setting, we call this the *outer Funk billiard* on $L$ with geometry set by $K$.

![Funk outer billiard reflection law](outer_billiard){#fig:outer_billiard width="0.4\\linewidth"}

::: exmp
Assume $K\subset B\subset\mathbb{R}^2$ are two discs centered at the origin. Then the resulting Funk billiard inside $K$ coincides with the standard Euclidean one, as illustrated in figure [3](#fig:circles){reference-type="ref" reference="fig:circles"}. Indeed, take $p_0,p_1\in\partial B$, and let $z$ be the intersection of the tangents to $B$ at those points. Since $\measuredangle op_0z=\measuredangle op_1z=\measuredangle oq_1z=\frac\pi 2$, the points $p_0, p_1,q_1, z,o$ all lie on the circle having $zo$ as its diameter. It follows that the incidence angle is $\measuredangle p_0q_1z=\measuredangle p_0p_1z$, while the reflected angle is $\measuredangle p_1q_1z=\measuredangle p_1p_0z$. It remains to note that $|zp_0|=|zp_1|$.
:::

![Funk billiard in concentric discs](circles){#fig:circles width="0.4\\linewidth"}

Examining the Funk billiard law description, we see it is projectively invariant. The following provides an alternative proof of this fact, and extends the projective invariance to include the length spectrum.

::: Proposition
[]{#prop:billiard_invariant label="prop:billiard_invariant"} Choose a hyperplane at infinity $\eta\in\mathop{\mathrm{int}}(L^\vee)$. The corresponding $L$-Funk billiard reflection law in the interior of $K$ is then independent of $\eta$, and thus projectively invariant. Furthermore, the $L$-Funk length of a periodic orbit is also projectively invariant.
:::

Let $d_{\eta}(x,y)$ be the $(L,\eta)$-Funk distance from $x$ to $y$. Replacing $\eta$ by $\eta'$, we have $d_{\eta'}(x,y)=d_{\eta}(x,y)+h(y)-h(x)$ for some $h=h_{\eta,\eta'}$ by Proposition [\[prop:funk_exact\]](#prop:funk_exact){reference-type="ref" reference="prop:funk_exact"}.

Now let $p,r\in\partial K$ be fixed points. Then $p,q,r$ are consecutive reflection points of the billiard if $q$ is an extremal point for $d_\eta(p,q)+d_\eta(q,r)$. Since $d_{\eta'}(p,q)+d_{\eta'}(q,r)=d_\eta(p,q)+d_\eta(q,r)+h(r)-h(p)$, this condition is independent of $\eta$.

Finally, if $p_0,\dots, p_{N-1}, p_N=p_0$ is a periodic orbit, then evidently $$\sum_{j=0}^{N-1} d_{\eta'}(p_j,p_{j+1})= \sum_{j=0}^{N-1} d_{\eta}(p_j,p_{j+1})+\sum_{j=0}^{N-1}(h(p_{j+1})-h(p_j))= \sum_{j=0}^{N-1} d_{\eta}(p_j,p_{j+1}),$$ concluding the proof.

::: exmp
[]{#exm:hyperbolic label="exm:hyperbolic"} Consider the Euclidean ball $B^n\subset\mathbb{R}^n$. The Funk Finsler norm in $\mathop{\mathrm{int}}(B^n)$ is given by $$\phi_x(v)=\frac{\sqrt{(1-|x|^2)|v|^2+\langle x,v\rangle^2}}{1-|x|^2}+\frac{\langle x,v\rangle}{1-|x|^2}.$$ The first summand is the Beltrami-Klein model of hyperbolic geometry . The second summand is the $1$-form $\frac{1}{1-|x|^2}\sum_{j=1}^nx_j dx_j$, which is exact. Consequently, for any domain $K\subset\mathop{\mathrm{int}}(B^n)$, the $B^n$-Funk billiard in $K$ coincides with the hyperbolic billiard, and the length of periodic orbits is the same in both geometries.
:::

A careful examination of the reflection law shows that it is anti-symmetric under the duality $(K,L)\leftrightarrow (L^\vee, K^\vee)$, namely a Funk billiard trajectory in one naturally defines a reverse Funk billiard trajectory in the other, which we call the dual trajectory, as follows. Let us write $Q_j=\mathcal L_K(q_j)=T_{q_j}\partial K\in\partial K^\vee$ for $q_j\in\partial K$, and similarly $P_j\in\partial  L^\vee$ for $p_j\in \partial L$. We identify the phase space with a subset of $\{(q,p): q\in \partial K, p\in \partial L^\vee\}$, where $(q,p)$ represents the outgoing ray from $q$ in the direction of $p$.

The billiard tranformation $(q_0,p_0)\mapsto (q_1,p_1)$ can be understood as two dual billiards unraveling simultaneously, taking alternating steps: the Funk billiard $\mathop{\mathrm{Funk}}_L(K)$, and the reverse Funk billiard $\mathop{\mathrm{RFunk}}_{K^\vee}(L^\vee)$. In $\mathbb P$, the ray arrives at $q_1\in\partial K$, and $Q_1=\mathcal L_K(q_1)$ is marked on $\partial K^\vee$. In $\mathbb P^\vee$, the interval from $Q_1$ to $P_0=\mathcal L_L(p_0)$ (which avoids $L^\vee$) is extended until its second intersection $P_1$ with $\partial L^\vee$. Now $p_1=\mathcal L_{L^\vee}(P_1)\in \partial L$ is marked, and the outgoing ray from $q_1$ is $(q_1, p_1)$. This dual dynamic is illustrated in figure [4](#fig:dual_billiards){reference-type="ref" reference="fig:dual_billiards"}, where the same letter is used for both a point and its dual hyperplane.

![Dual Funk - reverse Funk billiard dynamics](dual_billiards2){#fig:dual_billiards width="1\\linewidth"}

We thus established the following.

::: Proposition
[]{#prop:duality_billiards label="prop:duality_billiards"} Let $q_0,q_1,\dots \in\partial K$ be an $L$-Funk billiard trajectory in $K$. Let $p_j\in\partial L$ be the first intersection of the extension of the oriented segment $[q_j, q_{j+1}]$ with $\partial L$, and $P_j$ the hyperplane tangent to $L$ at $p_j$. Then $P_0,P_1,\dots$ is a $K^\vee$-reverse Funk billiard trajectory in $L^\vee$. In the plane, the two orbits have equal rotation number.
:::

::: Remark
The stark similarity to the duality in Minkowski billiards is not without reason. In the limit when $L$ is much bigger than $K$, the Funk billiard becomes Minkowski, much like the hyperbolic plane is almost Euclidean in small scale. More precisely, take $K\subset L\subset\mathbb{R}^n$, fix $a\in L$ and set $L_R=a+R(L-a)$. Then as $R\to\infty$, the Funk billiard orbits in $K$ converge to the Minkowski billiard orbits with geometry given by $L$ centered at $a$. In particular, if $L$ is the Euclidean ball and $a$ its center, we recover the Euclidean billiard inside $K$.
:::

Consider the case of the projective plane. Since the Funk billiard trajectory consists of straight segments and preserves the symplectic form on the phase space [@gutkin_tabachnikov Theorem 4.3], Birkhoff's theorem on the existence of two $m$-periodic orbits, for any $m\geq 2$ and any rotation number, remains valid.

As an example, the two $2$-periodic orbits when $K\subset L$ are two non-concentric circles appear in figure [5](#fig:2_periodic_circles){reference-type="ref" reference="fig:2_periodic_circles"}.

![2-periodic orbits in a pair of discs](2_periodic){#fig:2_periodic_circles width="0.4\\linewidth"}

To motivate the next result, let us consider 2-periodic orbits in general. Assume that $q_0, q_1\in\partial K$ are the bounce points of a 2-periodic orbit $\gamma$ of the $L$-Funk billiard in $K$, and $p_0, p_1\in \partial L$ the corresponding intersection points, appearing on the line in the order $p_1, q_0, q_1, p_0$ as in figure [6](#fig:2_periodic_general){reference-type="ref" reference="fig:2_periodic_general"}. Note that $\gamma$ is also a reverse Funk billiard orbit. Its Funk length is twice the Hilbert distance between the points: $$\textrm{Length}^F_L(\gamma)=\textrm{Length}^{RF}_L(\gamma)=\log \frac {|p_1q_1|}{|p_1q_0|}+\log \frac {|q_0p_0|}{|q_1p_0|}=2d^H_L(q_0, q_1).$$

![2-periodic orbit](2_periodic_general){#fig:2_periodic_general width="0.48\\linewidth"}

Since, $$d^H_L(q_0,q_1)=\frac12 \log [p_1, q_0, q_1, p_0]=\frac12 \log [P_1, Q_0, Q_1, P_0]=d^H_{K^\vee}(P_0, P_1),$$ it holds that dual 2-periodic orbits have equal length. In fact, the duality of billiard orbits extends to the metric realm in full generality.

We now assume $K\subset \mathop{\mathrm{int}}(L)$ are smooth, strictly convex bodies in $\mathbb{R}\mathbb{P}^n$.

::: Theorem
[]{#thm:dual_lengths label="thm:dual_lengths"} Dual periodic orbits in $\mathop{\mathrm{Funk}}_L(K)$ and $\mathop{\mathrm{RFunk}}_{K^\vee}(L^\vee)$ have equal lengths.
:::

We will need the following auxiliary fact of independent interest.

::: Proposition
[]{#prop:unique_symplecic label="prop:unique_symplecic"} There is a $\mathop{\mathrm{GL}}(V)$-invariant non-degenerate 2-form $\omega$ on $\mathbb P\times\mathbb P^\vee\setminus \mathcal Z$. Such a form is unique up to constant, and moreover it is canonically normalized. Furthermore, it is a symplectic form.
:::

Let $H=\mathop{\mathrm{Stab}}_{x,\xi}\subset \mathop{\mathrm{GL}}(V)$ be the stabilizer of a fixed point $(x,\xi)$, which acts on $T_x\mathbb P$ by the full linear group, and similarly on $T_\xi\mathbb P^\vee$. Observe that $$\wedge^2 T^*_{x,\xi}(\mathbb P\times\mathbb P^\vee)=\wedge^2(x\otimes x^\perp\oplus \xi\otimes \xi^\perp)=x^{\otimes 2}\otimes \wedge^2 x^\perp\oplus \xi^{\otimes 2}\otimes \wedge^2 \xi^\perp\oplus x\otimes x^\perp \otimes \xi\otimes\xi^\perp.$$ The first and second summand evidently have no $H$-invariant elements. As for the third summand, we may write $$x\otimes x^\perp \otimes \xi\otimes\xi^\perp= (x\otimes \xi)\otimes (x^\perp\otimes\xi^\perp).$$ There is a natural identification $\theta:x\otimes\xi\to \mathbb{R}$, and a natural pairing $\eta:x^\perp\otimes\xi^\perp \to \mathbb{R}$, which is moreover non-degenerate as $(x,\xi)\notin \mathcal Z$. We then let $\omega_{x,\xi}$ correspond to $\theta\otimes\eta^{-1}$. It is immediate from the construction that $\omega$ is non-degenerate, and it is evidently canonically normalized.

For uniqueness, it remains to show that any $H$-invariant non-trivial pairing $\psi:x^\perp\otimes \xi^\perp\to \mathbb{R}$ must be a multiple of $\eta^{-1}$. Writing $\xi^\perp=W$ and identifying $x^\perp=W^*$, $H$ acts on $x^\perp\otimes \xi^\perp=W^*\otimes W$ by $\mathop{\mathrm{GL}}(W)$, admitting a unique invariant line.

Finally, let us verify that $\omega$ is symplectic, that is $d\omega=0$. As $d\omega\in\Omega^3(\mathbb P\times\mathbb P^\vee\setminus \mathcal Z)$ is $\mathop{\mathrm{GL}}(V)$-invariant, it suffices to show that there are no non-trivial invariant $3$-forms. We have an invariant decomposition $$\begin{aligned}
    \wedge^3 T^*_{x,\xi}(\mathbb P\times\mathbb P^\vee)&=x^{\otimes 3}\otimes \wedge^3 x^\perp\oplus \xi^{\otimes 3}\otimes \wedge^3 \xi^\perp\\&\oplus x^{\otimes 2}\otimes \wedge^2 x^\perp \otimes \xi\otimes\xi^\perp\oplus x\otimes x^\perp \otimes  \xi^{\otimes 2}\otimes \wedge^2\xi^\perp.
    
\end{aligned}$$

As before, the first and second summands do not have invariant lines. Considering the third summand, we have $$x^{\otimes 2}\otimes \wedge^2 x^\perp \otimes \xi\otimes\xi^\perp=x\otimes \wedge^2 x^\perp\otimes\xi^\perp .$$ One can choose an element $g\in H$ acting by the identity on $x^\perp$ and $\xi^\perp$, and rescaling $x$ non-trivially. Thus there are no invariant elements in the third summand, and similiarly neither in the fourth.

*Proof of Theorem [\[thm:dual_lengths\]](#thm:dual_lengths){reference-type="ref" reference="thm:dual_lengths"}.* Recall that by Proposition [\[prop:billiard_invariant\]](#prop:billiard_invariant){reference-type="ref" reference="prop:billiard_invariant"}, the Funk length of a periodic orbit is a projective invariant.

Now fix $\eta\in\mathbb P^\vee$, and define $H_\eta:(\mathbb P\setminus \eta^\perp)\times \mathbb P^\vee\setminus \mathcal Z\to T^*\mathbb P$ by identifying, for any $x\notin\eta^\perp$, $x^*=\eta$, and setting $$\label{eq:identification}H_\eta(x,\xi)=-\left(\hat\eta \mapsto (x^\perp+\hat \eta)\cap \xi -\hat\eta\right) \in \eta^*\otimes x^\perp=x\otimes x^\perp=T_x^*\mathbb P.$$

For $\eta\neq \eta'$, we have in the common domain of definition the equality $$H_{\eta'}(x,\xi)=H_\eta(x,\xi)+\beta_{\eta,\eta'}(x),$$ where $\beta_{\eta,\eta'}\in\Omega^1(\mathbb P\setminus(\eta^\perp\cup\eta'^\perp))$ is a closed $1$-form by the proof of Proposition [\[prop:funk_exact\]](#prop:funk_exact){reference-type="ref" reference="prop:funk_exact"}.

Let $\omega_0$ be the canonic symplectic form on $T^*\mathbb{P}$. We claim that for distinct $\eta,\eta'\in\mathbb P^\vee$, the $2$-forms $H_\eta^*\omega_0$ and $H_{\eta'}^*\omega_0$ coincide on their common domain of definition. In light of the previous paragraph, it suffices to show that $\overline\beta^*\omega_0=0$, where $\overline\beta(x,\xi)=(x,\beta(x))$, and $\beta\in \Omega^1(U)$ is a closed form, defined in a neighborhood $U\subset\mathbb P$. We may choose coordinates locally such that $\omega_0=\sum dx_i\wedge d\xi_i$, while $\beta=\sum \frac{\partial f}{\partial x_i}dx_i$, and denote $B:=D_x\beta=(\frac{\partial^2f}{\partial x_i\partial x_j})$. Choose $u,v\in T_{x,\xi}(\mathbb P\times \mathbb P^\vee)$, and write $\hat u=dx(u), \hat v=dx(v)\in T_x\mathbb P$. We have

$$\begin{aligned}
\overline\beta^*\omega_0(u,v)&=\omega_0((\hat u, B\hat u), (\hat v, B\hat v))\\&=\sum_i( \hat u_i (B\hat v)_i- \hat v_i (B\hat u)_i)=\sum_{i,j}B_{ij}\hat u_i\hat v_j-\sum_{i,j}B_{ji}\hat u_i\hat v_j=0.
\end{aligned}$$

It follows that as $\eta\in\mathbb P^\vee$ varies, $H_\eta^*\omega_0$ patch to a globally defined form $\omega'\in \Omega^2(\mathbb P\times\mathbb P^\vee\setminus \mathcal Z)$. Let us check that $\omega'$ is projectively invariant. First we compute that for $g\in \mathop{\mathrm{GL}}(V)$, $$\begin{aligned}
 H_\eta\circ g(x,\xi)=H_\eta(gx,g^{-*}\xi)=(gx, \hat\eta\mapsto (g^{-*}x^\perp+\hat \eta)\cap g^{-*}\xi-\hat\eta)=gH_{g^*\eta}(x,\xi).
\end{aligned}$$ Consequently, $$g^*\omega'=g^*H_\eta^*\omega_0= H_{g^*\eta}^* g^*\omega_0= H_{g^*\eta}^*\omega_0=\omega'.$$ It follows by Proposition [\[prop:unique_symplecic\]](#prop:unique_symplecic){reference-type="ref" reference="prop:unique_symplecic"} that $\omega'=c\omega$, for some $c\in\mathbb{R}$. To find the value of $c$, we note that $\omega^n=\mu$ defines the Holmes-Thompson volume by Lemma [\[lem:two_measures\]](#lem:two_measures){reference-type="ref" reference="lem:two_measures"}, which by definition corresponds to $\omega_0^n$, and so $c^n=1$. It is also clear that $c>0$, e.g. by writing both forms explicitly using Euclidean coordinates at a point where $\xi=x$. Thus $c=1$.

Replacing $T^*\mathbb P$ with $T^*\mathbb P^\vee$, one similarly has the map $$\overline{H_\theta}:\mathbb{P}\times (\mathbb P^\vee\setminus \theta^\perp)\setminus \mathcal Z\to T^*\mathbb P^\vee, (x,\xi)\mapsto \left(\hat\theta \mapsto (\xi^\perp+\hat \theta)\cap x -\hat\theta\right) \in \theta^*\otimes \xi^\perp=\xi\otimes\xi^\perp,$$ and the various forms $\overline{H_\theta}^*\omega_0^\vee$ as $\theta$ varies patch to give $\omega''=\omega'=c'\omega$. The constant is $c'=1$, as the sign is flipped twice compared to $H_\eta$: once due to the change of order of $\mathbb{P}, \mathbb{P}^\vee$, and a second time due to the sign change in the definition of $\overline H_\theta$.

Fix $\eta\in \mathop{\mathrm{int}}(L^\vee)$, $\theta\in \mathop{\mathrm{int}}(K)$. It holds by Proposition [\[prop:projective_funk\]](#prop:projective_funk){reference-type="ref" reference="prop:projective_funk"} that $$S^*\mathop{\mathrm{Funk}}^\eta_L(K)=H_\eta(K\times\partial L^\vee),\quad S^*\mathop{\mathrm{RFunk}}^\theta_{K^\vee}(L^\vee)=\overline{H_\theta}(\partial K\times L^\vee).$$

Consider now $\Sigma:=\partial (K\times L^\vee)\subset\mathbb{P}\times\mathbb{P}^\vee\setminus\mathcal Z$. Denote by $\alpha_0, \overline\alpha_0$ the Liouville 1-forms on $T^*\mathbb P$, resp. $T^*\mathbb{P}^\vee$. Define $\alpha_\eta=H_\eta^*\alpha_0$, $\overline\alpha_\theta=\overline{H_\theta}^*\overline\alpha_0$. It holds that $d\alpha_\eta-d\overline \alpha_\theta=\omega-\omega=0$, and so $\alpha_\eta-\overline \alpha_\theta=df$ for some function $f$ defined near $\Sigma$.

A dual pair of billiard trajectories corresponds to a trajectory on $\Sigma$, as we now describe. It first follows an integral curve of $\mathop{\mathrm{Ker}}\omega|_{K\times \partial L^\vee}$ while on $\Sigma_1:=\mathop{\mathrm{int}}(K)\times \partial L^\vee$, and of $\mathop{\mathrm{Ker}}\omega|_{\partial K\times L^\vee}$ while on $\Sigma_2 = \partial K\times \mathop{\mathrm{int}}(L^\vee)$, corresponding to the straight segments of $\mathop{\mathrm{Funk}}_L(K)$ and $\mathop{\mathrm{RFunk}}_{K^\vee}(L^\vee)$, respectively. By Remark [\[rem:proper\]](#rem:proper){reference-type="ref" reference="rem:proper"}, it can only arrive to $\partial K\times\partial L^\vee$ transversally, and so the reflection law translates to simply switching from one integral curve to another, which similarly must also be transversal to $\partial K\times\partial L^\vee$. Such a trajectory on $\Sigma$ is called a generalized characteristic.

Let a generalized characteristic $\Gamma$ correspond to a dual pair of orbits $\gamma\subset \mathop{\mathrm{Funk}}_L(K)$ and $\overline\gamma\subset\mathop{\mathrm{RFunk}}_{K^\vee}(L^\vee)$. Noting that $\alpha_\eta|_{\Gamma\cap \partial K\times L^\vee}=0$, $\overline \alpha_\theta|_{\Gamma\cap K\times\partial L^\vee}=0$, we conclude that $$\textrm{Length}(\gamma)=\int_\Gamma \alpha_\eta=\int_\Gamma \overline\alpha_\theta=\textrm{Length}(\overline\gamma).$$
