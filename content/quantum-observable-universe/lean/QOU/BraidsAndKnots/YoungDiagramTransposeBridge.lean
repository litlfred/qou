import QOU.BraidsAndKnots.YoungDiagramKernel
import QOU.BraidsAndKnots.YoungDiagramTranspose
import Mathlib.Data.List.Sort
import Mathlib.Data.List.GetD

/-!
# QOU.BraidsAndKnots.YoungDiagramTransposeBridge — the sorted-List ↔ cell-model transpose bridge

`YoungDiagramKernel` states the Δ_λ covariance kernel on the weakly-decreasing `List ℕ` encoding
and proves conjugation-invariance of the content square only by bounded `decide`
(`contentSq_conj_invariant_of_le_six`, `k ≤ 6`), noting: *"the general (∀ sorted `l`) statement
follows from the sorted-List transpose bijection … that infra is not yet built here."*
`YoungDiagramTranspose` proves the transpose parity facts (`csq_transpose`, `csum_transpose`) on
the abstract cell model `Finset (ℕ × ℕ)`, asserting in prose that the coordinate swap "is realized
by `YoungDiagramKernel.conj`".

This file **builds that missing bridge**, sorry-free and for **all** `k`:

* `cells l` — the cell set `{(i,j) : j < l_i}` of a list diagram, as a disjoint row `biUnion`
  (`mem_cells`, no sortedness needed);
* `contentSq_eq_csq` — the kernel file's `contentSq` **is** the cell-model `csq` (row-by-row
  re-summation);
* `lt_countP_iff` — the **staircase equivalence** `c < #{x ∈ l : r < x} ↔ r < l_c` for sorted `l`
  (single induction on `l`);
* `conj_getD` — `(conj l)_c = #{x ∈ l : c < x}` for sorted `l` (both in- and out-of-range);
* `cells_conj` — **the bridge**: `cells (conj l) = transpose (cells l)` for sorted `l`;
* `contentSq_conj` / `omega3_conj` — conjugation-invariance of the content square and of the
  3-cycle eigenvalue `ω₃` for **all** sorted `l` (upgrading the `decide`-bounded `k ≤ 6` lemmas to
  the general statement the kernel file called for), by transport through `csq_transpose`.

Scope (honest): **infrastructure only** — the kernel sign `covariance_kernel_conjecture` stays
OPEN; indeed `YoungDiagramTranspose` proves the transpose route *cannot* sign `T₃` (the summand is
transpose-even). What this file adds is the exact pairing structure for every `k` (previously
`k ≤ 6`): the kernel summand is invariant under the genuine list-level conjugation, so summands
pair off along `λ ↔ λ'` with self-conjugate diagrams as fixed points.

Base ring: `ℤ` (contents are integers); everything else is `ℕ`-combinatorics. Standalone library
file (no `.ts`/`.md` sibling), verified per-file by `lean`-direct, like its two parents.

-- Ref: [manuscript] docs/audits/2026-07-19-deltalambda-kernel-sign-structural-narrowing.md
-/

namespace QOU.BraidsAndKnots.YoungDiagramTransposeBridge

open QOU.BraidsAndKnots.YoungDiagramKernel
open QOU.BraidsAndKnots.YoungDiagramTranspose
open Finset

/-! ## The cell set of a list diagram -/

/-- The cell set `{(i, j) : i < len l, j < l_i}` of a list diagram, as a disjoint union of rows. -/
def cells (l : List ℕ) : Finset (ℕ × ℕ) :=
  (Finset.range l.length).biUnion fun i =>
    (Finset.range (l.getD i 0)).map ⟨fun j => (i, j), fun a b h => by simpa using h⟩

/-- Cell membership is exactly `j < l_i` (the row bound `i < len` is implied: out-of-range rows
are empty since `getD` defaults to `0`). No sortedness needed. -/
theorem mem_cells (l : List ℕ) (p : ℕ × ℕ) : p ∈ cells l ↔ p.2 < l.getD p.1 0 := by
  unfold cells
  simp only [Finset.mem_biUnion, Finset.mem_range, Finset.mem_map,
    Function.Embedding.coeFn_mk]
  constructor
  · rintro ⟨i, _, j, hj, rfl⟩
    simpa using hj
  · intro h
    have hlen : p.1 < l.length := by
      by_contra hle
      rw [List.getD_eq_default _ _ (le_of_not_gt hle)] at h
      exact absurd h (Nat.not_lt_zero _)
    exact ⟨p.1, hlen, p.2, h, Prod.mk.eta⟩

/-- List-range sum = Finset-range sum (the `List.range`-map form used by `contentSq`). -/
theorem list_sum_map_range (n : ℕ) (f : ℕ → ℤ) :
    ((List.range n).map f).sum = ∑ j ∈ Finset.range n, f j := by
  induction n with
  | zero => simp
  | succ m ih =>
      rw [List.range_succ, List.map_append, List.sum_append, Finset.sum_range_succ, ih]
      simp

/-- The inner row sum in `contentSq`'s exact elaborated form (the `(j : ℤ)` binder ascription
coerces the `List.range` elementwise), re-expressed as a `Finset.range` sum. Stated with source
syntax identical to the definition so `rw` matches the unfolded term. -/
theorem inner_row_sum (n i : ℕ) :
    ((List.range n).map (fun j => ((j : ℤ) - (i : ℤ)) ^ 2)).sum
      = ∑ j ∈ Finset.range n, ((j : ℤ) - (i : ℤ)) ^ 2 := by
  induction n with
  | zero => simp
  | succ m ih =>
      rw [List.range_succ, Finset.sum_range_succ, ← ih]
      simp

/-- `contentSq` as a nested `Finset.range` sum. -/
theorem contentSq_eq_finset_sum (l : List ℕ) :
    contentSq l
      = ∑ i ∈ Finset.range l.length, ∑ j ∈ Finset.range (l.getD i 0),
          ((j : ℤ) - (i : ℤ)) ^ 2 := by
  unfold contentSq
  rw [list_sum_map_range]
  exact Finset.sum_congr rfl fun i _ => inner_row_sum (l.getD i 0) i

/-- **`contentSq` is the cell-model `csq`.** The kernel file's row-nested list sum re-sums over
the cell set, so the abstract transpose-parity lemmas of `YoungDiagramTranspose` apply to the
kernel's own content square. -/
theorem contentSq_eq_csq (l : List ℕ) : contentSq l = csq (cells l) := by
  rw [contentSq_eq_finset_sum]
  unfold csq cells
  rw [Finset.sum_biUnion (fun x _ y _ hxy => Finset.disjoint_left.mpr (by
      rintro p hp hq
      obtain ⟨j, _, rfl⟩ := Finset.mem_map.mp hp
      obtain ⟨j', _, h'⟩ := Finset.mem_map.mp hq
      exact hxy (by simpa using (congrArg Prod.fst h').symm)))]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Finset.sum_map]
  simp only [Function.Embedding.coeFn_mk]

/-! ## The staircase equivalence and `conj` on sorted lists -/

/-- Every element of a weakly-decreasing list is at most its head. -/
theorem mem_le_headD (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (x : ℕ) (hx : x ∈ l) :
    x ≤ l.headD 0 := by
  cases l with
  | nil => cases hx
  | cons a t =>
      rcases List.mem_cons.mp hx with rfl | hxt
      · simp
      · exact (List.sorted_cons.mp hs).1 x hxt

/-- **The staircase equivalence** for a weakly-decreasing list: `c < #{x ∈ l : r < x} ↔ r < l_c`.
The count of parts exceeding `r` is an initial segment of row indices, so membership of `c` in it
is exactly the cell condition `r < l_c` — the heart of the transpose correspondence. -/
theorem lt_countP_iff (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (r c : ℕ) :
    c < l.countP (fun x => decide (r < x)) ↔ r < l.getD c 0 := by
  induction l generalizing c with
  | nil => simp
  | cons a t ih =>
      obtain ⟨ha, hst⟩ := List.sorted_cons.mp hs
      rw [List.countP_cons]
      by_cases hra : r < a
      · rw [if_pos (by simpa using hra)]
        cases c with
        | zero => simpa using hra
        | succ c' =>
            rw [List.getD_cons_succ, add_lt_add_iff_right]
            exact ih hst c'
      · rw [if_neg (by simpa using hra)]
        have ht0 : t.countP (fun x => decide (r < x)) = 0 :=
          List.countP_eq_zero.mpr fun x hx => by
            simpa using not_lt.mpr (le_trans (ha x hx) (not_lt.mp hra))
        rw [ht0]
        simp only [Nat.add_zero, Nat.not_lt_zero, false_iff]
        cases c with
        | zero => simpa using hra
        | succ c' =>
            rw [List.getD_cons_succ]
            by_cases hc' : c' < t.length
            · rw [List.getD_eq_getElem _ _ hc']
              exact not_lt.mpr (le_trans (le_trans (ha _ (List.getElem_mem hc'))
                (not_lt.mp hra)) (le_refl r))
            · rw [List.getD_eq_default _ _ (le_of_not_gt hc')]
              exact Nat.not_lt_zero r

/-- **`conj` in `countP` normal form** on a sorted list: `(conj l)_c = #{x ∈ l : c < x}`, valid at
every index `c` (in range via the defining `range`-map, out of range because a sorted list has no
part exceeding its head). -/
theorem conj_getD (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (c : ℕ) :
    (conj l).getD c 0 = l.countP (fun x => decide (c < x)) := by
  unfold conj
  by_cases hc : c < l.headD 0
  · have hlen : c < ((List.range (l.headD 0)).map
        (fun j => l.countP (fun x => decide (j < x)))).length := by
      simpa using hc
    rw [List.getD_eq_getElem _ _ hlen, List.getElem_map, List.getElem_range]
  · rw [List.getD_eq_default _ _ (by simpa using le_of_not_gt hc)]
    refine (List.countP_eq_zero.mpr fun x hx => ?_).symm
    simpa using not_lt.mpr (le_trans (mem_le_headD l hs x hx) (le_of_not_gt hc))

/-! ## The bridge: list-level `conj` = cell-level `transpose` -/

/-- Transpose membership is coordinate-swap membership. -/
theorem mem_transpose (D : Finset (ℕ × ℕ)) (p : ℕ × ℕ) :
    p ∈ transpose D ↔ Prod.swap p ∈ D := by
  unfold transpose
  constructor
  · intro h
    obtain ⟨q, hq, rfl⟩ := Finset.mem_map.mp h
    simpa using hq
  · intro h
    exact Finset.mem_map.mpr ⟨Prod.swap p, h, Prod.swap_swap p⟩

/-- **The bridge (sorry-free, all `k`).** On a weakly-decreasing list, the cell set of the
list-level conjugate is the coordinate-swap transpose of the cell set:
`cells (conj l) = transpose (cells l)`. This is the statement the two parent files each assumed
about the other in prose. Proof: both memberships reduce to the staircase `r < l_c`. -/
theorem cells_conj (l : List ℕ) (hs : l.Sorted (· ≥ ·)) :
    cells (conj l) = transpose (cells l) := by
  ext p
  rw [mem_cells, mem_transpose, mem_cells, conj_getD l hs, lt_countP_iff l hs]
  rfl

/-- **Conjugation-invariance of the content square, all sorted `l`** — the general statement
`YoungDiagramKernel` carried only as `decide`-bounded `k ≤ 6`
(`contentSq_conj_invariant_of_le_six`). Transport through the cell model and apply the abstract
transpose-evenness `csq_transpose`. -/
theorem contentSq_conj (l : List ℕ) (hs : l.Sorted (· ≥ ·)) :
    contentSq (conj l) = contentSq l := by
  rw [contentSq_eq_csq, contentSq_eq_csq, cells_conj l hs, csq_transpose]

/-- **Conjugation-invariance of the 3-cycle class-sum eigenvalue `ω₃`, all `k`, all sorted `l`**
(upgrading `omega3_conj_invariant_of_le_six`). Consequence: the covariance-kernel summand
`(f^λ)³·ω₃(λ)` pairs off along `λ ↔ λ'` at every level `k` — provided the dimension is also
conjugation-invariant, which holds by hook-length transpose symmetry and is the remaining
(separate) list-level lemma. -/
theorem omega3_conj (k : ℕ) (l : List ℕ) (hs : l.Sorted (· ≥ ·)) :
    omega3 k (conj l) = omega3 k l := by
  unfold omega3
  rw [contentSq_conj l hs]

end QOU.BraidsAndKnots.YoungDiagramTransposeBridge
