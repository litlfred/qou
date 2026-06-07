/-
  Borromean Frobenius reconstruction (B): the per-representation Jones
  decomposition `tr_M(β_Bor) = Σ_λ y_λ · χ^λ(β_Bor)` reproduces the proved
  closed form, as a rational identity in `h = q − q⁻¹`.

  This is the "reconstruction" layer (B) complementing
  `BorromeanMarkovTrace.lean` (the closed form) and the per-rep `χ^λ`
  forms (narrative + numerically cross-checked in
  `borromean_chi_independent_crosscheck.py`, PR #1947). It does NOT derive
  `χ^{(2,1)}` from the seminormal representation (that is the heavier
  layer A); it proves that, GIVEN the documented per-rep `χ^λ` and the
  Jones–Frobenius weights, the Frobenius sum equals the closed form.

  ## Weight convention (IMPORTANT — distinct from production y_lambda_at)

  These `y_λ` are the **signed Jones / Markov** Wenzl weights of the
  Frobenius decomposition `tr_M = Σ y_λ χ^λ`, normalised by
  `Σ_λ y_λ d_λ = tr_M(id) = 1`.  For H₃ the two Markov constraints
  (normalisation + the closed form) force

      y_{(2,1)}(h) = 1/(h²+4) = 1/[2]_q²        (= 1/4 at q=1, cf. T18),
      y_{(3)}(h) + y_{(1³)}(h) = (h²+2)/(h²+4).

  Only `y_{(2,1)}` and the SUM `y_{(3)}+y_{(1³)}` enter `tr_M` (because
  `χ^{(3)} = χ^{(1³)} = 1`); the individual split is not needed here.

  ⚠ These are NOT the `wedderburn_jones_markov.y_lambda_at` weights used in
  the production MASS pipeline: those are paired with the MODULUS `|χ^λ|`
  (binding = |tr_M|) and give a different value (e.g. `y_{(2,1)} ≈ 0.316`
  vs `1/(h²+4) ≈ 0.213` at q=1.5).  This is the same signed-χ vs |χ| split
  documented in `docs/homfly-markov-convention-discipline.md §3`; do not
  conflate the two weight families.

  -- Ref: [jones1987] https://doi.org/10.1090/S0273-0979-1985-15304-2
  -- Ref: prop:borromean-markov-trace-closed-form
-/
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import QOU.BraidsAndKnots.BorromeanMarkovTrace

namespace QOU.BraidsAndKnots

/-- Jones–Frobenius weight of the standard (2,1) irrep: `1/[2]_q² = 1/(h²+4)`. -/
noncomputable def yJones_21 (h : ℚ) : ℚ := 1 / (h ^ 2 + 4)

/-- Sum of the two one-dimensional Jones–Frobenius weights,
    `y_{(3)} + y_{(1³)} = (h²+2)/(h²+4)`. -/
noncomputable def yJones_sym (h : ℚ) : ℚ := (h ^ 2 + 2) / (h ^ 2 + 4)

/-- The standard-irrep character of the Borromean braid,
    `χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶` (the one-dim characters are `1`). -/
def chi21_borromean (h : ℚ) : ℚ := 2 - 3 * h ^ 4 - h ^ 6

/-- `h² + 4 > 0` over ℚ (reused denominator non-vanishing). -/
theorem hsq_add_four_pos (h : ℚ) : (0 : ℚ) < h ^ 2 + 4 := by positivity

/-- **Markov normalisation.** `(y_{(3)}+y_{(1³)}) + 2·y_{(2,1)} = 1`,
    i.e. `Σ_λ y_λ d_λ = 1` with `d_{(3)}=d_{(1³)}=1`, `d_{(2,1)}=2`. -/
theorem jones_markov_normalization (h : ℚ) :
    yJones_sym h + 2 * yJones_21 h = 1 := by
  have hne : (h ^ 2 + 4 : ℚ) ≠ 0 := (hsq_add_four_pos h).ne'
  unfold yJones_sym yJones_21
  field_simp [hne]
  ring

/-- **Frobenius reconstruction (B).** The per-representation Jones sum
    `Σ_λ y_λ · χ^λ(β_Bor) = y_sym·1 + y_{(2,1)}·χ^{(2,1)}` equals the proved
    Borromean Markov-trace closed form `trM_borromean`. -/
theorem borromean_frobenius_reconstruction (h : ℚ) :
    yJones_sym h + yJones_21 h * chi21_borromean h = trM_borromean h := by
  have hne : (h ^ 2 + 4 : ℚ) ≠ 0 := (hsq_add_four_pos h).ne'
  unfold yJones_sym yJones_21 chi21_borromean trM_borromean
    trM_borromean_num trM_borromean_den
  field_simp [hne]
  ring

end QOU.BraidsAndKnots
