---
# qou-ff4b
title: 'lp-confinement-nf-forcing FAILS verify_dual_present: 6 records where active_set is empty but y_star has tight constraints'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-08T04:46:25Z
updated_at: 2026-11-16T20:10:00Z
parent: qou-trd0
---

Found 2026-09-08 while reading bean `qou-aze5` for the `qou-bstl` drain. Not a
new guard and not a proposal — the guard is already on `main` and this witness
already fails it.

## The failure, from the guard itself

```
$ PYTHONPATH=tools/pyhecke/python python3 -c "…verify_dual_present(…)"
lp-confinement-nf-forcing.witness.json
   ok: False | missing: []
   inconsistent: 6
     <root>.data.lp_dual_summary[0]: active_set is empty but y_star has 2
       nonzero entries at [1, 2] — the active set is by definition
       {i : y_star[i] > 0}
     …[1]: … nonzero at [1, 2]
     …[2]: … nonzero at [0, 2]
```

Six of the records under `data.lp_dual_summary[]`. `missing` is **empty** — this
is not a hollow dual. Every field is populated; the populated values contradict
each other. Sample `y_star` from record 0:
`[1.0602564630944876e-105, 1.1160262270833812, 0.420398699801…]` — entries of
order 1, so constraints 1 and 2 are genuinely tight, and `active_set` should be
`[1, 2]` rather than `[]`.

## Why it is worth its own bean

Three neighbouring beans touch this witness and **none of them covers this**:
`qou-ftuv` (raw float64 in LP-dual witnesses), `qou-lpio` (nine witnesses
carrying LP-dual field *names* with null values), `qou-augu` (thirteen
LP/SDP witnesses reporting a zero net). This is the opposite shape from
`qou-lpio`: nothing is null, the numbers disagree.

## What it contradicts, and this is the part to read

The guard was repaired under `qou-aze5` (`57db289fdff`), and the new test
`test_empty_active_set_with_zero_y_star_passes` carries this in its docstring:

> *"This is the case the corpus actually contains. Of 3096 witnesses, 14 carry
> an empty active set and ALL 14 pair it with an absent or all-zero `y_star`."*

**That was true when written and is not true now.** Re-measured 2026-09-08 over
**3702** tracked `computations/**/*.witness.json`, classifying every empty
`active_set` / `active_constraints` / `active_channels` by `max|y_star|`
against a 1e-9 tolerance:

| class | count | meaning |
|---|---|---|
| **A** `y_star` present, `max|y*| < 1e-9` | **10** | genuine interior optimum — the carve-out is real (1.08e-46 … 6.70e-14, in `r5-full-canonical-knot-solver` and `e-0-lp-dual-h3`) |
| **B** `y_star` present, `max|y*| ≥ 1e-9` | **6** | **inconsistent — this bean**; all six in `lp-confinement-nf-forcing`, `max|y*| = 1.1160` |
| **C** no `y_star` at all | **36** | hollow; caught by the separate `y_star` hollowness check, verified `ok: True` is NOT returned for these by accident |
| | 248 | non-empty active sets (the ordinary case) |

So the corpus went from 14 empty sets, all benign, to **52, of which 6 are live
violations of the repaired guard**. The docstring figure is stale rather than
wrong-at-the-time, and it is the kind of stale that reads as an all-clear.

## What is NOT established

- **Which side is wrong** — whether `active_set` was computed with a threshold
  that excluded everything, or never populated while `y_star` was. That needs
  the producer (`lp_confinement_nf_forcing`), not the witness.
- **Whether it was ever right.** This clone is shallow, so a pickaxe search on
  the witness's history cannot distinguish "regressed" from "always was".
- **Whether re-running fixes it.** Not attempted here — the producer's cost is
  unmeasured and re-running is a change, not a measurement.

## Next honest step

Read `lp_confinement_nf_forcing`'s dual-emission path and decide whether the
active set is thresholded or unpopulated; fix at the producer and regenerate.
Do **not** widen the guard's tolerance to make this pass — the guard is correct
here and is the only thing that caught it.


## Round 48 Execution Update (2026-11-16, PR #8161)

- **PR:** https://github.com/litlfred/qou/pull/8161 (`38bc15fe7214bb6951d6acb18fa8c8d7d32d5225`)
- **Action taken:**
  - Confirmed root cause: `computations/lp-confinement-nf-forcing.witness.json` (diagonal `G`) was generated under the pre-2026-08-24 primal-slack rule in `_rescale_mpfr_result` (`|(Gx)_i| / sum_j |G_ij x_j| == 1` on diagonal `G`, returning `active_set = []` for all 6 rows despite `y_star` entries up to `1.2589`).
  - Updated `_finish` in `tools/pyhecke/python/pyhecke/lp_dual_solver.py` and `computations/lp_confinement_nf_forcing.py` to always derive `active_set` from `y_star` / `y0_star`, and updated all 6 records in `computations/lp-confinement-nf-forcing.witness.json` from their committed 167-bit `lp_y_star_str` / `lp_y0_star_str` (`active_set` `[1, 2]`, `[1, 2]`, `[0, 2]`, `[1, 2, 3, 4]`, `[1, 2, 3, 4]`, `[1, 2, 3, 4]`; `maximizer_in_active_set: true` on 6/6 compounds).
  - Added `--self-test` / `--selftest` to `computations/lp_confinement_nf_forcing.py` and regression test `test_lp_confinement_nf_forcing_witness_passes_verify_dual_present` in `tools/pyhecke/tests/test_lp_dual_null_hardening.py` (`9 passed`).
- **Status:** Kept `in-progress` pending PR #8161 merge and owner review.
