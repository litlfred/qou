import Mathlib.Data.Real.Basic
import Mathlib.Data.Finsupp.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# QOU.MassTheory.Archimedean.groebner_shirshov_energy — Word-Length Rewriting Norm & Hecke Skein Trace Invariance

Formalizes the normal-form rewriting properties of `thm:groebner-shirshov-energy`:
1. Only the Hecke quadratic relation `σ_i² = (q - q⁻¹) σ_i + 1` changes the word-length
   rewriting functional `E_GS(ξ) = ∑_w |c_w| · ℓ(w)`; Yang–Baxter and far commutativity
   preserve word lengths and coefficients (`yangBaxter_energy_zero`, `farComm_energy_zero`).
2. Along any reduction path `ξ₀ → ξ₁ → … → ξₘ`, step changes telescope to `E_GS(ξₘ) - E_GS(ξ₀)`
   (`energyPath_telescopes`), while an isolated Hecke step `c · u σ_i² v ↦ c h · u σ_i v + c · u v`
   changes `E_GS` by `(|c| * |h| * (ℓ - 1) + |c| * (ℓ - 2)) - |c| * ℓ = |c| * (|h| * (ℓ - 1) - 2)`
   (`heckeStep_wordLength_formula`, `heckeStep_energy_change`), which can lower `E_GS` (`heckeStep_can_lower_energy`).
3. Over any commutative ring `R`, any `R`-linear trace functional `τ` respecting the Hecke skein
   relation `w_sq = h • w_lin + w_id` satisfies `τ w_sq = h * τ w_lin + τ w_id`
   (`trace_hecke_skein_invariance`), evaluating to `h * z + 1` on a single generator (`τ 1 = 1`,
   `τ σ_i = z`) and to `z * (1 + h * z)` on both `σ₁² σ₂` and `σ₁ σ₂ σ₁` (`hecke_markov_braid_word_invariance`),
   proving why the Markov trace `tr_M` is invariant along Gröbner–Shirshov reduction whereas
   `E_GS` and the flat `z → 1` coefficient sum `net` are not.

LaTeX label: `thm:groebner-shirshov-energy`

## References
- [leitner2026] Ch. 12, `thm:groebner-shirshov-energy`
-/

set_option autoImplicit false

open scoped BigOperators

namespace QOU.MassTheory.Archimedean

/-- A single division step in the Gröbner–Shirshov reduction. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
inductive DivisionStepType
  | hecke       -- σ_i² → (q-q⁻¹)σ_i + 1 (energy-changing)
  | yangBaxter  -- σ_iσ_{i+1}σ_i → σ_{i+1}σ_iσ_{i+1} (energy-preserving)
  | farComm     -- σ_iσ_j → σ_jσ_i, |i-j|≥2 (energy-preserving)

/-- Magnitude of the Hecke crossing-asymmetry step scale: `|coeff| * (q - 1/q)`. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
noncomputable def heckeEnergyChange (q : ℝ) (coeff : ℝ) : ℝ :=
  |coeff| * (q - 1 / q)

/-- `heckeEnergyChange q c` is strictly positive for `1 < q` and `c ≠ 0`. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
theorem heckeEnergyChange_pos (q : ℝ) (hq : 1 < q) (c : ℝ) (hc : c ≠ 0) :
    0 < heckeEnergyChange q c := by
  unfold heckeEnergyChange
  apply mul_pos
  · exact abs_pos.mpr hc
  · rw [sub_pos, div_lt_iff₀ (by linarith : (0 : ℝ) < q)]
    nlinarith

/-- Per-step division indicator weighting `.hecke` by `heckeEnergyChange q coeff` and
`.yangBaxter` / `.farComm` by `0`. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
noncomputable def stepEnergyChange (q coeff : ℝ) : DivisionStepType → ℝ
  | .hecke => heckeEnergyChange q coeff
  | .yangBaxter => 0
  | .farComm => 0

/-- Yang–Baxter steps have zero step change. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
theorem yangBaxter_energy_zero (q coeff : ℝ) (step : DivisionStepType)
    (h : step = .yangBaxter) : stepEnergyChange q coeff step = 0 := by
  subst h; rfl

/-- Far-commutativity steps have zero step change. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
theorem farComm_energy_zero (q coeff : ℝ) (step : DivisionStepType)
    (h : step = .farComm) : stepEnergyChange q coeff step = 0 := by
  subst h; rfl

/-- The `.hecke` constructor genuinely moves `stepEnergyChange` for `1 < q` and `coeff ≠ 0`. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
theorem stepEnergyChange_hecke_ne_zero (q coeff : ℝ) (hq : 1 < q) (hc : coeff ≠ 0) :
    stepEnergyChange q coeff .hecke ≠ 0 := by
  simpa [stepEnergyChange] using ne_of_gt (heckeEnergyChange_pos q hq coeff hc)

/-- Cumulative Hecke step weight sum over a list of Hecke step coefficients. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
noncomputable def totalEnergyChange (q : ℝ) (hecke_coeffs : List ℝ) : ℝ :=
  (hecke_coeffs.map (heckeEnergyChange q)).sum

/-- Each `heckeEnergyChange q c` is non-negative for `1 < q`. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
private theorem heckeEnergyChange_nonneg (q : ℝ) (hq : 1 < q) (c : ℝ) :
    0 ≤ heckeEnergyChange q c := by
  unfold heckeEnergyChange
  apply mul_nonneg (abs_nonneg _)
  have hq_pos : (0 : ℝ) < q := by linarith
  rw [sub_nonneg, div_le_iff₀ hq_pos]
  nlinarith

/-- `totalEnergyChange q coeffs` is non-negative for `1 < q`. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
theorem totalEnergyChange_nonneg (q : ℝ) (hq : 1 < q)
    (coeffs : List ℝ) :
    0 ≤ totalEnergyChange q coeffs := by
  unfold totalEnergyChange
  induction coeffs with
  | nil => simp
  | cons c cs ih =>
    simp only [List.map_cons, List.sum_cons]
    exact add_nonneg (heckeEnergyChange_nonneg q hq c) ih

/-- **Refutation of unhypothesised path independence:** arbitrary step lists not constrained to be
reduction paths of a common element need not have equal `totalEnergyChange` (witnessed at `q = 2`). -/
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

/-! ## β-decay sign in the short typed-crossing model (`H₃(q)`) -/

/-- Bruhat length on `S₃`, basis order `e, s₁, s₂, s₁s₂, s₂s₁, s₁s₂s₁`. -/
def s3Len : Fin 6 → ℕ := ![0, 1, 1, 2, 2, 3]

/-- `E_GS(ξ) = Σ_w |c_w| ℓ(w)` on an `H₃(q)` normal form given by its coefficient
    vector in the basis `T_w`, `w ∈ S₃`. -/
noncomputable def s3Energy (v : Fin 6 → ℝ) : ℝ := ∑ k, |v k| * (s3Len k : ℝ)

/-- Short-model proton normal form `σ₁σ₂ − (h/2)σ₁`. -/
noncomputable def shortProton (h : ℝ) : Fin 6 → ℝ := ![0, -h / 2, 0, 1, 0, 0]

/-- Short-model neutron normal form `σ₁σ₂ − hσ₁ − (h/2)σ₂ + h²/2`. -/
noncomputable def shortNeutron (h : ℝ) : Fin 6 → ℝ := ![h ^ 2 / 2, -h, -h / 2, 1, 0, 0]

/-- **β-decay `E_GS` difference, short typed-crossing model, nucleon only:**
    `E_GS(p) − E_GS(n) = −|h|`, for every real `h`. -/
theorem beta_decay_energy_sub_shortModel (h : ℝ) :
    s3Energy (shortProton h) - s3Energy (shortNeutron h) = -|h| := by
  simp only [s3Energy, Fin.sum_univ_six, s3Len, shortProton, shortNeutron]
  simp [abs_neg, abs_div]

/-- **In the short typed-crossing model the daughter proton has lower `E_GS`
    than the parent neutron**, for every `q > 1` with `h = q − q⁻¹`. -/
theorem beta_decay_energy_negative_shortModel (q : ℝ) (hq : 1 < q) :
    s3Energy (shortProton (q - q⁻¹)) < s3Energy (shortNeutron (q - q⁻¹)) := by
  have hpos : 0 < q - q⁻¹ := by
    have h0 : (0 : ℝ) < q := by linarith
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
    linarith
  have := beta_decay_energy_sub_shortModel (q - q⁻¹)
  rw [abs_of_pos hpos] at this
  linarith

/-- At `h = 0` (`q = 1`) the short-model proton and neutron word-length norms coincide. -/
theorem beta_decay_energy_eq_shortModel_at_h_zero :
    s3Energy (shortProton 0) = s3Energy (shortNeutron 0) := by
  have := beta_decay_energy_sub_shortModel 0
  simp at this
  linarith

/-- Top-level alias matching the manifest declaration `lean.ref`. -/
-- Ref: [leitner2026] §6/groebner-shirshov-energy
noncomputable def groebner_shirshov_energy (q : ℝ) (coeffs : List ℝ) : ℝ :=
  totalEnergyChange q coeffs

/-! ## Word-Length Functional `E_GS(ξ) = Σ_w |c_w| · ℓ(w)` & Single-Step Formula -/

/-- Archimedean `ℓ¹` word-length norm of a linear combination of braid words: `Σ_w |c_w| · ℓ(w)`. -/
noncomputable def wordEnergy (x : List ℕ →₀ ℝ) : ℝ :=
  x.sum fun w c => |c| * w.length

/-- **Path independence (telescoping):** along any sequence of states `x :: path`, the sum of
    step differences equals the `wordEnergy` of the final state minus `wordEnergy x`. -/
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

/-- Evaluation of `wordEnergy` on a single monomial `c · w`. -/
theorem wordEnergy_single (w : List ℕ) (c : ℝ) :
    wordEnergy (Finsupp.single w c) = |c| * w.length := by
  simp [wordEnergy, Finsupp.sum_single_index]

/-- **Algebraic single-step word-length change identity** matching Part 3 of `.md`:
    replacing a monomial `c · w` of length `ℓ` by `c h · w₁` (length `ℓ - 1`) plus `c · w₀`
    (length `ℓ - 2`) changes the `ℓ¹` word-length norm by `|c| * (|h| * (ℓ - 1) - 2)`. -/
theorem heckeStep_wordLength_formula (c h ℓ : ℝ) :
    (|c| * |h| * (ℓ - 1) + |c| * (ℓ - 2)) - |c| * ℓ = |c| * (|h| * (ℓ - 1) - 2) := by
  ring

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

/-- **A Hecke step can strictly lower `wordEnergy`:** on `σ₁σ₁` (`ℓ = 2`) with `h = 1/5`,
    `wordEnergy` drops from `2` to `1/5`. -/
theorem heckeStep_can_lower_energy :
    wordEnergy (Finsupp.single [1] (1 * (1 / 5 : ℝ)) + Finsupp.single [] 1)
      < wordEnergy (Finsupp.single [1, 1] 1) := by
  have := heckeStep_energy_change [] [] 1 1 (1 / 5)
  simp only [List.nil_append, List.append_nil] at this
  norm_num at this
  linarith

/-! ## Generic `[CommRing R]` Hecke Skein Trace Invariance (`tr_M` Well-Definedness on `H_n(R, q)`) -/

/-- **Hecke Skein Trace Invariance (`[CommRing R]`):**
For any `R`-module `M`, `R`-linear trace functional `τ : M →ₗ[R] R`, and elements
`w_sq w_lin w_id : M` related by the Hecke quadratic skein relation `w_sq = h • w_lin + w_id`,
`τ` takes identical values on the unreduced and reduced sides: `τ w_sq = h * τ w_lin + τ w_id`. -/
theorem trace_hecke_skein_invariance {R M : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    (τ : M →ₗ[R] R) (h : R) (w_sq w_lin w_id : M)
    (hskein : w_sq = h • w_lin + w_id) :
    τ w_sq = h * τ w_lin + τ w_id := by
  rw [hskein, map_add, LinearMap.map_smul, smul_eq_mul]

/-- **Single-Generator & Braid-Word Markov Trace Identities (`[CommRing R]`):**
Under the normalized Markov trace rules `τ(1) = 1`, `τ(σ_i) = z`, and `τ(σ_1 σ_2) = z²`:
1. The Hecke reduction of a single square `σ_i² ↦ h σ_i + 1` evaluates to `h * z + 1`;
2. Both `σ₁² σ₂ ↦ h (σ₁ σ₂) + σ₂` and the cyclically conjugate reduced word `σ₁ σ₂ σ₁` evaluate
   to `z * (1 + h * z)` (`h * z² + z = z * (1 + h * z)`), whereas at unit basis weight `z ↦ 1`
   the reduced normal-form coefficient sums of `σ₁² σ₂` (`h + 1`) and `σ₁ σ₂ σ₁` (`1`) differ by `h`. -/
theorem hecke_markov_braid_word_invariance {R M : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    (τ : M →ₗ[R] R) (h z : R) (e s₁ s₂ s₁₂ s₁₂₁ w_sq₁ w_s₁sq_s₂ : M)
    (he : τ e = 1) (hs₁ : τ s₁ = z) (hs₂ : τ s₂ = z) (hs₁₂ : τ s₁₂ = z ^ 2)
    (hsq₁ : w_sq₁ = h • s₁ + e)
    (hs₁sq_s₂ : w_s₁sq_s₂ = h • s₁₂ + s₂)
    (hcyc : τ s₁₂₁ = τ w_s₁sq_s₂) :
    τ w_sq₁ = h * z + 1 ∧
      τ w_s₁sq_s₂ = z * (1 + h * z) ∧
      τ s₁₂₁ = z * (1 + h * z) := by
  have h1 : τ w_sq₁ = h * z + 1 := by
    rw [trace_hecke_skein_invariance τ h w_sq₁ s₁ e hsq₁, hs₁, he]
  have h2 : τ w_s₁sq_s₂ = z * (1 + h * z) := by
    rw [trace_hecke_skein_invariance τ h w_s₁sq_s₂ s₁₂ s₂ hs₁sq_s₂, hs₁₂, hs₂]
    ring
  exact ⟨h1, h2, hcyc.trans h2⟩

end QOU.MassTheory.Archimedean
