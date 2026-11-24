import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.Ring
import QOU.BraidsAndKnots.DeltaLambdaGeneralNUnconditional
import QOU.MassTheory.ThreeRowSpringerSYTDerivation
import QOU.Mathlib.PartitionsOfBridge

/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/

set_option autoImplicit false

/-!
# Abstract `Nat.Partition` Fintype Bridge, Framed-Braid Ribbon Content Identity, and Temperley–Lieb Kernel Split for `sRow3` (`qou-jkmh`)

Completes the mathematical foundations around `QOU.MassTheory.ThreeRowSpringerSYTDerivation`
(`qou-jkmh`: *Close `sRow3` Derivation Seam: Prove `≥ 3`-Row Signed Springer-Dimension Table from
Frame–Robinson–Thrall Hook-Length `dimHLF`, `nStatList`, and Framed Braid Data*) additively,
without modifying `ThreeRowExtensiveCumulant` or `GPMTThreeRowCumulantBridge` (preserving zero
conflict with queued sibling PRs):

1. **All-`k` Fintype Bridge from Mathlib `Nat.Partition k` & Genuine `dimSYT` to `sRow3Derived`:**
   `ThreeRowSpringerSYTDerivation` proved `sRow3Derived_eq_sRow3` over the fuel-based list
   enumerator `partitionsOf k`. Using `PartitionsOfBridge.sum_map_partitionsOf` and the
   Frame–Robinson–Thrall theorem `IdentityIHLFBridge.dimSYT_eq_dimHLF`, we prove for **every**
   `k : ℕ` (`sRow3NatPartition_eq_sRow3Derived`) that the genuine Mathlib `Fintype` sum
   `sRow3NatPartition k = ∑_{p : Nat.Partition k, 3 ≤ p.parts.card} (-1)^{n(p)} · dimSYT(p)`
   equals `sRow3Derived k`, and hence equals `sRow3 k` for all `k ≤ 5` (`sRow3NatPartition_eq_sRow3`).

2. **Framed-Braid / Ribbon Full-Twist & Half-Twist Identity for the Springer Sign (All `k`):**
   - `sRow3NatPartition_eq_columnHalfTwistParity_sum`: for **every** `k : ℕ`, replaces `(-1)^{n(λ)}`
     inside `sRow3NatPartition k` by `(-1)^{∑_j C(λ'_j, 2)}`, the exact crossing-count parity of the
     product of positive half-twist braids on the columns of `λ` (`w₀^{S_{λ'}}`).
   - `diagramContentSum_eq_cell_sum` & `diagramContentSum_eq_rowHalfTwist_sub_colHalfTwist`: proves
     for every partition `l` (`l.Sorted (· ≥ ·)`) that the ribbon-twist / Jucys–Murphy full-twist
     Casimir exponent `c(λ) = ∑_{(i,j) ∈ λ} (j - i)` satisfies
     `c(λ) = ∑_i C(λ_i, 2) - n(λ) = ∑_i C(λ_i, 2) - ∑_j C(λ'_j, 2)`
     (`Macdonald` I.1 Ex. 3), locking the Springer grade `n(λ)` directly to the deficit between the
     row half-twist writhe and the central ribbon-twist exponent `c(λ)`.

3. **Temperley–Lieb (`≤ 2`-Row) vs `≥ 3`-Row Kernel Decomposition & Higher-Cluster Extension (`k ≤ 8`):**
   - `sTotalDerived_eq_sRowLe2_add_sRow3`: decomposes the full `H_k` / `S_k` signed dimension trace
     into the Temperley–Lieb quotient (`ℓ(λ) ≤ 2`) plus the killed `≥ 3`-row kernel `sRow3Derived k`
     for **every** `k : ℕ`.
   - `sRow3NatPartition_six_seven_eight`: proves exact higher-cluster values `(16, -15, -132)` at
     `k = 6, 7, 8` (`A = 6..8` p-shell boundary), alongside the alternating Catalan pattern
     `[1, 1, 0, -1, 0, 2, 0, -5, 0]` on the Temperley–Lieb `≤ 2`-row stratum.

## References
- [macdonald1995] I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., I.1 Ex. 3.
- [springer1976] T. A. Springer, *Trigonometric sums, Green functions of finite groups and
  representations of Weyl groups*, Invent. Math. 36 (1976), 173–207.
-/

namespace QOU.MassTheory.ThreeRowSpringerFintypeAndBraidTwist

open Finset
open QOU.BraidsAndKnots
open QOU.BraidKnot.IdentityI
open QOU.MassTheory.ThreeRowExtensiveCumulant
open QOU.MassTheory.ThreeRowSpringerSYTDerivation
open QOU.Mathlib
open QOU.Mathlib.PartitionListBridge
open QOU.Mathlib.PartitionsOfBridge

/-! ## 1. All-`k` Fintype Bridge: `Nat.Partition k` + Genuine `dimSYT` = `sRow3Derived k` -/

/-- Helper: summing `f` over `l.filter p` equals summing `if p x then f x else 0` over `l`. -/
theorem list_sum_map_filter {α : Type*} (l : List α) (p : α → Bool) (f : α → ℤ) :
    ((l.filter p).map f).sum = (l.map (fun x => if p x = true then f x else 0)).sum := by
  induction l with
  | nil => rfl
  | cons a tail ih =>
    cases hp : p a
    · simp [List.filter, hp, ih]
    · simp [List.filter, hp, ih]

/-- Length of `toList p = p.parts.sort (· ≥ ·)` equals the number of rows `p.parts.card`. -/
@[simp] theorem toList_length {n : ℕ} (p : Nat.Partition n) :
    (toList p).length = p.parts.card :=
  Multiset.length_sort _

/-- **Canonical abstract `≥ 3`-row signed Springer–SYT sum over Mathlib's `Nat.Partition k`:**
sums `(-1)^{n(λ)} · #SYT(λ)` over all `p : Nat.Partition k` with `3 ≤ p.parts.card`. -/
noncomputable def sRow3NatPartition (k : ℕ) : ℤ :=
  ∑ p : Nat.Partition k,
    if 3 ≤ p.parts.card then
      (-1 : ℤ) ^ nStatList (toList p) * (dimSYT p : ℤ)
    else 0

/-- **All-`k` Enumeration & Hook-Length Bridge (`qou-jkmh`):**
For **every** `k : ℕ` (no `k ≤ 5` cap), the abstract `Nat.Partition k` sum `sRow3NatPartition k`
over genuine `StandardYoungTableau` cardinalities `dimSYT p` equals the computable hook-length sum
`sRow3Derived k`. -/
theorem sRow3NatPartition_eq_sRow3Derived (k : ℕ) :
    sRow3NatPartition k = sRow3Derived k := by
  unfold sRow3Derived sRow3NatPartition
  rw [list_sum_map_filter, sum_map_partitionsOf]
  refine Finset.sum_congr rfl fun p _ => ?_
  simp only [toList_length, decide_eq_true_eq]
  split_ifs with h3
  · exact (deltaLambdaHLF_sort_eq_signed_dimSYT p).symm
  · rfl

/-- **Exact `Nat.Partition` Discharge of `sRow3` (`k ≤ 5`):**
For all `k ≤ 5`, the genuine `Nat.Partition k` / `dimSYT` sum `sRow3NatPartition k` equals the
table `sRow3 k` of `QOU.MassTheory.ThreeRowExtensiveCumulant`. -/
theorem sRow3NatPartition_eq_sRow3 (k : ℕ) (hk : k ≤ 5) :
    sRow3NatPartition k = sRow3 k := by
  rw [sRow3NatPartition_eq_sRow3Derived k, sRow3Derived_eq_sRow3 k hk]

/-- Structural vanishing on `k ≤ 2` proved directly on `sRow3NatPartition` without `decide`: no
partition of `k ≤ 2` has `≥ 3` positive parts. -/
theorem sRow3NatPartition_eq_zero_of_le_two {k : ℕ} (hk : k ≤ 2) :
    sRow3NatPartition k = 0 := by
  unfold sRow3NatPartition
  refine Finset.sum_eq_zero fun p _ => ?_
  have hlen : p.parts.card ≤ k := by
    have hpos := toList_pos p
    have hsum := toList_sum p
    have hle : ∀ l : List ℕ, (∀ a ∈ l, 0 < a) → l.length ≤ l.sum := by
      intro l hl
      induction l with
      | nil => simp
      | cons b bs ih =>
        have hb := hl b (by simp)
        have hbs := ih (fun a ha => hl a (List.mem_cons_of_mem b ha))
        simp only [List.length_cons, List.sum_cons]
        omega
    have := hle (toList p) hpos
    rw [toList_length, hsum] at this
    exact this
  have hnot : ¬ (3 ≤ p.parts.card) := by omega
  simp [hnot]

/-! ## 2. Framed-Braid Half-Twist & Ribbon Full-Twist Content Identity for `(-1)^{n(λ)}` -/

/-- **All-`k` Framed-Braid Column Half-Twist Formula for `sRow3NatPartition`:**
For **every** `k : ℕ`, `sRow3NatPartition k` equals the sum over `≥ 3`-row partitions of `dimSYT p`
weighted by the crossing-count parity `(-1)^{∑_j C(λ'_j, 2)}` of the Young column half-twist braid
`∏_j Δ_{λ'_j}` (`w₀^{S_{λ'}}`). -/
theorem sRow3NatPartition_eq_columnHalfTwistParity_sum (k : ℕ) :
    sRow3NatPartition k =
      ∑ p : Nat.Partition k,
        if 3 ≤ p.parts.card then
          (-1 : ℤ) ^ sumChoose2 (conjugate (toList p)) * (dimSYT p : ℤ)
        else 0 := by
  unfold sRow3NatPartition
  refine Finset.sum_congr rfl fun p _ => ?_
  split_ifs with h3
  · have hpar := parity_eq_w0_sign_general (toList p) (toList_sorted p)
    unfold deltaSignParity at hpar
    rw [hpar]
  · rfl

/-- Computable Young-diagram content sum `c(λ) = ∑_{(i,j) ∈ λ} (j - i)` defined by largest-row
peeling: prepending a top row of length `a` contributes `∑_{j < a} j = a(a - 1)/2` and shifts the
row index of every remaining cell in `l` up by `1` (subtracting `l.sum`). -/
def diagramContentSum : List ℕ → ℤ
  | [] => 0
  | a :: l => ((a * (a - 1) / 2 : ℕ) : ℤ) + diagramContentSum l - (l.sum : ℤ)

@[simp] theorem diagramContentSum_nil : diagramContentSum [] = 0 := rfl

@[simp] theorem diagramContentSum_cons (a : ℕ) (l : List ℕ) :
    diagramContentSum (a :: l) =
      ((a * (a - 1) / 2 : ℕ) : ℤ) + diagramContentSum l - (l.sum : ℤ) := rfl

/-- Integer Gauss identity matching `Nat` division by `2`: `∑_{j < a} (j : ℤ) = (a*(a-1)/2 : ℕ)`. -/
theorem sum_range_int_eq_choose2 (a : ℕ) :
    (∑ j ∈ Finset.range a, (j : ℤ)) = ((a * (a - 1) / 2 : ℕ) : ℤ) := by
  induction a with
  | zero => simp
  | succ m ih =>
    rw [Finset.sum_range_succ, ih]
    have hpas := choose2_succ m
    have hcast : (((m + 1) * (m + 1 - 1) / 2 : ℕ) : ℤ) =
        ((m * (m - 1) / 2 : ℕ) : ℤ) + (m : ℤ) := by
      exact_mod_cast hpas
    omega

/-- Sum of `(l.getD i 0 : ℤ)` over `i ∈ Finset.range l.length` equals `(l.sum : ℤ)`. -/
theorem sum_range_getD_eq_sum (l : List ℕ) :
    (∑ i ∈ Finset.range l.length, (l.getD i 0 : ℤ)) = (l.sum : ℤ) := by
  induction l with
  | nil => simp
  | cons a tail ih =>
    rw [List.length_cons, Finset.sum_range_succ']
    simp only [List.getD_cons_zero, List.getD_cons_succ, List.sum_cons, Nat.cast_add]
    linarith [ih]

/-- **Non-Collapse Equivalence:** `diagramContentSum l` equals the genuine double cell sum
`∑_{i < ℓ(l)} ∑_{j < l_i} (j - i)` over every cell `(i, j)` of the diagram (the eigenvalue
exponent of the central framed-braid / Hecke full twist `Δ_k²` on `V_λ`). -/
theorem diagramContentSum_eq_cell_sum (l : List ℕ) :
    diagramContentSum l =
      ∑ i ∈ Finset.range l.length,
        ∑ j ∈ Finset.range (l.getD i 0), ((j : ℤ) - (i : ℤ)) := by
  induction l with
  | nil => simp [diagramContentSum]
  | cons a tail ih =>
    rw [List.length_cons, Finset.sum_range_succ']
    simp only [List.getD_cons_zero, List.getD_cons_succ, Nat.cast_zero, sub_zero]
    rw [sum_range_int_eq_choose2 a]
    have hshift :
        (∑ k ∈ Finset.range tail.length,
          ∑ j ∈ Finset.range (tail.getD k 0), ((j : ℤ) - ((k + 1 : ℕ) : ℤ))) =
        (∑ k ∈ Finset.range tail.length,
          ∑ j ∈ Finset.range (tail.getD k 0), ((j : ℤ) - (k : ℤ))) -
          (tail.sum : ℤ) := by
      have hinner : ∀ k ∈ Finset.range tail.length,
          (∑ j ∈ Finset.range (tail.getD k 0), ((j : ℤ) - ((k + 1 : ℕ) : ℤ))) =
            (∑ j ∈ Finset.range (tail.getD k 0), ((j : ℤ) - (k : ℤ))) -
              (tail.getD k 0 : ℤ) := by
        intro k _
        have hrew : ∀ j : ℕ,
            ((j : ℤ) - ((k + 1 : ℕ) : ℤ)) = ((j : ℤ) - (k : ℤ)) - 1 := fun j => by
          push_cast; ring
        simp_rw [hrew, Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range]
        simp
      rw [Finset.sum_congr rfl hinner, Finset.sum_sub_distrib, sum_range_getD_eq_sum]
    rw [hshift, ← ih, diagramContentSum_cons]
    ring

/-- **Macdonald Content–Grade Law (`c(λ) = ∑_i C(λ_i, 2) - n(λ)` for ALL `l : List ℕ`):**
The ribbon-twist / Jucys–Murphy content sum equals the row half-twist crossing count `sumChoose2 l`
minus the Springer grade `nStatList l`. -/
theorem diagramContentSum_eq_rowHalfTwist_sub_nStat (l : List ℕ) :
    diagramContentSum l = (sumChoose2 l : ℤ) - (nStatList l : ℤ) := by
  change diagramContentSum l = (sumChoose2 l : ℤ) - (aStat l : ℤ)
  induction l with
  | nil => rfl
  | cons a tail ih =>
    rw [diagramContentSum_cons, ih, sumChoose2_cons, aStat_cons]
    push_cast
    ring

/-- **Framed-Braid Row-vs-Column Half-Twist Law (`c(λ) = ∑_i C(λ_i, 2) - ∑_j C(λ'_j, 2)`):**
For every sorted partition `l`, the central full-twist / ribbon-twist exponent `c(λ)` equals the
difference between the Young row half-twist crossing count and the Young column half-twist crossing
count, locking `n(λ) = ∑_i C(λ_i, 2) - c(λ)`. -/
theorem diagramContentSum_eq_rowHalfTwist_sub_colHalfTwist
    (l : List ℕ) (hl : l.Sorted (· ≥ ·)) :
    diagramContentSum l = (sumChoose2 l : ℤ) - (sumChoose2 (conjugate l) : ℤ) := by
  rw [diagramContentSum_eq_rowHalfTwist_sub_nStat l, ← aStat_eq_sumChoose2_conjugate l hl]
  rfl

/-! ## 3. Temperley–Lieb (`≤ 2`-Row) vs `≥ 3`-Row Kernel Split & `k ≤ 8` Extension -/

/-- Total signed Springer–SYT sum across **all** partitions of `k`. -/
def sTotalDerived (k : ℕ) : ℤ :=
  ((partitionsOf k).map deltaLambdaHLF).sum

/-- Temperley–Lieb (`ℓ(λ) ≤ 2`) signed Springer–SYT stratum at cluster size `k`. -/
def sRowLe2Derived (k : ℕ) : ℤ :=
  (((partitionsOf k).filter (fun lam => decide (lam.length ≤ 2))).map deltaLambdaHLF).sum

/-- **All-`k` Temperley–Lieb Quotient vs Kernel Decomposition:**
For every `k : ℕ`, the full `H_k` / `S_k` signed dimension sum splits into the Temperley–Lieb
`≤ 2`-row quotient stratum `sRowLe2Derived k` plus the killed `≥ 3`-row kernel `sRow3Derived k`. -/
theorem sTotalDerived_eq_sRowLe2_add_sRow3 (k : ℕ) :
    sTotalDerived k = sRowLe2Derived k + sRow3Derived k := by
  unfold sTotalDerived sRowLe2Derived sRow3Derived
  rw [list_sum_map_filter, list_sum_map_filter]
  have hpoint : ∀ l : List ℕ,
      deltaLambdaHLF l =
        (if decide (l.length ≤ 2) = true then deltaLambdaHLF l else 0) +
        (if decide (3 ≤ l.length) = true then deltaLambdaHLF l else 0) := by
    intro l
    by_cases h : l.length ≤ 2
    · have hnot : ¬ (3 ≤ l.length) := by omega
      simp [h, hnot]
    · have hge : 3 ≤ l.length := by omega
      simp [h, hge]
  have hsum : ∀ xs : List (List ℕ),
      (xs.map deltaLambdaHLF).sum =
        (xs.map (fun l => if decide (l.length ≤ 2) = true then deltaLambdaHLF l else 0)).sum +
        (xs.map (fun l => if decide (3 ≤ l.length) = true then deltaLambdaHLF l else 0)).sum := by
    intro xs
    induction xs with
    | nil => rfl
    | cons x tail ih =>
      simp only [List.map_cons, List.sum_cons, ih]
      have hx := hpoint x
      omega
  exact hsum (partitionsOf k)

/-- Exact Temperley–Lieb (`≤ 2`-row) stratum values for `k = 0..8`:
`[1, 1, 0, -1, 0, 2, 0, -5, 0]` (note the exact odd/even alternation at `k ≥ 2`). -/
theorem sRowLe2Derived_values_le8 :
    sRowLe2Derived 0 = 1 ∧ sRowLe2Derived 1 = 1 ∧ sRowLe2Derived 2 = 0 ∧
    sRowLe2Derived 3 = -1 ∧ sRowLe2Derived 4 = 0 ∧ sRowLe2Derived 5 = 2 ∧
    sRowLe2Derived 6 = 0 ∧ sRowLe2Derived 7 = -5 ∧ sRowLe2Derived 8 = 0 := by
  refine ⟨by decide, by decide, by decide, by decide, by decide, by decide,
    by decide, by decide, by decide⟩

/-- Exact higher-cluster `≥ 3`-row values at `k = 6, 7, 8` (`p`-shell regime):
`sRow3Derived 6 = 16`, `sRow3Derived 7 = -15`, `sRow3Derived 8 = -132`, transported onto
`sRow3NatPartition` as well. -/
theorem sRow3NatPartition_six_seven_eight :
    sRow3NatPartition 6 = 16 ∧ sRow3NatPartition 7 = -15 ∧ sRow3NatPartition 8 = -132 := by
  rw [sRow3NatPartition_eq_sRow3Derived 6,
      sRow3NatPartition_eq_sRow3Derived 7,
      sRow3NatPartition_eq_sRow3Derived 8]
  exact ⟨by decide, by decide, by decide⟩

end QOU.MassTheory.ThreeRowSpringerFintypeAndBraidTwist
