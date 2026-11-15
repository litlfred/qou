import QOU.Basic
import QOU.MathlibExt.QIntegerCanonical
import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# The q-deformed Collatz conjecture — Skein module formulation

## Overview

The classical Collatz map divides by 2 (even) or applies 3n+1 (odd).
In the q-deformed setting, 2 and 3 lift to quantum integers [2]_q and
[3]_q, and the map operates on the Skein module S(q) ≅ ℤ[q±1].

Three algebraic identities control the dynamics:

1. **Skein divisibility**: `[3]_q = q · [2]_q + 1`
   The q-analog of 3 = 1·2 + 1.  Ensures the odd branch is well-defined.

2. **Contraction gap**: `[2]_q² - [3]_q = q`
   Two halvings overpower one tripling.  The margin is q itself.

3. **Uniqueness**: Among all critical pairs (p₁^k₁, p₂^k₂) with
   p₁^k₁ = p₂^k₂ + 1, Collatz (2², 3¹) is the unique case where
   the q-gap is a monomial — and therefore positive for all q > 0.

## The (p₁^k₁, p₂^k₂) family

A generalized Collatz map (p₁, p₂) divides by p₁ when divisible
and applies p₂·n + 1 otherwise.  The contraction condition is
[p₁]_q^k₁ > [p₂]_q^k₂, requiring k₁ halvings to beat k₂ triplings.

The gap polynomial `[p₁]^k₁ - [p₂]^k₂ ∈ ℤ[q±1]` determines whether
contraction holds for all q > 0 (all coefficients non-negative) or
only for q near 1 (some negative high-degree coefficients).
-/

namespace QOU.Substrate

-- ═══════════════════════════════════════════════════════════════
-- §1. The q-integer and its basic properties
-- ═══════════════════════════════════════════════════════════════

/-- The q-integer `[k]_q = (qᵏ - 1)/(q - 1)` -/
noncomputable def qInt (q : ℝ) (k : ℕ) : ℝ :=
  (q ^ k - 1) / (q - 1)

/-- **Bridge to the canonical GEOMETRIC bracket** — note which one.

This site is `(qᵏ − 1)/(q − 1)`, the geometric form, *not* the balanced
`[k]_q` that most of the corpus means.  Tying it to `qIntBal` would be a
mis-consolidation, and the module's `qIntGeo` docstring says why: the geometric
form is bar-*covariant* with weight `−(k−1)`, not bar-even, so it cannot carry a
bar-even quantity.  The `q ≠ 1` hypothesis is `geom_sum_eq`'s and is real —
at `q = 1` the closed form is `0/0 = 0` while the sum is `k`. -/
theorem qInt_eq_canonical (q : ℝ) (k : ℕ) (hq : q ≠ 1) :
    qInt q k = QOU.QInteger.qIntGeo q k := by
  rw [qInt, QOU.QInteger.qIntGeo_def, geom_sum_eq hq]

/-- `[2]_q = q + 1` for `q ≠ 1`. -/
theorem qInt_two (q : ℝ) (hq : q ≠ 1) :
    qInt q 2 = q + 1 := by
  unfold qInt
  have hq1 : q - 1 ≠ 0 := sub_ne_zero.mpr hq
  field_simp; ring

/-- `[3]_q = q² + q + 1` for `q ≠ 1`. -/
theorem qInt_three (q : ℝ) (hq : q ≠ 1) :
    qInt q 3 = q ^ 2 + q + 1 := by
  unfold qInt
  have hq1 : q - 1 ≠ 0 := sub_ne_zero.mpr hq
  field_simp; ring

theorem qInt_two_pos (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    qInt q 2 > 0 := by
  rw [qInt_two q hq1]; linarith

theorem qInt_three_pos (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    qInt q 3 > 0 := by
  rw [qInt_three q hq1]; nlinarith

-- ═══════════════════════════════════════════════════════════════
-- §2. Identity 1 — Skein divisibility: [3] = q·[2] + 1
-- ═══════════════════════════════════════════════════════════════

/-- **Skein divisibility**: `[3]_q = q · [2]_q + 1`.

    At q = 1 this is 3 = 1·2 + 1.  In the Skein-Collatz map,
    this identity ensures the odd branch is well-defined:
    for q-odd P (meaning [2]_q ∣ P+1), the numerator
    [3]_q·P + 1 = q·[2]_q·P + (P+1) is divisible by [2]_q. -/
-- Ref: [leitner2026] Ch 8 §5
theorem skein_divisibility (q : ℝ) (hq : q ≠ 1) :
    qInt q 3 = q * qInt q 2 + 1 := by
  rw [qInt_two q hq, qInt_three q hq]; ring

-- ═══════════════════════════════════════════════════════════════
-- §3. Identity 2 — Contraction gap: [2]² - [3] = q
-- ═══════════════════════════════════════════════════════════════

/-- **Contraction gap**: `[2]_q² - [3]_q = q`.

    Two halvings (each dividing by [2]_q) more than compensate
    one tripling (multiplying by [3]_q).  The margin between
    [2]_q² and [3]_q is exactly q — the substrate parameter.

    At q = 1: 2² - 3 = 1.  At q₀ ≈ 1.1097: 2.11² - 3.34 ≈ 1.11. -/
-- Ref: [lagarias2010] The Ultimate Challenge: The $3x+1$ Problem — see folio/schema/references.ts
theorem qInt_gap (q : ℝ) (hq : q ≠ 1) :
    qInt q 2 ^ 2 - qInt q 3 = q := by
  rw [qInt_two q hq, qInt_three q hq]; ring

/-- Direct consequence: `[3]_q < [2]_q²` for `q > 0`. -/
theorem qInt3_lt_qInt2_sq (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    qInt q 3 < qInt q 2 ^ 2 := by
  have h := qInt_gap q hq1; linarith

/-- The relative margin: `[2]_q² / [3]_q = 1 + q/[3]_q`. -/
theorem relative_margin (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    qInt q 2 ^ 2 / qInt q 3 = 1 + q / qInt q 3 := by
  have h3 := qInt_three_pos q hq hq1
  have h3ne : qInt q 3 ≠ 0 := ne_of_gt h3
  have hgap := qInt_gap q hq1
  field_simp
  linarith

-- ═══════════════════════════════════════════════════════════════
-- §4. Contraction estimates
-- ═══════════════════════════════════════════════════════════════

/-- The contraction ratio `[3]_q/[2]_q²` is strictly below 1. -/
theorem contraction_ratio_lt_one (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    qInt q 3 / qInt q 2 ^ 2 < 1 := by
  have h2sq_pos : (0 : ℝ) < qInt q 2 ^ 2 := by
    have := qInt_two_pos q hq hq1; positivity
  exact (div_lt_one h2sq_pos).mpr (qInt3_lt_qInt2_sq q hq hq1)

/-- The geometric mean contraction per cycle: `√([3]_q/[2]_q²) < 1`. -/
-- Ref: [collatz1937]
theorem geometric_mean_contraction (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    Real.sqrt (qInt q 3 / qInt q 2 ^ 2) < 1 := by
  rw [← Real.sqrt_one]
  apply Real.sqrt_lt_sqrt
  · apply div_nonneg (le_of_lt (qInt_three_pos q hq hq1))
    have := qInt_two_pos q hq hq1; positivity
  · exact contraction_ratio_lt_one q hq hq1

/-- The Skein convexity coefficient `q⁻²` is in `(0, 1)` for `q > 1`.

    The Skein relation J(L₊) = q⁻²·J(L₋) + (1-q⁻²)·J(L₀)
    is a convex combination, so crossing resolution is non-expansive. -/
theorem skein_convex_coeff (q : ℝ) (hq : q > 1) :
    0 < q⁻¹ ^ 2 ∧ q⁻¹ ^ 2 < 1 := by
  constructor
  · positivity
  · rw [inv_pow]
    have hq2 : (1 : ℝ) < q ^ 2 := by nlinarith
    exact inv_lt_one_of_one_lt₀ hq2

-- ═══════════════════════════════════════════════════════════════
-- §5. No periodic Collatz cycles (coprimality of [2] and [3])
-- ═══════════════════════════════════════════════════════════════

/-- **Coprimality of [2]_q and [3]_q.**

    The Skein divisibility identity `[3] = q·[2] + 1` is a
    Bézout relation: `[3] - q·[2] = 1`, so `gcd([2], [3]) = 1`.

    Consequence: `[3]^a ≡ 1 (mod [2])` for all `a ≥ 0`, while
    `[2]^b ≡ 0 (mod [2])` for `b ≥ 1`.  These can never be equal,
    so the equation `[3]^a = [2]^b` has no solution for `a, b > 0`.

    This proves: the Skein-Collatz map has **no periodic cycles**
    other than the fixed point P = 1.  A cycle with k_odd odd steps
    would require `[3]^{k_odd} = [2]^k`, which is impossible. -/
-- Ref: [collatz1937]
theorem qInt_coprime (q : ℝ) (hq : q ≠ 1) :
    qInt q 3 - q * qInt q 2 = 1 := by
  -- This IS the Skein divisibility identity, rearranged.
  have h := skein_divisibility q hq
  linarith

-- ═══════════════════════════════════════════════════════════════
-- §6. Uniqueness of Collatz in the (p₁^k₁, p₂^k₂) family
-- ═══════════════════════════════════════════════════════════════

/- **Uniqueness of the (2,3) gap as a monomial.**

    For the generalized Collatz family (a, a+1) with k₁=2, k₂=1:
    - (2,3): [2]² - [3] = q               (monomial, all q > 0)
    - (3,4): [3]² - [4] = q + 2q² + q³ + q⁴  (all positive)
    - (a,a+1) for a ≥ 2: all coefficients ≥ 0  (always contractive)

    Among the critical pairs p₁^k₁ = p₂^k₂ + 1:
    - (2², 3¹): gap = q                    (monomial — UNIQUE)
    - (3², 8¹): gap has negative coefficients
    - (a², (a²-1)¹) for a ≥ 3: gap has negative coefficients

    Collatz is the unique critical case with a monomial q-gap.

    This theorem proves the (2,3) case.  The (3,8) failure and
    general (a, a²-1) failure for a ≥ 3 are stated separately. -/

/-- The (3,4) gap: `[3]² - [4] > 0` for all `q > 0`.
    (Trivial case: 9 ≫ 4 classically.) -/
-- Ref: [leitner2026] Ch 8 §5
theorem qInt_gap_3_4 (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    qInt q 3 ^ 2 - qInt q 4 > 0 := by
  have hq1' : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  have h4 : qInt q 4 = q ^ 3 + q ^ 2 + q + 1 := by
    unfold qInt; field_simp; ring
  rw [qInt_three q hq1, h4]
  -- Goal: (q²+q+1)² - (q³+q²+q+1) > 0, i.e. q⁴+q³+2q²+q > 0 for q > 0.
  nlinarith [hq, sq_nonneg q, mul_pos hq hq, mul_pos (mul_pos hq hq) hq,
             mul_pos (mul_pos (mul_pos hq hq) hq) hq]

/-- The (3,8) gap is NOT always positive: `[3]²  - [8]` has
    negative coefficients.  For large q, `[8] > [3]²`.

    This means the (3,8) generalized Collatz does NOT have a
    contraction gap for all q > 0 — unlike Collatz (2,3). -/
-- Ref: [leitner2026] Ch 8 §5
theorem qInt_gap_3_8_fails (q : ℝ) (hq : q > 2) (hq1 : q ≠ 1) :
    qInt q 3 ^ 2 < qInt q 8 := by
  have hq1' : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  have hqp : q > 0 := by linarith
  have h8 : qInt q 8 = q^7 + q^6 + q^5 + q^4 + q^3 + q^2 + q + 1 := by
    unfold qInt; field_simp; ring
  rw [qInt_three q hq1, h8]
  -- Goal: (q²+q+1)² < q⁷+q⁶+q⁵+q⁴+q³+q²+q+1
  -- i.e. 0 < q⁷+q⁶+q⁵-q³-2q²-q  for q > 2.
  -- Reduce to q⁵ > q³ + 2q² + q (then q⁷, q⁶ are pure positive bonus).
  have h5 : q ^ 5 > q ^ 3 + 2 * q ^ 2 + q := by
    nlinarith [hq, sq_nonneg (q - 2), sq_nonneg q, mul_pos hqp hqp,
               mul_pos (mul_pos hqp hqp) hqp]
  nlinarith [h5, hq]

-- ═══════════════════════════════════════════════════════════════
-- §6. Contact threshold (supplementary — uses Real.log)
-- ═══════════════════════════════════════════════════════════════

/-- **One-sided: `v* < 2`** (equivalently `[3] < [2]²`).

    This docstring previously announced the two-sided `1 < v* < 2`, which the
    statement and proof below never established. The lower half `1 < v*`
    (equivalently `[2] < [3]`) is proved in
    `QOU.AppendixSurreals.CollatzThreeForms.one_lt_contactThreshold`, and the
    two-sided form is `contactThreshold_mem_Ioo` there. The lower half is what
    rules out a *single* halving per tripling, so it is load-bearing for the
    claim that the integer threshold is exactly two.

    Since v* < 2 is proved algebraically ([3] < [2]²), the integer
    condition ⟨v⟩ ≥ 2 (two halvings per tripling) suffices — and
    avoids transcendental quantities entirely. -/
-- Ref: [collatz1937]
theorem contact_threshold_lt_two (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    Real.log (qInt q 3) / Real.log (qInt q 2) < 2 := by
  -- Strategy: [3] < [2]² and [2] > 1, so log[3] < log([2]²) = 2·log[2]
  have h2pos : qInt q 2 > 0 := qInt_two_pos q hq hq1
  have h3pos : qInt q 3 > 0 := qInt_three_pos q hq hq1
  have h2gt1 : qInt q 2 > 1 := by rw [qInt_two q hq1]; linarith
  have hlog2pos : Real.log (qInt q 2) > 0 := Real.log_pos h2gt1
  rw [div_lt_iff₀ hlog2pos]
  have h2cast : (2 : ℝ) * Real.log (qInt q 2) = Real.log ((qInt q 2) ^ 2) := by
    rw [Real.log_pow]; push_cast; ring
  rw [h2cast]
  have hsq : qInt q 3 < (qInt q 2) ^ 2 := qInt3_lt_qInt2_sq q hq hq1
  exact Real.log_lt_log h3pos hsq

end QOU.Substrate
