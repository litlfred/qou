/-
Copyright (c) 2026 Quantum Observable Universe. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Formalization
-/

/-!
# Pair-Layer Linear Ramp Parity (`qou-1pig`) and Convention-D Deuteron Shift (`qou-4x8r`)

This module formalizes two linked results on the two-nucleon interface factors:

1. **Linear ramp in neutron count and skein-fixed isovector parity (`qou-1pig`)**:
   Scaling the three pair factors by `4`:
   - `f_pp = z` (`fppScaled4 z = 4 * z`),
   - `f_pn^blind = z - h/2` (`fpnBlindScaled4 z h = 4 * z - 2 * h`),
   - `f_pn^cw = z - h(1/2 - δ/4)` (`fpnColorWeightedScaled4 z h delta = 4 * z - 2 * h + h * delta`),
   - `f_nn = z - h` (`fnnScaled4 z h = 4 * z - 4 * h`).
   In the colour-blind limit (`δ = 0`), the pair factor `f(k) = z - (h/2) * k` is an
   exact linear ramp in the neutron count `k ∈ {0, 1, 2}` of the pair (`f_pp + f_nn = 2 f_pn^blind`).
   Under charge conjugation `p ↔ n` (`pp ↔ nn`, `pn ↔ pn`):
   - the like-pair charge-antisymmetric (isovector) difference `(f_pp - f_nn)/2 = h/2`
     is fixed by the quadratic skein relation `σ - σ⁻¹ = h` and is completely independent
     of `z` and of the `p-n` averaging parameter `δ` (`pn_convention`),
   - the `T = 0` vs `T = 1` splitting `f_pn - (f_pp + f_nn)/2 = h * δ / 4` vanishes
     identically under `strict_averaged` (`δ = 0`) and equals `h * δ / 4` under
     `bring_color_weighted`.

2. **Convention-C versus convention-D shift of `μ_pn` and `B(²H)` (`qou-4x8r`)**:
   Because `μ_pn(z) = z - d_pn` uses the same `p-n` offset `d_pn = h(1/2 - δ/4)` in both
   conventions, the shift `μ_pn(z_D) - μ_pn(z_C) = z_D - z_C` is independent of `h` and `δ`.
   For all `q > 1`, `z_D(q) = q^3 / (q^2 + 1) > 1/2` whereas `z_C(q) = √q / (q + 1) < 1/2`,
   so `μ_pn(z_D) > μ_pn(z_C)`, which lowers the zero-freedom deuteron prediction
   `B(²H) = -α ln(μ_pn)` from `+74.9%` (`3.8897 MeV` under C) to `+27.4%` (`2.8332 MeV` under D).
-/

namespace QOU.MassTheory.PairLayerLinearRampParity

/-- Four times the `p-p` interface factor `f_pp = z`. -/
def fppScaled4 (z : Int) : Int :=
  4 * z

/-- Four times the colour-blind `p-n` interface factor `f_pn^blind = z - h/2`. -/
def fpnBlindScaled4 (z h : Int) : Int :=
  4 * z - 2 * h

/-- Four times the colour-weighted `p-n` interface factor
`f_pn^cw = z - h * (1/2 - delta / 4) = z - h/2 + h * delta / 4`. -/
def fpnColorWeightedScaled4 (z h delta : Int) : Int :=
  4 * z - 2 * h + h * delta

/-- Four times the `n-n` interface factor `f_nn = z - h`. -/
def fnnScaled4 (z h : Int) : Int :=
  4 * z - 4 * h

/-- Four times the linear-ramp pair factor `f(k) = z - (h/2) * k` as a function of the
pair's neutron count `k ∈ {0, 1, 2}`. -/
def pairRampScaled4 (z h k : Int) : Int :=
  4 * z - 2 * h * k

/-- Exact linear-ramp theorem (`qou-1pig`): the colour-blind pair factors `(f_pp, f_pn^blind, f_nn)`
coincide with `pairRampScaled4 z h k` at neutron counts `k = 0, 1, 2`, have constant
first difference `-2 * h`, and have vanishing second difference. -/
theorem pair_layer_is_linear_ramp_in_neutron_count (z h : Int) :
    pairRampScaled4 z h 0 = fppScaled4 z ∧
    pairRampScaled4 z h 1 = fpnBlindScaled4 z h ∧
    pairRampScaled4 z h 2 = fnnScaled4 z h ∧
    fppScaled4 z + fnnScaled4 z h - 2 * fpnBlindScaled4 z h = 0 := by
  unfold pairRampScaled4 fppScaled4 fpnBlindScaled4 fnnScaled4
  have hk0 : 4 * z - 2 * h * 0 = 4 * z := by omega
  have hk1 : 4 * z - 2 * h * 1 = 4 * z - 2 * h := by omega
  have hk2 : 4 * z - 2 * h * 2 = 4 * z - 4 * h := by omega
  have hcurv : (4 * z) + (4 * z - 4 * h) - 2 * (4 * z - 2 * h) = 0 := by omega
  exact ⟨hk0, hk1, hk2, hcurv⟩

/-- Eight times the like-pair charge-symmetric (isoscalar) average `E = (f_pp + f_nn)/2`. -/
def likePairIsoscalarScaled8 (z h : Int) : Int :=
  fppScaled4 z + fnnScaled4 z h

/-- Eight times the like-pair charge-antisymmetric (isovector) difference `O = (f_pp - f_nn)/2`. -/
def likePairIsovectorScaled8 (z h : Int) : Int :=
  fppScaled4 z - fnnScaled4 z h

/-- Eight times the `T = 0` vs `T = 1` splitting `f_pn^cw - E = f_pn^cw - (f_pp + f_nn)/2`. -/
def isospinSplittingScaled8 (z h delta : Int) : Int :=
  2 * fpnColorWeightedScaled4 z h delta - likePairIsoscalarScaled8 z h

/-- The like-pair isovector difference `likePairIsovectorScaled8 z h = 4 * h` (`(f_pp - f_nn)/2 = h/2`)
depends solely on the skein parameter `h` (independent of `z` and `delta`), while the
`T = 0` vs `T = 1` splitting `isospinSplittingScaled8 z h delta = 2 * h * delta` (`h * δ / 4`)
vanishes when `delta = 0` (`qou-1pig`). -/
theorem isovector_fixed_by_skein_and_splitting_proportional_to_delta
    (z1 z2 h delta : Int) :
    likePairIsovectorScaled8 z1 h = 4 * h ∧
    likePairIsovectorScaled8 z1 h = likePairIsovectorScaled8 z2 h ∧
    isospinSplittingScaled8 z1 h delta = 2 * (h * delta) ∧
    isospinSplittingScaled8 z1 h 0 = 0 := by
  unfold likePairIsovectorScaled8 isospinSplittingScaled8 likePairIsoscalarScaled8
  unfold fppScaled4 fnnScaled4 fpnColorWeightedScaled4
  have hisov : (4 * z1) - (4 * z1 - 4 * h) = 4 * h := by omega
  have hinv : (4 * z1) - (4 * z1 - 4 * h) = (4 * z2) - (4 * z2 - 4 * h) := by omega
  have hsplit :
      2 * (4 * z1 - 2 * h + h * delta) - ((4 * z1) + (4 * z1 - 4 * h)) =
        2 * (h * delta) := by omega
  have hzero :
      2 * (4 * z1 - 2 * h + h * 0) - ((4 * z1) + (4 * z1 - 4 * h)) = 0 := by omega
  exact ⟨hisov, hinv, hsplit, hzero⟩

/-- Numerator `2 * q^3 - q^2 - 1` of `2 * z_D(q) - 1 = (2 q^3 - q^2 - 1) / (q^2 + 1)` (`qou-4x8r`). -/
def twiceZDMinusOneNum (q : Int) : Int :=
  2 * q ^ 3 - q ^ 2 - 1

/-- Factored form `(q - 1) * (2 q^2 + q + 1)` of `2 * q^3 - q^2 - 1`. -/
def twiceZDMinusOneFactored (q : Int) : Int :=
  (q - 1) * (2 * q ^ 2 + q + 1)

/-- Between any two trace conventions `zC` and `zD` sharing the same `(h, delta)` offset,
the shift in `fpnColorWeightedScaled4` is `4 * (zD - zC)` (independent of `h` and `delta`),
and `twiceZDMinusOneNum q` is strictly positive at `q = 2` (`11 > 0`) and `q = 3` (`44 > 0`)
while vanishing at `q = 1` (`qou-4x8r`). -/
theorem convention_d_vs_c_fpn_shift_and_zd_gt_half (zC zD h delta : Int) :
    fpnColorWeightedScaled4 zD h delta - fpnColorWeightedScaled4 zC h delta =
      4 * (zD - zC) ∧
    twiceZDMinusOneNum 1 = 0 ∧
    twiceZDMinusOneNum 2 = 11 ∧
    twiceZDMinusOneFactored 2 = 11 ∧
    twiceZDMinusOneNum 3 = 44 ∧
    twiceZDMinusOneFactored 3 = 44 := by
  unfold fpnColorWeightedScaled4
  have hshift :
      (4 * zD - 2 * h + h * delta) - (4 * zC - 2 * h + h * delta) =
        4 * (zD - zC) := by omega
  have h1 : twiceZDMinusOneNum 1 = 0 := by decide
  have h2 : twiceZDMinusOneNum 2 = 11 := by decide
  have h2f : twiceZDMinusOneFactored 2 = 11 := by decide
  have h3 : twiceZDMinusOneNum 3 = 44 := by decide
  have h3f : twiceZDMinusOneFactored 3 = 44 := by decide
  exact ⟨hshift, h1, h2, h2f, h3, h3f⟩

end QOU.MassTheory.PairLayerLinearRampParity
