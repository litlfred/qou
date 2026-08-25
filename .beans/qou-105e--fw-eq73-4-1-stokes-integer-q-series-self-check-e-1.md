---
# qou-105e
title: FW eq(73) 4_1 Stokes integer q-series self-check (E_1 = divisor-fn Lambert series)
status: completed
type: task
priority: normal
created_at: 2026-08-01T18:42:34Z
updated_at: 2026-08-06T00:00:00Z
---

## Outcome — the compute landed and passes; the bean was simply never closed

Deliverable exists and is green:

- producer `computations/probes/fourone_stokes_series_selfcheck.py`
- witness `computations/probes/fourone-stokes-series-selfcheck.witness.json`

Three assertions, all passing:

| assertion | result |
|---|---|
| `E1_constant_term_is_minus_one_quarter` | `-1/4` ✓ |
| `E1_integer_coeffs_match_printed_eq73` | `[1,2,2,3,2,4,2,4,3]` ✓ |
| `E1_integer_coeffs_equal_divisor_function_sigma0` | matches `σ₀(n)` ✓ |

So the Fantini–Wheeler eq(73) `4₁` Stokes integer q-series is confirmed to be
the divisor-function Lambert series, with the `−1/4` constant term. That is
the self-check the bean asked for.

Closed on inspection 2026-08-06: the bean sat `in-progress` with an empty
body since 2026-08-01 while its compute was already committed and green.
Nothing further was required of *this* bean.

## Follow-on

The ∞-side continuation is `qou-mvb2` (leading blocks — now landed) and the
Stokes-multiplier extraction that follows it.
