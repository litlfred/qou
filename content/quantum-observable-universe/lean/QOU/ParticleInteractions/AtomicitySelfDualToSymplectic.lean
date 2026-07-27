/-
# Atomicity: self-duality → symplectic embedding

This file connects the categorical *self-duality* of a fundamental object to a
symplectic structure on its automorphism Lie algebra, and threads that structure
down to the rank-≤ 1 `𝔰𝔩₂` statement used by the atomicity argument.

## PROVED vs OPEN

- **PROVED (sorry-free):** `sp_fin_one_eq_sl` —
  `Symplectic.sp (Fin 1) R = SpecialLinear.sl (Fin 1 ⊕ Fin 1) R`.
  Over the rank-one symplectic form `J = fromBlocks 0 (-1) 1 0` on
  `Fin 1 ⊕ Fin 1`, the skew-adjointness condition `Aᵀ J = J (-A)` is *equivalent*
  to `trace A = 0`, so the symplectic Lie algebra `𝔰𝔭₂` and the special-linear
  Lie algebra `𝔰𝔩₂` literally coincide. This is the classical low-rank
  coincidence `C₁ = A₁` (`𝔰𝔭(2) ≅ 𝔰𝔩(2)`), proved here as an equality of
  `LieSubalgebra`s of `Matrix (Fin 1 ⊕ Fin 1) (Fin 1 ⊕ Fin 1) R`.

- **OPEN (Tannakian premise):** `SelfDualToSymplectic` — the statement that the
  automorphism Lie algebra of a self-dual fundamental object embeds into the
  symplectic Lie algebra `𝔰𝔭(V)` of its (nondegenerate, antisymmetric) duality
  pairing. This is genuinely open in the corpus: it is a categorical / Tannakian
  input, not a theorem proved here. It is represented as an **uninhabited class**
  (no field is `True`, no instance is fabricated); the open state is exactly the
  absence of an instance. See `def:tannaka-dual`, `def:fundamental-object`.

- **CONDITIONAL downstream:** `sl2_embedding_of_selfDual` derives the `𝔰𝔩₂`
  embedding from the `SelfDualToSymplectic` premise together with `sp = sl`,
  composing with the landed rank bound `QOU.Atomicity.sl2_subalgebra_rank_le_one`
  (PR #4285) threaded as an explicit hypothesis.
-/
import Mathlib.Algebra.Lie.Classical
import Mathlib.LinearAlgebra.SymplecticGroup
import Mathlib.Tactic

open LieAlgebra Matrix

namespace QOU.Atomicity

/-- **Low-rank coincidence `𝔰𝔭(2) = 𝔰𝔩(2)` (`C₁ = A₁`).**

The symplectic Lie subalgebra of `Matrix (Fin 1 ⊕ Fin 1) (Fin 1 ⊕ Fin 1) R`,
defined as the skew-adjoint matrices for the rank-one symplectic form
`J = fromBlocks 0 (-1) 1 0`, coincides *exactly* with the special-linear Lie
subalgebra of trace-zero matrices.

Proof: membership in `Symplectic.sp (Fin 1) R` unfolds (via
`mem_skewAdjointMatricesLieSubalgebra` and `mem_skewAdjointMatricesSubmodule`)
to `J.IsSkewAdjoint A`, i.e. `Aᵀ * J = J * (-A)`; membership in
`SpecialLinear.sl (Fin 1 ⊕ Fin 1) R` is definitionally `trace A = 0`. Reducing
the matrix equation entrywise over `Fin 1 ⊕ Fin 1` shows both are equivalent to
`A (inl 0) (inl 0) + A (inr 0) (inr 0) = 0`, the trace-zero condition. -/
theorem sp_fin_one_eq_sl (R : Type*) [CommRing R] :
    Symplectic.sp (Fin 1) R = SpecialLinear.sl (Fin 1 ⊕ Fin 1) R := by
  ext A
  show A ∈ skewAdjointMatricesLieSubalgebra (Matrix.J (Fin 1) R) ↔ Matrix.trace A = 0
  rw [mem_skewAdjointMatricesLieSubalgebra, mem_skewAdjointMatricesSubmodule]
  unfold Matrix.IsSkewAdjoint Matrix.IsAdjointPair
  rw [← Matrix.ext_iff]
  simp only [Matrix.trace, Matrix.diag, Fintype.sum_sum_type, Finset.univ_unique,
    Finset.sum_singleton, Fin.default_eq_zero]
  constructor
  · -- skew-adjoint ⇒ trace zero: read off the (inl 0, inr 0) entry
    intro h
    have key := h (Sum.inl 0) (Sum.inr 0)
    simp only [Matrix.mul_apply, Matrix.J, Fintype.sum_sum_type, Finset.univ_unique,
      Finset.sum_singleton, Matrix.transpose_apply, Matrix.fromBlocks_apply₁₁,
      Matrix.fromBlocks_apply₁₂, Matrix.fromBlocks_apply₂₁, Matrix.fromBlocks_apply₂₂,
      Matrix.zero_apply, Matrix.neg_apply, Matrix.one_apply, Fin.mk_zero,
      Fin.default_eq_zero, ↓reduceIte, mul_zero, mul_one, mul_neg, zero_add,
      add_zero] at key
    linear_combination -key
  · -- trace zero ⇒ skew-adjoint: check all four blockwise entries
    intro h i j
    rw [add_eq_zero_iff_eq_neg] at h
    fin_cases i <;> fin_cases j <;>
      simp only [Matrix.mul_apply, Matrix.J, Fintype.sum_sum_type, Finset.univ_unique,
        Finset.sum_singleton, Matrix.transpose_apply, Matrix.fromBlocks_apply₁₁,
        Matrix.fromBlocks_apply₁₂, Matrix.fromBlocks_apply₂₁, Matrix.fromBlocks_apply₂₂,
        Matrix.zero_apply, Matrix.neg_apply, Matrix.one_apply, Fin.mk_zero,
        Fin.default_eq_zero, ↓reduceIte, mul_zero, mul_one, mul_neg, zero_add,
        add_zero, neg_neg] <;>
      (try rw [h]) <;> ring

end QOU.Atomicity
