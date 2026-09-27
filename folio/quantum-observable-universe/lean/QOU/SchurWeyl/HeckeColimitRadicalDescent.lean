/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.HeckeColimitNotFaithful

/-!
# Radical descent on the Hecke colimit, with no conditional expectation

`QBeta.TLTowerRadicalDescent` (brick 3 of `qou-s7z2`) relates the radicals at
consecutive ranks — **conditionally** on `HeckeConditionalExpectation`, an open
§3b class with no instance.  Its forward direction, `map_mem_traceRadical`, does
not need it.

## What is narrowed

Brick 3's file argues that a bare inclusion cannot do better:

> A bare inclusion `ι : Hn →ₐ Hn1` says nothing about the two radicals:
> membership in `rad τn1` quantifies over all of `Hn1`, not over `ι '' Hn`, so no
> amount of compatibility between `τn` and `τn1` *on the subalgebra* constrains
> it.

Correct about a bare inclusion; **too strong about a tower.**  A test element of
the next stage is not arbitrary — `TowerSpan` says each stage is spanned by the
previous one together with single sandwiches `v * g * w` — so cyclicity moves the
outer factor to the front, Markov strips the generator, and the product lands
back in the stage below.  `MarkovTraceRadical.tr_mul_eq_zero_of_step_span` is
that step in the abstract, and `mem_rad_of_orthogonal_H` below is the Hecke
colimit's instance of the conclusion, **unconditionally**.

## What is NOT narrowed

* The **converse**, `mem_traceRadical_of_map`. That direction lifts a test
  element of `Hn` to `ι b` and then needs `ε (ι b) = b` — it spends
  `inst.retract`, and nothing here replaces it.  So the class is still required
  for `map_mem_traceRadical_iff`, hence for `TL_n ↪ TL_{n+1}` and for the
  tower's injectivity.
* `HeckeGramFactorial`'s open input, the general `T_w`-basis determinant, which
  bricks 1–3 never touched.
* A `WenzlTowerStep` instance at the Markov trace.  This is one hypothesis
  removed from one direction, not the bean closed.

  🛑 Measured 2026-09-27: **nothing in the corpus consumes `WenzlTowerStep`** — 27
  occurrences, of which 1 class definition, 2 discharge targets and 24 prose mentions,
  and **zero** instance-hypothesis positions. So an instance unblocks no consumer, and
  at a Hecke carrier its conclusion is free outright
  (`isSemisimpleRing_hecke_generic`; see
  `QOU.Machinery.HeckeRank.wenzlTowerStep_vacuous_of_isSemisimpleRing`). The sentence
  above is kept as the record of what this file did not do; read it as naming an open
  question, not a live blocker. Bean `qou-s7z2`.

## Scope

Convention **D**, `ℝ`, and the four genericity hypotheses `wtrace` already
carries.  The abstract half (`MarkovTraceRadical`) is generic
`[CommRing R] [Ring A] [Algebra R A]` and carries no genericity at all.
-/

namespace QOU.SchurWeyl.HeckeColimitRadicalDescent

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.DisjointBlockTrace
  QOU.MathlibExt.MarkovTraceRadical
open QOU.SchurWeyl QOU.SchurWeyl.HeckeColimit QOU.SchurWeyl.HeckeColimitMarkovTrace
open QOU.SchurWeyl.HeckeColimitNotFaithful

variable (q : ℝ) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
  (hq21 : q ^ 2 + 1 ≠ 0) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1)

include hq0 hq2 hq21 hgen

/-- **Orthogonality at one level is radical membership — unconditionally.**

If `a` sits at level `k ≥ 1` of the Hecke colimit and the Ocneanu trace form
cannot see it *within that level*, then it cannot see it anywhere: `a` is in the
radical of `trLim`.

This is the conclusion of `QBeta.TLTowerRadicalDescent.map_mem_traceRadical`
without its `HeckeConditionalExpectation` hypothesis.  `TowerSpan` does the work
instead, and the Hecke colimit has a `TowerSpan` instance
(`towerSpan_heckeColimit`, proved from the braid relations). -/
theorem mem_rad_of_orthogonal_H (k : ℕ) (hk : 1 ≤ k) (a : HeckeLim ℝ q q⁻¹)
    (ha : a ∈ H ℝ q q⁻¹ k)
    (horth : ∀ b ∈ H ℝ q q⁻¹ k, trLim q hq0 hq2 hq21 hgen (a * b) = 0) :
    a ∈ rad (heckeColimitMarkovTrace q hq0 hq2 hq21 hgen) := by
  haveI : TowerSpan (heckeColimitMarkovTrace q hq0 hq2 hq21 hgen) :=
    towerSpan_heckeColimit q hq0 hq2 hq21 hgen
  obtain ⟨M₀, rfl⟩ : ∃ M₀ : ℕ, k = M₀ + 1 := ⟨k - 1, by omega⟩
  refine mem_rad_of_exhausted (heckeColimitMarkovTrace q hq0 hq2 hq21 hgen)
    a (M₀ + 1) ha M₀ le_rfl ?_ (exists_mem_shiftedUpTo q hq0 hq2 hq21 hgen M₀)
  intro b hb
  exact horth b (shiftedUpTo_le _ 0 M₀ hb)

/-- The same statement as a non-faithfulness criterion: a nonzero element of one
level, invisible within that level, refutes faithfulness of `trLim`. -/
theorem not_isFaithful_of_orthogonal_H (k : ℕ) (hk : 1 ≤ k) (a : HeckeLim ℝ q q⁻¹)
    (ha : a ∈ H ℝ q q⁻¹ k) (ha0 : a ≠ 0)
    (horth : ∀ b ∈ H ℝ q q⁻¹ k, trLim q hq0 hq2 hq21 hgen (a * b) = 0) :
    ¬ IsFaithful (heckeColimitMarkovTrace q hq0 hq2 hq21 hgen) :=
  not_isFaithful _ (mem_rad_of_orthogonal_H q hq0 hq2 hq21 hgen k hk a ha horth) ha0

end QOU.SchurWeyl.HeckeColimitRadicalDescent
