---
# qou-veu1
title: Regenerating a witness can DROP its q0Anchor stamp, removing it from the audit's scope
status: todo
type: task
priority: normal
created_at: 2026-08-23T13:44:57Z
updated_at: 2026-08-23T14:05:30Z
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

## Cross-link: `qou-khmj` on main found the same mechanism from the other side

Filed independently at 13:14Z (`df9e1f3a95`), while this sweep was running:

> `gen_q0_anchor_manifest.py` does not detect three proton-pinned producers …
> All three import `Q_MP`/`Q_50_DIGIT_STR` from `q_parameter` (so NOT
> independent), but the generator omits them, so their witnesses ship with no
> `q0Anchor` and land in `Q0_ANCHOR_MISSING`. **Fix the generator's detection,
> not the manifest by hand.**

That supplies the cause this bean declined to assert: the omission is a
**detection gap in the manifest generator**, not a deliberate exclusion. And
its closing instruction is the right fix here too — hand-adding entries would
paper over a generator that will keep omitting the next producer.

## The two are NOT the same symptom, and the difference is the severity

| | `qou-khmj` | this bean |
|---|---|---|
| committed witness | **never had** `q0Anchor` | **has** `q0Anchor: "muon"` |
| audit state today | `Q0_ANCHOR_MISSING` — already visible as a gap | counted as muon-anchored, in scope |
| effect of regenerating | none; still missing | **loses a stamp it currently has** |

khmj's three are *already* outside the anchored population and are counted as
such. Mine is inside it and would silently leave — the audit's denominator
shrinks, and a `Q0_FLIP` disappears without being fixed. A gap you can see is
a smaller problem than one that closes itself while you watch.

This also settles why the committed witness has a stamp at all: it was written
when detection covered that producer, or with an anchor passed explicitly.
Either way the record and the current generator now disagree, which is the
thing to fix before #5500 regenerates anything.
