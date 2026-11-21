import QOU.QBeta.FlavourWeightSplit
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Data.Real.Basic

/-!
# Error budget of the scored `Q_β`: the whole cell is `m_e · R(q)` with `R(1) = 3/4`

Thread "Find where the n–p mass error comes from", 2026-11-21. Audit:
`docs/audits/2026-11-21-qbeta-np-error-budget.md`. Probe:
`computations/probes/qbeta_error_budget/qbeta_error_budget_probe.py`.

## The cell being audited

Owner ruling 2026-11-20 (D1 = A, D2 = Q_β): the scored `Q_β` is
`E₀^full · |ε_flavour(V³)|`, with `ε_flavour` the `T³`-split of the convention-D quantum trace
(`FlavourWeightSplit`) and `E₀^full = m_e / (q(q−1)) / (1 − ℏ_q²)`, `ℏ_q = 1 − q⁻¹`
(`computations/qbeta/qbeta_e0.py`, `canonical`). Then `m_n − m_p = Q_β + m_e` is kinematics.
Here every quantity is divided by `m_e`, so no dimensionful number and no empirical value appears.

## What is proved

1. `e0_mul_h`: `(1/(q(q−1)))·(q − q⁻¹) = (q+1)/q²`. The `1/h`-size scale `E₀` and the `h`-size
   flavour split cancel. So the pin `q₀` and the form of `E₀` enter `Q_β` only through an `O(1)`
   rational function of `q`, not through a large lever.
2. `qbetaOverMe_eq`: the scored cell divided by `m_e` is the single rational function
   `R(q) = −(q+1)·P(q) / (q³ (2q−1) (q²+1)³)`, `P` the polynomial of `FlavourWeightSplit`.
3. `rClosed_one`: `R(1) = 3/4`. In the `q → 1` limit the cell is `2 · 3 · (1/8)`: the `2` is
   `lim (q−q⁻¹)/(q−1)`, the `3` is the trace of `V³|_{q=1} = id` on the 3-dim weight space
   (`tau_V3_one`), the `1/8` is the global `[2]³` normalisation.
4. `rClosed_le_three_quarters`: `R(q) ≤ 3/4` for **every** real `q ≥ 1`. The proof writes
   `3/4 − R(q) = (q−1)·N(q) / (4 q³ (2q−1)(q²+1)³)` and `N(1+t)` has only positive coefficients.

## What this means (scope (b), invariant: the inequality in item 4)

Within this functional — the `T³` split of the `[2]³`-normalised trace of `V³`, times the
tower-summed `E₀` — no value of the pin, no `E₀` tower truncation and no other `q` can give
`Q_β > (3/4)·m_e`. The missing factor is therefore not a `q`-correction: at least the factor
`(Q_β^target/m_e)/(3/4)` has to come from a link that survives `q → 1` (the counting `3/8`, the
`2`, or the identification of the cell with `Q_β`). The comparison number itself is in the audit,
not here.

## What is NOT claimed

* Nothing about which link is wrong. This file bounds the cell; it does not repair it.
* That `E₀` or the tower series are derived. `E₀`'s form is `rem:energy-scale-planck`; the tower
  factor `1/(1−ℏ_q²)` is canonical by ruling, its series open (bean `qou-y3bm`).
-/

namespace QOU.QBeta.QBetaErrorBudget

open QOU.QBeta.FlavourWeightSplit
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

section Generic

variable {R : Type*} [Field R]

/-- `E₀^full / m_e = 1/(q(q−1)) / (1 − ℏ_q²)`, `ℏ_q = 1 − q⁻¹` (`qbeta_e0.tower_summed`). -/
def e0TowerOverMe (q : R) : R := 1 / (q * (q - 1)) / (1 - (1 - q⁻¹) ^ 2)

/-- The scored cell divided by `m_e`: `E₀^full/m_e · |ε_flavour(V³)|`, with the sign of
`ε_flavour(V³) < 0` on the physical range (`epsFlavour_V3_neg`) written out. -/
def qbetaOverMe (q : R) : R := e0TowerOverMe q * -(epsFlavourV3 q)

/-- The closed form `R(q)`. -/
def rClosed (q : R) : R := -(q + 1) * polyP q / (q ^ 3 * (2 * q - 1) * (q ^ 2 + 1) ^ 3)

/-- **The `1/h` of `E₀` cancels the `h` of the flavour split.** -/
theorem e0_mul_h (q : R) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    1 / (q * (q - 1)) * (q - q⁻¹) = (q + 1) / q ^ 2 := by
  field_simp
  ring

/-- **The scored `Q_β / m_e` is one rational function of `q`.** -/
theorem qbetaOverMe_eq (q : R) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) (h2 : 2 * q - 1 ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) : qbetaOverMe q = rClosed q := by
  unfold qbetaOverMe e0TowerOverMe rClosed
  rw [epsFlavour_V3_eq q hq hq2]
  unfold fV3
  have hT : 1 - (1 - q⁻¹) ^ 2 = (2 * q - 1) / q ^ 2 := by field_simp; ring
  rw [hT]
  have hq1' : q ^ 2 - 1 = (q - 1) * (q + 1) := by ring
  rw [hq1']
  field_simp

/-- **The weight-space trace of `V³` at `q = 1` is `3`** (`V³|_{q=1}` is the identity of `S₃`). -/
theorem tau_V3_one :
    -((1 : R) ^ 12 - 3 * 1 ^ 10 + 3 * 1 ^ 8 - 5 * 1 ^ 6 + 3 * 1 ^ 4 - 3 * 1 ^ 2 + 1) / 1 ^ 6
      = 3 := by
  norm_num

/-- **Classical limit: `R(1) = 3/4 = 2 · 3 · (1/8)`.** -/
theorem rClosed_one : rClosed (1 : R) = 3 / 4 := by
  unfold rClosed polyP
  norm_num
  -- generic field: `6 / 8 = 3 / 4` holds in every characteristic (both sides `0` in char 2)
  rcases eq_or_ne (2 : R) 0 with h2 | h2
  · rw [show (8 : R) = 2 * 4 by norm_num, show (4 : R) = 2 * 2 by norm_num, h2]
    simp
  · rw [show (6 : R) = 2 * 3 by norm_num, show (8 : R) = 2 * 4 by norm_num,
      mul_div_mul_left _ _ h2]

end Generic

/-! ## Archimedean: the bound holds for every pin -/

/-- **`R(q) ≤ 3/4` for every real `q ≥ 1`.** -/
theorem rClosed_le_three_quarters {q : ℝ} (hq : 1 ≤ q) : rClosed q ≤ 3 / 4 := by
  obtain ⟨t, ht, rfl⟩ : ∃ t : ℝ, 0 ≤ t ∧ q = 1 + t := ⟨q - 1, by linarith, by ring⟩
  have hden : 0 < (1 + t) ^ 3 * (2 * (1 + t) - 1) * ((1 + t) ^ 2 + 1) ^ 3 := by
    have : 0 < 2 * (1 + t) - 1 := by linarith
    positivity
  unfold rClosed polyP
  rw [div_le_iff₀ hden]
  have key : 3 / 4 * ((1 + t) ^ 3 * (2 * (1 + t) - 1) * ((1 + t) ^ 2 + 1) ^ 3)
      - (-((1 + t) + 1) * ((1 + t) ^ 12 - 3 * (1 + t) ^ 10 + 3 * (1 + t) ^ 8
          - 5 * (1 + t) ^ 6 + 3 * (1 + t) ^ 4 - 3 * (1 + t) ^ 2 + 1))
      = t * (4 * t ^ 12 + 56 * t ^ 11 + 348 * t ^ 10 + 1270 * t ^ 9 + 3029 * t ^ 8
          + 4989 * t ^ 7 + 5887 * t ^ 6 + 5147 * t ^ 5 + 3456 * t ^ 4 + 1842 * t ^ 3
          + 792 * t ^ 2 + 252 * t + 36) / 4 := by
    ring
  have hpos : 0 ≤ t * (4 * t ^ 12 + 56 * t ^ 11 + 348 * t ^ 10 + 1270 * t ^ 9 + 3029 * t ^ 8
          + 4989 * t ^ 7 + 5887 * t ^ 6 + 5147 * t ^ 5 + 3456 * t ^ 4 + 1842 * t ^ 3
          + 792 * t ^ 2 + 252 * t + 36) / 4 := by positivity
  linarith

/-- **The scored `Q_β/m_e` is at most `3/4` for every pin `q > 1`.** -/
theorem qbetaOverMe_le_three_quarters {q : ℝ} (hq : 1 < q) : qbetaOverMe q ≤ 3 / 4 := by
  rw [qbetaOverMe_eq q (by positivity) (by linarith) (by linarith) (by positivity)]
  exact rClosed_le_three_quarters hq.le

/-! ## Interaction functionals: only first order in `q − 1` survives at `q = 1` -/

section Interaction

variable {R : Type*} [Field R]

/-- **`E₀^full · (q − 1) = q/(2q − 1)`.** So for any functional `F = (q−1)·G`,
`E₀^full · F / m_e = G · q/(2q−1)`, whose `q = 1` value is `G(1)`: the `q = 1` coefficient of
`Q_β/m_e = E₀^full·F/m_e` is the first-order coefficient of `F` at `q = 1`. -/
theorem e0Tower_mul_sub_one (q : R) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) (h2 : 2 * q - 1 ≠ 0) :
    e0TowerOverMe q * (q - 1) = q / (2 * q - 1) := by
  unfold e0TowerOverMe
  have hT : 1 - (1 - q⁻¹) ^ 2 = (2 * q - 1) / q ^ 2 := by field_simp; ring
  rw [hT]
  field_simp

/-- **A functional of order `≥ 2` at `q = 1` has zero `q = 1` coefficient.** If
`F = (q − 1)²·G` then `E₀^full·F = (q − 1)·q·G/(2q − 1)`, which carries a factor `q − 1`. Every
one-term cross term `C₁(X)` on record (67 of them, probe `qbeta_interaction_q1`) has this form. -/
theorem e0Tower_mul_order_two (q G : R) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) (h2 : 2 * q - 1 ≠ 0) :
    e0TowerOverMe q * ((q - 1) ^ 2 * G) = (q - 1) * (q * G / (2 * q - 1)) := by
  have := e0Tower_mul_sub_one q hq hq1 h2
  calc e0TowerOverMe q * ((q - 1) ^ 2 * G)
      = (e0TowerOverMe q * (q - 1)) * ((q - 1) * G) := by ring
    _ = (q - 1) * (q * G / (2 * q - 1)) := by rw [this]; ring

end Interaction

end QOU.QBeta.QBetaErrorBudget
