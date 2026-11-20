---
# qou-jtgk
title: 'intermediate_knot_detection: float64 but NOT a defect — 1.2e-14 worst error at A=40, both verdicts robust, and draining needs hecke_core'
status: todo
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T13:13:40Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---

Screened 2026-09-13 as raw-float64 drain target 9 (350 baseline fields, the
largest remaining solo entry not blocked behind a regeneration decision).
**Cleared: it is float64 throughout and it is not a defect.** Recorded so the
size ranking stops offering it.

## Why it looked like one

Every recorded family is float64 and two of them are VERDICTS read off a cast:

    tight_idx = int(np.argmin(Gx))                  which constraint is tight
    stable    = all(float(g) >= -1e-10 for g in Gx) the stability certificate

and by ⁴⁰Ca the magnitudes are enormous — `frob = 1.79e30`,
`min_Gx = -601475912910099.125`. That `.125` ending is the float64 ulp at 6e14,
and I read it as "the recorded value is at the representation floor". **That
reading was wrong** and is the third alarm I raised from an uncalibrated look
today; it is recorded rather than deleted for the same reason as the others.

## What is actually true, measured

**Both verdicts are robust, by 12-14 orders.** Walked all 83 steps across the
seven atoms:

  * `argmin`: the two smallest `Gx` never come closer than **1.5e-2 relative**
    (worst at ⁴⁰Ca A=17: 79.1937 against 80.3799). Against ~1e-16 noise, the
    recorded `tight` constraint is never decided by rounding.
  * `stable`: no `Gx` ever comes closer than **0.53** to the -1e-10 threshold.

**The arithmetic is numerically STABLE in the relative sense.** Re-ran the whole
NF walk in mpmath at 70 dps — `hm()` is generic over the numeric type, and
`h = q - 1/q` / `z = q³/(q²+1)` reconstruct `hecke_core`'s float64 values to
5.5e-17 — and compared component by component:

| atom | A | max \|nf\| | worst rel err, f64 vs exact |
|---|---:|---:|---:|
| ²H | 2 | 1.08 | 8.36e-16 |
| ⁴He | 4 | 1.13 | 2.16e-15 |
| ⁶Li | 6 | 1.40 | 1.54e-15 |
| ¹²C | 12 | 3.79 | 2.62e-15 |
| ¹⁶O | 16 | 19.6 | 8.10e-15 |
| ⁴⁰Ca | 40 | **8.85e+14** | **1.23e-14** |

The NF magnitude grows **fifteen orders**; the relative error grows **one**. At
A=40 the values still carry ~11 significant digits — and the witness records
them through `round(x, 4)` / `round(x, 6)`, i.e. **4-6 decimals**. So the
published numbers are five orders more precise than what is published.

## Why it is not worth draining, and what it would cost

The whole chain is float64 at the source: `hecke_core` exports `z`, `h`, `q0`,
`qi` as Python floats and `G` as a float64 (6,6) ndarray. This producer cannot
carry `mpf` without `hecke_core` serving exact values, and that module has many
consumers — a blast radius far beyond one drain, and outside the file a drain
pass was sent to under the 2026-09-07 ASK-THE-OWNER directive.

**So the trade is: change a widely-consumed shared module, to move values from
~11 correct significant digits to 60, on fields published at 4-6 decimals, whose
two verdicts are already robust by 12+ orders.** Not worth it, and the 350
fields should be treated as a low-priority tail rather than as the 350-field
target the size ranking makes them look like.

**What WOULD change this**: if `hecke_core` is made exact for another reason,
this producer comes along nearly free — `hm()` is already type-generic, which is
the hard part. Worth doing then, not before.

**Not claimed**: that the `frob` / `cos_sim` / `min_Gx` values inherit the same
1.2e-14. Those go through `G @ x` and a norm ratio, which can cancel; I measured
the **NF vector**, which is what they all derive from, and did not measure them
separately because `hecke_core.G` has no exact counterpart to compare against.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8349, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
