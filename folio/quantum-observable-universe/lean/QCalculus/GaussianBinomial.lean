import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Tactic.LinearCombination
import Mathlib.Algebra.Order.Field.Power
import Mathlib.Tactic.FieldSimp

/-!
# Gaussian binomials over `ℤ`

`gaussG n k = [n+k choose n]_x ∈ ℤ[x]`, built from the q-Pascal recurrence, and the identity
`∏_{j<n}(1 − x^{j+1}) · G_{n,k}(x) = ∏_{j<n}(1 − x^{k+j+1})` over any commutative ring, and its
consequence `clasp_prod_eq` over any field. Nothing here uses the complex numbers or an ordering.

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. IV.2 (Gaussian binomials)
-/

namespace QOU.MathlibExt

open Polynomial Finset

/-! ### The Gaussian binomial -/

/-- The Gaussian binomial `G_{n,k} = [n+k choose n]_x ∈ ℤ[x]`, by the q-Pascal recurrence
`G_{n+1,k+1} = G_{n,k+1} + x^{n+1} G_{n+1,k}`. -/
noncomputable def gaussG : ℕ → ℕ → ℤ[X]
  | 0, _ => 1
  | _ + 1, 0 => 1
  | n + 1, k + 1 => gaussG n (k + 1) + X ^ (n + 1) * gaussG (n + 1) k

/-- **The Gaussian binomial clears the clasp denominators**, over any commutative ring:
`∏_{j<n}(1 − x^{j+1}) · G_{n,k}(x) = ∏_{j<n}(1 − x^{k+j+1})`. -/
theorem prod_mul_gaussG {R : Type*} [CommRing R] (x : R) :
    ∀ n k : ℕ, (∏ j ∈ range n, (1 - x ^ (j + 1))) * (gaussG n k).eval₂ (Int.castRingHom R) x
      = ∏ j ∈ range n, (1 - x ^ (k + j + 1))
  | 0, k => by simp [gaussG]
  | n + 1, 0 => by simp [gaussG]
  | n + 1, k + 1 => by
    have h1 := prod_mul_gaussG x n (k + 1)
    have h2 := prod_mul_gaussG x (n + 1) k
    have hP : ∏ j ∈ range (n + 1), (1 - x ^ (j + 1))
        = (∏ j ∈ range n, (1 - x ^ (j + 1))) * (1 - x ^ (n + 1)) := prod_range_succ _ _
    have hB : ∏ j ∈ range (n + 1), (1 - x ^ (k + j + 1))
        = (∏ j ∈ range n, (1 - x ^ (k + 1 + j + 1))) * (1 - x ^ (k + 1)) := by
      rw [prod_range_succ']
      congr 1
      exact prod_congr rfl fun j _ => by rw [show k + (j + 1) + 1 = k + 1 + j + 1 by omega]
    have hT : ∏ j ∈ range (n + 1), (1 - x ^ (k + 1 + j + 1))
        = (∏ j ∈ range n, (1 - x ^ (k + 1 + j + 1))) * (1 - x ^ (k + 1 + n + 1)) :=
      prod_range_succ _ _
    rw [hP, hB] at h2
    simp only [gaussG, eval₂_add, eval₂_mul, eval₂_X_pow]
    rw [hP, hT]
    linear_combination (1 - x ^ (n + 1)) * h1 + x ^ (n + 1) * h2

/-! ### The clasp product as a Laurent polynomial -/

/-- The clasp product of van der Veen's formula is a Laurent monomial product times the
Gaussian binomial at `t = s²`, wherever its denominators are nonzero. -/
theorem clasp_prod_eq {K : Type*} [Field K] {s : K} {N n k : ℕ}
    (hden : ∀ j ∈ range n, 1 - s ^ (2 * ((j : ℤ) + 1)) ≠ 0) :
    ∏ j ∈ range n,
        (1 - s ^ (2 * ((N : ℤ) - ((j : ℤ) + 1) - k))) * (1 - s ^ (2 * ((j : ℤ) + 1 + k)))
          / (1 - s ^ (2 * ((j : ℤ) + 1)))
      = (∏ j ∈ range n, (1 - s ^ (2 * ((N : ℤ) - ((j : ℤ) + 1) - k))))
          * (gaussG n k).eval₂ (Int.castRingHom K) (s ^ 2) := by
  have hpow : ∀ a : ℕ, s ^ (2 * (a : ℤ)) = (s ^ 2) ^ a := fun a => by
    rw [← zpow_natCast, ← zpow_natCast, ← zpow_mul]; push_cast; ring_nf
  have hD : ∏ j ∈ range n, (1 - (s ^ 2) ^ (j + 1)) ≠ 0 := by
    rw [prod_ne_zero_iff]
    intro j hj
    have := hden j hj
    rwa [show (2 * ((j : ℤ) + 1)) = 2 * ((j + 1 : ℕ) : ℤ) by push_cast; ring, hpow] at this
  rw [prod_div_distrib, prod_mul_distrib, mul_div_assoc]
  congr 1
  rw [div_eq_iff (by
    convert hD using 2 with j hj
    rw [show (2 * ((j : ℤ) + 1)) = 2 * ((j + 1 : ℕ) : ℤ) by push_cast; ring, hpow])]
  have key := prod_mul_gaussG (s ^ 2) n k
  have lhs : ∏ j ∈ range n, (1 - s ^ (2 * ((j : ℤ) + 1 + k)))
      = ∏ j ∈ range n, (1 - (s ^ 2) ^ (k + j + 1)) := by
    refine prod_congr rfl fun j _ => ?_
    rw [show (2 * ((j : ℤ) + 1 + k)) = 2 * ((k + j + 1 : ℕ) : ℤ) by push_cast; ring, hpow]
  have rhs : ∏ j ∈ range n, (1 - s ^ (2 * ((j : ℤ) + 1)))
      = ∏ j ∈ range n, (1 - (s ^ 2) ^ (j + 1)) := by
    refine prod_congr rfl fun j _ => ?_
    rw [show (2 * ((j : ℤ) + 1)) = 2 * ((j + 1 : ℕ) : ℤ) by push_cast; ring, hpow]
  rw [lhs, rhs, ← key, mul_comm]

end QOU.MathlibExt
