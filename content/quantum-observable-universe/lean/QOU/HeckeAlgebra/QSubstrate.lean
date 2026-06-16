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
lives in `computations/substrate/q_parameter.py`).

The 50-dps decimal expansion `q_0 ≈ 1.1099785955541805…` is
checked-in as a witness; the Lean axiom is just a positive-real-
number existence claim.

## References

- [manuscript] `def:m-mu-over-m-e-calibration` — the equation
  defining `q_0` from the lepton mass ratio
- `computations/substrate/q_parameter.py` — the 50-dps
  Python derivation
- `Q_50_DIGIT_STR` — the 50-decimal-digit literal
-/

namespace QOU.HeckeAlgebra.QSubstrate

/-- **The QOU substrate parameter** `q_0`.

    **`def` form** (was previously an `axiom`).  Discharged
    2026-06-07 in PR #1978 via the same placeholder-literal pattern
    used for `H3BraneTowerScaffold.q0` (same numerical value: the
    50-dps decimal expansion from
    `computations/full-twist-delta-n2-verification.witness.json::q_0`,
    produced by the proton-anchor re-pin of 2026-05-28 in
    `tools/qou-substrate/python/qou_substrate/constants.py::Q_50_DIGIT_STR`).

    Consumer audit (2026-06-07): only `QOU.HeckeAlgebra.Realification`
    references `q_0` by name, and only via the derived `q_0_ne_zero`.
    Other downstream files (`PerNucleusMassDerivation`,
    `JonesMarkovWenzl`, `HeckeAlgebra` root module) `open` the
    namespace but don't read the symbol — they parameterise on `q`
    generically. Locking `q_0` to a literal therefore does not
    constrain any downstream proof; a future refactor will rebind
    this `def` to the substrate-derivation pipeline output once the
    `def:m-mu-over-m-e-calibration` Lean port lands. -/
-- Ref: q-pinning-50-digit.witness.json (proton-anchor re-pin, 2026-05-28)
-- Ref: [manuscript] def:m-mu-over-m-e-calibration
noncomputable def q_0 : ℝ :=
  1.10997858275138080759166909561076887987449912187357763605672

/-- `q_0 > 1` (categorical-derivation property).
    **Theorem** (was previously an `axiom`).  Discharged 2026-06-07
    by `norm_num` against the literal `def q_0` above. -/
theorem q_0_gt_one : 1 < q_0 := by
  unfold q_0
  norm_num

/-- `q_0 ≠ 0` (immediate from `q_0 > 1`). -/
theorem q_0_ne_zero : q_0 ≠ 0 :=
  ne_of_gt (lt_trans one_pos q_0_gt_one)

/-- `q_0 - 1 > 0`. -/
theorem q_0_sub_one_pos : 0 < q_0 - 1 :=
  sub_pos.mpr q_0_gt_one

/-- **Speed of light in cat units**: `c_q := 1 / (q_0 - 1)`. -/
noncomputable def c_q : ℝ := 1 / (q_0 - 1)

/-- `c_q > 0`. -/
theorem c_q_pos : 0 < c_q := by
  unfold c_q
  exact div_pos one_pos q_0_sub_one_pos

/-- **Planck constant in cat units**: `ℏ_q := (q_0 - 1) / q_0`. -/
noncomputable def hbar_q : ℝ := (q_0 - 1) / q_0

/-- `ℏ_q > 0`. -/
theorem hbar_q_pos : 0 < hbar_q := by
  unfold hbar_q
  exact div_pos q_0_sub_one_pos (lt_trans one_pos q_0_gt_one)

/-- `c_q · ℏ_q = 1 / q_0`.  Identity `(1 / (q_0 - 1)) · ((q_0 - 1) /
    q_0) = 1 / q_0`. -/
theorem c_q_mul_hbar_q : c_q * hbar_q = 1 / q_0 := by
  unfold c_q hbar_q
  field_simp [ne_of_gt q_0_sub_one_pos, q_0_ne_zero]

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
noncomputable def eta_q : ℝ := (2 * q_0 - 1) / q_0 ^ 3

/-- `η_q > 0` for `q_0 > 1/2` (in particular for our `q_0 > 1`). -/
theorem eta_q_pos : 0 < eta_q := by
  unfold eta_q
  apply div_pos
  · linarith [q_0_gt_one]
  · exact pow_pos (lt_trans one_pos q_0_gt_one) 3

end QOU.HeckeAlgebra.QSubstrate
