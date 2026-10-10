---
# qou-w9s3
title: 'Unrun audit: witness_provenance_audit (top-level) works, is wired nowhere, and finds 7 real defects'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T23:24:47Z
updated_at: 2026-10-04T15:25:18Z
---


## Not a forked script — two different audits sharing a filename

`qou-zuln` recorded `witness_provenance_audit.py` as one of 4 "diverged
forks". **That characterisation is wrong for this pair.** They differ by 760
lines because they are *different audits*:

| path | docstring | wired? | has witness? | script-qa sidecar? |
|---|---|---|---|---|
| `computations/audits/witness_provenance_audit.py` | "I14 audit — witness provenance completeness" | yes, referenced ×3 | yes | yes |
| `computations/witness_provenance_audit.py` | "Does a witness's `scriptFile` actually WRITE that witness?" | **no** | **no** | **no** |

The other three pairs in `qou-zuln` may or may not be true forks; this one is
not, and each should be checked individually rather than treated as a class.

## The top-level one WORKS, and finds real defects

Ran it. Exit 0, no witness written, and it ships `--strict` (exit 1),
`--self-test`, and `--list <verdict>`:

```
witness-provenance: 2348 witnesses carry a scriptFile claim
  WRITES           2312
  UNCONFIRMED        29
  NOT_A_PRODUCER      2
  SCRIPT_MISSING      5
```

**NOT_A_PRODUCER — confirmed by hand.** Both named scripts exist and contain
the string "witness" ZERO times, so they provably cannot write these:

- `computations/psl27-irrep-verification.witness.json` -> `psl27_irrep_verification.py`
- `computations/sigma-all-evaluator.witness.json` -> `sigma_all_evaluator.py`

Re-running the named producer regenerates nothing, while `run_pipeline`
treats the witness as current — exactly the failure the audit's own docstring
describes for six `chi-*` witnesses.

**SCRIPT_MISSING — 5, but at least 2 look like false positives.** Two name
non-Python producers, which is legitimate:

- `mu3-submodularity-vacuous-deuteron.witness.json` -> a `.lean` file
- `joint-tower-sdp-rust.witness.json` -> `joint_tower_sdp.rs`

The other three name `.py` files that are absent:
`phase_transition_sdp_derivation.py`, `qbeta_c3_faddeev_rogers_probe.py`,
`qbeta_w_odd_categorical_net_probe.py`.

## This is the qou-j6gb pattern again

`precision-gates.sh`'s GATES array carries this warning in its own comment:

> **A GATE OUTSIDE THIS ARRAY IS A GATE NOBODY RUNS.** (2026-08-10, bean
> qou-j6gb) `mpf_import_time_dps_audit.py` was written 2026-08-07, worked
> from the start, and was in no array — so nothing ran it. Its defect class
> then landed five more times. […] When you write a detector, wiring it here
> is the half that makes it a gate.

Same shape, second instance. And the class this one detects is precisely the
knot-volumes bug fixed in #5170 — a witness whose named producer does not
write it. **This audit would have caught it.**

## Recommendation: wire it ADVISORY, not blocking

It starts red (7 findings), and the GATES array's own note says a gate that
is red on arrival gets skipped, which is how a checker goes quiet. The
existing precedent is the `audits-tree raw-float64 (advisory)` entry: added
non-blocking, with the backlog named, to be flipped once drained.

Not wired here: siblings are actively editing that array right now (#5159
adds a fourth gate, #5124 adds two more), so a concurrent edit would collide.
Wire it after those land.

## Wired (advisory) — the hold condition cleared

Recorded as "not wired: #5159 and #5124 are editing that array". Re-checked:

- **#5159 merged** (22:10). Notably its own "deliberately not done" section
  describes the SAME output-path clobber bug, scoped out for its own PR — so
  four sessions hit that one independently tonight (this one, #5159, #5124,
  and #5141 which actually landed the fix).
- **#5124 still open, but does NOT touch `precision-gates.sh`** — its own
  precision-gates fix was superseded by #5141 and resolved `--theirs`, so the
  file dropped out of its diff (verified against its head: 32 files, none
  matching `precision-gates` or `witness_provenance`).

The hold was specifically about colliding on the GATES array. That risk is
gone, so the gate is wired here.

**Entry** (same terms as the `audits-tree raw-float64 (advisory)` precedent):

```
"witness scriptFile provenance (advisory)|computations/witness_provenance_audit.py|--strict|yes|no"
```

Verified: `bash -n` clean; appears in `--list` as non-blocking; a full run
puts it under `ADVISORY (not gating)` and the `RED:` line still names only
the pre-existing `raw-float64 ratchet`, so **this adds no new red**.
Self-test 27/27.

The four audit witnesses the run regenerated were reverted, not committed —
per §5.1, a witness written by a gate run is not automatically a refresh.

Flip to blocking once the 2 NOT_A_PRODUCER are drained and the `.lean`/`.rs`
false-positive class is handled.

## Drained 1 of 2 NOT_A_PRODUCER

**`psl27-irrep-verification` — FIXED.** The witness named
`psl27_irrep_verification.py` as its producer; the script computed all four
witnessed quantities (`GL3F2_mats`, `conj_classes`, `sum_d_sq`,
`irrep_dims`) and emitted nothing. Nothing else wrote it either — the only
file in the corpus mentioning that witness name was the audit. Wired the
emission through `WitnessBuilder.wrap_legacy`, so the `scriptFile` claim is
now true and the file is derived rather than hand-maintained.

Every label — `engine: "python-exact"`, each `source`, each `unit` — is
reproduced VERBATIM from the committed witness. My first attempt reworded
them (and downgraded `engine` to `"python"`); that was gratuitous churn
discarding the original author's wording, and it is reverted. The payload is
semantically identical; the only content additions are `precisionMetadata`
and `environment`, which `WitnessBuilder` stamps on everything it writes.
(The remaining textual diff is `ensure_ascii`: the committed file escaped
`₂`, the builder writes literal `₂`. Same string.)

**The shape guard caught a real defect in my wiring.** First run recorded
`durationMs 50 -> 0`, flagged as "the hallmark of a run that was interrupted
mid-write". Correct: this module does its whole computation at IMPORT (no
`main()`), so building the witness afterwards measured only the build. Fixed
by capturing `_T0 = time.monotonic()` at import and passing
`start_time=_T0` — `durationMs` is now 480 and the guard reports
`collapsed: 0`. Notably the honest fix was available; `--accept` would have
silenced a true signal.

**`sigma-all-evaluator` — NOT fixed, and should not be "fixed" by widening
the audit.** Its witness is a different artifact class:
`auditOnly: docs/audits/2026-05-03-frob-filter-evaluator-wired.md`, zero
assertions, and a hand-authored payload (reference table, precision
schedule, `pipeline_callers_updated` / `..._intentionally_unwired`). It also
carries `evaluator_module: computations/sigma_all_evaluator.py` — so it
already has a field for "the module this is about". Its `scriptFile` is
using that second meaning, while the corpus contract for `scriptFile` is
"the script that WRITES this". The script's `__main__` is a self-test
comparing closed form against a symbolic table; it does not produce this
payload and should not be made to.

Resolution is authorial, one of: drop `scriptFile` (the `evaluator_module`
field already carries the true relationship), or wire a real producer. I did
NOT make the audit skip `auditOnly` witnesses — that would suppress a true
finding by widening the checker, which is the move the precision discipline
exists to prevent.

Gate now reports 1 NOT_A_PRODUCER, not 2. Flip to blocking once this one and
the `.lean`/`.rs` SCRIPT_MISSING class are handled.

## SCRIPT_MISSING triaged: 2 false positives fixed, 3 real findings kept

I had guessed "at least 2 look like false positives". Checked rather than
assumed — searched the whole tree for each of the 5 named producers:

| named producer | exists? | verdict |
|---|---|---|
| `DeuteronFirstOrderCluster.lean` | `content/…/QOU/MassTheory/` | **false positive** |
| `joint_tower_sdp.rs` | `tools/hecke-engine/src/bin/` | **false positive** |
| `phase_transition_sdp_derivation.py` | nowhere | **real** |
| `qbeta_c3_faddeev_rogers_probe.py` | nowhere | **real** |
| `qbeta_w_odd_categorical_net_probe.py` | nowhere | **real** |

**Cause of the false positives is structural.** `scan()` indexes
`comp.rglob("*.py")` — Python only, under `computations/` only — so a `.rs`
or `.lean` producer can never resolve, and SCRIPT_MISSING fires *by
construction*. That verdict asserts "the claim cannot be true" about a script
sitting in the repo.

**Fix:** resolve non-Python producers by basename across the tree, and give
them **UNCONFIRMED, never WRITES**. `classify()` reads Python — WitnessBuilder
names, write sinks — so it can neither confirm nor deny a Rust or Lean
producer, and UNCONFIRMED is precisely the audit's documented middle verdict.
Claiming WRITES would be the laundering this tool exists to catch.

Result: SCRIPT_MISSING 5 -> 3, UNCONFIRMED 29 -> 31, NOT_A_PRODUCER
unchanged at 1, self-test still 27/27. **No true finding was suppressed** —
the 3 survivors are witnesses naming `.py` files that exist nowhere.

## Remaining before the gate can flip to blocking

1. **`sigma-all-evaluator`** (NOT_A_PRODUCER) — authorial; its `scriptFile`
   means "module documented" and it already carries `evaluator_module`.
2. **3 SCRIPT_MISSING** — each names an absent `.py`. Needs per-witness
   investigation: renamed, deleted, or never existed. Not mechanical.



## Reasons for Scrapping

Duplicate of `qou-7aum` (work-plan reorganisation 2026-10-04). Evidence: [B] unrun provenance audit wired nowhere - same gap as 7aum
Content is untouched; only this work item is closed.
