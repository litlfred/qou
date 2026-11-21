import Mathlib.Algebra.Group.Defs

/-!
# QOU.AlgebraicSubstrate.ClassicalLimitObstruction

The classical limit obstruction of a quantum universe:
the Hochschild cohomology group HH²(𝒰_q(𝔤), Ad) that governs
whether properties holding at generic q persist through q = 1.

LaTeX label: `def:classical-limit-obstruction`

## References
- [yekutieli2010] https://doi.org/10.1016/j.aim.2009.12.006
- [leitner2026] §8/classical-limit-obstruction
-/

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

/-- **Classical limit obstruction**: the Hochschild cohomology group
    `HH²(𝒰_q(𝔤), Ad)` that controls whether algebraic properties
    of the quantum universe persist through the classical limit q → 1.

    Elements of Obs are obstructions to extending second-order
    deformations of the Frobenius–Hopf algebra A_q across q = 1.

    The Hochschild tower:
    - HH⁰(Ad): G-invariant adjoint vectors (hidden symmetries)
    - HH¹(Ad): outer derivations (infinitesimal deformations)
    - HH²(Ad): obstructions to extending deformations across q = 1
    - HH³(Ad): secondary obstructions (Massey products)

    A property 𝒫(q) that holds for generic non-torsion q persists
    through q = 1 iff its obstruction class [𝒫] ∈ HH²(Ad) vanishes. -/
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
-- Ref: [leitner2026] §8/classical-limit-obstruction
structure ClassicalLimitObstruction where
  /-- The underlying type of the obstruction group HH²(𝒰_q, Ad). -/
  carrier : Type*
  /-- The obstruction group has an additive group structure. -/
  [addGroupInst : AddCommGroup carrier]
  /-- Predicate: a deformation with obstruction class `obs` extends
      across the classical limit q → 1. -/
  deformation_extends : carrier → Prop
  /-- A deformation extends iff its obstruction class vanishes.
      This is the content of the Hochschild deformation theorem. -/
  -- Ref: [yekutieli2010] https://doi.org/10.1016/j.aim.2009.12.006
  extends_iff_zero : ∀ (obs : carrier),
    deformation_extends obs ↔ obs = (0 : carrier)
  /-- The obstruction class of the substrate parameter. -/
  substrate_class : carrier
  /-- The substrate class is non-trivial (q ≠ 1 is essential). -/
  substrate_nontrivial : substrate_class ≠ (0 : carrier)

end QOU.AlgebraicSubstrate
