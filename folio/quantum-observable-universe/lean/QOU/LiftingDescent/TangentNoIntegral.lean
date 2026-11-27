/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.DualNumber
import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Algebra.Polynomial.Taylor
import Mathlib.RingTheory.TensorProduct.Basic
import Mathlib.RingTheory.TensorProduct.Maps

/-!
# The additive group has no invariant integral in characteristic zero

`prop:jet-prolongation` needs a Frobenius form on the tangent algebra
`T(A) = Sym_A(Ω¹)`. For `A = 𝒪(G)` with `G` compact, the form on `A` is the Haar
integral. The tangent group `TG = G ⋉ 𝔤` contains the vector group `𝔤`, and the
coordinate algebra of the additive group is `k[X]` with `Δ X = X ⊗ 1 + 1 ⊗ X`.

This file proves that `k[X]` with that coproduct has no nonzero left integral when
`k` has characteristic zero:

* `integral_comp_derivative`: a left integral `λ`, meaning `(id ⊗ λ) Δ p = λ(p) · 1`,
  kills every derivative, `λ(p') = 0`. The proof sends the first tensor factor to
  the dual numbers, `X ↦ ε`, and uses `p(X + ε) = p(X) + ε p'(X)`.
* `eq_zero_of_comp_derivative`: in characteristic zero, a functional killing every
  derivative is zero, since `X^n = (X^(n+1))' / (n+1)`.
* `additive_no_integral`: the two together.

No `sorry`, no axiom beyond Lean's three.

## References
- [leitner2026] §3 Lifting and Descent
-/

namespace QOU.LiftingDescent

open Polynomial TensorProduct DualNumber

variable {k : Type*} [CommRing k]

/- Lean 4.35 port: `Algebra.TensorProduct.tmul_mul_tmul` now asks for
`IsScalarTower k k[ε] k[ε]` and `SMulCommClass k k[ε] k[ε]`, which instance search does
not find at this Mathlib (`TrivSqZeroExt.smul` vs `Algebra.toSMul`). Both are `Prop`s,
supplied here from the `Algebra` laws. -/
private instance : IsScalarTower k k[ε] k[ε] := ⟨fun a b c => Algebra.smul_mul_assoc a b c⟩
private instance : SMulCommClass k k[ε] k[ε] := ⟨fun a b c => (Algebra.mul_smul_comm a b c).symm⟩

/-- The additive coproduct `Δ p = p(X ⊗ 1 + 1 ⊗ X)` on `k[X]`. -/
noncomputable def addComul : k[X] →ₐ[k] k[X] ⊗[k] k[X] :=
  Polynomial.aeval (X ⊗ₜ[k] (1 : k[X]) + (1 : k[X]) ⊗ₜ[k] X)

/-- The algebra map `k[X] → k[ε]`, `X ↦ ε`. -/
noncomputable def evEps : k[X] →ₐ[k] k[ε] := Polynomial.aeval ε

/-- `evEps ⊗ id`. -/
noncomputable def evEpsTensor : k[X] ⊗[k] k[X] →ₐ[k] k[ε] ⊗[k] k[X] :=
  Algebra.TensorProduct.map evEps (AlgHom.id k k[X])

lemma aeval_one_tmul_X (q : k[X]) :
    Polynomial.aeval ((1 : k[ε]) ⊗ₜ[k] (X : k[X])) q = (1 : k[ε]) ⊗ₜ[k] q := by
  have := Polynomial.aeval_algHom_apply
    (Algebra.TensorProduct.includeRight : k[X] →ₐ[k] k[ε] ⊗[k] k[X]) X q
  rw [Polynomial.aeval_X_left_apply] at this
  exact this

lemma evEpsTensor_comp_addComul :
    (evEpsTensor (k := k)).comp addComul =
      Polynomial.aeval (ε ⊗ₜ[k] (1 : k[X]) + (1 : k[ε]) ⊗ₜ[k] X) := by
  apply Polynomial.algHom_ext
  rw [AlgHom.comp_apply, addComul, Polynomial.aeval_X, Polynomial.aeval_X, map_add,
    evEpsTensor, Algebra.TensorProduct.map_tmul, Algebra.TensorProduct.map_tmul]
  simp only [evEps, Polynomial.aeval_X, map_one, AlgHom.id_apply]

lemma aeval_eps_add (p : k[X]) :
    Polynomial.aeval (ε ⊗ₜ[k] (1 : k[X]) + (1 : k[ε]) ⊗ₜ[k] X) p =
      (1 : k[ε]) ⊗ₜ[k] p + ε ⊗ₜ[k] derivative p := by
  have hsq : (ε ⊗ₜ[k] (1 : k[X]) : k[ε] ⊗[k] k[X]) ^ 2 = 0 := by
    rw [pow_two, Algebra.TensorProduct.tmul_mul_tmul, eps_mul_eps, zero_tmul]
  have key := Polynomial.eval_add_of_sq_eq_zero
    (p.map (algebraMap k (k[ε] ⊗[k] k[X]))) ((1 : k[ε]) ⊗ₜ[k] X) (ε ⊗ₜ[k] (1 : k[X])) hsq
  rw [add_comm, Polynomial.aeval_def, ← Polynomial.eval_map, key, Polynomial.derivative_map,
    Polynomial.eval_map, Polynomial.eval_map, ← Polynomial.aeval_def, ← Polynomial.aeval_def,
    aeval_one_tmul_X, aeval_one_tmul_X, Algebra.TensorProduct.tmul_mul_tmul, one_mul, mul_one]

lemma evEpsTensor_addComul (p : k[X]) :
    evEpsTensor (addComul p) = (1 : k[ε]) ⊗ₜ[k] p + ε ⊗ₜ[k] derivative p := by
  rw [← aeval_eps_add, ← evEpsTensor_comp_addComul, AlgHom.comp_apply]

lemma map_snd_evEpsTensor (lam : k[X] →ₗ[k] k) (y : k[X] ⊗[k] k[X]) :
    TensorProduct.map (TrivSqZeroExt.sndHom k k) lam (evEpsTensor y) =
      LinearMap.rTensor k ((TrivSqZeroExt.sndHom k k) ∘ₗ (evEps (k := k)).toLinearMap)
        (LinearMap.lTensor k[X] lam y) := by
  induction y using TensorProduct.induction_on with
  | zero => simp only [map_zero]
  | tmul a b =>
    rw [evEpsTensor, Algebra.TensorProduct.map_tmul, TensorProduct.map_tmul,
      LinearMap.lTensor_tmul, LinearMap.rTensor_tmul, AlgHom.id_apply]
    rfl
  | add a b ha hb => simp only [map_add, ha, hb]

/-- A functional is killed by every derivative if it is a left integral for the
additive coproduct. -/
theorem integral_comp_derivative (lam : k[X] →ₗ[k] k)
    (hint : ∀ p, LinearMap.lTensor k[X] lam (addComul p) = (1 : k[X]) ⊗ₜ[k] lam p)
    (p : k[X]) : lam (derivative p) = 0 := by
  have h3 := map_snd_evEpsTensor lam (addComul p)
  rw [hint p, evEpsTensor_addComul, map_add, TensorProduct.map_tmul, TensorProduct.map_tmul,
    LinearMap.rTensor_tmul] at h3
  have hs1 : TrivSqZeroExt.sndHom k k (1 : k[ε]) = 0 := rfl
  have hs2 : TrivSqZeroExt.sndHom k k (ε : k[ε]) = 1 := rfl
  have hs3 : ((TrivSqZeroExt.sndHom k k) ∘ₗ (evEps (k := k)).toLinearMap) 1 = 0 := by
    rw [LinearMap.comp_apply, AlgHom.toLinearMap_apply, map_one]; exact hs1
  rw [hs1, hs2, hs3, zero_tmul, zero_add] at h3
  have h4 := congrArg (TensorProduct.lid k k) h3
  rw [TensorProduct.lid_tmul, one_smul, map_zero] at h4
  exact h4

/-- In characteristic zero, a functional on `k[X]` that kills every derivative is zero. -/
theorem eq_zero_of_comp_derivative [IsDomain k] [CharZero k] (lam : k[X] →ₗ[k] k)
    (h : ∀ p, lam (derivative p) = 0) : lam = 0 := by
  have hX : ∀ n : ℕ, lam (X ^ n) = 0 := by
    intro n
    have := h (X ^ (n + 1))
    rw [derivative_X_pow, Polynomial.C_mul', map_smul, smul_eq_mul, Nat.add_sub_cancel] at this
    rcases mul_eq_zero.mp this with h0 | h0
    · exact absurd h0 (by exact_mod_cast Nat.succ_ne_zero n)
    · exact h0
  ext n
  simp [← Polynomial.X_pow_eq_monomial, hX]

/-- **No left integral on the additive group in characteristic zero.** A left integral
for `Δ X = X ⊗ 1 + 1 ⊗ X` on `k[X]` is zero. -/
theorem additive_no_integral [IsDomain k] [CharZero k] (lam : k[X] →ₗ[k] k)
    (hint : ∀ p, LinearMap.lTensor k[X] lam (addComul p) = (1 : k[X]) ⊗ₜ[k] lam p) :
    lam = 0 :=
  eq_zero_of_comp_derivative lam (integral_comp_derivative lam hint)

end QOU.LiftingDescent
