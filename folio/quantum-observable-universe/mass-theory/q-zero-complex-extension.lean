import Mathlib.Analysis.Normed.Field.Basic
import Mathlib.Analysis.Complex.Basic

/-!
# QOU.BraidKnot.QZeroComplexExtension

Records the structural admissibility of complex $q$ with $|q| > 1$
as a specialization of the polymorphic pre-Archimedean substrate.

The existing Hecke / bar-involution / Frobenius / Markov-trace
infrastructure is stated over a generic commutative ring with a
unit parameter $q$; specializing to `R = ℂ` inherits it. This file
proves only the unit-witness `1 < ‖q‖ → IsUnit q` that allows
downstream substrate identities to instantiate at complex $q$.

The proposition does NOT claim $q_0$ is in fact complex (see the
companion audit
[`docs/audits/2026-05-24-q-zero-reality-audit.md`](../../../../docs/audits/2026-05-24-q-zero-reality-audit.md)).
It is research-grade infrastructure for the bar-symmetric /
bar-anti-symmetric decomposition refinement.
-/

-- Ref: [leitner2026] prop:q-zero-complex-extension
-- Ref: [leitner2026] def:bar-involution
-- Ref: [wenzl1988] doi:10.1007/BF01404457

namespace QOU.BraidKnot.QZeroComplexExtension

open scoped ComplexConjugate

/-- Structural admissibility witness: if `1 < ‖q‖` in `ℂ` then `q`
    is a unit, so the polymorphic substrate identities (Hecke
    quadratic, bar involution, Frobenius pairing, Markov trace)
    specialize at `R = ℂ` without modification. -/
theorem complex_q_is_unit (q : ℂ) (hq : 1 < ‖q‖) : IsUnit q := by
  apply isUnit_iff_ne_zero.mpr
  intro h
  rw [h, norm_zero] at hq
  linarith

/-- The complement statement on the modulus: `|q| > 1` rules out
    `q = 0` directly. -/
theorem complex_q_ne_zero (q : ℂ) (hq : 1 < ‖q‖) : q ≠ 0 := by
  intro h
  rw [h, norm_zero] at hq
  linarith

end QOU.BraidKnot.QZeroComplexExtension
