import QOU.SchurWeyl.OcneanuWeightBranching
import QOU.SchurWeyl.SeminormalParam

/-!
# QOU.SchurWeyl.OcneanuWeightMarkovCorner — the Markov condition's arithmetic core

The general-`n` Markov condition `tr(x·σ_n) = z·tr(x)` is the one statement standing between this
corpus and its last external citation (see `OcneanuWeightWenzl`).  It reduces to a finite identity
in the **corner contents of a single partition**, and this file proves that identity at convention D.

## The reduction, and what it costs

For `x ∈ H_n` decompose `V_λ = ⊕_{μ = λ − □} V_μ` and set `A_μ = P_μ σ_n P_μ`.  Then `A_μ` commutes
with `H_{n−1}`; Hecke branching is multiplicity-free, so the commutant of `H_{n−1}` in `End(V_μ)` is
the Gelfand–Tsetlin algebra and `A_μ` is **diagonal** in the seminormal basis, with `(T,T)` entry the
Hoefsmit parameter `seminormalParam q (c(λ/μ) − c_T(n))`.  Since `H_n = ⊕_μ End(V_μ)` the diagonal
entries `x_{TT}` range freely, so coefficients may be matched pointwise; and `n` being `T`'s largest
entry, its cell is a **removable corner** of `μ`.  The condition collapses to

> for every `μ ⊢ n` and every removable corner `r` of `μ`:
> `∑_{s addable corner of μ} w_{μ+s} · a(c(s) − c(r)) = z · w_μ`.

**Update — the structural half of that reduction IS now formalised**, in
`SeminormalBlockTrace`, and by a much shorter route than the one described above: `genMat` has
exactly two nonzero entries per column, so `σ_k`'s off-diagonal crossing blocks is immediate and
needs no Okounkov–Vershik argument at all.  Read the justification below as the heavier route it
is; `SeminormalBlockTrace`'s docstring records the correction.  What is still missing is the
*assembly* — the λ-indexed sum with weights — so the caveat below still stands as written.

**🛑 That reduction is NOT formalised, and this file does not formalise it.**  It is derived on
paper (`computations/schurweyl/ocneanu_markov_corner_reduction.py`, which also tests the resulting
identity exactly at symbolic `z` for every partition of `n ≤ 6`).  Steps (i) and (ii) —
multiplicity-freeness of branching, and the Hoefsmit entry — are what `seminormalRep` encodes, but
neither is proved in Lean.  **So the theorems below do not prove the Markov condition.**  They prove
its arithmetic core; the remaining gap is representation-theoretic, not arithmetic, and that is a
different and more tractable shape than the original statement.  Bean `qou-uer7`.

## What is proved here

At convention D the trace lives on the ≤2-row diagrams, and `μ = twoRow m k` has at most two
removable corners — `(0,m−1)` of content `m−1` (present iff `m > k`) and `(1,k−1)` of content `k−2`
(present iff `k > 0`) — and at most two addable corners of nonzero weight, `(0,m)` of content `m`
and `(1,k)` of content `k−1`; the third, `(2,0)`, has weight zero.  So the identity is two equations:

| | removable corner | statement |
|---|---|---|
| `markov_corner_row0` | `(0,m−1)`, needs `k < m` | `w_{(m+1,k)}·a(1) + w_{(m,k+1)}·a(k−m) = z_D·w_{(m,k)}` |
| `markov_corner_row1` | `(1,k−1)`, corner needs `k > 0` | `w_{(m+1,k)}·a(m−k+2) + w_{(m,k+1)}·a(1) = z_D·w_{(m,k)}` |
| `markov_corner_row1_diag` | as above at `k = m` | one term; `twoRow m (m+1)` is not a partition |

`markov_corner_row1` is stated without `0 < k` because the algebra does not need it — but at `k = 0`
row 1 has no removable corner, so there the identity corresponds to no corner and carries no
Markov content.

Both collapse, against the proved bracket form `schurPrincipal_twoRow`, to elementary geometric-sum
facts: row 0 to `[d+2] − 1 = x·[d+1]` and row 1 to `[d+1] = [d] + x^d`.

## Base ring (§7c)

Genuinely `ℝ`: `Seminormal.seminormalParam` is `ℝ`-valued, and using the corpus's own definition
rather than re-deriving the coefficient is the point — it ties these statements to the actual
seminormal representation.

LaTeX label: `thm:ocneanu-markov-corner`
-/

namespace QOU.SchurWeyl

open Finset YoungDiagram QOU.QBeta.WenzlWeight QOU.SchurWeyl.Seminormal

variable {m k : ℕ}

theorem seminormalParam_neg_nat (q : ℝ) (d : ℕ) :
    seminormalParam q (-(d : ℤ)) = (q - q⁻¹) / (1 - q ^ (2 * d)) := by
  unfold seminormalParam
  congr 2
  rw [show (-2 : ℤ) * (-(d : ℤ)) = ((2 * d : ℕ) : ℤ) by push_cast; ring, zpow_natCast]

theorem seminormalParam_pos_nat (q : ℝ) (d : ℕ) :
    seminormalParam q ((d : ℤ)) = (q - q⁻¹) / (1 - (q ^ (2 * d))⁻¹) := by
  unfold seminormalParam
  congr 2
  rw [show (-2 : ℤ) * (d : ℤ) = -((2 * d : ℕ) : ℤ) by push_cast; ring, zpow_neg, zpow_natCast]


theorem markov_corner_row0 (q : ℝ) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (hk : k < m) :
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow (m + 1) k (by omega))
        * seminormalParam q 1
      + ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow m (k + 1) (by omega))
        * seminormalParam q ((k : ℤ) - (m : ℤ))
      = (q ^ 3 / (q ^ 2 + 1)) * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow m k hk.le) := by
  have hq2 : (q ^ 2 : ℝ) ≠ 1 := by simpa using hgen 1 one_pos
  set d := m - k with hdd
  have hd1 : 1 ≤ d := by omega
  have hcast : (k : ℤ) - (m : ℤ) = -((d : ℕ) : ℤ) := by simp [hdd]; omega
  rw [ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21,
    ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21,
    ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21,
    schurPrincipal_twoRow (q ^ 2) hgen (by omega : k ≤ m + 1),
    schurPrincipal_twoRow (q ^ 2) hgen (by omega : k + 1 ≤ m),
    schurPrincipal_twoRow (q ^ 2) hgen hk.le,
    card_twoRow, card_twoRow, card_twoRow,
    seminormalParam_one q hq hq2, hcast, seminormalParam_neg_nat q d,
    show m + 1 - k + 1 = d + 2 by omega, show m - (k + 1) + 1 = d by omega,
    show m - k + 1 = d + 1 by omega,
    show m + 1 + k = (m + k) + 1 by omega, show m + (k + 1) = (m + k) + 1 by omega]
  have hS : (∑ i ∈ range d, (q ^ 2 : ℝ) ^ i) * (1 - q ^ 2) = 1 - (q ^ 2) ^ d :=
    geom_oneSub (q ^ 2) d
  have hM : (q ^ 2 : ℝ) * (∑ i ∈ range (d + 1), (q ^ 2) ^ i) + 1
      = ∑ i ∈ range (d + 2), (q ^ 2) ^ i := mul_geom_succ (q ^ 2) (d + 1)
  have hpow : ((q ^ 2 + 1 : ℝ)) ^ (m + k) ≠ 0 := pow_ne_zero _ hq21
  have hqd : ((q ^ 2 : ℝ)) ^ d ≠ 1 := hgen d (by omega)
  have hden : (1 : ℝ) - q ^ (2 * d) ≠ 0 := by
    have : (q ^ (2 * d) : ℝ) = (q ^ 2) ^ d := by rw [← pow_mul]
    rw [this]; intro hc; exact hqd (by linarith)
  have hS' : (∑ i ∈ range d, (q ^ 2 : ℝ) ^ i) * (1 - q ^ 2) = 1 - q ^ (2 * d) := by
    rw [show (q : ℝ) ^ (2 * d) = (q ^ 2) ^ d by rw [← pow_mul]]; exact hS
  rw [pow_succ]
  field_simp
  linear_combination
    (-((q ^ 2 + 1) * q ^ 2 * (q ^ 2) ^ k * (q ^ 2 + 1) ^ (m + k) * (1 - q ^ (2 * d)))) * hM
      + (-((q ^ 2 + 1) * q ^ 2 * (q ^ 2) ^ k * (q ^ 2 + 1) ^ (m + k))) * hS'


theorem seminormalParam_pos_nat' (q : ℝ) (hq : q ≠ 0) (j : ℕ) (hj : (q : ℝ) ^ (2 * j) ≠ 1) :
    seminormalParam q ((j : ℤ)) = (q ^ 2 - 1) * q ^ (2 * j) / (q * (q ^ (2 * j) - 1)) := by
  have hz : (q : ℝ) ^ (2 * j) ≠ 0 := pow_ne_zero _ hq
  have hz1 : (q : ℝ) ^ (2 * j) - 1 ≠ 0 := sub_ne_zero_of_ne hj
  rw [seminormalParam_pos_nat q j]
  field_simp

theorem markov_corner_row1 (q : ℝ) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (hk : k < m) :
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow (m + 1) k (by omega))
        * seminormalParam q ((m : ℤ) - (k : ℤ) + 2)
      + ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow m (k + 1) (by omega))
        * seminormalParam q 1
      = (q ^ 3 / (q ^ 2 + 1)) * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow m k hk.le) := by
  have hq2 : (q ^ 2 : ℝ) ≠ 1 := by simpa using hgen 1 one_pos
  set d := m - k with hdd
  have hcast : (m : ℤ) - (k : ℤ) + 2 = ((d + 2 : ℕ) : ℤ) := by simp [hdd]; omega
  have hpow2 : (q : ℝ) ^ (2 * (d + 2)) = (q ^ 2) ^ (d + 2) := by rw [← pow_mul]
  have hden : (q : ℝ) ^ (2 * (d + 2)) ≠ 1 := by
    rw [hpow2]; exact hgen (d + 2) (by omega)
  rw [ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21,
    ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21,
    ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21,
    schurPrincipal_twoRow (q ^ 2) hgen (by omega : k ≤ m + 1),
    schurPrincipal_twoRow (q ^ 2) hgen (by omega : k + 1 ≤ m),
    schurPrincipal_twoRow (q ^ 2) hgen hk.le,
    card_twoRow, card_twoRow, card_twoRow,
    seminormalParam_one q hq hq2, hcast, seminormalParam_pos_nat' q hq (d + 2) hden,
    show m + 1 - k + 1 = d + 2 by omega, show m - (k + 1) + 1 = d by omega,
    show m - k + 1 = d + 1 by omega,
    show m + 1 + k = (m + k) + 1 by omega, show m + (k + 1) = (m + k) + 1 by omega]
  have hA : (∑ i ∈ range (d + 2), (q ^ 2 : ℝ) ^ i) * (1 - q ^ 2) = 1 - q ^ (2 * (d + 2)) := by
    rw [hpow2]; exact geom_oneSub (q ^ 2) (d + 2)
  have hC : (∑ i ∈ range (d + 1), (q ^ 2 : ℝ) ^ i)
      = (∑ i ∈ range d, (q ^ 2 : ℝ) ^ i) + (q ^ 2) ^ d := Finset.sum_range_succ _ _
  have hpow : ((q ^ 2 + 1 : ℝ)) ^ (m + k) ≠ 0 := pow_ne_zero _ hq21
  have hz1 : (q : ℝ) ^ (2 * (d + 2)) - 1 ≠ 0 := sub_ne_zero_of_ne hden
  rw [pow_succ]
  field_simp
  linear_combination
    (-((q ^ 2 + 1) * (q ^ 2) ^ k * (q ^ 2 + 1) ^ (m + k) * q ^ (2 * (d + 2)))) * hA
      + (-((q ^ 2 + 1) * (q ^ 2) ^ k * (q ^ 2 + 1) ^ (m + k)
            * (q ^ (2 * (d + 2)) - 1) * q ^ 4)) * hC


theorem markov_corner_row1_diag (q : ℝ) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (m : ℕ) :
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow (m + 1) m (by omega))
        * seminormalParam q 2
      = (q ^ 3 / (q ^ 2 + 1)) * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow m m le_rfl) := by
  have hq2 : (q ^ 2 : ℝ) ≠ 1 := by simpa using hgen 1 one_pos
  have hpow2 : (q : ℝ) ^ (2 * 2) = (q ^ 2) ^ 2 := by rw [← pow_mul]
  have hden : (q : ℝ) ^ (2 * 2) ≠ 1 := by rw [hpow2]; exact hgen 2 (by omega)
  have hcast : ((2 : ℕ) : ℤ) = (2 : ℤ) := by norm_num
  rw [ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21,
    ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21,
    schurPrincipal_twoRow (q ^ 2) hgen (by omega : m ≤ m + 1),
    schurPrincipal_twoRow (q ^ 2) hgen (le_refl m),
    card_twoRow, card_twoRow,
    show (2 : ℤ) = ((2 : ℕ) : ℤ) by norm_num,
    seminormalParam_pos_nat' q hq 2 hden,
    show m + 1 - m + 1 = 2 by omega, show m - m + 1 = 1 by omega,
    show m + 1 + m = (m + m) + 1 by omega]
  have hpow : ((q ^ 2 + 1 : ℝ)) ^ (m + m) ≠ 0 := pow_ne_zero _ hq21
  have hz1 : (q : ℝ) ^ (2 * 2) - 1 ≠ 0 := sub_ne_zero_of_ne hden
  rw [pow_succ]
  norm_num [Finset.sum_range_succ]
  field_simp
  ring

end QOU.SchurWeyl
