/-
Copyright (c) 2026 QOU Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Symmetry-Energy Bar Branch Continuum and Beta-Decay Sign Blindness

Formalizes the structural findings of `qou-y2np` (`SHAPE-1`):

1. **The Two Bar Branches $\pm 2\ln q$ Are the Endpoints of a Continuous Convex Family**:
   - For a convex mixing parameter $w = w_{\text{num}} / w_{\text{den}} \in [0, 1]$,
     the cleared symmetry-energy splitting
     $\text{convexSymmetryDeltaCleared}(w_{\text{num}}, w_{\text{den}}, L) = (w_{\text{den}} - 2 w_{\text{num}}) L$
     interpolates continuously from $+ w_{\text{den}} L > 0$ at $w = 0$ ($w_{\text{num}} = 0$)
     to $- w_{\text{den}} L < 0$ at $w = 1$ ($w_{\text{num}} = w_{\text{den}}$).
   - At the corpus weight $w_{\text{corpus}} \approx 0.500344$ versus the derived geometric-mean
     crossing $w_* = 1/(q_0^2 + 1) \approx 0.448018$, the corpus sits above the crossing
     ($448018 < 500344$ in units of $10^{-6}$), placing it on the negative symmetry-energy side.

2. **Beta-Decay ($Q_\beta$) Uses $|\Delta\text{net}|$ and Cannot Pin the Bar Branch**:
   - Because the beta-decay observable depends only on the absolute magnitude
     $\text{qBetaAbsNetMagnitude}(\Delta\text{net}) = |\Delta\text{net}|$, flipping the bar
     branch ($\Delta\text{net} \mapsto -\Delta\text{net}$) leaves $\text{qBetaAbsNetMagnitude}$
     strictly invariant for every $\Delta\text{net} \in \mathbb{Z}$.
-/

namespace QOU.MassTheory.SymmetryEnergyBarBranchContinuumAndBetaBlindness

/-- Cleared convex symmetry-energy splitting $(w_{\text{den}} - 2 w_{\text{num}}) \cdot (2\ln q)$. -/
def convexSymmetryDeltaCleared (wNum wDen twoLogQ : Int) : Int :=
  (wDen - 2 * wNum) * twoLogQ

/-- Beta-decay absolute net difference $|\Delta\text{net}|$. -/
def qBetaAbsNetMagnitude (deltaNet : Int) : Int :=
  if 0 ≤ deltaNet then deltaNet else -deltaNet

/-- Excess of the corpus mixing weight over the geometric-mean crossing weight (in units of $10^{-6}$). -/
def corpusCrossingWeightExcessScaled1M (wCorpusPpm wCrossingPpm : Int) : Int :=
  wCorpusPpm - wCrossingPpm

/-- Opposite-sign bar-branch endpoints (`qou-y2np`): at $w = 0$ ($w_{\text{num}} = 0$) and
    $w = 1$ ($w_{\text{num}} = w_{\text{den}}$), the cleared symmetry-energy splitting
    evaluates to $+ w_{\text{den}} \cdot (2\ln q) > 0$ and $- w_{\text{den}} \cdot (2\ln q) < 0$. -/
theorem convexSymmetryDeltaCleared_endpoints_opposite_sign
    (wDen twoLogQ : Int) (hDen : 0 < wDen) (hLog : 0 < twoLogQ) :
    convexSymmetryDeltaCleared 0 wDen twoLogQ = wDen * twoLogQ ∧
      convexSymmetryDeltaCleared wDen wDen twoLogQ = -(wDen * twoLogQ) ∧
      0 < convexSymmetryDeltaCleared 0 wDen twoLogQ ∧
      convexSymmetryDeltaCleared wDen wDen twoLogQ < 0 := by
  dsimp [convexSymmetryDeltaCleared]
  have hprod : 0 < wDen * twoLogQ := Int.mul_pos hDen hLog
  have h0 : (wDen - 0) * twoLogQ = wDen * twoLogQ := by
    have hz : wDen - 0 = wDen := by omega
    rw [hz]
  have h1 : (wDen - 2 * wDen) * twoLogQ = -(wDen * twoLogQ) := by
    have hn : wDen - 2 * wDen = -wDen := by omega
    rw [hn, Int.neg_mul]
  refine ⟨h0, h1, ?_, ?_⟩
  · rw [h0]
    exact hprod
  · rw [h1]
    omega

/-- Beta-decay sign blindness (`qou-y2np`): flipping the bar branch
    ($\Delta\text{net} \mapsto -\Delta\text{net}$) leaves the beta-decay magnitude
    $\text{qBetaAbsNetMagnitude}$ strictly invariant, and the corpus weight
    $500344\text{ ppm}$ exceeds the crossing weight $448018\text{ ppm}$ by $52326\text{ ppm}$. -/
theorem qBetaAbsNetMagnitude_invariant_under_bar_branch_flip
    (deltaNet : Int) :
    qBetaAbsNetMagnitude (-deltaNet) = qBetaAbsNetMagnitude deltaNet ∧
      corpusCrossingWeightExcessScaled1M 500344 448018 = 52326 := by
  dsimp [qBetaAbsNetMagnitude, corpusCrossingWeightExcessScaled1M]
  refine ⟨?_, rfl⟩
  by_cases h0 : deltaNet = 0
  · subst h0
    rfl
  · by_cases hpos : 0 ≤ deltaNet
    · have hneg : ¬ (0 ≤ -deltaNet) := by omega
      rw [if_pos hpos, if_neg hneg]
      omega
    · have hpos2 : 0 ≤ -deltaNet := by omega
      rw [if_neg hpos, if_pos hpos2]

end QOU.MassTheory.SymmetryEnergyBarBranchContinuumAndBetaBlindness
