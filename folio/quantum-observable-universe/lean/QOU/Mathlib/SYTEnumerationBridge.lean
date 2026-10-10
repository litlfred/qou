import QOU.Mathlib.SYTEnumeration
import Mathlib.Data.List.Permutation
import Mathlib.Combinatorics.Young.YoungDiagram

/-!
# QOU.Mathlib.SYTEnumerationBridge — `numSYTenum` as a count of distinct standard fillings

`SYTEnumeration.numSYTenum` is `(allPerms rng).countP (isStdFilling l)` with
`rng = (List.range l.sum).map (·+1) = [1,…,n]` and a hand-rolled structurally-recursive `allPerms`.
This file proves the structural facts that turn that opaque `countP` into a clean characterisation —
the first half of the bridge from the brute-force list count to the genuine
`numStandardYoungTableaux = Nat.card (StandardYoungTableau μ)` (`RSKBurnsideTarget.dimSYT`).

**What is proved here (sorry-free).**

1. `allPerms = List.permutations'` — the hand-rolled generator *is* Mathlib's `permutations'`
   (`allPerms_eq`), because `insertEverywhere = permutations'Aux` definitionally up to recursion
   (`insertEverywhere_eq`).  Hence `a ∈ allPerms l ↔ a.Perm l` (`mem_allPerms_iff_perm`), inherited
   from `List.mem_permutations'`.
2. `numSYTenum l = (standardFillings l).length` (`numSYTenum_eq_length_standardFillings`), where
   `standardFillings l := (allPerms rng).filter (isStdFilling l)`.
3. `a ∈ standardFillings l ↔ a.Perm rng ∧ isStdFilling l a` (`mem_standardFillings_iff`) — the
   members are exactly the permutations of `[1,…,n]` that are standard fillings of shape `l`.

**What remains (the second half — explicitly the bijection, not the HLF).**  The genuine SYT count
`dimSYT p = Nat.card (StandardYoungTableau (partitionShape p))` is a cardinality of the *structure*
type; closing `numSYTenum (toList p) = dimSYT p` needs a bijection

    StandardYoungTableau (partitionShape p)  ≃  { a // a ∈ standardFillings (toList p) }

(row-major flatten one way; reshape + the four `SemistandardYoungTableau` obligations the other).
This file reduces that target to a **pure finite bijection between two explicit sets** — no list /
`countP` plumbing left in it.  That bijection (`allPerms`-side now fully characterised) is the next
brick; it is *not* the Frame–Robinson–Thrall hook-length formula (`IdentityIHLFBridge.dimSYT_eq_dimHLF`,
the separate closed-form `#SYT(λ) = n!/∏h_c` — since proved via the GNW corner recursion,
`SYTHookGNW.numSYTenum_eq_dimHLF`, composed with this file's counting bridge).

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTEnum

/-- All ways to insert `x` into `l` are exactly Mathlib's `permutations'Aux` (definitionally, up to
the structural recursion). -/
theorem insertEverywhere_eq (x : ℕ) (l : List ℕ) :
    insertEverywhere x l = List.permutations'Aux x l := by
  induction l with
  | nil => rfl
  | cons a rest ih => simp [insertEverywhere, List.permutations'Aux, ih]

/-- The hand-rolled `allPerms` is exactly Mathlib's `List.permutations'`. -/
theorem allPerms_eq (l : List ℕ) : allPerms l = l.permutations' := by
  induction l with
  | nil => rfl
  | cons a rest ih =>
    simp only [allPerms, List.permutations', ih]
    congr 1
    funext y
    exact insertEverywhere_eq a y

/-- Membership in `allPerms l` is exactly being a permutation of `l`. -/
theorem mem_allPerms_iff_perm (a l : List ℕ) : a ∈ allPerms l ↔ a.Perm l := by
  rw [allPerms_eq]; exact List.mem_permutations'

/-- The flat fillings of shape `l`: permutations of `[1,…,∑l]` that pass `isStdFilling`. -/
def standardFillings (l : List ℕ) : List (List ℕ) :=
  (allPerms ((List.range l.sum).map (· + 1))).filter (isStdFilling l)

/-- `numSYTenum` is the length of the list of standard fillings. -/
theorem numSYTenum_eq_length_standardFillings (l : List ℕ) :
    numSYTenum l = (standardFillings l).length := by
  rw [numSYTenum, standardFillings, List.countP_eq_length_filter]

/-- A list is a standard filling of shape `l` iff it is a permutation of `[1,…,∑l]` that passes
`isStdFilling` — the clean characterisation the structural bijection will match against. -/
theorem mem_standardFillings_iff (l a : List ℕ) :
    a ∈ standardFillings l ↔
      (a.Perm ((List.range l.sum).map (· + 1)) ∧ isStdFilling l a = true) := by
  rw [standardFillings, List.mem_filter, mem_allPerms_iff_perm]

/-- **The Young diagram of a row-length list has exactly `∑l` cells** (a Mathlib gap: there is no
`card (cellsOfRowLens w) = w.sum` in the pinned toolchain).  Proved by induction on the recursive
`cellsOfRowLens`: each cons adds a fresh row `{0} ×ˢ range a` (card `a`) disjoint from the rest
(whose first coordinate is `Nat.succ _ ≥ 1`).  This is the cardinality `n` that the
`StandardYoungTableau.bijOn` field ranges over (`Set.Icc 1 μ.cells.card`), pinning it to `∑l` — the
load-bearing fact for the remaining `numSYTenum = dimSYT` bijection. -/
theorem card_cellsOfRowLens (w : List ℕ) :
    (YoungDiagram.cellsOfRowLens w).card = w.sum := by
  induction w with
  | nil => simp [YoungDiagram.cellsOfRowLens]
  | cons a ws ih =>
    rw [YoungDiagram.cellsOfRowLens, List.sum_cons]
    rw [Finset.card_union_of_disjoint, Finset.card_map, ih]
    · simp
    · rw [Finset.disjoint_left]
      rintro ⟨i, j⟩ h1 h2
      simp only [Finset.mem_product, Finset.mem_singleton, Finset.mem_range] at h1
      obtain ⟨rfl, -⟩ := h1
      rw [Finset.mem_map] at h2
      obtain ⟨⟨i', j'⟩, -, heq⟩ := h2
      simp [Function.Embedding.prodMap] at heq

/-- `#cells (ofRowLens w hw) = ∑w`. -/
theorem card_cells_ofRowLens (w : List ℕ) (hw : List.Sorted (· ≥ ·) w) :
    (YoungDiagram.ofRowLens w hw).cells.card = w.sum :=
  card_cellsOfRowLens w

end QOU.Mathlib.SYTEnum
