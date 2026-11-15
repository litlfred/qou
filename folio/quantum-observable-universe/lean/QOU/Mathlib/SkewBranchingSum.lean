import QOU.Mathlib.SkewSYTBranchingBijection
import QOU.Mathlib.YoungLatticeCornerCount

/-!
# `QOU.Mathlib.SkewBranchingSum` — the classical branching sum `∑_λ f^λ f^{λ/μ}`

With the skew branching rule in hand (`SkewSYTBranchingBijection`) and the up-operator identity
already proved (`QOU.Mathlib.upSum_eq`), the classical identity

    ∑_{λ ⊢ k}  f^λ · f^{λ/μ}  =  (k! / |μ|!) · f^μ        (k ≥ |μ|)

falls out by a one-step induction on `k`.  Stated divisor-free as

    |μ|! · G(μ, k)  =  k! · f^μ.

## The argument

Write `G(μ, k) = ∑_{λ of size k} f^λ · f^{λ/μ}`.  Then

* **Base** `G(μ, |μ|) = f^μ`: the only diagram of size `|μ|` containing `μ` is `μ` itself, and
  `f^{μ/μ} = 1` (`fDimSkew_self` — the skew region is empty, so the tableau is the empty
  filling and nothing else).
* **Step** `G(μ, k+1) = (k+1) · G(μ, k)` for `k ≥ |μ|`: expand `f^{λ/μ}` by skew branching,
  reindex the resulting `(λ, corner)` pairs as `(ν, addable cell)` pairs by `rankExchange`, and
  collapse the inner sum with `upSum_eq`.

## Two places where the bookkeeping would go wrong if done naively

* **The corner sum must run over ALL corners of `λ`, not only those outside `μ`.**  A corner
  `c ∈ μ` contributes `f^{(λ∖c)/μ} = 0`, since `λ ∖ c` no longer contains `μ` — so widening the
  index is free, and it is what lets `rankExchange` apply unchanged.  That is
  `fDimSkew_branching_corners`.
* **Dually, the addable sum must run over ALL addable cells of `ν`.**  It looks like it should
  be restricted to cells outside `μ`, but the restriction is vacuous: if `μ ≤ ν` then no cell
  addable to `ν` can lie in `μ` (it would already be in `ν`), and if `μ ⊄ ν` the whole term
  carries the factor `f^{ν/μ} = 0`.  So the inner sum is exactly `upSum ν`, with nothing to
  strip.

Pure combinatorics; nothing archimedean (§7c); no fit.

## References

- [stanley1999ec2] Enumerative Combinatorics I, §7.10
- [leitner2026] bean `qou-b21r`
-/

namespace QOU.BraidKnot.YoungTableauStandard

open Finset QOU.Mathlib YoungDiagram

variable {outer inner μ : YoungDiagram} {c : ℕ × ℕ}

/-! ### `f^{μ/μ} = 1` -/

/-- The empty filling of the empty skew shape `μ/μ`. -/
def skewSelfTableau (μ : YoungDiagram) : SkewStandardYoungTableau μ μ where
  entry := fun _ _ => 0
  row_strict := by
    intro i j₁ j₂ hlt hj₂ hj₁
    exact absurd (μ.up_left_mem le_rfl (le_of_lt hlt) hj₂) hj₁
  col_strict := by
    intro i₁ i₂ j hlt hi₂ hi₁
    exact absurd (μ.up_left_mem (le_of_lt hlt) le_rfl hi₂) hi₁
  zeros := by intro i j _; rfl
  content := by simp

/-- **`f^{μ/μ} = 1`.**  The skew region is empty, so `zeros` forces every entry and the filling
above is the only one. -/
theorem fDimSkew_self (μ : YoungDiagram) : fDimSkew μ μ = 1 := by
  rw [fDimSkew_of_le le_rfl]
  have : Unique (SkewStandardYoungTableau μ μ) := by
    refine ⟨⟨skewSelfTableau μ⟩, fun T => ?_⟩
    refine skew_entry_ext (fun c hc => ?_)
    simp only [skewCellsOf, Finset.mem_sdiff] at hc
    exact absurd hc.1 hc.2
  exact Nat.card_eq_one_iff_unique.mpr ⟨inferInstance, inferInstance⟩

/-- Deleting a corner shrinks the diagram. -/
theorem eraseCorner_le (outer : YoungDiagram) (c : ℕ × ℕ) (hc : IsCornerCell outer c) :
    eraseCorner outer c hc ≤ outer := by
  intro x hx
  rw [YoungDiagram.mem_cells] at hx ⊢
  exact ((mem_eraseCorner outer c hc x).mp hx).1

/-- A corner inside `inner` contributes nothing: deleting it breaks the containment. -/
theorem fDimSkew_eraseCorner_eq_zero_of_mem (hc : IsCornerCell outer c) (hcm : c ∈ inner) :
    fDimSkew (eraseCorner outer c hc) inner = 0 := by
  refine fDimSkew_of_not_le (fun h => ?_)
  have hmem : c ∈ eraseCorner outer c hc := h hcm
  exact ((mem_eraseCorner outer c hc c).mp hmem).2 rfl

/-- **Skew branching over ALL corners.**  The corners lying inside `inner` contribute `0`, so
the restricted sum of `fDimSkew_branching` may be widened to the full corner subtype — which is
the index `rankExchange` speaks about. -/
theorem fDimSkew_branching_corners (outer inner : YoungDiagram)
    (hcard : inner.cells.card < outer.cells.card) :
    fDimSkew outer inner
      = ∑ c : {c : ℕ × ℕ // IsCornerCell outer c}, fDimSkew (eraseCorner outer c.1 c.2) inner := by
  classical
  by_cases hle : inner ≤ outer
  · have hpos : 0 < (skewCellsOf outer inner).card := by
      have hc : (skewCellsOf outer inner).card = outer.cells.card - inner.cells.card := by
        show (outer.cells \ inner.cells).card = _
        rw [Finset.card_sdiff,
          Finset.inter_eq_left.mpr (YoungDiagram.cells_subset_iff.mpr hle)]
      omega
    rw [fDimSkew_branching hle hpos]
    -- widen `{c // corner ∧ c ∉ inner}` to `{c // corner}`
    have step₁ : ∑ c : {c : ℕ × ℕ // IsCornerCell outer c ∧ c ∉ inner},
          fDimSkew (eraseCorner outer c.1 c.2.1) inner
        = ∑ x : {x : {c : ℕ × ℕ // IsCornerCell outer c} // x.1 ∉ inner},
            fDimSkew (eraseCorner outer x.1.1 x.1.2) inner :=
      (Fintype.sum_equiv
        (Equiv.subtypeSubtypeEquivSubtypeInter (IsCornerCell outer) (fun c => c ∉ inner))
        (fun x : {x : {c : ℕ × ℕ // IsCornerCell outer c} // x.1 ∉ inner} =>
          fDimSkew (eraseCorner outer x.1.1 x.1.2) inner)
        (fun c : {c : ℕ × ℕ // IsCornerCell outer c ∧ c ∉ inner} =>
          fDimSkew (eraseCorner outer c.1 c.2.1) inner)
        (fun _ => rfl)).symm
    rw [step₁,
      ← Finset.sum_subtype
        (Finset.univ.filter (fun x : {c : ℕ × ℕ // IsCornerCell outer c} => x.1 ∉ inner))
        (fun x => by simp)
        (fun x : {c : ℕ × ℕ // IsCornerCell outer c} =>
          fDimSkew (eraseCorner outer x.1 x.2) inner)]
    refine Finset.sum_filter_of_ne (fun x _ hne => ?_)
    by_contra hin
    exact hne (fDimSkew_eraseCorner_eq_zero_of_mem x.2 hin)
  · rw [fDimSkew_of_not_le hle]
    symm
    refine Finset.sum_eq_zero (fun x _ => ?_)
    exact fDimSkew_of_not_le (fun h => hle (le_trans h (eraseCorner_le outer x.1 x.2)))

/-! ### The branching sum -/

/-- `G(μ, k) = ∑_{λ of size k} f^λ · f^{λ/μ}`. -/
noncomputable def skewPair (μ : YoungDiagram) (k : ℕ) : ℕ :=
  ∑ ν : {ν : YoungDiagram // ν.cells.card = k}, numStandardYoungTableaux ν.1 * fDimSkew ν.1 μ

/-- **The base case.**  At `k = |μ|` the only diagram containing `μ` is `μ` itself. -/
theorem skewPair_card (μ : YoungDiagram) :
    skewPair μ μ.cells.card = numStandardYoungTableaux μ := by
  classical
  unfold skewPair
  rw [Finset.sum_eq_single (⟨μ, rfl⟩ : {ν : YoungDiagram // ν.cells.card = μ.cells.card})]
  · rw [fDimSkew_self, mul_one]
  · intro ν _ hne
    have hnle : ¬ (μ ≤ ν.1) := by
      intro hle
      refine hne (Subtype.ext ?_)
      refine YoungDiagram.ext ?_
      exact (Finset.eq_of_subset_of_card_le (YoungDiagram.cells_subset_iff.mpr hle)
        (by rw [ν.2])).symm
    rw [fDimSkew_of_not_le hnle, mul_zero]
  · intro h; exact absurd (Finset.mem_univ _) h

set_option maxHeartbeats 4000000 in
/-- **The step.**  For `k ≥ |μ|`, `G(μ, k+1) = (k+1)·G(μ, k)`.

Expand `f^{λ/μ}` by `fDimSkew_branching_corners`, reindex the `(λ, corner)` pairs as
`(ν, addable cell)` pairs by `rankExchange` (which sends `(λ, c)` to `(λ ∖ c, c)`), and collapse
the resulting inner sum with `upSum_eq`. -/
theorem skewPair_succ (μ : YoungDiagram) (k : ℕ) (hk : μ.cells.card ≤ k) :
    skewPair μ (k + 1) = (k + 1) * skewPair μ k := by
  classical
  have hbranch : ∀ LL : {LL : YoungDiagram // LL.cells.card = k + 1},
      numStandardYoungTableaux LL.1 * fDimSkew LL.1 μ
        = ∑ c : {c : ℕ × ℕ // IsCornerCell LL.1 c},
            numStandardYoungTableaux LL.1 * fDimSkew (eraseCorner LL.1 c.1 c.2) μ := by
    intro LL
    rw [← Finset.mul_sum, ← fDimSkew_branching_corners LL.1 μ (by rw [LL.2]; omega)]
  calc skewPair μ (k + 1)
      = ∑ LL : {LL : YoungDiagram // LL.cells.card = k + 1},
          ∑ c : {c : ℕ × ℕ // IsCornerCell LL.1 c},
            numStandardYoungTableaux LL.1 * fDimSkew (eraseCorner LL.1 c.1 c.2) μ :=
        Finset.sum_congr rfl fun LL _ => hbranch LL
    _ = ∑ x : (Σ LL : {LL : YoungDiagram // LL.cells.card = k + 1},
                {c : ℕ × ℕ // IsCornerCell LL.1 c}),
          numStandardYoungTableaux x.1.1 * fDimSkew (eraseCorner x.1.1 x.2.1 x.2.2) μ :=
        (Fintype.sum_sigma
          (fun x : (Σ LL : {LL : YoungDiagram // LL.cells.card = k + 1},
                     {c : ℕ × ℕ // IsCornerCell LL.1 c}) =>
            numStandardYoungTableaux x.1.1 * fDimSkew (eraseCorner x.1.1 x.2.1 x.2.2) μ)).symm
    _ = ∑ y : (Σ ν : {ν : YoungDiagram // ν.cells.card = k},
                {s : ℕ × ℕ // IsAddableCell ν.1 s}),
          numStandardYoungTableaux (addCell y.1.1 y.2.1 y.2.2) * fDimSkew y.1.1 μ := by
        refine Fintype.sum_equiv (rankExchange k) _ _ ?_
        rintro ⟨⟨L, hL⟩, ⟨c, hc⟩⟩
        show numStandardYoungTableaux L * fDimSkew (eraseCorner L c hc) μ
          = numStandardYoungTableaux
              (addCell (eraseCorner L c hc) c (isAddableCell_eraseCorner c hc))
            * fDimSkew (eraseCorner L c hc) μ
        rw [addCell_eraseCorner]
    _ = ∑ ν : {ν : YoungDiagram // ν.cells.card = k},
          ∑ s : {s : ℕ × ℕ // IsAddableCell ν.1 s},
            numStandardYoungTableaux (addCell ν.1 s.1 s.2) * fDimSkew ν.1 μ :=
        Fintype.sum_sigma
          (fun y : (Σ ν : {ν : YoungDiagram // ν.cells.card = k},
                     {s : ℕ × ℕ // IsAddableCell ν.1 s}) =>
            numStandardYoungTableaux (addCell y.1.1 y.2.1 y.2.2) * fDimSkew y.1.1 μ)
    _ = ∑ ν : {ν : YoungDiagram // ν.cells.card = k}, (k + 1) *
          (numStandardYoungTableaux ν.1 * fDimSkew ν.1 μ) := by
        refine Finset.sum_congr rfl fun ν _ => ?_
        rw [← Finset.sum_mul, sum_subtype_addable_eq_upSum, upSum_eq k ν.1 ν.2, mul_assoc]
    _ = (k + 1) * skewPair μ k := (Finset.mul_sum _ _ _).symm

/-- **The classical branching sum, divisor-free.**

    |μ|! · ∑_{λ of size |μ|+d}  f^λ · f^{λ/μ}  =  (|μ|+d)! · f^μ. -/
theorem factorial_mul_skewPair (μ : YoungDiagram) : ∀ d : ℕ,
    Nat.factorial μ.cells.card * skewPair μ (μ.cells.card + d)
      = Nat.factorial (μ.cells.card + d) * numStandardYoungTableaux μ := by
  intro d
  induction d with
  | zero => rw [Nat.add_zero, skewPair_card]
  | succ d ih =>
    have hstep : skewPair μ (μ.cells.card + d + 1)
        = (μ.cells.card + d + 1) * skewPair μ (μ.cells.card + d) :=
      skewPair_succ μ (μ.cells.card + d) (by omega)
    calc Nat.factorial μ.cells.card * skewPair μ (μ.cells.card + (d + 1))
        = (μ.cells.card + d + 1) *
            (Nat.factorial μ.cells.card * skewPair μ (μ.cells.card + d)) := by
          rw [show μ.cells.card + (d + 1) = μ.cells.card + d + 1 from rfl, hstep]; ring
      _ = (μ.cells.card + d + 1) *
            (Nat.factorial (μ.cells.card + d) * numStandardYoungTableaux μ) := by rw [ih]
      _ = Nat.factorial (μ.cells.card + (d + 1)) * numStandardYoungTableaux μ := by
          rw [show μ.cells.card + (d + 1) = (μ.cells.card + d) + 1 from rfl,
            Nat.factorial_succ]
          ring

/-- The same, indexed by the target size rather than by the increment. -/
theorem factorial_mul_skewPair_of_le (μ : YoungDiagram) (k : ℕ) (hk : μ.cells.card ≤ k) :
    Nat.factorial μ.cells.card * skewPair μ k
      = Nat.factorial k * numStandardYoungTableaux μ := by
  obtain ⟨d, rfl⟩ : ∃ d, k = μ.cells.card + d := ⟨k - μ.cells.card, by omega⟩
  exact factorial_mul_skewPair μ d

end QOU.BraidKnot.YoungTableauStandard
