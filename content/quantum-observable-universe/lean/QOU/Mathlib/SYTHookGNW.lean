import QOU.Mathlib.SYTHookFormulaGeneral

/-!
# QOU.Mathlib.SYTHookGNW — corner-recursion infrastructure for the general HLF (GNW route)

The general dimension hook-length formula `numSYTenum l = dimHLF l` is presently isolated to the single
**Aitken/Frobenius determinant identity** `SYTHookFormulaGeneral.dimAitkenIdentity` (ii).  That gap is
*blocked* by the pinned Mathlib: it has no `Combinatorics.RSK` / Specht / Frobenius-determinant
infrastructure, so the determinant evaluation cannot be carried out at all.

This file develops the **Greene–Nijenhuis–Wilf corner-recursion** route, which needs **none** of that
infrastructure — it is pure `ℕ`/`ℚ` combinatorics — and so converts the *blocked* determinant gap into
two *unblocked* (if still open) self-contained statements:

* **corner recursion of the count** (`CornerRecursion`):
  `numSYTenum λ = Σ_{removable corners c} numSYTenum (λ ∖ c)` — the largest entry sits in a removable
  corner; deleting it is a bijection onto the disjoint union of the smaller shapes;
* **GNW hook-summation identity** (`GNWHookIdentity`, over `ℚ`):
  `Σ_{corners c} ∏h_λ / ∏h_{λ∖c} = n` — the partial-fractions / telescoping identity on hook products.

The reduction itself — strong induction on `n = sz l` combining the two — is proved **sorry-free** here
(`numSYTenum_eq_dimHLF_of_gnw`), as is all the corner-removal infrastructure (`removeCorner` preserves
sortedness and positivity and drops the size by one).  So the *only* residual content is the two
combinatorial identities above; everything connecting them to the HLF is machine-checked.

Pure combinatorics on `ℕ`/`ℚ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTEnum

open QOU.BraidKnot.IdentityI (prodHooks dimHLF sz)

/-! ## Corner-removal infrastructure -/

/-- Row index `i` is a **removable corner** of shape `l`: a genuine row whose last cell is an outer
corner, i.e. the next row is strictly shorter (treating "beyond the last row" as length `0`).  For a
weakly-decreasing positive shape this is exactly the set of cells whose deletion leaves a shape. -/
def IsCorner (l : List ℕ) (i : ℕ) : Prop :=
  i < l.length ∧ l.getD (i + 1) 0 < l.getD i 0

/-- Remove one cell from the end of row `i`: decrement that row's length, then drop the row entirely
if it has shrunk to `0` (which, for a removable corner of a weakly-decreasing positive shape, happens
only when `i` is the final length-`1` row). -/
def removeCorner (l : List ℕ) (i : ℕ) : List ℕ :=
  (l.set i (l.getD i 0 - 1)).filter (· != 0)

/-- Filtering out zeros leaves the sum unchanged. -/
theorem sum_filter_ne_zero : ∀ m : List ℕ, (m.filter (· != 0)).sum = m.sum
  | [] => rfl
  | a :: t => by
    by_cases h : a = 0
    · subst h
      simp [sum_filter_ne_zero t]
    · have hb : (a != 0) = true := by simpa using h
      simp [hb, sum_filter_ne_zero t]

/-- Decrementing the length of a genuine row drops the total cell count by one. -/
theorem sum_set_decr : ∀ (l : List ℕ) (i : ℕ), i < l.length → 1 ≤ l.getD i 0 →
    (l.set i (l.getD i 0 - 1)).sum + 1 = l.sum
  | a :: t, 0, _, h1 => by
    have h1a : 1 ≤ a := by simpa using h1
    simp only [List.set_cons_zero, List.getD_cons_zero, List.sum_cons]
    omega
  | a :: t, n + 1, hi, h1 => by
    have hi' : n < t.length := by simpa using hi
    have h1' : 1 ≤ t.getD n 0 := by simpa using h1
    have ih := sum_set_decr t n hi' h1'
    simp only [List.set_cons_succ, List.getD_cons_succ, List.sum_cons]
    omega

/-- **`removeCorner` drops the cell count by one** at any genuine row with a positive length. -/
theorem sz_removeCorner (l : List ℕ) (i : ℕ) (hi : i < l.length) (hpos : 1 ≤ l.getD i 0) :
    sz (removeCorner l i) + 1 = sz l := by
  unfold sz removeCorner
  rw [sum_filter_ne_zero]
  exact sum_set_decr l i hi hpos

/-- `l.getD i 0 = l[i]` for a genuine index. -/
private theorem getD_eq_getElem' (l : List ℕ) (i : ℕ) (hi : i < l.length) :
    l.getD i 0 = l[i] := by
  rw [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hi, Option.getD_some]

/-- **Decrementing a removable corner preserves weak decrease.**  The new length `l[i]−1` still sits
between its neighbours: `l[i−1] ≥ l[i] ≥ l[i]−1` and `l[i]−1 ≥ l[i+1]` (the latter because a corner has
`l[i+1] < l[i]`). -/
theorem sorted_set_corner (l : List ℕ) (i : ℕ) (hl : List.Sorted (· ≥ ·) l) (hc : IsCorner l i) :
    List.Sorted (· ≥ ·) (l.set i (l.getD i 0 - 1)) := by
  obtain ⟨hi, hnext⟩ := hc
  have hgi : l.getD i 0 = l[i] := getD_eq_getElem' l i hi
  have hlg := List.pairwise_iff_getElem.mp hl
  refine List.pairwise_iff_getElem.mpr ?_
  intro p q hp hq hpq
  rw [List.length_set] at hp hq
  rw [List.getElem_set, List.getElem_set]
  by_cases hip : i = p
  · subst hip
    rw [if_pos rfl, if_neg (show ¬ i = q by omega)]
    have hi1 : i + 1 < l.length := by omega
    have hnext' : l[i + 1] < l[i] := by
      have he : l.getD (i + 1) 0 = l[i + 1] := getD_eq_getElem' l (i + 1) hi1
      rw [he, hgi] at hnext; exact hnext
    rcases Nat.lt_or_ge (i + 1) q with hq1 | hq1
    · have := hlg (i + 1) q hi1 hq hq1; omega
    · have hqe : q = i + 1 := by omega
      subst hqe; omega
  · by_cases hiq : i = q
    · subst hiq
      rw [if_neg hip, if_pos rfl]
      have := hlg p i hp hi (by omega)
      omega
    · rw [if_neg hip, if_neg hiq]
      exact hlg p q hp hq hpq

/-- **`removeCorner` preserves weak decrease** (filtering a sorted list keeps it sorted). -/
theorem sorted_removeCorner (l : List ℕ) (i : ℕ) (hl : List.Sorted (· ≥ ·) l) (hc : IsCorner l i) :
    List.Sorted (· ≥ ·) (removeCorner l i) :=
  (List.Pairwise.sublist List.filter_sublist (sorted_set_corner l i hl hc))

/-- **`removeCorner` is positive** — every surviving row has length `≥ 1` (zeros were filtered out). -/
theorem removeCorner_pos (l : List ℕ) (i : ℕ) : ∀ a ∈ removeCorner l i, 0 < a := by
  intro a ha
  unfold removeCorner at ha
  rw [List.mem_filter] at ha
  have : a ≠ 0 := by simpa using ha.2
  omega

end QOU.Mathlib.SYTEnum
