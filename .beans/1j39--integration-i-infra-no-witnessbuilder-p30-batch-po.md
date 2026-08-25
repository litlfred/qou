---
# 1j39
title: 'Integration: I-infra-no-witnessbuilder-P30 batch port'
status: todo
type: task
priority: normal
created_at: 2026-06-21T21:41:08Z
updated_at: 2026-08-25T21:15:53Z
---

## DUPLICATE of `cmiy` — DEFERRED (dedup 2026-06-28)

This bean and `cmiy` ("canonical watcher - P30 WitnessBuilder rollup") are
the **same work** (the P30 WitnessBuilder port, ~133 scripts). **`cmiy` is
the canonical bean**; see its body for the deferral rationale (high collision
with the active compute-PR storm — `/coordinate` 2026-06-28). Owner-close
this duplicate when convenient (resolve is human-only).

> **Investigated 2026-07-05 (swarm 2, PR #3344) — DUPLICATE of cmiy; kept OPEN pending owner close.** Same P30 WitnessBuilder scope; compute-blocked.


## 2026-08-25 — MEASURED: this is the only unstamped class regeneration cannot fix

Found while retracting a wrong recommendation on `qou-1c4y` (see its
2026-08-25-later entry). Relevant to this bean's scope:

`WitnessBuilder.build()` has called `resolve_q0_anchor_payload_first` since
`9d52483f5` (on `main` 2026-08-25T10:20 UTC), and it always sets `q0Anchor`.
So every WitnessBuilder producer stamps itself on its next run — the ~157
unstamped-but-single-pin witnesses in the corpus are simply stale and will
resolve on regeneration.

**Hand-rolled `json.dump` producers never reach `build()`, so they never
stamp — and re-running them never will.** Measured instance: four witnesses
computed 16:52 UTC / committed 16:54 (`58db04f28`), 6.5 h after the fix was on
`main`, all four unstamped. I verified that commit's own tree carried the fix
rather than assuming it, so this is not a dating artifact:

    computations/qbeta/birkhoff_barodd_pythagoras_bridge_probe.py
    computations/deltalambda/deuteron_interface_handle_curvature_probe.py
    computations/deltalambda/yekutieli_trefoil_surface2form_discretization_probe.py
    computations/qbeta/a3_branching_asymmetry_vs_required_probe.py

Each carries a single muon pin under a key `_Q0_FIELDS` already knows, at depth
≤ 3 — i.e. everything the resolver needs is present in the payload, and nothing
consults it. Porting these four to `WitnessBuilder` stamps them with no change
to any number.

This gives the port a second, sharper justification beyond consistency: it is
the difference between a witness that becomes verifiable on its next run and
one that stays unverifiable permanently.
