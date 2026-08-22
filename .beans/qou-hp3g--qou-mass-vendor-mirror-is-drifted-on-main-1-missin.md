---
# qou-hp3g
title: qou-mass vendor mirror is drifted on main — 1 missing + 9 drifted, sources moved 2-4 days ago
status: completed
type: task
priority: normal
created_at: 2026-08-21T15:42:00Z
updated_at: 2026-08-21T21:44:12Z
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



---

## CORRECTION 2026-08-21 — the title was wrong, and the real defect is elsewhere

**"drifted on main" was my error.** I measured on my own branch at
`8ba73cc915a` and reported it as a state of `main`. It was not:

    8ba73cc915a  2026-08-19 21:20:57   (my branch commit)
    e4906af5a4c  2026-08-19 21:31:30   chore(vendor): regenerate the mirror

`git merge-base --is-ancestor e4906af5a4c 8ba73cc915a` → **false**. My tree
predated the fix by **eleven minutes**; a sibling arc regenerated the mirror
while I was measuring a stale checkout. On current main `--check` exits **0**.

Verified the detector still works rather than trusting exit 0: clean → planted
one line into the vendored `_precision.py` → `exit 1, DRIFTED (1): _precision`
→ restored → clean. The gate fires.

## But the gate only covers HALF the mirror

`--check`/`--apply` iterate `cone` and compare `VENDOR / f"{mod}.py"`
(script line ~255). **Only Python modules.** It prints
`vendored copies are in sync (42 modules)` while **157 `*.witness.json` files
under `qou-mass/src` are compared to nothing.** All 157 are tracked and
committed. `required_witnesses()` already exists (line 195) and computes
exactly which witnesses the vendored modules load at runtime — but its result
feeds a reporting path, not the comparison.

Same shape as the defects this session has been draining: **a gate that reports
success without examining the thing that drifted.**

## What the unchecked half actually contains

Measured against same-named twins under `computations/` (157/157 have one):

| | count |
|---|---|
| identical raw-float64 count | 34 |
| differing | 123 |
| **mirror dirtier than source** | **17** |
| **mirror/source disagree on q₀ pin** | **122** |

The float64 half is NOT the sync introducing error — it is staleness.
`canonical-mass-table-extended.witness.json`: mirror frozen at `1af7d4b7a04`
(2026-08-15, "qou-mass v1.0.0"), source at `da2968cc335` (2026-08-19,
"migration: first witnesses at the proton pin"). Source 0 float64, mirror 33.

**The q₀ half is the serious one.** That same file is **proton at source and
muon in the mirror** — the canonical mass table, in the facade package, at the
anchor the 2026-08-07 owner directive superseded (reaffirmed as R2 on
2026-08-15).

## Blast radius — stated narrowly, on purpose

`qou-mass` is **not published** (AGENTS.md: 404 on PyPI, no `dist/`, no
publish step). There are **no external consumers** and this must not be
described as shipping wrong numbers to researchers. The exposure is the **5
in-repo importers**.

## Status

Sync-drift half: **resolved by e4906af5a4c**, not by me.
Unchecked-data half: **open**, and is the actual work. Split to its own bean.
