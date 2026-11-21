import QOU.SchurWeyl.OcneanuWeightBranching
import QOU.SchurWeyl.TwoRowSYTBallot

/-!
# QOU.SchurWeyl.SpinSectorMeasure — the Markov measure at convention D is the spin-sector split

At convention D (`z_D = q³/(q²+1)`), the Markov trace on `H_n(q)` is

`tr = ∑_λ W_λ · χ^λ`,  `W_λ = ocneanuWeight q z_D λ`,

and the **Markov measure** on partitions of `n` is `μ_λ = f^λ · W_λ`, where `f^λ` is the number of
standard Young tableaux of shape `λ` (the dimension of the Specht module `V_λ`).  Only partitions with
at most two rows carry weight (`ocneanuWeight_conventionD_eq_zero_of_three_rows`).

This file proves the closed form of that measure on the two-row shapes `(n − k, k)`:

`W_(n−k,k) = [n − 2k + 1]_q / [2]_qⁿ`,   `μ_(n−k,k) = m_k(n) · [n − 2k + 1]_q / [2]_qⁿ`,

with `[j]_q = (q^j − q^{−j})/(q − q⁻¹)` the balanced `q`-integer and `m_k(n) = C(n,k) − C(n,k−1)` the
ballot number.  Both statements are proved for every `n`, over a generic field, with the
denominators cleared so that no ordering and no `q`-integer division is needed:

* `ocneanuWeight_twoRow_conventionD` — `W · (q − q⁻¹) · (q + q⁻¹)ⁿ = q^{d+1} − q^{−(d+1)}`,
  `d = n − 2k`;
* `markovMeasure_twoRow_conventionD` — the same with the ballot number in front.

## Reading: the spin sectors of `n` qubits

`(q + q⁻¹)ⁿ = [2]ⁿ` is the quantum dimension of `V^{⊗n}` for the two-dimensional `U_q(sl₂)` module
`V`, and `m_k(n) · [n − 2k + 1]` is the quantum dimension of its isotypic component of spin
`(n − 2k)/2`: there are `m_k(n)` copies of the spin-`(n−2k)/2` module, each of quantum dimension
`[n − 2k + 1]`.  So the Markov measure at convention D assigns to each spin sector its share of the
quantum dimension of `n` qubits.  The decomposition `[2]ⁿ = ∑_k m_k(n)[n − 2k + 1]` itself is
`QOU.QBeta.QDimNormalisation.qdim_normalisation_general` (G2, proved for every `n`), and the fact that
the measure sums to one is `QOU.SchurWeyl.sum_dim_weight_eq_one`.  This file supplies the bridge
between them: the two were previously linked only by a numerical check of `yw` against
`y_lambda_su_n` (`TemperleyLiebTower.yw`, 50 dps, `n = 2 … 7`).

At `q = 1` the measure is `m_k(n)(n − 2k + 1)/2ⁿ`, the classical count of spin sectors among the
`2ⁿ` states of `n` bits.

## What this rests on (stated, not proved here)

* **"Spin sector" is a reading through Schur–Weyl duality.** The identity proved here is between
  two explicit expressions in `q`. Calling `μ_(n−k,k)` the weight of the spin-`(n−2k)/2` sector of
  `V^{⊗n}` uses quantum Schur–Weyl duality between `U_q(gl₂)` and `H_n(q)` on `V^{⊗n}`, which
  matches the two-row Specht module `V_(n−k,k)` with the spin-`(n−2k)/2` highest-weight module.
  That duality is **G3.4**, which is not fully proved in this corpus (the Dipper–James route is open
  in its own work stream). Nothing below uses it.
* **"The Markov trace" means the trace with these weights.** That the convention-D Markov trace is
  `∑ W_λ χ^λ` with `W = ocneanuWeight` uses Ocneanu/Jones uniqueness, which is not proved here
  either (`MarkovNormalisation` proves both defining properties of these weights, not uniqueness).

## Base ring (§7c)

Generic `[Field R]`; no ordering, no `ℝ`.

Bean `qou-078y` (information-theory reading of the mass).
-/

namespace QOU.SchurWeyl.SpinSector

open Finset QOU.SchurWeyl QOU.QBeta.WenzlWeight QOU.Mathlib QOU.SchurWeyl.TwoRowSYTBallot

variable {R : Type*} [Field R]

/-- **The two-row Ocneanu weight at convention D is `[n − 2k + 1]_q / [2]_qⁿ`.**

Stated with the denominators cleared:
`W_(m,k) · (q − q⁻¹) · (q + q⁻¹)^{m+k} = q^{d+1} − q^{−(d+1)}`, `d = m − k`. -/
theorem ocneanuWeight_twoRow_conventionD (q : R) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : R) ^ i ≠ 1) {m k : ℕ} (h : k ≤ m) :
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow m k h) * (q - q⁻¹) * (q + q⁻¹) ^ (m + k)
      = q ^ (m - k + 1) - q⁻¹ ^ (m - k + 1) := by
  rw [ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21, schurPrincipal_twoRow _ hgen h,
    card_twoRow]
  obtain ⟨d, rfl⟩ : ∃ d, m = k + d := ⟨m - k, by omega⟩
  rw [show k + d - k + 1 = d + 1 by omega]
  have hgeo := geom_oneSub (q ^ 2) (d + 1)
  set S := ∑ i ∈ range (d + 1), (q ^ 2) ^ i with hS
  have hqk : q ^ (k + d + k) ≠ 0 := pow_ne_zero _ hq
  have hden : (q ^ 2 + 1) ^ (k + d + k) ≠ 0 := pow_ne_zero _ hq21
  have hsum : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  have hdiff : q - q⁻¹ = (q ^ 2 - 1) / q := by field_simp
  rw [hsum, hdiff, div_pow, inv_pow, ← one_div]
  field_simp
  have e1 : q ^ (k + d + k) = q ^ k * q ^ d * q ^ k := by rw [pow_add, pow_add]
  have e2 : q ^ (d + 1) = q ^ d * q := pow_succ q d
  have e3 : (q ^ 2) ^ k = q ^ k * q ^ k := by rw [← pow_mul, mul_comm, pow_mul, sq]
  have e4 : (q ^ 2) ^ (d + 1) = q ^ d * q ^ d * q ^ 2 := by
    rw [← pow_mul, show 2 * (d + 1) = d + d + 2 by ring, pow_add, pow_add]
  rw [e4] at hgeo
  rw [e1, e2, e3]
  linear_combination (-(q ^ k * q ^ k) * (q ^ d * q)) * hgeo

/-- **The Markov measure on the two-row shape `(m, k)` at convention D.**

`f^(m,k) · W_(m,k) · (q − q⁻¹) · [2]^{m+k} = m_k(m+k) · (q^{d+1} − q^{−(d+1)})`, i.e.
`μ_(n−k,k) = m_k(n) · [n − 2k + 1]_q / [2]_qⁿ`: the spin-`(n−2k)/2` sector's share of the quantum
dimension of `n` qubits. -/
theorem markovMeasure_twoRow_conventionD (q : R) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : R) ^ i ≠ 1) {m k : ℕ} (h : k ≤ m) :
    (numStandardYoungTableaux (twoRow m k h) : R)
        * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow m k h) * (q - q⁻¹) * (q + q⁻¹) ^ (m + k)
      = (ballot (m + k) k : R) * (q ^ (m - k + 1) - q⁻¹ ^ (m - k + 1)) := by
  have hf : ((numStandardYoungTableaux (twoRow m k h) : ℤ) : R) = (ballot (m + k) k : R) :=
    congrArg (Int.cast : ℤ → R) (numSYT_twoRow_eq_ballot m k h)
  push_cast at hf
  rw [← ocneanuWeight_twoRow_conventionD q hq hq21 hgen h, ← hf]
  ring

/-- **The classical limit `q = 1`** of the sector weight, stated without dividing by `q − q⁻¹`:
`[j]_q → j`, so `W_(n−k,k)(1) = (n − 2k + 1)/2ⁿ`. Here: the numerator
`(q^j − q^{−j})/(q − q⁻¹)` is the sum `∑_{i<j} q^{j−1−2i}`, which at `q = 1` is `j`. -/
theorem qint_numerator_eq_sum (q : R) (hq : q ≠ 0) (j : ℕ) :
    q ^ j - q⁻¹ ^ j = (q - q⁻¹) * ∑ i ∈ range j, q ^ (j - 1 - i) * q⁻¹ ^ i := by
  induction j with
  | zero => simp
  | succ j ih =>
    have hstep : ∑ i ∈ range (j + 1), q ^ (j + 1 - 1 - i) * q⁻¹ ^ i
        = q * ∑ i ∈ range j, q ^ (j - 1 - i) * q⁻¹ ^ i + q⁻¹ ^ j := by
      rw [Finset.sum_range_succ, Finset.mul_sum]
      congr 1
      · refine Finset.sum_congr rfl fun i hi => ?_
        have hi := Finset.mem_range.mp hi
        rw [show j + 1 - 1 - i = (j - 1 - i) + 1 by omega, pow_succ]
        ring
      · simp
    rw [hstep, mul_add, ← mul_assoc, mul_comm (q - q⁻¹) q, mul_assoc, ← ih]
    rw [pow_succ, pow_succ]
    field_simp
    ring

theorem sector_sum_at_one (j : ℕ) :
    ∑ i ∈ range j, (1 : R) ^ (j - 1 - i) * (1 : R)⁻¹ ^ i = j := by
  simp

end QOU.SchurWeyl.SpinSector
