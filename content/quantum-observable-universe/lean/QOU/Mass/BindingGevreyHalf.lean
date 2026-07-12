import Mathlib.Tactic
import QOU.BraidKnot.KeystoneC8SuperExpBound

/-!
# The binding period is Gevrey-1/2: the integer sandwich `n! ≤ 4ⁿ·I(n)² ≤ 8ⁿ·n!`

The lever-1 binding period is `a_D^(n) = S(n)/n` with `S(n) = Σ_{λ⊢n} dim_q(λ)`;
at the classical limit `q = 1` this is `I(n)/n` where `I(n)` is the
involution/telephone number (`Σ_λ f^λ = I(n)`, OEIS A000085, concrete recurrence
`involutionNumber` in `KeystoneC8SuperExpBound`).

An external resurgence framing (2026-07-12 session dialog) claimed the period grows
**factorially** (Gevrey-1, `a_D^(n) ∝ (1/2)_n/Rⁿ`), so that the standard level-1
Borel transform would carry its alien derivatives. The corpus rate-refine probe
(`lever1_sw_period_lw_rate_refine.py`) already measured that this rate overshoots.
This file pins the growth **class** with two elementary integer inequalities, proved
by two-step induction from the telephone recurrence:

* `involution_sq_le_two_pow_mul_factorial` : `I(n)² ≤ 2ⁿ·n!`
* `factorial_le_four_pow_mul_involution_sq` : `n! ≤ 4ⁿ·I(n)²`

Together: `√(n!/4ⁿ) ≤ I(n) ≤ √(2ⁿ·n!)` — the period is `(n!)^{1/2}` times an
exponentially bounded factor, i.e. **Gevrey-1/2, not Gevrey-1**. Consequently the
level-1 Borel transform of `Σ a_D^(n) xⁿ` is entire (no finite singularities — no
alien derivatives live in that plane) and the canonical plane is the level-1/2
Borel (Écalle acceleration). Numerical companion:
`computations/lever1_gevrey_order_pin.py` (asserts both inequalities to `n = 60`
and measures the level-1/2 structure; at the substrate `q₀` the class deforms
further, toward q-Gevrey).

Base ring: `ℕ` (pure combinatorial integers; no archimedean content — §7c wall-safe).
-/

namespace QOU.Mass.BindingGevreyHalf

open QOU.BraidKnot.KeystoneC8SuperExpBound

/-- **Upper half of the Gevrey-1/2 sandwich:** `I(n)² ≤ 2ⁿ·n!`.

Two-step induction from `I(n+2) = I(n+1) + (n+1)·I(n)` via
`(a+b)² ≤ 2a² + 2b²`; the induction margin is `n+3 ≤ 2(n+2)`.
This bounds the binding period strictly below every Gevrey-1 (factorial) class:
`I(n) ≤ √(2ⁿ n!) = o(n!·rⁿ)` for every `r > 0`. -/
theorem involution_sq_le_two_pow_mul_factorial :
    ∀ n, involutionNumber n ^ 2 ≤ 2 ^ n * n.factorial := by
  intro n
  induction n using Nat.twoStepInduction with
  | zero => decide
  | one => decide
  | more n ih1 ih2 =>
    have hstep : involutionNumber (n + 2)
        = involutionNumber (n + 1) + (n + 1) * involutionNumber n := rfl
    have e1 : (n + 2).factorial = (n + 2) * (n + 1).factorial := Nat.factorial_succ _
    have e2 : (n + 1).factorial = (n + 1) * n.factorial := Nat.factorial_succ _
    set a := involutionNumber (n + 1) with ha
    set b := involutionNumber n with hb
    have key : (a + (n + 1) * b) ^ 2 ≤ 2 * a ^ 2 + 2 * ((n + 1) * b) ^ 2 := by
      zify
      nlinarith [sq_nonneg ((a : ℤ) - (n + 1) * b)]
    calc involutionNumber (n + 2) ^ 2
        = (a + (n + 1) * b) ^ 2 := by rw [hstep]
      _ ≤ 2 * a ^ 2 + 2 * ((n + 1) * b) ^ 2 := key
      _ = 2 * a ^ 2 + 2 * (n + 1) ^ 2 * b ^ 2 := by ring
      _ ≤ 2 * (2 ^ (n + 1) * (n + 1).factorial) + 2 * (n + 1) ^ 2 * (2 ^ n * n.factorial) :=
          Nat.add_le_add (Nat.mul_le_mul_left _ ih2) (Nat.mul_le_mul_left _ ih1)
      _ = 2 ^ (n + 2) * (n + 1).factorial + 2 ^ (n + 1) * (n + 1) * ((n + 1) * n.factorial) := by
          ring
      _ = 2 ^ (n + 2) * (n + 1).factorial + 2 ^ (n + 1) * (n + 1) * (n + 1).factorial := by
          rw [e2]
      _ = 2 ^ (n + 1) * (n + 1).factorial * (n + 3) := by ring
      _ ≤ 2 ^ (n + 1) * (n + 1).factorial * (2 * (n + 2)) := by
          exact Nat.mul_le_mul_left _ (by omega)
      _ = 2 ^ (n + 2) * ((n + 2) * (n + 1).factorial) := by ring
      _ = 2 ^ (n + 2) * (n + 2).factorial := by rw [← e1]

/-- **Lower half of the Gevrey-1/2 sandwich:** `n! ≤ 4ⁿ·I(n)²`.

Two-step induction using only `I(n+2) ≥ (n+1)·I(n)` (drop the `I(n+1)` term of the
telephone recurrence); the induction margin is `(n+2)(n+1) ≤ 16(n+1)²`.
This grounds the super-exponential (order exactly 1/2) growth of the period from
below: `I(n) ≥ √(n!/4ⁿ)`, so `a_D^(n)` genuinely leaves every exponential class. -/
theorem factorial_le_four_pow_mul_involution_sq :
    ∀ n, n.factorial ≤ 4 ^ n * involutionNumber n ^ 2 := by
  intro n
  induction n using Nat.twoStepInduction with
  | zero => decide
  | one => decide
  | more n ih1 _ih2 =>
    have hstep : involutionNumber (n + 2)
        = involutionNumber (n + 1) + (n + 1) * involutionNumber n := rfl
    have hge : (n + 1) * involutionNumber n ≤ involutionNumber (n + 2) := by
      rw [hstep]; omega
    have hsq : ((n + 1) * involutionNumber n) ^ 2 ≤ involutionNumber (n + 2) ^ 2 :=
      Nat.pow_le_pow_left hge 2
    have e1 : (n + 2).factorial = (n + 2) * (n + 1).factorial := Nat.factorial_succ _
    have e2 : (n + 1).factorial = (n + 1) * n.factorial := Nat.factorial_succ _
    have hquad : (n + 2) * (n + 1) ≤ 16 * (n + 1) ^ 2 := by nlinarith
    calc (n + 2).factorial
        = (n + 2) * ((n + 1) * n.factorial) := by rw [e1, e2]
      _ ≤ (n + 2) * ((n + 1) * (4 ^ n * involutionNumber n ^ 2)) :=
          Nat.mul_le_mul_left _ (Nat.mul_le_mul_left _ ih1)
      _ = (n + 2) * (n + 1) * (4 ^ n * involutionNumber n ^ 2) := by ring
      _ ≤ 16 * (n + 1) ^ 2 * (4 ^ n * involutionNumber n ^ 2) :=
          Nat.mul_le_mul_right _ hquad
      _ = 4 ^ (n + 2) * ((n + 1) * involutionNumber n) ^ 2 := by ring
      _ ≤ 4 ^ (n + 2) * involutionNumber (n + 2) ^ 2 := Nat.mul_le_mul_left _ hsq

/-- The two-sided **Gevrey-1/2 sandwich** in one statement:
`n! ≤ 4ⁿ·I(n)²` and `I(n)² ≤ 2ⁿ·n!`, i.e. `I(n) = (n!)^{1/2}·(exp-bounded)`.
The binding period's classical growth order is exactly 1/2 — the level-1 Borel
plane is singularity-free for it, and the level-1/2 plane is canonical. -/
theorem gevrey_half_sandwich (n : ℕ) :
    n.factorial ≤ 4 ^ n * involutionNumber n ^ 2 ∧
      involutionNumber n ^ 2 ≤ 2 ^ n * n.factorial :=
  ⟨factorial_le_four_pow_mul_involution_sq n, involution_sq_le_two_pow_mul_factorial n⟩

end QOU.Mass.BindingGevreyHalf
