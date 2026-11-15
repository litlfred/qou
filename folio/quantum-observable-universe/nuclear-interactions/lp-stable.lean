import Mathlib.Data.Real.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Fin.Basic


/-!
# QOU.ParticleInteractions.LPStable — LP-stable elements of H₃(q)

An element of `H₃(q)`, written in the 6-dimensional NF basis, is
LP-stable when the Gram matrix `G_ij = tr_M(b_i · b_j)` maps its
coordinate vector to a componentwise-nonnegative vector.

LaTeX label: `def:lp-stable`

## References
- [leitner2026] §2/lp-dual-stability
-/

namespace QOU.ParticleInteractions

/-- An element of `H₃(q)` is recorded by its 6-vector of NF coordinates. -/
abbrev H3Vector := Fin 6 → ℝ

/-- The Gram matrix `G_ij = tr_M(b_i · b_j)` on the 6 NF basis elements. -/
abbrev GramMatrix := Matrix (Fin 6) (Fin 6) ℝ

/-- `x` is **LP-stable** for Gram matrix `G` iff `G x ≥ 0` componentwise. -/
-- Ref: [leitner2026] §2/lp-dual-stability
def LPStable (G : GramMatrix) (x : H3Vector) : Prop :=
  ∀ i, 0 ≤ (G.mulVec x) i

/-- The zero element is LP-stable for every Gram matrix. -/
theorem lpStable_zero (G : GramMatrix) : LPStable G (0 : H3Vector) := by
  intro i
  simp [LPStable, Matrix.mulVec_zero]

end QOU.ParticleInteractions
