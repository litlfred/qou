# Pre-Registration: W10 Continuum `E_cat` Subdivision, Proton `(k = -3, 2, 12)` Schur Test & Intra-Nucleon Borromean EM `m_d - m_u` (`L_cal` Route 1)

Beans: `qou-mjo7` (`W10`), `qou-pzsi`, `qou-37y0`, `qou-17mq`, `qou-zp6a`, `qou-awxv` (item 1), `qou-99qc`.
Lean companion: `folio/quantum-observable-universe/lean/QOU/QBeta/ContinuumECatIntraNucleonEM.lean`.
Committed **prior** to writing or executing `w10_continuum_ecat_intranuc_em_probe.py`.

---

## 1. Fixed Derived & Calibration Inputs (`workdps = 80`, `q0Anchor = "proton"`, Zero Tuned Parameters)

- **Substrate anchor:** Proton-pinned `q₀ = q_at(80)` (`Q_MP`), `ℏ_q = 1 - q₀⁻¹`, `h₀ = q₀ - q₀⁻¹`,
  and independent muon-pinned cross-check `q_μ = q_muon_at(80)` (pure CAL-1 + CAL-2, zero `m_p` input).
- **Derived electromagnetic coupling (Form B, zero CODATA `α`):**
  `α_q(q₀) = (q₀ [9]_{q₀} [10]_{q₀} + 2 / (3 π))⁻¹`.
- **Self-consistent nucleon model mass (zero `m_π` unit):**
  `m_model(q) = m_e · (2 · (Vol(4₁) / ℏ_q²) · F_Bor(q) - 12)`,
  where `Vol(4₁) = 2 Cl₂(π/3)`, `F_Bor(q) = tr_M(β_Bor, q) · [3]_q! / q³`, and
  `tr_M(β_Bor, q) = (4 + h² - 3 h⁴ - h⁶) / (h² + 4)`.
- **Exact Borromean `6₃³` (`L6a4`) hyperbolic volume (zero free parameters):**
  `Vol(S³ \ B₃) = 8 G = 2 Vol(ideal octahedron)`, where `G = Cl₂(π/2)` is Catalan's constant;
  volume-equivalent `H³` geodesic ball radius `R_{B₃}` solves `π (sinh(2 R_{B₃}) - 2 R_{B₃}) = 8 G`,
  fixing the zero-mean O2 Robin constant `c₀(B₃) = sinh²(R_{B₃}) / (sinh(R_{B₃}) cosh(R_{B₃}) - R_{B₃})`.
- **Comparison-only external benchmarks (never entering model formulas):**
  - NIST CODATA-2022 `proton-electron mass ratio`, `neutron-proton mass difference energy equivalent in MeV` (`1.29333236(46) MeV`), and `proton rms charge radius` (`0.84075(64) fm`, strictly labelled `[COMPARISON-ONLY]`).
  - Dispersive Cottingham / lattice QCD+QED intra-nucleon EM splitting benchmarks:
    Gasser–Leutwyler / Cottingham `0.76(30) MeV` (`0.76–1.04 MeV` modern dispersive/lattice band),
    Borsanyi et al. (BMW 2015) `ΔE_EM(p - n) = 1.00(16) MeV`, and PDG `m_d - m_u` (`MS-bar, 2 GeV`) `= 2.52(17) MeV`.
    In dimensionless Route-1 units `f_emp = ΔE_EM / (α_q(q₀) · m_model(q₀))`:
    `f_emp(Cottingham 0.76 MeV) ≈ 0.1110`, `f_emp(BMW 1.00 MeV) ≈ 0.1460` (the `~0.1` target of `qou-awxv` item 1).

---

## 2. Pre-Registered Part A: Discrete-to-Continuum `E_cat` Subdivision Convergence (`qou-pzsi`)

Across `N ∈ {16, 32, 64, 128, 256}` at `workdps = 80`:
1. **Non-periodic braid-segment regulated kernel on `[0, 1]²`:**
   `K_δ(u, v) = ((u - v)² + δ²)⁻¹` at `δ = ℏ_q(q₀)` and `δ = 1/2`, compared against the exact closed-form integral
   `I(δ) = (2 / δ) arctan(1 / δ) - ln(1 + 1 / δ²)`.
   Verify:
   - Exact Lean Lipschitz Riemann bound `|S_N(δ) - I(δ)| ≤ 2 / (δ³ N)` and dyadic Cauchy step `|S_N(δ) - S_{2N}(δ)| ≤ 1 / (2 δ³ N)` at every `N`;
   - Midpoint + Richardson extrapolation over `N ∈ {16, 32, 64, 128, 256}` converging to `< 10⁻¹²` against `I(δ)`.
2. **Periodic `S¹ × S¹` chordal regulated sum & Bring cusp-torus O'Hara continuum bridge:**
   `S_N^per(δ) = (1 / N²) ∑_{i,j=0}^{N-1} (4 sin²(π(i-j)/N) + δ²)⁻¹` against the exact residue closed form
   `I^per(δ) = 1 / (δ √(δ² + 4))`, verifying convergence `< 10⁻²⁰` by `N = 256`, together with the `S₃`
   Wedderburn block split `E_cat^y = y_{(3)} E_{(3)} + y_{(2,1)} E_{(2,1)} + y_{(1³)} E_{(1³)}` (`y_{(3)} + 2 y_{(2,1)} + y_{(1³)} = 1` under Molien weights; `y_{(1³)}^D = 0` under Convention D).

---

## 3. Pre-Registered Part B: Extremal-Functional & Schur Test of Proton `(k₁ = -3, k₂ = 2, k₃ = 12)` (`qou-mjo7`)

1. Verify at 80 dps the `H₃(q²)` Schur identities proved in Lean:
   `c_{(3)}(q²) = q³ [3]_q!`, `c_{(2,1)}(q²) = [3]_q`, `c_{(1³)}(q²) = q⁻³ [3]_q!`,
   transpose duality `c_{λ*}(q²) = c_λ(q⁻²)`, Molien sum `1/c_{(3)} + 2/c_{(2,1)} + 1/c_{(1³)} = 1`,
   and classical values `c_{(3)}(1) = c_{(1³)}(1) = 6 = dim H₃`, `dim S^{(2,1)} · c_{(1³)}(1) = 2 · 6 = 12`.
2. **Non-circular muon-anchor integer scan (`q_μ`, zero `m_p` input):**
   Evaluate `M(q_μ; k₁, k₂, k₃) = k₂ (Vol(4₁) / ℏ_{q_μ}²) tr_M(β_Bor, q_μ) q_μ^{k₁} [3]_{q_μ}! - k₃`
   over `k₁ ∈ {-3, -2, -1, 0, 1, 3}`, `k₂ ∈ {1, 2, 3}`, `k₃ ∈ {0, 6, 12, 18}` against CODATA `m_p / m_e`,
   recording honestly that `(k₁, k₂, k₃) = (-3, 2, 12)` is uniquely singled out algebraically by
   `(c_{(1³)}, dim S^{(2,1)}, dim S^{(2,1)} · c_{(1³)}(1))` and hits `-244.4 ppb` at `q_μ`, while the linear
   assembly subtraction itself remains conditional (`ProtonBorromeanAssembly`).

---

## 4. Pre-Registered Part C: Charge-Unit `L_cal` Route 1 (`qou-awxv` Item 1 + `qou-37y0`) — Self-Consistent `Δ_EM = α · m_model · f` (NO `m_π` Unit!)

From the Lean-proved quark-charge identities on `B₃` (`μ̄₁₂₃² = 1`):
- Pairwise product sum: `∑_{i<j} Q_i Q_j(p) = 0`, `∑_{i<j} Q_i Q_j(n) = -1/3`, so `Δ_pair(p - n) = +1/3`.
- Self-charge sum: `∑_i Q_i²(p) = 1`, `∑_i Q_i²(n) = 2/3`, so `(1/2) Δ_self(p - n) = +1/6` and
  coherent equal-kernel `(1/2) Δ_self + Δ_pair = (1/2)(Q_p² - Q_n²) = +1/2`.

### Primary Pre-Registered Route-1 Dimensionless Shape Factors `f` (`Δ_EM = α_q(q₀) · m_model(q₀) · f`, ZERO `m_π`, ZERO Fits)

All ten dimensionless candidates from pure 3-strand `H₃(q₀)` algebra and Borromean `6₃³` (`L6a4`) hyperbolic geometry are pre-registered prior to numerical evaluation and will be reported in full (including misses):

1. **`f_R1_1a` (3-strand equal-partition constituent Compton baseline, pairwise `+1/3`):**
   `f = (1/3) · (1/3) = 1/9 = 0.111111...`
2. **`f_R1_1b` (`q`-deformed `(2,1)` Schur `[3]_{q₀}` constituent Compton, pairwise `+1/3`):**
   `f = 1 / (3 · [3]_{q₀}) = 1 / (3 (q₀² + 1 + q₀⁻²))`
3. **`f_R1_1c` (3-strand constituent Compton with coherent `(1s)³` self+pair `+1/2`):**
   `f = (1/2) · (1/3) = 1/6 = 0.166666...`
4. **`f_R1_2a` (O2-neutralized `H³` Green's kernel on `S³ \ B₃` at intrinsic half-ball separation `α = R_{B₃}/2` in constituent `3 / m_model` units, pairwise `+1/3`):**
   `f = (1/9) · (coth(R_{B₃} / 2) - c₀(B₃))`
5. **`f_R1_2b` (Inverse Borromean hyperbolic volume `1 / Vol(B₃) = 1 / (8 G)`, pairwise `+1/3`):**
   `f = 1 / (3 · 8 G) = 1 / (24 G)`
6. **`f_R1_2c` (Carrier-to-baryon hyperbolic volume ratio `Vol(4₁) / Vol(B₃)`, pairwise `+1/3`):**
   `f = (1/3) · (Vol(4₁) / (8 G))`
7. **`f_R1_3a` (Self-consistent Compton-HO inverse length `√(E_osc / m_model)` with `E_osc = m_e / (q₀ - 1)²` — `m_e` and `m_π` free — bare pairwise `+1/3`):**
   `f = (1/3) · √(E_osc(q₀) / m_model(q₀)) = 1 / (3 q₀ √(2 Vol(4₁) F_Bor(q₀) - 12 ℏ_q²))`
8. **`f_R1_3b` (Self-consistent `(1s)²` spherical HO Slater Coulomb integral `√(2/π) √(E_osc / m_model)`, pairwise `+1/3`):**
   `f = (1/3) · √(2 / π) · √(E_osc(q₀) / m_model(q₀))`
9. **`f_R1_3c` (Self-consistent `(1s)³` spherical HO Slater coherent self+pair `(1/2) √(2/π) √(E_osc / m_model)`):**
   `f = (1/2) · √(2 / π) · √(E_osc(q₀) / m_model(q₀))`
10. **`f_R1_3d` & `f_R1_3e` (Pure Hecke / Planck-defect suppression tests — expected small misses):**
    - `f_R1_3d = |tr_conn(p, V³)| = 2 (q₀ - 1)⁴ (q₀ + 1)⁴ (q₀⁴ + q₀² + 1) / (27 q₀⁶)` (`O(ℏ_q⁴)` connected 3-strand Borromean trace),
    - `f_R1_3e = ℏ_q / 3 = (1 - q₀⁻¹) / 3` (`O(ℏ_q)` Planck defect, vanishes at `q = 1`).

### Secondary Pre-Registered Diagnostic Scales (Explicitly Separated from Route 1)

- **D1 (`[SECONDARY: uses CAL-3 m_π]`):** Bare pion Compton `(1/3) α_q(q₀) m_π` and O2-neutralized `H³` Green's function `(1/3) α_q(q₀) m_π (coth(α) - c₀(B₃))` at both NZ meridian branches `α = 2 ln q₀` and `α = ln q₀` (`qou-pzsi`, `qou-17mq`, `qou-zp6a`).
- **D2 (`[COMPARISON-ONLY: uses CODATA r_p]`):** Uniform-sphere Born scale `(3/5) α_q(q₀) ℏc / (√(5/3) r_p)` and pairwise `(1/3) α_q(q₀) ℏc / r_p`.

For every primary Route-1 and secondary row, we extract the implied strong scheme difference
`(m_d - m_u)_scheme = (m_n - m_p)_exp + Δ_EM(p - n)` and report all values without post-hoc selection.
