/-!
# QOU.CategoricalQConnection.unique — uniqueness of the categorical q-connection

∇_q uniquely determined by (∇, ξ, θ, q), inheriting the gauge
freedom of ∇.

LaTeX: `\label{prop:categorical-q-connection-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-q-connection-unique
- [connes1994] Noncommutative Geometry
-/

import QOU.Basic

namespace QOU

/-- **Uniqueness of the categorical q-connection.**

    Given fixed (∇, ξ, θ, q), the q-connection
    `∇_q = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ ∇ ∘ θ` is uniquely determined;
    q-deformation introduces no additional gauge freedom. -/
-- Ref: [connes1994]
theorem CategoricalQConnection.unique
    (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    [CategoryTheory.Linear R_q C] :
    Subsingleton (CategoricalQConnection C) := by
  -- DIAGNOSTIC: The `Subsingleton` claim is too strong. The underlying
  -- structure carries free fields (parameters / morphisms / opaque
  -- functions) that admit distinct valid values, so two instances
  -- need not coincide. To recover a meaningful uniqueness claim,
  -- sharpen with a constraining hypothesis (fixing the carrier
  -- object, fixing the substrate parameter, or quantifying over a
  -- quotient by structural equivalence) — see
  -- `frobenius-pairing-unique.lean` for the pattern. Sorry retained
  -- with this diagnosis rather than closed-as-stated.
  sorry

end QOU
