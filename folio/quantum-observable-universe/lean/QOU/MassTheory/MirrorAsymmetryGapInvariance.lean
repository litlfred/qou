/-!
# Ordering Invariance of the `c₁` Mirror Asymmetry Across `(P, Q)` with `P - Q = 5`

Bean `qou-z4ba` (`The c1 mirror asymmetry has the WRONG SIGN, 0/230 against AME -- and it is
scale-free`) and `qou-hu1f` (`Atom word ordering: intra_order="grouped" vs "borromean"`).

## Mathematical content

In cleared-denominator integer form (multiplying `c₁(Z, N)` by `2 · 4^A = 2^{2A + 1}`, where
`A = Z + N` and `Z, N ≥ 1` so `I_pp = Z - 1`, `I_nn = N - 1`, and `I_pp - I_nn = Z - N`):

    c1Scaled P Q Z N = (P * Z + Q * N) * (2 ^ A - 2) - 8 * (Z - N)

1. **General `(P, Q)` mirror difference (`c1Scaled_mirror_diff_general`):**
   For any per-nucleon crossing coefficients `(P, Q : Int)` and any `Z, N : Int` at mass
   number `A : Nat`,
   `c1Scaled P Q Z N - c1Scaled P Q N Z = (Z - N) * ((P - Q) * (2 ^ A - 2) - 16)`.

2. **Invariance under `P - Q = 5` (`c1Scaled_mirror_diff_of_gap_five`):**
   Both the historical `grouped` word (`(P, Q) = (21, 16)`) and the canonical `borromean`
   word (`(P, Q) = (3, -2)`) satisfy `P - Q = 5`, so for **both** orderings:
   `c1Scaled P Q Z N - c1Scaled P Q N Z = (Z - N) * (5 * 2 ^ A - 26)`.

3. **Sign flip at `A = 2` vs `A ≥ 3` (`mirrorFactorFive_neg_at_two`, `mirrorFactorFive_pos_of_ge_three`):**
   The scaled mirror bracket `mirrorFactorFive A = 5 * 2 ^ A - 26` is `-6 < 0` at `A = 2`
   and strictly positive (`≥ 14 > 0`) for every `A ≥ 3`.

4. **Repulsive Coulomb threshold (`repulsive_coulomb_flips_scaled_mirror_sign`):**
   Subtracting a charge-dependent repulsive Coulomb term `ΔC` from `E₀ · c1Scaled P Q` flips
   the mirror sign to negative if and only if `ΔC_ZN - ΔC_NZ > E₀ · (Z - N) · (5 · 2^A - 26)`.

All declarations in this module are sorry-free and axiom-free (`0` `sorry`, `0` `axiom`).
-/

namespace QOU.MassTheory

/-- Cleared-denominator leading-order trace coefficient `2 · 4^A · c₁(Z, N)` for `Z, N ≥ 1`
(where `I_pp - I_nn = (Z - 1) - (N - 1) = Z - N`). -/
def c1Scaled (P Q Z N : Int) (A : Nat) : Int :=
  (P * Z + Q * N) * ((2 : Int) ^ A - 2) - 8 * (Z - N)

/-- Cleared-denominator mirror bracket `2 · 4^A · mirrorBracket(A) = (P - Q)(2^A - 2) - 16`. -/
def mirrorFactorGeneral (gap : Int) (A : Nat) : Int :=
  gap * ((2 : Int) ^ A - 2) - 16

/-- Cleared-denominator mirror bracket at `P - Q = 5`: `5 · 2^A - 26`. -/
def mirrorFactorFive (A : Nat) : Int :=
  5 * (2 : Int) ^ A - 26

/-- Helper bilinear antisymmetry identity:
`(P * Z + Q * N) - (P * N + Q * Z) = (Z - N) * (P - Q)`. -/
theorem pq_antisymm (P Q Z N : Int) :
    (P * Z + Q * N) - (P * N + Q * Z) = (Z - N) * (P - Q) := by
  have h1 : (Z - N) * (P - Q) = Z * P - Z * Q - (N * P - N * Q) := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_sub]
  rw [h1, Int.mul_comm Z P, Int.mul_comm Z Q, Int.mul_comm N P, Int.mul_comm N Q]
  omega

/-- **General `(P, Q)` mirror difference (`qou-z4ba`):**
The difference `c1Scaled P Q Z N A - c1Scaled P Q N Z A` depends on `(P, Q)` strictly
through the coefficient gap `P - Q`. -/
theorem c1Scaled_mirror_diff_general (P Q Z N : Int) (A : Nat) :
    c1Scaled P Q Z N A - c1Scaled P Q N Z A =
      (Z - N) * mirrorFactorGeneral (P - Q) A := by
  unfold c1Scaled mirrorFactorGeneral
  have hsub :
      (P * Z + Q * N) * ((2 : Int) ^ A - 2) - (P * N + Q * Z) * ((2 : Int) ^ A - 2) =
        ((P * Z + Q * N) - (P * N + Q * Z)) * ((2 : Int) ^ A - 2) := by
    rw [Int.sub_mul]
  have hmul :
      (Z - N) * ((P - Q) * ((2 : Int) ^ A - 2) - 16) =
        ((Z - N) * (P - Q)) * ((2 : Int) ^ A - 2) - (Z - N) * 16 := by
    rw [Int.mul_sub, Int.mul_assoc]
  rw [hmul, ← pq_antisymm P Q Z N, ← hsub]
  omega

/-- At `gap = 5`, `mirrorFactorGeneral 5 A = mirrorFactorFive A = 5 · 2^A - 26`. -/
theorem mirrorFactorGeneral_five (A : Nat) :
    mirrorFactorGeneral 5 A = mirrorFactorFive A := by
  unfold mirrorFactorGeneral mirrorFactorFive
  have h1 : 5 * ((2 : Int) ^ A - 2) = 5 * (2 : Int) ^ A - 10 := by omega
  have h2 : 5 * (2 : Int) ^ A - 10 - 16 = 5 * (2 : Int) ^ A - 26 := by omega
  omega

/-- **Ordering invariance for any `(P, Q)` with `P - Q = 5` (`qou-z4ba`, `qou-hu1f`):**
Whenever `P - Q = 5`, `c1Scaled P Q Z N A - c1Scaled P Q N Z A = (Z - N) * (5 * 2^A - 26)`. -/
theorem c1Scaled_mirror_diff_of_gap_five (P Q Z N : Int) (A : Nat) (hPQ : P - Q = 5) :
    c1Scaled P Q Z N A - c1Scaled P Q N Z A =
      (Z - N) * mirrorFactorFive A := by
  rw [c1Scaled_mirror_diff_general, hPQ, mirrorFactorGeneral_five]

/-- **Exact equivalence of the historical `(21, 16)` and canonical `(3, -2)` mirror differences:**
Both orderings share `P - Q = 5` (`21 - 16 = 5 = 3 - (-2)`), so their `c₁` mirror differences
coincide identically for all `(Z, N, A)`. -/
theorem c1Scaled_mirror_diff_grouped_eq_borromean (Z N : Int) (A : Nat) :
    c1Scaled 21 16 Z N A - c1Scaled 21 16 N Z A =
      c1Scaled 3 (-2) Z N A - c1Scaled 3 (-2) N Z A ∧
    c1Scaled 3 (-2) Z N A - c1Scaled 3 (-2) N Z A =
      (Z - N) * mirrorFactorFive A := by
  have h1 := c1Scaled_mirror_diff_of_gap_five 21 16 Z N A rfl
  have h2 := c1Scaled_mirror_diff_of_gap_five 3 (-2) Z N A rfl
  exact ⟨by rw [h1, h2], h2⟩

/-- At `A = 2`, `mirrorFactorFive 2 = -6 < 0`. -/
theorem mirrorFactorFive_neg_at_two : mirrorFactorFive 2 = -6 ∧ mirrorFactorFive 2 < 0 := by
  decide

/-- Helper lemma: `(2 : Int) ^ (k + 3) ≥ 8` for all `k : Nat`. -/
theorem two_pow_add_three_ge_eight (k : Nat) : 8 ≤ (2 : Int) ^ (k + 3) := by
  induction k with
  | zero => decide
  | succ k ih =>
    have hpow : (2 : Int) ^ (k + 1 + 3) = (2 : Int) ^ (k + 3) * 2 := by
      rw [Nat.add_right_comm k 1 3, Int.pow_succ]
    omega

/-- For every `A ≥ 3`, `mirrorFactorFive A ≥ 14 > 0`. -/
theorem mirrorFactorFive_pos_of_ge_three (A : Nat) (hA : 3 ≤ A) :
    14 ≤ mirrorFactorFive A ∧ 0 < mirrorFactorFive A := by
  have h8 : 8 ≤ (2 : Int) ^ A := by
    have hk : A - 3 + 3 = A := Nat.sub_add_cancel hA
    have := two_pow_add_three_ge_eight (A - 3)
    rw [hk] at this
    exact this
  unfold mirrorFactorFive
  omega

/-- **Necessary and sufficient repulsive Coulomb threshold (`qou-z4ba`):**
For any `(P, Q)` with `P - Q = 5`, subtracting a repulsive Coulomb energy `ΔC` from
`E₀ · c1Scaled P Q` flips the mirror difference to `< 0` if and only if
`ΔC_ZN - ΔC_NZ > E₀ · ((Z - N) · mirrorFactorFive A)`. -/
theorem repulsive_coulomb_flips_scaled_mirror_sign
    (P Q E0 Z N ΔC_ZN ΔC_NZ : Int) (A : Nat) (hPQ : P - Q = 5) :
    (E0 * c1Scaled P Q Z N A - ΔC_ZN) - (E0 * c1Scaled P Q N Z A - ΔC_NZ) < 0 ↔
      E0 * ((Z - N) * mirrorFactorFive A) < ΔC_ZN - ΔC_NZ := by
  have hdiff := c1Scaled_mirror_diff_of_gap_five P Q Z N A hPQ
  have hmul :
      E0 * c1Scaled P Q Z N A - E0 * c1Scaled P Q N Z A =
        E0 * ((Z - N) * mirrorFactorFive A) := by
    rw [← Int.mul_sub, hdiff]
  omega

end QOU.MassTheory
