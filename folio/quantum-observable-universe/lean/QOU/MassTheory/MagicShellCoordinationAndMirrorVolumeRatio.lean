/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Lane
-/

namespace QOU.MassTheory.MagicShellCoordinationAndMirrorVolumeRatio

/-!
# Magic-Shell Coordination Regime Gap & $A = 3$ Mirror Volume Ratio (`qou-fcn8`, `qou-fmfw`)

This module formalizes two structural results under `qou-v2om`:

1. **`qou-fcn8` (Forced-Chain $A - 1$ vs Magic-Shell $2 A$ Coordination Gap & $I_3 = 0$ Channel Blindness):**
   - Under the 3-strands-per-nucleon linear chain layout, a nucleus of mass number $A \ge 2$
     carries $M_{\mathrm{chain}}(A) = A - 1$ inter-nucleon bonds, whereas a saturated
     coordination-$2$ regime carries $M_{\mathrm{magic}}(A) = 2 A$ bond units.
   - The bond-count deficit $M_{\mathrm{magic}}(A) - M_{\mathrm{chain}}(A) = A + 1$ is
     strictly greater than $A$, and $M_{\mathrm{magic}}(A) - 2 M_{\mathrm{chain}}(A) = 2$
     for all $A \ge 2$.
   - Under the third-isospin inter-nucleon linking assignment $\mathrm{lk}(pp) = +1$,
     $\mathrm{lk}(nn) = -1$, $\mathrm{lk}(pn) = 0$, any symmetric $N = Z$ nucleus has
     equal $pp$ and $nn$ pair counts ($n_{pp} = n_{nn}$), so its net linking sum vanishes
     identically (`netI3LinkingSum 1 (-1) nPP nPP = 0`), establishing Route-2 channel
     blindness on all $N = Z$ magic shells ($^4\mathrm{He}, ^{16}\mathrm{O}, ^{40}\mathrm{Ca}$).

2. **`qou-fmfw` (Scale-Free $T / ^3\mathrm{He}$ Mirror Volume Ratio vs Deuteron Hopf Volume Blocker):**
   - For any linear-in-volume binding law $B_{\mathrm{Vol}}(K) = c \cdot \mathrm{Vol}(K)$,
     the cross-multiplied mirror ratio satisfies
     $B_{\mathrm{Vol}}(T) \cdot \mathrm{Vol}(^3\mathrm{He}) = B_{\mathrm{Vol}}(^3\mathrm{He}) \cdot \mathrm{Vol}(T)$
     for every scale factor $c \in \mathbb{Z}$.
   - Using the 7-digit hyperbolic volumes scaled by $10^7$ ($\mathrm{Vol}(8_{11}) = 82863168$
     for $T$ and $\mathrm{Vol}(L6a4) = 73277248$ for $^3\mathrm{He}$), the pure-volume ratio
     lies strictly above unity ($\mathrm{Vol}(8_{11}) > \mathrm{Vol}(L6a4)$) on the same
     side of $1$ as the experimental AME2020 ratio ($10990 > 10000$), whereas the
     $\mathrm{Vol} \cdot \mathrm{tr}_M$ ratio ($5700 < 10000$) is anti-correlated.
   - However, because the deuteron Hopf closure $L2a1$ is non-hyperbolic with
     volume $\mathrm{Vol}(L2a1) = 0$, any pure-volume law gives $B_{\mathrm{Vol}}(^2\mathrm{H}) = 0$,
     blocking extension to all four L2 targets without a non-hyperbolic term.
-/

/-- Forced 1D chain bond count $M_{\mathrm{chain}}(A) = A - 1$ (`qou-fcn8`). -/
def chainBondCount (A : Int) : Int :=
  A - 1

/-- Coordination-$2$ magic-shell bond count $M_{\mathrm{magic}}(A) = 2 A$ (`qou-fcn8`). -/
def magicTwoBondCount (A : Int) : Int :=
  2 * A

/-- Exact coordination deficit $M_{\mathrm{magic}}(A) - M_{\mathrm{chain}}(A) = A + 1$
and asymptotic ratio excess $M_{\mathrm{magic}}(A) - 2 M_{\mathrm{chain}}(A) = 2$ (`qou-fcn8`). -/
theorem magicTwo_minus_chain_identities (A : Int) (hA : A ≥ 2) :
    magicTwoBondCount A - chainBondCount A = A + 1 ∧
      magicTwoBondCount A - 2 * chainBondCount A = 2 ∧
      magicTwoBondCount A > chainBondCount A := by
  dsimp [magicTwoBondCount, chainBondCount]
  refine ⟨by omega, by omega, by omega⟩

/-- Net inter-nucleon $I_3$ linking sum $w_{pp} n_{pp} + w_{nn} n_{nn}$ across charged/neutral
like-nucleon pairs (`qou-fcn8`). -/
def netI3LinkingSum (wPP wNN nPP nNN : Int) : Int :=
  wPP * nPP + wNN * nNN

/-- Route-2 channel blindness (`qou-fcn8`): under opposite like-nucleon linking weights
$w_{pp} + w_{nn} = 0$ (such as $w_{pp} = +1, w_{nn} = -1$) and equal pair counts
$n_{pp} = n_{nn}$ (every $N = Z$ closed-shell nucleus), the net $I_3$ linking sum vanishes. -/
theorem netI3LinkingSum_eq_zero_of_nPP_eq_nNN (wPP wNN nPP : Int) (hOpp : wPP + wNN = 0) :
    netI3LinkingSum wPP wNN nPP nPP = 0 := by
  dsimp [netI3LinkingSum]
  rw [← Int.add_mul, hOpp, Int.zero_mul]

/-- Pure-volume binding law $B_{\mathrm{Vol}}(c, V) = c \cdot V$ (`qou-fmfw`). -/
def pureVolumeBinding (c V : Int) : Int :=
  c * V

/-- Scale-cancellation identity (`qou-fmfw`) and fibred-torus Hopf volume blocker
($V_{\mathrm{Hopf}} = 0 \implies B_{\mathrm{Vol}}(c, 0) = 0$). -/
theorem pureVolumeBinding_scale_cancels_and_hopf_zero (c VT VHe3 : Int) :
    pureVolumeBinding c VT * VHe3 = pureVolumeBinding c VHe3 * VT ∧
      pureVolumeBinding c 0 = 0 := by
  dsimp [pureVolumeBinding]
  refine ⟨?_, Int.mul_zero c⟩
  rw [Int.mul_assoc, Int.mul_assoc, Int.mul_comm VT VHe3]

/-- SnapPy 7-digit hyperbolic volume of $8_{11}$ (Triton candidate) scaled by $10^7$ (`qou-fmfw`). -/
def volTriton811Scaled : Int := 82863168

/-- SnapPy 7-digit hyperbolic volume of Borromean link $L6a4$ ($^3\mathrm{He}$ candidate) scaled by $10^7$ (`qou-fmfw`). -/
def volHelium3BorromeanScaled : Int := 73277248

/-- AME2020 mirror binding ratio $B(T)/B(^3\mathrm{He}) = 1.0990$ scaled by $10^4$, and
PR #4610 $\mathrm{Vol}\cdot\mathrm{tr}_M$ ratio $0.5700$ scaled by $10^4$ (`qou-fmfw`). -/
def ameMirrorRatioScaled : Int := 10990
def volTrMMirrorRatioScaled : Int := 5700
def ratioUnityScaled : Int := 10000

/-- On the $T / ^3\mathrm{He}$ mirror pair, both the AME binding ratio and the pure-volume
ratio exceed unity (co-directional, with cross-multiplied spread $< 3\%$), whereas
$\mathrm{Vol}\cdot\mathrm{tr}_M$ sits strictly below unity (`qou-fmfw`). -/
theorem mirrorPair_volume_coDirectional_and_within_three_percent :
    volTriton811Scaled > volHelium3BorromeanScaled ∧
      ameMirrorRatioScaled > ratioUnityScaled ∧
      volTrMMirrorRatioScaled < ratioUnityScaled ∧
      (volTriton811Scaled * ratioUnityScaled - volHelium3BorromeanScaled * ameMirrorRatioScaled) * 100 <
        3 * (volHelium3BorromeanScaled * ameMirrorRatioScaled) ∧
      volTriton811Scaled * ratioUnityScaled > volHelium3BorromeanScaled * ameMirrorRatioScaled := by
  dsimp [volTriton811Scaled, volHelium3BorromeanScaled, ameMirrorRatioScaled,
    volTrMMirrorRatioScaled, ratioUnityScaled]
  refine ⟨by decide, by decide, by decide, by decide, by decide⟩

end QOU.MassTheory.MagicShellCoordinationAndMirrorVolumeRatio
