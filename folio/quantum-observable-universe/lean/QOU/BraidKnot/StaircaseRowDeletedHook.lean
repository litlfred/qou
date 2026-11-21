import QOU.BraidKnot.StaircaseHookMultiset

/-!
# The staircase with corners on its top rows: its hooks are two staircases and an even rectangle

Bean `qou-fxym` (the bounded-excess LOWER bound, `e_n = M_n − A√(2n) ≥ −K₃`).  For
`n = T_k + r`, `0 ≤ r ≤ k`, the lower bound uses the shape

    λ_{k,r} = δ_k with one outer corner on each of its top r rows
            = (k+1, k, …, k−r+2, k−r, k−r−1, …, 1)
            = δ_{k+1} with row r+1 deleted,

presented here as the sublevel set `{(i, j) : i + j < k ∨ (i < r ∧ i + j = k)}`.  Writing
`m = k − r`, its hook lengths split into three blocks:

| block | cells | hook |
|---|---|---|
| a copy of `δ_m` | `r ≤ i` | `2(k − i − j) − 1` |
| a copy of `δ_r` | `i < r`, `m < j` | `2(k − i − j) + 1` |
| an `r × (m+1)` rectangle | `i < r`, `j ≤ m` | `2(k − i − j)` (even) |

so (`rowDeleted_hookSum`), for any `g` into an additive commutative monoid,

    Σ_{c ∈ λ_{k,r}} g(h(c)) = Σ_{c ∈ δ_m} g(h(c)) + Σ_{c ∈ δ_r} g(h(c)) + Σ_{i<r} Σ_{j≤m} g(2(k−i−j)).

## Why this is the lower bound

At `g = ε` (positive), the rectangle is `≥ 0`, so `Σ ε(h(λ_{k,r})) ≥ Σ ε(h(δ_m)) + Σ ε(h(δ_r))`,
and the staircase closed form `A j − B + rem_j` (`staircase_hookSum`) gives `A k − 2B`.  Adding
the `r` corners one at a time loses `2(A − E₂) − ε(1) = 0.4012` each; placing them on the TOP rows
is what makes the loss vanish — the corners' shifted cells re-form a second staircase.  The
`ε`-valued assembly is in `computations/deltalambda/rev_bounded_excess_lower_bound_probe.py`
(past the archimedean wall); this file is the combinatorial step.

## Base ring (§7c)

No ring: hooks are `ℕ`, and the identity is stated for an arbitrary `AddCommMonoid` target.

-- Ref: [leitner2026] computations/deltalambda/rev_bounded_excess_lower_bound_probe.py
-/

namespace QOU.BraidKnot.HookSum

open Finset

/-- `λ_{k,r}`: the staircase `δ_k` with one outer corner on each of its top `r` rows. -/
def rowDeletedYD (k r : ℕ) : YoungDiagram where
  cells := (range (k + 1) ×ˢ range (k + 1)).filter
    (fun c => c.1 + c.2 < k ∨ (c.1 < r ∧ c.1 + c.2 = k))
  isLowerSet := by
    rintro ⟨a, b⟩ ⟨a', b'⟩ hle hmem
    have h₁ : a' ≤ a := hle.1
    have h₂ : b' ≤ b := hle.2
    simp only [Finset.mem_coe, mem_filter, Finset.mem_product, mem_range] at hmem ⊢
    refine ⟨⟨by omega, by omega⟩, ?_⟩
    rcases hmem.2 with h | ⟨h, h'⟩
    · left; omega
    · by_cases hc : a' + b' < k
      · left; exact hc
      · right; omega

@[simp] theorem mem_rowDeletedYD (k r i j : ℕ) :
    (i, j) ∈ rowDeletedYD k r ↔ (i + j < k ∨ (i < r ∧ i + j = k)) := by
  change (i, j) ∈ (rowDeletedYD k r).cells ↔ _
  simp only [rowDeletedYD, mem_filter, Finset.mem_product, mem_range]
  omega

theorem rowDeletedYD_rowLen_lt (k r i : ℕ) (hi : i < r) (hr : r ≤ k) :
    (rowDeletedYD k r).rowLen i = k + 1 - i := by
  have h : ∀ j, j < (rowDeletedYD k r).rowLen i ↔ j < k + 1 - i := by
    intro j
    rw [← YoungDiagram.mem_iff_lt_rowLen, mem_rowDeletedYD]
    omega
  have h₁ := h ((rowDeletedYD k r).rowLen i)
  have h₂ := h (k + 1 - i)
  omega

theorem rowDeletedYD_rowLen_ge (k r i : ℕ) (hi : r ≤ i) :
    (rowDeletedYD k r).rowLen i = k - i := by
  have h : ∀ j, j < (rowDeletedYD k r).rowLen i ↔ j < k - i := by
    intro j
    rw [← YoungDiagram.mem_iff_lt_rowLen, mem_rowDeletedYD]
    omega
  have h₁ := h ((rowDeletedYD k r).rowLen i)
  have h₂ := h (k - i)
  omega

theorem rowDeletedYD_colLen_gt (k r j : ℕ) (hj : k - r < j) (hr : r ≤ k) :
    (rowDeletedYD k r).colLen j = k + 1 - j := by
  have h : ∀ i, i < (rowDeletedYD k r).colLen j ↔ i < k + 1 - j := by
    intro i
    rw [← YoungDiagram.mem_iff_lt_colLen, mem_rowDeletedYD]
    omega
  have h₁ := h ((rowDeletedYD k r).colLen j)
  have h₂ := h (k + 1 - j)
  omega

theorem rowDeletedYD_colLen_le (k r j : ℕ) (hj : j ≤ k - r) (hr : r ≤ k) :
    (rowDeletedYD k r).colLen j = k - j := by
  have h : ∀ i, i < (rowDeletedYD k r).colLen j ↔ i < k - j := by
    intro i
    rw [← YoungDiagram.mem_iff_lt_colLen, mem_rowDeletedYD]
    omega
  have h₁ := h ((rowDeletedYD k r).colLen j)
  have h₂ := h (k - j)
  omega

/-- Hooks in the lower block (`r ≤ i`): a copy of `δ_{k−r}`. -/
theorem rowDeleted_hook_low (k r i j : ℕ) (hr : r ≤ k) (hi : r ≤ i) (h : i + j < k) :
    QOU.QBeta.WenzlWeight.hook (rowDeletedYD k r) (i, j) = 2 * (k - i - j) - 1 := by
  simp only [QOU.QBeta.WenzlWeight.hook, rowDeletedYD_rowLen_ge k r i hi,
    rowDeletedYD_colLen_le k r j (by omega) hr]
  omega

/-- Hooks in the upper-right block (`i < r`, `k − r < j`): a copy of `δ_r`. -/
theorem rowDeleted_hook_corner (k r i j : ℕ) (hr : r ≤ k) (hi : i < r) (hj : k - r < j)
    (h : i + j ≤ k) :
    QOU.QBeta.WenzlWeight.hook (rowDeletedYD k r) (i, j) = 2 * (k - i - j) + 1 := by
  simp only [QOU.QBeta.WenzlWeight.hook, rowDeletedYD_rowLen_lt k r i hi hr,
    rowDeletedYD_colLen_gt k r j hj hr]
  omega

/-- Hooks in the rectangle (`i < r`, `j ≤ k − r`): EVEN, `2(k − i − j)`. -/
theorem rowDeleted_hook_rect (k r i j : ℕ) (hr : r ≤ k) (hi : i < r) (hj : j ≤ k - r) :
    QOU.QBeta.WenzlWeight.hook (rowDeletedYD k r) (i, j) = 2 * (k - i - j) := by
  simp only [QOU.QBeta.WenzlWeight.hook, rowDeletedYD_rowLen_lt k r i hi hr,
    rowDeletedYD_colLen_le k r j hj hr]
  omega

/-- **The hook sum of `λ_{k,r}`**: two staircases and an even rectangle. -/
theorem rowDeleted_hookSum {N : Type*} [AddCommMonoid N] (g : ℕ → N) (k r : ℕ) (hr : r ≤ k) :
    ∑ c ∈ (rowDeletedYD k r).cells, g (QOU.QBeta.WenzlWeight.hook (rowDeletedYD k r) c)
      = ∑ c ∈ (staircaseYD (k - r)).cells, g (QOU.QBeta.WenzlWeight.hook (staircaseYD (k - r)) c)
        + ∑ c ∈ (staircaseYD r).cells, g (QOU.QBeta.WenzlWeight.hook (staircaseYD r) c)
        + ∑ i ∈ range r, ∑ j ∈ range (k - r + 1), g (2 * (k - i - j)) := by
  set f : ℕ × ℕ → N := fun c => g (QOU.QBeta.WenzlWeight.hook (rowDeletedYD k r) c) with hf
  set S := (rowDeletedYD k r).cells with hS
  have hmem : ∀ c : ℕ × ℕ, c ∈ S ↔ (c.1 + c.2 < k ∨ (c.1 < r ∧ c.1 + c.2 = k)) := by
    intro c
    rw [hS, YoungDiagram.mem_cells]
    exact mem_rowDeletedYD k r c.1 c.2
  -- split off the lower block, then the rectangle from the corner block
  rw [← Finset.sum_filter_add_sum_filter_not S (fun c => r ≤ c.1),
    ← Finset.sum_filter_add_sum_filter_not (S.filter fun c => ¬ r ≤ c.1) (fun c => k - r < c.2)]
  -- lower block ↔ δ_{k−r}
  have hlow : ∑ c ∈ S.filter (fun c => r ≤ c.1), f c
      = ∑ c ∈ (staircaseYD (k - r)).cells,
          g (QOU.QBeta.WenzlWeight.hook (staircaseYD (k - r)) c) := by
    refine Finset.sum_nbij' (fun c => (c.1 - r, c.2)) (fun c => (c.1 + r, c.2)) ?_ ?_ ?_ ?_ ?_
    · rintro ⟨a, b⟩ hc
      simp only [mem_filter, hmem] at hc
      simp only [YoungDiagram.mem_cells, mem_staircaseYD]
      omega
    · rintro ⟨a, b⟩ hc
      simp only [YoungDiagram.mem_cells, mem_staircaseYD] at hc
      simp only [mem_filter, hmem]
      omega
    · rintro ⟨a, b⟩ hc
      simp only [mem_filter] at hc
      have hra : r ≤ a := hc.2
      simp [Nat.sub_add_cancel hra]
    · rintro ⟨a, b⟩ _
      simp
    · intro c hc
      simp only [mem_filter, hmem] at hc
      have hlt : c.1 + c.2 < k := by omega
      have h1 := rowDeleted_hook_low k r c.1 c.2 hr hc.2 hlt
      have h2 := staircase_hook (k - r) (c.1 - r) c.2 (by omega)
      simp only [hf, Prod.mk.eta] at h1 ⊢
      rw [h1, h2]
      congr 1
      omega
  -- corner block ↔ δ_r
  have hcorner : ∑ c ∈ (S.filter fun c => ¬ r ≤ c.1).filter (fun c => k - r < c.2), f c
      = ∑ c ∈ (staircaseYD r).cells, g (QOU.QBeta.WenzlWeight.hook (staircaseYD r) c) := by
    refine Finset.sum_nbij' (fun c => (c.1, c.2 - (k - r + 1))) (fun c => (c.1, c.2 + (k - r + 1)))
      ?_ ?_ ?_ ?_ ?_
    · rintro ⟨a, b⟩ hc
      simp only [mem_filter, hmem] at hc
      simp only [YoungDiagram.mem_cells, mem_staircaseYD]
      omega
    · rintro ⟨a, b⟩ hc
      simp only [YoungDiagram.mem_cells, mem_staircaseYD] at hc
      simp only [mem_filter, hmem]
      omega
    · rintro ⟨a, b⟩ hc
      simp only [mem_filter] at hc
      have hb : k - r + 1 ≤ b := by have := hc.2; omega
      simp [Nat.sub_add_cancel hb]
    · rintro ⟨a, b⟩ _
      simp
    · intro c hc
      simp only [mem_filter, hmem] at hc
      have h1 := rowDeleted_hook_corner k r c.1 c.2 hr (by omega) hc.2 (by omega)
      have h2 := staircase_hook r c.1 (c.2 - (k - r + 1)) (by omega)
      simp only [hf, Prod.mk.eta] at h1 ⊢
      rw [h1, h2]
      congr 1
      omega
  -- rectangle
  have hrect : ∑ c ∈ (S.filter fun c => ¬ r ≤ c.1).filter (fun c => ¬ k - r < c.2), f c
      = ∑ i ∈ range r, ∑ j ∈ range (k - r + 1), g (2 * (k - i - j)) := by
    have hset : (S.filter fun c => ¬ r ≤ c.1).filter (fun c => ¬ k - r < c.2)
        = range r ×ˢ range (k - r + 1) := by
      ext c
      simp only [mem_filter, hmem, Finset.mem_product, mem_range]
      omega
    rw [hset, Finset.sum_product]
    refine Finset.sum_congr rfl fun i hi => Finset.sum_congr rfl fun j hj => ?_
    rw [mem_range] at hi hj
    simp only [hf]
    rw [rowDeleted_hook_rect k r i j hr hi (by omega)]
  rw [hlow, hcorner, hrect, add_assoc]

/-- At `r = 0` the shape is the staircase itself. -/
theorem rowDeletedYD_zero (k : ℕ) : rowDeletedYD k 0 = staircaseYD k := by
  ext ⟨i, j⟩
  simp only [YoungDiagram.mem_cells, mem_rowDeletedYD, mem_staircaseYD]
  omega

/-- With a nonnegative `g`, the row-deleted shape's hook sum dominates the two staircase sums: the
rectangle term is dropped.  This is the step `Σ ε(h) ≥ S_δ(k−r) + S_δ(r)` of the lower bound.
Ported from #7802 (`cornerBlock_hookSum_ge`, an independent derivation of the same bound). -/
theorem rowDeleted_hookSum_ge {N : Type*} [AddCommMonoid N] [PartialOrder N]
    [IsOrderedAddMonoid N] (g : ℕ → N) (hg : ∀ m, 0 ≤ g m) (k r : ℕ) (hr : r ≤ k) :
    ∑ c ∈ (staircaseYD (k - r)).cells, g (QOU.QBeta.WenzlWeight.hook (staircaseYD (k - r)) c)
        + ∑ c ∈ (staircaseYD r).cells, g (QOU.QBeta.WenzlWeight.hook (staircaseYD r) c)
      ≤ ∑ c ∈ (rowDeletedYD k r).cells, g (QOU.QBeta.WenzlWeight.hook (rowDeletedYD k r) c) := by
  rw [rowDeleted_hookSum g k r hr]
  exact le_add_of_nonneg_right (Finset.sum_nonneg fun i _ => Finset.sum_nonneg fun j _ => hg _)

/-- The row-deleted shape has `T_{k−r} + T_r + r(k−r+1)` cells, i.e. `n = T_k + r`: the
hook-sum decomposition at `g ≡ 1`.  Ported from #7802 (`cornerBlockYD_card`). -/
theorem rowDeletedYD_card (k r : ℕ) (hr : r ≤ k) :
    (rowDeletedYD k r).cells.card
      = (staircaseYD (k - r)).cells.card + (staircaseYD r).cells.card + r * (k - r + 1) := by
  have h := rowDeleted_hookSum (N := ℕ) (fun _ => 1) k r hr
  simp only [Finset.sum_const, smul_eq_mul, mul_one, card_range] at h
  exact h

end QOU.BraidKnot.HookSum
