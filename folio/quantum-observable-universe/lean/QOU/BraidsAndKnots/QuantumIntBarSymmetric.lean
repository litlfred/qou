import QOU.StandardModel.ThetaQcdFramingCp

/-!
# Symmetric q-integers are bar-symmetric, for every `n`

Bean `qou-cds1`, tranche S1.  The load-bearing half of the S1 finding that the
bar-parity condition cannot select a Habiro generator.

The empirical observation (PR #6282) was that the parity filter admits `[2]_q`,
`[3]_q`, `[4]_q`, `[5]_q` — every symmetric q-integer tested.  The reason
(`computations/qbeta/qbeta_bar_fixed_field_is_q_of_two_probe.py`, 19/19) is that
`Fix(bar) = ℚ(s)` with `s = q + q⁻¹ = [2]_q`, and every `[n]_q` is the Chebyshev
polynomial `U_{n-1}(s)`, hence lies in that fixed field.

This file proves the consequence directly and for **all** `n`, without needing
the Chebyshev identity or any field theory: the numerator and denominator of
`[n]_q` are each bar-**anti**-symmetric, and their quotient is therefore
bar-symmetric.  The two minus signs cancel.

**What this is for.**  A gate that admits an entire infinite family cannot select
one member of it.  This theorem is that statement made permanent for the
q-integer family: no candidate generator built from symmetric q-integers can ever
be distinguished from another by bar-parity.  It is a *negative* result about the
gate, not a claim about which generator is correct.

**Base ring (§7c).**  Generic `{R : Type*} [Field R]` — `Field` only because
`[n]_q` needs `q⁻¹`.  No ordering, no `Real.sqrt`, no archimedean construct, no
numerical `q₀`.  Pre-archimedean throughout.

The `BarInvolution` class and `IsCPEven` are reused from
`QOU.StandardModel.ThetaQcdFramingCp`, which declares them in-library precisely
so downstream files need not depend on the content-block sibling
(`braids-and-knots/bar-involution.lean`) being compiled.  That sibling carries a
richer algebra but sits outside the `QOU` Lake glob and is imported by nothing.
-/

namespace QOU.BraidKnot.QuantumIntBarSymmetric

open QOU.StandardModel.ThetaQCDFraming

variable {R : Type*}

section Ring
variable [CommRing R] [BarInvolution R]

/-- `bar 0 = 0`, from additivity alone. -/
theorem bar_zero' : BarInvolution.bar (0 : R) = 0 := by
  have h : BarInvolution.bar (0 : R)
      = BarInvolution.bar (0 : R) + BarInvolution.bar (0 : R) := by
    conv_lhs => rw [show (0 : R) = 0 + 0 by rw [add_zero]]
    rw [BarInvolution.bar_add]
  linear_combination -h

/-- `bar` is additive-inverse preserving. -/
theorem bar_neg' (x : R) : BarInvolution.bar (-x) = -BarInvolution.bar x := by
  have h : BarInvolution.bar x + BarInvolution.bar (-x) = 0 := by
    rw [← BarInvolution.bar_add, add_neg_cancel, bar_zero']
  linear_combination h

/-- `bar` commutes with subtraction. -/
theorem bar_sub' (x y : R) :
    BarInvolution.bar (x - y) = BarInvolution.bar x - BarInvolution.bar y := by
  rw [sub_eq_add_neg, BarInvolution.bar_add, bar_neg', ← sub_eq_add_neg]

end Ring

section Field
variable [Field R] [BarInvolution R]

/-- `bar` commutes with inversion on nonzero elements: from `bar_mul` and
    `bar_one`, `bar x * bar x⁻¹ = 1`. -/
theorem bar_inv' {x : R} (hx : x ≠ 0) :
    BarInvolution.bar x⁻¹ = (BarInvolution.bar x)⁻¹ := by
  have h : BarInvolution.bar x * BarInvolution.bar x⁻¹ = 1 := by
    rw [← BarInvolution.bar_mul, mul_inv_cancel₀ hx, BarInvolution.bar_one]
  have hbx : BarInvolution.bar x ≠ 0 := by
    intro hz
    rw [hz, zero_mul] at h
    exact zero_ne_one h
  calc BarInvolution.bar x⁻¹
      = (BarInvolution.bar x)⁻¹ * (BarInvolution.bar x * BarInvolution.bar x⁻¹) := by
        rw [← mul_assoc, inv_mul_cancel₀ hbx, one_mul]
    _ = (BarInvolution.bar x)⁻¹ := by rw [h, mul_one]

/-- The bar action on the substrate parameter is an involution on `q`:
    `bar q = q⁻¹` forces `bar q⁻¹ = q`. -/
theorem bar_inv_eq {q : R} (hbarq : BarInvolution.bar q = q⁻¹) :
    BarInvolution.bar q⁻¹ = q := by
  have := BarInvolution.bar_involutive q
  rwa [hbarq] at this

/-- The **symmetric** q-integer `[n]_q = (qⁿ - q⁻ⁿ)/(q - q⁻¹)`. -/
noncomputable def quantumInt (n : ℕ) (q : R) : R :=
  (q ^ n - (q ^ n)⁻¹) / (q - q⁻¹)

/-- The numerator `qⁿ - q⁻ⁿ` is bar-**anti**-symmetric, for every `n`. -/
theorem numerator_bar_antisymmetric {q : R}
    (hbarq : BarInvolution.bar q = q⁻¹) (n : ℕ) :
    BarInvolution.bar (q ^ n - (q ^ n)⁻¹) = -(q ^ n - (q ^ n)⁻¹) := by
  have hpow : BarInvolution.bar (q ^ n) = (q ^ n)⁻¹ := bar_qpow hbarq n
  have hinv : BarInvolution.bar ((q ^ n)⁻¹) = q ^ n := by
    have := BarInvolution.bar_involutive (q ^ n)
    rwa [hpow] at this
  rw [bar_sub', hpow, hinv, neg_sub]

/-- The denominator `q - q⁻¹` is bar-**anti**-symmetric. -/
theorem denominator_bar_antisymmetric {q : R}
    (hbarq : BarInvolution.bar q = q⁻¹) :
    BarInvolution.bar (q - q⁻¹) = -(q - q⁻¹) := by
  rw [bar_sub', hbarq, bar_inv_eq hbarq, neg_sub]

/-- **Every symmetric q-integer is bar-symmetric.**

    Both numerator and denominator are bar-anti-symmetric; the two signs cancel
    in the quotient.  Holds for all `n : ℕ` with no further hypotheses beyond
    `bar q = q⁻¹` and a nonvanishing denominator. -/
theorem quantumInt_isCPEven {q : R}
    (hbarq : BarInvolution.bar q = q⁻¹) (hden : q - q⁻¹ ≠ 0) (n : ℕ) :
    IsCPEven (quantumInt n q) := by
  unfold IsCPEven quantumInt
  rw [div_eq_mul_inv, BarInvolution.bar_mul, bar_inv' hden,
      numerator_bar_antisymmetric hbarq n, denominator_bar_antisymmetric hbarq,
      ← neg_inv, mul_neg, neg_mul, neg_neg, ← div_eq_mul_inv]

/-- Restated as the parity statement the S1 argument uses: the bar-parity gate
    admits `[n]_q` for **every** `n`, so it cannot distinguish between them. -/
theorem parity_gate_admits_all_quantumInt {q : R}
    (hbarq : BarInvolution.bar q = q⁻¹) (hden : q - q⁻¹ ≠ 0) :
    ∀ n : ℕ, IsCPEven (quantumInt n q) :=
  fun n => quantumInt_isCPEven hbarq hden n

/-- Adding the bar-involution image of the denominator to the denominator itself yields zero. -/
theorem denominator_bar_add_self_eq_zero {q : R}
    (hbarq : BarInvolution.bar q = q⁻¹) :
    BarInvolution.bar (q - q⁻¹) + (q - q⁻¹) = 0 := by
  rw [denominator_bar_antisymmetric hbarq, neg_add_cancel]

end Field

end QOU.BraidKnot.QuantumIntBarSymmetric
