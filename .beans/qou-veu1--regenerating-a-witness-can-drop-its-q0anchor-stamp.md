---
# qou-veu1
title: Regenerating a witness can DROP its q0Anchor stamp, removing it from the audit's scope
status: todo
type: task
priority: normal
created_at: 2026-08-23T13:44:57Z
updated_at: 2026-08-23T13:45:29Z
---

## The measurement

The staleness sweep now records *which* fields move on a SUBSTANTIVE verdict.
The first one it measured, `cyclic_intertwiner_verify.py`, reports:

```
allPassed
assertions.0.computed
assertions.0.passed
data.h6_all_lambda6.max_abs_residual
data.q0
q0Anchor  (removed)
q0Value   (removed)
scriptHash
```

The committed witness carries `q0Anchor: "muon"` and
`q0Value: "1.10997859555733471989…"`. **The re-run emits neither.**

## Why this is load-bearing for #5500

The muon-anchored set is *defined* by those two fields — both the sweep's
target list and `q0_anchor_consistency_audit`'s scope. So for any witness that
behaves this way, regenerating it does not fix its `Q0_FLIP`; it removes the
witness from the audited population. The audit moves toward green because the
flagged witnesses **stopped declaring an anchor**, not because their anchors
were corrected. #5500's plan is "regenerate all 53", so the size of this class
decides whether that plan measures what it intends to.

## A hypothesis I formed and then refuted — do not repeat it

`witness.py` resolves the anchor by looking the producer's stem up in
`computations/q0_anchor_manifest.json`. **41 of the 55** in-scope producers are
absent from that manifest, which looks like an immediate explanation and a
count.

It is not, and the count is wrong. `q0_anchor_consistency_audit.py` is **also**
absent from the manifest and came back `UNCHANGED` — so it retained its stamp.
Manifest absence is therefore **not sufficient** to cause the drop (a producer
may pass an explicit anchor to `w.save()`, per `witness.py:1352`). Anyone
quoting "41 witnesses will lose their anchor" is quoting a refuted inference.

## How the real number gets established

Not by reasoning about the manifest — by the sweep. `changed_fields` now
records `q0Anchor (removed)` wherever it happens, so the count falls out of the
run in progress. Wait for it rather than estimating it.

## Then

For each producer that does drop the stamp, the fix is at the producer or its
manifest entry — restore the stamp **before** regenerating, so the regenerated
witness stays inside the audit rather than leaving it.
