---
# qou-n62l
title: Witness descriptions hardcode findings and drift; no gate reads a description
status: todo
type: task
created_at: 2026-09-06T11:31:55Z
updated_at: 2026-09-06T11:31:55Z
---

## The gap

Every staleness mechanism here compares a witness against its **producer** —
`scriptHash`, `q0Anchor`, the raw-float64 ratchet, the dps floor. **None reads
a `description`.** So a description that hardcodes a finding keeps asserting it
after the data moves underneath, and the witness ends up contradicting itself
inside a single file while staying green.

## Measured

`rho-binding-constancy.witness.json` said

> "the ratio varies ~182% (D 5.73, T 81.5, ³He 37.4)"

while carrying D 3.87 / T 36.99 / ³He 19.12 — and after regeneration under the
corrected atom word, 14.64 / 291.0 / 131.7. **The prose matched neither the
committed data nor the fresh data**: stale across at least two regenerations.
The same description also claimed "the D ratio 5.728 reproduces the published
α_M 5.729 (cross-validates the pipeline)" — a *claim* that had quietly stopped
holding.

## Built: `computations/audits/witness_prose_drift_audit.py`

Pulls every decimal number out of each `description` and buckets it by distance
to the nearest number anywhere else in the same document.

| bucket | rel | reported |
|---|---|---|
| EXACT | digits verbatim in data | no |
| ROUNDING | < 5e-3 | no |
| NEAR | < 5e-2 | no |
| **DRIFT** | **5e-2 .. 0.6** | **yes** |
| UNRELATED | > 0.6 | no |

`--selftest` passes **10/10**, including every calibrated false positive below.

### The calibration is the work — three passes, each driven by a measurement

1. **Distance, not presence.** `l1-ceiling-sign-prune`'s prose says `0.59`
   where the data has `0.5661` — an honest 3-sig-fig rounding at 4 %. A boolean
   "is the string present" test flags it exactly as loudly as a 49 %
   contradiction. Bucketing by distance clears it.
2. **Zeros destroy the ranking.** `|0 − x| / |x|` is **exactly 1.0 for every
   x**, and witnesses are full of zero counts and flags — so every prose number
   in every such witness scored 1.0 and the ranking saturated. A zero is never a
   drifted copy of a nonzero result. Dropping them: 233 → 210.
3. **The band needs an upper edge too.** Ranking by raw distance put a prose
   tolerance of `9.0e-18` beside data of order 1e-2 at **5e15**, burying
   everything real. The edge is set FROM the measured cases (0.058, 0.069,
   0.079, 0.33, 0.55), not guessed. 210 → 185.

Percent forms are matched against both `x` and `x/100`, because prose says
"~189.6 %" where the data carries `1.89576`. A decimal point is required, which
drops years, PR numbers (#1105) and bean ids without needing a list of them.

### Validated against the four cases whose status was already known

| witness | result | expected |
|---|---|---|
| `delta-lambda-qdim-route-probe` | FLAGGED 0.41, 5.62 | known stale ✓ |
| `delta-lambda-cancellation-ascaling` | FLAGGED 0.28, 1.27, 1.31 | known stale ✓ |
| `delta-lambda-l1-ceiling-sign-prune` | clean | known ROUNDING ✓ |
| `rho-binding-constancy` | FLAGGED 5.728, 5.729 | — see below |

The last is **the documented limitation demonstrating itself**, and is the most
useful line in this bean. That description was FIXED to interpolate its numbers,
and none of its live figures (189.6, 14.64, 291.0, 131.7) is flagged. What is
flagged is the sentence *withdrawing* the old claim. Those digits are quoted
history and an external constant, correctly absent from the data. **No static
rule separates a withdrawn number from a live one**, and the audit does not
pretend to.

## Result

    3528 witnesses scanned | 383 without a description
    185 witnesses with candidates | 239 candidate numbers

~6 % of witnesses carrying a description. That is a **triage list, not a defect
list** — the audit narrows a 3500-file haystack to 185 descriptions worth
reading.

## The durable fix is not to correct the numbers

Correcting a stale number only resets the clock. The fix is to make the prose
**derive** them: `rho_binding_constancy_probe.py` now interpolates its
description from the computed ratios and cannot go stale again. That is the
pattern the 185 want, and it has been applied to exactly one producer.

## Unclaimed

Nothing corrected here. The two known-stale descriptions
(`qdim-route`, `cancellation-ascaling`) still state convention-dependence
findings nobody here has studied, and rewriting an unverified conclusion is
worse than leaving it visibly flagged.
