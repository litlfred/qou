<!-- FILE_START: archimedean-hartree-crystal-alpha-em-categorical-intro.md -->
The upstream Mathlib additions catalogue the categorical structures underlying the substrate-flow construction. The trace ratio identity determines the substrate-flow value from the $\alpha_{\mathrm{EM}}$ categorical-trace ratio. The multiplicative-chain shift and $q$-chromaticity blocks specify the substrate-flow behaviour of $\alpha_{\mathrm{EM}}$ at the substrate parameter $q_0$.
<!-- FILE_END: archimedean-hartree-crystal-alpha-em-categorical-intro.md -->

<!-- FILE_START: alpha-em-categorical-trace-ratio.md -->
*Let $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$ be the base ring. Let $h = q - q^{-1}$ denote the skein parameter. Let $T_{2,9}$ and $T_{3,5}$ be the two genus-$4$-saturating torus knots ([`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness)). Let $\delta_q$ denote the $q$-dimension decoration ([`def:delta-q-decoration`](#def:delta-q-decoration)). The bare electromagnetic fine-structure constant $1/\alpha_{EM} = q\,[9]_q\,[10]_q$ ([`prop:em-coupling-projection`](#prop:em-coupling-projection)) admits the categorical-trace-ratio decomposition:*

$$
  \boxed{\;\;
    \alpha_{EM}
    \;=\;
    \frac{h^{2}}{q \cdot \delta_q(T_{2,9}) \cdot \delta_q(T_{3,5})}
  \;\;}
$$

### Derivation

In the natural $2$-strand representation, the categorical trace of a torus knot $T_{2,k}$ sums the contributions from the irreducible Hecke representations $V_{(2)}$ (eigenvalue $q$) and $V_{(1,1)}$ (eigenvalue $-q^{-1}$). For odd $k$, this yields:

$$
  \delta_q(T_{2,k})
  \;=\;
  q^{k} \cdot 1 + (-q^{-1})^{k} \cdot 1
  \;=\;
  q^{k} - q^{-k}.
$$

Evaluating at $k = 9$ gives $\delta_q(T_{2,9}) = q^{9} - q^{-9} = h\,[9]_q$.

For the $3$-strand torus knot $T_{3,5}$, the Rosso-Jones formula computes the categorical trace in $H_3(q)$. Summing the contributions from $V_{(3)}$, $V_{(2,1)}$, and $V_{(1,1,1)}$ with their respective eigenvalue powers yields $\delta_q(T_{3,5}) = q^{10} - q^{-10} = h\,[10]_q$.

Substitution produces the result:

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

Evaluation at $q_0 \approx 1.1099786$ yields an exact match to within $10^{-12}$. See [Table: Numerical verification of $\alpha_{EM}$ trace-ratio](#tbl:alpha-em-categorical-trace-ratio-table-data).

The witness assertion validates this match: [`delta-q-decoration.witness.json`](computations/delta-q-decoration.witness.json).

Expressing the relationship as a trace ratio on the $q$-dimension layer reformulates existing projection identities. This closes the categorical framework. The empirical electromagnetic coupling reduces to a structural trace-algebraic constraint.
<!-- FILE_END: alpha-em-categorical-trace-ratio.md -->

<!-- FILE_START: alpha-em-categorical-trace-ratio-interpretation.md -->
**Interpretation.** The trace-ratio identity ([$\alpha_{EM}$ categorical trace-ratio](#prop:alpha-em-categorical-trace-ratio)) refactors $\alpha_{EM}$ from the inverse Bring complex complexity into the ratio of $h^{2}$ over the product of force-carrier categorical traces. This shifts the $\alpha_{EM}$ formula from an operator-selection-LP-cost interpretation to the $q$-dimension layer.

The structural picture requires two components:
- For each force carrier, the $\delta_q$-decoration evaluates to a pure categorical trace $\delta_q(T_{p,q}) = q^{q} - q^{-q}$ in the appropriate $p$-strand realisation.
- The inverse product of these two traces, rescaled by $h^{2}/q$, yields $\alpha_{EM}$.

The $h^{2}$ numerator originates from the two $(q - q^{-1})$ factors in the denominators of $[9]_q$ and $[10]_q$.

**Significance for the Hartree-energy conjecture.** This identity supplies the algebraic mechanism introducing $\alpha_{EM}^{2}$ into the binding energy. The molecular bound state projects onto the Wedderburn channels $(3, 1)$ and $(2, 1, 1)$ with non-trivial $\delta_q$ weight ([`prop:force-carrier-intertwining-correspondence`](#prop:force-carrier-intertwining-correspondence)).

Squaring the trace-ratio identity yields:

$$
  \alpha_{EM}^{2}
  \;=\;
  \frac{h^{4}}{q^{2} \cdot \delta_q(T_{2,9})^{2} \cdot \delta_q(T_{3,5})^{2}}.
$$

The bound-state Markov trace contribution is bilinear in the characters $\chi_{(3,1)}$ and $\chi_{(2,1,1)}$. Conjecturally, these characters are proportional to $\delta_q(T_{3,5})^{-1}$ and $\delta_q(T_{2,9})^{-1}$. This bilinearity provides the categorical analogue of the Coulomb potential. Their product supplies the $\alpha_{EM}^{2}$ factor.

Closing this algebraic identity constitutes the next step for [`conj:e-hartree-categorical-derivation`](#conj:e-hartree-categorical-derivation).
<!-- FILE_END: alpha-em-categorical-trace-ratio-interpretation.md -->

<!-- FILE_START: alpha-em-shift-multiplicative-chain.md -->
<!-- Theorem (proved by composition of two named identities). -->

**Proposition (multiplicative-chain form of $\alpha_{EM}^{-1}$).**
*Let $R = \mathbb{Z}[q^{\pm 1/2}, (q - q^{-1})^{-1}]$ be the base ring. Let $q$ be the canonical substrate parameter. The inverse fine-structure constant admits the decomposition:*

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
**Significance: bridge to the w3-w4 atomic-shift framework.** Both factors in the multiplicative chain ([$\alpha_{EM}$ shift multiplicative chain](#prop:alpha-em-shift-multiplicative-chain)) expose the identical combinatorial primitive: the pole order at $q = 0$ of a seminormal Hecke trace.

| Object                          | Shift role                                                                                            |
|---------------------------------|--------------------------------------------------------------------------------------------------------|
| Atomic Markov-trace denominator | $D(u) = 2^{2A+1} \cdot u^{\mathrm{shift}} \cdot (1 + u^2)^{3A-1}$ ([`docs/audits/-w3-habiro-unblocked.md`](../../docs/audits/-w3-habiro-unblocked.md)) |
| Torus knot $T_{p,k}$ on $V_{(1^p)}$ | $\alpha_{\mathrm{shift}}(T_{p,k}) = k(p-1)$ ([`prop:alpha-shift-torus-knot`](#prop:alpha-shift-torus-knot))            |
| Inverse fine-structure constant | $\alpha_{EM}^{-1} = q \cdot [\alpha_{\mathrm{shift}}(T_{2,9})]_q \cdot [\alpha_{\mathrm{shift}}(T_{3,5})]_q$           |

The torus-braid case provides the clean limit of the atomic-braid shift framework. It restricts generators to $\sigma_i$ alone, avoiding averaged or inverse generators. It eliminates inter-nucleon terms. It prevents within-partition Hecke $\sigma^2$-cancellation, because the standard Young tableau path through the single column occupies distinct axial distances at every step. It precludes cross-partition Ocneanu cancellation, because the maximum localises on a unique irreducible representation.
<!-- FILE_END: alpha-em-shift-multiplicative-chain-significance.md -->

<!-- FILE_START: q-chromaticity.md -->
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

An individual quark forms a trefoil $T_{2,3}$ within a single color tube. This primary color fails to span the full Skein module with positive coefficients. Generic physical processes resolve into Skein sums containing $-q^{-1}$ factors. These terms hold physical meaning only upon evaluation of the complete Skein sum. Isolated evaluation of a single color component yields a meaningless negative probability.

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
<!-- FILE_END: q-chromaticity.md -->

<!-- FILE_START: schrodinger-color-falsifiability.md -->
The categorical [$q$-chromaticity construction](#rem:q-chromaticity) yields a falsifiable prediction regarding human color perception. This challenges the Riemannian paradigm \cite{schrodinger1920color} and aligns with the modern psychophysical results of Bujack et al. \cite{bujack2022}.

**The empirical result (Bujack et al., 2022).**

Bujack et al. \cite{bujack2022} proved that perceived color differences violate Riemannian additivity along geodesics. The observed differences satisfy the strict inequality:

$$
  \Delta E(A, B) + \Delta E(B, C) > \Delta E(A, C).
$$

This diminishing-returns principle contradicts the assumptions of Riemann, Helmholtz, and Schrödinger \cite{schrodinger1920color}. A crowdsourced color-triad experiment yielded a negative average-difference coefficient ($\beta_{\bar d} = -0.005$, $t(60) = -5.566$, $p < 0.001$). The observed scaling function exhibits concave, sub-linear curvature. Bujack et al. suggested a second-order Weber–Fechner law, which applies logarithmic scaling at large differences. Prior psychophysical studies fit perceived color differences to a power law with an exponent near $0.5$.

**The categorical prediction.**

The Skein relation $q[L_+] - q^{-1}[L_-] = (q^{1/2} - q^{-1/2})[L_0]$ deforms the distance on the $q$-chromaticity simplex. The distance inherits a non-Riemannian correction matching the quantum-integer arc-length:

$$
  \Delta E_{\mathrm{perc}}(d)
  \;=\;
  \frac{1}{\eta}\,\operatorname{arsinh}\!\bigl(\eta\,d\bigr),
  \qquad
  \eta := \frac{q - q^{-1}}{2}.
$$

Here $d$ denotes the Riemannian chord length, and $\Delta E_{\mathrm{perc}}$ denotes the perceived geodesic difference. This function constitutes the unique analytic one-parameter extension of $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ to a projective chromaticity 2-simplex metric. The limit $\eta \to 0$ recovers the purely Riemannian metric $\Delta E_{\mathrm{perc}} = d$.

See [Table 1](#tbl:schrodinger-color-falsifiability-table1-data).

The large-$d$ logarithmic asymptote precisely matches the second-order Weber–Fechner law suggested by \cite{bujack2022}. The empirical power-law exponent of $\approx 0.5$ captures the intermediate-$d$ behavior of $\operatorname{arsinh}(\eta d)/\eta$, mapping the transition between the linear and logarithmic regimes.

**Numerical prediction from the substrate parameter.**

Evaluation at the substrate value $q_0 \approx 1.109978595554181$ determines $\eta$ and the crossover scale $d^{\,*}$:

$$
  \eta = \frac{q_0 - q_0^{-1}}{2} \approx 0.1043,
  \qquad
  d^{\,*} := 1/\eta \approx 9.59.
$$

The transition from Riemannian to Weber–Fechner scaling occurs at $\Delta E \approx 9.6$ on a normalized $L^{*}$-style scale. This closely matches the empirical crossover. Bujack et al. \cite{bujack2022} found the diminishing-returns effect barely significant at $\Delta d = 5$ ($\beta_{\Delta d = 5} = 0.048$, $p = 0.010$) and strongly significant at $\Delta d = 10$ ($\beta_{\Delta d = 10} = 0.119$, $p < 0.001$). The perceptual crossover empirically lies in $[5, 10]$, bracketing the predicted $d^{\,*} \approx 9.6$.

**Falsifiability protocol.**

The categorical prediction forms a one-parameter family $\Delta E_{\mathrm{perc}}(d) = \operatorname{arsinh}(\eta d)/\eta$. A high-precision color-perception experiment can fit $\eta$ to a confidence interval $[\eta_-, \eta_+]$. This forces three possible outcomes:

See [Table 2](#tbl:schrodinger-color-falsifiability-table2-data).

An inconsistent measurement falsifies the hypothesis that retinal $\Delta E$ directly measures the Skein metric on the Bring-surface chromaticity simplex. It leaves the broader framework intact, because color perception operates several decoherence layers above the substrate.

**Sign and functional-form predictions.**

The framework makes three qualitative predictions already confirmed by \cite{bujack2022}, independent of numerical fitting:

See [Table 3](#tbl:schrodinger-color-falsifiability-table3-data).

The final empirical test lies in measuring the magnitude of $\eta$.

**Connection to confinement.**

The deformation parameter $q - q^{-1} = 2\eta$ determines the magnitude of the forced negative coefficients driving [color confinement](#rem:q-chromaticity). Measuring $\eta \approx 0.10$ via macroscopic color perception provides an independent measurement of the substrate deformation governing quark confinement.
<!-- FILE_END: schrodinger-color-falsifiability.md -->

