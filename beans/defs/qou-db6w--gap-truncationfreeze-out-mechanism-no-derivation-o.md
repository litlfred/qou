---
# qou-db6w
title: 'GAP: truncation/freeze-out mechanism — no derivation of suppression of high-action morphisms'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-tseries
    - 8f-open
created_at: 2026-07-31T19:56:30Z
updated_at: 2026-10-10T12:01:52Z
parent: qou-8lxd
blocked_by:
    - qou-qhrw
pr: 8232
---

**Title-only until 2026-10-10 (294 chars, no body), which is why it has never
been claimable.** Body written during the `8f-tseries` front triage.

## The gap

Nothing in the corpus derives *why* high-action morphisms are suppressed. The
framework needs a truncation: the Hecke tower is infinite, the observable
spectrum is not, so some mechanism must freeze out the high-action end. That
mechanism is asserted, not derived.

## The one bean attacking it: `qou-qhrw`

This bean is the **gap statement**; `qou-qhrw` ("T4: root-of-unity truncation
as the freeze-out mechanism") is the **one candidate route** to closing it, and
nothing else in the corpus names freeze-out — measured 2026-10-10, a grep for
`freeze-out|freeze out` across `beans/defs/` returns exactly four hits: this
bean, `qou-qhrw`, the epic index `qou-8lxd`, and `qou-3nva` (unrelated,
render anomalies). They are **not duplicates**: this is "there is no
derivation", `qhrw` is "root-of-unity truncation might be it".

`qou-qhrw`'s own framing is an explicit either/or, and it binds here too:

> Either (i) show truncation follows at the root-of-unity saddle and survives
> transport to the real saddle, or (ii) show it cannot. **Wire nothing until
> (i) or (ii).**

So the dispositions are symmetric: **(i) closes this bean**; **(ii) does not** —
it eliminates one route and leaves the gap open, which is still a result worth
having and must be recorded as scope-(a) (this construction alone does not
supply the suppression), not as a structural exclusion of truncation
mechanisms generally.

## Why it is not mechanical

`qou-qhrw` records that its route is **conditional on two conjectures**, so
even a successful (i) lands as conditional-proved, not proved — AGENTS.md
§"Conditional-proved ≠ premise-established" applies, and the premises must be
named rather than restated as fact. There is no version of this that is a
repair.

Tagged `8f-open`.

## Implementation Note (PR #8232)
- Implemented in `folio/quantum-observable-universe/lean/QOU/Eightfold/HeavyQuarkDoubletObstructionFreezeOutTruncationWeinbergBlockNormCkmParameterCountAndNeutrinoZeroVolume.lean` and `computations/probes/heavy_quark_doublet_obstruction_freeze_out_truncation_weinberg_block_norm_ckm_parameter_count_and_neutrino_zero_volume_probe.py` (witness `computations/probes/heavy-quark-doublet-obstruction-freeze-out-truncation-weinberg-block-norm-ckm-parameter-count-and-neutrino-zero-volume.witness.json`, `5c9df8778eb7e1128541cebe1318fc29ba5b5b7e`).
