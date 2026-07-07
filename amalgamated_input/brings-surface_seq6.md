<!-- FILE_START: brings-smoothness-intro.md -->
The color fibration of the previous section is well-defined
generically, but the geometry needs a smooth bundle to support the
spectral resolvents that follow. Remark: Color space as spectral curve and spinor bundle packages the color data as a spectral
curve carrying a spinor bundle, and Proposition: Smoothness of the Bring's surface and intrinsic resolution of projection singularities
together with Proposition: Smoothness of Bring's surface and resolution of spacetime defects establish that Bring's surface is smooth
and that its projection singularities resolve intrinsically — no
external blow-up is required.

The base-to-fibre interpretation occupies the middle of the section.
The exceptional-divisor and Thurston-relaxation expositions situate
the base manifold $M$ and the brane-point fibres $\mathcal{S}_p$
inside the same geometric data, and Definition: Briggs–Klein affine chart fixes a working affine chart for explicit computation.
Definition: Radial projection of Bring's surface is the chart's
geometric counterpart. Proposition: Four-colourability of Bring's surface and Remark: The four-colour theorem and Bring's surface
record the structural compatibility with the three color tubes plus
ambient color, and Remark: Cyclotomic reduction and $C_{\mathfrak{p}}$ preservation is the input the next section, spectral
resolvents and gauge structures, takes as given: the reduction
modulo cyclotomic primes that defines the resolvent basis.

_(draft.)_
<!-- FILE_END: brings-smoothness-intro.md -->

<!-- FILE_START: color-bundles.md -->
The spacetime--color decomposition of Bring's surface maps accordingly onto
three classical bundle structures over the $\mathbb{P}^1(\mathbb{C})$ base $z=x_0/x_1$.

**Cotangent bundle.**
The three-sheeted cubic ([color elliptic curve](#prop:color-elliptic)) realises the color
variables $X=(x_2,x_3,x_4)$ as a *spectral curve*
$\Sigma\subset T^{*}\mathbb{P}^1(\mathbb{C})$: the base coordinate $z$ parametrises
spacetime position, and the three roots $X_1,X_2,X_3$ of
[color elliptic curve](#prop:color-elliptic) are eigenvalues of a Higgs-like
field $\Phi$ on the base. The six singular fibres (where the discriminant
$\Delta(z)$ vanishes) are the loci at which eigenvalues coincide and the
differential $dX$ degenerates in the cotangent fibre.

**Spinor bundle.**
The spectral modes $w_1,\dots,w_4$
([Lagrange resolvents](#rem:lagrange-resolvents)) live in a rank-$2$ complex vector
bundle over $\mathbb{P}^1(\mathbb{C})$. The color doublet
$\Psi_L=(w_1,w_2)^T$ and its conjugate $\Psi_R=(w_4,w_3)^T$ transform
under the $\mathrm{SU}(2)$ holonomy generators
$H_1,H_2$ of
[holonomy of trefoil](#rem:holonomy-trefoil), making $\Psi_L$ a section of the
*spinor bundle* $\mathcal{S}^{+}\to\mathbb{P}^1(\mathbb{C})$. The $B_3$
monodromy equips this bundle with a flat connection whose holonomy is the
trefoil-knot group.

**Adjoint bundle.**
The $\mathrm{SO}(3)$ images $R_\alpha,R_\beta$
act on the triple $(\omega_1,\omega_2,\omega_3)$, which therefore spans a
section of the adjoint bundle $\mathrm{ad}P\to\mathbb{P}^1(\mathbb{C})$ associated
to the principal $\mathrm{SU}(2)$-bundle $P$. The T-duality involution
$\iota\colon X\leftrightarrow z$ ([T-duality on elliptic fibres](#rem:t-duality-elliptic))
interchanges the fibre and base of the adjoint bundle, exchanging
spectral eigenvalues with spacetime coordinates.
<!-- FILE_END: color-bundles.md -->

<!-- FILE_START: brings-smoothness-resolution.md -->
**Proposition.**
Let $\mathcal{S}$ denote the Bring's surface
([Bring's surface](#def:brings-surface)) and
$\pi \colon \mathcal{S} \to \mathbb{P}^1(\mathbb{C})$ the color projection.

1. **Smoothness.** The three power-sum constraints are transverse in
   $\mathbb{P}^4$, so $\mathcal{S}$ is a smooth algebraic variety with
   no singular points.

2. **Intrinsic resolution.** At each branch point $z = z_c$ where two
   color sheets $x_i, x_j$ collide, the local color coordinate
   $\delta = x_i - x_j$ satisfies $z - z_c \sim \delta^2$.  The
   exceptional divisor of the blow-up at each ramification point is
   already embedded in the color coordinates: no external resolution
   is required.

3. **Regularity of the Briggs--Klein chart.** The radial parameter
   $r = \lvert w_1 \rvert^2$ is a regular function on $\mathcal{S}$,
   and the $C_5$ orbits $w_k \mapsto \zeta^k w_k$ foliate the surface
   without fixed points for $0 < r < \infty$.
<!-- FILE_END: brings-smoothness-resolution.md -->

<!-- FILE_START: brings-smoothness.md -->
The Bring's surface $\mathcal{S}$ ([Bring's surface](#def:brings-surface)) is a
*smooth* algebraic variety: the three power-sum constraints are
transverse in $\mathbb{P}^4$, so their intersection carries no singular
points.  The six topological defects identified in
[color bundles](#rem:color-bundles)---where the discriminant $\Delta(z)$
vanishes and two color sheets $X_i,X_j$ collide---are singularities of
the *projection* $\pi\colon\mathcal{S}\to\mathbb{P}^1(\mathbb{C})$, not of the
surface itself.

**Resolution in the $x_j$ coordinates.**
At a branch point $z=z_c$ where, say, $x_2=x_3$, define the local color
coordinate $\delta=x_2-x_3$.  In a neighbourhood of the defect the
spacetime ratio satisfies

$$
  z-z_c \sim \delta^2,
$$

so while the projection map develops a ramification cusp, $\delta$ passes
smoothly through zero, carrying the geometry from one sheet to the other.
The exceptional divisor of the blow-up at each branch point is therefore
already embedded in the color coordinates $x_2,x_3,x_4$: no external
resolution is required.

**Resolution in the $w_k$ coordinates.**
The DFT mixes all five $x_j$ into every resolvent $w_k$
([Lagrange resolvents](#rem:lagrange-resolvents)), so no single $w_k$ vanishes at a
branch point.  The Briggs--Klein chart
([Briggs--Klein chart](#def:briggs-klein-chart)) remains a smooth coordinate
system throughout $0<r<\infty$: the radial parameter $r=\lvert w_1\rvert^2$
is a regular function on $\mathcal{S}$, and the $C_5$ orbits
$w_k\mapsto\zeta^k w_k$ foliate the surface without fixed points.  The
infinite torsion and eigenvalue crossings visible in the base
$\mathbb{P}^1(\mathbb{C})$ are artefacts of projecting away the internal degrees of
freedom that the $w_k$ retain.
<!-- FILE_END: brings-smoothness.md -->

<!-- FILE_START: approach-to-exceptional-divisor.md -->
## Approach: from base $M$ to fibre $\mathcal{S}_p$

In the QOU archimedean tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$
the base manifold $M$ carries the smooth metric in which two
free vortices propagate. As the vortex cores approach a brane
point $p \in M$, the smooth metric becomes degenerate: the
base coordinate ratio $z = \sqrt{q} - 1/\sqrt{q}$ drives the
exceptional divisor $\mathcal{S}_p$
([state bundle fibre](#def:exceptional-divisor)) into the
foreground.  *"Below Planck scale"* in QOU is therefore not a
metric statement (there is no metric below Planck) but a
**categorical** one: the relevant geometry has switched from the
base $M$ to the fibre $\mathcal{S}_p$, and morphisms in
$\mathcal{S}_p$ are knot operators
([knot-operator energy](#def:knot-operator-energy)).

Concretely, the encounter has three moments:

1. **Approach.**  Two vortex tubes propagate on $M$ and approach
   a common brane point $p$.  The Reeb flow on $M$ does the
   accounting; nothing new is needed.

2. **Crossing onto the fibre.**  At the threshold where
   $\partial F / \partial \mathbf{c} = 0$ on the colour-tube
   cubic (Picard--Lefschetz thimble
   §setup), the base coordinate $z$ hits a discriminant zero,
   the smooth base structure pinches, and the operative
   morphisms are now those of $\mathcal{S}_p$ — the
   $\Phi_q$-piece $K_S$
   ([$\Phi_q$-piece](#def:phi-q-piece)).

3. **Merging of fundamental groups.**  The two vortex cores
   become parallel strands in a single braid.  Their previously
   independent fundamental groups
   $\pi_1(\nu_1)$, $\pi_1(\nu_2)$ amalgamate into the
   fundamental group $\pi_1(U \setminus K)$ of the merged knot
   complement, where $U$ is a tubular neighbourhood of $p$ and
   $K$ is the link formed by the two strands inside it.

After moment (3) the encounter is a knot-theoretic question, not
a metric one.  The remaining sections of this chapter trace what
happens next: the merged complement admits a hyperbolic
structure ([Thurston relaxation](#sec:thurston-relaxation)), the
SDP/LP machinery of [Chapter 12](#chap:particle-interactions)
selects the lowest-energy link representative
(SDP as thimble flow), and Mostow
rigidity (geometric confinement)
makes the resulting topology --- and hence the mass --- discrete.
<!-- FILE_END: approach-to-exceptional-divisor.md -->

<!-- FILE_START: thurston-relaxation.md -->
## Thurston relaxation: SDP as a hyperbolic Newton solver

Once the two vortex cores have merged inside a tubular
neighbourhood $U \subset M$ of the encounter point, the
operative geometry is the complement $U \setminus K$, where $K$
is the link formed by the merged strands.  Thurston's
hyperbolisation programme tells us that, away from a finite list
of exceptional cases, $U \setminus K$ admits a complete
finite-volume hyperbolic structure, encoded by a triangulation
into ideal tetrahedra $\Delta_{z_k}$ and a system of *gluing
equations* in the shape parameters $z_k$.

The point of this section is that the algebraic SDP solver of
[Chapter 12](#chap:particle-interactions) is **not separate from
the hyperbolic-geometry calculation** — it is its
$\mathbb{Z}[q^{\pm 1/2}]$-shadow.  We make this precise in three
correspondences, each already established (or stated) elsewhere
in the manuscript:

* **Cusps from poles.** The roots of the $q$-Pochhammer
  denominator
  $\Phi_n(x; q) = \prod_{k=0}^{n-1}(1 - x q^k)^{-1}$
  --- which are the natural seeds of the Frobenius
  positivity constraints in the SDP --- are in bijection with
  the ideal vertices of the tetrahedral triangulation of the
  $\Phi_q$-piece $K_S$.  This is the
  [pole-to-cusp bijection](#conj:algebraic-geometric-dilog-equivalence)
  (1).

* **Newton iteration on the gluing equations.** The Newton solver
  used numerically to solve Thurston's gluing equations (e.g. by
  SnapPy) starts from these pole-derived seeds and converges to
  the shape parameters $z_k$ realising the complete hyperbolic
  structure.  The same algebraic-residue data feeds the SDP and
  the gluing solver; the two computations are different
  *evaluations* of one categorical object.

* **Steepest descent.** On the Archimedean side, the residue sum
  becomes the Picard--Lefschetz thimble decomposition of the
  Seiberg--Witten action $S(z)$
  (thimble); the Gröbner--Shirshov
  reduction depth maps to the number of ideal tetrahedra used in
  the triangulation
  (GB--PL bijection).
  The SDP's complementary-slackness rank equals the number of
  thimble flows realising the optimum.

In one sentence: **two knots settle into the lowest-energy
operator because that operator is the unique fixed point of
Newton iteration on the Thurston gluing equations seeded by the
$q$-Pochhammer poles, and that fixed point is the Archimedean
realisation of the SDP optimum**.  The algebraic and geometric
solvers are two faces of the same computation; the
[Archimedean realization functor](#def:archimedean-realization-functor)
is the explicit translator between them.

The interpretive content of *why* this is the
"hyperbolic relaxation" picture --- with the SDP dual variables
appearing as thimble depths --- is collected in the next remark.
<!-- FILE_END: thurston-relaxation.md -->

<!-- FILE_START: briggs-klein-chart.md -->
Let $r=\lvert w_1\rvert^2$ denote the squared modulus of the first resolvent
coordinate on
([Bring's surface](#def:brings-surface)).  The
**Briggs--Klein affine chart** is the coordinate system $(w_1,w_2)$
restricted to the open set $0<r<\infty$, equipped with the Hermitian metric
inherited from the Fubini--Study metric on $\mathbb{P}^4$.  In this chart
the $C_5$ action is the phase rotation $w_k\mapsto\zeta^kw_k$, and the
radial coordinate $r$ is $C_5$-invariant.
<!-- FILE_END: briggs-klein-chart.md -->

<!-- FILE_START: radial-projection.md -->
Restricting a Briggs--Klein affine chart
([Briggs--Klein chart](#def:briggs-klein-chart)) to the interval $r\in(0,1)$ and
projecting Bring's surface onto this radial coordinate yields a fibration
over the base manifold $M$ with trivial bundle $\mathcal{S}=\mathcal{S}_0$.  At each
$r$, the coordinate $w_1$ is restricted to a circle of radius $\sqrt{r}$ in
the complex plane $\mathbb{C}_{w_1}$.  This circle is the orbit of the $C_5$
symmetry: the rotation $w_1\mapsto\zetaw_1$ moves the point along this
circle without changing $r$.
<!-- FILE_END: radial-projection.md -->

<!-- FILE_START: four-colourability.md -->
By the Heawood bound, an orientable surface of genus $g$ has chromatic number
at most $\lfloor(7+\sqrt{1+48g})/2\rfloor$.  For genus $4$ this bound
equals $10$.  Bring's surface, however, admits a proper colouring with only
four colours --- considerably fewer than the maximum permitted by its genus.
This low chromatic number reflects the high degree of symmetry: the $S_5$
automorphism group constrains the combinatorics of any cell decomposition,
forcing a more efficient colouring than a generic genus-$4$ surface would
require.
<!-- FILE_END: four-colourability.md -->

<!-- FILE_START: four-colour-theorem.md -->
The classical four-colour theorem asserts that every planar graph (equivalently,
every graph embeddable in $S^2$) is four-colourable.  For higher-genus
surfaces the chromatic number can be much larger: the Heawood conjecture
(proved by Ringel--Youngs for $g\geq 1$) shows that the maximum chromatic
number grows as $O(\sqrt{g})$.  That Bring's surface attains the planar
bound of four --- despite living at genus $4$ --- is a reflection of the
rigidity imposed by its $S_5$ symmetry.  In the language of the Descartes
universe, the trivial bundle $\mathcal{S}=\mathcal{S}_0$
([radial projection](#rem:radial-projection)) carries no torsion, and the resulting
flatness of the tessellation forces the same chromatic economy as the
sphere.
<!-- FILE_END: four-colour-theorem.md -->

<!-- FILE_START: cyclotomic-reduction.md -->
Let $\mathfrak{p}$ be a prime (not to be confused with a point $p\in M$).
Working over the cyclotomic ring

```tex
\begin{equation}\label{eq:cyclotomic-ring}
  \mathbb{Z}_{\zeta_{\mathfrak{p}}}
   := \mathbb{Z}[i,\zeta_{\mathfrak{p}}],
\end{equation}
```

where $\zeta_{\mathfrak{p}}=e^{2\pi i/\mathfrak{p}}$ is a primitive
$\mathfrak{p}$-th root of unity, consider the sublocus

$$
  S_{\mathfrak{p}}
   := 
  \Sigma_4\cap\mathbb{Z}_{\zeta_{\mathfrak{p}}}^{5},
$$

that is, the set of points on Bring's surface whose resolvent coordinates
lie in $\mathbb{Z}_{\zeta_{\mathfrak{p}}}$.  The cyclic subgroup
$C_{\mathfrak{p}}\subset S_5$ generated by the $\mathfrak{p}$-cycle preserves
$S_{\mathfrak{p}}$: for any $P\in S_{\mathfrak{p}}$, the image
$\sigma^k(P)$ remains in $\mathbb{Z}_{\zeta_{\mathfrak{p}}}^{5}$ because
$\sigma$ acts by multiplication by $\zeta_{\mathfrak{p}}^{-k}$ in the
resolvent basis ([Lagrange resolvents](#rem:lagrange-resolvents)), and
$\zeta_{\mathfrak{p}}^{-k}\in\mathbb{Z}_{\zeta_{\mathfrak{p}}}$.  This
arithmetic compatibility between the cyclic symmetry and the cyclotomic ring
underlies the :refterm[descent]{#descent} of the $C_5$ action to finite characteristic.
<!-- FILE_END: cyclotomic-reduction.md -->

