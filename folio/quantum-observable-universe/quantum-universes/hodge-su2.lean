import Mathlib.Data.Nat.Basic


/-!
# QOU.Examples.hodge_su2 — Hodge star on O(SU(2))

The Hodge star operator on the 3D differential algebra of O(SU(2)):
- Volume form: vol = ω₁ ∧ ω₂ ∧ ω₃ with ∫_A(vol) = 1
- ⋆1 = vol,  ⋆vol = 1
- On 1-forms: ⋆ω_i = ½ε_{ijk} ω_j ∧ ω_k
- On 2-forms: ⋆(ω_i ∧ ω_j) = ε_{ijk} ω_k
- ⋆ is an involution: ⋆² = id (in odd dimension)

In 3D the Hodge star maps Ω¹ → Ω² and Ω² → Ω¹ (not self-maps),
There is no non-trivial self-dual/anti-self-dual decomposition.
The self-dual decomposition becomes non-trivial in the 4D archimedean
case (dim_ℝ H = 4).

LaTeX label: `ex:hodge-su2`

## References

- [leitner2026] §1 Example: Hodge star on O(SU(2))

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Examples

/-- **SU(2) Hodge star data**: the involutive Hodge operator on the
    3-dimensional de Rham complex.

    LaTeX: `\label{ex:hodge-su2}` -/
-- Ref: [leitner2026] §1
structure SU2HodgeData where
  /-- The manifold dimension (for SU(2): dim = 3). -/
  manifoldDim : ℕ
  /-- SU(2) is 3-dimensional. -/
  dim_three : manifoldDim = 3
  /-- ⋆ maps Ωᵏ → Ω^{n−k}: the target degree of ⋆ on k-forms. -/
  hodgeTarget : ℕ → ℕ
  /-- ⋆ maps Ω⁰ → Ω³. -/
  target_zero : hodgeTarget 0 = 3
  /-- ⋆ maps Ω¹ → Ω². -/
  target_one : hodgeTarget 1 = 2
  /-- ⋆ maps Ω² → Ω¹. -/
  target_two : hodgeTarget 2 = 1
  /-- ⋆ maps Ω³ → Ω⁰. -/
  target_three : hodgeTarget 3 = 0
  /-- ⋆² = id (involutivity): applying hodge twice returns to the same
      degree, for every valid form-degree `k ≤ 3 = manifoldDim` of the
      de Rham complex. (⋆ is only defined on `Ωᵏ` for `0 ≤ k ≤ 3`.) -/
  involutive : ∀ k, k ≤ 3 → hodgeTarget (hodgeTarget k) = k

/-- The Hodge star data for SU(2). -/
-- Ref: [leitner2026] §1
def su2Hodge : SU2HodgeData where
  manifoldDim := 3
  dim_three := rfl
  hodgeTarget := fun k => 3 - k
  target_zero := rfl
  target_one := rfl
  target_two := rfl
  target_three := rfl
  involutive := fun k hk => by omega

/-- Hodge star on a 3-manifold maps Ω¹ to Ω². -/
theorem su2_hodge_one_to_two : su2Hodge.hodgeTarget 1 = 2 := rfl

end QOU.Examples
