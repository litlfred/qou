The three color tubes of the Bring's surface ([color tube interpretation](#rem:color-tube-interpretation)) and the three $S_3$ subgroups of its automorphism group ([chirality of the trefoil](#rem:chirality-trefoil)) form a categorical basis for the color space. This basis fails to span all colors with positive coefficients. This geometric restriction constitutes the topological origin of color confinement.

**The chromaticity problem.**

Classical color theory \cite{feynman1963} defines a coordinate system from any three primary colors $(r, g, b)$. No three primaries span the entire space of perceived colors with strictly positive coefficients. The spectral locus forms an irregularly curved region, but three primaries span only a flat triangle. This triangle necessarily excludes parts of the gamut, requiring negative coefficients for complete coverage.

This reflects the intrinsic geometry of the color space rather than a deficient choice of primaries. The spectral locus lies outside any triangular cone.

**The $q$-deformed color space.**

In the Descartes universe, the Skein module $\mathrm{Sk}_q(\mathbf{C})$ constitutes the color space. The three color tubes $(r, g, b) = (w_2 - z, w_3 - z, w_4 - z)$ supply the primary directions. Every element of $\mathrm{Sk}_q$ expands as a formal linear combination of knot types with $q$-polynomial coefficients.

The Skein relation

$$
  q  [L_+] - q^{-1} [L_-]
  = (q^{1/2} - q^{-1/2}) [L_0]
$$

enforces **negative coefficients** into the expansion. The term $-q^{-1}[L_-]$ introduces unavoidable negativity. This provides the $q$-deformed analogue of chromaticity negativity. At $q = 1$, the relation evaluates to $[L_+] - [L_-] = 0$ and the negativity vanishes. For physical values $q \neq 1$, negative Skein coefficients remain mandatory.

**Three primaries, three trefoils, three $S_3$ subgroups.**

The automorphism group $S_5$ of Bring's surface contains exactly three copies of $S_3$. Each $S_3$ arises as the quotient of the trefoil knot group $\langle x, y \mid x^2 = y^3 \rangle$ restricted to a single color sector. These three $S_3$ subgroups serve as the primaries of the categorical color space:

| Color | $S_3$ subgroup | Trefoil copy | Color coordinate |
|-------|---------------|-------------|-----------------|
| Red | $S_3^{(r)} \leq S_5$ | $T_{2,3}^{(r)}$ | $c_r = w_2 - z$ |
| Green | $S_3^{(g)} \leq S_5$ | $T_{2,3}^{(g)}$ | $c_g = w_3 - z$ |
| Blue | $S_3^{(b)} \leq S_5$ | $T_{2,3}^{(b)}$ | $c_b = w_4 - z$ |

Each $S_3$ acts on one color fiber. Elements of $S_5$ outside all three $S_3$ subgroups conjugate the subgroups, permuting the three color sectors. This $S_5$ permutation action yields the color permutation symmetry of QCD.

**Necessity of confinement.**

Just as spectral colors require negative primary coefficients, some Skein elements carry negative coefficients in the color-tube basis.

An individual quark is an unknot strand carrying one crossing letter within a single color tube; the trefoil $T_{2,3}$ is the lepton partner of $\mathfrak{u}$ and $\mathfrak{d}$, not their knot type. This primary color fails to span the full Skein module with positive coefficients. Generic physical processes resolve into Skein sums containing $-q^{-1}$ factors. These terms hold physical meaning only upon evaluation of the complete Skein sum. Isolated evaluation of a single color component yields a meaningless negative probability.

Confinement resolves this negativity. Combinations invariant under all three $S_3$ subgroups remain invariant under the full $S_5$ color permutation. Only these color-neutral combinations guarantee positive evaluations under the fibre functor:

$$
  \tau \colon \mathrm{Sk}_q(\mathbf{C}) \to \mathbb{R}_{\geq 0}.
$$

The map $\tau$ ensures positivity exclusively on the $S_5$-invariant submodule. Individual color components risk negative values, exactly as chromaticity coefficients become negative for spectral colors outside the primary triangle.

**The role of $T_{2,9}$.**

The three-fold cover $T_{2,9}$ ([force identification](#rem:force-knot-identification)) enforces this positivity. By interpolating all three color tubes along a single closed curve, $T_{2,9}$ binds the components into an $S_5$-invariant whole. Unbound trefoils permit isolated, potentially negative evaluations. The $T_{2,9}$ binding yields an unconditionally positive $S_5$-invariant configuration.

Confinement emerges structurally from this torus knot architecture. A physical color-mixing apparatus requires all three primaries to synthesize a visible result. Similarly, $T_{2,9}$ wraps the three primary quarks into a closed, observable system.

**$q$-chromaticity coordinates.**

Following the CIE chromaticity diagram, the $q$-chromaticity coordinates of a Skein element $\psi \in \mathrm{Sk}_q$ normalize the $q$-coefficients $a_r, a_g, a_b$:

$$
  (\hat{c}_r, \hat{c}_g, \hat{c}_b)
  = 
  \frac{(a_r, a_g, a_b)}{a_r + a_g + a_b}.
$$

These coordinates sum to unity, spanning the $q$-simplex chromaticity triangle.

Color-neutral hadron states sit at the centroid $\hat{c}_r = \hat{c}_g = \hat{c}_b = 1/3$. Individual quarks push some coordinates above $1$ and drive others negative. These states fall outside the physical triangle, mirroring spectral colors outside a primary gamut.

The physical gamut containing all strictly positive $\tau$-evaluations forms a $q$-deformed convex region inscribed within the triangle. The $q$-spectral locus bounds this region, formed by the $q$-chromaticity projection of pure knot types. At $q = 1$, the gamut fills the entire triangle, rendering confinement unnecessary. At the physical substrate parameter $q$, the gamut shrinks. It excludes individual colors and admits only confined, near-centroid combinations.
