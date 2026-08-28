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

---

## 2026-08-28 — the 4 are ported; the CLASS is measured; `cmiy` still owns the full port

### What landed

The four named producers now stamp, via a new shared helper
[`computations/_witness_q0_stamp.py`](../computations/_witness_q0_stamp.py)
(`stamp_q0(payload, __file__)`, called immediately before `json.dump`). Each
witness gained **exactly two keys** and nothing else:

    + "q0Anchor": "muon"
    + "q0Value": "1.10997859555733471989976322048322502665620840878015368660798114614493"

All four resolve **muon** — a `qou-1c4y` datum in itself: these were invisible to
every anchor audit and belong to the population that migration has to move.
Measured after re-running all four: 16 insertions / 8 deletions across the four
witnesses, and **0** changed lines outside `computedAt` / `notes` / the two new
keys. Assertions still pass, exit 0 on all four.

### A stamp, deliberately, NOT the WitnessBuilder port

This bean proposes porting to `WitnessBuilder`; that is still the right end state
and is still `cmiy`. But a hand-rolled payload is an arbitrary dict, so the port
reshapes each witness file — a large per-file diff, 120 times. The stamp adds the
two provenance keys and touches nothing else, so it applies uniformly across the
class where the port does not. A stamped hand-rolled witness still lacks
`environment` / `scriptHash` / `commitSha` / `precisionMetadata`. **`cmiy` is not
discharged by this.**

### The class, measured on `main` (this is the number `cmiy` needs to size itself)

    witnesses carrying q0Anchor                          1103
    unstamped, no resolvable pin                         1897
    UNSTAMPED but carrying a resolvable pin at depth <=3  169
      -> attributed to a named producer                  124   (120 producers)
      -> UNATTRIBUTED, scriptFile null                     45   (cannot be ported)

Producers using `WitnessBuilder`: 1341. Hand-rolled `json.dump` with no builder:
251. Every one of the 169 is hand-rolled, confirming this bean's premise.

The **45 unattributed** are the harder half and are not addressable by either
route: with `scriptFile` null there is no producer to port or to re-run. They are
the "bare producers" class this bean's own earlier entry names.

### Two defects I introduced and caught before they shipped

1. **The helper stamped payloads with NO pin.** `resolve_q0_anchor_payload_first`
   consults the payload first but *falls back to the manifest/env* when there is
   no payload evidence — measured, `{"zzz": 1}` resolves to `("proton", <proton
   pin>)`. Right for `WitnessBuilder`, which knows what q₀ its producer was
   handed; **wrong** here, where it would assert a layer the numbers may not
   belong to, with a provenance field vouching for it — the exact straddle this
   work exists to expose, manufactured by the tool meant to reveal it. Fixed:
   `stamp_q0` now requires the payload to carry a recognisable pin at depth ≤ 3,
   and an unstampable witness stays visibly unstamped. Five-case self-check in
   the commit.
2. **A regex patch hit the wrong site.** My `out = … with open(out, "w")` anchor
   also matched a *local* `out` inside `surface2Form()` in the yekutieli probe,
   injecting `stamp_q0(witness, …)` where `witness` is undefined —
   `NameError`, caught by running it. Re-patched by hand against the witness
   *filename literal*. Confirmed against the pre-change file that the failure was
   mine, not pre-existing.

### Still true

This bean remains a DUPLICATE of `cmiy` and is still owner-close-when-convenient.
