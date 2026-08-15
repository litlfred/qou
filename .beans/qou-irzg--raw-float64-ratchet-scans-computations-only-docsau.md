---
# qou-irzg
title: raw-float64 ratchet scans computations/ only — docs/audits/scripts/ witnesses are ungated (5 carry raw floats)
status: todo
type: task
created_at: 2026-08-15T02:49:47Z
updated_at: 2026-08-15T02:49:47Z
---


## Evidence

`scripts/precision-gates.sh --changed` on a branch touching only
`docs/audits/scripts/` reports:

    precision-gates: no witness or computations/ script touched — skipped.

That is correct behaviour for the script as written, and it is the problem: the
raw-float64 ratchet's scan root is `computations/`, so every witness under
`docs/audits/scripts/` is outside the NO-FLOAT64 discipline. Audit probes emit
witnesses there routinely — this session alone added three.

Scanning that directory by hand (JSON walk for Python `float` instances) found
**5 witnesses carrying raw float64**, none of them from this arc:

| witness | raw floats |
|---|---|
| `qbeta-action-qsqrt3-saddle-probe` | 8 |
| `qbeta-ohtsuki-deformed-meridian-rungs` | 6 |
| `keystone-wlambda-unitarity-normalization-gate` | 4 |
| `qbeta-ohtsuki-deformed-kappa5-phase-test` | 1 |
| `qbeta-ohtsuki-deformed-kappa3-tall-ladder` | 1 |

Several are `max_loss_digits` / `c_ratios` — diagnostic magnitudes rather than
physical predictions, so the *harm* may be low. The *gap* is not: nothing stops
a q₀-bearing prediction landing there ungated, and the directory is where
audit probes naturally write.

## Two separable pieces

1. **Widen the ratchet's scan root** to include `docs/audits/scripts/`. Cheap.
   Expect it to go red immediately on the five above — which is the point, but
   means it needs a baseline decision, not a one-line patch.
2. **Drain the five.** Belongs to whichever arc owns those probes, per the
   prepare-merge rule that inherited red is not the current branch's regression.

Found while running `/prepare-merge` step 4b on PR #5060. Not fixed there: the
branch introduced no red, and widening a ratchet mid-merge would have made the
gate's first run red on someone else's witnesses.
