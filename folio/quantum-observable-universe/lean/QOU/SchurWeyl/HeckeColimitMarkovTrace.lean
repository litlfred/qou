/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.HeckeColimit
import QOU.SchurWeyl.MarkovTraceInstance
import QOU.MathlibExt.OcneanuTrace
import QOU.MathlibExt.HeckeSandwichReduces

/-!
# The Ocneanu trace on the colimit: closing the bridge

Steps 4–6 of bean `qou-0fmb`.  Steps 1–3 built the colimit `HeckeLim`, its
`K`-algebra structure, the range filtration `H`, and the generators — and showed
the three braid relations hold there.  What was missing was the **trace**, and
with it the four remaining `OcneanuTrace.MarkovTrace` fields.

## What is proved here

* `wtrace_inclLE` — the level-wise trace is compatible with the *iterated*
  inclusion, not merely with one step.  `DirectLimit.Module.lift` needs the
  former; `MarkovTraceInstance.wtrace_incl` supplies the latter, and this is its
  `Nat.le_induction` iterate.
* `trLim` — the Ocneanu trace on the colimit, as a **linear** map `HeckeLim →ₗ[ℝ] ℝ`.
  It is `DirectLimit.Module.lift`, not `Ring.lift`: `wtrace` is linear and is not
  a ring map (it is not multiplicative), so the ring lift does not apply and the
  module lift is what the `MarkovTrace.tr` field wants anyway.
* `trLim_cyclic`, `trLim_one`, `trLim_markov`, `trLim_markov_inv` — the four
  trace axioms, each obtained by `DirectLimit.induction` down to a single level
  where the corresponding `wtrace` lemma already holds.
* `heckeColimitMarkovTrace` — the `MarkovTrace ℝ (HeckeLim ℝ q q⁻¹)` instance.
  **This is the bridge**: `HeckeCoset.MarkovTraceFamily`, which is indexed by
  level, now has a counterpart on a single algebra, which is the interface every
  `MathlibExt` tower result is stated against.

## The two Markov parameters

`z = q³/(q²+1)` is **convention D**, canonical per the owner ruling of
2026-08-15, and it is inherited from `wtrace_markov`, not chosen here.

`zinv` is **derived, not posited**: `σ⁻¹ = σ - (q - q⁻¹)·1` by definition, so
`tr (a σ⁻¹) = tr (a σ) - (q - q⁻¹) tr a = (z - (q - q⁻¹)) tr a`, giving
`zinv = q³/(q²+1) - (q - q⁻¹)`.  This is the `markovParam_inv_eq_sub` shape of
`OcneanuTrace` realised concretely, and nothing about it is fitted.

## Hypotheses, and what they are

The construction carries exactly the hypotheses that `MarkovTraceInstance`'s
`wtrace` already carries — `hq0 : q ≠ 0`, `hq2 : NotRootOfUnity q`,
`hq21 : q² + 1 ≠ 0`, `hgen : ∀ i > 0, (q²)^i ≠ 1` — and adds none.  They are
genericity conditions on the parameter under which the seminormal form exists;
they are not assumptions about the trace.

Note `qi = q⁻¹` throughout, so the `q * qi = 1` hypothesis of step 3's
`gLim_mul_ginvLim` is discharged by `hq0` and never surfaces.

## The payoff

`braidedTower_heckeColimit` records that the colimit satisfies the three
`MathlibExt.BraidedTower` fields — the relations of step 3, unchanged.  That
instance is what carries `towerSpan_heckeColimit` and
`disjointBlock_heckeColimit`: `TowerSpan` (`H_{n+1} = H_n + H_n g_n H_n`) and
the disjoint-block trace law now hold for the **genuine Iwahori–Hecke tower**,
not only for the free `HeckeTower` carrier they were first witnessed on.

## What is NOT proved here

No faithfulness.  `H n` remains the *image* of level `n`, and whether `ofLim n`
is injective is bean `qou-ejde`, assumed nowhere.  Nor is `trLim` claimed
faithful — the `HeckeTower` witness of `MathlibExt` is explicitly not, and
nothing here changes that.
-/

namespace QOU.SchurWeyl.HeckeColimitMarkovTrace

open QOU.SchurWeyl QOU.SchurWeyl.Hecke QOU.SchurWeyl.HeckeInclusion
open QOU.SchurWeyl.HeckeDirectedSystem QOU.SchurWeyl.HeckeColimit QOU.SchurWeyl.SeminormalRep
open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.HeckeSandwichReduces
open QOU.MathlibExt.TowerSpanReduction QOU.MathlibExt.DisjointBlockTrace

variable (q : ℝ) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
  (hq21 : q ^ 2 + 1 ≠ 0) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1)

-- Every declaration below needs all four genericity hypotheses, most of them only
-- in the proof; a section-wide `include` keeps them in the signatures.
include hq0 hq2 hq21 hgen

/-- The level-wise trace is compatible with the **iterated** inclusion.

`wtrace_incl` gives one step; `DirectLimit.Module.lift` needs every step, and
this is the `Nat.le_induction` iterate. -/
theorem wtrace_inclLE (i j : ℕ) (hij : i ≤ j) (x : Hecke ℝ q q⁻¹ i) :
    wtrace q hq0 hq2 j (heckeInclLE ℝ q q⁻¹ i j hij x) = wtrace q hq0 hq2 i x := by
  induction j, hij using Nat.le_induction with
  | base => rw [heckeInclLE_self]; rfl
  | succ n hn ih =>
      rw [heckeInclLE_succ ℝ q q⁻¹ i n hn, AlgHom.comp_apply,
        wtrace_incl q hq0 hq2 hq21 hgen n, ih]

/-- **The Ocneanu trace on the colimit.**

A `Module` lift, not a `Ring` lift: `wtrace` is `ℝ`-linear but not
multiplicative, so `DirectLimit.Ring.lift` does not apply — and linearity is
exactly what the `MarkovTrace.tr` field asks for. -/
noncomputable def trLim : HeckeLim ℝ q q⁻¹ →ₗ[ℝ] ℝ :=
  DirectLimit.Module.lift ℝ ℕ (Hecke ℝ q q⁻¹) (heckeF ℝ q q⁻¹)
    (wtrace q hq0 hq2) (fun i j hij x => wtrace_inclLE q hq0 hq2 hq21 hgen i j hij x)

@[simp] theorem trLim_ofLim (n : ℕ) (x : Hecke ℝ q q⁻¹ n) :
    trLim q hq0 hq2 hq21 hgen (ofLimₐ ℝ q q⁻¹ n x) = wtrace q hq0 hq2 n x :=
  DirectLimit.Module.lift_of (f := heckeF ℝ q q⁻¹) _ _ x

/-- **(T1)** The trace property on the colimit. -/
theorem trLim_cyclic (a b : HeckeLim ℝ q q⁻¹) :
    trLim q hq0 hq2 hq21 hgen (a * b) = trLim q hq0 hq2 hq21 hgen (b * a) := by
  induction a, b using DirectLimit.induction₂ (f := heckeF ℝ q q⁻¹) with
  | _ i x y =>
    show trLim q hq0 hq2 hq21 hgen (ofLimₐ ℝ q q⁻¹ i x * ofLimₐ ℝ q q⁻¹ i y)
      = trLim q hq0 hq2 hq21 hgen (ofLimₐ ℝ q q⁻¹ i y * ofLimₐ ℝ q q⁻¹ i x)
    rw [← map_mul, ← map_mul, trLim_ofLim, trLim_ofLim]
    exact wtrace_cyclic q hq0 hq2 i x y

/-- **(T2)** Normalisation on the colimit. -/
theorem trLim_one : trLim q hq0 hq2 hq21 hgen 1 = 1 := by
  have h1 : (1 : HeckeLim ℝ q q⁻¹) = ofLimₐ ℝ q q⁻¹ 0 1 := (map_one _).symm
  rw [h1, trLim_ofLim]
  exact wtrace_one q hq0 hq2 hq21 hgen 0

/-- **(T3)** Markov stabilisation on the colimit, with `z = q³/(q²+1)`
(convention D). -/
theorem trLim_markov (n : ℕ) (a : HeckeLim ℝ q q⁻¹) (ha : a ∈ H ℝ q q⁻¹ n) :
    trLim q hq0 hq2 hq21 hgen (a * gLim ℝ q q⁻¹ n)
      = (q ^ 3 / (q ^ 2 + 1)) * trLim q hq0 hq2 hq21 hgen a := by
  obtain ⟨y, rfl⟩ := ha
  show trLim q hq0 hq2 hq21 hgen (ofLimₐ ℝ q q⁻¹ n y * gLim ℝ q q⁻¹ n)
    = (q ^ 3 / (q ^ 2 + 1)) * trLim q hq0 hq2 hq21 hgen (ofLimₐ ℝ q q⁻¹ n y)
  have hstep : ofLimₐ ℝ q q⁻¹ n y
      = ofLimₐ ℝ q q⁻¹ (n + 1) (heckeIncl ℝ q q⁻¹ n y) := by
    have := ofLimₐ_comp ℝ q q⁻¹ (Nat.le_succ n) y
    rw [← this, heckeInclLE_succ ℝ q q⁻¹ n n le_rfl, AlgHom.comp_apply, heckeInclLE_self]
    rfl
  have hlast : σ ℝ q q⁻¹ (n + 1) ⟨n, Nat.lt_succ_self n⟩
      = σ ℝ q q⁻¹ (n + 1) (Fin.last n) := rfl
  nth_rewrite 1 [hstep]
  rw [gLim, hlast, ← map_mul, trLim_ofLim, trLim_ofLim]
  exact wtrace_markov q hq0 hq2 hq21 hgen n y

/-- **(T3')** Markov stabilisation by the inverse generator.

The parameter `zinv = q³/(q²+1) - (q - q⁻¹)` is **derived** from
`σ⁻¹ = σ - (q - q⁻¹)·1`, not posited. -/
theorem trLim_markov_inv (n : ℕ) (a : HeckeLim ℝ q q⁻¹) (ha : a ∈ H ℝ q q⁻¹ n) :
    trLim q hq0 hq2 hq21 hgen (a * ginvLim ℝ q q⁻¹ n)
      = (q ^ 3 / (q ^ 2 + 1) - (q - q⁻¹)) * trLim q hq0 hq2 hq21 hgen a := by
  have hsplit : a * ginvLim ℝ q q⁻¹ n
      = a * gLim ℝ q q⁻¹ n - (q - q⁻¹) • a := by
    rw [ginvLim, gLim, σInv, map_sub, map_smul, map_one, mul_sub, mul_smul_comm, mul_one]
  rw [hsplit, map_sub, map_smul, trLim_markov q hq0 hq2 hq21 hgen n a ha]
  simp only [smul_eq_mul]
  ring

/-- **The bridge.**  The colimit of the Iwahori–Hecke tower, with the lifted
Ocneanu trace, is a `MathlibExt.OcneanuTrace.MarkovTrace`.

Every hypothesis is one `MarkovTraceInstance.wtrace` already carries; none is
added.  With this, the level-indexed `HeckeCoset.MarkovTraceFamily` and the
single-algebra `OcneanuTrace.MarkovTrace` interfaces are connected, and the
tower results proved against the latter — `tr_conj`, `tr_eq_of_isConj`,
`tr_mul_stabWord`, and via step 3's braid relations `TowerSpan` and
`DisjointBlockTraceLaw` — apply to the genuine Hecke tower. -/
noncomputable def heckeColimitMarkovTrace : MarkovTrace ℝ (HeckeLim ℝ q q⁻¹) where
  H := H ℝ q q⁻¹
  H_mono := H_mono ℝ q q⁻¹
  g := gLim ℝ q q⁻¹
  g_mem := gLim_mem ℝ q q⁻¹
  ginv := ginvLim ℝ q q⁻¹
  ginv_mem := ginvLim_mem ℝ q q⁻¹
  ginv_mul n := ginvLim_mul_gLim ℝ q q⁻¹ (mul_inv_cancel₀ hq0) n
  mul_ginv n := gLim_mul_ginvLim ℝ q q⁻¹ (mul_inv_cancel₀ hq0) n
  tr := trLim q hq0 hq2 hq21 hgen
  tr_mul_comm := trLim_cyclic q hq0 hq2 hq21 hgen
  tr_one := trLim_one q hq0 hq2 hq21 hgen
  z := q ^ 3 / (q ^ 2 + 1)
  zinv := q ^ 3 / (q ^ 2 + 1) - (q - q⁻¹)
  markov := trLim_markov q hq0 hq2 hq21 hgen
  markov_inv := trLim_markov_inv q hq0 hq2 hq21 hgen

/-! ## The colimit is a braided tower

This is where steps 1–6 meet #7153.  The three relations of step 3 are exactly
the `BraidedTower` fields, so every tower result proved from the braid relations
alone transfers to the genuine Iwahori–Hecke tower. -/

/-- The colimit Markov trace is a **braided tower**.

`quad` reads `g² = (q - q⁻¹)·g + (q·q⁻¹)·1` with `q·q⁻¹ = 1` discharged by
`hq0`, giving `h = q - q⁻¹`. -/
instance braidedTower_heckeColimit :
    BraidedTower (heckeColimitMarkovTrace q hq0 hq2 hq21 hgen) where
  quad m := ⟨q - q⁻¹, by
    have h := gLim_quadratic ℝ q q⁻¹ m
    rw [mul_inv_cancel₀ hq0, one_smul] at h
    exact h⟩
  far m k hk := gLim_far ℝ q q⁻¹ m k hk
  braid m := gLim_braid ℝ q q⁻¹ m

/-- **`TowerSpan` holds on the Iwahori–Hecke tower.**

`H_{n+1} = H_n + H_n · g_n · H_n`, for the genuine Hecke algebras — not for the
free `HeckeTower` carrier.  Proved from the braid relations in #7153; this is its
instantiation. -/
theorem towerSpan_heckeColimit :
    TowerSpan (heckeColimitMarkovTrace q hq0 hq2 hq21 hgen) :=
  towerSpan_of_braided _

/-- **The disjoint-block trace law holds on the Iwahori–Hecke tower.** -/
theorem disjointBlock_heckeColimit :
    DisjointBlockMultiplicative (heckeColimitMarkovTrace q hq0 hq2 hq21 hgen) :=
  disjointBlock_of_braided _

end QOU.SchurWeyl.HeckeColimitMarkovTrace
