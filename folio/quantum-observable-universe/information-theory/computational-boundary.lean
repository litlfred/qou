import Mathlib.Data.Set.Basic
import Mathlib.Data.Nat.Basic
import Mathlib.Data.Set.BooleanAlgebra
import Mathlib.Order.Disjoint


/-!
# QOU.PvsNPBoundary.computationalBoundary

The **computational boundary** H_c(L, q) = closure(R°) ∖ R° = V(𝔥_c):
the frontier of the polynomial observable subcategory, where every
polynomial-time degree-0 section vanishes.  This is the computational
analog of the jet horizon H = V(𝔥).

LaTeX label: `def:computational-boundary`

## References
- [leitner2026] §9/p-vs-np-boundary
-/

namespace QOU.PvsNPBoundary

/-- **Computational boundary** H_c(L, q) = closure(R°) ∖ R°.

    The frontier of the polynomial observable subcategory `R°`,
    obtained as the topological closure minus the set itself.  In the
    abstract Set model, `closure` is supplied as a set `cl` containing
    `R°`; the boundary is the set-difference `cl ∖ R°`. -/
-- Ref: [leitner2026] §9/p-vs-np-boundary
def computationalBoundary
    (rCirc cl : Set ℕ) : Set ℕ :=
  cl \ rCirc

/-- The computational boundary is disjoint from the polynomial
    observable subcategory: no node is simultaneously inside R° and on
    its boundary. -/
-- Ref: [leitner2026] §9/p-vs-np-boundary
theorem computationalBoundary_disjoint
    (rCirc cl : Set ℕ) :
    Disjoint (computationalBoundary rCirc cl) rCirc := by
  -- Ref: [leitner2026] §9/p-vs-np-boundary
  unfold computationalBoundary
  exact disjoint_sdiff_self_left

/-- The computational boundary is empty iff the closure adds no new
    nodes beyond R° (closure ⊆ R°). -/
-- Ref: [leitner2026] §9/p-vs-np-boundary
theorem computationalBoundary_empty_iff
    (rCirc cl : Set ℕ) :
    computationalBoundary rCirc cl = ∅ ↔ cl ⊆ rCirc := by
  -- Ref: [leitner2026] §9/p-vs-np-boundary
  unfold computationalBoundary
  rw [Set.eq_empty_iff_forall_not_mem]
  constructor
  · intro h a ha
    by_contra hb
    exact h a ⟨ha, hb⟩
  · intro h a ha
    exact ha.2 (h ha.1)

end QOU.PvsNPBoundary
