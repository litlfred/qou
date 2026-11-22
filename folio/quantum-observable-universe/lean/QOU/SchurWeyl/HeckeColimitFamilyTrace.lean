/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.HeckeColimit
import QOU.SchurWeyl.MarkovTraceUnique
import QOU.MathlibExt.OcneanuTrace
import QOU.MathlibExt.HeckeSandwichReduces

/-!
# Any Markov trace family on the Hecke tower is a braided-tower Markov trace on the colimit

Bean `qou-5zl1`, step 1.  `HeckeColimitMarkovTrace` builds an
`OcneanuTrace.MarkovTrace` on the colimit `HeckeLim` of the tower
`Hecke K q qi 0 → Hecke K q qi 1 → ⋯` (built from `heckeIncl`), but only for one
trace: the convention-D Ocneanu trace `wtrace` over `ℝ`, at `z = q³/(q²+1)`.
That file reads a fixed weight and fixed genericity hypotheses into every
statement.  None of them is used by the construction itself: the lift needs only
the four axioms of `HeckeCoset.MarkovTraceFamily`.

This file states the construction once, for **every** Markov trace family, at
**every** parameter `z`, over **any** commutative ring with `q * qi = 1`:

| declaration | content |
|---|---|
| `trFam_inclLE` | the iterated inclusion preserves the trace (from `tr_incl`) |
| `trFam` | the lifted functional on `HeckeLim` |
| `trFam_cyclic` / `trFam_one` / `trFam_markov` / `trFam_markov_inv` | axioms T1, T2, T3, T3' |
| `ocneanuMarkovTraceAt` | the `OcneanuTrace.MarkovTrace` with parameter `z` |
| `braidedTower_ocneanuMarkovTraceAt` | it is a `BraidedTower`, with `h = q - qi` |
| `disjointBlock_ocneanuMarkovTraceAt` | so the disjoint-block trace law holds on it |
| `ocneanuMarkovTraceAt_z` | its parameter is the family's `z`; nothing is chosen |

`zinv` is derived, not posited: `σ⁻¹ = σ - (q - qi)·1`, so `zinv = z - (q - qi)`.

## What this does NOT supply

**It is not an existence theorem for a Markov trace at arbitrary `z`.**  It turns
a `MarkovTraceFamily` into a tower trace; it does not produce the family.  The
families the corpus has proved to exist are the convention-D Ocneanu trace
(`MarkovTraceInstance.ocneanuMarkovTrace`, `z = q³/(q²+1)`) and the level-`r`
Wenzl traces (`WenzlMarkovTraceInstance.wenzlMarkovTrace`,
`z_r = Q^r/(q·[r]_Q)`), both over a field with `q` not a root of unity.  The
general-`z` Ocneanu weight `ocneanuWeight q z` is defined in `OcneanuWeight`,
but its Markov property at general `n` is **open** (that file says so), so no
general-`z` family is instantiated here.  Every theorem downstream of
`ocneanuMarkovTraceAt` is therefore a theorem about whichever family is fed in,
and holds at a given `z` exactly when a family at that `z` exists.

**Update 2026-11-20:** a family now exists at **every** `z` (over a field, `q` and `q²` not roots
of unity): `SeminormalRep.ocneanuMarkovTraceEveryZ` in `OcneanuMarkovTraceEveryZ`, whose colimit
trace is `SeminormalRep.ocneanuMarkovTraceColimit`. The general-`z` Markov property described as
open above is proved there; this file is unchanged.

`ofLim n` is not known to be injective (bean `qou-ejde`), so `H n` is the image
of level `n`, as in `HeckeColimit`.

## Base ring (§7c)

Generic `[CommRing K]`, `q qi : K` with `q * qi = 1`.  No ordering, no `ℝ`.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [leitner2026] beans qou-5zl1 / qou-0fmb / qou-ejde; `HeckeColimitMarkovTrace`.
-/

namespace QOU.SchurWeyl.HeckeColimitFamilyTrace

open QOU.SchurWeyl QOU.SchurWeyl.Hecke QOU.SchurWeyl.HeckeInclusion
open QOU.SchurWeyl.HeckeDirectedSystem QOU.SchurWeyl.HeckeColimit
open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.HeckeSandwichReduces
open QOU.MathlibExt.TowerSpanReduction QOU.MathlibExt.DisjointBlockTrace

variable {K : Type*} [CommRing K] {q qi z : K}
variable (U : HeckeCoset.MarkovTraceFamily K q qi z)

/-- The level-wise traces are compatible with the **iterated** inclusion. -/
theorem trFam_inclLE (i j : ℕ) (hij : i ≤ j) (x : Hecke K q qi i) :
    U.tr j (heckeInclLE K q qi i j hij x) = U.tr i x := by
  induction j, hij using Nat.le_induction with
  | base => rw [heckeInclLE_self]; rfl
  | succ n hn ih =>
      rw [heckeInclLE_succ K q qi i n hn, AlgHom.comp_apply, U.tr_incl n, ih]

/-- The family's trace lifted to the colimit.  A `Module` lift: the level traces
are linear and not multiplicative. -/
noncomputable def trFam : HeckeLim K q qi →ₗ[K] K :=
  DirectLimit.Module.lift K ℕ (Hecke K q qi) (heckeF K q qi)
    U.tr (fun i j hij x => trFam_inclLE U i j hij x)

@[simp] theorem trFam_ofLim (n : ℕ) (x : Hecke K q qi n) :
    trFam U (ofLimₐ K q qi n x) = U.tr n x :=
  DirectLimit.Module.lift_of (f := heckeF K q qi) _ _ x

/-- **(T1)** The trace property on the colimit. -/
theorem trFam_cyclic (a b : HeckeLim K q qi) :
    trFam U (a * b) = trFam U (b * a) := by
  induction a, b using DirectLimit.induction₂ (f := heckeF K q qi) with
  | _ i x y =>
    show trFam U (ofLimₐ K q qi i x * ofLimₐ K q qi i y)
      = trFam U (ofLimₐ K q qi i y * ofLimₐ K q qi i x)
    rw [← map_mul, ← map_mul, trFam_ofLim, trFam_ofLim]
    exact U.tr_cyclic i x y

/-- **(T2)** Normalisation on the colimit. -/
theorem trFam_one : trFam U 1 = 1 := by
  have h1 : (1 : HeckeLim K q qi) = ofLimₐ K q qi 0 1 := (map_one _).symm
  rw [h1, trFam_ofLim]
  exact U.tr_one 0

/-- **(T3)** Markov stabilisation on the colimit, with the family's own `z`. -/
theorem trFam_markov (n : ℕ) (a : HeckeLim K q qi) (ha : a ∈ H K q qi n) :
    trFam U (a * gLim K q qi n) = z * trFam U a := by
  obtain ⟨y, rfl⟩ := ha
  show trFam U (ofLimₐ K q qi n y * gLim K q qi n) = z * trFam U (ofLimₐ K q qi n y)
  have hstep : ofLimₐ K q qi n y = ofLimₐ K q qi (n + 1) (heckeIncl K q qi n y) := by
    have := ofLimₐ_comp K q qi (Nat.le_succ n) y
    rw [← this, heckeInclLE_succ K q qi n n le_rfl, AlgHom.comp_apply, heckeInclLE_self]
    rfl
  have hlast : σ K q qi (n + 1) ⟨n, Nat.lt_succ_self n⟩ = σ K q qi (n + 1) (Fin.last n) := rfl
  nth_rewrite 1 [hstep]
  rw [gLim, hlast, ← map_mul, trFam_ofLim, trFam_ofLim]
  exact U.tr_markov n y

/-- **(T3')** Markov stabilisation by the inverse generator; `zinv = z - (q - qi)`
is derived from `σ⁻¹ = σ - (q - qi)·1`. -/
theorem trFam_markov_inv (n : ℕ) (a : HeckeLim K q qi) (ha : a ∈ H K q qi n) :
    trFam U (a * ginvLim K q qi n) = (z - (q - qi)) * trFam U a := by
  have hsplit : a * ginvLim K q qi n = a * gLim K q qi n - (q - qi) • a := by
    rw [ginvLim, gLim, σInv, map_sub, map_smul, map_one, mul_sub, mul_smul_comm, mul_one]
  rw [hsplit, map_sub, map_smul, trFam_markov U n a ha]
  simp only [smul_eq_mul]
  ring

variable (hqi : q * qi = 1)

/-- **The general-`z` Markov trace on the Hecke colimit.**  Any Markov trace
family on the tower `Hecke K q qi n`, at any parameter `z`, packaged as an
`OcneanuTrace.MarkovTrace` on the colimit. -/
noncomputable def ocneanuMarkovTraceAt : MarkovTrace K (HeckeLim K q qi) where
  H := H K q qi
  H_mono := H_mono K q qi
  g := gLim K q qi
  g_mem := gLim_mem K q qi
  ginv := ginvLim K q qi
  ginv_mem := ginvLim_mem K q qi
  ginv_mul n := ginvLim_mul_gLim K q qi hqi n
  mul_ginv n := gLim_mul_ginvLim K q qi hqi n
  tr := trFam U
  tr_mul_comm := trFam_cyclic U
  tr_one := trFam_one U
  z := z
  zinv := z - (q - qi)
  markov := trFam_markov U
  markov_inv := trFam_markov_inv U

/-- The parameter of the colimit trace is the family's: nothing is chosen. -/
@[simp] theorem ocneanuMarkovTraceAt_z : (ocneanuMarkovTraceAt U hqi).z = z := rfl

@[simp] theorem ocneanuMarkovTraceAt_tr_ofLim (n : ℕ) (x : Hecke K q qi n) :
    (ocneanuMarkovTraceAt U hqi).tr (ofLimₐ K q qi n x) = U.tr n x :=
  trFam_ofLim U n x

@[simp] theorem ocneanuMarkovTraceAt_g (n : ℕ) :
    (ocneanuMarkovTraceAt U hqi).g n = gLim K q qi n := rfl

/-- **The colimit trace is a braided tower**, with `h = q - qi`: the three
`BraidedTower` fields are the quadratic, far-commutation and braid relations of
the tower, with `q * qi = 1` closing the quadratic. -/
instance braidedTower_ocneanuMarkovTraceAt :
    BraidedTower (ocneanuMarkovTraceAt U hqi) where
  quad m := ⟨q - qi, by
    have h := gLim_quadratic K q qi m
    rw [hqi, one_smul] at h
    exact h⟩
  far m k hk := gLim_far K q qi m k hk
  braid m := gLim_braid K q qi m

/-- `TowerSpan` on the colimit, at every `z` for which a family is given. -/
theorem towerSpan_ocneanuMarkovTraceAt : TowerSpan (ocneanuMarkovTraceAt U hqi) :=
  towerSpan_of_braided _

/-- **The disjoint-block trace law on the colimit**, at every `z` for which a
family is given. -/
theorem disjointBlock_ocneanuMarkovTraceAt :
    DisjointBlockMultiplicative (ocneanuMarkovTraceAt U hqi) :=
  disjointBlock_of_braided _

end QOU.SchurWeyl.HeckeColimitFamilyTrace
