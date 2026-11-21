import QOU.Mass.QHookDimension
import QOU.Mass.QHookDimensionBalanced
import QOU.QBeta.WenzlWeightVanishing
import QOU.Mathlib.RSKBurnsideTarget
import Mathlib.Data.List.GetD

/-!
# The list hook formula `QOU.Mass.dimQ` on Young diagrams

`QOU.Mass.dimQ q l = [|l|]_q! / ∏ [h]_q` takes a partition as a weakly decreasing list `l` and
computes its hooks by `hooks l`, reading column lengths off `conjugate l`. The Hecke-side files
work with the Young diagram `ofRowLens l` and its cell hooks `hook μ (i, j)`. This file proves
that the two encodings agree.

## Main results

* `colLen_ofRowLens`: the column length of `ofRowLens l` is the length of `l.filter (j < ·)`.
* `hook_ofRowLens`: on every cell, `hookAt l i j = hook (ofRowLens l) (i, j)`.
* `hooks_prod_eq`: `((hooks l).map f).prod = ∏_{x ∈ cells} f (hook μ x)`.
* `qInt_eq_qIntBal`: the sum-of-powers `[n]_q` equals the balanced `(qⁿ − q⁻ⁿ)/(q − q⁻¹)` when
  `q² ≠ 1`.
* `dimQ_partition_eq`: for a partition `λ ⊢ N`,
  `dimQ q (sorted parts) = ∏_{j < N} [j+1]_q / ∏_{x ∈ λ} [h(x)]_q`.

## Base ring (§7c)

Generic `[Field R]`; the balanced comparison needs `q ≠ 0`, `q² ≠ 1`. No ordering.

LaTeX label: `lem:qhook-dimension-diagram`
-/

namespace QOU.Mass.QHookDiagram

open Finset YoungDiagram QOU.Mass

/-- In a weakly decreasing list, `i` indexes an entry above `j` iff `i` is below the number of
entries above `j`. -/
theorem lt_length_filter_iff (j : ℕ) :
    ∀ (l : List ℕ), List.Sorted (· ≥ ·) l → ∀ i : ℕ,
      (i < (l.filter fun r => j < r).length ↔ ∃ h : i < l.length, j < l[i])
  | [], _, i => by simp
  | a :: t, hs, i => by
    have hst : List.Sorted (· ≥ ·) t := hs.of_cons
    have hle : ∀ b ∈ t, b ≤ a := fun b hb => List.rel_of_sorted_cons hs b hb
    by_cases hja : j < a
    · rw [List.filter_cons_of_pos (by simpa using hja)]
      cases i with
      | zero => simp [hja]
      | succ k =>
        simp only [List.length_cons, Nat.add_lt_add_iff_right, List.getElem_cons_succ] at *
        rw [lt_length_filter_iff j t hst k]
    · rw [List.filter_cons_of_neg (by simpa using hja)]
      have hnil : (t.filter fun r => j < r) = [] := by
        rw [List.filter_eq_nil_iff]
        intro b hb
        have := hle b hb
        simp only [decide_eq_true_eq]
        omega
      rw [hnil]
      simp only [List.length_nil, Nat.not_lt_zero, false_iff, not_exists]
      intro h
      cases i with
      | zero => simpa using hja
      | succ k =>
        simp only [List.getElem_cons_succ]
        have := hle _ (List.getElem_mem (l := t) (by simp at h; omega))
        omega

theorem colLen_ofRowLens (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) (j : ℕ) :
    (ofRowLens l hl).colLen j = (l.filter fun r => j < r).length := by
  apply le_antisymm
  · by_contra hc
    push_neg at hc
    have hmem : ((l.filter fun r => j < r).length, j) ∈ ofRowLens l hl :=
      mem_iff_lt_colLen.mpr hc
    rw [mem_ofRowLens] at hmem
    exact (lt_irrefl _) ((lt_length_filter_iff j l hl _).mpr hmem)
  · by_contra hc
    push_neg at hc
    have hmem : ((ofRowLens l hl).colLen j, j) ∈ ofRowLens l hl := by
      rw [mem_ofRowLens]
      exact (lt_length_filter_iff j l hl _).mp hc
    exact (lt_irrefl _) (mem_iff_lt_colLen.mp hmem)

/-- **The two hook encodings agree on every cell.** -/
theorem hook_ofRowLens (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) {i j : ℕ}
    (hij : (i, j) ∈ ofRowLens l hl) :
    hookAt l i j = QOU.QBeta.WenzlWeight.hook (ofRowLens l hl) (i, j) := by
  have hrow := mem_iff_lt_rowLen.mp hij
  have hcol := mem_iff_lt_colLen.mp hij
  obtain ⟨hi, hj⟩ := mem_ofRowLens.mp hij
  have hr : (ofRowLens l hl).rowLen i = l[i] := rowLen_ofRowLens ⟨i, hi⟩
  have hc := colLen_ofRowLens l hl j
  have hhead : j < l.headI := by
    cases l with
    | nil => simp at hi
    | cons a t =>
      simp only [List.headI_cons]
      cases i with
      | zero => simpa using hj
      | succ k =>
        have := List.rel_of_sorted_cons hl _ (List.getElem_mem (l := t) (by simp at hi; omega))
        simp only [List.getElem_cons_succ] at hj
        omega
  unfold hookAt QOU.QBeta.WenzlWeight.hook conjugate
  rw [List.getD_eq_getElem _ _ hi, List.getD_eq_getElem _ _ (by simpa using hhead)]
  simp only [List.getElem_map, List.getElem_range]
  rw [hr, ← hc]
  rw [hr] at hrow
  omega

/-- Products over `List.range` are `Finset.range` products. -/
theorem list_range_map_prod {M : Type*} [CommMonoid M] (g : ℕ → M) :
    ∀ n : ℕ, ((List.range n).map g).prod = ∏ i ∈ range n, g i
  | 0 => by simp
  | n + 1 => by
    rw [List.range_succ, List.map_append, List.prod_append, list_range_map_prod g n,
      prod_range_succ]
    simp

theorem list_range_flatMap_prod {M : Type*} [CommMonoid M] (f : ℕ → M) (L : ℕ → List ℕ) :
    ∀ n : ℕ, (((List.range n).flatMap L).map f).prod = ∏ i ∈ range n, ((L i).map f).prod
  | 0 => by simp
  | n + 1 => by
    rw [List.range_succ, List.flatMap_append, List.map_append, List.prod_append,
      list_range_flatMap_prod f L n, prod_range_succ]
    simp

/-- The cells of `ofRowLens l` as an indexed union of rows. -/
theorem cells_ofRowLens (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    (ofRowLens l hl).cells
      = (range l.length).biUnion fun i => (range (l.getD i 0)).map ⟨(i, ·), fun _ _ h => by
          simpa using h⟩ := by
  ext ⟨i, j⟩
  simp only [mem_cells, mem_ofRowLens, mem_biUnion, mem_range, mem_map,
    Function.Embedding.coeFn_mk, Prod.mk.injEq]
  constructor
  · rintro ⟨hi, hj⟩
    exact ⟨i, hi, j, by rwa [List.getD_eq_getElem _ _ hi], rfl, rfl⟩
  · rintro ⟨a, ha, b, hb, rfl, rfl⟩
    exact ⟨ha, by rwa [List.getD_eq_getElem _ _ ha] at hb⟩

/-- **The list hook product is the diagram hook product.** -/
theorem hooks_prod_eq {M : Type*} [CommMonoid M] (f : ℕ → M) (l : List ℕ)
    (hl : List.Sorted (· ≥ ·) l) :
    ((hooks l).map f).prod
      = ∏ x ∈ (ofRowLens l hl).cells, f (QOU.QBeta.WenzlWeight.hook (ofRowLens l hl) x) := by
  classical
  rw [hooks, list_range_flatMap_prod, cells_ofRowLens l hl, prod_biUnion]
  · refine prod_congr rfl fun i hi => ?_
    rw [List.map_map, list_range_map_prod, prod_map]
    refine prod_congr rfl fun j hj => ?_
    simp only [Function.comp_apply, Function.Embedding.coeFn_mk]
    rw [hook_ofRowLens l hl]
    rw [mem_ofRowLens]
    rw [mem_range] at hi hj
    exact ⟨hi, by rwa [List.getD_eq_getElem _ _ hi] at hj⟩
  · intro a _ b _ hab
    simp only [Function.onFun]
    rw [Finset.disjoint_left]
    intro x hxa hxb
    simp only [mem_map, Function.Embedding.coeFn_mk] at hxa hxb
    obtain ⟨_, _, rfl⟩ := hxa
    obtain ⟨_, _, h⟩ := hxb
    exact hab (Prod.mk.inj h).1.symm

variable {R : Type*} [Field R]

/-- **The sum-of-powers q-integer is the balanced one.** -/
theorem qInt_eq_qIntBal (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (n : ℕ) :
    qInt q n = QHookDimensionBalanced.qIntBal q n := by
  have hs : q - q⁻¹ ≠ 0 := QHookDimensionBalanced.sub_inv_ne_zero hq hq2
  apply mul_left_cancel₀ hs
  rw [QHookDimensionBalanced.sub_inv_mul_qIntBal q n hq hq2]
  cases n with
  | zero => simp [qInt]
  | succ m =>
    unfold qInt
    have hterm : ∀ i : ℕ, q ^ (2 * (i : ℤ) - (((m + 1 : ℕ) : ℤ) - 1))
        = q⁻¹ ^ m * (q ^ 2) ^ i := by
      intro i
      rw [inv_pow, ← pow_mul, ← zpow_natCast q (2 * i), ← zpow_natCast q m, ← zpow_neg,
        ← zpow_add₀ hq]
      congr 1
      push_cast
      ring
    rw [sum_congr rfl fun i _ => hterm i, ← mul_sum]
    have hg := geom_sum_mul (q ^ 2) (m + 1)
    calc (q - q⁻¹) * (q⁻¹ ^ m * ∑ i ∈ range (m + 1), (q ^ 2) ^ i)
        = q⁻¹ ^ (m + 1) * ((∑ i ∈ range (m + 1), (q ^ 2) ^ i) * (q ^ 2 - 1)) := by
          rw [show q - q⁻¹ = q⁻¹ * (q ^ 2 - 1) by
            rw [mul_sub, mul_one, sq, ← mul_assoc, inv_mul_cancel₀ hq, one_mul], pow_succ]
          ring
      _ = q⁻¹ ^ (m + 1) * ((q ^ 2) ^ (m + 1) - 1) := by rw [hg]
      _ = q ^ (m + 1) - q⁻¹ ^ (m + 1) := by
          have h1 : (q ^ 2) ^ (m + 1) = q ^ (m + 1) * q ^ (m + 1) := by rw [← mul_pow, sq]
          have h2 : q⁻¹ ^ (m + 1) * q ^ (m + 1) = 1 := by
            rw [← mul_pow, inv_mul_cancel₀ hq, one_pow]
          rw [h1]
          linear_combination q ^ (m + 1) * h2

theorem qFact_eq_prod (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    ∀ N : ℕ, qFact q N = ∏ j ∈ range N, QHookDimensionBalanced.qIntBal q (j + 1)
  | 0 => by simp [qFact]
  | N + 1 => by
    rw [qFact, qFact_eq_prod q hq hq2 N, prod_range_succ, qInt_eq_qIntBal q hq hq2, mul_comm]

/-- **Production's `dimQ` on a partition is the diagram hook formula.** For `λ ⊢ N` with sorted
parts `l`, `dimQ q l = ∏_{j < N} [j+1]_q / ∏_{x ∈ λ} [h(x)]_q`. -/
theorem dimQ_partition_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) {N : ℕ} (lam : Nat.Partition N) :
    dimQ q (lam.parts.sort (· ≥ ·))
      = (∏ j ∈ range N, QHookDimensionBalanced.qIntBal q (j + 1))
        / ∏ x ∈ (QOU.Mathlib.partitionShape lam).cells,
            QHookDimensionBalanced.qIntBal q
              (QOU.QBeta.WenzlWeight.hook (QOU.Mathlib.partitionShape lam) x) := by
  have hsum : (lam.parts.sort (· ≥ ·)).sum = N := by
    rw [← Multiset.sum_coe, Multiset.sort_eq, lam.parts_sum]
  unfold dimQ
  rw [hsum, qFact_eq_prod q hq hq2, QOU.Mathlib.partitionShape,
    ← hooks_prod_eq (QHookDimensionBalanced.qIntBal q) _ (Multiset.sort_sorted _ _)]
  congr 1
  congr 1
  exact List.map_congr_left (fun h _ => qInt_eq_qIntBal q hq hq2 h)

end QOU.Mass.QHookDiagram
