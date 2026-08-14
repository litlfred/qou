---
# qou-n7mj
title: 3 live probes import probe_staircase_ew_k3_categorical from _deprecated/
status: todo
type: task
created_at: 2026-08-10T14:15:16Z
updated_at: 2026-08-10T14:15:16Z
---


## What was found

Surfaced as an `exit1` in the `qou-eea0` pass-2 regeneration run (PR #4928):

```
File "computations/probes/q_hecke_seminormal_character_closure_probe.py"
    from probe_staircase_ew_k3_categorical import build_hoefsmit_mpfr
ModuleNotFoundError: No module named 'probe_staircase_ew_k3_categorical'
```

The module exists — at **`_deprecated/probes/probe_staircase_ew_k3_categorical.py`**,
top-level, not under `computations/`. Three *live* probes import
`build_hoefsmit_mpfr` from it, at module scope, so each fails at import:

| live probe | line |
|---|---|
| `computations/probes/q_hecke_seminormal_character_closure_probe.py` | 40 |
| `computations/probes/knot_factor_borromean_composite_probe.py` | 50 |
| `computations/probes/knot_factor_amphicheiral_BD_probe.py` | 56 |

## Why this is the same defect class as qou-rohl

`qou-rohl` is a witness whose producer was retired; this is a producer whose
*dependency* was retired. Both are a deprecation carried out without following
the consumers, and both are invisible until something actually executes the
downstream file — which, for probes nothing runs routinely, is close to never.

`build_hoefsmit_mpfr` is not incidental: it builds the Hoefsmit
representation at MPFR precision, which is the numerical core of all three
probes. So this is not a stale import that can simply be deleted.

## Do not "fix" by widening sys.path

Adding `_deprecated/probes` to the harness `SYS_PATHS`, or to the probes' own
`sys.path.insert` preamble, would make the error disappear while leaving live
compute running on deliberately-retired code. That is laundering, and the
regeneration harness explicitly refuses `_deprecated/` as a producer
resolution for the same reason.

## Options

1. **Un-deprecate the module** into `computations/probes/` (or a shared
   `computations/hecke/` home) if `build_hoefsmit_mpfr` is still canonical.
   Cheapest, but only correct if the deprecation was of the *probe*, not of
   the construction.
2. **Repoint the three probes** at whatever superseded it —
   `pyhecke`/`pyhecke_native` expose Hoefsmit builders, and if one of those is
   the replacement then the import is simply stale.
3. **Deprecate the three probes too**, if the retirement was intentional and
   they were meant to follow.

Answering *why* the module was deprecated decides between these; the git
history of the move is the place to start.

## Close condition

The three probes either import from a live module or are themselves retired.
Not closed by making the import resolve to `_deprecated/`.
