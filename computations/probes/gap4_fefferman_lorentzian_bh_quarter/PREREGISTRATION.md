# Pre-Registration: Canonical Fefferman 4D Lorentzian CR Circle-Bundle Metric $g_\theta$ & Modular–Raychaudhuri $(2\pi)/(8\pi) = 1/4$ Horizon Law (Gap 4 — Option 4A)

**Date:** 2026-11-23
**Branch:** `claude/gap4-a0-fefferman-lorentzian-modular-20261123` (stacked on `claude/reeb-length-time-bh-lcq-20261123`, PR `#9240`, Issue `#9239`, Bean `qou-slfm`)
**Discipline:** Written, committed, and pushed **before** writing or executing `gap4_fefferman_lorentzian_bh_quarter_probe.py`.

---

## 1. Precision, Calibration & Anti-Fit Lock (STRICT)

- **Working precision:** `mpmath.workdps(80)` (`WORK_DPS = 80`, `OUT_DPS = 70` serialized into the witness JSON), `truncation_bound = 1e-70`.
- **Substrate pin:** `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`).
- **Zero `float64`:** Zero `float(...)` casts, zero floating-point literals, zero `numpy` float arrays anywhere in the script or witness.
- **Zero tunable parameters:**
  - The contact 1-form $\theta$ is fixed by QOU's Layer-I unit Reeb-circuit normalization $\ell_P(q) = \hbar_q t_P(q) = 1$ (`normalisedCircuitLength_eq_one`), with per-step share $\hbar_q = 1 - q^{-1}$ and causal cone speed $c_q = (q - 1)^{-1}$.
  - On the canonical CR circle bundle $\pi : C(M^3) = (K_M \setminus \{0\})/\mathbb{R}_{>0} \to M^3$ ($\dim_{\mathbb{R}} C(M^3) = 4$), Lee's (1986) pseudohermitian Fefferman metric
    $$g_\theta(u, v) = \theta(u)\,\omega_0(v) + \theta(v)\,\omega_0(u) + L_\theta(\pi_* u, \pi_* v)$$
    has **zero adjustable Immirzi-like or conformal parameters** once $\theta$ is fixed.
  - Both substrate gravitational normalizations proved in `ReebLengthTimeAndLightConeEntropy.lean` (`G_q(\hbar_q/c_q)^2 = 1` vs `\hbar_q G_q / c_q^3 = q`) are evaluated side-by-side (`selectedCandidate = "none"`), with no post-hoc rescaling to force $1/4$.

---

## 2. Live-Verified Literature Citations (`doi.org/api/handles` `responseCode == 1` & Crossref)

1. **Charles L. Fefferman (1976)**, *"Monge-Ampere Equations, the Bergman Kernel, and Geometry of Pseudoconvex Domains"*, *Annals of Mathematics* (2) **103**(2), 395–416 — DOI: `10.2307/1970945` (`responseCode == 1`).
2. **John M. Lee (1986)**, *"The Fefferman metric and pseudo-Hermitian invariants"*, *Transactions of the American Mathematical Society* **296**(1), 411–429 — DOI: `10.1090/S0002-9947-1986-0837820-2` (`responseCode == 1`; note `10.2307/2000577` resolves to Kennedy & Rogers 1986, pp. 327–340, caught during pre-registration live check).
3. **C. Robin Graham (1987)**, *"On Sparling's Characterization of Fefferman Metrics"*, *American Journal of Mathematics* **109**(5), 853–874 — DOI: `10.2307/2374491` (`responseCode == 1`).
4. **D. Burns, Jr., K. Diederich, & S. Shnider (1977)**, *"Distinguished curves in pseudoconvex boundaries"*, *Duke Mathematical Journal* **44**(2), 407–431 — DOI: `10.1215/S0012-7094-77-04419-2` (`responseCode == 1`).
5. **Ted Jacobson (1995)**, *"Thermodynamics of Spacetime: The Einstein Equation of State"*, *Physical Review Letters* **75**(7), 1260–1263 — DOI: `10.1103/PhysRevLett.75.1260` (`responseCode == 1`, repo key `[jacobson1995]`).
6. **Joseph J. Bisognano & Eyvind H. Wichmann (1975)**, *"On the duality condition for a Hermitian scalar field"*, *Journal of Mathematical Physics* **16**(4), 985–1007 — DOI: `10.1063/1.522605` (`responseCode == 1`).
7. **Joseph J. Bisognano & Eyvind H. Wichmann (1976)**, *"On the duality condition for quantum fields"*, *Journal of Mathematical Physics* **17**(3), 303–321 — DOI: `10.1063/1.522898` (`responseCode == 1`).

---

## 3. Pre-Registered Lean 4 & 80-dps Probe Batteries

### Battery F1 — Algebraic `(3,1)` Lorentzian Signature & Zero-Parameter Null Geometry of $g_\theta$
- **Lean 4 (`§7c` generic field `K` + `[LinearOrder K] [IsStrictOrderedRing K]`):**
  - Formalize the $4 \times 4$ Gram matrix $G_{\mathrm{Feff}}(c_R, \ell_1, \ell_2)$ of $g_\theta(u, v) = \theta(u)\omega_0(v) + \theta(v)\omega_0(u) + L_\theta(\pi_* u, \pi_* v)$ on $V = K \cdot R_\theta \oplus K \cdot \partial_\sigma \oplus H$ (`dim H = 2`, positive-definite Levi eigenvalues $\ell_1, \ell_2 > 0$, Reeb connection component $\omega_0(R_\theta) = c_R$, $\omega_0(\partial_\sigma) = 1$, $\theta(R_\theta) = 1$, $\theta(\partial_\sigma) = 0$).
  - Prove $\det G_{\mathrm{Feff}}(c_R, \ell_1, \ell_2) = -\ell_1 \ell_2 < 0$ independently of $c_R$, universal fibre nullity $g_\theta(\partial_\sigma, \partial_\sigma) = 0$, canonical pairing $g_\theta(R_\theta, \partial_\sigma) = 1$, Reeb nullity $g_\theta(R_\theta, R_\theta) = 0$ at $c_R = 0$, and shifted null generator $k_+ = R_\theta - c_R \partial_\sigma$ satisfying $g_\theta(k_+, k_+) = 0$ and $g_\theta(k_+, \partial_\sigma) = 1$ for **every** $c_R \in K$.
  - Prove an explicit unimodular $\mathrm{SL}_4(K)$ Sylvester congruence ($\det P = 1$, `Invertible (2 : K)`, zero square roots required) $P^T G_{\mathrm{Feff}}(c_R, \ell_1, \ell_2) P = \mathrm{diag}(-1, +1, \ell_1, \ell_2)$, establishing exact Lorentzian Sylvester inertia `(3, 1, 0)` (three strictly positive and one strictly negative diagonal entries) plus positive-definite 2D horizon screen metric $g_\theta|_H = L_\theta$.
- **80-dps Probe Check:** Verify $\det G_{\mathrm{Feff}}$, $\mathrm{SL}_4$ congruence residual, nullity residuals, and exact eigenvalue spectrum $(\lambda_-, \lambda_+, \ell_1, \ell_2) = (c_R - \sqrt{c_R^2 + 1},\, c_R + \sqrt{c_R^2 + 1},\, \ell_1,\, \ell_2)$ across Webster-flat ($R_W = 0$), spherical CR $S^3$ ($R_W = +2$), hyperbolic/Bring contact link $UT(\Sigma_4)$ ($R_W = -2$), and substrate-scaled Levi forms at $q_0$.

### Battery F2 — Sparling–Graham–Lee Curvature $R_{\mu\nu}(g_\theta)$, Conformal Flatness, & Vacuum Obstruction
- **Cartan Moving-Frame & Bochner–Raychaudhuri Test:**
  - Evaluate the Levi-Civita connection, full Riemann tensor $R^a{}_{bcd}(g_\theta)$, Ricci tensor $R_{ab}(g_\theta)$, scalar curvature $R(g_\theta)$, Einstein tensor $G_{ab}(g_\theta)$, and Weyl tensor $W_{abcd}(g_\theta)$ on the general constant-Webster-curvature Sasakian 3-manifold family $M_{R_W}^3$ ($R_W > 0$: CR 3-sphere $S^3 \subset \mathbb{C}^2$; $R_W = 0$: Heisenberg CR group $\mathbb{H}^1$; $R_W < 0$: hyperbolic unit tangent bundle $UT(\Sigma_g)$ including Bring's genus-4 surface $\Sigma_{\mathrm{Bring}}$, Euler characteristic $\chi(\Sigma_4) = 2 - 2(4) = -6$).
  - Test the exact Lee (1986) conformal-flatness lock $\lambda_0 R_W + c_R = \frac{1}{2} R_W$ ($\lambda_0 = \frac{1}{n+2} = \frac{1}{3} \implies c_R = \frac{1}{6} R_W$):
    1. Verify whether $W_{abcd}(g_\theta) = 0$ identically (and hence the 4D Bach / Fefferman–Graham obstruction tensor vanishes identically on locally spherical models).
    2. Test whether $g_\theta$ can satisfy **vacuum** Einstein equations ($R_{ab} = \Lambda g_{ab}$): check Sparling–Graham's twist obstruction $R_{ab} K^a K^b = \omega_{ab}\omega^{ab} = +1/2 > 0$ along the null Killing fibre $K = \partial_\sigma$ ($g_{ab} K^a K^b = 0$).
    3. Test the exact rank-1 Einstein–$\Lambda_W$ null-current decomposition $G_{ab}(g_\theta) + \frac{R_W}{4} g_{ab} = \frac{1}{2}\xi_a \xi_b$ ($\xi = \sigma_\theta - \frac{R_W}{2}\theta$) and verify the universal Null Energy / Raychaudhuri positivity identity $R_{ab}(g_\theta) k^a k^b = \frac{1}{2}(\xi_a k^a)^2 \ge 0$ across the entire 4D null cone $g_{ab} k^a k^b = 0$ (formalized algebraically in Lean 4!).

### Battery F3 — Modular–Raychaudhuri $(2\pi)/(8\pi) = 1/4$ Cancellation & Dual Gravitational Normalizations (`1` vs `q_0`)
- **Lean 4 (`§7c` generic field `K`):**
  - Prove in both surface-gravity ($\kappa$, $[\kappa]=1/T$) and proper-acceleration ($a = c\kappa$, $[a]=L/T^2$) conventions over any field `K` (`(2 : K) ≠ 0`, `pi ≠ 0`, `hbar ≠ 0`, `c ≠ 0`, `G ≠ 0`, `κ ≠ 0`, `δA ≠ 0`) that Unruh/Bisognano–Wichmann Rindler modular temperature $T_U = \frac{\hbar a}{2\pi c} = \frac{\hbar \kappa}{2\pi}$ combined with Einstein–Raychaudhuri horizon heat flux $\delta Q = \frac{c^2 a}{8\pi G}\delta A = \frac{c^3 \kappa}{8\pi G}\delta A$ gives
    $$\frac{\delta Q / T_U}{\delta A} = \frac{c^3}{4 \hbar G} = \frac{1}{4\,\ell_{\mathrm{grav}}^2} \qquad \left(\ell_{\mathrm{grav}}^2 := \frac{\hbar G}{c^3}\right).$$
- **Critical Side-by-Side 80-dps Comparison at $q_0 = 1.10997858...$ (`qou-slfm` Dual Normalizations):**
  - **Arm N1 (`def:gravitational-constant` / native unit Planck identity $\ell_{\mathrm{grav,N1}}^2 = G_q(\hbar_q/c_q)^2 = 1$):** Evaluate $\frac{1}{4\,\ell_{\mathrm{grav,N1}}^2} = \frac{1}{4} = 0.25$ (`0%` deviation vs $1/4$ in unit Reeb-circuit area cells $\ell_P(q_0)^2 = 1$) and corresponding puncture lock $a_0^{\mathrm{N1}} = 4 s_{\mathrm{punct}}$.
  - **Arm N2 (Direct native-$q$ relativistic combination $\ell_{\mathrm{grav,N2}}^2 = \hbar_q G_q / c_q^3 = q_0$):** Evaluate $\frac{c_q^3}{4 \hbar_q G_q} = \frac{1}{4 q_0} = \frac{q_0^{-1}}{4}$ in unit Reeb-circuit area cells, testing the exact `q_0` shift $0.22522957...$ (`-\hbar_{q_0} = -9.90817...%` relative to $0.25$, while equaling exact `0.25` per relativistic $\ell_{\mathrm{grav,N2}}^2 = q_0$ cell) and prove in Lean that the ratio of Arm N2 to Arm N1 equals $\hbar_q c_q = q^{-1}$.
  - Isolate the remaining dynamical action & normalization bridge honestly as a zero-instance Rule-13a conjecture class (`FeffermanDynamicalEinsteinHorizonConjecture`).
