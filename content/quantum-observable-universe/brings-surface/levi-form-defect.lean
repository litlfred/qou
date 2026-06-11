import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Algebra.Module.Basic


/-!
# QOU.AlgebraicSubstrate.LeviFormDefect — Matter as Frobenius failure

The Levi form measures the non-degeneracy of the contact structure at
a point in the spectral fiber. When non-zero, the Frobenius form cannot
extend smoothly, creating a topological defect — the matter locus.

LaTeX label: `def:levi-form-defect`

## References

- [manuscript] Ch 8 §2, The unit particle as a cohomological defect
-/

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

universe u

variable {C : Type u} [CategoryTheory.Category C]

/-- The Levi form defect structure: captures the failure of the
    Frobenius form at a point in the spectral fiber.

    At a point p, the Levi form ℒ_p measures non-degeneracy of the
    contact structure. The matter locus is the set of points where
    ℒ_p ≠ 0. -/
structure LeviFormDefect (R : Type*) [CommRing R] where
  /-- The ambient algebra (spectral fiber). -/
  carrier : Type*
  /-- Module structure on the carrier. -/
  [modulInst : Module R carrier]
  /-- The Levi form as a bilinear map (abstracting T^{1,0} × T^{0,1} → k). -/
  leviForm : carrier →ₗ[R] carrier →ₗ[R] R
  /-- Non-degeneracy: there exists a point where the Levi form is nonzero. -/
  -- Ref: [manuscript] Ch 8 §2
  nondeg : ∃ (x y : carrier), leviForm x y ≠ 0

attribute [instance] LeviFormDefect.modulInst

/-- The matter locus is nonempty when the Levi form defect exists. -/
-- Ref: [manuscript] Ch 8 §2
theorem matter_locus_nonempty {R : Type*} [CommRing R]
    (d : LeviFormDefect R) : ∃ (x y : d.carrier), d.leviForm x y ≠ 0 :=
  d.nondeg

end QOU.AlgebraicSubstrate
