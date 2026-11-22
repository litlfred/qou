import Mathlib.NumberTheory.ZetaValues
import QOU.Infra.Polylogarithm

/-!
# Im Li_3(ζ_n) closed form at every root of unity

Compiled formalisation of
`prop:cyclotomic-trilog-imaginary-closed-form`.
Sibling docstub at
`braids-and-knots/cyclotomic-trilog-imaginary-closed-form.lean`.

The closed form `Im Li_3(ζ_n) = (n - 1)(n - 2) π³ / (3 n³)`
is the substantive Theorem A content; identification with the
analytic polylog value lives in
`QOU.Infra.Polylogarithm.TheoremA`.
-/

namespace QOU.BraidKnot.CyclotomicTrilogImaginary

open QOU.Infra.Polylogarithm

/-! ### `closed_form_holds` — REMOVED 2026-08-21

    It read `∀ n, 2 ≤ n → imLi3ZetaPredicted n = imLi3ZetaPredicted n`,
    closed by `rfl` (vacuity ledger, `proof-no-trivial-true` /
    `reflexive-tautology`, verdict genuine).  A name asserting that a
    closed form *holds* is exactly the claim a reflexive equality cannot
    make: a closed-form statement needs the predicted value on one side
    and the closed form on the other.  That makes it worse than a merely
    empty theorem — a reader grepping for whether the `Im Li₃` closed form
    is established would have found a green `theorem` and stopped.

    It was **dropped rather than restated** because both halves of the
    real content already exist upstream, and duplicating either here would
    add nothing:

    - the verified `n = 4` row is
      `QOU.Infra.Polylogarithm.beta3_from_jonquiere :
      imLi3ZetaPredicted 4 = beta3`, proved from the definitions;
    - the **general-`n`** identification with the analytic
      `Im Li₃(exp(2πi/n)) = Σ sin(2πm/n)/m³` is `imLi3_zeta_hasSum` below
      (proved 2026-11-21 from Mathlib's Bernoulli Fourier series).

    Nothing referenced this declaration. -/

/-- `B₃(x) = x³ − (3/2)x² + (1/2)x`. -/
theorem bernoulli3_eval (x : ℝ) :
    Polynomial.eval x (Polynomial.map (algebraMap ℚ ℝ) (Polynomial.bernoulli 3))
      = x ^ 3 - 3 / 2 * x ^ 2 + 1 / 2 * x := by
  simp [Polynomial.bernoulli, Finset.sum_range_succ, bernoulli, bernoulli'_two, bernoulli'_three, Nat.choose]
  ring

/-- **Theorem A, proved for every `n ≥ 1`.** With `Im Li₃(ζₙ) = Σ_{m ≥ 1} sin(2πm/n)/m³`,

      `Im Li₃(ζₙ) = (n − 1)(n − 2) π³ / (3 n³)`.

    Proof: the Fourier series of the Bernoulli polynomial `B₃` at `x = 1/n`
    (Mathlib `hasSum_one_div_nat_pow_mul_sin`, `k = 1`), with
    `B₃(x) = x³ − (3/2)x² + (1/2)x`. -/
-- Ref: [lewin1981] Polylogarithms and Associated Functions, Ch. 7
theorem imLi3_zeta_hasSum (n : ℕ) (hn : 1 ≤ n) :
    HasSum (fun m : ℕ => 1 / (m : ℝ) ^ 3 * Real.sin (2 * Real.pi * m / n))
      (imLi3ZetaPredicted n) := by
  have hx : (1 / (n : ℝ)) ∈ Set.Icc (0 : ℝ) 1 := by
    have : (1 : ℝ) ≤ n := by exact_mod_cast hn
    constructor
    · positivity
    · rw [div_le_one (by linarith)]; exact this
  have h := hasSum_one_div_nat_pow_mul_sin (k := 1) one_ne_zero hx
  rw [bernoulli3_eval] at h
  have hn0 : (n : ℝ) ≠ 0 := by
    have : (1 : ℝ) ≤ n := by exact_mod_cast hn
    linarith
  convert h using 1
  · funext m
    congr 2
    field_simp
  · unfold imLi3ZetaPredicted
    field_simp
    norm_num [Nat.factorial]
    ring

end QOU.BraidKnot.CyclotomicTrilogImaginary
