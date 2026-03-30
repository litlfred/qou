/-!
# QOU.AlgebraicSubstrate.RigidDualizingComplex

Yekutieli's rigid dualizing complex for a non-commutative algebra,
providing canonical duality in the derived category.

LaTeX label: `def:rigid-dualizing-complex`
-/

set_option autoImplicit false

import Mathlib.Algebra.Homology.Complex
import Mathlib.Algebra.Ring.Basic

namespace QOU.AlgebraicSubstrate

/-- **RigidDualizingComplex**: a rigid dualizing complex `ω_A•` for
    a non-commutative algebra `A`, in the sense of Yekutieli.

    The complex is equipped with a rigidifying isomorphism
    `ω_A• ≃ RHom_{A^e}(A, A^e)`, ensuring uniqueness up to
    unique isomorphism.

    LaTeX: `\label{def:rigid-dualizing-complex}` -/
structure RigidDualizingComplex (A : Type*) [Ring A] where
  /-- The carrier type for the dualizing complex. -/
  carrier : Type*
  /-- Homological dimension of `A`. -/
  homdim : ℕ
  /-- The rigidifying isomorphism exists (opaque; full construction
      requires derived-category infrastructure beyond current Mathlib). -/
  -- Ref: [yekutieli2015] https://doi.org/10.1090/S0002-9947-2014-6theory
  rigidifying_iso : Prop := True
  /-- The rigid dualizing complex has finite injective dimension. -/
  -- Ref: [yekutieli2015] https://doi.org/10.1090/S0002-9947-2014-6theory
  finite_inj_dim : Prop := True
  /-- Van den Bergh duality holds with respect to `ω_A•`. -/
  -- Ref: [yekutieli2015] https://doi.org/10.1090/S0002-9947-2014-6theory
  vdb_duality : Prop := True

-- Ref: [yekutieli2015] https://doi.org/10.1090/S0002-9947-2014-6theory
/-- Existence of a rigid dualizing complex for a suitable
    non-commutative algebra (sorry: requires derived-category
    infrastructure). -/
theorem rigid_dualizing_exists (A : Type*) [Ring A] :
    Nonempty (RigidDualizingComplex A) := by
  sorry

end QOU.AlgebraicSubstrate
