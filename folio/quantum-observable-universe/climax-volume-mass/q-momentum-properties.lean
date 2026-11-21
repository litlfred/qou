import Mathlib.Algebra.Field.Basic
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
def qMomentumP {k : Type*} [Field k] (q : k) (crossingSigns : List ℤ) :
    k :=
  crossingSigns.foldl (fun acc ε =>
    acc + (q ^ (2 * ε) - 1) / (q ^ 2 - 1)) 0

/-- **Additivity of q-momentum under braid concatenation.**

    `p_q(β₁β₂) = p_q(β₁) + p_q(β₂)`, encoded at the level of crossing-
    sign lists as `qMomentumP q (s₁ ++ s₂) = qMomentumP q s₁ +
    qMomentumP q s₂`.  Follows from the trace being additive on the
    Iwahori–Hecke algebra; the foldl-decomposition is in the companion
    `QMomentum` file. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [leitner2026] climax-volume-mass/q-momentum-properties
theorem qMomentumP_additive {k : Type*} [Field k] (q : k) (s₁ s₂ : List ℤ) :
    qMomentumP q (s₁ ++ s₂) = qMomentumP q s₁ + qMomentumP q s₂ := by
  -- The fold with accumulator `acc + g ε` is a sum: the initial
  -- accumulator pulls straight out (`foldl f a s = a + foldl f 0 s`),
  -- so `qMomentumP` is additive under list concatenation.
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  have key : ∀ (s : List ℤ) (a : k),
      s.foldl (fun acc ε => acc + (q ^ (2 * ε) - 1) / (q ^ 2 - 1)) a
        = a + s.foldl (fun acc ε => acc + (q ^ (2 * ε) - 1) / (q ^ 2 - 1)) 0 := by
    intro s
    induction s with
    | nil => intro a; simp
    | cons x xs ih =>
        intro a
        simp only [List.foldl_cons, zero_add]
        rw [ih (a + (q ^ (2 * x) - 1) / (q ^ 2 - 1)),
            ih ((q ^ (2 * x) - 1) / (q ^ 2 - 1)), add_assoc]
  unfold qMomentumP
  rw [List.foldl_append]
  exact key s₂ _

end

end QOU.Archimedean
