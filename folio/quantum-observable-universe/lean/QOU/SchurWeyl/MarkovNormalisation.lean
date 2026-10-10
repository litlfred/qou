import QOU.SchurWeyl.MarkovConventionD
import QOU.Mathlib.StandardYoungTableauBot

/-!
# QOU.SchurWeyl.MarkovNormalisation — the second defining property, at every n

`MarkovConventionD` proves the Markov property `tr(x·σ_n) = z·tr(x)`.  "These are the Ocneanu
weights" is **two** properties; this file proves the other one, the normalisation `tr(1) = 1`:

```
∑_{|λ| = n} f^λ · W_λ = 1        for every n,  W = ocneanuWeight q z_D
```

(`tr(1) = ∑_λ W_λ · tr(ρ_λ(1)) = ∑_λ W_λ · dim V_λ`, and `dim V_λ = f^λ` is the number of standard
tableaux.)

## The proof is the same exchange, run without the Hoefsmit factor

`MarkovAssembly`'s reindexing does all the work again:

* `ocneanuWeight_addable_sum` — for **every** diagram, `∑_{s addable} W_{ν+s} = W_ν`.  Same case
  split as the corner identity: ≥3 rows makes both sides `0`, and on a `twoRow` the `(2,0)` cell
  drops out, leaving `ocneanuWeight_twoRow_branching`.
* `sum_dim_weight_succ` — `∑_{|λ|=n+1} f^λ W_λ = ∑_{|ν|=n} f^ν W_ν`, by expanding `f^λ` through
  `numStandardYoungTableaux_branching` and reindexing `(λ, corner) ↔ (ν, addable)`.
* `sum_dim_weight_zero` — the base case: the only diagram of size `0` is `⊥`, with `f = 1`
  (`numStandardYoungTableaux_bot`, already in the corpus) and `W = 1` (an empty product over an
  empty product).

So the sum is *constant in `n`*, and equal to its value at `n = 0`.

## Relation to the existing normalisation lemmas

`OcneanuWeightMarkov3.ocneanuWeight_normalisation_three` / `_four` prove the same identity at
`n = 3, 4` for **arbitrary** `z`.  This file is the complement, not a replacement: all `n`, but
convention D only.  Neither subsumes the other.

## What is now proved, and what is not

Both defining properties of the Ocneanu/Markov weight hold, at convention D, at every `n`, in
Lean.  **Uniqueness is not proved** — that a Markov trace with a given `z` is the *only* one — so
"these are *the* Ocneanu weights" still rests on that standard argument.  For the downstream mass
channel, which needs a Markov trace rather than the uniqueness of one, the two properties are what
is used; but the uniqueness step should not be described as discharged.

## Base ring (§7c)

`ℝ`, inherited from the convention-D chain.

LaTeX label: `thm:markov-normalisation`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib YoungDiagram

variable {m k : ℕ}

/-- **Weight branching, for every diagram.**  The weights of the diagrams obtained by adding one
addable cell sum to the weight of the diagram itself. -/
theorem ocneanuWeight_addable_sum (q : ℝ) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (ν : YoungDiagram) :
    ∑ s : {s : ℕ × ℕ // IsAddableCell ν s},
        ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (addCell ν s.1 s.2)
      = ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν := by
  classical
  rcases Nat.eq_zero_or_pos (ν.rowLen 2) with h2 | h2
  · obtain ⟨M, K, hMK, rfl⟩ : ∃ M K, ∃ hMK : K ≤ M, ν = twoRow M K hMK :=
      ⟨ν.rowLen 0, ν.rowLen 1, YoungDiagram.rowLen_anti ν 0 1 (by omega),
        eq_twoRow_of_rowLen_two_eq_zero ν h2⟩
    have hcell : ∑ s : {s : ℕ × ℕ // IsAddableCell (twoRow M K hMK) s},
        ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (addCell (twoRow M K hMK) s.1 s.2)
        = ∑ s : {s : ℕ × ℕ // IsAddableCell (twoRow M K hMK) s},
            (fun c => ocneanuWeight q (q ^ 3 / (q ^ 2 + 1))
              (addCellOrSelf (twoRow M K hMK) c)) s.1 :=
      Finset.sum_congr rfl fun s _ => by rw [← addCellOrSelf_of s.2]
    rw [hcell, sum_addable_twoRow hMK (fun c => ocneanuWeight q (q ^ 3 / (q ^ 2 + 1))
        (addCellOrSelf (twoRow M K hMK) c)), sum_addableTwoRow_expand]
    have h0 : addCellOrSelf (twoRow M K hMK) (0, M) = twoRow (M + 1) K (by omega) := by
      rw [addCellOrSelf_of ((isAddableCell_twoRow_iff hMK (0, M)).mpr (Or.inl rfl)),
        addCell_twoRow_row0]
    have hzero2 : ∀ hk0 : 0 < K,
        ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (addCellOrSelf (twoRow M K hMK) (2, 0)) = 0 := by
      intro hk0
      have hadd : IsAddableCell (twoRow M K hMK) (2, 0) :=
        (isAddableCell_twoRow_iff hMK (2, 0)).mpr (Or.inr (Or.inr ⟨rfl, hk0⟩))
      rw [addCellOrSelf_of hadd]
      exact ocneanuWeight_conventionD_eq_zero_of_three_rows q hq21 _
        (rowLen_two_addCell_row2 hMK hadd)
    rw [h0]
    rcases Nat.lt_or_ge K M with hkm | hkm
    · have h1 : addCellOrSelf (twoRow M K hMK) (1, K) = twoRow M (K + 1) (by omega) := by
        rw [addCellOrSelf_of ((isAddableCell_twoRow_iff hMK (1, K)).mpr
          (Or.inr (Or.inl ⟨rfl, hkm⟩))), addCell_twoRow_row1 hMK hkm]
      rw [if_pos hkm, h1]
      split_ifs with hk0
      · rw [hzero2 hk0, add_zero]
        exact (ocneanuWeight_twoRow_branching q hq hq21 hgen hkm).symm
      · rw [add_zero]
        exact (ocneanuWeight_twoRow_branching q hq hq21 hgen hkm).symm
    · have hkeq : K = M := by omega
      subst hkeq
      rw [if_neg (by omega), add_zero]
      split_ifs with hk0
      · rw [hzero2 hk0, add_zero]
        exact (ocneanuWeight_twoRow_branching_diag q hq hq21 hgen K).symm
      · rw [add_zero]
        exact (ocneanuWeight_twoRow_branching_diag q hq hq21 hgen K).symm
  · rw [ocneanuWeight_conventionD_eq_zero_of_three_rows q hq21 ν h2]
    refine Finset.sum_eq_zero fun s _ => ?_
    exact ocneanuWeight_conventionD_eq_zero_of_three_rows q hq21 _
      (rowLen_two_pos_addCell s.2 h2)

/-- **The weighted dimension sum does not depend on `n`.** -/
theorem sum_dim_weight_succ (q : ℝ) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (n : ℕ) :
    ∑ L : {ρ : YoungDiagram // ρ.cells.card = n + 1},
        (numStandardYoungTableaux L.1 : ℝ) * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) L.1
      = ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          (numStandardYoungTableaux ν.1 : ℝ) * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1 := by
  classical
  set F : {ν : YoungDiagram // ν.cells.card = n} → (ℕ × ℕ) → ℝ :=
    fun ν c => (numStandardYoungTableaux ν.1 : ℝ)
      * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (addCellOrSelf ν.1 c) with hF
  have step : ∀ L : {ρ : YoungDiagram // ρ.cells.card = n + 1},
      (numStandardYoungTableaux L.1 : ℝ) * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) L.1
        = ∑ c : {c : ℕ × ℕ // IsCornerCell L.1 c},
            F ⟨eraseCorner L.1 c.1 c.2, by
              have := card_eraseCorner L.1 c.1 c.2
              have := L.2
              omega⟩ c.1 := by
    intro L
    have hpos : 0 < L.1.cells.card := by rw [L.2]; omega
    rw [numStandardYoungTableaux_branching hpos, Nat.cast_sum, Finset.sum_mul]
    refine Finset.sum_congr rfl fun c _ => ?_
    rw [hF]
    have hadd : addCellOrSelf (eraseCorner L.1 c.1 c.2) c.1 = L.1 := by
      rw [addCellOrSelf_of (isAddableCell_eraseCorner c.1 c.2), addCell_eraseCorner]
    simp only [hadd]
  calc ∑ L : {ρ : YoungDiagram // ρ.cells.card = n + 1},
        (numStandardYoungTableaux L.1 : ℝ) * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) L.1
      = ∑ L : {ρ : YoungDiagram // ρ.cells.card = n + 1},
          ∑ c : {c : ℕ × ℕ // IsCornerCell L.1 c},
            F ⟨eraseCorner L.1 c.1 c.2, by
              have := card_eraseCorner L.1 c.1 c.2
              have := L.2
              omega⟩ c.1 := Finset.sum_congr rfl fun L _ => step L
    _ = ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          ∑ s : {s : ℕ × ℕ // IsAddableCell ν.1 s}, F ν s.1 :=
        sum_corner_eq_sum_addable n F
    _ = ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          (numStandardYoungTableaux ν.1 : ℝ) * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1 := by
        refine Finset.sum_congr rfl fun ν _ => ?_
        rw [hF]
        simp only
        rw [← Finset.mul_sum, ← ocneanuWeight_addable_sum q hq hq21 hgen ν.1]
        congr 1
        exact Finset.sum_congr rfl fun s _ => by rw [addCellOrSelf_of s.2]

theorem eq_bot_of_card_zero (ν : YoungDiagram) (h : ν.cells.card = 0) : ν = ⊥ := by
  have hc : ν.cells = ∅ := Finset.card_eq_zero.mp h
  ext c
  rw [hc]
  simp [YoungDiagram.cells_bot]

theorem ocneanuWeight_bot (q z : ℝ) : ocneanuWeight q z (⊥ : YoungDiagram) = 1 := by
  simp [ocneanuWeight, YoungDiagram.cells_bot]

theorem sum_dim_weight_zero (q z : ℝ) :
    ∑ ν : {ν : YoungDiagram // ν.cells.card = 0},
        (numStandardYoungTableaux ν.1 : ℝ) * ocneanuWeight q z ν.1 = 1 := by
  have hb : (⊥ : YoungDiagram).cells.card = 0 := by rw [YoungDiagram.cells_bot]; rfl
  rw [Fintype.sum_eq_single (⟨⊥, hb⟩ : {ν : YoungDiagram // ν.cells.card = 0})
    (fun x hx => absurd (Subtype.ext (eq_bot_of_card_zero x.1 x.2)) hx)]
  rw [ocneanuWeight_bot, numStandardYoungTableaux_bot]
  norm_num

/-- **The normalisation, at every `n`.** -/
theorem sum_dim_weight_eq_one (q : ℝ) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (n : ℕ) :
    ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
        (numStandardYoungTableaux ν.1 : ℝ) * ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν.1 = 1 := by
  induction n with
  | zero => exact sum_dim_weight_zero q _
  | succ n ih => rw [sum_dim_weight_succ q hq hq21 hgen n]; exact ih

end QOU.SchurWeyl
