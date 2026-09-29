import QOU.Hecke.H2GramArithmetic

/-!
# QOU.Hecke.H3GramArithmetic — the n=3 Gram-determinant target, arithmetic core

Brick `qou-bnhe` (arithmetic anchor), following `H2GramArithmetic` at the
next rank.  The Iwahori–Hecke algebra `H_3(q)` is `6`-dimensional
(basis `{T_w : w ∈ S_3}`, `|S_3| = 3! = 6`) and — unlike `H_2(q)` — is
**not monogenic**: it has two generators `σ₁, σ₂` with the braid relation
`σ₁σ₂σ₁ = σ₂σ₁σ₂`, and Wedderburn-decomposes as
`M₁ ⊕ M₂ ⊕ M₁` over the partitions `(3), (21), (111)` of `3`
(`1² + 2² + 1² = 6`).

This file settles the **arithmetic** the eventual `T_w`-basis Gram
determinant must reproduce (brick `qou-twwf` at `n = 3`):

  `[3]_q  = 1 + q + q²`,
  `[3]_q! = (1 + q)(1 + q + q²) = 1 + 2q + 2q² + q³`,   and
  `[3]_q! ≠ 0  ⟺  q ≠ -1  ∧  q² + q + 1 ≠ 0`  (Wenzl-generic at rank 3).

The matrix-level `det(Gram) = [3]_q!` (up to a unit) needs the `6`-dim
regular representation of the two-generator braid algebra — the remaining
deep piece of `qou-bnhe`.  The arithmetic that computation must land on is
proved here, sorry-free over a field.
-/

namespace QOU.Hecke

open QOU.MathlibExt

variable {K : Type*} [Field K]

/-- `[3]_q = 1 + q + q²` (sorry-free). -/
theorem qInt_three (q : K) : qInt q 3 = 1 + q + q ^ 2 := by
  simp [qInt, Finset.sum_range_succ]

/-- `[3]_q! = (1 + q)(1 + q + q²)` (sorry-free). -/
theorem qFactorial_three (q : K) :
    qFactorial q 3 = (1 + q) * (1 + q + q ^ 2) := by
  rw [qFactorial, Finset.prod_range_succ, Finset.prod_range_succ,
    Finset.prod_range_succ, Finset.prod_range_zero]
  simp only [qInt, Finset.sum_range_succ, Finset.sum_range_zero]
  ring

/-- **`[3]_q!` in expanded form (sorry-free):** `1 + 2q + 2q² + q³`. -/
theorem qFactorial_three_expand (q : K) :
    qFactorial q 3 = 1 + 2 * q + 2 * q ^ 2 + q ^ 3 := by
  rw [qFactorial_three]; ring

/-- **The `n = 3` Wenzl-genericity split (sorry-free).**  `[3]_q! ≠ 0` iff
    `q` is neither a root of `1 + x` nor of `1 + x + x²` — i.e. `q ≠ -1`
    and `q` is not a primitive cube root of unity.  This is the concrete
    `n = 3` content of `qFactorial_ne_zero_iff` (`QGeneric q 3`). -/
theorem h3_qFactorial_ne_zero_iff (q : K) :
    qFactorial q 3 ≠ 0 ↔ (1 + q ≠ 0 ∧ 1 + q + q ^ 2 ≠ 0) := by
  rw [qFactorial_three, mul_ne_zero_iff]

/-- **The real substrate is generic at rank 3 (sorry-free).**  For `q > 1`
    (in particular the substrate `q₀ ≈ 1.10998`), `[3]_q! > 0`, so `H_3(q)`
    passes the parameter side of Wenzl's criterion — both `1 + q` and
    `1 + q + q²` are strictly positive. -/
theorem h3_qFactorial_pos_of_one_lt {q : ℝ} (hq : 1 < q) :
    0 < qFactorial q 3 :=
  qFactorial_pos (lt_trans one_pos hq) 3

end QOU.Hecke
