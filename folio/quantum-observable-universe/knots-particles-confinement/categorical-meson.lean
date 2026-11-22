import QOU.Basic


/-!
# QOU.Torsion.CategoricalMeson

The meson as a valence-2 hadron: a quark–antiquark pair
bound by the Hopf link L_H.

LaTeX label: `def:categorical-meson`

## References

- [jones1985] https://doi.org/10.1090/S0273-0979-1985-15304-2
-/

namespace QOU.Torsion

/-- **Meson (categorical)**: a hadron of valence 2, consisting of
    a quark–antiquark pair bound by the Hopf link.
    The braid word is T₀₁ · L_H · T₁₀ = (σ₀σ₁)² · σ₁σ₀. -/
-- Ref: [jones1985] Jones, "A polynomial invariant for knots via von Neumann algebras," Bull. AMS 12 (1985)
structure CategoricalMeson where
  /-- The underlying type of knot invariants. -/
  InvariantType : Type*
  /-- Quark crossing pair T₀₁ = σ₀σ₁ (L₊; closure in B₃: unknot). -/
  T01 : InvariantType
  /-- Antiquark crossing pair T₁₀ = σ₁σ₀ (L₋; closure in B₃: unknot). -/
  T10 : InvariantType
  /-- Binding word L_H = σ₀σ₁ (closure in B₃: unknot). -/
  hopfBinding : InvariantType
  /-- The meson is the composite T₀₁ · L_H · T₁₀. -/
  composite : InvariantType
  /-- Valence is 2 (quark + antiquark). -/
  valence : Nat := 2
  /-- The valence is exactly 2. -/
  valence_eq : valence = 2 := by rfl

end QOU.Torsion
