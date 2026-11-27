/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import QOU.Observations.ElectronUnitSplit
import QOU.Observations.FiniteJetNormPoleOrder

/-!
# Inhomogeneous Lepton Loop Resolvent, `4₁` Reidemeister Torsion, and Differential QED Shift

Workstream W6 / `Q-Gap-2` (beans `qou-91w7`, `qou-6gf9`, `qou-mk7u`). Formalizes the structural
resolution of the `R = τ_e / ℏ_q²` homogeneous carrier obstruction (`ElectronUnitSplit`,
`FiniteJetNormPoleOrder`, `QVolumeCarrier`) together with exact algebraic tests of the `4₁`
1-loop Reidemeister torsion (`[murakami-h2011]`) and two-term differential radiative shifts.

Every declaration in this module is stated over a generic `[Field K]` or ordered field
`[Field K] [LinearOrder K] [IsStrictOrderedRing K]` (§7c: zero `ℝ`, zero empirical literals,
zero `sorry`, zero custom axioms).

## Main Results

1. **Homogeneous Pure-Trace Obstruction (`unit_ratio_gt_six`, `unit_ratio_ne_one`,
   `fig8_21_trace`, `tauFigureEight_closed_form`, `homogeneous_trace_ratio_at_one`):**
   - For the 3-strand figure-eight muon braid `β_μ = (σ₀ σ₁⁻¹)²`, the `(2,1)` character is
     `(q - q⁻¹)⁴ + 2(q - q⁻¹)² - 1` (contrasting with `0` on the Hopf electron `σ₀ σ₁ σ₀`),
     giving the exact bar-invariant closed form
     `τ_{4₁}(q) = ((q - q⁻¹)⁴ + 3(q - q⁻¹)² + 1) / (q + q⁻¹)²` with `τ_{4₁}(1) / τ_e(1) = 1/2`
     (pole order `0`).
   - Over any ordered field, `τ_e(q) / ℏ_q² > 6` (hence `τ_e(q) / ℏ_q² ≠ 1`) for **every** `q > 1`,
     and over any field `τ_e(q) / ℏ_q² = 1` forces the monic degree-9 polynomial identity
     `q⁵(q⁴ + 1) - (q - 1)²(q² + 1)² = 0`.

2. **Inhomogeneous Borel-Resummed Loop Resolvent (`InhomogeneousLoopResolvent`):**
   Decomposes `W(X; q) = W_alg(X; q) + ℏ_q⁻² Vol(X) · (1 + c_tors(X) ℏ_q + c₂(X) ℏ_q²)` into:
   - **Toroidal / Zero-Volume Contact Branch (`singPart_eq_zero_of_vol_zero`,
     `eval_eq_wAlg_of_vol_zero`):** when `Vol(e) = 0` (Hopf link or torus link `T(a,b)`), the
     singular saddle cut vanishes identically and `W(e; q) = W_alg(e; q)`.
   - **Hyperbolic / Saddle-Cut Branch (`hbar_sq_mul_eval_sub_vol`, `carrier_ratio_decomp`,
     `carrier_ratio_of_electron_unit_alg`):** when `Vol(μ) ≠ 0`, `ℏ_q² W(μ; q) - Vol(μ)` factors
     explicitly through `ℏ_q`, and normalizing `W_alg` on the `(3)` symmetric electron channel
     (`W_alg(e; q) = 1`, i.e. `Ŵ_alg(X; q) = τ_X(q) / τ_e(q)`) yields leading pole `Vol(μ) / ℏ_q²`
     without `QVolumeCarrier`'s constant-`c` scale drift (`half_div_tauElectron_lt_one`).

3. **Exact `4₁` Riley–Murakami Reidemeister Torsion & Cone Window (`reidemeisterDisc41_eq_wCoord`,
   `riley_longitude_unit_norm_identity`, `reidemeisterTorsionAbsSq_excess_pos`):**
   In terms of the bar-even coordinate `w(m) = m + m⁻¹ - 2 = m ℏ_m²`:
   - `(m + m⁻¹ + 1)(m + m⁻¹ - 3) = (w + 3)(w - 1) = w² + 2w - 3`, taking `-3` at `m = 1`
     (`T_Reid²(1) = -4/3`, untwisted inverse norm `3 = (√3)²`).
   - Riley's longitude eigenvalue satisfies `((m² - m - 2 - m⁻¹ + m⁻²)² - (m - m⁻¹)² Δ_{4₁}(m)) / 4 = 1`
     identically over every field (`char K ≠ 2`), placing `ℓ(m)` on the unit circle across the cone
     window `0 < w(m) < 1` (which covers all `1 < m ≤ 3/2`).
   - Across `0 < w(m) < 1`, the squared torsion magnitude `4 / (-Δ_{4₁}(m))` strictly exceeds its
     `m = 1` value `4/3` (`sign > 0`, opposite to a negative carrier correction).

4. **Two-Term Differential QED Shift & Satellite Additivity (`universal_qed_self_energy_cancels`,
   `differential_two_term_ratio_shift`, `differential_shift_neg_iff`,
   `satellite_torus_volume_eq_companion`):**
   Universal multiplicative self-energy cancels identically in `m_μ / m_e`; a topological two-term
   self-energy `m_ℓ = m_ℓ⁽⁰⁾(1 + ε Σ_ℓ)` shifts `m_μ / m_e` negatively iff `Σ_μ < Σ_e` (mirrored by
   the negative `(2,1)`-channel trace on `4₁` vs `0` on `Hopf`); and zero-volume torus patterns
   contribute zero simplicial volume under additive satellite gluing.

-- Ref: [leitner2026] beans qou-91w7, qou-6gf9, qou-mk7u
-- Ref: [murakami-h2011] H. Murakami, arXiv:1102.3530, Thm. 1.2–1.3 & §4.1–4.2
-- Ref: [andersen-hansen2006] J. E. Andersen, S. K. Hansen, J. Knot Theory Ramifications 15 (2006)
-- Ref: [habiro2004cyclotomic] K. Habiro, Invent. Math. 171 (2008) / RIMS 2004
-- Ref: [ohtsuki2002] T. Ohtsuki, Quantum Invariants, World Scientific 2002
-- Ref: [kashaev1997] R. M. Kashaev, Lett. Math. Phys. 39 (1997) 269–275
-- Ref: [thurston1978] W. P. Thurston, Geometry and Topology of Three-Manifolds, Ch. 6
-/

namespace QOU.Observations.InhomogeneousLeptonLoopResolvent

open Matrix
open QOU.QBeta.WeightSpaceMarkov
open QOU.QBeta.E0WeightCandidates
open QOU.Observations.ElectronUnitSplit
open QOU.Observations.FiniteJetNormPoleOrder

/-! ## Section 1: Pure-Trace Homogeneous Obstruction & `H₃(q)` Figure-Eight Closed Form -/

section HomogeneousObstruction

variable {K : Type*} [Field K]

/-- Convention-D trace `τ_e(q) = τ_D(σ₀ σ₁ σ₀)` of the 3-strand Hopf electron braid. -/
def tauElectron (q : K) : K :=
  tauD3 q (q ^ 3) (r21a q * r21b q * r21a q)

/-- The `(2,1)` representation matrix `(ρ(σ₀) ρ(σ₁⁻¹))²` of the figure-eight braid `(σ₀ σ₁⁻¹)²`. -/
def fig8Mat21 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  (r21a q * inv21 q (r21b q)) ^ 2

/-- Convention-D trace `τ_{4₁}(q) = τ_D((σ₀ σ₁⁻¹)²)` of the 3-strand figure-eight braid
(writhe `0`, so the `(3)` character is `1`). -/
def tauFigureEight (q : K) : K :=
  tauD3 q 1 (fig8Mat21 q)

/-- Exact `(2,1)` character of `(σ₀ σ₁⁻¹)²`: `(q - q⁻¹)⁴ + 2(q - q⁻¹)² - 1`, non-vanishing at
`q = 1` (`-1`), in contrast to `electron_21_trace_zero` (`0` on `σ₀ σ₁ σ₀`). -/
theorem fig8_21_trace (q : K) (hq : q ≠ 0) :
    (fig8Mat21 q).trace = (q - q⁻¹) ^ 4 + 2 * (q - q⁻¹) ^ 2 - 1 := by
  unfold fig8Mat21
  rw [inv21_r21b, sq]
  simp [r21a, Matrix.trace_fin_two]
  field_simp
  ring

/-- Exact closed form `τ_{4₁}(q) = ((q - q⁻¹)⁴ + 3(q - q⁻¹)² + 1) / (q + q⁻¹)²`. -/
theorem tauFigureEight_closed_form (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    tauFigureEight q = ((q - q⁻¹) ^ 4 + 3 * (q - q⁻¹) ^ 2 + 1) / (q + q⁻¹) ^ 2 := by
  have hs : q + q⁻¹ ≠ 0 := by
    intro h; apply hq2; field_simp at h; linear_combination h
  unfold tauFigureEight tauD3 y3 y21
  rw [fig8_21_trace q hq]
  field_simp
  ring

/-- **Amphichiral bar-invariance of `τ_{4₁}(q)`:** `τ_{4₁}(q⁻¹) = τ_{4₁}(q)`. -/
theorem tauFigureEight_bar (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    tauFigureEight q⁻¹ = tauFigureEight q := by
  have hqi : q⁻¹ ≠ 0 := inv_ne_zero hq
  have hqi2 : (q⁻¹) ^ 2 + 1 ≠ 0 := by
    intro h; apply hq2; field_simp at h; linear_combination h
  rw [tauFigureEight_closed_form q⁻¹ hqi hqi2, tauFigureEight_closed_form q hq hq2, inv_inv]
  ring

/-- Classical `q = 1` value of the Hopf electron trace: `τ_e(1) = 1/2`. -/
theorem tauElectron_at_one (h2 : (2 : K) ≠ 0) :
    tauElectron (1 : K) = 1 / 2 := by
  have h12 : (1 : K) ^ 2 + 1 ≠ 0 := by norm_num; exact h2
  unfold tauElectron
  rw [tau_electron 1 one_ne_zero h12]
  have he : (1 : K) ^ 3 * (1 ^ 4 + 1) / (1 ^ 2 + 1) ^ 2 = 2 / (2 * 2) := by norm_num
  rw [he]
  field_simp

/-- Classical `q = 1` value of the figure-eight trace: `τ_{4₁}(1) = 1/4`. -/
theorem tauFigureEight_at_one (h2 : (2 : K) ≠ 0) :
    tauFigureEight (1 : K) = 1 / 4 := by
  have h12 : (1 : K) ^ 2 + 1 ≠ 0 := by norm_num; exact h2
  rw [tauFigureEight_closed_form 1 one_ne_zero h12]
  norm_num

/-- **Pole-order-zero homogeneous trace ratio at `q = 1`:** `τ_{4₁}(1) / τ_e(1) = 1/2`, matching
`FiniteJetNormPoleOrder.no_laurent_trace_ratio_pole_at_one`. -/
theorem homogeneous_trace_ratio_at_one (h2 : (2 : K) ≠ 0) :
    tauFigureEight (1 : K) / tauElectron (1 : K) = 1 / 2 := by
  rw [tauFigureEight_at_one h2, tauElectron_at_one h2]
  have h4 : (4 : K) ≠ 0 := by
    have e : (4 : K) = 2 * 2 := by norm_num
    rw [e]; exact mul_ne_zero h2 h2
  field_simp
  ring

/-- **Generic-field polynomial obstruction to `R(q) = τ_e(q) / ℏ_q² = 1`:**
equality at `q ∉ {0, 1}` with `q² + 1 ≠ 0` forces `q⁵(q⁴ + 1) - (q - 1)²(q² + 1)² = 0`. -/
theorem unit_ratio_eq_one_poly_obstruction (q : K) (hq : q ≠ 0) (hq1 : q ≠ 1)
    (hq2 : q ^ 2 + 1 ≠ 0) (heq : tauElectron q / hbar q ^ 2 = 1) :
    q ^ 5 * (q ^ 4 + 1) - (q - 1) ^ 2 * (q ^ 2 + 1) ^ 2 = 0 := by
  have hh : hbar q ≠ 0 := hbar_ne_zero q hq1
  unfold tauElectron at heq
  rw [tau_electron q hq hq2] at heq
  unfold hbar at heq
  have hsub : 1 - q⁻¹ = (q - 1) / q := by field_simp
  rw [hsub] at heq
  have hq1' : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  field_simp at heq
  linear_combination heq

end HomogeneousObstruction

section OrderedHomogeneousObstruction

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Universal lower bound on the electron unit ratio (`q > 1`):** for **every** `q > 1` in any
ordered field, `6 < τ_e(q) / ℏ_q²`. -/
theorem unit_ratio_gt_six {q : K} (hq : 1 < q) :
    6 < tauElectron q / hbar q ^ 2 := by
  have hq0 : 0 < q := by linarith
  have hsub : 0 < q - 1 := sub_pos.mpr hq
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  unfold tauElectron
  rw [unit_ratio_split q hq0.ne' hq.ne' hq2 two_ne_zero]
  have hterm2 : 0 < q ^ 5 * (q + 1) ^ 2 / (2 * (q ^ 2 + 1) ^ 2) := by positivity
  have hterm1_eq : q ^ 3 / (2 * hbar q ^ 2) = q ^ 5 / (2 * (q - 1) ^ 2) := by
    unfold hbar
    have he : 1 - q⁻¹ = (q - 1) / q := by field_simp
    rw [he]
    field_simp
  rw [hterm1_eq]
  have hden : 0 < 2 * (q - 1) ^ 2 := by positivity
  have hterm1 : 6 < q ^ 5 / (2 * (q - 1) ^ 2) := by
    rw [lt_div_iff₀ hden]
    have hdiff : q ^ 5 - 6 * (2 * (q - 1) ^ 2) =
        1 + (q - 1) * (4 + (q - 2) ^ 2 + 9 * (q - 1) ^ 2) + 5 * (q - 1) ^ 4 + (q - 1) ^ 5 := by
      ring
    have hpos : 0 < q ^ 5 - 6 * (2 * (q - 1) ^ 2) := by
      rw [hdiff]
      positivity
    linarith
  linarith

/-- **Universal homogeneous obstruction (`R(q) ≠ 1`):** `τ_e(q) / ℏ_q² ≠ 1` for every `q > 1`. -/
theorem unit_ratio_ne_one {q : K} (hq : 1 < q) :
    tauElectron q / hbar q ^ 2 ≠ 1 := by
  have h6 := unit_ratio_gt_six hq
  linarith

/-- Strict positivity of `τ_{4₁}(q)` across all `q ≠ 0` in any ordered field. -/
theorem tauFigureEight_pos {q : K} (hq : q ≠ 0) :
    0 < tauFigureEight q := by
  have hq2_pos : 0 < q ^ 2 + 1 := by
    have : 0 ≤ q ^ 2 := sq_nonneg q
    linarith
  rw [tauFigureEight_closed_form q hq hq2_pos.ne']
  have hnum : 0 < (q - q⁻¹) ^ 4 + 3 * (q - q⁻¹) ^ 2 + 1 := by positivity
  have hs : q + q⁻¹ ≠ 0 := by
    intro h; apply hq2_pos.ne'; field_simp at h; linear_combination h
  have hden : 0 < (q + q⁻¹) ^ 2 := sq_pos_of_ne_zero hs
  exact div_pos hnum hden

end OrderedHomogeneousObstruction

/-! ## Section 2: Inhomogeneous Habiro–Ohtsuki / Makeenko–Migdal Loop Resolvent -/

section InhomogeneousResolvent

variable {ι K : Type*} [Field K]

/-- **Inhomogeneous Borel-resummed loop resolvent**
`W(X; q) = W_alg(X; q) + ℏ_q⁻² Vol(X) · (1 + c_tors(X) ℏ_q + c₂(X) ℏ_q²)` separating:
* `wAlg`: the regular algebraic/contact branch `ℛ_X^reg(q)` (finite at `q = 1`), and
* `singPart`: the hyperbolic Borel saddle-cut branch `ℛ_X^sing(q)` proportional to `Vol(X)`. -/
structure InhomogeneousLoopResolvent (ι K : Type*) where
  /-- Regular rational/Habiro contact branch `W_alg(X; q)`. -/
  wAlg : ι → K → K
  /-- Simplicial / hyperbolic saddle volume `Vol(X)` (`0` on toroidal links). -/
  vol : ι → K
  /-- Subleading 1-loop Reidemeister-torsion / Stokes coefficient `c_tors(X)`. -/
  cTors : ι → K
  /-- Subleading 2-loop asymptotic coefficient `c₂(X)`. -/
  cTwo : ι → K

namespace InhomogeneousLoopResolvent

/-- Singular saddle-cut branch `ℛ_X^sing(q) = ℏ_q⁻² Vol(X) · (1 + c_tors(X) ℏ_q + c₂(X) ℏ_q²)`. -/
def singPart (R : InhomogeneousLoopResolvent ι K) (X : ι) (q : K) : K :=
  hbarInvSq q * R.vol X * (1 + R.cTors X * hbar q + R.cTwo X * hbar q ^ 2)

/-- Full inhomogeneous loop functional `W(X; q) = ℛ_X^reg(q) + ℛ_X^sing(q)`. -/
def eval (R : InhomogeneousLoopResolvent ι K) (X : ι) (q : K) : K :=
  R.wAlg X q + R.singPart X q

/-- **Toroidal / Zero-Volume Contact Branch (singular vanishing):** on any zero-volume knot or link
(`Vol(e) = 0`, including the Hopf link and torus links `T(a,b)`), `ℛ_e^sing(q) = 0` identically. -/
theorem singPart_eq_zero_of_vol_zero (R : InhomogeneousLoopResolvent ι K) {e : ι}
    (hve : R.vol e = 0) (q : K) :
    R.singPart e q = 0 := by
  unfold singPart
  rw [hve, mul_zero, zero_mul]

/-- **Toroidal / Zero-Volume Contact Branch (exact reduction):** when `Vol(e) = 0`, the resolvent
reduces identically to its regular algebraic branch `W(e; q) = W_alg(e; q)`. -/
theorem eval_eq_wAlg_of_vol_zero (R : InhomogeneousLoopResolvent ι K) {e : ι}
    (hve : R.vol e = 0) (q : K) :
    R.eval e q = R.wAlg e q := by
  unfold eval
  rw [R.singPart_eq_zero_of_vol_zero hve q, add_zero]

/-- **Hyperbolic / Saddle-Cut Branch (`O(ℏ_q)` asymptotic factorization):** for `q ≠ 1`,
`ℏ_q² W(X; q) - Vol(X) = ℏ_q · (Vol(X) c_tors(X) + ℏ_q (W_alg(X; q) + Vol(X) c₂(X)))`, proving
purely algebraically that `ℏ_q² W(X; q)` recovers `Vol(X)` up to an explicit `ℏ_q`-multiple. -/
theorem hbar_sq_mul_eval_sub_vol (R : InhomogeneousLoopResolvent ι K) (X : ι)
    {q : K} (hq1 : q ≠ 1) :
    hbar q ^ 2 * R.eval X q - R.vol X =
      hbar q * (R.vol X * R.cTors X + hbar q * (R.wAlg X q + R.vol X * R.cTwo X)) := by
  have hh : hbar q ≠ 0 := hbar_ne_zero q hq1
  have hh2 : hbar q ^ 2 ≠ 0 := pow_ne_zero 2 hh
  have hinv : hbarInvSq q = (hbar q ^ 2)⁻¹ := rfl
  unfold eval singPart
  rw [hinv]
  field_simp
  ring

/-- **Joint Lepton Ratio Decomposition:** when `Vol(e) = 0` and `W_alg(e; q) ≠ 0`,
`W(μ; q) / W(e; q)` splits into the regular ratio `W_alg(μ; q) / W_alg(e; q)` plus the
`W_alg(e; q)⁻¹`-weighted hyperbolic saddle cut. -/
theorem carrier_ratio_decomp (R : InhomogeneousLoopResolvent ι K) {e mu : ι} {q : K}
    (hve : R.vol e = 0) (hwe : R.wAlg e q ≠ 0) :
    R.eval mu q / R.eval e q =
      R.wAlg mu q / R.wAlg e q +
        (R.wAlg e q)⁻¹ * (hbarInvSq q * R.vol mu *
          (1 + R.cTors mu * hbar q + R.cTwo mu * hbar q ^ 2)) := by
  rw [R.eval_eq_wAlg_of_vol_zero hve q]
  unfold eval singPart
  field_simp

/-- **Symmetric-Channel / Electron-Normalized Resolvent (`W_alg(e; q) = 1`):** when the regular
branch is normalized by the `(3)` symmetric electron reference (`Ŵ_alg(X; q) = τ_X(q) / τ_e(q)` so
`Ŵ_alg(e; q) = 1`), the leading `ℏ_q⁻²` pole of `W(μ; q) / W(e; q)` is **exact** `Vol(μ) / ℏ_q²`,
with finite-`q` remainder `W_alg(μ; q) + (ℏ_q)⁻¹ Vol(μ) c_tors(μ) + Vol(μ) c₂(μ)`. -/
theorem carrier_ratio_of_electron_unit_alg (R : InhomogeneousLoopResolvent ι K) {e mu : ι} {q : K}
    (hq1 : q ≠ 1) (hve : R.vol e = 0) (hwe : R.wAlg e q = 1) :
    R.eval mu q / R.eval e q - hbarInvSq q * R.vol mu =
      R.wAlg mu q + (hbar q)⁻¹ * R.vol mu * R.cTors mu + R.vol mu * R.cTwo mu := by
  have hh : hbar q ≠ 0 := hbar_ne_zero q hq1
  have hh2 : hbar q ^ 2 ≠ 0 := pow_ne_zero 2 hh
  have hinv : hbarInvSq q = (hbar q ^ 2)⁻¹ := rfl
  rw [R.carrier_ratio_decomp hve (by rw [hwe]; exact one_ne_zero), hwe, hinv]
  field_simp
  ring

end InhomogeneousLoopResolvent

end InhomogeneousResolvent

section ScaleDriftReconciliation

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Why `QVolumeCarrier`'s constant-`c` unnormalized sum drifts below `Vol / ℏ_q²` for `q > 1`:**
if `W_alg(e; q) = τ_e(q)` is left unnormalized and `c = τ_e(1) = 1/2` is held constant, then
`τ_e(q) > 1/2` for every `q > 1`, forcing `(1/2) / τ_e(q) < 1` (at `q₀`, `0.5 / 0.6912 = 0.7234`,
accounting for `QVolumeCarrier`'s `-27.3%` miss). -/
theorem half_div_tauElectron_lt_one {q : K} (hq : 1 < q) :
    (1 / 2 : K) / tauElectron q < 1 := by
  have hq0 : 0 < q := by linarith
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hte : tauElectron q =
      q ^ 3 * (1 / 2 + (q - q⁻¹) ^ 2 / (2 * (q + q⁻¹) ^ 2)) := by
    unfold tauElectron
    rw [tau_electron_eq_framing_mul_y3 q hq0.ne', y3_split q hq0.ne' hq2 two_ne_zero]
  have hs : q + q⁻¹ ≠ 0 := by
    intro h; apply hq2; field_simp at h; linear_combination h
  have hrem_nonneg : 0 ≤ (q - q⁻¹) ^ 2 / (2 * (q + q⁻¹) ^ 2) := by
    have hnum : 0 ≤ (q - q⁻¹) ^ 2 := sq_nonneg _
    have hden : 0 < 2 * (q + q⁻¹) ^ 2 := mul_pos two_pos (sq_pos_of_ne_zero hs)
    exact div_nonneg hnum hden.le
  have hq3_gt_one : 1 < q ^ 3 := by
    have hsub : 0 < q - 1 := sub_pos.mpr hq
    have hfac : q ^ 3 - 1 = (q - 1) * (q ^ 2 + q + 1) := by ring
    have hpos : 0 < q ^ 3 - 1 := by rw [hfac]; positivity
    linarith
  have hgt_half : (1 / 2 : K) < tauElectron q := by
    rw [hte]
    nlinarith
  have hte_pos : 0 < tauElectron q := by linarith
  exact (div_lt_one hte_pos).mpr hgt_half

end ScaleDriftReconciliation

/-! ## Section 3: `4₁` 1-Loop Reidemeister Torsion & Murakami Real-`q` Cone Window (`qou-mk7u`) -/

section MurakamiReidemeisterTorsion

variable {K : Type*} [Field K]

/-- Bar-even meridian coordinate `w(m) = m + m⁻¹ - 2 = [2]_m - 2`. -/
def wCoord (m : K) : K := m + m⁻¹ - 2

theorem wCoord_eq_mul_hbar_sq (m : K) (hm : m ≠ 0) :
    wCoord m = m * hbar m ^ 2 := by
  unfold wCoord hbar
  field_simp
  ring

theorem wCoord_bar_inv (m : K) : wCoord m⁻¹ = wCoord m := by
  unfold wCoord
  rw [inv_inv]
  ring

/-- Riley–Murakami `4₁` Reidemeister torsion discriminant `(m + m⁻¹ + 1)(m + m⁻¹ - 3)`
(`[murakami-h2011]` Thm. 1.3 & §4.1–4.2, where `m = e^u`). -/
def reidemeisterDisc41 (m : K) : K :=
  (m + m⁻¹ + 1) * (m + m⁻¹ - 3)

/-- Cohomological twisted Reidemeister torsion squared `T_Reid(m)² = 4 / Δ_{4₁}(m)`
(`[murakami-h2011]` Thm. 1.3: `T(u) = 2 / √((e^u + e⁻ᵘ + 1)(e^u + e⁻ᵘ - 3))`). -/
def reidemeisterTorsionSq41 (m : K) : K :=
  4 / reidemeisterDisc41 m

/-- **Exact factorization in the bar-even `w`-coordinate:**
`Δ_{4₁}(m) = (w(m) + 3)(w(m) - 1) = w(m)² + 2 w(m) - 3`. -/
theorem reidemeisterDisc41_eq_wCoord (m : K) :
    reidemeisterDisc41 m = (wCoord m + 3) * (wCoord m - 1) ∧
      reidemeisterDisc41 m = wCoord m ^ 2 + 2 * wCoord m - 3 := by
  unfold reidemeisterDisc41 wCoord
  exact ⟨by ring, by ring⟩

/-- **Exact bar-invariance (`4₁` amphichirality):** `Δ_{4₁}(m⁻¹) = Δ_{4₁}(m)`. -/
theorem reidemeisterDisc41_bar_inv (m : K) :
    reidemeisterDisc41 m⁻¹ = reidemeisterDisc41 m := by
  rw [(reidemeisterDisc41_eq_wCoord m⁻¹).1, (reidemeisterDisc41_eq_wCoord m).1, wCoord_bar_inv]

/-- **Parabolic `m = 1` (`u = 0`) specialization:** `Δ_{4₁}(1) = -3` and `T_Reid(1)² = -4/3`,
recovering `T(0) = 2 / √(-3)` and untwisted torsion norm `|4 / T(0)²| = 3 = (√3)²`. -/
theorem reidemeisterDisc41_at_one (h3 : (3 : K) ≠ 0) :
    reidemeisterDisc41 (1 : K) = -3 ∧ reidemeisterTorsionSq41 (1 : K) = -4 / 3 := by
  have hd : reidemeisterDisc41 (1 : K) = -3 := by unfold reidemeisterDisc41; norm_num
  refine ⟨hd, ?_⟩
  unfold reidemeisterTorsionSq41
  rw [hd]
  have hm3 : (-3 : K) ≠ 0 := neg_ne_zero.mpr h3
  field_simp

/-- **Riley–Murakami `4₁` Longitude Unit-Norm Identity (`[murakami-h2011]` §4.1):**
over any field (`char K ≠ 2`, `m ≠ 0`),
`((m² - m - 2 - m⁻¹ + m⁻²)² - (m - m⁻¹)² Δ_{4₁}(m)) / 4 = 1`, proving that on the cone-manifold
window `Δ_{4₁}(m) < 0` (`2 < m + m⁻¹ < 3`) the complex longitude eigenvalue `ℓ(m)` satisfies
`|ℓ(m)|² = 1` identically. -/
theorem riley_longitude_unit_norm_identity (m : K) (hm : m ≠ 0) (h2 : (2 : K) ≠ 0) :
    ((m ^ 2 - m - 2 - m⁻¹ + m⁻¹ ^ 2) ^ 2 - (m - m⁻¹) ^ 2 * reidemeisterDisc41 m) / 4 = 1 := by
  have h4 : (4 : K) ≠ 0 := by
    have e : (4 : K) = 2 * 2 := by norm_num
    rw [e]; exact mul_ne_zero h2 h2
  unfold reidemeisterDisc41
  field_simp
  ring

end MurakamiReidemeisterTorsion

section OrderedConeWindow

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Every real substrate parameter in `(1, 3/2]` (in particular `q₀ ≈ 1.11`) lies strictly inside
Murakami's hyperbolic cone-manifold window `0 < w(m) < 1` (`2 < m + m⁻¹ < 3`). -/
theorem wCoord_in_cone_of_le_three_halves {m : K} (hm1 : 1 < m) (hm32 : m ≤ 3 / 2) :
    0 < wCoord m ∧ wCoord m < 1 := by
  have hm0 : 0 < m := by linarith
  have hsub : 0 < m - 1 := sub_pos.mpr hm1
  have hw_eq : wCoord m = (m - 1) ^ 2 / m := by
    unfold wCoord; field_simp; ring
  rw [hw_eq]
  refine ⟨by positivity, ?_⟩
  rw [div_lt_one hm0]
  have hle : m - 1 ≤ 1 / 2 := by linarith
  nlinarith

/-- On the cone window `0 < w(m) < 1`, `-3 < Δ_{4₁}(m) < 0` and the squared Reidemeister torsion
magnitude `4 / (-Δ_{4₁}(m))` strictly exceeds its `m = 1` value `4/3` (positive relative shift). -/
theorem reidemeisterTorsionAbsSq_excess_pos {m : K} (hw0 : 0 < wCoord m) (hw1 : wCoord m < 1) :
    -3 < reidemeisterDisc41 m ∧
      reidemeisterDisc41 m < 0 ∧
      0 < (4 / (-reidemeisterDisc41 m)) / (4 / 3) - 1 := by
  rw [(reidemeisterDisc41_eq_wCoord m).2]
  have hneg : wCoord m ^ 2 + 2 * wCoord m - 3 < 0 := by
    have hf : wCoord m ^ 2 + 2 * wCoord m - 3 = (wCoord m + 3) * (wCoord m - 1) := by ring
    rw [hf]
    exact mul_neg_of_pos_of_neg (by linarith) (by linarith)
  have hgt : -3 < wCoord m ^ 2 + 2 * wCoord m - 3 := by nlinarith
  refine ⟨hgt, hneg, ?_⟩
  have hden : 0 < 3 - 2 * wCoord m - wCoord m ^ 2 := by linarith
  have hexcess :
      (4 / (-(wCoord m ^ 2 + 2 * wCoord m - 3))) / (4 / 3) - 1 =
        wCoord m * (2 + wCoord m) / (3 - 2 * wCoord m - wCoord m ^ 2) := by
    have hd_ne : 3 - 2 * wCoord m - wCoord m ^ 2 ≠ 0 := hden.ne'
    have hneg_eq : -(wCoord m ^ 2 + 2 * wCoord m - 3) = 3 - 2 * wCoord m - wCoord m ^ 2 := by ring
    rw [hneg_eq]
    field_simp
    ring
  rw [hexcess]
  positivity

end OrderedConeWindow

/-! ## Section 4: Differential Two-Term QED Self-Energy & Satellite Volume Additivity -/

section DifferentialQEDAndSatellite

variable {K : Type*} [Field K]

/-- **Universal multiplicative QED self-energy cancels in `m_μ / m_e`:** any topological-blind
1-loop multiplicative factor `1 + δ ≠ 0` cancels identically between numerator and denominator. -/
theorem universal_qed_self_energy_cancels (me0 mmu0 δ : K) (hδ : 1 + δ ≠ 0) :
    (mmu0 * (1 + δ)) / (me0 * (1 + δ)) = mmu0 / me0 := by
  exact mul_div_mul_right mmu0 me0 hδ

/-- **Exact differential two-term radiative shift:** for `m_ℓ = m_ℓ⁽⁰⁾(1 + ε Σ_ℓ)` (`m_e⁽⁰⁾ ≠ 0`,
`1 + ε Σ_e ≠ 0`), the shifted ratio satisfies
`m_μ / m_e - m_μ⁽⁰⁾ / m_e⁽⁰⁾ = (m_μ⁽⁰⁾ / m_e⁽⁰⁾) · ε (Σ_μ - Σ_e) / (1 + ε Σ_e)`. -/
theorem differential_two_term_ratio_shift (me0 mmu0 ε se smu : K)
    (hme0 : me0 ≠ 0) (hden : 1 + ε * se ≠ 0) :
    (mmu0 * (1 + ε * smu)) / (me0 * (1 + ε * se)) - mmu0 / me0 =
      (mmu0 / me0) * (ε * (smu - se) / (1 + ε * se)) := by
  field_simp
  ring

/-- **Satellite zero-volume pattern identity (`T(2,7) ⋈ 4₁`):** under simplicial volume additivity
`volSat = volPattern + volCompanion`, any zero-volume torus pattern (`volPattern = 0`) leaves both
the volume and the `ℏ_q⁻²` singular saddle carrier identical to the companion's (`Vol(4₁) / ℏ_q²`). -/
theorem satellite_torus_volume_eq_companion (volSat volPattern volCompanion q : K)
    (hadd : volSat = volPattern + volCompanion) (hpat : volPattern = 0) :
    volSat = volCompanion ∧ hbarInvSq q * volSat = hbarInvSq q * volCompanion := by
  rw [hadd, hpat, zero_add]
  exact ⟨rfl, rfl⟩

end DifferentialQEDAndSatellite

section OrderedDifferentialQED

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Sign selection rule for lowering a positive bare carrier overshoot:** when `m_μ⁽⁰⁾ / m_e⁽⁰⁾ > 0`,
`ε > 0`, and `1 + ε Σ_e > 0`, the radiative shift lowers `m_μ / m_e` strictly below `m_μ⁽⁰⁾ / m_e⁽⁰⁾`
**if and only if** `Σ_μ < Σ_e`. -/
theorem differential_shift_neg_iff {me0 mmu0 ε se smu : K}
    (hme0 : 0 < me0) (hmmu0 : 0 < mmu0) (hε : 0 < ε) (hden : 0 < 1 + ε * se) :
    (mmu0 * (1 + ε * smu)) / (me0 * (1 + ε * se)) < mmu0 / me0 ↔ smu < se := by
  have hdiff := differential_two_term_ratio_shift me0 mmu0 ε se smu hme0.ne' hden.ne'
  have hr0 : 0 < mmu0 / me0 := div_pos hmmu0 hme0
  constructor
  · intro hlt
    have hneg : (mmu0 * (1 + ε * smu)) / (me0 * (1 + ε * se)) - mmu0 / me0 < 0 := sub_neg.mpr hlt
    rw [hdiff] at hneg
    by_contra hge
    push_neg at hge
    have hnn : 0 ≤ (mmu0 / me0) * (ε * (smu - se) / (1 + ε * se)) :=
      mul_nonneg hr0.le (div_nonneg (mul_nonneg hε.le (sub_nonneg.mpr hge)) hden.le)
    linarith
  · intro hlt
    have hnum : ε * (smu - se) < 0 := mul_neg_of_pos_of_neg hε (sub_neg.mpr hlt)
    have hfrac : ε * (smu - se) / (1 + ε * se) < 0 := div_neg_of_neg_of_pos hnum hden
    have hprod : (mmu0 / me0) * (ε * (smu - se) / (1 + ε * se)) < 0 :=
      mul_neg_of_pos_of_neg hr0 hfrac
    linarith

/-- **Opposite `(2,1)`-channel asymmetry on `1 < q ≤ 5/4`:** while the Hopf electron has `(2,1)`
trace `0` (`electron_21_trace_zero`), the figure-eight `(2,1)` trace is strictly negative across
`1 < q ≤ 5/4` (`(q - q⁻¹)² ≤ 81/400 < 1/3`, covering `q₀ ≈ 1.11`). -/
theorem fig8_21_trace_neg_of_le_five_fourths {q : K} (hq1 : 1 < q) (hq54 : q ≤ 5 / 4) :
    (fig8Mat21 q).trace < (r21a q * r21b q * r21a q).trace := by
  have hq0 : 0 < q := by linarith
  rw [fig8_21_trace q hq0.ne', electron_21_trace_zero q hq0.ne']
  have hinv_ge : (4 / 5 : K) ≤ q⁻¹ := by
    rw [le_inv_comm₀ (by positivity) hq0]
    linarith
  have hh_pos : 0 < q - q⁻¹ := by
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq1
    linarith
  have hh_le : q - q⁻¹ ≤ 9 / 20 := by linarith
  have hh2_le : (q - q⁻¹) ^ 2 ≤ 81 / 400 := by nlinarith
  nlinarith

end OrderedDifferentialQED

end QOU.Observations.InhomogeneousLeptonLoopResolvent
