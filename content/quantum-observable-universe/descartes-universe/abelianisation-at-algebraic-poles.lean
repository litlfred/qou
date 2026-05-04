/-!
# MI abelianisation at algebraic poles (conjecture class)

The conjecture: at each τ_arch-image of a q-Pochhammer denominator
zero, the nonabelian multiplicative integral abelianises to the
prolonged Seiberg-Witten differential.  Class-based per CLAUDE.md
§3b.

-- Ref: [manuscript] conj:abelianisation-at-algebraic-poles
-- Ref: [witten2011] https://doi.org/10.1090/amsip/050/19
-/

import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

namespace QOU.PicardLefschetz

/-- Placeholder: the nonabelian MI restricted to the exceptional
    divisor at `z_c`, projected onto the `n`-th jet. -/
-- Ref: [manuscript] prop:mi-sw-abelianisation
opaque miOnDivisor (n : ℕ) (z_c : ℂ) : ℂ

/-- Placeholder: the prolonged SW period on the same divisor. -/
-- Ref: [manuscript] prop:mi-sw-abelianisation
opaque swPeriod (n : ℕ) (z_c : ℂ) : ℂ

/-- The conjecture as a typeclass over a state variable `x`,
    substrate `q`, depth `n`, and a denominator-zero index `k < n`.
    An instance asserts that the MI evaluated at the τ_arch-image
    of the algebraic zero equals the SW prolonged period. -/
-- Ref: [manuscript] conj:abelianisation-at-algebraic-poles
class AbelianisationAtAlgebraicPole
    (q x : ℝ) (n : ℕ) (k : ℕ) : Type where
  /-- The matched τ_arch-image of `x = q^{-k}`. -/
  matched_critical_point : ℂ
  /-- MI on this divisor equals the SW period. -/
  mi_eq_sw : miOnDivisor n matched_critical_point
              = swPeriod n matched_critical_point

/-- Stated form: at the matched critical point, MI equals the SW
    prolonged period.  Inhabited only via a class instance. -/
-- Ref: [manuscript] conj:abelianisation-at-algebraic-poles
theorem abelianisation_at_algebraic_poles
    (q x : ℝ) (n : ℕ) (k : ℕ)
    [h : AbelianisationAtAlgebraicPole q x n k] :
    miOnDivisor n h.matched_critical_point
      = swPeriod n h.matched_critical_point :=
  h.mi_eq_sw

end QOU.PicardLefschetz
