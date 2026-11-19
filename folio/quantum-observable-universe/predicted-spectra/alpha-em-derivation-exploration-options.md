**Remark (exploration options to close the $1/\alpha_{EM}$ derivation).**

On Bring's genus-$4$ surface, Hodge theory and Gauss–Bonnet identify the infrared shift $2/(3\pi) = 2g/(4\pi(g{-}1)) = b_1/\mathrm{Area}$ ([Bring-surface photon infrared zero-mode](#prop:photon-ir-zero-mode-bring), [Bring-surface zero-mode coupling](#prop:em-coupling-bring-zero-mode)). Exhibiting the explicit Bloch-group class in $B(\mathbb{C})$ and deriving the two-loop remainder $\Delta_2$ are conjectural; the existing geometric structures suggest four complementary approaches.

## Existing infrastructure

The missing step connects the current machinery to the coupling side.

### 1. Hopf fibration $S^3 \to S^2$ as the aether geometry

The [Reeb bundle](#def:reeb-bundle) at a brane point $p$ is

$$
  \mathcal{R}_p \;=\; \bigl( S^3 \xrightarrow{\pi_H} \mathcal{S}_p \cong S^2,\; \xi_q \bigr).
$$

The projection $\pi_H$ is the Hopf fibration. The base $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$ is the exceptional divisor space. The total space $S^3$ evaluates braid words in $B_n$ via $H_n(R,q)$. This geometric pair identically matches the algebraic identity $2/(3\pi) = \mathrm{Vol}(S^2)/(3\cdot\mathrm{Vol}(S^3))$.

### 2. Three color tubes on Bring's surface

Three colour primaries reside on Bring's surface ([$q$-chromaticity](#rem:q-chromaticity)). These are the three $S_3$ subgroups of the Bring automorphism group. This provides the natural source of the denominator $3$ in $2/(3\pi)$. It represents photon coupling averaged over three independent chromaticity channels.

### 3. Filtration with confinement levels

A depth filtration structures $H_n(R,q)$ via the [shadow-price confinement level](#def:confinement-level) and the [curvature-rank Gröbner stratification](#prop:curvature-rank-gb-stratification). For $H_3$, depths $\ell = 0,1,2,3$ yield a four-step filtration. The maximum depth of 3 correlates with the denominator $3$.

### 4. Spectral sequence collapse

Hochschild cohomology vanishes ($\mathrm{HH}^k = 0$ for $k \ge 1$) ([spectral sequence collapse](#prop:spectral-sequence-collapse)). The spectral sequence collapses at $E_1$. All contributions reside in $E_\infty^{0,0} = Z(H_n) = \bigoplus_\lambda R\cdot e_\lambda$. This mechanism yields the closed-form mass-formula $\alpha_k$ via Plancherel-weighted Markov pairings on the centre.

### 5. Wenzl-bridge closed form for stratum prefactors

An explicit $q$-rational expression gives the Markov-trace coefficients $y_\lambda$ in the mass-formula $\alpha_k$ ([Wenzl-bridge closed form](#prop:y-lambda-closed-form-wenzl-bridge)). This machinery applies to the coupling side.

## Four exploration options

### Option A — Hopf-fibration vacuum-polarisation integral

**Claim:** The photon vacuum-polarisation graph evaluates in the categorical framework. The photon propagator occupies the Hopf total space $S^3$. External legs project via $\pi_H$ to the base $S^2$. The zero-mode contribution at zero external momentum is

$$
  \Pi_{\text{zero}}(0)
  \;=\;
  \frac{\mathrm{Vol}(S^2)}{3 \cdot \mathrm{Vol}(S^3)}
  \;=\;
  \frac{2}{3\pi}.
$$

The factor $1/3$ arises from chromaticity averaging.

**Requirements:** An explicit formula defines the vacuum-polarisation graph in the categorical Lagrangian framework. The photon two-point function on $S^3$ converges to $1/\mathrm{Vol}(S^3)$ as a constant zero-momentum residue. The external-leg projection contributes the $\mathrm{Vol}(S^2)$ numerator. The chromaticity normalisation contributes the factor $1/3$.

### Option B — Stratum-prefactor approach via spectral sequence collapse

**Claim:** The mass-formula spectral-sequence machinery ([unified curvature-rank mass formula](#prop:unified-curvature-rank-mass-formula)) applies to the coupling side. The $\alpha_{EM}$ correction equals the depth-$\ell$ stratum prefactor of the filtration.

**Concretely:** The bare formula $1/\alpha = q\cdot[9]_q\cdot[10]_q$ is the depth-$0$ centre contribution. The $2/(3\pi)$ correction expresses a Plancherel-weighted Markov pairing on the depth-$\ell$ stratum for $\ell \ge 1$.

**Requirements:** A depth-$k$ contribution defines $1/\alpha_{EM}$. Computation proceeds via the closed form at depth $\ell$. Verification confirms the depth-$\ell$ contribution equals $2/(3\pi)$ at $q = q_0$.

### Option C — Reeb-bundle holonomy

**Claim:** The $\mathrm{U}(1)$ fibre of the Reeb bundle has holonomy $e^{2\pi i / [2]_q}$. Integrating the photon over the fibre and averaging over the base yields a finite phase-volume factor equal to $2/(3\pi)$ at $q = q_0$ for $g = 4$.

**Requirements:** The photon holonomy integral defines over the fibre. Squaring it and averaging over $\mathcal{S}_p$ uses the Fubini-Study measure. This approach predicts a $q$-dependent constant. This contradicts the required $q$-independence. Option C is falsified.

### Option D — Chern-Simons partition-function ratio

**Claim:** The constant $2/(3\pi)$ is the ratio of Chern-Simons partition functions on distinguished 3-manifolds:

$$
  \frac{2}{3\pi}
  \;=\;
  \frac{Z_{\mathrm{CS}}(S^3, \mathrm{SU}(2)_k)}{3 \cdot Z_{\mathrm{CS}}(S^3 \times S^1, \cdots)}.
$$

The constant emerges from the universal $k \to \infty$ asymptotics.

**Requirements:** The partition functions evaluate and limits take $k \to \infty$. The limit produces $1/k$ factors that map to $1/\pi$ via $k+2 = \pi/\log q$.

## Recommended path

Option B utilises existing infrastructure and clarifies the relationship between the mass and coupling formulas.

A practical execution follows:
1. Implement Option B in $H_3$ ([explicit $H_3$ spectral sequence](#prop:spectral-sequence-h3-explicit)).
2. Define the depth-$\ell$ coupling functional.
3. Compute the value at $q_0$ for each $\ell$ to isolate $2/(3\pi)$.
4. Generalise to higher $H_n$ and verify consistency.
5. Cross-validate against Option A.

## Natural sources for each ingredient

The natural sources for the $1/\alpha_{EM}$ ingredients appear in [Table: Natural QOU sources for the $1/\alpha_{EM}$ ingredients](#tbl:alpha-em-derivation-exploration-options-table-data). The derivation awaits the coupling-side analog of the mass-formula stratum decomposition.
