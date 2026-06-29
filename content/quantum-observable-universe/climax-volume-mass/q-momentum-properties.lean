import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.List.Basic


/-!
# QOU.Archimedean.QMomentumProperties — properties of q-momentum

Additivity under concatenation, Markov-I conjugation invariance,
Markov-II stabilisation shift, and parity behaviour of the q-momentum.

LaTeX: `\label{prop:q-momentum-properties}`
-/

namespace QOU.Archimedean

noncomputable section

/-- The q-momentum of a braid, computed from its crossing signs
    (mirror of `QOU.Archimedean.qMomentum`). -/
def qMomentumP (q : LaurentPolynomial ℤ) (crossingSigns : List ℤ) :
    LaurentPolynomial ℤ :=
  crossingSigns.foldl (fun acc ε =>
    acc + (q ^ (2 * ε) - 1) / (q ^ 2 - 1)) 0

/-- **Additivity of q-momentum under braid concatenation.**

    `p_q(β₁β₂) = p_q(β₁) + p_q(β₂)`, encoded at the level of crossing-
    sign lists as `qMomentumP q (s₁ ++ s₂) = qMomentumP q s₁ +
    qMomentumP q s₂`.  Follows from the trace being additive on the
    Iwahori–Hecke algebra; the foldl-decomposition is in the companion
    `QMomentum` file. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [manuscript] climax-volume-mass/q-momentum-properties
theorem qMomentumP_additive (q : LaurentPolynomial ℤ) (s₁ s₂ : List ℤ) :
    qMomentumP q (s₁ ++ s₂) = qMomentumP q s₁ + qMomentumP q s₂ := by
  -- Ref: [manuscript] climax-volume-mass/q-momentum-properties
  sorry

end QOU.Archimedean
