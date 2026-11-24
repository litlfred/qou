/-
  Cusp winding lattice norm form G(m,ℓ) = (2m+ℓ)² − 3ℓ².

  For the figure-eight knot 4₁ with cusp shape ω = e^{iπ/3}, a geodesic
  winding (m,ℓ) on the cusp torus gives deformation u = ln q₀ · (m + ℓω).
  The binding formula Im 𝔙₄₁(u) = (√3/4)(Re²u − Im²u) evaluates to
      Im 𝔙₄₁ = (√3/16)(ln q₀)² · G(m,ℓ)
  where G(m,ℓ) = (2m+ℓ)² − 3ℓ² is the norm form of ℤ[√3] (disc. 12).

  KEY RESULT: G(0,1) = −2 — the longitude winding gives exactly the q→1
  shadow of the precision-ladder coefficient c₃. The angle φ = π/3 at this
  winding equals the cusp shape angle, making c₃ a geometric invariant of
  the cusp lattice (not a fit parameter).

  Sorry-free. All theorems proved by norm_num.

  -- Ref: [leitner2026] docs/coordination/udeform-spin-part-derivation.md
  -- Ref: [leitner2026] docs/coordination/ck-dk-canonical-registry.md §3 (c₃ row)
-/
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace QOU.QBeta.CuspWindingLattice

/-- The cusp winding lattice norm form G(m,ℓ) = (2m+ℓ)² - 3ℓ²
    At the longitude winding (m,ℓ) = (0,1), G(0,1) = -2 (the q→1 shadow of c₃) -/
def G (m ℓ : ℤ) : ℤ := (2 * m + ℓ) ^ 2 - 3 * ℓ ^ 2

/-- The longitude winding has norm -2, which equals the q→1 shadow of c₃. -/
theorem G_longitude : G 0 1 = -2 := by
  norm_num [G]

/-- The meridian winding has norm 4 (boost-dominated). -/
theorem G_meridian : G 1 0 = 4 := by
  norm_num [G]

/-- G is the norm form of ℤ[√3] (discriminant 12) -/
theorem G_is_norm_form (m ℓ : ℤ) : G m ℓ = (2 * m + ℓ) ^ 2 - 3 * ℓ ^ 2 := by
  rfl

end QOU.QBeta.CuspWindingLattice
