import Mathlib.Data.Real.Basic
import Mathlib.Data.Finset.Card

/-!
# QOU.PhiQPiece — Φ_q-piece sub-link of a braid closure

For a braid `β ∈ B_n` and a subset `S ⊆ {0, …, n-2}` of its crossing
indices, the **Φ_q-piece** `K_S ⊆ S³` is the link obtained by smoothing
(L₀-resolution) every crossing of `β` outside `S` and keeping the
crossings indexed by `S` intact.

LaTeX label: `def:phi-q-piece`

## References

- [leitner2026] Ch 3 §sec:calibration-algebraic-mass / phi-q-piece
- [kauffman1991] Knots and Physics, World Scientific, ISBN 978-981-02-0343-7
-/

namespace QOU.PhiQPiece

/-- Abstract braid: a finite list of (signed) Hecke-generator indices.
    `n` is the number of strands; each generator index is a `Fin (n-1)`.
    A negative crossing carries `Bool = true`. -/
structure Braid where
  n : ℕ
  word : List (Fin (n - 1) × Bool)
deriving Repr

/-- Abstract sub-link type carrying a name and a (placeholder) topological
    invariant.  In the formal development this is replaced by the actual
    sub-link `K_S ⊆ S³`; here it is kept abstract because the volume
    only enters through the Kashaev volume conjecture class. -/
structure SubLink where
  name : String
  /-- Hyperbolic volume of `S³ \ K_S` (zero when the complement is not
      hyperbolic, by the convention recorded in the .md file). -/
  hypVolume : ℝ
  hypVolume_nonneg : 0 ≤ hypVolume

/-- The Φ_q-piece `K_S` of a braid `β`: the closure of the sub-braid
    obtained by deleting (= replacing by the identity strand) every
    crossing whose index is **not** in `S`.

    This is the abstract specification; the geometric construction
    (Kauffman L₀-smoothing of the diagram) is recorded in the
    accompanying `.md` file. -/
-- Ref: [leitner2026] Ch 3 §sec:calibration-algebraic-mass / phi-q-piece
-- Ref: [kauffman1991] Knots and Physics, World Scientific
noncomputable def subLink (β : Braid) (S : Finset (Fin (β.n - 1))) :
    SubLink :=
  { name := s!"K_S(β, {S.card})"
    hypVolume := 0   -- abstract: real value supplied by KashaevVolumeConjecture
    hypVolume_nonneg := le_refl 0 }

/-- The empty piece `K_∅` is the trivial unlink; its hyperbolic volume
    is zero by convention. -/
-- Ref: [leitner2026] Ch 3 §sec:calibration-algebraic-mass / phi-q-piece
theorem subLink_empty (β : Braid) :
    (subLink β ∅).hypVolume = 0 := rfl

end QOU.PhiQPiece
