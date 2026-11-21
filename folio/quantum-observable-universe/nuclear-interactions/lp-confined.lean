import Mathlib.Data.Real.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Fin.Basic


/-!
# QOU.ParticleInteractions.LPConfined — LP-confined elements of H₃(q)

An LP-stable element is **LP-confined** when no proper sub-braid of its
braid word is itself LP-stable: stability requires the topologically
complete braid, not any of its sub-words.

LaTeX label: `def:lp-confined`

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

/-- An element `x` is **LP-confined** for Gram matrix `G` relative to a
    family of proper sub-braid coordinate vectors `subBraids` iff `x`
    itself is LP-stable and none of the proper sub-braids is LP-stable. -/
-- Ref: [leitner2026] §2/lp-dual-stability
def LPConfined (G : GramMatrix) (x : H3Vector)
    (subBraids : List H3Vector) : Prop :=
  LPStable G x ∧ ∀ s ∈ subBraids, ¬ LPStable G s

/-- An LP-confined element is in particular LP-stable. -/
theorem LPConfined.lpStable {G : GramMatrix} {x : H3Vector}
    {subBraids : List H3Vector} (h : LPConfined G x subBraids) :
    LPStable G x :=
  h.1

end QOU.ParticleInteractions
