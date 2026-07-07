<!-- FILE_START: simulations-intro.md -->
The previous sections catalogued numerical predictions. Here we supply interactive tools to test them. 

- **q-Deformed Double-Slit Simulator** and **Double-Slit Analytical Simulator** implement the two-mode interference patterns.
- **Bring's Surface Simulator** and **Quantum Bring's Surface Simulator** expose the Bring-surface geometry underlying particle-identification and $S_5$-equivariant embeddings.
- **Beta-Decay Half-Life Simulator** permits variation of $q$ to track predicted half-lives against experimental data. 

These tools close the chapter by rendering every numerical prediction of Chapter 7 reproducible at the slider level.

_(draft.)_
<!-- FILE_END: simulations-intro.md -->

<!-- FILE_START: q-double-slit.md -->
We present an interactive particle simulation of the $q$-deformed double-slit experiment (§6.7, §11).

Particles are emitted from a source, traverse a pair of slits in a barrier material with knot volume $\mathrm{Vol}(K)$, and strike a detection screen. The categorical Dirac equation $\mathcal{D}_\nabla \psi = 0$ governs the interference pattern. The Reeb contraction term $(1 - q^{-1})\iota_\xi \nabla$ modifies the phase accumulation relative to the classical ($q = 1$) baseline.

**Default view.** We set a moderate $q$-deformation ($q \approx q_0$) with torsion parameters matching a typical nucleon boundary. The accumulation of $\sim 500$ particles reveals the fringe shift relative to Fraunhofer diffraction.

**Parameters.**

- $q$ — substrate parameter; controls $\hbar_q = 1 - q^{-1}$.
- $D$ — slit separation (mm).
- $d$ — slit width ($\mu$m).
- $w$ — barrier thickness ($\mu$m).
- $\lambda$ — wavelength (nm).
- $w_0$ — Gaussian beam waist at barrier (mm).
- $\mathrm{Vol}(K)$ — hyperbolic volume of the boundary knot.
- Torsion — torsion intensity of the slit material.

The simulation executes in real time on an HTML5 canvas. Particle emission rate and speed are configurable.
<!-- FILE_END: q-double-slit.md -->

<!-- FILE_START: double-slit-analytical.md -->
We present an analytical intensity pattern plotter for the $q$-deformed double-slit experiment (§6.7).

This simulator computes and plots the interference intensity envelope for two scattering modes derived from the categorical Dirac equation:

1. **Mode 1 (Massive particle)**: $q$-harmonic form scattering. The substrate parameter $q$ modifies the phase via the Reeb contraction term.
2. **Mode 2 (Photon)**: Julia-set envelope scattering with wavelength-dependent $q$-corrections.

**Default view**: Bach 2013 electron data (600 eV) overlaid on the $q$-deformed prediction with $q = 1.020$. This displays the fit between theory and digitised experimental points.

**Parameters**:

- $q$ — substrate parameter
- $a$ — slit width (nm)
- $d$ — slit separation (nm)
- $\lambda$ — de Broglie wavelength (pm for massive, nm for photon)
- $r_\xi$ — Reeb coupling ratio

The standard Fraunhofer pattern can be toggled for comparison. Preset configurations match published experimental setups.
<!-- FILE_END: double-slit-analytical.md -->

<!-- FILE_START: brings-surface-simulator.md -->
Interactive 3D visualisation of quaternionic spectral resolvent coordinates on Bring's surface (§3.1).

The simulator renders the four $\beta$-branches of the spectral resolvent in $\omega$-coordinates using Three.js WebGL:

- $\beta_1 = \pi - 3\alpha$ (blue)
- $\beta_2 = (\pi + \alpha)/3$ (red-orange)
- $\beta_3 = (3\pi + \alpha)/3$ (green)
- $\beta_4 = (5\pi + \alpha)/3$ (orange-yellow)

**Default view**: Standard resolvent with $N = 18$ $q$-series terms, moderate grid density, and $\omega$-coordinate projection. Auto-rotation enabled for an overview of the surface topology.

**Parameters**:

- $r_{\min}$, $r_{\max}$ — radial range for the resolvent.
- $\delta r$, $\delta\zeta$ — grid density (radial and angular).
- $N$ — $q$-series truncation precision (number of terms).
- Projection mode: $\omega$-coords, $+\mathrm{Sp}(1)$ rotation, or raw $x_j$.

Growth factor profiles and Weierstrass curve data appear in auxiliary panels.
<!-- FILE_END: brings-surface-simulator.md -->

<!-- FILE_START: quantum-brings-surface.md -->
We present an advanced interactive simulator of quantum Bring's surface with chiral tubes on the projective space-time brane (§3.1).

This extends the [basic Bring's surface simulator](#sim:brings-surface) with multi-canvas analysis panels:

- **Chiral grid.** Quantum colour coding (RGB components) of the chiral tube structure.
- **Weierstrass chart.** Elliptic curve invariants $\Delta$, $j$-invariant, and discriminant.
- **Affine coordinate chart.** Real and imaginary parts of the affine coordinates.
- **Fiber $\mathbb{CP}^1$.** Complex projective line parametrisation with interactive point selection.
- **Julia set.** Escape-time fractal computation at selected spectral points.
- **Möbius spectral panel.** Classification of spectral resolvents as elliptic, parabolic, or hyperbolic.

**Default view.** We display an overview with the chiral grid enabled. This reveals the relationship between the surface topology and the colour-tube coordinate system.

All panels are draggable and independently collapsible. The 3D surface and 2D analysis panels update in synchrony as parameters are adjusted.
<!-- FILE_END: quantum-brings-surface.md -->

<!-- FILE_START: beta-decay-simulator.md -->
This interactive simulator computes nuclear beta-decay half-lives from the substrate parameter $q$. It evaluates the transfer matrix Skein polynomial ([Skein polynomial](#prop:skein-polynomial-transfer-matrix)).

## Computed quantities

For a nucleus $\mathcal{N}(Z, N)$, the simulator determines four observables:

1. **Skein polynomials.** It evaluates $P_{\mathrm{par}}(q)$ and $P_{\mathrm{dau}}(q)$ for parent and daughter via $\binom{A}{2}$ transfer matrix multiplications ([transfer matrix operator](#def:transfer-matrix-operator)).
2. **$Q$-value.** It calculates $Q = |\ln(P_{\mathrm{dau}}/P_{\mathrm{par}})| \times E_{\times} \times \mu_0$. This calculation optionally includes the shell correction $\Delta_{\mathrm{shell}} + \Delta_{T_{3,5}}$ ([shell construction rules](#rem:shell-construction-rules)).
3. **Phase-space integral.** It evaluates $f(Z, Q)$ with the Skein-Coulomb Fermi function $F_q(Z, E)$ ([Skein-Coulomb enhancement](#prop:skein-coulomb-enhancement)) using $\alpha_{\mathrm{EM}}(q) = q^{-1}/([9]_q \cdot [10]_q)$.
4. **Half-life.** It computes $t_{1/2} = \ln 2 / \Gamma_\beta$, where $\Gamma_\beta = G_F^2 m_e^5 / (2\pi^3 \hbar) \cdot [2]_q \cdot f(Z, Q)$ ([hadron half-life](#prop:hadron-half-life)).

## Operating modes

- **From $q$.** The simulator predicts the $Q$-value from the transfer matrix ratio. This yields $5$--$7\%$ error for light nuclei ($A \leq 14$). Heavy nuclei overshoot due to naive nucleon ordering ([verification](#ex:hadron-half-life-verification)).
- **From $Q_{\mathrm{exp}}$.** The simulator uses experimental $Q$-values (NNDC/ENSDF). This isolates the $q$-dependent prefactors and Coulomb enhancement. All six benchmarks agree to $< 3\%$.

## Physical regimes

The canvas plot shows $t_{1/2}$ versus $q$ for the selected nucleus. It illustrates three regimes ([half-life regimes](#rem:hadron-half-life-regimes)):

- **Classical** ($q \to 1$). Here $\Gamma_\beta \to 0$. The system exhibits no beta decay.
- **Descartes** ($q = q_0$). The framework recovers observed nuclear lifetimes.
- **Deep quantum** ($q \to \infty$). Here $\Gamma_\beta \to \infty$. Decay is instantaneous.

The plot displays the sensitivity $\partial \ln \Gamma / \partial \ln q \approx 48$ at $q_0$. A $1\%$ shift in $q$ alters decay rates by roughly $50\%$.

## Benchmark nuclei

The verification nuclei and their experimental data are tabulated in [Table: Verification nuclei](#tbl:beta-decay-simulator-table-data). Witness data from `computations/all-nuclei-transfer-matrix.py`.
<!-- FILE_END: beta-decay-simulator.md -->

<!-- FILE_START: outro-observations.md -->
This closes the physical-observation chapter. We evaluated every categorical prediction from previous chapters at the substrate parameter $q_0 \approx 1.1097$. These include fundamental constants (speed of light $c_q$, Planck constant $\hbar_q$, Hausdorff dimension $d_H$), particle masses, atomic-mass ratios, hyperbolic volumes, and $\beta$-decay $Q$-values. We compared them against CODATA and NIST measurements to meet precision targets. Interactive simulators distributed with the paper expose this numerical machinery in a browser. A reader can perturb $q$ and watch the predictions track the substrate parameter live.

The next chapter restarts the building-up process at the molecular scale. We reuse the categorical mass predictions as energy inputs for the Hopf-chain construction of covalent bonds. The precision achieved here propagates into the chemistry chapters that follow.
<!-- FILE_END: outro-observations.md -->

