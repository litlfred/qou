import QOU.BraidKnot.StaircaseHookMultiset

/-!
# The staircase plus a top corner block: its hooks split into two staircases and a rectangle

The `REV_n` arc (bean `qou-fxym`) needs a lower bound on `M_n` at NON-triangular
`n = T_k + r`, `1 ≤ r ≤ k`.  The family used is the staircase `δ_k` with its `r` **top** outer
corners added — row lengths `k+1, k, …, k+2−r, k−r, …, 1`.  With `a := r`, `c := k − r`
(0-indexed cells) it is

    μ(a, c) = {(i, j) : i + j < a + c  ∨  (i + j = a + c ∧ i < a)} ,

and its hook lengths fall into three blocks:

    i < a, j ≤ c :  h = 2(a + c − i − j)        (twice the hooks of an `a × (c+1)` rectangle)
    i < a, c < j :  h = 2(a + c − i − j) + 1    (the staircase `δ_a`)
    a ≤ i, j ≤ c :  h = 2(a + c − i − j) − 1    (the staircase `δ_c`)

so `hooks μ(a,c) = hooks δ_a + hooks δ_c + 2·hooks(a × (c+1))` (`cornerBlock_hookSum`).  That is
the whole reason the top corner block costs `O(1)` against `δ_k` rather than `O(r)`: every hook
that turned even sits in ONE rectangle, whose `ε(2h)`-sum is a convergent positive series.

| | |
|---|---|
| `mem_cornerBlockYD` | the membership predicate |
| `cornerBlockYD_rowLen` / `_colLen` | `a + c + [i < a] − i` / `a + c + [c < j] − j` |
| `cornerBlock_hook_rect` / `_stairA` / `_stairC` | the three per-region hook formulas |
| `cornerBlock_hookSum` | the hook-sum decomposition, any `g` into an `AddCommMonoid` |
| `cornerBlock_hookSum_ge` | `g ≥ 0` ⇒ the sum dominates the two staircase sums |

## Base ring (§7c)

None: hooks are `ℕ`, sums land in an arbitrary `AddCommMonoid` (ordered for the corollary).
The `ε`-valued specialisation, `A k − 2B − C ≤ Ψ(μ)`, lives downstream in
`computations/deltalambda/rev_lower_bound_probe.py`.

-- Ref: [manuscript] computations/deltalambda/rev_lower_bound_probe.py
-/

namespace QOU.BraidKnot.HookSum

open Finset

/-- `μ(a, c)`: the staircase `δ_{a+c}` with its top `a` outer corners added. -/
def cornerBlockYD (a c : ℕ) : YoungDiagram where
  cells := (range (a + c + 1) ×ˢ range (a + c + 1)).filter
    (fun x => x.1 + x.2 < a + c ∨ (x.1 + x.2 = a + c ∧ x.1 < a))
  isLowerSet := by
    rintro ⟨i, j⟩ ⟨i', j'⟩ hle hmem
    have h₁ : i' ≤ i := hle.1
    have h₂ : j' ≤ j := hle.2
    simp only [Finset.mem_coe, mem_filter, Finset.mem_product, mem_range] at hmem ⊢
    omega

@[simp] theorem mem_cornerBlockYD (a c i j : ℕ) :
    (i, j) ∈ cornerBlockYD a c ↔ (i + j < a + c ∨ (i + j = a + c ∧ i < a)) := by
  change (i, j) ∈ (cornerBlockYD a c).cells ↔ _
  simp only [cornerBlockYD, mem_filter, Finset.mem_product, mem_range]
  omega

theorem cornerBlockYD_rowLen (a c i : ℕ) :
    (cornerBlockYD a c).rowLen i = a + c + (if i < a then 1 else 0) - i := by
  have h : ∀ j, j < (cornerBlockYD a c).rowLen i ↔ j < a + c + (if i < a then 1 else 0) - i := by
    intro j
    rw [← YoungDiagram.mem_iff_lt_rowLen, mem_cornerBlockYD]
    split_ifs <;> omega
  have h₁ := h ((cornerBlockYD a c).rowLen i)
  have h₂ := h (a + c + (if i < a then 1 else 0) - i)
  omega

theorem cornerBlockYD_colLen (a c j : ℕ) :
    (cornerBlockYD a c).colLen j = a + c + (if c < j then 1 else 0) - j := by
  have h : ∀ i, i < (cornerBlockYD a c).colLen j ↔ i < a + c + (if c < j then 1 else 0) - j := by
    intro i
    rw [← YoungDiagram.mem_iff_lt_colLen, mem_cornerBlockYD]
    split_ifs <;> omega
  have h₁ := h ((cornerBlockYD a c).colLen j)
  have h₂ := h (a + c + (if c < j then 1 else 0) - j)
  omega

/-- Rectangle block: `i < a`, `j ≤ c` gives `h = 2(a + c − i − j)` (even). -/
theorem cornerBlock_hook_rect (a c i j : ℕ) (hi : i < a) (hj : j ≤ c) :
    QOU.QBeta.WenzlWeight.hook (cornerBlockYD a c) (i, j) = 2 * (a + c - i - j) := by
  simp only [QOU.QBeta.WenzlWeight.hook, cornerBlockYD_rowLen, cornerBlockYD_colLen]
  have : ¬ c < j := by omega
  simp only [hi, this, if_true, if_false]
  omega

/-- `δ_a` block: `i < a`, `c < j`, on a cell, gives `h = 2(a + c − i − j) + 1`. -/
theorem cornerBlock_hook_stairA (a c i j : ℕ) (hi : i < a) (hj : c < j) (hc : i + j ≤ a + c) :
    QOU.QBeta.WenzlWeight.hook (cornerBlockYD a c) (i, j) = 2 * (a + c - i - j) + 1 := by
  simp only [QOU.QBeta.WenzlWeight.hook, cornerBlockYD_rowLen, cornerBlockYD_colLen]
  simp only [hi, hj, if_true]
  omega

/-- `δ_c` block: `a ≤ i`, `j ≤ c`, on a cell, gives `h = 2(a + c − i − j) − 1`. -/
theorem cornerBlock_hook_stairC (a c i j : ℕ) (hi : a ≤ i) (hj : j ≤ c) (hc : i + j < a + c) :
    QOU.QBeta.WenzlWeight.hook (cornerBlockYD a c) (i, j) = 2 * (a + c - i - j) - 1 := by
  simp only [QOU.QBeta.WenzlWeight.hook, cornerBlockYD_rowLen, cornerBlockYD_colLen]
  have h1 : ¬ i < a := by omega
  have h2 : ¬ c < j := by omega
  simp only [h1, h2, if_false]
  omega

-- `all_goals simp only` uses each lemma on only some of the five goals.
set_option linter.unusedSimpArgs false in
/-- **Hook-sum decomposition of the corner block.**  For any `g` into an additive commutative
monoid,

    Σ_{x ∈ μ(a,c)} g(h(x)) = Σ_{x ∈ δ_a} g(h(x)) + Σ_{x ∈ δ_c} g(h(x))
                             + Σ_{(i,j) ∈ [0,a) × [0,c]} g(2(i + j + 1)) . -/
theorem cornerBlock_hookSum {N : Type*} [AddCommMonoid N] (g : ℕ → N) (a c : ℕ) :
    ∑ x ∈ (cornerBlockYD a c).cells, g (QOU.QBeta.WenzlWeight.hook (cornerBlockYD a c) x)
      = ∑ x ∈ (staircaseYD a).cells, g (QOU.QBeta.WenzlWeight.hook (staircaseYD a) x)
        + ∑ x ∈ (staircaseYD c).cells, g (QOU.QBeta.WenzlWeight.hook (staircaseYD c) x)
        + ∑ x ∈ range a ×ˢ range (c + 1), g (2 * (x.1 + x.2 + 1)) := by
  set μ := cornerBlockYD a c with hμ
  have hcell : ∀ x : ℕ × ℕ, x ∈ μ.cells ↔ (x.1 + x.2 < a + c ∨ (x.1 + x.2 = a + c ∧ x.1 < a)) := by
    rintro ⟨i, j⟩
    rw [YoungDiagram.mem_cells, hμ, mem_cornerBlockYD]
  have hst : ∀ m : ℕ, ∀ x : ℕ × ℕ, x ∈ (staircaseYD m).cells ↔ x.1 + x.2 < m := by
    intro m x
    rw [YoungDiagram.mem_cells]
    exact mem_staircaseYD m x.1 x.2
  -- split off the `a ≤ i` block, then the rectangle from the `δ_a` block
  rw [← Finset.sum_filter_add_sum_filter_not μ.cells (fun x => x.1 < a),
      ← Finset.sum_filter_add_sum_filter_not (μ.cells.filter (fun x => x.1 < a))
        (fun x => x.2 ≤ c)]
  -- rectangle block
  have hrect : ∑ x ∈ (μ.cells.filter (fun x => x.1 < a)).filter (fun x => x.2 ≤ c),
        g (QOU.QBeta.WenzlWeight.hook μ x)
      = ∑ x ∈ range a ×ˢ range (c + 1), g (2 * (x.1 + x.2 + 1)) := by
    refine Finset.sum_nbij' (fun x => (a - 1 - x.1, c - x.2)) (fun y => (a - 1 - y.1, c - y.2))
      ?_ ?_ ?_ ?_ ?_
    all_goals rintro ⟨i, j⟩ hx
    all_goals dsimp only at hx ⊢
    all_goals simp only [mem_filter, hcell, Finset.mem_product, mem_range,
      Prod.mk.injEq, true_and, and_true] at hx ⊢
    · omega
    · omega
    · omega
    · omega
    · rw [hμ, cornerBlock_hook_rect a c i j hx.1.2 hx.2]
      congr 1
      omega
  -- δ_a block
  have hA : ∑ x ∈ (μ.cells.filter (fun x => x.1 < a)).filter (fun x => ¬ x.2 ≤ c),
        g (QOU.QBeta.WenzlWeight.hook μ x)
      = ∑ x ∈ (staircaseYD a).cells, g (QOU.QBeta.WenzlWeight.hook (staircaseYD a) x) := by
    refine Finset.sum_nbij' (fun x => (x.1, x.2 - (c + 1))) (fun y => (y.1, y.2 + (c + 1)))
      ?_ ?_ ?_ ?_ ?_
    all_goals rintro ⟨i, j⟩ hx
    all_goals dsimp only at hx ⊢
    all_goals simp only [mem_filter, hcell, hst, Prod.mk.injEq, true_and, and_true] at hx ⊢
    · omega
    · omega
    · omega
    · omega
    · have hlt : i + (j - (c + 1)) < a := by omega
      rw [hμ, cornerBlock_hook_stairA a c i j hx.1.2 (by omega) (by omega),
        staircase_hook a i (j - (c + 1)) hlt]
      congr 1
      omega
  -- δ_c block
  have hC : ∑ x ∈ μ.cells.filter (fun x => ¬ x.1 < a), g (QOU.QBeta.WenzlWeight.hook μ x)
      = ∑ x ∈ (staircaseYD c).cells, g (QOU.QBeta.WenzlWeight.hook (staircaseYD c) x) := by
    refine Finset.sum_nbij' (fun x => (x.1 - a, x.2)) (fun y => (y.1 + a, y.2))
      ?_ ?_ ?_ ?_ ?_
    all_goals rintro ⟨i, j⟩ hx
    all_goals dsimp only at hx ⊢
    all_goals simp only [mem_filter, hcell, hst, Prod.mk.injEq, true_and, and_true] at hx ⊢
    · omega
    · omega
    · omega
    · omega
    · have hlt : (i - a) + j < c := by omega
      rw [hμ, cornerBlock_hook_stairC a c i j (by omega) (by omega) (by omega),
        staircase_hook c (i - a) j hlt]
      congr 1
      omega
  rw [hrect, hA, hC]
  abel

/-- With a nonnegative `g`, the corner block's hook sum dominates the two staircase sums: the
rectangle term is dropped.  This is the step `Σ ε(h) ≥ S_δ(r) + S_δ(k−r)` of the lower bound. -/
theorem cornerBlock_hookSum_ge {N : Type*} [AddCommMonoid N] [PartialOrder N]
    [IsOrderedAddMonoid N] (g : ℕ → N) (hg : ∀ m, 0 ≤ g m) (a c : ℕ) :
    ∑ x ∈ (staircaseYD a).cells, g (QOU.QBeta.WenzlWeight.hook (staircaseYD a) x)
        + ∑ x ∈ (staircaseYD c).cells, g (QOU.QBeta.WenzlWeight.hook (staircaseYD c) x)
      ≤ ∑ x ∈ (cornerBlockYD a c).cells, g (QOU.QBeta.WenzlWeight.hook (cornerBlockYD a c) x) := by
  rw [cornerBlock_hookSum g a c]
  exact le_add_of_nonneg_right (Finset.sum_nonneg fun x _ => hg _)

/-- The corner block has `T_{a+c} + a` cells (size `n = T_k + r` with `k = a + c`, `r = a`),
read off the hook-sum decomposition at `g ≡ 1`. -/
theorem cornerBlockYD_card (a c : ℕ) :
    (cornerBlockYD a c).cells.card
      = (staircaseYD a).cells.card + (staircaseYD c).cells.card + a * (c + 1) := by
  have h := cornerBlock_hookSum (N := ℕ) (fun _ => 1) a c
  simp only [Finset.sum_const, smul_eq_mul, mul_one, Finset.card_product, card_range] at h
  exact h

end QOU.BraidKnot.HookSum
