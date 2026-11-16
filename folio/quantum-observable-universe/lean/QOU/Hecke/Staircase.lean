import QOU.Hecke.Hoefsmit

/-!
# Staircase partitions and the canonical β_EW Δ_I^minimal word

This file specialises the abstract `HoefsmitRepresentation`
infrastructure of `QOU.Hecke.Hoefsmit` to the **staircase**
partitions `ρ k = (k, k-1, …, 1)`, and records the canonical
`β_EW Δ_I^minimal` braid word used by the Python pipeline
(`computations/staircase_ew_predictions.py`).

The pieces here are the Lean-side counterparts of the Python
helpers `beta_ew_word` and the staircase shape used by
`hoefsmit_build`.  The actual matrix construction is part of
the (still-research-grade) `HoefsmitRepresentation` instance and
is *not* duplicated here; this file only fixes the **inputs**
(partition + word) so a downstream theorem can talk about

  ```
  HoefsmitRepresentation.HasEigenvalueRatio
      (HoefsmitRepresentation.wordImage (betaEWWord n))
      (q ^ (1 / (2 * k - 1)))
  ```

without committing to a particular construction strategy.

## References

* Hoefsmit (1974), thesis, §III.
* `staircase_ew_predictions.py` — Python reference implementation
  of `beta_ew_word`.
* `docs/audits/2026-05-06-staircase-ew-residual-conjecture.md`.
-/

namespace QOU.Hecke

universe u

/-- The staircase shape `ρ k := (k, k-1, …, 1)` as a plain list.
Defined recursively for clarity.  `staircaseList 0 = []`,
`staircaseList 3 = [3, 2, 1]`. -/
def staircaseList : ℕ → List ℕ
  | 0     => []
  | k + 1 => (k + 1) :: staircaseList k

/-- Sum of the staircase: `1 + 2 + … + k = k(k+1)/2`.

Used to discharge `Partition.sum_eq` for `staircasePartition`. -/
theorem staircaseList_sum (k : ℕ) :
    (staircaseList k).sum = k * (k + 1) / 2 := by
  induction k with
  | zero       => simp [staircaseList]
  | succ k ih  =>
    simp only [staircaseList, List.sum_cons, ih]
    -- (k+1) + k(k+1)/2 = (k+1)(k+2)/2 ; omega can't do the nonlinear
    -- product, so fold (k+1) into the division and close the numerator
    -- equality with ring.
    rw [Nat.add_comm (k + 1), ← Nat.add_mul_div_left _ _ (by norm_num : 0 < 2)]
    congr 1
    ring

/-- Every part of the staircase is positive. -/
theorem staircaseList_positive (k : ℕ) :
    ∀ p ∈ staircaseList k, 0 < p := by
  induction k with
  | zero      => intro p hp; cases hp
  | succ k ih =>
    intro p hp
    rcases List.mem_cons.mp hp with h | h
    · subst h; exact Nat.succ_pos _
    · exact ih p h

/-- Membership in `staircaseList k`: every part is at most `k`. -/
theorem staircaseList_le (k : ℕ) :
    ∀ p ∈ staircaseList k, p ≤ k := by
  induction k with
  | zero      => intro p hp; cases hp
  | succ k ih =>
    intro p hp
    rcases List.mem_cons.mp hp with h | h
    · subst h; exact Nat.le_refl _
    · exact Nat.le_succ_of_le (ih p h)

/-- The staircase list is non-increasing. -/
theorem staircaseList_sorted (k : ℕ) :
    (staircaseList k).Sorted (· ≥ ·) := by
  induction k with
  | zero      => simp [staircaseList]
  | succ k ih =>
    rw [staircaseList, List.sorted_cons]
    refine ⟨?_, ih⟩
    intro p hp
    -- Every p ∈ staircaseList k is ≤ k ≤ k+1
    exact Nat.le_succ_of_le (staircaseList_le k p hp)

/-- The staircase partition `ρ k = (k, k-1, …, 1) ⊢ k(k+1)/2`. -/
def staircasePartition (k : ℕ) : Partition (k * (k + 1) / 2) where
  parts      := staircaseList k
  sum_eq     := staircaseList_sum k
  positive   := staircaseList_positive k
  decreasing := staircaseList_sorted k

/-- Sanity: `ρ 3 = (3, 2, 1)`. -/
example : (staircasePartition 3).parts = [3, 2, 1] := by
  decide

/-- Sanity: `n(ρ 3) = 6`. -/
example : (3 * (3 + 1)) / 2 = 6 := by decide

/-- Number of strands for the canonical β_EW operator on `ρ k`:
`n_k = k(k+1)/2`. -/
def staircaseStrands (k : ℕ) : ℕ := k * (k + 1) / 2

/-- The canonical "Δ_I^minimal" sub-word `[1, 3, 1]` shared by all
`β_EW` words on `n ≥ 4` strands.

Matches `staircase_ew_predictions.beta_ew_word`'s `delta_I` constant. -/
def deltaIMinimal {n : ℕ} (h₁ : 1 < n - 1) (h₃ : 3 < n - 1) :
    List (Generator n) :=
  [⟨⟨1, h₁⟩⟩, ⟨⟨3, h₃⟩⟩, ⟨⟨1, h₁⟩⟩]

/-- Concrete reproduction of one `β_EW` block: `[σ_k, σ_k, σ_k, σ_k, σ_1, σ_3, σ_1]`.

Requires `5 ≤ n` so that index `3` fits in `Fin (n - 1)` (the `Δ_I`
sub-word uses generator indices `1, 3`); the caller also passes a
proof that the block's anchor index `2j` is in range. -/
def betaEWBlock {n : ℕ} (h₅ : 5 ≤ n) (j : ℕ) (hk : 2 * j < n - 1) :
    List (Generator n) :=
  have h₁ : (1 : ℕ) < n - 1 := by omega
  have h₃ : (3 : ℕ) < n - 1 := by omega
  let g  : Generator n := ⟨⟨2 * j, hk⟩⟩
  let g₁ : Generator n := ⟨⟨1, h₁⟩⟩
  let g₃ : Generator n := ⟨⟨3, h₃⟩⟩
  [g, g, g, g, g₁, g₃, g₁]

/-- Internal helper: append `m` blocks counted **up** from index
`0` so that the final left-to-right order matches the Python
`for k in range(0, n_strands - 1, 2)` loop (smallest `j` first).

`accumulateBlocks 0` is `[]`; `accumulateBlocks (m + 1)` is
`accumulateBlocks m ++ block_m`.  Out-of-range anchors emit no
generators so the function is total. -/
private def accumulateBlocks {n : ℕ} (h₅ : 5 ≤ n) : ℕ → List (Generator n)
  | 0      => []
  | m + 1  =>
      let prev := accumulateBlocks h₅ m
      if hk : 2 * m < n - 1 then
        prev ++ betaEWBlock h₅ m hk
      else
        prev

/-- Concrete realisation of the canonical `β_EW Δ_I^minimal` word
on `n` strands.

The Python reference (verbatim from `staircase_ew_predictions.py`):

```python
def beta_ew_word(n_strands: int) -> list[int]:
    if n_strands < 4: return [0, 1, 0]
    delta_I = [1, 3, 1]
    word = []
    for k in range(0, n_strands - 1, 2):
        word.extend([k] * 4 + delta_I)
    return word
```

For `n ≥ 5` we emit the `[2j] * 4 ++ [1, 3, 1]` block for every
`j ∈ {0, 1, …, n/2 − 1}` whose anchor index `2j` fits in
`Fin (n − 1)`; the in-range check is discharged by `omega` per
block.  For `3 ≤ n < 5` we emit the Python fallback
`[σ₀, σ₁, σ₀]`.  For `n < 3` no generators exist and the word
is empty.

**Intentional deviation from the verbatim Python at `n = 4`.** The
Python reference applies the `< 4` fallback (so `n = 4` enters the
loop body), but the loop's `delta_I = [1, 3, 1]` writes index `3`,
which is out of bounds in `Fin (n − 1) = Fin 3` for `n = 4` and
would not type-check on the Lean side. We therefore extend the
fallback to `3 ≤ n < 5` so the construction stays well-typed. The
`n = 4` case is not part of the staircase conjecture's testable
regime (`staircaseStrands k = k(k+1)/2 ∈ {3, 6, 10, 15, …}`), so
this deviation does not weaken any downstream theorem.

Replaces the previous `opaque` declaration so downstream
`wordImage` calls see a concrete list rather than an unevaluable
black box. -/
def betaEWWord (n : ℕ) : List (Generator n) :=
  if h₅ : 5 ≤ n then
    accumulateBlocks h₅ (n / 2)
  else if h₃ : 3 ≤ n then
    have h₀ : (0 : ℕ) < n - 1 := by omega
    have h₁ : (1 : ℕ) < n - 1 := by omega
    [⟨⟨0, h₀⟩⟩, ⟨⟨1, h₁⟩⟩, ⟨⟨0, h₀⟩⟩]
  else []

/-- Sanity: at `n = 6` (i.e. `staircaseStrands 3`) the word has length
`3 · 7 = 21` (three full blocks `j = 0, 1, 2`). -/
example : (betaEWWord 6).length = 21 := by decide

/-- Sanity: at `n = 10` (i.e. `staircaseStrands 4`) the word has length
`5 · 7 = 35` (five full blocks). -/
example : (betaEWWord 10).length = 35 := by decide

/-- Sanity: the fallback at `n = 3` is `[σ₀, σ₁, σ₀]` (length 3). -/
example : (betaEWWord 3).length = 3 := by decide

/-! ### Row count and Temperley–Lieb kernel threshold (`qou-4qno`) -/

/-- The staircase list `staircaseList k = [k, k-1, …, 1]` has length `k`. -/
theorem staircaseList_length (k : ℕ) :
    (staircaseList k).length = k := by
  induction k with
  | zero => simp [staircaseList]
  | succ k ih =>
    simp only [staircaseList, List.length_cons, ih]

/-- The staircase partition `ρ_k = (k, k-1, …, 1)` has `k` rows. -/
theorem staircasePartition_rows (k : ℕ) :
    (staircasePartition k).parts.length = k := by
  have h : (staircasePartition k).parts = staircaseList k := rfl
  rw [h]
  exact staircaseList_length k

/-- Under the `SU(2)_q` / Temperley–Lieb row cap (`N = 2`), `ρ_k` exceeds two rows
(and hence lies in the kernel of `H_{n_k}(q) → TL_{n_k}(q)`) if and only if `3 ≤ k`. -/
theorem staircase_in_tl_kernel_iff_three_le (k : ℕ) :
    2 < (staircasePartition k).parts.length ↔ 3 ≤ k := by
  rw [staircasePartition_rows]
  omega

/-- `ρ_k` satisfies the `N = 2` Schur–Weyl row bound `ℓ(ρ_k) ≤ 2` if and only if `k ≤ 2`. -/
theorem staircase_physical_at_su2_iff_le_two (k : ℕ) :
    (staircasePartition k).parts.length ≤ 2 ↔ k ≤ 2 := by
  rw [staircasePartition_rows]
  omega

/-- Among the staircase cases `k ≥ 2`, `k = 2` (`ρ₂ = (2,1)` on `3` strands) is the
unique case within the `N = 2` row bound (`qou-4qno`). -/
theorem staircase_unique_physical_ge_two (k : ℕ) (hk : 2 ≤ k) :
    (staircasePartition k).parts.length ≤ 2 ↔ k = 2 := by
  rw [staircase_physical_at_su2_iff_le_two]
  omega

/-- Explicit strand counts and row-cap classifications at `k = 2, 3, 4`:
`n₂ = 3` (`2` rows, physical at `N = 2`), `n₃ = 6` (`3 > 2` rows, in TL kernel),
and `n₄ = 10` (`4 > 2` rows, in TL kernel). -/
theorem staircaseStrands_small_values :
    staircaseStrands 2 = 3 ∧
      staircaseStrands 3 = 6 ∧
      staircaseStrands 4 = 10 ∧
      (staircasePartition 2).parts.length = 2 ∧
      2 < (staircasePartition 3).parts.length ∧
      2 < (staircasePartition 4).parts.length := by
  rw [staircasePartition_rows, staircasePartition_rows, staircasePartition_rows]
  unfold staircaseStrands
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · omega
  · omega
  · omega
  · omega
  · omega
  · omega

end QOU.Hecke
