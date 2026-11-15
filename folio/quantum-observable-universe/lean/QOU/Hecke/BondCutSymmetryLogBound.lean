/-
# The convex interface bounds the bond-cut slope by `2 ln q`

Archimedean specialisation (§7c) of `QOU/Hecke/BondCutSymmetry.lean`, in the
`e = -ln b` letters. The generic file proves that the whole layout dependence
of a pair-additive bond count is `δ · n_pn` with `δ = e_pn - (e_pp+e_nn)/2`,
and that on a well-mixed degree-`k` graph the symmetry coefficient is
`E₀·δ·k/4`. This file bounds `δ` for the corpus's actual interface.

The corpus's p–n bond is a convex combination `b_pn = w·b_pp + (1-w)·b_nn`
(`SymmetrySignAmGm`, `weight_of_convention`). For any `w ∈ [0,1]` the interface
lies between the two like-species bonds, so `δ ≤ (e_nn - e_pp)/2`
(`energySlope_convex_le`), and with the pinned `b_pp = q²/[2]_q`,
`b_nn = q⁻²/[2]_q` that is **exactly `2 ln q`** (`half_splitting_pinned`,
`energySlope_convex_le_two_log`). At `q₀` the bound is `0.2087`; the corpus's
`δ` is `-0.0218`. Through `BondCutSymmetry.bondSum_wellMixed_symmetry` the
symmetry coefficient of *any* convex interface on a degree-`k` well-mixed graph
is at most `(k/2)·E₀·ln q` — `0.44` MeV at `k = 2`, `2.65` MeV at `k = 12`,
against the SEMF `a_A ≈ 23.7` MeV. Flipping the sign is cheap; supplying the
magnitude is not available to any interface weight.

Producer: `computations/qbeta/qbeta_bond_cut_symmetry_shape_probe.py`.
Bean `qou-qve5`.
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import QOU.Hecke.BondCutSymmetry

namespace QOU.Hecke.BondCutSymmetryLogBound

open QOU.Hecke.BondCutSymmetry

section Real

open Real

/-- The corpus's p–n bond: a convex combination of the like-species bonds
(`SymmetrySignAmGm.weight_of_convention` derives `w = 1/2 + δ_f/4`). -/
noncomputable def interface (bpp bnn w : ℝ) : ℝ :=
  w * bpp + (1 - w) * bnn

/-- `energySlope` in `e = -ln b` letters is `SymmetrySignAmGm.delta` — the same
number, so the AM-vs-GM sign result transfers verbatim. -/
theorem energySlope_eq_log_form (bpp bpn bnn : ℝ) :
    energySlope (-Real.log bpp) (-Real.log bpn) (-Real.log bnn)
      = (Real.log bpp + Real.log bnn) / 2 - Real.log bpn := by
  unfold energySlope
  ring

/-- For a convex weight the interface lies between the two like-species bonds. -/
theorem interface_mem {bpp bnn w : ℝ} (h : bnn ≤ bpp) (hw0 : 0 ≤ w) (hw1 : w ≤ 1) :
    bnn ≤ interface bpp bnn w ∧ interface bpp bnn w ≤ bpp := by
  unfold interface
  constructor <;> nlinarith

/-- **Invariant (1): the convex family bounds the slope.** For every weight in
`[0, 1]`, `δ ≤ (e_nn - e_pp)/2`, with equality at `w = 0` (pure `σ⁻¹`
interface). The *sign* can be flipped by a weight below the crossing; the
*magnitude* cannot exceed half the like-species splitting, whatever the weight. -/
theorem energySlope_convex_le {bpp bnn w : ℝ} (hnn : 0 < bnn) (h : bnn ≤ bpp)
    (hw0 : 0 ≤ w) (hw1 : w ≤ 1) :
    energySlope (-Real.log bpp) (-Real.log (interface bpp bnn w)) (-Real.log bnn)
      ≤ (Real.log bpp - Real.log bnn) / 2 := by
  have hmem := interface_mem h hw0 hw1
  have hlog : Real.log bnn ≤ Real.log (interface bpp bnn w) :=
    Real.log_le_log hnn hmem.1
  unfold energySlope
  linarith

/-- With the pinned bonds `b_pp = q²/[2]_q`, `b_nn = q⁻²/[2]_q`, half the
like-species splitting is exactly `2 ln q`: `b_pp/b_nn = q⁴`. -/
theorem half_splitting_pinned {q : ℝ} (hq : 0 < q) :
    (Real.log (q ^ 2 / (q + 1 / q)) - Real.log ((q ^ 2)⁻¹ / (q + 1 / q))) / 2
      = 2 * Real.log q := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hsum : 0 < q + 1 / q := by positivity
  have hpp : 0 < q ^ 2 / (q + 1 / q) := by positivity
  have hnn : 0 < (q ^ 2)⁻¹ / (q + 1 / q) := by positivity
  have hratio : q ^ 2 / (q + 1 / q) / ((q ^ 2)⁻¹ / (q + 1 / q)) = q ^ 4 := by
    field_simp
  rw [← Real.log_div (ne_of_gt hpp) (ne_of_gt hnn), hratio, Real.log_pow]
  push_cast
  ring

/-- **Invariant (1), pinned: `δ ≤ 2 ln q` for every convex interface weight.**
At `q₀` the bound is `0.2087`, attained at `w = 0`; the corpus sits at
`-0.0218`. Through `bondSum_wellMixed_symmetry` the symmetry coefficient of
*any* convex interface on a degree-`k` well-mixed graph is at most
`(k/2)·ln q` per unit `E₀` — one order of magnitude below the SEMF target. -/
theorem energySlope_convex_le_two_log {q w : ℝ} (hq : 1 ≤ q)
    (hw0 : 0 ≤ w) (hw1 : w ≤ 1) :
    energySlope (-Real.log (q ^ 2 / (q + 1 / q)))
        (-Real.log (interface (q ^ 2 / (q + 1 / q)) ((q ^ 2)⁻¹ / (q + 1 / q)) w))
        (-Real.log ((q ^ 2)⁻¹ / (q + 1 / q)))
      ≤ 2 * Real.log q := by
  have hq0 : 0 < q := by linarith
  have hsum : 0 < q + 1 / q := by positivity
  have hnn : 0 < (q ^ 2)⁻¹ / (q + 1 / q) := by positivity
  have hle : (q ^ 2)⁻¹ / (q + 1 / q) ≤ q ^ 2 / (q + 1 / q) := by
    apply div_le_div_of_nonneg_right _ hsum.le
    have h1 : (1 : ℝ) ≤ q ^ 2 := by nlinarith
    calc (q ^ 2)⁻¹ ≤ 1 := inv_le_one_of_one_le₀ h1
      _ ≤ q ^ 2 := h1
  calc _ ≤ (Real.log (q ^ 2 / (q + 1 / q)) - Real.log ((q ^ 2)⁻¹ / (q + 1 / q))) / 2 :=
        energySlope_convex_le hnn hle hw0 hw1
    _ = 2 * Real.log q := half_splitting_pinned hq0

end Real

end QOU.Hecke.BondCutSymmetryLogBound
