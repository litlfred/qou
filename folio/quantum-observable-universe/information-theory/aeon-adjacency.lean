import Mathlib.Data.Set.Basic

/-!
# QOU.AeonAdjacency — Aeon adjacency

Two aeons are adjacent iff their boundaries share a common object:
∂𝒜 ∩ ∂𝒜' ≠ ∅.  The shared boundary object is the terminal horizon of
one aeon and the initial configuration of the next — one cosmological
cycle handing off to the following one.

LaTeX label: `def:aeon-adjacency`

## References
- [penrose2010] R. Penrose, "Cycles of Time", Bodley Head 2010.
- [leitner2026] §9/aeon
-/

namespace QOU

/-- An object of `Bun(ℙ(V))`, abstracted as its index. -/
abbrev AdjBunObject := ℕ

/-- **Aeon adjacency**: two aeons are adjacent iff their boundaries
    intersect.  Given the two boundary sets `b₁`, `b₂`, adjacency is
    the non-emptiness of `b₁ ∩ b₂`. -/
-- Ref: [penrose2010] R. Penrose, "Cycles of Time", Bodley Head 2010.
-- Ref: [leitner2026] §9/aeon
def aeonAdjacent (b₁ b₂ : Set AdjBunObject) : Prop :=
  (b₁ ∩ b₂).Nonempty

/-- Adjacency is symmetric. -/
-- Ref: [leitner2026] §9/aeon
theorem aeonAdjacent_symm {b₁ b₂ : Set AdjBunObject}
    (h : aeonAdjacent b₁ b₂) : aeonAdjacent b₂ b₁ := by
  obtain ⟨x, hx₁, hx₂⟩ := h
  exact ⟨x, hx₂, hx₁⟩

/-- Adjacency exhibits a shared boundary object. -/
-- Ref: [leitner2026] §9/aeon
theorem aeonAdjacent_shared {b₁ b₂ : Set AdjBunObject}
    (h : aeonAdjacent b₁ b₂) : ∃ s, s ∈ b₁ ∧ s ∈ b₂ :=
  h

end QOU
