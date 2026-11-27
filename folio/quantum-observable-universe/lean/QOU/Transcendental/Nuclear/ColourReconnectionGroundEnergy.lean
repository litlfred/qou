import QOU.Nuclear.ColourReconnectionStokesAssembly
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# Colour reconnection: the exact 2-channel ground energy

Split out of `QOU.Nuclear.ColourReconnectionStokesAssembly` because the closed-form lowest
eigenvalue `E₀ + (Δ₈ − √(Δ₈² + 4v²))/2` takes a real square root. The rational multi-channel
Schur-complement bound `multiChannel_schur_rayleigh_lt` and everything else stay in that file,
outside the transcendental boundary. Namespace and names are unchanged.
-/

namespace QOU.Nuclear.ColourReconnectionStokesAssembly

/-- Exact lowest eigenvalue `E_-(E₀, Δ₈, v) = E₀ + (Δ₈ - √(Δ₈² + 4 v²)) / 2` of the coupled `2 × 2`
nucleon–hidden-colour Hamiltonian `[[E₀, v], [v, E₀ + Δ₈]]` over `ℝ`. -/
noncomputable def reconnGroundEnergy (E₀ Δ₈ v : ℝ) : ℝ :=
  E₀ + (Δ₈ - Real.sqrt (Δ₈ ^ 2 + 4 * v ^ 2)) / 2

/-- **Exact 2-Channel Bloch–Horowitz / Schur-Complement Variational Bound
(`colourReconnection_lowers_ground_energy`).**
Coupling the factorized `|11⟩` channel at energy `E₀` to the hidden-colour `|88⟩` channel at gap
`Δ₈ > 0` via any nonzero off-diagonal braid crossing `v ≠ 0`:
1. Solves the characteristic equation `(E₀ - E_-)(E₀ + Δ₈ - E_-) - v² = 0`;
2. Satisfies the exact Bloch–Horowitz Schur-complement equation
   `E_- - E₀ = -v² / (Δ₈ + (E₀ - E_-))`;
3. Strictly lowers the ground-state energy (`E_- < E₀`);
4. Satisfies the global `O(v⁴)` Schur-complement sandwich
   `-v² / Δ₈ < E_- - E₀ ∧ E_- - E₀ ≤ -v² / Δ₈ + v⁴ / Δ₈³`. -/
theorem colourReconnection_lowers_ground_energy
    (E₀ Δ₈ v : ℝ) (hΔ : 0 < Δ₈) (hv : v ≠ 0) :
    (E₀ - reconnGroundEnergy E₀ Δ₈ v) * (E₀ + Δ₈ - reconnGroundEnergy E₀ Δ₈ v) - v ^ 2 = 0 ∧
    reconnGroundEnergy E₀ Δ₈ v - E₀ =
      -v ^ 2 / (Δ₈ + (E₀ - reconnGroundEnergy E₀ Δ₈ v)) ∧
    reconnGroundEnergy E₀ Δ₈ v < E₀ ∧
    (-v ^ 2 / Δ₈ < reconnGroundEnergy E₀ Δ₈ v - E₀ ∧
      reconnGroundEnergy E₀ Δ₈ v - E₀ ≤ -v ^ 2 / Δ₈ + v ^ 4 / Δ₈ ^ 3) := by
  set S := Real.sqrt (Δ₈ ^ 2 + 4 * v ^ 2) with hS_def
  have hv2 : 0 < v ^ 2 := sq_pos_of_ne_zero hv
  have hrad_pos : 0 < Δ₈ ^ 2 + 4 * v ^ 2 := by positivity
  have hS_sq : S ^ 2 = Δ₈ ^ 2 + 4 * v ^ 2 := Real.sq_sqrt hrad_pos.le
  have hS_gt : Δ₈ < S := by
    rw [← Real.sqrt_sq hΔ.le]
    exact Real.sqrt_lt_sqrt (sq_nonneg Δ₈) (by linarith)
  have hS_pos : 0 < S := lt_trans hΔ hS_gt
  set δ := E₀ - reconnGroundEnergy E₀ Δ₈ v with hδ_def
  have hδ_eq : δ = (S - Δ₈) / 2 := by
    simp only [hδ_def, reconnGroundEnergy]
    ring
  have hδ_pos : 0 < δ := by
    rw [hδ_eq]; linarith
  have hquad : δ * (Δ₈ + δ) = v ^ 2 := by
    rw [hδ_eq]
    nlinarith [hS_sq]
  have hchar : (E₀ - reconnGroundEnergy E₀ Δ₈ v) *
      (E₀ + Δ₈ - reconnGroundEnergy E₀ Δ₈ v) - v ^ 2 = 0 := by
    have hrew : E₀ + Δ₈ - reconnGroundEnergy E₀ Δ₈ v = Δ₈ + δ := by
      simp only [hδ_def]; ring
    rw [← hδ_def, hrew]
    linarith [hquad]
  have hden_pos : 0 < Δ₈ + δ := by linarith
  have hbh : reconnGroundEnergy E₀ Δ₈ v - E₀ = -v ^ 2 / (Δ₈ + δ) := by
    have h1 : reconnGroundEnergy E₀ Δ₈ v - E₀ = -δ := by simp only [hδ_def]; ring
    rw [h1, eq_div_iff hden_pos.ne']
    linarith [hquad]
  have hlt_E0 : reconnGroundEnergy E₀ Δ₈ v < E₀ := by
    simp only [hδ_def] at hδ_pos; linarith
  have hδ_lt_first : δ < v ^ 2 / Δ₈ := by
    rw [lt_div_iff₀ hΔ]
    nlinarith [hquad, sq_pos_of_pos hδ_pos]
  have hlo : -v ^ 2 / Δ₈ < reconnGroundEnergy E₀ Δ₈ v - E₀ := by
    have h1 : reconnGroundEnergy E₀ Δ₈ v - E₀ = -δ := by simp only [hδ_def]; ring
    rw [h1, neg_div]
    linarith [hδ_lt_first]
  have hhi : reconnGroundEnergy E₀ Δ₈ v - E₀ ≤ -v ^ 2 / Δ₈ + v ^ 4 / Δ₈ ^ 3 := by
    have h1 : reconnGroundEnergy E₀ Δ₈ v - E₀ = -δ := by simp only [hδ_def]; ring
    rw [h1, neg_div]
    have hdiff : v ^ 2 / Δ₈ - δ = (v ^ 2 * δ) / (Δ₈ * (Δ₈ + δ)) := by
      have hd1 : Δ₈ ≠ 0 := hΔ.ne'
      have hd2 : Δ₈ + δ ≠ 0 := hden_pos.ne'
      have hd3 : Δ₈ * (Δ₈ + δ) ≠ 0 := mul_ne_zero hd1 hd2
      rw [eq_div_iff hd3]
      calc (v ^ 2 / Δ₈ - δ) * (Δ₈ * (Δ₈ + δ))
          = (v ^ 2 / Δ₈ * Δ₈) * (Δ₈ + δ) - δ * Δ₈ * (Δ₈ + δ) := by ring
        _ = v ^ 2 * (Δ₈ + δ) - Δ₈ * (δ * (Δ₈ + δ)) := by
              rw [div_mul_cancel₀ _ hd1]; ring
        _ = v ^ 2 * (Δ₈ + δ) - Δ₈ * v ^ 2 := by rw [hquad]
        _ = v ^ 2 * δ := by ring
    have hub1 : (v ^ 2 * δ) / (Δ₈ * (Δ₈ + δ)) ≤ (v ^ 2 * (v ^ 2 / Δ₈)) / (Δ₈ * Δ₈) := by
      have hnum_le : v ^ 2 * δ ≤ v ^ 2 * (v ^ 2 / Δ₈) :=
        mul_le_mul_of_nonneg_left hδ_lt_first.le hv2.le
      have hden_le : Δ₈ * Δ₈ ≤ Δ₈ * (Δ₈ + δ) :=
        mul_le_mul_of_nonneg_left (by linarith) hΔ.le
      exact div_le_div₀ (by positivity) hnum_le (by positivity) hden_le
    have hsimp : (v ^ 2 * (v ^ 2 / Δ₈)) / (Δ₈ * Δ₈) = v ^ 4 / Δ₈ ^ 3 := by
      field_simp [hΔ.ne']
    linarith [hdiff, hub1, hsimp]
  exact ⟨hchar, hbh, hlt_E0, ⟨hlo, hhi⟩⟩

end QOU.Nuclear.ColourReconnectionStokesAssembly
