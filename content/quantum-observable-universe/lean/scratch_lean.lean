import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

-- Assume we have the QBeta definitions
def numOdd (q : R) [CommRing R] : R :=
  q ^ 14 - 5 * q ^ 12 + 10 * q ^ 10 - 16 * q ^ 8 + 16 * q ^ 6
    - 10 * q ^ 4 + 5 * q ^ 2 - 1

def R12 (q : R) [CommRing R] : R :=
  q ^ 12 - 4 * q ^ 10 + 6 * q ^ 8 - 10 * q ^ 6 + 6 * q ^ 4 - 4 * q ^ 2 + 1

def cubicC (y : R) [CommRing R] : R := y ^ 3 - 4 * y ^ 2 + 3 * y - 2

theorem numOdd_factor {R : Type*} [CommRing R] (q : R) : numOdd q = (q ^ 2 - 1) * R12 q := by
  unfold numOdd R12; ring

theorem w_odd_categorical_net {F : Type*} [Field F] (q : F) (hq : q ≠ 0) :
    numOdd q / (4 * q ^ 7) = ((q - q⁻¹) / 4) * cubicC (q ^ 2 + q⁻¹ ^ 2) := by
  have hR : R12 q = q ^ 6 * cubicC (q ^ 2 + q⁻¹ ^ 2) := by
    unfold R12 cubicC; field_simp; ring
  rw [numOdd_factor, hR]
  field_simp
  ring

