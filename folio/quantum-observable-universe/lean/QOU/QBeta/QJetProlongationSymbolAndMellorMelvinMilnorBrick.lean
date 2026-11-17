/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# q-Jet Prolongation Symbol, Mellor-Melvin Milnor Decomposition, Saddle Stencil, and DGG 4_1 Index Brick

This self-contained Lean 4 module formalizes exact algebraic and structural identities for five
items in the `b9cj` formalization arc:

1. **Mellor-Melvin Triple-Linking Decomposition (`qou-2g9j`)**:
   Formalizes the raw integer core of Mellor and Melvin's triple-linking formula
   `mubar_ijk = (e_ijk + e_jki + e_kij) - t_ijk` (Alg. Geom. Topol. 3 (2003) 557-568),
   proving its exact reduction to the middle-word Magnus coefficient `e_ijk` when outer
   Seifert surfaces are disjoint (`t_ijk = 0`) and outer two-letter Magnus coefficients vanish
   (`e_jki = 0`, `e_kij = 0`), together with the Borromean rings control (`e_123 = -1`) and
   the symmetrized Magnus sum identity `(eps_ij + eps_ji) - mu_ik * mu_jk`.

2. **Second-Order q-Difference Prolongation Symbol Vieta Factorization (`qou-mf2v`)**:
   Formalizes the second-order `q`-difference prolongation characteristic polynomial
   `P(tau, lam) = lam^2 - tau * lam + 1` and its factored root product
   `F(lamPlus, lamMinus, lam) = (lam - lamPlus) * (lam - lamMinus)`, proving the exact
   universal Vieta discrepancy identity
   `F(lamPlus, lamMinus, lam) - P(lamPlus + lamMinus, lam) = lamPlus * lamMinus - 1`
   and root annihilation at `lam = lamPlus` and `lam = lamMinus`.

3. **First-Order q-Jet Prolongation Operator Twisted Leibniz Identity (`qou-ql68`)**:
   Formalizes the `q`-shifted evaluation `E_h(f0, df) = f0 + h * df` for a 1-jet `(f0, df)`
   with step `h = (q - 1) * x` and proves the exact twisted Leibniz product increment identity
   `E_h(f0, df) * E_h(g0, dg) - f0 * g0 = h * (f0 * dg + df * g0 + h * df * dg)`.

4. **Reusable Triangulation-Potential Quadratic Saddle Stencil (`qou-vnqe`)**:
   Formalizes the twice-scaled second-order potential expansion
   `2 * V(z0 + dz) = 2 * v0 + 2 * grad * dz + hessian * dz^2`, proving its exact difference
   from the pure quadratic saddle form `2 * v0 + hessian * dz^2` is `2 * grad * dz`, and
   showing that the symmetric stencil `2 * V(z0 + dz) + 2 * V(z0 - dz) - 4 * v0` eliminates
   the linear gradient identically to isolate `2 * hessian * dz^2`.

5. **DGG 4_1 3d-Index Charge-Conjugation Pairing & Neutral Truncation (`qou-yaz9`)**:
   Formalizes the bilateral electric-charge sum `iZero + posSum + negSum` at zero magnetic
   flux `m = 0` for the Dimofte-Gaiotto-Gukov 3d index of `4_1`, proving its discrepancy
   from the charge-conjugation-symmetric folded sum `iZero + 2 * posSum` is `negSum - posSum`,
   along with exact evaluations of the cubic neutral-sector truncation `1 - 2q - 3q^2 + 2q^3`.
-/

namespace QOU.QBeta.QJetProlongationSymbolAndMellorMelvinMilnorBrick

/-! ## 1. Mellor-Melvin Triple-Linking Decomposition (`qou-2g9j`) -/

/-- Raw integer lift of Mellor-Melvin's triple-linking formula
`(e_ijk + e_jki + e_kij) - t_ijk`, where `e_pqr` are degree-2 Magnus coefficients
and `t_ijk` is the signed count of triple intersection points `F_i ∩ F_j ∩ F_k`. -/
def mellorMelvinMilnorRaw (eIjk eJki eKij tIjk : Int) : Int :=
  (eIjk + eJki + eKij) - tIjk

/-- Disjoint-outer-surface reduction: when `eJki = 0`, `eKij = 0`, and `tIjk = 0`,
`mellorMelvinMilnorRaw` reduces identically to `eIjk`. -/
theorem mellorMelvinMilnorRaw_disjoint_outer (eIjk : Int) :
    mellorMelvinMilnorRaw eIjk 0 0 0 = eIjk := by
  dsimp [mellorMelvinMilnorRaw]
  omega

/-- Borromean rings positive control: `e_123 = -1` with `e_231 = 0, e_312 = 0, t_123 = 0`
yields `-1`. -/
theorem mellorMelvinMilnorRaw_borromean_control :
    mellorMelvinMilnorRaw (-1) 0 0 0 = -1 := by
  rfl

/-- Additivity of `mellorMelvinMilnorRaw` under simultaneous scaling of all four components. -/
theorem mellorMelvinMilnorRaw_scale (c eIjk eJki eKij tIjk : Int) :
    mellorMelvinMilnorRaw (c * eIjk) (c * eJki) (c * eKij) (c * tIjk) =
      c * mellorMelvinMilnorRaw eIjk eJki eKij tIjk := by
  dsimp [mellorMelvinMilnorRaw]
  rw [← Int.mul_add, ← Int.mul_add, ← Int.mul_sub]

/-- Symmetrized degree-2 Magnus sum discrepancy `(epsIj + epsJi) - muIk * muJk`. -/
def mellorMelvinSymmetrizedMagnusDiff (epsIj epsJi muIk muJk : Int) : Int :=
  (epsIj + epsJi) - muIk * muJk

/-- When `epsJi = muIk * muJk - epsIj` (Mellor-Melvin line 88 identity), the symmetrized
Magnus discrepancy vanishes identically. -/
theorem mellorMelvinSymmetrizedMagnusDiff_eq_zero (epsIj muIk muJk : Int) :
    mellorMelvinSymmetrizedMagnusDiff epsIj (muIk * muJk - epsIj) muIk muJk = 0 := by
  dsimp [mellorMelvinSymmetrizedMagnusDiff]
  omega

/-! ## 2. Second-Order q-Difference Prolongation Symbol (`qou-mf2v`) -/

/-- Unimodular second-order `q`-difference prolongation characteristic polynomial
`P(tau, lam) = lam^2 - tau * lam + 1` with trace parameter `tau`. -/
def qDiffProlongationSymbolPoly (tau lam : Int) : Int :=
  lam * lam - tau * lam + 1

/-- Factored quadratic prolongation symbol `F(lamPlus, lamMinus, lam) = (lam - lamPlus) * (lam - lamMinus)`. -/
def qDiffFactoredSymbol (lamPlus lamMinus lam : Int) : Int :=
  (lam - lamPlus) * (lam - lamMinus)

/-- Universal Vieta discrepancy between the factored symbol `(lam - lamPlus)*(lam - lamMinus)`
and the unimodular prolongation polynomial with trace `tau = lamPlus + lamMinus`:
their difference equals the determinant defect `lamPlus * lamMinus - 1` for every `lam`. -/
theorem qDiffFactoredSymbol_sub_prolongationPoly (lamPlus lamMinus lam : Int) :
    qDiffFactoredSymbol lamPlus lamMinus lam -
      qDiffProlongationSymbolPoly (lamPlus + lamMinus) lam =
      lamPlus * lamMinus - 1 := by
  dsimp [qDiffFactoredSymbol, qDiffProlongationSymbolPoly]
  rw [Int.sub_mul, Int.mul_sub, Int.mul_sub, Int.add_mul, Int.mul_comm lam lamMinus]
  omega

/-- Root annihilation of the factored prolongation symbol at `lam = lamPlus`. -/
theorem qDiffFactoredSymbol_eval_left_root (lamPlus lamMinus : Int) :
    qDiffFactoredSymbol lamPlus lamMinus lamPlus = 0 := by
  dsimp [qDiffFactoredSymbol]
  rw [Int.sub_self, Int.zero_mul]

/-- Root annihilation of the factored prolongation symbol at `lam = lamMinus`. -/
theorem qDiffFactoredSymbol_eval_right_root (lamPlus lamMinus : Int) :
    qDiffFactoredSymbol lamPlus lamMinus lamMinus = 0 := by
  dsimp [qDiffFactoredSymbol]
  rw [Int.sub_self, Int.mul_zero]

/-- Evaluating the unimodular prolongation polynomial at `lam = 0` yields `1` for every trace `tau`. -/
theorem qDiffProlongationSymbolPoly_eval_zero (tau : Int) :
    qDiffProlongationSymbolPoly tau 0 = 1 := by
  dsimp [qDiffProlongationSymbolPoly]
  omega

/-! ## 3. First-Order q-Jet Prolongation Twisted Leibniz Identity (`qou-ql68`) -/

/-- `q`-shifted evaluation `f(q x) = f0 + h * df` reconstructed from the 1-jet `(f0, df)`
at step `h = (q - 1) * x`. -/
def qJetShiftedVal (f0 df h : Int) : Int :=
  f0 + h * df

/-- Total increment of the product `(f * g)(q x) - f(x) * g(x)` along the 1-jet prolongation. -/
def qJetProductIncrement (f0 df g0 dg h : Int) : Int :=
  qJetShiftedVal f0 df h * qJetShiftedVal g0 dg h - f0 * g0

/-- Right-hand side of the twisted `q`-jet Leibniz rule:
`h * (f0 * dg + df * g0 + h * df * dg)`. -/
def qJetTwistedLeibnizRHS (f0 df g0 dg h : Int) : Int :=
  h * (f0 * dg + df * g0) + (h * df) * (h * dg)

/-- Exact twisted Leibniz product increment identity for the 1-jet prolongation operator. -/
theorem qJetProductIncrement_eq_twistedLeibniz (f0 df g0 dg h : Int) :
    qJetProductIncrement f0 df g0 dg h = qJetTwistedLeibnizRHS f0 df g0 dg h := by
  dsimp [qJetProductIncrement, qJetShiftedVal, qJetTwistedLeibnizRHS]
  rw [Int.add_mul, Int.mul_add, Int.mul_add, Int.mul_add]
  rw [← Int.mul_assoc f0 h dg, Int.mul_comm f0 h, Int.mul_assoc h f0 dg, Int.mul_assoc h df g0]
  omega

/-- Classical limit (`h = 0`): the `q`-shifted evaluation coincides with `f0`. -/
theorem qJetShiftedVal_classical_limit (f0 df : Int) :
    qJetShiftedVal f0 df 0 = f0 := by
  dsimp [qJetShiftedVal]
  omega

/-! ## 4. Reusable Triangulation-Potential Quadratic Saddle Stencil (`qou-vnqe`) -/

/-- Twice the second-order Taylor-perturbed potential `2 * V(z0 + dz) = 2*v0 + 2*grad*dz + hessian*dz^2`. -/
def twicePerturbedPotential (v0 grad hessian dz : Int) : Int :=
  2 * v0 + 2 * grad * dz + hessian * dz * dz

/-- Twice the pure quadratic saddle expansion `2 * V_saddle(dz) = 2*v0 + hessian*dz^2`. -/
def twiceSaddleQuadraticForm (v0 hessian dz : Int) : Int :=
  2 * v0 + hessian * dz * dz

/-- Exact discrepancy between the full second-order potential expansion and the pure quadratic
saddle form is the linear gradient work term `2 * grad * dz`. -/
theorem twicePerturbedPotential_sub_saddleQuadratic (v0 grad hessian dz : Int) :
    twicePerturbedPotential v0 grad hessian dz - twiceSaddleQuadraticForm v0 hessian dz =
      2 * grad * dz := by
  dsimp [twicePerturbedPotential, twiceSaddleQuadraticForm]
  omega

/-- At a stationary critical point (`grad = 0`), the second-order potential expansion
reduces identically to the pure quadratic saddle form. -/
theorem twicePerturbedPotential_at_critical_point (v0 hessian dz : Int) :
    twicePerturbedPotential v0 0 hessian dz = twiceSaddleQuadraticForm v0 hessian dz := by
  dsimp [twicePerturbedPotential, twiceSaddleQuadraticForm]
  omega

/-- Symmetric central second-difference stencil eliminates the linear gradient term `grad`
for every `v0, grad, hessian, dz`, isolating `2 * hessian * dz * dz`. -/
theorem twicePerturbedPotential_symmetric_stencil (v0 grad hessian dz : Int) :
    twicePerturbedPotential v0 grad hessian dz +
      twicePerturbedPotential v0 grad hessian (-dz) - 4 * v0 =
      2 * (hessian * dz * dz) := by
  dsimp [twicePerturbedPotential]
  rw [Int.mul_neg, Int.mul_neg, Int.mul_neg, Int.neg_mul, Int.neg_neg]
  omega

/-! ## 5. DGG 4_1 3d-Index Charge-Conjugation Pairing (`qou-yaz9`) -/

/-- Bilateral electric-charge sector sum `I(0,0) + sum_{e>0} I(0,e) + sum_{e<0} I(0,e)` at `m = 0`. -/
def dggBilateralChargePairSum (iZero posSum negSum : Int) : Int :=
  iZero + posSum + negSum

/-- Charge-conjugation-folded meridian-zero sum `I(0,0) + 2 * sum_{e>0} I(0,e)`. -/
def dggSymmetricMeridianZeroIndex (iZero posSum : Int) : Int :=
  iZero + 2 * posSum

/-- Exact discrepancy between the bilateral charge sum and the charge-conjugation-folded
sum equals the electric charge-asymmetry `negSum - posSum`. -/
theorem dggBilateralChargePairSum_sub_symmetric (iZero posSum negSum : Int) :
    dggBilateralChargePairSum iZero posSum negSum -
      dggSymmetricMeridianZeroIndex iZero posSum =
      negSum - posSum := by
  dsimp [dggBilateralChargePairSum, dggSymmetricMeridianZeroIndex]
  omega

/-- Under DGG charge-conjugation symmetry `negSum = posSum`, the bilateral sum equals
the folded sum `iZero + 2 * posSum`. -/
theorem dggBilateralChargePairSum_when_symmetric (iZero posSum : Int) :
    dggBilateralChargePairSum iZero posSum posSum =
      dggSymmetricMeridianZeroIndex iZero posSum := by
  dsimp [dggBilateralChargePairSum, dggSymmetricMeridianZeroIndex]
  omega

/-- Cubic truncation `1 - 2*q - 3*q^2 + 2*q^3` of the neutral DGG 3d-index `I_{4_1}(0,0; q)`. -/
def dgg41NeutralTruncatedPoly (q : Int) : Int :=
  1 - 2 * q - 3 * q * q + 2 * q * q * q

/-- At `q = 0`, the neutral DGG `4_1` index truncation evaluates to the vacuum unit `1`. -/
theorem dgg41NeutralTruncatedPoly_at_zero :
    dgg41NeutralTruncatedPoly 0 = 1 := by
  rfl

/-- At `q = 1`, the cubic neutral DGG `4_1` index truncation evaluates to `1 - 2 - 3 + 2 = -2`. -/
theorem dgg41NeutralTruncatedPoly_at_one :
    dgg41NeutralTruncatedPoly 1 = -2 := by
  rfl

end QOU.QBeta.QJetProlongationSymbolAndMellorMelvinMilnorBrick
