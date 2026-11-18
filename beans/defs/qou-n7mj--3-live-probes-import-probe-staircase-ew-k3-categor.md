---
# qou-n7mj
title: 3 live probes import probe_staircase_ew_k3_categorical from _deprecated/
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T14:15:16Z
updated_at: 2026-10-04T15:16:03Z
parent: qou-trd0
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


## Re-measured 2026-08-19 — it is 11 producers, not 3, and a second module

Measured with `computations/audits/producer_importability_audit.py` (imports
every witness-emitting producer in a subprocess) after draining the
sys.path class of failures around it. The count in the title understates it:

| missing module | live producers |
|---|---|
| `probe_staircase_ew_k3_categorical` | **10** |
| `lambda_scale_alt_g_skein_polynomial_direct` | **1** |

The ten:

```
computations/probes/hecke_1d_irrep_closed_form_character_probe.py
computations/probes/hecke_branching_trace_decomposition_probe.py
computations/probes/hecke_markov_transition_probe.py
computations/probes/hoefsmit_seminormal_form_probe.py
computations/probes/knot_factor_amphicheiral_BD_probe.py
computations/probes/knot_factor_borromean_composite_probe.py
computations/probes/pauli_factor_wedderburn_probe.py
computations/probes/q_hecke_seminormal_character_closure_probe.py
computations/probes/symbolic_character_table_probe.py
computations/probes/three_parameters_wedderburn_probe.py
```

The eleventh is `computations/probes/lambda_scale_homflypt_skein_recursion_probe.py`,
importing `lambda_scale_alt_g_skein_polynomial_direct` — same shape, same
cause: `_deprecated/strategy-spikes/lambda_scale_alt_g_skein_polynomial_direct.py`,
untracked by the same commit `0763606e4`.

Both modules are confirmed gone from the working tree, and
`git log --diff-filter=D` names `0763606e4 chore: untrack the five root-level
agent-scratch dirs (2,344 files)` as the deletion for each.

**These 11 are now the entire residual `in-repo-wiring` backlog.** The rest of
that class — 72 producers when first measured — was sys.path wiring and is
drained on `claude/convention-d-tranche-2026-08-18` (`a6e5c4496`, `b048328fe`,
`e9324f29f`): 72 -> 40 by wiring `tools/pyhecke` into `_path_bridge`, 40 -> 15
by bootstrapping 25 producers, 15 -> 11 by four targeted fixes. Nothing left in
the class is reachable by a path entry, so this bean is the whole remainder and
needs the real decision: restore the two modules to a live location, or retire
the 11 producers and their witnesses.

Note the audit itself excludes `_deprecated/`, so it can see the broken
importers but never the modules they want — the dependency crosses a boundary
the tooling deliberately does not.
