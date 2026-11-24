/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import MathlibExt.JetModuleSplitting
import Mathlib.LinearAlgebra.Dual.Lemmas
import Mathlib.Algebra.Polynomial.Derivative

/-!
# The jet module `(S ⊗ S)/I²` does not inherit a bialgebra structure

`prop:jet-prolongation` claims that `J¹(A)` inherits a Frobenius–Hopf structure from `A`.
For the jet object `J¹(S) = (S ⊗ S)/I²` of the owner ruling of 2026-11-22 this fails over a
field of characteristic zero.

1. A primitive element whose square is zero vanishes (`eq_zero_of_primitive_sq_eq_zero`):
   `Δ(y²) = 2 y ⊗ y` and `y ⊗ y = 0` forces `y = 0`. Only the multiplicativity of `Δ` at `y`
   is used, not coassociativity, the counit or an antipode.
2. If both jet sections `a ↦ [a ⊗ 1]` and `a ↦ [1 ⊗ a]` intertwine the comultiplications,
   then `[x ⊗ 1 − 1 ⊗ x]` is primitive for each primitive `x`, and its square is zero because
   it lies in `I/I²`. So it vanishes: `x ⊗ 1 − 1 ⊗ x ∈ I²` (`primitive_mem_sq_of_sections`).
3. For `S = k[X]` with `X` primitive (the additive group), `X ⊗ 1 − 1 ⊗ X ∉ I²`: the functional
   `a ⊗ b ↦ a · b'` kills `I²` and sends it to `−1` (`X_tmul_sub_not_mem_sq`). Hence no
   multiplicative `Δ` on `J¹(k[X])` makes both sections compatible (`jet_polynomial_no_bialgebra`).

No `sorry`, no axiom beyond Lean's three.

## References
- [leitner2026] §3 Lifting and Descent
-/

namespace QOU.LiftingDescent

open TensorProduct

section Primitive

variable {k B : Type*} [Field k] [CharZero k] [Ring B] [Algebra k B]

/-- **A square-zero primitive vanishes** in characteristic zero. -/
theorem eq_zero_of_primitive_sq_eq_zero (Δ : B →ₗ[k] B ⊗[k] B) (y : B)
    (hmul : Δ (y * y) = Δ y * Δ y) (hy : Δ y = y ⊗ₜ 1 + 1 ⊗ₜ y) (h2 : y * y = 0) :
    y = 0 := by
  have h : y ⊗ₜ[k] y + y ⊗ₜ[k] y = 0 := by
    have := hmul
    rw [h2, map_zero, hy] at this
    simp only [add_mul, mul_add, Algebra.TensorProduct.tmul_mul_tmul, h2, mul_one, one_mul,
      TensorProduct.zero_tmul, TensorProduct.tmul_zero, zero_add, add_zero] at this
    exact this.symm
  have hyy : y ⊗ₜ[k] y = 0 := by
    rw [← two_smul k] at h
    exact (smul_eq_zero.mp h).resolve_left two_ne_zero
  rw [← Module.forall_dual_apply_eq_zero_iff k y]
  intro φ
  have := congrArg (fun t => TensorProduct.lid k k (TensorProduct.map φ φ t)) hyy
  simp only [TensorProduct.map_tmul, TensorProduct.lid_tmul, smul_eq_mul, map_zero] at this
  exact mul_self_eq_zero.mp this

end Primitive

section Sections

variable (k S : Type*) [Field k] [CharZero k] [CommRing S] [Algebra k S]

/-- The second jet section `a ↦ [1 ⊗ a]`. -/
noncomputable def jetSectionRight : S →ₐ[k] jetModule k S :=
  (Ideal.Quotient.mkₐ k _).comp Algebra.TensorProduct.includeRight

omit [CharZero k] in
theorem tmul_sub_mem_ideal (x : S) :
    (x ⊗ₜ[k] (1 : S) - 1 ⊗ₜ x) ∈ KaehlerDifferential.ideal k S := by
  rw [KaehlerDifferential.ideal, RingHom.mem_ker]
  simp

/-- **If both jet sections intertwine the comultiplications, every primitive `x` has
`x ⊗ 1 − 1 ⊗ x ∈ I²`**, i.e. `dx = 0`. -/
theorem primitive_mem_sq_of_sections
    (Δ : jetModule k S →ₗ[k] jetModule k S ⊗[k] jetModule k S)
    (hmul : ∀ a b, Δ (a * b) = Δ a * Δ b)
    (ΔS : S →ₗ[k] S ⊗[k] S)
    (hl : ∀ a, Δ (jetSection k S a) =
      TensorProduct.map (jetSection k S).toLinearMap (jetSection k S).toLinearMap (ΔS a))
    (hr : ∀ a, Δ (jetSectionRight k S a) =
      TensorProduct.map (jetSectionRight k S).toLinearMap (jetSectionRight k S).toLinearMap (ΔS a))
    (x : S) (hx : ΔS x = x ⊗ₜ 1 + 1 ⊗ₜ x) :
    (x ⊗ₜ[k] (1 : S) - 1 ⊗ₜ x) ∈ KaehlerDifferential.ideal k S ^ 2 := by
  set y : jetModule k S := jetSection k S x - jetSectionRight k S x with hydef
  have hy_mk : y = Ideal.Quotient.mk _ (x ⊗ₜ[k] (1 : S) - 1 ⊗ₜ x) := by
    rw [hydef, RingHom.map_sub]
    simp only [jetSection, jetSectionRight, AlgHom.comp_apply, Ideal.Quotient.mkₐ_eq_mk,
      Algebra.TensorProduct.includeLeft_apply, Algebra.TensorProduct.includeRight_apply]
  have hsq : y * y = 0 := by
    rw [hy_mk, ← RingHom.map_mul, Ideal.Quotient.eq_zero_iff_mem, ← pow_two]
    exact Ideal.pow_mem_pow (tmul_sub_mem_ideal k S x) 2
  have hprim : Δ y = y ⊗ₜ 1 + 1 ⊗ₜ y := by
    rw [hydef, map_sub, hl, hr, hx]
    simp only [map_add, TensorProduct.map_tmul, AlgHom.toLinearMap_apply, map_one,
      TensorProduct.sub_tmul, TensorProduct.tmul_sub]
    abel
  have := eq_zero_of_primitive_sq_eq_zero Δ y (hmul y y) hprim hsq
  rw [hy_mk, Ideal.Quotient.eq_zero_iff_mem] at this
  exact this

end Sections

section Derivation

variable {R S : Type*} [CommRing R] [CommRing S] [Algebra R S]

/-- The functional `a ⊗ b ↦ a · D b` attached to a linear map `D`. -/
noncomputable def derivFunctional (D : S →ₗ[R] S) : S ⊗[R] S →ₗ[R] S :=
  TensorProduct.lift ((LinearMap.mul R S).compl₂ D)

theorem derivFunctional_mul (D : S →ₗ[R] S) (hD : ∀ a b, D (a * b) = a * D b + b * D a)
    (y z : S ⊗[R] S) :
    derivFunctional D (y * z) =
      LinearMap.mul' R S y * derivFunctional D z + LinearMap.mul' R S z * derivFunctional D y := by
  induction y using TensorProduct.induction_on with
  | zero => simp
  | add y₁ y₂ h₁ h₂ => simp only [add_mul, map_add, h₁, h₂]; ring
  | tmul a b =>
    induction z using TensorProduct.induction_on with
    | zero => simp
    | add z₁ z₂ h₁ h₂ => simp only [mul_add, map_add, h₁, h₂]; ring
    | tmul c d =>
      simp only [Algebra.TensorProduct.tmul_mul_tmul, derivFunctional, TensorProduct.lift.tmul,
        LinearMap.compl₂_apply, LinearMap.mul_apply', LinearMap.mul'_apply, hD]
      ring

/-- `a ⊗ b ↦ a · D b` vanishes on `I²` when `D` is a derivation. -/
theorem derivFunctional_eq_zero_of_mem_sq (D : S →ₗ[R] S)
    (hD : ∀ a b, D (a * b) = a * D b + b * D a) {t : S ⊗[R] S}
    (ht : t ∈ KaehlerDifferential.ideal R S ^ 2) : derivFunctional D t = 0 := by
  rw [pow_two] at ht
  refine Submodule.mul_induction_on ht ?_ ?_
  · intro m hm n hn
    have hm' : LinearMap.mul' R S m = 0 := by
      have := (RingHom.mem_ker).mp hm
      simpa using this
    have hn' : LinearMap.mul' R S n = 0 := by
      have := (RingHom.mem_ker).mp hn
      simpa using this
    rw [derivFunctional_mul D hD, hm', hn']; ring
  · intro a b ha hb; rw [map_add, ha, hb, add_zero]

end Derivation

section Polynomial

open Polynomial

variable (k : Type*) [Field k] [CharZero k]

/-- **`dX ≠ 0`**: `X ⊗ 1 − 1 ⊗ X ∉ I²` in `k[X] ⊗ k[X]`. -/
theorem X_tmul_sub_not_mem_sq :
    (X ⊗ₜ[k] (1 : k[X]) - 1 ⊗ₜ X) ∉ KaehlerDifferential.ideal k k[X] ^ 2 := by
  intro h
  have hD : ∀ a b : k[X], derivative (a * b) = a * derivative b + b * derivative a := by
    intro a b; rw [derivative_mul]; ring
  have := derivFunctional_eq_zero_of_mem_sq (R := k) (derivative : k[X] →ₗ[k] k[X]) hD h
  simp [derivFunctional] at this

/-- **No bialgebra structure on `J¹(k[X])` is compatible with both jet sections**, when `X`
is primitive. -/
theorem jet_polynomial_no_bialgebra
    (Δ : jetModule k k[X] →ₗ[k] jetModule k k[X] ⊗[k] jetModule k k[X])
    (hmul : ∀ a b, Δ (a * b) = Δ a * Δ b)
    (ΔS : k[X] →ₗ[k] k[X] ⊗[k] k[X]) (hX : ΔS X = X ⊗ₜ 1 + 1 ⊗ₜ X)
    (hl : ∀ a, Δ (jetSection k k[X] a) =
      TensorProduct.map (jetSection k k[X]).toLinearMap (jetSection k k[X]).toLinearMap (ΔS a))
    (hr : ∀ a, Δ (jetSectionRight k k[X] a) =
      TensorProduct.map (jetSectionRight k k[X]).toLinearMap
        (jetSectionRight k k[X]).toLinearMap (ΔS a)) : False :=
  X_tmul_sub_not_mem_sq k (primitive_mem_sq_of_sections k k[X] Δ hmul ΔS hl hr X hX)

end Polynomial

end QOU.LiftingDescent
