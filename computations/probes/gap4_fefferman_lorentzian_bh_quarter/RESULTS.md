# Closing Open Gap 4 (Option 4A): Canonical Fefferman 4D Lorentzian CR Circle-Bundle Metric $g_\theta$, Sparling–Graham–Lee Curvature, & Modular $(2\pi)/(8\pi) = 1/4$ Horizon Law

**Branch:** `claude/gap4-a0-fefferman-lorentzian-modular-20261123` (stacked on `claude/reeb-length-time-bh-lcq-20261123`, PR `#9240`, Issue `#9239`, Bean `qou-slfm`)
**Pre-registration commit:** `edf9f174ae4decbb7a8f702d554ab3fcf8f592b6`
**Lean 4 module (`§7c`, zero `ℝ`, `0` sorries, `0` custom axioms):** `folio/quantum-observable-universe/lean/QOU/GravitySpacetime/FeffermanLorentzianHorizonEntropy.lean` (`a3b2ffad7eb`)
**80-dps probe & witness:** `computations/probes/gap4_fefferman_lorentzian_bh_quarter/gap4_fefferman_lorentzian_bh_quarter_probe.py` (`ca3e49e4f99`) & `gap4-fefferman-lorentzian-bh-quarter.witness.json` (`107354d3edf`, `q0Anchor = "proton"`, `workdps = 80`, `output_dps = 70`, `selectedCandidate = "none"`, zero `float64`)

---

## 1. Executive Summary & Honest Verdict

1. **Kinematical Lorentzian Lift Gap Closed (`PROVED`, `0 sorry`, `§7c` Generic Field `K`):**
   - Whereas `cr-structure-lorentzian-lift.md` previously noted *"No such lift is constructed here"*, Fefferman's (1976) and Lee's (1986) canonical circle-bundle metric on $\pi : C(M^3) = (K_M \setminus \{0\})/\mathbb{R}_{>0} \to M^3$ ($\dim_{\mathbb{R}} C(M^3) = 4$),
     $$g_\theta(u, v) = \theta(u)\,\omega_0(v) + \theta(v)\,\omega_0(u) + L_\theta(\pi_* u, \pi_* v),$$
     provides a **canonical, zero-parameter 4D Lorentzian `(3,1)` metric** from $(M^3, \theta, J)$ alone once $\theta$ is normalized by QOU's Layer-I unit Reeb circuit $\ell_P(q) = \hbar_q t_P(q) = 1$ (`fefferman_locked_by_unit_reeb_circuit`).
   - Over any commutative ring / generic field `K` (`(2 : K) ≠ 0`, positive-definite Levi eigenvalues $\ell_1, \ell_2 > 0$, Tanaka–Webster scalar shift $c_R \in K$):
     * $\det G_{\mathrm{Feff}}(c_R, \ell_1, \ell_2) = -\ell_1 \ell_2 < 0$ independently of $c_R$ (`det_feffermanGram`, `det_feffermanGram_neg`),
     * Explicit unimodular $\mathrm{SL}_4(K)$ Sylvester congruence ($\det P(c_R) = 1$, zero square roots required) gives $P(c_R)^T G_{\mathrm{Feff}}(c_R, \ell_1, \ell_2) P(c_R) = \mathrm{diag}(-1, +1, \ell_1, \ell_2)$, certifying exact Lorentzian Sylvester inertia `(3, 1, 0)` (`fefferman_sylvester_congruence_3_1`, `fefferman_lorentzian_quadratic_inertia`),
     * Both the vertical $S^1$-fibre generator $\partial_\sigma$ and the shifted Reeb generator $k_+ = R_\theta - c_R \partial_\sigma$ are strictly null ($g_\theta(\partial_\sigma, \partial_\sigma) = g_\theta(k_+, k_+) = 0$, $g_\theta(k_+, \partial_\sigma) = 1$; `fefferman_null_and_pairing_identities`), and the induced 2D horizon-screen metric on $H = \ker\theta \cap \ker\omega_0$ is identically $L_\theta$ (`fefferman_screen_metric_eq_leviForm`).

2. **Sparling–Graham–Lee Curvature Diagnosis (`Weyl = 0`, Vacuum Obstruction `Ric(K, K) = 1/2`, & Universal Null Energy Positivity):**
   - Full Cartan moving-frame curvature evaluation (proved algebraically in `FeffermanLorentzianHorizonEntropy.lean` §2 and cross-checked numerically to `2.27e-80` across $S^3$, Heisenberg $\mathbb{H}^1$, Bring's hyperbolic contact link $UT(\Sigma_4)$, and the $q_0^{-1}$-rescaled horizontal model) establishes three structural results:
     1. **Conformal flatness (`W_{abcd} = 0`):** At Lee's canonical $\Lambda^{2,0}$ weight $\lambda_0 = 1/(n+2) = 1/3$ ($n = 1$), the Weyl curvature vanishes identically **if and only if** $c_R = R_W / 6$ (`lee_conformal_flatness_lock_iff`; omitting Lee's $R_W / 6$ shift produces $\|W\|_\infty = |R_W|/9 = 2/9 = 0.222222... \neq 0$ on $S^3$ and $UT(\Sigma_4)$). Consequently, the 4D Bach / Fefferman–Graham obstruction tensor vanishes identically on all locally spherical / constant-Webster-curvature Sasakian 3-manifolds.
     2. **Sparling–Graham obstruction to vacuum Einstein (`Ric = Λ g_θ` refuted):** Along the null Killing $S^1$-fibre $K = \partial_\sigma$, $g_\theta(K, K) = 0$ while $\mathrm{Ric}_{ab}(g_\theta) K^a K^b = +1/2 \neq 0$ for **every** $R_W$ (driven by contact twist $\omega_{ab}\omega^{ab} = \frac{1}{4}|d\theta|_{L_\theta}^2 = 1/2 > 0$), ruling out vacuum Einstein $R_{ab} = \Lambda g_{ab}$ (`sparling_graham_vacuum_einstein_obstruction`).
     3. **Exact Einstein–$\Lambda_W$ rank-1 wave tensor & null-cone focusing sign:** Instead of vacuum Ricci-flatness, $g_\theta$ satisfies the exact Einstein–$\Lambda_W$ equation with pure-radiation / wave covector $\xi = \sigma_\theta - \frac{R_W}{2}\theta$ and $\Lambda_W = R_W / 4$:
        $$G_{ab}(g_\theta) + \frac{R_W}{4}\,g_{ab} = \frac{1}{2}\,\xi_a \xi_b \qquad \Longrightarrow \qquad R_{ab}(g_\theta)\,k^a k^b = G_{ab}(g_\theta)\,k^a k^b = \frac{1}{2}\!\left(k_1 - \frac{R_W}{2} k_0\right)^2 \ge 0$$
        for **every** 4D null vector $k$ ($2 k_0 k_1 + k_2^2 + k_3^2 = 0$; `fefferman_einstein_rank_one_decomposition`, `fefferman_null_cone_ricci_nonneg`).

3. **Modular–Raychaudhuri $(2\pi)/(8\pi) = 1/4$ Law & Critical Dual Substrate Normalization Split (`1/4` vs `1/(4 q_0)`):**
   - Over any generic field `K`, dividing Jacobson's Einstein–Raychaudhuri horizon heat flux $\delta Q = \frac{c^2 a}{8\pi G}\delta A = \frac{c^3 \kappa}{8\pi G}\delta A$ by the Unruh/Bisognano–Wichmann Rindler modular temperature $T_U = \frac{\hbar a}{2\pi c} = \frac{\hbar \kappa}{2\pi}$ cancels $\pi$, $a$ ($\kappa$), and $\delta A$ identically to give $\frac{\delta Q / T_U}{\delta A} = \frac{1}{4\,\ell_{\mathrm{grav}}^2}$ with $\ell_{\mathrm{grav}}^2 = \frac{\hbar G}{c^3}$ (`modular_raychaudhuri_quarter_law`).
   - Testing **both** substrate gravitational normalizations from `qou-slfm` at 80 dps (`substrate_modular_entropy_density_dual_arms`):
     * **Arm N1 (`def:gravitational-constant` Planck identity $\ell_{\mathrm{grav,N1}}^2 = G_q(\hbar_q/c_q)^2 = 1$):** Gives **exact** $\delta S / \delta A_{\mathrm{sub}} = 1/4 = 0.2500000000...$ (`0%` deviation in unit Reeb-circuit area cells $\ell_P(q_0)^2 = 1$), requiring $a_0^{\mathrm{N1}} = 4 s_{\mathrm{punct}}$ ($2.77258872...$ for Catalan $\ln 2$; $2.79432330...$ for $TL$ $\ln[2]_{q_0}$).
     * **Arm N2 (Direct native-$q$ relativistic $\ell_{\mathrm{grav,N2}}^2 = \hbar_q G_q / c_q^3 = q_0 = 1.10997858...$):** Gives exact $1/4 = 0.25$ per relativistic $\ell_{\mathrm{grav,N2}}^2$ cell, and $\frac{1}{4 q_0} = 0.22522957098893537304...$ per unit Reeb-circuit cell $\ell_P(q_0)^2 = 1$ — an exact relative shift of **$-\hbar_{q_0} = -(1 - q_0^{-1}) = -9.90817160...\%$** originating from $\hbar_q c_q = q^{-1} \neq 1$, with corresponding Reeb-cell puncture area $a_0^{\mathrm{N2,sub}} = 4 q_0 s_{\mathrm{punct}}$ ($3.07751410...$ for $\ln 2$; $3.10163902...$ for $\ln[2]_{q_0}$).

---

## 2. Live-Verified Bibliographic Ledger (`doi.org/api/handles` `responseCode == 1`)

| Reference | Citation | Verified DOI (`responseCode == 1`) |
|---|---|---|
| Fefferman (1976) | *Ann. of Math.* (2) **103**(2), 395–416 | `10.2307/1970945` |
| Lee (1986) | *Trans. Amer. Math. Soc.* **296**(1), 411–429 | `10.1090/S0002-9947-1986-0837820-2` |
| Graham (1987) | *Amer. J. Math.* **109**(5), 853–874 | `10.2307/2374491` |
| Burns, Diederich & Shnider (1977) | *Duke Math. J.* **44**(2), 407–431 | `10.1215/S0012-7094-77-04419-2` |
| Jacobson (1995) | *Phys. Rev. Lett.* **75**(7), 1260–1263 | `10.1103/PhysRevLett.75.1260` |
| Bisognano & Wichmann (1975) | *J. Math. Phys.* **16**(4), 985–1007 | `10.1063/1.522605` |
| Bisognano & Wichmann (1976) | *J. Math. Phys.* **17**(3), 303–321 | `10.1063/1.522898` |

---

## 3. 80-dps Numerical Results (`q0Anchor = "proton"`)

### 3.1 Batteries F1 & F2 — Fefferman `(3,1)` Signature, Eigenvalues, & Sparling–Graham–Lee Curvature

| Model | $R_W$ | Lee Shift $c_R = R_W/6$ | $\det G_{\mathrm{Feff}}$ | Eigenvalues $(\lambda_-, \lambda_+, \ell_1, \ell_2)$ | $\mathrm{Ric}_{00}, \mathrm{Ric}_{01}, \mathrm{Ric}_{11}, \mathrm{Ric}_{22}$ | $\|W\|_\infty$ (Lee lock / $c_R=0$) |
|---|---:|---:|---:|---|---|---|
| `M0_heisenberg_flat` ($\mathbb{H}^1$) | `0` | `0` | `-1` | `(-1, +1, +1, +1)` | `(0, 0, +0.5, 0)` | `0` / `0` |
| `M1_cr_three_sphere_S3` ($S^3$) | `+2` | `+1/3` | `-1` | `(-0.72075922, +1.38742589, +1, +1)` | `(+0.5, +0.5, +0.5, +1)` | `0` / `0.222222...` |
| `M2_bring_ut_sigma4` ($UT(\Sigma_4)$, $\chi=-6$) | `-2` | `-1/3` | `-1` | `(-1.38742589, +0.72075922, +1, +1)` | `(+0.5, -0.5, +0.5, -1)` | `0` / `0.222222...` |
| `M3_substrate_anisotropic_q0` ($\ell_i = q_0^{-2}$) | `-1.62330751` | `-0.27055125` | `-0.65878182` | `(-1.30650394, +0.76540144, +0.81165375, +0.81165375)` | `(+0.32939091, -0.40582688, +0.5, -0.81165375)` | `1.58e-81` / `0.18036750...` |

- Maximum $\mathrm{SL}_4$ Sylvester congruence, Leibniz determinant, and null-pairing residual across all models: **`2.11e-81`**.
- Maximum Cartan torsion-freeness, metric-compatibility, rank-1 Einstein–$\Lambda_W$ wave decomposition, and 6-ray null-cone Raychaudhuri identity residual: **`2.27e-80`**.

### 3.2 Battery F3 — Side-by-Side Comparison of QOU Gravitational Normalizations (`selectedCandidate = "none"`)

| Arm | Planck-Area Definition $\ell_{\mathrm{grav}}^2$ | $\ell_{\mathrm{grav}}^2$ at $q_0$ | $\delta S / \delta A_{\mathrm{sub}}$ in Reeb Cells ($\ell_P^2 = 1$) | Exact Rel. Shift vs $1/4$ | Required $a_0^\star$ in Reeb Cells (`Cat` $\ln 2$ / `TL` $\ln[2]_{q_0}$ / `Haar`) |
|---|---|---:|---:|---:|---|
| **Arm N1** (`def:gravitational-constant`) | $G_q (\hbar_q / c_q)^2$ | `1` (exact) | `0.250000000000000000000000000000` | `0` (`0.0000%`) | `2.7725887222` / `2.7943232996` / `2.7509327060` |
| **Arm N2** (Direct Relativistic) | $\hbar_q G_q / c_q^3 = \hbar_q^2 / S_{\mathrm{cell}}(q)$ | `1.109978582751380807591669095611` ($= q_0$) | `0.225229570988935373040205720620` ($= \frac{1}{4 q_0}$) | $-\hbar_{q_0} = -0.0990817160...$ (`-9.9082%`) | `3.0775141005` / `3.1016390158` / `3.0534763863` |

---

## 4. Remaining Open Boundary (`Rule 13a` — `FeffermanDynamicalEinsteinHorizonConjecture`)

- **Closed in this package:** Canonical zero-parameter `(3,1)` Lorentzian CR circle-bundle metric lift $g_\theta$ (`FeffermanLorentzianHorizonEntropy` §1), exact Sparling–Graham–Lee curvature and universal null-focusing positivity `Ric(k, k) >= 0` (§2), and exact generic-field `(2*pi)/(8*pi) = 1/4` cancellation + dual `1` vs `q` split (§3).
- **Isolated as open (`0` instances):**
  1. Deriving dynamical metric perturbation response $\delta G_{ab} k^a k^b = \frac{8\pi G}{c^4}\delta T_{ab} k^a k^b$ on hypersurface-orthogonal Rindler cuts of $(C(M^3), g_\theta)$ from QOU's $q$-Yang–Mills–Levi / spectral action (since background $g_\theta$ is fixed by CR data with intrinsic twist curvature $\mathrm{Ric}(K,K) = 1/2$).
  2. Deriving from QOU's action whether horizon boost coupling uses native unit Planck area $\ell_{\mathrm{grav,N1}}^2 = 1$ (giving exact $1/4$) or relativistic $\ell_{\mathrm{grav,N2}}^2 = q_0$ (giving $\frac{1}{4 q_0}$ in unit Reeb cells, exact $1/4$ in $\ell_{\mathrm{grav,N2}}^2$ cells).
