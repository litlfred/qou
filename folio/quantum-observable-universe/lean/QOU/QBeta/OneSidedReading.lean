import QOU.QBeta.OneSidedLeptonFactor

/-!
# Which energy is `E₀·F`? Under a linear energy map, neither `Q_β` nor `m_n − m_p`

Thread "Find where the n–p mass error comes from", 2026-11-21. Audit
`docs/audits/2026-11-21-qbeta-np-error-budget.md` §12. Owner ruling 2026-11-21: "not yet, derive
the reading" of the one-sided functional `F = ε_n(V³) − ε_p(V³)·f` (`OneSidedLeptonFactor`).

## Setting

The scored cell reads an energy off a trace linearly: `E(X) = E₀·ε(X)` with `E₀ > 0`. The
one-sided placement makes the final-state trace multiplicative, `ε(p e⁻ ν̄) = ε_p·f`. Under that
same map:

* `E(n) − E(p e⁻ ν̄) = E₀·F` (the `Q_β` reading),
* `E(p e⁻ ν̄) − E(p) = E₀·ε_p·(f − 1)` (the energy the map assigns to the lepton pair),
* `E(n) − E(p) = E₀·ε_flavour(V³)` (the `m_n − m_p` reading).

## What is proved (on `1 < q ≤ 23/20`)

1. `epsP_V3A_pos`: `ε_p(V³) > 0`.
2. `leptonFactor_lt_one`: `f < 1` (for every `q > 1`).
3. `leptonPair_neg`: `ε_p·f − ε_p < 0`. So the `Q_β` reading forces the lepton pair to carry
   **negative** energy under the same map, whereas `m_n − m_p = Q_β + m_e (+ E_ν̄)` needs it
   positive. The `Q_β` reading is not consistent with the map it uses.
4. `fOneSided_eq_flavour_add`: `F = ε_flavour + ε_p·(1 − f)`.
5. `fOneSided_ne_flavour`: `F > 0 > ε_flavour`, so `E₀·F ≠ E(n) − E(p)`. The `m_n − m_p` reading
   contradicts the same map applied to the two nucleons.

## Scope

Scope (a): this excludes the two readings **under a linear, sign-preserving energy map** with
multiplicative traces. It does not exclude a different energy map (e.g. a logarithmic one, which
the probe evaluates and which gives no `m_e` either). No numerical value is used.
-/

namespace QOU.QBeta.OneSidedReading

open QOU.QBeta.FlavourWeightSplit
open QOU.QBeta.OneSidedLeptonFactor
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

section Generic

variable {R : Type*} [Field R]

/-- **`F = ε_flavour + ε_p·(1 − f)`.** -/
theorem fOneSided_eq_flavour_add (q : R) :
    fOneSided q = epsFlavourV3 q + epsP q (borromeanV3A q) * (1 - leptonFactor q) := by
  unfold fOneSided epsFlavourV3
  ring

end Generic

/-- `ε_p(V³) > 0` on the selection range. -/
theorem epsP_V3A_pos {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) :
    0 < epsP q (borromeanV3A q) := by
  have hq : q ≠ 0 := by positivity
  unfold epsP
  rw [trace_borromeanV3A q hq]
  have hP := polyP_neg hq1 hq2
  unfold polyP at hP
  have hd : 0 < qd2 q := by unfold qd2; positivity
  apply div_pos _ (by positivity)
  apply mul_pos (by positivity)
  apply div_pos (by linarith) (by positivity)

/-- `f = q/[2]⁴ < 1` for `q > 1`. -/
theorem leptonFactor_lt_one {q : ℝ} (hq1 : 1 < q) : leptonFactor q < 1 := by
  unfold leptonFactor qd2
  have hq0 : 0 < q := by linarith
  have hgt : q < q + q⁻¹ := by have := inv_pos.mpr hq0; linarith
  have h4 : q ^ 4 < (q + q⁻¹) ^ 4 := by
    apply pow_lt_pow_left₀ hgt hq0.le (by norm_num)
  have hq4 : q ≤ q ^ 4 := by
    have : 1 ≤ q ^ 3 := one_le_pow₀ hq1.le
    nlinarith
  rw [div_lt_one (by positivity)]
  linarith

/-- **The `Q_β` reading assigns the lepton pair negative energy under the same map.** -/
theorem leptonPair_neg {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) :
    epsP q (borromeanV3A q) * leptonFactor q - epsP q (borromeanV3A q) < 0 := by
  have h1 := epsP_V3A_pos hq1 hq2
  have h2 := leptonFactor_lt_one hq1
  nlinarith

/-- **`F` and `ε_flavour` have opposite signs, so `E₀·F ≠ E(n) − E(p)`.** -/
theorem fOneSided_ne_flavour {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) :
    epsFlavourV3 q < 0 ∧ 0 < fOneSided q ∧ fOneSided q ≠ epsFlavourV3 q := by
  have a := epsFlavour_V3_neg hq1 hq2
  have b := fOneSided_pos hq1 hq2
  exact ⟨a, b, by intro h; linarith⟩

end QOU.QBeta.OneSidedReading
