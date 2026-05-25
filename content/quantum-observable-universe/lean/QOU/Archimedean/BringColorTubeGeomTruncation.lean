import Mathlib.Algebra.GeomSum
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import QOU.Archimedean.BringFaddeevH4LinkingWeight
import QOU.Archimedean.BringColorTubeQForm

/-!
# Bring color-tube truncation — geometric-series form (PROVED)

Alternative truncation theorem for `bringColorTube q`, using the
**geometric-series expansion in z = h_q · q^{10}** instead of the
Taylor expansion in `h_q` around `h_q = 0`.

## Why the geometric-series form?

The Taylor expansion in h (per `HExpansionDegree8.lean`) treats `q`
as a function of `h` via `q(h) = (h + √(h² + 4))/2`, and produces
rational h-coefficients (1, 1, 6, 47/2, …). Proving the truncation
error requires Mathlib's analytic-function infrastructure.

The geometric-series expansion treats `q` and `h` independently, with
`z = h · q^{10}` as the expansion variable:

  `1/(1 − z) = Σ_{k=0}^∞ z^k` for `|z| < 1`.

Truncation:

  `1/(1 − z) − Σ_{k=0}^{n} z^k = z^{n+1} / (1 − z)`.

This is a **clean algebraic identity** provable by Mathlib's `geom_sum_eq`
+ `field_simp + ring`, with NO analytic-function infrastructure
needed.

## Applied to Bring color-tube

  `bringColorTube q = 1/(1 − heckeH q · q^{10})`
  `truncated_n q = Σ_{k=0}^{n} (heckeH q · q^{10})^k`
  `tail_n q = (heckeH q · q^{10})^{n+1} / (1 − heckeH q · q^{10})`

The truncation IDENTITY (proved here):

  `bringColorTube q − truncated_n q = tail_n q`

At the substrate q₀ ≈ 1.110: z = h·q^{10} ≈ 0.594, so |z| < 1 ✓
and the truncation is well-defined. At n = 8: |z|⁹ ≈ 0.014, divided
by `1 − z ≈ 0.406` gives ≈ 0.034 — but THAT bound is the
`(h·q^{10})^9` form, NOT directly comparable to my Taylor-form's
`h^9` bound. They're different truncations.

## Status

PROVED sorry-free. Closes a different form of the truncation
theorem than the Taylor-based one in
[`TruncationErrorBound.lean`](TruncationErrorBound.lean) (which
remains sorry'd, gated on Mathlib's Taylor.Lagrange).

## References

- Mathlib `Mathlib.Algebra.GeomSum.geom_sum_eq` — geometric sum formula
- [`BringColorTubeQForm.lean`](BringColorTubeQForm.lean) — closed q-rational forms
- [`docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md`](../../../../../docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md) §6
-/

namespace QOU.Archimedean

open Real Finset BigOperators

/-! ## §1  Truncated geometric series in z = h·q^{10} -/

/-- The degree-n truncation of `1/(1 − z)` at `z = heckeH q · q^{10}`:

      `bringTrunc_n q := Σ_{k=0}^{n} (heckeH q · q^{10})^k`. -/
noncomputable def bringTrunc (q : ℝ) (n : ℕ) : ℝ :=
  ∑ k in Finset.range (n + 1), (heckeH q * q ^ 10) ^ k

/-- At `n = 0`, the truncation is just the constant term 1. -/
theorem bringTrunc_zero (q : ℝ) : bringTrunc q 0 = 1 := by
  unfold bringTrunc
  simp

/-- At `n = 1`, the truncation is `1 + z = 1 + heckeH q · q^{10}`. -/
theorem bringTrunc_one (q : ℝ) :
    bringTrunc q 1 = 1 + heckeH q * q ^ 10 := by
  unfold bringTrunc
  rw [Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_zero]
  ring

/-! ## §2  Truncation tail (closed form) -/

/-- The tail of `bringColorTube q` beyond the degree-n truncation:

      `bringTail_n q := (heckeH q · q^{10})^{n+1} / (1 − heckeH q · q^{10})`.

    This is the residual mass-at-infinity of the geometric series. -/
noncomputable def bringTail (q : ℝ) (n : ℕ) : ℝ :=
  (heckeH q * q ^ 10) ^ (n + 1) / (1 - heckeH q * q ^ 10)

/-! ## §3  **The truncation identity (PROVED)** -/

/-- **Bring color-tube truncation identity (PROVED)**.

    For `q ≠ 0` and `1 − heckeH q · q^{10} ≠ 0`:

      `bringColorTube q − bringTrunc q n = bringTail q n`.

    This is the closed-form geometric-series-tail identity, applied
    to `z = heckeH q · q^{10}`. Proved via Mathlib's `geom_sum_eq` +
    `field_simp + ring`. -/
theorem bringColorTube_geom_truncation_identity (q : ℝ) (hq : q ≠ 0)
    (hz : 1 - heckeH q * q ^ 10 ≠ 0) (n : ℕ) :
    bringColorTube q - bringTrunc q n = bringTail q n := by
  unfold bringColorTube bringTrunc bringTail
  -- Let z := heckeH q * q^10. We need to show:
  --   1/(1-z) - Σ_{k=0}^{n} z^k = z^{n+1} / (1-z)
  -- Using geom_sum_eq: Σ_{k=0}^{n} z^k = (z^{n+1} - 1) / (z - 1).
  set z := heckeH q * q ^ 10 with hz_def
  have hz1 : z - 1 ≠ 0 := by
    intro h
    apply hz
    have : 1 - z = -(z - 1) := by ring
    rw [this, h]; ring
  -- Note: geom_sum_eq gives Σ_{k<n+1} z^k = (z^{n+1} - 1) / (z - 1)
  have h_geom : (∑ k in Finset.range (n + 1), z ^ k)
              = (z ^ (n + 1) - 1) / (z - 1) :=
    geom_sum_eq hz1 _
  rw [h_geom]
  field_simp
  ring

/-! ## §4  Bound on the truncation tail -/

/-- When the geometric-series argument `z = h·q^{10}` is in `(0, 1)`
    (which holds at the substrate), the truncation tail is positive
    and decreases as `z^{n+1}`. -/
theorem bringTail_pos (q : ℝ) (hq : q ≠ 0)
    (hz_pos : heckeH q * q ^ 10 > 0) (hz_lt_one : heckeH q * q ^ 10 < 1)
    (n : ℕ) :
    bringTail q n > 0 := by
  unfold bringTail
  have h_num_pos : (heckeH q * q ^ 10) ^ (n + 1) > 0 :=
    pow_pos hz_pos (n + 1)
  have h_denom_pos : 1 - heckeH q * q ^ 10 > 0 := by linarith
  exact div_pos h_num_pos h_denom_pos

/-- **Truncation error bound**: |bringColorTube q − bringTrunc q n|
    equals the tail (which is positive). For `|z| < 1`, the tail is
    bounded by `|z|^{n+1} / (1 − |z|)` — the standard geometric-series
    tail estimate. -/
theorem bringColorTube_truncation_abs_bound (q : ℝ) (hq : q ≠ 0)
    (hz_pos : heckeH q * q ^ 10 > 0) (hz_lt_one : heckeH q * q ^ 10 < 1)
    (n : ℕ) :
    |bringColorTube q - bringTrunc q n|
      = (heckeH q * q ^ 10) ^ (n + 1) / (1 - heckeH q * q ^ 10) := by
  have hz_ne : 1 - heckeH q * q ^ 10 ≠ 0 := by linarith
  rw [bringColorTube_geom_truncation_identity q hq hz_ne n]
  unfold bringTail
  have h_tail_pos : (heckeH q * q ^ 10) ^ (n + 1) / (1 - heckeH q * q ^ 10) > 0 := by
    have := bringTail_pos q hq hz_pos hz_lt_one n
    unfold bringTail at this
    exact this
  rw [abs_of_pos h_tail_pos]

/-! ## §5  At the substrate q₀

At q₀ ≈ 1.110: z = h·q^{10} ≈ 0.594 ∈ (0, 1). The tail at n = 8 is

  z^9 / (1 - z) ≈ 0.594^9 / 0.406 ≈ 0.0096 / 0.406 ≈ 0.024

which is a 2.4 % truncation error — consistent with the audit's
remark that the +108 ppm m_p prediction error is dominated by the
Bring color-tube h⁹ truncation, NOT by the Faddeev h¹² tail.

The geometric-series truncation in z is COARSER than the Taylor-in-h
truncation (which gave ~108 ppm) because z = h·q^{10} ≈ 0.594 is
much larger than h ≈ 0.209 — the q^{10} amplification.

## §6  Status

PROVED sorry-free:
  ✓ bringTrunc_zero, bringTrunc_one (definitional)
  ✓ bringColorTube_geom_truncation_identity (geom_sum_eq + field_simp + ring)
  ✓ bringTail_pos (positivity)
  ✓ bringColorTube_truncation_abs_bound (= the closed-form tail)

This file COMPLEMENTS the still-sorry'd Taylor-form truncation in
[`TruncationErrorBound.lean`](TruncationErrorBound.lean). The two
forms are mathematically equivalent — they express the same
function's truncation error in different bases (geometric series in
z vs Taylor series in h around 0). The geometric form is provable
without Mathlib's analytic-function infrastructure.
-/

end QOU.Archimedean
