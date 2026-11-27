/-
# A trace weight cannot be a linear mass weight: the electron's weight is additive

Thread "Derive the electron's categorical weight" (2026-11-27). Companions
`QOU.Observations.ElectronUnitSplit` (the two electron units `ℏ_q²` and `τ_e`),
`QOU.QBeta.SpectatorEnergyMap` (additivity ⇒ spectator invariance) and the transcendental half
`QOU.Transcendental.MassTheory.ElectronCategoricalEnergy` (additivity + continuity ⇒ log).
Audit: `docs/audits/2026-11-27-electron-categorical-weight.md`.

The corpus carries two electron weights for a *linear* chart `m(X) = Λ·w(X)`: the mass-formula
`ℏ_q²` (placed by hand, `ElectronUnitSplit.product_weight_ne`) and the trace
`τ_e = q³(q⁴+1)/(q²+1)²` (derived). This file shows that the trace cannot be used linearly.

* The convention-D trace is multiplicative on disjoint strand sets
  (`SpectatorEnergyMap.trace_kron`): two non-interacting electrons have trace `τ_e²`.
* Masses of non-interacting parts add: the pair has mass `2 m_e`.
* `linear_chart_additive_iff`: `Λ·t² = 2·Λ·t` with `Λ, t ≠ 0` holds iff `t = 2`.
* `tauE_lt_one`: `τ_e < 1` on `1 ≤ q ≤ 6/5`, so there `τ_e ≠ 2`
  (`linear_trace_chart_not_additive`). The real root of `τ_e = 1` is near `q = 1.2414`, and of
  `τ_e = 2` near `q = 1.5135` (probe); neither is used.

So a linear chart in the trace is not additive, and the mass-formula weight `ℏ_q²` is not given
by any rule. The additive weight is a logarithm of the trace; that half needs `Real.log` and is in
`QOU/Transcendental/`. Here everything is over an ordered field and no measured value enters.
-/
import QOU.Nuclear.E0WeightCandidates

namespace QOU.Observations.ElectronWeightAdditivity

open QOU.QBeta.WeightSpaceMarkov QOU.QBeta.E0WeightCandidates

/-- The electron's convention-D trace, `τ_e = q³(q⁴+1)/(q²+1)²`. -/
def tauE {R : Type*} [Field R] (q : R) : R := q ^ 3 * (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2

/-- `tauE` is the convention-D trace of the ruled electron word `σ₀σ₁σ₀`. -/
theorem tauE_eq_trace {R : Type*} [Field R] (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    tauD3 q (q ^ 3) (r21a q * r21b q * r21a q) = tauE q :=
  tau_electron q hq hq2

/-- `tauE = q³·y₍₃₎`: framing (writhe 3) times the one-row Ocneanu weight. -/
theorem tauE_eq_framing_mul_y3 {R : Type*} [Field R] (q : R) (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) : tauE q = q ^ 3 * y3 q := by
  have hs : q + q⁻¹ ≠ 0 := by
    intro h; apply hq2; field_simp at h; linear_combination h
  unfold tauE y3
  field_simp
  ring

/-- Classical value `τ_e(1) = 1/2` (`2^{c−n}`, `c = 2`, `n = 3`). -/
theorem tauE_one {R : Type*} [Field R] [CharZero R] : tauE (1 : R) = 1 / 2 := by
  unfold tauE; norm_num

/-- **A linear chart is additive on a pair exactly when the weight is `2`.** -/
theorem linear_chart_additive_iff {R : Type*} [Field R] (Λ t : R) (hΛ : Λ ≠ 0) (ht : t ≠ 0) :
    Λ * (t * t) = Λ * t + Λ * t ↔ t = 2 := by
  constructor
  · intro h
    have h' : Λ * t * (t - 2) = 0 := by linear_combination h
    rcases mul_eq_zero.mp h' with h1 | h1
    · exact absurd h1 (mul_ne_zero hΛ ht)
    · linear_combination h1
  · intro h; subst h; ring

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

theorem tauE_pos (q : R) (hq : 0 < q) : 0 < tauE q := by
  unfold tauE; positivity

/-- **`τ_e < 1` on `1 ≤ q ≤ 6/5`.** With `q = 1 + t`,
`(q²+1)² − q³(q⁴+1) = 2 − 2t − 16t² − 32t³ − 34t⁴ − 21t⁵ − 7t⁶ − t⁷`. -/
theorem tauE_lt_one (q : R) (h1 : 1 ≤ q) (h2 : q ≤ 6 / 5) : tauE q < 1 := by
  have hq : 0 < q := by linarith
  have hd : 0 < (q ^ 2 + 1) ^ 2 := by positivity
  unfold tauE
  rw [div_lt_one hd]
  obtain ⟨t, rfl⟩ : ∃ t, q = 1 + t := ⟨q - 1, by ring⟩
  have ht0 : 0 ≤ t := by linarith
  have ht5 : t ≤ 1 / 5 := by linarith
  have p2 : t ^ 2 ≤ t / 5 := by nlinarith
  have p3 : t ^ 3 ≤ t / 25 := by nlinarith [pow_nonneg ht0 2]
  have p4 : t ^ 4 ≤ t / 125 := by nlinarith [pow_nonneg ht0 3]
  have p5 : t ^ 5 ≤ t / 625 := by nlinarith [pow_nonneg ht0 4]
  have p6 : t ^ 6 ≤ t / 3125 := by nlinarith [pow_nonneg ht0 5]
  have p7 : t ^ 7 ≤ t / 15625 := by nlinarith [pow_nonneg ht0 6]
  have key : 1 * ((1 + t) ^ 2 + 1) ^ 2 - (1 + t) ^ 3 * ((1 + t) ^ 4 + 1) =
      2 - 2 * t - 16 * t ^ 2 - 32 * t ^ 3 - 34 * t ^ 4 - 21 * t ^ 5 - 7 * t ^ 6 - t ^ 7 := by
    ring
  linarith

/-- **The linear trace chart is not additive.** On `1 ≤ q ≤ 6/5`, for every non-zero unit `Λ`,
two disjoint electrons (trace `τ_e²`) do not get twice the electron's value. -/
theorem linear_trace_chart_not_additive (Λ q : R) (hΛ : Λ ≠ 0) (h1 : 1 ≤ q) (h2 : q ≤ 6 / 5) :
    Λ * (tauE q * tauE q) ≠ Λ * tauE q + Λ * tauE q := by
  rw [Ne, linear_chart_additive_iff Λ _ hΛ (tauE_pos q (by linarith)).ne']
  have := tauE_lt_one q h1 h2
  intro h; rw [h] at this; norm_num at this

end QOU.Observations.ElectronWeightAdditivity
