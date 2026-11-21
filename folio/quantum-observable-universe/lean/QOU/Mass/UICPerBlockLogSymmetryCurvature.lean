/-
# The all-pairs symmetry curvature is positive: the UIC's additive part is an anti-valley

Bean `qou-zlra`. The **archimedean** half of `QOU/Mass/UICPerBlockLogPairTerm.lean`, split
out per §7c: this statement is about `Real.log` and an ordering, so it cannot be stated
over a generic `CommRing`, and §7c puts the archimedean specialisation in its own file
consuming the generic result.

## What is proved

Convention D's three bond factors satisfy `b_pn ≥ (b_pp + b_nn)/2`: the `pn` interface
letter is by construction the pp/nn **average**, shifted upward by `h·δ_pn/4 ≥ 0` where
`δ_pn ≥ 0` is `ChainTraceFactor.deltaPN_nonneg`. (This is the same structural fact bean
`qou-mu1h` records as *"the pn bond is an average and cannot be extremal"*.)

For the additive letters `L = −log b` that position **forces the sign** of the symmetry
curvature:

    L_pp + L_nn − 2·L_pn > 0        whenever b_pp ≠ b_nn        (`symmetryCurvature_pos`)

and by `UICPerBlockLogPairTerm.census_secondDiff` that quantity is (half) the second
difference in `Z` of the all-pairs additive binding. So that binding is **strictly convex**
in `Z` (`allPairs_additive_secondDiff_pos`): the symmetric nucleus `N = Z` is a strict
**minimum** of the binding, not a maximum.

That is an **anti-valley**, and the sign is forced for every `q > 1` — it is not a fact
measured at `q₀`. Measured at `q₀` for scale:
`L_pp + L_nn − 2·L_pn = +0.04351846501566097275`
(`computations/probes/uic_per_block_log_valley_scan_probe.py`, S4.4).

## Proof shape

Two applications of `(b_pp − b_nn)² > 0`:

* `b_pn ≥ m := (b_pp+b_nn)/2` and `m² > b_pp·b_nn` (AM–GM, strict since `b_pp ≠ b_nn`),
  so `b_pn² > b_pp·b_nn`;
* `Real.log` is strictly monotone, and `log(b_pp·b_nn) = log b_pp + log b_nn`,
  `log(b_pn²) = 2·log b_pn`.

## Scope

This governs the **additive** part of the UIC — the component that is a linear function of
the bond census. The per-block log carries a genuine non-census correlation on top of it
(`UICPerBlockLogPairTerm.twoCrossing_defect`, and the measured `Δ³_Z ≠ 0`), and this file
says nothing about the sign of *that* piece. What it establishes is that the forced
component points away from a valley, for every `q > 1`.

-- Ref: [leitner2026] prop:unified-iterative-correction; the convention-D letters and
-- `deltaPN_nonneg` are `QOU/Mass/ChainTraceFactor.lean`.
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import QOU.Mass.UICPerBlockLogPairTerm

namespace QOU.Mass.UICPerBlockLogSymmetryCurvature

open QOU.Mass.UICPerBlockLogPairTerm

/-- **The `pn` letter's position forces an anti-valley.** With bond factors `b > 0` and the
additive letters `L = −log b`, if the `pn` factor is at least the midpoint of the `pp` and
`nn` factors — which convention D guarantees via `ChainTraceFactor.deltaPN_nonneg` — and the
`pp` and `nn` factors differ, then `L_pp + L_nn − 2·L_pn > 0`. -/
theorem symmetryCurvature_pos {bpp bpn bnn : ℝ}
    (hpp : 0 < bpp) (hnn : 0 < bnn) (hne : bpp ≠ bnn)
    (hmid : (bpp + bnn) / 2 ≤ bpn) :
    0 < (-Real.log bpp) + (-Real.log bnn) - 2 * (-Real.log bpn) := by
  have hm : (0:ℝ) < (bpp + bnn) / 2 := by linarith
  have hbpn : 0 < bpn := lt_of_lt_of_le hm hmid
  have hsq : (0:ℝ) < (bpp - bnn) ^ 2 :=
    lt_of_le_of_ne (sq_nonneg _) (Ne.symm (pow_ne_zero 2 (sub_ne_zero.mpr hne)))
  have hstep : bpp * bnn < bpn ^ 2 := by
    nlinarith [mul_nonneg (sub_nonneg.mpr hmid)
      (by linarith : (0:ℝ) ≤ bpn + (bpp + bnn) / 2)]
  have hlog : Real.log (bpp * bnn) < Real.log (bpn ^ 2) :=
    Real.log_lt_log (by positivity) hstep
  rw [Real.log_mul hpp.ne' hnn.ne', Real.log_pow] at hlog
  push_cast at hlog
  linarith

/-- The same statement read through `census_secondDiff`: the all-pairs additive binding is
**strictly convex** in `Z`, so the symmetric nucleus is a strict minimum — an anti-valley,
not a valley of stability. -/
theorem allPairs_additive_secondDiff_pos {bpp bpn bnn A Z : ℝ}
    (hpp : 0 < bpp) (hnn : 0 < bnn) (hne : bpp ≠ bnn)
    (hmid : (bpp + bnn) / 2 ≤ bpn) (c : ℝ) :
    0 < fwd (fwd (census c (-Real.log bpp) (-Real.log bpn) (-Real.log bnn) A)) Z := by
  rw [census_secondDiff]
  have := symmetryCurvature_pos hpp hnn hne hmid
  linarith

#print axioms symmetryCurvature_pos
#print axioms allPairs_additive_secondDiff_pos

end QOU.Mass.UICPerBlockLogSymmetryCurvature
