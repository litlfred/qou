---
# qou-pin6
title: 'pentagon_reduction_li2q witness is stale by 5 ORDERS OF MAGNITUDE on T1_atom — unrelated to q0, held out of the load_q_50dps migration'
status: todo
type: task
priority: normal
created_at: 2026-08-08T23:10:00Z
updated_at: 2026-08-08T23:10:00Z
---

Held out of the 2026-08-08 `load_q_50dps` default-flip migration, deliberately,
after the value audit caught it. Same discipline as `qou-pin3`: an anchor
migration is bookkeeping, and a substantive change must not ride in on one.

## What the audit saw

`pentagon_reduction_li2q` is one of the 15 producers whose q₀ moved when
`_li_2_q_util.load_q_50dps()`'s default flipped from the muon pinning witness to
the caller's own resolved pin. Regenerating it moved 18 fields by far more than
an 11.5 ppb q₀ shift can produce — `T1_atom` by **five orders of magnitude**:

    atom   committed        regenerated
    D      4.5283072561     0.0000305810737
    T      2.4610392279     0.0000019192797
    3He    1.4866054031     0.0000022644584

`ratio_pred_over_AME` and `B_MeV_first_plus_T3` move with it (up to 5.0e-02).

## Why it is NOT the q₀ flip — a three-way run, not an inference

Ran the producer under BOTH arms in the same container:

    arm A   pre-flip  `_li_2_q_util.py` + `q0_anchor_manifest.json` from HEAD
    arm B   post-flip working-tree versions

    atom | committed        | arm A (pre-flip)   | arm B (post-flip)
    D    | 4.5283072561032  | 0.0000305810737085 | 0.0000305810737085
    T    | 2.4610392278924  | 0.0000019192796920 | 0.0000019192796920
    3He  | 1.4866054030558  | 0.0000022644583563 | 0.0000022644583563

Arms A and B are **bit-identical**. Both differ from the committed witness by
5 orders. So the flip contributes nothing here (its own A/B delta is 1.154e-08,
exactly the layer separation) — the producer's `T1` computation changed at some
point and the witness was never regenerated.

This is why the audit compares run-vs-run and not committed-vs-run: diffing
against a committed witness measures the change under test **plus** whatever
staleness the file already carried, and attributes all of it to the change.

## Next step

Find the commit that changed `T1_atom`'s definition and decide whether the
current code or the committed witness is right — a 5-order move in a per-atom
tower term is either a real correction or a real regression, and it is not
knowable from the witness alone. `git log -p --follow computations/pentagon_reduction_li2q.py`
over the T1 block is the place to start.

Only then regenerate, as its own change with its own justification.

## Held out mechanically, not by memory

`computations/audits/load_q_50dps_flip_regenerate.py` carries
`HOLD_OUT = {"pentagon_reduction_li2q"}` with this evidence inline, and the
hold-out gates both `--apply` and `--audit-only`. Re-running the migration will
not silently pick it back up.


## SECOND INSTANCE 2026-08-08 — `probe_9b_gate_interface_algebra`

Found the same way, during the UNDETERMINED-pin triage. Its witness records
`muon` while the code resolves proton (tnjb class), so it was a declaration
candidate — but regenerating it flips `allPassed` True → False on two
assertions, both **cross-witness comparisons**:

    structural_constants_match_probe1     0.0      -> 7.330992e-07  (tol 1e-09)
    m3_residuals_match_hpower_witness     5.82e-15 -> 2.894e-06     (tol 1e-09)

**Proven pre-existing, not caused by the 2026-08-08 anchor work.** Ran the
producer from a `git worktree` at the base commit `d8d22890` — before any of
that day's changes — and it emits **bit-identical** failing values. So the
committed witness is stale and the producer has been unable to reproduce it
since before this branch existed.

Not declared, deliberately. Declaring it would convert an UNDETERMINED pin into
a **DECL_MISMATCH**, which is worse: the declaration only pays off once the
witness matches, and it cannot be regenerated without committing an assertion
failure.

Next step is the same shape as pentagon's: find what moved
`structural_constants_match_probe1` away from its comparison target, decide
whether the current code or the committed witness is right, then regenerate as
its own change. Both comparison targets are other witnesses, so the answer may
be that one of THEM is the stale side.

Held out mechanically in `computations/audits/q0_undetermined_triage.py`
(`HOLD_OUT`), with this evidence inline.
