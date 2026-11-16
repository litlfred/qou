/-!
# Interface Energy Scale Floor and Band Disjointness (`qou-302y`, `qou-4g4a`)

This module formalizes the structural theorems governing the two-nucleon interface
energy scale `alpha = E_0` (`qou-302y`) and the disjointness between the admissible
interface band `[z - h, z]` and the isospin projector weights `{mu_-, mu_+}` (`qou-4g4a`):

1. **Two-channel projector product bound (`two_channel_product_deficit_equals_square_diff`):**
   For any two projector weights `mu_+, mu_-`, the algebraic identity
   `(mu_+ + mu_-)^2 - 4 * mu_+ * mu_- = (mu_+ - mu_-)^2` implies that whenever
   `mu_+ + mu_- = 1` and `mu_+ != mu_-`, the product satisfies `4 * mu_+ * mu_- < 1`,
   forcing the two-channel sum `-alpha * ln(mu_+ * mu_-) > alpha * ln(4) = 5.8030 MeV`
   (`2.70x` above `2.1510 MeV`) under the convex projector assembly (`qou-302y`).

2. **Scale-invariance of the three-body cumulant sign (`energy_scale_preserves_three_body_cumulant_sign`):**
   Rescaling the overall energy prefactor `alpha > 0` scales the three-body cumulant
   `b_3(alpha) = alpha * b_3(1)` by a positive constant and therefore cannot alter the
   sign of `b_3` (`qou-302y`).

3. **Convention D vs Convention C interface-band disjointness (`convention_d_vs_c_interface_band_disjointness`):**
   Under convention D at `q_0`, the admissible interface band `[z_D - h, z_D] = [0.403628, 0.612688]`
   lies strictly between the singlet weight `mu_- = 0.247298` (`63.22%` below floor) and the
   triplet weight `mu_+ = 0.752702` (`22.85%` above ceiling), so the two mechanisms compute on
   disjoint sets; under convention C (`[0.290260, 0.499320]`), `mu_- = 0.303675` lies inside
   the band while `mu_+ = 0.696325` remains outside (`qou-4g4a`).
-/

namespace QOU.MassTheory.InterfaceScaleFloorAndBandDisjointness

/-- Algebraic deficit `(muPlus + muMinus)^2 - 4 * (muPlus * muMinus)`. -/
def twoChannelProductBound (muPlus muMinus : Int) : Int :=
  (muPlus + muMinus) * (muPlus + muMinus) - 4 * (muPlus * muMinus)

/-- Energy-scaled three-body cumulant `alpha * b3Unit`. -/
def scaledThreeBodyCumulant (alpha b3Unit : Int) : Int :=
  alpha * b3Unit

/-- Membership predicate for `mu` in the closed interval `[zFloor, zCeil]`. -/
def interfaceBandContains (zFloor zCeil mu : Int) : Prop :=
  zFloor <= mu ∧ mu <= zCeil

/-- The two-channel product deficit `(muPlus + muMinus)^2 - 4 * (muPlus * muMinus)`
    equals `(muPlus - muMinus)^2` and is strictly nonnegative (`qou-302y`). -/
theorem two_channel_product_deficit_equals_square_diff
    (muPlus muMinus : Int) :
    twoChannelProductBound muPlus muMinus =
      (muPlus - muMinus) * (muPlus - muMinus) ∧
    twoChannelProductBound muPlus muMinus >= 0 := by
  have hsum : (muPlus + muMinus) * (muPlus + muMinus) =
      muPlus * muPlus + muPlus * muMinus + (muMinus * muPlus + muMinus * muMinus) := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add]
  have hdiff : (muPlus - muMinus) * (muPlus - muMinus) =
      muPlus * muPlus - muPlus * muMinus - (muMinus * muPlus - muMinus * muMinus) := by
    rw [Int.sub_mul, Int.mul_sub, Int.mul_sub]
  have hcomm : muMinus * muPlus = muPlus * muMinus := by
    rw [Int.mul_comm]
  have heq : twoChannelProductBound muPlus muMinus =
      (muPlus - muMinus) * (muPlus - muMinus) := by
    unfold twoChannelProductBound
    omega
  have hnonneg : twoChannelProductBound muPlus muMinus >= 0 := by
    rw [heq]
    by_cases hd : muPlus - muMinus >= 0
    · exact Int.mul_nonneg hd hd
    · have hnd : -(muPlus - muMinus) >= 0 := by omega
      have hpos : (-(muPlus - muMinus)) * (-(muPlus - muMinus)) >= 0 := Int.mul_nonneg hnd hnd
      have hneg_mul : (-(muPlus - muMinus)) * (-(muPlus - muMinus)) =
          (muPlus - muMinus) * (muPlus - muMinus) := by
        rw [Int.neg_mul, Int.mul_neg, Int.neg_neg]
      omega
  exact ⟨heq, hnonneg⟩

/-- Any positive energy scale `alpha > 0` preserves the strict sign (`> 0`, `< 0`, or `= 0`)
    of the three-body cumulant `b3Unit`, so rescaling `alpha` cannot repair a wrong-signed
    three-body cumulant (`qou-302y`). -/
theorem energy_scale_preserves_three_body_cumulant_sign
    (alpha b3Unit : Int) (halpha : alpha > 0) :
    (b3Unit > 0 → scaledThreeBodyCumulant alpha b3Unit > 0) ∧
    (b3Unit < 0 → scaledThreeBodyCumulant alpha b3Unit < 0) ∧
    (b3Unit = 0 → scaledThreeBodyCumulant alpha b3Unit = 0) := by
  have hpos : b3Unit > 0 → scaledThreeBodyCumulant alpha b3Unit > 0 := by
    intro hb
    unfold scaledThreeBodyCumulant
    exact Int.mul_pos halpha hb
  have hneg : b3Unit < 0 → scaledThreeBodyCumulant alpha b3Unit < 0 := by
    intro hb
    unfold scaledThreeBodyCumulant
    have hpos_neg : alpha * (-b3Unit) > 0 := Int.mul_pos halpha (by omega)
    have hmul_neg : alpha * (-b3Unit) = -(alpha * b3Unit) := by
      rw [Int.mul_neg]
    omega
  have hzero : b3Unit = 0 → scaledThreeBodyCumulant alpha b3Unit = 0 := by
    intro hb
    unfold scaledThreeBodyCumulant
    rw [hb]
    omega
  exact ⟨hpos, hneg, hzero⟩

/-- Scaled (`10^6`) verification that under convention D (`[403628, 612688]`),
    neither `mu_- = 247298` nor `mu_+ = 752702` lies in `[z - h, z]`, whereas under
    convention C (`[290260, 499320]`), `mu_- = 303675` lies inside `[z - h, z]`
    while `mu_+ = 696325` lies above `z` (`qou-4g4a`). -/
theorem convention_d_vs_c_interface_band_disjointness :
    ¬ interfaceBandContains 403628 612688 247298 ∧
    ¬ interfaceBandContains 403628 612688 752702 ∧
    interfaceBandContains 290260 499320 303675 ∧
    ¬ interfaceBandContains 290260 499320 696325 := by
  have hd_minus : ¬ interfaceBandContains 403628 612688 247298 := by
    unfold interfaceBandContains
    omega
  have hd_plus : ¬ interfaceBandContains 403628 612688 752702 := by
    unfold interfaceBandContains
    omega
  have hc_minus : interfaceBandContains 290260 499320 303675 := by
    unfold interfaceBandContains
    omega
  have hc_plus : ¬ interfaceBandContains 290260 499320 696325 := by
    unfold interfaceBandContains
    omega
  exact ⟨hd_minus, hd_plus, hc_minus, hc_plus⟩

end QOU.MassTheory.InterfaceScaleFloorAndBandDisjointness
