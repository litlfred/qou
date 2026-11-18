---
# qou-veu1
title: Regenerating a witness can DROP its q0Anchor stamp, removing it from the audit's scope
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T13:44:57Z
updated_at: 2026-10-04T15:23:20Z
parent: qou-5vkl
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

## Count update at 32/55: five, not one

`q0Anchor (removed)` now appears in **5 of 19** SUBSTANTIVE results:

- `a_operator/cyclic_intertwiner_verify.py`
- `probe_9b_gate_interface_algebra.py`
- `probes/flavor_split_alpha_bond_dilog_probe.py`
- `probes/flavor_split_alpha_dilog_expansion_probe.py`
- `probes/trefoil_complex_volume_probe.py`

Roughly a quarter of the producers whose witnesses actually move also stop
declaring their anchor when re-run. Extrapolating to the full 55 would be
guessing, and the sweep will finish; the point already stands that this is a
class, not the single instance it looked like.

Note `flavor_split_alpha_bond_dilog_probe.py` is also one of the three paths
`qou-6q7q` found drifting against current `main` — it was migrated there by
`bc96793e5d` ("q0 literals: migrate the 5 unblocked sites"). So for that one,
re-measure after the rebase before concluding anything: the version measured
here is not the version on main, and a q0-literal migration is exactly the kind
of change that could either cause or cure the dropped stamp.

## Measured against the sibling's landed fix — 3 of 5 covered, 2 not

`qou-khmj` is **in-progress**, not idle, and its owner already landed
`8b4825920b` ("the producer lookup was root-only, so half the corpus was
invisible", #5550). The manifest grew **410 → 645** stems. So I am **not**
taking that work — it is mechanical, it has an owner, and duplicating it is
exactly what the one-owner rule forbids. What follows is measurement, offered
to them rather than a second attempt at their fix.

Checked the five droppers against `origin/main`'s post-fix manifest:

| producer | now listed |
|---|---|
| `cyclic_intertwiner_verify` | yes |
| `probe_9b_gate_interface_algebra` | yes |
| `trefoil_complex_volume_probe` | yes |
| `flavor_split_alpha_bond_dilog_probe` | no |
| `flavor_split_alpha_dilog_expansion_probe` | no |

**Listed is necessary, not sufficient — do not read a "yes" as fixed.** This
bean already establishes that manifest absence is not sufficient to cause the
drop (`q0_anchor_consistency_audit` is absent and retains its stamp). So the
three yes rows have had *a candidate cause* removed; whether the stamp actually
survives regeneration is a re-measurement, not an inference. That check comes
free after the rebase — the sweep records `q0Anchor (removed)` directly.

The two "no" rows are the `flavor_split_alpha_*` pair, and they may fall under the
sibling's own follow-up `qou-5t8y` (650 suffixed producers the manifest cannot
see) — worth their checking against that scope rather than my guessing at it.

Note `flavor_split_alpha_bond_dilog_probe` is **doubly implicated**: it is also
one of `qou-6q7q`'s three paths that drifted on main. Its verdict here was
measured against a pre-migration version *and* it is unlisted. That one needs
re-measuring before any claim is made about it in either bean.

## OBSERVED ON MAIN — this is no longer a predicted hazard

The rebase onto `main` (+206) dropped the in-scope population **56 → 48**.
Nine witnesses left the muon-anchored set, and they split into two causes that
must not be conflated:

**Five re-pinned to proton** — `q0Anchor: "proton"`,
`q0Value: 1.109978582751380807591669`. Legitimate migration, the authorised
`qou-1c4y` sweep doing its job. Not a defect.

**Four lost the stamp entirely** — `q0Anchor` and `q0Value` **absent**:

| witness | my sweep predicted the drop |
|---|---|
| `probes/flavor-split-alpha-bond-dilog.witness.json` | yes |
| `probes/flavor-split-alpha-dilog-expansion.witness.json` | yes |
| `signed-crossing-feasibility.witness.json` | yes |
| `probes/binding-qgaussian-ell1-ceiling-measurement.witness.json` | no not predicted |

Three of the four are producers this sweep independently flagged as
anchor-stamp droppers — and they are three of the **four that #5550 did not
cover**. The prediction and the observation were made from different directions
and agree.

**The fourth was not predicted**, and that matters: it is one of `qou-6q7q`'s
main-drift paths (migrated by `bc96793e5d`), so the version that lost its stamp
is not the version I measured. Do not count it as a confirmation; count it as a
second, separate route to the same end state.

## Why this is the consequential half

`q0_anchor_consistency_audit` classifies a stamp-less witness as
**`Q0_ANCHOR_MISSING` — explicitly "not a failure"** (line 29). So a witness
that was a `Q0_FLIP` becomes a non-failure by losing the field the audit keys
on. Nothing was fixed. The audit's denominator shrank.

That is the mechanism this bean described, now with an instance: **the count of
flips can fall without a single anchor being corrected.** It happened on `main`
while this sweep was measuring it.

## What follows

- A drop in `Q0_FLIP` is **not** evidence of progress on its own. Any report of
  that count needs the `Q0_ANCHOR_MISSING` count beside it, or it cannot be
  read.
- Before #5500 regenerates its 53, the stamp-emission has to be fixed at the
  producer/generator, or the tranche converts flips into missing-anchors at
  scale — the audit goes green and the corpus is *less* checkable than before.
- The 4 above are already in that state and need the stamp restored, not merely
  re-pinned.

## A FOURTH mechanism — and the one no audit can see

Found by re-running `parabolic_cylinder_channel_mixing_probe` for `qou-n7ue`.
Its regenerated witness moved `constants.q_0` from the muon value to the
proton value (`ppb_vs_canonical` `-1.79e-08` → `-11.537117889980326`), while
its top-level stamp still reads `q0Anchor: muon`.

The chain:

1. The probe **copies** `constants.q_0` verbatim out of its input witness,
   `binding-bar-even-odd-probe.witness.json`.
2. `main` re-pinned **that input** to proton.
3. The probe is classified **`ideal_muon`** in `q0_anchor_manifest.json`, so
   `q_parameter` stamps its witness `muon`.

Result: **stamped muon, computed at proton.** The q-deformed column is
`gamma_q_gt1(x, q0)` evaluated on the copied proton constant, so this is the
arithmetic, not a label.

**Why this is worse than the drop this bean already tracks.** The anchor-stamp
drop at least removes the witness from the audited set, where a shrinking
denominator is visible to anyone who looks. This one leaves a *fully
consistent-looking* muon witness: `q0Anchor: muon`, `q0Value: <muon>`, both
present, both agreeing. `q0_anchor_consistency_audit` checks the stamp against
itself and reports `Q0_OK`. Nothing in the pipeline compares the stamp against
the constants the producer actually consumed.

So the four mechanisms by which the muon-anchored population moves under
regeneration are now:

| # | mechanism | visible to the audit? |
|---|---|---|
| 1 | deliberate re-pin to proton (`qou-1c4y`) | yes — reclassified |
| 2 | anchor-stamp **dropped** entirely | yes — becomes `Q0_ANCHOR_MISSING` |
| 3 | producer moved on main, verdict stale | yes — via drift measurement |
| 4 | **upstream input re-pinned, consumer keeps its muon stamp** | **NO** |

Not fixed here — the fix is either to reclassify the consumer or to stop
copying a constant the producer does not own, and that is a scoping call. But
it sharpens the #5500 recommendation: an audit that reads `Q0_OK` does not
establish that a witness was computed at the anchor it claims.
