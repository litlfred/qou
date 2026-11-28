/-
# The electron's categorical energy is `−log_q τ_e`, and CAL-1 then fixes the unit

Thread "Derive the electron's categorical weight" (2026-11-27). Algebraic half:
`QOU.Observations.ElectronWeightAdditivity`. Audit:
`docs/audits/2026-11-27-electron-categorical-weight.md`. Behind the transcendental boundary
because it uses `Real.log` and a limit.

**Premise (corpus, not new).** Energy is additive over non-interacting parts, and the
convention-D trace is multiplicative on disjoint strand sets (`SpectatorEnergyMap.trace_kron`).
The corpus already uses this premise to derive spectator invariance (`spectator_of_additive`).

**What follows.**

1. `additive_eq_log`: a continuous map `Φ` on positive trace values with `Φ(xy) = Φ x + Φ y`
   is `c·log`, with no additive constant (`Φ 1 = 0`: the empty diagram has energy `0`).
2. `cal1_unique`: if also `Φ(τ_e) = m_e` with `τ_e ≠ 1`, then `Φ x = m_e·log x / log τ_e` for every
   `x > 0`. `derived_map_additive` and `derived_map_cal1` show this map exists. So once additivity
   and CAL-1 are imposed there is no free unit and no "multiple of `E₀`" to choose.
3. `derived_dictionary_form`: in the `β = ln q` dictionary (`QOU.Thermo.energyOf`),
   `Φ y = m_e · 𝔈(y)/𝔈_e` with `𝔈(y) = −log_q y` and `𝔈_e = −log_q τ_e`. The `ln q` cancels.
   This is audit 2026-11-22 §2's `calMap` with the electron's categorical energy
   `𝔈_e = −log_q τ_e`, the dictionary's own rule applied to the electron.
4. `electron_energy_split`: `𝔈_e = −3 + 𝔈(y₍₃₎)`: the writhe, with the dictionary's sign, plus
   the energy of the one-row block.
5. `derived_unit_neg` and `derived_cell_pos`: on `1 < q ≤ 6/5` the derived per-nat unit is
   negative, so the n–p log cell puts the neutron above the proton (`log_cell_pos_iff`). The
   sign is a consequence, not an input.
6. `derived_unit_eq_mul_e0`: as a multiple of the quantum temperature `E₀ = m_e/(q(q−1))`, the
   per-nat unit is `q(q−1)/(−ln τ_e)`.
7. `derived_unit_classical_limit`: `1/(−ln τ_e) → 1/ln 2` as `q → 1`. Classically the electron's
   mass is `|c|·ln 2`, one bit at the derived temperature. `E₀` instead has a pole at `q = 1`.

No measured value enters. Numbers at `q₀` are in
`computations/probes/electron_weight/electron_log_weight_probe.py`.
-/
import QOU.Observations.ElectronWeightAdditivity
import QOU.Transcendental.Nuclear.SpectatorEnergyMap
import QOU.Transcendental.Core.QBetaEnergyDictionary

namespace QOU.Transcendental.MassTheory.ElectronCategoricalEnergy

open QOU.Observations.ElectronWeightAdditivity QOU.QBeta.SpectatorEnergyMap
open Filter Topology

/-- Energy additive over non-interacting parts, on positive trace values. -/
def AdditiveOnTraces (Φ : ℝ → ℝ) : Prop :=
  ∀ x y : ℝ, 0 < x → 0 < y → Φ (x * y) = Φ x + Φ y

/-- **Additivity and continuity force `Φ = c·log`, with no constant.** -/
theorem additive_eq_log (Φ : ℝ → ℝ) (hA : AdditiveOnTraces Φ) (hc : ContinuousOn Φ (Set.Ioi 0)) :
    ∃ c : ℝ, ∀ x : ℝ, 0 < x → Φ x = c * Real.log x := by
  obtain ⟨c, d, h⟩ := eq_log_of_spectatorInvariant Φ (spectator_of_additive Φ hA) hc
  have h1 : Φ 1 = 0 := by
    have := hA 1 1 one_pos one_pos
    rw [mul_one] at this
    linarith
  have hd : d = 0 := by
    have := h 1 one_pos
    rw [Real.log_one, mul_zero, zero_add] at this
    linarith
  exact ⟨c, fun x hx => by rw [h x hx, hd, add_zero]⟩

/-- **CAL-1 fixes the map uniquely.** -/
theorem cal1_unique (Φ : ℝ → ℝ) (hA : AdditiveOnTraces Φ) (hc : ContinuousOn Φ (Set.Ioi 0))
    (τ m : ℝ) (hτ : 0 < τ) (hτ1 : τ ≠ 1) (hcal : Φ τ = m) :
    ∀ x : ℝ, 0 < x → Φ x = m * Real.log x / Real.log τ := by
  obtain ⟨c, h⟩ := additive_eq_log Φ hA hc
  have hl : Real.log τ ≠ 0 := Real.log_ne_zero_of_pos_of_ne_one hτ hτ1
  have hcm : c = m / Real.log τ := by
    rw [h τ hτ] at hcal
    field_simp
    linarith
  intro x hx
  rw [h x hx, hcm]
  ring

/-- The derived map. -/
noncomputable def derivedMap (τ m : ℝ) (x : ℝ) : ℝ := m * Real.log x / Real.log τ

theorem derived_map_additive (τ m : ℝ) : AdditiveOnTraces (derivedMap τ m) := by
  intro x y hx hy
  unfold derivedMap
  rw [Real.log_mul hx.ne' hy.ne']
  ring

theorem derived_map_continuousOn (τ m : ℝ) : ContinuousOn (derivedMap τ m) (Set.Ioi 0) := by
  unfold derivedMap
  refine ContinuousOn.div_const (ContinuousOn.mul continuousOn_const ?_) _
  exact Real.continuousOn_log.mono (fun x hx => (ne_of_gt (Set.mem_Ioi.mp hx)))

theorem derived_map_cal1 (τ m : ℝ) (hτ : 0 < τ) (hτ1 : τ ≠ 1) : derivedMap τ m τ = m := by
  have hl : Real.log τ ≠ 0 := Real.log_ne_zero_of_pos_of_ne_one hτ hτ1
  unfold derivedMap
  field_simp

/-- **Dictionary form: `Φ y = m_e·𝔈(y)/𝔈_e`, the `ln q` cancels.** -/
theorem derived_dictionary_form (q τ m y : ℝ) (hq : 1 < q) :
    derivedMap τ m y = m * QOU.Thermo.energyOf (Real.log q) y /
      QOU.Thermo.energyOf (Real.log q) τ := by
  have hl : Real.log q ≠ 0 := (Real.log_pos hq).ne'
  unfold derivedMap QOU.Thermo.energyOf
  by_cases hτ : Real.log τ = 0
  · simp [hτ]
  · field_simp

/-- **The electron's categorical energy is the writhe plus the one-row block:**
`𝔈_e = −3 + 𝔈(y₍₃₎)`. -/
theorem electron_energy_split (q : ℝ) (hq : 1 < q) :
    QOU.Thermo.energyOf (Real.log q) (tauE q) =
      -3 + QOU.Thermo.energyOf (Real.log q) (QOU.QBeta.WeightSpaceMarkov.y3 q) := by
  have hq0 : 0 < q := by linarith
  have hl : Real.log q ≠ 0 := (Real.log_pos hq).ne'
  have hy : 0 < QOU.QBeta.WeightSpaceMarkov.y3 q := by
    have h := tauE_pos q hq0
    rw [tauE_eq_framing_mul_y3 q hq0.ne' (by positivity)] at h
    exact pos_of_mul_pos_right h (by positivity)
  rw [tauE_eq_framing_mul_y3 q hq0.ne' (by positivity)]
  unfold QOU.Thermo.energyOf
  rw [Real.log_mul (by positivity) hy.ne', Real.log_pow]
  field_simp
  push_cast
  ring

/-- **The derived per-nat unit is negative on `1 < q ≤ 6/5`.** -/
theorem derived_unit_neg (q m : ℝ) (hm : 0 < m) (h1 : 1 < q) (h2 : q ≤ 6 / 5) :
    m / Real.log (tauE q) < 0 := by
  have hτ := tauE_pos q (by linarith)
  have hτ1 := tauE_lt_one q h1.le h2
  exact div_neg_of_pos_of_neg hm (Real.log_neg hτ hτ1)

/-- **The derived chart puts the neutron above the proton** (n–p log cell, any word, trace and
normalisation). -/
theorem derived_cell_pos (q m t D : ℝ) (hm : 0 < m) (h1 : 1 < q) (h2 : q ≤ 6 / 5)
    (ht : 0 < t) (hD : 0 < D) :
    0 < derivedMap (tauE q) m (epsN q t D) - derivedMap (tauE q) m (epsP q t D) := by
  have key := (log_cell_pos_iff (m / Real.log (tauE q)) 0 q t D h1 ht hD).mpr
    (derived_unit_neg q m hm h1 h2)
  unfold derivedMap
  have e : ∀ x, m * Real.log x / Real.log (tauE q) = m / Real.log (tauE q) * Real.log x + 0 := by
    intro x; ring
  rw [e, e]
  exact key

/-- The n–p cell in the derived chart: `2·m_e·ln q/(−ln τ_e)`. -/
theorem derived_cell_eq (q m t D : ℝ) (hq : 1 < q) (ht : 0 < t) (hD : 0 < D) :
    derivedMap (tauE q) m (epsN q t D) - derivedMap (tauE q) m (epsP q t D) =
      2 * m * Real.log q / (-Real.log (tauE q)) := by
  have key := log_cell (m / Real.log (tauE q)) 0 q t D (by linarith) ht hD
  unfold derivedMap
  have e : ∀ x, m * Real.log x / Real.log (tauE q) = m / Real.log (tauE q) * Real.log x + 0 := by
    intro x; ring
  rw [e, e, key]
  by_cases hl : Real.log (tauE q) = 0
  · simp [hl]
  · field_simp

/-- **The derived per-nat unit as a multiple of `E₀`:** `1/(−ln τ_e) = E₀ · q(q−1)/(−ln τ_e)`. -/
theorem derived_unit_eq_mul_e0 (q : ℝ) (hq : 1 < q) :
    1 / (-Real.log (tauE q)) = e0 q * (q * (q - 1) / (-Real.log (tauE q))) := by
  have h0 : q ≠ 0 := by linarith
  have h1 : q - 1 ≠ 0 := by linarith
  unfold e0
  by_cases hl : Real.log (tauE q) = 0
  · simp [hl]
  · field_simp

/-- **Classical limit: `1/(−ln τ_e) → 1/ln 2` as `q → 1`.** -/
theorem derived_unit_classical_limit :
    Tendsto (fun q : ℝ => 1 / (-Real.log (tauE q))) (𝓝 1) (𝓝 (1 / Real.log 2)) := by
  have hcont : ContinuousAt (fun q : ℝ => tauE q) 1 := by
    unfold tauE
    refine ContinuousAt.div (by fun_prop) (by fun_prop) (by norm_num)
  have hτ : Tendsto (fun q : ℝ => tauE q) (𝓝 1) (𝓝 (1 / 2)) := by
    have := hcont.tendsto
    rwa [tauE_one] at this
  have hlog : Tendsto (fun q : ℝ => Real.log (tauE q)) (𝓝 1) (𝓝 (Real.log (1 / 2))) :=
    (Real.continuousAt_log (by norm_num)).tendsto.comp hτ
  have h2 : Real.log (1 / 2 : ℝ) = -Real.log 2 := by
    rw [one_div, Real.log_inv]
  rw [h2] at hlog
  have hne : (-(-Real.log 2)) ≠ 0 := by
    rw [neg_neg]; exact (Real.log_pos (by norm_num)).ne'
  have := (hlog.neg).inv₀ hne
  simpa [one_div, neg_neg] using this

end QOU.Transcendental.MassTheory.ElectronCategoricalEnergy
