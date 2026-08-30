import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Order.Interval.Finset.Nat
import QOU.SchurWeyl.OcneanuWeightWenzl

/-!
# QOU.SchurWeyl.OcneanuWeightBranching — the branching identity at convention D

The Markov trace on the tower `H_1 ⊂ H_2 ⊂ ⋯` is consistent iff its weights satisfy

`w_μ^{(n)} = ∑_{λ = μ + □} w_λ^{(n+1)}`,

the sum running over the addable corners of `μ`.  This file proves that identity for
`ocneanuWeight` at convention D's Markov parameter `z = q³/(q²+1)`.

## Why convention D makes this tractable

At convention D every diagram with three or more rows carries weight zero
(`ocneanuWeight_conventionD_eq_zero_iff`).  So the whole trace lives on the diagrams of **at most
two rows**, `twoRow m k` with `k ≤ m`, and such a diagram has at most three addable corners —
`(0,m)`, `(1,k)`, and `(2,0)` — of which the third contributes **zero**.  The branching identity is
therefore a **two-term** identity, not a sum over all addable corners of an arbitrary diagram.

Via `ocneanuWeight_conventionD_eq_schurPrincipal` it reduces further.  The two-row weight has the
closed form

`schurPrincipal 2 Q (twoRow m k) = Q^k · (1 + Q + ⋯ + Q^{m−k})`

(`schurPrincipal_twoRow`) — the hook-content product telescopes completely — and branching becomes
the single arithmetic identity

`(1 + Q + ⋯ + Q^d)(1 + Q) = (1 + Q + ⋯ + Q^{d+1}) + Q(1 + Q + ⋯ + Q^{d−1})`

(`qBracket_pieri`), which is the Pieri rule `s_μ · e₁ = ∑_{λ = μ+□} s_λ` in two variables.  The
`d = 0` case needs no special handling in the arithmetic — the empty sum kills the last term — but
it does at the level of diagrams, since `twoRow m (m+1)` is not a partition; hence the separate
`_diag` statements.

## What this is and is not

It is the **consistency of the trace tower** at convention D: the weight family is coherent under
restriction `H_{n+1} → H_n`.  It is **not** the Markov condition `tr(x·σ_n) = z·tr(x)`, which
remains open — see `OcneanuWeight`'s docstring and bean `qou-uer7`.  Consistency is one of the two
halves; it does not imply the other.

## Base ring (§7c)

Generic `[Field R]` throughout; the combinatorial lemmas are pure `ℕ`.  No `ℝ`, no ordering.

LaTeX label: `thm:ocneanu-weight-branching-conventionD`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset QOU.QBeta.WenzlWeight

variable {m k : ℕ}

def twoRow (m k : ℕ) (h : k ≤ m) : YoungDiagram :=
  ofRowLens [m, k] (by simp [List.Sorted]; omega)

theorem mem_twoRow (h : k ≤ m) (i j : ℕ) :
    ((i, j) ∈ twoRow m k h) ↔ (i = 0 ∧ j < m) ∨ (i = 1 ∧ j < k) := by
  rw [twoRow, YoungDiagram.mem_ofRowLens]
  constructor
  · rintro ⟨hlen, hlt⟩
    have h2 : i = 0 ∨ i = 1 := by simp at hlen; omega
    rcases h2 with rfl | rfl <;> simp at hlt <;> tauto
  · rintro (⟨rfl, h2⟩ | ⟨rfl, h2⟩) <;> exact ⟨by simp, by simpa using h2⟩

theorem rowLen_twoRow_zero (h : k ≤ m) : (twoRow m k h).rowLen 0 = m := by
  have := YoungDiagram.rowLen_ofRowLens (w := [m,k]) (hw := by simp [List.Sorted]; omega) ⟨0, by simp⟩
  simpa [twoRow] using this

theorem rowLen_twoRow_one (h : k ≤ m) : (twoRow m k h).rowLen 1 = k := by
  have := YoungDiagram.rowLen_ofRowLens (w := [m,k]) (hw := by simp [List.Sorted]; omega) ⟨1, by simp⟩
  simpa [twoRow] using this

theorem colLen_twoRow (h : k ≤ m) (j : ℕ) :
    (twoRow m k h).colLen j = if j < k then 2 else if j < m then 1 else 0 := by
  have key : ∀ i, i < (twoRow m k h).colLen j ↔ ((i, j) ∈ twoRow m k h) := by
    intro i; exact (YoungDiagram.mem_iff_lt_colLen).symm
  have hmem : ∀ i, ((i, j) ∈ twoRow m k h) ↔ ((i = 0 ∧ j < m) ∨ (i = 1 ∧ j < k)) := by
    intro i; exact mem_twoRow h i j
  split_ifs with h1 h2
  · have a : 1 < (twoRow m k h).colLen j := (key 1).mpr ((hmem 1).mpr (Or.inr ⟨rfl, h1⟩))
    have b : ¬ (2 < (twoRow m k h).colLen j) := fun hc => by
      have := (key 2).mp hc; rw [hmem 2] at this; omega
    omega
  · have a : 0 < (twoRow m k h).colLen j := (key 0).mpr ((hmem 0).mpr (Or.inl ⟨rfl, h2⟩))
    have b : ¬ (1 < (twoRow m k h).colLen j) := fun hc => by
      have := (key 1).mp hc; rw [hmem 1] at this; omega
    omega
  · have b : ¬ (0 < (twoRow m k h).colLen j) := fun hc => by
      have := (key 0).mp hc; rw [hmem 0] at this; omega
    omega

-- Stage B: cells and hook values
theorem cells_twoRow (h : k ≤ m) :
    (twoRow m k h).cells
      = (Finset.range m).image (fun j => (0, j)) ∪ (Finset.range k).image (fun j => (1, j)) := by
  ext c
  obtain ⟨i, j⟩ := c
  simp only [YoungDiagram.mem_cells, Finset.mem_union, Finset.mem_image, Finset.mem_range,
    Prod.mk.injEq, mem_twoRow h i j]
  constructor
  · rintro (⟨rfl, hj⟩ | ⟨rfl, hj⟩)
    · exact Or.inl ⟨j, hj, rfl, rfl⟩
    · exact Or.inr ⟨j, hj, rfl, rfl⟩
  · rintro (⟨a, ha, rfl, rfl⟩ | ⟨a, ha, rfl, rfl⟩)
    · exact Or.inl ⟨rfl, ha⟩
    · exact Or.inr ⟨rfl, ha⟩

theorem hook_twoRow_row0 (h : k ≤ m) {j : ℕ} (hj : j < m) :
    hook (twoRow m k h) (0, j) = if j < k then m - j + 1 else m - j := by
  unfold hook
  rw [rowLen_twoRow_zero, colLen_twoRow]
  split_ifs with h1
  · omega
  · omega

theorem hook_twoRow_row1 (h : k ≤ m) {j : ℕ} (hj : j < k) :
    hook (twoRow m k h) (1, j) = k - j := by
  unfold hook
  rw [rowLen_twoRow_one, colLen_twoRow]
  simp only [hj, if_true]
  omega

theorem nPart_twoRow (h : k ≤ m) :
    ∑ c ∈ (twoRow m k h).cells, c.1 = k := by
  rw [cells_twoRow h, Finset.sum_union, Finset.sum_image, Finset.sum_image] <;>
    simp [Finset.disjoint_left]

-- Stage C: the telescope
theorem prod_oneSub_telescope (R : Type*) [CommRing R] (Q : R) (d : ℕ) :
    (∏ j ∈ range d, (1 - Q ^ (j + 2))) * (1 - Q)
      = (∏ j ∈ range d, (1 - Q ^ (j + 1))) * (1 - Q ^ (d + 1)) := by
  induction d with
  | zero => simp
  | succ n ih =>
    rw [Finset.prod_range_succ, Finset.prod_range_succ]
    calc (∏ j ∈ range n, (1 - Q ^ (j + 2))) * (1 - Q ^ (n + 2)) * (1 - Q)
        = ((∏ j ∈ range n, (1 - Q ^ (j + 2))) * (1 - Q)) * (1 - Q ^ (n + 2)) := by ring
      _ = ((∏ j ∈ range n, (1 - Q ^ (j + 1))) * (1 - Q ^ (n + 1))) * (1 - Q ^ (n + 2)) := by
            rw [ih]
      _ = (∏ j ∈ range n, (1 - Q ^ (j + 1))) * (1 - Q ^ (n + 1)) * (1 - Q ^ (n + 1 + 1)) := by
            ring_nf

/-- `Q·(1 + ⋯ + Q^{n−1}) + 1 = 1 + ⋯ + Q^n`.  The companion of `geom_oneSub`, and the whole
arithmetic content of the row-0 Markov corner identity in `OcneanuWeightMarkovCorner`. -/
theorem mul_geom_succ {R : Type*} [CommRing R] (x : R) :
    ∀ n : ℕ, x * (∑ i ∈ range n, x ^ i) + 1 = ∑ i ∈ range (n + 1), x ^ i
  | 0 => by simp
  | n + 1 => by
      rw [Finset.sum_range_succ (n := n), Finset.sum_range_succ (n := n + 1), ← mul_geom_succ x n]
      ring

/-- `(1 + Q + ⋯ + Q^{n−1})(1 − Q) = 1 − Q^n`.  Proved here rather than imported: the Mathlib
module carrying `geom_sum_mul` is deprecated, and this is four lines. -/
theorem geom_oneSub {R : Type*} [CommRing R] (Q : R) :
    ∀ n : ℕ, (∑ i ∈ range n, Q ^ i) * (1 - Q) = 1 - Q ^ n
  | 0 => by simp
  | n + 1 => by rw [Finset.sum_range_succ, add_mul, geom_oneSub Q n, pow_succ]; ring

theorem schurPrincipal_twoRow {R : Type*} [Field R] (Q : R)
    (hgen : ∀ i : ℕ, 0 < i → Q ^ i ≠ 1) (h : k ≤ m) :
    schurPrincipal 2 Q (twoRow m k h) = Q ^ k * ∑ i ∈ range (m - k + 1), Q ^ i := by
  have hne : ∀ i : ℕ, 0 < i → (1 : R) - Q ^ i ≠ 0 := fun i hi hc =>
    hgen i hi (by linear_combination -hc)
  set d := m - k with hd
  have hmd : m = k + d := by omega
  -- the two products over the two rows
  have hcells := cells_twoRow h
  have hdisj : Disjoint ((range m).image (fun j => ((0:ℕ), j)))
      ((range k).image (fun j => ((1:ℕ), j))) := by
    simp [Finset.disjoint_left]
  rw [schurPrincipal, nPart, nPart_twoRow h, hcells, Finset.prod_union hdisj,
    Finset.prod_image (by intro a _ b _ hab; simpa using hab),
    Finset.prod_image (by intro a _ b _ hab; simpa using hab)]
  -- rewrite the row-0 and row-1 factors into nat-power form
  have e0 : ∀ j ∈ range m,
      (1 - Q ^ (((2:ℕ):ℤ) + content (0, j))) / (1 - Q ^ hook (twoRow m k h) (0, j))
        = (1 - Q ^ (j + 2)) / (1 - Q ^ (if j < k then m - j + 1 else m - j)) := by
    intro j hj
    rw [hook_twoRow_row0 h (Finset.mem_range.mp hj)]
    congr 2
    · have : ((2:ℕ):ℤ) + content (0, j) = ((j + 2 : ℕ) : ℤ) := by unfold content; push_cast; ring
      rw [this, zpow_natCast]
  have e1 : ∀ j ∈ range k,
      (1 - Q ^ (((2:ℕ):ℤ) + content (1, j))) / (1 - Q ^ hook (twoRow m k h) (1, j))
        = (1 - Q ^ (j + 1)) / (1 - Q ^ (k - j)) := by
    intro j hj
    rw [hook_twoRow_row1 h (Finset.mem_range.mp hj)]
    congr 2
    · have : ((2:ℕ):ℤ) + content (1, j) = ((j + 1 : ℕ) : ℤ) := by unfold content; push_cast; ring
      rw [this, zpow_natCast]
  rw [Finset.prod_congr rfl e0, Finset.prod_congr rfl e1]
  congr 1
  have hmd' : m = d + k := by omega
  set A := ∏ x ∈ range k, (1 - Q ^ (x + 1)) with hA
  set B := ∏ x ∈ range k, (1 - Q ^ (d + x + 2)) with hB
  set C := ∏ x ∈ range d, (1 - Q ^ (x + 1)) with hC
  set P := ∏ x ∈ range d, (1 - Q ^ (x + 2)) with hP
  have hA0 : A ≠ 0 := Finset.prod_ne_zero_iff.mpr fun i _ => hne _ (by omega)
  have hB0 : B ≠ 0 := Finset.prod_ne_zero_iff.mpr fun i _ => hne _ (by omega)
  have hC0 : C ≠ 0 := Finset.prod_ne_zero_iff.mpr fun i _ => hne _ (by omega)
  have hQ1 : (1 : R) - Q ≠ 0 := by simpa using hne 1 one_pos
  -- row 1 collapses to 1
  have hrefl1 : ∏ x ∈ range k, (1 - Q ^ (k - x)) = A := by
    rw [hA, ← Finset.prod_range_reflect (fun x => 1 - Q ^ (x + 1)) k]
    exact Finset.prod_congr rfl fun x hx => by
      have := Finset.mem_range.mp hx; rw [show k - 1 - x + 1 = k - x by omega]
  -- row 0 numerator and denominator
  have hnum : ∏ x ∈ range m, (1 - Q ^ (x + 2)) = P * B := by
    rw [hP, hB, hmd', Finset.prod_range_add]
  have hden : ∏ x ∈ range m, (1 - Q ^ (if x < k then m - x + 1 else m - x)) = B * C := by
    rw [hmd] at *
    rw [Finset.prod_range_add]
    congr 1
    · rw [hB, ← Finset.prod_range_reflect (fun x => 1 - Q ^ (d + x + 2)) k]
      exact Finset.prod_congr rfl fun x hx => by
        have := Finset.mem_range.mp hx
        rw [if_pos (by omega), show d + (k - 1 - x) + 2 = k + d - x + 1 by omega]
    · rw [hC, ← Finset.prod_range_reflect (fun x => 1 - Q ^ (x + 1)) d]
      exact Finset.prod_congr rfl fun x hx => by
        have := Finset.mem_range.mp hx
        rw [if_neg (by omega), show d - 1 - x + 1 = k + d - (k + x) by omega]
  rw [Finset.prod_div_distrib, Finset.prod_div_distrib, hrefl1, div_self hA0, mul_one,
    hnum, hden]
  -- P * B / (B * C) = geometric sum
  rw [mul_comm P B, mul_div_mul_left _ _ hB0]
  have htel := prod_oneSub_telescope R Q d
  rw [← hP, ← hC] at htel
  have hgeo : (∑ i ∈ range (d + 1), Q ^ i) * (1 - Q) = 1 - Q ^ (d + 1) := geom_oneSub Q (d + 1)
  have hPC : P = C * ∑ i ∈ range (d + 1), Q ^ i := by
    refine mul_right_cancel₀ hQ1 ?_
    rw [mul_assoc, hgeo]
    exact htel
  rw [hPC]
  exact mul_div_cancel_left₀ _ hC0

theorem qBracket_pieri {R : Type*} [CommRing R] (x : R) (d : ℕ) :
    (∑ i ∈ range (d + 1), x ^ i) * (1 + x)
      = (∑ i ∈ range (d + 2), x ^ i) + x * ∑ i ∈ range d, x ^ i := by
  have h2 : (∑ i ∈ range (d + 2), x ^ i) = (∑ i ∈ range (d + 1), x ^ i) + x ^ (d + 1) :=
    Finset.sum_range_succ _ _
  have h3 : x * ∑ i ∈ range (d + 1), x ^ i
      = x * (∑ i ∈ range d, x ^ i) + x ^ (d + 1) := by
    rw [Finset.sum_range_succ]; ring
  rw [h2]
  calc (∑ i ∈ range (d + 1), x ^ i) * (1 + x)
      = (∑ i ∈ range (d + 1), x ^ i) + x * ∑ i ∈ range (d + 1), x ^ i := by ring
    _ = (∑ i ∈ range (d + 1), x ^ i) + (x * (∑ i ∈ range d, x ^ i) + x ^ (d + 1)) := by rw [h3]
    _ = (∑ i ∈ range (d + 1), x ^ i) + x ^ (d + 1) + x * ∑ i ∈ range d, x ^ i := by ring

theorem card_twoRow (h : k ≤ m) : (twoRow m k h).cells.card = m + k := by
  rw [cells_twoRow h, Finset.card_union_of_disjoint (by simp [Finset.disjoint_left]),
    Finset.card_image_of_injective _ (by intro a b hab; simpa using hab),
    Finset.card_image_of_injective _ (by intro a b hab; simpa using hab),
    Finset.card_range, Finset.card_range]

theorem schurPrincipal_twoRow_pieri {R : Type*} [Field R] (Q : R)
    (hgen : ∀ i : ℕ, 0 < i → Q ^ i ≠ 1) (hk : k < m) :
    (1 + Q) * schurPrincipal 2 Q (twoRow m k hk.le)
      = schurPrincipal 2 Q (twoRow (m + 1) k (by omega))
        + schurPrincipal 2 Q (twoRow m (k + 1) (by omega)) := by
  rw [schurPrincipal_twoRow Q hgen hk.le, schurPrincipal_twoRow Q hgen (by omega : k ≤ m + 1),
    schurPrincipal_twoRow Q hgen (by omega : k + 1 ≤ m),
    show m + 1 - k + 1 = (m - k) + 2 by omega,
    show m - (k + 1) + 1 = m - k by omega]
  set d := m - k with hd
  calc (1 + Q) * (Q ^ k * ∑ i ∈ range (d + 1), Q ^ i)
      = Q ^ k * ((∑ i ∈ range (d + 1), Q ^ i) * (1 + Q)) := by ring
    _ = Q ^ k * ((∑ i ∈ range (d + 2), Q ^ i) + Q * ∑ i ∈ range d, Q ^ i) := by
          rw [qBracket_pieri Q d]
    _ = Q ^ k * ∑ i ∈ range (d + 2), Q ^ i + Q ^ (k + 1) * ∑ i ∈ range d, Q ^ i := by ring

theorem schurPrincipal_twoRow_pieri_diag {R : Type*} [Field R] (Q : R)
    (hgen : ∀ i : ℕ, 0 < i → Q ^ i ≠ 1) (m : ℕ) :
    (1 + Q) * schurPrincipal 2 Q (twoRow m m le_rfl)
      = schurPrincipal 2 Q (twoRow (m + 1) m (by omega)) := by
  rw [schurPrincipal_twoRow Q hgen le_rfl, schurPrincipal_twoRow Q hgen (by omega : m ≤ m + 1),
    show m - m + 1 = 1 by omega, show m + 1 - m + 1 = 2 by omega]
  simp [Finset.sum_range_succ]
  ring

theorem ocneanuWeight_twoRow_branching {R : Type*} [Field R] (q : R) (hq : q ≠ 0)
    (hq21 : q ^ 2 + 1 ≠ 0) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : R) ^ i ≠ 1) (hk : k < m) :
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow m k hk.le)
      = ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow (m + 1) k (by omega))
        + ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow m (k + 1) (by omega)) := by
  rw [ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21,
    ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21,
    ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21,
    card_twoRow, card_twoRow, card_twoRow]
  have hpow : ∀ n : ℕ, ((q ^ 2 + 1 : R)) ^ n ≠ 0 := fun n => pow_ne_zero _ hq21
  have hpieri := schurPrincipal_twoRow_pieri (R := R) (q ^ 2) hgen hk
  rw [show m + 1 + k = (m + k) + 1 by omega, show m + (k + 1) = (m + k) + 1 by omega,
    pow_succ]
  field_simp
  linear_combination ((q ^ 2 + 1 : R) ^ (m + k)) * hpieri

/-- **Branching at the diagonal `k = m`.**  `twoRow m (m+1)` is not a partition, so `(1,k)` is not
an addable corner here and only one term survives.  The third addable corner `(2,0)` again
contributes zero, by `ocneanuWeight_conventionD_eq_zero_of_three_rows`. -/
theorem ocneanuWeight_twoRow_branching_diag {R : Type*} [Field R] (q : R) (hq : q ≠ 0)
    (hq21 : q ^ 2 + 1 ≠ 0) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : R) ^ i ≠ 1) (m : ℕ) :
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow m m le_rfl)
      = ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow (m + 1) m (by omega)) := by
  rw [ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21,
    ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21, card_twoRow, card_twoRow]
  have hpieri := schurPrincipal_twoRow_pieri_diag (R := R) (q ^ 2) hgen m
  have hpow : ((q ^ 2 + 1 : R)) ^ (m + m) ≠ 0 := pow_ne_zero _ hq21
  rw [show m + 1 + m = (m + m) + 1 by omega, pow_succ]
  field_simp
  linear_combination ((q ^ 2 + 1 : R) ^ (m + m)) * hpieri

end QOU.SchurWeyl
