---
# qou-ircb
title: Producers that INHERIT a q0 from another witness are stamped from a manifest that cannot know it
status: todo
type: task
created_at: 2026-08-24T13:34:53Z
updated_at: 2026-08-24T13:34:53Z
---

## What it is

A producer reads a q0 out of another producer's `*.witness.json` and computes
with it. Its own witness is then stamped by `witness.py` from its stem in
`q0_anchor_manifest.json`. Those two facts are independent: the manifest says
what the producer is *supposed* to be pinned at, the upstream witness carries
whatever it *is* pinned at today. Re-pin the upstream and the producer silently
follows while its stamp does not move.

Worked instance, and the one this was found on:
`parabolic_cylinder_channel_mixing_probe` — listed `ideal_muon`, so stamped
`q0Anchor: "muon"`, while `constants.q_0` in its witness is the **proton** pin,
copied verbatim from `binding-bar-even-odd-probe.witness.json` which main
re-pinned. The value reaches the arithmetic (`gamma_q_gt1(x, q0)`, line 92,
read at line 67); there is no `add_parameter` in the file, so this is **not**
the stamp-only class the aK retraction (`83de3b847c`) covers.

## Five gates, none of which can see it — measured, not reasoned

| gate | its question | verdict |
|---|---|---|
| `q0_anchor_consistency_audit` | stamp vs itself | `Q0_OK` |
| `anchor_flip_straddle_audit` (BLOCKING, `fa2794159b`) | does output move under `QOU_Q0_ANCHOR`? a q read from a FILE does not | **clean** |
| `q0_producer_pin_classifier` | accessors / imports / muon artifacts / 50-digit literals | `('none', [])` |
| `tnjb_stale_stamp_migrate` | producers the classifier resolves *proton* | `none` ⇒ excluded |
| `q0_anchor_contradiction_triage` | witnesses declaring **proton** | declares muon ⇒ out of scope |

None is wrong about its own question. The gap is that **nothing compares the
stamp against the numbers in the same file.**

## The control that settles intent

`defect_weighted_zero_point_probe` and `zero_point_channel_energy_probe` read
the **same** upstream witness by the **same** expression and are listed
`physical_proton`. Three readers of one file, two proton and one muon, is one
row disagreeing with its own input — not a layer-policy choice.

## Fixed here, and the fix moved no number

Manifest → `physical_proton`, witness regenerated **in the same commit**
(AGENTS.md constraint 4: do not split the change). The regeneration moved
`q0Anchor`, `q0Value` and the environment record and **nothing else** — the
`qou-bdkx` (b) signature: payload right, declaration wrong.

## Detector

[`computations/audits/inherited_q0_pin_audit.py`](computations/audits/inherited_q0_pin_audit.py).
Full tree after the fix: **MISLABEL=0, agrees=3, undetermined=17**.

**Its own blind spot is how it was found.** A first pass keyed on *literal*
subscript keys and missed the very producer this bean is about, which spells
the key as a module constant (`Q0_KEY = "q_0"; src["constants"][Q0_KEY]`).
Module-level `str` constants are resolved now; a key built at runtime or
reached through a helper still escapes. `--selftest` therefore pins the
**key-resolution reach**, not the (now-fixed) MISLABEL verdict — a gate that
goes red when the bug it names is fixed is not a gate.

## What is left

17 `undetermined`. Two causes, and they need different work:

1. the upstream filename does not resolve statically (`upstream=?`) — the path
   is assembled rather than named;
2. the producer is **ABSENT** from the manifest, so there is no declared class
   to compare the inherited pin against.

(2) is the more interesting half: an absent producer inherits a pin with
*nothing at all* asserting what it should be.
