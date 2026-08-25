---
# qou-hqjf
title: binding-family producers crashed on mpf JSON serialization (magic-A / Kashaev / alpha-cluster / b-over-a)
status: completed
type: bug
priority: normal
created_at: 2026-08-15T23:41:50Z
updated_at: 2026-08-15T23:42:35Z
---

## What broke

Four producers exited rc=1 with `TypeError: Object of type mpf is not JSON
serializable`:

    computations/magic_A_formula.py
    computations/family_1_kashaev.py
    computations/alpha/alpha_cluster_recursion.py
    computations/b_over_a_v5_unified.py

Verified PRE-EXISTING, not caused by the mass_table_ppb port (qou-3wqg): the
same failure reproduces in a worktree at `b393679b5~1`. Found while checking
consumers of the corrected ppb predictions on `claude/ppb-consumers-recheck`.

## Cause: a half-migration nobody ran into

`codata_constants.M_E_MEV` became an mpf. These modules kept importing knot
volumes through the back-compat f64 aliases in `knot_volumes.py` — whose own
comment names `magic_A_formula.py` and `alpha_cluster_recursion.py` as the
consumers those aliases were kept for. `m_e * Vol` then yielded an mpf that
`json.dumps` refuses, and nothing had executed these since the constants moved.

## Why `default=str` was the wrong fix

An mpf carrying ~16 honest digits, printed at OUTPUT_DPS, is float64 laundered
into a long decimal — the exact hazard the NO-FLOAT64 gates exist to catch. Each
producer instead took the migration `mass_table_ppb.py` already took: `_MPF`
volumes, mpf AME literals, `set_compute_dps()` at module scope BEFORE any
multiplication, and a `json.dumps(default=...)` hook routing mpf to
`_precision.fmt`.

## Side finding — a wrong knot volume, worth its own look

`family_1_kashaev.py` hardcoded `Vol(8_11) = 8.28631808635811`. The canonical
`knot_volumes` value is `8.2863168178065925881` (SnapPy HP 50-dps). They
disagree at the EIGHTH significant digit — not rounding. Every other 8_11 in the
repo already carries the canonical digits (`binding_link_volumes.py`,
`he4_vol4_prediction_test_probe.py`, `binding-a3plus-full-theta-assembly`, the
deltalambda witnesses), so this literal was the lone outlier.

Effect: tritium's family-1 B_pred moves -1.296e-6 MeV (-1.53e-7 relative).
err_pct vs AME is unchanged at every reported digit, so no conclusion moves.

OPEN: the comment in `family_1_kashaev.py` cites `binding_ladder_catalog.py:48`
and `d_inter_correction_test.py:57` as the source of these literals. Nobody has
checked whether the bad digits also sit in either of those, or whether some
older result was computed against 8.286318.

## Result

    raw-float64      NEW 0, REGRESSED 1 (rho-k only — qou-mnrd, needs >=24 GiB)
    never-raises     NEW 0, REGRESSED 0    (11 -> 10 producers, 44 -> 42)
    b-over-a-v5-unified          95 -> 0 raw float64
    alpha-cluster-recursion      47 -> 0
    canonical-mass-table-extended 24 -> 0

Also drained two structural constants written as floats: `rho_F` is a counting
prefactor (2, not 2.0) and `paper_hard_floor_ppb` is a declared threshold (780,
not 780.0).

`categorical_bypass_volmatch_demo.py` gained the `set_compute_dps()` it should
have had when I first lifted mass-table strings with `mp.mpf` last turn — the
never-raises gate flagged it as NEW, which is the gate working on my own change.

## Not done

`magic-A-formula.witness.json` and `family-1-kashaev.witness.json` are NOT
tracked. PR #554 moved both to `computations/_deprecated/` as dead-exploratory
and nothing consumes them; the `.py` files survive only because live code
imports their functions. Running either now leaves an untracked file. Reviving a
deliberately pruned witness is a separate decision, not mine to make in passing.

Fixed on `claude/ppb-consumers-recheck` @ 4d852e5d4.
