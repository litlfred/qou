/-
# Is E₀'s weight `ℏ_q/q²` a convention-D Markov trace?

Companion to `computations/probes/e0_weight/` (prereg commit 89dc8589e37). The probe computes
six convention-D traces in exact `ℚ(q)` arithmetic; this file proves their closed forms from the
Ocneanu weights and the 2-dimensional `(2,1)` representation already in
`QOU.QBeta.WeightSpaceMarkov`, and proves that none of them is the weight
`w(q) = (q - 1)/q³` as a function of `q > 1`.

It also proves the two limits used in the energy-map audit (§30, §32):
`log q / (q (q - 1)) → 1` and the n–p cell weight `2 (q - 1) log q / q³ → 0` as `q → 1⁺`.
-/
import QOU.QBeta.WeightSpaceMarkov
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace QOU.QBeta.E0WeightCandidates

open QOU.QBeta.WeightSpaceMarkov Filter Topology

variable {R : Type*} [Field R]

/-- `σ⁻¹ = σ - h` in the `(2,1)` representation, `h = q - q⁻¹`. -/
def inv21 (q : R) (M : Matrix (Fin 2) (Fin 2) R) : Matrix (Fin 2) (Fin 2) R :=
  M - (q - q⁻¹) • (1 : Matrix (Fin 2) (Fin 2) R)

theorem r21a_mul_inv (q : R) (hq : q ≠ 0) : r21a q * inv21 q (r21a q) = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [r21a, inv21, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem r21b_mul_inv (q : R) (hq : q ≠ 0) : r21b q * inv21 q (r21b q) = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [r21b, inv21, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem inv21_r21a (q : R) : inv21 q (r21a q) = !![q⁻¹, 1; 0, -q] := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [inv21, r21a]; ring

theorem inv21_r21b (q : R) : inv21 q (r21b q) = !![-q, 0; 1, q⁻¹] := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [inv21, r21b]; ring

/-- The convention-D trace on `H₃`: `y₃ χ₃ + y₂₁ χ₂₁` (`y_(1³) = 0`). -/
def tauD3 (q c3 : R) (M : Matrix (Fin 2) (Fin 2) R) : R := y3 q * c3 + y21 q * M.trace

/-- C3: the electron word `σ₀σ₁σ₀`. -/
theorem tau_electron (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    tauD3 q (q ^ 3) (r21a q * r21b q * r21a q) = q ^ 3 * (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  have hs : q + q⁻¹ ≠ 0 := by
    intro h; apply hq2; field_simp at h; linear_combination h
  unfold tauD3 y3 y21
  simp [r21a, r21b, Matrix.trace_fin_two]
  field_simp
  ring

/-- C3: the inverse electron word. -/
theorem tau_electron_inv (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    tauD3 q (q⁻¹ ^ 3) (inv21 q (r21a q) * inv21 q (r21b q) * inv21 q (r21a q)) =
      (q ^ 4 + 1) / (q ^ 3 * (q ^ 2 + 1) ^ 2) := by
  have hs : q + q⁻¹ ≠ 0 := by
    intro h; apply hq2; field_simp at h; linear_combination h
  rw [inv21_r21a, inv21_r21b]
  unfold tauD3 y3 y21
  simp [Matrix.trace_fin_two]
  field_simp
  ring

/-- C4: the photon vertex `σ₀σ₁⁻¹`. -/
theorem tau_vertex (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    tauD3 q (q * q⁻¹) (r21a q * inv21 q (r21b q)) = q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  have hs : q + q⁻¹ ≠ 0 := by
    intro h; apply hq2; field_simp at h; linear_combination h
  rw [inv21_r21b]
  unfold tauD3 y3 y21
  simp [r21a, Matrix.trace_fin_two]
  field_simp
  ring

/-! ### n = 2 -/

/-- Convention-D Ocneanu weights at `n = 2`. -/
def y11 (q : R) : R := q ^ 2 / (q ^ 2 + 1) ^ 2
def y2 (q : R) : R := 1 - y11 q

/-- The weights solve the `n = 2` Markov moment equations at `z_D = q³/(q²+1)`. -/
theorem n2_moments (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    y2 q + y11 q = 1 ∧ q * y2 q - q⁻¹ * y11 q = q ^ 3 / (q ^ 2 + 1) := by
  refine ⟨by unfold y2; ring, ?_⟩
  unfold y2 y11; field_simp; ring

/-- C1: `tr(σ⁻¹) = 1/(q(q²+1))` at `n = 2`. -/
theorem tau2_inv (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    y2 q * q⁻¹ + y11 q * (-q) = 1 / (q * (q ^ 2 + 1)) := by
  unfold y2 y11; field_simp; ring

/-! ### None of them is the weight -/

/-- The weight of `E₀` in the units `m_e/ℏ_q²`. -/
noncomputable def w (q : ℝ) : ℝ := (q - 1) / q ^ 3

/-- A function of `q` that agrees with `w` on `q > 1` must agree at `q = 2`; each candidate
does not. -/
theorem not_weight_of_two (f : ℝ → ℝ) (h2 : f 2 ≠ 1 / 8) : ¬ ∀ q : ℝ, 1 < q → f q = w q := by
  intro h
  apply h2
  rw [h 2 (by norm_num)]
  unfold w; norm_num

theorem C1_not_weight : ¬ ∀ q : ℝ, 1 < q → 1 / (q * (q ^ 2 + 1)) = w q :=
  not_weight_of_two (fun q => 1 / (q * (q ^ 2 + 1))) (by norm_num)

theorem C2a_not_weight : ¬ ∀ q : ℝ, 1 < q → 1 - q ^ 2 / (q ^ 2 + 1) ^ 2 = w q :=
  not_weight_of_two (fun q => 1 - q ^ 2 / (q ^ 2 + 1) ^ 2) (by norm_num)

theorem C2b_not_weight : ¬ ∀ q : ℝ, 1 < q → q ^ 2 / (q ^ 2 + 1) ^ 2 = w q :=
  not_weight_of_two (fun q => q ^ 2 / (q ^ 2 + 1) ^ 2) (by norm_num)

theorem C3a_not_weight : ¬ ∀ q : ℝ, 1 < q → q ^ 3 * (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 = w q :=
  not_weight_of_two (fun q => q ^ 3 * (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2) (by norm_num)

theorem C3b_not_weight : ¬ ∀ q : ℝ, 1 < q → (q ^ 4 + 1) / (q ^ 3 * (q ^ 2 + 1) ^ 2) = w q :=
  not_weight_of_two (fun q => (q ^ 4 + 1) / (q ^ 3 * (q ^ 2 + 1) ^ 2)) (by norm_num)

theorem C4b_not_weight : ¬ ∀ q : ℝ, 1 < q →
    1 + (Tpoly q - 3) / (q + q⁻¹) ^ 2 = w q :=
  not_weight_of_two (fun q => 1 + (Tpoly q - 3) / (q + q⁻¹) ^ 2) (by unfold Tpoly; norm_num)

/-! ### The limits at `q = 1` -/

/-- `log q / (q (q - 1)) → 1` as `q → 1⁺`: the MeV cell `2 E₀ log q` tends to `2 m_e`. -/
theorem cell_unit_limit :
    Tendsto (fun q : ℝ => Real.log q / (q * (q - 1))) (𝓝[>] 1) (𝓝 1) := by
  have hd : HasDerivAt Real.log 1 1 := by simpa using Real.hasDerivAt_log (one_ne_zero)
  have hs := hd.tendsto_slope_zero_right
  have h1 : Tendsto (fun t : ℝ => Real.log (1 + t) / t) (𝓝[>] 0) (𝓝 1) := by
    refine hs.congr' ?_
    filter_upwards [self_mem_nhdsWithin] with t ht
    simp [Real.log_one, div_eq_inv_mul]
  have h2 : Tendsto (fun q : ℝ => Real.log q / (q - 1)) (𝓝[>] 1) (𝓝 1) := by
    have hmap : Tendsto (fun q : ℝ => q - 1) (𝓝[>] 1) (𝓝[>] 0) := by
      refine tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _ ?_ ?_
      · have : Tendsto (fun q : ℝ => q - 1) (𝓝 1) (𝓝 (1 - 1)) :=
          (continuous_id.sub continuous_const).tendsto 1
        simpa using this.mono_left nhdsWithin_le_nhds
      · filter_upwards [self_mem_nhdsWithin] with q hq
        simpa using sub_pos.mpr (show (1 : ℝ) < q from hq)
    refine (h1.comp hmap).congr' ?_
    filter_upwards with q
    simp
  have h3 : Tendsto (fun q : ℝ => q⁻¹) (𝓝[>] 1) (𝓝 1) := by
    have : Tendsto (fun q : ℝ => q⁻¹) (𝓝 1) (𝓝 (1 : ℝ)⁻¹) :=
      (continuousAt_inv₀ one_ne_zero).tendsto
    simpa using this.mono_left nhdsWithin_le_nhds
  have := h3.mul h2
  simp only [one_mul] at this
  refine this.congr' ?_
  filter_upwards [self_mem_nhdsWithin] with q hq
  have hq0 : q ≠ 0 := by linarith [show (1 : ℝ) < q from hq]
  field_simp

/-- The n–p cell weight `2 (q - 1) log q / q³ → 0` as `q → 1⁺`: the categorical difference
vanishes at `q = 1`. -/
theorem cell_weight_limit :
    Tendsto (fun q : ℝ => 2 * (q - 1) * Real.log q / q ^ 3) (𝓝[>] 1) (𝓝 0) := by
  have hc : Continuous (fun q : ℝ => 2 * (q - 1)) := by continuity
  have : Tendsto (fun q : ℝ => 2 * (q - 1) * Real.log q / q ^ 3) (𝓝 1)
      (𝓝 (2 * (1 - 1) * Real.log 1 / 1 ^ 3)) := by
    refine ((hc.tendsto 1).mul ?_).div ((continuous_pow 3).tendsto 1) (by norm_num)
    exact (Real.continuousAt_log one_ne_zero).tendsto
  simpa using this.mono_left nhdsWithin_le_nhds

/-! ### §25: where `T` changes sign -/

/-- `T` as a function of `x = q²`. -/
def Tx (x : R) : R := -(x ^ 6 - 3 * x ^ 5 + 3 * x ^ 4 - 5 * x ^ 3 + 3 * x ^ 2 - 3 * x + 1) / x ^ 3

theorem Tpoly_eq_Tx (q : R) (hq : q ≠ 0) : Tpoly q = Tx (q ^ 2) := by
  unfold Tpoly Tx; field_simp

/-- `T > 0` at `q² = 2.47` and `T < 0` at `q² = 2.48`: the sign change of §25 lies between. -/
theorem T_sign_change :
    0 < Tpoly (Real.sqrt (247 / 100)) ∧ Tpoly (Real.sqrt (248 / 100)) < 0 := by
  have h1 : Real.sqrt (247 / 100) ≠ 0 := by positivity
  have h2 : Real.sqrt (248 / 100) ≠ 0 := by positivity
  rw [Tpoly_eq_Tx _ h1, Tpoly_eq_Tx _ h2, Real.sq_sqrt (by norm_num), Real.sq_sqrt (by norm_num)]
  unfold Tx
  constructor <;> norm_num

end QOU.QBeta.E0WeightCandidates
