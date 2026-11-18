/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Beans:
  * qou-5uj7: Categorical Dirac operator convex split (gradient share 1/q vs Reeb share hbar_q = (q-1)/q).
  * qou-6s8k: Figure-eight deformed complex volume V_41(u) = Vol(u) + i*CS(u) conjugation reflection parity.
  * qou-7fyw: Parameterized Delta_max two-sided slack margin sum and quadratic bound factorization.
  * qou-9s8k: Garoufalidis-Kashaev bilinear block pairing diagonal-even vs off-diagonal-odd decomposition.
  * qou-cyon: Harmonic imaginary form (x^2 - y^2) diagonal factorization and coordinate-swap antisymmetry.
-/

namespace QOU.QBeta.DeformedVolumeParityAndDiracReebConvexSplitBrick

/-! ### 1. Categorical Dirac operator gradient/Reeb convex split (`qou-5uj7`) -/

/-- Numerator of the gradient weight `1/q` in `q * D_grad = grad + (q - 1) * iota_xi grad`. -/
def diracGradNumerator : Int := 1

/-- Numerator of the Reeb weight `hbar_q = (q - 1)/q` in `q * D_grad`. -/
def diracReebNumerator (q : Int) : Int := q - 1

/-- Weighted step cost numerator `1 * sGrad + (q - 1) * sReeb` over common denominator `q`. -/
def diracWeightedStepNumerator (q sGrad sReeb : Int) : Int :=
  diracGradNumerator * sGrad + diracReebNumerator q * sReeb

/-- The gradient numerator `1` and Reeb numerator `q - 1` sum identically to `q` (convexity `1/q + (q-1)/q = 1`),
    and for uniform step cost `sGrad = sReeb = s`, the total weighted numerator equals `q * s`. -/
theorem diracGradReeb_convex_split (q s : Int) :
    diracGradNumerator + diracReebNumerator q = q ∧
    diracWeightedStepNumerator q s s = q * s := by
  unfold diracGradNumerator diracReebNumerator diracWeightedStepNumerator
  have h : 1 * s + (q - 1) * s = q * s := by
    rw [Int.sub_mul, Int.one_mul]
    omega
  exact ⟨by omega, h⟩

/-! ### 2. Figure-eight deformed complex volume conjugation parity (`qou-6s8k`) -/

/-- Complex volume pair `(Vol, CS)` representing `V_41(u) = Vol(u) + i * CS(u)`. -/
structure DeformedComplexVolume where
  volPart : Int
  csPart : Int
  deriving DecidableEq, Repr

/-- Reflection `u |-> -u` acting on a bar-even real part `Vol(-u) = Vol(u)` and a bar-odd
    Chern-Simons imaginary part `CS(-u) = -CS(u)`. -/
def reflectDeformedVolume (v : DeformedComplexVolume) : DeformedComplexVolume :=
  { volPart := v.volPart
    csPart := -v.csPart }

/-- Norm-squared `Vol^2 + CS^2` of the deformed complex volume `V_41(u)`. -/
def deformedVolumeNormSq (v : DeformedComplexVolume) : Int :=
  v.volPart * v.volPart + v.csPart * v.csPart

/-- Reflection `u |-> -u` is an involution (`reflect (reflect v) = v`) that preserves the
    deformed complex volume norm-squared `Vol^2 + CS^2` identically. -/
theorem reflectDeformedVolume_involution_and_normSq (v : DeformedComplexVolume) :
    reflectDeformedVolume (reflectDeformedVolume v) = v ∧
    deformedVolumeNormSq (reflectDeformedVolume v) = deformedVolumeNormSq v := by
  cases v with
  | mk vr vc =>
    dsimp [reflectDeformedVolume, deformedVolumeNormSq]
    have hneg : (-vc) * (-vc) = vc * vc := by
      rw [Int.neg_mul_neg]
    refine ⟨?_, by omega⟩
    simp

/-! ### 3. Parameterized Delta_max two-sided slack margin (`qou-7fyw`) -/

/-- Upper slack margin `bMax - delta` for a parameterized `Delta_max` numerical bound `bMax`. -/
def deltaMaxUpperSlack (bMax delta : Int) : Int :=
  bMax - delta

/-- Lower slack margin `bMax + delta` for a parameterized `Delta_max` numerical bound `bMax`. -/
def deltaMaxLowerSlack (bMax delta : Int) : Int :=
  bMax + delta

/-- The two-sided slack margins sum to `2 * bMax` (independent of `delta`) and their product
    equals the quadratic bound margin `bMax^2 - delta^2`. -/
theorem deltaMax_two_sided_slack_identities (bMax delta : Int) :
    deltaMaxUpperSlack bMax delta + deltaMaxLowerSlack bMax delta = 2 * bMax ∧
    deltaMaxUpperSlack bMax delta * deltaMaxLowerSlack bMax delta =
      bMax * bMax - delta * delta := by
  unfold deltaMaxUpperSlack deltaMaxLowerSlack
  have hprod : (bMax - delta) * (bMax + delta) = bMax * bMax - delta * delta := by
    rw [Int.sub_mul, Int.mul_add, Int.mul_add, Int.mul_comm delta bMax]
    omega
  exact ⟨by omega, hprod⟩

/-! ### 4. GK bilinear block pairing odd/even channel decomposition (`qou-9s8k`) -/

/-- Full 2x2 Garoufalidis-Kashaev bilinear block sum `d00 + d11 + c01 + c10`, where `d00, d11`
    are diagonal bar-even block pairings and `c01, c10` are off-diagonal bar-odd cross-pairings. -/
def gkBilinearTotal (d00 d11 c01 c10 : Int) : Int :=
  (d00 + d11) + (c01 + c10)

/-- Under the bar-parity sign flip `(d00, d11, c01, c10) |-> (d00, d11, -c01, -c10)`,
    half the antisymmetrized difference `gkBilinearTotal(+) - gkBilinearTotal(-)` isolates
    `2 * (c01 + c10)` (the off-diagonal odd channel), while the symmetrized sum isolates
    `2 * (d00 + d11)` (the diagonal even channel). -/
theorem gkBilinear_odd_even_channel_projection (d00 d11 c01 c10 : Int) :
    gkBilinearTotal d00 d11 c01 c10 - gkBilinearTotal d00 d11 (-c01) (-c10) =
      2 * (c01 + c10) ∧
    gkBilinearTotal d00 d11 c01 c10 + gkBilinearTotal d00 d11 (-c01) (-c10) =
      2 * (d00 + d11) := by
  unfold gkBilinearTotal
  omega

/-! ### 5. Harmonic imaginary form `(x^2 - y^2)` diagonal factorization (`qou-cyon`) -/

/-- Unscaled harmonic imaginary quadratic form `Q_harm(x, y) = x^2 - y^2` governing the sign of
    `(sqrt(3)/4) * (x^2 - y^2)` on the u-deformation plane. -/
def harmonicImForm (x y : Int) : Int :=
  x * x - y * y

/-- `harmonicImForm` factors into the diagonal product `(x - y) * (x + y)`, vanishes along both
    diagonals `y = x` and `y = -x`, and is antisymmetric under coordinate swap `(x, y) |-> (y, x)`. -/
theorem harmonicImForm_diagonal_factorization_and_swap (x y : Int) :
    harmonicImForm x y = (x - y) * (x + y) ∧
    harmonicImForm x x = 0 ∧
    harmonicImForm x (-x) = 0 ∧
    harmonicImForm y x = -harmonicImForm x y := by
  unfold harmonicImForm
  have hfac : x * x - y * y = (x - y) * (x + y) := by
    rw [Int.sub_mul, Int.mul_add, Int.mul_add, Int.mul_comm y x]
    omega
  have hneg : (-x) * (-x) = x * x := by
    rw [Int.neg_mul_neg]
  exact ⟨hfac, by omega, by omega, by omega⟩

end QOU.QBeta.DeformedVolumeParityAndDiracReebConvexSplitBrick
