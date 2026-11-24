# Reeb Length/Time Reconciliation ($d_{\mathrm{Reeb}}$, KMS Time, $c_q$, $\mathfrak{E} = \mathfrak{m} c_q^2$, $L_{\mathrm{cal}}$) & Light-Cone (`LCQ`) Bekenstein–Hawking Channel Counting

**Bean:** `qou-slfm` (integrating upstream threads `qou-mumr`, `qou-5uj7`, `qou-jfx8`, `qou-apma`, and `#9207` `UnifiedClockScaleLayers` / `FiniteRieffelQuantumMetric`)
**Branch:** `claude/reeb-length-time-bh-lcq-20261123`
**Pre-registration commit:** `3008f273ec92545960757eb158f6afd6951aff6a`
**Lean 4 module (`§7c`, zero `ℝ`, `0` sorries):** `folio/quantum-observable-universe/lean/QOU/GravitySpacetime/ReebLengthTimeAndLightConeEntropy.lean`
**80-dps probe & witness:** `computations/probes/reeb_length_time_bh_lcq/reeb_length_time_bh_lcq_probe.py` & `reeb-length-time-bh-lcq.witness.json` (`q0Anchor = "proton"`, `workdps = 80`, `output_dps = 70`, zero `float64`)

---

## 1. Executive Summary & Honest Verdict

1. **Exact Length / Computation-Time / Causal-Cone / Mass-Energy / $L_{\mathrm{cal}}$ Dictionary (`PROVED`, `0` sorries, `§7c` generic field `K`):**
   - **Share vs Total (`qou-mumr`, `#9207`):** The single algebraic grain $\hbar_q = 1 - q^{-1} = (q-1)/q$ is the per-step Reeb share of $D_\nabla = q^{-1}\nabla + \hbar_q \iota_\xi \nabla$, while $t_P(q) = \hbar_q^{-1} = q/(q-1)$ is the full-circuit Reeb tick, giving the unit-normalised Reeb circuit $\ell_P(q) = \hbar_q t_P(q) = 1$ (`normalisedCircuitLength_eq_one`).
   - **Causal Lieb–Robinson Cone (`lieb_robinson_cone_slope`, `dirac_split_step_cost_identity`):** Over $N = d_{\mathrm{Reeb}}(\gamma) \in \mathbb{N}$ discrete $f_q$-iterations, Reeb computation time is $\Delta t_{\mathrm{comp}}(N, q) = N \hbar_q$ and horizontal spatial reach is $\Delta x_{\mathrm{cone}}(N, q) = N q^{-1}$. Their ratio is the speed of light $c_q(q) = q^{-1}/\hbar_q = (q-1)^{-1} = t_P(q) - 1$, satisfying $\Delta x_{\mathrm{cone}}(N, q) = c_q(q) \Delta t_{\mathrm{comp}}(N, q)$ and $\Delta x_{\mathrm{cone}}(N, q) + \Delta t_{\mathrm{comp}}(N, q) = N$.
   - **KMS Modular Clock vs Traciality Obstruction (`kms-length-dynamics` + `OqSU2ModularNakayama`):** Any tracial functional $\varphi(xy) = \varphi(yx)$ (`tr_M`) forces $\omega = 1$ ($\beta = 0$) on any grading character (`tracial_kms_grading_trivial`), and the inhomogeneous Hecke relation $T_s^2 = h T_s + 1$ ($h \neq 0$) admits no non-trivial multiplicative length character (`hecke_quadratic_grading_trivial`). Non-trivial modular computation time arises instead from non-tracial density-weighted states $\varphi_D(x) = \tau(D x)$ (`density_weighted_discrete_kms`), realized on $O_q(SU(2))$ by Woronowicz's modular automorphism $\nu_q(\alpha) = q^2 \alpha$ (`oqsu2_modular_clock_iterate`, modular inverse temperature $\beta_{\mathrm{mod}}(q_0) = 2 \ln q_0 = 0.2086820...$).
   - **Categorical Energy $\mathfrak{E} = \mathfrak{m} c_q^2$ & Dual Gravitational Normalisations (`qou-91w7`):** Over any field $K$, $\mathfrak{E}(q, \mathfrak{m}) = \mathfrak{m}/(q-1)^2$ satisfies $\mathfrak{E}(q, \mathfrak{m}) \hbar_q^2 = \mathfrak{m} q^{-2}$ (`categoricalEnergy_identities`). Because $\hbar_q c_q(q) = q^{-1} \neq 1$ in native $q$-connection units, $G_q = c_q^3 \hbar_q / S_{\mathrm{cell}}(q) = q^2/(q-1)^4$ satisfies **both** $G_q (\hbar_q / c_q)^2 = 1$ (`def:gravitational-constant`) **and** $\hbar_q G_q / c_q^3 = \hbar_q^2 / S_{\mathrm{cell}}(q) = q$ (`gravCoupling_planck_units_and_newton_area`).
   - **Boundary $L_{\mathrm{cal}}$ Scale Invariance (`rescaleLipInv_dualBound_iff`, `calibration_cancels_in_observables`):** Laboratory length calibration $L_{\mathrm{cal}} > 0$ (CAL-1 $\bar{\lambda}_{C,e}$ vs SI $\ell_{\mathrm{Planck}}^{\mathrm{SI}}$, separated by $2.389222 \times 10^{22}$) rescales Layer-II Rieffel distance bounds linearly while cancelling identically from all dimensionless ratios, $c_q(q)$, and $A / (4 \ell_P^2)$.

2. **Honest Diagnosis on Bekenstein–Hawking $S_{\mathrm{BH}} = A / (4 \ell_P^2)$ from Minimal Crossing / `LCQ` Channel Counting (`OPEN GEOMETRIC GAP` — Rule-13a Class `LCQHorizonPunctureAreaConjecture`):**
   - **What channel counting proves unconditionally:** On a causal horizon cut $\Sigma$ pierced by $N_\Sigma$ minimal $TL_{N_\Sigma}(q)$ / spin-$1/2$ punctures (at non-root-of-unity $q_0 > 1$), odd $N_\Sigma$ has zero singlets (`tlSingletDim_odd`), while even $N_\Sigma = 2m$ has exact singlet dimension $C_m = \frac{1}{m+1}\binom{2m}{m}$ (`tlSingletDim_even`), bounded purely over $\mathbb{N}$ by $4^m / (m+1)^2 \le C_m \le 4^m$ (`catalan_two_sided_exponential_bounds`). This pins the microcanonical singlet entropy per puncture to **$s_{\mathrm{Cat}} = \ln 2 = 0.69314718...$** with the exact **Kaul–Majumdar $-\frac{3}{2}\ln N_\Sigma$** subleading logarithmic term (contrasted with $-\frac{1}{2}\ln N_\Sigma$ for $U(1)$-only projections, $s_{\mathrm{TL}}(q_0) = \ln [2]_{q_0} = 0.69858082...$ for loop fugacity, and $s_{\mathrm{Haar}}(q_0) = 0.68773318...$ for Woronowicz Haar modular qubits).
   - **Why $S = A / (4 \ell_P^2)$ does NOT follow without an area-focusing theorem:** By `horizon_quarter_area_lock_iff`, $S = N_\Sigma s_{\mathrm{punct}}$ equals $A / (4 \ell_P^2)$ for $A = N_\Sigma a_0 \ell_P^2$ **if and only if** $a_0 = 4 s_{\mathrm{punct}}$ ($4 \ln 2 = 2.7725887...$ or $4 \ln [2]_{q_0} = 2.7943233...$). Every pre-registered un-tuned rational/Sasakian candidate in QOU misses $1/4$ by **$\ge 11.1\%$** (`unit_puncture_area_misses_quarter_law` + Battery C table below), and QOU's $D_\nabla$ Reeb share $\hbar_{q_0} = 0.0990817...$ differs from the critical LQG Immirzi poles ($0.2086194...$ Casimir; $0.2371449...$ DL $\sqrt{\text{Casimir}}$; $0.2740182...$ full-qdim $\sqrt{\text{Casimir}}$) by **$2.11\times$–$2.77\times$**.
   - **Where $1/4$ structurally comes from in `LCQ`:** Across a Lorentzian light-cone / Rindler horizon cut, Bisognano–Wichmann modular boost periodicity ($\delta S = \frac{2\pi}{\hbar}\delta K_{\mathrm{boost}}$) divided by Einstein–Raychaudhuri null-sheet focusing ($\delta A = \frac{8\pi G}{c^3}\delta K_{\mathrm{boost}}$) cancels $2\pi / (8\pi) = 1/4$ identically and forces $a_0 = 4 s_{\mathrm{punct}}$ (`bekenstein_hawking_and_puncture_lock_of_lcq`). Because `cr-structure-lorentzian-lift.md` explicitly records that no Lorentzian metric lift or Raychaudhuri variation has yet been constructed from QOU's twisting CR 3-manifold, these two premises are isolated as the **zero-instance primary conjecture class** `LCQHorizonPunctureAreaConjecture` (Rule 13a).

---

## 2. Prior Pushed Thread & Branch Notes Recovered

| Source / Pushed Branch | Key Result Recovered & Integrated |
|---|---|
| `origin/main` `#9207` (`UnifiedClockScaleLayers.lean`, `FiniteRieffelQuantumMetric.lean`, `spacetime-length-distance-layers.md`) | Three-layer scale stratification: Layer I $\hbar_q = 1 - q^{-1}$, $t_P = \hbar_q^{-1}$, $\hbar_q t_P = 1$; Layer II Rieffel–Kantorovich distance on faithful $TL_n(q) = H_n(q)/\mathrm{rad}$; Layer III empirical $\lambda_{C,e}$ vs $\ell_{\mathrm{Planck}}^{\mathrm{SI}}$. |
| `claude/kms-length-dynamics-2026-08-31` (`kms_length_dynamics_exclusion_probe.py`) | Proves Coxeter-length scaling fails on $H_n(q)$ (inhomogeneous quadratic) and tracial $\mathrm{tr}_M$ forces $\beta = 0$ even on $\mathrm{gr}\,H_n(q)$; finite-$\beta$ modular dynamics requires a non-tracial density weight $\varphi(x) = \tau(D x)$. Formalized generically in §2 of `ReebLengthTimeAndLightConeEntropy.lean`. |
| `claude/speedoflight-generic-promotion-2026-09-05` & `information-speed-of-light.lean` | Flags `MathConstants.speedOfLight` classicality `1/0 = 0` boundary and notes `planck_identity` in `MathConstants.lean` was over `ℝ`. §1 proves `gravCoupling_planck_units_and_newton_area` over any generic `[Field K]` (`q ≠ 0, 1`, $2q-1 \neq 0$) with zero `ℝ`. |
| `claude/sdp-analysis-light-cone-recursion-2026-09-16` & `qou-jfx8` | Establishes disjoint-block LR multiplicativity, common affine light-cone interface trace $z_D + d_{\mathrm{kind}}$, and canonical geodesic contact orientation $\alpha$ on $UT(\Sigma_4)$ ($\ell = -1/6$). |
| `claude/port-8096-reeb-holonomy-laplacian-2026-11-20` | Shows the Reeb-holonomy Laplacian weight is $(q^{-1} + \hbar_q)^2 = 1^2 = 1$ (no spurious $\hbar_q^2$ factor). |
| `cat/round88-...-immirzihorizontower-...` & `lqg-entropy-qdim-partition-pole.{md,lean}` | Distinguishes pure $j=1/2$ vs full higher-spin horizon partition pole $Z_1(s_\star) = 1$, noting explicitly that $\gamma(q) = s_\star(q)/(2\pi)$ fixes $\gamma$ *by matching* $S = A/(4\ell_P^2)$ rather than deriving $1/4$ from scratch. |
| `docs/coordination/owner-rulings.md` (`qou-91w7`, 2026-11-22) | Rules that $\mathfrak{E} = \mathfrak{m} c_q^2$ is a dimensionless **categorical energy** in $\mathbb{Q}(q)$ whose map to MeV must come from CAL-1/2/3 at the Layer-III boundary. |

---

## 3. 80-dps Numerical Results (`q0Anchor = "proton"`)

### 3.1 Battery A — Reeb Scales, Causal Cone, KMS Clock, & Gravitational Normalisations

| Quantity | Formula | 80-dps Value (truncated to 30 digits) |
|---|---|---|
| $q_0$ (proton pin) | `q_at(80)` | `1.109978582751380807591669095611` |
| Horizontal $D_\nabla$ weight | $q_0^{-1}$ | `0.900918283955741492160822882481` |
| Per-step Reeb share | $\hbar_{q_0} = 1 - q_0^{-1}$ | `0.099081716044258507839177117519` |
| Full-circuit Planck tick | $t_P(q_0) = \hbar_{q_0}^{-1}$ | `10.092679456150245391103970355657` |
| Causal cone speed | $c_q(q_0) = (q_0 - 1)^{-1} = t_P(q_0) - 1$ | `9.092679456150245391103970355657` |
| Categorical energy factor | $c_q(q_0)^2 = (q_0 - 1)^{-2}$ | `82.676819692296722298122086503386` |
| Share $\times$ speed | $\hbar_{q_0} c_q(q_0) = q_0^{-1}$ | `0.900918283955741492160822882481` |
| $O_{q_0}(SU(2))$ modular step | $q_0^2$ ($\beta_{\mathrm{mod}} = 2 \ln q_0$) | `1.232052454166497461180151110864` (`0.208682034688...`) |
| Operational / cell entropy | $\eta_q(q_0),\; S_{\mathrm{cell}}(q_0)$ | `0.892751751146652...`, `0.008845539246672...` |
| Substrate $G_q(q_0)$ | $q_0^2 / (q_0 - 1)^4$ | `8421.6409739568087278554280875259` |
| Dual Planck normalisations | $G_q(\hbar_q/c_q)^2$ vs $\hbar_q G_q / c_q^3$ | `1` (exact) vs `1.109978582751380807591669095611` ($= q_0$) |
| Layer-III scale hierarchy | $\bar{\lambda}_{C,e} / \ell_{\mathrm{Planck}}^{\mathrm{SI}}$ | `2.389222415027331701990094e+22` |

### 3.2 Battery B — Horizon Crossing Channel Entropy Rates & Kaul–Majumdar Scaling

| Channel / Ensemble | Exact Expression | Entropy Rate per Puncture (30 digits) | Required $a_0^\star = 4 s_{\mathrm{punct}}$ |
|---|---|---|---|
| **Catalan $TL_{N_\Sigma}$ singlet** ($N_\Sigma = 2m$) | $\lim_{m\to\infty} \frac{1}{2m}\ln C_m = \ln 2$ | `0.693147180559945309417232121458` | `2.772588722239781237668928485833` |
| **Jones–Wenzl loop fugacity** ($[2]_{q_0}$) | $\ln(q_0 + q_0^{-1})$ | `0.698580824894173876038362727441` | `2.794323299576695504153450909763` |
| **Half-power fugacity** ($[2]_{q_0^{1/2}}$) | $\ln(q_0^{1/2} + q_0^{-1/2})$ | `0.694506919115836415172185358134` | `2.778027676463345660688741432535` |
| **Woronowicz Haar modular qubit** | $-\sum_{\pm} p_\pm \ln p_\pm$ ($p_+ = \frac{q_0^2}{1+q_0^2}$) | `0.687733176500215729768657507926` | `2.750932706000862919074630031703` |
| **Spin-1 / adjoint** ($[3]_{q_0}$) | $\ln(q_0^2 + 1 + q_0^{-2})$ | `1.113075920404819572858101800321` | `4.452303681619278291432407201283` |
| **3-strand $TL_3$ planar per strand** | $\frac{1}{3}\ln 5$ ($\dim TL_3 = C_3 = 5$) | `0.536479304144700090525992205936` | `2.145917216578800362103968823742` |

- **Subleading logarithmic law verified to $N_\Sigma = 10{,}000$ ($m = 5{,}000$):**
  - Full $U_{q_0}(\mathfrak{sl}_2)$ singlet $C_m$: effective logarithmic exponent converges cleanly to **$-3/2 = -1.5$** (`1.50002441...` at $N_\Sigma = 10{,}000$, order-$N_\Sigma^{-1}$ asymptotic residual `2.83e-8`), reproducing the Kaul–Majumdar (2000) $-\frac{3}{2}\ln A$ correction.
  - Abelian $U(1)$ zero-weight projection $\binom{2m}{m}$: effective logarithmic exponent converges to **$-1/2 = -0.5$** (`0.50002713...` at $N_\Sigma = 10{,}000$), reproducing Meissner's (2004) $-\frac{1}{2}\ln A$ correction.
- **Full $SU_{q_0}(2)$ spin-tower partition poles ($Z_1(s_\star) = 1$):**
  - Casimir exponent (`lqg-entropy-qdim-partition-pole.lean`): $s_\star(q_0) = 1.31079446...$, $\gamma_\star(q_0) = 0.20861942...$ (vs $q=1$: $\gamma_\star(1) = 0.20828962...$).
  - Domagala–Lewandowski $\sqrt{\text{Casimir}}$ ($w=2$): $\gamma_{\mathrm{DL}}(q_0) = 0.23714492...$ (vs classical $\gamma_{\mathrm{DL}}(1) = 0.23753296...$).
  - Full $[2j+1]_q$ $\sqrt{\text{Casimir}}$: $\gamma_{\mathrm{ABDFV}}(q_0) = 0.27401825...$.

### 3.3 Battery C — Side-by-Side Test of Un-Tuned Candidate Area Quanta $a_0$

| Candidate ID | Zero-Parameter Area Definition $a_0$ | $a_0$ Value | $S/(A/\ell_P^2)$ (Catalan $\ln 2$) | Rel. Diff vs $1/4$ (Cat) | $S/(A/\ell_P^2)$ ($TL$ $\ln[2]_{q_0}$) | Rel. Diff vs $1/4$ ($TL$) |
|---|---|---:|---:|---:|---:|---:|
| `Q1_unit_circuit_cell` | $1$ | `1.0000000000` | `0.6931471806` | `+177.26%` | `0.6985808249` | `+179.43%` |
| `Q2a_horiz_step_sq` | $q_0^{-2}$ | `0.8116537544` | `0.8539936849` | `+241.60%` | `0.8606882198` | `+244.28%` |
| `Q2b_newton_cell_ratio` | $\hbar_{q_0}^2 / S_{\mathrm{cell}}(q_0) = q_0$ | `1.1099785828` | `0.6244689685` | `+149.79%` | `0.6293642380` | `+151.75%` |
| `Q3_dirac_share_ashtekar` | $8\pi \hbar_{q_0}\sqrt{[1/2]_{q_0}[3/2]_{q_0}}$ | `2.1575485233` | `0.3212660912` | `+28.51%` | `0.3237845255` | `+29.51%` |
| `Q4_contact_anisotropy` | $8\pi (q_0 - 1)\sqrt{[1/2]_{q_0}[3/2]_{q_0}}$ | `2.3948326521` | `0.2894344955` | `+15.77%` | `0.2917033991` | `+16.68%` |
| `Q5a_meridian_disk_pi` | $\pi$ | `3.1415926536` | `0.2206356002` | `-11.75%` | `0.2223651829` | `-11.05%` |
| `Q5b_hemisphere_2pi` | $2\pi$ | `6.2831853072` | `0.1103178001` | `-55.87%` | `0.1111825914` | `-55.53%` |
| `Q5c_two_sphere_4pi` | $4\pi$ | `12.5663706144` | `0.0551589000` | `-77.94%` | `0.0555912957` | `-77.76%` |
| **`Q6_LCQ_null_focusing`** | **Conditional on `LCQHorizonPunctureAreaConjecture`** | **`4 s_{\mathrm{punct}}$** | **`0.2500000000`** | **`0` (`< 1e-76`)** | **`0.2500000000`** | **`0` (`< 1e-76`)** |

---

## 4. Open Blocker Isolated for Future Derivation (`Rule 13a`)

- **Open Conjecture Carrier:** `QOU.GravitySpacetime.ReebLengthTimeAndLightConeEntropy.LCQHorizonPunctureAreaConjecture` (zero instances).
- **What is needed to discharge it:** Construct the explicit Lorentzian metric lift of QOU's twisting contact CR 3-manifold (`cr-structure-lorentzian-lift.md`) and prove from the $q$-Yang–Mills–Levi action that (i) Rindler/null horizon cuts carry the Bisognano–Wichmann modular boost period $2\pi/\hbar_q$ and (ii) null-generator expansion obeys Raychaudhuri focusing with Einstein normalization $8\pi G_q / c_q^3$. Until that Lorentzian CR bridge is derived, `qou-slfm` remains `in-progress` per Rule 13a.
