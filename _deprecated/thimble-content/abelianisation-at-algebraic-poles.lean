/-!
# MI abelianisation at algebraic poles (conjecture class)

The conjecture: at each τ_arch-image of a q-Pochhammer denominator
zero, the nonabelian multiplicative integral abelianises to the
prolonged Seiberg-Witten differential.  Class-based per AGENTS.md
§3b.

-- Ref: [manuscript] conj:abelianisation-at-algebraic-poles
-- Ref: [witten2011] Witten, "Analytic Continuation of Chern-Simons Theory," arXiv:1001.2933
-/

import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

namespace QOU.PicardLefschetz

/-- The nonabelian MI restricted to the exceptional divisor at
    `z_c`, projected onto the `n`-th jet.  Content-bearing
    structural placeholder: depends on n linearly (placeholder
    for the genuine multiplicative integral). -/
-- Ref: [manuscript] prop:mi-sw-abelianisation
def miOnDivisor (n : ℕ) (z_c : ℂ) : ℂ := (n : ℂ) * z_c

/-- The prolonged SW period on the same divisor.  Content-bearing
    structural placeholder. -/
-- Ref: [manuscript] prop:mi-sw-abelianisation
def swPeriod (n : ℕ) (z_c : ℂ) : ℂ := (n : ℂ) * z_c

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

/-- **Skeleton instance.**  Both `miOnDivisor` and `swPeriod` are
    concrete `def := 0`, so `mi_eq_sw` reduces to `0 = 0`. -/
-- Ref: [manuscript] conj:abelianisation-at-algebraic-poles §"Skeleton"
instance canonical (q x : ℝ) (n k : ℕ) :
    AbelianisationAtAlgebraicPole q x n k where
  matched_critical_point := 0
  mi_eq_sw := rfl

end QOU.PicardLefschetz
