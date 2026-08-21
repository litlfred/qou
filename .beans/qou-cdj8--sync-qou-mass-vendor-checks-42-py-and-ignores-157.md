---
# qou-cdj8
title: sync-qou-mass-vendor checks 42 .py and ignores 157 .witness.json — 122 disagree with source on the q0 pin
status: in-progress
type: task
priority: normal
created_at: 2026-08-21T21:44:29Z
updated_at: 2026-08-21T21:44:58Z
---

Split from `qou-hp3g`, whose sync-drift half turned out already fixed
(`e4906af5a4c`) and whose title I had to retract. This is the half that is real.

## The defect

`scripts/sync-qou-mass-vendor.py` `--check`/`--apply` iterate `cone` and
compare `VENDOR / f"{mod}.py"` — **Python modules only**. It reports

    vendored copies are in sync (42 modules)

while **157 tracked `*.witness.json` under `qou-mass/src` are compared to
nothing.** A gate that reports success without examining the thing that drifted.

`required_witnesses()` (line ~195) already computes which witnesses the
vendored modules load at runtime; its result feeds a `--list` report, not the
comparison. So the design anticipated the data files — the check just never
consumed it.

## Measured (current main, 157/157 have a computations/ twin)

| | count |
|---|---|
| identical raw-float64 count | 34 |
| differing | 123 |
| mirror dirtier than source | 17 |
| **mirror/source disagree on q₀ pin** | **122** |

Worked case — `canonical-mass-table-extended.witness.json`:

    mirror  1af7d4b7a04  2026-08-15  "qou-mass v1.0.0"          33 f64   MUON
    source  da2968cc335  2026-08-19  "first witnesses at the    0 f64    PROTON
                                       proton pin"

Four days stale, and on the anchor the 2026-08-07 owner directive superseded
(reaffirmed R2, 2026-08-15). The float64 gap is a CONSEQUENCE of the staleness,
not the sync introducing error — the sync never writes these files at all.

## Blast radius — narrow, and must stay stated that way

`qou-mass` is **not published** (AGENTS.md: 404 on PyPI, no dist/, no publish
step). No external consumers. Exposure is the **5 in-repo importers**. Do not
write this up as researchers receiving wrong numbers.

## Plan

1. Extend `--check` to compare the witness JSONs `required_witnesses()`
   already identifies, so the gate covers what it ships.
2. Show it fires (plant/detect/restore), as with the .py half.
3. Re-sync the data and confirm the q₀ disagreement goes to 0.
4. Precision preflight on the result — re-syncing changes what the package
   carries, so the raw-float64 posture must be measured after, not assumed.
