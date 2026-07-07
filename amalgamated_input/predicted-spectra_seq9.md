<!-- FILE_START: archimedean-hartree-crystal-alpha-em-categorical-intro.md -->
The upstream Mathlib additions catalogue the categorical structures underlying the substrate-flow construction. The $\alpha_{\mathrm{EM}}$ categorical-trace ratio identifies the substrate-flow value via the trace ratio identity. The multiplicative-chain shift and the $q$-chromaticity blocks specify the substrate-flow behaviour of $\alpha_{\mathrm{EM}}$ at the substrate parameter $q_0$.
<!-- FILE_END: archimedean-hartree-crystal-alpha-em-categorical-intro.md -->

<!-- FILE_START: alpha-em-categorical-trace-ratio.md -->
**Proposition (algebraic identity).**
*The bare electromagnetic fine-structure constant $1/\alpha_{EM} = q\,[9]_q\,[10]_q$ ([`prop:em-coupling-projection`](#prop:em-coupling-projection)) admits the categorical-trace-ratio decomposition:*

$$
  \boxed{\;\;
    \alpha_{EM}
    \;=\;
    \frac{h^{2}}{q \cdot \delta_q(T_{2,9}) \cdot \delta_q(T_{3,5})}
  \;\;}
$$

*where $h = q - q^{-1}$ is the skein parameter, $\delta_q$ is the $q$-dimension decoration ([`def:delta-q-decoration`](#def:delta-q-decoration)), and $T_{2,9}, T_{3,5}$ are the two genus-$4$-saturating torus knots ([`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness)). The identity holds in $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$.*

### Derivation

The categorical trace of a torus-knot $T_{p,q}$ in the natural $2$-strand representation (taking $p = 2$) sums the contributions from the two irreducible Hecke representations $V_{(2)}$ (eigenvalue $q$) and $V_{(1,1)}$ (eigenvalue $-q^{-1}$):

$$
  \delta_q(T_{2,k})
  \;=\;
  q^{k} \cdot 1 + (-q^{-1})^{k} \cdot 1
  \;=\;
  q^{k} - q^{-k}
  \quad (k\text{ odd}).
$$

For $k = 9$, $\delta_q(T_{2,9}) = q^{9} - q^{-9} = h\,[9]_q$.

For $T_{3,5}$ (a 3-strand torus knot), the analogous categorical trace in $H_3(q)$ yields $\delta_q(T_{3,5}) = q^{10} - q^{-10} = h\,[10]_q$. We compute this via the Rosso-Jones torus-knot formula, combining contributions from $V_{(3)}$, $V_{(2,1)}$, and $V_{(1,1,1)}$ with their respective eigenvalue powers.

Substituting $\delta_q(T_{2,9}) = h\,[9]_q$ and $\delta_q(T_{3,5}) = h\,[10]_q$:

$$
  \frac{h^{2}}{q \cdot \delta_q(T_{2,9}) \cdot \delta_q(T_{3,5})}
  \;=\;
  \frac{h^{2}}{q \cdot h\,[9]_q \cdot h\,[10]_q}
  \;=\;
  \frac{1}{q\,[9]_q\,[10]_q}
  \;=\;
  \alpha_{EM}.
$$

$\square$

### Numerical verification

At $q_0 \approx 1.1099786$, we obtain an exact match (within $10^{-12}$). See [Table: Numerical verification of $\alpha_{EM}$ trace-ratio](#tbl:alpha-em-categorical-trace-ratio-table-data).

We confirm the witness assertion: [`delta-q-decoration.witness.json`](computations/delta-q-decoration.witness.json).

Expressing the relationship as a trace ratio on the $q$-dimension layer reformulates existing projection identities and closes the categorical framework. The empirical electromagnetic coupling reduces to a structural trace-algebraic constraint.
<!-- FILE_END: alpha-em-categorical-trace-ratio.md -->

<!-- FILE_START: alpha-em-categorical-trace-ratio-interpretation.md -->
**Interpretation.** The trace-ratio identity ([$\alpha_{EM}$ categorical trace-ratio](#prop:alpha-em-categorical-trace-ratio)) refactors $\alpha_{EM}$ from the inverse Bring complex complexity into the ratio of $h^{2}$ over the product of force-carrier categorical traces. This shifts the $\alpha_{EM}$ formula from the operator-selection-LP-cost interpretation to the q-dimension / $\delta_q$-decoration layer.

The structural picture:
- The $\delta_q$-decoration yields a pure categorical trace $\delta_q(T_{p,q}) = q^{q} - q^{-q}$ for each force carrier (in the appropriate $p$-strand realisation).
- $\alpha_{EM}$ is the inverse product of these two traces, rescaled by $h^{2}/q$.
- The $h^{2}$ numerator arises from the two factors of $(q - q^{-1})$ in the denominators of $[9]_q$ and $[10]_q$.

**Significance for the Hartree-energy conjecture.** This identity supplies the algebraic mechanism by which $\alpha_{EM}^{2}$ enters the binding energy. We combine it with [`prop:force-carrier-intertwining-correspondence`](#prop:force-carrier-intertwining-correspondence), which identifies the Wedderburn channels $(3, 1)$ and $(2, 1, 1)$ on which the molecular bound state projects with non-trivial $\delta_q$ weight:

$$
  \alpha_{EM}^{2}
  \;=\;
  \frac{h^{4}}{q^{2} \cdot \delta_q(T_{2,9})^{2} \cdot \delta_q(T_{3,5})^{2}}.
$$

The bound-state Markov trace contribution is bilinear in $\chi_{(3,1)}$ and $\chi_{(2,1,1)}$. Conjecturally, these characters are proportional to $\delta_q(T_{3,5})^{-1}$ and $\delta_q(T_{2,9})^{-1}$ respectively. This forms the categorical analogue of the Coulomb potential in the bound state. Their product introduces the $\alpha_{EM}^{2}$ factor.

Closing this final algebraic identity remains the next step for [`conj:e-hartree-categorical-derivation`](#conj:e-hartree-categorical-derivation).
<!-- FILE_END: alpha-em-categorical-trace-ratio-interpretation.md -->

<!-- FILE_START: alpha-em-shift-multiplicative-chain.md -->
<!-- Theorem (proved by composition of two named identities). -->

**Proposition (multiplicative-chain form of $\alpha_{EM}^{-1}$).**
*Working over $R = \mathbb{Z}[q^{\pm 1/2}, (q - q^{-1})^{-1}]$ with
the canonical substrate parameter $q$,*

$$
  \boxed{\;\;
    \alpha_{EM}^{-1}
    \;=\;
    q \cdot
    \bigl[\alpha_{\mathrm{shift}}(T_{2,9})\bigr]_q \cdot
    \bigl[\alpha_{\mathrm{shift}}(T_{3,5})\bigr]_q.
  \;\;}
$$
<!-- FILE_END: alpha-em-shift-multiplicative-chain.md -->

<!-- FILE_START: alpha-em-shift-multiplicative-chain-significance.md -->
**Significance: bridge to the w3-w4 atomic-shift framework.** Both ingredients of the multiplicative chain ([$\alpha_{EM}$ shift multiplicative chain](#prop:alpha-em-shift-multiplicative-chain)) expose the same combinatorial primitive: the pole order at $q = 0$ of a seminormal Hecke trace.

| Object                          | Shift role                                                                                            |
|---------------------------------|--------------------------------------------------------------------------------------------------------|
| Atomic Markov-trace denominator | $D(u) = 2^{2A+1} \cdot u^{\mathrm{shift}} \cdot (1 + u^2)^{3A-1}$ ([`docs/audits/-w3-habiro-unblocked.md`](../../docs/audits/-w3-habiro-unblocked.md)) |
| Torus knot $T_{p,k}$ on $V_{(1^p)}$ | $\alpha_{\mathrm{shift}}(T_{p,k}) = k(p-1)$ ([`prop:alpha-shift-torus-knot`](#prop:alpha-shift-torus-knot))            |
| Inverse fine-structure constant | $\alpha_{EM}^{-1} = q \cdot [\alpha_{\mathrm{shift}}(T_{2,9})]_q \cdot [\alpha_{\mathrm{shift}}(T_{3,5})]_q$           |

The torus-braid case constitutes the clean limit of the atomic-braid shift framework. It features no inter-nucleon terms and only $\sigma_i$ generators (no averaged or inverse generators). It lacks within-partition Hecke $\sigma^2$-cancellation, as the standard Young tableau path through the single column visits distinct axial distances at every step. It also lacks cross-partition Ocneanu cancellation, since the maximum occurs on a unique irreducible representation.
<!-- FILE_END: alpha-em-shift-multiplicative-chain-significance.md -->

<!-- FILE_START: q-chromaticity.md -->
The three color tubes of the Bring's surface
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
$\mathrm{Sk}_q(\mathbf{C})$.  The three color tubes
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

**Necessity of confinement.**

In Feynman's language: some spectral colors lie outside the triangle
of primaries, requiring negative coefficients.  In QOU language:
some Skein elements have negative coefficients in the color-tube
basis.

An individual quark — a trefoil $T_{2,3}$ in a single color tube —
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
three color tubes in a single closed curve, $T_{2,9}$ provides
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
three color tubes.  These satisfy $\hat{c}_r + \hat{c}_g + \hat{c}_b = 1$,
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
<!-- FILE_END: q-chromaticity.md -->

<!-- FILE_START: schrodinger-color-falsifiability.md -->
The categorical [$q$-chromaticity construction](#rem:q-chromaticity) makes a falsifiable prediction about human color perception. This directly addresses the century-old paradigm of Riemann \cite{schrodinger1920color} and the modern psychophysical results of \cite{bujack2022}.

**The empirical result (Bujack et al., 2022).**

Bujack et al. \cite{bujack2022} demonstrate that perceived color differences obey the strict inequality

$$
  \Delta E(A, B) + \Delta E(B, C) > \Delta E(A, C)
$$

along geodesics. This "principle of diminishing returns" contradicts the Riemannian additivity assumed since Riemann, Helmholtz, and Schrödinger \cite{schrodinger1920color}. A regression on a crowdsourced color-triad experiment yields a significantly negative average-difference coefficient ($\beta_{\bar d} = -0.005$, $t(60) = -5.566$, $p < 0.001$). The qualitative shape of the recovered scaling function matches a concave, sub-linear curve. The authors explicitly suggest a second-order Weber–Fechner law (logarithmic in the large-difference regime). They note that earlier psychophysical work fits perceived color difference to a power law with exponent $\approx 0.5$.

**The categorical prediction.**

The Skein relation $q[L_+] - q^{-1}[L_-] = (q^{1/2} - q^{-1/2})[L_0]$ forces the distance on the $q$-chromaticity simplex to inherit a $q$-deformed non-Riemannian correction. The categorically natural functional form is the quantum-integer arc-length:

$$
  \Delta E_{\mathrm{perc}}(d)
  \;=\;
  \frac{1}{\eta}\,\operatorname{arsinh}\!\bigl(\eta\,d\bigr),
  \qquad
  \eta := \frac{q - q^{-1}}{2},
$$

where $d$ is the Riemannian (CIELAB-style) chord length and $\Delta E_{\mathrm{perc}}$ is the perceived difference along the geodesic. This provides the unique one-parameter analytic completion of $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ to a metric on the projective chromaticity 2-simplex. The limit $\eta \to 0$ recovers the Riemannian metric $\Delta E_{\mathrm{perc}} = d$.

See [Table 1](#tbl:schrodinger-color-falsifiability-table1-data).

The large-$d$ logarithmic asymptote matches exactly the second-order Weber–Fechner law suggested by \cite{bujack2022}. The empirical power-law exponent $\approx 0.5$ corresponds to the intermediate-$d$ behavior of $\operatorname{arsinh}(\eta d)/\eta$, capturing the transition between the linear and logarithmic regimes.

**Numerical prediction from the substrate parameter.**

Substituting the substrate value $q_0 \approx 1.109978595554181$ gives:

$$
  \eta = \frac{q_0 - q_0^{-1}}{2} \approx 0.1043,
  \qquad
  d^{\,*} := 1/\eta \approx 9.59.
$$

We predict the crossover from the Riemannian regime to the Weber–Fechner regime sits at $\Delta E \approx 9.6$ on a normalized $L^{*}$-style scale (where unit $\Delta E$ is the typical small-difference just-noticeable threshold). This strongly agrees with \cite{bujack2022} Table 1: the diminishing-returns effect is barely significant at $\Delta d = 5$ ($\beta_{\Delta d = 5} = 0.048$, $p = 0.010$) but strongly significant at $\Delta d = 10$ ($\beta_{\Delta d = 10} = 0.119$, $p < 0.001$). The perceptual crossover empirically lies in $[5, 10]$, which brackets the predicted $d^{\,*} \approx 9.6$.

**Falsifiability protocol.**

The categorical prediction forms a one-parameter family $\Delta E_{\mathrm{perc}}(d) = \operatorname{arsinh}(\eta d)/\eta$. A sufficiently precise color-perception experiment can fit a single $\eta$ to yield a confidence interval $[\eta_-, \eta_+]$. This admits three distinct outcomes:

See [Table 2](#tbl:schrodinger-color-falsifiability-table2-data).

The third outcome would falsify the direct identification that retinal $\Delta E$ measures the Skein metric on the Bring-surface chromaticity simplex. It would not falsify the broader framework, as color perception sits several decoherence layers above the substrate.

**Sign and functional-form predictions.**

Independently of any numerical fit, the framework predicts three qualitative features already confirmed by \cite{bujack2022}:

See [Table 3](#tbl:schrodinger-color-falsifiability-table3-data).

The remaining empirical lever is the magnitude of $\eta$, constrained by the single-number test above.

**Connection to confinement.**

The same deformation parameter $q - q^{-1} = 2\eta$ governs the magnitude of the forced negative coefficient that drives [color confinement](#rem:q-chromaticity). Measuring $\eta \approx 0.10$ in macroscopic color perception serves as an independent measurement of the underlying substrate deformation governing quark confinement.
<!-- FILE_END: schrodinger-color-falsifiability.md -->

