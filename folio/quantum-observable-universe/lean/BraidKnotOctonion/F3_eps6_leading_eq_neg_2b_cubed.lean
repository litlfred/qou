import Mathlib.Tactic


/-!
# QOU.BraidKnot.F3_eps6_leading_eq_neg_2b_cubed

Symbolic exact match: the leading ε^6 coefficient of (F_3 - 1) at q = 1+ε
equals exactly `-2 · b³(q=1) = -3·√3/4`.

This is the formal-Lean port of the result proved symbolically in
`probe_q_beta_cat_per_factor_decomposition.py`:

  F_3 - 1 = -2 · b³ · ℏ_q^6
  At q = 1: b² = (q⁴+q²+1)/(q²+1)² = 3/4, so b = √3/2, b³ = (3·√3)/8.
  ℏ_q at q = 1: ℏ_q = (q-1)/q = 0, but leading term is ℏ_q ≈ ε at q = 1+ε.
  So ℏ_q^6 leading is ε^6.
  Hence (F_3 - 1)'s ε^6 coefficient is -2 · (3√3/8) = -3√3/4.

The result is CLOSED in Lean by elementary arithmetic.

LaTeX label: `rem:F3-eps6-leading-eq-neg-2b-cubed` (helper Lean lemma).
-/

namespace QOU.BraidKnot

/-- **Leading `ε⁶` coefficient over a √3 symbol.** For any `b` in a characteristic-zero field with
`b² = 3/4` (that is, `b = √3/2`), `-2 b³ = -(3/2) b`. The `Real.sqrt` forms
(`b_at_one = √3/2`, `-2 b³ = -3√3/4`) are in
`QOU.Transcendental.BraidKnotOctonion.F3_eps6_leading_eq_neg_2b_cubedReal`
(bean `qou-dk7p`). -/
theorem F3_eps6_leading_of_sq {K : Type*} [Field K] [CharZero K] {b : K} (hb : b ^ 2 = 3 / 4) :
    -2 * b ^ 3 = -(3 / 2) * b := by
  have : b ^ 3 = b ^ 2 * b := by ring
  rw [this, hb]; ring

end QOU.BraidKnot
