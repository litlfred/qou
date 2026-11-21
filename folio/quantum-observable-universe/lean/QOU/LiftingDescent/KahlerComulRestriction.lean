/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.RingTheory.Bialgebra.Basic
import Mathlib.RingTheory.Coalgebra.TensorProduct

/-!
# The comultiplication does not restrict to the Kähler differentials

Let `A` be a bialgebra over a commutative ring `R`, and let
`Ω¹(A) = ker (m : A ⊗ A → A)`. Give `A ⊗ A` its tensor-product coalgebra structure.
If `Δ_{A⊗A}` maps `Ω¹(A)` into the image of `Ω¹(A) ⊗ Ω¹(A)`, then `Ω¹(A) = 0`.

Reason: on `A ⊗ A` the counit is `ε ∘ m`, so it vanishes on `Ω¹(A)`, and the counit
law `(id ⊗ ε) Δ x = x ⊗ 1` then forces `x = 0`.

So "Δ restricts to a comultiplication on the jet object" fails for every bialgebra
with `m` not injective, for instance every group algebra `R[G]` of a nontrivial group
(`g ⊗ g⁻¹ − 1 ⊗ 1 ∈ Ω¹`). This refutes Step 2 of the former proof of
`lem:jet-prolongation-categorical-jet`.

No `sorry`, no axiom beyond Lean's three.
-/

namespace QOU.LiftingDescent

open TensorProduct Coalgebra

variable (R A : Type*) [CommRing R] [Ring A] [Bialgebra R A]

/-- The Kähler differentials `Ω¹(A) = ker (m : A ⊗ A → A)`. -/
abbrev kahlerOmega : Submodule R (A ⊗[R] A) := LinearMap.ker (LinearMap.mul' R A)

/-- On `A ⊗ A` the tensor-product counit is `ε ∘ m`. -/
theorem counit_tensor_eq_counit_comp_mul :
    (Coalgebra.counit : A ⊗[R] A →ₗ[R] R) = Coalgebra.counit ∘ₗ LinearMap.mul' R A := by
  ext x y
  simp [Bialgebra.counit_mul, mul_comm]

/-- The counit of `A ⊗ A` vanishes on `Ω¹(A)`. -/
theorem counit_kahlerOmega {x : A ⊗[R] A} (hx : x ∈ kahlerOmega R A) :
    Coalgebra.counit (R := R) x = 0 := by
  rw [counit_tensor_eq_counit_comp_mul, LinearMap.comp_apply, LinearMap.mem_ker.1 hx, map_zero]

/-- **The comultiplication of `A ⊗ A` restricts to `Ω¹(A)` only when `Ω¹(A) = 0`.** -/
theorem kahlerOmega_eq_bot_of_comul_restricts
    (h : ∀ x ∈ kahlerOmega R A, Coalgebra.comul (R := R) x ∈
      LinearMap.range (TensorProduct.map (kahlerOmega R A).subtype (kahlerOmega R A).subtype)) :
    kahlerOmega R A = ⊥ := by
  rw [eq_bot_iff]
  intro x hx
  obtain ⟨y, hy⟩ := h x hx
  have hε : (Coalgebra.counit : A ⊗[R] A →ₗ[R] R) ∘ₗ (kahlerOmega R A).subtype = 0 := by
    ext ⟨z, hz⟩
    exact counit_kahlerOmega R A hz
  have h1 : (Coalgebra.counit (R := R)).lTensor (A ⊗[R] A) (Coalgebra.comul x) = 0 := by
    rw [← hy, LinearMap.lTensor, ← LinearMap.comp_apply, ← TensorProduct.map_comp,
      LinearMap.id_comp, hε, TensorProduct.map_zero_right, LinearMap.zero_apply]
  rw [Coalgebra.lTensor_counit_comul] at h1
  have h2 := congrArg (TensorProduct.rid R (A ⊗[R] A)) h1
  rw [TensorProduct.rid_tmul, one_smul, map_zero] at h2
  rw [Submodule.mem_bot]
  exact h2

/-- Contrapositive: when `Ω¹(A) ≠ 0`, some Kähler differential has its coproduct outside
`Ω¹(A) ⊗ Ω¹(A)`. -/
theorem exists_comul_not_mem_of_kahlerOmega_ne_bot (hne : kahlerOmega R A ≠ ⊥) :
    ∃ x ∈ kahlerOmega R A, Coalgebra.comul (R := R) x ∉
      LinearMap.range (TensorProduct.map (kahlerOmega R A).subtype (kahlerOmega R A).subtype) := by
  by_contra hc
  push_neg at hc
  exact hne (kahlerOmega_eq_bot_of_comul_restricts R A hc)

end QOU.LiftingDescent
