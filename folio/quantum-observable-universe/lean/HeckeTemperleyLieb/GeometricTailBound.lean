/-
# Summing a geometric tail is bounded by its own second term

The flavour split `δ = Δm_pn/M_N` is carried in the corpus as a derived leading
term times a posited correction:

```
δ_leading = (q-1)²(1-q⁻⁴)/3        δ_canonical = δ_leading · (1 + ℏ_q³)
```

and `(1 + ℏ_q³)` is the first two terms of `1/(1 - ℏ_q³)`. The natural instinct —
**"use all the terms"** — is right in principle, and this file bounds exactly what
it can buy.

The whole tail beyond the two-term form is

```
(1-x)⁻¹ - (1+x) = x²/(1-x)
```

At `x = ℏ_q³ ≈ 9.727e-4` that is `9.47e-7`, while the gap between the two-term
form and the measured `Δm_pn/M_N` is `3.06e-4` — **323 times larger**. So summing
every remaining term closes about one three-hundredth of what is missing:
`summing_cannot_close` is the general statement, and the numbers above are its
instance.

Two things this file deliberately does not do.

**It does not claim the series is the right object.** `(1 + ℏ_q³)` is labelled a
"3-loop substrate-Planck" correction, not a geometric series, and nothing derives
it (`docs/audits/2026-06-29-color-weighting-coverage-and-flavor-split-closed-form.md`,
Parts B and C). Reading two terms as the start of a geometric series and summing
them is a step nobody has justified.

**And it does not rescue the series numerically either.** Solving
`δ_leading/(1 - ℏ_q^k) = δ_CODATA` for the exponent gives `k = 2.8822`, not `3`;
and `1 + c·ℏ_q^k` needs `c = 0.0129, 0.1302, 1.3146, 13.267` at `k = 1, 2, 3, 4`
— none of them `1` or any simple rational. Those are measurements
(`computations/qbeta/qbeta_flavour_split_series_probe.py`, extending
`computations/probes/flavor_split_geometric_closure_probe.py`, which had already
measured the `k = 3` coefficient as `1.31459` and ruled the factor "a partial,
posited factor, not merely unproven"), not theorems, and they are what makes the
theorem below the relevant one: the missing `0.03 %` is not in this tower at any
order.

## What is proved

Pure algebra over an ordered field, with no substrate constant in it. The physics
enters only as the hypothesis `K > 1` in `summing_cannot_close`, which says the
outstanding gap exceeds the entire tail — a measured fact, stated as a hypothesis
rather than smuggled in.
-/

import Mathlib.Tactic

namespace QOU.Hecke.GeometricTailBound

/-- **The whole tail of a geometric series past its second term.**
`(1-x)⁻¹ - (1+x) = x²/(1-x)`, for any `x ≠ 1`. -/
theorem tail_eq {x : ℝ} (hx : x ≠ 1) :
    (1 - x)⁻¹ - (1 + x) = x ^ 2 / (1 - x) := by
  have h : (1 : ℝ) - x ≠ 0 := sub_ne_zero.mpr (Ne.symm hx)
  field_simp
  ring

/-- The tail is positive when `0 < x < 1`, so summing always moves in the same
direction — it just cannot move far. -/
theorem tail_pos {x : ℝ} (h0 : 0 < x) (h1 : x < 1) :
    0 < (1 - x)⁻¹ - (1 + x) := by
  have hpos : (0 : ℝ) < 1 - x := by linarith
  rw [tail_eq (ne_of_lt h1)]
  exact div_pos (pow_pos h0 2) hpos

/-- A crude but useful bound: for `0 ≤ x ≤ 1/2` the entire tail is at most
`2x²`. So "all the terms" is second order in a quantity already small. -/
theorem tail_le {x : ℝ} (_h0 : 0 ≤ x) (h1 : x ≤ 1/2) :
    (1 - x)⁻¹ - (1 + x) ≤ 2 * x ^ 2 := by
  have hlt : x < 1 := by linarith
  have hpos : (0 : ℝ) < 1 - x := by linarith
  rw [tail_eq (ne_of_lt hlt), div_le_iff₀ hpos]
  nlinarith [mul_nonneg (sq_nonneg x) (by linarith : (0:ℝ) ≤ 1 - 2 * x)]

/-- **Summing every remaining term cannot reach a target that the tail
undershoots.**

If the outstanding gap `C - (1+x)` is `K` times the entire tail with `K > 1`,
then even the full geometric sum `(1-x)⁻¹` falls short of `C`.

This is the honest content of "we should use all the terms": one may, and it is
still not enough. At `x = ℏ_q³` the measured `K` is `323`. -/
theorem summing_cannot_close {x C K : ℝ} (h0 : 0 < x) (h1 : x < 1) (hK : 1 < K)
    (hgap : C - (1 + x) = K * (x ^ 2 / (1 - x))) :
    (1 - x)⁻¹ < C := by
  have hpos : (0 : ℝ) < 1 - x := by linarith
  have htail : (0 : ℝ) < x ^ 2 / (1 - x) := div_pos (pow_pos h0 2) hpos
  -- Rewrite the full sum as `(1+x)` plus the whole tail, and `C` as `(1+x)`
  -- plus `K` copies of that same tail.  With `K > 1` the comparison is then
  -- one subtraction, with no division left in it.
  have hinv : (1 - x)⁻¹ = (1 + x) + x ^ 2 / (1 - x) := by
    have h := tail_eq (x := x) (ne_of_lt h1)
    linarith
  have hC : C = (1 + x) + K * (x ^ 2 / (1 - x)) := by linarith
  have hstrict : x ^ 2 / (1 - x) < K * (x ^ 2 / (1 - x)) := by
    nlinarith [mul_pos (sub_pos.mpr hK) htail]
  rw [hinv, hC]
  linarith

/-- Contrapositive form, which is how the measurement is actually used: if the
full sum DOES reach the target, the gap was at most the tail. -/
theorem gap_le_tail_of_summing_closes {x C : ℝ} (_h0 : 0 < x) (h1 : x < 1)
    (hreach : C ≤ (1 - x)⁻¹) :
    C - (1 + x) ≤ x ^ 2 / (1 - x) := by
  rw [← tail_eq (ne_of_lt h1)]
  linarith

end QOU.Hecke.GeometricTailBound
