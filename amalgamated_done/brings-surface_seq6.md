<!-- FILE_START: brings-smoothness-intro.md -->
The color fibration is well-defined generically, but the geometry requires a smooth bundle to support the spectral resolvents. We package the color data as a spectral curve carrying a spinor bundle. We then establish that Bring's surface is smooth and that its projection singularities resolve intrinsically; no external blow-up is needed.

The base-to-fibre interpretation dominates the middle of this section. The exceptional-divisor and Thurston-relaxation expositions situate the base manifold $M$ and the brane-point fibres $\mathcal{S}_p$ inside a single geometric framework. We introduce the Briggs–Klein affine chart for explicit computation and the radial projection of Bring's surface as its geometric counterpart.

We document the structural compatibility with the three color tubes plus ambient color via the four-colourability of Bring's surface. Finally, we provide the cyclotomic reduction that the next section takes as given: the reduction modulo cyclotomic primes defines the resolvent basis.
<!-- FILE_END: brings-smoothness-intro.md -->

<!-- FILE_START: color-bundles.md -->
The spacetime--color decomposition of Bring's surface maps onto three classical bundle structures over the $\mathbb{P}^1(\mathbb{C})$ base $z=x_0/x_1$.

**Cotangent bundle.**
The three-sheeted cubic ([color elliptic curve](#prop:color-elliptic)) realises the color variables $X=(x_2,x_3,x_4)$ as a *spectral curve* $\Sigma\subset T^{*}\mathbb{P}^1(\mathbb{C})$. The base coordinate $z$ parametrises spacetime position. The three roots $X_1,X_2,X_3$ of [color elliptic curve](#prop:color-elliptic) are eigenvalues of a Higgs-like field $\Phi$ on the base. The six singular fibres (where the discriminant $\Delta(z)$ vanishes) specify the loci at which eigenvalues coincide and the differential $dX$ degenerates in the cotangent fibre.

**Spinor bundle.**
The spectral modes $w_1,\dots,w_4$ ([Lagrange resolvents](#rem:lagrange-resolvents)) reside in a rank-$2$ complex vector bundle over $\mathbb{P}^1(\mathbb{C})$. The color doublet $\Psi_L=(w_1,w_2)^T$ and its conjugate $\Psi_R=(w_4,w_3)^T$ transform under the $\mathrm{SU}(2)$ holonomy generators $H_1,H_2$ of [holonomy of trefoil](#rem:holonomy-trefoil). Thus $\Psi_L$ constitutes a section of the *spinor bundle* $\mathcal{S}^{+}\to\mathbb{P}^1(\mathbb{C})$. The $B_3$ monodromy equips this bundle with a flat connection whose holonomy is the trefoil-knot group.

**Adjoint bundle.**
The $\mathrm{SO}(3)$ images $R_\alpha,R_\beta$ act on the triple $(\omega_1,\omega_2,\omega_3)$. This triple therefore spans a section of the adjoint bundle $\mathrm{ad}P\to\mathbb{P}^1(\mathbb{C})$ associated to the principal $\mathrm{SU}(2)$-bundle $P$. The T-duality involution $\iota\colon X\leftrightarrow z$ ([T-duality on elliptic fibres](#rem:t-duality-elliptic)) interchanges the fibre and base of the adjoint bundle, exchanging spectral eigenvalues with spacetime coordinates.
<!-- FILE_END: color-bundles.md -->

<!-- FILE_START: brings-smoothness-resolution.md -->
**Proposition.**
Let $\mathcal{S}$ denote the Bring's surface ([Bring's surface](#def:brings-surface)) and $\pi \colon \mathcal{S} \to \mathbb{P}^1(\mathbb{C})$ the color projection.

1. **Smoothness.** The three power-sum constraints are transverse in $\mathbb{P}^4$. Consequently, $\mathcal{S}$ is a smooth algebraic variety lacking singular points.
2. **Intrinsic resolution.** At each branch point $z = z_c$ where two color sheets $x_i, x_j$ collide, the local color coordinate $\delta = x_i - x_j$ satisfies $z - z_c \sim \delta^2$. The exceptional divisor of the blow-up at each ramification point is already embedded in the color coordinates. No external resolution is required.
3. **Regularity of the Briggs--Klein chart.** The radial parameter $r = \lvert w_1 \rvert^2$ constitutes a regular function on $\mathcal{S}$. The $C_5$ orbits $w_k \mapsto \zeta^k w_k$ foliate the surface without fixed points for $0 < r < \infty$.
<!-- FILE_END: brings-smoothness-resolution.md -->

<!-- FILE_START: brings-smoothness.md -->
Bring's surface $\mathcal{S}$ ([Bring's surface](#def:brings-surface)) is a *smooth* algebraic variety. The three power-sum constraints intersect transversely in $\mathbb{P}^4$, ensuring no singular points exist. The six topological defects identified in [color bundles](#rem:color-bundles)—where the discriminant $\Delta(z)$ vanishes and two color sheets $X_i,X_j$ collide—are singularities of the *projection* $\pi\colon\mathcal{S}\to\mathbb{P}^1(\mathbb{C})$, not of the surface itself.

**Resolution in the $x_j$ coordinates.**
At a branch point $z=z_c$ where $x_2=x_3$, define the local color coordinate $\delta=x_2-x_3$. In a neighbourhood of the defect, the spacetime ratio satisfies

$$
  z-z_c \sim \delta^2.
$$

While the projection map develops a ramification cusp, $\delta$ passes smoothly through zero, carrying the geometry from one sheet to the other. The exceptional divisor of the blow-up at each branch point sits already embedded in the color coordinates $x_2,x_3,x_4$. No external resolution is required.

**Resolution in the $w_k$ coordinates.**
The DFT mixes all five $x_j$ into every resolvent $w_k$ ([Lagrange resolvents](#rem:lagrange-resolvents)). Thus no single $w_k$ vanishes at a branch point. The Briggs--Klein chart ([Briggs--Klein chart](#def:briggs-klein-chart)) remains smooth throughout $0<r<\infty$. The radial parameter $r=\lvert w_1\rvert^2$ is regular on $\mathcal{S}$, and the $C_5$ orbits $w_k\mapsto\zeta^k w_k$ foliate the surface without fixed points. The infinite torsion and eigenvalue crossings visible in the base $\mathbb{P}^1(\mathbb{C})$ are artefacts of projecting away the internal degrees of freedom that the $w_k$ retain.
<!-- FILE_END: brings-smoothness.md -->

<!-- FILE_START: approach-to-exceptional-divisor.md -->
## Approach: from base $M$ to fibre $\mathcal{S}_p$

In the QOU archimedean tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$, the base manifold $M$ carries the smooth metric in which two free vortices propagate. As the vortex cores approach a brane point $p \in M$, the smooth metric becomes degenerate. The base coordinate ratio $z = \sqrt{q} - 1/\sqrt{q}$ drives the exceptional divisor $\mathcal{S}_p$ ([state bundle fibre](#def:exceptional-divisor)) into the foreground. "Below Planck scale" in QOU is a **categorical** statement, not a metric one. The relevant geometry switches from the base $M$ to the fibre $\mathcal{S}_p$, where the morphisms are knot operators ([knot-operator energy](#def:knot-operator-energy)).

The encounter unfolds in three moments:

1. **Approach.** Two vortex tubes propagate on $M$ and approach a common brane point $p$. The Reeb flow on $M$ tracks the motion.
2. **Crossing onto the fibre.** At the threshold $\partial F / \partial \mathbf{c} = 0$ on the colour-tube cubic (Picard--Lefschetz thimble §setup), the base coordinate $z$ hits a discriminant zero. The smooth base structure pinches. The operative morphisms transition to those of $\mathcal{S}_p$ — the $\Phi_q$-piece $K_S$ ([$\Phi_q$-piece](#def:phi-q-piece)).
3. **Merging of fundamental groups.** The two vortex cores become parallel strands in a single braid. Their independent fundamental groups $\pi_1(\nu_1)$ and $\pi_1(\nu_2)$ amalgamate into the fundamental group $\pi_1(U \setminus K)$ of the merged knot complement. Here $U$ is a tubular neighbourhood of $p$, and $K$ is the link formed by the two strands inside it.

After moment (3), the encounter constitutes a knot-theoretic problem. The merged complement admits a hyperbolic structure ([Thurston relaxation](#sec:thurston-relaxation)). The SDP/LP machinery of [Chapter 12](#chap:particle-interactions) selects the lowest-energy link representative (SDP as thimble flow). Mostow rigidity (geometric confinement) makes the resulting topology—and hence the mass—discrete.
<!-- FILE_END: approach-to-exceptional-divisor.md -->

<!-- FILE_START: thurston-relaxation.md -->
## Thurston relaxation: SDP as a hyperbolic Newton solver

Once the two vortex cores merge inside a tubular neighbourhood $U \subset M$, the operative geometry is the complement $U \setminus K$. Thurston's hyperbolisation programme proves that, excluding a finite list of exceptions, $U \setminus K$ admits a complete finite-volume hyperbolic structure. A triangulation into ideal tetrahedra $\Delta_{z_k}$ and a system of *gluing equations* in the shape parameters $z_k$ encode this structure.

The algebraic SDP solver of [Chapter 12](#chap:particle-interactions) is **not separate from the hyperbolic-geometry calculation**. It is its $\mathbb{Z}[q^{\pm 1/2}]$-shadow. We establish this via three correspondences:

* **Cusps from poles.** The roots of the $q$-Pochhammer denominator $\Phi_n(x; q) = \prod_{k=0}^{n-1}(1 - x q^k)^{-1}$ seed the Frobenius positivity constraints in the SDP. These roots are in bijection with the ideal vertices of the tetrahedral triangulation of the $\Phi_q$-piece $K_S$ ([pole-to-cusp bijection](#conj:algebraic-geometric-dilog-equivalence)(1)).
* **Newton iteration on the gluing equations.** The Newton solver for Thurston's gluing equations (e.g. SnapPy) seeds from these poles and converges to the shape parameters $z_k$ realising the complete hyperbolic structure. The same algebraic-residue data feeds both the SDP and the gluing solver; they are different *evaluations* of one categorical object.
* **Steepest descent.** On the Archimedean side, the residue sum becomes the Picard--Lefschetz thimble decomposition of the Seiberg--Witten action $S(z)$ (thimble). The Gröbner--Shirshov reduction depth maps to the number of ideal tetrahedra used in the triangulation (GB--PL bijection). The SDP's complementary-slackness rank equals the number of thimble flows realising the optimum.

In short: **two knots settle into the lowest-energy operator because that operator is the unique fixed point of Newton iteration on the Thurston gluing equations seeded by the $q$-Pochhammer poles, and that fixed point is the Archimedean realisation of the SDP optimum**. The algebraic and geometric solvers are two faces of the same computation. The [Archimedean realization functor](#def:archimedean-realization-functor) acts as the explicit translator between them.

The next remark details why this functions as the "hyperbolic relaxation" picture, mapping SDP dual variables to thimble depths.
<!-- FILE_END: thurston-relaxation.md -->

<!-- FILE_START: briggs-klein-chart.md -->
Let $r=\lvert w_1\rvert^2$ denote the squared modulus of the first resolvent coordinate on Bring's surface ([Bring's surface](#def:brings-surface)). The **Briggs--Klein affine chart** is the coordinate system $(w_1,w_2)$ restricted to the open set $0<r<\infty$. It carries the Hermitian metric inherited from the Fubini--Study metric on $\mathbb{P}^4$. In this chart, the $C_5$ action acts as the phase rotation $w_k\mapsto\zeta^kw_k$, rendering the radial coordinate $r$ invariant under $C_5$.
<!-- FILE_END: briggs-klein-chart.md -->

<!-- FILE_START: radial-projection.md -->
We restrict a Briggs--Klein affine chart ([Briggs--Klein chart](#def:briggs-klein-chart)) to the interval $r\in(0,1)$ and project Bring's surface onto this radial coordinate. This yields a fibration over the base manifold $M$ with trivial bundle $\mathcal{S}=\mathcal{S}_0$. At each $r$, the coordinate $w_1$ restricts to a circle of radius $\sqrt{r}$ in the complex plane $\mathbb{C}_{w_1}$. This circle constitutes the orbit of the $C_5$ symmetry: the rotation $w_1\mapsto\zetaw_1$ moves the point along this circle without altering $r$.
<!-- FILE_END: radial-projection.md -->

<!-- FILE_START: four-colourability.md -->
By the Heawood bound, an orientable surface of genus $g$ has chromatic number at most $\lfloor(7+\sqrt{1+48g})/2\rfloor$. For genus $4$, this bound equals $10$. Bring's surface, however, admits a proper colouring with only four colours. This low chromatic number reflects the high degree of symmetry. The $S_5$ automorphism group constrains the combinatorics of any cell decomposition, forcing a more efficient colouring than a generic genus-$4$ surface permits.
<!-- FILE_END: four-colourability.md -->

<!-- FILE_START: four-colour-theorem.md -->
The classical four-colour theorem dictates that every planar graph is four-colourable. For higher-genus surfaces, the chromatic number grows as $O(\sqrt{g})$ (Heawood conjecture, proved by Ringel--Youngs). That Bring's surface attains the planar bound of four at genus $4$ reflects the rigidity imposed by its $S_5$ symmetry. In the Descartes universe, the trivial bundle $\mathcal{S}=\mathcal{S}_0$ ([radial projection](#rem:radial-projection)) carries no torsion. The resulting flatness of the tessellation forces the same chromatic economy as the sphere.
<!-- FILE_END: four-colour-theorem.md -->

<!-- FILE_START: cyclotomic-reduction.md -->
Let $\mathfrak{p}$ be a prime (not to be confused with a point $p\in M$). Working over the cyclotomic ring

```tex
\begin{equation}\label{eq:cyclotomic-ring}
  \mathbb{Z}_{\zeta_{\mathfrak{p}}}
   := \mathbb{Z}[i,\zeta_{\mathfrak{p}}],
\end{equation}
```

where $\zeta_{\mathfrak{p}}=e^{2\pi i/\mathfrak{p}}$ is a primitive $\mathfrak{p}$-th root of unity, we examine the sublocus

$$
  S_{\mathfrak{p}}
   := 
  \Sigma_4\cap\mathbb{Z}_{\zeta_{\mathfrak{p}}}^{5}.
$$

This defines the set of points on Bring's surface whose resolvent coordinates lie in $\mathbb{Z}_{\zeta_{\mathfrak{p}}}$. The cyclic subgroup $C_{\mathfrak{p}}\subset S_5$ generated by the $\mathfrak{p}$-cycle preserves $S_{\mathfrak{p}}$. For any $P\in S_{\mathfrak{p}}$, the image $\sigma^k(P)$ remains in $\mathbb{Z}_{\zeta_{\mathfrak{p}}}^{5}$ because $\sigma$ multiplies by $\zeta_{\mathfrak{p}}^{-k}$ in the resolvent basis ([Lagrange resolvents](#rem:lagrange-resolvents)), and $\zeta_{\mathfrak{p}}^{-k}\in\mathbb{Z}_{\zeta_{\mathfrak{p}}}$. This arithmetic compatibility between the cyclic symmetry and the cyclotomic ring underscores the descent of the $C_5$ action to finite characteristic.
<!-- FILE_END: cyclotomic-reduction.md -->
