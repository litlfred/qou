---
# qou-w9s3
title: 'Unrun audit: witness_provenance_audit (top-level) works, is wired nowhere, and finds 7 real defects'
status: todo
type: task
created_at: 2026-08-15T23:24:47Z
updated_at: 2026-08-15T23:24:47Z
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
