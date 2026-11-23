import Mathlib.Data.Real.Basic
import Mathlib.Tactic


/-!
# QOU.Archimedean.groebner_shirshov_energy — Energy as a Gröbner-Shirshov invariant

Only the Hecke relation σ² = (q-q⁻¹)σ + 1 changes energy.
Yang-Baxter and far commutativity preserve energy.
Energy is path-independent (diamond lemma / confluence).

LaTeX label: `thm:groebner-shirshov-energy`

## References
- [leitner2026] §6/groebner-shirshov-energy
-/

namespace QOU.Archimedean

/-- A single division step in the Gröbner reduction. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
inductive DivisionStepType
  | hecke       -- σ_i² → (q-q⁻¹)σ_i + 1 (energy-changing)
  | yangBaxter  -- σ_iσ_{i+1}σ_i → σ_{i+1}σ_iσ_{i+1} (energy-preserving)
  | farComm     -- σ_iσ_j → σ_jσ_i, |i-j|≥2 (energy-preserving)

/-- The energy change per Hecke step: |c| × (q - q⁻¹). -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
noncomputable def heckeEnergyChange (q : ℝ) (coeff : ℝ) : ℝ :=
  |coeff| * (q - 1/q)

/-- The energy change is positive for q > 1. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
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
-- Ref: [leitner2026] §6/groebner-shirshov-energy
noncomputable def stepEnergyChange (q coeff : ℝ) : DivisionStepType → ℝ
  | .hecke => heckeEnergyChange q coeff
  | .yangBaxter => 0
  | .farComm => 0

/-- Yang-Baxter steps have zero energy change. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
theorem yangBaxter_energy_zero (q coeff : ℝ) (step : DivisionStepType)
    (h : step = .yangBaxter) : stepEnergyChange q coeff step = 0 := by
  subst h; rfl

/-- Far commutativity steps have zero energy change. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
theorem farComm_energy_zero (q coeff : ℝ) (step : DivisionStepType)
    (h : step = .farComm) : stepEnergyChange q coeff step = 0 := by
  subst h; rfl

/-- The step hypothesis in the two results above is load-bearing: the remaining
    constructor genuinely moves energy, so neither statement holds for an
    arbitrary `step`. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
theorem stepEnergyChange_hecke_ne_zero (q coeff : ℝ) (hq : 1 < q) (hc : coeff ≠ 0) :
    stepEnergyChange q coeff .hecke ≠ 0 := by
  simpa [stepEnergyChange] using ne_of_gt (heckeEnergyChange_pos q hq coeff hc)

/-- The total energy change is the sum of Hecke step energies.
    Yang-Baxter and far commutativity contribute zero. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
noncomputable def totalEnergyChange (q : ℝ) (hecke_coeffs : List ℝ) : ℝ :=
  (hecke_coeffs.map (heckeEnergyChange q)).sum

/-- Each Hecke energy change is non-negative for q > 1. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
private theorem heckeEnergyChange_nonneg (q : ℝ) (hq : 1 < q) (c : ℝ) :
    0 ≤ heckeEnergyChange q c := by
  unfold heckeEnergyChange
  apply mul_nonneg (abs_nonneg _)
  have hq_pos : (0 : ℝ) < q := by linarith
  rw [sub_nonneg, div_le_iff₀ hq_pos]
  nlinarith

/-- The total energy is non-negative for q > 1. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
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

/-! ## β-decay sign, short typed-crossing model (replaces a vacuous theorem, 2026-11-21)

The declaration `beta_decay_energy_negative` stood here until 2026-11-21 with
the statement `∃ (𝒮_par E_dau : ℝ), E_dau < 𝒮_par`. Both reals were
existentially quantified and tied to no parent, daughter, normal form or
energy, and every hypothesis (`_q`, `_hq`, `_p`, `_n`, `_hn`) was unused, so
`⟨1, 0, one_pos⟩` proved it. It asserted nothing about β decay. Its docstring
also said "computationally verified for all A ≤ 6"; no producer or witness
for that claim was found in `computations/`, `docs/audits/` or the beans.

There is no model-free statement to put in its place. PR #8682 (bean
`qou-99qc`, P3) measured the nucleon-only change of `E(ξ) = Σ_w |c_w| ℓ(w)`
at the proton `q₀` in the three corpus nucleon models: daughter lower in the
short typed-crossing model (`−0.20906`), daughter higher in the 11-letter
typed model (`+0.06389`), equal on the γγ base `V³`. That is a scope-(a)
measurement on named models, not a structural exclusion.

What is true, and proved below for every real `h`, is the short-model case.
In the `H₃(q)` basis `T_w`, ordered `e, s₁, s₂, s₁s₂, s₂s₁, s₁s₂s₁`, the
short-model nucleon normal forms are
`p = σ₁σ₂ − (h/2)σ₁` and `n = σ₁σ₂ − hσ₁ − (h/2)σ₂ + h²/2`, with
`n − p = Δ_S` (`computations/qbeta/qbeta_delta_element_fork_pricing_probe.py`;
the same vectors are `nucP` / `nucN` in PR #8682's
`QOU/QBeta/NormalFormLengthInvariants.lean`). Then
`E(p) − E(n) = −|h|`, so for `q > 1` the daughter proton has the lower energy. -/

/-- Bruhat length on `S₃`, basis order `e, s₁, s₂, s₁s₂, s₂s₁, s₁s₂s₁`. -/
def s3Len : Fin 6 → ℕ := ![0, 1, 1, 2, 2, 3]

/-- `E(ξ) = Σ_w |c_w| ℓ(w)` on an `H₃(q)` normal form given by its coefficient
    vector in the basis `T_w`, `w ∈ S₃`. -/
noncomputable def s3Energy (v : Fin 6 → ℝ) : ℝ := ∑ k, |v k| * (s3Len k : ℝ)

/-- Short-model proton normal form `σ₁σ₂ − (h/2)σ₁`. -/
noncomputable def shortProton (h : ℝ) : Fin 6 → ℝ := ![0, -h / 2, 0, 1, 0, 0]

/-- Short-model neutron normal form `σ₁σ₂ − hσ₁ − (h/2)σ₂ + h²/2`. -/
noncomputable def shortNeutron (h : ℝ) : Fin 6 → ℝ := ![h ^ 2 / 2, -h, -h / 2, 1, 0, 0]

/-- **β-decay energy change, short typed-crossing model, nucleon only:**
    `E(p) − E(n) = −|h|`, for every real `h`. The `h²/2` term of the neutron
    sits on the identity (`ℓ = 0`) and does not contribute. -/
theorem beta_decay_energy_sub_shortModel (h : ℝ) :
    s3Energy (shortProton h) - s3Energy (shortNeutron h) = -|h| := by
  simp only [s3Energy, Fin.sum_univ_six, s3Len, shortProton, shortNeutron]
  simp [abs_neg, abs_div]

/-- **In the short typed-crossing model the daughter proton has lower energy
    than the parent neutron**, for every `q > 1` with `h = q − q⁻¹`.
    Scope: this model only. PR #8682 measures the opposite sign in the
    11-letter typed model and equality on `V³`. -/
theorem beta_decay_energy_negative_shortModel (q : ℝ) (hq : 1 < q) :
    s3Energy (shortProton (q - q⁻¹)) < s3Energy (shortNeutron (q - q⁻¹)) := by
  have hpos : 0 < q - q⁻¹ := by
    have h0 : (0 : ℝ) < q := by linarith
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
    linarith
  have := beta_decay_energy_sub_shortModel (q - q⁻¹)
  rw [abs_of_pos hpos] at this
  linarith

/-- The sign is fixed by `h ≠ 0` alone; at `h = 0` (`q = 1`) the two
    energies are equal, so the strict inequality needs `q ≠ 1`. -/
theorem beta_decay_energy_eq_shortModel_at_h_zero :
    s3Energy (shortProton 0) = s3Energy (shortNeutron 0) := by
  have := beta_decay_energy_sub_shortModel 0
  simp at this
  linarith

/-- Top-level alias matching the manifest declaration. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
noncomputable def groebner_shirshov_energy (q : ℝ) (coeffs : List ℝ) : ℝ :=
  totalEnergyChange q coeffs

/-! ## Repaired form (option B, 2026-11-15)

The `.md` defines the energy on an element of `H_A(q)` written in the word
basis: `E(ξ) = Σ_w |c_w| · ℓ(w)`. With that definition:

* **Path independence is telescoping.** Along any reduction path
  `ξ₀ → ξ₁ → … → ξₘ` the step changes sum to `E(ξₘ) − E(ξ₀)`. By confluence
  every path ends at the same normal form, so the total change depends only on
  `ξ₀` (`energyPath_telescopes`).
* **The per-step formula in the `.md` is wrong.** A Hecke step on an isolated
  monomial `c·w`, with `w = u σᵢσᵢ v` of length `ℓ`, changes the energy by
  `|c|·(|h|(ℓ − 1) − 2)`, with `h = q − q⁻¹` (`heckeStep_energy_change`).
  The `.md` says `|c|·|h|`. At `ℓ = 2` and `|h| < 2` (true near `q₀ ≈ 1.11`,
  where `h ≈ 0.21`) the step *lowers* the energy, contradicting "every Hecke
  step increases the total weight". -/

/-- Energy of a linear combination of braid words: `Σ_w |c_w| · ℓ(w)`. -/
noncomputable def wordEnergy (x : List ℕ →₀ ℝ) : ℝ :=
  x.sum fun w c => |c| * w.length

/-- **Path independence (telescoping).** For any path of states, the sum of
    the step changes is the energy of the last state minus that of the first. -/
theorem energyPath_telescopes (x : List ℕ →₀ ℝ) :
    ∀ (path : List (List ℕ →₀ ℝ)),
      (((x :: path).zip path).map fun p => wordEnergy p.2 - wordEnergy p.1).sum
        = wordEnergy ((x :: path).getLast (List.cons_ne_nil _ _)) - wordEnergy x := by
  intro path
  induction path generalizing x with
  | nil => simp
  | cons y ys ih =>
    simp only [List.zip_cons_cons, List.map_cons, List.sum_cons]
    rw [ih y, List.getLast_cons (List.cons_ne_nil _ _)]
    ring

theorem wordEnergy_single (w : List ℕ) (c : ℝ) :
    wordEnergy (Finsupp.single w c) = |c| * w.length := by
  simp [wordEnergy, Finsupp.sum_single_index]

/-- **Energy change of one Hecke step** on an isolated monomial
    `c · u σᵢσᵢ v ↦ c h · u σᵢ v + c · u v`. -/
theorem heckeStep_energy_change (u v : List ℕ) (i : ℕ) (c h : ℝ) :
    wordEnergy (Finsupp.single (u ++ [i] ++ v) (c * h) + Finsupp.single (u ++ v) c)
      - wordEnergy (Finsupp.single (u ++ [i, i] ++ v) c)
      = |c| * (|h| * ((u ++ [i, i] ++ v).length - 1) - 2) := by
  have hne : u ++ [i] ++ v ≠ u ++ v := by
    intro he; have := congrArg List.length he; simp at this
  have hdisj : Disjoint (Finsupp.single (u ++ [i] ++ v) (c * h)).support
      (Finsupp.single (u ++ v) c).support := by
    rw [Finset.disjoint_left]
    intro a ha hb
    have h1 := Finsupp.support_single_subset ha
    have h2 := Finsupp.support_single_subset hb
    simp only [Finset.mem_singleton] at h1 h2
    exact hne (h1.symm.trans h2)
  rw [wordEnergy, Finsupp.sum_add_index_of_disjoint hdisj, ← wordEnergy,
    ← wordEnergy, wordEnergy_single, wordEnergy_single, wordEnergy_single, abs_mul]
  simp only [List.length_append, List.length_cons, List.length_nil]
  push_cast
  ring

/-- **The `.md` claim "every Hecke step increases the energy" is false.**
    On `σ₁σ₁` with `h = 1/5` the energy drops. -/
theorem heckeStep_can_lower_energy :
    wordEnergy (Finsupp.single [1] (1 * (1/5 : ℝ)) + Finsupp.single [] 1)
      < wordEnergy (Finsupp.single [1, 1] 1) := by
  have := heckeStep_energy_change [] [] 1 1 (1/5)
  simp only [List.nil_append, List.append_nil] at this
  norm_num at this
  linarith

end QOU.Archimedean
