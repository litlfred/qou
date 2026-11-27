# Pre-Registration: W6 Inhomogeneous Lepton Loop Resolvent, `+211.206 ppb` `μ–p` Offset & `m_τ / m_e` Check

Beans: `qou-91w7`, `qou-6gf9`, `qou-mk7u` (`Q-Gap-2` / W6).
Lean companion: `folio/quantum-observable-universe/lean/QOU/Observations/InhomogeneousLeptonLoopResolvent.lean`.
Committed **prior** to writing or executing `w6_inhomogeneous_lepton_resolvent_probe.py`.

## 1. Fixed Derived & CAL-1/2/3 Inputs (`workdps = 80`, `q0Anchor = "proton"`, Zero Tuned Parameters)

- **Substrate anchor:** Proton-pinned `q₀ = q_at(80)` (`Q_MP`), `ℏ_q = 1 - q₀⁻¹`, `h₀ = q₀ - q₀⁻¹`,
  and bar-even meridian coordinate `w₀ = q₀ + q₀⁻¹ - 2 = q₀ ℏ_q²`.
  (Muon-pinned `q_μ = q_muon_at(80)` is recorded strictly as a labelled E1 comparison arm; `q₀` is
  held fixed throughout per permanent owner gate `qou-eic1`.)
- **Derived electromagnetic coupling (Form B, zero CODATA `α`):**
  `α_q(q₀) = (q₀ [9]_{q₀} [10]_{q₀} + 2 / (3 π))⁻¹`.
- **Exact geometric volumes (zero free parameters):**
  - Toroidal Hopf link (`β_e = σ₀ σ₁ σ₀`) and torus knot `T(2,7)`: `Vol(Hopf) = Vol(T(2,7)) = 0`.
  - Figure-eight knot `4₁` (`β_μ = (σ₀ σ₁⁻¹)²`): `Vol(4₁) = 2 Cl₂(π/3)`.
  - Three-twist knot `5₂`: `Vol(5₂) = 3 D(z_{5₂})`, where `z_{5₂}` is the unique root with `Im(z) > 0`
    of `z³ - z² + 1 = 0` and `D(z) = Im Li₂(z) + arg(1 - z) ln|z|` is the Bloch–Wigner dilogarithm.
- **Comparison-only NIST CODATA-2022 constants (parsed from `value_str`, never entering formulas):**
  - `muon-electron mass ratio` (`206.7682827`, experimental `σ = 4.6e-6`, `22.2 ppb`).
  - `tau-electron mass ratio` (`3477.23`, experimental `σ = 0.23`, `66.1 ppm`).

## 2. Pre-Registered Structural Verification Checks (Matching Lean Theorems)

1. Verify `fig8_21_trace` (`χ_{(2,1)}((σ₀ σ₁⁻¹)²) = h₀⁴ + 2 h₀² - 1`), `tauFigureEight_closed_form`
   (`τ_{4₁}(q₀) = (h₀⁴ + 3 h₀² + 1) / (q₀ + q₀⁻¹)²`), `tauFigureEight_bar`, `unit_ratio_gt_six`
   (`R(q₀) = τ_e(q₀) / ℏ_q² = 70.403723... > 6`), and `half_div_tauElectron_lt_one`
   (`(1/2) / τ_e(q₀) = 0.723414... < 1`).
2. Compare the inhomogeneous loop resolvent `W(X; q₀) = W_alg(X; q₀) + ℏ_q⁻² Vol(X)(1 + c_tors ℏ_q + c₂ ℏ_q²)`
   under:
   - Unnormalized trace `W_alg = τ_X` with constant `c = 1/2` (`QVolumeCarrier` baseline), vs
   - Symmetric-channel electron-normalized `Ŵ_alg(X; q) = τ_X(q) / τ_e(q)` (`Ŵ_alg(Hopf; q) = 1`,
     `carrier_ratio_of_electron_unit_alg`).

## 3. Pre-Registered Zero-Parameter Hypotheses for the `+211.206 ppb` `m_μ / m_e` Offset

At `q₀`, the bare volume carrier `R₀ = Vol(4₁) / ℏ_q²` sits above CODATA `m_μ / m_e` by `+211.206 ppb`
(`+4.367 × 10⁻⁵` absolute), requiring a negative fractional shift `δ_req ≈ -2.11206 × 10⁻⁷`. All sub-arms
below are evaluated with **zero fitted coefficients** and reported side-by-side:

### (H1) Kashaev–Andersen–Hansen / Dimofte–Gukov / Murakami Real-`q` Asymptotic Series (`qou-mk7u`)
- **H1.a (Root-of-unity Kashaev–Ohtsuki at `N_eff = 2π / ℏ_q²`):** 1-loop prefactor
  `3/2 ln N_eff - (1/4) ln 3` plus Ohtsuki rungs `κ₁ / N_eff + κ₂ / N_eff² + κ₃ / N_eff³`
  (`κ₁ = 11√3 π / 108`, `κ₂ = 2π² / 27`, `κ₃ = 1081√3 π³ / 21870`).
- **H1.b (Real-`ℏ_q` multiplicative 1-loop torsion / Ohtsuki series):** test `S₁(4₁) = -(1/4) ln 3`
  and `κ₁ = 11√3 π / 108` multiplied by `ℏ_q` and `ℏ_q²` (`c_tors ℏ_q`, `c₂ ℏ_q²`).
- **H1.c (Murakami 2011 `[murakami-h2011]` Thm. 1.3 real deformation at `u₀ = ln q₀`, `ξ₀ = 2π i + u₀`):**
  evaluate `φ(u₀) = i arccos(cosh u₀ - 1/2)`, `S(u₀) = Li₂(e^{u₀ - φ(u₀)}) - Li₂(e^{u₀ + φ(u₀)}) - u₀ φ(u₀)`,
  `Δ_{4₁}(q₀) = (w₀ + 3)(w₀ - 1)`, Riley longitude norm `|ℓ(q₀)|² = 1`, deformed exponential rate
  `2π Re(S(u₀) / ξ₀) / Vol(4₁) - 1`, and twisted Reidemeister torsion shift `|T(u₀)|² / (4/3) - 1`.

### (H2) Two-Term Electromagnetic Radiative Self-Energy Difference (`Hopf` vs `4₁` at Form-B `α_q(q₀)`)
- **H2.a (Universal 1-loop Schwinger factor `α_q / (2π)`):** cancels identically (`0 ppb`) in
  `m_μ / m_e` (`universal_qed_self_energy_cancels`); contrast with shared-UV-cutoff pole-mass log
  `-(3 α_q / (2π)) ln(Vol(4₁) / ℏ_q²)`.
- **H2.b (Pure multi-loop QED scales):** `-(α_q / π)²` and `-(α_q / π)³`.
- **H2.c (Mixed QED × Hecke crossing-defect graph scales, zero tuned prefactors):**
  - `-α_q² h₀²` (two-photon × quadratic Hecke defect),
  - `-α_q h₀⁴ / (4π)` (1-loop radiative × 4-crossing quartic `(2,1)` Hecke defect `h₀⁴` on `4₁`,
    absent on `Hopf`),
  - `-α_q w₀² / (2π)` (1-loop radiative × bar-even `w₀²` defect),
  - `(α_q / (2π)) · y_{(2,1)}(q₀) · χ_{(2,1)}((σ₀ σ₁⁻¹)²)` and
    `(α_q / (2π))² · (χ_{(2,1)}((σ₀ σ₁⁻¹)²) / τ_{4₁}(q₀))` (exact `(2,1)`-channel asymmetry vs `0` on `Hopf`).
- **Entropy discipline (`qou-6gf9`):** `δ_req` carries `~0.98` significant digits (`22.2 ppb` 1σ = `10.5%`
  of `211.2 ppb`), so any numerical proximity in H2.c without a prior categorical-Lagrangian graph
  derivation of the exact rational prefactor is classified strictly as an **open candidate scale
  (not a closed derivation)**.

### (H3) Satellite `T(2,7) ⋈ 4₁` and Hyperbolic `5₂` Resolvent Check for `m_τ / m_e`
- **H3.a (`T(2,7) ⋈ 4₁` additive simplicial volume at `ℏ_q⁻²`):** `Vol(T(2,7)) + Vol(4₁) = Vol(4₁)`
  gives `Vol(4₁) / ℏ_q²` (`+ τ_{T(2,7)}(q₀) / τ_e(q₀)` regular contact shift).
- **H3.b (`T(2,7) ⋈ 4₁` cable-winding `2² = 4` vs generation-step `ℏ_q⁻³`):** `4 Vol(4₁) / ℏ_q²` and
  `Vol(4₁) / ℏ_q³`.
- **H3.c (Three-twist knot `5₂`):** `Vol(5₂) / ℏ_q²`, `Vol(5₂) / ℏ_q³`, and `q`-volume `3 Im G(z_{5₂}; q₀)`.
