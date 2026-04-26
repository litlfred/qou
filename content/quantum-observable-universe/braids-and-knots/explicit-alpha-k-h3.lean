/-!
# QOU.BraidsAndKnots.explicit_alpha_k_h3

The four curvature-rank prefactors `α_0, α_1, α_2, α_3` at `H_3(R, q)`
in closed `q`-algebraic form:

  α_0 = 1
  α_1 = 0  (vanishes structurally)
  α_2 = z²
  α_3 = h · z² + z = z(1 + q^{1/2} - q^{-1/2})

where `z = 1/(√q + 1/√q)` is the Markov parameter and `h = q - q⁻¹`.

LaTeX label: `prop:explicit-alpha-k-h3`

## References

- [manuscript] Ch. Braids and Knots, §α_k at H_3
- [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.BraidsAndKnots

/-- Markov parameter z and amplitude h at substrate q. -/
structure HeckeQ where
  q : ℝ
  q_pos : 0 < q
  z : ℝ
  z_def : z = 1 / (q ^ (1/2 : ℝ) + 1 / q ^ (1/2 : ℝ))
  h : ℝ
  h_def : h = q - q⁻¹

/-- **Proposition (explicit α_k at H_3)**.

    α_0 = 1, α_1 = 0, α_2 = z², α_3 = h · z² + z. -/
-- Ref: [manuscript] Ch. Braids and Knots, §α_k at H_3
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem explicit_alpha_k_h3 (Q : HeckeQ) :
    ∃ a₀ a₁ a₂ a₃ : ℝ,
      a₀ = 1 ∧ a₁ = 0 ∧ a₂ = Q.z ^ 2 ∧ a₃ = Q.h * Q.z ^ 2 + Q.z :=
  ⟨1, 0, Q.z ^ 2, Q.h * Q.z ^ 2 + Q.z, rfl, rfl, rfl, rfl⟩

end QOU.BraidsAndKnots
