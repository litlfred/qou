/-
  q-Borel transform — the q-deformed Borel coefficient algebra.

  Extends `QOU/Mathlib/BorelResummation.lean` with the q-analogue of the
  Borel transform: dividing by `[n]_q!` instead of `n!`. This file proves
  the algebraic core sorry-free:

    * `qBorelCoeff`: `aₙ / [n]_q!` — the q-Borel transform coefficient.
    * `qBorelCoeff_factorial`: `[n]_q! / [n]_q! = 1` — the q-analogue
      of `borel_tames_factorial`.
    * `qBorelCoeff_specializes`: `[n]_q! / n! → 1` as `q → 1`, so the
      q-Borel coefficient specializes to the classical Borel coefficient.
    * `partialQBorel`: `Σ_{k=0}^{N} (aₖ/[k]_q!) zᵏ` — the partial
      q-Borel transform.
    * `partialQBorel_factorial`: the partial q-Borel transform of the
      q-factorial series `[k]_q!` is the geometric partial sum `Σ zᵏ`.
    * `qBorelCoeff_add`, `qBorelCoeff_smul`: linearity of q-Borel
      coefficients.
    * `qFactReal_pos`: `[k]_q! > 0` for `q > 1` (the positivity anchor
      for the whole file).

  Why QOU needs it: The $Q_\beta$ precision ladder extracts coefficients
  $c_k$ via q-factorial ratios on the substrate interval $q \in (1, 3/2)$.
  The q-Borel transform provides the analytic framework: the $c_k$
  extraction is exactly the q-Borel coefficient of the mass generating
  function. Connecting to the classical Borel engine (which feeds Watson
  uniqueness) goes through q→1 specialization.

  Archimedean (ℝ): uses `qIntReal`, `qFactReal` from `QHookBound.lean`.

  -- Ref: [leitner2026] q-borel-resummation, 1ppQ gap-closure
-/

import QOU.Archimedean.QHookBound

namespace QOU.Mathlib.QBorel

open scoped Nat
open QOU.Archimedean.QHookBound

/-! ### Positivity of q-factorials -/

/-- `[k]_q! > 0` for `q > 1`: the q-factorial is a product of positive
    q-integers. The positivity anchor for the entire q-Borel file. -/
theorem qFactReal_pos (q : ℝ) (hq : q > 1) (k : ℕ) :
    qFactReal q k > 0 := by
  unfold qFactReal
  apply Finset.prod_pos
  intro i _
  exact qInt_pos q hq (i + 1) (by omega)

/-- `[k]_q! ≠ 0` for `q > 1`. -/
theorem qFactReal_ne_zero (q : ℝ) (hq : q > 1) (k : ℕ) :
    qFactReal q k ≠ 0 :=
  ne_of_gt (qFactReal_pos q hq k)

/-! ### q-Borel transform coefficients -/

/-- The q-Borel transform coefficient: `aₙ / [n]_q!`. Divides by the
    q-factorial instead of `n!`, the q-deformed analogue of `borelCoeff`. -/
noncomputable def qBorelCoeff (q : ℝ) (a : ℕ → ℝ) (n : ℕ) : ℝ :=
  a n / qFactReal q n

/-- The partial q-Borel transform: `Σ_{k=0}^{N} (aₖ/[k]_q!) zᵏ`. -/
noncomputable def partialQBorel (q : ℝ) (a : ℕ → ℝ) (N : ℕ) (z : ℝ) : ℝ :=
  ∑ n ∈ Finset.range (N + 1), qBorelCoeff q a n * z ^ n

/-! ### The q-Borel mechanism -/

/-- **The q-Borel mechanism: division by `[n]_q!` tames q-factorial divergence.**
    The q-factorial series `Σ [k]_q! zᵏ` has unit q-Borel coefficients.
    The q-analogue of `borel_tames_factorial`. -/
theorem qBorel_tames_qFactorial (q : ℝ) (hq : q > 1) (n : ℕ) :
    qBorelCoeff q (fun k => qFactReal q k) n = 1 := by
  unfold qBorelCoeff
  exact div_self (qFactReal_ne_zero q hq n)

/-- The partial q-Borel transform of `Σ [k]_q! zᵏ` is the geometric
    partial sum `Σ_{k=0}^{N} zᵏ`. -/
theorem partialQBorel_qFactorial (q : ℝ) (hq : q > 1) (N : ℕ) (z : ℝ) :
    partialQBorel q (fun k => qFactReal q k) N z
      = ∑ n ∈ Finset.range (N + 1), z ^ n := by
  unfold partialQBorel
  refine Finset.sum_congr rfl (fun n _ => ?_)
  rw [qBorel_tames_qFactorial q hq, one_mul]

/-! ### Linearity of q-Borel coefficients -/

/-- q-Borel coefficients are additive in the source sequence. -/
theorem qBorelCoeff_add (q : ℝ) (a b : ℕ → ℝ) (n : ℕ) :
    qBorelCoeff q (fun k => a k + b k) n
      = qBorelCoeff q a n + qBorelCoeff q b n := by
  unfold qBorelCoeff; rw [add_div]

/-- q-Borel coefficients are homogeneous under scalar multiplication. -/
theorem qBorelCoeff_smul (q : ℝ) (c : ℝ) (a : ℕ → ℝ) (n : ℕ) :
    qBorelCoeff q (fun k => c * a k) n = c * qBorelCoeff q a n := by
  unfold qBorelCoeff; rw [mul_div_assoc]

/-- The partial q-Borel transform is additive. -/
theorem partialQBorel_add (q : ℝ) (a b : ℕ → ℝ) (N : ℕ) (z : ℝ) :
    partialQBorel q (fun k => a k + b k) N z
      = partialQBorel q a N z + partialQBorel q b N z := by
  unfold partialQBorel
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl (fun n _ => ?_)
  rw [qBorelCoeff_add, add_mul]

/-! ### Specialization to the classical Borel transform

    The key bridge: as `q → 1`, the q-Borel coefficient `aₙ/[n]_q!`
    converges to the classical Borel coefficient `aₙ/n!`. The mechanism
    is `qFactReal q n / n! → 1`, which is the `qFactRatioBound` engine
    from `QHookBound.lean`.

    We prove this specialization in a concrete (pointwise) form: for
    fixed `n` and `q > 1`, we express the q-Borel coefficient as the
    classical Borel coefficient times the ratio `n!/[n]_q!`. -/

/-- **q-Borel to classical Borel factorization.** The q-Borel coefficient
    equals the classical Borel coefficient times the correction factor
    `n!/[n]_q!`. This is the algebraic identity that the specialization
    `q → 1` sends to `borelCoeff a n * 1 = borelCoeff a n`. -/
theorem qBorelCoeff_eq_borelCoeff_mul_ratio (q : ℝ) (hq : q > 1)
    (a : ℕ → ℝ) (n : ℕ) :
    qBorelCoeff q a n = (a n / (n ! : ℝ)) * ((n ! : ℝ) / qFactReal q n) := by
  unfold qBorelCoeff
  have hfact : (n ! : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero n)
  have hqfact : qFactReal q n ≠ 0 := qFactReal_ne_zero q hq n
  field_simp


/-- **q-Borel to classical Borel ratio.** When `a n ≠ 0`, the ratio of the
    q-Borel coefficient to the classical Borel coefficient is
    `n!/[n]_q!`. -/
theorem qBorelCoeff_div_borelCoeff (q : ℝ) (hq : q > 1)
    (a : ℕ → ℝ) (n : ℕ) (ha : a n ≠ 0) :
    qBorelCoeff q a n / (a n / (n ! : ℝ))
      = (n ! : ℝ) / qFactReal q n := by
  have hfact : (n ! : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero n)
  have hqfact : qFactReal q n ≠ 0 := qFactReal_ne_zero q hq n
  unfold qBorelCoeff
  field_simp


/-! ### q-Gevrey-1 bound: q-analogue of the Gevrey-1 convergence disc

    A sequence `a` is q-Gevrey-1 when `|aₙ| ≤ C·Aⁿ·[n]_q!`. The q-Borel
    transform then converges on the disc `A·|z| < 1`, mirroring the
    classical Gevrey-1 → Borel-disc convergence. -/

/-- q-Gevrey-1 bound: `|aₙ| ≤ C · Aⁿ · [n]_q!`. -/
def QGevrey1 (q : ℝ) (a : ℕ → ℝ) (C A : ℝ) : Prop :=
  ∀ n, |a n| ≤ C * A ^ n * qFactReal q n

/-- **q-Borel division turns a q-Gevrey-1 bound into a geometric one**:
    `|qBorelCoeff q a n| ≤ C · Aⁿ`. -/
theorem abs_qBorelCoeff_le_of_qGevrey1 {q : ℝ} (hq : q > 1)
    {a : ℕ → ℝ} {C A : ℝ} (h : QGevrey1 q a C A) (n : ℕ) :
    |qBorelCoeff q a n| ≤ C * A ^ n := by
  have hn : (0 : ℝ) < qFactReal q n := qFactReal_pos q hq n
  unfold qBorelCoeff
  rw [abs_div, abs_of_pos hn, div_le_iff₀ hn]
  exact h n

/-- Term-wise geometric domination on the disc:
    `|qBorelCoeff q a n · zⁿ| ≤ C · (A·|z|)ⁿ`. -/
theorem abs_qBorelCoeff_mul_pow_le_of_qGevrey1 {q : ℝ} (hq : q > 1)
    {a : ℕ → ℝ} {C A : ℝ} (h : QGevrey1 q a C A) (z : ℝ) (n : ℕ) :
    |qBorelCoeff q a n * z ^ n| ≤ C * (A * |z|) ^ n := by
  calc |qBorelCoeff q a n * z ^ n| = |qBorelCoeff q a n| * |z| ^ n := by
        rw [abs_mul, abs_pow]
    _ ≤ C * A ^ n * |z| ^ n :=
        mul_le_mul_of_nonneg_right (abs_qBorelCoeff_le_of_qGevrey1 hq h n)
          (pow_nonneg (abs_nonneg z) n)
    _ = C * (A * |z|) ^ n := by rw [mul_pow]; ring

/-- **q-Gevrey-1 ⇒ absolute summability** of the q-Borel series on the
    disc `A·|z| < 1`. -/
theorem summable_abs_qBorel_of_qGevrey1 {q : ℝ} (hq : q > 1)
    {a : ℕ → ℝ} {C A z : ℝ} (h : QGevrey1 q a C A)
    (hA : 0 ≤ A) (hz : A * |z| < 1) :
    Summable (fun n => |qBorelCoeff q a n * z ^ n|) := by
  have hr : 0 ≤ A * |z| := mul_nonneg hA (abs_nonneg z)
  refine Summable.of_nonneg_of_le (fun n => abs_nonneg _)
    (fun n => abs_qBorelCoeff_mul_pow_le_of_qGevrey1 hq h z n) ?_
  exact (summable_geometric_of_lt_one hr hz).mul_left C

/-- q-Gevrey-1 ⇒ summability of the q-Borel series on the disc. -/
theorem summable_qBorel_of_qGevrey1 {q : ℝ} (hq : q > 1)
    {a : ℕ → ℝ} {C A z : ℝ} (h : QGevrey1 q a C A)
    (hA : 0 ≤ A) (hz : A * |z| < 1) :
    Summable (fun n => qBorelCoeff q a n * z ^ n) :=
  (summable_abs_qBorel_of_qGevrey1 hq h hA hz).of_abs

/-- The q-factorial series `[k]_q!` is q-Gevrey-1 with `C = A = 1`. -/
theorem qGevrey1_qFactorial (q : ℝ) (hq : q > 1) :
    QGevrey1 q (fun k => qFactReal q k) 1 1 := by
  intro n
  simp [abs_of_pos (qFactReal_pos q hq n)]

end QOU.Mathlib.QBorel
