---
# qou-wn1w
title: 'GAP: the CODATA stale-edition scan was a gate nobody ran'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-22T16:00:32Z
updated_at: 2026-11-16T18:12:00Z
parent: qou-2002
---

## What

`computations/codata_corpus_literal_scan.py --strict` was written
2026-08-19, worked from the start, and drained 61 executable stale-CODATA
sites to 0 across #5423 and #5439. It was **in no gate array** — so the
day after the drain, nothing stopped site 62 from landing.

This is `scripts/precision-gates.sh`'s own recorded failure mode, one
detector later: *"A GATE OUTSIDE THIS ARRAY IS A GATE NOBODY RUNS"*
(2026-08-10, bean qou-j6gb, about `mpf_import_time_dps_audit.py` — written,
working, unwired, and its defect class then landed five more times).

## Done

1. Added to `GATES` as **blocking**, with a self-test. Green on arrival:
   CODE sites 0, measured on main at `74c00bb0`.
2. **Widened the `--changed` predicate** to include
   `content/**/*.{lean,ts}`. This is the part that would have been easy
   to miss: every other gate examines witnesses and `computations/`
   Python, so the old two-pattern predicate was right for them. Of the 30
   executable sites remaining when #5439 reached its last tranche,
   **20 were `.lean`** — so wiring the gate without widening would have
   shipped it short-circuited on the file type carrying two thirds of its
   own defect class.

## Verified it FIRES, not just that it passes

Re-injected the exact CODATA-2018 value drained from
`AtomicMass.lean:65` (`931.49410242` for `931.49410372`). The gate
reported CODE sites 1, named `AtomicMass.lean:65`, and exited 1. Tree
restored.

A gate that only ever passes is indistinguishable from a gate that
examines nothing — the same principle behind this file's own self-test
mechanism.

## Cost, stated plainly

**~100 s, the slowest gate in the array**, against ~40 s for all the
others combined. Accepted rather than trimmed, because the alternative
on the table was leaving it unwired. The cost is in the per-literal
mpmath comparison over ~25k files, not the I/O, if it ever needs
reducing.

The `--changed` widening also means a Lean-only commit now runs the full
preflight where it previously ran nothing. If that proves too heavy, the
fix is to scope THIS gate to changed paths — not to narrow the predicate
back and re-open the hole.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-22 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-16 — live verification on `origin/main` (PR #8146)

Verified on `origin/main` (`dc12b128cc`) and PR #8146 (`5c6c5fb610a38f0405e9d280b16b0999a8124c8f`):

- `scripts/precision-gates.sh` carries `"CODATA stale-edition|computations/codata_corpus_literal_scan.py|--strict --quiet --no-witness|yes|yes"` as a blocking gate with self-test enabled (`--changed` predicate includes `^folio/.*\.(lean|ts)$`).
- Re-ran `python3 computations/codata_corpus_literal_scan.py --self-test`: 30/30 assertions pass (`self-test passed`, exit 0). Kept at `status: in-progress` for owner review.
