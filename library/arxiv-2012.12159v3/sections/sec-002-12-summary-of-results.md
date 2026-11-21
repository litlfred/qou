---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-002-12-summary-of-results
section_title: "Summary of results"
section_number: 1.2
pages: 2-6
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.985
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
---
If $K\subset\mathbb{R}\mathbb{P}^n$ is a convex body with interior, we may fix a hyperplane at infinity $\eta$ that is disjoint from $K$, and consider the corresponding $\eta$-Funk metric on $K$, denoted $\mathop{\mathrm{Funk}}_K^\eta$. Changing $\eta$ results in a change to the Funk metric, but of a very particular type: the Finsler norm is changed by an exact 1-form. This is the core reason behind the projective invariance of many metric invariants associated to the Funk metric, as follows.

For a submanifold $X\subset \mathop{\mathrm{int}}(K)$, let $\mathop{\mathrm{Funk}}^\eta_K(X)$ stand for the Finsler metric that is induced on $X$ from $\mathop{\mathrm{Funk}}_K^\eta$, that is it is the intrinsic metric induced on $X$ from the Funk metric. When $\eta$ is clear from context, e.g. when $K$ belongs to an affine space, we simply write $\mathop{\mathrm{Funk}}_K(X)$.

::: MainTheorem
[]{#main:projective_invariants label="main:projective_invariants"} Assume $K\subset \mathbb{R}^n$ is $C^2$-smooth and strictly convex. Let $\Omega\subset \mathop{\mathrm{int}}(K)$ be a smooth $k$-dimensional submanifold with boundary. The following are invariant under the action of any invertible projective map $g$ keeping $K$ compact.

::: enumerate
The $k$-dimensional Holmes-Thompson volume of $\mathop{\mathrm{Funk}}_K(\Omega)$, denoted $\mathop{\mathrm{vol}}^{F}_K(\Omega)$.

The geodesics of $\mathop{\mathrm{Funk}}_K(\Omega)$, as well as the length of closed geodesics.

Assume $k=n$, that is $\Omega$ is a smooth domain. Then the Finsler billiard orbits in $\mathop{\mathrm{Funk}}_K(\Omega)$, as well as the length of the periodic orbits, are invariant.
:::
:::

Therefore, whenever we discuss any of those invariants, we may assume $K\subset\mathbb{R}\mathbb{P}^n$ is a convex set, without specifying an affine chart. Here and in the following, smoothness and strict convexity assumptions in statements concerning volumes can be relaxed through a continuity argument.

The *reverse Funk metric* is defined similarly to the Funk metric by setting $B_xK=a_x(K)$, where $a_x$ is the antipodal map with respect to $x$, or equivalently $d_K^{RF}(x,y)=d_K^F(y,x)$. For $K, \eta$ as before we denote the corresponding reverse Funk metric on $\mathop{\mathrm{int}}(K)$ by $\mathop{\mathrm{RFunk}}_K^\eta$. Theorem [\[main:projective_invariants\]](#main:projective_invariants){reference-type="ref" reference="main:projective_invariants"} applies equally to $\mathop{\mathrm{RFunk}}$.

In a sense, those invariants are more natural than the corresponding ones for the Hilbert metric, which is most clearly manifested by their invariance under projective duality. Recall that the *polar* convex body $K^\vee\subset \mathbb{P}^\vee=(\mathbb{R}\mathbb P^n)^\vee$ is the closure of the set of all hyperplanes disjoint from $K$.

::: MainTheorem
[]{#main:duality label="main:duality"} Assume $K\subset \mathop{\mathrm{int}}(L)$ are $C^2$-smooth, strictly convex bodies in $\mathbb{R}\mathbb{P}^n$. Then

1.  $\mathop{\mathrm{vol}}^F_L(K)=\mathop{\mathrm{vol}}^{F}_{K^\vee}(L^\vee)$.

2.  The billiard orbits in $\mathop{\mathrm{Funk}}_L(K)$ and $\mathop{\mathrm{RFunk}}_{K^\vee}(L^\vee)$ are in a natural bijective correspondence. Moreover, a periodic orbit corresponds to a periodic orbit, and they have equal length.

3.  The Holmes-Thompson volumes of $\mathop{\mathrm{Funk}}_L(\partial K)$ and $\mathop{\mathrm{Funk}}_{K^\vee}(\partial L^\vee)$ coincide.

4.  The geodesics of $\mathop{\mathrm{Funk}}_L(\partial K)$ and $\mathop{\mathrm{RFunk}}_{K^\vee}(\partial L^\vee)$ are in a natural bijective correspondence, and the respective closed geodesics have equal length.
:::

In the limit where $K$ is shrinking to a fixed point inside $L$ through homotheties, we get corresponding statements for linear spaces with Minkowski norms, as follows.

Let $K, L\subset V=\mathbb{R}^n$ be fixed convex sets with $0$ in their interior, and consider $K\subset (V, \|\bullet\|_L)$ and $L^o\subset (V^*, \|\bullet\|_{K^o})$. The first statement becomes a tautology, as both volumes, when properly rescaled, approach the symplectic volume of $K\times L^o\subset V\oplus V^*$. The second statement is the duality of the Minkowski billiards $(K, L)$ and $(L^o,-K^o)$, first established in [@gutkin_tabachnikov], and which permeates the work of Artstein-Avidan and Ostrover on the relationship between Minkowski billiards, symplectic geometry and the Mahler conjecture [@artstein_ostrover; @artstein_karasev_ostrover], see also [@ostrover] for a survey. It is the approach of [@artstein_ostrover] that we take to establish the duality. The third statement was established in [@holmes_thompson] in the particular case of $K=L$. The fourth statement is the (non-symmetric) Schäffer dual girth conjecture [@schaeffer], which can also be understood as a duality of gliding billiard orbits. It was established in [@alvarez-paiva] together with the general case of the third statement.

The first statement implies an isomorphic form of duality in Hilbert geometry. Let $\mathop{\mathrm{vol}}_K^H$ be the Holmes-Thompson volume of the Hilbert metric in $K$.

::: MainCorollary
[]{#cor:hilbert_volume label="cor:hilbert_volume"} Given $K\subset \mathop{\mathrm{int}}(L)$ in $\mathbb{R}\mathbb{P}^n$, $\mathop{\mathrm{vol}}^H_L(K)\leq \frac{1}{2^n}{2n\choose n} \mathop{\mathrm{vol}}_{K^\vee}^H(L^\vee)$. Equality is attained if and only if $K$ is an ellipsoid, and $L$ is a simplex.
:::

The third statement implies a duality in Hilbert geometry in the projective plane.

::: MainCorollary
[]{#cor:hilbert_plane label="cor:hilbert_plane"} Let $K\subset\mathop{\mathrm{int}}(L)$ be two convex sets in $\mathbb{R}\mathbb{P}^2$. Then the Hilbert lengths $\mathop{\mathrm{vol}}^H_L(\partial K)$ and $\mathop{\mathrm{vol}}^H_{K^\vee}(\partial L^\vee)$ coincide.
:::

It is not hard to verify that for an ellipsoid $B\subset\mathbb{R}\mathbb{P}^n$, the Funk billiard (though not the metric itself) in a domain $\Omega\subset \mathop{\mathrm{int}}(B)$ coincides with that of the Beltrami-Klein hyperbolic metric. It follows in particular that for an ellipsoid $K\subset B\subset \mathbb{R}\mathbb P^n$, the Funk billiard in $K$ is completely integrable, see [@veselov]. We provide a Funk perspective and an alternative proof of this result in the projective plane, as follows.

::: MainTheorem
[]{#main:conics label="main:conics"} Let $K\subset \mathop{\mathrm{int}}(B)$ be nested ellipses in $\mathbb{R}\mathbb{P}^2$. Then every orbit of the $B$-Funk billiard in $K$ has a caustic, which is a conic in the dual pencil defined by $\partial K, \partial B$. Furthermore, if $Q$ is a caustic for $\mathop{\mathrm{Funk}}_B(K)$, and $\widehat Q\subset \mathbb P^\vee$ is the caustic of the dual orbit in $\mathop{\mathrm{RFunk}}_{K^\vee}(B^\vee)$, then $\widehat Q^*, \partial B, \partial K, Q$ form a harmonic quadruplet of conics.
:::

Here $Q^*\subset\mathbb P^\vee$ denotes the dual quadric, consisting of all tangent hyperplanes to $Q\subset\mathbb{P}$. For a harmonic quadruplet of quadrics, see Definition [\[def:harmonic_quadrics\]](#def:harmonic_quadrics){reference-type="ref" reference="def:harmonic_quadrics"}. In particular, we can interpret the Poncelet porism of any pair of nested conics in terms of closed Funk (equivalently, hyperbolic) billiard orbits.

In the second part of this note, we consider the Holmes-Thompson volume of balls in the Funk metric. Assume $K\subset\mathbb{R}^n$, and let $B_r^F(q, K)$ denote the outward $r$-ball in the Funk metric on $K$ centered at $q$. Denoting by $K^z\subset (\mathbb{R}^n)^*$ the dual body with respect to $z$, and by $\omega_n$ the volume of the Euclidean unit ball in $\mathbb{R}^n$, one has $\mathop{\mathrm{vol}}^{F}_K(B_r^F(0,K))=\frac{1}{\omega_n}\int_{(1-e^{-r})K}|K^z|dz$. We show that for $K$ unconditional and any $r$, the volume of $B_r^F(0, K)$ is maximized when $K$ is an ellipsoid, which translates into the following equivalent systems of affine inequalities.

::: MainTheorem
[]{#main:bodies_inequality label="main:bodies_inequality"} For an unconditional convex body $K\subset \mathbb{R}^n$, one has

-   For all $0< \rho<1$ $$\int_{\rho K} |K^z|dz\leq n\omega_n^2\int_0^\rho\frac{t^{n-1}dt}{(1-t^2)^{\frac{n+1}{2}}}.$$

-   For all $j\geq 0$, $$\int_{K\times K^o}\langle x, \xi\rangle^{2j}dxd\xi\leq \frac{(2\pi)^n}{n+2j}\frac{1}{ (n+2j)!!(n-2)!!(2j-1)!!} \left(\frac2\pi\right)^{\frac{1-(-1)^n}{2} }.$$

Equality in each case is attained uniquely by ellipsoids.
:::

For $j=1$, this is a theorem of Ball [@ball_remarks].

In the limit $\rho\to0$, which corresponds to Funk balls of infinitesimal radius, the Blaschke-Santaló inequality is recovered: $$|K\times K^o|\leq |B^n\times (B^n)^o|=\omega_n^2.$$ On the other end of the scale, one has the following result of [@berck_bernig_vernicos].

::: MainProposition
[]{#prop:centro_affine_main label="prop:centro_affine_main"} Assume $K\subset\mathbb{R}^n$ is $C^2$-smooth and strictly convex, and $0\in\mathop{\mathrm{int}}(K)$. Then as $\rho\to 1^{-}$, $$\int_{\rho K}|K^z|dz\sim 2^{-\frac{n-1}{2}}\frac{\omega_n}{n-1}\frac{1}{(1-\rho)^{\frac{n-1}{2}}}\Omega_n(K),$$ where $\Omega_n(K)$ is the centro-affine surface area of $K$.
:::

For the definition of centro-affine surface area, see eq. [\[eq:centro_affine\]](#eq:centro_affine){reference-type="eqref" reference="eq:centro_affine"}. Therefore in the limit of large Funk balls, Theorem [\[main:bodies_inequality\]](#main:bodies_inequality){reference-type="ref" reference="main:bodies_inequality"} yields the centro-affine isoperimetric inequality: $$\Omega_n(K)\leq \Omega_n(B^n)=n\omega_n.$$ Thus Funk geometry interpolates between those two extremes through a continuum of affine inequalities. As both the Blaschke-Santaló and the centro-affine inequalities are valid for arbitrary convex bodies with centroid at the origin, we naturally conjecture that Theorem [\[main:bodies_inequality\]](#main:bodies_inequality){reference-type="ref" reference="main:bodies_inequality"} remains true in this generality.

The Colbois-Verovic volume entropy conjecture [@colbois_verovic] asserts that the volume growth entropy of metric balls in Hilbert geometry is maximized by ellipsoids, or equivalently by smooth strictly convex bodies. This was recently proved by Tholozan [@tholozan] and Vernicos-Walsh [@vernicos_walsh] using very different methods, and previously established up to dimension $3$ in [@vernicos3d]. Theorem [\[main:bodies_inequality\]](#main:bodies_inequality){reference-type="ref" reference="main:bodies_inequality"} yields yet another proof of the volume entropy conjecture, albeit only for unconditional bodies. We write $B^H_r(q,K)$ for the metric ball in the Hilbert metric.

::: MainCorollary
[]{#cor:entropy label="cor:entropy"} For $K\subset \mathbb{R}^n$ a convex unconditional body, $$\limsup_{R\to \infty}\frac{1}{R}\log \mathop{\mathrm{vol}}_K^H (B^H_R(q,K))\leq n-1.$$
:::

Theorem [\[main:bodies_inequality\]](#main:bodies_inequality){reference-type="ref" reference="main:bodies_inequality"} follows from a more general functional form of the same inequalities. Below $\mathcal L$ is the Legendre transform, defined in eq. [\[eq:legendre\]](#eq:legendre){reference-type="eqref" reference="eq:legendre"}.

::: MainTheorem
[]{#main:inequality_functional label="main:inequality_functional"} For an unconditional Borel function $f=e^{-\phi}:\mathbb{R}^n\to[0,\infty)$, one has the equivalent systems of inequalities

-   For all $j\geq 0$, $$\int_{\mathbb{R}^n\times\mathbb{R}^n}\langle x,\xi\rangle ^{2j}e^{-\phi(x)-\mathcal L\phi(\xi)}dx d\xi\leq (2\pi)^n \frac{(n-2+2j)!!}{(n-2)!!(2j-1)!!}.$$

-   For all $0\leq \rho<1$, $$\int_{\mathbb{R}^n\times\mathbb{R}^n}e^{-\phi(x)-\mathcal L \phi (\xi)+\rho\langle x,\xi\rangle}dxd\xi\leq \frac{(2\pi)^n}{(1-\rho^2)^{\frac n 2}}.$$

Equality in each case is attained uniquely, up to equality a.e., by $f$ that is a multiple of a gaussian.
:::

In the limit $\rho\to0$ we recover the functional Blaschke-Santaló inequality for unconditional functions. For $j=1$, this is a theorem of Huang and Li [@huang_li]. The proof we give is inspired by, and largely the same as the proof of the functional Blaschke-Santaló inequality of Lehec [@lehec].

By Proposition [\[prop:centro_affine_main\]](#prop:centro_affine_main){reference-type="ref" reference="prop:centro_affine_main"}, the centro-affine surface area of $K$ can be viewed as a regularization of the total Holmes-Thompson volume of $K$ equipped with its Funk metric. It excels at capturing the volume growth of the metric, but has the drawback of being dependent on the precise way in which the volume is exhausted, namely through metric balls centered at a point. As a consequence, it depends on the choice of a center point; worse yet, it is not a projective invariant, defying the expectations one might entertain in light of Theorem [\[main:projective_invariants\]](#main:projective_invariants){reference-type="ref" reference="main:projective_invariants"} i).

In an attempt to remedy this situation, in section [\[sec:projective_total_volume\]](#sec:projective_total_volume){reference-type="ref" reference="sec:projective_total_volume"} we propose a different regularization of the total volume, which turns out to be a projective invariant of the body alone. For simplicity we focus on the projective plane, although it is likely that a similar procedure can be carried out in greater generality. To state precisely, we use the standard Euclidean structure on $\mathbb{R}^{3}$, and locally identify $\mathbb{R}\mathbb{P}^2$ with $S^2$. Given $\Omega\subset \mathop{\mathrm{int}}(K)$ in $S^2$, it then holds that $$\mathop{\mathrm{vol}}^F_K(\Omega)=\frac{1}{\omega_n}\int_{\Omega\times K^\vee}\frac{dxd\xi}{\langle x,\xi\rangle^3},$$ where $K^\vee\subset S^2$ is the polar set given by $K^\vee=\{\xi\in S^2:\forall x\in K, \langle x,\xi\rangle\geq 0\}$.

For a convex set $K\subset S^2$ we define, borrowing a term from [@brylinski], the *Beta function of $K$* by the integral $$B_K(z)=\int_{K\times K^\vee}\langle x,\xi\rangle^zdxd\xi, \quad \mathrm {Re}z>-1.$$

::: MainTheorem
[]{#main:beta label="main:beta"} Let $K\subset S^2$ be $C^2$-smooth and strictly convex. Then $B_K(z)$ extends as a meromorphic function with simple poles contained in $\{-\frac52,-\frac72,-\frac 92,\dots\}$. Moreover, the value $B_K(-3)$ is a projective invariant of $K\subset\mathbb{R}\mathbb{P}^2$.
:::

While the affinity to Funk volume is transparent, an explicit description of $B_K(-3)$ in terms of the Funk metric on $K$ remains to be found. The regularized total volume was inspired by the theory of Möbius energy of knots [@ohara_knots], and particularly its extensions to linking and Riesz energy [@ohara_solanes_linking; @ohara_solanes_riesz].
