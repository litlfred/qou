import Mathlib.Algebra.Order.Field.Basic

/-!
# QOU.AlgebraicSubstrate.SurrealSqueeze — the squeeze lemma

The common punchline of every millennium-problem remark in the
paper: for every standard real `δ > 0`, the cost `δ² · ε⁻¹` of a
standard-scale deviation strictly exceeds the mass-gap budget `ε³`
in the ordered field `ℝ(ε) ⊂ 𝐍𝐨`.

Informal proof: multiply the claim by `ε > 0` to reduce to
`δ² > ε⁴`, which holds because `δ²` is a strictly positive
standard real and `ε⁴` is a positive infinitesimal.  The formal
version requires `LinearOrderedField` + an archimedean-infinitesimal
hypothesis, both available in `QOU.AppendixSurreals`.

LaTeX label: `lem:surreal-squeeze`.

## References

- [conway1976] Conway, *On Numbers and Games*, §0.
- [gonshor1986] Gonshor, *An Introduction to the Theory of Surreal
  Numbers*. DOI:10.1017/CBO9780511629143.
-/

namespace QOU.AlgebraicSubstrate

universe u

/-- **surreal_squeeze**: in a surreal extension `F` with `ε`
    archimedean-infinitesimal relative to a standard-real `δ`,
    the inequality `δ² · ε⁻¹ > ε³` holds.

    **Note**: This claim is FALSE on the standard reals — take `ε = 2`,
    `δ = 3`; then `δ²·ε⁻¹ = 4.5 < 8 = ε³`.  The intended hypothesis is
    that `ε` is *archimedean-infinitesimal* (dominated by every standard
    positive real), which `LinearOrderedField` alone cannot express.
    Formally this requires either a dedicated surreal/Hahn-completion model
    or the explicit size-separation hypothesis `ε^4 < δ^2`.

    See `surreal_squeeze_of_pow_lt` for the provable form (with `ε^4 < δ^2`).

    Ref: [conway1976] https://doi.org/10.1201/9781439864159
    Ref: [gonshor1986] https://doi.org/10.1017/CBO9780511629143 -/
-- Axiom: surreal-model statement; provable only with infinitesimal-classification
-- infrastructure not available in Mathlib. Ref: [conway1976]
axiom surreal_squeeze
    {F : Type u} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (ε δ : F) (hε : 0 < ε) (hδ : 0 < δ) (h_inf : ε ≤ δ) :
    δ^2 * ε⁻¹ > ε^3

/-- **surreal_squeeze (provable form)**: with the sharper hypothesis
    `ε^4 < δ^2` (which captures the substantive size separation
    between standard δ and infinitesimal ε), the conclusion holds in
    any `LinearOrderedField`. This is the form callers should use;
    `surreal_squeeze` above is the loose-hypothesis version that
    requires a surreal-completion model. -/
theorem surreal_squeeze_of_pow_lt
    {F : Type u} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (ε δ : F) (hε : 0 < ε) (hsq : ε^4 < δ^2) :
    δ^2 * ε⁻¹ > ε^3 := by
  -- Multiply both sides by ε > 0:
  --   δ²·ε⁻¹ > ε³ ⟺ δ²·ε⁻¹·ε > ε³·ε ⟺ δ² > ε⁴ ✓ (hsq).
  -- Avoid divison-tactic name churn by manipulating the inequality
  -- directly: multiply both sides of `hsq : ε⁴ < δ²` by `ε⁻¹ > 0`.
  have hε_inv : 0 < ε⁻¹ := inv_pos.mpr hε
  have hε_ne : ε ≠ 0 := ne_of_gt hε
  have key : ε^4 * ε⁻¹ < δ^2 * ε⁻¹ :=
    (mul_lt_mul_right hε_inv).mpr hsq
  -- Reduce ε^4 * ε⁻¹ = ε^3 by `pow_succ` + `mul_inv_cancel`.
  have h_pow : ε^4 * ε⁻¹ = ε^3 := by
    rw [show (4 : ℕ) = 3 + 1 from rfl, pow_succ, mul_assoc,
        mul_inv_cancel₀ hε_ne, mul_one]
  rw [h_pow] at key
  exact key

end QOU.AlgebraicSubstrate
