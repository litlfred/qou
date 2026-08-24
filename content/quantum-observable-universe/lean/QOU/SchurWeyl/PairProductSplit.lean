import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Tactic

/-!
# QOU.SchurWeyl.PairProductSplit — splitting `∏_{i<j<r}` at one index

The β-pair product `P(β) = ∏_{i<j<r} f(β_i − β_j)` changes, under `β ↦ β + e_a`, only in the pairs
that involve `a`.  To compare `P(β')` with `P(β)` one therefore wants the product split into

* **row `a`** — the pairs `(a, j)` with `j > a`,
* **column `a`** — the pairs `(i, a)` with `i < a`,
* the rest, which is untouched.

This file is that split, stated division-free for an arbitrary `g : ℕ → ℕ → M` so it applies to
`P(β)` and `P(β')` alike.

`prod_pairs_split_ne` is the form actually used: two families agreeing off the pairs involving `a`
have the same "rest", so their products differ exactly by the row-`a` and column-`a` factors.

## Base ring (§7c)

Generic `[CommMonoid M]`.  Pure `ℕ` indexing.

LaTeX label: `lem:pair-product-split`
-/

namespace QOU.SchurWeyl

open Finset

variable {M : Type*} [CommMonoid M]

/-- **The pair product, split at `a`.** -/
theorem prod_pairs_split {r a : ℕ} (ha : a < r) (g : ℕ → ℕ → M) :
    (∏ i ∈ Finset.range r, ∏ j ∈ Finset.Ico (i + 1) r, g i j)
      = ((∏ j ∈ Finset.Ico (a + 1) r, g a j) * ∏ i ∈ Finset.range a, g i a)
        * ((∏ i ∈ Finset.range a, ∏ j ∈ (Finset.Ico (i + 1) r).erase a, g i j)
            * ∏ i ∈ Finset.Ico (a + 1) r, ∏ j ∈ Finset.Ico (i + 1) r, g i j) := by
  classical
  have hsplit : ∏ i ∈ Finset.range r, (∏ j ∈ Finset.Ico (i + 1) r, g i j)
      = (∏ i ∈ Finset.range a, ∏ j ∈ Finset.Ico (i + 1) r, g i j)
        * ∏ i ∈ Finset.Ico a r, ∏ j ∈ Finset.Ico (i + 1) r, g i j :=
    (Finset.prod_range_mul_prod_Ico _ (le_of_lt ha)).symm
  have hIco : Finset.Ico a r = insert a (Finset.Ico (a + 1) r) := by
    ext x
    simp only [Finset.mem_Ico, Finset.mem_insert]
    omega
  have hnot : a ∉ Finset.Ico (a + 1) r := by simp
  have hpre : (∏ i ∈ Finset.range a, ∏ j ∈ Finset.Ico (i + 1) r, g i j)
      = (∏ i ∈ Finset.range a, g i a)
        * ∏ i ∈ Finset.range a, ∏ j ∈ (Finset.Ico (i + 1) r).erase a, g i j := by
    rw [← Finset.prod_mul_distrib]
    refine Finset.prod_congr rfl fun i hi => ?_
    rw [Finset.mem_range] at hi
    have hmem : a ∈ Finset.Ico (i + 1) r := Finset.mem_Ico.mpr ⟨by omega, ha⟩
    exact (Finset.mul_prod_erase _ _ hmem).symm
  rw [hsplit, hIco, Finset.prod_insert hnot, hpre]
  ac_rfl

/-- **Two families agreeing off the pairs that involve `a`** have products differing only by the
row-`a` and column-`a` factors. -/
theorem prod_pairs_split_ne {r a : ℕ} (ha : a < r) (g h : ℕ → ℕ → M)
    (hoff : ∀ i j, i < a → j ≠ a → h i j = g i j)
    (hbelow : ∀ i j, a < i → a < j → h i j = g i j) :
    (∏ i ∈ Finset.range r, ∏ j ∈ Finset.Ico (i + 1) r, h i j)
        * ((∏ j ∈ Finset.Ico (a + 1) r, g a j) * ∏ i ∈ Finset.range a, g i a)
      = (∏ i ∈ Finset.range r, ∏ j ∈ Finset.Ico (i + 1) r, g i j)
        * ((∏ j ∈ Finset.Ico (a + 1) r, h a j) * ∏ i ∈ Finset.range a, h i a) := by
  classical
  have hrest : (∏ i ∈ Finset.range a, ∏ j ∈ (Finset.Ico (i + 1) r).erase a, h i j)
      * (∏ i ∈ Finset.Ico (a + 1) r, ∏ j ∈ Finset.Ico (i + 1) r, h i j)
      = (∏ i ∈ Finset.range a, ∏ j ∈ (Finset.Ico (i + 1) r).erase a, g i j)
        * ∏ i ∈ Finset.Ico (a + 1) r, ∏ j ∈ Finset.Ico (i + 1) r, g i j := by
    congr 1
    · refine Finset.prod_congr rfl fun i hi => ?_
      rw [Finset.mem_range] at hi
      exact Finset.prod_congr rfl fun j hj => hoff i j hi (Finset.ne_of_mem_erase hj)
    · refine Finset.prod_congr rfl fun i hi => ?_
      rw [Finset.mem_Ico] at hi
      refine Finset.prod_congr rfl fun j hj => ?_
      rw [Finset.mem_Ico] at hj
      exact hbelow i j (by omega) (by omega)
  rw [prod_pairs_split ha h, prod_pairs_split ha g, hrest]
  ac_rfl

end QOU.SchurWeyl
