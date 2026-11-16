/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Formalization of the 5-bean cluster under `qou-frzo`:
1. `8we6`: Casoratian determinant `W_k = cEven_k * cOdd_{k+1} - cEven_{k+1} * cOdd_k`
   antisymmetry under channel swap, and the exact rational `c_2` decoupling-gate shifts
   `+12`, `+13/6`, and `-40` of the three `H_4` Route-A candidate framings (`A1`, `A2`, `A3`),
   whose sum is `-155 / 6 ≠ 0`.
2. `qou-2qt2`: Bar-even and bar-odd half-projections `barEvenHalf(fQ, fQInv) = (fQ + fQInv) / 2`
   and `barOddHalf(fQ, fQInv) = (fQ - fQInv) / 2`, proving exact reconstruction
   `barEvenHalf + barOddHalf = fQ` and the bar-even-channel falsifier (`barOddHalf(fQ, fQ) = 0`).
3. `qou-3cgi`: Newton-polygon quadratic growth `thetaHalf(m) = m * (m - 1) / 2` first-difference
   identity `thetaHalf(m + 1) - thetaHalf(m) = m`, and strict separation of the `C1` slope
   `1 / 2` from the GGM Stokes slopes `{-1, 1}`.
4. `qou-3qla`: Palindromic Chebyshev reduction of the colour-cubic discriminant sextic
   `16(z^3 + z⁻³) + 24(z^2 + z⁻²) + 35(z + z⁻¹) + 50 = 16w^3 + 24w^2 - 13w + 2` for
   `w = z + z⁻¹`, together with its exact cubic discriminant `-80000 = -2^7 * 5^4` and the
   `45 + 28 = 73` resurgence audit partition.
5. `qou-6hzr`: Separation between an equational ODE Stokes term `aEq * df` (which vanishes
   when `aEq = 0`, as for an entire EGF at `q = 1`) and a co-equational coefficient-plane
   bridge `aCoeq * gK` (which remains non-zero whenever `aCoeq ≠ 0 ∧ gK ≠ 0`).
-/
import Mathlib.Tactic

namespace QOU.MassTheory.ResurgenceCasoratianAndBarSymmetrization

/-! ### 1. `8we6`: Casoratian Determinant Antisymmetry & `H_4` Route-A Decoupling Shifts -/

/-- Two-channel Casoratian determinant `W_k = cEvenK * cOddNext - cEvenNext * cOddK`
for the `u`-rung tie decision (`8we6`). -/
def rungCasoratian (cEvenK cOddK cEvenNext cOddNext : ℚ) : ℚ :=
  cEvenK * cOddNext - cEvenNext * cOddK

/-- Sum of the three `H_4` Route-A `c_2` decoupling-gate shifts (`sA1`, `sA2`, `sA3`) (`8we6`). -/
def routeADecouplingShiftSum (sA1 sA2 sA3 : ℚ) : ℚ :=
  sA1 + sA2 + sA3

/-- Exact antisymmetry of `rungCasoratian` under swapping the even and odd channels,
vanishing on proportional rungs (`cEvenNext = r * cEvenK`, `cOddNext = r * cOddK`), and
the exact `H_4` Route-A `c_2` shift sum `12 + 13/6 + (-40) = -155 / 6 ≠ 0` (`8we6`). -/
theorem casoratian_antisymmetry_and_routeA_shifts
    (cEvenK cOddK cEvenNext cOddNext r : ℚ) :
    rungCasoratian cOddK cEvenK cOddNext cEvenNext =
      -rungCasoratian cEvenK cOddK cEvenNext cOddNext ∧
    rungCasoratian cEvenK cOddK (r * cEvenK) (r * cOddK) = 0 ∧
    routeADecouplingShiftSum 12 (13 / 6) (-40) = -155 / 6 ∧
    routeADecouplingShiftSum 12 (13 / 6) (-40) ≠ 0 := by
  unfold rungCasoratian routeADecouplingShiftSum
  refine ⟨by ring, by ring, by norm_num, by norm_num⟩

/-! ### 2. `qou-2qt2`: Bar-Symmetrization Decomposition & Bar-Even-Channel Falsifier -/

/-- Bar-even projection `(fQ + fQInv) / 2` under the bar involution `q ↔ q⁻¹` (`qou-2qt2`). -/
def barEvenHalf (fQ fQInv : ℚ) : ℚ :=
  (fQ + fQInv) / 2

/-- Bar-odd projection `(fQ - fQInv) / 2` under the bar involution `q ↔ q⁻¹` (`qou-2qt2`). -/
def barOddHalf (fQ fQInv : ℚ) : ℚ :=
  (fQ - fQInv) / 2

/-- Exact bar-symmetrization decomposition `barEvenHalf + barOddHalf = fQ`, involution
parity `barEvenHalf fQInv fQ = barEvenHalf fQ fQInv` and `barOddHalf fQInv fQ = -barOddHalf fQ fQInv`,
and the bar-even-channel falsifier `barOddHalf fQ fQ = 0` (`qou-2qt2`). -/
theorem bar_symmetrization_identity_and_even_falsifier (fQ fQInv : ℚ) :
    barEvenHalf fQ fQInv + barOddHalf fQ fQInv = fQ ∧
    barEvenHalf fQInv fQ = barEvenHalf fQ fQInv ∧
    barOddHalf fQInv fQ = -barOddHalf fQ fQInv ∧
    barOddHalf fQ fQ = 0 := by
  unfold barEvenHalf barOddHalf
  refine ⟨by ring, by ring, by ring, by ring⟩

/-! ### 3. `qou-3cgi`: `C1` Newton-Polygon Slope `1/2` vs GGM Stokes Slopes `{-1, +1}` -/

/-- Quadratic `q`-Gevrey exponent `thetaHalf(m) = m * (m - 1) / 2` (`θ = ½ C(m, 2)`)
for the `C1` prolongation leg (`qou-3cgi`). -/
def thetaHalf (m : ℚ) : ℚ :=
  m * (m - 1) / 2

/-- First-difference identity `thetaHalf(m + 1) - thetaHalf(m) = m`, second-difference
slope `1`, and strict separation of the `C1` slope `1 / 2` from the GGM Stokes slopes
`{-1, 1}` (`qou-3cgi`). -/
theorem thetaHalf_difference_and_slope_separation (m : ℚ) :
    thetaHalf (m + 1) - thetaHalf m = m ∧
    (thetaHalf (m + 2) - thetaHalf (m + 1)) - (thetaHalf (m + 1) - thetaHalf m) = 1 ∧
    (1 : ℚ) / 2 ≠ -1 ∧
    (1 : ℚ) / 2 ≠ 1 ∧
    ((1 : ℚ) - 1 / 2) + (1 / 2 - (-1)) = 2 := by
  unfold thetaHalf
  refine ⟨by ring, by ring, by norm_num, by norm_num, by norm_num⟩

/-! ### 4. `qou-3qla`: Palindromic Reduction of the Colour-Cubic Sextic & `-80000` Discriminant -/

/-- Reduced cubic `16*w^3 + 24*w^2 - 13*w + 2` in `w = z + 1/z` obtained from the
palindromic colour-cubic discriminant sextic `(16, 24, 35, 50, 35, 24, 16)` (`qou-3qla`). -/
def bringPalindromicReducedCubic (w : ℚ) : ℚ :=
  16 * w ^ 3 + 24 * w ^ 2 - 13 * w + 2

/-- Cubic discriminant `18abcd - 4b^3d + b^2c^2 - 4ac^3 - 27a^2d^2` (`qou-3qla`). -/
def cubicDiscriminant (a b c d : ℚ) : ℚ :=
  18 * a * b * c * d - 4 * b ^ 3 * d + b ^ 2 * c ^ 2 - 4 * a * c ^ 3 - 27 * a ^ 2 * d ^ 2

/-- For any `z ≠ 0`, dividing the palindromic sextic
`16*z^6 + 24*z^5 + 35*z^4 + 50*z^3 + 35*z^2 + 24*z + 16` by `z^3` equals
`bringPalindromicReducedCubic (z + 1 / z)`, its cubic discriminant is
`-80000 = -(2^7 * 5^4)`, and the resurgence audit census partitions as `45 + 28 = 73` (`qou-3qla`). -/
theorem bring_sextic_palindromic_reduction_and_discriminant (z : ℚ) (hz : z ≠ 0) :
    (16 * z ^ 6 + 24 * z ^ 5 + 35 * z ^ 4 + 50 * z ^ 3 + 35 * z ^ 2 + 24 * z + 16) / z ^ 3 =
      bringPalindromicReducedCubic (z + 1 / z) ∧
    cubicDiscriminant 16 24 (-13) 2 = -80000 ∧
    -(2 ^ 7 * 5 ^ 4 : ℚ) = -80000 ∧
    (45 : ℚ) + 28 = 73 := by
  unfold bringPalindromicReducedCubic cubicDiscriminant
  refine ⟨?_, by norm_num, by norm_num, by norm_num⟩
  field_simp [hz]
  ring

/-! ### 5. `qou-6hzr`: Co-Equational vs Equational Bridge Separation (G4) -/

/-- Combined bridge response `aEq * df + aCoeq * gK` separating the equational ODE
Stokes multiplier `aEq` from the co-equational coefficient-plane Stokes constant `aCoeq`
(`qou-6hzr`). -/
def combinedBridgeResponse (aEq df aCoeq gK : ℚ) : ℚ :=
  aEq * df + aCoeq * gK

/-- When the equational Stokes multiplier vanishes (`aEq = 0`, as for the entire binding
EGF `e^{x + x^2/2}` at `q = 1`), `combinedBridgeResponse 0 df aCoeq gK` reduces identically
to the co-equational coefficient term `aCoeq * gK`, which is non-zero whenever
`aCoeq ≠ 0 ∧ gK ≠ 0` (`qou-6hzr`). -/
theorem coequational_bridge_survival_at_vanishing_equational_stokes
    (df aCoeq gK : ℚ) (hA : aCoeq ≠ 0) (hG : gK ≠ 0) :
    combinedBridgeResponse 0 df aCoeq gK = aCoeq * gK ∧
    combinedBridgeResponse 0 df aCoeq gK ≠ 0 := by
  unfold combinedBridgeResponse
  refine ⟨by ring, ?_⟩
  have hmul : aCoeq * gK ≠ 0 := mul_ne_zero hA hG
  simpa using hmul

end QOU.MassTheory.ResurgenceCasoratianAndBarSymmetrization
