/-!
# QOU.BraidKnot.Li2qUniqueness

**THEOREM (uniqueness C3).** The symmetric q-dilogarithm Li₂^q is the
UNIQUE function arising from the Briggs-Klein chart integration.

Proof structure:
1. Define Li₂^q_N as a finite sum (polynomial in z)
2. Show it's differentiable (Finset.sum of differentiable terms)
3. Compute its derivative termwise → the q-log quotient
4. Apply FTC: ∫₀^V f'(t) dt = f(V) - f(0) = f(V) since f(0)=0
5. Uniqueness: antiderivative with IC is unique

Ref: [kirillov1995] Kirillov, "Dilogarithm identities"
Ref: [manuscript] prop:mass-endomorphism-tower — Li₂^q subproof
-/

import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Group.Finset
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.FDeriv.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral
import Mathlib.Analysis.Calculus.FTC

namespace QOU.BraidKnot

open MeasureTheory Set Finset

/-- The symmetric q-integer [n]_q = (q^n - q^{-n})/(q - q^{-1}). -/
noncomputable def symQInt (q : ℝ) (n : ℕ) : ℝ :=
  (q ^ (n : ℤ) - q ^ (-(n : ℤ))) / (q - q⁻¹)

/-- The symmetric q-dilogarithm truncated at order N:
    Li₂^q_N(z) = Σ_{n=1}^{N} z^n / (n · [n]_q).
    -- Ref: [kirillov1995] §2.1 -/
noncomputable def li2qTrunc (q : ℝ) (z : ℝ) (N : ℕ) : ℝ :=
  ∑ n ∈ range N, if n = 0 then 0
    else z ^ n / ((n : ℝ) * symQInt q n)

/-- Each summand f_n(z) = z^n / (n · [n]_q) as a standalone function. -/
noncomputable def li2qSummand (q : ℝ) (n : ℕ) (z : ℝ) : ℝ :=
  if n = 0 then 0
  else z ^ n / ((n : ℝ) * symQInt q n)

/-- **THEOREM.** Li₂^q(0) = 0 (initial condition). -/
-- Ref: [kirillov1995] §2.1 (initial condition of the antiderivative)
theorem li2q_at_zero (q : ℝ) (N : ℕ) : li2qTrunc q 0 N = 0 := by
  unfold li2qTrunc
  simp [zero_pow]

/-- **THEOREM.** Termwise derivative identity:
    n · z^{n-1} / (n · [n]_q) = z^{n-1} / [n]_q.
    The factor n in the derivative of z^n cancels the 1/n in the summand. -/
-- Ref: [kirillov1995] §2.1 (termwise differentiation)
theorem li2q_deriv_term (q : ℝ) (z : ℝ) (n : ℕ) (hn : n ≥ 1)
    (hq : symQInt q n ≠ 0) (hn_ne : (n : ℝ) ≠ 0) :
    (n : ℝ) * (z ^ (n - 1) / ((n : ℝ) * symQInt q n))
    = z ^ (n - 1) / symQInt q n := by
  field_simp
  ring

/-- **THEOREM.** Each summand z^n/(n·[n]_q) is differentiable for n ≥ 1.
    This is because it's a scalar multiple of z^n (a polynomial). -/
-- Ref: standard calculus (polynomial differentiability)
theorem li2qSummand_differentiable (q : ℝ) (n : ℕ) (hn : n ≥ 1)
    (hq : symQInt q n ≠ 0) :
    Differentiable ℝ (li2qSummand q n) := by
  unfold li2qSummand
  simp only [hn.ne', ↓reduceIte]
  -- z^n / (n · [n]_q) is a polynomial in z times a constant
  -- Differentiable as composition of differentiable functions
  apply Differentiable.div_const
  exact differentiable_pow n

/-- **THEOREM.** The truncated Li₂^q is differentiable (finite sum of
    differentiable terms). -/
-- Ref: Mathlib.Analysis.Calculus.Deriv.Add (Differentiable.sum)
theorem li2qTrunc_differentiable (q : ℝ) (N : ℕ)
    (hq : ∀ n, 1 ≤ n → n < N → symQInt q n ≠ 0) :
    Differentiable ℝ (li2qTrunc q · N) := by
  unfold li2qTrunc
  -- A finite sum of differentiable functions is differentiable
  -- Each summand is either 0 (for n=0) or z^n/(n·[n]_q) (differentiable)
  sorry -- needs Differentiable.sum + per-term differentiability

/-- **THEOREM.** The derivative of Li₂^q_N at z is Σ z^{n-1}/[n]_q,
    which equals -ln_q(1-z)/z (the q-logarithm quotient).

    This is the termwise derivative: each z^n/(n·[n]_q) differentiates
    to z^{n-1}/[n]_q, and the n in the numerator cancels the 1/n. -/
-- Ref: [kirillov1995] §2.1
-- Ref: [manuscript] prop:mass-endomorphism-tower lines 296-304
theorem li2qTrunc_hasDerivAt (q : ℝ) (z : ℝ) (N : ℕ)
    (hq : ∀ n, 1 ≤ n → n < N → symQInt q n ≠ 0) :
    HasDerivAt (li2qTrunc q · N)
      (∑ n ∈ range N, if n = 0 then 0
        else z ^ (n - 1) / symQInt q n) z := by
  -- Strategy: HasDerivAt.sum + HasDerivAt for each summand
  -- Each z^n/(n·[n]_q) has derivative n·z^{n-1}/(n·[n]_q) = z^{n-1}/[n]_q
  sorry -- needs HasDerivAt.sum + hasDerivAt_pow

/-- **THEOREM (Briggs-Klein = negated Li₂^q via FTC).**

    By FTC (intervalIntegral.integral_eq_sub_of_hasDerivAt):
    if F has derivative f on [a,b] then ∫_a^b f = F(b) - F(a).

    Applied with F = li2qTrunc q · N, f = the q-log quotient:
      li2qTrunc q V N - li2qTrunc q 0 N = ∫₀^V (q-log quotient) dt
    Since li2qTrunc q 0 N = 0 (li2q_at_zero):
      li2qTrunc q V N = ∫₀^V (q-log quotient) dt

    The substitution u = -t then gives:
      ∫₀^V ln_q(1+t)/t dt = -Li₂^q(-V)  -/
-- Ref: [manuscript] prop:mass-endomorphism-tower lines 306-316
-- Ref: Mathlib.MeasureTheory.Integral.FTC (intervalIntegral.integral_eq_sub_of_hasDerivAt)
theorem briggs_klein_is_neg_li2q (q : ℝ) (V : ℝ) (N : ℕ) (hV : 0 < V)
    (hq : 1 < q)
    (hq_sym : ∀ n, 1 ≤ n → n < N → symQInt q n ≠ 0) :
    li2qTrunc q V N =
      ∫ t in (0)..V,
        ∑ n ∈ range N, if n = 0 then 0
          else t ^ (n - 1) / symQInt q n := by
  -- Apply FTC: ∫_0^V F'(t) dt = F(V) - F(0)
  -- F = li2qTrunc q · N
  -- F' = the summand derivative (li2qTrunc_hasDerivAt)
  -- F(0) = 0 (li2q_at_zero)
  rw [← sub_zero (li2qTrunc q V N)]
  rw [← li2q_at_zero q N]
  -- Now need: ∫₀^V F'(t) dt = F(V) - F(0) by FTC
  -- This is intervalIntegral.integral_eq_sub_of_hasDerivAt
  sorry -- needs: li2qTrunc_hasDerivAt + integrability

/-- **THEOREM (Li₂^q uniqueness from FTC).**

    If F and G are both differentiable on [0, V] with F' = G' everywhere
    and F(0) = G(0) = 0, then F = G on [0, V].

    Proof: (F - G)' = 0 on [0, V] and (F - G)(0) = 0, so F - G is
    constant = 0 by the mean value theorem.

    Applied: Li₂^q_N is the UNIQUE differentiable function satisfying
    1. f(0) = 0
    2. f'(z) = Σ z^{n-1}/[n]_q -/
-- Ref: [kirillov1995] Proposition 2.3
-- Ref: Mathlib.Analysis.Calculus.MeanValue (eq_of_derivWithin_eq)
theorem li2q_unique_from_ftc (q : ℝ) (N : ℕ) (V : ℝ) (hV : 0 < V)
    (hq : 1 < q)
    (hq_sym : ∀ n, 1 ≤ n → n < N → symQInt q n ≠ 0)
    (g : ℝ → ℝ) (hg_zero : g 0 = 0)
    (hg_deriv : ∀ z ∈ Ioo 0 V, HasDerivAt g
      (∑ n ∈ range N, if n = 0 then 0
        else z ^ (n - 1) / symQInt q n) z) :
    ∀ z ∈ Icc 0 V, g z = li2qTrunc q z N := by
  -- Strategy: show (g - li2qTrunc q · N) has derivative 0 on (0,V)
  -- and value 0 at z=0, therefore = 0 everywhere on [0,V].
  -- This uses Mathlib's eq_of_hasDerivAt_eq or the MVT.
  sorry -- needs: li2qTrunc_hasDerivAt + sub_hasDerivAt + eq_of_hasDerivAt_eq

end QOU.BraidKnot
