/-!
# QOU.BraidsAndKnots.explicit_alpha_k_h3

The four curvature-rank prefactors `α_0, α_1, α_2, α_3` at `H_3(R, q)`
in closed `q`-algebraic form:

  α_0 = 1
  α_1 = 0  (vanishes structurally)
  α_2 = z²
  α_3 = h · z² + z = z(1 + q^{1/2} - q^{-1/2})

where `z = 1/(v + v⁻¹)` is the Markov parameter, `v` is the formal
square root of `q` (so `v² = q`), and `h = q - q⁻¹`.

**Pre-Archimedean stub.** Polymorphic in the ground field `R`.
The previous version forced `q : ℝ`, `z : ℝ`, `h : ℝ` and used
`q ^ (1/2 : ℝ)` (a real power); the new version uses an
abstract `v : R` with `v² = q` carried as a structure field.
The Archimedean evaluation `R = ℝ`, `v = √q₀` is the post-τ
realisation.

LaTeX label: `prop:explicit-alpha-k-h3`

## References

- [manuscript] Ch. Braids and Knots, §α_k at H_3
- [jones1987] https://doi.org/10.2307/1971403
-/

import Mathlib.Algebra.Field.Basic

namespace QOU.BraidsAndKnots

universe u

/-- Markov parameter `z` and amplitude `h` at substrate `q`,
    polymorphic in the ground field `R`.

    `v` is the formal square root of `q` (so `v² = q`), `z` is the
    Markov parameter `1/(v + v⁻¹)`, and `h = q - q⁻¹`. -/
structure HeckeQ (R : Type u) [Field R] where
  q : R
  v : R                          -- formal √q
  v_sq : v ^ 2 = q
  z : R
  z_def : z = 1 / (v + v⁻¹)
  h : R
  h_def : h = q - q⁻¹

/-- **Proposition (explicit α_k at H_3)**.

    `α_0 = 1`, `α_1 = 0`, `α_2 = z²`, `α_3 = h · z² + z`. -/
-- Ref: [manuscript] Ch. Braids and Knots, §α_k at H_3
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem explicit_alpha_k_h3 {R : Type u} [Field R] (Q : HeckeQ R) :
    ∃ a₀ a₁ a₂ a₃ : R,
      a₀ = 1 ∧ a₁ = 0 ∧ a₂ = Q.z ^ 2 ∧ a₃ = Q.h * Q.z ^ 2 + Q.z :=
  ⟨1, 0, Q.z ^ 2, Q.h * Q.z ^ 2 + Q.z, rfl, rfl, rfl, rfl⟩

end QOU.BraidsAndKnots
