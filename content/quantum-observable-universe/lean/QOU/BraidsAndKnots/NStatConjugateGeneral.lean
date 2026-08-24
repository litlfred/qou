/-
  (†)  `n(λ) = Σ_i C(λ'_i, 2)`  for GENERAL partitions — the textbook
  double-counting identity, proved sorry-free for ALL `n`.

  Context (epic `qou-r2nh`, bean `qou-r0xk`, parent `qou-bvpp`/PR #4558).
  `DeltaLambdaDTIndexGeneralN.lean` (PR #4558) lifts the DT / 3d-index Euler
  characteristic unification `dtEuler = deltaLambda` off the finite
  `PartitionOf5` enum to ALL `n`, with ONE residual conditional leg: matching
  the a-function parity `(-1)^{n(λ)}` to the geometric chirality
  `sgn(w₀^{S_{λ'}}) = (-1)^{Σ_i C(λ'_i,2)}` needs the single identity

        n(λ)  =  Σ_i C(λ'_i, 2)                                          (†)

  i.e. `aStat parts = sumChoose2 (conjugate parts)` (`λ'` = conjugate/transpose).
  There it is discharged only at `n ≤ 5` (`PartitionOf5.nStat_eq_sumChoose2_conj`
  by `decide`), leaving the general-`n` proof of (†) as the sole gap in the
  general-`n` chirality leg (the conditional lemma
  `parity_eq_w0_sign_of_nStat_eq_sumChoose2`).

  This file proves (†) for EVERY partition, sorry-free, by a genuine
  double-counting induction over the Young diagram (row-peeling, mirroring the
  left-fold that defines `n(λ)`).  With (†) general, the a-function-parity ↔
  geometric-longest-element-sign match is UNCONDITIONAL for all `n`, so the
  general-`n` DT unification's chirality leg is no longer `n ≤ 5`-restricted.

  Method (both sides count vertical domino-pairs of cells).
  `n(λ) = Σ_i (i-1)λ_i` counts, per cell `(i,c)`, the `(i-1)` cells strictly
  above it in the same column (all present since `λ` is decreasing) — the pairs
  of same-column cells counted by ROW.  `Σ_i C(λ'_i,2)` counts the same
  same-column pairs by COLUMN (`C(λ'_j,2)` vertical pairs in column `j`).  The
  Lean proof realises this as: `aStat` peels the largest row
  (`aStat (a::l) = aStat l + l.sum`), the conjugate peels the same row
  (`conjugate (a::l) = addRow a (conjugate l)`), and both increments agree
  (`sumChoose2 (addRow a c) = sumChoose2 c + Σ c` when `c.length ≤ a`, via
  Pascal `C(c+1,2) = C(c,2) + c`).

  Discipline.  The statements and proofs are purely combinatorial — base ring
  `ℕ` (statistics/dimensions) and `ℤ` (signs), no `ℝ` in the mathematical content
  (§7c).  (The transitive import cone does pull in `ℝ` via the reused
  `PartitionOf5` from `S5SO3FiberAction`; extracting a combinatorics-only core of
  `S5SO3FiberAction` is a beaned follow-up, not required for these facts.)
  Nothing fitted, nothing wired to
  production — this is the per-partition `Δ_λ` chirality sign, not a
  binding-energy magnitude (the many-body scalar `r*` stays open, walled).

  Names here (`aStat`, `chiralityParity`) are defeq to
  `DeltaLambdaDTIndexGeneralN`'s `nStatList` / `deltaSignParity` (identical fold
  / `(-1)^N`); a distinct sub-naming avoids a decl clash until #4558 lands, at
  which point (†) below discharges `parity_eq_w0_sign_of_nStat_eq_sumChoose2`
  for all `n` verbatim (see `chiralityParity_eq_w0_sign_general`).

  Primary source: the identity `n(λ) = Σ_i C(λ'_i,2)` is standard;
  -- Ref: [macdonald1995] https://doi.org/10.1093/oso/9780198534891.001.0001
  (I.1, Ex. 3: `n(λ) = Σ_i (i-1)λ_i = Σ_i C(λ'_i,2)`).
  -- Ref: [james1984representation] https://doi.org/10.1007/978-1-4684-9458-7
-/
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.List.Sort
import Mathlib.Tactic.Ring
import QOU.BraidsAndKnots.S5SO3FiberAction

namespace QOU.BraidsAndKnots

/-! ## The a-function statistic `n(λ)` on a general partition -/

/-- The `(index, running-sum)` fold step defining `n(λ)`: on reading part `part`
    at current index `acc.1`, advance the index and add `acc.1 · part`.  This is
    the same step used inline by `PartitionOf5.nStat` and
    `DeltaLambdaDTIndexGeneralN.nStatList`; naming it keeps `foldl` rewrites
    clean.  (Unfolds to their inline lambda, so `aStat` stays defeq to both.) -/
def stepf : ℕ × ℕ → ℕ → ℕ × ℕ := fun acc part => (acc.1 + 1, acc.2 + acc.1 * part)

@[simp] theorem stepf_apply (i s p : ℕ) : stepf (i, s) p = (i + 1, s + i * p) := rfl

/-- `n(λ) = Σ_i (i-1)·λ_i` on a partition's parts (0-indexed `Σ i·λ_i`), via the
    `(index, sum)` left fold.  Defeq to `PartitionOf5.nStat` and
    `DeltaLambdaDTIndexGeneralN.nStatList`. -/
def aStat (parts : List ℕ) : ℕ := (parts.foldl stepf (0, 0)).2

/-- Closed form of the fold's `.2` component under an arbitrary start `(i, s)`:
    `s + n(λ) + i·Σλ`.  The engine behind the largest-row peel `aStat_cons`. -/
theorem foldl_stepf (l : List ℕ) (i s : ℕ) :
    (l.foldl stepf (i, s)).2 = s + (l.foldl stepf (0, 0)).2 + i * l.sum := by
  induction l generalizing i s with
  | nil => simp
  | cons p t ih =>
    rw [List.foldl_cons, List.foldl_cons, stepf_apply, stepf_apply,
        ih (i + 1) (s + i * p), ih (0 + 1) (0 + 0 * p), List.sum_cons]
    ring

/-- **Largest-row peel.**  `n(a :: l) = n(l) + Σ l`: removing the largest (first)
    row `a` from a decreasing partition drops the `n`-statistic by exactly the
    number of remaining cells `Σ l = |λ| - λ_1`.  (The head sits at index 0, so
    contributes `0` and only shifts the remaining indices up by one.) -/
theorem aStat_cons (a : ℕ) (l : List ℕ) : aStat (a :: l) = aStat l + l.sum := by
  unfold aStat
  rw [List.foldl_cons, stepf_apply, foldl_stepf l (0 + 1) (0 + 0 * a)]
  omega

/-! ## The conjugate (transpose) partition, as a row-adding recursion -/

/-- Add a new largest row of length `a` on top of a Young diagram recorded by its
    column lengths `c`: increment the first `a` column lengths by 1, and append
    fresh length-1 columns for any overhang beyond `c.length`.  This is the
    transpose of "prepend a part `a`". -/
def addRow : ℕ → List ℕ → List ℕ
  | 0,     c         => c
  | (a+1), []        => 1 :: addRow a []
  | (a+1), (c :: cs) => (c + 1) :: addRow a cs

/-- The conjugate/transpose `λ'` of a partition given by its parts (largest
    first): fold the parts as successive largest rows.  For a decreasing `λ`,
    `conjugate λ` is the genuine transpose (`conjugate p.parts = p.conjParts`,
    checked below). -/
def conjugate : List ℕ → List ℕ
  | []       => []
  | (a :: l) => addRow a (conjugate l)

/-! ### Elementary facts about `sumChoose2` and `addRow` -/

/-- `sumChoose2` (from `S5SO3FiberAction`) on a cons. -/
theorem sumChoose2_cons (x : ℕ) (xs : List ℕ) :
    sumChoose2 (x :: xs) = x * (x - 1) / 2 + sumChoose2 xs := by
  simp only [sumChoose2, List.map_cons, List.sum_cons]

/-- Adding a length-`a` row adds exactly `a` cells: `Σ (addRow a c) = Σ c + a`. -/
theorem sum_addRow (a : ℕ) (c : List ℕ) : (addRow a c).sum = c.sum + a := by
  induction a generalizing c with
  | zero => simp [addRow]
  | succ a ih =>
    cases c with
    | nil => simp only [addRow, List.sum_cons, List.sum_nil, ih []]; omega
    | cons c0 cs => simp only [addRow, List.sum_cons, ih cs]; omega

/-- `addRow a c` has length `max a c.length` (the taller of new row / diagram). -/
theorem length_addRow (a : ℕ) (c : List ℕ) :
    (addRow a c).length = max a c.length := by
  induction a generalizing c with
  | zero => simp only [addRow]; omega
  | succ a ih =>
    cases c with
    | nil => simp only [addRow, List.length_cons, List.length_nil, ih []]; omega
    | cons c0 cs => simp only [addRow, List.length_cons, ih cs]; omega

/-- Pascal's rule in the `C(·,2) = ·(·-1)/2` form: `C(c+1,2) = C(c,2) + c`. -/
theorem choose2_succ (c : ℕ) :
    (c + 1) * ((c + 1) - 1) / 2 = c * (c - 1) / 2 + c := by
  have e : (c + 1).choose 2 = c.choose 1 + c.choose 2 := Nat.choose_succ_succ c 1
  rw [Nat.choose_one_right] at e
  rw [Nat.choose_two_right, Nat.choose_two_right] at e
  omega

/-- **The row-increment on `sumChoose2`.**  When the new row `a` is at least as
    wide as the current diagram (`c.length ≤ a` — the case that occurs in the
    conjugate recursion for a decreasing partition), adding it increments the
    column-pair count `sumChoose2` by exactly the cell count `Σ c`.  Each of the
    `c.length` existing columns gains one cell, contributing `+ c_j` (Pascal);
    the overhang columns start empty (`C(1,2)=0`). -/
theorem sumChoose2_addRow_ge (a : ℕ) (c : List ℕ) (h : c.length ≤ a) :
    sumChoose2 (addRow a c) = sumChoose2 c + c.sum := by
  induction a generalizing c with
  | zero =>
    cases c with
    | nil => simp [addRow, sumChoose2]
    | cons c0 cs => simp only [List.length_cons] at h; omega
  | succ a ih =>
    cases c with
    | nil =>
      simp only [addRow]
      rw [sumChoose2_cons, ih [] (Nat.zero_le a)]
      simp [sumChoose2]
    | cons c0 cs =>
      have hcs : cs.length ≤ a := by simp only [List.length_cons] at h; omega
      simp only [addRow]
      rw [sumChoose2_cons, sumChoose2_cons, ih cs hcs, List.sum_cons]
      have := choose2_succ c0
      omega

/-! ### The conjugate preserves cell count, and is bounded by the largest part -/

/-- The conjugate has the same number of cells: `Σ (conjugate l) = Σ l`. -/
theorem sum_conjugate (l : List ℕ) : (conjugate l).sum = l.sum := by
  induction l with
  | nil => simp [conjugate]
  | cons a l ih => simp only [conjugate, sum_addRow, List.sum_cons, ih]; omega

/-- When `a` bounds every part of `l`, the conjugate's length (= the largest
    part) is `≤ a`.  Supplies the `c.length ≤ a` hypothesis of
    `sumChoose2_addRow_ge` at each peel of a decreasing partition. -/
theorem length_conjugate_le (a : ℕ) (l : List ℕ) (hbound : ∀ x ∈ l, x ≤ a) :
    (conjugate l).length ≤ a := by
  induction l with
  | nil => simp [conjugate]
  | cons b l ih =>
    have hb : b ≤ a := hbound b (by simp)
    have hrest : ∀ x ∈ l, x ≤ a := fun x hx => hbound x (by simp [hx])
    have hlen := ih hrest
    simp only [conjugate, length_addRow]
    omega

/-! ## (†) — `n(λ) = Σ_i C(λ'_i, 2)` for every partition -/

/-- **(†), general `n` (sorry-free).**  For any partition `λ` given by a
    weakly-decreasing list of parts, the a-function statistic equals the sum of
    `C(·,2)` over the conjugate partition's parts:

        `aStat l = sumChoose2 (conjugate l)`.

    Proof: induction on `l` (largest-row peeling).  Both sides drop by the same
    increment `Σ (tail)` when the largest row is removed — `aStat` by
    `aStat_cons`, `sumChoose2 ∘ conjugate` by `sumChoose2_addRow_ge` (its
    `c.length ≤ a` hypothesis furnished by `length_conjugate_le` from
    decreasingness) together with `sum_conjugate`. -/
theorem aStat_eq_sumChoose2_conjugate (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    aStat l = sumChoose2 (conjugate l) := by
  induction l with
  | nil => simp [aStat, conjugate, sumChoose2]
  | cons a l ih =>
    rw [List.sorted_cons] at hl
    obtain ⟨hhead, htail⟩ := hl
    have hbound : ∀ x ∈ l, x ≤ a := fun x hx => hhead x hx
    have hlen : (conjugate l).length ≤ a := length_conjugate_le a l hbound
    rw [aStat_cons]
    simp only [conjugate]
    rw [sumChoose2_addRow_ge a (conjugate l) hlen, sum_conjugate, ih htail]

/-! ## Consequence: the general-`n` geometric-chirality leg is UNCONDITIONAL

    `DeltaLambdaDTIndexGeneralN.deltaSignParity N := (-1)^N` is the a-function
    parity chirality; here `chiralityParity` is defeq to it.  The conditional
    lemma `parity_eq_w0_sign_of_nStat_eq_sumChoose2` matched it to the geometric
    sign `(-1)^{Σ_i C(λ'_i,2)}` *given* (†); (†) now holds for all `n`, so the
    match is unconditional. -/

/-- Chirality parity `(-1)^{n(λ)}` (defeq to `deltaSignParity` in
    `DeltaLambdaDTIndexGeneralN`). -/
def chiralityParity (N : ℕ) : ℤ := (-1 : ℤ) ^ N

/-- **UNCONDITIONAL general-`n` geometric chirality.**  For every partition, the
    a-function-parity chirality `(-1)^{n(λ)}` equals the geometric
    longest-element sign `(-1)^{Σ_i C(λ'_i,2)} = sgn(w₀^{S_{λ'}})` of the
    conjugate Young subgroup — the leg left conditional at `n ≤ 5` in
    `DeltaLambdaDTIndexGeneralN`, now closed for all `n` by (†). -/
theorem chiralityParity_eq_w0_sign_general
    (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    chiralityParity (aStat l) = (-1 : ℤ) ^ (sumChoose2 (conjugate l)) := by
  unfold chiralityParity
  rw [aStat_eq_sumChoose2_conjugate l hl]

/-! ## Corpus bridge: the general identity SUBSUMES the `n = 5` `decide` anchor

    `PartitionOf5.nStat` / `PartitionOf5.conjParts` (on `main`, from
    `S5SO3FiberAction`) are the `n = 5` specialisations.  The general (†) recovers
    `PartitionOf5.nStat_eq_sumChoose2_conj` for each of the seven `λ ⊢ 5` WITHOUT
    a per-partition `decide` — evidence the general theorem subsumes the corpus
    anchor. -/

/-- `aStat` on a block's parts is the corpus `PartitionOf5.nStat` (same fold). -/
theorem aStat_parts (p : PartitionOf5) : aStat p.parts = p.nStat := rfl

/-- The recursive `conjugate` equals the corpus hardcoded `PartitionOf5.conjParts`
    for every `λ ⊢ 5` (a genuine transpose check). -/
theorem conjugate_parts (p : PartitionOf5) : conjugate p.parts = p.conjParts := by
  cases p <;> rfl

/-- **`PartitionOf5.nStat_eq_sumChoose2_conj`, re-derived from the GENERAL (†)**
    (not `decide`).  Each `λ ⊢ 5` has decreasing parts, so the general identity
    applies; with the two bridges above it reproduces the corpus anchor,
    confirming (†) subsumes the finite enum. -/
theorem nStat_eq_sumChoose2_conj_via_general (p : PartitionOf5) :
    p.nStat = sumChoose2 p.conjParts := by
  have hsorted : List.Sorted (· ≥ ·) p.parts := by cases p <;> decide
  rw [← aStat_parts, ← conjugate_parts, aStat_eq_sumChoose2_conjugate p.parts hsorted]

end QOU.BraidsAndKnots
