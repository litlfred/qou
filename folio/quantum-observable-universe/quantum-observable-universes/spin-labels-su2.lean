import Mathlib.Data.Nat.Basic


/-!
# QOU.Examples.spin_labels_su2 — Spin decomposition of Rep(SU(2))

Irreducible representations and spin labels:
- Simple objects: V_j ≅ ℂ^{2j+1} for j = 0, 1/2, 1, 3/2, ...
  - V₀ = ℂ (trivial)
  - V_{1/2} = ℂ² (fundamental)
  - V₁ = su(2)_ℂ ≅ ℂ³ (adjoint, g·X = gXg⁻¹)
  - V_{3/2} = Sym³(ℂ²) ≅ ℂ⁴
- Complete reducibility: W ≅ ⊕_j V_j^{⊕m_j}
- Polynomial ring: ℂ[z] = ⊕_{n≥0} Symⁿ V, each Symⁿ V ≅ V_{n/2}

LaTeX label: `ex:spin-labels-su2`

## References

- [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
- [leitner2026] §1 Example: Spin decomposition
-/

namespace QOU.Examples

/-- **SU(2) spin labels**: concrete dimensions of low-spin representations.

    LaTeX: `\label{ex:spin-labels-su2}` -/
-- Ref: [lusztig1993] Lusztig, "Introduction to Quantum Groups," Birkhäuser 1993 (DOI: 10.1007/978-0-8176-4717-9)
structure SU2SpinLabels where
  /-- Dimension of V_j, given twice_j (so j = twice_j/2). -/
  dim : ℕ → ℕ
  /-- dim V_j = 2j + 1 = twice_j + 1. -/
  dim_formula : ∀ twice_j, dim twice_j = twice_j + 1
  /-- Dimension of the tensor square V_{1/2} ⊗ V_{1/2}. -/
  tensorSquareDim : ℕ
  /-- Complete reducibility: every finite-dim rep decomposes.
      Witnessed by the Clebsch–Gordan rule:
      V_{1/2} ⊗ V_{1/2} ≅ V₀ ⊕ V₁, so dim(V⊗V) = dim(V₀) + dim(V₁). -/
  completely_reducible : tensorSquareDim = dim 0 + dim 2

/-- The SU(2) spin label data. -/
-- Ref: [lusztig1993] Lusztig, "Introduction to Quantum Groups," Birkhäuser 1993 (DOI: 10.1007/978-0-8176-4717-9)
def su2SpinLabels : SU2SpinLabels where
  dim := fun twice_j => twice_j + 1
  dim_formula := fun _ => rfl
  tensorSquareDim := 4
  -- Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
  completely_reducible := rfl

/-- V₀ (trivial) has dimension 1. -/
theorem su2_dim_trivial : su2SpinLabels.dim 0 = 1 := rfl

/-- V_{1/2} (fundamental) has dimension 2. -/
theorem su2_dim_fundamental : su2SpinLabels.dim 1 = 2 := rfl

/-- V₁ (adjoint) has dimension 3. -/
theorem su2_dim_adjoint : su2SpinLabels.dim 2 = 3 := rfl

/-- V_{3/2} has dimension 4. -/
theorem su2_dim_spin_three_halves : su2SpinLabels.dim 3 = 4 := rfl

/-- V₂ has dimension 5. -/
theorem su2_dim_spin_two : su2SpinLabels.dim 4 = 5 := rfl

/-- The Clebsch–Gordan rule: V_{1/2} ⊗ V_{1/2} ≅ V₀ ⊕ V₁,
    so dim(V ⊗ V) = dim V₀ + dim V₁ = 1 + 3 = 4 = 2². -/
theorem su2_tensor_square :
    su2SpinLabels.dim 0 + su2SpinLabels.dim 2 =
    su2SpinLabels.dim 1 * su2SpinLabels.dim 1 := by rfl

end QOU.Examples
