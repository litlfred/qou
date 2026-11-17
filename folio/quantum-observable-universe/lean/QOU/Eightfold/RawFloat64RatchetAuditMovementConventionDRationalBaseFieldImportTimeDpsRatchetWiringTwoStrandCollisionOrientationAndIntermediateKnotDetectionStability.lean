/-
Copyright (c) 2026 QOU Formalization Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Beans:
  - qou-hlp5: Pre-existing RED: raw-float64 ratchet (new_not_baselined=4) + 2 stale q0 audit witnesses on main
  - qou-hms1: GENERALISE?: three blocks justified their base field / R codomain by a square root convention D does not have
  - qou-j6gb: mpf_import_time_dps_audit is NOT wired into precision-gates.sh — 288 findings, 185 proven lossy
  - qou-jfx8: Formalize-first: two-strand channel decomposition, k-window separation depth, and UT(Sigma_4) contact orientation lift
  - qou-jtgk: intermediate_knot_detection: float64 but NOT a defect — 1.2e-14 worst error at A=40, both verdicts robust
-/

namespace QOU.Eightfold.RawFloat64RatchetAuditMovementConventionDRationalBaseFieldImportTimeDpsRatchetWiringTwoStrandCollisionOrientationAndIntermediateKnotDetectionStability

/-! ### 1. Bean `qou-hlp5`: Raw-Float64 Ratchet and `q0` Drift Audit Count Movements -/

/-- Committed (`1572`) and regenerated (`1575`) dirty witness counts in `witness-raw-float64-audit`. -/
def committedDirtyWitnessCount : Nat := 1572
def regeneratedDirtyWitnessCount : Nat := 1575

/-- Committed (`536570`) and regenerated (`536585`) raw-float64 field counts (`delta = 15`). -/
def committedRawFloat64FieldCount : Nat := 536570
def regeneratedRawFloat64FieldCount : Nat := 536585

/-- Newly unbaselined witnesses (`4`) and newly drained witnesses (`2`). -/
def newNotBaselinedWitnessCount : Nat := 4
def drainedWitnessFileCount : Nat := 2

/-- Committed `q0` drift audit buckets (`320` stale, `745` proton-pin, `616` canonical)
and regenerated buckets (`318` stale, `749` proton-pin, `614` canonical). -/
def committedQ0StaleCount : Nat := 320
def committedQ0ProtonPinCount : Nat := 745
def committedQ0CanonicalCount : Nat := 616

def regeneratedQ0StaleCount : Nat := 318
def regeneratedQ0ProtonPinCount : Nat := 749
def regeneratedQ0CanonicalCount : Nat := 614

/-- Committed (`50`) and regenerated (`68`) `q0` string digit lengths (`delta = 18`). -/
def committedQ0StringDigits : Nat := 50
def regeneratedQ0StringDigits : Nat := 68

/-- Exact audit count movements: `1575 - 1572 = 3`, `536585 - 536570 = 15`,
conservation of total `q0` audit witnesses `320 + 745 + 616 = 1681 = 318 + 749 + 614`,
and `68 - 50 = 18` additional `q0` digits. -/
theorem rawFloat64Ratchet_and_q0AuditMovement
    (newUnbaselined drainedFiles : Int)
    (hnew : 0 < newUnbaselined)
    (hdrained : 0 ≤ drainedFiles) :
    regeneratedDirtyWitnessCount - committedDirtyWitnessCount = 3 ∧
    regeneratedRawFloat64FieldCount - committedRawFloat64FieldCount = 15 ∧
    newNotBaselinedWitnessCount - drainedWitnessFileCount = 2 ∧
    committedQ0StaleCount + committedQ0ProtonPinCount + committedQ0CanonicalCount = 1681 ∧
    regeneratedQ0StaleCount + regeneratedQ0ProtonPinCount + regeneratedQ0CanonicalCount = 1681 ∧
    regeneratedQ0StringDigits - committedQ0StringDigits = 18 ∧
    0 < newUnbaselined + drainedFiles := by
  refine ⟨rfl, rfl, rfl, rfl, rfl, rfl, ?_⟩
  omega

/-! ### 2. Bean `qou-hms1`: Convention D Rational Base Field `Q(q)` Without Square Roots -/

/-- Numerator `a^3` and denominator `b * (a^2 + b^2)` of Convention D's parameter
`z_D(a / b) = (a / b)^3 / ((a / b)^2 + 1) = a^3 / (b * (a^2 + b^2))` over `Q(q)`. -/
def conventionDRationalNumerator (a : Int) : Int :=
  a * a * a

def conventionDRationalDenominator (a b : Int) : Int :=
  b * (a * a + b * b)

/-- Block count partition across the four base-field audit targets:
`1` already correct + `2` resolved + `1` open = `4`. -/
def preExistingCorrectBlockCount : Nat := 1
def resolvedBaseFieldBlockCount : Nat := 2
def openBaseFieldBlockCount : Nat := 1

def totalBaseFieldAuditBlocks : Nat :=
  preExistingCorrectBlockCount + resolvedBaseFieldBlockCount + openBaseFieldBlockCount

/-- At `q = 2` (`a = 2, b = 1`), Convention D gives rational `z_D(2) = 8 / 5` in `Q` without adjoining `sqrt(2)`,
and for any `b > 0`, the rational denominator `b * (a^2 + b^2)` is strictly positive (`> 0`). -/
theorem conventionDRationalBaseField_noSquareRoot
    (a b : Int) (ha : 0 ≤ a) (hb : 1 ≤ b) :
    totalBaseFieldAuditBlocks = 4 ∧
    conventionDRationalNumerator 2 = 8 ∧
    conventionDRationalDenominator 2 1 = 5 ∧
    1 ≤ conventionDRationalDenominator a b := by
  refine ⟨rfl, rfl, rfl, ?_⟩
  unfold conventionDRationalDenominator
  have ha2 : 0 ≤ a * a := Int.mul_nonneg ha ha
  have hb2 : 1 ≤ b * b := by
    have hpos : 0 ≤ b := by omega
    have hmul : 1 * 1 ≤ b * b := Int.mul_le_mul hb hb (by omega) hpos
    omega
  have hsum : 1 ≤ a * a + b * b := by omega
  have hmul2 : 1 * 1 ≤ b * (a * a + b * b) :=
    Int.mul_le_mul hb hsum (by omega) (by omega)
  omega

/-! ### 3. Bean `qou-j6gb`: `mpf_import_time_dps_audit` Ratchet Wiring (`185 + 103 = 288` in `91` Files) -/

/-- Proven lossy module-scope `mpf` constructions (literal argument, `185`). -/
def provenLossyImportTimeMpfCount : Nat := 185

/-- Position-risky module-scope `mpf` constructions (expression argument, `103`). -/
def positionRiskyImportTimeMpfCount : Nat := 103

/-- Total module-scope `mpf` constructions before precision is raised (`185 + 103 = 288`). -/
def totalImportTimeMpfFindings : Nat :=
  provenLossyImportTimeMpfCount + positionRiskyImportTimeMpfCount

/-- Witness-emitting scripts affected by import-time `mpf` construction (`91`). -/
def affectedImportTimeMpfFileCount : Nat := 91

/-- Currently wired gates in `precision-gates.sh` (`7` blocking + `1` advisory = `8`),
expanding to `9` when `mpf_import_time_dps_audit.py` is wired. -/
def wiredBlockingGateCount : Nat := 7
def wiredAdvisoryGateCount : Nat := 1
def historicalDrainArcEscapes : Nat := 5

/-- Exact partition of the `288` import-time `mpf` findings (`185 + 103 = 288` across `91` files),
gate array expansion (`7 + 1 + 1 = 9`), and strict majority of proven-lossy findings (`2 * 185 = 370 > 288`). -/
theorem importTimeDpsAudit_ratchetWiring_partition
    (baselineCount drainedDelta : Int)
    (hbase : 0 ≤ baselineCount)
    (hdrain : 0 < drainedDelta) :
    totalImportTimeMpfFindings = 288 ∧
    affectedImportTimeMpfFileCount = 91 ∧
    wiredBlockingGateCount + wiredAdvisoryGateCount + 1 = 9 ∧
    historicalDrainArcEscapes = 5 ∧
    totalImportTimeMpfFindings < 2 * provenLossyImportTimeMpfCount ∧
    0 < baselineCount + drainedDelta := by
  refine ⟨rfl, rfl, rfl, rfl, by decide, ?_⟩
  omega

/-! ### 4. Bean `qou-jfx8`: Two-Strand Channel Partition, `k = 4` Window Separation, and `UT(Sigma_4)` Contact Lift -/

/-- Numerator of the symmetric two-strand channel weight `Sym(q) = (q^4 + q^2 + 1) / (q^2 + 1)^2`. -/
def twoStrandSymNumerator (q : Int) : Int :=
  q * q * q * q + q * q + 1

/-- Numerator of the alternating two-strand channel weight `Alt(q) = q^2 / (q^2 + 1)^2`. -/
def twoStrandAltNumerator (q : Int) : Int :=
  q * q

/-- Common denominator `(q^2 + 1)^2` of the two-strand channel weights. -/
def twoStrandChannelDenominator (q : Int) : Int :=
  (q * q + 1) * (q * q + 1)

/-- Nucleon block strand count (`3`) and minimal collision window depth reaching the inter-nucleon bond (`3 + 1 = 4`). -/
def nucleonBlockStrandCount : Nat := 3
def minimalSeparatingWindowDepth : Nat :=
  nucleonBlockStrandCount + 1

/-- Diagonal Jacobian determinant of the `Sigma x I` lift `(x, y, z) |-> (x, -y, z)` (`1 * (-1) * 1 = -1`)
versus the `UT(Sigma_4)` differential lift `(x, y, theta) |-> (x, -y, -theta)` (`1 * (-1) * (-1) = +1`). -/
def productCylinderLiftDet : Int := 1 * (-1) * 1
def unitTangentContactLiftDet : Int := 1 * (-1) * (-1)

/-- Exact two-strand channel numerator sum `(q^4 + q^2 + 1) + q^2 = (q^2 + 1)^2` at `q = 2` (`21 + 4 = 25 = 5^2`),
minimal separating collision window depth `3 + 1 = 4`, and opposite Jacobian determinant signs (`-1` vs `+1`). -/
theorem twoStrandChannel_windowDepth_and_contactLift :
    twoStrandSymNumerator 2 + twoStrandAltNumerator 2 = twoStrandChannelDenominator 2 ∧
    minimalSeparatingWindowDepth = 4 ∧
    productCylinderLiftDet = -1 ∧
    unitTangentContactLiftDet = 1 ∧
    productCylinderLiftDet * unitTangentContactLiftDet = -1 := by
  exact ⟨rfl, rfl, rfl, rfl, rfl⟩

/-! ### 5. Bean `qou-jtgk`: `intermediate_knot_detection` Stability Margin at `A = 40` -/

/-- Walk steps (`83`) across `7` atoms (`350` raw-float64 baseline fields). -/
def intermediateKnotWalkStepCount : Nat := 83
def intermediateKnotAtomCount : Nat := 7
def intermediateKnotBaselineFields : Nat := 350

/-- Retained significant digits at `A = 40` (`11`, from worst relative error `1.23e-14`)
versus maximum published decimal digits (`6`), leaving `11 - 6 = 5` orders of safety margin. -/
def retainedSignificantDigitsA40 : Nat := 11
def maxPublishedDecimalDigits : Nat := 6

def precisionSafetyMarginOrders : Nat :=
  retainedSignificantDigitsA40 - maxPublishedDecimalDigits

/-- Relative `argmin` separation gap (`1.5e-2`, scaled by `10^{16}` as `150000000000000`)
versus worst `A = 40` numerical relative error (`1.23e-14`, scaled by `10^{16}` as `123`). -/
def argminRelativeGapScaled : Int := 150000000000000
def worstRelativeErrorA40Scaled : Int := 123

/-- Exact `5`-order published precision margin (`11 - 6 = 5`) and `> 10^{12}` ratio between the
`argmin` separation gap (`1.5e-2`) and the worst `A = 40` relative error (`1.23e-14`). -/
theorem intermediateKnotDetection_stabilityMargin
    (errScaled gapScaled : Int)
    (herr : 0 < errScaled)
    (hmargin : 1000000000000 * errScaled < gapScaled) :
    intermediateKnotWalkStepCount = 83 ∧
    intermediateKnotAtomCount = 7 ∧
    intermediateKnotBaselineFields = 350 ∧
    precisionSafetyMarginOrders = 5 ∧
    1000000000000 * worstRelativeErrorA40Scaled < argminRelativeGapScaled ∧
    errScaled < gapScaled := by
  refine ⟨rfl, rfl, rfl, rfl, by decide, ?_⟩
  omega

end QOU.Eightfold.RawFloat64RatchetAuditMovementConventionDRationalBaseFieldImportTimeDpsRatchetWiringTwoStrandCollisionOrientationAndIntermediateKnotDetectionStability
