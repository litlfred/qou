---
# qou-kn46
title: raw-float64 ratchet baseline is calibrated on STALE witnesses, so a refresh reads as a regression
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T07:39:37Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---

MEASURED on branch claude/q0-anchor-flip-tranche-2026-08-19, 2026-08-24.

## What happened

The q0 migration re-ran ~150 producers. The raw-float64 ratchet went RED:

    NEW dirty witnesses            : 0
    REGRESSED (count increased)    : 5

All five were attributed to this branch (`git diff origin/main HEAD -- <w>`
showed CHANGED-HERE for each). But **none of the five producers changed on
this branch** -- `git diff --quiet origin/main HEAD -- <producer>` was clean
for all five.

## The actual cause

main's committed witnesses were written by OLDER producer versions. The
current producers emit more float64 fields than the committed witnesses
record. So the baseline, which is computed from the committed witnesses,
is calibrated **below the producers' true output**.

Consequence: the ratchet under-reports the real backlog, and it bills the
first agent to re-run a stale producer for a defect that has been sitting
in main's producer the whole time. This is the mirror image of qou-qrsp
(baseline drains while the producer defect stays); here the baseline is
*low* and a truthful refresh reads as a regression.

## Second finding: the detector cannot distinguish exact-int-as-float

Every one of the 63 "gained" fields was an exact integer whose JSON type
flipped, with ZERO precision change:

    0 -> 0.0    (toffoli conclusions/classical_limit_q_equals_1/Phi)
    0 -> -0.0   (sublemma value_im -- signed-zero artifact)
    1 -> 1.0    (t35 unknot_markov_trace; toffoli gram_matrix_at_q0[0][0])
    2 -> 2.0    (six-term S_lambda for D  -- this is A=2, a nucleon count)
    4 -> 4.0    (six-term S_lambda for He4 -- A=4)
    6 -> 6.0    (nv factor_value, 3! = |S_3|)
    5730 -> 5730.0 (t35 C-14 half-life in years)

`witness_raw_float64_audit.py` counts `isinstance(x, float)`, which is
correct as far as it goes -- `0.0` IS a float64 in the witness -- but it
cannot tell a leaked float64 computation from an exact integer that
happened to be serialized with a decimal point. Both are equally red.

## Suggested fixes

1. **Baseline**: regenerate it from a fresh producer sweep rather than from
   the committed witnesses, or record per-file the producer sha the count
   was measured at, so a refresh-driven delta is distinguishable from a
   genuine leak. (See the witness_staleness_triage.py precedent in AGENTS.md
   -- same class of problem, same fix shape.)
2. **Detector**: annotate fields where `float(x).is_integer()` separately
   from genuinely-fractional float64. That does NOT excuse them (an exact
   integer should still be serialized as an int), but it turns a red
   "precision regression" into an accurate "exactness regression", which
   is a different and much cheaper fix.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8357, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
