import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination


/-!
# QOU.BraidsAndKnots.skein_bar_antisymmetry — Bar-antisymmetry of Skein

The Hecke–Skein relation L_+ − L_− = (q − q⁻¹) L_0 is antisymmetric
under the bar involution that swaps (L_+, L_−) and (q, q⁻¹).

This file abstracts the Skein relation as an algebraic identity in
a commutative ring R with a unit q ∈ Rˣ. The bar involution acts on
triples (L_+, L_−, L_0) with values in R by swapping the first two
and inverting q.

LaTeX label: `prop:skein-bar-antisymmetry`

## References

- [leitner2026] §5/skein-bar-antisymmetry
- [leitner2026] §5/iwahori-hecke-algebra
-/

namespace QOU.BraidsAndKnots.SkeinBarAntisymmetry

variable {R : Type*} [CommRing R]

/-- The Skein relation: L_+ − L_− = (q − q⁻¹) · L_0, evaluated in
    the field of fractions (or any ring where q is a unit). -/
def SkeinRel (q Lp Lm L0 : R) (qInv : R) (hq : q * qInv = 1) : Prop :=
  Lp - Lm = (q - qInv) * L0

/-- **Bar-antisymmetry of the Skein relation.**

    Substituting (Lp, Lm, q, qInv) ↦ (Lm, Lp, qInv, q) into the
    Skein relation yields the negation of the original relation. -/
-- Ref: [leitner2026] §5/skein-bar-antisymmetry
theorem skein_bar_antisymmetry
    (q Lp Lm L0 qInv : R) (hq : q * qInv = 1)
    (h : SkeinRel q Lp Lm L0 qInv hq) :
    -- The bar-image of the relation:
    Lm - Lp = (qInv - q) * L0 := by
  unfold SkeinRel at h
  linear_combination -h

/-- **Sign-flip identity**: the bar-image of (q − q⁻¹) is −(q − q⁻¹). -/
-- Ref: [leitner2026] §5/skein-bar-antisymmetry
theorem bar_q_minus_qInv (q qInv : R) : qInv - q = -(q - qInv) := by ring

/-- **Sign-flip identity**: the bar-image of (Lp − Lm) is −(Lp − Lm). -/
-- Ref: [leitner2026] §5/skein-bar-antisymmetry
theorem bar_Lp_minus_Lm (Lp Lm : R) : Lm - Lp = -(Lp - Lm) := by ring

/-- **Both sides flip together**: applying bar to the Skein relation
    multiplies both sides by −1, leaving the equation unchanged
    (consistency of bar-antisymmetry). -/
-- Ref: [leitner2026] §5/skein-bar-antisymmetry
theorem skein_bar_consistent
    (q Lp Lm L0 qInv : R) (hq : q * qInv = 1) :
    SkeinRel q Lp Lm L0 qInv hq ↔
    SkeinRel qInv Lm Lp L0 q (by rw [mul_comm]; exact hq) := by
  unfold SkeinRel
  constructor
  · intro h; linear_combination -h
  · intro h; linear_combination -h

/-- **Skein bar-antisymmetry** (Proposition):

    The Skein relation in any commutative ring is antisymmetric
    under simultaneous swap of (L_+, L_-) and (q, q⁻¹), and the
    bar-image relation is logically equivalent to the original. -/
-- Ref: [leitner2026] §5/skein-bar-antisymmetry
theorem skein_bar_antisymmetry_full
    (q Lp Lm L0 qInv : R) (hq : q * qInv = 1) :
    (SkeinRel q Lp Lm L0 qInv hq →
      Lm - Lp = (qInv - q) * L0) ∧
    (SkeinRel q Lp Lm L0 qInv hq ↔
      SkeinRel qInv Lm Lp L0 q (by rw [mul_comm]; exact hq)) :=
  ⟨skein_bar_antisymmetry q Lp Lm L0 qInv hq,
   skein_bar_consistent q Lp Lm L0 qInv hq⟩

end QOU.BraidsAndKnots.SkeinBarAntisymmetry
