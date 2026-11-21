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

/-- `0 < I(n)` — the involution numbers are positive (needed as the `Ik > 0`
input to the C8 super-exponential bound). -/
theorem involutionNumber_pos : ∀ n, 0 < involutionNumber n := by
  intro n
  induction n using Nat.twoStepInduction with
  | zero => decide
  | one => decide
  | more n ih1 ih2 =>
    have hstep : involutionNumber (n + 2)
        = involutionNumber (n + 1) + (n + 1) * involutionNumber n := rfl
    omega

/-- **The C8 lower bound is genuinely super-exponential (concrete form).** Plugging the
Gevrey-1/2 involution bound `I(k)² ≤ 2^k·k!` into the abstract
`c8_superexp_sq_lower_bound` gives, for the Plancherel-weighted branched sum
`w_std = (Σ f² g)/k!` with the SYT inputs (A) `Σ f g = k!/3` and (C) `Σ g ≤ I(k)`:

  `w_std² ≥ k! / (81 · 2^k)`,

a genuinely **super-exponential** lower bound (`k!/2^k → ∞`), strengthening the bare
`w_std ≥ 1/9` that `I(k) ≤ k!` alone yields. The SYT inputs (A)/(C) remain the open
combinatorial core (they are hypotheses here, not discharged); this only sharpens the
*downstream bound* they feed — honestly, no fabrication of the branched identities. -/
theorem wstd_superexp_sq {ι : Type*} (s : Finset ι) (f g : ι → ℝ) (k : ℕ)
    (hg : ∀ i ∈ s, 0 ≤ g i)
    (hA : ∑ i ∈ s, f i * g i = (k.factorial : ℝ) / 3)
    (hC : ∑ i ∈ s, g i ≤ (involutionNumber k : ℝ)) :
    (k.factorial : ℝ) / (81 * 2 ^ k)
      ≤ ((∑ i ∈ s, f i ^ 2 * g i) / (k.factorial : ℝ)) ^ 2 := by
  have hkfac : 0 < (k.factorial : ℝ) := by exact_mod_cast k.factorial_pos
  have hIkpos : 0 < (involutionNumber k : ℝ) := by exact_mod_cast involutionNumber_pos k
  have hIsq : (involutionNumber k : ℝ) ^ 2 ≤ 2 ^ k * (k.factorial : ℝ) := by
    exact_mod_cast involution_sq_le_two_pow_mul_factorial k
  exact c8_superexp_sq_lower_bound s f g (k.factorial : ℝ) (involutionNumber k : ℝ) k
    hg hkfac hIkpos hA hC hIsq

/-- **Strict positivity of the Gevrey-1/2 scaled square `4^n * I(n)^2` (`b9ms`).**
For every `n : ℕ`, `1 ≤ 4 ^ n * involutionNumber n ^ 2`, witnessed directly by
combining `n.factorial_pos` with the lower Gevrey-1/2 sandwich `n! ≤ 4^n * I(n)^2`. -/
theorem one_le_four_pow_mul_involution_sq (n : ℕ) :
    1 ≤ 4 ^ n * involutionNumber n ^ 2 := by
  have h1 : 1 ≤ n.factorial := Nat.succ_le_of_lt n.factorial_pos
  exact le_trans h1 (factorial_le_four_pow_mul_involution_sq n)

end QOU.Mass.BindingGevreyHalf
