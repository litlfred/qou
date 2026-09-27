/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.MarkovTraceInstance
import QOU.SchurWeyl.HeckeProductInjective
import QOU.SchurWeyl.OcneanuWeight
import QOU.Mathlib.SchenstedPartitionShape
import QOU.Mathlib.NumSYTPos
import QOU.MathlibExt.WenzlSchurElementBridge

/-!
# The Ocneanu trace is NOT faithful on `H_n(q)` — at the carrier, not in the abstract

The corpus already holds every ingredient of this statement, sorry-free on `main`,
and had never composed them at the carrier the tower results actually use.  What
was missing is assembled here: a single element of `Hecke ℝ q q⁻¹ 2 = H_3(q)`
that is nonzero and that the trace form `⟨x, b⟩ = wtrace (x * b)` cannot see.

## Why this is an assembly and not a derivation

Two facts do all the work, and both are on `main`:

* `wtrace` is **defined** as the Frobenius sum `Σ_ν y_ν · tr ρ_ν`
  (`SeminormalRep.wtrace`, `wtrace_apply` is `rfl`) — so no character-theoretic
  decomposition has to be proved here.
* `ocneanuWeight_conventionD_eq_zero_of_three_rows` says the weight `y_ν`
  **vanishes** at convention `D` for every shape with a third row, unconditionally
  over any field with `q² + 1 ≠ 0`.

So the trace form factors through the blocks with at most two rows, and anything
supported on a three-row block is invisible to it.  `heckeProduct_surjective`
(Wedderburn) produces such an element and `heckeProduct_injective` shows it is
nonzero.

## Scope — this is a structural exclusion, and the invariant is named

Per AGENTS.md §"Before declaring refuted", this is scope **(b)**: not "this
construction alone did not work", but "the form provably annihilates a nonzero
element".  The invariant is the **weight vanishing** above.  It is a statement
about **convention D** (`z = q³/(q²+1)`, canonical per the owner ruling of
2026-08-15) and inverts under the excised convention C, where the three-row
weight is nonzero and the form is nondegenerate.

## What this does NOT say

* It does not say the framework loses anything.  The radical is the
  Temperley–Lieb ideal, and the form **is** nondegenerate on the quotient
  `H_n/rad ≅ TL_n` (`QBeta.MarkovTraceQuotient.quot_pairing_nondegenerate`).
  This file supplies the negative half at the `wtrace` carrier; that file
  supplies the positive half abstractly.
* It does not identify the radical.  That the radical is *exactly* the
  `ℓ(λ) ≥ 3` blocks, of dimension `n! − Catalan n`, is `QBeta.MarkovGramDegenerate`.
  Here only one direction is needed and only one element is exhibited.
* It says nothing about `heckeIncl` or `ofLim` injectivity, which is a different
  question about the tower *inclusions* and is proved affirmatively in
  `HeckeInclInjective` / `HeckeColimitFaithful`.  "Faithful" is a homonym in this
  corpus and these two answers point opposite ways.
-/

namespace QOU.SchurWeyl.OcneanuTraceNotFaithful

open YoungDiagram QOU.Mathlib QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep

/-! ## A shape with three rows -/

/-- The column shape `(1,1,1)` — three cells in three rows, the smallest shape
whose Ocneanu weight vanishes at convention `D`. -/
def colThree : YoungDiagram := YoungDiagram.ofRowLens [1, 1, 1] (by decide)

theorem colThree_card : colThree.cells.card = 3 := by decide

theorem colThree_rowLen_two : 0 < colThree.rowLen 2 := by
  rw [colThree, QOU.MathlibExt.WenzlSchurElementBridge.rowLen_ofRowLens_getD]
  norm_num

/-- **The weight vanishes on the column shape.**  This is the invariant the
scope-(b) exclusion rests on. -/
theorem ocneanuWeight_colThree {q : ℝ} (hq21 : q ^ 2 + 1 ≠ 0) :
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) colThree = 0 :=
  ocneanuWeight_conventionD_eq_zero_of_three_rows q hq21 colThree colThree_rowLen_two

/-! ## The invisible element -/

/-- **The Ocneanu trace form on `H_3(q)` is degenerate.**

There is a nonzero `x ∈ Hecke ℝ q q⁻¹ 2` with `wtrace (x * b) = 0` for *every*
`b` — so the form `⟨x, b⟩ = wtrace (x * b)` has nonzero radical and `wtrace` is
not faithful.

`x` is the Wedderburn preimage of the tuple that is the identity on the
three-row block and zero on the other two.  Nonzero because `heckeProduct` is
injective; invisible because the three-row weight is zero and every other block
kills it. -/
theorem exists_nonzero_wtrace_orthogonal (q : ℝ) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0) :
    ∃ x : Hecke ℝ q q⁻¹ 2, x ≠ 0 ∧ ∀ b : Hecke ℝ q q⁻¹ 2, wtrace q hq0 hq2 2 (x * b) = 0 := by
  classical
  obtain ⟨lam₀, hlam₀⟩ := exists_partitionShape_eq (n := 3) colThree colThree_card
  obtain ⟨x, hx⟩ := heckeProduct_surjective q hq0 hq2 2
    (Function.update 0 lam₀ (1 : Matrix (StandardYoungTableau (partitionShape lam₀))
      (StandardYoungTableau (partitionShape lam₀)) ℝ))
  refine ⟨x, ?_, ?_⟩
  · -- nonzero: the tuple is the identity on block `lam₀`, and that block is nonempty
    intro h0
    rw [h0, map_zero] at hx
    have hlam := congrFun hx lam₀
    rw [Function.update_self] at hlam
    obtain ⟨T⟩ : Nonempty (StandardYoungTableau (partitionShape lam₀)) := inferInstance
    have hentry : (0 : Matrix (StandardYoungTableau (partitionShape lam₀))
        (StandardYoungTableau (partitionShape lam₀)) ℝ) T T
        = (1 : Matrix (StandardYoungTableau (partitionShape lam₀))
        (StandardYoungTableau (partitionShape lam₀)) ℝ) T T := by
      rw [← hlam]; rfl
    rw [Matrix.zero_apply, Matrix.one_apply_eq] at hentry
    exact zero_ne_one hentry
  · -- invisible: every summand of the Frobenius sum vanishes
    intro b
    rw [wtrace_apply]
    refine Finset.sum_eq_zero ?_
    rintro ⟨d, hd⟩ -
    obtain ⟨lam, rfl⟩ := exists_partitionShape_eq (n := 3) d hd
    by_cases hl : lam = lam₀
    · -- the weight is zero: this block has three rows
      subst hl
      have hw : ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (partitionShape lam) = 0 := by
        rw [hlam₀]; exact ocneanuWeight_colThree hq21
      rw [hw, zero_mul]
    · -- the block kills `x`, hence kills `x * b`
      have hxz : seminormalRep q hq0 hq2 2 hd x = 0 := by
        have h := congrFun hx lam
        rw [Function.update_of_ne hl] at h
        exact h.trans rfl
      have hxb : seminormalRep q hq0 hq2 2 hd (x * b) = 0 := by
        rw [map_mul, hxz, zero_mul]
      rw [hxb, Matrix.trace_zero, mul_zero]

end QOU.SchurWeyl.OcneanuTraceNotFaithful
