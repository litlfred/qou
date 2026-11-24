import MathlibExt.PermutationEnumeration
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Order.Interval.Finset.Fin
import Mathlib.Tactic.Ring

/-!
# The Poincaré polynomial of `S_n`, for every `n`

For `w ∈ S_n` let `ℓ(w)` be its Coxeter length, the number of inversions
(`QOU.Mathlib.PermutationEnumeration.coxeterLength`). This file proves, over any commutative
semiring `R` and any `q : R`,

    ∑_{w ∈ S_n} q^{ℓ(w)} = ∏_{i < n} (1 + q + ⋯ + q^i) = [n]_q!        (`sum_pow_length`)

which is the right-hand side of the `T_w` Gram computation in `H_n(q)` (bean `qou-em1j`), at every
`n` rather than only `n = 3, 4`.

## Proof

Insertion of a first value. For `p : Fin (n+1)` and `τ ∈ S_n` let `ins p τ ∈ S_{n+1}` send
`0 ↦ p` and `i + 1 ↦ p.succAbove (τ i)`. Then

* `(p, τ) ↦ ins p τ` is a bijection `Fin (n+1) × S_n ≃ S_{n+1}` (`ins_bijective`);
* `ℓ(ins p τ) = p + ℓ(τ)` (`coxeterLength_ins`): the pairs `(0, j+1)` contribute the `p` values
  below `p`, and the pairs `(i+1, j+1)` contribute exactly the inversions of `τ`, because
  `p.succAbove` is strictly monotone.

So the generating function factors as `(∑_{p ≤ n} q^p) · ∑_{τ ∈ S_n} q^{ℓ(τ)}`, and induction on
`n` finishes. This is the Lehmer-code argument.

Generic base ring, no ordering on `R`, no `ℝ`.

-- Ref: [bjornerbrenti2005] A. Björner, F. Brenti, *Combinatorics of Coxeter Groups*, GTM 231,
--   Springer 2005 (the length generating function of a finite Coxeter group; for `S_n` it is
--   `[n]_q!`, proved there through the inversion table, which is the argument used here).
-/

namespace QOU.MathlibExt.SymmetricGroupPoincare

open QOU.Mathlib.PermutationEnumeration Finset

/-! ### Inserting a first value -/

/-- `ins p τ` sends `0 ↦ p` and `i + 1 ↦ p.succAbove (τ i)`. -/
def insFun {n : ℕ} (p : Fin (n + 1)) (τ : Equiv.Perm (Fin n)) : Fin (n + 1) → Fin (n + 1) :=
  Fin.cases p (fun i => p.succAbove (τ i))

@[simp] theorem insFun_zero {n : ℕ} (p : Fin (n + 1)) (τ : Equiv.Perm (Fin n)) :
    insFun p τ 0 = p := rfl

@[simp] theorem insFun_succ {n : ℕ} (p : Fin (n + 1)) (τ : Equiv.Perm (Fin n)) (i : Fin n) :
    insFun p τ i.succ = p.succAbove (τ i) := rfl

theorem insFun_injective {n : ℕ} (p : Fin (n + 1)) (τ : Equiv.Perm (Fin n)) :
    Function.Injective (insFun p τ) := by
  intro a b hab
  induction a using Fin.cases with
  | zero =>
    induction b using Fin.cases with
    | zero => rfl
    | succ j =>
      simp only [insFun_zero, insFun_succ] at hab
      exact absurd hab.symm (Fin.succAbove_ne p (τ j))
  | succ i =>
    induction b using Fin.cases with
    | zero =>
      simp only [insFun_zero, insFun_succ] at hab
      exact absurd hab (Fin.succAbove_ne p (τ i))
    | succ j =>
      simp only [insFun_succ] at hab
      rw [τ.injective (Fin.succAbove_right_injective hab)]

/-- `ins p τ ∈ S_{n+1}`. -/
noncomputable def ins {n : ℕ} (p : Fin (n + 1)) (τ : Equiv.Perm (Fin n)) :
    Equiv.Perm (Fin (n + 1)) :=
  Equiv.ofBijective (insFun p τ) (Finite.injective_iff_bijective.mp (insFun_injective p τ))

@[simp] theorem ins_apply {n : ℕ} (p : Fin (n + 1)) (τ : Equiv.Perm (Fin n)) (i : Fin (n + 1)) :
    ins p τ i = insFun p τ i := rfl

/-- `(p, τ) ↦ ins p τ` is injective. -/
theorem ins_injective {n : ℕ} :
    Function.Injective (fun x : Fin (n + 1) × Equiv.Perm (Fin n) => ins x.1 x.2) := by
  rintro ⟨p, τ⟩ ⟨p', τ'⟩ h
  have h0 := congrArg (fun w : Equiv.Perm (Fin (n + 1)) => w 0) h
  simp only [ins_apply, insFun_zero] at h0
  subst h0
  have hτ : τ = τ' := by
    ext i
    have hi := congrArg (fun w : Equiv.Perm (Fin (n + 1)) => w i.succ) h
    simp only [ins_apply, insFun_succ] at hi
    rw [Fin.succAbove_right_injective hi]
  rw [hτ]

/-- `(p, τ) ↦ ins p τ` is a bijection `Fin (n+1) × S_n → S_{n+1}`. -/
theorem ins_bijective {n : ℕ} :
    Function.Bijective (fun x : Fin (n + 1) × Equiv.Perm (Fin n) => ins x.1 x.2) := by
  rw [Fintype.bijective_iff_injective_and_card]
  refine ⟨ins_injective, ?_⟩
  simp only [Fintype.card_prod, Fintype.card_fin, Fintype.card_perm, Nat.factorial_succ]

/-! ### The length of an insertion -/

/-- The inversion count as a double sum of indicators. -/
theorem coxeterLength_eq_sum {n : ℕ} (w : Equiv.Perm (Fin n)) :
    coxeterLength w = ∑ i : Fin n, ∑ j : Fin n, if i < j ∧ w j < w i then 1 else 0 := by
  unfold coxeterLength
  rw [Finset.card_filter, ← Finset.univ_product_univ, Finset.sum_product]

/-- Exactly `p` elements `v : Fin n` have `v.castSucc < p`. -/
theorem card_castSucc_lt {n : ℕ} (p : Fin (n + 1)) :
    (univ.filter (fun v : Fin n => v.castSucc < p)).card = p := by
  have hmap : (univ.filter (fun v : Fin n => v.castSucc < p)).map Fin.castSuccEmb
      = Finset.Iio p := by
    ext u
    simp only [Finset.mem_map, Finset.mem_filter, Finset.mem_univ, true_and,
      Fin.castSuccEmb_apply, Finset.mem_Iio]
    constructor
    · rintro ⟨v, hv, rfl⟩; exact hv
    · intro hu
      have hne : u ≠ Fin.last n := by
        rintro rfl; exact absurd hu (not_lt.mpr (Fin.le_last p))
      exact ⟨u.castPred hne, by simpa using hu, by simp⟩
  rw [← Finset.card_map, hmap, Fin.card_Iio]

/-- **`ℓ(ins p τ) = p + ℓ(τ)`.** -/
theorem coxeterLength_ins {n : ℕ} (p : Fin (n + 1)) (τ : Equiv.Perm (Fin n)) :
    coxeterLength (ins p τ) = (p : ℕ) + coxeterLength τ := by
  rw [coxeterLength_eq_sum, coxeterLength_eq_sum, Fin.sum_univ_succ]
  congr 1
  · -- the row `i = 0`
    rw [Fin.sum_univ_succ]
    simp only [lt_self_iff_false, false_and, if_false, zero_add, Fin.succ_pos, true_and,
      ins_apply, insFun_zero, insFun_succ, Fin.succAbove_lt_iff_castSucc_lt]
    rw [← Finset.card_filter]
    rw [← card_castSucc_lt p]
    exact Finset.card_bij (fun j _ => τ j)
      (by intro j hj; simpa using hj)
      (by intro a _ b _ h; exact τ.injective h)
      (by intro v hv; exact ⟨τ.symm v, by simpa using hv, by simp⟩)
  · -- the rows `i = i' + 1`
    refine Finset.sum_congr rfl (fun i _ => ?_)
    rw [Fin.sum_univ_succ]
    simp only [Fin.succ_lt_succ_iff, ins_apply, insFun_succ, insFun_zero,
      Fin.succAbove_lt_succAbove_iff, Fin.not_lt_zero, false_and, if_false,
      zero_add]

/-! ### The generating function -/

/-- **The Poincaré polynomial of `S_n`**: `∑_{w ∈ S_n} q^{ℓ(w)} = ∏_{i<n} ∑_{k ≤ i} q^k`. -/
theorem sum_pow_length {R : Type*} [CommSemiring R] (q : R) :
    ∀ n : ℕ, ∑ w : Equiv.Perm (Fin n), q ^ coxeterLength w
      = ∏ i ∈ range n, ∑ k ∈ range (i + 1), q ^ k
  | 0 => by simp [coxeterLength]
  | n + 1 => by
    rw [← ins_bijective.sum_comp (fun w => q ^ coxeterLength w), Fintype.sum_prod_type]
    simp only [coxeterLength_ins, pow_add]
    rw [← Finset.sum_mul_sum, sum_pow_length q n, Finset.prod_range_succ, mul_comm,
      Fin.sum_univ_eq_sum_range (fun k => q ^ k)]

/-- At `q = 1` the identity counts: `|S_n| = n!`. A consistency check on the statement. -/
example (n : ℕ) : ∑ _w : Equiv.Perm (Fin n), (1 : ℕ) ^ 0 = n.factorial := by
  simp [Fintype.card_perm]

/-- **`n = 3`** (bean `qou-em1j`): `∑_{w ∈ S_3} q^{ℓ(w)} = (1 + q)(1 + q + q²)`. -/
theorem sum_pow_length_three {R : Type*} [CommSemiring R] (q : R) :
    ∑ w : Equiv.Perm (Fin 3), q ^ coxeterLength w = (1 + q) * (1 + q + q ^ 2) := by
  rw [sum_pow_length q 3]
  simp only [Finset.prod_range_succ, Finset.sum_range_succ, Finset.prod_range_zero,
    Finset.sum_range_zero]
  ring

/-- **`n = 4`**: `∑_{w ∈ S_4} q^{ℓ(w)} = (1 + q)(1 + q + q²)(1 + q + q² + q³)`. -/
theorem sum_pow_length_four {R : Type*} [CommSemiring R] (q : R) :
    ∑ w : Equiv.Perm (Fin 4), q ^ coxeterLength w
      = (1 + q) * (1 + q + q ^ 2) * (1 + q + q ^ 2 + q ^ 3) := by
  rw [sum_pow_length q 4]
  simp only [Finset.prod_range_succ, Finset.sum_range_succ, Finset.prod_range_zero,
    Finset.sum_range_zero]
  ring

end QOU.MathlibExt.SymmetricGroupPoincare
