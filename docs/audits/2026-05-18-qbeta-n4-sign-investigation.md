# Q_β precision-ladder N=4 sign investigation

**Date:** 2026-05-18
**Branch:** `claude/track-a-b-per-isotope-and-rho-xi`
**Context:** while wiring the N=3 categorical rung into `per_observable_100x_status.py`, the precision-ladder doc's N=4 claim (`-7×10⁻⁶ ppm = -7 ppt`) could not be reproduced from its written formula. This audit traces the discrepancy.

## TL;DR

The precision-ladder doc has **two issues** with the N=4 row:

1. **Sign error in the boxed formula.** Per
   [`q-beta-categorical-precision-ladder.md`](../../content/quantum-observable-universe/braids-and-knots/q-beta-categorical-precision-ladder.md), the N=4 factor is written
   `(1 + (b² + 1/2)·b⁴·ℏ_q⁸)`. With this **positive** coefficient
   `c_4 = +(b² + 1/2) = +1.253`, recomputation at 50 dps gives
   N=4 residual **+12.6 ppb**, worse than the N=3 categorical residual
   of +6.0 ppb. The doc's reported "−7×10⁻⁶ ppm = −7 ppt" is
   inconsistent with the formula as written.

2. **Categorical c_k ≠ empirical c_k.** The doc's reported residuals
   (N=3: `-0.0066 ppm`; N=4: `-7×10⁻⁶ ppm`) appear to use **fitted**
   c_k values, not the categorical ones (`c_3 = -2 = J_Hopf(q=1)`,
   `c_4 = b² + 1/2`). With the categorical values, residuals are
   larger by 5–80×. The "99.5% empirical match" / "99.9% empirical
   match" annotations on the c_k → categorical-source table actually
   measure this gap.

| rung | c_k (categorical) | c_k (empirical fit) | residual w/ categorical | residual w/ empirical |
|------|---:|---:|---:|---:|
| N=3 | -2 (J_Hopf(q=1)) | -2.0097 | **+6.02 ppb** | 0 (by fit) |
| N=4 (doc form, `+c_4`) | +(b²+1/2) = +1.253 | — | **+12.61 ppb** | — |
| N=4 (sign-flipped, `−c_4`) | -(b²+1/2) = -1.253 | -1.1435 | **-0.57 ppb** | 0 (by fit) |

## Method

Reproduce the precision-ladder values from
`q-beta-operator-valued-N3.witness.json` at 50 dps:

```python
b      = 0.86758406730705817865...
ℏ_q²   = 0.0098171885134786714364...
Q_N2   = 0.78233438546764064891...
Q_AME  = 0.78233341400000004818...
```

Apply N=3 with `c_3 = -2` (categorical):

```
factor_N3 = 1 - 2 · b³ · ℏ_q⁶
          = 1 - 1.2357e-6
Q_N3 = Q_N2 · factor_N3
     = 0.78233341870800394103
err_N3 = +4.708e-9 MeV = +6.018 ppb relative
```

Apply N=4 with doc's `c_4 = +(b² + 1/2)`:

```
c_4 = +1.252702
factor_N4 = 1 + c_4 · b⁴ · ℏ_q⁸
          = 1 + 5.16e-9
Q_N4 = Q_N3 · factor_N4 = 0.78233342386544752668
err_N4 = +9.865e-9 MeV = +12.610 ppb relative
```

This **worsens** the prediction relative to N=3. Inconsistent with
the doc's "N=4 within ceiling" claim.

Apply N=4 with sign-flipped `c_4 = −(b² + 1/2)`:

```
c_4 = -1.252702
factor_N4 = 1 + c_4 · b⁴ · ℏ_q⁸
          = 1 - 5.16e-9
Q_N4 = Q_N3 · factor_N4 = 0.78233341355056035537
err_N4 = -4.494e-10 MeV = -0.574 ppb relative
```

**This matches the doc's intent** (residual much smaller than N=3,
below the 9.2×10⁻⁵ ppm ceiling = 92 ppt). But the magnitude (-0.57 ppb)
is still ~80× larger than the doc's claimed "-7 ppt", because:

Solving for `c_4` to exactly close `Q_N4 = Q_AME`:

```
c_4_emp = (Q_AME - Q_N3) / (Q_N3 · b⁴ · ℏ_q⁸) = -1.143537
```

The empirical c_4 (-1.144) differs from sign-flipped categorical (-1.253)
by **9.5%**. The 9.5% gap is what produces the -0.574 ppb residual at
N=4-categorical (vs ~0 at N=4-empirical). The doc reports the
**empirical** N=4 fit, not the categorical.

## Implication for 100× experimental target

Even with these doc-vs-recomputation issues:

| rung | residual (categorical) | 100× target | status |
|------|---:|---:|---|
| N=0 (Form A) | 1 677 540 ppb | 7.8 ppb | misses ×215 000 |
| N=1 | 73 790 ppb | 7.8 ppb | misses ×9 460 |
| N=2 | 1 242 ppb | 7.8 ppb | misses ×159 |
| **N=3** (c₃=-2) | **+6.02 ppb** | 7.8 ppb | **beats by 24% ✓** |
| **N=4** (sign-flipped, c₄=-(b²+1/2)) | **-0.57 ppb** | 7.8 ppb | **beats by 14× ✓** |

**N=3 categorical alone already beats the 100×-experimental target.**
N=4 sign-flipped categorical beats it by an additional 10×. The doc's
"-7 ppt" claim at N=4 requires the empirical c_4 (-1.144), not the
categorical (-1.253).

## Recommended fixes to the precision-ladder content block

1. **Fix the boxed formula.** Change N=4 factor from
   `(1 + (b² + 1/2)·b⁴·ℏ_q⁸)` to `(1 − (b² + 1/2)·b⁴·ℏ_q⁸)` (minus
   sign). Alternatively, restate as `c_4 = -(b² + 1/2)` so the doc's
   uniform `(1 + c_k·b^k·ℏ_q^(2k))` pattern continues with a negative
   c_4.

2. **Clarify the residual table.** State explicitly whether the
   reported residuals (−0.0066 ppm at N=3, −7×10⁻⁶ ppm at N=4) use
   the categorical c_k or the empirical-fit c_k. The "99.5%" /
   "99.9%" empirical-match column suggests categorical, but the
   residual magnitudes only close to those values with empirical c_k.

3. **Add categorical-vs-empirical residual columns.** A two-column
   format clarifies whether the categorical prediction itself meets
   the c(K) ceiling, or whether the fit closure does. Currently
   ambiguous.

## What this branch does

- `per_observable_100x_status.py` now reads N=3 categorical (Q_N3
  with c_3 = -2) instead of N=0 Form A bare. Result: Q_β
  miss factor 215 000× → **0.77× (beats 100× target by 24%)**.

- This audit documents the N=4 sign issue and the categorical-vs-
  empirical c_k ambiguity for downstream cleanup of the precision-
  ladder content block.

- `binding_q_target_sweep.py` shows the full per-rung table at 50 dps
  so future agents can reproduce the values and spot any further
  discrepancies.

## Cross-references

- [`content/quantum-observable-universe/braids-and-knots/q-beta-categorical-precision-ladder.md`](../../content/quantum-observable-universe/braids-and-knots/q-beta-categorical-precision-ladder.md) — the precision-ladder content block (needs fixes per §"Recommended fixes" above)
- [`computations/q-beta-operator-valued-N3.witness.json`](../../computations/q-beta-operator-valued-N3.witness.json) — source values for N=2, N=3 reproduction
- [`computations/sweeps/binding_q_target_sweep.py`](../../computations/sweeps/binding_q_target_sweep.py) — reproduces the full ladder at 50 dps
- [`docs/audits/2026-05-18-1ppb-workplan-v7-100x-experimental.md`](2026-05-18-1ppb-workplan-v7-100x-experimental.md) — workplan
- [`docs/precision-goals.md`](../precision-goals.md) — Q_β 100×-experimental row now reflects N=3 categorical
