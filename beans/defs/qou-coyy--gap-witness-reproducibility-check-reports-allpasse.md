---
# qou-coyy
title: 'GAP: witness-reproducibility-check reports allPassed true while recording 4 drifting builders'
status: in-progress
pr: 8350
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T14:28:41Z
updated_at: 2026-10-04T15:20:34Z
parent: qou-5vkl
---

Found while draining `qou-srvu` slice C. LEFT in the baseline deliberately —
this one is not a witness that has nothing to say, it is a witness whose own
recorded data says the check FAILED while it reports green.

## The finding

`computations/witness-reproducibility-check.witness.json` reports

    allPassed: true
    assertions: []          <- none
    data.by_status:  {"pass": 5, "drift": 4, "skip": 2}
    data.pass_ratio: 0.5555555555555556

`drift` is this checker's word for **the builder is non-deterministic**: its
docstring says it will *"snapshot the on-disk output, re-run the builder, and
assert the new output is byte-equal to the snapshot"*. It never calls
`add_assertion`, so `all([])` makes the witness green over four recorded
failures. Of every vacuous-green entry I triaged, this is the one where the
green claim is most actively misleading — not "nothing was checked" but
"something was checked, it failed, and the verdict says pass".

## The four drifting builders

    drift  build_markov_trace_assembly_deuteron_chain.py
    drift  build_markov_trace_assembly_neutron_chain.py
    drift  build_proton_mass_50dps_chain.py
    drift  build_q0_anchor_chain.py
    skip   build_neutron_mass_50dps_chain.py
    skip   braid_encoding_audit.py

`build_q0_anchor_chain.py` is the q0 anchor chain builder. A non-deterministic
builder for a `*.derivation.json` that is committed and consumed downstream is
exactly the failure the docstring says the check exists to catch:

> *"A non-deterministic builder silently rewrites them on every CI run,
> polluting diffs and making git-blame meaningless."*

The witness is also **stale**: `computedAt: 2026-07-07T13:58:23Z`, so the four
drift verdicts are nearly two months old and may have grown or shrunk.

## Why I did not drain it

Adding the honest assertion (`drift == 0`) would make the witness report
`allPassed: false`. That is the truthful state, but two things stop a drain
agent doing it unilaterally:

1. **It lands a RED witness on `main`.** `scripts/check-computation-status.py
   --strict-unbacked` (bean `qou-vfy1`) gates what a paper CLAIMS on
   `allPassed`, and about a dozen producers hand-roll
   `return 0 if wit["allPassed"] else 1`. Flipping this one to false is a
   deliberate act with consumers, not witness hygiene.
2. **Re-running it executes eleven other builders.** Each has a 600 s timeout
   and writes its own `*.derivation.json`. The checker auto-restores, but that
   is a large blast radius spanning other agents' slices, and the `qou-srvu`
   partition rule is that a producer touching witnesses outside your slice is
   not yours to re-run.

## What closing this looks like

Either fix the four builders' non-determinism (the docstring names the usual
causes: dict-iteration order, embedded timestamps, float-precision drift,
PYTHONHASHSEED) and then add the assertion so it lands green — or add the
assertion first, accept a red witness, and treat it as the tracking signal.
That is an owner-or-coordinator call, not an agent one, because it changes
what a gate reads.

Either way the assertion to add is:

    reproducibility_no_builder_drifts
      computed = by_status.get("drift", 0)
      expected = 0
      guarded on len(registry) > 0

Re-measure first: the recorded verdicts are from 2026-07-07.


## Round 57 Implementation (PR #8350)
- Implemented on branch `claude/round57-trd0-9nnz-fixes` (commit `35175f892e4827e826a23a3d007073dd800ff733`, https://github.com/litlfred/qou/pull/8350).
