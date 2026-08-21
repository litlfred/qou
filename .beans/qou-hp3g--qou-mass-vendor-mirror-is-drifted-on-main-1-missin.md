---
# qou-hp3g
title: qou-mass vendor mirror is drifted on main — 1 missing + 9 drifted, sources moved 2-4 days ago
status: todo
type: task
created_at: 2026-08-21T15:42:00Z
updated_at: 2026-08-21T15:42:00Z
---


## Measured on main @ 8ba73cc915a, 2026-08-21

`python3 scripts/sync-qou-mass-vendor.py --check` **exits 1**:

    MISSING from qou-mass/src/qou_mass/_internal (1):
      data/hecke-character-symbolic.witness.json
    DRIFTED from source (9):
      data/atomic-tr-m-mpfr-50dps.witness.json
      _li_2_q_util, _precision, canonical_braid_crossings, codata_constants,
      hecke_character_symbolic, markov_peel, markov_trace_canonical,
      wedderburn_jones_markov

## It is plain staleness, not a hand-edit conflict

The mirror was last regenerated **2026-08-14**; its sources have moved since:

| module | source | source last changed | mirror last changed |
|---|---|---|---|
| `_precision` | `computations/substrate/_precision.py` | **2026-08-18** | 2026-08-14 |
| `markov_peel` | `computations/markov/markov_peel.py` | **2026-08-16** | 2026-08-14 |
| `codata_constants` | `computations/substrate/codata_constants.py` | **2026-08-16** | 2026-08-14 |

So nobody hand-edited `_internal/`; the sources simply advanced and `--apply`
was not re-run. That makes the fix mechanical and low-risk — `--apply`
regenerates FROM `computations/`, so it cannot clobber a source of truth, and
AGENTS.md already forbids hand-editing the mirror.

## Why it matters more than a stale copy usually would

AGENTS.md records that this mirror drifted before, that **all 14 copies had
drifted**, and — the part that matters — that the drift **masked a live
defect**: `test_ephemeral_mask_sync` exists to detect mirror divergence and was
green only because the mirror was stale. A stale mirror here does not merely
lag; it can silence the test written to catch it.

Two of the ten drifted entries are `*.witness.json`, so this is also a
NO-FLOAT64-adjacent surface: `qou-mass/src` holds **156** witnesses that the
raw-float64 ratchet does not scan (its root is `computations/`), and 124 of the
150 with same-named twins there differ from those twins.

## Fix

    python3 scripts/sync-qou-mass-vendor.py --apply

then `--check` to confirm exit 0. Not done here: this is a different package
from the arc in flight (qou-irzg), the diff spans ~10 generated files, and no
one directed it. Cheap for whoever owns it.

## A measurement trap, recorded because it nearly became a false report

I first read this gate as "detects drift but exits 0" — which would have made
it a broken gate of exactly the class this session has been fixing. It was my
error: `cmd | tail; echo $?` reports **`tail`'s** status, not the command's.
Re-measured without the pipe, `--check` correctly exits **1**. Same shape as
the `pgrep -f` self-match trap in qou-9br4: the monitoring construct lied, not
the thing being monitored. Check the exit code of the process you mean.
