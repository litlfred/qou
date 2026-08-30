/-
# QOU.MassTheory.DeficitRecursionReduction — the algebraic heart of the ∀A Milnor recursion (qou-v7ro)

The ∀A proof of the deficit recursion `D_{A+1} = −h²(h²+2)·D_A` (audit
`docs/audits/2026-08-30-milnor-recursion-forall-A-PROVED.md`) has two kinds of ingredient:

1. **Temperley–Lieb facts** about the Markov trace of the Brunnian word — identity **(I)**
   `G_n = [2]^n(1+h²) − h²·Q_n` (three of four qtr-terms A-independent) and the **2-term
   Q-recursion** `Q_n = [2]^n(1+u h²) − u h²[2]·Q_{n-1}` (`u = h²+2`), obtained by the
   cap-cup / Markov / cyclicity reduction. These live on the TL operator algebra and are proved
   in the accompanying probe (`milnor_recursion_forall_A_proof_probe.py`), not yet in Lean.

2. **Pure field algebra** turning (I) + the Q-recursion into the deficit recursion. That step is
   what this file formalizes — sorry-free, over a generic field.

Isolating (2) in Lean makes the remaining Lean obligation **precise and minimal**: to discharge
the `BrunnianDeficitRecursion` instance for real, one needs only to formalize the two TL facts
(I) and the Q-recursion for the concrete Markov-trace `G`, `Q`; the passage to the deficit
recursion is then this `theorem`, already checked.

`G`, `Q : ℕ → K` are abstract "trace" and "fourth-term" sequences; `b` plays the role of `[2]`
(the loop value), `h = q − 1/q`. `deficit b G k = 1 − G k / b^k`. No archimedean structure is used,
so everything is over a generic `[Field K]` (§7c base-ring convention).
-/
import Mathlib.Tactic

namespace QOU.MassTheory.DeficitRecursionReduction

/-- The normalized trace deficit `D_k = 1 − G_k / b^k` (here `b = [2]`, `G_k = qtr(ρ(w_k))`). -/
noncomputable def deficit {K : Type*} [Field K] (b : K) (G : ℕ → K) (k : ℕ) : K :=
  1 - G k / b ^ k

/-- **The algebraic reduction (sorry-free).** From the Temperley–Lieb identity **(I)**
`G_k = b^k(1+h²) − h²·Q_k` (at `n` and `n+1`) and the **2-term Q-recursion**
`Q_{n+1} = b^{n+1}(1 + (h²+2)h²) − (h²+2)h²·b·Q_n`, the deficit obeys
`D_{n+1} = −h²(h²+2)·D_n`. This is the field-algebra core of the ∀A Milnor deficit recursion;
the two hypotheses are exactly the TL facts the accompanying probe establishes. -/
theorem deficit_recursion_of_reduction {K : Type*} [Field K]
    (b h : K) (hb : b ≠ 0) (G Q : ℕ → K) (n : ℕ)
    (hIn  : G n       = b ^ n       * (1 + h ^ 2) - h ^ 2 * Q n)
    (hIn1 : G (n + 1) = b ^ (n + 1) * (1 + h ^ 2) - h ^ 2 * Q (n + 1))
    (hQ   : Q (n + 1) = b ^ (n + 1) * (1 + (h ^ 2 + 2) * h ^ 2)
                          - (h ^ 2 + 2) * h ^ 2 * b * Q n) :
    deficit b G (n + 1) = -h ^ 2 * (h ^ 2 + 2) * deficit b G n := by
  have hbn : b ^ n ≠ 0 := pow_ne_zero n hb
  simp only [deficit, hIn1, hIn, hQ, pow_succ]
  field_simp
  ring

/-- Corollary: the "trace" sequence `G` itself satisfies the same 2-term recursion as `Q`,
`G_{n+1} = b^{n+1}(1 + u h²) − u h²·b·G_n` (`u = h²+2`) — a clean by-product of (I) + the
Q-recursion, recorded because it is the form the deficit recursion is read off from. -/
theorem trace_recursion_of_reduction {K : Type*} [Field K]
    (b h : K) (G Q : ℕ → K) (n : ℕ)
    (hIn  : G n       = b ^ n       * (1 + h ^ 2) - h ^ 2 * Q n)
    (hIn1 : G (n + 1) = b ^ (n + 1) * (1 + h ^ 2) - h ^ 2 * Q (n + 1))
    (hQ   : Q (n + 1) = b ^ (n + 1) * (1 + (h ^ 2 + 2) * h ^ 2)
                          - (h ^ 2 + 2) * h ^ 2 * b * Q n) :
    G (n + 1) = b ^ (n + 1) * (1 + (h ^ 2 + 2) * h ^ 2)
                  - (h ^ 2 + 2) * h ^ 2 * b * G n := by
  rw [hIn1, hQ, hIn, pow_succ]
  ring

end QOU.MassTheory.DeficitRecursionReduction
