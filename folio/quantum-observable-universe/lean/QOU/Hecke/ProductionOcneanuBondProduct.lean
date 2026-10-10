/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.HeckeColimitMarkovTrace
import QOU.Hecke.PureBondChainProduct
import QOU.Mass.ProductionChainBondProduct

/-!
# The bond products at the PRODUCTION Ocneanu trace

`QOU.Hecke.InteriorMarkovOfBraidedTower`, `QOU.Hecke.PureBondChainProduct` and
`QOU.Mass.ProductionChainBondProduct` each prove a bond-product factorisation for
**every** `OcneanuTrace.MarkovTrace` carrying a `BraidedTower` instance.  Until
the colimit bridge (`QOU.SchurWeyl.HeckeColimitMarkovTrace`) the only such
instance in the tree was `heckeTowerMarkovTrace`, whose trace factors through a
rank-2 quotient — so all three were statements about a *class*, with no
production carrier.

`braidedTower_heckeColimit` supplies the carrier.  This file is the
instantiation, and its content is not the re-statement but the **concrete
Markov parameter**: at the production Ocneanu trace `z = q³/(q²+1)` (convention
D, inherited from `MarkovTraceInstance.wtrace_markov` rather than chosen), so
each abstract `∏ (z + d k)` becomes a product in `q`.

## What is proved here

* `prodZ_eq` — `(toTowerB prodTrace).z = q³/(q²+1)`, the substitution that makes
  everything below a formula in `q`.
* `tr_bondWord_ocneanu` — the general bond word, at the production trace.
* `tr_pureBondChain_ocneanu` — the strictly-increasing pure chain:
  `tr((σ_{g₀}+d₀)(σ_{g₁}+d₁)⋯) = ∏ₖ (q³/(q²+1) + d k)`.
* `tr_productionChain_ocneanu` — the production strand layout, whose bonds sit at
  `σ_{3k+2}`.

## What is NOT proved here

**Nothing about the `d k`.** Every statement below quantifies over arbitrary
scalars `d : ℕ → ℝ`; the *letter identification* (`pp ↦ 0`, `nn ↦ −h`,
`pn ↦ d_averaged_weighted`) is a separate, measured question and is assumed
nowhere. So none of this is a binding-energy claim — it is the factorisation,
with the framework's own `z` substituted in.

No faithfulness, and no injectivity of `ofLim n` (bean `qou-ejde`): these are
statements about `trLim` and about the image filtration exactly as the bridge
leaves them.

The hypotheses are those `MarkovTraceInstance.wtrace` already carries
(`hq0 : q ≠ 0`, `hq2 : NotRootOfUnity q`, `hq21 : q² + 1 ≠ 0`,
`hgen : ∀ i > 0, (q²)^i ≠ 1`) and none is added.
-/

namespace QOU.Hecke.ProductionOcneanuBondProduct

open QOU.MathlibExt.MarkovUnusedGenerator
open QOU.Hecke.MarkovInteriorBond
open QOU.Hecke.InteriorMarkovOfBraidedTower
open QOU.Hecke.PureBondChainProduct
open QOU.Mass.ProductionChainBondProduct
open QOU.MathlibExt.OcneanuTrace
open QOU.SchurWeyl.HeckeColimit QOU.SchurWeyl.HeckeColimitMarkovTrace

variable (q : ℝ) (hq0 : q ≠ 0) (hq2 : QOU.SchurWeyl.GenericParameter.NotRootOfUnity q)
  (hq21 : q ^ 2 + 1 ≠ 0) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1)

include hq0 hq2 hq21 hgen

/-- The production Ocneanu trace on the Iwahori–Hecke colimit. -/
noncomputable abbrev prodTrace : MarkovTrace ℝ (HeckeLim ℝ q q⁻¹) :=
  heckeColimitMarkovTrace q hq0 hq2 hq21 hgen

/-- **The substitution.**  The Markov parameter of the production trace is
`q³/(q²+1)` — convention D.  Every product below is a product in `q` because of
this one `rfl`. -/
@[simp] theorem prodZ_eq :
    (toTowerB (prodTrace q hq0 hq2 hq21 hgen)).z = q ^ 3 / (q ^ 2 + 1) := rfl

/-- **General bond word at the production trace.**  `#7265`'s
`tr_bondWord_of_braided`, instantiated, with `z` substituted. -/
theorem tr_bondWord_ocneanu
    (l : List (ℕ × ℝ × HeckeLim ℝ q q⁻¹)) (x : HeckeLim ℝ q q⁻¹)
    (hc : ChainOK (toTowerB (prodTrace q hq0 hq2 hq21 hgen)) l)
    (hx : x ∈ (toTowerB (prodTrace q hq0 hq2 hq21 hgen)).H (headBond l)) :
    (toTowerB (prodTrace q hq0 hq2 hq21 hgen)).tr
        (bondWord (toTowerB (prodTrace q hq0 hq2 hq21 hgen)) x l)
      = (l.map fun p => q ^ 3 / (q ^ 2 + 1) + p.2.1).prod
        * (toTowerB (prodTrace q hq0 hq2 hq21 hgen)).tr
            (freeWord x l) := by
  simpa using tr_bondWord_of_braided (prodTrace q hq0 hq2 hq21 hgen) l x hc hx

/-- **The pure bond chain at the production trace**, in closed form in `q`:

`tr((σ_{g₀} + d₀)(σ_{g₁} + d₁)⋯) = ∏ₖ (q³/(q²+1) + d k)`

for strictly increasing bonds.  `#7337`'s `tr_pureBondChain_of_braided`,
instantiated.  This is the statement that was previously about a class. -/
theorem tr_pureBondChain_ocneanu (gs : List (ℕ × ℝ)) (h : Increasing gs) :
    (toTowerB (prodTrace q hq0 hq2 hq21 hgen)).tr
        (bondWord (toTowerB (prodTrace q hq0 hq2 hq21 hgen)) 1
          (pureChain (A := HeckeLim ℝ q q⁻¹) gs))
      = (gs.map fun p => q ^ 3 / (q ^ 2 + 1) + p.2).prod := by
  simpa using tr_pureBondChain_of_braided (prodTrace q hq0 hq2 hq21 hgen) gs h

/-- **The production strand layout at the production trace.**  The inter-nucleon
bridges sit at `σ_{3k+2}` (`StrandLayoutForcesChain` upstream), and `#7281`'s
`tr_productionChain_braided` factorises over them; here with `z` substituted.

The `d k` are arbitrary: the letter identification is not claimed. -/
theorem tr_productionChain_ocneanu
    (blk : ℕ → HeckeLim ℝ q q⁻¹) (d : ℕ → ℝ) (n : ℕ)
    (hlow : ∀ k, blk k ∈ (toTowerB (prodTrace q hq0 hq2 hq21 hgen)).H (3 * k + 2))
    (hup : ∀ k, blk (k + 1) ∈ upper (toTowerB (prodTrace q hq0 hq2 hq21 hgen)) (3 * k + 2)) :
    (toTowerB (prodTrace q hq0 hq2 hq21 hgen)).tr
        (bondWord (toTowerB (prodTrace q hq0 hq2 hq21 hgen)) (blk 0)
          (chainFrom blk d 0 (n + 1)))
      = (∏ k ∈ Finset.range (n + 1), (q ^ 3 / (q ^ 2 + 1) + d k))
        * (toTowerB (prodTrace q hq0 hq2 hq21 hgen)).tr
            (freeWord (blk 0) (chainFrom blk d 0 (n + 1))) := by
  simpa using
    tr_productionChain_braided (prodTrace q hq0 hq2 hq21 hgen) blk d n hlow hup

/-- `InteriorMarkov` holds at the production trace — the hypothesis the three
results above are built on, discharged rather than assumed. -/
theorem interiorMarkov_ocneanu :
    InteriorMarkov (toTowerB (prodTrace q hq0 hq2 hq21 hgen)) :=
  interiorMarkov_of_braided _

end QOU.Hecke.ProductionOcneanuBondProduct
