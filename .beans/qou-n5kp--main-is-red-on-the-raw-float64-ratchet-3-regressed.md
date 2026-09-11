---
# qou-n5kp
title: 'main is RED on the raw-float64 ratchet: 3 REGRESSED witnesses, and one of them is a carve-out NAME miss not a precision defect'
status: completed
type: task
priority: normal
created_at: 2026-09-08T04:18:38Z
updated_at: 2026-09-11T15:11:54Z
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


---

## RESOLVED 2026-09-11 — all three fixed at the producer, ratchet GREEN

    witness_raw_float64_audit.py --strict      # exit 0
      NEW dirty witnesses : 0
      REGRESSED           : 0        (was 3)

| witness | before | after | what it was |
|---|---|---|---|
| bar-pairing-binding-observable-extension | 20 | **0** | five mpf truncated by `float()` at the dict write |
| binding-rotation-phase-lead | 12 | **0** | every spread computed in float64 (`float(rho[i])` then ratio) |
| chi-free-via-lr | 4 | **0** | four `wall_sec` wall-clock durations, undeclared name |

No baseline touched. `raw-float64-baseline.json` is unchanged, there is no
`--rebaseline` on the branch, every fix is at the producer.

### The one that was not a precision defect

`chi-free-via-lr`'s four fields are `time.time() - t0`. The ratchet already
excuses durations, but **by name** against a closed six-name vocabulary
filtered out of `qou_substrate.witness._EPHEMERAL_META_FIELDS` — and
`wall_sec` is in neither the mask nor the `/dur|elapsed/` filter.

Fixed by renaming the producer's field to `elapsed_sec`, which IS declared.
**Deliberately did NOT widen the mask**: `witness_raw_float64_audit.py:216`
names `wall_sec` as exactly the case that fails SILENTLY under a one-sided
edit, and `qou-ywee` / `qou-hhm3` scope the widening as a wider change owned
by the declaring module. ~411 timing-shaped fields under ~65 undeclared
names remain; that is `qou-ywee`'s follow-up, untouched here.

### A SEPARATE finding the re-run exposed — `binding-rotation-phase-lead` was STALE

Established by running the **unmodified** producer from HEAD first: it
reproduces the new numbers exactly, so this is not caused by the float fix.

| field | committed | live inputs |
|---|---|---|
| S1_unweighted.spread_pct | 528.44 | 1283.29 |
| S2_dim.spread_pct | 17254.06 | 402.26 |
| S3_markov.spread_pct | 417.02 | 2303.18 |
| **tightest** | **S3_markov (417%)** | **S2_dim (402%)** |

The probe's own headline — which aggregation gives the tightest constant
binding scale — names a different aggregation than the committed witness.

**Localised to the ⁴He leg**, and the evidence is that everything else is
byte-identical: all four `A3_pair_spread_pct` (T,³He only) and both
`DTHe3_spread_*` (D/T/³He only) reproduce to the last digit. Only the full
spreads, the ones including ⁴He, moved.

Cause, to the commit: `atom-chi-rust-4he.witness.json` regenerated at
`8e52020e64` (2026-09-07 13:11) while this witness was last written at
`500e283706` (2026-09-07 11:51) — 80 minutes earlier, same day, **both under
bean `qou-k54t`**. The input was refreshed and this downstream consumer was
not re-run. Import-cone drift (`qou-e9pp` class); a file-local `git diff` on
the producer cannot see it.

### Latent bug fixed on the way

`best = min(..., key=lambda a: results[a]["spread_pct"])`. Once that field
is a serialized string, `min` is **lexicographic**: `"17254.05…"` sorts
before `"417.02…"`, so the string key would have named the WORST aggregation
as the tightest. Ordering now runs on a separate `spread_mpf` dict.

### Did NOT trade one gate for the other

The `qou-3jwy` failure mode (a float64 drain that pushes the padding ratchet
up) was checked explicitly: **zero** of the three witnesses appear anywhere
in `witness_float64_padding_audit.py --strict` output.

`scripts/precision-gates.sh --changed` is RED on ten gates — q0-anchor flip,
q0-anchor refill, import-time dps, never-raises-dps, float64-padding,
reference-literal, witness-value copy, q0-value drift, CODATA stale-edition,
mixed mpf/f64. **None is attributable to this branch**, checked file by file
rather than assumed:

- `witness-provenance-audit`: all three **PROV_OK**.
- `q0-anchor-consistency-audit`: `bar-pairing` **Q0_OK**; the other two
  **Q0_ANCHOR_MISSING** — and the *committed* versions carry no q0 key
  either, so it is pre-existing, not introduced.
- `q0-value-drift-audit`: one row, `bar-pairing`, class `proton-pin`,
  `-11.614 ppb vs canonical` — that IS the μ–p substrate tension, the
  correct reading for a proton pin, and the `q0Value` string is unchanged
  from the committed witness.
- padding / value-copy / codata / never-raises / mixed-arithmetic: **zero**
  hits on any of the three stems.

Contended tree-measuring audit witnesses were reverted per the script's own
instruction (`qou-v0t8`).
