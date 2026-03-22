/-!
# QOU.CategoricalQTorsionLeaf — q-torsion leaf in a Frobenius–Hopf object

A q-torsion leaf is a maximal sub-object L ↪ A such that L is
horizontal (contained in ker(π_V)) and flow-invariant under the
q-Reeb flow.

## References

- [leitner2026] §1 Quantum Observable Universe
-/

import Mathlib.Algebra.Module.Basic

namespace QOU

variable {R : Type*} [CommRing R]

/-- A categorical q-torsion leaf: a maximal submodule that is horizontal
    and invariant under the q-Reeb flow.

    LaTeX: `\label{def:categorical-q-torsion-leaf}` -/
-- Ref: [leitner2026] §1, Definition: Categorical q-torsion leaf
structure CategoricalQTorsionLeaf (M : Type*) [AddCommGroup M] [Module R M] where
  /-- The leaf as a submodule. -/
  leaf : Submodule R M
  /-- The vertical projection π_V. -/
  verticalProj : M →ₗ[R] M
  /-- Horizontality: the leaf is in the kernel of π_V. -/
  horizontal : ∀ x ∈ leaf, verticalProj x = 0
  /-- The q-Reeb flow automorphism. -/
  qReebFlow : M →ₗ[R] M
  /-- Flow invariance: the q-Reeb flow preserves the leaf. -/
  flow_invariant : ∀ x ∈ leaf, qReebFlow x ∈ leaf

end QOU
