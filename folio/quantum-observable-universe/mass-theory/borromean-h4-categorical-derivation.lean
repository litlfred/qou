/-
# `prop:borromean-h4-categorical-derivation`

Borromean h⁴ = -3/4 derived as (-3) · (1/4) via the (2,1) Hecke
spectral projector + symmetric-point Markov normalisation.

The h⁴ coefficient of the Borromean Markov trace
`tr_M(β_Bor) = (4 + h² - 3h⁴ - h⁶)/(h² + 4)` factorises as
`(-3) · (1/4)` where:

- The character coefficient `-3` is the h⁴ coefficient of
  `χ^{(2,1)}(β_Bor) = 2 - 3h⁴ - h⁶`, the standard-irrep character on
  the Borromean braid.  The polynomial form is now structurally a
  consequence of the q-heat-kernel Peter-Weyl decomposition merged
  in PR #2131 (`prop:q-heat-kernel-peter-weyl`,
  `prop:habiro-residue-sum-equivalence`).  The categorical projector
  onto the (2,1) channel is the e_- minus-eigenspace projector of
  the Hecke quadratic relation, formalised sorry-free in
  `QOU.Hecke.SpectralProjector` (`eminus_idem`,
  `eplus_eminus_orthogonal`, `eplus_add_eminus = 1`).

- The factor `1/4 = 1/[2]_q²|_{q=1}` is the q = 1 evaluation of the
  exact closed-form Wenzl weight `y_(2,1)(q) = 1/[2]_q²` established
  in `prop:h3-markov-wenzl-weights`.  The full H_3 weight vector is
  `([4]_q/[2]_q³, 1/[2]_q², 0)` — NOT uniform at q = 1 (it evaluates
  to (1/2, 1/4, 0); the sign channel carries zero weight identically
  by the Temperley-Lieb quotient, and the Jones-normalised trace is
  chiral, so no bar-involution uniformity applies).

This file states the numeric factorisation lemma `(-3) · (1/4) = -3/4`
and proves it by `norm_num`.  Each ingredient now has a categorical
home on `main` (see references in the `.md` and at the bottom of
this file); the composition theorem connecting them to
`tr_M(β_Bor)` is deferred to a follow-up Lean PR once q-Schur
duality lands at the needed depth.

Computational verification (50 dps) lives in:
- T15 (`gap_a4_T15_character_polynomial_probe.py`) — polynomial form
  of `χ^{(2,1)}(β_Bor)` via algebraic substitution.
- T18 (`gap_a4_T18_markov_normalization_probe.py`) — derivation of
  `y_{(2,1)}(q=1) = 1/4` from the Frobenius expansion + Markov
  normalisation `Σ_λ y_λ d_λ = tr_M(1_3) = 1`.
-/

import Mathlib.Algebra.Polynomial.Coeff
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

namespace QOU.BraidsAndKnots

open Polynomial

/-! ## The h⁴ factorisation, and where each factor comes from

The combinatorial core of the categorical chain:

  h⁴(tr_M(β_Bor)) = [χ^{(2,1)} h⁴-coeff via e_- projector]
                  × [Markov normalisation at symmetric point]
                  = (-3) · (1/4)
                  = -3/4

Each factor has its categorical home on `main`:
- `-3` derives from the Hecke spectral projector e_-
  (`QOU.Hecke.SpectralProjector.eminus_idem`) acting on the standard
  (2,1) channel, with the polynomial form
  `χ^{(2,1)}(β_Bor) = 2 - 3h⁴ - h⁶` supplied by the q-heat-kernel
  Peter-Weyl decomposition (`prop:q-heat-kernel-peter-weyl`,
  `prop:habiro-residue-sum-equivalence`).
- `1/4 = 1/[2]_q²|_{q=1}` is the q = 1 evaluation of the exact
  closed-form weight `y_(2,1)(q) = 1/[2]_q²`
  (cf. `prop:h3-markov-wenzl-weights`).

The composition theorem connecting these to `tr_M(β_Bor)` (q-Schur
duality + Markov-trace existence) is deferred to a follow-up Lean
PR.  Computational verification at 50 dps lives in T15 / T18. -/

/-- The `(2,1)` character of the Borromean braid as a polynomial in `h`:
    `χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶`, supplied by the q-heat-kernel
    Peter–Weyl decomposition (`prop:q-heat-kernel-peter-weyl`,
    `prop:habiro-residue-sum-equivalence`). -/
noncomputable def chiTwoOneBorromean : ℝ[X] := 2 - 3 * X ^ 4 - X ^ 6

/-- The symmetric q-integer `[2]_q = q + q⁻¹`. -/
noncomputable def qInt2 (q : ℝ) : ℝ := q + q⁻¹

/-- The `(2,1)` Markov–Wenzl weight in closed form,
    `y_(2,1)(q) = 1/[2]_q²` (`prop:h3-markov-wenzl-weights`). -/
noncomputable def yTwoOne (q : ℝ) : ℝ := 1 / (qInt2 q) ^ 2

/-- The `h⁴` coefficient of `χ^{(2,1)}(β_Bor)` is `−3`. -/
theorem chiTwoOneBorromean_coeff_four : chiTwoOneBorromean.coeff 4 = -3 := by
  simp [chiTwoOneBorromean, coeff_X_pow]

/-- At the symmetric point `q = 1`, `[2]_q = 2` and `y_(2,1) = 1/4`. -/
theorem yTwoOne_at_one : yTwoOne 1 = 1 / 4 := by
  norm_num [yTwoOne, qInt2]

/-- **Numeric factorisation lemma** for the Borromean h⁴ coefficient:
    the `h⁴` coefficient of the `(2,1)` character, times the `(2,1)`
    Markov–Wenzl weight at the symmetric point, is `−3/4`.

    **This was previously stated as `(-3 : ℝ) * (1/4 : ℝ) = -3/4`, proved
    by `norm_num`** — a true arithmetic fact that mentions nothing in the
    framework and would still hold if either factor came from somewhere
    else entirely. The statement now names both inputs, so it is false if
    the character polynomial or the weight closed form is wrong: that is
    the falsifiability AGENTS.md §"Derive-then-check" asks for before a
    proof is attempted.

    What is still NOT proved here is the composition — that this product
    IS `h⁴(tr_M(β_Bor))`. That needs q-Schur duality plus Markov-trace
    existence and is stated as the deferred theorem in the comment
    below. -/
theorem borromean_h4_numeric_factorisation :
    chiTwoOneBorromean.coeff 4 * yTwoOne 1 = -3 / 4 := by
  rw [chiTwoOneBorromean_coeff_four, yTwoOne_at_one]
  norm_num

-- Ref: [murasugi1996] https://doi.org/10.1007/978-3-642-58947-1
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Categorical building blocks now on main:
--   • QOU.Hecke.SpectralProjector — e_± idempotent, orthogonal, complete
--     (eminus_idem, eplus_eminus_orthogonal, eplus_add_eminus = 1);
--     supplies the categorical (2,1)-channel projector.
--   • QOU.Braiding.HeckeGenPolyReduction.hecke_gen_poly_reduction —
--     Cayley-Hamilton block reduction of the Hecke generator σ;
--     useful for closed-form trace computation on V^⊗n.
--   • prop:q-heat-kernel-peter-weyl + prop:habiro-residue-sum-equivalence
--     (PR #2131) — supply the polynomial form
--     χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶ as a q-heat-kernel consequence.
--   • prop:h3-markov-wenzl-weights — exact closed-form weights
--     ([4]_q/[2]_q³, 1/[2]_q², 0); the 1/4 is y_(2,1)(q) = 1/[2]_q²
--     at q = 1 (weights NOT uniform; sign channel is TL-quotient zero).
-- Full categorical Lean derivation (deferred — needs q-Schur duality
-- + Markov-trace existence theorems that compose the above):
--
--   theorem BorromeanH4CategoricalDerivation :
--     h4_coefficient (markov_trace (closure beta_Bor)) =
--       chi_standard_irrep_h4_coeff_via_eminus *
--       markov_norm_at_symmetric_point 3
--     := sorry

end QOU.BraidsAndKnots
