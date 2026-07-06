import QOU.MathlibExt.QPartitionCombinatorics

/-!
# QOU.MathlibExt.QSelfSquareCapacity — the q-deformed shell-capacity identity

The **self-square identity** for the q-bracket:

  `[n]_q² = Σ_{ℓ=0}^{n-1} [2ℓ+1]_q`.

At `q = 1` this is the classical `n² = Σ_{ℓ<n} (2ℓ+1)` — the arithmetic
behind the `2n² = Σ_{ℓ<n} 2(2ℓ+1)` electron-shell capacity (Gap 1 of the
periodic-table derivation; content
`predicted-spectra/shell-eigenvalue-properties.md`, where each sub-shell `ℓ`
contributes `2(2ℓ+1)` and the shell sums to `2n²`).  Here it is the genuine
**q-deformed** identity over `[m]_q = (q^m − q^{-m})/(q − q⁻¹)`.

The proof is the telescoping of the one-line difference identity
`[k+1]_q² − [k]_q² = [2k+1]_q`, which itself reduces to `(q·q⁻¹ − 1)(a−b)² = 0`
(needs only `q ≠ 0`).

Sorry-free; unconditional over `ℝ` with `q ≠ 0` and `q − q⁻¹ ≠ 0`.

Refs:
- [macdonald1995] Symmetric Functions and Hall Polynomials, I.3
- [manuscript] predicted-spectra/shell-eigenvalue-properties (the 2n² capacity)
-/

namespace QOU.MathlibExt.QPartitionCombinatorics

open Finset

/-- Uniform closed form for `qBracket` (the `if n = 0` branch collapses because
    the numerator `q^0 − q^0 = 0`), with `q^{-n}` written as `(q⁻¹)^n`. -/
theorem qBracket_eq (q : ℝ) (n : ℕ) :
    qBracket q n = (q ^ n - (q⁻¹) ^ n) / (q - q⁻¹) := by
  unfold qBracket
  have hz : q ^ (-(n : ℤ)) = (q⁻¹) ^ n := by rw [zpow_neg, zpow_natCast, inv_pow]
  split
  · next h => subst h; simp
  · rw [hz]

/-- The algebraic core over opaque variables: with `Q·Qi = 1`,
    `((AQ − B Qi)/(Q − Qi))² − ((A − B)/(Q − Qi))² = (A²Q − B²Qi)/(Q − Qi)`. -/
theorem qBracket_diffSq_aux (A B Q Qi : ℝ) (hd : Q - Qi ≠ 0) (hqq : Q * Qi = 1) :
    ((A * Q - B * Qi) / (Q - Qi)) ^ 2 - ((A - B) / (Q - Qi)) ^ 2
      = (A ^ 2 * Q - B ^ 2 * Qi) / (Q - Qi) := by
  have core : (A * Q - B * Qi) ^ 2 - (A - B) ^ 2
      = (A ^ 2 * Q - B ^ 2 * Qi) * (Q - Qi) := by
    linear_combination (A - B) ^ 2 * hqq
  rw [div_pow, div_pow, div_sub_div_same, core, pow_two (Q - Qi),
      mul_div_mul_right _ _ hd]

/-- **One-line difference identity**: `[k+1]_q² − [k]_q² = [2k+1]_q`. -/
theorem qBracket_succ_sq_sub (q : ℝ) (hq : q ≠ 0) (hd : q - q⁻¹ ≠ 0) (k : ℕ) :
    qBracket q (k + 1) ^ 2 - qBracket q k ^ 2 = qBracket q (2 * k + 1) := by
  rw [qBracket_eq, qBracket_eq, qBracket_eq,
      show q ^ (k + 1) = q ^ k * q from pow_succ q k,
      show (q⁻¹) ^ (k + 1) = (q⁻¹) ^ k * q⁻¹ from pow_succ q⁻¹ k,
      show q ^ (2 * k + 1) = (q ^ k) ^ 2 * q by rw [pow_succ, mul_comm 2 k, pow_mul],
      show (q⁻¹) ^ (2 * k + 1) = ((q⁻¹) ^ k) ^ 2 * q⁻¹ by
        rw [pow_succ, mul_comm 2 k, pow_mul]]
  exact qBracket_diffSq_aux (q ^ k) ((q⁻¹) ^ k) q q⁻¹ hd (mul_inv_cancel₀ hq)

/-- **The q-deformed shell-capacity self-square identity**:

      `[n]_q² = Σ_{ℓ=0}^{n-1} [2ℓ+1]_q`.

    The q-analog of `n² = Σ_{ℓ<n}(2ℓ+1)` — the arithmetic core of the `2n²`
    electron-shell capacity (each `ℓ` sub-shell contributing `2(2ℓ+1)`). -/
theorem qBracket_sq_eq_sum_odd (q : ℝ) (hq : q ≠ 0) (hd : q - q⁻¹ ≠ 0) (n : ℕ) :
    (∑ l ∈ range n, qBracket q (2 * l + 1)) = qBracket q n ^ 2 := by
  induction n with
  | zero => simp [qBracket]
  | succ k ih => rw [sum_range_succ, ih]; linarith [qBracket_succ_sq_sub q hq hd k]

end QOU.MathlibExt.QPartitionCombinatorics
