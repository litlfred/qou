import QOU.Transcendental.Nuclear.HadronChargeLineCoulomb
import Mathlib.Analysis.SpecialFunctions.Complex.Log

/-!
# A unitary charge-line braiding carries no real pair energy

Audit `docs/audits/2026-11-21-neutron-heavier-sign.md` §37. `HadronChargeLineCoulomb` gives the
hadron-line pair energy as the log of the line monodromy, `κ·Q_A·Q_B` with `κ = 2 log t` for real
`t > 0`. If instead `t` is a unitary braiding phase, as for a U(1) Chern–Simons line (`|t| = 1`),
the monodromy has modulus one for every pair of charges, so the real part of its log vanishes:
there is no real charge–charge energy at all. A real Coulomb pair term therefore needs a
non-unitary `t`. No empirical input.
-/

namespace QOU.QBeta.UnitaryLineNoEnergy

open QOU.QBeta.HadronChargeLineCoulomb

/-- The monodromy of a unitary line braiding has modulus one. -/
theorem norm_monodromy_of_unitary (t : ℂ) (ht : ‖t‖ = 1) (Q Q' : ℤ) :
    ‖monodromy t Q Q'‖ = 1 := by
  have ht0 : t ≠ 0 := by intro h; simp [h] at ht
  rw [monodromy_eq t ht0, norm_zpow, ht, one_zpow]

/-- Hence the real pair energy `Re log` of a unitary monodromy is zero for all charges. -/
theorem re_log_monodromy_of_unitary (t : ℂ) (ht : ‖t‖ = 1) (Q Q' : ℤ) :
    (Complex.log (monodromy t Q Q')).re = 0 := by
  rw [Complex.log_re, norm_monodromy_of_unitary t ht, Real.log_one]

end QOU.QBeta.UnitaryLineNoEnergy
