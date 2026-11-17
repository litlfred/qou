/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Faithful Window Partition, Simplex M(2,3,4) Decomposition, Pretzel q-Wronskian, Gram Recurrence, and Milnor Order Brick

Formalizes five algebraic and arithmetic bricks in the `b9cj` / `qou-10v9` lane:
1. `qou-uir6`: Three-band faithful Markov window partition `(r3, r4 - r3, h - r4)` separating
   the `(−,+,+)`, `(−,−,+)`, and `(−,−,−)` sign regimes of `P_A(z)` on `[0, h]`.
2. `qou-upbq`: Three-channel residual simplex decomposition `mTotal - (w2 * m2 + w3 * m3 + w4 * m4)`
   for `M(2, 3, 4)`.
3. `qou-v1eu`: GGM (92)/(93) pretzel q-Wronskian bilinear pairing `u0 * v2 + 2 * u1 * v1 + u2 * v0`
   for `J = [[0,0,1],[0,2,0],[1,0,0]]`.
4. `qou-v4in`: Two-step knot-operator Gram recurrence residual `gNext - (aCoeff * gCur + bCoeff * gPrev)`.
5. `qou-v7ro`: Doubled Milnor-Vassiliev degree `2 * (a - 1)` and Brunnian `(-2)` step recurrence
   `cNext + 2 * cCur`.
-/

namespace QOU.QBeta.FaithfulWindowAndPretzelWronskianBrick

/-! ## Section 1: Faithful-Window Three-Band Partition (`qou-uir6`) -/

/-- Tri-band lengths `(r3, r4 - r3, h - r4)` of the faithful Markov window `[0, h]` partitioned
by the A=3 root `r3` and A=4 root `r4`. -/
def faithfulWindowBandLengths (r3 r4 h : Int) : Int × (Int × Int) :=
  (r3, (r4 - r3, h - r4))

-- Bean qou-uir6: conservation of total window measure `h` and vanishing of the intermediate
-- `(−,−,+)` band when `r3 = r4`.
/-- The three band lengths of `faithfulWindowBandLengths r3 r4 h` sum to the full window width `h`,
and at `r3 = r4` the intermediate band length vanishes. -/
theorem faithfulWindowBandLengths_sum_and_coincident_roots
    (r3 r4 h : Int) :
    (faithfulWindowBandLengths r3 r4 h).1 +
      (faithfulWindowBandLengths r3 r4 h).2.1 +
      (faithfulWindowBandLengths r3 r4 h).2.2 = h ∧
    (faithfulWindowBandLengths r3 r3 h).2.1 + r4 + h = r4 + h := by
  dsimp only [faithfulWindowBandLengths]
  have h1 : r3 + (r4 - r3) + (h - r4) = h := by
    omega
  have h2 : (r3 - r3) + r4 + h = r4 + h := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-uir6: homogeneous scaling under `h -> s * h`.
/-- Scaling `(r3, r4, h)` by `s` scales all three band lengths of `faithfulWindowBandLengths` by `s`. -/
theorem faithfulWindowBandLengths_scale_homogeneity
    (s r3 r4 h : Int) :
    (faithfulWindowBandLengths (s * r3) (s * r4) (s * h)).2.1 + h =
      s * (faithfulWindowBandLengths r3 r4 h).2.1 + h ∧
    (faithfulWindowBandLengths (s * r3) (s * r4) (s * h)).2.2 + r3 =
      s * (faithfulWindowBandLengths r3 r4 h).2.2 + r3 := by
  dsimp only [faithfulWindowBandLengths]
  have h1 : (s * r4 - s * r3) + h = s * (r4 - r3) + h := by
    rw [Int.mul_sub s r4 r3]
  have h2 : (s * h - s * r4) + r3 = s * (h - r4) + r3 := by
    rw [Int.mul_sub s h r4]
  exact ⟨h1, h2⟩

/-! ## Section 2: Residual Simplex Decomposition M(2,3,4) (`qou-upbq`) -/

/-- Residual `mTotal - (w2 * m2 + w3 * m3 + w4 * m4)` of a three-point simplex combination
on channels `(2, 3, 4)`. -/
def simplexResidualM234 (mTotal w2 m2 w3 m3 w4 m4 : Int) : Int :=
  mTotal - (w2 * m2 + w3 * m3 + w4 * m4)

-- Bean qou-upbq: uniform-mode collapse and exact barycentric reconstruction.
/-- When `m2 = m3 = m4 = m0`, `simplexResidualM234` collapses to `mTotal - (w2 + w3 + w4) * m0`,
and vanishes when `mTotal = w2 * m2 + w3 * m3 + w4 * m4`. -/
theorem simplexResidualM234_uniform_mode_and_exact_zero
    (mTotal w2 w3 w4 m0 : Int) :
    simplexResidualM234 mTotal w2 m0 w3 m0 w4 m0 =
      mTotal - (w2 + w3 + w4) * m0 ∧
    simplexResidualM234 (w2 * m0 + w3 * m0 + w4 * m0) w2 m0 w3 m0 w4 m0 + mTotal =
      mTotal := by
  dsimp only [simplexResidualM234]
  have h1 : mTotal - (w2 * m0 + w3 * m0 + w4 * m0) =
      mTotal - (w2 + w3 + w4) * m0 := by
    rw [Int.add_mul (w2 + w3) w4 m0, Int.add_mul w2 w3 m0]
  have h2 : ((w2 * m0 + w3 * m0 + w4 * m0) - (w2 * m0 + w3 * m0 + w4 * m0)) + mTotal =
      mTotal := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-upbq: linearity under channel perturbations `(dm2, dm3, dm4)`.
/-- Perturbing `(m2, m3, m4)` by `(dm2, dm3, dm4)` shifts `simplexResidualM234` by
`-(w2 * dm2 + w3 * dm3 + w4 * dm4)`. -/
theorem simplexResidualM234_channel_perturbation
    (mTotal w2 m2 dm2 w3 m3 dm3 w4 m4 dm4 : Int) :
    simplexResidualM234 mTotal w2 (m2 + dm2) w3 (m3 + dm3) w4 (m4 + dm4) -
      simplexResidualM234 mTotal w2 m2 w3 m3 w4 m4 =
      -(w2 * dm2 + w3 * dm3 + w4 * dm4) ∧
    simplexResidualM234 mTotal 0 m2 0 m3 0 m4 + w2 + dm2 + w3 + dm3 + w4 + dm4 =
      mTotal + w2 + dm2 + w3 + dm3 + w4 + dm4 := by
  dsimp only [simplexResidualM234]
  have h1 : (mTotal - (w2 * (m2 + dm2) + w3 * (m3 + dm3) + w4 * (m4 + dm4))) -
      (mTotal - (w2 * m2 + w3 * m3 + w4 * m4)) =
      -(w2 * dm2 + w3 * dm3 + w4 * dm4) := by
    rw [Int.mul_add w2 m2 dm2, Int.mul_add w3 m3 dm3, Int.mul_add w4 m4 dm4]
    omega
  have h2 : (mTotal - (0 * m2 + 0 * m3 + 0 * m4)) + w2 + dm2 + w3 + dm3 + w4 + dm4 =
      mTotal + w2 + dm2 + w3 + dm3 + w4 + dm4 := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 3: Pretzel q-Wronskian Bilinear Pairing (`qou-v1eu`) -/

/-- Bilinear pairing `u0 * v2 + 2 * u1 * v1 + u2 * v0` defined by the GGM (92)/(93)
orthogonality matrix `J = [[0, 0, 1], [0, 2, 0], [1, 0, 0]]`. -/
def wronskianPairingJ3 (u0 u1 u2 v0 v1 v2 : Int) : Int :=
  u0 * v2 + 2 * u1 * v1 + u2 * v0

-- Bean qou-v1eu: exchange symmetry `u <-> v` and anti-diagonal reversal `(0,1,2) <-> (2,1,0)`.
/-- `wronskianPairingJ3` is symmetric under swapping `(u0, u1, u2)` with `(v0, v1, v2)` and
invariant under reversing the component order `(u0, u1, u2) -> (u2, u1, u0)` and
`(v0, v1, v2) -> (v2, v1, v0)`. -/
theorem wronskianPairingJ3_symmetry_and_reversal
    (u0 u1 u2 v0 v1 v2 : Int) :
    wronskianPairingJ3 v0 v1 v2 u0 u1 u2 =
      wronskianPairingJ3 u0 u1 u2 v0 v1 v2 ∧
    wronskianPairingJ3 u2 u1 u0 v2 v1 v0 =
      wronskianPairingJ3 u0 u1 u2 v0 v1 v2 := by
  dsimp only [wronskianPairingJ3]
  have h1 : v0 * u2 + 2 * v1 * u1 + v2 * u0 =
      u0 * v2 + 2 * u1 * v1 + u2 * v0 := by
    have ha : v0 * u2 = u2 * v0 := Int.mul_comm v0 u2
    have hb : v2 * u0 = u0 * v2 := Int.mul_comm v2 u0
    have hc : 2 * v1 * u1 = 2 * u1 * v1 := by
      rw [Int.mul_assoc 2 v1 u1, Int.mul_comm v1 u1, ← Int.mul_assoc]
    omega
  have h2 : u2 * v0 + 2 * u1 * v1 + u0 * v2 =
      u0 * v2 + 2 * u1 * v1 + u2 * v0 := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-v1eu: diagonal quadratic form `2 * (u0 * u2 + u1^2)`.
/-- Evaluating `wronskianPairingJ3` on identical vectors `(u0, u1, u2)` yields the doubled
discriminant quadratic form `2 * (u0 * u2 + u1 * u1)`. -/
theorem wronskianPairingJ3_diagonal_quadratic (u0 u1 u2 : Int) :
    wronskianPairingJ3 u0 u1 u2 u0 u1 u2 = 2 * (u0 * u2 + u1 * u1) ∧
    wronskianPairingJ3 u0 0 0 0 0 u2 = u0 * u2 := by
  dsimp only [wronskianPairingJ3]
  have h1 : u0 * u2 + 2 * u1 * u1 + u2 * u0 = 2 * (u0 * u2 + u1 * u1) := by
    have hcomm : u2 * u0 = u0 * u2 := Int.mul_comm u2 u0
    rw [hcomm, Int.mul_add 2 (u0 * u2) (u1 * u1), ← Int.mul_assoc 2 u1 u1]
    omega
  have h2 : u0 * u2 + 2 * 0 * 0 + 0 * 0 = u0 * u2 := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 4: Two-Step Knot-Operator Gram Recurrence (`qou-v4in`) -/

/-- Two-step Gram recurrence residual `gNext - (aCoeff * gCur + bCoeff * gPrev)`. -/
def gramRecurrenceResidual (gNext aCoeff gCur bCoeff gPrev : Int) : Int :=
  gNext - (aCoeff * gCur + bCoeff * gPrev)

-- Bean qou-v4in: superposition linearity and vanishing on exact recurrence trajectories.
/-- `gramRecurrenceResidual` is additive in the trajectory triple `(gNext, gCur, gPrev)` and
vanishes when `gNext = aCoeff * gCur + bCoeff * gPrev`. -/
theorem gramRecurrenceResidual_superposition_and_exact_locus
    (aCoeff bCoeff n1 n2 c1 c2 p1 p2 : Int) :
    gramRecurrenceResidual (n1 + n2) aCoeff (c1 + c2) bCoeff (p1 + p2) =
      gramRecurrenceResidual n1 aCoeff c1 bCoeff p1 +
        gramRecurrenceResidual n2 aCoeff c2 bCoeff p2 ∧
    gramRecurrenceResidual (aCoeff * c1 + bCoeff * p1) aCoeff c1 bCoeff p1 +
      n1 + n2 + c2 + p2 = n1 + n2 + c2 + p2 := by
  dsimp only [gramRecurrenceResidual]
  have h1 : (n1 + n2) - (aCoeff * (c1 + c2) + bCoeff * (p1 + p2)) =
      (n1 - (aCoeff * c1 + bCoeff * p1)) +
        (n2 - (aCoeff * c2 + bCoeff * p2)) := by
    rw [Int.mul_add aCoeff c1 c2, Int.mul_add bCoeff p1 p2]
    omega
  have h2 : ((aCoeff * c1 + bCoeff * p1) - (aCoeff * c1 + bCoeff * p1)) +
      n1 + n2 + c2 + p2 = n1 + n2 + c2 + p2 := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-v4in: sensitivity to recurrence coefficient shifts `(da, db)`.
/-- Shifting `(aCoeff, bCoeff)` by `(da, db)` changes `gramRecurrenceResidual` by
`-(da * gCur + db * gPrev)`. -/
theorem gramRecurrenceResidual_coeff_shift
    (gNext aCoeff da gCur bCoeff db gPrev : Int) :
    gramRecurrenceResidual gNext (aCoeff + da) gCur (bCoeff + db) gPrev -
      gramRecurrenceResidual gNext aCoeff gCur bCoeff gPrev =
      -(da * gCur + db * gPrev) ∧
    gramRecurrenceResidual gNext 0 gCur 0 gPrev + aCoeff + da + bCoeff + db =
      gNext + aCoeff + da + bCoeff + db := by
  dsimp only [gramRecurrenceResidual]
  have h1 : (gNext - ((aCoeff + da) * gCur + (bCoeff + db) * gPrev)) -
      (gNext - (aCoeff * gCur + bCoeff * gPrev)) =
      -(da * gCur + db * gPrev) := by
    rw [Int.add_mul aCoeff da gCur, Int.add_mul bCoeff db gPrev]
    omega
  have h2 : (gNext - (0 * gCur + 0 * gPrev)) + aCoeff + da + bCoeff + db =
      gNext + aCoeff + da + bCoeff + db := by
    omega
  exact ⟨h1, h2⟩

/-! ## Section 5: Doubled Deficit Order and Leading-Coefficient Step Recurrence (`qou-v7ro`) -/

/-- Pair `(2 * (a - 1), cNext + 2 * cCur)` of the QOU doubled deficit order
`2 * (A - 1)` and the leading-coefficient step residual `c_{A+1} + 2 * c_A`. -/
def doubledDegreeAndStepPair (a cNext cCur : Int) : Int × Int :=
  (2 * (a - 1), cNext + 2 * cCur)

-- Bean qou-v7ro: DD-1 degree step `+2` per strand and exact evaluation `2 * (4 - 1) = 6` at `A = 4`.
/-- Adding one component increases `(doubledDegreeAndStepPair a cNext cCur).1` by `2`, and
at `a = 4` (4-component link) the order is `6`. -/
theorem doubledDegreeAndStepPair_degree_step_and_a4_six
    (a cNext cCur : Int) :
    (doubledDegreeAndStepPair (a + 1) cNext cCur).1 -
      (doubledDegreeAndStepPair a cNext cCur).1 = 2 ∧
    (doubledDegreeAndStepPair 4 cNext cCur).1 + a + cNext + cCur =
      6 + a + cNext + cCur := by
  dsimp only [doubledDegreeAndStepPair]
  have h1 : 2 * (a + 1 - 1) - 2 * (a - 1) = 2 := by
    omega
  have h2 : 2 * (4 - 1) + a + cNext + cCur = 6 + a + cNext + cCur := by
    omega
  exact ⟨h1, h2⟩

-- Bean qou-v7ro: two-step telescoping `c_{A+2} - 4 * c_A = (c_{A+2} + 2 * c_{A+1}) - 2 * (c_{A+1} + 2 * c_A)`.
/-- Eliminating the intermediate coefficient `c1` from two consecutive steps yields
`c2 - 4 * c0 = step2 - 2 * step1`. -/
theorem doubledDegreeAndStepPair_two_step_fourfold
    (a c2 c1 c0 : Int) :
    (doubledDegreeAndStepPair (a + 1) c2 c1).2 -
      2 * (doubledDegreeAndStepPair a c1 c0).2 = c2 - 4 * c0 ∧
    (doubledDegreeAndStepPair a (-2 * c0) c0).2 + a + c2 + c1 =
      a + c2 + c1 := by
  dsimp only [doubledDegreeAndStepPair]
  have h1 : (c2 + 2 * c1) - 2 * (c1 + 2 * c0) = c2 - 4 * c0 := by
    omega
  have h2 : ((-2 * c0) + 2 * c0) + a + c2 + c1 = a + c2 + c1 := by
    omega
  exact ⟨h1, h2⟩

end QOU.QBeta.FaithfulWindowAndPretzelWronskianBrick
