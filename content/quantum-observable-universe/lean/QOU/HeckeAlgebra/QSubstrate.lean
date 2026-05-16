import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic
import QOU.HeckeAlgebra.Common

/-!
# QOU.HeckeAlgebra.QSubstrate — q_0 specialisation

The QOU substrate parameter `q_0 ≈ 1.10998` is the unique
positive real root of the equation `m_μ / m_e = 206.7682830`
under the categorical mass-ratio formula (per
`def:m-mu-over-m-e-calibration`).

## What this module provides

- `q_0 : ℝ` — the QOU substrate parameter, axiomatised at this
  abstraction level (Mathlib doesn't have the categorical-
  derivation Lean infra to compute it from first principles
  yet; the Python compute layer derives the 50-dps value).
- `c_q : ℝ` — speed of light in cat units, `c_q = 1 / (q_0 - 1)`.
- `hbar_q : ℝ` — Planck constant in cat units, `(q_0 - 1) / q_0`.
- `markovParameter : ℝ` — `z = 1 / (q_0^{1/2} + q_0^{-1/2})`.
- `eta_q : ℝ` — operational entropy, `(2q_0 - 1) / q_0³`.

## Categorical content

These are the derived constants that appear throughout the QOU
manuscript and feed downstream computations.  They are
axiomatised here at the Lean level (concrete value derivation
lives in `folio-assistant/computations/q_parameter.py`).

The 50-dps decimal expansion `q_0 ≈ 1.1099785955541805…` is
checked-in as a witness; the Lean axiom is just a positive-real-
number existence claim.

## References

- [manuscript] `def:m-mu-over-m-e-calibration` — the equation
  defining `q_0` from the lepton mass ratio
- `folio-assistant/computations/q_parameter.py` — the 50-dps
  Python derivation
- `Q_50_DIGIT_STR` — the 50-decimal-digit literal
-/

namespace QOU.HeckeAlgebra.QSubstrate

/-- **The QOU substrate parameter** `q_0`.  Axiomatised as a real
    number greater than 1 (per the categorical derivation in
    `def:m-mu-over-m-e-calibration`); concrete 50-dps value lives
    in `folio-assistant/computations/q_parameter.py`. -/
axiom q_0 : ℝ

/-- `q_0 > 1` (categorical-derivation property). -/
axiom q_0_gt_one : 1 < q_0

/-- `q_0 ≠ 0` (immediate from `q_0 > 1`). -/
theorem q_0_ne_zero : q_0 ≠ 0 :=
  ne_of_gt (lt_trans one_pos q_0_gt_one)

/-- `q_0 - 1 > 0`. -/
theorem q_0_sub_one_pos : 0 < q_0 - 1 :=
  sub_pos.mpr q_0_gt_one

/-- **Speed of light in cat units**: `c_q := 1 / (q_0 - 1)`. -/
def c_q : ℝ := 1 / (q_0 - 1)

/-- `c_q > 0`. -/
theorem c_q_pos : 0 < c_q := by
  unfold c_q
  exact div_pos one_pos q_0_sub_one_pos

/-- **Planck constant in cat units**: `ℏ_q := (q_0 - 1) / q_0`. -/
def hbar_q : ℝ := (q_0 - 1) / q_0

/-- `ℏ_q > 0`. -/
theorem hbar_q_pos : 0 < hbar_q := by
  unfold hbar_q
  exact div_pos q_0_sub_one_pos (lt_trans one_pos q_0_gt_one)

/-- `c_q · ℏ_q = 1 / q_0`.  Identity `(1 / (q_0 - 1)) · ((q_0 - 1) /
    q_0) = 1 / q_0`. -/
theorem c_q_mul_hbar_q : c_q * hbar_q = 1 / q_0 := by
  unfold c_q hbar_q
  field_simp

/-- **Markov parameter**: `z := 1 / (q_0^{1/2} + q_0^{-1/2})`.  This
    is the eigenvalue of the Markov-trace stabilisation operator
    (per `prop:markov-trace-axioms`). -/
noncomputable def markovParameter : ℝ :=
  1 / (q_0 ^ ((1 : ℝ) / 2) + q_0 ^ (-(1 : ℝ) / 2))

/-- `√q_0 > 0` (immediate from `q_0 > 0`). -/
theorem q_0_sqrt_pos : 0 < q_0 ^ ((1 : ℝ) / 2) := by
  apply Real.rpow_pos_of_pos
  exact lt_trans one_pos q_0_gt_one

/-- **Operational entropy**: `η_q := (2q_0 - 1) / q_0^3`. -/
def eta_q : ℝ := (2 * q_0 - 1) / q_0 ^ 3

/-- `η_q > 0` for `q_0 > 1/2` (in particular for our `q_0 > 1`). -/
theorem eta_q_pos : 0 < eta_q := by
  unfold eta_q
  apply div_pos
  · linarith [q_0_gt_one]
  · exact pow_pos (lt_trans one_pos q_0_gt_one) 3

end QOU.HeckeAlgebra.QSubstrate
