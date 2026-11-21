import Mathlib.Algebra.Module.Basic
import Mathlib.Algebra.Module.Submodule.Ker


/-!
# QOU.BraneBoundary — Defining boundary of the brane

The defining boundary ∂Aₙ consists of subobjects of Aₙ on which
the restriction morphism rₙ : Aₙ → A_{n-1} has non-trivial kernel.

## References

- [leitner2026] §3 Lifting and Descent
-/

namespace QOU

variable {R : Type*} [CommRing R]

/-- The defining boundary of the n-th brane: the submodule consisting
    of elements that are "new" at level n (not descended from level n-1).

    Categorically: ∂Aₙ = {S ↪ Aₙ | ker(rₙ|_S) ≠ 0}

    LaTeX: `\label{def:brane-boundary}` -/
-- Ref: [leitner2026] §3, Definition: Brane boundary
def braneBoundary {M N : Type*} [AddCommGroup M] [Module R M]
    [AddCommGroup N] [Module R N]
    (restriction : M →ₗ[R] N) : Submodule R M :=
  LinearMap.ker restriction

end QOU
