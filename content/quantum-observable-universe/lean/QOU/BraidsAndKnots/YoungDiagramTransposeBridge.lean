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

/-! ## The conjugation involution on sorted positive lists -/

theorem getD_zero_eq_headD (m : List ℕ) : m.getD 0 0 = m.headD 0 := by
  cases m <;> rfl

theorem length_conj (m : List ℕ) : (conj m).length = m.headD 0 := by
  unfold conj
  simp

/-- `conj` of ANY list is weakly decreasing: the count of parts exceeding `j` is antitone. -/
theorem conj_sorted (m : List ℕ) : (conj m).Sorted (· ≥ ·) := by
  unfold conj
  exact List.Pairwise.map _
    (fun a b hab => List.countP_mono_left fun x _ hx => by
      simp only [decide_eq_true_iff] at hx ⊢
      exact lt_trans hab hx)
    (List.pairwise_lt_range)

/-- Counting `j < k` over `List.range n` gives `min n k`. -/
theorem countP_range_lt (n k : ℕ) :
    (List.range n).countP (fun j => decide (j < k)) = min n k := by
  induction n with
  | zero => simp
  | succ m ih =>
      rw [List.range_succ, List.countP_append, ih]
      by_cases h : m < k <;> simp [h] <;> omega

/-- Counting parts of `conj l` exceeding `c` caps the staircase: `min (headD) (l_c)`. -/
theorem countP_conj (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (c : ℕ) :
    (conj l).countP (fun x => decide (c < x)) = min (l.headD 0) (l.getD c 0) := by
  unfold conj
  have hfun : ((fun x => decide (c < x)) ∘ fun j => l.countP fun x => decide (j < x))
      = fun j => decide (j < l.getD c 0) := by
    funext j
    simp only [Function.comp_apply]
    rw [decide_eq_decide]
    exact lt_countP_iff l hs j c
  rw [List.countP_map, hfun, countP_range_lt]

/-- **`conj` is an involution on sorted positive lists**: `conj (conj l) = l`. The staircase
equivalence makes this getD-extensional: `(conj (conj l))_c = min (headD) (l_c) = l_c`. Positivity
is genuinely needed (a trailing `0` part is erased by `conj`). -/
theorem conj_conj (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (hpos : ∀ x ∈ l, 0 < x) :
    conj (conj l) = l := by
  have hlen : (conj (conj l)).length = l.length := by
    rw [length_conj, ← getD_zero_eq_headD, conj_getD l hs 0]
    exact List.countP_eq_length.mpr fun x hx => by simpa using hpos x hx
  apply List.ext_getElem hlen
  intro i h1 h2
  rw [← List.getD_eq_getElem _ 0 h1, ← List.getD_eq_getElem _ 0 h2,
    conj_getD (conj l) (conj_sorted l) i, countP_conj l hs i,
    Nat.min_eq_right (mem_le_headD l hs _ (by
      rw [List.getD_eq_getElem _ 0 h2]
      exact List.getElem_mem h2))]

/-- `Σ_{i < len} l_i = l.sum` in `getD` form. -/
theorem sum_getD_range (l : List ℕ) : ∑ i ∈ Finset.range l.length, l.getD i 0 = l.sum := by
  induction l with
  | nil => simp
  | cons a t ih =>
      rw [List.length_cons, Finset.sum_range_succ', List.sum_cons]
      simp only [List.getD_cons_succ, List.getD_cons_zero]
      rw [ih]
      omega

/-- The cell count of a list diagram is its size: `|cells l| = Σ l_i`. -/
theorem card_cells (l : List ℕ) : (cells l).card = l.sum := by
  unfold cells
  rw [Finset.card_biUnion (fun x _ y _ hxy => Finset.disjoint_left.mpr (by
      rintro p hp hq
      obtain ⟨j, _, rfl⟩ := Finset.mem_map.mp hp
      obtain ⟨j', _, h'⟩ := Finset.mem_map.mp hq
      exact hxy (by simpa using (congrArg Prod.fst h').symm)))]
  simp only [Finset.card_map, Finset.card_range]
  exact sum_getD_range l

/-- **Conjugation preserves the size** `|λ'| = |λ|` — via the cell bijection, not arithmetic:
`(conj l).sum = |cells (conj l)| = |transpose (cells l)| = |cells l| = l.sum`. -/
theorem sum_conj (l : List ℕ) (hs : l.Sorted (· ≥ ·)) : (conj l).sum = l.sum := by
  rw [← card_cells, ← card_cells, cells_conj l hs]
  unfold transpose
  exact Finset.card_map _

/-! ## Hook-product transpose symmetry and `sytDim (conj l) = sytDim l` -/

/-- List-range product = Finset-range product (ℕ; the `hookProd` inner/outer form). -/
theorem list_prod_map_range (n : ℕ) (f : ℕ → ℕ) :
    ((List.range n).map f).prod = ∏ j ∈ Finset.range n, f j := by
  induction n with
  | zero => simp
  | succ m ih =>
      rw [List.range_succ, List.map_append, List.prod_append, Finset.prod_range_succ, ih]
      simp

/-- `hookProd` as a product over the cell set (hook of `(i,j)` written in the definition's
literal `ℕ`-subtraction order). -/
theorem hookProd_eq_prod_cells (l : List ℕ) :
    hookProd l = ∏ p ∈ cells l,
      (l.getD p.1 0 + (conj l).getD p.2 0 - p.2 - p.1 - 1) := by
  unfold hookProd cells
  rw [Finset.prod_biUnion (fun x _ y _ hxy => Finset.disjoint_left.mpr (by
      rintro p hp hq
      obtain ⟨j, _, rfl⟩ := Finset.mem_map.mp hp
      obtain ⟨j', _, h'⟩ := Finset.mem_map.mp hq
      exact hxy (by simpa using (congrArg Prod.fst h').symm)))]
  rw [list_prod_map_range]
  refine Finset.prod_congr rfl fun i _ => ?_
  rw [list_prod_map_range]
  rw [Finset.prod_map]
  simp only [Function.Embedding.coeFn_mk]

/-- **Hook products are transpose-invariant** (list level): `hookProd (conj l) = hookProd l`.
Transport the cell product along `cells_conj` and identify hooks pairwise via `conj_conj`
(`hook_{λ'}(j,i) = hook_λ(i,j)`). -/
theorem hookProd_conj (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (hpos : ∀ x ∈ l, 0 < x) :
    hookProd (conj l) = hookProd l := by
  rw [hookProd_eq_prod_cells, hookProd_eq_prod_cells, cells_conj l hs]
  unfold transpose
  rw [Finset.prod_map]
  refine Finset.prod_congr rfl fun p _ => ?_
  simp only [Function.Embedding.coeFn_mk, Prod.fst_swap, Prod.snd_swap]
  rw [conj_conj l hs hpos]
  omega

/-- **The hook-length dimension is conjugation-invariant** (list level):
`sytDim (conj l) = sytDim l` — i.e. `f^{λ'} = f^λ`, since `|λ'| = |λ|` and the hook multiset is
preserved. This is the remaining factor the kernel-summand pairing needed beyond `omega3_conj`. -/
theorem sytDim_conj (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (hpos : ∀ x ∈ l, 0 < x) :
    sytDim (conj l) = sytDim l := by
  unfold sytDim
  rw [sum_conj l hs, hookProd_conj l hs hpos]

/-! ## The kernel-summand pairing -/

/-- **The covariance-kernel summand is invariant under genuine list-level conjugation, all `k`**:
`(f^{λ'})³·ω₃(λ') = (f^λ)³·ω₃(λ)` for every sorted positive `l`. Both factors are separately
invariant (`sytDim_conj`, `omega3_conj`), so the kernel `Σ_λ (f^λ)³ ω₃(λ)` pairs off along
`λ ↔ λ'` with self-conjugate diagrams as fixed points — at every level, not just `k ≤ 6`/`k ≤ 7`.
Scope-honest: a structural symmetry of the summand; it supplies **no** sign information
(`YoungDiagramTranspose` proves the summand is transpose-even), so
`covariance_kernel_conjecture` stays open. -/
theorem kernel_summand_conj (k : ℕ) (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (hpos : ∀ x ∈ l, 0 < x) :
    (sytDim (conj l) : ℤ) ^ 3 * omega3 k (conj l)
      = (sytDim l : ℤ) ^ 3 * omega3 k l := by
  rw [sytDim_conj l hs hpos, omega3_conj k l hs]

end QOU.BraidsAndKnots.YoungDiagramTransposeBridge
