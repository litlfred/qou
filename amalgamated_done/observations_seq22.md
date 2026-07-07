<!-- FILE_START: simulations-intro.md -->
We supply interactive tools to test numerical predictions:

- **q-Deformed Double-Slit Simulator** and **Double-Slit Analytical Simulator** implement the two-mode interference patterns.
- **Bring's Surface Simulator** and **Quantum Bring's Surface Simulator** expose the Bring-surface geometry.
- **Beta-Decay Half-Life Simulator** tracks predicted half-lives against experimental data via $q$ variation.

These tools render every numerical prediction reproducible.
<!-- FILE_END: simulations-intro.md -->

<!-- FILE_START: q-double-slit.md -->
We provide an interactive particle simulation of the $q$-deformed double-slit experiment.

Particles traverse slits in a barrier with knot volume $\mathrm{Vol}(K)$. The categorical Dirac equation $\mathcal{D}_\nabla \psi = 0$ governs interference. The Reeb contraction term $(1 - q^{-1})\iota_\xi \nabla$ modifies the phase accumulation relative to the classical baseline.

**Default view.** We set a moderate $q$-deformation ($q \approx q_0$). The accumulation reveals the fringe shift relative to Fraunhofer diffraction.

**Parameters.**

- $q$ — substrate parameter.
- $D$ — slit separation.
- $d$ — slit width.
- $w$ — barrier thickness.
- $\lambda$ — wavelength.
- $w_0$ — Gaussian beam waist.
- $\mathrm{Vol}(K)$ — hyperbolic volume.
- Torsion — torsion intensity.

The simulation executes in real time.
<!-- FILE_END: q-double-slit.md -->

<!-- FILE_START: double-slit-analytical.md -->
We provide an analytical intensity pattern plotter for the $q$-deformed double-slit experiment.

This simulator computes the interference intensity envelope for two scattering modes:

1. **Mode 1 (Massive particle)**: $q$-harmonic form scattering.
2. **Mode 2 (Photon)**: Julia-set envelope scattering.

**Default view**: Bach 2013 electron data (600 eV) overlaid on the $q$-deformed prediction ($q = 1.020$).

**Parameters**:

- $q$ — substrate parameter
- $a$ — slit width
- $d$ — slit separation
- $\lambda$ — de Broglie wavelength
- $r_\xi$ — Reeb coupling ratio
<!-- FILE_END: double-slit-analytical.md -->

<!-- FILE_START: brings-surface-simulator.md -->
We provide a 3D visualisation of quaternionic spectral resolvent coordinates on Bring's surface.

The simulator renders the four $\beta$-branches of the spectral resolvent:

- $\beta_1 = \pi - 3\alpha$ (blue)
- $\beta_2 = (\pi + \alpha)/3$ (red-orange)
- $\beta_3 = (3\pi + \alpha)/3$ (green)
- $\beta_4 = (5\pi + \alpha)/3$ (orange-yellow)

**Default view**: Standard resolvent with $N = 18$ $q$-series terms and $\omega$-coordinate projection.

**Parameters**:

- $r_{\min}$, $r_{\max}$ — radial range.
- $\delta r$, $\delta\zeta$ — grid density.
- $N$ — $q$-series truncation precision.
- Projection mode: $\omega$-coords, $+\mathrm{Sp}(1)$ rotation, or raw $x_j$.
<!-- FILE_END: brings-surface-simulator.md -->

<!-- FILE_START: quantum-brings-surface.md -->
We provide an advanced interactive simulator of quantum Bring's surface.

This extends the basic simulator with multi-canvas analysis panels:

- **Chiral grid.** Quantum colour coding.
- **Weierstrass chart.** Elliptic curve invariants.
- **Affine coordinate chart.** Affine coordinates.
- **Fiber $\mathbb{CP}^1$.** Complex projective line parametrisation.
- **Julia set.** Escape-time fractal computation.
- **Möbius spectral panel.** Spectral resolvent classification.

**Default view.** Overview with the chiral grid enabled.
<!-- FILE_END: quantum-brings-surface.md -->

<!-- FILE_START: beta-decay-simulator.md -->
This simulator computes nuclear beta-decay half-lives from the substrate parameter $q$. It evaluates the transfer matrix Skein polynomial.

## Computed quantities

For a nucleus $\mathcal{N}(Z, N)$, the simulator determines:

1. **Skein polynomials.** It evaluates $P_{\mathrm{par}}(q)$ and $P_{\mathrm{dau}}(q)$.
2. **$Q$-value.** It calculates $Q = |\ln(P_{\mathrm{dau}}/P_{\mathrm{par}})| \times E_{\times} \times \mu_0$.
3. **Phase-space integral.** It evaluates $f(Z, Q)$ with the Skein-Coulomb Fermi function $F_q(Z, E)$.
4. **Half-life.** It computes $t_{1/2} = \ln 2 / \Gamma_\beta$.

## Operating modes

- **From $q$.** The simulator predicts the $Q$-value from the transfer matrix ratio.
- **From $Q_{\mathrm{exp}}$.** The simulator isolates the $q$-dependent prefactors and Coulomb enhancement using experimental $Q$-values.

## Physical regimes

The plot illustrates three regimes:

- **Classical** ($q \to 1$). $\Gamma_\beta \to 0$. No beta decay.
- **Descartes** ($q = q_0$). Recovers observed nuclear lifetimes.
- **Deep quantum** ($q \to \infty$). $\Gamma_\beta \to \infty$. Instantaneous decay.

## Benchmark nuclei

The verification nuclei and data are tabulated in [Table: Verification nuclei](#tbl:beta-decay-simulator-table-data).
<!-- FILE_END: beta-decay-simulator.md -->

<!-- FILE_START: outro-observations.md -->
We evaluated categorical predictions at the substrate parameter $q_0 \approx 1.1097$. These match CODATA and NIST measurements. Interactive simulators expose this numerical machinery.

We subsequently reuse the categorical mass predictions as energy inputs for covalent bonds.
<!-- FILE_END: outro-observations.md -->
