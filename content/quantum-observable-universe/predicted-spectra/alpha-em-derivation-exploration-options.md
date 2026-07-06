**Remark (exploration options to close the $1/\alpha_{EM}$ derivation).**

We map the existing QOU infrastructure to the open $2/(3\pi)$ derivation. The numerical match $1/\alpha_{EM} \approx q\cdot[9]_q\cdot[10]_q + 2/(3\pi)$ ([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)) holds exactly via the algebraic identity $2/(3\pi) = 2g/(4\pi(g{-}1))$ at $g = 4$. However, it requires a derivation. We record the existing infrastructure and four potential paths forward.

## Existing infrastructure

The missing step is connecting the current machinery to the coupling side.

### 1. Hopf fibration $S^3 \to S^2$ as the substrate geometry

The [Reeb bundle](#def:reeb-bundle) at a brane point $p$ is

$$
  \mathcal{R}_p \;=\; \bigl( S^3 \xrightarrow{\pi_H} \mathcal{S}_p \cong S^2,\; \xi_q \bigr),
$$

where $\pi_H$ is the Hopf fibration, the base $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$ is the exceptional divisor (colour space), and the total space $S^3$ evaluates braid words in $B_n$ via $H_n(R,q)$. This geometric pair identically matches the algebraic identity $2/(3\pi) = \mathrm{Vol}(S^2)/(3\cdot\mathrm{Vol}(S^3))$. The category of the base is $\mathcal{S}_p \cong S^2$ and the category of the total space is $S^3$.

### 2. Three color tubes / chromaticity primaries on Bring's surface

We identify three colour primaries on Bring's surface (the three color tubes, or three $S_3$ subgroups of the Bring automorphism group) in [`rem:q-chromaticity`](#rem:q-chromaticity). This provides the natural source of the "$/3$" denominator in $2/(3\pi)$. It represents photon coupling averaged over three independent chromaticity channels.

### 3. GB filtration with confinement levels

We filter $H_n(R,q)$ by GB-depth via [`def:confinement-level`](#def:confinement-level) and [`prop:curvature-rank-gb-stratification`](#prop:curvature-rank-gb-stratification). For $H_3$, depths $\ell = 0,1,2,3$ yield a four-step filtration. The maximum depth of 3 correlates with the $/3$ denominator.

### 4. Spectral sequence collapse

Hochschild cohomology vanishes ($\mathrm{HH}^k = 0$ for $k \ge 1$) ([`prop:spectral-sequence-collapse`](#prop:spectral-sequence-collapse)). The GB spectral sequence collapses at $E_1$. All contributions reside in $E_\infty^{0,0} = \mathrm{HH}^0 = Z(H_n) = \bigoplus_\lambda R\cdot e_\lambda$. This mechanism yields the closed-form mass-formula $\alpha_k$ via Plancherel-weighted Markov pairings on the centre.

### 5. Wenzl-bridge closed form for stratum prefactors

We obtain an explicit q-rational expression for the Markov-trace coefficients $y_\lambda$ in the mass-formula $\alpha_k$ ([`prop:y-lambda-closed-form-wenzl-bridge`](#prop:y-lambda-closed-form-wenzl-bridge)). We apply this machinery to the coupling side rather than the mass side.

## Four exploration options

### Option A — Hopf-fibration vacuum-polarisation integral

**Claim:** We compute the photon vacuum-polarisation 1PI graph in the QOU framework. We set the photon propagator on the Hopf total space $S^3$ and external legs (force-carrier knots) projecting via $\pi_H$ to the base $\mathcal{S}_p \cong S^2$. The zero-mode contribution at zero external momentum is

$$
  \Pi_{\text{zero}}(0)
  \;=\;
  \frac{\mathrm{Vol}(S^2)}{3 \cdot \mathrm{Vol}(S^3)}
  \;=\;
  \frac{2}{3\pi},
$$

where the $1/3$ factor arises from chromaticity averaging across the three colour primaries on Bring's surface.

**Requirements:** We need an explicit formula for the vacuum-polarisation 1PI graph in the categorical-Lagrangian framework. This includes:
1. The photon two-point function on $S^3$ (Hodge-decomposed). Harmonic 1-forms vanish because $H^1(S^3) = 0$. The non-harmonic spectrum converges to $1/\mathrm{Vol}(S^3)$ as a constant zero-momentum residue.
2. The external-leg projection $\pi_H \colon S^3 \to S^2$, contributing the $\mathrm{Vol}(S^2)$ numerator.
3. The Lie-algebra / chromaticity normalisation, contributing the $1/3$ factor.

### Option B — Stratum-prefactor approach via spectral sequence collapse

**Claim:** We apply the spectral-sequence machinery used for the mass formula ([`prop:unified-curvature-rank-mass-formula`](#prop:unified-curvature-rank-mass-formula)) to the coupling side. The $\alpha_{EM}$ correction equals the depth-$\ell$ stratum prefactor of the GB filtration for a specific $\ell$.

**Concretely:** The bare formula $1/\alpha = q\cdot[9]_q\cdot[10]_q$ is the depth-$0$ centre contribution. The $2/(3\pi)$ correction expresses a Plancherel-weighted Markov pairing on the depth-$\ell$ stratum for $\ell \ge 1$, computed via the Wenzl-bridge closed form.

**Requirements:**
1. We define a depth-$k$ contribution to $1/\alpha_{EM}$, analogous to the mass functional $\mathfrak{m}^{(k)}$.
2. We compute this via the $y_\lambda$ closed form at depth $\ell$.
3. We verify that the depth-$\ell$ contribution at $q = q_0$ equals $2/(3\pi)$.

### Option C — Reeb-bundle holonomy + U(1) integration

**Claim:** The $\mathrm{U}(1)$ fibre of the Reeb bundle has holonomy $e^{2\pi i / [2]_q}$. Integrating the photon over the fibre and averaging over the base yields a finite phase-volume factor equal to $2/(3\pi)$ at $q = q_0$ for $g = 4$.

**Requirements:**
1. We define the photon holonomy integral over the $\mathrm{U}(1)$ fibre: $\oint_{U(1)} A_\mu d\theta = 2\pi/[2]_q$.
2. We square or take the modulus and average over $\mathcal{S}_p$ using the Fubini-Study measure.
3. We verify the result equals $2/(3\pi)$ at $q = q_0$. However, this predicts a $q$-dependent constant, contradicting the required $q$-independence. This falsifies the holonomy approach.

### Option D — Chern-Simons partition-function ratio

**Claim:** The constant $2/(3\pi)$ is the ratio of Chern-Simons partition functions on distinguished 3-manifolds at the QOU substrate level $k(q)$:

$$
  \frac{2}{3\pi}
  \;=\;
  \frac{Z_{\mathrm{CS}}(S^3, \mathrm{SU}(2)_k)}{3 \cdot Z_{\mathrm{CS}}(S^3 \times S^1, \cdots)}
  \quad\text{or similar}.
$$

The constant emerges from the universal $k \to \infty$ asymptotics, independent of the finite-$k$ value.

**Requirements:** We evaluate the Chern-Simons partition functions on the relevant 3-manifolds and take the appropriate limit. The Witten formulas provide explicit closed forms for $\mathrm{SU}(2)_k$ on $S^3$. The $k \to \infty$ limit produces $1/k$ factors that map to $1/\pi$ via $k+2 = \pi/\log q$.

## Recommended path

We recommend Option B (stratum-prefactor via spectral sequence). It utilises existing infrastructure and clarifies the relationship between the QOU mass and coupling formulas. Option A provides a direct QFT calculation but requires new infrastructure.

A practical execution follows:
1. Implement Option B in $H_3$ ([`prop:spectral-sequence-h3-explicit`](#prop:spectral-sequence-h3-explicit)).
2. Define the depth-$\ell$ coupling functional analogously to the mass functional.
3. Compute the value at $q_0$ for each $\ell$ to isolate $2/(3\pi)$.
4. Generalise to higher $H_n$ and verify consistency.
5. Cross-validate against Option A by comparing the depth-$\ell$ stratum-prefactor to the Hopf-fibration zero-mode integral.

## Natural sources for each ingredient

We catalogue the natural QOU sources for the $1/\alpha_{EM}$ ingredients in [Table: Natural QOU sources for the $1/\alpha_{EM}$ ingredients](#tbl:alpha-em-derivation-exploration-options-table-data). The derivation awaits the coupling-side analog of the mass-formula stratum decomposition.
