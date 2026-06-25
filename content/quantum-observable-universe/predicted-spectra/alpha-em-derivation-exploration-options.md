**Remark (exploration options to close the $1/\alpha_{EM}$ derivation).**

This remark maps the existing QOU infrastructure to the open
$2/(3\pi)$ derivation. The numerical match
$1/\alpha_{EM} \approx q\cdot[9]_q\cdot[10]_q + 2/(3\pi)$
(see [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode))
is exact at the algebraic identity
$2/(3\pi) = 2g/(4\pi(g{-}1))$ at $g = 4$ but lacks a derivation.
Below: what's already in place, and four concrete paths forward.

## Existing infrastructure (relevant pieces)

The QOU paper already contains the machinery needed to close this
derivation; the missing step is connecting it to the coupling side.

### 1. Hopf fibration $S^3 \to S^2$ as the substrate geometry

The [Reeb bundle](#def:reeb-bundle) at a brane point $p$ is

$$
  \mathcal{R}_p \;=\; \bigl( S^3 \xrightarrow{\pi_H} \mathcal{S}_p \cong S^2,\; \xi_q \bigr),
$$

with $\pi_H$ the Hopf fibration, base $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$
(the exceptional divisor / colour space), and total $S^3$ "the arena
where braid words in $B_n$ are evaluated via $H_n(R,q)$." This is
**precisely** the geometric pair appearing in the algebraic identity
$2/(3\pi) = \mathrm{Vol}(S^2)/(3\cdot\mathrm{Vol}(S^3))$. The
"category of base" is $\mathcal{S}_p \cong S^2$ and the "category of
total space" is $S^3$.

### 2. Three color tubes / chromaticity primaries on Bring's surface

[`rem:q-chromaticity`](#rem:q-chromaticity) identifies three
colour primaries on Bring's surface (the three color tubes /
three $S_3$ subgroups of the Bring automorphism group). This is
the **natural source of the "$/3$" denominator** in $2/(3\pi)$:
photon coupling averaged over three independent chromaticity channels.

### 3. GB filtration with confinement levels

[`def:confinement-level`](#def:confinement-level) and
[`prop:curvature-rank-gb-stratification`](#prop:curvature-rank-gb-stratification)
filter $H_n(R,q)$ by GB-depth. For $H_3$, depths $\ell = 0,1,2,3$
give a 4-step filtration (matching the "3" in $/3$? — depth $\le 3$).

### 4. Spectral sequence collapse

[`prop:spectral-sequence-collapse`](#prop:spectral-sequence-collapse)
shows Hochschild cohomology vanishes ($\mathrm{HH}^k = 0$ for
$k \ge 1$) so the GB spectral sequence collapses at $E_1$ with all
contribution in
$E_\infty^{0,0} = \mathrm{HH}^0 = Z(H_n) = \bigoplus_\lambda R\cdot e_\lambda$.
This is the **engine** that produces the closed-form mass-formula
$\alpha_k$ via Plancherel-weighted Markov pairings on the centre.

### 5. Wenzl-bridge closed form for stratum prefactors

[`prop:y-lambda-closed-form-wenzl-bridge`](#prop:y-lambda-closed-form-wenzl-bridge)
gives an explicit q-rational expression for the Markov-trace
coefficients $y_\lambda$ entering the mass-formula $\alpha_k$.
This same machinery can in principle be applied to the **coupling**
side rather than the mass side.

## Four exploration options

### Option A — Hopf-fibration vacuum-polarisation integral

**Claim:** Compute the photon vacuum-polarisation 1PI graph in the
QOU framework with the photon propagator on the Hopf total space
$S^3$ and external legs (force-carrier knots) projecting via $\pi_H$
to the base $\mathcal{S}_p \cong S^2$. The zero-mode contribution
at zero external momentum is

$$
  \Pi_{\text{zero}}(0)
  \;=\;
  \frac{\mathrm{Vol}(S^2)}{3 \cdot \mathrm{Vol}(S^3)}
  \;=\;
  \frac{2}{3\pi},
$$

with the $1/3$ factor from chromaticity averaging across the three
colour primaries on Bring's surface.

**What's needed:** explicit formula for the vacuum-polarisation 1PI
graph in the categorical-Lagrangian framework, including:
1. Photon two-point function on $S^3$ (Hodge-decomposed; harmonic
   1-forms vanish because $H^1(S^3) = 0$, leaving only the
   non-harmonic spectrum which converges to $1/\mathrm{Vol}(S^3)$
   as a constant zero-momentum residue).
2. External-leg projection $\pi_H \colon S^3 \to S^2$ contributing
   the Vol$(S^2)$ factor in the numerator.
3. Lie-algebra / chromaticity normalisation contributing $1/3$.

**Bounded scope:** This is a one-loop calculation on a known
geometry. Could plausibly close in a few days of focused work.

### Option B — Stratum-prefactor approach via spectral sequence collapse

**Claim:** Apply the same spectral-sequence machinery used for the
mass formula
([`prop:unified-curvature-rank-mass-formula`](#prop:unified-curvature-rank-mass-formula))
to the **coupling** side. The $\alpha_{EM}$ correction
should be the depth-$\ell$ stratum prefactor of the GB filtration
for some specific $\ell$.

**Concretely:** the bare formula $1/\alpha = q\cdot[9]_q\cdot[10]_q$
is the depth-$0$ centre contribution. The $2/(3\pi)$ correction
should be expressible as a Plancherel-weighted Markov pairing on
the depth-$\ell$ stratum for $\ell \ge 1$, computed via the
Wenzl-bridge closed form.

**What's needed:**
1. Identify the "coupling-side analog" of the mass functional
   $\mathfrak{m}^{(k)}$ — specifically, define a depth-$k$
   contribution to $1/\alpha_{EM}$.
2. Compute it via $y_\lambda$ closed form at depth $\ell$.
3. Verify the depth-$\ell$ contribution at $q = q_0$ equals
   $2/(3\pi)$.

**Bounded scope:** infrastructure already exists; need to identify
the right $\ell$ and run the calculation. Days to a week.

### Option C — Reeb-bundle holonomy + U(1) integration

**Claim:** The U(1) fibre of the Reeb bundle has holonomy
$e^{2\pi i / [2]_q}$. Integrating the photon over the fibre and
averaging over the base gives a finite phase-volume factor that
equals $2/(3\pi)$ at $q = q_0$ for $g = 4$.

**What's needed:**
1. Define the photon holonomy integral over the U(1) fibre:
   $\oint_{U(1)} A_\mu d\theta = 2\pi/[2]_q$.
2. Square / take modulus and average over $\mathcal{S}_p$ with the
   Fubini-Study measure.
3. Verify the result is $2/(3\pi)$ at $q = q_0$ — note this would
   make $2/(3\pi)$ inherently $q$-dependent, contradicting the
   constant nature of the term in the additive form. **This option
   is therefore likely WRONG**; it predicts a $q$-dependent constant
   where the data shows a $q$-independent one.

**Bounded scope:** quick to falsify (a few hours).

### Option D — Chern-Simons partition-function ratio

**Claim:** $2/(3\pi)$ is the ratio of CS partition functions on
distinguished 3-manifolds at the QOU substrate level $k(q)$:

$$
  \frac{2}{3\pi}
  \;=\;
  \frac{Z_{\mathrm{CS}}(S^3, \mathrm{SU}(2)_k)}{3 \cdot Z_{\mathrm{CS}}(S^3 \times S^1, \cdots)}
  \quad\text{or similar},
$$

with the constant emerging from the universal $k \to \infty$
asymptotics rather than the substrate-dependent finite-$k$ value.

**What's needed:** evaluation of CS partition functions on the
relevant 3-manifolds, taking the appropriate limit. The Witten
formulas give explicit closed forms for SU(2)$_k$ on $S^3$ and
related geometries; the $k \to \infty$ limit produces $1/k$ factors
that correspond to $1/\pi$ via $k+2 = \pi/\log q$.

**Bounded scope:** standard Witten-Reshetikhin-Turaev computations.
Days.

## Recommended path

**Option B** (stratum-prefactor via spectral sequence) is the most
natural fit given the existing infrastructure and would also
illuminate the relationship between the QOU mass and coupling
formulas (currently treated separately). Option A is the more
direct QFT calculation but requires more new infrastructure.
Option C is a useful sanity check (predicts the wrong $q$-dependence
hence falsifies the simplest holonomy interpretation).

A practical attack would:

1. Begin with Option B in $H_3$ (smallest non-trivial case where
   spectral-sequence machinery is fully explicit, see
   [`prop:spectral-sequence-h3-explicit`](#prop:spectral-sequence-h3-explicit)).
2. Define the depth-$\ell$ coupling functional analogous to the
   mass functional.
3. Compute its value at $q_0$ for each $\ell$ and identify the one
   that gives $2/(3\pi)$.
4. If found, generalise to higher $H_n$ and verify consistency.
5. Cross-validate against Option A by comparing the depth-$\ell$
   stratum-prefactor identification to the Hopf-fibration zero-mode
   integral.

## Natural sources for each ingredient (summary)

See [Table: Natural QOU sources for the $1/\alpha_{EM}$ ingredients](#tbl:alpha-em-derivation-exploration-options-table-data).

Every ingredient has a natural source already in the paper. The
missing piece is the **coupling-side analog of the mass-formula
stratum decomposition**, applied at the depth where the answer
becomes $2/(3\pi)$.
