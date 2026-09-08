---
# qou-n5kp
title: 'main is RED on the raw-float64 ratchet: 3 REGRESSED witnesses, and one of them is a carve-out NAME miss not a precision defect'
status: in-progress
type: task
priority: normal
created_at: 2026-09-08T04:18:38Z
updated_at: 2026-09-08T04:19:07Z
---

## Measured on `main` `a61496dbc8` (2026-09-08), 36466 commits

    PYTHONPATH="computations:tools/qou-substrate/python:tools/pyhecke/python" \
      python3 computations/witness_raw_float64_audit.py --strict     # exit 1

      witnesses carrying raw float64 : 996
      NEW dirty witnesses            : 0
      REGRESSED (count increased)    : 3

             5 -> 20   computations/bar-pairing-binding-observable-extension.witness.json
             7 -> 12   computations/binding-rotation-phase-lead.witness.json
             3 -> 4    computations/chi-free-via-lr.witness.json

`NEW` is 0 — no witness became dirty from clean. All three were already
dirty and got dirtier when their producer was re-run, which is the
`qou-mnrd` / `qou-82ur` pattern: a drained witness is replaced by a
differently-dirty one.

## The three are NOT one defect — they are three, and one is not a defect at all

Field paths listed with the ratchet's own classification logic (same
`_count` traversal, paths instead of counts):

**1. `chi-free-via-lr` (3 -> 4) — a carve-out NAME miss, not precision loss.**
All four fields are `data.rows[i].wall_sec`, e.g. `0.0016`, `0.0648`.
These are wall-clock durations. The ratchet already carves out exactly
this class — but **by name**, against a closed vocabulary:

    EPHEMERAL_TIMING_FIELDS =
      {durationMs, durationSeconds, duration_sec, elapsed_s, elapsed_sec,
       elapsed_seconds}

`wall_sec` is not in it. So a producer that spelled its duration field
one legal-English way instead of another is reported as a precision
defect while an identical field one name over is silently excused. This
is entry N of the detector-blindness taxonomy in a new place: the
*carve-out* is blind, not the detector.

**2. `binding-rotation-phase-lead` (7 -> 12) — real payload floats.**
Twelve `*_pct` percentages: `spread_pct`, `A3_pair_spread_pct` under
five aggregation keys, plus `DTHe3_spread_full_pct` /
`DTHe3_spread_d0_pct`. e.g. `528.4406910371381`, `17254.056635865716`.

**3. `bar-pairing-binding-observable-extension` (5 -> 20) — real payload
floats.** Twenty fields across four `results[]` rows:
`B_arch_MeV`, `B_bar_MeV`, `AME_MeV`, `err_arch_pct`, `err_bar_pct`.
e.g. `B_arch_MeV = 0.16455022397738905`, `AME_MeV = 2.2245662` (the
deuteron AME binding, an experimental input).

## Producers

| witness | producer |
|---|---|
| chi-free-via-lr | `computations/chi_free_via_lr.py` |
| binding-rotation-phase-lead | `computations/binding_rotation_phase_lead.py` |
| bar-pairing-binding-observable-extension | `computations/bar_pairing_binding_observable.py` |

## Corpus-grep before claiming this open

Beans naming these three witness stems: `qou-k54t` (todo — chi source
straddle, not float64) and `qou-wlaf` (in-progress — a *different*
witness's cross-check). `qou-43v0` (todo) and `qou-w8rv` (completed,
fixed 2026-09-07) are about `bar_pairing_binding_observable` clobbering
its own input cache, not about its float payload. Nothing claims the
float64 regression. `qou-1u56` is the same *class* on four different
witnesses and is completed.

## What is NOT permitted here

`--rebaseline`, and adding any of these to `raw-float64-baseline.json`.
Baselines drain, never grow. Fix at the producer.
