/-
Copyright (c) 2026 litlfred. All rights reserved.

# Q_β W-odd tranche: bar-odd categorical net identity

This module proves the identity for the W-odd tranche of the H₃ GS categorical net:
the bar-odd part of the net decay-width Laurent polynomial evaluates exactly to
(h / 4) · C(q² + q⁻²), where h = q - q⁻¹ and C(y) is the irreducible odd-channel cubic.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import QOU.QBeta.QBetaZeta4ResidueRefutation

namespace QOU.QBeta.WOddTranche

open QOU.QBeta.Zeta4Residue

variable {F : Type*} [Field F]

/-- The bar-odd part of the net exactly reproduces the KC20 odd-channel cubic
    with ratio `(q - q⁻¹) / 4`. -/
theorem net_odd_eq_cubic_trace (q : F) (hq : q ≠ 0) :
    numOdd q / (4 * q ^ 7) = ((q - q⁻¹) / 4) * cubicC (q ^ 2 + q⁻¹ ^ 2) := by
  -- `numOdd` is `(q^2 - 1) * R12`
  rw [numOdd_factor]
  -- `R12` relates to `cubicC`
  have hR : R12 q = q ^ 6 * cubicC (q ^ 2 + q⁻¹ ^ 2) := R12_eq_cubic_trace q hq
  rw [hR]
  field_simp

/-- The modulated bar-odd component of the categorical net with crossing weight `w` attached.
    The Hopf sector (2 crossings) is scaled by `w^2`, while the unknot sector
    (0 crossings) is scaled by `w^0 = 1`. -/
def netOddModulated (q w : F) : F :=
  ((q - q⁻¹) / 4) * (w ^ 2 * cubicC_Hopf (q ^ 2 + q⁻¹ ^ 2) + cubicC_unknot (q ^ 2 + q⁻¹ ^ 2))

/-- When the crossing weight `w = 1`, the modulated odd channel recovers the original
    unweighted categorical net bar-odd component. -/
theorem netOddModulated_one (q : F) (hq : q ≠ 0) :
    netOddModulated q 1 = numOdd q / (4 * q ^ 7) := by
  unfold netOddModulated
  rw [one_pow, one_mul, ← cubicC_sector_decomp]
  exact (net_odd_eq_cubic_trace q hq).symm

end QOU.QBeta.WOddTranche
