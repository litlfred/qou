import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Tactic

/-!
# QOU.Mathlib.SYTHookFormulaBeta — the per-row Frame–Robinson–Thrall hook product

This file proves, **in full generality and sorry-free**, the per-row hook-product identity that the
beta-number form of the Frame–Robinson–Thrall hook-length formula rests on.  It is self-contained
combinatorics on `ℕ` — it does *not* import the heavy `IdentityIContentDecomposition` substrate; the
wiring of these lemmas to the corpus `prodHooks` lives in a companion file.

## The per-row hook product

For a weakly-decreasing partition `l`, the hook of cell `(i,j)` (`0`-indexed, `j < l[i]`) is
`h(i,j) = (l[i] − j) + (colLen j − i) − 1`.  Because every row `0,…,i` is at least as long as row `i`
(`l[r] ≥ l[i] > j`), the leg simplifies to `colLen j − 1 − i = #{r > i : l[r] > j}` — it depends only
on the **tail** `t = l[i+1:]` (with every part `≤ l[i]`).  So row `i`'s hook product is

    rowHookProd a t = ∏_{j < a} ((a − j) + #{p ∈ t : p > j}),   a = l[i], t = l[i+1:].

`rowHookProd` satisfies the **divisor-free recursion**

* `rowHookProd a [] = a!`                                            (`rowHookProd_nil`)
* `rowHookProd a (c :: r) · (a + 1 − c) = rowHookProd (a+1) r`       (`rowHookProd_cons_mul`)

(for `c ≤ a` and `r` weakly-decreasing with `max r ≤ c`).  Iterating gives the closed form

    rowHookProd a t · D a t = (a + |t|)!,    D a [] = 1,  D a (c::r) = (a+1−c) · D (a+1) r,

which is the per-row Frame–Robinson–Thrall hook product `∏_c h(i,c) = β_i! / ∏_{j>i}(β_i − β_j)` in
divisor-free form (`β_i = l[i] + (k−1−i)`; `D a t = ∏_{j>i}(β_i − β_j)`).  Pure `ℕ` combinatorics;
nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTBeta

/-- `cnt t j = #{p ∈ t : p > j}` — the column-`j` leg contribution of the tail `t`. -/
def cnt (t : List ℕ) (j : ℕ) : ℕ := (t.filter (fun p => j < p)).length

@[simp] theorem cnt_nil (j : ℕ) : cnt [] j = 0 := rfl

/-- `cnt` recursion on a cons: prepending `c` adds one iff `j < c`. -/
theorem cnt_cons (c : ℕ) (t : List ℕ) (j : ℕ) :
    cnt (c :: t) j = (if j < c then 1 else 0) + cnt t j := by
  unfold cnt
  rw [List.filter_cons]
  by_cases h : j < c <;> simp [h, Nat.add_comm]

/-- If every part of `t` is `≤ j`, the column-`j` leg is empty. -/
theorem cnt_eq_zero_of_le (t : List ℕ) (j : ℕ) (h : ∀ p ∈ t, p ≤ j) : cnt t j = 0 := by
  unfold cnt
  simp only [List.length_eq_zero_iff]
  rw [List.filter_eq_nil_iff]
  intro p hp
  simp only [decide_eq_true_eq, Nat.not_lt]
  exact h p hp

/-- **The per-row hook product** `∏_{j<a} ((a − j) + cnt t j)`. -/
def rowHookProd (a : ℕ) (t : List ℕ) : ℕ :=
  ((List.range a).map (fun j => (a - j) + cnt t j)).prod

/-- **Base case (sorry-free).** With an empty tail the leg vanishes and the hook product is the
descending product `∏_{j<a}(a − j) = a!`. -/
theorem rowHookProd_nil (a : ℕ) : rowHookProd a [] = Nat.factorial a := by
  unfold rowHookProd
  simp only [cnt_nil, Nat.add_zero]
  induction a with
  | zero => simp [Nat.factorial]
  | succ n ih =>
    rw [List.range_succ_eq_map, List.map_cons]
    simp only [Nat.sub_zero, List.prod_cons, List.map_map]
    have hcomp : ((fun j => (n + 1) - j) ∘ Nat.succ) = (fun j => n - j) := by
      funext j; simp [Nat.succ_sub_succ]
    rw [hcomp, ih, Nat.factorial_succ]

/-- Bridge a `List.range`-mapped product to the corresponding `Finset.range` product (fixed `f`). -/
theorem list_range_map_prod (n : ℕ) (f : ℕ → ℕ) :
    ((List.range n).map f).prod = ∏ j ∈ Finset.range n, f j := by
  induction n with
  | zero => simp
  | succ m ih =>
    rw [List.range_succ, List.map_append, List.prod_append, ih, Finset.prod_range_succ]
    simp

/-- `rowHookProd` as a `Finset.range` product (the flexible form for reindexing). -/
theorem rowHookProd_eq_finset (a : ℕ) (t : List ℕ) :
    rowHookProd a t = ∏ j ∈ Finset.range a, ((a - j) + cnt t j) := by
  unfold rowHookProd
  exact list_range_map_prod a (fun j => (a - j) + cnt t j)

/-- **Inductive step (sorry-free).** `rowHookProd a (c :: r) · (a + 1 − c) = rowHookProd (a+1) r`,
for `c ≤ a` and a weakly-decreasing tail `r` with every part `≤ c`.  The factor `(a + 1 − c)` is the
beta-gap `β_i − β_{i+1}`; the proof reindexes the row-`i` product against `g j = (a+1−j) + cnt r j`
(the `a+1` row product), supplying the missing middle factor `g c = a + 1 − c`. -/
theorem rowHookProd_cons_mul (a c : ℕ) (r : List ℕ) (hca : c ≤ a) (hr : ∀ p ∈ r, p ≤ c) :
    rowHookProd a (c :: r) * (a + 1 - c) = rowHookProd (a + 1) r := by
  -- abbreviation: g j is the (a+1)-row factor
  set g : ℕ → ℕ := fun j => (a + 1 - j) + cnt r j with hg
  -- cnt r j = 0 whenever c ≤ j (all parts ≤ c ≤ j)
  have hcnt0 : ∀ j, c ≤ j → cnt r j = 0 := fun j hj =>
    cnt_eq_zero_of_le r j (fun p hp => le_trans (hr p hp) hj)
  -- LHS factor of rowHookProd a (c::r) at index j
  have hLfac : ∀ j, ((a - j) + cnt (c :: r) j)
      = (a - j) + (if j < c then 1 else 0) + cnt r j := by
    intro j; rw [cnt_cons]; ring
  rw [rowHookProd_eq_finset, rowHookProd_eq_finset]
  simp_rw [hLfac]
  -- split range a into [0,c) and [c,a)
  have hsplit : Finset.range a = Finset.range c ∪ Finset.Ico c a := by
    rw [Finset.range_eq_Ico, Finset.Ico_union_Ico_eq_Ico (Nat.zero_le c) hca]
  have hdisj : Disjoint (Finset.range c) (Finset.Ico c a) := by
    rw [Finset.range_eq_Ico]; exact Finset.Ico_disjoint_Ico_consecutive 0 c a
  rw [hsplit, Finset.prod_union hdisj]
  -- prefix j < c : factor = (a-j)+1+cnt r j = g j
  have hpre : ∏ j ∈ Finset.range c, ((a - j) + (if j < c then 1 else 0) + cnt r j)
      = ∏ j ∈ Finset.range c, g j := by
    apply Finset.prod_congr rfl
    intro j hj
    rw [Finset.mem_range] at hj
    simp only [hj, if_true, hg]
    omega
  -- tail c ≤ j < a : if-branch false; cnt r j = 0; factor = a-j = g (j+1)
  have htail : ∏ j ∈ Finset.Ico c a, ((a - j) + (if j < c then 1 else 0) + cnt r j)
      = ∏ j ∈ Finset.Ico c a, g (j + 1) := by
    apply Finset.prod_congr rfl
    intro j hj
    rw [Finset.mem_Ico] at hj
    have hnj : ¬ j < c := by omega
    have e1 : cnt r j = 0 := hcnt0 j hj.1
    have e2 : cnt r (j + 1) = 0 := hcnt0 (j + 1) (by omega)
    simp only [hnj, if_false, hg, e1, e2, Nat.add_zero]
    omega
  rw [hpre, htail]
  -- reindex the tail product g(j+1) over Ico c a to g over Ico (c+1) (a+1)
  have hreindex : ∏ j ∈ Finset.Ico c a, g (j + 1) = ∏ j ∈ Finset.Ico (c + 1) (a + 1), g j := by
    rw [Finset.prod_Ico_eq_prod_range, Finset.prod_Ico_eq_prod_range]
    apply Finset.prod_congr (by congr 1; omega)
    intro j _; congr 1; omega
  rw [hreindex]
  -- now (∏_{range c} g) * (∏_{Ico (c+1) (a+1)} g) * (a+1-c) = ∏_{range (a+1)} g
  -- supply g c = a + 1 - c as the missing middle factor
  have hgc : g c = a + 1 - c := by simp only [hg]; rw [hcnt0 c (le_refl c)]; rfl
  have hca1 : c + 1 ≤ a + 1 := by omega
  -- range (a+1) = range (c+1) ∪ Ico (c+1) (a+1), and range (c+1) = range c with g c peeled
  have hsplit2 : ∏ j ∈ Finset.range (a + 1), g j
      = (∏ j ∈ Finset.range (c + 1), g j) * ∏ j ∈ Finset.Ico (c + 1) (a + 1), g j := by
    have hu : Finset.range (a + 1) = Finset.range (c + 1) ∪ Finset.Ico (c + 1) (a + 1) := by
      ext x
      simp only [Finset.mem_range, Finset.mem_union, Finset.mem_Ico]
      omega
    have hdj : Disjoint (Finset.range (c + 1)) (Finset.Ico (c + 1) (a + 1)) := by
      rw [Finset.range_eq_Ico]
      exact Finset.Ico_disjoint_Ico_consecutive 0 (c + 1) (a + 1)
    rw [hu, Finset.prod_union hdj]
  rw [hsplit2, Finset.prod_range_succ, hgc]
  ring

end QOU.Mathlib.SYTBeta
