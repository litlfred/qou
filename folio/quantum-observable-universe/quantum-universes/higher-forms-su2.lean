import Mathlib.Data.Nat.Basic


/-!
# QOU.Examples.higher_forms_su2 — Higher forms on O(SU(2))

The de Rham complex of left-invariant differential forms on O(SU(2)):
  Ω⁰(A) = A                               (functions, rank 1)
  Ω¹(A) = A ⊗ span{ω₁, ω₂, ω₃}          (1-forms, rank 3)
  Ω²(A) = A ⊗ span{ω₁∧ω₂, ω₁∧ω₃, ω₂∧ω₃} (2-forms, rank 3)
  Ω³(A) = A ⊗ span{ω₁∧ω₂∧ω₃}            (volume form, rank 1)
  Ωᵏ(A) = 0 for k ≥ 4

The Maurer–Cartan equation gives dω_i = −½ε_{ijk} ω_j ∧ ω_k.

LaTeX label: `ex:higher-forms-su2`

## References

- [leitner2026] §1 Example: Higher forms on O(SU(2))
-/

namespace QOU.Examples

/-- **SU(2) differential form data**: dimensions of the graded pieces
    of the de Rham complex on O(SU(2)).

    LaTeX: `\label{ex:higher-forms-su2}` -/
-- Ref: [leitner2026] §1
structure SU2FormDimensions where
  /-- Rank of Ωᵏ(A) as a free left A-module, for each degree k. -/
  rank : ℕ → ℕ
  /-- Ω⁰(A) = A has rank 1. -/
  rank_zero : rank 0 = 1
  /-- Ω¹(A) has rank 3 (three left-invariant 1-forms). -/
  rank_one : rank 1 = 3
  /-- Ω²(A) has rank 3 (three independent 2-forms). -/
  rank_two : rank 2 = 3
  /-- Ω³(A) has rank 1 (the volume form). -/
  rank_three : rank 3 = 1
  /-- Ωᵏ(A) = 0 for k ≥ 4. -/
  rank_high : ∀ k, k ≥ 4 → rank k = 0

/-- The differential form dimensions for SU(2). -/
-- Ref: [leitner2026] §1
def su2FormDims : SU2FormDimensions where
  rank := fun k => match k with
    | 0 => 1
    | 1 => 3
    | 2 => 3
    | 3 => 1
    | _ => 0
  rank_zero := rfl
  rank_one := rfl
  rank_two := rfl
  rank_three := rfl
  rank_high := by
    intro k hk
    obtain ⟨n, rfl⟩ : ∃ n, k = n + 4 := ⟨k - 4, by omega⟩
    rfl

/-- Total dimension: Σ rank(Ωᵏ) = 1 + 3 + 3 + 1 = 8 = 2³. -/
theorem su2_total_form_dim :
    su2FormDims.rank 0 + su2FormDims.rank 1 +
    su2FormDims.rank 2 + su2FormDims.rank 3 = 8 := by rfl

/-- The de Rham complex has length 3 (top form is Ω³). -/
theorem su2_top_degree : su2FormDims.rank 3 = 1 := rfl

end QOU.Examples
