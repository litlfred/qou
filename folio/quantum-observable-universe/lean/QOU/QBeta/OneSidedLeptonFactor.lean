import QOU.QBeta.FlavourWeightSplit
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Data.Real.Basic

/-!
# One-sided lepton factor under the nucleon rule: closed form, `q = 1` value, sign

Thread "Find where the n–p mass error comes from", 2026-11-21. Audit
`docs/audits/2026-11-21-qbeta-np-error-budget.md` §11. **Exploration requested by the owner
("explore both of the options"); NOT adopted** — the 2026-11-21 ruling is "not one-sided yet".

## Setting

* K-weight conservation for `n → p e⁻ ν̄`: `K(n) = q⁻¹`, `K(p) = q`, `K(e⁻) = q^{3−2b}` on the
  electron's three strands with `b` of them `d`, `K(ν̄) = q^{s}`. `kConservation_no_nubar`: there
  is no `b` without a `ν̄`; `kConservation_nubar_minus`: with `s = −1`, `b = 2` is forced.
* Nucleon rule (the rule already ruled for `ε`: `K`-weight × plain sector trace / `[2]ⁿ`): the
  electron `Δ = σ₀σ₁σ₀` on the `b = 2` sector has plain trace `q³` (probe), so its factor is
  `q⁻¹ q³ / [2]³`; the `ν̄` strand gives `q⁻¹/[2]`. Product `f = q/[2]⁴`.
* One-sided placement: the factor multiplies the final state only,
  `F = ε_n(V³) − ε_p(V³)·f`.

## What is proved

1. `fOneSided_eq`: `F = −(q²+q+1)·S(q)·P(q) / (q⁴ (q²+1)⁷)`,
   `S = q⁶ − 2q⁵ + 5q⁴ − 3q³ + 4q² − q + 1`.
2. `fOneSided_one`: `F(1) = 45/128` (order 0 at `q = 1`).
3. `fOneSided_pos`: `F > 0` on `1 < q ≤ 23/20`: the neutron side is the larger one, the sign the
   scored cell lacks under "mass ∝ trace".

## Not claimed

That `E₀·F` is `Q_β` or `m_n − m_p`: that is the reading the owner rules. No numerical value.
-/

namespace QOU.QBeta.OneSidedLeptonFactor

open QOU.QBeta.FlavourWeightSplit
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

/-- No electron sector conserves `K` without a `ν̄` strand. -/
theorem kConservation_no_nubar (b : ℤ) : (-1 : ℤ) ≠ 1 + (3 - 2 * b) := by omega

/-- With a `ν̄` of weight `q⁻¹`, `K` conservation forces `b = 2`. -/
theorem kConservation_nubar_minus (b : ℤ) : (-1 : ℤ) = 1 + (3 - 2 * b) + (-1) ↔ b = 2 := by
  omega

/-- With a `ν̄` of weight `q⁺¹`, `K` conservation forces `b = 3`. -/
theorem kConservation_nubar_plus (b : ℤ) : (-1 : ℤ) = 1 + (3 - 2 * b) + 1 ↔ b = 3 := by
  omega

section Generic

variable {R : Type*} [Field R]

/-- The nucleon-rule lepton factor `f = q/[2]⁴`. -/
def leptonFactor (q : R) : R := q / qd2 q ^ 4

/-- The one-sided functional `F = ε_n(V³) − ε_p(V³)·f`. -/
def fOneSided (q : R) : R :=
  epsN q (borromeanV3B q) - epsP q (borromeanV3A q) * leptonFactor q

/-- `S(q)`. -/
def polyS (q : R) : R := q ^ 6 - 2 * q ^ 5 + 5 * q ^ 4 - 3 * q ^ 3 + 4 * q ^ 2 - q + 1

/-- The closed form. -/
def fClosed (q : R) : R :=
  -(q ^ 2 + q + 1) * polyS q * polyP q / (q ^ 4 * (q ^ 2 + 1) ^ 7)

theorem fOneSided_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    fOneSided q = fClosed q := by
  unfold fOneSided leptonFactor epsN epsP fClosed polyS polyP qd2
  rw [trace_borromeanV3A q hq, trace_borromeanV3B q hq]
  have e2 : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp; try ring
  rw [e2]
  field_simp
  ring

end Generic

/-- `F(1) = 45/128`. -/
theorem fClosed_one : fClosed (1 : ℝ) = 45 / 128 := by
  unfold fClosed polyS polyP
  norm_num

/-- `S(q) > 0` for `q ≥ 1`. -/
theorem polyS_pos {q : ℝ} (hq : 1 ≤ q) : 0 < polyS q := by
  obtain ⟨t, ht, rfl⟩ : ∃ t : ℝ, 0 ≤ t ∧ q = 1 + t := ⟨q - 1, by linarith, by ring⟩
  unfold polyS
  have key : (1 + t) ^ 6 - 2 * (1 + t) ^ 5 + 5 * (1 + t) ^ 4 - 3 * (1 + t) ^ 3
      + 4 * (1 + t) ^ 2 - (1 + t) + 1
      = t ^ 6 + 4 * t ^ 5 + 10 * t ^ 4 + 17 * t ^ 3 + 20 * t ^ 2 + 14 * t + 5 := by ring
  rw [key]
  positivity

/-- **The one-sided functional is positive on the selection range: neutron side larger.** -/
theorem fOneSided_pos {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) : 0 < fOneSided q := by
  rw [fOneSided_eq q (by positivity) (by positivity)]
  unfold fClosed
  have hP := polyP_neg hq1 hq2
  have hS := polyS_pos hq1.le
  have hA : 0 < q ^ 2 + q + 1 := by positivity
  apply div_pos
  · have : 0 < (q ^ 2 + q + 1) * polyS q * -polyP q := by
      apply mul_pos (mul_pos hA hS); linarith
    linarith [show -(q ^ 2 + q + 1) * polyS q * polyP q
      = (q ^ 2 + q + 1) * polyS q * -polyP q by ring]
  · positivity

end QOU.QBeta.OneSidedLeptonFactor
