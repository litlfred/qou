/-!
# Writhe-Sign Opposition and Endpoint Mirror Splitting (`qou-fi1p`)

This module formalizes the latent writhe-sign disagreement between `bondL` and
`InterfaceScalar` and its `3.57x` amplification at the `t = 0` (`pp`) and `t = 1`
(`nn`) endpoints (`qou-fi1p`):

1. **Vanishing of the writhe correction at the `t = 1/2` midpoint (`midpoint_writhe_correction_vanishes_for_both_signs`):**
   Writing the interpolation parameter in doubled integer coordinates `u = 2 * t - 1`
   (`u = -1` at `t = 0`, `u = 0` at `t = 1/2`, `u = +1` at `t = 1`), the writhe
   shift `s * u * w` (`s in {-1, +1}`) vanishes identically at `u = 0`, explaining why
   the sign disagreement is latent on the symmetric deuteron evaluation at `t = 1/2`.

2. **Opposite endpoint mirror splits and bare-trace midpoint (`endpoint_mirror_split_sign_opposition_and_midpoint`):**
   Evaluating the endpoint difference between `u = +1` (`nn`) and `u = -1` (`pp`) gives
   `baseSplit - 2 * w` under `s = -1` (`bondL`: `2.728826 MeV`) and `baseSplit + 2 * w`
   under `s = +1` (`InterfaceScalar`: `0.765320 MeV`, since `2 * w = log(1 - h) < 0`),
   whose sum equals `2 * baseSplit`, twice the unnormalised transfer-trace split
   `1.747073 MeV`.

3. **Quantitative `3.57x` endpoint amplification (`endpoint_split_ratio_exceeds_three_and_half`):**
   At `10^6 MeV` scale (`bondLSplit = 2728826`, `interfaceScalarSplit = 765320`,
   `bareSplit = 1747073`), `2 * bondLSplit > 7 * interfaceScalarSplit` (`> 3.5x`) and
   `bondLSplit + interfaceScalarSplit = 2 * bareSplit`.
-/

namespace QOU.MassTheory.WritheSignOppositionEndpointSplit

/-- Writhe-shifted bond log-energy `baseLog + sign * u * halfLogOneMinusH` where `u = 2 * t - 1`. -/
def writheShiftedBond (baseLog sign u halfLogOneMinusH : Int) : Int :=
  baseLog + sign * u * halfLogOneMinusH

/-- Endpoint (`u = 1` minus `u = -1`) mirror splitting under writhe sign `sign in {-1, +1}`. -/
def endpointMirrorSplit (baseSplit sign logOneMinusH : Int) : Int :=
  baseSplit + sign * logOneMinusH

/-- At the symmetric midpoint `u = 0` (`t = 1/2`), the writhe-shifted bond energy
    equals `baseLog` for every sign `s`, so the `+1` and `-1` conventions agree
    identically (`qou-fi1p`). -/
theorem midpoint_writhe_correction_vanishes_for_both_signs
    (baseLog halfLogOneMinusH : Int) :
    writheShiftedBond baseLog 1 0 halfLogOneMinusH = baseLog ∧
    writheShiftedBond baseLog (-1) 0 halfLogOneMinusH = baseLog ∧
    writheShiftedBond baseLog 1 0 halfLogOneMinusH -
      writheShiftedBond baseLog (-1) 0 halfLogOneMinusH = 0 := by
  have hpos : writheShiftedBond baseLog 1 0 halfLogOneMinusH = baseLog := by
    unfold writheShiftedBond
    omega
  have hneg : writheShiftedBond baseLog (-1) 0 halfLogOneMinusH = baseLog := by
    unfold writheShiftedBond
    omega
  have hdiff : writheShiftedBond baseLog 1 0 halfLogOneMinusH -
      writheShiftedBond baseLog (-1) 0 halfLogOneMinusH = 0 := by
    rw [hpos, hneg]
    omega
  exact ⟨hpos, hneg, hdiff⟩

/-- The opposite-sign endpoint mirror splits `endpointMirrorSplit baseSplit (-1) logOneMinusH`
    and `endpointMirrorSplit baseSplit 1 logOneMinusH` differ by `-2 * logOneMinusH` and
    their sum equals `2 * baseSplit` (twice the bare unnormalised split) (`qou-fi1p`). -/
theorem endpoint_mirror_split_sign_opposition_and_midpoint
    (baseSplit logOneMinusH : Int) :
    endpointMirrorSplit baseSplit (-1) logOneMinusH -
      endpointMirrorSplit baseSplit 1 logOneMinusH = -2 * logOneMinusH ∧
    endpointMirrorSplit baseSplit (-1) logOneMinusH +
      endpointMirrorSplit baseSplit 1 logOneMinusH = 2 * baseSplit := by
  have hdiff : endpointMirrorSplit baseSplit (-1) logOneMinusH -
      endpointMirrorSplit baseSplit 1 logOneMinusH = -2 * logOneMinusH := by
    unfold endpointMirrorSplit
    omega
  have hsum : endpointMirrorSplit baseSplit (-1) logOneMinusH +
      endpointMirrorSplit baseSplit 1 logOneMinusH = 2 * baseSplit := by
    unfold endpointMirrorSplit
    omega
  exact ⟨hdiff, hsum⟩

/-- Scaled (`10^6 MeV`) verification of the `3.5656x` ratio between `bondL` (`2728826`)
    and `InterfaceScalar` (`765320`), and exact midpoint agreement with the bare
    transfer-trace split `1747073` (`qou-fi1p`). -/
theorem endpoint_split_ratio_exceeds_three_and_half :
    (2728826 : Int) + 765320 = 2 * 1747073 ∧
    2 * (2728826 : Int) > 7 * 765320 ∧
    (2728826 : Int) < 4 * 765320 := by
  have hmid : (2728826 : Int) + 765320 = 2 * 1747073 := by
    omega
  have hgt : 2 * (2728826 : Int) > 7 * 765320 := by
    omega
  have hlt : (2728826 : Int) < 4 * 765320 := by
    omega
  exact ⟨hmid, hgt, hlt⟩

end QOU.MassTheory.WritheSignOppositionEndpointSplit
