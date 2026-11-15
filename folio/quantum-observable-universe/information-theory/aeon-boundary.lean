import Mathlib.Data.Set.Basic
import Mathlib.Data.Set.BooleanAlgebra
import Mathlib.Order.Disjoint

/-!
# QOU.AeonBoundary — Boundary of an aeon

The boundary ∂𝒜 = closure(𝒜) ∖ 𝒜° of an aeon: the objects that are
limits of diagrams in the aeon but lie outside the observable
subcategory Bun° (where Γ(𝒮, A₀) = 0).  Each boundary object is a jet
horizon or a big bang state.

LaTeX label: `def:aeon-boundary`

## References
- [penrose2010] R. Penrose, "Cycles of Time", Bodley Head 2010.
- [leitner2026] §9/aeon
-/

namespace QOU

/-- An object of `Bun(ℙ(V))`, abstracted as its index. -/
abbrev BunObject := ℕ

/-- **Boundary of an aeon** `∂𝒜 = closure(𝒜) ∖ 𝒜°`.

    Given the aeon `aeonObjs` (a subset of `Bun°`) and the closure
    `cl` of its directed diagrams inside `Bun(ℙ(V))`, the boundary is
    the set-difference: the limit objects that are not themselves
    observable.  These are the jet horizons / big-bang states with
    `Γ(𝒮, A₀) = 0`. -/
-- Ref: [penrose2010] R. Penrose, "Cycles of Time", Bodley Head 2010.
-- Ref: [leitner2026] §9/aeon
def aeonBoundary (aeonObjs cl : Set BunObject) : Set BunObject :=
  cl \ aeonObjs

/-- A boundary object lies in the closure but not in the aeon. -/
-- Ref: [leitner2026] §9/aeon
theorem mem_aeonBoundary (aeonObjs cl : Set BunObject) (s : BunObject) :
    s ∈ aeonBoundary aeonObjs cl ↔ s ∈ cl ∧ s ∉ aeonObjs :=
  Iff.rfl

/-- The boundary is disjoint from the aeon interior. -/
-- Ref: [leitner2026] §9/aeon
theorem aeonBoundary_disjoint (aeonObjs cl : Set BunObject) :
    Disjoint (aeonBoundary aeonObjs cl) aeonObjs := by
  unfold aeonBoundary
  exact disjoint_sdiff_self_left

end QOU
