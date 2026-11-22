import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Logic.Equiv.Fin.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.LinearCombination

/-!
# `hol − 1` is the Temperley–Lieb part of the mass identity's state sum

`def:mass-identity` expands each crossing transport as `T(σ_a^{±1}) = q^{±1}·1 − e_a` and the
ordered holonomy `hol = T(ℓ₁) ⋯ T(ℓ_k)` as a sum over states `s ∈ {0,1}^k`, choosing the scalar
`c(ℓ_j)·1` (state 0) or `−e_{a_j}` (state 1) at each crossing, in order.

For `V³ = (σ₀σ₁⁻¹)³` the all-zero state is `(q·q⁻¹)³·1 = 1`, so

  `hol − 1 = Σ_{s ≠ 0} (state term s)`,

the sum of the states with at least one Temperley–Lieb generator. Stated over any `R`-algebra
`A` (noncommutative), with `e₀ e₁ : A` arbitrary. No empirical input.

This is evidence for the *reading* `∇ = hol − 1`; it does not prove that the `∇` of the
q-connection equals `hol − 1`.
-/

namespace QOU.MassTheory.HolonomyTLStateSum

open BigOperators

variable {A : Type*} [Ring A]

/-- Ordered expansion of a product of binomials over `{0,1}^n` (noncommutative). -/
theorem ofFn_prod_add_eq_sum (n : ℕ) (a b : Fin n → A) :
    (List.ofFn fun j => a j + b j).prod =
      ∑ s : Fin n → Bool, (List.ofFn fun j => if s j then b j else a j).prod := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [List.ofFn_succ, List.prod_cons, ih (fun j => a j.succ) (fun j => b j.succ),
      ← (Fin.consEquiv fun _ => Bool).sum_comp, Fintype.sum_prod_type, Fintype.sum_bool,
      add_mul, Finset.mul_sum, Finset.mul_sum, add_comm]
    simp [Fin.consEquiv, List.ofFn_succ]

variable {R : Type*} [CommRing R] [Algebra R A]

/-- The six crossings of `(σ₀σ₁⁻¹)³`: scalar part `c j` and Temperley–Lieb part `E j`. -/
def c (q qi : R) (j : Fin 6) : A := algebraMap R A (if (j : ℕ) % 2 = 0 then q else qi)

def E (e₀ e₁ : A) (j : Fin 6) : A := if (j : ℕ) % 2 = 0 then e₀ else e₁

/-- The state term of `s`: the ordered product choosing `c j` (state 0) or `−E j` (state 1). -/
def stateTerm (q qi : R) (e₀ e₁ : A) (s : Fin 6 → Bool) : A :=
  (List.ofFn fun j => if s j then -E e₀ e₁ j else c q qi j).prod

/-- The holonomy of `(σ₀σ₁⁻¹)³` with `T(σ₀) = q·1 − e₀`, `T(σ₁⁻¹) = q⁻¹·1 − e₁`. -/
def hol (q qi : R) (e₀ e₁ : A) : A :=
  ((algebraMap R A q - e₀) * (algebraMap R A qi - e₁)) ^ 3

theorem hol_eq_stateSum (q qi : R) (e₀ e₁ : A) :
    hol q qi e₀ e₁ = ∑ s : Fin 6 → Bool, stateTerm q qi e₀ e₁ s := by
  have h := ofFn_prod_add_eq_sum 6 (c q qi) (fun j => -E e₀ e₁ j)
  simp only [stateTerm]
  rw [← h]
  simp [hol, List.ofFn_succ, c, E, sub_eq_add_neg, pow_succ, mul_assoc]

theorem stateTerm_zero (q qi : R) (hq : q * qi = 1) (e₀ e₁ : A) :
    stateTerm q qi e₀ e₁ (fun _ => false) = 1 := by
  simp only [stateTerm, c, List.ofFn_succ, List.ofFn_zero, List.prod_cons, List.prod_nil,
    Bool.false_eq_true, if_false, Fin.val_zero, Fin.val_succ]
  norm_num
  simp only [← map_mul]
  rw [← map_one (algebraMap R A)]
  congr 1
  linear_combination (q ^ 2 * qi ^ 2 + q * qi + 1) * hq

/-- **`hol − 1` is the sum of the states with at least one Temperley–Lieb generator.** -/
theorem hol_sub_one_eq_TL_states (q qi : R) (hq : q * qi = 1) (e₀ e₁ : A) :
    hol q qi e₀ e₁ - 1 =
      ∑ s ∈ (Finset.univ.erase fun _ => false), stateTerm q qi e₀ e₁ s := by
  rw [hol_eq_stateSum, ← Finset.add_sum_erase _ _ (Finset.mem_univ (fun _ => false)),
    stateTerm_zero q qi hq, add_sub_cancel_left]

end QOU.MassTheory.HolonomyTLStateSum
