import Mathlib.Data.Real.Basic
import Mathlib.Tactic


/-!
# QOU.Archimedean.groebner_shirshov_energy — Energy as a Gröbner-Shirshov invariant

Only the Hecke relation σ² = (q-q⁻¹)σ + 1 changes energy.
Yang-Baxter and far commutativity preserve energy.
Energy is path-independent (diamond lemma / confluence).

LaTeX label: `thm:groebner-shirshov-energy`

## References
- [manuscript] §6/groebner-shirshov-energy
-/

namespace QOU.Archimedean

/-- A single division step in the Gröbner reduction. -/
-- Ref: [manuscript] §6/groebner-shirshov-energy
inductive DivisionStepType
  | hecke       -- σ_i² → (q-q⁻¹)σ_i + 1 (energy-changing)
  | yangBaxter  -- σ_iσ_{i+1}σ_i → σ_{i+1}σ_iσ_{i+1} (energy-preserving)
  | farComm     -- σ_iσ_j → σ_jσ_i, |i-j|≥2 (energy-preserving)

/-- The energy change per Hecke step: |c| × (q - q⁻¹). -/
-- Ref: [manuscript] §6/groebner-shirshov-energy
noncomputable def heckeEnergyChange (q : ℝ) (coeff : ℝ) : ℝ :=
  |coeff| * (q - 1/q)

/-- The energy change is positive for q > 1. -/
-- Ref: [manuscript] §6/groebner-shirshov-energy
theorem heckeEnergyChange_pos (q : ℝ) (hq : 1 < q) (c : ℝ) (hc : c ≠ 0) :
    0 < heckeEnergyChange q c := by
  unfold heckeEnergyChange
  apply mul_pos
  · exact abs_pos.mpr hc
  · rw [sub_pos, div_lt_iff₀ (by linarith : (0 : ℝ) < q)]
    nlinarith

/-- The energy change of a single division step carrying coefficient `coeff`.
    Only the Hecke relation moves energy; Yang-Baxter and far commutativity are
    energy-preserving. This is the per-step form of the `.hecke`-only filter
    used by `energy_path_independent` below. -/
-- Ref: [manuscript] §6/groebner-shirshov-energy
noncomputable def stepEnergyChange (q coeff : ℝ) : DivisionStepType → ℝ
  | .hecke => heckeEnergyChange q coeff
  | .yangBaxter => 0
  | .farComm => 0

/-- Yang-Baxter steps have zero energy change. -/
-- Ref: [manuscript] §6/groebner-shirshov-energy
theorem yangBaxter_energy_zero (q coeff : ℝ) (step : DivisionStepType)
    (h : step = .yangBaxter) : stepEnergyChange q coeff step = 0 := by
  subst h; rfl

/-- Far commutativity steps have zero energy change. -/
-- Ref: [manuscript] §6/groebner-shirshov-energy
theorem farComm_energy_zero (q coeff : ℝ) (step : DivisionStepType)
    (h : step = .farComm) : stepEnergyChange q coeff step = 0 := by
  subst h; rfl

/-- The step hypothesis in the two results above is load-bearing: the remaining
    constructor genuinely moves energy, so neither statement holds for an
    arbitrary `step`. -/
-- Ref: [manuscript] §6/groebner-shirshov-energy
theorem stepEnergyChange_hecke_ne_zero (q coeff : ℝ) (hq : 1 < q) (hc : coeff ≠ 0) :
    stepEnergyChange q coeff .hecke ≠ 0 := by
  simpa [stepEnergyChange] using ne_of_gt (heckeEnergyChange_pos q hq coeff hc)

/-- The total energy change is the sum of Hecke step energies.
    Yang-Baxter and far commutativity contribute zero. -/
-- Ref: [manuscript] §6/groebner-shirshov-energy
noncomputable def totalEnergyChange (q : ℝ) (hecke_coeffs : List ℝ) : ℝ :=
  (hecke_coeffs.map (heckeEnergyChange q)).sum

/-- Each Hecke energy change is non-negative for q > 1. -/
-- Ref: [manuscript] §6/groebner-shirshov-energy
private theorem heckeEnergyChange_nonneg (q : ℝ) (hq : 1 < q) (c : ℝ) :
    0 ≤ heckeEnergyChange q c := by
  unfold heckeEnergyChange
  apply mul_nonneg (abs_nonneg _)
  have hq_pos : (0 : ℝ) < q := by linarith
  rw [sub_nonneg, div_le_iff₀ hq_pos]
  nlinarith

/-- The total energy is non-negative for q > 1. -/
-- Ref: [manuscript] §6/groebner-shirshov-energy
theorem totalEnergyChange_nonneg (q : ℝ) (hq : 1 < q)
    (coeffs : List ℝ) :
    0 ≤ totalEnergyChange q coeffs := by
  unfold totalEnergyChange
  apply List.sum_nonneg
  intro x hx
  rw [List.mem_map] at hx
  obtain ⟨c, _, rfl⟩ := hx
  exact heckeEnergyChange_nonneg q hq c

/-! **The former axiom `energy_path_independent` was false** (removed
    2026-11-15). It equated the energy of *any* two step lists, with no
    hypothesis that they are reduction paths of the same element. A path
    with one Hecke step costs `q - 1/q > 0` and the empty path costs `0`.
    `not_energy_path_independent` below proves this at `q = 2`. The true
    statement (energy depends only on the normal form, by confluence)
    needs the paths to be actual reductions of `initial`; open in Lean,
    bean `qou-n2un`. -/

/-- **The former axiom is false.** -/
theorem not_energy_path_independent :
    ¬ ∀ (q : ℝ) (_hq : 1 < q) (_initial : List (List ℕ × ℝ))
      (path1 path2 : List DivisionStepType),
      totalEnergyChange q (path1.filterMap fun s =>
          match s with | .hecke => some 1 | _ => none) =
        totalEnergyChange q (path2.filterMap fun s =>
          match s with | .hecke => some 1 | _ => none) := by
  intro h
  have := h 2 (by norm_num) [] [.hecke] []
  simp [totalEnergyChange, heckeEnergyChange] at this
  norm_num at this

/-- The beta-decay energy difference is always negative:
    the daughter has lower energy than the parent.
    (Computationally verified for all A ≤ 6.)

    **Was an axiom; now proved (2026-11-15).** As stated, the two reals
    are existentially quantified and not tied to any parent or daughter,
    so `1` and `0` witness it. The intended content (the energies of the
    actual parent and daughter normal forms) is open in Lean, bean
    `qou-n2un`. -/
-- Ref: [manuscript] §6/groebner-shirshov-energy
theorem beta_decay_energy_negative (_q : ℝ) (_hq : 1 < _q)
    (_p _n : ℕ) (_hn : 0 < _n) :
    ∃ (𝒮_par E_dau : ℝ), E_dau < 𝒮_par :=
  ⟨1, 0, one_pos⟩

/-- Top-level alias matching the manifest declaration. -/
-- Ref: [manuscript] §6/groebner-shirshov-energy
noncomputable def groebner_shirshov_energy (q : ℝ) (coeffs : List ℝ) : ℝ :=
  totalEnergyChange q coeffs

end QOU.Archimedean
