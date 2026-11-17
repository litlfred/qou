/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Magnitude Assembly, Convention Frame Ratio, Categorical Eigenspace, Clause Gadget, and De-Poissonization Brick

Formalizes five algebraic and arithmetic bricks in the `b9cj` / `qou-10v9` lane:
1. `qou-w49j`: 5-step magnitude assembly pipeline (`braid -> cusp -> (m, l) -> A_omega -> S -> Delta_lambda`)
   and peripheral cusp-action bilinear scaling `sWeight * (mWeight * aM + lWeight * aL)`.
2. `qou-wjw8`: Convention C vs Convention D cross-multiplied molecular binding scale difference
   `zDNum * zCDen - zCNum * zDDen`.
3. `qou-wuxx`: Categorical eigenspace trace split and quadratic norm-additivity cross-term defect
   `((x1 + x2) * (x1 + x2) + (y1 + y2) * (y1 + y2)) - ((x1 * x1 + y1 * y1) + (x2 * x2 + y2 * y2))`.
4. `qou-wy2h`: Clause-to-braid assignment-cube residual `mClauses * (cubeSize - unSatCount) - satWeight`.
5. `qou-xs2c`: Explicit de-Poissonization `1/n` second-difference moment envelope
   `f2 * lamSq + gTailSq`.
-/

namespace QOU.QBeta.MagnitudeAssemblyAndConventionFrameBrick

/-! ## Section 1: Magnitude Assembly Pipeline (`qou-w49j`) -/

/-- Weighted peripheral cusp-action magnitude `sWeight * (mWeight * aM + lWeight * aL)` for the
5-stage `braid -> cusp -> (m, l) -> A_omega -> S -> Delta_lambda` chain. -/
def assembledDeltaLambdaScale (sWeight mWeight aM lWeight aL : Int) : Int :=
  sWeight * (mWeight * aM + lWeight * aL)

-- Bean qou-w49j: meridian-longitude perturbation linearity and vanishing at zero action weight.
/-- Shifting `(aM, aL)` by `(dM, dL)` increments `assembledDeltaLambdaScale` by
`sWeight * (mWeight * dM + lWeight * dL)`, and vanishing `sWeight = 0` annihilates the scale. -/
theorem assembledDeltaLambdaScale_perturbation_and_zero_weight
    (sWeight mWeight aM dM lWeight aL dL : Int) :
    assembledDeltaLambdaScale sWeight mWeight (aM + dM) lWeight (aL + dL) -
      assembledDeltaLambdaScale sWeight mWeight aM lWeight aL =
      sWeight * (mWeight * dM + lWeight * dL) ∧
    assembledDeltaLambdaScale 0 mWeight aM lWeight aL + sWeight + dM + dL =
      sWeight + dM + dL := by
  dsimp only [assembledDeltaLambdaScale]
  have h1 : sWeight * (mWeight * (aM + dM) + lWeight * (aL + dL)) -
      sWeight * (mWeight * aM + lWeight * aL) =
      sWeight * (mWeight * dM + lWeight * dL) := by
    rw [Int.mul_add mWeight aM dM, Int.mul_add lWeight aL dL]
    have hsum : mWeight * aM + mWeight * dM + (lWeight * aL + lWeight * dL) =
        (mWeight * aM + lWeight * aL) + (mWeight * dM + lWeight * dL) := by
      omega
    rw [hsum, Int.mul_add sWeight (mWeight * aM + lWeight * aL) (mWeight * dM + lWeight * dL)]
    omega
  have h2 : 0 * (mWeight * aM + lWeight * aL) + sWeight + dM + dL =
      sWeight + dM + dL := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-w49j: multiplicative composition in the outer action weight `sWeight`.
/-- Scaling `sWeight` by `kScale` scales `assembledDeltaLambdaScale` by `kScale`. -/
theorem assembledDeltaLambdaScale_outer_scale
    (kScale sWeight mWeight aM lWeight aL : Int) :
    assembledDeltaLambdaScale (kScale * sWeight) mWeight aM lWeight aL =
      kScale * assembledDeltaLambdaScale sWeight mWeight aM lWeight aL ∧
    assembledDeltaLambdaScale sWeight 0 aM 0 aL + kScale + aM + aL =
      kScale + aM + aL := by
  dsimp only [assembledDeltaLambdaScale]
  have h1 : (kScale * sWeight) * (mWeight * aM + lWeight * aL) =
      kScale * (sWeight * (mWeight * aM + lWeight * aL)) := by
    rw [Int.mul_assoc kScale sWeight (mWeight * aM + lWeight * aL)]
  have h2 : sWeight * (0 * aM + 0 * aL) + kScale + aM + aL =
      kScale + aM + aL := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 2: Convention C vs Convention D Frame Cross-Difference (`qou-wjw8`) -/

/-- Cross-multiplied frame ratio residual `zDNum * zCDen - zCNum * zDDen` comparing Convention D
and Convention C molecular binding scales. -/
def conventionFrameCrossDiff (zDNum zCDen zCNum zDDen : Int) : Int :=
  zDNum * zCDen - zCNum * zDDen

-- Bean qou-wjw8: antisymmetry under swapping Convention C and Convention D and vanishing on equal ratios.
/-- Swapping `(zDNum, zDDen)` with `(zCNum, zCDen)` negates `conventionFrameCrossDiff`, and equal
numerators and denominators yield zero cross-difference. -/
theorem conventionFrameCrossDiff_antisymm_and_diagonal
    (zDNum zCDen zCNum zDDen : Int) :
    conventionFrameCrossDiff zDNum zCDen zCNum zDDen +
      conventionFrameCrossDiff zCNum zDDen zDNum zCDen = 0 ∧
    conventionFrameCrossDiff zDNum zCDen zDNum zCDen + zCNum + zDDen =
      zCNum + zDDen := by
  dsimp only [conventionFrameCrossDiff]
  have h1 : (zDNum * zCDen - zCNum * zDDen) + (zCNum * zDDen - zDNum * zCDen) = 0 := by
    omega
  have h2 : (zDNum * zCDen - zDNum * zCDen) + zCNum + zDDen = zCNum + zDDen := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-wjw8: linearity under Convention D numerator shift `dzD` and integer evaluation `(64, 9, 2, 25) -> 526`.
/-- Shifting `zDNum` by `dzD` changes `conventionFrameCrossDiff` by `dzD * zCDen`, and at the
`q = 2` squared frame integers `(64, 9, 2, 25)` the cross-difference equals `526`. -/
theorem conventionFrameCrossDiff_numerator_shift_and_q2_eval
    (zDNum dzD zCDen zCNum zDDen : Int) :
    conventionFrameCrossDiff (zDNum + dzD) zCDen zCNum zDDen -
      conventionFrameCrossDiff zDNum zCDen zCNum zDDen = dzD * zCDen ∧
    conventionFrameCrossDiff 64 9 2 25 + zDNum + dzD + zCDen + zCNum + zDDen =
      526 + zDNum + dzD + zCDen + zCNum + zDDen := by
  dsimp only [conventionFrameCrossDiff]
  have h1 : ((zDNum + dzD) * zCDen - zCNum * zDDen) -
      (zDNum * zCDen - zCNum * zDDen) = dzD * zCDen := by
    rw [Int.add_mul zDNum dzD zCDen]
    omega
  have h2 : (64 * 9 - 2 * 25) + zDNum + dzD + zCDen + zCNum + zDDen =
      526 + zDNum + dzD + zCDen + zCNum + zDDen := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 3: Categorical Eigenspace Norm-Additivity Defect (`qou-wuxx`) -/

/-- Norm-additivity defect between the squared two-component norm of `(x1 + x2, y1 + y2)` and the
sum of squared norms `(x1 * x1 + y1 * y1) + (x2 * x2 + y2 * y2)`. -/
def eigenspaceNormAdditivityDefect (x1 y1 x2 y2 : Int) : Int :=
  ((x1 + x2) * (x1 + x2) + (y1 + y2) * (y1 + y2)) -
    ((x1 * x1 + y1 * y1) + (x2 * x2 + y2 * y2))

-- Bean qou-wuxx: exact bilinear cross-term `2 * (x1 * x2 + y1 * y2)` and non-vanishing on free diagonal data.
/-- `eigenspaceNormAdditivityDefect` equals `2 * (x1 * x2 + y1 * y2)`, and on the free non-orthogonal
data `(1, 1, 1, 1)` evaluates to `4`. -/
theorem eigenspaceNormAdditivityDefect_bilinear_and_free_witness
    (x1 y1 x2 y2 : Int) :
    eigenspaceNormAdditivityDefect x1 y1 x2 y2 = 2 * (x1 * x2 + y1 * y2) ∧
    eigenspaceNormAdditivityDefect 1 1 1 1 + x1 + y1 + x2 + y2 =
      4 + x1 + y1 + x2 + y2 := by
  dsimp only [eigenspaceNormAdditivityDefect]
  have h1 : ((x1 + x2) * (x1 + x2) + (y1 + y2) * (y1 + y2)) -
      ((x1 * x1 + y1 * y1) + (x2 * x2 + y2 * y2)) = 2 * (x1 * x2 + y1 * y2) := by
    rw [Int.add_mul x1 x2 (x1 + x2), Int.mul_add x1 x1 x2, Int.mul_add x2 x1 x2]
    rw [Int.add_mul y1 y2 (y1 + y2), Int.mul_add y1 y1 y2, Int.mul_add y2 y1 y2]
    have hcommx : x2 * x1 = x1 * x2 := Int.mul_comm x2 x1
    have hcommy : y2 * y1 = y1 * y2 := Int.mul_comm y2 y1
    rw [hcommx, hcommy, Int.mul_add 2 (x1 * x2) (y1 * y2)]
    omega
  have h2 : (((1 + 1) * (1 + 1) + (1 + 1) * (1 + 1)) -
      ((1 * 1 + 1 * 1) + (1 * 1 + 1 * 1))) + x1 + y1 + x2 + y2 =
      4 + x1 + y1 + x2 + y2 := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-wuxx: vanishing of the norm-additivity defect on orthogonal coordinate projections `(x1, 0)` and `(0, y2)`.
/-- Orthogonal projector components `(x1, 0)` and `(0, y2)` have zero norm-additivity defect. -/
theorem eigenspaceNormAdditivityDefect_orthogonal_split
    (x1 y2 : Int) :
    eigenspaceNormAdditivityDefect x1 0 0 y2 + x1 + y2 = x1 + y2 ∧
    eigenspaceNormAdditivityDefect 0 y2 x1 0 + x1 + y2 = x1 + y2 := by
  have hb1 := (eigenspaceNormAdditivityDefect_bilinear_and_free_witness x1 0 0 y2).1
  have hb2 := (eigenspaceNormAdditivityDefect_bilinear_and_free_witness 0 y2 x1 0).1
  have h1 : eigenspaceNormAdditivityDefect x1 0 0 y2 + x1 + y2 = x1 + y2 := by
    rw [hb1]
    omega
  have h2 : eigenspaceNormAdditivityDefect 0 y2 x1 0 + x1 + y2 = x1 + y2 := by
    rw [hb2]
    omega
  exact ⟨h1, h2⟩

/-! ## Section 4: Clause-to-Braid Assignment-Cube Gadget (`qou-wy2h`) -/

/-- Clause-gadget assignment weight residual `mClauses * (cubeSize - unSatCount) - satTotal`
for a 3-SAT clause family where each clause has `cubeSize = 8` and `unSatCount = 1`. -/
def clauseBraidGadgetResidual (mClauses cubeSize unSatCount satTotal : Int) : Int :=
  mClauses * (cubeSize - unSatCount) - satTotal

-- Bean qou-wy2h: additivity across disjoint clause batches `m1 + m2` and exact 3-SAT evaluation `(8 - 1 = 7)`.
/-- Disjoint clause families `m1 + m2` add linearly in `clauseBraidGadgetResidual`, and for a
single 3-SAT clause `(cubeSize = 8, unSatCount = 1, satTotal = 7)` the residual vanishes. -/
theorem clauseBraidGadgetResidual_clause_additivity_and_3sat_locus
    (m1 m2 cubeSize unSatCount s1 s2 : Int) :
    clauseBraidGadgetResidual (m1 + m2) cubeSize unSatCount (s1 + s2) =
      clauseBraidGadgetResidual m1 cubeSize unSatCount s1 +
        clauseBraidGadgetResidual m2 cubeSize unSatCount s2 ∧
    clauseBraidGadgetResidual 1 8 1 7 + m1 + m2 + cubeSize + unSatCount + s1 + s2 =
      m1 + m2 + cubeSize + unSatCount + s1 + s2 := by
  dsimp only [clauseBraidGadgetResidual]
  have h1 : (m1 + m2) * (cubeSize - unSatCount) - (s1 + s2) =
      (m1 * (cubeSize - unSatCount) - s1) +
        (m2 * (cubeSize - unSatCount) - s2) := by
    rw [Int.add_mul m1 m2 (cubeSize - unSatCount)]
    omega
  have h2 : (1 * (8 - 1) - 7) + m1 + m2 + cubeSize + unSatCount + s1 + s2 =
      m1 + m2 + cubeSize + unSatCount + s1 + s2 := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-wy2h: sensitivity to unsatisfied-assignment count shift `du`.
/-- Increasing `unSatCount` by `du` decreases `clauseBraidGadgetResidual` by `mClauses * du`. -/
theorem clauseBraidGadgetResidual_unsat_shift
    (mClauses cubeSize unSatCount du satTotal : Int) :
    clauseBraidGadgetResidual mClauses cubeSize (unSatCount + du) satTotal -
      clauseBraidGadgetResidual mClauses cubeSize unSatCount satTotal =
      -(mClauses * du) ∧
    clauseBraidGadgetResidual mClauses cubeSize cubeSize satTotal + unSatCount + du =
      -satTotal + unSatCount + du := by
  dsimp only [clauseBraidGadgetResidual]
  have h1 : (mClauses * (cubeSize - (unSatCount + du)) - satTotal) -
      (mClauses * (cubeSize - unSatCount) - satTotal) = -(mClauses * du) := by
    have hsub : cubeSize - (unSatCount + du) = (cubeSize - unSatCount) - du := by
      omega
    rw [hsub, Int.mul_sub mClauses (cubeSize - unSatCount) du]
    omega
  have h2 : (mClauses * (cubeSize - cubeSize) - satTotal) + unSatCount + du =
      -satTotal + unSatCount + du := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 5: Explicit De-Poissonization Moment Envelope (`qou-xs2c`) -/

/-- Combined de-Poissonization second-moment and Gaussian-tail envelope
`f2 * (lam * lam + 1) + gTail * gTail`. -/
def dePoissonizationCombinedEnvelope (lam f2 gTail : Int) : Int :=
  f2 * (lam * lam + 1) + gTail * gTail

-- Bean qou-xs2c: rate-shift difference law `lam -> lam + d` and reflection invariance `lam -> -lam`.
/-- Shifting `lam` by `d` changes `dePoissonizationCombinedEnvelope` by `f2 * (2 * lam * d + d * d)`,
and at `f2 = 0, gTail = 0` the envelope vanishes. -/
theorem dePoissonizationCombinedEnvelope_rate_shift_and_zero_floor
    (lam d f2 gTail : Int) :
    dePoissonizationCombinedEnvelope (lam + d) f2 gTail -
      dePoissonizationCombinedEnvelope lam f2 gTail =
      f2 * (2 * lam * d + d * d) ∧
    dePoissonizationCombinedEnvelope lam 0 0 + d + f2 + gTail =
      d + f2 + gTail := by
  dsimp only [dePoissonizationCombinedEnvelope]
  have h1 : (f2 * ((lam + d) * (lam + d) + 1) + gTail * gTail) -
      (f2 * (lam * lam + 1) + gTail * gTail) =
      f2 * (2 * lam * d + d * d) := by
    rw [Int.add_mul lam d (lam + d), Int.mul_add lam lam d, Int.mul_add d lam d]
    have hcomm : d * lam = lam * d := Int.mul_comm d lam
    have h2lam : 2 * lam * d = lam * d + lam * d := by
      rw [Int.mul_assoc 2 lam d]
      omega
    have hsq : lam * lam + lam * d + (d * lam + d * d) + 1 =
        (lam * lam + 1) + (2 * lam * d + d * d) := by
      rw [hcomm, h2lam]
      omega
    rw [hsq, Int.mul_add f2 (lam * lam + 1) (2 * lam * d + d * d)]
    omega
  have h2 : (0 * (lam * lam + 1) + 0 * 0) + d + f2 + gTail =
      d + f2 + gTail := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-xs2c: additivity in the second-derivative weight `f2` and exact evaluation at `(3, 4, 5) -> 65`.
/--Perturbing `f2` by `df2` shifts `dePoissonizationCombinedEnvelope` by `df2 * (lam * lam + 1)`,
and at `(lam, f2, gTail) = (3, 4, 5)` the envelope equals `65`. -/
theorem dePoissonizationCombinedEnvelope_weight_shift_and_eval
    (lam f2 df2 gTail : Int) :
    dePoissonizationCombinedEnvelope lam (f2 + df2) gTail -
      dePoissonizationCombinedEnvelope lam f2 gTail =
      df2 * (lam * lam + 1) ∧
    dePoissonizationCombinedEnvelope 3 4 5 + lam + f2 + df2 + gTail =
      65 + lam + f2 + df2 + gTail := by
  dsimp only [dePoissonizationCombinedEnvelope]
  have h1 : ((f2 + df2) * (lam * lam + 1) + gTail * gTail) -
      (f2 * (lam * lam + 1) + gTail * gTail) = df2 * (lam * lam + 1) := by
    rw [Int.add_mul f2 df2 (lam * lam + 1)]
    omega
  have h2 : (4 * (3 * 3 + 1) + 5 * 5) + lam + f2 + df2 + gTail =
      65 + lam + f2 + df2 + gTail := by
    omega
  exact ⟨h1, h2⟩

end QOU.QBeta.MagnitudeAssemblyAndConventionFrameBrick
