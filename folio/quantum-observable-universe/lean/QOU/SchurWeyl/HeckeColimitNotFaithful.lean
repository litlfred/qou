/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.MarkovTraceRadical
import QOU.SchurWeyl.HeckeColimitMarkovTrace
import QOU.SchurWeyl.HeckeColimitFaithful
import QOU.SchurWeyl.OcneanuTraceNotFaithful

/-!
# `trLim` is NOT faithful — the question four docstrings flag as untouched

`HeckeColimit`, `HeckeColimitMarkovTrace`, `HeckeTowerStrict` and
`HeckeInclInjective` each record that `trLim` faithfulness is a separate question
that nothing bears on.  It is settled here, and the answer is **no**.

## The shape of the argument

Three ingredients, each already proved:

1. **One level is enough.**  `OcneanuTraceNotFaithful` exhibits a nonzero
   `x ∈ Hecke ℝ q q⁻¹ 2` invisible to `wtrace` — supported on the column shape
   `(1,1,1)`, whose Ocneanu weight vanishes at convention `D`.
2. **It stays nonzero upstairs.**  `HeckeColimitFaithful.ofLimₐ_injective` (the
   tower *inclusions* are injective — the opposite answer to the opposite
   question) sends it to a nonzero element of the colimit.
3. **Orthogonality propagates.**  `MarkovTraceRadical.mem_rad_of_exhausted` lifts
   orthogonality from one filtration stage to all of them: cyclicity turns each
   sandwich `v · g · w` inside out, Markov strips the generator, and `v · w` lands
   back in the stage below.  `TowerSpan` supplies the step and the Hecke colimit
   has it (`towerSpan_heckeColimit`).

The exhaustion `⋃_M shiftedUpTo 0 M = ⊤` is the one piece with no prior carrier;
it is `adjoin_range_σ_eq_top` transported along `gLim_eq`, which reads the
level-`m` generator `σ_i` as the colimit generator `g i`.

## Why this is not a defect in the framework

The radical is the Temperley–Lieb ideal and the form **is** nondegenerate on
`H_∞/rad ≅ TL_∞` (`QBeta.MarkovTraceQuotient.quot_pairing_nondegenerate`).  What
is refuted is faithfulness *on the Hecke tower itself*, which is the over-claim
already adjudicated as bean `qou-phlk`.  This file is the statement about the
`trLim` carrier that adjudication did not reach.

## Scope

Convention **D** (`z = q³/(q²+1)`), `ℝ`, and the four genericity hypotheses that
`wtrace` already carries — none is added.  Under the excised convention C the
three-row weight is nonzero and the verdict inverts; this is a statement about D.
-/

namespace QOU.SchurWeyl.HeckeColimitNotFaithful

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.DisjointBlockTrace
  QOU.MathlibExt.MarkovTraceRadical
open QOU.SchurWeyl QOU.SchurWeyl.Hecke QOU.SchurWeyl.HeckeInclusion
  QOU.SchurWeyl.HeckeDirectedSystem QOU.SchurWeyl.HeckeColimit
  QOU.SchurWeyl.HeckeColimitMarkovTrace QOU.SchurWeyl.SeminormalRep

variable (q : ℝ) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
  (hq21 : q ^ 2 + 1 ≠ 0) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1)

include hq0 hq2 hq21 hgen

/-- **The filtration stages exhaust the colimit.**

Every element sits at some level `m`, `adjoin_range_σ_eq_top` writes it in the
level-`m` generators, and `gLim_eq` reads each of those as a colimit generator
`g i` with `i < m`.  The `max` keeps the stage above any prescribed `M₀`. -/
theorem exists_mem_shiftedUpTo (M₀ : ℕ) (c : HeckeLim ℝ q q⁻¹) :
    ∃ M : ℕ, M₀ ≤ M ∧
      c ∈ shiftedUpTo (heckeColimitMarkovTrace q hq0 hq2 hq21 hgen) 0 M := by
  obtain ⟨m, y, rfl⟩ : ∃ (m : ℕ) (y : Hecke ℝ q q⁻¹ m), ofLimₐ ℝ q q⁻¹ m y = c := by
    induction c using DirectLimit.induction (f := heckeF ℝ q q⁻¹) with
    | _ i x => exact ⟨i, x, rfl⟩
  refine ⟨max M₀ m, le_max_left _ _, ?_⟩
  have hz : y ∈ Algebra.adjoin ℝ (Set.range (σ ℝ q q⁻¹ m)) := by
    rw [adjoin_range_σ_eq_top]; exact Algebra.mem_top
  induction hz using Algebra.adjoin_induction with
  | mem x hx =>
      obtain ⟨i, rfl⟩ := hx
      rw [← gLim_eq ℝ q q⁻¹ i.val m i.isLt]
      exact Algebra.subset_adjoin
        ⟨i.val, Nat.zero_le _, le_trans (le_of_lt i.isLt) (le_max_right _ _), Or.inl rfl⟩
  | algebraMap r => rw [AlgHom.commutes]; exact Subalgebra.algebraMap_mem _ r
  | add x y _ _ hx hy => rw [map_add]; exact Subalgebra.add_mem _ hx hy
  | mul x y _ _ hx hy => rw [map_mul]; exact Subalgebra.mul_mem _ hx hy

/-- **The Ocneanu trace on the colimit has a nonzero radical.**

A nonzero element of `H_∞(q)` that `trLim` cannot see, however it is paired. -/
theorem exists_nonzero_trLim_orthogonal :
    ∃ a : HeckeLim ℝ q q⁻¹, a ≠ 0 ∧
      ∀ c : HeckeLim ℝ q q⁻¹, trLim q hq0 hq2 hq21 hgen (a * c) = 0 := by
  obtain ⟨x, hx0, hxorth⟩ :=
    OcneanuTraceNotFaithful.exists_nonzero_wtrace_orthogonal q hq0 hq2 hq21
  haveI : TowerSpan (heckeColimitMarkovTrace q hq0 hq2 hq21 hgen) :=
    towerSpan_heckeColimit q hq0 hq2 hq21 hgen
  refine ⟨ofLimₐ ℝ q q⁻¹ 2 x, ?_, ?_⟩
  · intro h
    exact hx0 (ofLimₐ_injective hq0 hq2 2 (by rw [h, map_zero]))
  · have hrad : ofLimₐ ℝ q q⁻¹ 2 x ∈
        rad (heckeColimitMarkovTrace q hq0 hq2 hq21 hgen) := by
      refine mem_rad_of_exhausted (heckeColimitMarkovTrace q hq0 hq2 hq21 hgen)
        _ 2 (ofLim_mem_H ℝ q q⁻¹ 2 x) 1 le_rfl ?_
        (exists_mem_shiftedUpTo q hq0 hq2 hq21 hgen 1)
      intro b hb
      obtain ⟨y, rfl⟩ := shiftedUpTo_le _ 0 1 hb
      show trLim q hq0 hq2 hq21 hgen
          (ofLimₐ ℝ q q⁻¹ 2 x * ofLimₐ ℝ q q⁻¹ 2 y) = 0
      rw [← map_mul, trLim_ofLim]
      exact hxorth y
    exact hrad

/-- **`trLim` is not faithful.** -/
theorem not_isFaithful_trLim :
    ¬ IsFaithful (heckeColimitMarkovTrace q hq0 hq2 hq21 hgen) := by
  obtain ⟨a, ha0, haorth⟩ := exists_nonzero_trLim_orthogonal q hq0 hq2 hq21 hgen
  exact not_isFaithful _ (a := a) haorth ha0

end QOU.SchurWeyl.HeckeColimitNotFaithful
