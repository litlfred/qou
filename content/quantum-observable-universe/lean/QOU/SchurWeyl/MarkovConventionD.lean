import QOU.SchurWeyl.TwoRowCorners
import QOU.SchurWeyl.OcneanuWeightMarkovCorner
import QOU.SchurWeyl.MarkovAssembly

/-!
# QOU.SchurWeyl.MarkovConventionD — the Markov condition, unconditionally, at every n

`MarkovAssembly` reduced the Markov condition for the weighted seminormal trace to a per-corner
identity, taken there as a hypothesis.  This file **discharges that hypothesis** at convention D,
for every Young diagram and every removable corner — so the Markov condition itself holds
unconditionally:

```
∑_{|λ| = m+2} W_λ · tr(ρ_λ(ι y) · σ_{m+1}) = z_D · ∑_{|ν| = m+1} W_ν · tr(ρ_ν(y))
```

for every `y ∈ H_{m+1}(q)`, with `W = ocneanuWeight q z_D` and `z_D = q³/(q²+1)`.

## Why this needs no general-`n` arithmetic

The per-corner identity quantifies over **every** diagram, and `OcneanuWeightMarkovCorner` proves
it only for the ≤2-row ones.  The gap is closed by the convention-D vanishing rather than by more
arithmetic, and the split is clean:

* **≥3 rows** — `W_ν = 0`, and adding a cell cannot *reduce* the row count, so every `W_{ν+s} = 0`
  as well.  Both sides are `0`; no corner arithmetic is involved at all
  (`corner_identity_of_three_rows`).
* **≤2 rows** — the diagram **is** a `twoRow` (`eq_twoRow_of_rowLen_two_eq_zero`), it has at most
  three addable cells, and the third — `(2,0)` — produces a 3-row diagram of weight `0`.  What
  survives is exactly the two-term statement `OcneanuWeightMarkovCorner` proves
  (`corner_identity_twoRow`).

So the two-term shape of that file, which looks like a restriction, is the general statement once
the vanishing is applied.

## What this closes

`OcneanuWeightWenzl`'s docstring names the remaining external input as *"`ocneanuWeight` satisfies
`tr(x·σ_n) = z·tr(x)` at general `n`"*.  At convention D — the canonical one per the 2026-08-15
owner ruling — that is this file's `markov_conventionD`, and it is sorry-free.  For **arbitrary**
`z` the per-corner identity is still open; `ocneanu_markov_corner_reduction.py` tests it exactly
at symbolic `z` through `n = 6`.

## Base ring (§7c)

`ℝ`, inherited from `seminormalParam` and `seminormalRep`.  The genericity hypothesis
`hgen : ∀ i, 0 < i → (q²)^i ≠ 1` is the standard not-a-root-of-unity condition, and it is
archimedean only in that it is stated over `ℝ`.

LaTeX label: `thm:markov-convention-d`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib YoungDiagram QOU.SchurWeyl.Seminormal QOU.SchurWeyl.HeckeInclusion

variable {m k : ℕ}

/-- A diagram with an empty row 2 **is** a `twoRow`. -/
theorem eq_twoRow_of_rowLen_two_eq_zero (ν : YoungDiagram) (h2 : ν.rowLen 2 = 0) :
    ν = twoRow (ν.rowLen 0) (ν.rowLen 1) (YoungDiagram.rowLen_anti ν 0 1 (by omega)) := by
  ext c
  obtain ⟨i, j⟩ := c
  rw [YoungDiagram.mem_cells, YoungDiagram.mem_iff_lt_rowLen,
    show ((i, j) ∈ (twoRow (ν.rowLen 0) (ν.rowLen 1)
        (YoungDiagram.rowLen_anti ν 0 1 (by omega))).cells)
      ↔ ((i, j) ∈ twoRow (ν.rowLen 0) (ν.rowLen 1)
        (YoungDiagram.rowLen_anti ν 0 1 (by omega))) from Iff.rfl,
    mem_twoRow]
  match i with
  | 0 => simp
  | 1 => simp
  | (n + 2) =>
    have hle : ν.rowLen (n + 2) ≤ ν.rowLen 2 := YoungDiagram.rowLen_anti ν 2 (n + 2) (by omega)
    constructor
    · intro hc; omega
    · rintro (⟨hc, -⟩ | ⟨hc, -⟩) <;> omega

/-- Adding a cell cannot empty row 2. -/
theorem rowLen_two_pos_addCell {ν : YoungDiagram} {s : ℕ × ℕ} (hs : IsAddableCell ν s)
    (h : 0 < ν.rowLen 2) : 0 < (addCell ν s hs).rowLen 2 := by
  rw [← YoungDiagram.mem_iff_lt_rowLen] at h ⊢
  exact (mem_addCell s hs (2, 0)).mpr (Or.inr h)

theorem corner_identity_of_three_rows (q : ℝ) (hq21 : q ^ 2 + 1 ≠ 0)
    (ν : YoungDiagram) (h : 0 < ν.rowLen 2) (r : ℕ × ℕ) :
    ∑ s : {s : ℕ × ℕ // IsAddableCell ν s},
        ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (addCell ν s.1 s.2)
          * seminormalParam q (axialDistance r s.1)
      = (q ^ 3 / (q ^ 2 + 1)) * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν := by
  rw [ocneanuWeight_conventionD_eq_zero_of_three_rows q hq21 ν h, mul_zero]
  refine Finset.sum_eq_zero fun s _ => ?_
  rw [ocneanuWeight_conventionD_eq_zero_of_three_rows q hq21 _
    (rowLen_two_pos_addCell s.2 h), zero_mul]

theorem corner_identity_twoRow (q : ℝ) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (h : k ≤ m)
    (r : ℕ × ℕ) (hr : IsCornerCell (twoRow m k h) r) :
    ∑ s : {s : ℕ × ℕ // IsAddableCell (twoRow m k h) s},
        ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (addCell (twoRow m k h) s.1 s.2)
          * seminormalParam q (axialDistance r s.1)
      = (q ^ 3 / (q ^ 2 + 1)) * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow m k h) := by
  classical
  set z : ℝ := q ^ 3 / (q ^ 2 + 1) with hz
  -- move to a summand that depends only on the cell
  have hcell : ∑ s : {s : ℕ × ℕ // IsAddableCell (twoRow m k h) s},
      ocneanuWeight q z (addCell (twoRow m k h) s.1 s.2)
        * seminormalParam q (axialDistance r s.1)
      = ∑ s : {s : ℕ × ℕ // IsAddableCell (twoRow m k h) s},
          (fun c => ocneanuWeight q z (addCellOrSelf (twoRow m k h) c)
            * seminormalParam q (axialDistance r c)) s.1 :=
    Finset.sum_congr rfl fun s _ => by rw [← addCellOrSelf_of s.2]
  rw [hcell, sum_addable_twoRow h (fun c => ocneanuWeight q z (addCellOrSelf (twoRow m k h) c)
      * seminormalParam q (axialDistance r c)),
    sum_addableTwoRow_expand]
  -- identify the three summands
  have h0 : addCellOrSelf (twoRow m k h) (0, m) = twoRow (m + 1) k (by omega) := by
    rw [addCellOrSelf_of ((isAddableCell_twoRow_iff h (0, m)).mpr (Or.inl rfl)),
      addCell_twoRow_row0]
  have hzero2 : ∀ hk0 : 0 < k,
      ocneanuWeight q z (addCellOrSelf (twoRow m k h) (2, 0)) = 0 := by
    intro hk0
    have hadd : IsAddableCell (twoRow m k h) (2, 0) :=
      (isAddableCell_twoRow_iff h (2, 0)).mpr (Or.inr (Or.inr ⟨rfl, hk0⟩))
    rw [addCellOrSelf_of hadd]
    exact ocneanuWeight_conventionD_eq_zero_of_three_rows q hq21 _
      (rowLen_two_addCell_row2 h hadd)
  rcases (isCornerCell_twoRow_iff h r).mp hr with ⟨rfl, hkm⟩ | ⟨rfl, hk0⟩
  · -- removable corner at the end of row 0
    have h1 : addCellOrSelf (twoRow m k h) (1, k) = twoRow m (k + 1) (by omega) := by
      rw [addCellOrSelf_of ((isAddableCell_twoRow_iff h (1, k)).mpr
        (Or.inr (Or.inl ⟨rfl, hkm⟩))), addCell_twoRow_row1 h hkm]
    have ha0 : axialDistance (0, m - 1) (0, m) = 1 := by
      simp only [axialDistance, cellContent]; omega
    have ha1 : axialDistance (0, m - 1) (1, k) = (k : ℤ) - (m : ℤ) := by
      simp only [axialDistance, cellContent]; omega
    rw [if_pos hkm, h0, h1, ha0, ha1]
    split_ifs with hk0
    · rw [hzero2 hk0, zero_mul, add_zero]
      exact markov_corner_row0 q hq hq21 hgen hkm
    · rw [add_zero]
      exact markov_corner_row0 q hq hq21 hgen hkm
  · -- removable corner at the end of row 1
    have ha0 : axialDistance (1, k - 1) (0, m) = (m : ℤ) - (k : ℤ) + 2 := by
      simp only [axialDistance, cellContent]; omega
    rw [h0, ha0, if_pos hk0, hzero2 hk0, zero_mul, add_zero]
    rcases Nat.lt_or_ge k m with hkm | hkm
    · have h1 : addCellOrSelf (twoRow m k h) (1, k) = twoRow m (k + 1) (by omega) := by
        rw [addCellOrSelf_of ((isAddableCell_twoRow_iff h (1, k)).mpr
          (Or.inr (Or.inl ⟨rfl, hkm⟩))), addCell_twoRow_row1 h hkm]
      have ha1 : axialDistance (1, k - 1) (1, k) = 1 := by
        simp only [axialDistance, cellContent]; omega
      rw [if_pos hkm, h1, ha1]
      exact markov_corner_row1 q hq hq21 hgen hkm
    · have hkeq : k = m := by omega
      subst hkeq
      rw [if_neg (by omega), add_zero,
        show ((k : ℤ) - (k : ℤ) + 2 : ℤ) = 2 by omega]
      exact markov_corner_row1_diag q hq hq21 hgen k

/-- **The per-corner Markov identity at convention D, for every Young diagram.** -/
theorem ocneanuWeight_corner_identity (q : ℝ) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (ν : YoungDiagram) (r : ℕ × ℕ)
    (hr : IsCornerCell ν r) :
    ∑ s : {s : ℕ × ℕ // IsAddableCell ν s},
        ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (addCell ν s.1 s.2)
          * seminormalParam q (axialDistance r s.1)
      = (q ^ 3 / (q ^ 2 + 1)) * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν := by
  rcases Nat.eq_zero_or_pos (ν.rowLen 2) with h2 | h2
  · obtain ⟨M, K, hMK, rfl⟩ : ∃ M K, ∃ hMK : K ≤ M, ν = twoRow M K hMK :=
      ⟨ν.rowLen 0, ν.rowLen 1, YoungDiagram.rowLen_anti ν 0 1 (by omega),
        eq_twoRow_of_rowLen_two_eq_zero ν h2⟩
    exact corner_identity_twoRow q hq hq21 hgen hMK r hr
  · exact corner_identity_of_three_rows q hq21 ν h2 r

namespace SeminormalRep

/-- **The Markov condition for the Ocneanu weight at convention D, at every `n`.** -/
theorem markov_conventionD (q : ℝ) (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) {m : ℕ} (y : Hecke ℝ q q⁻¹ m) :
    ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
        ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) L.1
          * ((seminormalRep q hq0 hq2 (m + 1) L.2 (heckeIncl ℝ q q⁻¹ m y))
              * genMat q (m + 1) (by omega) L.2.ge).trace
      = (q ^ 3 / (q ^ 2 + 1)) * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
          ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1 * (seminormalRep q hq0 hq2 m ν.2 y).trace :=
  markov_of_corner_identity hq0 hq2 (ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)))
    (fun ν _ r hr => ocneanuWeight_corner_identity q hq0 hq21 hgen ν r hr) y

end SeminormalRep
end QOU.SchurWeyl
