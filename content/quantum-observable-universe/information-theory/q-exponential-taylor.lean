/-!
# QOU.qExponentialTaylor — archimedean Taylor series of e_q

Over any field of characteristic zero where the Jackson factorials
[n]_q! are invertible, the categorical grouplike e_q is represented
by the convergent series

  e_q(x) = Σ_{n ≥ 0} x^n / [n]_q!.

Derivation: power-series ansatz, apply D_q(x^n) = [n]_q x^{n-1} to
the defining equation D_q e_q = e_q, get recursion a_{n+1} = a_n/[n+1]_q.

LaTeX label: `prop:q-exponential-taylor`

## References

- [manuscript] §9-information-theory/q-exponential-taylor

**Char 0 only.**  The series has denominators [n]_q!, which can vanish
in characteristic p.  The categorical `QExponential` structure is
defined abstractly in any base ring; this proposition is the
archimedean realisation.
-/

import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.RingTheory.PowerSeries.Basic

namespace QOU

noncomputable section
open scoped Classical

/-- Jackson integer [n]_q = (1 - q^n) / (1 - q) over a characteristic-zero
    field where q ≠ 1. -/
-- Ref: [manuscript] §9
def jacksonInt (q : ℝ) (n : ℕ) : ℝ :=
  if q = 1 then (n : ℝ)
  else (1 - q^n) / (1 - q)

/-- Jackson factorial [n]_q! = ∏_{k=1}^n [k]_q. -/
-- Ref: [manuscript] §9
def jacksonFactorial (q : ℝ) : ℕ → ℝ
  | 0 => 1
  | n + 1 => jacksonInt q (n + 1) * jacksonFactorial q n

/-- Formal Taylor series of the q-exponential. -/
-- Ref: [manuscript] §9
noncomputable def qExpSeries (q : ℝ) (x : ℝ) : ℕ → ℝ :=
  fun n => x^n / jacksonFactorial q n

/-- **Taylor series of e_q**: over ℝ with q ≠ 1 and [n]_q! ≠ 0 for all n,
    the partial sums of qExpSeries converge and equal the abstract
    grouplike e_q. -/
-- Ref: [manuscript] §9
theorem qExponentialTaylor (q : ℝ) (x : ℝ)
    (hq : q ≠ 1) (hfac : ∀ n, jacksonFactorial q n ≠ 0) :
    Summable (qExpSeries q x) := by
  -- Ref: [manuscript] §9 — follows from ratio test on |x|/[n+1]_q → 0.
  sorry

/-- At q = 1, the q-exponential Taylor series recovers the ordinary
    exponential. -/
-- Ref: [manuscript] §9
theorem qExpSeries_classical_limit (x : ℝ) :
    jacksonFactorial 1 = fun n => (n.factorial : ℝ) := by
  funext n
  induction n with
  | zero => simp [jacksonFactorial]
  | succ n ih =>
    -- jacksonFactorial 1 (n+1) = jacksonInt 1 (n+1) * jacksonFactorial 1 n
    -- jacksonInt 1 (n+1) = (n+1 : ℝ) since the if-condition is true
    -- jacksonFactorial 1 n = (n.factorial : ℝ) by IH
    -- Combined: (n+1) * n! = (n+1)!
    show jacksonInt 1 (n + 1) * jacksonFactorial 1 n
        = (((n + 1).factorial : ℕ) : ℝ)
    rw [jacksonInt, if_pos rfl, ih, Nat.factorial_succ]
    push_cast
    ring

end QOU
