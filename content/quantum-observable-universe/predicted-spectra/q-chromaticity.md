The three coral tubes of the Bring's surface
([color tube interpretation](#rem:color-tube-interpretation)) and
the three $S_3$ subgroups of its automorphism group
([chirality of the trefoil](#rem:chirality-trefoil)) provide a
categorical basis for the color space.  The structure of this
basis — specifically, its failure to span all "colors" with
positive coefficients — is the topological origin of color
confinement.

**The chromaticity problem.**

In classical color theory \cite{feynman1963}, any choice of three
primary colors $(r, g, b)$ defines a coordinate system for the
space of perceived colors.  A central fact is that **no three
primaries suffice with only positive coefficients**: some spectral
colors require negative amounts of at least one primary.  The
visible gamut is the convex hull of the spectral locus — an
irregularly curved region — while any three primaries span only a
triangle.  The triangle always leaves part of the gamut outside,
accessible only via negative coefficients.

This is not a deficiency of a particular choice of primaries; it
is a theorem about the geometry of the color space: the spectral
locus is not contained in any triangular cone.

**The $q$-deformed color space.**

In the Descartes universe, the "color space" is the Skein module
$\mathrm{Sk}_q(\mathbf{C})$.  The three coral tubes
$(r, g, b) = (w_2 - z, w_3 - z, w_4 - z)$ provide three
distinguished directions — the "primaries" of the categorical
color space.  An arbitrary element of $\mathrm{Sk}_q$ is a formal
linear combination of knot types with $q$-polynomial coefficients.

The Skein relation

$$
  q  [L_+] - q^{-1} [L_-]
  = (q^{1/2} - q^{-1/2}) [L_0]
$$

forces **negative coefficients** into the expansion: the term
$-q^{-1}[L_-]$ is unavoidable.  This is the $q$-deformed analogue
of the chromaticity negativity.  At $q = 1$, the relation becomes
$[L_+] - [L_-] = 0$ and the negativity vanishes — but at $q \neq 1$
(the physical Descartes universe), negative Skein coefficients are
mandatory.

**Three primaries, three trefoils, three $S_3$ subgroups.**

The automorphism group $S_5$ of Bring's surface contains exactly three
copies of $S_3$, each the quotient of the trefoil knot group
$\langle x, y \mid x^2 = y^3 \rangle$ restricted to one color
sector.  These three $S_3$ subgroups are the "primaries" of the
categorical color space:

| Color | $S_3$ subgroup | Trefoil copy | Color coordinate |
|-------|---------------|-------------|-----------------|
| Red | $S_3^{(r)} \leq S_5$ | $T_{2,3}^{(r)}$ | $c_r = w_2 - z$ |
| Green | $S_3^{(g)} \leq S_5$ | $T_{2,3}^{(g)}$ | $c_g = w_3 - z$ |
| Blue | $S_3^{(b)} \leq S_5$ | $T_{2,3}^{(b)}$ | $c_b = w_4 - z$ |

Each $S_3$ acts on one color fiber.  The elements of $S_5$ that
lie *outside* all three $S_3$ subgroups act by **conjugation**,
permuting the three color sectors among themselves — this is the
$S_5$-theoretic origin of the color permutation symmetry of QCD.

**Why confinement is necessary.**

In Feynman's language: some spectral colors lie outside the triangle
of primaries, requiring negative coefficients.  In QOU language:
some Skein elements have negative coefficients in the coral-tube
basis.

An individual quark — a trefoil $T_{2,3}$ in a single coral tube —
is a "primary color."  It does not span the full Skein module with
positive coefficients.  The Skein resolution of a physical process
generically produces terms with $-q^{-1}$ factors, which are
interpretable only when the full Skein sum is evaluated.  A single
color component, evaluated in isolation, can yield a negative
"probability" — physically meaningless.

The resolution is **confinement**: only **color-neutral**
combinations — those invariant under all three $S_3$ subgroups,
hence under the full $S_5$ color permutation — yield positive
evaluations under the fibre functor $\tau$.  The fibre functor
maps the Skein module to non-negative reals:

$$
  \tau \colon \mathrm{Sk}_q(\mathbf{C}) \to \mathbb{R}_{\geq 0}
$$

but this map is positive only on the **$S_5$-invariant** submodule.
On individual color components, $\tau$ can produce negative values
— exactly as a chromaticity coefficient can be negative for a
spectral color outside the primary triangle.

**The role of $T_{2,9}$.**

The three-fold cover $T_{2,9}$
([force identification](#rem:force-knot-identification)) is the
topological agent that enforces positivity.  By interpolating all
three coral tubes in a single closed curve, $T_{2,9}$ provides
the binding that makes the full Skein sum $S_5$-invariant.  Without
$T_{2,9}$, the three trefoil copies could be evaluated separately
(in which case negative coefficients are possible); with $T_{2,9}$,
they are bound into a single $S_5$-invariant configuration whose
$\tau$-evaluation is guaranteed non-negative.

This is the precise sense in which confinement follows from the
torus knot architecture: $T_{2,9}$ wraps the three primaries into a
closed system, just as a physical color-mixing apparatus must
combine all three primaries to produce a visible (positive-intensity)
result.

**$q$-chromaticity coordinates.**

By analogy with the CIE chromaticity diagram, define the
$q$-chromaticity coordinates of a Skein element
$\psi \in \mathrm{Sk}_q$:

$$
  (\hat{c}_r, \hat{c}_g, \hat{c}_b)
  = 
  \frac{(a_r, a_g, a_b)}{a_r + a_g + a_b}
$$

where $a_r, a_g, a_b$ are the $q$-coefficients of $\psi$ in the
three coral tubes.  These satisfy $\hat{c}_r + \hat{c}_g + \hat{c}_b = 1$,
The $q$-chromaticity diagram is a triangle (the $q$-simplex).

For color-neutral states (hadrons): $\hat{c}_r = \hat{c}_g = \hat{c}_b = 1/3$
— the white point at the centroid.  For individual quarks, some
coordinates exceed $1$ and others are negative — these points lie
outside the physical triangle, just as spectral colors lie outside
the gamut of any three primaries.

The **physical gamut** — the set of states with all-positive
$\tau$-evaluation — is a $q$-deformed convex region inscribed in
the triangle.  Its boundary is the **$q$-spectral locus**, the
image of the pure knot types under the $q$-chromaticity projection.
At $q = 1$, this region fills the entire triangle (no confinement
needed); at the substrate parameter $q$, it shrinks, excluding individual colors
and admitting only near-centroid (confined) combinations.
