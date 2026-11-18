/-
Copyright (c) 2026 Quantum Observable Universe. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Quantum Observable Universe Formalization

Beans:
  - qou-r6ki: Cite 0006156v1.pdf [faddeev-kashaev-volkov2000] at prop:faddeev-phib-uniqueness
  - qou-sf0s: Cite [bilsonthompson2007] at def:strand-twist-datum
  - qou-spds: Cross-check On_the_geometry_of_two_state_models_for_the_colore.pdf [arxiv-2209.06973v1]
  - qou-ssly: Cite 2203.17029v1.pdf [garoufalidis-wheeler-modular] at prop:habiro-tail-archimedean-action
  - qou-t579: Cross-check gn2.pdf [gelca-nagasato] at computations/complex_volume_witness.py
-/

/-!
# Modular-Double Shift Ratios, Braided Ribbon Twist Conservation & 3-Braid State Sums (Round 67)

This module formalizes five algebraic and structural cross-checks for Round 67:

1. **Modular-double shift denominators and half-lattice index reciprocity (`qou-r6ki`,
   `[faddeev-kashaev-volkov2000]`):**
   Establishes the cleared two-step multiplicative shift factor `(1 + w)(1 + q^2 w)` and the
   transposition reciprocity of the half-integer zero/pole lattice index
   `(2 m + 1) b^2 + (2 n + 1)`.

2. **Braided 3-ribbon twist spread and coupled writhe charge conservation (`qou-sf0s`,
   `[bilsonthompson2007]`):**
   Proves that under uniform framing-writhe slide moves `(t_1 - d, t_2 - d, t_3 - d, w + d)`,
   both the pairwise twist spread `(t_1 - t_2)^2 + (t_2 - t_3)^2 + (t_3 - t_1)^2` and the
   coupled topological charge `t_1 + t_2 + t_3 + 3 w` are strictly conserved, and verifies
   the quark-like `(2, 2, -1)` (`spread = 18`, `total = 3`) vs lepton-like `(-2, -2, -2)`
   (`spread = 0`, `total = -6`) twist sectors.

3. **Two-state 3-braid closure trace identities for `k = 1, 2, 3` (`qou-spds`,
   `[arxiv-2209.06973v1]`):**
   Verifies the unimodular 2D channel trace recurrence `tr(X^k)` at `tr(X) = 1 - s` (`s = q + q⁻¹`)
   and proves that adding the 1D symmetric channel weight `s` recovers `1` for `k = 1`,
   `s^2 - s - 1 = q^2 - q + 1 - q⁻¹ + q⁻²` for `k = 2` (`4_1`), and `4` at the classical
   specialization `s = 2` for `k = 3` (`L6a4`).

4. **Symmetric Laurent step multiplier and cyclotomic root truncation (`qou-ssly`,
   `[garoufalidis-wheeler-modular]`):**
   Proves that the symmetric step multiplier `2 - s_k` (`s_k = q^k + q^{-k}`) vanishes at
   the root-of-unity specialization `s_k = 2` and satisfies the first-order inhomogeneous
   step difference `T_{n+1} - T_n = (1 - s_k) T_n`.

5. **Figure-eight peripheral trace-to-adjoint polynomial reduction (`qou-t579`,
   `[gelca-nagasato]`):**
   Proves that the `4_1` meridian trace polynomial `x^4 - 5 x^2 + 2` factors through the
   adjoint trace `s = x^2 - 2` as `s^2 - s - 4`, is invariant under the `t = -1` skein sign
   flip `x ↦ -x`, and evaluates to `-2` at the parabolic point `x = 2` (`s = 2`).

-- Ref: [faddeev-kashaev-volkov2000]
-- Ref: [bilsonthompson2007]
-- Ref: [arxiv-2209.06973v1]
-- Ref: [garoufalidis-wheeler-modular]
-- Ref: [gelca-nagasato]
-/

namespace QOU.QBeta.ModularDoubleSkeinRibbonRound67

/-! ## 1. Modular-Double Shift Denominator & Half-Lattice Index (`qou-r6ki`) -/

/-- Cleared two-step multiplicative shift denominator `(1 + w) * (1 + qSqW)`. -/
def modularDoubleClearedTwoStepDenom (w qSqW : Int) : Int :=
  (1 + w) * (1 + qSqW)

/-- Half-integer zero/pole lattice index `(2 * m + 1) * bSq + (2 * n + 1)`. -/
def halfLatticeIndex (m n bSq : Int) : Int :=
  (2 * m + 1) * bSq + (2 * n + 1)

/-- Bilinear expansion of the two-step shift denominator and self-dual symmetry of the
    half-integer lattice index at `bSq = 1`. -/
theorem modularDouble_two_step_and_half_lattice_reciprocity (m n bSq w qSqW : Int) :
    modularDoubleClearedTwoStepDenom w qSqW = 1 + w + qSqW + w * qSqW ∧
    modularDoubleClearedTwoStepDenom 0 qSqW = 1 + qSqW ∧
    halfLatticeIndex m n 1 = halfLatticeIndex n m 1 ∧
    halfLatticeIndex m n 1 = 2 * (m + n) + 2 ∧
    halfLatticeIndex m n bSq - halfLatticeIndex n m bSq =
      (2 * m - 2 * n) * (bSq - 1) := by
  dsimp [modularDoubleClearedTwoStepDenom, halfLatticeIndex]
  have h1 : (1 + w) * (1 + qSqW) = 1 + w + qSqW + w * qSqW := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add, Int.one_mul, Int.mul_one]
    omega
  have h2 : (1 + 0) * (1 + qSqW) = 1 + qSqW := by omega
  have h3 : (2 * m + 1) * 1 + (2 * n + 1) = (2 * n + 1) * 1 + (2 * m + 1) := by omega
  have h4 : (2 * m + 1) * 1 + (2 * n + 1) = 2 * (m + n) + 2 := by omega
  have hDiffL : ((2 * m + 1) * bSq + (2 * n + 1)) - ((2 * n + 1) * bSq + (2 * m + 1)) =
      (2 * m + 1) * bSq - (2 * n + 1) * bSq - 2 * m + 2 * n := by omega
  have hDiffR : (2 * m - 2 * n) * (bSq - 1) =
      (2 * m + 1) * bSq - (2 * n + 1) * bSq - 2 * m + 2 * n := by
    rw [Int.mul_sub, Int.sub_mul, Int.add_mul, Int.add_mul, Int.one_mul, Int.mul_one]
    omega
  have h5 : ((2 * m + 1) * bSq + (2 * n + 1)) - ((2 * n + 1) * bSq + (2 * m + 1)) =
      (2 * m - 2 * n) * (bSq - 1) := by
    rw [hDiffL, hDiffR]
  exact ⟨h1, h2, h3, h4, h5⟩

/-! ## 2. Braided 3-Ribbon Twist Spread & Coupled Writhe Conservation (`qou-sf0s`) -/

/-- Total half-twist sum `t1 + t2 + t3` on a 3-ribbon triplet. -/
def ribbonTotalTwist (t1 t2 t3 : Int) : Int :=
  t1 + t2 + t3

/-- Signed cyclic difference sum `(t1 - t2) + (t2 - t3) + (t3 - t1)`. -/
def ribbonPairwiseDiffSum (t1 t2 t3 : Int) : Int :=
  (t1 - t2) + (t2 - t3) + (t3 - t1)

/-- Pairwise squared twist spread `(t1 - t2)^2 + (t2 - t3)^2 + (t3 - t1)^2`. -/
def ribbonTwistSpread (t1 t2 t3 : Int) : Int :=
  (t1 - t2) * (t1 - t2) + (t2 - t3) * (t2 - t3) + (t3 - t1) * (t3 - t1)

/-- Coupled twist-writhe topological charge `t1 + t2 + t3 + 3 * w`. -/
def ribbonWritheCoupledCharge (t1 t2 t3 w : Int) : Int :=
  t1 + t2 + t3 + 3 * w

/-- Uniform framing-writhe slide `(t_i - d, w + d)` preserves both the coupled topological
    charge and the pairwise twist spread, and separates anisotropic `(2, 2, -1)` from
    isotropic `(-2, -2, -2)` triplets. -/
theorem ribbon_twist_writhe_slide_and_sector_invariants (t1 t2 t3 w d : Int) :
    ribbonWritheCoupledCharge (t1 - d) (t2 - d) (t3 - d) (w + d) =
      ribbonWritheCoupledCharge t1 t2 t3 w ∧
    ribbonPairwiseDiffSum t1 t2 t3 = 0 ∧
    ribbonTwistSpread (t1 - d) (t2 - d) (t3 - d) = ribbonTwistSpread t1 t2 t3 ∧
    ribbonTwistSpread 2 2 (-1) = 18 ∧
    ribbonTotalTwist 2 2 (-1) = 3 ∧
    ribbonTwistSpread (-2) (-2) (-2) = 0 ∧
    ribbonTotalTwist (-2) (-2) (-2) = -6 := by
  dsimp [ribbonWritheCoupledCharge, ribbonPairwiseDiffSum, ribbonTwistSpread, ribbonTotalTwist]
  have h1 : (t1 - d) + (t2 - d) + (t3 - d) + 3 * (w + d) = t1 + t2 + t3 + 3 * w := by omega
  have h2 : (t1 - t2) + (t2 - t3) + (t3 - t1) = 0 := by omega
  have hd12 : (t1 - d) - (t2 - d) = t1 - t2 := by omega
  have hd23 : (t2 - d) - (t3 - d) = t2 - t3 := by omega
  have hd31 : (t3 - d) - (t1 - d) = t3 - t1 := by omega
  have h3 : ((t1 - d) - (t2 - d)) * ((t1 - d) - (t2 - d)) +
      ((t2 - d) - (t3 - d)) * ((t2 - d) - (t3 - d)) +
      ((t3 - d) - (t1 - d)) * ((t3 - d) - (t1 - d)) =
      (t1 - t2) * (t1 - t2) + (t2 - t3) * (t2 - t3) + (t3 - t1) * (t3 - t1) := by
    rw [hd12, hd23, hd31]
  have h4 : (2 - 2) * (2 - 2) + (2 - -1) * (2 - -1) + (-1 - 2) * (-1 - 2) = (18 : Int) := by
    omega
  have h5 : (2 : Int) + 2 + -1 = 3 := by omega
  have h6 : (-2 - -2) * (-2 - -2) + (-2 - -2) * (-2 - -2) + (-2 - -2) * (-2 - -2) = (0 : Int) := by
    omega
  have h7 : (-2 : Int) + -2 + -2 = -6 := by omega
  exact ⟨h1, h2, h3, h4, h5, h6, h7⟩

/-! ## 3. Two-State 3-Braid Closure Trace Identities (`qou-spds`) -/

/-- Unimodular 2D 3-braid channel trace for `k = 1` at `s = q + q⁻¹`. -/
def threeBraidChannelTrace1 (s : Int) : Int :=
  1 - s

/-- Unimodular 2D 3-braid channel trace for `k = 2` via `tr(X^2) = tr(X)^2 - 2`. -/
def threeBraidChannelTrace2 (s : Int) : Int :=
  (1 - s) * (1 - s) - 2

/-- Unimodular 2D 3-braid channel trace for `k = 3` via `tr(X^3) = tr(X)^3 - 3 tr(X)`. -/
def threeBraidChannelTrace3 (s : Int) : Int :=
  (1 - s) * ((1 - s) * (1 - s) - 3)

/-- Full 2-state 3-braid closure sum combining the 1D channel weight `s` and 2D trace `trK`. -/
def threeBraidClosureStateSum (s trK : Int) : Int :=
  s + trK

/-- Exact 3-braid closure state-sum identities for `k = 1` (unknot), `k = 2` (`4_1` polynomial
    `s^2 - s - 1`), and `k = 3` (`L6a4` Borromean specialization at `s = ±2`). -/
theorem threeBraidClosure_k1_k2_k3_identities (s : Int) :
    threeBraidClosureStateSum s (threeBraidChannelTrace1 s) = 1 ∧
    threeBraidClosureStateSum s (threeBraidChannelTrace2 s) = s * s - s - 1 ∧
    threeBraidClosureStateSum 2 (threeBraidChannelTrace2 2) = 1 ∧
    threeBraidClosureStateSum 2 (threeBraidChannelTrace3 2) = 4 ∧
    threeBraidClosureStateSum (-2) (threeBraidChannelTrace3 (-2)) = 16 := by
  dsimp [threeBraidClosureStateSum, threeBraidChannelTrace1,
    threeBraidChannelTrace2, threeBraidChannelTrace3]
  have h1 : s + (1 - s) = 1 := by omega
  have hSq : (1 - s) * (1 - s) = 1 - 2 * s + s * s := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_sub, Int.one_mul, Int.mul_one]
    omega
  have h2 : s + ((1 - s) * (1 - s) - 2) = s * s - s - 1 := by
    rw [hSq]
    omega
  have h3 : (2 : Int) + ((1 - 2) * (1 - 2) - 2) = 1 := by omega
  have h4 : (2 : Int) + (1 - 2) * ((1 - 2) * (1 - 2) - 3) = 4 := by omega
  have h5 : (-2 : Int) + (1 - -2) * ((1 - -2) * (1 - -2) - 3) = 16 := by omega
  exact ⟨h1, h2, h3, h4, h5⟩

/-! ## 4. Symmetric Laurent Step Multiplier & Cyclotomic Truncation (`qou-ssly`) -/

/-- Cleared negative-square numerator `-(x - 1)^2` of `x (1 - x)(1 - x⁻¹)`. -/
def clearedLaurentStepNumerator (x : Int) : Int :=
  -(x - 1) * (x - 1)

/-- Symmetric step multiplier `2 - sK` where `sK = q^k + q^{-k}`. -/
def cyclotomicTraceStepFactor (sK : Int) : Int :=
  2 - sK

/-- Next cyclotomic tail summand `T_{n+1} = (2 - sK) * T_n`. -/
def cyclotomicStepTerm (tN sK : Int) : Int :=
  cyclotomicTraceStepFactor sK * tN

/-- At the root-of-unity specialization `sK = 2` (`x = 1`), the cyclotomic step term vanishes
    identically, and for general `sK` satisfies `T_{n+1} - T_n = (1 - sK) * T_n`. -/
theorem cyclotomicStepTerm_root_truncation_and_diff (tN sK : Int) :
    cyclotomicStepTerm tN 2 = 0 ∧
    cyclotomicStepTerm tN sK - tN = (1 - sK) * tN ∧
    clearedLaurentStepNumerator 1 = 0 ∧
    clearedLaurentStepNumerator 2 = -1 := by
  dsimp [cyclotomicStepTerm, cyclotomicTraceStepFactor, clearedLaurentStepNumerator]
  have h1 : (2 - 2) * tN = 0 := by omega
  have h2 : (2 - sK) * tN - tN = (1 - sK) * tN := by
    rw [Int.sub_mul, Int.sub_mul, Int.one_mul]
    omega
  have h3 : -(1 - 1) * (1 - 1) = (0 : Int) := by omega
  have h4 : -(2 - 1) * (2 - 1) = (-1 : Int) := by omega
  exact ⟨h1, h2, h3, h4⟩

/-! ## 5. Figure-Eight Peripheral Trace-to-Adjoint Reduction (`qou-t579`) -/

/-- Meridian trace polynomial `x^4 - 5 x^2 + 2` in `x = M + M⁻¹`. -/
def figureEightTracePol (x : Int) : Int :=
  (x * x) * (x * x) - 5 * (x * x) + 2

/-- Adjoint-trace polynomial `s^2 - s - 4` in `s = M^2 + M⁻² = x^2 - 2`. -/
def figureEightAdjointTracePol (s : Int) : Int :=
  s * s - s - 4

/-- The meridian trace polynomial factors through `s = x^2 - 2`, is invariant under the
    `t = -1` skein sign flip `x ↦ -x`, and evaluates to `-2` at the parabolic point `x = 2`. -/
theorem figureEightTrace_eq_adjoint_and_parabolic (x : Int) :
    figureEightTracePol x = figureEightAdjointTracePol (x * x - 2) ∧
    figureEightTracePol (-x) = figureEightTracePol x ∧
    figureEightTracePol 2 = -2 ∧
    figureEightAdjointTracePol 2 = -2 := by
  dsimp [figureEightTracePol, figureEightAdjointTracePol]
  have uSq : (x * x - 2) * (x * x - 2) = (x * x) * (x * x) - 4 * (x * x) + 4 := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_sub]
    omega
  have h1 : (x * x) * (x * x) - 5 * (x * x) + 2 =
      (x * x - 2) * (x * x - 2) - (x * x - 2) - 4 := by
    rw [uSq]
    omega
  have hNegSq : (-x) * (-x) = x * x := by
    rw [Int.neg_mul_neg]
  have h2 : ((-x) * (-x)) * ((-x) * (-x)) - 5 * ((-x) * (-x)) + 2 =
      (x * x) * (x * x) - 5 * (x * x) + 2 := by
    rw [hNegSq]
  have h3 : ((2 : Int) * 2) * (2 * 2) - 5 * (2 * 2) + 2 = -2 := by omega
  have h4 : (2 : Int) * 2 - 2 - 4 = -2 := by omega
  exact ⟨h1, h2, h3, h4⟩

end QOU.QBeta.ModularDoubleSkeinRibbonRound67
